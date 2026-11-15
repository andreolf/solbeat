# Solbeat — State of the Solana Network

> Generated 2026-11-15T06:18:59Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1087 is 10% complete (~23h remaining), with the cluster processing ~1,327 TPS (1,327 non-vote). Measured slot time is 214ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $454.5K of Real Economic Value over the last 24h ($316/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $70.21 (-7.4% / 24h). Decentralization: Nakamoto coefficient 18, 662 active validators, 0.1% of stake delinquent. Alpenglow readiness: validators holding 100% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 5 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 469,626,418 |
| Block height | 447,641,432 |
| Epoch | 1087 (9.82% complete, ~23.1h left) |
| TPS (10 min avg) | 1,327 |
| Non-vote TPS | 1,327 |
| Slot time (measured) | 213.6 ms |
| Confirmation time (measured) | 0.21 s |
| Finality time (measured) | 0.21 s — **Alpenglow active** |
| Est. daily transactions | 150,415,097 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0024 |
| Node version | 4.4.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $70.21 (-7.4%/24h) |
| Market cap | $41.5B |
| **REV (24h)** | **$454.5K** (fees $357.1K + Jito tips $97.4K) |
| Chain TVL | $4.7B |
| Stablecoin supply | $14.1B |
| DEX volume (24h) | $1.6B (3.4%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 591,629,208 SOL |
| Inflation | 3.56% |

Top DEXs by 24h volume: Orca DEX ($324.2M), BisonFi ($186.9M), Meteora DLMM ($164.8M), PumpSwap ($156.4M), Raydium AMM ($144.7M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 662 / 38 |
| Delinquent stake | 0.08% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.8% |
| Avg / median commission | 12.6% / 5.0% |
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

- **[WARNING]** SOL price contraction (z=-2.7 vs its recent baseline)
- **[WARNING]** Solana TVL contraction (z=-2.6 vs its recent baseline)
- **[WARNING]** Stablecoin supply contraction (z=-2.2 vs its recent baseline)
- **[WARNING · market_move]** Market-wide move: SOL price anomaly accompanied by liquidity/volume shifts — an ecosystem-level repricing rather than an isolated metric.
- **[WARNING · liquidity_rotation]** Stablecoin supply and TVL moving together — capital rotating in or out of the chain.

## Solana Pulse — sentiment (experimental)

**40/100 — Bearish** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 79.0 |
| fear greed | 10 |
| momentum | 26.6 |
| news | 42 |

Crypto Fear & Greed: 10 (Extreme Fear) · CoinGecko votes bullish: 78.97% · headline tone (48h): -1

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 1,008 |
| Raydium AMM v4 | 603 |
| Orca Whirlpool | 1,500 |
| Pump.fun | 1,500 |
| Tensor | 0 |
| Magic Eden v2 | 45 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,300,003 |
| Binance (cold) | 66 |
| OKX (attributed) | 34,568 |
| Coinbase (hot) | 30,401 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 214ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 100.0% of stake.
- **Agave**: latest release v4.4.1 · running 4.4.0 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 9719 ms |
| solana_rpc_validators | OK | 291 ms |
| coingecko | OK | 1670 ms |
| defillama_tvl | OK | 323 ms |
| defillama_dex | OK | 472 ms |
| defillama_fees | OK | 677 ms |
| defillama_stablecoins | OK | 637 ms |
| defillama_xstocks | FAILED | 38 ms |
| jito_kobe | OK | 414 ms |
| stakewiz | OK | 1140 ms |
| github | OK | 737 ms |
| solana_com_news | FAILED | 87 ms |
| sentiment | OK | 2308 ms |
| solana_status_page | OK | 269 ms |
| solana_rpc_whales | OK | 1154 ms |
| solana_rpc_programs | OK | 1856 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*