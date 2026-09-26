# Solbeat — State of the Solana Network

> Generated 2026-09-26T03:27:47Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1042 is 95% complete (~2h remaining), with the cluster processing ~4,997 TPS (2,543 non-vote). Measured slot time is 273ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $1.2M of Real Economic Value over the last 24h ($836/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $120.78 (+3.4% / 24h). Decentralization: Nakamoto coefficient 18, 675 active validators, 0.0% of stake delinquent. Alpenglow readiness: validators holding 99% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 1 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 450,553,591 |
| Block height | 428,593,391 |
| Epoch | 1042 (94.81% complete, ~1.7h left) |
| TPS (10 min avg) | 4,997 |
| Non-vote TPS | 2,543 |
| Slot time (measured) | 273.1 ms |
| Est. daily transactions | 435,627,669 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0043 |
| Node version | 4.3.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $120.78 (+3.4%/24h) |
| Market cap | $71.0B |
| **REV (24h)** | **$1.2M** (fees $962.2K + Jito tips $241.6K) |
| Chain TVL | $6.6B |
| Stablecoin supply | $16.9B |
| DEX volume (24h) | $2.8B (14.3%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 587,641,744 SOL |
| Inflation | 3.63% |

Top DEXs by 24h volume: PumpSwap ($426.0M), BisonFi ($395.1M), Orca DEX ($386.4M), Raydium AMM ($293.7M), Meteora DLMM ($204.6M)

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

- **[WARNING]** Solana TVL surge (z=+2.5 vs its recent baseline)

## Solana Pulse — sentiment (experimental)

**79/100 — Bullish** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 89.2 |
| fear greed | 74 |
| momentum | 71.3 |
| news | 82 |

Crypto Fear & Greed: 74 (Greed) · CoinGecko votes bullish: 89.16% · headline tone (48h): +4

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 149 |
| Raydium AMM v4 | 149 |
| Orca Whirlpool | 165 |
| Pump.fun | 165 |
| Tensor | 1 |
| Magic Eden v2 | 31 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,943,926 |
| Binance (cold) | 1,539,483 |
| OKX (attributed) | 387,384 |
| Coinbase (hot) | 10,250 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 273ms · proposal merged.
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
| solana_rpc | OK | 7768 ms |
| solana_rpc_validators | OK | 157 ms |
| coingecko | OK | 1686 ms |
| defillama_tvl | OK | 166 ms |
| defillama_dex | OK | 426 ms |
| defillama_fees | OK | 129 ms |
| defillama_stablecoins | OK | 117 ms |
| defillama_xstocks | OK | 521 ms |
| jito_kobe | OK | 190 ms |
| stakewiz | OK | 695 ms |
| github | OK | 578 ms |
| solana_com_news | OK | 93 ms |
| sentiment | OK | 2067 ms |
| solana_status_page | OK | 331 ms |
| solana_rpc_whales | OK | 976 ms |
| solana_rpc_programs | OK | 1568 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*