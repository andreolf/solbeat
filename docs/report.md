# Solbeat — State of the Solana Network

> Generated 2026-09-27T21:18:37Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1044 is 25% complete (~24h remaining), with the cluster processing ~4,838 TPS (2,331 non-vote). Measured slot time is 268ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $1.5M of Real Economic Value over the last 24h ($1.01K/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $123.05 (+1.8% / 24h). Decentralization: Nakamoto coefficient 18, 675 active validators, 0.0% of stake delinquent. Alpenglow readiness: validators holding 99% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 2 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 451,115,540 |
| Block height | 429,155,217 |
| Epoch | 1044 (24.89% complete, ~24.1h left) |
| TPS (10 min avg) | 4,838 |
| Non-vote TPS | 2,331 |
| Slot time (measured) | 267.8 ms |
| Est. daily transactions | 397,300,863 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0067 |
| Node version | 4.3.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $123.05 (+1.8%/24h) |
| Market cap | $72.3B |
| **REV (24h)** | **$1.5M** (fees $1.2M + Jito tips $242.7K) |
| Chain TVL | $6.7B |
| Stablecoin supply | $16.7B |
| DEX volume (24h) | $2.2B (-17.5%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 587,782,691 SOL |
| Inflation | 3.63% |

Top DEXs by 24h volume: PumpSwap ($513.6M), BisonFi ($251.3M), Orca DEX ($236.3M), pump.fun ($210.8M), Raydium AMM ($180.2M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 675 / 8 |
| Delinquent stake | 0.01% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.5% |
| Avg / median commission | 12.7% / 5% |
| Alpenglow BLS-key readiness | 700 validators, 99.3% of stake |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L43ZWjwCHART3o…` | 17,867,779 | 4.06% | 7% |
| 2 | `he1iusunGwqrNtafDtLd…` | 15,840,792 | 3.6% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5…` | 12,330,570 | 2.8% | 0% |
| 4 | `CatzoSMUkTRidT5DwBxA…` | 11,215,732 | 2.55% | 5% |
| 5 | `8GbwASqdpw4dVcwbWUxb…` | 10,838,730 | 2.46% | 0% |
| 6 | `26pV97Ce83ZQ6Kz9XT4t…` | 9,238,854 | 2.1% | 7% |
| 7 | `51JBzSTU5rAM8gLAVQKg…` | 9,209,776 | 2.09% | 10% |
| 8 | `9QU2QSxhb24FUX3Tu2Fp…` | 7,623,407 | 1.73% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJn…` | 7,094,526 | 1.61% | 5% |
| 10 | `DumiCKHVqoCQKD8roLAp…` | 6,511,334 | 1.48% | 0% |

## Signals (anomaly detection)

- **[WARNING]** Solana TVL surge (z=+2.5 vs its recent baseline)
- **[WARNING]** Real Economic Value deviating from its run-history baseline (z=+2.0)

## Solana Pulse — sentiment (experimental)

**78/100 — Bullish** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 93.2 |
| fear greed | 70 |
| momentum | 60.6 |
| news | 95 |

Crypto Fear & Greed: 70 (Greed) · CoinGecko votes bullish: 93.18% · headline tone (48h): +6

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 144 |
| Raydium AMM v4 | 144 |
| Orca Whirlpool | 159 |
| Pump.fun | 159 |
| Tensor | 0 |
| Magic Eden v2 | 64 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,943,926 |
| Binance (cold) | 2,004,577 |
| OKX (attributed) | 387,383 |
| Coinbase (hot) | 9,865 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 268ms · proposal merged.
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
| solana_rpc | OK | 8361 ms |
| solana_rpc_validators | OK | 288 ms |
| coingecko | OK | 1772 ms |
| defillama_tvl | OK | 1029 ms |
| defillama_dex | OK | 1363 ms |
| defillama_fees | OK | 2154 ms |
| defillama_stablecoins | OK | 243 ms |
| defillama_xstocks | OK | 54 ms |
| jito_kobe | OK | 221 ms |
| stakewiz | OK | 1514 ms |
| github | OK | 744 ms |
| solana_com_news | OK | 132 ms |
| sentiment | OK | 2278 ms |
| solana_status_page | OK | 490 ms |
| solana_rpc_whales | OK | 1214 ms |
| solana_rpc_programs | OK | 1999 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*