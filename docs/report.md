# Solbeat — State of the Solana Network

> Generated 2026-11-14T16:11:47Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1086 is 55% complete (~11h remaining), with the cluster processing ~1,787 TPS (1,787 non-vote). Measured slot time is 213ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $552.4K of Real Economic Value over the last 24h ($384/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $73.29 (-8.3% / 24h). Decentralization: Nakamoto coefficient 18, 662 active validators, 0.1% of stake delinquent. Alpenglow readiness: validators holding 100% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 5 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 469,390,249 |
| Block height | 447,405,332 |
| Epoch | 1086 (55.15% complete, ~11.4h left) |
| TPS (10 min avg) | 1,787 |
| Non-vote TPS | 1,787 |
| Slot time (measured) | 212.7 ms |
| Confirmation time (measured) | 0.21 s |
| Finality time (measured) | 0.21 s — **Alpenglow active** |
| Est. daily transactions | 116,763,088 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0038 |
| Node version | 4.4.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $73.29 (-8.3%/24h) |
| Market cap | $43.3B |
| **REV (24h)** | **$552.4K** (fees $448.8K + Jito tips $103.6K) |
| Chain TVL | $4.8B |
| Stablecoin supply | $14.1B |
| DEX volume (24h) | $1.6B (3.8%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 591,573,784 SOL |
| Inflation | 3.56% |

Top DEXs by 24h volume: Orca DEX ($228.3M), BisonFi ($186.9M), PumpSwap ($177.3M), Meteora DLMM ($164.8M), Raydium AMM ($113.8M)

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

- **[WARNING]** SOL price contraction (z=-2.7 vs its recent baseline)
- **[WARNING]** Solana TVL contraction (z=-2.3 vs its recent baseline)
- **[WARNING]** Stablecoin supply contraction (z=-2.3 vs its recent baseline)
- **[WARNING · market_move]** Market-wide move: SOL price anomaly accompanied by liquidity/volume shifts — an ecosystem-level repricing rather than an isolated metric.
- **[WARNING · liquidity_rotation]** Stablecoin supply and TVL moving together — capital rotating in or out of the chain.

## Solana Pulse — sentiment (experimental)

**41/100 — Neutral** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 69.8 |
| fear greed | 13 |
| momentum | 28.4 |
| news | 58 |

Crypto Fear & Greed: 13 (Extreme Fear) · CoinGecko votes bullish: 69.84% · headline tone (48h): +1

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 1,500 |
| Raydium AMM v4 | 1,500 |
| Orca Whirlpool | 1,500 |
| Pump.fun | 1,500 |
| Tensor | 0 |
| Magic Eden v2 | 46 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,300,003 |
| Binance (cold) | 66 |
| OKX (attributed) | 23,115 |
| Coinbase (hot) | 96,618 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 213ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 100.0% of stake.
- **Agave**: latest release v4.4.1 · running 4.4.0 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 8546 ms |
| solana_rpc_validators | OK | 97 ms |
| coingecko | OK | 1567 ms |
| defillama_tvl | OK | 28 ms |
| defillama_dex | OK | 29 ms |
| defillama_fees | OK | 51 ms |
| defillama_stablecoins | OK | 43 ms |
| defillama_xstocks | FAILED | 22 ms |
| jito_kobe | OK | 90 ms |
| stakewiz | OK | 648 ms |
| github | OK | 562 ms |
| solana_com_news | FAILED | 38 ms |
| sentiment | OK | 2211 ms |
| solana_status_page | OK | 47 ms |
| solana_rpc_whales | OK | 788 ms |
| solana_rpc_programs | OK | 1365 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*