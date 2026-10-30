# Solbeat — State of the Solana Network

> Generated 2026-10-30T08:29:14Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1072 is 26% complete (~19h remaining), with the cluster processing ~1,268 TPS (1,268 non-vote). Measured slot time is 214ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $713.4K of Real Economic Value over the last 24h ($495/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $97.22 (-2.7% / 24h). Decentralization: Nakamoto coefficient 18, 665 active validators, 0.7% of stake delinquent. Alpenglow readiness: validators holding 100% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: all clear across every monitored metric.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 463,217,923 |
| Block height | 441,240,358 |
| Epoch | 1072 (26.37% complete, ~18.9h left) |
| TPS (10 min avg) | 1,268 |
| Non-vote TPS | 1,268 |
| Slot time (measured) | 213.7 ms |
| Confirmation time (measured) | 0.21 s |
| Finality time (measured) | 0.21 s — **Alpenglow active** |
| Est. daily transactions | 131,191,431 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0043 |
| Node version | 4.3.2 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $97.22 (-2.7%/24h) |
| Market cap | $57.4B |
| **REV (24h)** | **$713.4K** (fees $564.5K + Jito tips $148.9K) |
| Chain TVL | $5.4B |
| Stablecoin supply | $15.4B |
| DEX volume (24h) | $1.9B (11.0%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 590,039,945 SOL |
| Inflation | 3.58% |

Top DEXs by 24h volume: Orca DEX ($431.5M), Manifest Trade ($231.3M), Raydium AMM ($227.0M), BisonFi ($205.5M), Tessera V ($148.2M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 665 / 26 |
| Delinquent stake | 0.7% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.6% |
| Avg / median commission | 12.8% / 5% |
| Alpenglow BLS-key readiness | 679 validators, 100.0% of stake |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L43ZWjwCHART3o…` | 16,965,456 | 3.9% | 7% |
| 2 | `he1iusunGwqrNtafDtLd…` | 16,678,000 | 3.83% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5…` | 12,919,680 | 2.97% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxb…` | 10,502,229 | 2.41% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxA…` | 9,659,910 | 2.22% | 5% |
| 6 | `51JBzSTU5rAM8gLAVQKg…` | 9,473,552 | 2.18% | 10% |
| 7 | `26pV97Ce83ZQ6Kz9XT4t…` | 9,222,406 | 2.12% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2Fp…` | 7,780,140 | 1.79% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJn…` | 7,045,150 | 1.62% | 5% |
| 10 | `DumiCKHVqoCQKD8roLAp…` | 7,001,506 | 1.61% | 0% |

## Signals (anomaly detection)

All clear — no anomalies across monitored metrics.

## Solana Pulse — sentiment (experimental)

**52/100 — Neutral** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 76.7 |
| fear greed | 30 |
| momentum | 42.8 |
| news | 58 |

Crypto Fear & Greed: 30 (Fear) · CoinGecko votes bullish: 76.67% · headline tone (48h): +1

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 1,412 |
| Raydium AMM v4 | 369 |
| Orca Whirlpool | 1,412 |
| Pump.fun | 1,500 |
| Tensor | 0 |
| Magic Eden v2 | 93 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 11,890,003 |
| Binance (cold) | 4 |
| OKX (attributed) | 337,735 |
| Coinbase (hot) | 17,215 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 214ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 100.0% of stake.
- **Agave**: latest release v4.4.0 · running 4.3.2 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 9978 ms |
| solana_rpc_validators | OK | 394 ms |
| coingecko | OK | 1781 ms |
| defillama_tvl | OK | 167 ms |
| defillama_dex | OK | 996 ms |
| defillama_fees | OK | 199 ms |
| defillama_stablecoins | OK | 221 ms |
| defillama_xstocks | FAILED | 734 ms |
| jito_kobe | OK | 268 ms |
| stakewiz | OK | 1275 ms |
| github | OK | 900 ms |
| solana_com_news | FAILED | 127 ms |
| sentiment | OK | 2318 ms |
| solana_status_page | OK | 422 ms |
| solana_rpc_whales | OK | 1216 ms |
| solana_rpc_programs | OK | 2252 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*