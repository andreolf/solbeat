# Solbeat — State of the Solana Network

> Generated 2026-09-03T19:27:22Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1027 is 90% complete (~4h remaining), with the cluster processing ~4,459 TPS (2,339 non-vote). Measured slot time is 316ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $784.6K of Real Economic Value over the last 24h ($545/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $105.42 (+6.2% / 24h). Decentralization: Nakamoto coefficient 18, 676 active validators, 0.1% of stake delinquent. Alpenglow readiness: validators holding 99% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 3 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 444,050,881 |
| Block height | 422,097,633 |
| Epoch | 1027 (89.56% complete, ~4.0h left) |
| TPS (10 min avg) | 4,459 |
| Non-vote TPS | 2,339 |
| Slot time (measured) | 316.2 ms |
| Est. daily transactions | 366,886,923 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0033 |
| Node version | 4.2.2 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $105.42 (+6.2%/24h) |
| Market cap | $61.7B |
| **REV (24h)** | **$784.6K** (fees $612.6K + Jito tips $172.0K) |
| Chain TVL | $6.0B |
| Stablecoin supply | $16.0B |
| DEX volume (24h) | $2.3B (5.4%/1d) |
| Tokenized equities (xStocks TVL) | $462.8M |
| Circulating supply | 585,274,592 SOL |
| Inflation | 3.67% |

Top DEXs by 24h volume: PumpSwap ($1.0B), Orca DEX ($267.0M), BisonFi ($194.4M), Manifest Trade ($184.8M), Raydium AMM ($147.8M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 676 / 19 |
| Delinquent stake | 0.05% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.2% |
| Avg / median commission | 12.5% / 5.0% |
| Alpenglow BLS-key readiness | 689 validators, 99.4% of stake |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L43ZWjwCHART3o…` | 17,348,904 | 3.96% | 7% |
| 2 | `he1iusunGwqrNtafDtLd…` | 16,325,737 | 3.72% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5…` | 12,462,274 | 2.84% | 0% |
| 4 | `CatzoSMUkTRidT5DwBxA…` | 11,304,498 | 2.58% | 5% |
| 5 | `8GbwASqdpw4dVcwbWUxb…` | 9,565,273 | 2.18% | 0% |
| 6 | `26pV97Ce83ZQ6Kz9XT4t…` | 9,285,486 | 2.12% | 7% |
| 7 | `51JBzSTU5rAM8gLAVQKg…` | 9,040,435 | 2.06% | 10% |
| 8 | `9QU2QSxhb24FUX3Tu2Fp…` | 7,220,140 | 1.65% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJn…` | 7,125,475 | 1.63% | 5% |
| 10 | `DumiCKHVqoCQKD8roLAp…` | 6,590,653 | 1.5% | 0% |

## Signals (anomaly detection)

- **[WARNING]** SOL price surge (z=+2.3 vs its recent baseline)
- **[WARNING]** Solana TVL surge (z=+2.9 vs its recent baseline)
- **[WARNING · market_move]** Market-wide move: SOL price anomaly accompanied by liquidity/volume shifts — an ecosystem-level repricing rather than an isolated metric.

## Solana Pulse — sentiment (experimental)

**66/100 — Bullish** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 77.8 |
| fear greed | 65 |
| momentum | 52.4 |
| news | 74 |

Crypto Fear & Greed: 65 (Greed) · CoinGecko votes bullish: 77.78% · headline tone (48h): +3

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 126 |
| Raydium AMM v4 | 138 |
| Orca Whirlpool | 138 |
| Pump.fun | 138 |
| Tensor | 1 |
| Magic Eden v2 | 72 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,188,448 |
| Binance (cold) | 2,035,602 |
| OKX (attributed) | 315,396 |
| Coinbase (hot) | 49,257 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 316ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 99.4% of stake.
- **Agave**: latest release v4.2.2 · running 4.2.2 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

### Latest ecosystem news (solana.com)

- [Payment Channels: 1 Million Payments Per Second](https://solana.com/news/payment-channels-1-million-payments-per-second) — Thu, 03 Sep 2026
- [The Token Supercycle: Everything of Value is Becoming Programmable](https://solana.com/news/the-token-supercycle-oped) — Wed, 02 Sep 2026
- [Webinar Recap: Cross-Border Payments in Latin America](https://solana.com/news/webinar-recap-cross-border-payments-in-latin-america) — Tue, 01 Sep 2026
- [Solana Changelog: August 27, 2026](https://solana.com/news/solana-changelog-august-27-2026) — Fri, 28 Aug 2026
- [The Token Supercycle Is Here: Solana Brings Breakpoint 2026 to London](https://solana.com/news/breakpoint-2026-london-speakers) — Thu, 27 Aug 2026
- [Solana Changelog: August 20, 2026](https://solana.com/news/solana-changelog-august-20-2026) — Mon, 24 Aug 2026

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 7948 ms |
| solana_rpc_validators | OK | 98 ms |
| coingecko | OK | 1637 ms |
| defillama_tvl | OK | 43 ms |
| defillama_dex | OK | 793 ms |
| defillama_fees | OK | 670 ms |
| defillama_stablecoins | OK | 54 ms |
| defillama_xstocks | OK | 1140 ms |
| jito_kobe | OK | 198 ms |
| stakewiz | OK | 934 ms |
| github | OK | 602 ms |
| solana_com_news | OK | 60 ms |
| sentiment | OK | 2180 ms |
| solana_status_page | OK | 411 ms |
| solana_rpc_whales | OK | 754 ms |
| solana_rpc_programs | OK | 1382 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*