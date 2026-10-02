# Solbeat — State of the Solana Network

> Generated 2026-10-02T11:25:15Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1047 is 68% complete (~10h remaining), with the cluster processing ~4,020 TPS (1,483 non-vote). Measured slot time is 264ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $1.4M of Real Economic Value over the last 24h ($942/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $122.11 (+3.8% / 24h). Decentralization: Nakamoto coefficient 18, 672 active validators, 0.0% of stake delinquent. Alpenglow readiness: validators holding 99% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 1 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 452,595,943 |
| Block height | 430,634,662 |
| Epoch | 1047 (67.58% complete, ~10.3h left) |
| TPS (10 min avg) | 4,020 |
| Non-vote TPS | 1,483 |
| Slot time (measured) | 263.9 ms |
| Est. daily transactions | 354,139,200 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0081 |
| Node version | 4.3.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $122.11 (+3.8%/24h) |
| Market cap | $71.8B |
| **REV (24h)** | **$1.4M** (fees $1.1M + Jito tips $236.6K) |
| Chain TVL | $6.7B |
| Stablecoin supply | $16.5B |
| DEX volume (24h) | $2.5B (-3.2%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 588,075,286 SOL |
| Inflation | 3.62% |

Top DEXs by 24h volume: PumpSwap ($371.2M), Orca DEX ($357.9M), Raydium AMM ($240.0M), BisonFi ($216.9M), Meteora DLMM ($195.5M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 672 / 12 |
| Delinquent stake | 0.02% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.6% |
| Avg / median commission | 13% / 5.0% |
| Alpenglow BLS-key readiness | 703 validators, 99.4% of stake |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L43ZWjwCHART3o…` | 17,839,408 | 4.05% | 7% |
| 2 | `he1iusunGwqrNtafDtLd…` | 15,905,145 | 3.61% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5…` | 12,328,203 | 2.8% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxb…` | 11,357,265 | 2.58% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxA…` | 11,209,121 | 2.54% | 5% |
| 6 | `26pV97Ce83ZQ6Kz9XT4t…` | 9,267,704 | 2.1% | 7% |
| 7 | `51JBzSTU5rAM8gLAVQKg…` | 9,246,451 | 2.1% | 10% |
| 8 | `9QU2QSxhb24FUX3Tu2Fp…` | 7,601,711 | 1.72% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJn…` | 7,063,975 | 1.6% | 5% |
| 10 | `3JD3jMmnR6g88qff2WZ3…` | 6,682,305 | 1.52% | 0% |

## Signals (anomaly detection)

- **[WARNING]** Solana TVL surge (z=+2.1 vs its recent baseline)

## Solana Pulse — sentiment (experimental)

**69/100 — Bullish** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 84.6 |
| fear greed | 72 |
| momentum | 51.6 |
| news | 66 |

Crypto Fear & Greed: 72 (Greed) · CoinGecko votes bullish: 84.62% · headline tone (48h): +2

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 158 |
| Raydium AMM v4 | 131 |
| Orca Whirlpool | 158 |
| Pump.fun | 177 |
| Tensor | 0 |
| Magic Eden v2 | 104 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 10,572,652 |
| Binance (cold) | 1,322,148 |
| OKX (attributed) | 387,517 |
| Coinbase (hot) | 13,463 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 264ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 99.4% of stake.
- **Agave**: latest release v4.3.0 · running 4.3.0 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

### Latest ecosystem news (solana.com)

- [Open USD Is Live on Solana](https://solana.com/news/open-usd-is-live-on-solana) — Wed, 30 Sep 2026
- [Slot Time Reduction Effects](https://solana.com/news/slot-time-reduction-effects) — Mon, 28 Sep 2026
- [Solana Foundation Appoints Rachel Conlan as Chief Strategy Officer and Jamal Raees as General Manager of Payments](https://solana.com/news/solana-foundation-appoints-2026) — Thu, 24 Sep 2026
- [Stocks Go Onchain: What the SEC's Innovation Exemption Means for Solana](https://solana.com/news/stocks-sec-innovation-exemption) — Wed, 23 Sep 2026
- [Solana Changelog: September 18, 2026](https://solana.com/news/solana-changelog-september-18-2026) — Sat, 19 Sep 2026
- [How AI Is Reshaping Crypto Security, with Michael Coates](https://solana.com/news/bits-to-bricks-crypto-security-michael-coates) — Sat, 19 Sep 2026

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 9051 ms |
| solana_rpc_validators | OK | 267 ms |
| coingecko | OK | 1619 ms |
| defillama_tvl | OK | 75 ms |
| defillama_dex | OK | 829 ms |
| defillama_fees | OK | 3407 ms |
| defillama_stablecoins | OK | 60 ms |
| defillama_xstocks | OK | 508 ms |
| jito_kobe | OK | 174 ms |
| stakewiz | OK | 727 ms |
| github | OK | 720 ms |
| solana_com_news | OK | 62 ms |
| sentiment | OK | 2116 ms |
| solana_status_page | OK | 452 ms |
| solana_rpc_whales | OK | 1103 ms |
| solana_rpc_programs | OK | 1827 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*