# Solbeat — State of the Solana Network

> Generated 2026-09-27T12:02:14Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1043 is 96% complete (~1h remaining), with the cluster processing ~4,091 TPS (1,556 non-vote). Measured slot time is 266ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $1.5M of Real Economic Value over the last 24h ($1.01K/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $123.97 (+2.2% / 24h). Decentralization: Nakamoto coefficient 18, 676 active validators, 0.0% of stake delinquent. Alpenglow readiness: validators holding 99% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 2 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 450,991,097 |
| Block height | 429,030,800 |
| Epoch | 1043 (96.09% complete, ~1.2h left) |
| TPS (10 min avg) | 4,091 |
| Non-vote TPS | 1,556 |
| Slot time (measured) | 265.6 ms |
| Est. daily transactions | 349,384,792 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0092 |
| Node version | 4.3.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $123.97 (+2.2%/24h) |
| Market cap | $72.8B |
| **REV (24h)** | **$1.5M** (fees $1.2M + Jito tips $251.5K) |
| Chain TVL | $6.7B |
| Stablecoin supply | $16.7B |
| DEX volume (24h) | $2.2B (-17.5%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 587,711,783 SOL |
| Inflation | 3.63% |

Top DEXs by 24h volume: PumpSwap ($513.6M), BisonFi ($251.3M), pump.fun ($210.8M), Orca DEX ($206.1M), Raydium AMM ($177.8M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 676 / 11 |
| Delinquent stake | 0.01% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.6% |
| Avg / median commission | 12.9% / 5.0% |
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
- **[WARNING]** Real Economic Value deviating from its run-history baseline (z=+2.2)

## Solana Pulse — sentiment (experimental)

**76/100 — Bullish** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 85.1 |
| fear greed | 70 |
| momentum | 61.6 |
| news | 95 |

Crypto Fear & Greed: 70 (Greed) · CoinGecko votes bullish: 85.11% · headline tone (48h): +7

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 146 |
| Raydium AMM v4 | 146 |
| Orca Whirlpool | 146 |
| Pump.fun | 161 |
| Tensor | 0 |
| Magic Eden v2 | 44 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,943,926 |
| Binance (cold) | 2,090,549 |
| OKX (attributed) | 387,383 |
| Coinbase (hot) | 16,036 |

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
| solana_rpc | OK | 7549 ms |
| solana_rpc_validators | OK | 163 ms |
| coingecko | OK | 1711 ms |
| defillama_tvl | OK | 34 ms |
| defillama_dex | OK | 967 ms |
| defillama_fees | OK | 66 ms |
| defillama_stablecoins | OK | 83 ms |
| defillama_xstocks | OK | 25 ms |
| jito_kobe | OK | 163 ms |
| stakewiz | OK | 1005 ms |
| github | OK | 576 ms |
| solana_com_news | OK | 143 ms |
| sentiment | OK | 1989 ms |
| solana_status_page | OK | 273 ms |
| solana_rpc_whales | OK | 753 ms |
| solana_rpc_programs | OK | 1590 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*