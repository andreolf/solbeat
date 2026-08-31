# Solbeat

**The heartbeat terminal for the Solana network.** An auto-updating report on the
state of the Solana ecosystem — zero dependencies, zero API keys, Python
standard library only.

Built for the Superteam Canada bounty *"Develop Solana Ecosystem Auto-Updating
Report & Interactive Dashboard."*

**Live dashboard:** *(GitHub Pages URL — enabled after first Actions run)*

![dashboard](docs/screenshot.png)

## What it produces

Every refresh generates three synchronized outputs in `docs/`:

| Output | File | What it is |
|---|---|---|
| Interactive dashboard | [`docs/index.html`](docs/index.html) | Self-contained dark-theme HTML terminal: live-ticking slot counter, REV clock, epoch ring, sparklines, status-page-style anomaly strips, validator table — no chart libraries, no CDN, works offline |
| Human-readable report | [`docs/report.md`](docs/report.md) | The full report as Markdown tables + generated analyst commentary |
| Machine-readable data | [`docs/data.json`](docs/data.json) | The complete structured snapshot (schema-versioned), including per-source provenance |

Committed samples from a real run live in [`samples/`](samples/).

## Quickstart

```bash
git clone <this repo> && cd <this repo>
python3 solbeat.py run        # collect + render (~2-4 min, one full refresh)
python3 solbeat.py serve      # ...then serve docs/ on :8017, refreshing every 30 min
```

That is the entire setup. No `pip install`, no `.env`, no API keys — Python 3.9+
and an internet connection.

## What it covers

**Network performance** — TPS (total and non-vote), measured slot time, block
height, epoch number/progress/ETA, lifetime transaction count, estimated daily
transactions, node version, cluster health, a 12-hour TPS chart and a 12-hour
slot-performance strip.

**Validators** — active vs delinquent counts, delinquent stake share, Nakamoto
coefficient, top-10/top-20 stake concentration, top validators by stake with
commission, average/median commission, total stake, and **Alpenglow readiness**:
the live share of stake that has registered BLS keys for the new consensus.

**Economic indicators** — SOL price/market cap/24h change, **Real Economic Value
(REV) computed with the Blockworks methodology** (chain base + priority fees
plus Jito MEV tips — see below), chain TVL, stablecoin supply, DEX volume with
top venues, median priority fee (+ p90 and % of slots paying), estimated average
fee per transaction, circulating supply, inflation rate.

**Ecosystem growth** — **tokenized equities** (xStocks TVL with history), a
live **program activity pulse** for flagship protocols (Jupiter, Raydium, Orca,
Pump.fun, Tensor, Magic Eden, Marinade) sampled from on-chain signatures, and
exchange reserve tracking via `getBalance` on community-attributed wallets.

**Upgrades & news** — SIMD-0525 slot-time reduction (with our own RPC
measurement as live on-chain proof the 350ms step is active), Alpenglow /
SIMD-0236 (with measured BLS-key registration), latest Agave release from
GitHub, and unresolved incidents from status.solana.com.

## Data sources & integration

Every endpoint is public and keyless. Each fetch is individually wrapped: a
failing source degrades gracefully and is reported honestly in the provenance
panel rather than breaking the report.

| Source | Endpoint | Used for |
|---|---|---|
| Solana mainnet RPC | `api.mainnet-beta.solana.com` | `getSlot`, `getEpochInfo`, `getRecentPerformanceSamples`, `getVoteAccounts`, `getSupply`, `getInflationRate`, `getRecentPrioritizationFees`, `getHealth`, `getVersion`, `getBalance` (exchange reserves), `getSignaturesForAddress` (program pulse) |
| CoinGecko (free) | `api.coingecko.com` | SOL price, market cap, 24h change, 30-day price series |
| DeFiLlama | `api.llama.fi`, `stablecoins.llama.fi` | Chain TVL + history, DEX volumes, chain fees/revenue, stablecoin supply + history, xStocks (tokenized equities) TVL |
| Jito Kobe | `kobe.mainnet.jito.network` | Network MEV tips per epoch (REV input) |
| Stakewiz | `api.stakewiz.com` | BLS-key registration → Alpenglow readiness |
| GitHub API | `api.github.com` | Latest Agave release; SIMD-0525 proposal state |
| Solana status page | `status.solana.com` | Operational status, unresolved incidents |

