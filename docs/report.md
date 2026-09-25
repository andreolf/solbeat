# Solbeat — State of the Solana Network

> Generated 2026-09-25T22:43:09Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1042 is 80% complete (~6h remaining), with the cluster processing ~4,353 TPS (1,831 non-vote). Measured slot time is 267ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $1.2M of Real Economic Value over the last 24h ($836/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $122.30 (+5.2% / 24h). Decentralization: Nakamoto coefficient 18, 675 active validators, 0.0% of stake delinquent. Alpenglow readiness: validators holding 99% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 5 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 450,490,322 |
| Block height | 428,530,186 |
| Epoch | 1042 (80.17% complete, ~6.3h left) |
| TPS (10 min avg) | 4,353 |
| Non-vote TPS | 1,831 |
| Slot time (measured) | 266.7 ms |
| Est. daily transactions | 394,194,227 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0054 |
| Node version | 4.3.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $122.30 (+5.2%/24h) |
| Market cap | $71.9B |
| **REV (24h)** | **$1.2M** (fees $952.7K + Jito tips $250.5K) |
| Chain TVL | $6.6B |
| Stablecoin supply | $17.6B |
| DEX volume (24h) | $2.5B (-4%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 587,641,960 SOL |
| Inflation | 3.63% |

Top DEXs by 24h volume: BisonFi ($395.1M), Orca DEX ($385.3M), Raydium AMM ($303.9M), Meteora DLMM ($191.0M), HumidiFi ($190.3M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 675 / 10 |
| Delinquent stake | 0.01% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.4% |
| Avg / median commission | 12.9% / 5% |
| Alpenglow BLS-key readiness | 699 validators, 99.3% of stake |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L43ZWjwCHART3o…` | 17,819,007 | 4.04% | 7% |
| 2 | `he1iusunGwqrNtafDtLd…` | 15,817,079 | 3.59% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5…` | 12,387,904 | 2.81% | 0% |
| 4 | `CatzoSMUkTRidT5DwBxA…` | 11,274,982 | 2.56% | 5% |
| 5 | `8GbwASqdpw4dVcwbWUxb…` | 10,595,499 | 2.4% | 0% |
| 6 | `26pV97Ce83ZQ6Kz9XT4t…` | 9,221,893 | 2.09% | 7% |
| 7 | `51JBzSTU5rAM8gLAVQKg…` | 9,163,088 | 2.08% | 10% |
| 8 | `9QU2QSxhb24FUX3Tu2Fp…` | 7,599,959 | 1.72% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJn…` | 7,091,911 | 1.61% | 5% |
| 10 | `DumiCKHVqoCQKD8roLAp…` | 6,557,887 | 1.49% | 0% |

## Signals (anomaly detection)

- **[WARNING]** SOL price surge (z=+2.0 vs its recent baseline)
- **[WARNING]** Solana TVL surge (z=+2.5 vs its recent baseline)
- **[SERIOUS]** Stablecoin supply surge (z=+3.4 vs its recent baseline)
- **[WARNING · market_move]** Market-wide move: SOL price anomaly accompanied by liquidity/volume shifts — an ecosystem-level repricing rather than an isolated metric.
- **[WARNING · liquidity_rotation]** Stablecoin supply and TVL moving together — capital rotating in or out of the chain.

## Solana Pulse — sentiment (experimental)

**79/100 — Bullish** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 90.9 |
| fear greed | 71 |
| momentum | 68.7 |
| news | 90 |

Crypto Fear & Greed: 71 (Greed) · CoinGecko votes bullish: 90.91% · headline tone (48h): +5

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 163 |
| Raydium AMM v4 | 163 |
| Orca Whirlpool | 163 |
| Pump.fun | 163 |
| Tensor | 0 |
| Magic Eden v2 | 60 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,943,926 |
| Binance (cold) | 1,602,158 |
| OKX (attributed) | 387,384 |
| Coinbase (hot) | 33,810 |

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
| solana_rpc | OK | 7327 ms |
| solana_rpc_validators | OK | 214 ms |
| coingecko | OK | 1757 ms |
| defillama_tvl | OK | 101 ms |
| defillama_dex | OK | 1188 ms |
| defillama_fees | OK | 2123 ms |
| defillama_stablecoins | OK | 375 ms |
| defillama_xstocks | OK | 805 ms |
| jito_kobe | OK | 237 ms |
| stakewiz | OK | 1537 ms |
| github | OK | 961 ms |
| solana_com_news | OK | 110 ms |
| sentiment | OK | 2395 ms |
| solana_status_page | OK | 450 ms |
| solana_rpc_whales | OK | 843 ms |
| solana_rpc_programs | OK | 1612 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*