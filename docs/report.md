# Solbeat — State of the Solana Network

> Generated 2026-10-04T01:46:20Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1048 is 87% complete (~4h remaining), with the cluster processing ~4,213 TPS (1,695 non-vote). Measured slot time is 266ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $1.4M of Real Economic Value over the last 24h ($976/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $120.00 (+0.6% / 24h). Decentralization: Nakamoto coefficient 18, 671 active validators, 0.0% of stake delinquent. Alpenglow readiness: validators holding 99% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: all clear across every monitored metric.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 453,112,294 |
| Block height | 431,150,750 |
| Epoch | 1048 (87.11% complete, ~4.1h left) |
| TPS (10 min avg) | 4,213 |
| Non-vote TPS | 1,695 |
| Slot time (measured) | 265.5 ms |
| Est. daily transactions | 396,115,212 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0061 |
| Node version | 4.3.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $120.00 (+0.6%/24h) |
| Market cap | $70.6B |
| **REV (24h)** | **$1.4M** (fees $1.1M + Jito tips $311.2K) |
| Chain TVL | $6.6B |
| Stablecoin supply | $16.8B |
| DEX volume (24h) | $2.1B (-22.8%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 588,145,432 SOL |
| Inflation | 3.62% |

Top DEXs by 24h volume: PumpSwap ($402.0M), BisonFi ($347.8M), pump.fun ($177.6M), Tessera V ($154.9M), fomo Wallet ($135.3M)

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

**60/100 — Bullish** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 77.4 |
| fear greed | 65 |
| momentum | 36.9 |
| news | 66 |

Crypto Fear & Greed: 65 (Greed) · CoinGecko votes bullish: 77.42% · headline tone (48h): +2

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 149 |
| Raydium AMM v4 | 135 |
| Orca Whirlpool | 165 |
| Pump.fun | 165 |
| Tensor | 0 |
| Magic Eden v2 | 48 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 10,572,652 |
| Binance (cold) | 1,246,233 |
| OKX (attributed) | 307,939 |
| Coinbase (hot) | 13,875 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 266ms · proposal merged.
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
| solana_rpc | OK | 7575 ms |
| solana_rpc_validators | OK | 247 ms |
| coingecko | OK | 1697 ms |
| defillama_tvl | OK | 37 ms |
| defillama_dex | OK | 1067 ms |
| defillama_fees | OK | 2843 ms |
| defillama_stablecoins | OK | 633 ms |
| defillama_xstocks | OK | 27 ms |
| jito_kobe | OK | 218 ms |
| stakewiz | OK | 1486 ms |
| github | OK | 789 ms |
| solana_com_news | OK | 36 ms |
| sentiment | OK | 2128 ms |
| solana_status_page | OK | 363 ms |
| solana_rpc_whales | OK | 990 ms |
| solana_rpc_programs | OK | 1820 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*