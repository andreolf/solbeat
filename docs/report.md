# Solbeat — State of the Solana Network

> Generated 2026-11-16T11:39:55Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1088 is 24% complete (~20h remaining), with the cluster processing ~1,318 TPS (1,318 non-vote). Measured slot time is 213ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $452.2K of Real Economic Value over the last 24h ($314/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $71.54 (-1.4% / 24h). Decentralization: Nakamoto coefficient 18, 662 active validators, 0.0% of stake delinquent. Alpenglow readiness: validators holding 100% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 3 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 470,118,027 |
| Block height | 448,132,914 |
| Epoch | 1088 (23.62% complete, ~19.5h left) |
| TPS (10 min avg) | 1,318 |
| Non-vote TPS | 1,318 |
| Slot time (measured) | 212.8 ms |
| Confirmation time (measured) | 0.21 s |
| Finality time (measured) | 0.21 s — **Alpenglow active** |
| Est. daily transactions | 117,003,585 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0030 |
| Node version | 4.4.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $71.54 (-1.4%/24h) |
| Market cap | $42.3B |
| **REV (24h)** | **$452.2K** (fees $353.0K + Jito tips $99.2K) |
| Chain TVL | $4.7B |
| Stablecoin supply | $14.3B |
| DEX volume (24h) | $1.5B (-13.4%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 591,684,500 SOL |
| Inflation | 3.55% |

Top DEXs by 24h volume: BisonFi ($236.7M), Orca DEX ($175.1M), Meteora DLMM ($154.9M), PumpSwap ($142.8M), Raydium AMM ($113.4M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 662 / 37 |
| Delinquent stake | 0.04% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.8% |
| Avg / median commission | 12.6% / 5.0% |
| Alpenglow BLS-key readiness | 687 validators, 100.0% of stake |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `he1iusunGwqrNtafDtLd…` | 16,936,855 | 3.95% | 0% |
| 2 | `CcaHc2L43ZWjwCHART3o…` | 16,432,361 | 3.83% | 7% |
| 3 | `3N7s9zXMZ4QqvHQR15t5…` | 12,486,687 | 2.91% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxb…` | 10,142,842 | 2.36% | 0% |
| 5 | `51JBzSTU5rAM8gLAVQKg…` | 9,787,748 | 2.28% | 10% |
| 6 | `CatzoSMUkTRidT5DwBxA…` | 9,620,150 | 2.24% | 5% |
| 7 | `26pV97Ce83ZQ6Kz9XT4t…` | 9,212,350 | 2.15% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2Fp…` | 7,959,108 | 1.85% | 7% |
| 9 | `DumiCKHVqoCQKD8roLAp…` | 6,992,227 | 1.63% | 0% |
| 10 | `CvSb7wdQAFpHuSpTYTJn…` | 6,709,566 | 1.56% | 5% |

## Signals (anomaly detection)

- **[WARNING]** SOL price contraction (z=-2.5 vs its recent baseline)
- **[WARNING]** Solana TVL contraction (z=-2.6 vs its recent baseline)
- **[WARNING · market_move]** Market-wide move: SOL price anomaly accompanied by liquidity/volume shifts — an ecosystem-level repricing rather than an isolated metric.

## Solana Pulse — sentiment (experimental)

**38/100 — Bearish** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 67.9 |
| fear greed | 10 |
| momentum | 19.8 |
| news | 58 |

Crypto Fear & Greed: 10 (Extreme Fear) · CoinGecko votes bullish: 67.92% · headline tone (48h): +1

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 1,223 |
| Raydium AMM v4 | 674 |
| Orca Whirlpool | 1,223 |
| Pump.fun | 1,500 |
| Tensor | 0 |
| Magic Eden v2 | 74 |
| Marinade | 1 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,300,003 |
| Binance (cold) | 66 |
| OKX (attributed) | 67,833 |
| Coinbase (hot) | 37,332 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 213ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 100.0% of stake.
- **Agave**: latest release v4.4.1 · running 4.4.0 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 10878 ms |
| solana_rpc_validators | OK | 273 ms |
| coingecko | OK | 1793 ms |
| defillama_tvl | OK | 71 ms |
| defillama_dex | OK | 548 ms |
| defillama_fees | OK | 940 ms |
| defillama_stablecoins | OK | 96 ms |
| defillama_xstocks | FAILED | 526 ms |
| jito_kobe | OK | 122 ms |
| stakewiz | OK | 699 ms |
| github | OK | 1593 ms |
| solana_com_news | FAILED | 72 ms |
| sentiment | OK | 2004 ms |
| solana_status_page | OK | 200 ms |
| solana_rpc_whales | OK | 1056 ms |
| solana_rpc_programs | OK | 1558 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*