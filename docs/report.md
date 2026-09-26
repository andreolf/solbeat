# Solbeat — State of the Solana Network

> Generated 2026-09-26T10:32:36Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1043 is 17% complete (~27h remaining), with the cluster processing ~4,083 TPS (1,558 non-vote). Measured slot time is 267ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $1.2M of Real Economic Value over the last 24h ($837/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $120.42 (+1.4% / 24h). Decentralization: Nakamoto coefficient 18, 676 active validators, 0.0% of stake delinquent. Alpenglow readiness: validators holding 99% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 1 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 450,648,574 |
| Block height | 428,688,347 |
| Epoch | 1043 (16.8% complete, ~26.6h left) |
| TPS (10 min avg) | 4,083 |
| Non-vote TPS | 1,558 |
| Slot time (measured) | 266.9 ms |
| Est. daily transactions | 374,397,120 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0061 |
| Node version | 4.3.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $120.42 (+1.4%/24h) |
| Market cap | $70.8B |
| **REV (24h)** | **$1.2M** (fees $962.2K + Jito tips $243.1K) |
| Chain TVL | $6.6B |
| Stablecoin supply | $16.9B |
| DEX volume (24h) | $2.8B (14.3%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 587,712,844 SOL |
| Inflation | 3.63% |

Top DEXs by 24h volume: PumpSwap ($426.0M), BisonFi ($395.1M), Orca DEX ($383.3M), Raydium AMM ($256.5M), Meteora DLMM ($204.6M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 676 / 11 |
| Delinquent stake | 0.01% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.6% |
| Avg / median commission | 12.6% / 5.0% |
| Alpenglow BLS-key readiness | 700 validators, 99.3% of stake |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L43ZWjwCHART3o…` | 17,860,284 | 4.08% | 7% |
| 2 | `he1iusunGwqrNtafDtLd…` | 15,799,204 | 3.61% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5…` | 12,343,056 | 2.82% | 0% |
| 4 | `CatzoSMUkTRidT5DwBxA…` | 11,222,561 | 2.56% | 5% |
| 5 | `8GbwASqdpw4dVcwbWUxb…` | 10,836,562 | 2.48% | 0% |
| 6 | `26pV97Ce83ZQ6Kz9XT4t…` | 9,237,102 | 2.11% | 7% |
| 7 | `51JBzSTU5rAM8gLAVQKg…` | 9,182,742 | 2.1% | 10% |
| 8 | `9QU2QSxhb24FUX3Tu2Fp…` | 7,606,181 | 1.74% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJn…` | 7,093,311 | 1.62% | 5% |
| 10 | `DumiCKHVqoCQKD8roLAp…` | 6,506,505 | 1.49% | 0% |

## Signals (anomaly detection)

- **[WARNING]** Solana TVL surge (z=+2.4 vs its recent baseline)

## Solana Pulse — sentiment (experimental)

**82/100 — Bullish** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 93.2 |
| fear greed | 74 |
| momentum | 70.0 |
| news | 95 |

Crypto Fear & Greed: 74 (Greed) · CoinGecko votes bullish: 93.18% · headline tone (48h): +6

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 142 |
| Raydium AMM v4 | 142 |
| Orca Whirlpool | 157 |
| Pump.fun | 157 |
| Tensor | 0 |
| Magic Eden v2 | 43 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,943,926 |
| Binance (cold) | 1,950,520 |
| OKX (attributed) | 387,383 |
| Coinbase (hot) | 18,035 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 267ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 99.3% of stake.
- **Agave**: latest release v4.3.0 · running 4.3.0 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

### Latest ecosystem news (solana.com)

- [Solana Foundation Appoints Rachel Conlan as Chief Strategy Officer and Jamal Raees as General Manager of Payments](https://solana.com/news/solana-foundation-appoints-2026) — Thu, 24 Sep 2026
- [Stocks Go Onchain: What the SEC's Innovation Exemption Means for Solana](https://solana.com/news/stocks-sec-innovation-exemption) — Wed, 23 Sep 2026
- [Solana Changelog: September 18, 2026](https://solana.com/news/solana-changelog-september-18-2026) — Sat, 19 Sep 2026
- [How AI Is Reshaping Crypto Security, with Michael Coates](https://solana.com/news/bits-to-bricks-crypto-security-michael-coates) — Sat, 19 Sep 2026
- [Project Harmonia Brings Institutional Tokenized Funds to Solana](https://solana.com/news/project-harmonia-brings-institutional-tokenized-funds-to-solana) — Wed, 16 Sep 2026
- [Solana Summer School 2026: From first program to demo day](https://solana.com/news/solana-summer-school-2026) — Mon, 14 Sep 2026

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 7916 ms |
| solana_rpc_validators | OK | 351 ms |
| coingecko | OK | 1722 ms |
| defillama_tvl | OK | 1071 ms |
| defillama_dex | OK | 1238 ms |
| defillama_fees | OK | 2082 ms |
| defillama_stablecoins | OK | 1276 ms |
| defillama_xstocks | OK | 816 ms |
| jito_kobe | OK | 377 ms |
| stakewiz | OK | 1416 ms |
| github | OK | 840 ms |
| solana_com_news | OK | 104 ms |
| sentiment | OK | 2486 ms |
| solana_status_page | OK | 377 ms |
| solana_rpc_whales | OK | 1215 ms |
| solana_rpc_programs | OK | 1913 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*