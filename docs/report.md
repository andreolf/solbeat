# Solbeat — State of the Solana Network

> Generated 2026-09-28T20:21:23Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1044 is 96% complete (~1h remaining), with the cluster processing ~5,156 TPS (2,655 non-vote). Measured slot time is 269ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $1.2M of Real Economic Value over the last 24h ($821/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $118.77 (-3.6% / 24h). Decentralization: Nakamoto coefficient 18, 675 active validators, 0.0% of stake delinquent. Alpenglow readiness: validators holding 99% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 1 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 451,424,827 |
| Block height | 429,464,457 |
| Epoch | 1044 (96.49% complete, ~1.1h left) |
| TPS (10 min avg) | 5,156 |
| Non-vote TPS | 2,655 |
| Slot time (measured) | 268.9 ms |
| Est. daily transactions | 414,634,208 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0048 |
| Node version | 4.3.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $118.77 (-3.6%/24h) |
| Market cap | $69.8B |
| **REV (24h)** | **$1.2M** (fees $949.1K + Jito tips $233.3K) |
| Chain TVL | $6.6B |
| Stablecoin supply | $16.7B |
| DEX volume (24h) | $1.9B (-10.6%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 587,781,656 SOL |
| Inflation | 3.63% |

Top DEXs by 24h volume: Orca DEX ($386.1M), PumpSwap ($297.1M), BisonFi ($270.0M), Raydium AMM ($256.0M), Meteora DLMM ($158.3M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 675 / 8 |
| Delinquent stake | 0.02% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.5% |
| Avg / median commission | 12.8% / 5% |
| Alpenglow BLS-key readiness | 702 validators, 99.4% of stake |

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

- **[WARNING]** Solana TVL surge (z=+2.2 vs its recent baseline)

## Solana Pulse — sentiment (experimental)

**63/100 — Bullish** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 72.5 |
| fear greed | 74 |
| momentum | 50.6 |
| news | 50 |

Crypto Fear & Greed: 74 (Greed) · CoinGecko votes bullish: 72.5% · headline tone (48h): +0

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 149 |
| Raydium AMM v4 | 149 |
| Orca Whirlpool | 149 |
| Pump.fun | 166 |
| Tensor | 0 |
| Magic Eden v2 | 79 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 10,772,652 |
| Binance (cold) | 1,092,488 |
| OKX (attributed) | 387,383 |
| Coinbase (hot) | 20,890 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 269ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 99.4% of stake.
- **Agave**: latest release v4.3.0 · running 4.3.0 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

### Latest ecosystem news (solana.com)

- [Slot Time Reduction Effects](https://solana.com/news/slot-time-reduction-effects) — Mon, 28 Sep 2026
- [Solana Foundation Appoints Rachel Conlan as Chief Strategy Officer and Jamal Raees as General Manager of Payments](https://solana.com/news/solana-foundation-appoints-2026) — Thu, 24 Sep 2026
- [Stocks Go Onchain: What the SEC's Innovation Exemption Means for Solana](https://solana.com/news/stocks-sec-innovation-exemption) — Wed, 23 Sep 2026
- [Solana Changelog: September 18, 2026](https://solana.com/news/solana-changelog-september-18-2026) — Sat, 19 Sep 2026
- [How AI Is Reshaping Crypto Security, with Michael Coates](https://solana.com/news/bits-to-bricks-crypto-security-michael-coates) — Sat, 19 Sep 2026
- [Project Harmonia Brings Institutional Tokenized Funds to Solana](https://solana.com/news/project-harmonia-brings-institutional-tokenized-funds-to-solana) — Wed, 16 Sep 2026

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 8645 ms |
| solana_rpc_validators | OK | 307 ms |
| coingecko | OK | 1715 ms |
| defillama_tvl | OK | 173 ms |
| defillama_dex | OK | 854 ms |
| defillama_fees | OK | 8600 ms |
| defillama_stablecoins | OK | 221 ms |
| defillama_xstocks | OK | 4006 ms |
| jito_kobe | OK | 266 ms |
| stakewiz | OK | 883 ms |
| github | OK | 813 ms |
| solana_com_news | OK | 196 ms |
| sentiment | OK | 2343 ms |
| solana_status_page | OK | 476 ms |
| solana_rpc_whales | OK | 1324 ms |
| solana_rpc_programs | OK | 2133 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*