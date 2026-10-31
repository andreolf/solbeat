# Solbeat — State of the Solana Network

> Generated 2026-10-31T07:23:17Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1073 is 16% complete (~22h remaining), with the cluster processing ~998 TPS (998 non-vote). Measured slot time is 215ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $588.5K of Real Economic Value over the last 24h ($409/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $95.83 (-2.1% / 24h). Decentralization: Nakamoto coefficient 18, 665 active validators, 0.8% of stake delinquent. Alpenglow readiness: validators holding 100% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: all clear across every monitored metric.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 463,602,966 |
| Block height | 441,624,844 |
| Epoch | 1073 (15.5% complete, ~21.8h left) |
| TPS (10 min avg) | 998 |
| Non-vote TPS | 998 |
| Slot time (measured) | 214.9 ms |
| Confirmation time (measured) | 0.21 s |
| Finality time (measured) | 0.21 s — **Alpenglow active** |
| Est. daily transactions | 111,949,062 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0044 |
| Node version | 4.3.2 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $95.83 (-2.1%/24h) |
| Market cap | $56.6B |
| **REV (24h)** | **$588.5K** (fees $491.9K + Jito tips $96.6K) |
| Chain TVL | $5.4B |
| Stablecoin supply | $15.4B |
| DEX volume (24h) | $2.4B (4.5%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 590,095,190 SOL |
| Inflation | 3.58% |

Top DEXs by 24h volume: BisonFi ($301.3M), Orca DEX ($266.2M), PumpSwap ($221.7M), Tessera V ($209.3M), Scorch ($194.1M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 665 / 27 |
| Delinquent stake | 0.85% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.7% |
| Avg / median commission | 12.8% / 5% |
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

**50/100 — Neutral** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 75.0 |
| fear greed | 30 |
| momentum | 40.5 |
| news | 50 |

Crypto Fear & Greed: 30 (Fear) · CoinGecko votes bullish: 75.0% · headline tone (48h): +0

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 1,106 |
| Raydium AMM v4 | 637 |
| Orca Whirlpool | 1,500 |
| Pump.fun | 1,500 |
| Tensor | 0 |
| Magic Eden v2 | 78 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 11,890,003 |
| Binance (cold) | 4 |
| OKX (attributed) | 339,498 |
| Coinbase (hot) | 12,094 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 215ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 100.0% of stake.
- **Agave**: latest release v4.4.0 · running 4.3.2 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 10535 ms |
| solana_rpc_validators | OK | 283 ms |
| coingecko | OK | 1728 ms |
| defillama_tvl | OK | 81 ms |
| defillama_dex | OK | 2715 ms |
| defillama_fees | OK | 1144 ms |
| defillama_stablecoins | OK | 1214 ms |
| defillama_xstocks | FAILED | 779 ms |
| jito_kobe | OK | 463 ms |
| stakewiz | OK | 1475 ms |
| github | OK | 761 ms |
| solana_com_news | FAILED | 128 ms |
| sentiment | OK | 2486 ms |
| solana_status_page | OK | 272 ms |
| solana_rpc_whales | OK | 1294 ms |
| solana_rpc_programs | OK | 2154 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*