# Solbeat — State of the Solana Network

> Generated 2026-10-30T06:56:25Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1072 is 20% complete (~20h remaining), with the cluster processing ~969 TPS (969 non-vote). Measured slot time is 214ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $714.5K of Real Economic Value over the last 24h ($496/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $98.10 (-1.9% / 24h). Decentralization: Nakamoto coefficient 18, 666 active validators, 0.7% of stake delinquent. Alpenglow readiness: validators holding 100% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: all clear across every monitored metric.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 463,191,863 |
| Block height | 441,214,325 |
| Epoch | 1072 (20.34% complete, ~20.5h left) |
| TPS (10 min avg) | 969 |
| Non-vote TPS | 969 |
| Slot time (measured) | 214.1 ms |
| Confirmation time (measured) | 0.21 s |
| Finality time (measured) | 0.21 s — **Alpenglow active** |
| Est. daily transactions | 147,807,014 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0038 |
| Node version | 4.3.2 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $98.10 (-1.9%/24h) |
| Market cap | $57.8B |
| **REV (24h)** | **$714.5K** (fees $564.5K + Jito tips $150.0K) |
| Chain TVL | $5.4B |
| Stablecoin supply | $15.4B |
| DEX volume (24h) | $1.9B (11.0%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 590,039,962 SOL |
| Inflation | 3.58% |

Top DEXs by 24h volume: Orca DEX ($431.5M), Raydium AMM ($227.0M), Manifest Trade ($224.1M), BisonFi ($205.5M), Tessera V ($148.2M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 666 / 25 |
| Delinquent stake | 0.68% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.6% |
| Avg / median commission | 12.7% / 5.0% |
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

**51/100 — Neutral** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 74.2 |
| fear greed | 30 |
| momentum | 43.2 |
| news | 58 |

Crypto Fear & Greed: 30 (Fear) · CoinGecko votes bullish: 74.19% · headline tone (48h): +1

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 1,482 |
| Raydium AMM v4 | 746 |
| Orca Whirlpool | 1,482 |
| Pump.fun | 1,482 |
| Tensor | 0 |
| Magic Eden v2 | 250 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 11,890,003 |
| Binance (cold) | 4 |
| OKX (attributed) | 335,688 |
| Coinbase (hot) | 12,262 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 214ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 100.0% of stake.
- **Agave**: latest release v4.4.0 · running 4.3.2 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 9042 ms |
| solana_rpc_validators | OK | 328 ms |
| coingecko | OK | 1776 ms |
| defillama_tvl | OK | 88 ms |
| defillama_dex | OK | 1166 ms |
| defillama_fees | OK | 1442 ms |
| defillama_stablecoins | OK | 921 ms |
| defillama_xstocks | FAILED | 53 ms |
| jito_kobe | OK | 161 ms |
| stakewiz | OK | 1425 ms |
| github | OK | 1089 ms |
| solana_com_news | FAILED | 96 ms |
| sentiment | OK | 2332 ms |
| solana_status_page | OK | 488 ms |
| solana_rpc_whales | OK | 1076 ms |
| solana_rpc_programs | OK | 1583 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*