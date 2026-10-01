# Solbeat — State of the Solana Network

> Generated 2026-10-01T13:47:40Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1047 is 0% complete (~32h remaining), with the cluster processing ~5,229 TPS (2,758 non-vote). Measured slot time is 270ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $1.3M of Real Economic Value over the last 24h ($875/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $117.88 (-2.6% / 24h). Decentralization: Nakamoto coefficient 18, 671 active validators, 0.1% of stake delinquent. Alpenglow readiness: validators holding 99% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 1 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 452,305,451 |
| Block height | 430,344,396 |
| Epoch | 1047 (0.34% complete, ~32.3h left) |
| TPS (10 min avg) | 5,229 |
| Non-vote TPS | 2,758 |
| Slot time (measured) | 270.1 ms |
| Est. daily transactions | 355,489,231 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0075 |
| Node version | 4.3.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $117.88 (-2.6%/24h) |
| Market cap | $69.3B |
| **REV (24h)** | **$1.3M** (fees $1.0M + Jito tips $209.5K) |
| Chain TVL | $6.5B |
| Stablecoin supply | $16.3B |
| DEX volume (24h) | $2.6B (1.4%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 588,076,454 SOL |
| Inflation | 3.62% |

Top DEXs by 24h volume: Orca DEX ($403.4M), BisonFi ($285.0M), Raydium AMM ($243.3M), PumpSwap ($207.0M), Meteora DLMM ($205.4M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 671 / 13 |
| Delinquent stake | 0.06% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.6% |
| Avg / median commission | 12.7% / 5% |
| Alpenglow BLS-key readiness | 704 validators, 99.4% of stake |

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

- **[SERIOUS]** TPS spike: 5,229 vs 12h mean 4,075 (z=+3.0)

## Solana Pulse — sentiment (experimental)

**67/100 — Bullish** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 71.4 |
| fear greed | 74 |
| momentum | 53.6 |
| news | 74 |

Crypto Fear & Greed: 74 (Greed) · CoinGecko votes bullish: 71.43% · headline tone (48h): +3

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 154 |
| Raydium AMM v4 | 140 |
| Orca Whirlpool | 154 |
| Pump.fun | 154 |
| Tensor | 0 |
| Magic Eden v2 | 54 |
| Marinade | 12 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 10,572,652 |
| Binance (cold) | 1,063,532 |
| OKX (attributed) | 387,517 |
| Coinbase (hot) | 12,755 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 270ms · proposal merged.
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
| solana_rpc | OK | 6982 ms |
| solana_rpc_validators | OK | 140 ms |
| coingecko | OK | 1998 ms |
| defillama_tvl | OK | 145 ms |
| defillama_dex | OK | 12452 ms |
| defillama_fees | OK | 2081 ms |
| defillama_stablecoins | OK | 133 ms |
| defillama_xstocks | OK | 50 ms |
| jito_kobe | OK | 369 ms |
| stakewiz | OK | 1387 ms |
| github | OK | 2052 ms |
| solana_com_news | OK | 120 ms |
| sentiment | OK | 2471 ms |
| solana_status_page | OK | 332 ms |
| solana_rpc_whales | OK | 903 ms |
| solana_rpc_programs | OK | 1732 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*