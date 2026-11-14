# Solbeat — State of the Solana Network

> Generated 2026-11-14T14:39:23Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1086 is 49% complete (~13h remaining), with the cluster processing ~2,101 TPS (2,101 non-vote). Measured slot time is 217ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $551.3K of Real Economic Value over the last 24h ($383/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $73.91 (-8.7% / 24h). Decentralization: Nakamoto coefficient 18, 662 active validators, 0.1% of stake delinquent. Alpenglow readiness: validators holding 100% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 6 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 469,364,463 |
| Block height | 447,379,554 |
| Epoch | 1086 (49.18% complete, ~13.2h left) |
| TPS (10 min avg) | 2,101 |
| Non-vote TPS | 2,101 |
| Slot time (measured) | 216.7 ms |
| Confirmation time (measured) | 0.22 s |
| Finality time (measured) | 0.22 s — **Alpenglow active** |
| Est. daily transactions | 108,255,983 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0041 |
| Node version | 4.4.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $73.91 (-8.7%/24h) |
| Market cap | $43.7B |
| **REV (24h)** | **$551.3K** (fees $448.8K + Jito tips $102.6K) |
| Chain TVL | $4.8B |
| Stablecoin supply | $14.1B |
| DEX volume (24h) | $1.6B (3.8%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 591,573,813 SOL |
| Inflation | 3.56% |

Top DEXs by 24h volume: Orca DEX ($228.3M), BisonFi ($186.9M), PumpSwap ($177.3M), Meteora DLMM ($164.8M), Raydium AMM ($110.1M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 662 / 37 |
| Delinquent stake | 0.09% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.7% |
| Avg / median commission | 12.7% / 5.0% |
| Alpenglow BLS-key readiness | 685 validators, 100.0% of stake |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `he1iusunGwqrNtafDtLd…` | 16,955,905 | 3.95% | 0% |
| 2 | `CcaHc2L43ZWjwCHART3o…` | 16,374,909 | 3.81% | 7% |
| 3 | `3N7s9zXMZ4QqvHQR15t5…` | 12,611,498 | 2.94% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxb…` | 10,140,468 | 2.36% | 0% |
| 5 | `51JBzSTU5rAM8gLAVQKg…` | 9,736,890 | 2.27% | 10% |
| 6 | `CatzoSMUkTRidT5DwBxA…` | 9,574,439 | 2.23% | 5% |
| 7 | `26pV97Ce83ZQ6Kz9XT4t…` | 9,199,377 | 2.14% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2Fp…` | 7,914,792 | 1.84% | 7% |
| 9 | `DumiCKHVqoCQKD8roLAp…` | 6,990,062 | 1.63% | 0% |
| 10 | `CvSb7wdQAFpHuSpTYTJn…` | 6,707,745 | 1.56% | 5% |

## Signals (anomaly detection)

- **[WARNING]** TPS spike: 2,101 vs 12h mean 1,236 (z=+2.9)
- **[WARNING]** SOL price contraction (z=-2.6 vs its recent baseline)
- **[WARNING]** Solana TVL contraction (z=-2.3 vs its recent baseline)
- **[WARNING]** Stablecoin supply contraction (z=-2.3 vs its recent baseline)
- **[WARNING · market_move]** Market-wide move: SOL price anomaly accompanied by liquidity/volume shifts — an ecosystem-level repricing rather than an isolated metric.
- **[WARNING · liquidity_rotation]** Stablecoin supply and TVL moving together — capital rotating in or out of the chain.

## Solana Pulse — sentiment (experimental)

**42/100 — Neutral** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 67.8 |
| fear greed | 13 |
| momentum | 28.8 |
| news | 66 |

Crypto Fear & Greed: 13 (Extreme Fear) · CoinGecko votes bullish: 67.8% · headline tone (48h): +2

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 1,032 |
| Raydium AMM v4 | 1,500 |
| Orca Whirlpool | 1,500 |
| Pump.fun | 1,500 |
| Tensor | 0 |
| Magic Eden v2 | 16 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,300,003 |
| Binance (cold) | 66 |
| OKX (attributed) | 40,072 |
| Coinbase (hot) | 97,359 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 217ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 100.0% of stake.
- **Agave**: latest release v4.4.1 · running 4.4.0 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 10271 ms |
| solana_rpc_validators | OK | 306 ms |
| coingecko | OK | 1650 ms |
| defillama_tvl | OK | 471 ms |
| defillama_dex | OK | 920 ms |
| defillama_fees | OK | 707 ms |
| defillama_stablecoins | OK | 312 ms |
| defillama_xstocks | FAILED | 663 ms |
| jito_kobe | OK | 323 ms |
| stakewiz | OK | 1119 ms |
| github | OK | 779 ms |
| solana_com_news | FAILED | 82 ms |
| sentiment | OK | 2283 ms |
| solana_status_page | OK | 338 ms |
| solana_rpc_whales | OK | 1153 ms |
| solana_rpc_programs | OK | 2071 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*