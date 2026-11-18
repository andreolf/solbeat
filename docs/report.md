# Solbeat — State of the Solana Network

> Generated 2026-11-18T12:14:30Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1090 is 12% complete (~23h remaining), with the cluster processing ~2,318 TPS (2,318 non-vote). Measured slot time is 216ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $557.6K of Real Economic Value over the last 24h ($387/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $74.45 (+1.8% / 24h). Decentralization: Nakamoto coefficient 17, 660 active validators, 0.0% of stake delinquent. Alpenglow readiness: validators holding 100% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 5 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 470,930,987 |
| Block height | 448,945,583 |
| Epoch | 1090 (11.8% complete, ~22.9h left) |
| TPS (10 min avg) | 2,318 |
| Non-vote TPS | 2,318 |
| Slot time (measured) | 216.2 ms |
| Confirmation time (measured) | 0.22 s |
| Finality time (measured) | 0.22 s — **Alpenglow active** |
| Est. daily transactions | 134,991,682 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0033 |
| Node version | 4.4.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $74.45 (+1.8%/24h) |
| Market cap | $44.1B |
| **REV (24h)** | **$557.6K** (fees $445.2K + Jito tips $112.3K) |
| Chain TVL | $4.8B |
| Stablecoin supply | $13.9B |
| DEX volume (24h) | $1.5B (2.0%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 591,794,912 SOL |
| Inflation | 3.55% |

Top DEXs by 24h volume: Orca DEX ($231.6M), Meteora DLMM ($172.7M), PumpSwap ($155.3M), BisonFi ($149.6M), Raydium AMM ($124.1M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 660 / 25 |
| Delinquent stake | 0.02% |
| Nakamoto coefficient | 17 |
| Top-10 stake share | 25.0% |
| Avg / median commission | 12.6% / 5.0% |
| Alpenglow BLS-key readiness | 670 validators, 100.0% of stake |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `he1iusunGwqrNtafDtLd…` | 17,030,759 | 3.99% | 0% |
| 2 | `CcaHc2L43ZWjwCHART3o…` | 16,476,078 | 3.86% | 7% |
| 3 | `3N7s9zXMZ4QqvHQR15t5…` | 12,423,470 | 2.91% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxb…` | 10,297,722 | 2.41% | 0% |
| 5 | `51JBzSTU5rAM8gLAVQKg…` | 9,815,430 | 2.3% | 10% |
| 6 | `CatzoSMUkTRidT5DwBxA…` | 9,574,562 | 2.24% | 5% |
| 7 | `26pV97Ce83ZQ6Kz9XT4t…` | 9,222,715 | 2.16% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2Fp…` | 7,973,220 | 1.87% | 7% |
| 9 | `DumiCKHVqoCQKD8roLAp…` | 6,996,720 | 1.64% | 0% |
| 10 | `CvSb7wdQAFpHuSpTYTJn…` | 6,771,472 | 1.59% | 5% |

## Signals (anomaly detection)

- **[WARNING]** SOL price contraction (z=-2.0 vs its recent baseline)
- **[WARNING]** Solana TVL contraction (z=-2.2 vs its recent baseline)
- **[WARNING]** Stablecoin supply contraction (z=-2.6 vs its recent baseline)
- **[WARNING · market_move]** Market-wide move: SOL price anomaly accompanied by liquidity/volume shifts — an ecosystem-level repricing rather than an isolated metric.
- **[WARNING · liquidity_rotation]** Stablecoin supply and TVL moving together — capital rotating in or out of the chain.

## Solana Pulse — sentiment (experimental)

**47/100 — Neutral** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 75.9 |
| fear greed | 11 |
| momentum | 35.2 |
| news | 74 |

Crypto Fear & Greed: 11 (Extreme Fear) · CoinGecko votes bullish: 75.93% · headline tone (48h): +3

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 1,500 |
| Raydium AMM v4 | 1,500 |
| Orca Whirlpool | 1,500 |
| Pump.fun | 1,500 |
| Tensor | 1 |
| Magic Eden v2 | 43 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,300,003 |
| Binance (cold) | 66 |
| OKX (attributed) | 8,207 |
| Coinbase (hot) | 13,986 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 216ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 100.0% of stake.
- **Agave**: latest release v4.4.1 · running 4.4.0 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 45910 ms |
| solana_rpc_validators | OK | 2293 ms |
| coingecko | OK | 1632 ms |
| defillama_tvl | OK | 74 ms |
| defillama_dex | OK | 36 ms |
| defillama_fees | OK | 1019 ms |
| defillama_stablecoins | OK | 83 ms |
| defillama_xstocks | FAILED | 33 ms |
| jito_kobe | OK | 244 ms |
| stakewiz | OK | 777 ms |
| github | OK | 756 ms |
| solana_com_news | FAILED | 73 ms |
| sentiment | OK | 2032 ms |
| solana_status_page | OK | 176 ms |
| solana_rpc_whales | OK | 12151 ms |
| solana_rpc_programs | OK | 12559 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*