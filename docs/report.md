# Solbeat — State of the Solana Network

> Generated 2026-10-03T23:38:09Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1048 is 80% complete (~6h remaining), with the cluster processing ~4,548 TPS (2,057 non-vote). Measured slot time is 268ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $1.4M of Real Economic Value over the last 24h ($973/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $119.71 (+1.0% / 24h). Decentralization: Nakamoto coefficient 18, 671 active validators, 0.0% of stake delinquent. Alpenglow readiness: validators holding 99% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: all clear across every monitored metric.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 453,083,516 |
| Block height | 431,121,992 |
| Epoch | 1048 (80.44% complete, ~6.3h left) |
| TPS (10 min avg) | 4,548 |
| Non-vote TPS | 2,057 |
| Slot time (measured) | 268.5 ms |
| Est. daily transactions | 413,435,430 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0055 |
| Node version | 4.3.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $119.71 (+1.0%/24h) |
| Market cap | $70.4B |
| **REV (24h)** | **$1.4M** (fees $1.1M + Jito tips $307.0K) |
| Chain TVL | $6.7B |
| Stablecoin supply | $16.9B |
| DEX volume (24h) | $2.8B (10.9%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 588,145,523 SOL |
| Inflation | 3.62% |

Top DEXs by 24h volume: BisonFi ($347.8M), PumpSwap ($321.1M), Meteora DLMM ($180.7M), pump.fun ($177.6M), Tessera V ($154.9M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 671 / 14 |
| Delinquent stake | 0.04% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.5% |
| Avg / median commission | 13.0% / 5% |
| Alpenglow BLS-key readiness | 703 validators, 99.4% of stake |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L43ZWjwCHART3o…` | 17,923,954 | 4.06% | 7% |
| 2 | `he1iusunGwqrNtafDtLd…` | 15,898,894 | 3.6% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5…` | 12,338,401 | 2.79% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxb…` | 11,304,108 | 2.56% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxA…` | 11,133,145 | 2.52% | 5% |
| 6 | `26pV97Ce83ZQ6Kz9XT4t…` | 9,247,324 | 2.09% | 7% |
| 7 | `51JBzSTU5rAM8gLAVQKg…` | 9,244,926 | 2.09% | 10% |
| 8 | `9QU2QSxhb24FUX3Tu2Fp…` | 7,605,153 | 1.72% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJn…` | 7,060,361 | 1.6% | 5% |
| 10 | `3JD3jMmnR6g88qff2WZ3…` | 6,684,213 | 1.51% | 0% |

## Signals (anomaly detection)

All clear — no anomalies across monitored metrics.

## Solana Pulse — sentiment (experimental)

**67/100 — Bullish** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 76.7 |
| fear greed | 67 |
| momentum | 54.6 |
| news | 74 |

Crypto Fear & Greed: 67 (Greed) · CoinGecko votes bullish: 76.67% · headline tone (48h): +3

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 134 |
| Raydium AMM v4 | 123 |
| Orca Whirlpool | 134 |
| Pump.fun | 163 |
| Tensor | 0 |
| Magic Eden v2 | 74 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 10,572,652 |
| Binance (cold) | 1,251,836 |
| OKX (attributed) | 307,939 |
| Coinbase (hot) | 14,060 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 268ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 99.4% of stake.
- **Agave**: latest release v4.3.0 · running 4.3.0 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

### Latest ecosystem news (solana.com)

- [Solana x AI: The Democratization Layer](https://solana.com/news/solana-ai-the-democratization-layer) — Fri, 02 Oct 2026
- [Open USD Is Live on Solana](https://solana.com/news/open-usd-is-live-on-solana) — Wed, 30 Sep 2026
- [Slot Time Reduction Effects](https://solana.com/news/slot-time-reduction-effects) — Mon, 28 Sep 2026
- [Solana Foundation Appoints Rachel Conlan as Chief Strategy Officer and Jamal Raees as General Manager of Payments](https://solana.com/news/solana-foundation-appoints-2026) — Thu, 24 Sep 2026
- [Stocks Go Onchain: What the SEC's Innovation Exemption Means for Solana](https://solana.com/news/stocks-sec-innovation-exemption) — Wed, 23 Sep 2026
- [Solana Changelog: September 18, 2026](https://solana.com/news/solana-changelog-september-18-2026) — Sat, 19 Sep 2026

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 7756 ms |
| solana_rpc_validators | OK | 224 ms |
| coingecko | OK | 1730 ms |
| defillama_tvl | OK | 39 ms |
| defillama_dex | OK | 1199 ms |
| defillama_fees | OK | 1363 ms |
| defillama_stablecoins | OK | 71 ms |
| defillama_xstocks | OK | 25 ms |
| jito_kobe | OK | 245 ms |
| stakewiz | OK | 1496 ms |
| github | OK | 744 ms |
| solana_com_news | OK | 42 ms |
| sentiment | OK | 2254 ms |
| solana_status_page | OK | 372 ms |
| solana_rpc_whales | OK | 944 ms |
| solana_rpc_programs | OK | 1809 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*