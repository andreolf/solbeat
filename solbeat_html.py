"""HTML dashboard renderer for Solbeat.

Renders the collected snapshot into a single self-contained dark-theme HTML
file: server-side SVG charts (no chart libraries), status-page-style anomaly
strips, provenance badges on every tile, and a small vanilla-JS layer for the
live slot ticker / REV clock / data-age counter. Stdlib only.
"""

import html
import json
from pathlib import Path

BASE_URL = "https://andreolf.github.io/solbeat/"
SITE_DESC = ("Live, auto-updating Solana network dashboard: TPS, slot time, "
             "validators, Real Economic Value (REV), TVL, stablecoins, DEX "
             "volume, tokenized equities, Alpenglow & SIMD-525 tracking, "
             "anomaly detection. Open-source, zero API keys, Python stdlib only.")

# Dark palette (validated: page #0d0d0d, surface #1a1a19, series blue #3987e5,
# reserved status colors; text tokens carry all labels).
STATUS_COLORS = {"ok": "#0ca30c", "good": "#0ca30c", "warning": "#fab219",
                 "serious": "#ec835a", "critical": "#d03b3b", "na": "#383835"}
STATUS_ICONS = {"ok": "●", "good": "●", "warning": "▲", "serious": "▲",
                "critical": "■", "na": "·"}
BLUE = "#3987e5"

# Friendly display names + endpoint domains for the provenance panel.
SOURCE_LABELS = {
    "solana_rpc": ("Solana RPC · network core", "api.mainnet-beta.solana.com"),
    "solana_rpc_validators": ("Solana RPC · vote accounts", "api.mainnet-beta.solana.com"),
    "solana_rpc_whales": ("Solana RPC · exchange wallets", "api.mainnet-beta.solana.com"),
    "solana_rpc_programs": ("Solana RPC · program pulse", "api.mainnet-beta.solana.com"),
    "coingecko": ("CoinGecko · market data", "api.coingecko.com"),
    "defillama_tvl": ("DeFiLlama · chain TVL", "api.llama.fi"),
    "defillama_dex": ("DeFiLlama · DEX volume", "api.llama.fi"),
    "defillama_fees": ("DeFiLlama · chain fees", "api.llama.fi"),
    "defillama_stablecoins": ("DeFiLlama · stablecoins", "stablecoins.llama.fi"),
    "defillama_xstocks": ("DeFiLlama · xStocks", "api.llama.fi"),
    "jito_kobe": ("Jito Kobe · MEV tips", "kobe.mainnet.jito.network"),
    "stakewiz": ("Stakewiz · validator meta", "api.stakewiz.com"),
    "github": ("GitHub · Agave & SIMDs", "api.github.com"),
    "solana_com_news": ("solana.com · news RSS", "solana.com"),
    "solana_status_page": ("Solana status page", "status.solana.com"),
    "dune": ("Dune Analytics (optional)", "api.dune.com"),
}

CHANGELOG = [
    ("2026-08-31", "v1.3", "Real live mode: browser polls keyless RPC (slot re-sync, live TPS, ticking tx counter), `verify` self-audit command, SEO + llms.txt for agents"),
    ("2026-08-31", "v1.2", "Sources panel redesign, footer with changelog & resources, hero layout fix"),
    ("2026-08-31", "v1.1", "solana.com news feed, on-chain clock (getSlot/getBlockTime), optional Dune extractor, configurable refresh interval, mobile polish"),
    ("2026-08-31", "v1.0", "Initial release — 14 keyless sources, computed REV, correlation-based anomaly incidents, HTML/Markdown/JSON outputs, GitHub Actions autopilot"),
]


def esc(s):
    return html.escape(str(s), quote=True)


def fmt_usd(v, digits=1):
    if v is None:
        return "n/a"
    for cut, suffix in [(1e12, "T"), (1e9, "B"), (1e6, "M"), (1e3, "K")]:
        if abs(v) >= cut:
            return f"${v / cut:.{digits}f}{suffix}"
    return f"${v:,.0f}"


def fmt_num(v, digits=0):
    if v is None:
        return "n/a"
    for cut, suffix in [(1e9, "B"), (1e6, "M"), (1e3, "K")]:
        if abs(v) >= cut:
            return f"{v / cut:.1f}{suffix}"
    return f"{v:,.{digits}f}"


# ---------------------------------------------------------------- SVG charts

def sparkline(series, w=150, h=40, color=BLUE):
    """Tiny single-series line with area wash and ringed end-dot."""
    pts = [v for v in series if v is not None]
    if len(pts) < 2:
        return ""
    lo, hi = min(pts), max(pts)
    span = (hi - lo) or 1
    pad = 5
    step = (w - 2 * pad) / (len(pts) - 1)
    coords = [(pad + i * step, h - pad - (v - lo) / span * (h - 2 * pad))
              for i, v in enumerate(pts)]
    line = " ".join(f"{x:.1f},{y:.1f}" for x, y in coords)
    area = f"{pad},{h - pad} " + line + f" {coords[-1][0]:.1f},{h - pad}"
    ex, ey = coords[-1]
    return (
        f'<svg class="spark" width="{w}" height="{h}" viewBox="0 0 {w} {h}" '
        f'aria-hidden="true">'
        f'<polygon points="{area}" fill="{color}" opacity="0.1"/>'
        f'<polyline points="{line}" fill="none" stroke="{color}" '
        f'stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>'
        f'<circle cx="{ex:.1f}" cy="{ey:.1f}" r="4" fill="{color}" '
        f'stroke="#1a1a19" stroke-width="2"/></svg>'
    )


def big_chart(series, w=1120, h=150, color=BLUE, label=""):
    """Main line chart (TPS over ~12h) with hairline grid + endpoint label."""
    pts = [v for v in series if v is not None]
    if len(pts) < 2:
        return ""
    lo, hi = min(pts), max(pts)
    span = (hi - lo) or 1
    padl, padr, padt, padb = 8, 90, 12, 8
    step = (w - padl - padr) / (len(pts) - 1)
    coords = [(padl + i * step,
               h - padb - (v - lo) / span * (h - padt - padb))
              for i, v in enumerate(pts)]
    line = " ".join(f"{x:.1f},{y:.1f}" for x, y in coords)
    area = f"{padl},{h - padb} " + line + f" {coords[-1][0]:.1f},{h - padb}"
    grid = "".join(
        f'<line x1="{padl}" y1="{y}" x2="{w - padr}" y2="{y}" '
        f'stroke="#2c2c2a" stroke-width="1"/>'
        for y in (padt, (padt + h - padb) / 2, h - padb))
    ex, ey = coords[-1]
    ey_label = min(max(ey, padt + 10), h - padb - 2)
    return (
        f'<svg id="tpschart" width="100%" viewBox="0 0 {w} {h}" '
        f'preserveAspectRatio="none" role="img" aria-label="{esc(label)}">'
        f'{grid}'
        f'<polygon points="{area}" fill="{color}" opacity="0.08"/>'
        f'<polyline points="{line}" fill="none" stroke="{color}" '
        f'stroke-width="2" stroke-linejoin="round"/>'
        f'<circle cx="{ex:.1f}" cy="{ey:.1f}" r="4" fill="{color}" '
        f'stroke="#1a1a19" stroke-width="2"/>'
        f'<text x="{ex + 10:.1f}" y="{ey_label + 4:.1f}" fill="#ffffff" '
        f'font-size="13" font-weight="600">{pts[-1]:,.0f}</text>'
        f'<text x="{ex + 10:.1f}" y="{ey_label + 20:.1f}" fill="#898781" '
        f'font-size="11">now</text>'
        f'</svg>'
    )


