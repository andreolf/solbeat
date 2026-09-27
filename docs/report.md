# Solbeat — State of the Solana Network

> Generated 2026-09-27T04:51:08Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1043 is 74% complete (~8h remaining), with the cluster processing ~4,074 TPS (1,556 non-vote). Measured slot time is 266ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $1.5M of Real Economic Value over the last 24h ($1.01K/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $120.23 (-0.3% / 24h). Decentralization: Nakamoto coefficient 18, 673 active validators, 0.2% of stake delinquent. Alpenglow readiness: validators holding 99% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 2 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 450,894,442 |
| Block height | 428,934,157 |
| Epoch | 1043 (73.71% complete, ~8.4h left) |
| TPS (10 min avg) | 4,074 |
| Non-vote TPS | 1,556 |
| Slot time (measured) | 266.4 ms |
| Est. daily transactions | 388,828,684 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0070 |
| Node version | 4.3.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $120.23 (-0.3%/24h) |
| Market cap | $70.7B |
| **REV (24h)** | **$1.5M** (fees $1.2M + Jito tips $243.2K) |
| Chain TVL | $6.6B |
| Stablecoin supply | $16.7B |
| DEX volume (24h) | $2.4B (-10.1%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 587,712,059 SOL |
| Inflation | 3.63% |

Top DEXs by 24h volume: PumpSwap ($513.6M), BisonFi ($327.8M), Orca DEX ($231.3M), fomo Wallet ($201.7M), Raydium AMM ($184.0M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 673 / 14 |
| Delinquent stake | 0.18% |
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

- **[WARNING]** Solana TVL surge (z=+2.4 vs its recent baseline)
- **[WARNING]** Real Economic Value deviating from its run-history baseline (z=+2.2)

## Solana Pulse — sentiment (experimental)

**73/100 — Bullish** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 80.0 |
| fear greed | 70 |
| momentum | 60.4 |
| news | 90 |

Crypto Fear & Greed: 70 (Greed) · CoinGecko votes bullish: 80.0% · headline tone (48h): +5

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 150 |
| Raydium AMM v4 | 150 |
| Orca Whirlpool | 150 |
| Pump.fun | 166 |
| Tensor | 0 |
| Magic Eden v2 | 47 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,943,926 |
| Binance (cold) | 1,972,466 |
| OKX (attributed) | 387,383 |
| Coinbase (hot) | 25,551 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 266ms · proposal merged.
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
| solana_rpc | OK | 7179 ms |
| solana_rpc_validators | OK | 215 ms |
| coingecko | OK | 1701 ms |
| defillama_tvl | OK | 62 ms |
| defillama_dex | OK | 1161 ms |
| defillama_fees | OK | 1482 ms |
| defillama_stablecoins | OK | 62 ms |
| defillama_xstocks | OK | 22 ms |
| jito_kobe | OK | 209 ms |
| stakewiz | OK | 1002 ms |
| github | OK | 750 ms |
| solana_com_news | OK | 51 ms |
| sentiment | OK | 2560 ms |
| solana_status_page | OK | 352 ms |
| solana_rpc_whales | OK | 993 ms |
| solana_rpc_programs | OK | 1781 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*