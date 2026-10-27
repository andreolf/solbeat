# Solbeat — State of the Solana Network

> Generated 2026-10-27T11:13:58Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1069 is 56% complete (~11h remaining), with the cluster processing ~1,253 TPS (1,253 non-vote). Measured slot time is 212ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $708.1K of Real Economic Value over the last 24h ($492/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $100.17 (-0.9% / 24h). Decentralization: Nakamoto coefficient 18, 665 active validators, 0.1% of stake delinquent. Alpenglow readiness: validators holding 100% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: all clear across every monitored metric.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 462,049,539 |
| Block height | 440,075,296 |
| Epoch | 1069 (55.91% complete, ~11.2h left) |
| TPS (10 min avg) | 1,253 |
| Non-vote TPS | 1,253 |
| Slot time (measured) | 212.1 ms |
| Confirmation time (measured) | 0.21 s |
| Finality time (measured) | 0.21 s — **Alpenglow active** |
| Est. daily transactions | 115,781,064 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0049 |
| Node version | 4.3.2 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $100.17 (-0.9%/24h) |
| Market cap | $59.1B |
| **REV (24h)** | **$708.1K** (fees $568.3K + Jito tips $139.8K) |
| Chain TVL | $5.7B |
| Stablecoin supply | $15.7B |
| DEX volume (24h) | $2.1B (42.9%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 589,874,601 SOL |
| Inflation | 3.58% |

Top DEXs by 24h volume: BisonFi ($293.1M), Manifest Trade ($281.5M), Orca DEX ($206.0M), Tessera V ($183.7M), PumpSwap ($167.0M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 665 / 20 |
| Delinquent stake | 0.09% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.6% |
| Avg / median commission | 13.1% / 5% |
| Alpenglow BLS-key readiness | 676 validators, 100.0% of stake |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L43ZWjwCHART3o…` | 17,059,304 | 3.9% | 7% |
| 2 | `he1iusunGwqrNtafDtLd…` | 16,636,453 | 3.81% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5…` | 12,660,117 | 2.9% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxb…` | 10,812,577 | 2.47% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxA…` | 9,716,980 | 2.22% | 5% |
| 6 | `51JBzSTU5rAM8gLAVQKg…` | 9,494,053 | 2.17% | 10% |
| 7 | `26pV97Ce83ZQ6Kz9XT4t…` | 9,206,552 | 2.11% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2Fp…` | 7,754,189 | 1.77% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJn…` | 7,040,177 | 1.61% | 5% |
| 10 | `DumiCKHVqoCQKD8roLAp…` | 6,996,375 | 1.6% | 0% |

## Signals (anomaly detection)

All clear — no anomalies across monitored metrics.

## Solana Pulse — sentiment (experimental)

**55/100 — Neutral** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 65.5 |
| fear greed | 48 |
| momentum | 55.8 |
| news | 42 |

Crypto Fear & Greed: 48 (Neutral) · CoinGecko votes bullish: 65.52% · headline tone (48h): -1

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 1,500 |
| Raydium AMM v4 | 586 |
| Orca Whirlpool | 1,500 |
| Pump.fun | 1,500 |
| Tensor | 0 |
| Magic Eden v2 | 111 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 11,175,975 |
| Binance (cold) | 1,174,837 |
| OKX (attributed) | 330,876 |
| Coinbase (hot) | 14,390 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 212ms · proposal merged.
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
| solana_rpc | OK | 10553 ms |
| solana_rpc_validators | OK | 329 ms |
| coingecko | OK | 1625 ms |
| defillama_tvl | OK | 829 ms |
| defillama_dex | OK | 940 ms |
| defillama_fees | OK | 1587 ms |
| defillama_stablecoins | OK | 928 ms |
| defillama_xstocks | FAILED | 54 ms |
| jito_kobe | OK | 339 ms |
| stakewiz | OK | 1105 ms |
| github | OK | 831 ms |
| solana_com_news | OK | 114 ms |
| sentiment | OK | 2173 ms |
| solana_status_page | OK | 340 ms |
| solana_rpc_whales | OK | 1205 ms |
| solana_rpc_programs | OK | 1965 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*