def strip(levels, titles=None, label=""):
    """Status-page-style tick strip: one tick per interval, colored by level."""
    ticks = []
    titles = titles or [""] * len(levels)
    for lv, t in zip(levels, titles):
        c = STATUS_COLORS.get(lv, STATUS_COLORS["na"])
        ticks.append(f'<i style="background:{c}" title="{esc(t)}"></i>')
    return (f'<div class="strip" role="img" aria-label="{esc(label)}">'
            + "".join(ticks) + "</div>")


def epoch_ring(pct, size=92):
    r = 38
    c = 2 * 3.14159 * r
    filled = c * pct / 100
    return (
        f'<svg width="{size}" height="{size}" viewBox="0 0 {size} {size}" '
        f'role="img" aria-label="Epoch progress {pct}%">'
        f'<circle cx="{size/2}" cy="{size/2}" r="{r}" fill="none" '
        f'stroke="#2c2c2a" stroke-width="7"/>'
        f'<circle cx="{size/2}" cy="{size/2}" r="{r}" fill="none" '
        f'stroke="{BLUE}" stroke-width="7" stroke-linecap="round" '
        f'stroke-dasharray="{filled:.1f} {c:.1f}" '
        f'transform="rotate(-90 {size/2} {size/2})"/>'
        f'<text x="50%" y="53%" text-anchor="middle" dominant-baseline="middle" '
        f'fill="#ffffff" font-size="19" font-weight="650">{pct:.0f}%</text>'
        f'</svg>'
    )


LOGO_SVG = ('<svg class="logomark" width="30" height="20" viewBox="0 0 34 20" '
            'aria-hidden="true"><polyline points="0,11 9,11 12,5 16,17 20,3 23,11 34,11" '
            f'fill="none" stroke="{BLUE}" stroke-width="2.4" stroke-linecap="round" '
            'stroke-linejoin="round"/></svg>')

FAVICON = ('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" '
           'viewBox="0 0 32 32"><rect width="32" height="32" rx="7" '
           'fill="%230d0d0d"/><polyline points="4,17 11,17 13,10 17,23 20,7 22,17 28,17" '
           'fill="none" stroke="%233987e5" stroke-width="2.6" '
           'stroke-linecap="round" stroke-linejoin="round"/></svg>')


def world_map(geo, w=1120, h=430):
    """Validator world map: equirectangular dot plot from Stakewiz geodata."""
    if not geo:
        return ""
    lat_top, lat_bot = 74, -58
    def xy(lat, lon):
        x = (lon + 180) / 360 * w
        y = (lat_top - lat) / (lat_top - lat_bot) * h
        return x, y
    # faint graticule for spatial structure
    grid = ""
    for lon in range(-150, 181, 30):
        x, _ = xy(0, lon)
        grid += (f'<line x1="{x:.0f}" y1="0" x2="{x:.0f}" y2="{h}" '
                 'stroke="#2c2c2a" stroke-width="1"/>')
    for lat in range(-30, 61, 30):
        _, y = xy(lat, 0)
        wgt = 1.5 if lat == 0 else 1
        grid += (f'<line x1="0" y1="{y:.0f}" x2="{w}" y2="{y:.0f}" '
                 f'stroke="#2c2c2a" stroke-width="{wgt}"/>')
    max_stake = geo[0]["stake"] or 1
    dots = ""
    # draw small dots first so heavyweights sit on top
    for g in reversed(geo):
        x, y = xy(g["lat"], g["lon"])
        r = max(2.1, 9 * (g["stake"] / max_stake) ** 0.5)
        label = esc(f'{g["name"] or "validator"} — {g["stake"]:,} SOL — {g["loc"]}')
        big = g["stake"] > max_stake / 8
        dots += (f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r:.1f}" fill="{BLUE}" '
                 f'opacity="{0.95 if big else 0.7}"'
                 + (f' stroke="#1a1a19" stroke-width="1.5"' if big else "")
                 + f'><title>{label}</title></circle>')
    return (f'<svg width="100%" viewBox="0 0 {w} {h}" role="img" '
            f'aria-label="World map of Solana validators, dot size by stake">'
            f'{grid}{dots}</svg>')


def meter(pct, color=BLUE):
    pct = max(0, min(100, pct or 0))
    return (f'<div class="meter"><div class="meter-fill" '
            f'style="width:{pct:.1f}%;background:{color}"></div></div>')


# ------------------------------------------------------------ HTML sections

def provenance_badge(snap, source, label):
    s = (snap.get("sources") or {}).get(source)
    if not s:
        return ""
    dot = STATUS_COLORS["good"] if s["ok"] else STATUS_COLORS["critical"]
    tip = (f"{label} · fetched {s['fetched_at']} · {s['latency_ms']}ms"
           + ("" if s["ok"] else f" · FAILED: {s.get('error', '')[:80]}"))
    return (f'<span class="prov" title="{esc(tip)}">'
            f'<i style="background:{dot}"></i>{esc(label)}</span>')


def tile(label, value, sub="", spark="", badge="", value_id="", delta=None):
    delta_html = ""
    if delta is not None:
        good = delta >= 0
        col = "#0ca30c" if good else "#e66767"
        delta_html = (f'<span class="delta" style="color:{col}">'
                      f'{"+" if good else ""}{delta:.1f}% / 24h</span>')
    idattr = f' id="{value_id}"' if value_id else ""
    return f"""<div class="tile">
  <div class="tile-head"><span class="tile-label">{esc(label)}</span>{badge}</div>
  <div class="tile-value"{idattr}>{value}</div>
  <div class="tile-sub">{delta_html}{sub}</div>
  {spark}
</div>"""


def signal_row(level, text, klass=""):
    c = STATUS_COLORS.get(level, STATUS_COLORS["na"])
    icon = STATUS_ICONS.get(level, "·")
    tag = f'<span class="sig-class">{esc(klass)}</span>' if klass else ""
    return (f'<div class="signal"><span class="sig-icon" style="color:{c}">'
            f'{icon}</span><span class="sig-level" style="color:{c}">'
            f'{esc(level.upper())}</span>{tag}<span>{esc(text)}</span></div>')


