# Solbeat — State of the Solana Network

> Generated 2026-10-03T20:13:43Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1048 is 70% complete (~10h remaining), with the cluster processing ~5,194 TPS (2,704 non-vote). Measured slot time is 268ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $1.4M of Real Economic Value over the last 24h ($974/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $119.92 (+1.5% / 24h). Decentralization: Nakamoto coefficient 18, 670 active validators, 0.1% of stake delinquent. Alpenglow readiness: validators holding 99% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: all clear across every monitored metric.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 453,037,764 |
| Block height | 431,076,268 |
| Epoch | 1048 (69.85% complete, ~9.7h left) |
| TPS (10 min avg) | 5,194 |
| Non-vote TPS | 2,704 |
| Slot time (measured) | 268.1 ms |
| Est. daily transactions | 419,353,486 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0054 |
| Node version | 4.3.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $119.92 (+1.5%/24h) |
| Market cap | $70.5B |
| **REV (24h)** | **$1.4M** (fees $1.1M + Jito tips $308.0K) |
| Chain TVL | $6.7B |
| Stablecoin supply | $16.9B |
| DEX volume (24h) | $2.8B (10.9%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 588,145,675 SOL |
| Inflation | 3.62% |

Top DEXs by 24h volume: BisonFi ($347.8M), PumpSwap ($321.1M), Orca DEX ($197.5M), Meteora DLMM ($180.7M), pump.fun ($177.6M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 670 / 15 |
| Delinquent stake | 0.1% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.5% |
| Avg / median commission | 13.0% / 5.0% |
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

**64/100 — Bullish** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 66.7 |
| fear greed | 67 |
| momentum | 54.7 |
| news | 74 |

Crypto Fear & Greed: 67 (Greed) · CoinGecko votes bullish: 66.67% · headline tone (48h): +3

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 154 |
| Raydium AMM v4 | 140 |
| Orca Whirlpool | 128 |
| Pump.fun | 172 |
| Tensor | 0 |
| Magic Eden v2 | 76 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 10,572,652 |
| Binance (cold) | 1,259,196 |
| OKX (attributed) | 310,338 |
| Coinbase (hot) | 14,483 |

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
| solana_rpc | OK | 9618 ms |
| solana_rpc_validators | OK | 308 ms |
| coingecko | OK | 1693 ms |
| defillama_tvl | OK | 134 ms |
| defillama_dex | OK | 987 ms |
| defillama_fees | OK | 815 ms |
| defillama_stablecoins | OK | 273 ms |
| defillama_xstocks | OK | 69 ms |
| jito_kobe | OK | 388 ms |
| stakewiz | OK | 1144 ms |
| github | OK | 806 ms |
| solana_com_news | OK | 145 ms |
| sentiment | OK | 2264 ms |
| solana_status_page | OK | 287 ms |
| solana_rpc_whales | OK | 1210 ms |
| solana_rpc_programs | OK | 2203 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*