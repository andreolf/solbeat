# Solbeat — State of the Solana Network

> Generated 2026-11-22T08:02:08Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1093 is 67% complete (~8h remaining), with the cluster processing ~1,199 TPS (1,199 non-vote). Measured slot time is 215ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $423.9K of Real Economic Value over the last 24h ($294/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $69.10 (+2.7% / 24h). Decentralization: Nakamoto coefficient 18, 661 active validators, 0.0% of stake delinquent. Alpenglow readiness: validators holding 100% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 3 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 472,466,523 |
| Block height | 450,480,418 |
| Epoch | 1093 (67.25% complete, ~8.5h left) |
| TPS (10 min avg) | 1,199 |
| Non-vote TPS | 1,199 |
| Slot time (measured) | 215.1 ms |
| Confirmation time (measured) | 0.22 s |
| Finality time (measured) | 0.22 s — **Alpenglow active** |
| Est. daily transactions | 113,953,467 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0028 |
| Node version | 4.4.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $69.10 (+2.7%/24h) |
| Market cap | $40.9B |
| **REV (24h)** | **$423.9K** (fees $317.1K + Jito tips $106.8K) |
| Chain TVL | $4.5B |
| Stablecoin supply | $13.3B |
| DEX volume (24h) | $1.6B (-17.2%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 591,961,525 SOL |
| Inflation | 3.55% |

Top DEXs by 24h volume: BisonFi ($206.4M), Meteora DLMM ($177.9M), Orca DEX ($163.1M), Scorch ($147.3M), PumpSwap ($124.0M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 661 / 24 |
| Delinquent stake | 0.02% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.9% |
| Avg / median commission | 12.9% / 5% |
| Alpenglow BLS-key readiness | 670 validators, 100.0% of stake |

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

- **[WARNING]** Solana TVL contraction (z=-2.4 vs its recent baseline)
- **[WARNING]** Stablecoin supply contraction (z=-3.0 vs its recent baseline)
- **[WARNING · liquidity_rotation]** Stablecoin supply and TVL moving together — capital rotating in or out of the chain.

## Solana Pulse — sentiment (experimental)

**44/100 — Neutral** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 73.2 |
| fear greed | 11 |
| momentum | 35.0 |
| news | 58 |

Crypto Fear & Greed: 11 (Extreme Fear) · CoinGecko votes bullish: 73.17% · headline tone (48h): +1

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 911 |
| Raydium AMM v4 | 911 |
| Orca Whirlpool | 1,500 |
| Pump.fun | 1,500 |
| Tensor | 0 |
| Magic Eden v2 | 26 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,300,003 |
| Binance (cold) | 66 |
| OKX (attributed) | 120,740 |
| Coinbase (hot) | 124,376 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 215ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 100.0% of stake.
- **Agave**: latest release v4.4.1 · running 4.4.0 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 8884 ms |
| solana_rpc_validators | OK | 157 ms |
| coingecko | OK | 1561 ms |
| defillama_tvl | OK | 529 ms |
| defillama_dex | OK | 860 ms |
| defillama_fees | OK | 960 ms |
| defillama_stablecoins | OK | 75 ms |
| defillama_xstocks | FAILED | 24 ms |
| jito_kobe | OK | 118 ms |
| stakewiz | OK | 991 ms |
| github | OK | 700 ms |
| solana_com_news | FAILED | 50 ms |
| sentiment | OK | 1950 ms |
| solana_status_page | OK | 236 ms |
| solana_rpc_whales | OK | 909 ms |
| solana_rpc_programs | OK | 1531 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*