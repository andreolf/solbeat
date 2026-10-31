# Solbeat — State of the Solana Network

> Generated 2026-10-31T08:24:15Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1073 is 19% complete (~21h remaining), with the cluster processing ~1,040 TPS (1,040 non-vote). Measured slot time is 215ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $588.3K of Real Economic Value over the last 24h ($409/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $95.52 (-1.9% / 24h). Decentralization: Nakamoto coefficient 18, 664 active validators, 0.9% of stake delinquent. Alpenglow readiness: validators holding 100% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: all clear across every monitored metric.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 463,620,035 |
| Block height | 441,641,909 |
| Epoch | 1073 (19.45% complete, ~20.8h left) |
| TPS (10 min avg) | 1,040 |
| Non-vote TPS | 1,040 |
| Slot time (measured) | 214.7 ms |
| Confirmation time (measured) | 0.21 s |
| Finality time (measured) | 0.21 s — **Alpenglow active** |
| Est. daily transactions | 106,954,155 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0046 |
| Node version | 4.3.2 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $95.52 (-1.9%/24h) |
| Market cap | $56.4B |
| **REV (24h)** | **$588.3K** (fees $491.9K + Jito tips $96.4K) |
| Chain TVL | $5.4B |
| Stablecoin supply | $15.4B |
| DEX volume (24h) | $2.4B (4.5%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 590,095,180 SOL |
| Inflation | 3.58% |

Top DEXs by 24h volume: BisonFi ($301.3M), Orca DEX ($266.2M), PumpSwap ($221.7M), Tessera V ($209.3M), Scorch ($194.1M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 664 / 28 |
| Delinquent stake | 0.86% |
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

**49/100 — Neutral** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 74.1 |
| fear greed | 30 |
| momentum | 40.0 |
| news | 50 |

Crypto Fear & Greed: 30 (Fear) · CoinGecko votes bullish: 74.07% · headline tone (48h): +0

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 732 |
| Raydium AMM v4 | 732 |
| Orca Whirlpool | 1,430 |
| Pump.fun | 1,500 |
| Tensor | 0 |
| Magic Eden v2 | 68 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 11,890,003 |
| Binance (cold) | 4 |
| OKX (attributed) | 339,498 |
| Coinbase (hot) | 11,938 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 215ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 100.0% of stake.
- **Agave**: latest release v4.4.0 · running 4.3.2 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 9752 ms |
| solana_rpc_validators | OK | 237 ms |
| coingecko | OK | 1693 ms |
| defillama_tvl | OK | 54 ms |
| defillama_dex | OK | 1239 ms |
| defillama_fees | OK | 1090 ms |
| defillama_stablecoins | OK | 1170 ms |
| defillama_xstocks | FAILED | 776 ms |
| jito_kobe | OK | 333 ms |
| stakewiz | OK | 1403 ms |
| github | OK | 665 ms |
| solana_com_news | FAILED | 92 ms |
| sentiment | OK | 2270 ms |
| solana_status_page | OK | 302 ms |
| solana_rpc_whales | OK | 1204 ms |
| solana_rpc_programs | OK | 2112 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*