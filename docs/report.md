# Solbeat — State of the Solana Network

> Generated 2026-09-26T22:13:59Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1043 is 53% complete (~15h remaining), with the cluster processing ~4,504 TPS (1,985 non-vote). Measured slot time is 267ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $1.2M of Real Economic Value over the last 24h ($839/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $121.68 (+0.1% / 24h). Decentralization: Nakamoto coefficient 18, 675 active validators, 0.1% of stake delinquent. Alpenglow readiness: validators holding 99% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 1 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 450,805,634 |
| Block height | 428,845,365 |
| Epoch | 1043 (53.16% complete, ~15.0h left) |
| TPS (10 min avg) | 4,504 |
| Non-vote TPS | 1,985 |
| Slot time (measured) | 267.0 ms |
| Est. daily transactions | 400,886,761 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0052 |
| Node version | 4.3.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $121.68 (+0.1%/24h) |
| Market cap | $71.5B |
| **REV (24h)** | **$1.2M** (fees $962.2K + Jito tips $245.6K) |
| Chain TVL | $6.6B |
| Stablecoin supply | $16.9B |
| DEX volume (24h) | $2.6B (6.6%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 587,712,343 SOL |
| Inflation | 3.63% |

Top DEXs by 24h volume: PumpSwap ($426.0M), BisonFi ($327.8M), Orca DEX ($231.7M), fomo Wallet ($209.6M), Raydium AMM ($205.5M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 675 / 12 |
| Delinquent stake | 0.05% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.6% |
| Avg / median commission | 12.9% / 5% |
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

- **[WARNING]** Solana TVL surge (z=+2.5 vs its recent baseline)

## Solana Pulse — sentiment (experimental)

**77/100 — Bullish** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 80.7 |
| fear greed | 74 |
| momentum | 68.0 |
| news | 95 |

Crypto Fear & Greed: 74 (Greed) · CoinGecko votes bullish: 80.7% · headline tone (48h): +6

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 142 |
| Raydium AMM v4 | 142 |
| Orca Whirlpool | 157 |
| Pump.fun | 176 |
| Tensor | 0 |
| Magic Eden v2 | 81 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,943,926 |
| Binance (cold) | 2,002,452 |
| OKX (attributed) | 387,383 |
| Coinbase (hot) | 26,690 |

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
| solana_rpc | OK | 7591 ms |
| solana_rpc_validators | OK | 436 ms |
| coingecko | OK | 1816 ms |
| defillama_tvl | OK | 891 ms |
| defillama_dex | OK | 1251 ms |
| defillama_fees | OK | 1820 ms |
| defillama_stablecoins | OK | 257 ms |
| defillama_xstocks | OK | 79 ms |
| jito_kobe | OK | 252 ms |
| stakewiz | OK | 1329 ms |
| github | OK | 898 ms |
| solana_com_news | OK | 178 ms |
| sentiment | OK | 2344 ms |
| solana_status_page | OK | 533 ms |
| solana_rpc_whales | OK | 1338 ms |
| solana_rpc_programs | OK | 2190 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*