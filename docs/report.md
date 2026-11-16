# Solbeat — State of the Solana Network

> Generated 2026-11-16T01:49:47Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1087 is 85% complete (~4h remaining), with the cluster processing ~1,776 TPS (1,776 non-vote). Measured slot time is 215ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $455.5K of Real Economic Value over the last 24h ($316/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $71.25 (+5.3% / 24h). Decentralization: Nakamoto coefficient 18, 662 active validators, 0.1% of stake delinquent. Alpenglow readiness: validators holding 100% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 3 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 469,953,128 |
| Block height | 447,968,078 |
| Epoch | 1087 (85.45% complete, ~3.7h left) |
| TPS (10 min avg) | 1,776 |
| Non-vote TPS | 1,776 |
| Slot time (measured) | 214.6 ms |
| Confirmation time (measured) | 0.21 s |
| Finality time (measured) | 0.21 s — **Alpenglow active** |
| Est. daily transactions | 168,064,034 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0021 |
| Node version | 4.4.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $71.25 (+5.3%/24h) |
| Market cap | $42.2B |
| **REV (24h)** | **$455.5K** (fees $357.1K + Jito tips $98.4K) |
| Chain TVL | $4.7B |
| Stablecoin supply | $14.3B |
| DEX volume (24h) | $1.5B (-7.9%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 591,628,906 SOL |
| Inflation | 3.56% |

Top DEXs by 24h volume: BisonFi ($236.7M), Orca DEX ($226.7M), Meteora DLMM ($154.9M), PumpSwap ($142.8M), Scorch ($131.5M)

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
| community | 62.3 |
| fear greed | 10 |
| momentum | 23.3 |
| news | 58 |

Crypto Fear & Greed: 10 (Extreme Fear) · CoinGecko votes bullish: 62.32% · headline tone (48h): +1

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 1,105 |
| Raydium AMM v4 | 636 |
| Orca Whirlpool | 1,500 |
| Pump.fun | 1,500 |
| Tensor | 0 |
| Magic Eden v2 | 62 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,300,003 |
| Binance (cold) | 66 |
| OKX (attributed) | 34,568 |
| Coinbase (hot) | 34,260 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 215ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 100.0% of stake.
- **Agave**: latest release v4.4.1 · running 4.4.0 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 8995 ms |
| solana_rpc_validators | OK | 233 ms |
| coingecko | OK | 1696 ms |
| defillama_tvl | OK | 38 ms |
| defillama_dex | OK | 1177 ms |
| defillama_fees | OK | 1094 ms |
| defillama_stablecoins | OK | 790 ms |
| defillama_xstocks | FAILED | 39 ms |
| jito_kobe | OK | 145 ms |
| stakewiz | OK | 1516 ms |
| github | OK | 764 ms |
| solana_com_news | FAILED | 50 ms |
| sentiment | OK | 3227 ms |
| solana_status_page | OK | 171 ms |
| solana_rpc_whales | OK | 1034 ms |
| solana_rpc_programs | OK | 1950 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*