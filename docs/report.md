# Solbeat — State of the Solana Network

> Generated 2026-09-03T23:47:48Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1028 is 1% complete (~38h remaining), with the cluster processing ~3,444 TPS (1,330 non-vote). Measured slot time is 316ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $782.2K of Real Economic Value over the last 24h ($543/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $103.96 (+4.0% / 24h). Decentralization: Nakamoto coefficient 18, 674 active validators, 0.1% of stake delinquent. Alpenglow readiness: validators holding 99% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 3 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 444,100,367 |
| Block height | 422,146,889 |
| Epoch | 1028 (1.01% complete, ~37.6h left) |
| TPS (10 min avg) | 3,444 |
| Non-vote TPS | 1,330 |
| Slot time (measured) | 316.2 ms |
| Est. daily transactions | 336,073,261 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0040 |
| Node version | 4.2.2 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $103.96 (+4.0%/24h) |
| Market cap | $60.9B |
| **REV (24h)** | **$782.2K** (fees $612.6K + Jito tips $169.6K) |
| Chain TVL | $6.0B |
| Stablecoin supply | $16.0B |
| DEX volume (24h) | $2.3B (5.4%/1d) |
| Tokenized equities (xStocks TVL) | $461.6M |
| Circulating supply | 585,360,885 SOL |
| Inflation | 3.66% |

Top DEXs by 24h volume: PumpSwap ($1.0B), Orca DEX ($273.0M), BisonFi ($194.4M), Manifest Trade ($177.5M), Raydium AMM ($153.8M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 674 / 20 |
| Delinquent stake | 0.14% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.4% |
| Avg / median commission | 12.3% / 5.0% |
| Alpenglow BLS-key readiness | 689 validators, 99.3% of stake |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L43ZWjwCHART3o…` | 17,393,318 | 3.98% | 7% |
| 2 | `he1iusunGwqrNtafDtLd…` | 16,324,259 | 3.74% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5…` | 12,459,602 | 2.85% | 0% |
| 4 | `CatzoSMUkTRidT5DwBxA…` | 11,379,843 | 2.6% | 5% |
| 5 | `8GbwASqdpw4dVcwbWUxb…` | 9,567,623 | 2.19% | 0% |
| 6 | `26pV97Ce83ZQ6Kz9XT4t…` | 9,278,151 | 2.12% | 7% |
| 7 | `51JBzSTU5rAM8gLAVQKg…` | 9,042,760 | 2.07% | 10% |
| 8 | `9QU2QSxhb24FUX3Tu2Fp…` | 7,376,879 | 1.69% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJn…` | 7,127,366 | 1.63% | 5% |
| 10 | `DumiCKHVqoCQKD8roLAp…` | 6,593,517 | 1.51% | 0% |

## Signals (anomaly detection)

- **[WARNING]** SOL price surge (z=+2.1 vs its recent baseline)
- **[WARNING]** Solana TVL surge (z=+3.0 vs its recent baseline)
- **[WARNING · market_move]** Market-wide move: SOL price anomaly accompanied by liquidity/volume shifts — an ecosystem-level repricing rather than an isolated metric.

## Solana Pulse — sentiment (experimental)

**66/100 — Bullish** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 74.5 |
| fear greed | 65 |
| momentum | 51.3 |
| news | 82 |

Crypto Fear & Greed: 65 (Greed) · CoinGecko votes bullish: 74.47% · headline tone (48h): +4

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 126 |
| Raydium AMM v4 | 108 |
| Orca Whirlpool | 138 |
| Pump.fun | 138 |
| Tensor | 0 |
| Magic Eden v2 | 76 |
| Marinade | 2 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,188,448 |
| Binance (cold) | 2,023,952 |
| OKX (attributed) | 315,396 |
| Coinbase (hot) | 33,503 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 316ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 99.3% of stake.
- **Agave**: latest release v4.2.2 · running 4.2.2 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

### Latest ecosystem news (solana.com)

- [Payment Channels: 1 Million Payments Per Second](https://solana.com/news/payment-channels-1-million-payments-per-second) — Thu, 03 Sep 2026
- [How to Reclaim Excess SOL After Rent Reduction](https://solana.com/news/how-to-reclaim-excess-sol-after-rent-reduction) — Thu, 03 Sep 2026
- [The Token Supercycle: Everything of Value is Becoming Programmable](https://solana.com/news/the-token-supercycle-oped) — Wed, 02 Sep 2026
- [Webinar Recap: Cross-Border Payments in Latin America](https://solana.com/news/webinar-recap-cross-border-payments-in-latin-america) — Tue, 01 Sep 2026
- [Solana Changelog: August 27, 2026](https://solana.com/news/solana-changelog-august-27-2026) — Fri, 28 Aug 2026
- [The Token Supercycle Is Here: Solana Brings Breakpoint 2026 to London](https://solana.com/news/breakpoint-2026-london-speakers) — Thu, 27 Aug 2026

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 9261 ms |
| solana_rpc_validators | OK | 320 ms |
| coingecko | OK | 1693 ms |
| defillama_tvl | OK | 276 ms |
| defillama_dex | OK | 975 ms |
| defillama_fees | OK | 3143 ms |
| defillama_stablecoins | OK | 344 ms |
| defillama_xstocks | OK | 1397 ms |
| jito_kobe | OK | 627 ms |
| stakewiz | OK | 802 ms |
| github | OK | 803 ms |
| solana_com_news | OK | 115 ms |
| sentiment | OK | 2339 ms |
| solana_status_page | OK | 374 ms |
| solana_rpc_whales | OK | 1133 ms |
| solana_rpc_programs | OK | 1940 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*