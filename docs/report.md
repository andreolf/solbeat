# Solbeat — State of the Solana Network

> Generated 2026-11-16T08:27:14Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1088 is 11% complete (~23h remaining), with the cluster processing ~1,208 TPS (1,208 non-vote). Measured slot time is 216ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $449.9K of Real Economic Value over the last 24h ($312/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $70.86 (+0.8% / 24h). Decentralization: Nakamoto coefficient 18, 662 active validators, 0.0% of stake delinquent. Alpenglow readiness: validators holding 100% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 3 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 470,064,175 |
| Block height | 448,079,110 |
| Epoch | 1088 (11.15% complete, ~23.0h left) |
| TPS (10 min avg) | 1,208 |
| Non-vote TPS | 1,208 |
| Slot time (measured) | 215.8 ms |
| Confirmation time (measured) | 0.22 s |
| Finality time (measured) | 0.22 s — **Alpenglow active** |
| Est. daily transactions | 129,557,245 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0027 |
| Node version | 4.4.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $70.86 (+0.8%/24h) |
| Market cap | $41.9B |
| **REV (24h)** | **$449.9K** (fees $353.0K + Jito tips $96.9K) |
| Chain TVL | $4.7B |
| Stablecoin supply | $14.3B |
| DEX volume (24h) | $1.5B (-8.8%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 591,684,541 SOL |
| Inflation | 3.55% |

Top DEXs by 24h volume: BisonFi ($236.7M), Orca DEX ($172.2M), Meteora DLMM ($154.9M), PumpSwap ($142.8M), Scorch ($131.5M)

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
- **[WARNING]** Solana TVL contraction (z=-2.5 vs its recent baseline)
- **[WARNING · market_move]** Market-wide move: SOL price anomaly accompanied by liquidity/volume shifts — an ecosystem-level repricing rather than an isolated metric.

## Solana Pulse — sentiment (experimental)

**38/100 — Bearish** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 67.9 |
| fear greed | 10 |
| momentum | 22.2 |
| news | 58 |

Crypto Fear & Greed: 10 (Extreme Fear) · CoinGecko votes bullish: 67.86% · headline tone (48h): +1

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 1,154 |
| Raydium AMM v4 | 349 |
| Orca Whirlpool | 652 |
| Pump.fun | 1,500 |
| Tensor | 0 |
| Magic Eden v2 | 105 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,300,003 |
| Binance (cold) | 66 |
| OKX (attributed) | 36,671 |
| Coinbase (hot) | 37,799 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 216ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 100.0% of stake.
- **Agave**: latest release v4.4.1 · running 4.4.0 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 9254 ms |
| solana_rpc_validators | OK | 290 ms |
| coingecko | OK | 1784 ms |
| defillama_tvl | OK | 1032 ms |
| defillama_dex | OK | 1206 ms |
| defillama_fees | OK | 1037 ms |
| defillama_stablecoins | OK | 240 ms |
| defillama_xstocks | FAILED | 53 ms |
| jito_kobe | OK | 147 ms |
| stakewiz | OK | 1363 ms |
| github | OK | 621 ms |
| solana_com_news | FAILED | 64 ms |
| sentiment | OK | 2201 ms |
| solana_status_page | OK | 318 ms |
| solana_rpc_whales | OK | 1217 ms |
| solana_rpc_programs | OK | 2030 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*