def daily_levels(series, warn_pct, serious_pct):
    """Color a daily series by day-over-day % change for the status strips."""
    levels, titles = [], []
    for i in range(1, len(series)):
        prev, cur = series[i - 1], series[i]
        if not prev or cur is None:
            levels.append("na")
            titles.append("no data")
            continue
        ch = 100 * (cur - prev) / prev
        lv = ("serious" if abs(ch) >= serious_pct
              else "warning" if abs(ch) >= warn_pct else "ok")
        levels.append(lv)
        titles.append(f"{ch:+.1f}% day-over-day")
    return levels, titles


def _map_block(snap):
    sw = snap.get("stakewiz") or {}
    geo = sw.get("geo") or []
    if not geo:
        return ""
    crows = ""
    for c in sw.get("countries") or []:
        crows += f"""<div class="prow">
  <span class="prow-label">{esc(c['country'])}</span>
  <div class="prow-track"><div class="prow-bar" style="width:{min(100, c['stake_pct'] * 2.2):.0f}%"></div></div>
  <span class="prow-val">{c['stake_pct']}%</span>
</div>"""
    badge = provenance_badge(snap, "stakewiz", "Stakewiz · geodata")
    return f"""<div class="mapwrap">
  <div class="tile-label" style="margin:20px 0 6px">VALIDATOR MAP — {len(geo):,} nodes, dot size = stake {badge}</div>
  {world_map(geo)}
  <div class="tile-label" style="margin:14px 0 4px">STAKE BY COUNTRY</div>
  {crows}
</div>"""


def _news_block(snap):
    items = (snap.get("news") or {}).get("items") or []
    if not items:
        return ""
    rows = "".join(
        f'<div class="newsrow"><a href="{esc(it["link"])}" target="_blank" '
        f'rel="noopener">{esc(it["title"])}</a>'
        f'<span class="muted small"> — {esc(it["published"][:16])}</span></div>'
        for it in items[:5])
    badge = provenance_badge(snap, "solana_com_news", "solana.com RSS")
    return (f'<div class="newsblock"><div class="tile-label" style="margin:16px 0 8px">'
            f'LATEST ECOSYSTEM NEWS {badge}</div>{rows}</div>')


# ------------------------------------------------------------------ render

