# Solbeat — State of the Solana Network

> Generated 2026-10-31T03:43:16Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1073 is 1% complete (~26h remaining), with the cluster processing ~1,279 TPS (1,279 non-vote). Measured slot time is 215ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $638.7K of Real Economic Value over the last 24h ($444/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $96.42 (-0.2% / 24h). Decentralization: Nakamoto coefficient 18, 664 active validators, 0.9% of stake delinquent. Alpenglow readiness: validators holding 100% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: all clear across every monitored metric.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 463,541,364 |
| Block height | 441,563,386 |
| Epoch | 1073 (1.24% complete, ~25.5h left) |
| TPS (10 min avg) | 1,279 |
| Non-vote TPS | 1,279 |
| Slot time (measured) | 214.9 ms |
| Confirmation time (measured) | 0.21 s |
| Finality time (measured) | 0.21 s — **Alpenglow active** |
| Est. daily transactions | 128,727,151 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0038 |
| Node version | 4.3.2 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $96.42 (-0.2%/24h) |
| Market cap | $56.9B |
| **REV (24h)** | **$638.7K** (fees $491.9K + Jito tips $146.9K) |
| Chain TVL | $5.4B |
| Stablecoin supply | $15.4B |
| DEX volume (24h) | $2.4B (4.5%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 590,095,335 SOL |
| Inflation | 3.58% |

Top DEXs by 24h volume: Orca DEX ($325.9M), BisonFi ($301.3M), PumpSwap ($221.7M), Tessera V ($209.3M), Scorch ($194.1M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 664 / 28 |
| Delinquent stake | 0.87% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.7% |
| Avg / median commission | 12.8% / 5.0% |
| Alpenglow BLS-key readiness | 679 validators, 100.0% of stake |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L43ZWjwCHART3o…` | 17,020,574 | 3.92% | 7% |
| 2 | `he1iusunGwqrNtafDtLd…` | 16,688,715 | 3.85% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5…` | 12,931,864 | 2.98% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxb…` | 10,425,467 | 2.4% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxA…` | 9,651,671 | 2.23% | 5% |
| 6 | `51JBzSTU5rAM8gLAVQKg…` | 9,449,481 | 2.18% | 10% |
| 7 | `26pV97Ce83ZQ6Kz9XT4t…` | 9,227,526 | 2.13% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2Fp…` | 7,778,595 | 1.79% | 7% |
| 9 | `DumiCKHVqoCQKD8roLAp…` | 7,000,338 | 1.61% | 0% |
| 10 | `CvSb7wdQAFpHuSpTYTJn…` | 6,976,145 | 1.61% | 5% |

## Signals (anomaly detection)

All clear — no anomalies across monitored metrics.

## Solana Pulse — sentiment (experimental)

**51/100 — Neutral** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 75.0 |
| fear greed | 30 |
| momentum | 41.0 |
| news | 58 |

Crypto Fear & Greed: 30 (Fear) · CoinGecko votes bullish: 75.0% · headline tone (48h): +1

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 1,500 |
| Raydium AMM v4 | 1,500 |
| Orca Whirlpool | 1,500 |
| Pump.fun | 1,500 |
| Tensor | 0 |
| Magic Eden v2 | 196 |
| Marinade | 3 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 11,890,003 |
| Binance (cold) | 4 |
| OKX (attributed) | 339,498 |
| Coinbase (hot) | 20,691 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 215ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 100.0% of stake.
- **Agave**: latest release v4.4.0 · running 4.3.2 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 11542 ms |
| solana_rpc_validators | OK | 309 ms |
| coingecko | OK | 1702 ms |
| defillama_tvl | OK | 213 ms |
| defillama_dex | OK | 941 ms |
| defillama_fees | OK | 1168 ms |
| defillama_stablecoins | OK | 684 ms |
| defillama_xstocks | FAILED | 649 ms |
| jito_kobe | OK | 290 ms |
| stakewiz | OK | 1144 ms |
| github | OK | 786 ms |
| solana_com_news | FAILED | 95 ms |
| sentiment | OK | 2284 ms |
| solana_status_page | OK | 427 ms |
| solana_rpc_whales | OK | 1169 ms |
| solana_rpc_programs | OK | 2047 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*