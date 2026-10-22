"""HTML dashboard renderer for Solbeat.

Renders the collected snapshot into a single self-contained dark-theme HTML
file: server-side SVG charts (no chart libraries), status-page-style anomaly
strips, provenance badges on every tile, and a small vanilla-JS layer for the
live slot ticker / REV clock / data-age counter. Stdlib only.
"""

import html
import json
from datetime import datetime, timedelta
from pathlib import Path

from solbeat_worldpath import WORLD_PATH

BASE_URL = "https://www.solbeat.xyz/"
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
    ("2026-10-22", "v1.6", "Alpenglow is live: measured confirmation & finality times (single-node batched getSlot by commitment), historical finality chart with the Alpenglow cliff (pre-upgrade bars protocol-implied from recorded slot times), dynamic upgrade card"),
    ("2026-08-31", "v1.5", "Solana Pulse sentiment composite (Fear & Greed, community votes, momentum, headline tone), status page + RSS, docs sidebar, anchor-scroll fix, scrollable changelog"),
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
        f'<polygon class="sv-fill" points="{area}"/>'
        f'<polyline class="sv-line" points="{line}" fill="none" '
        f'stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>'
        f'<circle class="sv-dot" cx="{ex:.1f}" cy="{ey:.1f}" r="4"/></svg>'
    )


def big_chart(series, w=1120, h=150, color=BLUE, label=""):
    """Main line chart (TPS over ~12h) with hairline grid + endpoint label."""
    pts = [v for v in series if v is not None]
    if len(pts) < 2:
        return ""
    lo, hi = min(pts), max(pts)
    span = (hi - lo) or 1
    padl, padr, padt, padb = 52, 90, 12, 8
    step = (w - padl - padr) / (len(pts) - 1)
    coords = [(padl + i * step,
               h - padb - (v - lo) / span * (h - padt - padb))
              for i, v in enumerate(pts)]
    line = " ".join(f"{x:.1f},{y:.1f}" for x, y in coords)
    area = f"{padl},{h - padb} " + line + f" {coords[-1][0]:.1f},{h - padb}"
    grid = ""
    for y, v in ((padt, hi), ((padt + h - padb) / 2, (hi + lo) / 2), (h - padb, lo)):
        grid += (f'<line class="sv-grid" x1="{padl}" y1="{y}" x2="{w - padr}" '
                 f'y2="{y}" stroke-width="1"/>'
                 f'<text class="sv-muted" x="{padl - 8}" y="{y + 4:.0f}" '
                 f'font-size="11" text-anchor="end">{fmt_num(v)}</text>')
    ex, ey = coords[-1]
    ey_label = min(max(ey, padt + 10), h - padb - 2)
    return (
        f'<svg id="tpschart" width="100%" viewBox="0 0 {w} {h}" '
        f'preserveAspectRatio="none" role="img" aria-label="{esc(label)}">'
        f'{grid}'
        f'<polygon class="sv-fill2" points="{area}"/>'
        f'<polyline class="sv-line" points="{line}" fill="none" '
        f'stroke-width="2" stroke-linejoin="round"/>'
        f'<circle class="sv-dot" cx="{ex:.1f}" cy="{ey:.1f}" r="4"/>'
        f'<text class="sv-ink" x="{ex + 10:.1f}" y="{ey_label + 4:.1f}" '
        f'font-size="13" font-weight="600">{pts[-1]:,.0f}</text>'
        f'<text class="sv-muted" x="{ex + 10:.1f}" y="{ey_label + 20:.1f}" '
        f'font-size="11">now</text>'
        f'</svg>'
    )


def strip(levels, titles=None, label=""):
    """Status-page-style tick strip: one tick per interval, colored by level.
    Ticks carry data-tip and are click/tap-inspectable via the popover JS."""
    ticks = []
    titles = titles or [""] * len(levels)
    for lv, t in zip(levels, titles):
        c = STATUS_COLORS.get(lv, STATUS_COLORS["na"])
        ticks.append(f'<i style="background:{c}" data-tip="{esc(t)}" tabindex="0"></i>')
    return (f'<div class="strip" role="img" aria-label="{esc(label)}">'
            + "".join(ticks) + "</div>")


def epoch_ring(pct, size=92):
    r = 38
    c = 2 * 3.14159 * r
    filled = c * pct / 100
    return (
        f'<svg width="{size}" height="{size}" viewBox="0 0 {size} {size}" '
        f'role="img" aria-label="Epoch progress {pct}%">'
        f'<circle class="ring-track" cx="{size/2}" cy="{size/2}" r="{r}" '
        f'fill="none" stroke-width="7"/>'
        f'<circle class="ring-prog" cx="{size/2}" cy="{size/2}" r="{r}" '
        f'fill="none" stroke-width="7" stroke-linecap="round" '
        f'stroke-dasharray="{filled:.1f} {c:.1f}" '
        f'transform="rotate(-90 {size/2} {size/2})"/>'
        f'<text class="sv-ink" x="50%" y="53%" text-anchor="middle" '
        f'dominant-baseline="middle" font-size="19" font-weight="650">{pct:.0f}%</text>'
        f'</svg>'
    )


SOL_GRAD = ('<linearGradient id="solg" x1="0" y1="1" x2="1" y2="0">'
            '<stop offset="0" stop-color="#9945FF"/>'
            '<stop offset="1" stop-color="#14F195"/></linearGradient>')

LOGO_SVG = ('<svg class="logomark" width="30" height="20" viewBox="0 0 34 20" '
            f'aria-hidden="true"><defs>{SOL_GRAD}</defs>'
            '<polyline points="0,11 9,11 12,5 16,17 20,3 23,11 34,11" '
            'fill="none" stroke="url(#solg)" stroke-width="2.4" '
            'stroke-linecap="round" stroke-linejoin="round"/></svg>')

# The Solana three-bar glyph (simplified), Solana brand gradient.
SOL_GLYPH = ('<svg width="{s}" height="{s2}" viewBox="0 0 100 80" aria-hidden="true">'
             '<defs><linearGradient id="solg{uid}" x1="0" y1="1" x2="1" y2="0">'
             '<stop offset="0" stop-color="#9945FF"/>'
             '<stop offset="1" stop-color="#14F195"/></linearGradient></defs>'
             '<path fill="url(#solg{uid})" d="M14 0 H100 L86 16 H0 Z"/>'
             '<path fill="url(#solg{uid})" d="M0 32 H86 L100 48 H14 Z"/>'
             '<path fill="url(#solg{uid})" d="M14 64 H100 L86 80 H0 Z"/></svg>')


def sol_glyph(size=14, uid="a"):
    return SOL_GLYPH.format(s=size, s2=round(size * 0.8), uid=uid)

FAVICON = ('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" '
           'viewBox="0 0 32 32"><rect width="32" height="32" rx="7" '
           'fill="%230d0d0d"/><polyline points="4,17 11,17 13,10 17,23 20,7 22,17 28,17" '
           'fill="none" stroke="%233987e5" stroke-width="2.6" '
           'stroke-linecap="round" stroke-linejoin="round"/></svg>')


TOWERBFT_FINALITY_SLOTS = 31.5
TOWERBFT_CONF_SLOTS = 1.5
# Alpenglow took over block-by-block at this published mainnet slot
# (Oct 21 2026, epoch 1064) — history entries record slots, so the era
# split is exact even for snapshots taken before we measured finality.
ALPENGLOW_SLOT = 459_653_000


