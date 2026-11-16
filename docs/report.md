# Solbeat — State of the Solana Network

> Generated 2026-11-16T01:12:18Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1087 is 83% complete (~4h remaining), with the cluster processing ~2,333 TPS (2,333 non-vote). Measured slot time is 215ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $455.7K of Real Economic Value over the last 24h ($316/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $71.60 (+4.1% / 24h). Decentralization: Nakamoto coefficient 18, 662 active validators, 0.1% of stake delinquent. Alpenglow readiness: validators holding 100% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 3 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 469,942,741 |
| Block height | 447,957,691 |
| Epoch | 1087 (83.04% complete, ~4.4h left) |
| TPS (10 min avg) | 2,333 |
| Non-vote TPS | 2,333 |
| Slot time (measured) | 215.1 ms |
| Confirmation time (measured) | 0.0 s |
| Finality time (measured) | 0.0 s — **Alpenglow active** |
| Est. daily transactions | 163,477,493 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0022 |
| Node version | 4.4.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $71.60 (+4.1%/24h) |
| Market cap | $42.4B |
| **REV (24h)** | **$455.7K** (fees $357.1K + Jito tips $98.6K) |
| Chain TVL | $4.7B |
| Stablecoin supply | $14.3B |
| DEX volume (24h) | $1.6B (-4.5%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 591,628,919 SOL |
| Inflation | 3.56% |

Top DEXs by 24h volume: BisonFi ($236.7M), Orca DEX ($226.7M), PumpSwap ($156.4M), Meteora DLMM ($154.9M), Scorch ($131.5M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 662 / 38 |
| Delinquent stake | 0.08% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.8% |
| Avg / median commission | 12.7% / 5.0% |
| Alpenglow BLS-key readiness | 686 validators, 100.0% of stake |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `he1iusunGwqrNtafDtLd…` | 16,927,749 | 3.94% | 0% |
| 2 | `CcaHc2L43ZWjwCHART3o…` | 16,404,544 | 3.82% | 7% |
| 3 | `3N7s9zXMZ4QqvHQR15t5…` | 12,614,561 | 2.94% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxb…` | 10,141,932 | 2.36% | 0% |
| 5 | `51JBzSTU5rAM8gLAVQKg…` | 9,754,208 | 2.27% | 10% |
| 6 | `CatzoSMUkTRidT5DwBxA…` | 9,640,656 | 2.25% | 5% |
| 7 | `26pV97Ce83ZQ6Kz9XT4t…` | 9,204,466 | 2.14% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2Fp…` | 7,943,264 | 1.85% | 7% |
| 9 | `DumiCKHVqoCQKD8roLAp…` | 6,991,232 | 1.63% | 0% |
| 10 | `CvSb7wdQAFpHuSpTYTJn…` | 6,708,648 | 1.56% | 5% |

## Signals (anomaly detection)

- **[WARNING]** SOL price contraction (z=-2.5 vs its recent baseline)
- **[WARNING]** Solana TVL contraction (z=-2.5 vs its recent baseline)
- **[WARNING · market_move]** Market-wide move: SOL price anomaly accompanied by liquidity/volume shifts — an ecosystem-level repricing rather than an isolated metric.

## Solana Pulse — sentiment (experimental)

**37/100 — Bearish** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 59.7 |
| fear greed | 10 |
| momentum | 25.0 |
| news | 58 |

Crypto Fear & Greed: 10 (Extreme Fear) · CoinGecko votes bullish: 59.72% · headline tone (48h): +1

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 1,065 |
| Raydium AMM v4 | 1,500 |
| Orca Whirlpool | 1,500 |
| Pump.fun | 1,500 |
| Tensor | 1 |
| Magic Eden v2 | 86 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,300,003 |
| Binance (cold) | 66 |
| OKX (attributed) | 34,568 |
| Coinbase (hot) | 33,891 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 215ms.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 100.0% of stake.
- **Agave**: latest release None · running 4.4.0 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 9653 ms |
| solana_rpc_validators | OK | 415 ms |
| coingecko | OK | 1669 ms |
| defillama_tvl | OK | 43 ms |
| defillama_dex | OK | 1249 ms |
| defillama_fees | OK | 1412 ms |
| defillama_stablecoins | OK | 56 ms |
| defillama_xstocks | FAILED | 35 ms |
| jito_kobe | OK | 7325 ms |
| stakewiz | OK | 1437 ms |
| github | FAILED | 6186 ms |
| solana_com_news | FAILED | 75 ms |
| sentiment | OK | 2167 ms |
| solana_status_page | OK | 164 ms |
| solana_rpc_whales | OK | 1040 ms |
| solana_rpc_programs | OK | 1940 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*