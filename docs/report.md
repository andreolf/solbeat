# Solbeat — State of the Solana Network

> Generated 2026-09-30T03:51:38Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1045 is 95% complete (~2h remaining), with the cluster processing ~4,406 TPS (1,908 non-vote). Measured slot time is 269ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $1.3M of Real Economic Value over the last 24h ($908/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $119.27 (+1.2% / 24h). Decentralization: Nakamoto coefficient 18, 674 active validators, 0.1% of stake delinquent. Alpenglow readiness: validators holding 99% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: all clear across every monitored metric.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 451,848,532 |
| Block height | 429,887,984 |
| Epoch | 1045 (94.57% complete, ~1.8h left) |
| TPS (10 min avg) | 4,406 |
| Non-vote TPS | 1,908 |
| Slot time (measured) | 268.6 ms |
| Est. daily transactions | 370,504,030 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0070 |
| Node version | 4.3.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $119.27 (+1.2%/24h) |
| Market cap | $70.2B |
| **REV (24h)** | **$1.3M** (fees $1.1M + Jito tips $238.9K) |
| Chain TVL | $6.5B |
| Stablecoin supply | $16.4B |
| DEX volume (24h) | $2.7B (-0.1%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 587,934,854 SOL |
| Inflation | 3.63% |

Top DEXs by 24h volume: BisonFi ($381.9M), Orca DEX ($369.4M), PumpSwap ($337.5M), Raydium AMM ($299.4M), Meteora DLMM ($189.7M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 674 / 9 |
| Delinquent stake | 0.05% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.4% |
| Avg / median commission | 12.8% / 5.0% |
| Alpenglow BLS-key readiness | 703 validators, 99.4% of stake |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L43ZWjwCHART3o…` | 17,824,525 | 4.04% | 7% |
| 2 | `he1iusunGwqrNtafDtLd…` | 15,886,038 | 3.6% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5…` | 12,338,577 | 2.8% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxb…` | 11,300,554 | 2.56% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxA…` | 11,209,855 | 2.54% | 5% |
| 6 | `26pV97Ce83ZQ6Kz9XT4t…` | 9,243,744 | 2.09% | 7% |
| 7 | `51JBzSTU5rAM8gLAVQKg…` | 9,224,466 | 2.09% | 10% |
| 8 | `9QU2QSxhb24FUX3Tu2Fp…` | 7,637,468 | 1.73% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJn…` | 6,700,083 | 1.52% | 5% |
| 10 | `DumiCKHVqoCQKD8roLAp…` | 6,518,407 | 1.48% | 0% |

## Signals (anomaly detection)

All clear — no anomalies across monitored metrics.

## Solana Pulse — sentiment (experimental)

**71/100 — Bullish** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 76.2 |
| fear greed | 71 |
| momentum | 53.8 |
| news | 95 |

Crypto Fear & Greed: 71 (Greed) · CoinGecko votes bullish: 76.19% · headline tone (48h): +6

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 138 |
| Raydium AMM v4 | 152 |
| Orca Whirlpool | 152 |
| Pump.fun | 152 |
| Tensor | 0 |
| Magic Eden v2 | 80 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 10,772,652 |
| Binance (cold) | 888,769 |
| OKX (attributed) | 387,515 |
| Coinbase (hot) | 23,992 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 269ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 99.4% of stake.
- **Agave**: latest release v4.3.0 · running 4.3.0 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

### Latest ecosystem news (solana.com)

- [Slot Time Reduction Effects](https://solana.com/news/slot-time-reduction-effects) — Mon, 28 Sep 2026
- [Solana Foundation Appoints Rachel Conlan as Chief Strategy Officer and Jamal Raees as General Manager of Payments](https://solana.com/news/solana-foundation-appoints-2026) — Thu, 24 Sep 2026
- [Stocks Go Onchain: What the SEC's Innovation Exemption Means for Solana](https://solana.com/news/stocks-sec-innovation-exemption) — Wed, 23 Sep 2026
- [Solana Changelog: September 18, 2026](https://solana.com/news/solana-changelog-september-18-2026) — Sat, 19 Sep 2026
- [How AI Is Reshaping Crypto Security, with Michael Coates](https://solana.com/news/bits-to-bricks-crypto-security-michael-coates) — Sat, 19 Sep 2026
- [Breakpoint 2026: A guide to getting oriented (Part 1)](https://solana.com/news/breakpoint-guide-part1) — Fri, 18 Sep 2026

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 7846 ms |
| solana_rpc_validators | OK | 88 ms |
| coingecko | OK | 1631 ms |
| defillama_tvl | OK | 67 ms |
| defillama_dex | OK | 759 ms |
| defillama_fees | OK | 56 ms |
| defillama_stablecoins | OK | 64 ms |
| defillama_xstocks | OK | 35 ms |
| jito_kobe | OK | 316 ms |
| stakewiz | OK | 1001 ms |
| github | OK | 544 ms |
| solana_com_news | OK | 53 ms |
| sentiment | OK | 2082 ms |
| solana_status_page | OK | 386 ms |
| solana_rpc_whales | OK | 902 ms |
| solana_rpc_programs | OK | 1471 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*