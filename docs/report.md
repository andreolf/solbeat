# Solbeat — State of the Solana Network

> Generated 2026-11-22T04:59:45Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1093 is 55% complete (~11h remaining), with the cluster processing ~1,102 TPS (1,102 non-vote). Measured slot time is 214ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $424.7K of Real Economic Value over the last 24h ($295/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $69.31 (+5.0% / 24h). Decentralization: Nakamoto coefficient 18, 661 active validators, 0.0% of stake delinquent. Alpenglow readiness: validators holding 100% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 3 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 472,415,631 |
| Block height | 450,429,550 |
| Epoch | 1093 (55.47% complete, ~11.4h left) |
| TPS (10 min avg) | 1,102 |
| Non-vote TPS | 1,102 |
| Slot time (measured) | 214.0 ms |
| Confirmation time (measured) | 0.21 s |
| Finality time (measured) | 0.21 s — **Alpenglow active** |
| Est. daily transactions | 125,722,632 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0025 |
| Node version | 4.4.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $69.31 (+5.0%/24h) |
| Market cap | $41.0B |
| **REV (24h)** | **$424.7K** (fees $317.1K + Jito tips $107.7K) |
| Chain TVL | $4.6B |
| Stablecoin supply | $13.3B |
| DEX volume (24h) | $1.6B (-17.2%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 591,961,560 SOL |
| Inflation | 3.55% |

Top DEXs by 24h volume: BisonFi ($206.4M), Meteora DLMM ($177.9M), Orca DEX ($169.3M), Scorch ($147.3M), Raydium AMM ($125.0M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 661 / 24 |
| Delinquent stake | 0.02% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.9% |
| Avg / median commission | 12.9% / 5% |
| Alpenglow BLS-key readiness | 671 validators, 100.0% of stake |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `he1iusunGwqrNtafDtLd…` | 17,043,671 | 3.98% | 0% |
| 2 | `CcaHc2L43ZWjwCHART3o…` | 16,329,817 | 3.81% | 7% |
| 3 | `3N7s9zXMZ4QqvHQR15t5…` | 12,412,620 | 2.9% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxb…` | 10,241,724 | 2.39% | 0% |
| 5 | `51JBzSTU5rAM8gLAVQKg…` | 9,826,793 | 2.29% | 10% |
| 6 | `CatzoSMUkTRidT5DwBxA…` | 9,616,961 | 2.25% | 5% |
| 7 | `26pV97Ce83ZQ6Kz9XT4t…` | 9,237,166 | 2.16% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2Fp…` | 7,985,737 | 1.86% | 7% |
| 9 | `DumiCKHVqoCQKD8roLAp…` | 6,985,063 | 1.63% | 0% |
| 10 | `CvSb7wdQAFpHuSpTYTJn…` | 6,774,154 | 1.58% | 5% |

## Signals (anomaly detection)

- **[WARNING]** Solana TVL contraction (z=-2.3 vs its recent baseline)
- **[WARNING]** Stablecoin supply contraction (z=-3.0 vs its recent baseline)
- **[WARNING · liquidity_rotation]** Stablecoin supply and TVL moving together — capital rotating in or out of the chain.

## Solana Pulse — sentiment (experimental)

**46/100 — Neutral** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 70.7 |
| fear greed | 11 |
| momentum | 36.0 |
| news | 74 |

Crypto Fear & Greed: 11 (Extreme Fear) · CoinGecko votes bullish: 70.73% · headline tone (48h): +3

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 1,225 |
| Raydium AMM v4 | 1,225 |
| Orca Whirlpool | 1,225 |
| Pump.fun | 1,500 |
| Tensor | 0 |
| Magic Eden v2 | 21 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,300,003 |
| Binance (cold) | 66 |
| OKX (attributed) | 120,740 |
| Coinbase (hot) | 138,044 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 214ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 100.0% of stake.
- **Agave**: latest release v4.4.1 · running 4.4.0 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 8992 ms |
| solana_rpc_validators | OK | 186 ms |
| coingecko | OK | 1613 ms |
| defillama_tvl | OK | 70 ms |
| defillama_dex | OK | 783 ms |
| defillama_fees | OK | 566 ms |
| defillama_stablecoins | OK | 759 ms |
| defillama_xstocks | FAILED | 26 ms |
| jito_kobe | OK | 272 ms |
| stakewiz | OK | 973 ms |
| github | OK | 886 ms |
| solana_com_news | FAILED | 76 ms |
| sentiment | OK | 5083 ms |
| solana_status_page | OK | 125 ms |
| solana_rpc_whales | OK | 895 ms |
| solana_rpc_programs | OK | 1545 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*