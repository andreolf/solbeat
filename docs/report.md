# Solbeat — State of the Solana Network

> Generated 2026-09-03T16:42:22Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1027 is 82% complete (~7h remaining), with the cluster processing ~4,106 TPS (1,975 non-vote). Measured slot time is 315ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $783.2K of Real Economic Value over the last 24h ($544/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $104.27 (+5.2% / 24h). Decentralization: Nakamoto coefficient 18, 676 active validators, 0.1% of stake delinquent. Alpenglow readiness: validators holding 99% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 3 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 444,019,512 |
| Block height | 422,066,388 |
| Epoch | 1027 (82.29% complete, ~6.7h left) |
| TPS (10 min avg) | 4,106 |
| Non-vote TPS | 1,975 |
| Slot time (measured) | 315.2 ms |
| Est. daily transactions | 347,567,683 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0037 |
| Node version | 4.2.2 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $104.27 (+5.2%/24h) |
| Market cap | $61.0B |
| **REV (24h)** | **$783.2K** (fees $612.6K + Jito tips $170.7K) |
| Chain TVL | $5.9B |
| Stablecoin supply | $16.0B |
| DEX volume (24h) | $2.3B (5.4%/1d) |
| Tokenized equities (xStocks TVL) | $456.2M |
| Circulating supply | 585,274,699 SOL |
| Inflation | 3.67% |

Top DEXs by 24h volume: PumpSwap ($1.0B), Orca DEX ($223.8M), Manifest Trade ($197.3M), BisonFi ($194.4M), Meteora DLMM ($137.8M)

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

- **[WARNING]** SOL price surge (z=+2.2 vs its recent baseline)
- **[WARNING]** Solana TVL surge (z=+2.6 vs its recent baseline)
- **[WARNING · market_move]** Market-wide move: SOL price anomaly accompanied by liquidity/volume shifts — an ecosystem-level repricing rather than an isolated metric.

## Solana Pulse — sentiment (experimental)

**66/100 — Bullish** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 77.8 |
| fear greed | 65 |
| momentum | 49.8 |
| news | 74 |

Crypto Fear & Greed: 65 (Greed) · CoinGecko votes bullish: 77.78% · headline tone (48h): +3

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 126 |
| Raydium AMM v4 | 126 |
| Orca Whirlpool | 138 |
| Pump.fun | 138 |
| Tensor | 0 |
| Magic Eden v2 | 58 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,188,448 |
| Binance (cold) | 1,929,140 |
| OKX (attributed) | 315,396 |
| Coinbase (hot) | 68,094 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 315ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 99.4% of stake.
- **Agave**: latest release v4.2.2 · running 4.2.2 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

### Latest ecosystem news (solana.com)

- [The Token Supercycle: Everything of Value is Becoming Programmable](https://solana.com/news/the-token-supercycle-oped) — Wed, 02 Sep 2026
- [Webinar Recap: Cross-Border Payments in Latin America](https://solana.com/news/webinar-recap-cross-border-payments-in-latin-america) — Tue, 01 Sep 2026
- [Solana Changelog: August 27, 2026](https://solana.com/news/solana-changelog-august-27-2026) — Fri, 28 Aug 2026
- [The Token Supercycle Is Here: Solana Brings Breakpoint 2026 to London](https://solana.com/news/breakpoint-2026-london-speakers) — Thu, 27 Aug 2026
- [Solana Changelog: August 20, 2026](https://solana.com/news/solana-changelog-august-20-2026) — Mon, 24 Aug 2026
- [Lowering Slot Time and Validator Economics](https://solana.com/news/lowering-slot-time-and-validators-economic) — Wed, 19 Aug 2026

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 8927 ms |
| solana_rpc_validators | OK | 296 ms |
| coingecko | OK | 1740 ms |
| defillama_tvl | OK | 103 ms |
| defillama_dex | OK | 1204 ms |
| defillama_fees | OK | 2106 ms |
| defillama_stablecoins | OK | 152 ms |
| defillama_xstocks | OK | 111 ms |
| jito_kobe | OK | 262 ms |
| stakewiz | OK | 1417 ms |
| github | OK | 742 ms |
| solana_com_news | OK | 262 ms |
| sentiment | OK | 2289 ms |
| solana_status_page | OK | 461 ms |
| solana_rpc_whales | OK | 1151 ms |
| solana_rpc_programs | OK | 2046 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*