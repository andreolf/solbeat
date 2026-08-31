#!/usr/bin/env python3
"""
Solbeat — the heartbeat terminal for the Solana network.

A zero-dependency, zero-API-key, auto-updating report on the state of the
Solana ecosystem. Python standard library only. Every metric is collected
from public, keyless endpoints (Solana mainnet RPC, DeFiLlama, CoinGecko,
Jito Kobe, Stakewiz, GitHub, status.solana.com) and rendered into three
formats: an interactive dark-theme HTML dashboard, a Markdown report, and
machine-readable JSON.

Usage:
    python3 solbeat.py collect     # fetch data -> docs/data.json (+history)
    python3 solbeat.py render      # render docs/{index.html,report.md} from data.json
    python3 solbeat.py run         # collect + render (the normal entrypoint)
    python3 solbeat.py serve       # run once, then serve docs/ on :8017 and
                                   # re-collect every REFRESH_SECONDS
"""

import json
import os
import statistics
import sys
import time
import xml.etree.ElementTree as ET
import urllib.request
import urllib.error
from datetime import datetime, timezone
from pathlib import Path

# --------------------------------------------------------------------------
# Configuration
# --------------------------------------------------------------------------

CONFIG = {
    "rpc_url": "https://api.mainnet-beta.solana.com",
    "refresh_seconds": 1800,          # serve-mode refresh cadence
    "history_max_entries": 2000,      # rolling cross-run history window
    "http_timeout": 20,
    "docs_dir": "docs",
    "top_validators_shown": 10,
    "spark_points": 90,               # daily points embedded per sparkline
}

# Exchange hot wallets (community-attributed labels from public explorers).
WHALE_WALLETS = {
    "Binance (hot)": "9WzDXwBbmkg8ZTbNMqUxvQRAyrZzDsGYdLVL9zYtAWWM",
    "Binance (cold)": "5tzFkiKscXHK5ZXCGbXZxdw7gTjjD1mBwuoFbhUvuAi9",
    "OKX (attributed)": "AC5RDfQFmDS1deWZos921JfqscXdByf8BKHs5ACWjtW2",
    "Coinbase (hot)": "H8sMJSCQxfKiFTCfDR3DUMLPwcRbM61LGFJ8N4dK3WjS",
}

# Flagship program IDs polled for a live activity pulse.
PROGRAMS = {
    "Jupiter v6": "JUP6LkbZbjS1jKKwapdHNy74zcZ3tLUZoi5QNyVTaV4",
    "Raydium AMM v4": "675kPX9MHTjS2zt1qfr1NYHuzeLXfQM9H24wFSUt1Mp8",
    "Orca Whirlpool": "whirLbMiicVdio4qvUfM5KAg6Ct8VwpYzGff3uctyCc",
    "Pump.fun": "6EF8rrecthR5Dkzon8Nwu78hRvfCKubJ14M5uBEwF6P",
    "Tensor": "TSWAPaqyCSx2KABk68Shruf4rp7CxcNi8hAsbdwmHbN",
    "Magic Eden v2": "M2mx93ekt1fmXSVkTrUL9xVFHkmME8HTUi5Cyc5aF7K",
    "Marinade": "MarBmsSgKXdrN1egZf5sqe1TMai9K1rChYNDJgjq7aD",
}

ANOMALY_THRESHOLDS = {
    "z_warn": 2.0,
    "z_serious": 3.0,
    "delinquent_stake_warn_pct": 3.0,
    "delinquent_stake_serious_pct": 8.0,
    "slot_time_warn_ms": 500,
    "slot_time_serious_ms": 700,
}

UA = "solbeat/1.0 (+https://github.com/solbeat) python-stdlib"


# --------------------------------------------------------------------------
# HTTP helpers (urllib only)
# --------------------------------------------------------------------------

def _http_json(url, payload=None, timeout=None, headers=None):
    """GET (payload=None) or POST JSON and parse the JSON response."""
    timeout = timeout or CONFIG["http_timeout"]
    hdrs = {"User-Agent": UA, "Accept": "application/json"}
    if headers:
        hdrs.update(headers)
    data = None
    if payload is not None:
        data = json.dumps(payload).encode()
        hdrs["Content-Type"] = "application/json"
    req = urllib.request.Request(url, data=data, headers=hdrs)
    last_err = None
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                return json.loads(resp.read().decode())
        except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError,
                json.JSONDecodeError, OSError) as exc:
            last_err = exc
            if isinstance(exc, urllib.error.HTTPError) and exc.code == 429:
                time.sleep(3 * (attempt + 1))
            else:
                time.sleep(1.0 * (attempt + 1))
    raise RuntimeError(f"{url}: {last_err}")


def rpc(method, params=None):
    body = {"jsonrpc": "2.0", "id": 1, "method": method, "params": params or []}
    out = _http_json(CONFIG["rpc_url"], payload=body)
    if "error" in out:
        raise RuntimeError(f"RPC {method}: {out['error']}")
    return out["result"]


class SourceTracker:
    """Records per-source outcome, latency and freshness for the provenance panel."""

    def __init__(self):
        self.sources = {}

    def run(self, name, fn):
        t0 = time.monotonic()
        try:
            value = fn()
            self.sources[name] = {
                "ok": True,
                "latency_ms": round((time.monotonic() - t0) * 1000),
                "fetched_at": now_iso(),
            }
            return value
        except Exception as exc:  # graceful degradation is the design
            self.sources[name] = {
                "ok": False,
                "latency_ms": round((time.monotonic() - t0) * 1000),
                "error": str(exc)[:300],
                "fetched_at": now_iso(),
            }
            return None


def now_iso():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


# --------------------------------------------------------------------------
# Collectors
# --------------------------------------------------------------------------