def finality_chart(history, w=1120, h=230):
    """Confirmation & finality over the full run history. Entries without a
    measured value (pre-upgrade snapshots) are back-computed from TowerBFT's
    consensus rules x that snapshot's measured slot time, and labeled implied.
    A dashed marker sits at the first measured sub-2s finality: Alpenglow."""
    pts = []
    for e in history:
        sm = e.get("slot_ms")
        post = (e.get("slot") or 0) >= ALPENGLOW_SLOT
        if e.get("final_s") is not None:
            pts.append({"ts": e.get("ts", ""), "conf": e.get("conf_s") or 0,
                        "fin": e["final_s"], "kind": "measured", "post": True})
        elif sm and post:
            # Alpenglow era before we measured: ~1 slot to finality.
            pts.append({"ts": e.get("ts", ""), "conf": round(sm / 1000, 2),
                        "fin": round(sm / 1000, 2),
                        "kind": "implied (Alpenglow era)", "post": True})
        elif sm:
            pts.append({"ts": e.get("ts", ""),
                        "conf": round(TOWERBFT_CONF_SLOTS * sm / 1000, 2),
                        "fin": round(TOWERBFT_FINALITY_SLOTS * sm / 1000, 2),
                        "kind": "implied (TowerBFT rule)", "post": False})
    if len(pts) < 2:
        return ""
    # Downsample to <=110 bars, averaging within chunks.
    target = 110
    chunk = max(1, -(-len(pts) // target))
    bars = []
    for i in range(0, len(pts), chunk):
        grp = pts[i:i + chunk]
        bars.append({
            "ts": grp[0]["ts"],
            "conf": sum(p["conf"] for p in grp) / len(grp),
            "fin": sum(p["fin"] for p in grp) / len(grp),
            "post": any(p["post"] for p in grp),
            "kind": grp[-1]["kind"],
        })
    padl, padr, padt, padb = 46, 10, 14, 26
    plot_w, plot_h = w - padl - padr, h - padt - padb
    ymax = max(max(b["fin"] for b in bars) * 1.15, 1.0)
    bw = plot_w / len(bars)
    gap = min(2, bw * 0.25)

    grid, out = "", ""
    step = 2 if ymax > 4 else 1
    y = step
    while y < ymax:
        yy = padt + plot_h * (1 - y / ymax)
        grid += (f'<line class="sv-grid" x1="{padl}" y1="{yy:.0f}" '
                 f'x2="{w - padr}" y2="{yy:.0f}" stroke-width="1"/>'
                 f'<text class="sv-muted" x="{padl - 8}" y="{yy + 4:.0f}" '
                 f'font-size="11" text-anchor="end">{y:g}s</text>')
        y += step
    grid += (f'<text class="sv-muted" x="{padl - 8}" y="{padt + plot_h + 4:.0f}" '
             f'font-size="11" text-anchor="end">0</text>')
    marker_x = None
    for i, b in enumerate(bars):
        if b["post"] and marker_x is None:
            marker_x = padl + i * bw
        x = padl + i * bw
        fh = plot_h * b["fin"] / ymax
        ch = plot_h * min(b["conf"], b["fin"]) / ymax
        day = b["ts"][:16].replace("T", " ")
        kind = b["kind"]
        tip = esc(f'{day} UTC · confirmation {b["conf"]:.2f}s · '
                  f'finality {b["fin"]:.2f}s · {kind}')
        out += (f'<g class="fbar" data-tip="{tip}" tabindex="0">'
                f'<rect class="fc-fin" x="{x + gap/2:.1f}" '
                f'y="{padt + plot_h - fh:.1f}" width="{max(bw - gap, 1):.1f}" '
                f'height="{max(fh - ch, 0):.1f}" rx="1.5"/>'
                f'<rect class="fc-conf" x="{x + gap/2:.1f}" '
                f'y="{padt + plot_h - ch:.1f}" width="{max(bw - gap, 1):.1f}" '
                f'height="{max(ch, 1):.1f}" rx="1.5"/></g>')
    marker = ""
    if marker_x is not None and marker_x > padl + 4:
        marker = (f'<line class="ag-marker" x1="{marker_x:.0f}" y1="{padt - 4}" '
                  f'x2="{marker_x:.0f}" y2="{padt + plot_h}" stroke-width="1.5"/>'
                  f'<text x="{marker_x - 6:.0f}" y="{padt + 6}" font-size="11.5" '
                  f'font-weight="650" text-anchor="end" fill="var(--series3)">'
                  f'Alpenglow</text>')
    lab_l = esc((bars[0]["ts"][:10]))
    lab_r = esc((bars[-1]["ts"][:10]))
    axis = (f'<text class="sv-muted" x="{padl}" y="{h - 6}" font-size="11">{lab_l}</text>'
            f'<text class="sv-muted" x="{w - padr}" y="{h - 6}" font-size="11" '
            f'text-anchor="end">{lab_r}</text>')
    return (f'<svg width="100%" viewBox="0 0 {w} {h}" role="img" '
            f'aria-label="Confirmation and finality time history">'
            f'{grid}{out}{marker}{axis}</svg>')


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
        grid += (f'<line class="sv-grid" x1="{x:.0f}" y1="0" x2="{x:.0f}" '
                 f'y2="{h}" stroke-width="1"/>')
    for lat in range(-30, 61, 30):
        _, y = xy(lat, 0)
        wgt = 1.5 if lat == 0 else 1
        grid += (f'<line class="sv-grid" x1="0" y1="{y:.0f}" x2="{w}" '
                 f'y2="{y:.0f}" stroke-width="{wgt}"/>')
    max_stake = geo[0]["stake"] or 1
    dots = ""
    # draw small dots first so heavyweights sit on top
    for g in reversed(geo):
        x, y = xy(g["lat"], g["lon"])
        r = max(2.1, 9 * (g["stake"] / max_stake) ** 0.5)
        label = esc(f'{g["name"] or "validator"} — {g["stake"]:,} SOL — {g["loc"]}')
        big = g["stake"] > max_stake / 8
        dots += (f'<circle class="vdot{" big" if big else ""}" cx="{x:.1f}" '
                 f'cy="{y:.1f}" r="{r:.1f}" opacity="{0.95 if big else 0.7}" '
                 f'data-tip="{label}" tabindex="0"></circle>')
    land = f'<path class="land" d="{WORLD_PATH}" stroke-width="0.6"/>'
    return (f'<svg width="100%" viewBox="0 0 {w} {h}" role="img" '
            f'aria-label="World map of Solana validators, dot size by stake">'
            f'{land}{grid}{dots}</svg>')


def meter(pct):
    pct = max(0, min(100, pct or 0))
    return (f'<div class="meter"><div class="meter-fill" '
            f'style="width:{pct:.1f}%"></div></div>')


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
        delta_html = (f'<span class="delta {"d-up" if good else "d-down"}">'
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


def daily_levels(series, warn_pct, serious_pct, end_date=None, is_price=False):
    """Color a daily series by day-over-day % change for the status strips.
    Titles carry date + value + change for the click-to-inspect popover."""
    levels, titles = [], []
    n = len(series)
    for i in range(1, n):
        prev, cur = series[i - 1], series[i]
        day = ""
        if end_date:
            day = (end_date - timedelta(days=n - 1 - i)).strftime("%b %d") + " · "
        if not prev or cur is None:
            levels.append("na")
            titles.append(f"{day}no data")
            continue
        ch = 100 * (cur - prev) / prev
        lv = ("serious" if abs(ch) >= serious_pct
              else "warning" if abs(ch) >= warn_pct else "ok")
        levels.append(lv)
        val = f"${cur:,.2f}" if is_price else fmt_usd(cur)
        titles.append(f"{day}{val} · {ch:+.1f}% day-over-day")
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
    for p in ((snap.get("x") or {}).get("posts") or [])[:5]:
        rows += (f'<div class="newsrow">𝕏 <b>@{esc(p["handle"])}</b> '
                 f'<a href="{esc(p["url"])}" target="_blank" rel="noopener">'
                 f'{esc(p["text"][:140])}…</a></div>')
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
    try:
        gen_dt = datetime.strptime(snap.get("generated_at", ""), "%Y-%m-%dT%H:%M:%SZ")
    except ValueError:
        gen_dt = None
    for i in range(0, len(perf), bucket):
        chunk = [p["slot_ms"] for p in perf[i:i + bucket] if p.get("slot_ms")]
        if not chunk:
            continue
        avg = sum(chunk) / len(chunk)
        lv = ("serious" if avg >= 700 else "warning" if avg >= 500 else "ok")
        slot_levels.append(lv)
        when = ""
        if gen_dt:
            t = gen_dt - timedelta(minutes=len(perf) - i)
            when = t.strftime("%H:%M") + " UTC · "
        slot_titles.append(f"{when}{avg:.0f}ms avg slot time")

    # Confirmation & finality chart over the recorded history, with range
    # selector (snapshots land ~every 30 min, so counts approximate time).
    try:
        full_hist = json.loads(Path("docs/history.json").read_text())
    except Exception:
        full_hist = snap.get("history") or []
    fin_panels, fin_btns = "", ""
    for lab, n in (("24h", 48), ("7d", 336), ("30d", 1440), ("All", None)):
        fc = finality_chart(full_hist if n is None else full_hist[-n:])
        if not fc:
            continue
        active = n is None
        fin_panels += (f'<div class="range-panel" data-range="{lab}"'
                       f'{"" if active else " hidden"}>{fc}</div>')
        fin_btns += (f'<button class="rbtn{" active" if active else ""}" '
                     f'data-range="{lab}">{lab}</button>')
    finality_card = "" if not fin_panels else f"""
<section class="card chartcard">
  <div class="section-head"><h2>Confirmation &amp; finality time</h2>
    <span class="legend"><span><i style="background:var(--accent)"></i>confirmation</span>
      <span><i style="background:var(--series3)"></i>finality (rest)</span></span>
    {B('solana_rpc', 'RPC · getSlot by commitment')}
    <span class="rangesel">{fin_btns}</span></div>
  {fin_panels}
  <div class="muted small" style="margin-top:6px">Alpenglow marker = published
    takeover slot 459,653,000 (Oct 21 2026, epoch 1064). Bars before it are
    protocol-implied (TowerBFT rooting depth: ~31.5 slots × that snapshot's
    measured slot time — the canonical "~12.8s at 400ms" figure, scaled);
    after it, measured live from RPC commitment levels (~1 slot implied for
    the brief gap before measuring began). Dashboards using shallower
    intervals (e.g. confirmed→finalized) show smaller pre-Alpenglow values ·
    click any bar for details</div>
</section>"""

    # TPS chart ranges (performance samples are ~1/min).
    tps_panels, tps_btns = "", ""
    for lab, n in (("1h", 60), ("3h", 180), ("6h", 360), ("12h", None)):
        ser = tps_series if n is None else tps_series[-n:]
        bc = big_chart(ser, label=f"TPS over the last {lab}")
        if not bc:
            continue
        active = n is None
        tps_panels += (f'<div class="range-panel" data-range="{lab}"'
                       f'{"" if active else " hidden"}>{bc}</div>')
        tps_btns += (f'<button class="rbtn{" active" if active else ""}" '
                     f'data-range="{lab}">{lab}</button>')

    hero = f"""
<section class="card" id="network">
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
        <div><span class="hs-label">finality</span><span class="hs-value">{f"{net['finality_s']:.2f}s" if net.get('finality_s') is not None else "n/a"}</span>
          <span class="hs-note">{f"conf {net['confirmation_s']:.2f}s · ⚡ Alpenglow live" if der.get('alpenglow_active') and net.get('confirmation_s') is not None else ("⚡ Alpenglow live — measured" if der.get('alpenglow_active') else "")}</span></div>
        <div><span class="hs-label">est. daily txs</span><span class="hs-value">{fmt_num(net.get('est_daily_txs'))}</span></div>
      </div>
    </div>
    <div class="hero-right">
      {epoch_ring(net.get('epoch_progress_pct') or 0)}
      <div class="hero-epoch">epoch {net.get('epoch', '?')}<br>
        <span class="muted">~{der.get('epoch_eta_hours', '?')}h remaining</span><br>
        <span class="solpill" style="margin-top:6px">{sol_glyph(11, 'hero')} MAINNET</span></div>
    </div>
  </div>
  <div class="herostrip">
    <div class="hero-under" style="margin-bottom:2px">last 12h slot performance</div>
    {strip(slot_levels, slot_titles, "12h slot performance")}
  </div>
</section>
<section class="card chartcard">
  <div class="section-head"><h2>Transactions per second</h2>
    {B('solana_rpc', 'RPC · getRecentPerformanceSamples')}
    <span class="rangesel">{tps_btns}</span></div>
  {tps_panels}
</section>
{finality_card}"""

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
                   '<i style="background:var(--accent)"></i>computed</span>'),
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

    try:
        end_date = datetime.strptime(snap.get("generated_at", "")[:10], "%Y-%m-%d")
    except ValueError:
        end_date = None
    strips_html = ""
    strip_defs = [
        ("SOL price", mkt.get("price_series_30d") or [], 5, 10, True),
        ("Chain TVL", tvl.get("tvl_series") or [], 5, 10, False),
        ("Stablecoins", stb.get("stablecoin_series") or [], 2, 5, False),
        ("DEX volume", dex.get("dex_series") or [], 25, 50, False),
    ]
    for name, series, w, s, is_price in strip_defs:
        if len(series) > 5:
            lv, ti = daily_levels(series[-61:], w, s, end_date, is_price)
            strips_html += (f'<div class="striprow"><span class="strip-label">'
                            f'{esc(name)}</span>{strip(lv, ti, name)}</div>')
    hist = snap.get("history") or []
    if len(hist) >= 3:
        recent = hist[-60:]
        lv = [h.get("anomaly_level", "ok") for h in recent]
        ti = [f"{(h.get('ts') or '')[:16].replace('T', ' ')} UTC · "
              + ("all clear" if h.get("anomaly_level") == "ok"
                 else f"{h.get('anomaly_level')}: "
                      + (", ".join((h.get("levels") or {}).keys()) or "signal"))
              for h in recent]
        pad = 60 - len(recent)
        lv = ["na"] * pad + lv
        ti = ["future refresh slot — history grows every 30 min"] * pad + ti
        strips_html += (f'<div class="striprow"><span class="strip-label">'
                        f'run history</span>{strip(lv, ti, "run history")}</div>')

    signals = f"""
<section class="card" id="signals">
  <div class="section-head"><h2>Signals — anomaly detection</h2>
    <span class="muted small">per-metric z-scores + multi-source correlation</span></div>
  {signals_html}
  <div class="strips">{strips_html}</div>
  <div class="muted small striplegend">daily ticks, last ~60d ·
    <span style="color:{STATUS_COLORS['ok']}">●</span> normal ·
    <span style="color:{STATUS_COLORS['warning']}">▲</span> notable move ·
    <span style="color:{STATUS_COLORS['serious']}">▲</span> large move</div>
</section>"""

    # ---- Solana Pulse (sentiment)
    sen = snap.get("sentiment") or {}
    pulse_score = der.get("pulse") or {}
    sentiment_html = ""
    if pulse_score:
        comp_labels = {"community": "Community votes (CoinGecko)",
                       "fear_greed": "Crypto Fear & Greed",
                       "momentum": "Market momentum (price·DEX·TVL)",
                       "news": "Headline tone (48h)"}
        comp_rows = ""
        for k, v in pulse_score.get("components", {}).items():
            comp_rows += f"""<div class="prow">
  <span class="prow-label pl-wide">{esc(comp_labels.get(k, k))}</span>
  <div class="prow-track"><div class="prow-bar" style="width:{v:.0f}%"></div></div>
  <span class="prow-val">{v:.0f}/100</span>
</div>"""
        emoji = {"Bullish": "🐂", "Neutral": "🦀", "Bearish": "🐻"}[pulse_score["label"]]
        head_rows = ""
        for hl in (sen.get("headlines") or [])[:6]:
            icon = ("<span class='d-up'>▲</span>" if hl["tone"] > 0 else
                    "<span class='d-down'>▼</span>" if hl["tone"] < 0 else
                    "<span class='muted'>·</span>")
            head_rows += (f'<div class="newsrow">{icon} '
                          f'<a href="{esc(hl["link"])}" target="_blank" '
                          f'rel="noopener">{esc(hl["title"])}</a></div>')
        fng_spark = sparkline(sen.get("fng_series_30d") or [])
        sentiment_html = f"""
<section class="twocol" id="sentiment">
<div class="card">
  <div class="section-head"><h2>Solana Pulse — sentiment</h2>
    <span class="muted small">experimental composite · keyless signals</span></div>
  <div class="pulse-score"><span class="pulse-num">{pulse_score['score']}</span>
    <span class="pulse-label">{emoji} {esc(pulse_score['label'])}</span></div>
  <div class="meter" style="margin:10px 0 16px"><div class="meter-fill"
    style="width:{pulse_score['score']}%"></div></div>
  {comp_rows}
  <div class="muted small" style="margin-top:10px">Composite of CoinGecko
    community votes ({sen.get('cg_watchlist_users', 0):,} watchlists),
    the crypto Fear &amp; Greed index
    ({sen.get('fng_value', '?')} · {esc(sen.get('fng_label', ''))}),
    price/DEX/TVL momentum, and a keyword read of fresh headlines.
    Heuristic, not financial advice.</div>
</div>
<div class="card">
  <div class="section-head"><h2>Headline tone</h2>
    {B('sentiment', 'Google News RSS')}</div>
  {head_rows or '<div class="muted">no fresh headlines</div>'}
  <div class="tile-label" style="margin:12px 0 2px">FEAR &amp; GREED — 30 DAYS</div>
  {fng_spark}
</div>
</section>"""

    # ---- Pulse orb: draggable shortcut to the sentiment page
    orb_html = ""
    if pulse_score:
        orb_emoji = {"Bullish": "🐂", "Neutral": "🦀",
                     "Bearish": "🐻"}[pulse_score["label"]]
        orb_html = (
            f'<a id="pulseorb" href="pulse.html" draggable="false" '
            f'title="Solana Pulse: {pulse_score["score"]}/100 '
            f'{pulse_score["label"]} — drag me around, click for the full '
            f'breakdown">'
            f'<span class="orb-num">{pulse_score["score"]}</span>'
            f'<span class="orb-emoji">{orb_emoji}</span>'
            f'<span class="orb-tag">PULSE</span></a>'
            f'<span id="orbhint">check the Solana Pulse 👉</span>')

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
<section class="card" id="validators">
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
<section class="twocol" id="ecosystem">
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
<section class="card" id="almanac">
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
      <div class="up-status">{f'<span class="live-dot"></span> ACTIVE — finality {net["finality_s"]:.2f}s measured' if der.get("alpenglow_active") else (f"{bls_pct}% of stake BLS-ready" if bls_pct is not None else "pending")}</div>
      <div class="muted small">Consensus overhaul (Votor + Rotor) replacing
        TowerBFT{", live on mainnet since October 2026. Our own RPC measurement of sub-second finality (vs ~10s under TowerBFT) is on-chain proof — see the finality chart above" if der.get("alpenglow_active") else ": ~100–150ms finality. Approved by 98% of stake; activation via Agave v4.3"}.</div>
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
      <p class="muted small">Autonomous, zero-key terminal for the state of the
      Solana network. Python stdlib only, refreshes every 30 min,
      <b>$0/month</b> to run.</p>
      <p class="small muted" style="margin-top:8px; display:flex; align-items:center; gap:7px">
        {sol_glyph(12, 'ftr')} independent community project</p>
    </div>
    <div>
      <div class="foot-head">Solbeat</div>
      <a class="footlink" href="pulse.html">Pulse &amp; Almanac</a>
      <a class="footlink" href="https://docs.solbeat.xyz">Documentation</a>
      <a class="footlink" href="status.html">System status</a>
      <a class="footlink" href="https://github.com/andreolf/solbeat">GitHub</a>
      <a class="footlink" href="https://github.com/andreolf/solbeat/blob/main/CHANGELOG.md">Full changelog</a>
    </div>
    <div>
      <div class="foot-head">Data</div>
      <a class="footlink" href="report.md">Markdown report</a>
      <a class="footlink" href="data.json">JSON (schema v{esc(snap.get('schema_version', '1'))})</a>
      <a class="footlink" href="llms.txt">llms.txt (agents)</a>
      <a class="footlink" href="https://solana.com/data">solana.com/data</a>
      <a class="footlink" href="https://defillama.com/chain/solana">DeFiLlama</a>
    </div>
    <div>
      <div class="foot-head">Changelog</div>
      <div class="clbox">{changelog_rows}</div>
    </div>
  </div>
</section>
<footer class="muted small">built with 💙 by
  <a href="https://github.com/andreolf">andreolf</a> · Solbeat · generated
  {esc(snap.get('generated_at', ''))} · refreshes every 30 min · not
  affiliated with the Solana Foundation · not financial advice</footer>"""

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
<script>
/* apply saved theme before first paint to avoid a flash */
(function () {{
  var p = localStorage.getItem('solbeat-theme') || 'dark';
  var r = p === 'system'
    ? (matchMedia('(prefers-color-scheme: light)').matches ? 'light' : 'dark') : p;
  document.documentElement.dataset.theme = r;
}})();
</script>
<style>
:root {{
  --page:#0d0d0d; --surface:#1a1a19; --border:rgba(255,255,255,.10);
  --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --grid:#2c2c2a;
  --accent:#3987e5; --land:#242423; --landline:#3a3a37; --pop:#232322;
  --meter-track:rgba(57,135,229,.16); --d-up:#0ca30c; --d-down:#e66767;
  --series3:#199e70;
}}
html[data-theme="light"] {{
  --page:#f9f9f7; --surface:#fcfcfb; --border:rgba(11,11,11,.10);
  --ink:#0b0b0b; --ink2:#52514e; --muted:#898781; --grid:#e1e0d9;
  --accent:#2a78d6; --land:#eceae2; --landline:#d6d4ca; --pop:#ffffff;
  --meter-track:rgba(42,120,214,.16); --d-up:#006300; --d-down:#d03b3b;
  --series3:#1baf7a;
}}
* {{ box-sizing:border-box; margin:0; padding:0; }}
html {{ scroll-behavior:smooth; }}
body {{ background:var(--page); color:var(--ink2);
  font:15px/1.5 system-ui,-apple-system,"Segoe UI",sans-serif; padding:20px; }}
section[id], header[id] {{ scroll-margin-top:118px; }}
.hide-md {{ display:none; }}
@media (min-width:1280px) {{ .hide-md {{ display:inline; }} }}
.sv-line {{ stroke:var(--accent); }}
.sv-fill {{ fill:var(--accent); opacity:.1; }}
.sv-fill2 {{ fill:var(--accent); opacity:.08; }}
.sv-dot {{ fill:var(--accent); stroke:var(--surface); stroke-width:2; }}
.sv-grid {{ stroke:var(--grid); }}
.sv-ink {{ fill:var(--ink); }}
.sv-muted {{ fill:var(--muted); }}
.ring-track {{ stroke:var(--grid); }}
.ring-prog {{ stroke:var(--accent); }}
.land {{ fill:var(--land); stroke:var(--landline); }}
.vdot {{ fill:var(--accent); }}
.vdot.big {{ stroke:var(--surface); stroke-width:1.5; }}
.d-up {{ color:var(--d-up); }}
.d-down {{ color:var(--d-down); }}
.fc-conf {{ fill:var(--accent); }}
.fc-fin {{ fill:var(--series3); }}
.fbar {{ cursor:pointer; }}
.fbar:hover rect {{ opacity:.8; }}
.ag-marker {{ stroke:var(--series3); stroke-dasharray:4 4; }}
.legend {{ display:inline-flex; gap:14px; align-items:center; font-size:12px;
  color:var(--ink2); }}
.legend i {{ width:9px; height:9px; border-radius:50%; display:inline-block;
  margin-right:5px; }}
.rangesel {{ margin-left:auto; display:inline-flex; gap:4px; }}
.rbtn {{ background:none; border:1px solid var(--border); color:var(--muted);
  border-radius:7px; padding:3px 10px; font-size:11.5px; cursor:pointer;
  font-variant-numeric:tabular-nums; }}
.rbtn:hover {{ color:var(--ink); }}
.rbtn.active {{ color:var(--ink); border-color:var(--accent);
  background:var(--meter-track); }}
.wrap {{ max-width:1160px; margin:0 auto; display:flex; flex-direction:column; gap:14px; }}
a {{ color:var(--accent); }}
.card {{ background:var(--surface); border:1px solid var(--border);
  border-radius:10px; padding:18px 20px; overflow-x:auto; }}
header.top {{ position:sticky; top:10px; z-index:60; display:flex;
  align-items:center; gap:12px; flex-wrap:wrap; padding:12px 20px; }}
.wordmark {{ font-family:ui-monospace,SFMono-Regular,Menlo,monospace;
  font-size:22px; font-weight:700; color:var(--ink); letter-spacing:1px; }}
.wordmark b {{ color:var(--accent); }}
.tagline {{ color:var(--muted); font-size:13px; }}
.pricechip {{ display:inline-flex; gap:6px; align-items:center; font-size:12.5px;
  background:var(--page); border:1px solid var(--border); border-radius:8px;
  padding:5px 10px; color:var(--ink); font-variant-numeric:tabular-nums;
  white-space:nowrap; }}
.nav {{ margin-left:auto; display:flex; gap:2px; }}
.nav a {{ color:var(--ink2); text-decoration:none; font-size:13px;
  padding:5px 9px; border-radius:6px; white-space:nowrap; }}
.nav a:hover {{ color:var(--ink); background:var(--grid); }}
#themebtn {{ background:none; border:1px solid var(--border); border-radius:8px;
  padding:4px 9px; cursor:pointer; font-size:14px; line-height:1.4; }}
.healthpill {{ display:flex; align-items:center; gap:8px;
  font-size:12px; font-weight:650; letter-spacing:1px; color:var(--ink); }}
@media (max-width:980px) {{
  .nav {{ order:9; width:100%; margin-left:0; overflow-x:auto; }}
  .healthpill {{ margin-left:auto; }}
  header.top {{ position:static; }}
}}
@media (max-width:600px) {{ .pl-wide {{ width:130px; }}
  #pulseorb {{ width:76px; height:76px; right:14px; bottom:14px; }}
  .orb-num {{ font-size:21px; }}
  #orbhint {{ right:100px; bottom:40px; font-size:11.5px; }} }}
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
.vdot {{ cursor:pointer; }}
.vdot:hover, .vdot:focus {{ stroke:var(--ink); stroke-width:1.5; opacity:1; outline:none; }}
.solpill {{ display:inline-flex; align-items:center; gap:6px; font-size:10.5px;
  font-weight:650; letter-spacing:1.2px; color:var(--ink2);
  border:1px solid var(--border); border-radius:20px; padding:3px 10px; }}
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
  padding:2px 8px; white-space:nowrap; }}
.prov i, .dot {{ width:6px; height:6px; border-radius:50%; display:inline-block; }}
.strip {{ display:flex; gap:2px; margin-top:6px; flex-wrap:nowrap; }}
.strip i {{ height:16px; border-radius:2px; flex:1 1 2px; min-width:0;
  cursor:pointer; transition:transform .08s; }}
.strip i:hover, .strip i:focus {{ transform:scaleY(1.25); outline:none; }}
#tickpop {{ position:absolute; z-index:50; background:var(--pop);
  border:1px solid rgba(255,255,255,.16); border-radius:8px; padding:8px 12px;
  font-size:12.5px; color:var(--ink); box-shadow:0 6px 24px rgba(0,0,0,.5);
  max-width:280px; pointer-events:none; display:none; }}
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
.meter {{ background:var(--meter-track); border-radius:5px; height:10px;
  margin:8px 0 6px; }}
.meter-fill {{ height:10px; border-radius:5px; background:var(--accent); }}
.blsrow {{ margin-top:18px; }}
.twocol {{ display:grid; grid-template-columns:1fr 1fr; gap:14px; }}
@media (max-width:820px) {{ .twocol {{ grid-template-columns:1fr; }} }}
.prow {{ display:flex; align-items:center; gap:10px; margin:8px 0; }}
.prow-label {{ width:120px; font-size:13px; flex-shrink:0; }}
.prow-track {{ flex:1; background:var(--grid); border-radius:3px; height:8px; }}
.prow-bar {{ background:var(--accent); height:8px; border-radius:3px; }}
.prow-val {{ width:110px; text-align:right; font-size:12.5px; color:var(--ink);
  font-variant-numeric:tabular-nums; flex-shrink:0; }}
.pulse-score {{ display:flex; align-items:baseline; gap:12px; }}
.pulse-num {{ font-size:44px; font-weight:650; color:var(--ink); }}
.pulse-label {{ font-size:17px; font-weight:650; color:var(--ink); }}
.pl-wide {{ width:220px; }}
#pulseorb {{ position:fixed; right:24px; bottom:24px; z-index:55; width:94px;
  height:94px; border-radius:50%; background:var(--surface);
  border:2px solid var(--accent); display:flex; flex-direction:column;
  align-items:center; justify-content:center; gap:1px; text-decoration:none;
  cursor:grab; box-shadow:0 6px 24px rgba(0,0,0,.45); touch-action:none;
  user-select:none; -webkit-user-drag:none; }}
#pulseorb:active {{ cursor:grabbing; }}
#pulseorb.dragging {{ transform:scale(1.06); }}
#pulseorb.dragging::after {{ animation:none; opacity:0; }}
#orbhint {{ position:fixed; right:128px; bottom:56px; z-index:54;
  background:var(--surface); border:1px solid var(--accent); color:var(--ink);
  font-size:12.5px; font-weight:600; border-radius:20px; padding:7px 14px;
  box-shadow:0 6px 20px rgba(0,0,0,.4); white-space:nowrap;
  animation:beat 2.4s ease-in-out infinite; }}
#pulseorb::after {{ content:''; position:absolute; inset:-2px;
  border-radius:50%; border:2px solid var(--accent); opacity:.5;
  animation:orbring 2s ease-out infinite; pointer-events:none; }}
@keyframes orbring {{ 0% {{ transform:scale(1); opacity:.5; }}
  100% {{ transform:scale(1.45); opacity:0; }} }}
.orb-num {{ font-size:27px; font-weight:700; color:var(--ink); line-height:1; }}
.orb-emoji {{ font-size:17px; line-height:1.2; }}
.orb-tag {{ font-size:8.5px; letter-spacing:1.8px; color:var(--muted); }}
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
.footgrid {{ display:grid; grid-template-columns:1.4fr 1fr 1fr 1.6fr; gap:24px; }}
@media (max-width:900px) {{ .footgrid {{ grid-template-columns:1fr 1fr; gap:18px; }} }}
@media (max-width:540px) {{ .footgrid {{ grid-template-columns:1fr; }} }}
* {{ scrollbar-width:thin; scrollbar-color:var(--grid) transparent; }}
.clbox::-webkit-scrollbar {{ width:7px; }}
.clbox::-webkit-scrollbar-thumb {{ background:var(--grid); border-radius:4px; }}
.clbox::-webkit-scrollbar-track {{ background:transparent; }}
.foot-head {{ font-size:13px; font-weight:700; color:var(--ink);
  letter-spacing:1px; margin-bottom:8px; }}
.footlink {{ display:block; font-size:13px; padding:3px 0; color:var(--ink2);
  text-decoration:none; }}
.footlink:hover {{ color:var(--accent); }}
.clbox {{ max-height:190px; overflow-y:auto; padding-right:8px; }}
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
  <span class="tagline hide-md">the zero-API-key Solana ecosystem terminal</span>
  <nav class="nav">
    <a href="#network">Network</a><a href="#economy">Economy</a>
    <a href="#signals">Signals</a><a href="#validators">Validators</a>
    <a href="#ecosystem">Ecosystem</a><a href="pulse.html">Pulse</a>
    <a href="https://docs.solbeat.xyz">Docs</a>
  </nav>
  <button id="themebtn" aria-label="Switch theme">🌙</button>
  <span class="healthpill"><i class="pulse" style="background:{hcol}"></i>
    {htxt} · <span class="age" id="age">just updated</span></span>
</header>
{hero}
<section class="tiles" id="economy">
{tiles}
</section>
{signals}
{validators}
{orb_html}
{pulse_html}
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
// Tick inspector: click/tap or hover any strip tick for date + value details.
const pop = document.createElement('div'); pop.id = 'tickpop';
document.body.appendChild(pop);
function showTip(el) {{
  const tip = el.getAttribute('data-tip');
  if (!tip) return;
  pop.textContent = tip;
  pop.style.display = 'block';
  const r = el.getBoundingClientRect();
  const px = Math.min(Math.max(6, r.left + window.scrollX - 60),
                      window.scrollX + document.documentElement.clientWidth - 290);
  pop.style.left = px + 'px';
  pop.style.top = (r.top + window.scrollY - pop.offsetHeight - 10) + 'px';
}}
// Theme toggle: dark -> light -> system (persisted).
const tbtn = document.getElementById('themebtn');
const T_ICON = {{dark: '🌙', light: '☀️', system: '💻'}};
let themePref = localStorage.getItem('solbeat-theme') || 'dark';
function applyTheme() {{
  const r = themePref === 'system'
    ? (matchMedia('(prefers-color-scheme: light)').matches ? 'light' : 'dark')
    : themePref;
  document.documentElement.dataset.theme = r;
  tbtn.textContent = T_ICON[themePref];
  tbtn.title = `Theme: ${{themePref}} — click to change`;
}}
tbtn.addEventListener('click', () => {{
  themePref = themePref === 'dark' ? 'light'
            : themePref === 'light' ? 'system' : 'dark';
  localStorage.setItem('solbeat-theme', themePref);
  applyTheme();
}});
matchMedia('(prefers-color-scheme: light)').addEventListener('change', () => {{
  if (themePref === 'system') applyTheme();
}});
applyTheme();

// Draggable Pulse orb: drag it anywhere (position remembered), click -> pulse page.
const orb = document.getElementById('pulseorb');
const hint = document.getElementById('orbhint');
if (orb) {{
  try {{
    const saved = JSON.parse(localStorage.getItem('solbeat-orb') || 'null');
    if (saved) {{ orb.style.left = saved.x + 'px'; orb.style.top = saved.y + 'px';
      orb.style.right = 'auto'; orb.style.bottom = 'auto'; }}
    if (hint && (saved || localStorage.getItem('solbeat-orb-seen')))
      hint.remove();
  }} catch (e) {{}}
  // kill the browser's native link-drag ghost — this is what made it janky
  orb.addEventListener('dragstart', e => e.preventDefault());
  let grabX, grabY, moved = false, down = false;
  orb.addEventListener('pointerdown', e => {{
    e.preventDefault();
    down = true; moved = false;
    const r = orb.getBoundingClientRect();
    grabX = e.clientX - r.left; grabY = e.clientY - r.top;
    if (hint) hint.remove();
    try {{ orb.setPointerCapture(e.pointerId); }} catch (e2) {{}}
  }});
  orb.addEventListener('pointermove', e => {{
    if (!down) return;
    const w = orb.offsetWidth;
    const x = Math.min(Math.max(4, e.clientX - grabX), innerWidth - w - 4);
    const y = Math.min(Math.max(4, e.clientY - grabY), innerHeight - w - 4);
    const r = orb.getBoundingClientRect();
    if (Math.abs(x - r.left) + Math.abs(y - r.top) > 2) {{
      moved = true;
      orb.classList.add('dragging');
      orb.style.left = x + 'px'; orb.style.top = y + 'px';
      orb.style.right = 'auto'; orb.style.bottom = 'auto';
    }}
  }});
  orb.addEventListener('pointerup', () => {{
    down = false;
    orb.classList.remove('dragging');
    if (moved) {{
      const r = orb.getBoundingClientRect();
      try {{ localStorage.setItem('solbeat-orb',
        JSON.stringify({{x: Math.round(r.left), y: Math.round(r.top)}})); }} catch (e2) {{}}
    }}
  }});
  orb.addEventListener('click', e => {{
    try {{ localStorage.setItem('solbeat-orb-seen', '1'); }} catch (e2) {{}}
    if (moved) e.preventDefault();
  }});
}}

// Chart range selectors: show the matching pre-rendered panel.
document.addEventListener('click', e => {{
  const b = e.target.closest('.rbtn');
  if (!b) return;
  const card = b.closest('section');
  card.querySelectorAll('.rbtn').forEach(x =>
    x.classList.toggle('active', x === b));
  card.querySelectorAll('.range-panel').forEach(p =>
    p.hidden = p.dataset.range !== b.dataset.range);
}});

const TIP_SEL = '.strip i, .vdot, .fbar';
document.addEventListener('pointerover', e => {{
  const t = e.target.closest(TIP_SEL);
  if (t) showTip(t); }});
document.addEventListener('pointerout', e => {{
  if (e.target.closest(TIP_SEL)) pop.style.display = 'none'; }});
document.addEventListener('click', e => {{
  const t = e.target.closest(TIP_SEL);
  if (t) {{ showTip(t); e.stopPropagation(); }}
  else pop.style.display = 'none'; }});
// Vercel Web Analytics — inject only when served by Vercel (the script path
// doesn't exist on GitHub Pages/localhost, so we skip it there).
if (!/localhost|\\.github\\.io$/.test(location.hostname)) {{
  window.va = window.va || function () {{ (window.vaq = window.vaq || []).push(arguments); }};
  const va = document.createElement('script');
  va.defer = true; va.src = '/_vercel/insights/script.js';
  document.head.appendChild(va);
}}
</script>
</body></html>"""

    Path("docs").mkdir(parents=True, exist_ok=True)
    Path("docs/index.html").write_text(page)
    _write_pulse(snap, sentiment_html, upgrades)
    _write_agent_files(snap)
    _write_status(snap)


def _write_status(snap):
    """githubstatus.com-style status page + RSS feed for Solbeat's own systems,
    derived from the per-source provenance and cross-run history."""
    sources = snap.get("sources") or {}
    hist = snap.get("history") or []
    net = snap.get("network") or {}
    stp = snap.get("status_page") or {}
    gen = snap.get("generated_at", "")
    all_ok = all(s.get("ok") for s in sources.values()) and net.get("health") == "ok"
    banner_txt = ("All Systems Operational" if all_ok
                  else "Partial Degradation — see components")
    banner_col = "#0ca30c" if all_ok else "#fab219"

    recent = hist[-60:]
    rows = ""
    for name, s in sources.items():
        label, domain = SOURCE_LABELS.get(name, (name, ""))
        fails = sum(1 for h in recent if name in (h.get("failed_sources") or []))
        uptime = 100 * (1 - fails / len(recent)) if recent else 100.0
        ticks = ""
        for h in recent:
            bad = name in (h.get("failed_sources") or [])
            c = STATUS_COLORS["critical" if bad else "ok"]
            t = f'{(h.get("ts") or "")[:16].replace("T", " ")} UTC · ' + \
                ("outage" if bad else "operational")
            ticks += f'<i style="background:{c}" data-tip="{esc(t)}" tabindex="0"></i>'
        dot = STATUS_COLORS["good" if s.get("ok") else "critical"]
        state = f'{s.get("latency_ms", "?")}ms' if s.get("ok") else "FAILED"
        rows += f"""<div class="comp">
  <div class="comp-head"><i class="dot" style="background:{dot}"></i>
    <span class="comp-name">{esc(label)}</span>
    <span class="mono muted small">{esc(domain)}</span>
    <span class="comp-state">{esc(state)} · {uptime:.1f}% uptime</span></div>
  <div class="strip">{ticks}</div>
</div>"""

    incidents = [h for h in reversed(hist)
                 if h.get("failed_sources") or h.get("anomaly_level") not in (None, "ok")][:12]
    inc_html = ""
    for h in incidents:
        when = (h.get("ts") or "")[:16].replace("T", " ") + " UTC"
        what = []
        if h.get("failed_sources"):
            what.append("source outage: " + ", ".join(h["failed_sources"]))
        if h.get("anomaly_level") not in (None, "ok"):
            what.append(f'network signal ({h["anomaly_level"]}): '
                        + (", ".join((h.get("levels") or {}).keys()) or "anomaly"))
        lv = "critical" if h.get("failed_sources") else h.get("anomaly_level", "warning")
        inc_html += (f'<div class="signal"><span class="sig-icon" '
                     f'style="color:{STATUS_COLORS.get(lv, "#fab219")}">▲</span>'
                     f'<span class="muted small">{esc(when)}</span>'
                     f'<span>{esc("; ".join(what))}</span></div>')
    if not inc_html:
        inc_html = '<p class="muted">No incidents recorded in the current history window.</p>'

    page = f"""<!doctype html>
<html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Solbeat Status</title>
<meta name="description" content="Live status of Solbeat's data sources and the Solana network — uptime history, incidents, RSS subscription.">
<link rel="alternate" type="application/rss+xml" title="Solbeat status feed" href="status.xml">
<link rel="icon" href='{FAVICON}'>
<style>
:root {{ --page:#0d0d0d; --surface:#1a1a19; --border:rgba(255,255,255,.10);
  --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --grid:#2c2c2a; --accent:#3987e5; }}
* {{ box-sizing:border-box; margin:0; padding:0; }}
body {{ background:var(--page); color:var(--ink2);
  font:15px/1.55 system-ui,-apple-system,"Segoe UI",sans-serif; padding:20px; }}
.wrap {{ max-width:880px; margin:0 auto; display:flex; flex-direction:column; gap:14px; }}
a {{ color:var(--accent); }}
.card {{ background:var(--surface); border:1px solid var(--border);
  border-radius:10px; padding:18px 22px; }}
.top {{ display:flex; align-items:center; gap:12px; flex-wrap:wrap; }}
.wordmark {{ font-family:ui-monospace,Menlo,monospace; font-size:20px;
  font-weight:700; color:var(--ink); }}
.wordmark b {{ color:var(--accent); }}
.crumb {{ color:var(--muted); font-size:13px; }}
.backlink {{ margin-left:auto; font-size:13px; }}
.banner {{ border-radius:10px; padding:18px 22px; font-size:17px; font-weight:700;
  color:#0d0d0d; background:{banner_col}; }}
h2 {{ color:var(--ink); font-size:15px; margin-bottom:12px; }}
.comp {{ padding:10px 0; border-bottom:1px solid var(--border); }}
.comp:last-child {{ border-bottom:none; }}
.comp-head {{ display:flex; align-items:center; gap:9px; margin-bottom:6px; }}
.comp-name {{ color:var(--ink); font-size:13.5px; font-weight:600; }}
.comp-state {{ margin-left:auto; font-size:12px; color:var(--muted);
  font-variant-numeric:tabular-nums; }}
.dot {{ width:8px; height:8px; border-radius:50%; display:inline-block; flex-shrink:0; }}
.mono {{ font-family:ui-monospace,Menlo,monospace; }}
.small {{ font-size:11.5px; }} .muted {{ color:var(--muted); }}
.strip {{ display:flex; gap:2px; }}
.strip i {{ height:14px; border-radius:2px; flex:1 1 2px; min-width:0; cursor:pointer; }}
.signal {{ display:flex; gap:10px; align-items:baseline; padding:7px 0;
  border-bottom:1px solid var(--border); font-size:13.5px; }}
.signal:last-child {{ border-bottom:none; }}
#tickpop {{ position:absolute; z-index:50; background:#232322;
  border:1px solid rgba(255,255,255,.16); border-radius:8px; padding:8px 12px;
  font-size:12.5px; color:var(--ink); box-shadow:0 6px 24px rgba(0,0,0,.5);
  max-width:280px; pointer-events:none; display:none; }}
footer {{ text-align:center; color:var(--muted); font-size:12px; padding:8px 0 18px; }}
</style></head>
<body><div class="wrap">
<header class="top card">
  <span class="wordmark">SOL<b>BEAT</b></span><span class="crumb">/ status</span>
  <a class="backlink" href="https://www.solbeat.xyz">← dashboard</a>
</header>
<div class="banner">{banner_txt}</div>
<section class="card">
  <h2>Components — last {len(recent)} refresh cycles</h2>
  {rows}
</section>
<section class="card">
  <h2>Incident history</h2>
  {inc_html}
</section>
<section class="card">
  <h2>Subscribe to updates</h2>
  <p style="margin-bottom:8px">Solbeat runs serverless, so subscriptions are
  serverless too:</p>
  <p style="margin-bottom:6px">📡 <a href="status.xml">RSS feed</a> — updated
  every refresh; add it to any RSS reader or a Slack/Discord RSS bot.</p>
  <p style="margin-bottom:6px">📬 Email — <a
  href="https://github.com/andreolf/solbeat">watch the GitHub repository</a>
  (Watch → Custom → Issues): incident issues notify you through GitHub's own
  email delivery.</p>
  <p class="muted small">For the Solana network's official status, see
  <a href="https://status.solana.com">status.solana.com</a> (currently:
  {esc(stp.get('statuspage_description') or 'n/a')}). This page tracks
  Solbeat's own data pipeline.</p>
</section>
<footer>Solbeat status · generated {esc(gen)} · refreshes every 30 min</footer>
</div>
<script>
const pop = document.createElement('div'); pop.id = 'tickpop';
document.body.appendChild(pop);
document.addEventListener('pointerover', e => {{
  const t = e.target.closest('.strip i'); if (!t) return;
  pop.textContent = t.getAttribute('data-tip'); pop.style.display = 'block';
  const r = t.getBoundingClientRect();
  pop.style.left = Math.max(6, r.left + scrollX - 60) + 'px';
  pop.style.top = (r.top + scrollY - pop.offsetHeight - 10) + 'px';
}});
document.addEventListener('pointerout', e => {{
  if (e.target.closest('.strip i')) pop.style.display = 'none'; }});
</script>
</body></html>"""
    Path("docs/status.html").write_text(page)

    # RSS feed of incidents (+ a heartbeat item so the feed is never empty).
    def rfc822(ts):
        try:
            return datetime.strptime(ts, "%Y-%m-%dT%H:%M:%SZ").strftime(
                "%a, %d %b %Y %H:%M:%S GMT")
        except ValueError:
            return ts
    items = ""
    for h in incidents[:20]:
        what = []
        if h.get("failed_sources"):
            what.append("Source outage: " + ", ".join(h["failed_sources"]))
        if h.get("anomaly_level") not in (None, "ok"):
            what.append(f'Network signal ({h.get("anomaly_level")}): '
                        + (", ".join((h.get("levels") or {}).keys()) or "anomaly"))
        items += (f"<item><title>{esc('; '.join(what))}</title>"
                  f"<pubDate>{rfc822(h.get('ts', ''))}</pubDate>"
                  f"<guid isPermaLink=\"false\">{esc(h.get('ts', ''))}</guid>"
                  f"<link>{BASE_URL}status.html</link></item>")
    items += (f"<item><title>{esc(banner_txt)}</title>"
              f"<pubDate>{rfc822(gen)}</pubDate>"
              f"<guid isPermaLink=\"false\">status-{esc(gen)}</guid>"
              f"<link>{BASE_URL}status.html</link></item>")
    Path("docs/status.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?><rss version="2.0"><channel>'
        f"<title>Solbeat Status</title><link>{BASE_URL}status.html</link>"
        "<description>Status of Solbeat's data pipeline and Solana network "
        f"signals</description><lastBuildDate>{rfc822(gen)}</lastBuildDate>"
        f"{items}</channel></rss>")


def _write_pulse(snap, sentiment_html, upgrades_html):
    """Second page: sentiment + the Almanac (news, upgrades, commentary) —
    editorial content split off so the main dashboard stays technical."""
    gen = snap.get("generated_at", "")
    page = f"""<!doctype html>
<html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Solbeat Pulse — Solana Sentiment &amp; Almanac</title>
<meta name="description" content="Solana sentiment composite (Fear &amp; Greed, community votes, momentum, headline tone), ecosystem news and upgrade tracking — Alpenglow, SIMD-525.">
<link rel="canonical" href="{BASE_URL}pulse.html">
<link rel="icon" href='{FAVICON}'>
<style>
:root {{ --page:#0d0d0d; --surface:#1a1a19; --border:rgba(255,255,255,.10);
  --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --grid:#2c2c2a;
  --accent:#3987e5; --meter-track:rgba(57,135,229,.16);
  --d-up:#0ca30c; --d-down:#e66767; }}
* {{ box-sizing:border-box; margin:0; padding:0;
  scrollbar-width:thin; scrollbar-color:var(--grid) transparent; }}
body {{ background:var(--page); color:var(--ink2);
  font:15px/1.55 system-ui,-apple-system,"Segoe UI",sans-serif; padding:20px; }}
.wrap {{ max-width:1160px; margin:0 auto; display:flex; flex-direction:column; gap:14px; }}
a {{ color:var(--accent); }}
.card {{ background:var(--surface); border:1px solid var(--border);
  border-radius:10px; padding:18px 20px; overflow-x:auto; }}
.top {{ display:flex; align-items:center; gap:12px; flex-wrap:wrap; }}
.wordmark {{ font-family:ui-monospace,Menlo,monospace; font-size:20px;
  font-weight:700; color:var(--ink); text-decoration:none; }}
.wordmark b {{ color:var(--accent); }}
.crumb {{ color:var(--muted); font-size:13px; }}
.toplinks {{ margin-left:auto; display:flex; gap:14px; font-size:13px; }}
.section-head {{ display:flex; align-items:baseline; gap:10px;
  margin-bottom:12px; flex-wrap:wrap; }}
.section-head h2 {{ font-size:15px; color:var(--ink); font-weight:650; }}
.twocol {{ display:grid; grid-template-columns:1fr 1fr; gap:14px; }}
@media (max-width:820px) {{ .twocol {{ grid-template-columns:1fr; }} }}
.prov {{ display:inline-flex; align-items:center; gap:5px; font-size:10.5px;
  color:var(--muted); border:1px solid var(--border); border-radius:20px;
  padding:2px 8px; white-space:nowrap; }}
.prov i, .dot {{ width:6px; height:6px; border-radius:50%; display:inline-block; }}
.pulse-score {{ display:flex; align-items:baseline; gap:12px; }}
.pulse-num {{ font-size:44px; font-weight:650; color:var(--ink); }}
.pulse-label {{ font-size:17px; font-weight:650; color:var(--ink); }}
.meter {{ background:var(--meter-track); border-radius:5px; height:10px; margin:8px 0 6px; }}
.meter-fill {{ height:10px; border-radius:5px; background:var(--accent); }}
.prow {{ display:flex; align-items:center; gap:10px; margin:8px 0; }}
.prow-label {{ width:120px; font-size:13px; flex-shrink:0; }}
.prow-track {{ flex:1; background:var(--grid); border-radius:3px; height:8px; }}
.prow-bar {{ background:var(--accent); height:8px; border-radius:3px; }}
.prow-val {{ width:110px; text-align:right; font-size:12.5px; color:var(--ink);
  font-variant-numeric:tabular-nums; flex-shrink:0; }}
.newsrow {{ padding:6px 0; border-bottom:1px solid var(--border); font-size:14px; }}
.newsrow:last-child {{ border-bottom:none; }}
.tile-label {{ font-size:11px; letter-spacing:1px; color:var(--muted);
  text-transform:uppercase; }}
.commentary {{ font-size:14.5px; color:var(--ink2);
  border-left:3px solid var(--accent); padding-left:14px; margin-bottom:16px; }}
.upgrid {{ display:grid; grid-template-columns:repeat(auto-fill,minmax(250px,1fr)); gap:14px; }}
.upcard {{ border:1px solid var(--border); border-radius:8px; padding:12px 14px; }}
.up-name {{ font-size:13px; font-weight:650; color:var(--ink); }}
.up-status {{ font-size:13px; color:var(--accent); font-weight:600;
  margin:4px 0 6px; display:flex; align-items:center; gap:7px; }}
@keyframes beat {{ 0%,100% {{ transform:scale(1); opacity:1; }}
  50% {{ transform:scale(1.35); opacity:.7; }} }}
.live-dot {{ width:8px; height:8px; border-radius:50%; background:#0ca30c;
  display:inline-block; animation:beat 1.6s infinite; }}
.sv-line {{ stroke:var(--accent); }} .sv-fill {{ fill:var(--accent); opacity:.1; }}
.sv-dot {{ fill:var(--accent); stroke:var(--surface); stroke-width:2; }}
.d-up {{ color:var(--d-up); }} .d-down {{ color:var(--d-down); }}
.muted {{ color:var(--muted); }} .small {{ font-size:12px; }}
b, h2 {{ color:var(--ink); }}
.pl-wide {{ width:220px; }}
footer {{ text-align:center; color:var(--muted); font-size:12px; padding:8px 0 18px; }}
@media (max-width:600px) {{
  body {{ padding:10px; }}
  .card {{ padding:14px; }}
  .pulse-num {{ font-size:34px; }}
  .pl-wide {{ width:128px; font-size:12px; }}
  .prow-label {{ width:100px; font-size:12px; }}
  .prow-val {{ width:64px; font-size:11px; }}
  .newsrow {{ font-size:13px; overflow-wrap:anywhere; }}
}}
</style></head>
<body><div class="wrap">
<header class="top card">
  {LOGO_SVG}
  <a class="wordmark" href="./">SOL<b>BEAT</b></a>
  <span class="crumb">/ pulse &amp; almanac</span>
  <div class="toplinks">
    <a href="./">Dashboard</a>
    <a href="https://docs.solbeat.xyz">Docs</a>
    <a href="status.html">Status</a>
  </div>
</header>
{sentiment_html}
{upgrades_html}
<footer>Solbeat Pulse · generated {esc(gen)} · refreshes every 30 min ·
  sentiment is an experimental heuristic, not financial advice</footer>
</div></body></html>"""
    Path("docs/pulse.html").write_text(page)


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
- [Documentation](https://docs.solbeat.xyz): architecture, per-source
  collection details, glossary of every metric, FAQ.
- [Status page]({BASE_URL}status.html) + [RSS]({BASE_URL}status.xml):
  per-source uptime and incidents.

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
        for p in ("", "pulse.html", "docs.html", "status.html",
                  "data.json", "report.md", "llms.txt"))
    Path("docs/sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
        f"{urls}</urlset>")