def render_html(snap):
    net = snap.get("network") or {}
    val = snap.get("validators") or {}
    mkt = snap.get("market") or {}
    der = snap.get("derived") or {}
    dex = snap.get("dex") or {}
    tvl = snap.get("tvl") or {}
    stb = snap.get("stablecoins") or {}
    xst = snap.get("xstocks") or {}
    fee = snap.get("fees") or {}
    sw = snap.get("stakewiz") or {}
    gh = snap.get("github") or {}
    stp = snap.get("status_page") or {}
    anom = snap.get("anomalies") or {}

    B = lambda src, lbl: provenance_badge(snap, src, lbl)  # noqa: E731

    # ---- header health badge
    healthy = net.get("health") == "ok" and (stp.get("unresolved_incidents") or 0) == 0
    hcol = STATUS_COLORS["good" if healthy else "warning"]
    htxt = "OPERATIONAL" if healthy else "DEGRADED"

    # ---- hero strip
    slot_ms = net.get("slot_time_ms")
    simd_note = ("SIMD-525 350ms step live"
                 if der.get("simd525_step_active") else "target 400ms")
    perf = net.get("perf_series") or []
    tps_series = [p["tps"] for p in perf if p.get("tps") is not None]

    # slot-performance strip: bucket ~12h of samples into ticks by slot time
    bucket = max(1, len(perf) // 96)
    slot_levels, slot_titles = [], []
    for i in range(0, len(perf), bucket):
        chunk = [p["slot_ms"] for p in perf[i:i + bucket] if p.get("slot_ms")]
        if not chunk:
            continue
        avg = sum(chunk) / len(chunk)
        lv = ("serious" if avg >= 700 else "warning" if avg >= 500 else "ok")
        slot_levels.append(lv)
        slot_titles.append(f"{avg:.0f}ms avg slot time")

    hero = f"""
<section class="card">
  <div class="hero">
    <div class="hero-left">
      <div class="hero-label">CURRENT SLOT {B('solana_rpc', 'RPC')}
        <span class="livedot" id="livedot" title="green = slot confirmed live from RPC in your browser (PublicNode); dim = extrapolated from measured slot time">LIVE</span></div>
      <div class="hero-slot" id="slot">{net.get('slot', 0):,}</div>
      <div class="hero-under"><span id="txcount">{net.get('tx_count_total', 0):,}</span>
        lifetime txs · block height {net.get('block_height', 0):,} ·
        node v{esc(net.get('node_version', '?'))}
        {f"· chain clock {esc(net['chain_time'])}" if net.get('chain_time') else ""}</div>
    </div>
    <div class="hero-mid">
      <div class="hero-stats">
        <div><span class="hs-label">TPS</span><span class="hs-value" id="v-tps">{fmt_num(net.get('tps'))}</span></div>
        <div><span class="hs-label">non-vote TPS</span><span class="hs-value" id="v-nvtps">{fmt_num(net.get('nonvote_tps'))}</span></div>
        <div><span class="hs-label">slot time</span><span class="hs-value" id="v-slotms">{f"{slot_ms:.0f}ms" if slot_ms else "n/a"}</span>
          <span class="hs-note">{esc(simd_note)}</span></div>
        <div><span class="hs-label">est. daily txs</span><span class="hs-value">{fmt_num(net.get('est_daily_txs'))}</span></div>
      </div>
    </div>
    <div class="hero-right">
      {epoch_ring(net.get('epoch_progress_pct') or 0)}
      <div class="hero-epoch">epoch {net.get('epoch', '?')}<br>
        <span class="muted">~{der.get('epoch_eta_hours', '?')}h remaining</span></div>
    </div>
  </div>
  <div class="herostrip">
    <div class="hero-under" style="margin-bottom:2px">last 12h slot performance</div>
    {strip(slot_levels, slot_titles, "12h slot performance")}
  </div>
</section>
<section class="card chartcard">
  <div class="section-head"><h2>Transactions per second — last 12h</h2>{B('solana_rpc', 'RPC · getRecentPerformanceSamples')}</div>
  {big_chart(tps_series, label='TPS over the last 12 hours')}
</section>"""

    # ---- economic tiles
    rev_sub = (f'fees {fmt_usd(fee.get("chain_fees24h_usd"))} + Jito tips '
               f'{fmt_usd(der.get("jito_tips24h_usd"))} · '
               f'{fmt_usd(der.get("rev_per_min_usd"), 0)}/min'
               f'<br><span id="revclock"></span>')
    tiles = "\n".join([
        tile("SOL price", f"${mkt.get('sol_price_usd', 0):,.2f}",
             sub=f"mcap {fmt_usd(mkt.get('sol_mcap_usd'))}",
             spark=sparkline(mkt.get("price_series_30d") or []),
             badge=B("coingecko", "CoinGecko"),
             delta=mkt.get("sol_change24h_pct")),
        tile("Real Economic Value (24h)", fmt_usd(der.get("rev24h_usd")),
             sub=rev_sub,
             spark=sparkline(fee.get("fees_series") or []),
             badge='<span class="prov" title="Computed: DeFiLlama chain fees + '
                   'Jito Kobe MEV tips — Blockworks REV methodology">'
                   '<i style="background:#3987e5"></i>computed</span>'),
        tile("Chain TVL", fmt_usd(tvl.get("tvl_usd")),
             sub="DeFi total value locked",
             spark=sparkline(tvl.get("tvl_series") or []),
             badge=B("defillama_tvl", "DeFiLlama")),
        tile("Stablecoin supply", fmt_usd(stb.get("stablecoin_supply_usd")),
             sub="circulating on Solana",
             spark=sparkline(stb.get("stablecoin_series") or []),
             badge=B("defillama_stablecoins", "DeFiLlama")),
        tile("DEX volume (24h)", fmt_usd(dex.get("dex_vol24h_usd")),
             sub="top: " + ", ".join(p["name"] for p in (dex.get("dex_top_protocols") or [])[:3]),
             spark=sparkline(dex.get("dex_series") or []),
             badge=B("defillama_dex", "DeFiLlama"),
             delta=dex.get("dex_change1d_pct")),
        tile("Tokenized equities (xStocks)", fmt_usd(xst.get("xstocks_tvl_usd")),
             sub="RWA equities TVL on Solana",
             spark=sparkline(xst.get("xstocks_series") or []),
             badge=B("defillama_xstocks", "DeFiLlama")),
        tile("Circulating supply", f"{fmt_num(net.get('supply_circulating_sol'))} SOL",
             sub=f"inflation {net.get('inflation_total_pct', '?')}% · "
                 f"total {fmt_num(net.get('supply_total_sol'))} SOL",
             badge=B("solana_rpc", "RPC")),
        tile("Transaction fees",
             (f"${der['avg_fee_per_tx_usd']:.4f}"
              if der.get("avg_fee_per_tx_usd") else "n/a"),
             sub=f"avg fee per user tx (24h) · median priority fee "
                 f"{fmt_num(net.get('priority_fee_median'))} µ-lam/CU"
                 + (" (uncongested)" if not net.get("priority_fee_median") else "")
                 + f" · {net.get('priority_fee_nonzero_share_pct', 0)}% of recent "
                 f"slots paid priority",
             badge=B("solana_rpc", "RPC")),
    ] + ([
        tile("Daily active addresses",
             fmt_num((snap.get("dune") or {}).get("daily_active_addresses")),
             sub=f"Dune query {esc((snap.get('dune') or {}).get('query_id', ''))}",
             badge=B("dune", "Dune")),
    ] if (snap.get("dune") or {}).get("daily_active_addresses") else []))

    # ---- signals
    findings = anom.get("findings") or []
    incidents = anom.get("incidents") or []
    if anom.get("all_clear"):
        signals_html = signal_row("good", "All clear — no anomalies detected "
                                  "across monitored metrics this cycle.")
    else:
        signals_html = "\n".join(
            [signal_row(i["level"], i["text"], i["class"]) for i in incidents]
            + [signal_row(f["level"], f["text"]) for f in findings])

    strips_html = ""
    strip_defs = [
        ("SOL price", mkt.get("price_series_30d") or [], 5, 10),
        ("Chain TVL", tvl.get("tvl_series") or [], 5, 10),
        ("Stablecoins", stb.get("stablecoin_series") or [], 2, 5),
        ("DEX volume", dex.get("dex_series") or [], 25, 50),
    ]
    for name, series, w, s in strip_defs:
        if len(series) > 5:
            lv, ti = daily_levels(series[-61:], w, s)
            strips_html += (f'<div class="striprow"><span class="strip-label">'
                            f'{esc(name)}</span>{strip(lv, ti, name)}</div>')
    hist = snap.get("history") or []
    if len(hist) >= 3:
        lv = [h.get("anomaly_level", "ok") for h in hist[-96:]]
        ti = [f"{h.get('ts', '')}: {h.get('anomaly_level', 'ok')}" for h in hist[-96:]]
        strips_html += (f'<div class="striprow"><span class="strip-label">'
                        f'run history</span>{strip(lv, ti, "run history")}</div>')

    signals = f"""
<section class="card">
  <div class="section-head"><h2>Signals — anomaly detection</h2>
    <span class="muted small">per-metric z-scores + multi-source correlation</span></div>
  {signals_html}
  <div class="strips">{strips_html}</div>
  <div class="muted small striplegend">daily ticks, last ~60d ·
    <span style="color:{STATUS_COLORS['ok']}">●</span> normal ·
    <span style="color:{STATUS_COLORS['warning']}">▲</span> notable move ·
    <span style="color:{STATUS_COLORS['serious']}">▲</span> large move</div>
</section>"""

    # ---- validators (named via Stakewiz where known)
    names = sw.get("names") or {}
    vrows = ""
    for i, v in enumerate(val.get("top_validators") or [], 1):
        bar_w = min(100, v["stake_pct"] * 30)
        who = names.get(v["vote_pubkey"])
        who_html = (f'{esc(who)} <span class="mono muted small">{esc(v["vote_pubkey"][:8])}…</span>'
                    if who else f'<span class="mono">{esc(v["vote_pubkey"][:16])}…</span>')
        vrows += f"""<tr>
  <td class="muted">{i}</td>
  <td>{who_html}</td>
  <td class="num">{v['stake_sol']:,}</td>
  <td class="num">{v['stake_pct']}%</td>
  <td class="num">{v['commission_pct']}%</td>
  <td><div class="stakebar"><div style="width:{bar_w:.0f}%"></div></div></td>
</tr>"""

    bls_pct = sw.get("bls_stake_pct")
    validators = f"""
<section class="card">
  <div class="section-head"><h2>Validators</h2>{B('solana_rpc_validators', 'RPC · getVoteAccounts')}</div>
  <div class="vstats">
    <div><span class="hs-value">{val.get('active_count', '?')}</span><span class="hs-label">active</span></div>
    <div><span class="hs-value" style="color:{STATUS_COLORS['serious'] if (val.get('delinquent_stake_pct') or 0) > 3 else '#ffffff'}">{val.get('delinquent_count', '?')}</span><span class="hs-label">delinquent ({val.get('delinquent_stake_pct', '?')}% of stake)</span></div>
    <div><span class="hs-value">{val.get('nakamoto_coefficient', '?')}</span><span class="hs-label">Nakamoto coefficient</span></div>
    <div><span class="hs-value">{val.get('top10_stake_pct', '?')}%</span><span class="hs-label">top-10 stake share</span></div>
    <div><span class="hs-value">{val.get('median_commission_pct', '?')}%</span><span class="hs-label">median commission (avg {val.get('avg_commission_pct', '?')}%)</span></div>
    <div><span class="hs-value">{fmt_num(val.get('total_stake_sol'))}</span><span class="hs-label">SOL staked</span></div>
  </div>
  <table class="vtable">
    <thead><tr><th>#</th><th>validator</th><th class="num">stake (SOL)</th>
      <th class="num">share</th><th class="num">commission</th><th></th></tr></thead>
    <tbody>{vrows}</tbody>
  </table>
  {_map_block(snap)}
  {"" if bls_pct is None else f'''
  <div class="blsrow">
    <div class="tile-label">ALPENGLOW READINESS — BLS keys registered {B('stakewiz', 'Stakewiz')}</div>
    {meter(bls_pct)}
    <div class="muted small">{sw.get('bls_registered_count', '?')} validators holding
      {bls_pct}% of stake have registered BLS keys for the new consensus</div>
  </div>'''}
</section>"""

    # ---- ecosystem pulse
    pulse = [p for p in (snap.get("program_pulse") or []) if p.get("tx_per_min")]
    maxrate = max((p["tx_per_min"] for p in pulse), default=1)
    prows = ""
    for p in sorted(pulse, key=lambda x: -x["tx_per_min"]):
        w = max(2, 100 * (p["tx_per_min"] / maxrate) ** 0.5)  # sqrt scale, labeled
        prows += f"""<div class="prow">
  <span class="prow-label">{esc(p['program'])}</span>
  <div class="prow-track"><div class="prow-bar" style="width:{w:.0f}%"></div></div>
  <span class="prow-val">{(f"{p['tx_per_min']:.1f}" if p['tx_per_min'] < 10 else fmt_num(p['tx_per_min']))} tx/min</span>
</div>"""
    wrows = "".join(
        f'<tr><td>{esc(w["label"])}</td><td class="mono small">{esc(w["address"][:20])}…</td>'
        f'<td class="num">{fmt_num(w["balance_sol"])} SOL</td></tr>'
        for w in (snap.get("whales") or []))
    pulse_html = f"""
<section class="twocol">
<div class="card">
  <div class="section-head"><h2>Program activity pulse</h2>{B('solana_rpc_programs', 'RPC · getSignaturesForAddress')}</div>
  {prows or '<div class="muted">no data this cycle</div>'}
  <div class="muted small">sampled from each program's 25 most recent signatures · sqrt scale, values labeled</div>
</div>
<div class="card">
  <div class="section-head"><h2>Exchange reserves</h2>{B('solana_rpc_whales', 'RPC · getBalance')}</div>
  <table class="vtable"><thead><tr><th>wallet</th><th>address</th><th class="num">balance</th></tr></thead>
  <tbody>{wrows}</tbody></table>
  <div class="muted small">community-attributed exchange hot wallets, polled live</div>
</div>
</section>"""

    # ---- almanac: commentary + upgrades
    simd_live = der.get("simd525_step_active")
    upgrades = f"""
<section class="card">
  <div class="section-head"><h2>The Almanac — upgrades &amp; ecosystem watch</h2>
    {B('github', 'GitHub')} {B('solana_status_page', 'status.solana.com')}</div>
  <p class="commentary">{esc(snap.get('commentary', ''))}</p>
  <div class="upgrid">
    <div class="upcard">
      <div class="up-name">SIMD-0525 · slot-time reduction</div>
      <div class="up-status">{'<span class="live-dot"></span>STEP 1 ACTIVE — measured ' + f"{slot_ms:.0f}ms" if simd_live and slot_ms else 'tracking'}</div>
      <div class="muted small">400→200ms in four feature-gated steps. Our own RPC
        measurement of ~{f"{slot_ms:.0f}" if slot_ms else "?"}ms slot time is live,
        on-chain proof the 350ms step is running.
        Proposal state: {esc(gh.get('simd525_state') or 'n/a')}.</div>
    </div>
    <div class="upcard">
      <div class="up-name">Alpenglow · SIMD-0236</div>
      <div class="up-status">{f"{bls_pct}% of stake BLS-ready" if bls_pct is not None else "pending"}</div>
      <div class="muted small">Consensus overhaul (Votor + Rotor): ~100–150ms finality,
        replacing TowerBFT. Approved by 98% of stake; activation via Agave v4.3,
        targeted for this fall. BLS-key registration measured live from Stakewiz.</div>
    </div>
    <div class="upcard">
      <div class="up-name">Agave client</div>
      <div class="up-status">{esc(gh.get('agave_latest_tag') or 'n/a')} latest</div>
      <div class="muted small">Polled node runs v{esc(net.get('node_version') or '?')}.
        Latest release published {esc((gh.get('agave_published_at') or '')[:10])}.</div>
    </div>
    <div class="upcard">
      <div class="up-name">Network status</div>
      <div class="up-status">{esc(stp.get('statuspage_description') or 'n/a')}</div>
      <div class="muted small">{stp.get('unresolved_incidents', 0)} unresolved incident(s)
        on status.solana.com · RPC health check: {esc(net.get('health') or '?')}.</div>
    </div>
  </div>
  {_news_block(snap)}
</section>"""

    # ---- provenance panel: one chip per source
    chips = ""
    for name, s in (snap.get("sources") or {}).items():
        label, domain = SOURCE_LABELS.get(name, (name, ""))
        c = STATUS_COLORS["good" if s["ok"] else "critical"]
        state = f'{s["latency_ms"]}ms' if s["ok"] else "failed"
        tip = (f'{label} · fetched {s["fetched_at"]}'
               + ("" if s["ok"] else f' · {(s.get("error") or "")[:100]}'))
        chips += f"""<div class="srcchip" title="{esc(tip)}">
  <i class="dot" style="background:{c}"></i>
  <div class="srcchip-txt"><span class="srcchip-name">{esc(label)}</span>
    <span class="srcchip-domain">{esc(domain)}</span></div>
  <span class="srcchip-lat">{esc(state)}</span>
</div>"""

    changelog_rows = "".join(
        f'<div class="clrow"><span class="clver">{esc(ver)}</span>'
        f'<span class="muted small">{esc(date)}</span>'
        f'<div class="small">{esc(text)}</div></div>'
        for date, ver, text in CHANGELOG)

    footer = f"""
<section class="card">
  <div class="section-head"><h2>Sources &amp; methodology</h2>
    <span class="muted small">every endpoint public &amp; keyless · hover a chip for details</span></div>
  <div class="srcgrid">{chips}</div>
  <p class="muted small" style="margin-top:14px">REV = chain base+priority fees
  (DeFiLlama) + Jito MEV tips (Kobe), following the Blockworks methodology.
  Daily active addresses has no keyless source; non-vote TPS is the labeled
  activity proxy (or enable the optional Dune extractor). X/Twitter's keyless
  endpoints are gone; announcements come from solana.com's official feed,
  GitHub and the status page instead.</p>
</section>
<section class="card footgrid-card">
  <div class="footgrid">
    <div>
      <div class="foot-head">SOL<b style="color:var(--accent)">BEAT</b></div>
      <p class="muted small">An autonomous, zero-key terminal for the state of
      the Solana network. Python stdlib only — no frameworks, no chart
      libraries, no API keys. Refreshes itself every 30 minutes.</p>
      <p class="small" style="margin-top:8px">built with 💙 by
        <a href="https://github.com/andreolf">andreolf</a></p>
    </div>
    <div>
      <div class="foot-head">Resources</div>
      <a class="footlink" href="https://github.com/andreolf/solbeat">GitHub repository</a>
      <a class="footlink" href="report.md">Markdown report</a>
      <a class="footlink" href="data.json">JSON data (schema v{esc(snap.get('schema_version', '1'))})</a>
      <a class="footlink" href="https://solana.com/data">solana.com/data</a>
      <a class="footlink" href="https://status.solana.com">Solana status page</a>
      <a class="footlink" href="https://defillama.com/chain/solana">DeFiLlama · Solana</a>
    </div>
    <div>
      <div class="foot-head">Changelog</div>
      {changelog_rows}
    </div>
  </div>
</section>
<footer class="muted small">Solbeat · generated {esc(snap.get('generated_at', ''))}
  · data refreshes every 30 min · not financial advice</footer>"""

    # ---- live JS payload
    live = {
        "slot": net.get("slot"),
        "slotMs": slot_ms or 400,
        "revPerMin": der.get("rev_per_min_usd") or 0,
        "generatedAt": snap.get("generated_at"),
        "tps": net.get("tps") or 0,
        "txTotal": net.get("tx_count_total") or 0,
    }

    jsonld = json.dumps({
        "@context": "https://schema.org",
        "@type": "Dataset",
        "name": "Solbeat — State of the Solana Network",
        "description": SITE_DESC,
        "url": BASE_URL,
        "license": "https://opensource.org/licenses/MIT",
        "isAccessibleForFree": True,
        "creator": {"@type": "Person", "name": "andreolf",
                    "url": "https://github.com/andreolf"},
        "keywords": ["Solana", "dashboard", "TPS", "validators", "REV",
                     "TVL", "stablecoins", "DEX volume", "Alpenglow",
                     "SIMD-525", "blockchain analytics", "open source"],
        "temporalCoverage": snap.get("generated_at"),
        "distribution": [
            {"@type": "DataDownload", "encodingFormat": "application/json",
             "contentUrl": BASE_URL + "data.json"},
            {"@type": "DataDownload", "encodingFormat": "text/markdown",
             "contentUrl": BASE_URL + "report.md"},
        ],
    })

    page = f"""<!doctype html>
<html lang="en"><head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Solbeat — Live Solana Network Dashboard (TPS, Validators, REV, TVL)</title>
<meta name="description" content="{esc(SITE_DESC)}">
<link rel="canonical" href="{BASE_URL}">
<meta name="theme-color" content="#0d0d0d">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Solbeat">
<meta property="og:title" content="Solbeat — the heartbeat terminal for the Solana network">
<meta property="og:description" content="{esc(SITE_DESC)}">
<meta property="og:url" content="{BASE_URL}">
<meta property="og:image" content="{BASE_URL}screenshot.png">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="Solbeat — the heartbeat terminal for the Solana network">
<meta name="twitter:description" content="Live Solana metrics, zero API keys, refreshes itself every 30 min. Open source.">
<meta name="twitter:image" content="{BASE_URL}screenshot.png">
<link rel="alternate" type="application/json" href="data.json" title="Machine-readable snapshot">
<link rel="icon" href='{FAVICON}'>
<script type="application/ld+json">{jsonld}</script>
<style>
:root {{
  --page:#0d0d0d; --surface:#1a1a19; --border:rgba(255,255,255,.10);
  --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --grid:#2c2c2a;
  --accent:#3987e5;
}}
* {{ box-sizing:border-box; margin:0; padding:0; }}
body {{ background:var(--page); color:var(--ink2);
  font:15px/1.5 system-ui,-apple-system,"Segoe UI",sans-serif; padding:20px; }}
.wrap {{ max-width:1160px; margin:0 auto; display:flex; flex-direction:column; gap:14px; }}
a {{ color:var(--accent); }}
.card {{ background:var(--surface); border:1px solid var(--border);
  border-radius:10px; padding:18px 20px; overflow-x:auto; }}
header.top {{ display:flex; align-items:center; gap:14px; flex-wrap:wrap; }}
.wordmark {{ font-family:ui-monospace,SFMono-Regular,Menlo,monospace;
  font-size:22px; font-weight:700; color:var(--ink); letter-spacing:1px; }}
.wordmark b {{ color:var(--accent); }}
.tagline {{ color:var(--muted); font-size:13px; }}
.healthpill {{ margin-left:auto; display:flex; align-items:center; gap:8px;
  font-size:12px; font-weight:650; letter-spacing:1px; color:var(--ink); }}
.pulse {{ width:10px; height:10px; border-radius:50%; }}
@keyframes beat {{ 0%,100% {{ transform:scale(1); opacity:1; }} 50% {{ transform:scale(1.35); opacity:.7; }} }}
.pulse {{ animation:beat 1.6s ease-in-out infinite; }}
.age {{ color:var(--muted); font-size:12px; }}
.hero {{ display:flex; gap:28px; align-items:center; flex-wrap:wrap; }}
.herostrip {{ margin-top:16px; }}
.hero-left {{ flex:1.3; min-width:280px; }}
.hero-mid {{ flex:1; min-width:260px; }}
.hero-right {{ display:flex; align-items:center; gap:14px; }}
.hero-label {{ font-size:11px; letter-spacing:1.5px; color:var(--muted);
  display:flex; gap:8px; align-items:center; }}
.livedot {{ font-size:9px; font-weight:700; letter-spacing:1px; color:#0ca30c;
  border:1px solid #0ca30c44; border-radius:20px; padding:1px 7px;
  opacity:.28; cursor:help; transition:opacity .4s; }}
.livedot.on {{ opacity:1; }}
.livedot.on::before {{ content:''; display:inline-block; width:5px; height:5px;
  border-radius:50%; background:#0ca30c; margin-right:4px;
  animation:beat 1.6s infinite; }}
.hero-slot {{ font-size:46px; font-weight:650; color:var(--ink); line-height:1.15;
  font-variant-numeric:normal; }}
.hero-under {{ color:var(--muted); font-size:12px; margin-top:4px; }}
.hero-epoch {{ font-size:14px; color:var(--ink); }}
.hero-stats {{ display:grid; grid-template-columns:1fr 1fr; gap:12px 20px; }}
.hero-stats > div {{ display:flex; flex-direction:column; }}
.hs-label {{ font-size:11px; letter-spacing:1px; color:var(--muted); text-transform:uppercase; }}
.hs-value {{ font-size:22px; font-weight:650; color:var(--ink); }}
.hs-note {{ display:block; font-size:11px; color:var(--accent); line-height:1.3; }}
.chartcard h2 {{ font-size:14px; }}
.section-head {{ display:flex; align-items:baseline; gap:10px; margin-bottom:12px; flex-wrap:wrap; }}
.section-head h2 {{ font-size:15px; color:var(--ink); font-weight:650; }}
.tiles {{ display:grid; grid-template-columns:repeat(auto-fill,minmax(255px,1fr)); gap:14px; }}
.tile {{ background:var(--surface); border:1px solid var(--border);
  border-radius:10px; padding:14px 16px; display:flex; flex-direction:column; gap:4px; }}
.tile-head {{ display:flex; justify-content:space-between; align-items:center; gap:6px; }}
.tile-label {{ font-size:11px; letter-spacing:1px; color:var(--muted); text-transform:uppercase; }}
.tile-value {{ font-size:26px; font-weight:650; color:var(--ink); }}
.tile-sub {{ font-size:12px; color:var(--muted); }}
.delta {{ font-weight:600; margin-right:6px; }}
.spark {{ margin-top:6px; align-self:flex-start; }}
.prov {{ display:inline-flex; align-items:center; gap:5px; font-size:10.5px;
  color:var(--muted); border:1px solid var(--border); border-radius:20px;
  padding:2px 8px; white-space:nowrap; cursor:help; }}
.prov i, .dot {{ width:6px; height:6px; border-radius:50%; display:inline-block; }}
.strip {{ display:flex; gap:2px; margin-top:6px; flex-wrap:nowrap; }}
.strip i {{ height:16px; border-radius:2px; flex:1 1 2px; min-width:0; max-width:10px; }}
.striprow {{ display:flex; align-items:center; gap:10px; margin-top:8px; }}
.strip-label {{ width:90px; font-size:11px; color:var(--muted); text-transform:uppercase;
  letter-spacing:.5px; flex-shrink:0; }}
.striprow .strip {{ flex:1; margin-top:0; }}
.striplegend {{ margin-top:10px; }}
.signal {{ display:flex; gap:10px; align-items:baseline; padding:7px 0;
  border-bottom:1px solid var(--border); font-size:14px; }}
.signal:last-of-type {{ border-bottom:none; }}
.sig-icon {{ width:14px; text-align:center; }}
.sig-level {{ font-size:11px; font-weight:700; letter-spacing:1px; }}
.sig-class {{ font-size:11px; color:var(--muted); border:1px solid var(--border);
  border-radius:4px; padding:1px 6px; font-family:ui-monospace,monospace; }}
.vstats {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(150px,1fr));
  gap:14px; margin-bottom:16px; }}
.vstats > div {{ display:flex; flex-direction:column; }}
.vtable {{ width:100%; border-collapse:collapse; font-size:13.5px; }}
.vtable th {{ text-align:left; font-size:11px; letter-spacing:1px; color:var(--muted);
  text-transform:uppercase; font-weight:600; padding:6px 8px;
  border-bottom:1px solid var(--border); }}
.vtable td {{ padding:7px 8px; border-bottom:1px solid var(--border);
  font-variant-numeric:tabular-nums; }}
.vtable tr:last-child td {{ border-bottom:none; }}
.vtable .num, .vtable th.num {{ text-align:right; }}
.mono {{ font-family:ui-monospace,SFMono-Regular,Menlo,monospace; font-size:12.5px; }}
.stakebar {{ background:var(--grid); border-radius:3px; height:6px; width:100%; min-width:60px; }}
.stakebar div {{ background:var(--accent); height:6px; border-radius:3px; }}
.meter {{ background:rgba(57,135,229,.16); border-radius:5px; height:10px;
  margin:8px 0 6px; }}
.meter-fill {{ height:10px; border-radius:5px; }}
.blsrow {{ margin-top:18px; }}
.twocol {{ display:grid; grid-template-columns:1fr 1fr; gap:14px; }}
@media (max-width:820px) {{ .twocol {{ grid-template-columns:1fr; }} }}
.prow {{ display:flex; align-items:center; gap:10px; margin:8px 0; }}
.prow-label {{ width:120px; font-size:13px; flex-shrink:0; }}
.prow-track {{ flex:1; background:var(--grid); border-radius:3px; height:8px; }}
.prow-bar {{ background:var(--accent); height:8px; border-radius:3px; }}
.prow-val {{ width:110px; text-align:right; font-size:12.5px; color:var(--ink);
  font-variant-numeric:tabular-nums; flex-shrink:0; }}
.commentary {{ font-size:14.5px; color:var(--ink2); border-left:3px solid var(--accent);
  padding-left:14px; margin-bottom:16px; }}
.upgrid {{ display:grid; grid-template-columns:repeat(auto-fill,minmax(250px,1fr)); gap:14px; }}
.upcard {{ border:1px solid var(--border); border-radius:8px; padding:12px 14px; }}
.up-name {{ font-size:13px; font-weight:650; color:var(--ink); }}
.up-status {{ font-size:13px; color:var(--accent); font-weight:600; margin:4px 0 6px;
  display:flex; align-items:center; gap:7px; }}
.live-dot {{ width:8px; height:8px; border-radius:50%; background:#0ca30c;
  display:inline-block; animation:beat 1.6s infinite; }}
.muted {{ color:var(--muted); }}
.small {{ font-size:12px; }}
footer {{ text-align:center; padding:8px 0 20px; }}
.newsrow {{ padding:6px 0; border-bottom:1px solid var(--border); font-size:14px; }}
.newsrow:last-child {{ border-bottom:none; }}
.srcgrid {{ display:grid; grid-template-columns:repeat(auto-fill,minmax(240px,1fr)); gap:10px; }}
.srcchip {{ display:flex; align-items:center; gap:9px; border:1px solid var(--border);
  border-radius:8px; padding:9px 12px; cursor:help; }}
.srcchip .dot {{ flex-shrink:0; width:7px; height:7px; }}
.srcchip-txt {{ display:flex; flex-direction:column; min-width:0; flex:1; }}
.srcchip-name {{ font-size:12.5px; color:var(--ink); white-space:nowrap;
  overflow:hidden; text-overflow:ellipsis; }}
.srcchip-domain {{ font-size:10.5px; color:var(--muted);
  font-family:ui-monospace,SFMono-Regular,Menlo,monospace; white-space:nowrap;
  overflow:hidden; text-overflow:ellipsis; }}
.srcchip-lat {{ font-size:11px; color:var(--muted); font-variant-numeric:tabular-nums; }}
.footgrid {{ display:grid; grid-template-columns:1.2fr 1fr 1.6fr; gap:28px; }}
@media (max-width:820px) {{ .footgrid {{ grid-template-columns:1fr; gap:20px; }} }}
.foot-head {{ font-size:13px; font-weight:700; color:var(--ink);
  letter-spacing:1px; margin-bottom:8px; }}
.footlink {{ display:block; font-size:13px; padding:3px 0; color:var(--ink2);
  text-decoration:none; }}
.footlink:hover {{ color:var(--accent); }}
.clrow {{ margin-bottom:10px; }}
.clver {{ font-size:11.5px; font-weight:700; color:var(--accent);
  font-family:ui-monospace,monospace; margin-right:8px; }}
@media (max-width:600px) {{
  body {{ padding:10px; }}
  .card {{ padding:14px; }}
  .hero {{ gap:14px; }}
  .hero-slot {{ font-size:31px; }}
  .hs-value {{ font-size:18px; }}
  .tile-value {{ font-size:22px; }}
  .strip-label {{ width:64px; font-size:10px; }}
  .prow-label {{ width:86px; font-size:12px; }}
  .prow-val {{ width:78px; font-size:11px; }}
  .healthpill {{ margin-left:0; width:100%; }}
  .hero-right {{ width:100%; }}
}}
</style></head>
<body><div class="wrap">
<header class="top card">
  {LOGO_SVG}
  <span class="wordmark">SOL<b>BEAT</b></span>
  <span class="tagline">the heartbeat terminal for the Solana network</span>
  <span class="healthpill"><i class="pulse" style="background:{hcol}"></i>
    {htxt} · <span class="age" id="age">just updated</span></span>
</header>
{hero}
<section class="tiles">
{tiles}
</section>
{signals}
{validators}
{pulse_html}
{upgrades}
{footer}
</div>
<script>
const LIVE = {json.dumps(live)};
const t0 = Date.now();
const gen = Date.parse(LIVE.generatedAt);
// Browser-side live layer: PublicNode is a keyless RPC that allows browser
// origins (the official public endpoint 403s them). Graceful: on any failure
// the page falls back to extrapolating from the snapshot's measured slot time.
const RPC = 'https://solana-rpc.publicnode.com';
let baseSlot = LIVE.slot, baseT = t0, liveOk = false;

async function rpcCall(method, params) {{
  const r = await fetch(RPC, {{
    method: 'POST', headers: {{'Content-Type': 'application/json'}},
    body: JSON.stringify({{jsonrpc: '2.0', id: 1, method, params: params || []}})
  }});
  return (await r.json()).result;
}}
async function pollSlot() {{
  try {{
    const s = await rpcCall('getSlot');
    if (s) {{ baseSlot = s; baseT = Date.now(); liveOk = true;
      document.getElementById('livedot').classList.add('on'); }}
  }} catch (e) {{ /* stay in extrapolation mode */ }}
}}
async function pollPerf() {{
  try {{
    const s = (await rpcCall('getRecentPerformanceSamples', [1]))[0];
    if (!s || !s.numSlots) return;
    const secs = s.samplePeriodSecs || 60;
    LIVE.tps = s.numTransactions / secs;
    LIVE.slotMs = 1000 * secs / s.numSlots;
    const set = (id, v) => {{ const el = document.getElementById(id); if (el) el.textContent = v; }};
    set('v-tps', Math.round(LIVE.tps).toLocaleString('en-US'));
    if (s.numNonVoteTransactions != null)
      set('v-nvtps', Math.round(s.numNonVoteTransactions / secs).toLocaleString('en-US'));
    set('v-slotms', Math.round(LIVE.slotMs) + 'ms');
  }} catch (e) {{ /* keep snapshot values */ }}
}}
function tick() {{
  const el = Date.now() - t0;
  // slot: real (re-synced every 10s from RPC) or extrapolated
  const slot = baseSlot + Math.floor((Date.now() - baseT) / LIVE.slotMs);
  const slotEl = document.getElementById('slot');
  if (slotEl) slotEl.textContent = slot.toLocaleString('en-US');
  // lifetime transactions, ticking at the live TPS rate
  const tx = document.getElementById('txcount');
  if (tx && LIVE.txTotal) tx.textContent =
    Math.floor(LIVE.txTotal + LIVE.tps * el / 1000).toLocaleString('en-US');
  // data age
  const ageS = Math.max(0, Math.round((Date.now() - gen) / 1000));
  const ageEl = document.getElementById('age');
  if (ageEl) ageEl.textContent = ageS < 90 ? `updated ${{ageS}}s ago`
    : ageS < 5400 ? `updated ${{Math.round(ageS/60)}}m ago`
    : `updated ${{(ageS/3600).toFixed(1)}}h ago`;
  // REV clock: dollars accrued while you watch
  const rc = document.getElementById('revclock');
  if (rc && LIVE.revPerMin) rc.textContent =
    `+$${{(LIVE.revPerMin * el / 60000).toFixed(2)}} while you've watched`;
}}
setInterval(tick, 250); tick();
pollSlot(); setInterval(pollSlot, 10000);
pollPerf(); setInterval(pollPerf, 60000);
</script>
</body></html>"""

    Path("docs").mkdir(parents=True, exist_ok=True)
    Path("docs/index.html").write_text(page)
    _write_agent_files(snap)


def _write_agent_files(snap):
    """SEO + AI-agent affordances: llms.txt, robots.txt, sitemap.xml."""
    net = snap.get("network") or {}
    der = snap.get("derived") or {}
    mkt = snap.get("market") or {}
    gen = snap.get("generated_at", "")
    llms = f"""# Solbeat

> Live, keyless, auto-updating report on the state of the Solana network.
> Open source (MIT), Python stdlib only, no API keys. Data refreshes every
> 30 minutes via GitHub Actions. Last refresh: {gen}.

Current snapshot: slot {net.get('slot', 0):,}, epoch {net.get('epoch', '?')}
({net.get('epoch_progress_pct', '?')}% complete), ~{net.get('tps', 0):,.0f} TPS,
slot time {net.get('slot_time_ms', '?')}ms, SOL ${mkt.get('sol_price_usd', 0):,.2f},
REV(24h) ${der.get('rev24h_usd', 0):,.0f}.

## Data

- [data.json]({BASE_URL}data.json): full structured snapshot — network
  performance, validators (incl. Nakamoto coefficient, delinquency), economic
  indicators (price, computed REV, TVL, stablecoins, DEX volume, fees),
  tokenized equities (xStocks), program activity, exchange reserves, upgrade
  tracking (Alpenglow, SIMD-525), anomaly findings with correlation incidents,
  per-source provenance. Schema-versioned; regenerated every 30 minutes.
- [report.md]({BASE_URL}report.md): the same report as human-readable Markdown.
- [history.json]({BASE_URL}history.json): rolling cross-run metric history.

## Notes for agents

- All values originate from public keyless endpoints (Solana mainnet RPC,
  DeFiLlama, CoinGecko, Jito Kobe, Stakewiz, GitHub, solana.com RSS,
  status.solana.com); `sources` in data.json reports per-source status,
  latency and fetch time.
- REV = chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe),
  following the Blockworks methodology.
- Source code: https://github.com/andreolf/solbeat — run it yourself with
  `python3 solbeat.py run` (Python 3.9+, no dependencies).
"""
    Path("docs/llms.txt").write_text(llms)
    Path("docs/robots.txt").write_text(
        f"User-agent: *\nAllow: /\nSitemap: {BASE_URL}sitemap.xml\n")
    urls = "".join(
        f"<url><loc>{BASE_URL}{p}</loc><lastmod>{gen[:10]}</lastmod></url>"
        for p in ("", "data.json", "report.md", "llms.txt"))
    Path("docs/sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
        f"{urls}</urlset>")
