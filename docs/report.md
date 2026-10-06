# Solbeat — State of the Solana Network

> Generated 2026-10-06T02:34:57Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1050 is 39% complete (~20h remaining), with the cluster processing ~4,454 TPS (1,961 non-vote). Measured slot time is 268ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $1.3M of Real Economic Value over the last 24h ($892/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $120.55 (-0.6% / 24h). Decentralization: Nakamoto coefficient 18, 672 active validators, 0.0% of stake delinquent. Alpenglow readiness: validators holding 99% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: all clear across every monitored metric.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 453,768,370 |
| Block height | 431,806,225 |
| Epoch | 1050 (38.97% complete, ~19.7h left) |
| TPS (10 min avg) | 4,454 |
| Non-vote TPS | 1,961 |
| Slot time (measured) | 268.5 ms |
| Est. daily transactions | 395,341,314 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0058 |
| Node version | 4.3.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $120.55 (-0.6%/24h) |
| Market cap | $70.9B |
| **REV (24h)** | **$1.3M** (fees $1.0M + Jito tips $244.4K) |
| Chain TVL | $6.8B |
| Stablecoin supply | $17.0B |
| DEX volume (24h) | $1.9B (11.5%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 588,385,707 SOL |
| Inflation | 3.62% |

Top DEXs by 24h volume: PumpSwap ($306.6M), Orca DEX ($294.9M), BisonFi ($236.7M), pump.fun ($184.2M), Raydium AMM ($174.2M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 672 / 13 |
| Delinquent stake | 0.02% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.6% |
| Avg / median commission | 12.7% / 5.0% |
| Alpenglow BLS-key readiness | 703 validators, 99.4% of stake |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L43ZWjwCHART3o…` | 17,915,070 | 4.06% | 7% |
| 2 | `he1iusunGwqrNtafDtLd…` | 15,937,333 | 3.61% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5…` | 12,292,997 | 2.78% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxb…` | 11,310,013 | 2.56% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxA…` | 11,144,638 | 2.52% | 5% |
| 6 | `26pV97Ce83ZQ6Kz9XT4t…` | 9,258,566 | 2.1% | 7% |
| 7 | `51JBzSTU5rAM8gLAVQKg…` | 9,254,450 | 2.1% | 10% |
| 8 | `9QU2QSxhb24FUX3Tu2Fp…` | 7,629,486 | 1.73% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJn…` | 7,062,716 | 1.6% | 5% |
| 10 | `3JD3jMmnR6g88qff2WZ3…` | 6,687,904 | 1.51% | 0% |

## Signals (anomaly detection)

All clear — no anomalies across monitored metrics.

## Solana Pulse — sentiment (experimental)

**72/100 — Bullish** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 82.3 |
| fear greed | 73 |
| momentum | 62.2 |
| news | 66 |

Crypto Fear & Greed: 73 (Greed) · CoinGecko votes bullish: 82.35% · headline tone (48h): +2

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 147 |
| Raydium AMM v4 | 134 |
| Orca Whirlpool | 163 |
| Pump.fun | 163 |
| Tensor | 0 |
| Magic Eden v2 | 106 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 10,572,652 |
| Binance (cold) | 1,222,869 |
| OKX (attributed) | 303,366 |
| Coinbase (hot) | 7,470 |

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
| solana_rpc | OK | 8750 ms |
| solana_rpc_validators | OK | 377 ms |
| coingecko | OK | 1714 ms |
| defillama_tvl | OK | 141 ms |
| defillama_dex | OK | 916 ms |
| defillama_fees | OK | 1130 ms |
| defillama_stablecoins | OK | 540 ms |
| defillama_xstocks | OK | 54 ms |
| jito_kobe | OK | 220 ms |
| stakewiz | OK | 1142 ms |
| github | OK | 860 ms |
| solana_com_news | OK | 97 ms |
| sentiment | OK | 2226 ms |
| solana_status_page | OK | 564 ms |
| solana_rpc_whales | OK | 1172 ms |
| solana_rpc_programs | OK | 2166 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*