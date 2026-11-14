# Solbeat — State of the Solana Network

> Generated 2026-11-14T19:04:22Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1086 is 66% complete (~9h remaining), with the cluster processing ~1,632 TPS (1,632 non-vote). Measured slot time is 215ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $550.0K of Real Economic Value over the last 24h ($382/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $72.26 (-9.7% / 24h). Decentralization: Nakamoto coefficient 18, 662 active validators, 0.1% of stake delinquent. Alpenglow readiness: validators holding 100% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 5 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 469,438,320 |
| Block height | 447,453,391 |
| Epoch | 1086 (66.28% complete, ~8.7h left) |
| TPS (10 min avg) | 1,632 |
| Non-vote TPS | 1,632 |
| Slot time (measured) | 214.7 ms |
| Confirmation time (measured) | 0.21 s |
| Finality time (measured) | 0.21 s — **Alpenglow active** |
| Est. daily transactions | 168,277,580 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0027 |
| Node version | 4.4.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $72.26 (-9.7%/24h) |
| Market cap | $42.7B |
| **REV (24h)** | **$550.0K** (fees $448.8K + Jito tips $101.2K) |
| Chain TVL | $4.7B |
| Stablecoin supply | $14.1B |
| DEX volume (24h) | $1.6B (3.8%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 591,573,726 SOL |
| Inflation | 3.56% |

Top DEXs by 24h volume: Orca DEX ($228.3M), BisonFi ($186.9M), PumpSwap ($177.3M), Meteora DLMM ($164.8M), Raydium AMM ($123.9M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 662 / 37 |
| Delinquent stake | 0.12% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.7% |
| Avg / median commission | 12.9% / 5.0% |
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

- **[WARNING]** SOL price contraction (z=-2.8 vs its recent baseline)
- **[WARNING]** Solana TVL contraction (z=-2.5 vs its recent baseline)
- **[WARNING]** Stablecoin supply contraction (z=-2.3 vs its recent baseline)
- **[WARNING · market_move]** Market-wide move: SOL price anomaly accompanied by liquidity/volume shifts — an ecosystem-level repricing rather than an isolated metric.
- **[WARNING · liquidity_rotation]** Stablecoin supply and TVL moving together — capital rotating in or out of the chain.

## Solana Pulse — sentiment (experimental)

**39/100 — Bearish** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 65.6 |
| fear greed | 13 |
| momentum | 27.2 |
| news | 50 |

Crypto Fear & Greed: 13 (Extreme Fear) · CoinGecko votes bullish: 65.63% · headline tone (48h): +0

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 1,500 |
| Raydium AMM v4 | 760 |
| Orca Whirlpool | 1,500 |
| Pump.fun | 1,500 |
| Tensor | 0 |
| Magic Eden v2 | 65 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,300,003 |
| Binance (cold) | 66 |
| OKX (attributed) | 8,975 |
| Coinbase (hot) | 94,663 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 215ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 100.0% of stake.
- **Agave**: latest release v4.4.1 · running 4.4.0 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 9261 ms |
| solana_rpc_validators | OK | 217 ms |
| coingecko | OK | 1659 ms |
| defillama_tvl | OK | 231 ms |
| defillama_dex | OK | 1243 ms |
| defillama_fees | OK | 1926 ms |
| defillama_stablecoins | OK | 643 ms |
| defillama_xstocks | FAILED | 22 ms |
| jito_kobe | OK | 112 ms |
| stakewiz | OK | 1396 ms |
| github | OK | 721 ms |
| solana_com_news | FAILED | 81 ms |
| sentiment | OK | 2270 ms |
| solana_status_page | OK | 244 ms |
| solana_rpc_whales | OK | 1038 ms |
| solana_rpc_programs | OK | 1813 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*