**Deliberately excluded:** Dune Analytics — every Dune access path (API and
embeds) requires an API key, which conflicts with the zero-key design goal, so
its most valuable Solana metrics are covered from the keyless sources above
instead. Daily active addresses likewise has no keyless source in 2026
(Solscan/Dune/Blockworks all gate it); non-vote TPS is shown as the
transparent, honestly-labeled activity proxy.

### REV methodology

`REV(24h) = chain base+priority fees (DeFiLlama dailyFees) + Jito MEV tips`.
Tips are Kobe's per-epoch total, converted to a daily rate using the *measured*
slot time, priced at spot. This follows the Blockworks Research definition of
Real Economic Value and is labeled as computed wherever it appears.

## Automation strategy

- **GitHub Actions** ([`.github/workflows/solbeat.yml`](.github/workflows/solbeat.yml))
  runs `python3 solbeat.py run` every 30 minutes, commits `docs/`, and GitHub
  Pages serves the dashboard — a fully autonomous loop with zero
  infrastructure and zero secrets.
- **Self-hosted option:** `python3 solbeat.py serve` does the same loop locally
  with `http.server`. The cadence is one constant (`refresh_seconds`).
- The dashboard needs no server-side rendering at view time: JS animates the
  slot counter (from measured slot time), the REV clock, and the data-age
  indicator between refreshes, so a 30-minute cadence still *feels* live.
- Rolling cross-run history (`docs/history.json`, capped) feeds the anomaly
  baselines and the run-history strip; it grows automatically with each cycle.

## Anomaly detection

Two layers:

1. **Per-metric scoring** — z-scores against the best available baseline for
   each metric: TPS and slot time against the last ~12h of RPC performance
   samples; price/TVL/stablecoins/DEX volume against their 30–90 day daily
   series (fetched from source history, so detection works from the very first
   run); REV against the cross-run history. Absolute-threshold rules cover
   delinquent stake share, slow slots, and >10% daily SOL moves.
2. **Multi-source correlation** — co-firing signals are classified into named
   incidents with plain-language narratives: *network incident* (throughput
   anomaly + slow slots/delinquency), *consensus stress*, *market-wide move*
   (price + liquidity), *liquidity rotation* (stablecoins + TVL moving
   together). A TPS drop that coincides with a delinquency spike is a different
   story than a quiet Sunday, and the report says which one it is.

Findings render as status-page-style tick strips (60 days per market metric,
12h for slot performance, plus the run-history strip) — the most instantly
readable anomaly visualization there is.

## Design notes

- **Single-file outputs, no build step.** The HTML embeds all CSS/JS/SVG; charts
  are server-side-generated SVG. It renders identically from a file:// URL.
- **Provenance everywhere.** Every tile carries a source badge (hover: endpoint,
  fetch time, latency); the footer table reports each source's status honestly.
- **Dark theme** on a validated palette; status colors are reserved for status,
  identity never rides on color alone (icons + labels accompany every signal).
- Text/labels never wear data colors; tables use tabular numerals; the layout is
  responsive down to mobile widths.

## Repository layout

```
solbeat.py          # collectors, derived metrics, anomaly engine, MD/JSON renderers, CLI
solbeat_html.py     # HTML dashboard renderer (SVG charts, strips, live JS layer)
docs/               # generated site (Pages root): index.html, report.md, data.json, history.json
samples/            # committed sample outputs from a real run
.github/workflows/  # the 30-minute refresh loop
```

## License

MIT — see [LICENSE](LICENSE).
