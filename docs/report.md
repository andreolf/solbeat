# Solbeat — State of the Solana Network

> Generated 2026-10-27T23:02:46Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1070 is 2% complete (~25h remaining), with the cluster processing ~2,123 TPS (2,123 non-vote). Measured slot time is 211ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $710.0K of Real Economic Value over the last 24h ($493/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $101.16 (+1.0% / 24h). Decentralization: Nakamoto coefficient 18, 662 active validators, 0.9% of stake delinquent. Alpenglow readiness: validators holding 100% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: all clear across every monitored metric.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 462,249,323 |
| Block height | 440,274,309 |
| Epoch | 1070 (2.16% complete, ~24.8h left) |
| TPS (10 min avg) | 2,123 |
| Non-vote TPS | 2,123 |
| Slot time (measured) | 211.4 ms |
| Confirmation time (measured) | 0.21 s |
| Finality time (measured) | 0.21 s — **Alpenglow active** |
| Est. daily transactions | 181,305,793 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0031 |
| Node version | 4.3.2 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $101.16 (+1.0%/24h) |
| Market cap | $59.7B |
| **REV (24h)** | **$710.0K** (fees $568.3K + Jito tips $141.6K) |
| Chain TVL | $5.7B |
| Stablecoin supply | $15.7B |
| DEX volume (24h) | $2.1B (42.9%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 589,927,161 SOL |
| Inflation | 3.58% |

Top DEXs by 24h volume: BisonFi ($293.1M), Manifest Trade ($237.5M), Tessera V ($183.7M), PumpSwap ($167.0M), Orca DEX ($152.6M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 662 / 29 |
| Delinquent stake | 0.89% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.6% |
| Avg / median commission | 12.7% / 5.0% |
| Alpenglow BLS-key readiness | 675 validators, 100.0% of stake |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L43ZWjwCHART3o…` | 17,006,422 | 3.89% | 7% |
| 2 | `he1iusunGwqrNtafDtLd…` | 16,661,096 | 3.81% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5…` | 12,791,931 | 2.93% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxb…` | 10,815,143 | 2.47% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxA…` | 9,718,548 | 2.22% | 5% |
| 6 | `51JBzSTU5rAM8gLAVQKg…` | 9,464,443 | 2.16% | 10% |
| 7 | `26pV97Ce83ZQ6Kz9XT4t…` | 9,208,877 | 2.11% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2Fp…` | 7,757,994 | 1.77% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJn…` | 7,041,146 | 1.61% | 5% |
| 10 | `DumiCKHVqoCQKD8roLAp…` | 6,997,044 | 1.6% | 0% |

## Signals (anomaly detection)

All clear — no anomalies across monitored metrics.

## Solana Pulse — sentiment (experimental)

**54/100 — Neutral** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 61.8 |
| fear greed | 48 |
| momentum | 57.6 |
| news | 42 |

Crypto Fear & Greed: 48 (Neutral) · CoinGecko votes bullish: 61.76% · headline tone (48h): -1

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 1,498 |
| Raydium AMM v4 | 375 |
| Orca Whirlpool | 749 |
| Pump.fun | 1,500 |
| Tensor | 0 |
| Magic Eden v2 | 150 |
| Marinade | 1 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 11,175,975 |
| Binance (cold) | 1,244,708 |
| OKX (attributed) | 330,876 |
| Coinbase (hot) | 12,553 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 211ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 100.0% of stake.
- **Agave**: latest release v4.3.2 · running 4.3.2 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

### Latest ecosystem news (solana.com)

- [Solana Breakpoint 2026 Adds Revolut Chair, Former Prime Minister, Former Chancellor and City Leaders to London Lineup](https://solana.com/news/breakpoint-london-lineup) — Mon, 26 Oct 2026
- [Solana Changelog: October 22, 2026](https://solana.com/news/solana-changelog-october-22-2026) — Fri, 23 Oct 2026
- [Solana Changelog: October 16, 2026](https://solana.com/news/solana-changelog-october-16-2026) — Fri, 16 Oct 2026
- [Geo-Aware Leader Schedule](https://solana.com/news/geo-aware-leader-schedule) — Wed, 14 Oct 2026
- [More Breakpoint 2026 Speakers Confirmed for London](https://solana.com/news/breakpoint-2026-london-speakers-2) — Mon, 12 Oct 2026
- [Payments on Solana: September 2026 in Five Stories](https://solana.com/news/payments-on-solana-september-2026-in-five-stories) — Fri, 09 Oct 2026

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 10032 ms |
| solana_rpc_validators | OK | 306 ms |
| coingecko | OK | 1667 ms |
| defillama_tvl | OK | 162 ms |
| defillama_dex | OK | 878 ms |
| defillama_fees | OK | 433 ms |
| defillama_stablecoins | OK | 240 ms |
| defillama_xstocks | FAILED | 81 ms |
| jito_kobe | OK | 446 ms |
| stakewiz | OK | 1122 ms |
| github | OK | 791 ms |
| solana_com_news | OK | 124 ms |
| sentiment | OK | 2441 ms |
| solana_status_page | OK | 313 ms |
| solana_rpc_whales | OK | 1080 ms |
| solana_rpc_programs | OK | 1860 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*