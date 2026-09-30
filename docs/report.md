# Solbeat — State of the Solana Network

> Generated 2026-09-30T17:08:14Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1046 is 36% complete (~21h remaining), with the cluster processing ~5,078 TPS (2,588 non-vote). Measured slot time is 269ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $1.3M of Real Economic Value over the last 24h ($891/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $120.31 (+1.8% / 24h). Decentralization: Nakamoto coefficient 18, 672 active validators, 0.1% of stake delinquent. Alpenglow readiness: validators holding 99% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 1 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 452,027,288 |
| Block height | 430,066,568 |
| Epoch | 1046 (35.95% complete, ~20.7h left) |
| TPS (10 min avg) | 5,078 |
| Non-vote TPS | 2,588 |
| Slot time (measured) | 269.1 ms |
| Est. daily transactions | 418,559,932 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0053 |
| Node version | 4.3.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $120.31 (+1.8%/24h) |
| Market cap | $70.7B |
| **REV (24h)** | **$1.3M** (fees $1.1M + Jito tips $214.6K) |
| Chain TVL | $6.6B |
| Stablecoin supply | $16.4B |
| DEX volume (24h) | $2.5B (-4.8%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 588,005,665 SOL |
| Inflation | 3.62% |

Top DEXs by 24h volume: Orca DEX ($430.0M), BisonFi ($349.0M), PumpSwap ($337.5M), Raydium AMM ($293.6M), Meteora DLMM ($189.7M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 672 / 11 |
| Delinquent stake | 0.05% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.5% |
| Avg / median commission | 12.7% / 5.0% |
| Alpenglow BLS-key readiness | 703 validators, 99.4% of stake |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L43ZWjwCHART3o…` | 17,227,376 | 3.91% | 7% |
| 2 | `he1iusunGwqrNtafDtLd…` | 15,893,945 | 3.61% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5…` | 12,330,668 | 2.8% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxb…` | 11,384,141 | 2.58% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxA…` | 11,206,135 | 2.54% | 5% |
| 6 | `26pV97Ce83ZQ6Kz9XT4t…` | 9,257,721 | 2.1% | 7% |
| 7 | `51JBzSTU5rAM8gLAVQKg…` | 9,232,740 | 2.1% | 10% |
| 8 | `9QU2QSxhb24FUX3Tu2Fp…` | 7,652,675 | 1.74% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJn…` | 7,092,577 | 1.61% | 5% |
| 10 | `DumiCKHVqoCQKD8roLAp…` | 6,513,562 | 1.48% | 0% |

## Signals (anomaly detection)

- **[WARNING]** Solana TVL surge (z=+2.0 vs its recent baseline)

## Solana Pulse — sentiment (experimental)

**74/100 — Bullish** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 92.9 |
| fear greed | 71 |
| momentum | 52.8 |
| news | 82 |

Crypto Fear & Greed: 71 (Greed) · CoinGecko votes bullish: 92.86% · headline tone (48h): +4

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 158 |
| Raydium AMM v4 | 143 |
| Orca Whirlpool | 158 |
| Pump.fun | 158 |
| Tensor | 0 |
| Magic Eden v2 | 57 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 10,772,652 |
| Binance (cold) | 1,002,542 |
| OKX (attributed) | 387,516 |
| Coinbase (hot) | 18,852 |

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
| solana_rpc | OK | 7054 ms |
| solana_rpc_validators | OK | 160 ms |
| coingecko | OK | 1931 ms |
| defillama_tvl | OK | 200 ms |
| defillama_dex | OK | 1190 ms |
| defillama_fees | OK | 1915 ms |
| defillama_stablecoins | OK | 500 ms |
| defillama_xstocks | OK | 178 ms |
| jito_kobe | OK | 284 ms |
| stakewiz | OK | 3434 ms |
| github | OK | 1029 ms |
| solana_com_news | OK | 130 ms |
| sentiment | OK | 2490 ms |
| solana_status_page | OK | 509 ms |
| solana_rpc_whales | OK | 931 ms |
| solana_rpc_programs | OK | 1566 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*