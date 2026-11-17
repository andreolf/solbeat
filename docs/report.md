# Solbeat — State of the Solana Network

> Generated 2026-11-17T09:16:06Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1089 is 7% complete (~24h remaining), with the cluster processing ~999 TPS (999 non-vote). Measured slot time is 214ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $569.0K of Real Economic Value over the last 24h ($395/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $72.19 (+2.4% / 24h). Decentralization: Nakamoto coefficient 18, 661 active validators, 0.0% of stake delinquent. Alpenglow readiness: validators holding 100% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 3 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 470,480,072 |
| Block height | 448,494,898 |
| Epoch | 1089 (7.42% complete, ~23.8h left) |
| TPS (10 min avg) | 999 |
| Non-vote TPS | 999 |
| Slot time (measured) | 214.4 ms |
| Confirmation time (measured) | 0.21 s |
| Finality time (measured) | 0.21 s — **Alpenglow active** |
| Est. daily transactions | 118,891,345 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0038 |
| Node version | 4.4.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $72.19 (+2.4%/24h) |
| Market cap | $42.7B |
| **REV (24h)** | **$569.0K** (fees $446.3K + Jito tips $122.7K) |
| Chain TVL | $4.8B |
| Stablecoin supply | $14.3B |
| DEX volume (24h) | $1.4B (3.4%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 591,739,785 SOL |
| Inflation | 3.55% |

Top DEXs by 24h volume: Orca DEX ($207.4M), BisonFi ($158.8M), PumpSwap ($157.2M), Raydium AMM ($120.1M), Meteora DLMM ($119.7M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 661 / 5 |
| Delinquent stake | 0.01% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.8% |
| Avg / median commission | 12.7% / 5% |
| Alpenglow BLS-key readiness | 686 validators, 100.0% of stake |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `he1iusunGwqrNtafDtLd…` | 16,834,343 | 3.93% | 0% |
| 2 | `CcaHc2L43ZWjwCHART3o…` | 16,442,668 | 3.83% | 7% |
| 3 | `3N7s9zXMZ4QqvHQR15t5…` | 12,432,778 | 2.9% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxb…` | 10,144,846 | 2.37% | 0% |
| 5 | `51JBzSTU5rAM8gLAVQKg…` | 9,802,677 | 2.29% | 10% |
| 6 | `CatzoSMUkTRidT5DwBxA…` | 9,625,021 | 2.24% | 5% |
| 7 | `26pV97Ce83ZQ6Kz9XT4t…` | 9,218,745 | 2.15% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2Fp…` | 7,970,891 | 1.86% | 7% |
| 9 | `DumiCKHVqoCQKD8roLAp…` | 6,996,288 | 1.63% | 0% |
| 10 | `CvSb7wdQAFpHuSpTYTJn…` | 6,730,472 | 1.57% | 5% |

## Signals (anomaly detection)

- **[WARNING]** SOL price contraction (z=-2.3 vs its recent baseline)
- **[WARNING]** Solana TVL contraction (z=-2.3 vs its recent baseline)
- **[WARNING · market_move]** Market-wide move: SOL price anomaly accompanied by liquidity/volume shifts — an ecosystem-level repricing rather than an isolated metric.

## Solana Pulse — sentiment (experimental)

**42/100 — Neutral** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 69.0 |
| fear greed | 12 |
| momentum | 32.7 |
| news | 58 |

Crypto Fear & Greed: 12 (Extreme Fear) · CoinGecko votes bullish: 68.97% · headline tone (48h): +1

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 1,083 |
| Raydium AMM v4 | 443 |
| Orca Whirlpool | 1,083 |
| Pump.fun | 1,500 |
| Tensor | 0 |
| Magic Eden v2 | 70 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,300,003 |
| Binance (cold) | 66 |
| OKX (attributed) | 67,900 |
| Coinbase (hot) | 29,451 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 214ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 100.0% of stake.
- **Agave**: latest release v4.4.1 · running 4.4.0 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 8987 ms |
| solana_rpc_validators | OK | 220 ms |
| coingecko | OK | 1688 ms |
| defillama_tvl | OK | 48 ms |
| defillama_dex | OK | 52 ms |
| defillama_fees | OK | 1367 ms |
| defillama_stablecoins | OK | 1326 ms |
| defillama_xstocks | FAILED | 30 ms |
| jito_kobe | OK | 214 ms |
| stakewiz | OK | 1008 ms |
| github | OK | 795 ms |
| solana_com_news | FAILED | 76 ms |
| sentiment | OK | 2260 ms |
| solana_status_page | OK | 371 ms |
| solana_rpc_whales | OK | 1044 ms |
| solana_rpc_programs | OK | 2122 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*