# Solbeat — State of the Solana Network

> Generated 2026-09-26T04:58:53Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1042 is 100% complete (~0h remaining), with the cluster processing ~4,959 TPS (2,469 non-vote). Measured slot time is 270ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $1.2M of Real Economic Value over the last 24h ($838/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $120.65 (+3.3% / 24h). Decentralization: Nakamoto coefficient 18, 675 active validators, 0.0% of stake delinquent. Alpenglow readiness: validators holding 99% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 1 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 450,573,829 |
| Block height | 428,613,628 |
| Epoch | 1042 (99.5% complete, ~0.2h left) |
| TPS (10 min avg) | 4,959 |
| Non-vote TPS | 2,469 |
| Slot time (measured) | 270.3 ms |
| Est. daily transactions | 434,803,905 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0044 |
| Node version | 4.3.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $120.65 (+3.3%/24h) |
| Market cap | $70.9B |
| **REV (24h)** | **$1.2M** (fees $962.2K + Jito tips $243.8K) |
| Chain TVL | $6.6B |
| Stablecoin supply | $16.9B |
| DEX volume (24h) | $2.8B (14.3%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 587,641,672 SOL |
| Inflation | 3.63% |

Top DEXs by 24h volume: PumpSwap ($426.0M), BisonFi ($395.1M), Orca DEX ($386.4M), Raydium AMM ($289.4M), Meteora DLMM ($204.6M)

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

- **[WARNING]** Solana TVL surge (z=+2.4 vs its recent baseline)

## Solana Pulse — sentiment (experimental)

**80/100 — Bullish** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 89.5 |
| fear greed | 74 |
| momentum | 70.7 |
| news | 90 |

Crypto Fear & Greed: 74 (Greed) · CoinGecko votes bullish: 89.53% · headline tone (48h): +5

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 145 |
| Raydium AMM v4 | 145 |
| Orca Whirlpool | 145 |
| Pump.fun | 160 |
| Tensor | 1 |
| Magic Eden v2 | 62 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,943,926 |
| Binance (cold) | 2,023,630 |
| OKX (attributed) | 387,384 |
| Coinbase (hot) | 10,313 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 270ms · proposal merged.
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
| solana_rpc | OK | 7603 ms |
| solana_rpc_validators | OK | 127 ms |
| coingecko | OK | 1659 ms |
| defillama_tvl | OK | 71 ms |
| defillama_dex | OK | 777 ms |
| defillama_fees | OK | 696 ms |
| defillama_stablecoins | OK | 134 ms |
| defillama_xstocks | OK | 35 ms |
| jito_kobe | OK | 183 ms |
| stakewiz | OK | 750 ms |
| github | OK | 580 ms |
| solana_com_news | OK | 157 ms |
| sentiment | OK | 2076 ms |
| solana_status_page | OK | 164 ms |
| solana_rpc_whales | OK | 1003 ms |
| solana_rpc_programs | OK | 1544 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*