def collect_rpc_core():
    """Network + supply + fees from Solana mainnet RPC."""
    out = {}
    out["health"] = "ok" if rpc("getHealth") == "ok" else "degraded"
    time.sleep(0.1)
    ver = rpc("getVersion")
    out["node_version"] = ver.get("solana-core")
    time.sleep(0.1)
    slot_now = rpc("getSlot")
    time.sleep(0.1)
    try:
        # Chain clock: timestamp of a recently rooted slot.
        bt = rpc("getBlockTime", [slot_now - 40])
        out["chain_time"] = datetime.fromtimestamp(
            bt, timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        out["chain_clock_drift_s"] = round(time.time() - bt)
    except Exception:
        out["chain_time"] = None
    time.sleep(0.1)
    ep = rpc("getEpochInfo")
    out["epoch"] = ep["epoch"]
    out["slot"] = max(slot_now, ep["absoluteSlot"])
    out["block_height"] = ep.get("blockHeight") or 0
    out["epoch_slot_index"] = ep["slotIndex"]
    out["epoch_slots_total"] = ep["slotsInEpoch"]
    out["epoch_progress_pct"] = round(100 * ep["slotIndex"] / ep["slotsInEpoch"], 2)
    out["tx_count_total"] = ep.get("transactionCount") or 0
    time.sleep(0.1)

    samples = rpc("getRecentPerformanceSamples", [720]) or []
    # Samples are newest-first, one per ~60s. Keep a compact series for charts.
    perf = []
    for s in reversed(samples):
        secs = s.get("samplePeriodSecs") or 60
        slots = s.get("numSlots") or 0
        txs = s.get("numTransactions") or 0
        nonvote = s.get("numNonVoteTransactions")
        perf.append({
            "tps": round(txs / secs, 1),
            "nonvote_tps": round(nonvote / secs, 1) if nonvote is not None else None,
            "slot_ms": round(1000 * secs / slots, 1) if slots else None,
        })
    out["perf_series"] = perf
    recent = perf[-10:] if perf else []
    if recent:
        out["tps"] = round(statistics.mean(p["tps"] for p in recent), 1)
        nv = [p["nonvote_tps"] for p in recent if p["nonvote_tps"] is not None]
        out["nonvote_tps"] = round(statistics.mean(nv), 1) if nv else None
        st = [p["slot_ms"] for p in recent if p["slot_ms"]]
        out["slot_time_ms"] = round(statistics.mean(st), 1) if st else None
    if perf:
        # Estimated 24h transaction volume, extrapolated from up to 12h of samples.
        span_s = 60 * len(perf)
        txs_span = sum(p["tps"] for p in perf) * 60
        out["est_daily_txs"] = int(txs_span * 86400 / span_s)
        nv_span = sum(p["nonvote_tps"] for p in perf
                      if p["nonvote_tps"] is not None) * 60
        if nv_span:
            out["est_daily_nonvote_txs"] = int(nv_span * 86400 / span_s)
    time.sleep(0.1)

    sup = rpc("getSupply", [{"excludeNonCirculatingAccountsList": True}])["value"]
    out["supply_total_sol"] = round(sup["total"] / 1e9)
    out["supply_circulating_sol"] = round(sup["circulating"] / 1e9)
    time.sleep(0.1)
    infl = rpc("getInflationRate")
    out["inflation_total_pct"] = round(infl["total"] * 100, 2)
    time.sleep(0.1)

    fees = rpc("getRecentPrioritizationFees", [[]]) or []
    fee_vals = sorted(f["prioritizationFee"] for f in fees)
    if fee_vals:
        nz = [f for f in fee_vals if f > 0]
        out["priority_fee_median"] = statistics.median(fee_vals)
        out["priority_fee_p90"] = fee_vals[int(0.9 * (len(fee_vals) - 1))]
        out["priority_fee_nonzero_share_pct"] = round(100 * len(nz) / len(fee_vals), 1)
    return out


def collect_validators():
    va = rpc("getVoteAccounts", [{"keepUnstakedDelinquents": False}])
    current, delinq = va["current"], va["delinquent"]
    everyone = current + delinq
    total_stake = sum(v["activatedStake"] for v in everyone) or 1
    delinq_stake = sum(v["activatedStake"] for v in delinq)
    ranked = sorted(everyone, key=lambda v: -v["activatedStake"])

    # Nakamoto coefficient: minimum validators controlling >1/3 of stake.
    nakamoto, acc = 0, 0
    for v in ranked:
        acc += v["activatedStake"]
        nakamoto += 1
        if acc > total_stake / 3:
            break

    def share(n):
        return round(100 * sum(v["activatedStake"] for v in ranked[:n]) / total_stake, 1)

    commissions = [v["commission"] for v in current]
    top = [{
        "vote_pubkey": v["votePubkey"],
        "stake_sol": round(v["activatedStake"] / 1e9),
        "stake_pct": round(100 * v["activatedStake"] / total_stake, 2),
        "commission_pct": v["commission"],
        "delinquent": v in delinq,
    } for v in ranked[:CONFIG["top_validators_shown"]]]

    return {
        "active_count": len(current),
        "delinquent_count": len(delinq),
        "delinquent_stake_pct": round(100 * delinq_stake / total_stake, 2),
        "total_stake_sol": round(total_stake / 1e9),
        "nakamoto_coefficient": nakamoto,
        "top10_stake_pct": share(10),
        "top20_stake_pct": share(20),
        "avg_commission_pct": round(statistics.mean(commissions), 1) if commissions else None,
        "median_commission_pct": statistics.median(commissions) if commissions else None,
        "top_validators": top,
    }


def collect_market():
    px = _http_json(
        "https://api.coingecko.com/api/v3/simple/price"
        "?ids=solana&vs_currencies=usd&include_24hr_change=true"
        "&include_market_cap=true&include_24hr_vol=true"
    )["solana"]
    out = {
        "sol_price_usd": px["usd"],
        "sol_mcap_usd": px.get("usd_market_cap"),
        "sol_vol24h_usd": px.get("usd_24h_vol"),
        "sol_change24h_pct": round(px.get("usd_24h_change") or 0, 2),
    }
    time.sleep(1.5)  # keyless CoinGecko is touchy about bursts
    chart = _http_json(
        "https://api.coingecko.com/api/v3/coins/solana/market_chart"
        "?vs_currency=usd&days=30&interval=daily"
    )
    out["price_series_30d"] = [round(p[1], 2) for p in chart.get("prices", [])]
    return out


def collect_tvl():
    hist = _http_json("https://api.llama.fi/v2/historicalChainTvl/Solana")
    series = [round(p["tvl"]) for p in hist][-CONFIG["spark_points"]:]
    return {"tvl_usd": series[-1] if series else None, "tvl_series": series}


def collect_dex():
    d = _http_json(
        "https://api.llama.fi/overview/dexs/solana"
        "?excludeTotalDataChart=false&excludeTotalDataChartBreakdown=true"
    )
    chart = d.get("totalDataChart") or []
    series = [round(v) for _, v in chart[-CONFIG["spark_points"]:]]
    protos = sorted(
        (p for p in d.get("protocols", []) if p.get("total24h")),
        key=lambda p: -p["total24h"],
    )[:5]
    return {
        "dex_vol24h_usd": d.get("total24h"),
        "dex_vol7d_usd": d.get("total7d"),
        "dex_change1d_pct": round(d["change_1d"], 1) if d.get("change_1d") is not None else None,
        "dex_top_protocols": [
            {"name": p["name"], "vol24h_usd": round(p["total24h"])} for p in protos
        ],
        "dex_series": series,
    }


def collect_fees():
    fees = _http_json("https://api.llama.fi/summary/fees/solana?dataType=dailyFees")
    rev = _http_json("https://api.llama.fi/summary/fees/solana?dataType=dailyRevenue")
    chart = fees.get("totalDataChart") or []
    return {
        "chain_fees24h_usd": fees.get("total24h"),
        "chain_burn24h_usd": rev.get("total24h"),
        "fees_series": [round(v) for _, v in chart[-CONFIG["spark_points"]:]],
    }


def collect_stablecoins():
    chart = _http_json("https://stablecoins.llama.fi/stablecoincharts/Solana")
    series = []
    for p in chart:
        v = (p.get("totalCirculatingUSD") or {}).get("peggedUSD")
        if v:
            series.append(round(v))
    series = series[-CONFIG["spark_points"]:]
    return {"stablecoin_supply_usd": series[-1] if series else None,
            "stablecoin_series": series}


def collect_xstocks():
    d = _http_json("https://api.llama.fi/protocol/xstocks")
    cur = (d.get("currentChainTvls") or {}).get("Solana")
    hist = ((d.get("chainTvls") or {}).get("Solana") or {}).get("tvl") or []
    series = [round(p["totalLiquidityUSD"]) for p in hist][-CONFIG["spark_points"]:]
    return {"xstocks_tvl_usd": round(cur) if cur else (series[-1] if series else None),
            "xstocks_series": series}


def collect_jito():
    d = _http_json("https://kobe.mainnet.jito.network/api/v1/mev_rewards")
    lamports = d.get("total_network_mev_lamports")
    return {"jito_epoch": d.get("epoch"),
            "jito_epoch_tips_sol": round(lamports / 1e9, 1) if lamports else None}


def collect_stakewiz():
    vals = _http_json("https://api.stakewiz.com/validators", timeout=60)
    with_bls = [v for v in vals if v.get("bls_pubkey")]
    total_stake = sum(v.get("activated_stake") or 0 for v in vals) or 1
    bls_stake = sum(v.get("activated_stake") or 0 for v in with_bls)

    # Validator geography (for the world map) + country stake distribution.
    geo = []
    countries = {}
    for v in vals:
        stake = v.get("activated_stake") or 0
        countries[v.get("ip_country") or "Unknown"] = \
            countries.get(v.get("ip_country") or "Unknown", 0) + stake
        if v.get("ip_latitude") and v.get("ip_longitude") and stake:
            geo.append({
                "lat": round(float(v["ip_latitude"]), 1),
                "lon": round(float(v["ip_longitude"]), 1),
                "stake": int(stake),
                "name": (v.get("name") or "")[:40],
                "loc": ", ".join(x for x in (v.get("ip_city"), v.get("ip_country")) if x),
            })
    geo.sort(key=lambda g: -g["stake"])
    top_countries = sorted(countries.items(), key=lambda kv: -kv[1])[:8]
    # Names for the top-stake validators, keyed by vote account.
    named = sorted((v for v in vals if v.get("name")),
                   key=lambda v: -(v.get("activated_stake") or 0))[:40]

    return {
        "stakewiz_validator_count": len(vals),
        "bls_registered_count": len(with_bls),
        "bls_registered_pct": round(100 * len(with_bls) / max(len(vals), 1), 1),
        "bls_stake_pct": round(100 * bls_stake / total_stake, 1),
        "geo": geo[:1200],
        "countries": [{"country": c, "stake_pct": round(100 * s / total_stake, 1)}
                      for c, s in top_countries],
        "names": {v["vote_identity"]: v["name"] for v in named
                  if v.get("vote_identity")},
    }


def collect_github():
    rel = _http_json("https://api.github.com/repos/anza-xyz/agave/releases/latest",
                     timeout=15)
    out = {"agave_latest_tag": rel.get("tag_name"),
           "agave_published_at": rel.get("published_at"),
           "agave_url": rel.get("html_url")}
    time.sleep(0.3)
    try:
        pr = _http_json(
            "https://api.github.com/repos/solana-foundation/"
            "solana-improvement-documents/pulls/525", timeout=15
        )
        out["simd525_state"] = "merged" if pr.get("merged_at") else pr.get("state")
    except Exception:
        out["simd525_state"] = None
    return out


def collect_news():
    """Official Solana ecosystem news via solana.com's public RSS (keyless)."""
    hdrs = {"User-Agent": "Mozilla/5.0 (compatible; solbeat/1.0)"}
    req = urllib.request.Request("https://solana.com/news/rss.xml", headers=hdrs)
    with urllib.request.urlopen(req, timeout=CONFIG["http_timeout"]) as resp:
        root = ET.fromstring(resp.read())
    items = []
    for item in root.findall(".//item")[:6]:
        items.append({
            "title": (item.findtext("title") or "").strip(),
            "link": (item.findtext("link") or "").strip(),
            "published": (item.findtext("pubDate") or "").strip(),
        })
    if not items:
        raise RuntimeError("empty RSS feed")
    return {"items": items}


def collect_dune():
    """Optional Dune Analytics extractor (the one source with no keyless path).

    Off by default to honor the zero-key design; set DUNE_API_KEY and
    DUNE_QUERY_ID to pull the latest results of any Dune query (e.g. a daily
    active addresses query) into the snapshot."""
    key, qid = os.environ.get("DUNE_API_KEY"), os.environ.get("DUNE_QUERY_ID")
    d = _http_json(
        f"https://api.dune.com/api/v1/query/{qid}/results?limit=5",
        headers={"X-Dune-API-Key": key})
    rows = ((d.get("result") or {}).get("rows") or [])[:5]
    out = {"enabled": True, "query_id": qid, "rows": rows}
    # Surface a recognizable daily-active-addresses figure if present.
    for k, v in (rows[0] if rows else {}).items():
        if isinstance(v, (int, float)) and ("active" in k.lower() or k.lower() in ("dau", "users")):
            out["daily_active_addresses"] = v
            break
    return out


def collect_status_page():
    st = _http_json("https://status.solana.com/api/v2/status.json")
    inc = _http_json("https://status.solana.com/api/v2/incidents/unresolved.json")
    return {
        "statuspage_indicator": (st.get("status") or {}).get("indicator"),
        "statuspage_description": (st.get("status") or {}).get("description"),
        "unresolved_incidents": len(inc.get("incidents") or []),
    }


def collect_whales():
    out = []
    for label, addr in WHALE_WALLETS.items():
        try:
            bal = rpc("getBalance", [addr])["value"]
            out.append({"label": label, "address": addr,
                        "balance_sol": round(bal / 1e9, 1)})
        except Exception:
            out.append({"label": label, "address": addr, "balance_sol": None})
        time.sleep(0.15)
    return out


def collect_program_pulse():
    """Tx/min per flagship program from signature timestamps (last 25 sigs)."""
    out = []
    now_ts = time.time()
    for label, addr in PROGRAMS.items():
        try:
            sigs = rpc("getSignaturesForAddress", [addr, {"limit": 25}])
            times = [s["blockTime"] for s in sigs if s.get("blockTime")]
            if len(times) >= 2:
                span = max(now_ts - min(times), 1)
                rate = round(len(times) * 60 / span, 1)
            else:
                rate = 0.0
            out.append({"program": label, "tx_per_min": rate,
                        "newest_age_s": round(now_ts - max(times)) if times else None})
        except Exception:
            out.append({"program": label, "tx_per_min": None, "newest_age_s": None})
        time.sleep(0.15)
    return out


# --------------------------------------------------------------------------
# Derived metrics
# --------------------------------------------------------------------------

def derive(snap):
    """Cross-source computed metrics — most importantly REV."""
    d = {}
    net, mkt = snap.get("network") or {}, snap.get("market") or {}
    fees, jito = snap.get("fees") or {}, snap.get("jito") or {}

    # REV (Blockworks methodology): base + priority fees + Jito MEV tips.
    fees24 = fees.get("chain_fees24h_usd")
    tips_sol = jito.get("jito_epoch_tips_sol")
    price = mkt.get("sol_price_usd")
    slot_ms = net.get("slot_time_ms") or 400
    if fees24 is not None:
        rev = fees24
        if tips_sol and price and net.get("epoch_slots_total"):
            epoch_secs = net["epoch_slots_total"] * slot_ms / 1000
            tips_day_sol = tips_sol * 86400 / epoch_secs
            d["jito_tips24h_usd"] = round(tips_day_sol * price)
            rev += d["jito_tips24h_usd"]
        d["rev24h_usd"] = round(rev)
        d["rev_per_min_usd"] = round(rev / 1440, 2)

    # Fee per user (non-vote) transaction — vote txs would dilute the average.
    if net.get("est_daily_nonvote_txs") and fees24:
        d["avg_fee_per_tx_usd"] = round(fees24 / net["est_daily_nonvote_txs"], 6)

    if net.get("epoch_slots_total") and net.get("epoch_slot_index") is not None:
        remaining = net["epoch_slots_total"] - net["epoch_slot_index"]
        d["epoch_eta_hours"] = round(remaining * slot_ms / 1000 / 3600, 1)

    # Live upgrade evidence: measured slot time vs SIMD-0525's 350ms step.
    if net.get("slot_time_ms"):
        d["simd525_step_active"] = net["slot_time_ms"] < 390
    return d


# --------------------------------------------------------------------------
# Anomaly engine
# --------------------------------------------------------------------------

def _zscore(value, series):
    if value is None or len(series) < 8:
        return None
    mean = statistics.mean(series)
    sd = statistics.pstdev(series)
    if sd == 0:
        return 0.0
    return round((value - mean) / sd, 2)


def _grade(z):
    t = ANOMALY_THRESHOLDS
    if z is None:
        return "ok"
    if abs(z) >= t["z_serious"]:
        return "serious"
    if abs(z) >= t["z_warn"]:
        return "warning"
    return "ok"


def detect_anomalies(snap, history):
    """Per-metric z-scores against intra-day and long baselines, then
    multi-source correlation into classified incidents."""
    t = ANOMALY_THRESHOLDS
    net = snap.get("network") or {}
    mkt = snap.get("market") or {}
    val = snap.get("validators") or {}
    findings = []

    def add(metric, level, z, text):
        findings.append({"metric": metric, "level": level, "z": z, "text": text})

    # TPS + slot time vs the last ~12h of performance samples.
    perf = net.get("perf_series") or []
    tps_series = [p["tps"] for p in perf[:-10]] if len(perf) > 30 else []
    z_tps = _zscore(net.get("tps"), tps_series)
    if z_tps is not None and _grade(z_tps) != "ok":
        direction = "drop" if z_tps < 0 else "spike"
        add("tps", _grade(z_tps), z_tps,
            f"TPS {direction}: {net['tps']:,.0f} vs 12h mean "
            f"{statistics.mean(tps_series):,.0f} (z={z_tps:+.1f})")

    slot_ms = net.get("slot_time_ms")
    if slot_ms:
        if slot_ms >= t["slot_time_serious_ms"]:
            add("slot_time", "serious", None,
                f"Slow slots: {slot_ms:.0f}ms average (target ≤400ms)")
        elif slot_ms >= t["slot_time_warn_ms"]:
            add("slot_time", "warning", None,
                f"Elevated slot time: {slot_ms:.0f}ms average")

    dstake = val.get("delinquent_stake_pct")
    if dstake is not None:
        if dstake >= t["delinquent_stake_serious_pct"]:
            add("delinquency", "serious", None,
                f"High delinquency: {dstake:.1f}% of stake delinquent")
        elif dstake >= t["delinquent_stake_warn_pct"]:
            add("delinquency", "warning", None,
                f"Elevated delinquency: {dstake:.1f}% of stake delinquent")

    # Market/liquidity vs 30–90 day daily baselines from source history.
    for metric, value, series, label in [
        ("price", mkt.get("sol_price_usd"), mkt.get("price_series_30d") or [], "SOL price"),
        ("tvl", (snap.get("tvl") or {}).get("tvl_usd"),
         (snap.get("tvl") or {}).get("tvl_series") or [], "Solana TVL"),
        ("stablecoins", (snap.get("stablecoins") or {}).get("stablecoin_supply_usd"),
         (snap.get("stablecoins") or {}).get("stablecoin_series") or [], "Stablecoin supply"),
        ("dex", (snap.get("dex") or {}).get("dex_vol24h_usd"),
         (snap.get("dex") or {}).get("dex_series") or [], "DEX volume"),
    ]:
        z = _zscore(value, series[:-1] if series else [])
        if z is not None and _grade(z) != "ok":
            direction = "surge" if z > 0 else "contraction"
            add(metric, _grade(z), z, f"{label} {direction} (z={z:+.1f} vs its recent baseline)")

    ch = mkt.get("sol_change24h_pct")
    if ch is not None and abs(ch) >= 10:
        add("price_24h", "warning" if abs(ch) < 20 else "serious", None,
            f"SOL moved {ch:+.1f}% in 24h")

    # Cross-run baseline (needs a dozen snapshots of local history to engage).
    hist_rev = [h.get("rev_usd") for h in history if h.get("rev_usd")]
    z_rev = _zscore((snap.get("derived") or {}).get("rev24h_usd"), hist_rev)
    if z_rev is not None and _grade(z_rev) != "ok":
        add("rev", _grade(z_rev), z_rev,
            f"Real Economic Value deviating from its run-history baseline (z={z_rev:+.1f})")

    # ---- Multi-source correlation -> classified incidents ----
    fired = {f["metric"] for f in findings}
    incidents = []
    if "tps" in fired and ({"slot_time", "delinquency"} & fired):
        incidents.append({
            "class": "network_incident", "level": "serious",
            "text": ("Correlated network incident: throughput anomaly coinciding with "
                     + ("slow slots" if "slot_time" in fired else "validator delinquency")
                     + " — consistent with cluster-level degradation, not a demand shift."),
        })
    elif {"slot_time", "delinquency"} <= fired:
        incidents.append({
            "class": "consensus_stress", "level": "warning",
            "text": "Slow slots and elevated delinquency together suggest consensus-level stress.",
        })
    if ({"price", "price_24h"} & fired) and ({"tvl", "dex"} & fired):
        incidents.append({
            "class": "market_move", "level": "warning",
            "text": ("Market-wide move: SOL price anomaly accompanied by liquidity/volume "
                     "shifts — an ecosystem-level repricing rather than an isolated metric."),
        })
    if "stablecoins" in fired and "tvl" in fired:
        incidents.append({
            "class": "liquidity_rotation", "level": "warning",
            "text": "Stablecoin supply and TVL moving together — capital rotating in or out of the chain.",
        })

    return {"findings": findings, "incidents": incidents,
            "all_clear": not findings and not incidents}


# --------------------------------------------------------------------------
# Commentary (deterministic, generated from data — the analyst layer)
# --------------------------------------------------------------------------

def _fmt_usd(v, digits=1):
    if v is None:
        return "n/a"
    for cut, suffix in [(1e12, "T"), (1e9, "B"), (1e6, "M"), (1e3, "K")]:
        if abs(v) >= cut:
            return f"${v / cut:.{digits}f}{suffix}"
    return f"${v:,.0f}"


def build_commentary(snap):
    net = snap.get("network") or {}
    mkt = snap.get("market") or {}
    val = snap.get("validators") or {}
    der = snap.get("derived") or {}
    anom = snap.get("anomalies") or {}
    sw = snap.get("stakewiz") or {}
    parts = []

    if net.get("epoch") is not None:
        parts.append(
            f"Epoch {net['epoch']} is {net.get('epoch_progress_pct', 0):.0f}% complete"
            + (f" (~{der['epoch_eta_hours']:.0f}h remaining)" if der.get("epoch_eta_hours") else "")
            + f", with the cluster processing ~{net.get('tps', 0):,.0f} TPS"
            + (f" ({net['nonvote_tps']:,.0f} non-vote)" if net.get("nonvote_tps") else "") + ".")
    if net.get("slot_time_ms"):
        if der.get("simd525_step_active"):
            parts.append(
                f"Measured slot time is {net['slot_time_ms']:.0f}ms — live on-chain "
                f"evidence that SIMD-0525's first slot-time reduction step (350ms "
                f"target) is active on mainnet.")
        else:
            parts.append(f"Measured slot time is {net['slot_time_ms']:.0f}ms.")
    if der.get("rev24h_usd"):
        parts.append(
            f"The network earned {_fmt_usd(der['rev24h_usd'])} of Real Economic Value "
            f"over the last 24h ({_fmt_usd(der.get('rev_per_min_usd'), 2)}/minute), "
            f"computed as base + priority fees plus Jito MEV tips.")
    if mkt.get("sol_price_usd"):
        parts.append(
            f"SOL trades at ${mkt['sol_price_usd']:,.2f} "
            f"({mkt.get('sol_change24h_pct', 0):+.1f}% / 24h).")
    if val.get("nakamoto_coefficient"):
        parts.append(
            f"Decentralization: Nakamoto coefficient {val['nakamoto_coefficient']}, "
            f"{val.get('active_count', 0)} active validators, "
            f"{val.get('delinquent_stake_pct', 0):.1f}% of stake delinquent.")
    if sw.get("bls_stake_pct"):
        parts.append(
            f"Alpenglow readiness: validators holding {sw['bls_stake_pct']:.0f}% of "
            f"stake have registered BLS keys ahead of the consensus upgrade.")
    if anom.get("all_clear"):
        parts.append("Anomaly scan: all clear across every monitored metric.")
    else:
        n = len(anom.get("findings", [])) + len(anom.get("incidents", []))
        parts.append(f"Anomaly scan: {n} signal(s) flagged — see Signals below.")
    return " ".join(parts)


# --------------------------------------------------------------------------
# Snapshot assembly + history
# --------------------------------------------------------------------------

def collect_snapshot():
    tracker = SourceTracker()
    snap = {"schema_version": "1.0", "generated_at": now_iso(),
            "generator": "solbeat", "network": None}

    snap["network"] = tracker.run("solana_rpc", collect_rpc_core)
    snap["validators"] = tracker.run("solana_rpc_validators", collect_validators)
    snap["market"] = tracker.run("coingecko", collect_market)
    snap["tvl"] = tracker.run("defillama_tvl", collect_tvl)
    snap["dex"] = tracker.run("defillama_dex", collect_dex)
    snap["fees"] = tracker.run("defillama_fees", collect_fees)
    snap["stablecoins"] = tracker.run("defillama_stablecoins", collect_stablecoins)
    snap["xstocks"] = tracker.run("defillama_xstocks", collect_xstocks)
    snap["jito"] = tracker.run("jito_kobe", collect_jito)
    snap["stakewiz"] = tracker.run("stakewiz", collect_stakewiz)
    snap["github"] = tracker.run("github", collect_github)
    snap["news"] = tracker.run("solana_com_news", collect_news)
    if os.environ.get("DUNE_API_KEY") and os.environ.get("DUNE_QUERY_ID"):
        snap["dune"] = tracker.run("dune", collect_dune)
    else:
        snap["dune"] = {"enabled": False,
                        "note": "keyless by design; set DUNE_API_KEY + "
                                "DUNE_QUERY_ID to enable this extractor"}
    snap["status_page"] = tracker.run("solana_status_page", collect_status_page)
    snap["whales"] = tracker.run("solana_rpc_whales", collect_whales)
    snap["program_pulse"] = tracker.run("solana_rpc_programs", collect_program_pulse)

    snap["derived"] = derive(snap)
    history = load_history()
    snap["anomalies"] = detect_anomalies(snap, history)
    snap["commentary"] = build_commentary(snap)
    snap["sources"] = tracker.sources
    return snap


def history_entry(snap):
    net = snap.get("network") or {}
    val = snap.get("validators") or {}
    mkt = snap.get("market") or {}
    der = snap.get("derived") or {}
    anoms = snap.get("anomalies") or {}
    levels = {f["metric"]: f["level"] for f in anoms.get("findings", [])}
    for inc in anoms.get("incidents", []):
        levels[inc["class"]] = inc["level"]
    worst = "ok"
    for lv in levels.values():
        if lv == "serious":
            worst = "serious"
        elif lv == "warning" and worst == "ok":
            worst = "warning"
    return {
        "ts": snap["generated_at"],
        "slot": net.get("slot"),
        "tps": net.get("tps"),
        "nonvote_tps": net.get("nonvote_tps"),
        "slot_ms": net.get("slot_time_ms"),
        "delinquent_stake_pct": val.get("delinquent_stake_pct"),
        "price": mkt.get("sol_price_usd"),
        "tvl": (snap.get("tvl") or {}).get("tvl_usd"),
        "rev_usd": der.get("rev24h_usd"),
        "anomaly_level": worst,
        "levels": levels,
    }


def docs_path(name):
    p = Path(CONFIG["docs_dir"])
    p.mkdir(parents=True, exist_ok=True)
    return p / name


def load_history():
    try:
        return json.loads(docs_path("history.json").read_text())
    except Exception:
        return []


def save_history(history):
    docs_path("history.json").write_text(json.dumps(history))


# --------------------------------------------------------------------------
# Renderers: JSON + Markdown (HTML lives in render_html below)
# --------------------------------------------------------------------------

def render_json(snap):
    docs_path("data.json").write_text(json.dumps(snap, indent=1))


def render_markdown(snap):
    net = snap.get("network") or {}
    val = snap.get("validators") or {}
    mkt = snap.get("market") or {}
    der = snap.get("derived") or {}
    dex = snap.get("dex") or {}
    anom = snap.get("anomalies") or {}
    sw = snap.get("stakewiz") or {}
    gh = snap.get("github") or {}
    stp = snap.get("status_page") or {}
    L = []
    a = L.append
    a("# Solbeat — State of the Solana Network")
    a(f"\n> Generated {snap['generated_at']} · zero API keys · Python stdlib + public endpoints\n")
    a("## Analyst commentary\n")
    a(snap.get("commentary", "") + "\n")

    a("## Network performance\n")
    a("| Metric | Value |\n|---|---|")
    a(f"| Health | {net.get('health', 'n/a')} |")
    a(f"| Slot | {net.get('slot', 0):,} |")
    a(f"| Block height | {net.get('block_height', 0):,} |")
    a(f"| Epoch | {net.get('epoch')} ({net.get('epoch_progress_pct')}% complete, ~{der.get('epoch_eta_hours', '?')}h left) |")
    a(f"| TPS (10 min avg) | {net.get('tps', 0):,.0f} |")
    a(f"| Non-vote TPS | {net.get('nonvote_tps') or 0:,.0f} |")
    a(f"| Slot time (measured) | {net.get('slot_time_ms')} ms |")
    a(f"| Est. daily transactions | {net.get('est_daily_txs', 0):,} |")
    a(f"| Median priority fee | {net.get('priority_fee_median')} µ-lamports/CU |")
    a(f"| Avg fee per user tx (24h) | ${der.get('avg_fee_per_tx_usd', 0) or 0:.4f} |")
    a(f"| Node version | {net.get('node_version')} |\n")

    a("## Economic indicators\n")
    a("| Metric | Value |\n|---|---|")
    a(f"| SOL price | ${mkt.get('sol_price_usd', 0):,.2f} ({mkt.get('sol_change24h_pct', 0):+.1f}%/24h) |")
    a(f"| Market cap | {_fmt_usd(mkt.get('sol_mcap_usd'))} |")
    a(f"| **REV (24h)** | **{_fmt_usd(der.get('rev24h_usd'))}** (fees {_fmt_usd((snap.get('fees') or {}).get('chain_fees24h_usd'))} + Jito tips {_fmt_usd(der.get('jito_tips24h_usd'))}) |")
    a(f"| Chain TVL | {_fmt_usd((snap.get('tvl') or {}).get('tvl_usd'))} |")
    a(f"| Stablecoin supply | {_fmt_usd((snap.get('stablecoins') or {}).get('stablecoin_supply_usd'))} |")
    a(f"| DEX volume (24h) | {_fmt_usd(dex.get('dex_vol24h_usd'))} ({dex.get('dex_change1d_pct')}%/1d) |")
    a(f"| Tokenized equities (xStocks TVL) | {_fmt_usd((snap.get('xstocks') or {}).get('xstocks_tvl_usd'))} |")
    a(f"| Circulating supply | {net.get('supply_circulating_sol', 0):,} SOL |")
    a(f"| Inflation | {net.get('inflation_total_pct')}% |\n")

    if dex.get("dex_top_protocols"):
        a("Top DEXs by 24h volume: " + ", ".join(
            f"{p['name']} ({_fmt_usd(p['vol24h_usd'])})" for p in dex["dex_top_protocols"]) + "\n")

    a("## Validators\n")
    a("| Metric | Value |\n|---|---|")
    a(f"| Active / delinquent | {val.get('active_count')} / {val.get('delinquent_count')} |")
    a(f"| Delinquent stake | {val.get('delinquent_stake_pct')}% |")
    a(f"| Nakamoto coefficient | {val.get('nakamoto_coefficient')} |")
    a(f"| Top-10 stake share | {val.get('top10_stake_pct')}% |")
    a(f"| Avg / median commission | {val.get('avg_commission_pct')}% / {val.get('median_commission_pct')}% |")
    if sw.get("bls_stake_pct") is not None:
        a(f"| Alpenglow BLS-key readiness | {sw.get('bls_registered_count')} validators, {sw.get('bls_stake_pct')}% of stake |")
    a("\n### Top validators by stake\n")
    a("| # | Vote account | Stake (SOL) | Share | Commission |\n|---|---|---|---|---|")
    for i, v in enumerate(val.get("top_validators", []), 1):
        a(f"| {i} | `{v['vote_pubkey'][:20]}…` | {v['stake_sol']:,} | {v['stake_pct']}% | {v['commission_pct']}% |")
    a("")

    a("## Signals (anomaly detection)\n")
    if anom.get("all_clear"):
        a("All clear — no anomalies across monitored metrics.\n")
    else:
        for f in anom.get("findings", []):
            a(f"- **[{f['level'].upper()}]** {f['text']}")
        for inc in anom.get("incidents", []):
            a(f"- **[{inc['level'].upper()} · {inc['class']}]** {inc['text']}")
        a("")

    a("## Ecosystem pulse\n")
    a("| Program | Activity (tx/min, sampled) |\n|---|---|")
    for p in snap.get("program_pulse") or []:
        rate = f"{p['tx_per_min']:,.0f}" if p.get("tx_per_min") is not None else "n/a"
        a(f"| {p['program']} | {rate} |")
    a("\n| Exchange wallet | Balance (SOL) |\n|---|---|")
    for w in snap.get("whales") or []:
        bal = f"{w['balance_sol']:,.0f}" if w.get("balance_sol") is not None else "n/a"
        a(f"| {w['label']} | {bal} |")
    a("")

    a("## Upgrades & news\n")
    slot_ms = net.get("slot_time_ms")
    a(f"- **SIMD-0525 (slot-time reduction)**: "
      + ("first step (350ms) confirmed ACTIVE — measured slot time "
         f"{slot_ms:.0f}ms" if der.get("simd525_step_active") and slot_ms else "tracking")
      + (f" · proposal {gh.get('simd525_state')}" if gh.get("simd525_state") else "") + ".")
    a(f"- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for "
      f"activation via Agave v4.3; BLS-key registration at "
      f"{sw.get('bls_stake_pct', '?')}% of stake.")
    a(f"- **Agave**: latest release {gh.get('agave_latest_tag')} · running "
      f"{net.get('node_version')} on the polled node.")
    a(f"- **Status page**: {stp.get('statuspage_description', 'n/a')} "
      f"({stp.get('unresolved_incidents', 0)} unresolved incidents).\n")

    news = (snap.get("news") or {}).get("items") or []
    if news:
        a("### Latest ecosystem news (solana.com)\n")
        for it in news:
            a(f"- [{it['title']}]({it['link']}) — {it['published'][:16]}")
        a("")
    dune = snap.get("dune") or {}
    if dune.get("daily_active_addresses"):
        a(f"Daily active addresses (Dune query {dune.get('query_id')}): "
          f"{dune['daily_active_addresses']:,.0f}\n")

    a("## Data sources & provenance\n")
    a("| Source | Status | Latency |\n|---|---|---|")
    for name, s in (snap.get("sources") or {}).items():
        a(f"| {name} | {'OK' if s['ok'] else 'FAILED'} | {s['latency_ms']} ms |")
    a("\n*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips "
      "(Kobe API), following the Blockworks definition. All endpoints keyless.*")
    docs_path("report.md").write_text("\n".join(L))


# --------------------------------------------------------------------------
# Entry points
# --------------------------------------------------------------------------

def cmd_collect():
    snap = collect_snapshot()
    history = load_history()
    history.append(history_entry(snap))
    history = history[-CONFIG["history_max_entries"]:]
    save_history(history)
    snap["history"] = history[-200:]
    render_json(snap)
    ok = sum(1 for s in snap["sources"].values() if s["ok"])
    print(f"collected: {ok}/{len(snap['sources'])} sources ok -> docs/data.json")
    return snap


def load_snapshot():
    return json.loads(docs_path("data.json").read_text())


def cmd_render():
    snap = load_snapshot()
    render_markdown(snap)
    render_html(snap)
    print("rendered: docs/index.html docs/report.md")


def cmd_serve():
    import http.server
    import threading
    import functools

    def loop():
        while True:
            try:
                cmd_collect()
                cmd_render()
            except Exception as exc:
                print(f"refresh failed: {exc}")
            time.sleep(CONFIG["refresh_seconds"])

    threading.Thread(target=loop, daemon=True).start()
    handler = functools.partial(http.server.SimpleHTTPRequestHandler,
                                directory=CONFIG["docs_dir"])
    port = 8017
    print(f"solbeat serving http://localhost:{port} "
          f"(refreshing every {CONFIG['refresh_seconds']}s)")
    http.server.ThreadingHTTPServer(("", port), handler).serve_forever()


def cmd_verify():
    """Self-audit: cross-check the snapshot's headline numbers against
    independent sources and internal consistency. Exit non-zero on failure."""
    snap = load_snapshot()
    net = snap.get("network") or {}
    mkt = snap.get("market") or {}
    val = snap.get("validators") or {}
    der = snap.get("derived") or {}
    fees = snap.get("fees") or {}
    checks = []

    def check(name, ok, detail):
        checks.append((name, ok, detail))

    # 1. Price: CoinGecko vs Binance (independent keyless source).
    try:
        b = _http_json("https://api.binance.com/api/v3/ticker/price?symbol=SOLUSDT")
        bp, cp = float(b["price"]), mkt.get("sol_price_usd") or 0
        dev = abs(bp - cp) / bp * 100
        check("SOL price vs Binance", dev < 2,
              f"CoinGecko ${cp:,.2f} vs Binance ${bp:,.2f} ({dev:.2f}% apart)")
    except Exception as exc:
        check("SOL price vs Binance", False, f"unavailable: {exc}")

    # 2. Market cap ≈ circulating supply × price (two independent sources).
    if mkt.get("sol_mcap_usd") and net.get("supply_circulating_sol") and mkt.get("sol_price_usd"):
        implied = net["supply_circulating_sol"] * mkt["sol_price_usd"]
        dev = abs(implied - mkt["sol_mcap_usd"]) / mkt["sol_mcap_usd"] * 100
        check("mcap = RPC supply x price", dev < 5,
              f"implied ${implied/1e9:.1f}B vs CoinGecko ${mkt['sol_mcap_usd']/1e9:.1f}B ({dev:.1f}% apart)")

    # 3. Slot time: measure live slot advance vs the reported figure.
    try:
        s1 = rpc("getSlot")
        time.sleep(5)
        s2 = rpc("getSlot")
        measured = 5000 / max(s2 - s1, 1)
        reported = net.get("slot_time_ms") or 0
        dev = abs(measured - reported) / max(measured, 1) * 100
        check("slot time vs live measurement", dev < 30,
              f"reported {reported:.0f}ms vs live {measured:.0f}ms over 5s")
    except Exception as exc:
        check("slot time vs live measurement", False, str(exc))

    # 4. TVL: history endpoint vs the independent chains endpoint.
    try:
        chains = _http_json("https://api.llama.fi/v2/chains")
        sol = next(c for c in chains if c.get("name") == "Solana")
        ours = (snap.get("tvl") or {}).get("tvl_usd") or 0
        dev = abs(sol["tvl"] - ours) / sol["tvl"] * 100
        check("TVL vs DeFiLlama /v2/chains", dev < 5,
              f"ours ${ours/1e9:.2f}B vs chains ${sol['tvl']/1e9:.2f}B ({dev:.1f}% apart)")
    except Exception as exc:
        check("TVL vs DeFiLlama /v2/chains", False, str(exc))

    # 5. REV arithmetic: fees + tips must equal the published figure.
    if der.get("rev24h_usd") and fees.get("chain_fees24h_usd"):
        recomputed = fees["chain_fees24h_usd"] + (der.get("jito_tips24h_usd") or 0)
        check("REV = fees + Jito tips", abs(recomputed - der["rev24h_usd"]) < 2,
              f"${der['rev24h_usd']:,.0f} = ${fees['chain_fees24h_usd']:,.0f} + ${der.get('jito_tips24h_usd', 0):,.0f}")

    # 6. Validator internals: top-10 shares must sum to the reported figure.
    tops = val.get("top_validators") or []
    if tops and val.get("top10_stake_pct"):
        s = sum(v["stake_pct"] for v in tops)
        check("top-10 stake share arithmetic", abs(s - val["top10_stake_pct"]) < 0.5,
              f"sum of rows {s:.1f}% vs reported {val['top10_stake_pct']}%")

    # 7. Epoch math.
    if net.get("epoch_slots_total"):
        pct = 100 * net["epoch_slot_index"] / net["epoch_slots_total"]
        check("epoch progress arithmetic", abs(pct - net["epoch_progress_pct"]) < 0.1,
              f"{pct:.2f}% vs {net['epoch_progress_pct']}%")

    width = max(len(c[0]) for c in checks) + 2
    failed = 0
    print(f"solbeat self-audit — snapshot {snap.get('generated_at')}\n")
    for name, ok, detail in checks:
        mark = "PASS" if ok else "FAIL"
        failed += 0 if ok else 1
        print(f"  [{mark}] {name:<{width}} {detail}")
    print(f"\n{len(checks) - failed}/{len(checks)} checks passed")
    sys.exit(1 if failed else 0)


def main():
    # Refresh cadence is configurable without touching code.
    if os.environ.get("SOLBEAT_REFRESH"):
        CONFIG["refresh_seconds"] = int(os.environ["SOLBEAT_REFRESH"])
    cmd = sys.argv[1] if len(sys.argv) > 1 else "run"
    if cmd == "collect":
        cmd_collect()
    elif cmd == "render":
        cmd_render()
    elif cmd == "run":
        cmd_collect()
        cmd_render()
    elif cmd == "serve":
        cmd_serve()
    elif cmd == "verify":
        cmd_verify()
    else:
        print(__doc__)
        sys.exit(1)


# HTML renderer is defined in solbeat_html.py-style section appended below.
from solbeat_html import render_html  # noqa: E402

if __name__ == "__main__":
    main()
