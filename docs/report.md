# Solbeat — State of the Solana Network

> Generated 2026-09-26T05:59:45Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1043 is 3% complete (~31h remaining), with the cluster processing ~4,545 TPS (2,022 non-vote). Measured slot time is 267ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $1.2M of Real Economic Value over the last 24h ($840/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $120.51 (+3.5% / 24h). Decentralization: Nakamoto coefficient 18, 675 active validators, 0.0% of stake delinquent. Alpenglow readiness: validators holding 99% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 1 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 450,587,433 |
| Block height | 428,627,224 |
| Epoch | 1043 (2.65% complete, ~31.2h left) |
| TPS (10 min avg) | 4,545 |
| Non-vote TPS | 2,022 |
| Slot time (measured) | 266.9 ms |
| Est. daily transactions | 426,127,392 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0046 |
| Node version | 4.3.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $120.51 (+3.5%/24h) |
| Market cap | $70.8B |
| **REV (24h)** | **$1.2M** (fees $962.2K + Jito tips $246.7K) |
| Chain TVL | $6.6B |
| Stablecoin supply | $16.9B |
| DEX volume (24h) | $2.8B (14.3%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 587,713,244 SOL |
| Inflation | 3.63% |

Top DEXs by 24h volume: PumpSwap ($426.0M), BisonFi ($395.1M), Orca DEX ($383.3M), Raydium AMM ($283.2M), Meteora DLMM ($204.6M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 675 / 12 |
| Delinquent stake | 0.01% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.6% |
| Avg / median commission | 12.6% / 5% |
| Alpenglow BLS-key readiness | 699 validators, 99.3% of stake |

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

**80/100 — Bullish** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 89.8 |
| fear greed | 74 |
| momentum | 70.6 |
| news | 90 |

Crypto Fear & Greed: 74 (Greed) · CoinGecko votes bullish: 89.77% · headline tone (48h): +5

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 136 |
| Raydium AMM v4 | 150 |
| Orca Whirlpool | 150 |
| Pump.fun | 166 |
| Tensor | 0 |
| Magic Eden v2 | 39 |
| Marinade | 1 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,943,926 |
| Binance (cold) | 2,027,878 |
| OKX (attributed) | 387,384 |
| Coinbase (hot) | 11,176 |

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
| solana_rpc | OK | 8357 ms |
| solana_rpc_validators | OK | 97 ms |
| coingecko | OK | 1646 ms |
| defillama_tvl | OK | 99 ms |
| defillama_dex | OK | 771 ms |
| defillama_fees | OK | 688 ms |
| defillama_stablecoins | OK | 221 ms |
| defillama_xstocks | OK | 32 ms |
| jito_kobe | OK | 172 ms |
| stakewiz | OK | 1016 ms |
| github | OK | 614 ms |
| solana_com_news | OK | 82 ms |
| sentiment | OK | 2170 ms |
| solana_status_page | OK | 470 ms |
| solana_rpc_whales | OK | 993 ms |
| solana_rpc_programs | OK | 1595 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*