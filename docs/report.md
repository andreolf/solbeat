# Solbeat — State of the Solana Network

> Generated 2026-09-29T18:41:51Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1045 is 66% complete (~11h remaining), with the cluster processing ~5,043 TPS (2,522 non-vote). Measured slot time is 266ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $1.1M of Real Economic Value over the last 24h ($737/minute), computed as base + priority fees plus Jito MEV tips. Decentralization: Nakamoto coefficient 18, 674 active validators, 0.0% of stake delinquent. Alpenglow readiness: validators holding 99% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: all clear across every monitored metric.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 451,725,355 |
| Block height | 429,764,849 |
| Epoch | 1045 (66.05% complete, ~10.9h left) |
| TPS (10 min avg) | 5,043 |
| Non-vote TPS | 2,522 |
| Slot time (measured) | 266.4 ms |
| Est. daily transactions | 421,332,855 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0052 |
| Node version | 4.3.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $0.00 (+0.0%/24h) |
| Market cap | n/a |
| **REV (24h)** | **$1.1M** (fees $1.1M + Jito tips n/a) |
| Chain TVL | $6.5B |
| Stablecoin supply | $16.6B |
| DEX volume (24h) | $2.7B (38.2%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 587,851,534 SOL |
| Inflation | 3.63% |

Top DEXs by 24h volume: Orca DEX ($382.9M), BisonFi ($381.9M), PumpSwap ($268.4M), Raydium AMM ($250.5M), Meteora DLMM ($205.6M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 674 / 9 |
| Delinquent stake | 0.04% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.4% |
| Avg / median commission | 12.8% / 5.0% |
| Alpenglow BLS-key readiness | 703 validators, 99.4% of stake |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L43ZWjwCHART3o…` | 17,824,525 | 4.04% | 7% |
| 2 | `he1iusunGwqrNtafDtLd…` | 15,886,038 | 3.6% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5…` | 12,338,577 | 2.8% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxb…` | 11,300,554 | 2.56% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxA…` | 11,209,855 | 2.54% | 5% |
| 6 | `26pV97Ce83ZQ6Kz9XT4t…` | 9,243,744 | 2.09% | 7% |
| 7 | `51JBzSTU5rAM8gLAVQKg…` | 9,224,466 | 2.09% | 10% |
| 8 | `9QU2QSxhb24FUX3Tu2Fp…` | 7,637,468 | 1.73% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJn…` | 6,700,083 | 1.52% | 5% |
| 10 | `DumiCKHVqoCQKD8roLAp…` | 6,518,407 | 1.48% | 0% |

## Signals (anomaly detection)

All clear — no anomalies across monitored metrics.

## Solana Pulse — sentiment (experimental)

**79/100 — Bullish** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 76.5 |
| fear greed | 73 |
| news | 95 |

Crypto Fear & Greed: 73 (Greed) · CoinGecko votes bullish: 76.47% · headline tone (48h): +6

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 158 |
| Raydium AMM v4 | 158 |
| Orca Whirlpool | 158 |
| Pump.fun | 176 |
| Tensor | 0 |
| Magic Eden v2 | 81 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 10,772,652 |
| Binance (cold) | 935,141 |
| OKX (attributed) | 387,392 |
| Coinbase (hot) | 29,711 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 266ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 99.4% of stake.
- **Agave**: latest release v4.3.0 · running 4.3.0 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

### Latest ecosystem news (solana.com)

- [Slot Time Reduction Effects](https://solana.com/news/slot-time-reduction-effects) — Mon, 28 Sep 2026
- [Solana Foundation Appoints Rachel Conlan as Chief Strategy Officer and Jamal Raees as General Manager of Payments](https://solana.com/news/solana-foundation-appoints-2026) — Thu, 24 Sep 2026
- [Stocks Go Onchain: What the SEC's Innovation Exemption Means for Solana](https://solana.com/news/stocks-sec-innovation-exemption) — Wed, 23 Sep 2026
- [Solana Changelog: September 18, 2026](https://solana.com/news/solana-changelog-september-18-2026) — Sat, 19 Sep 2026
- [How AI Is Reshaping Crypto Security, with Michael Coates](https://solana.com/news/bits-to-bricks-crypto-security-michael-coates) — Sat, 19 Sep 2026
- [Breakpoint 2026: A guide to getting oriented (Part 1)](https://solana.com/news/breakpoint-guide-part1) — Fri, 18 Sep 2026

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 8263 ms |
| solana_rpc_validators | OK | 128 ms |
| coingecko | FAILED | 6197 ms |
| defillama_tvl | OK | 155 ms |
| defillama_dex | OK | 802 ms |
| defillama_fees | OK | 356 ms |
| defillama_stablecoins | OK | 234 ms |
| defillama_xstocks | OK | 12937 ms |
| jito_kobe | OK | 452 ms |
| stakewiz | OK | 772 ms |
| github | OK | 664 ms |
| solana_com_news | OK | 135 ms |
| sentiment | OK | 2138 ms |
| solana_status_page | OK | 275 ms |
| solana_rpc_whales | OK | 828 ms |
| solana_rpc_programs | OK | 1499 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*