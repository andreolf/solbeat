# Solbeat — State of the Solana Network

> Generated 2026-11-21T17:19:26Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1093 is 10% complete (~23h remaining), with the cluster processing ~1,826 TPS (1,826 non-vote). Measured slot time is 214ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $505.0K of Real Economic Value over the last 24h ($351/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $70.69 (+2.6% / 24h). Decentralization: Nakamoto coefficient 18, 660 active validators, 0.1% of stake delinquent. Alpenglow readiness: validators holding 100% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 3 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 472,220,280 |
| Block height | 450,234,226 |
| Epoch | 1093 (10.25% complete, ~23.0h left) |
| TPS (10 min avg) | 1,826 |
| Non-vote TPS | 1,826 |
| Slot time (measured) | 213.7 ms |
| Confirmation time (measured) | 0.21 s |
| Finality time (measured) | 0.21 s — **Alpenglow active** |
| Est. daily transactions | 125,851,471 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0031 |
| Node version | 4.4.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $70.69 (+2.6%/24h) |
| Market cap | $41.8B |
| **REV (24h)** | **$505.0K** (fees $395.1K + Jito tips $110.0K) |
| Chain TVL | $4.6B |
| Stablecoin supply | $13.2B |
| DEX volume (24h) | $1.9B (-1.0%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 591,961,740 SOL |
| Inflation | 3.55% |

Top DEXs by 24h volume: Orca DEX ($283.3M), BisonFi ($206.4M), Meteora DLMM ($177.9M), Raydium AMM ($168.1M), PumpSwap ($166.1M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 660 / 25 |
| Delinquent stake | 0.05% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.9% |
| Avg / median commission | 12.8% / 5.0% |
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

- **[WARNING]** Solana TVL contraction (z=-2.4 vs its recent baseline)
- **[SERIOUS]** Stablecoin supply contraction (z=-3.4 vs its recent baseline)
- **[WARNING · liquidity_rotation]** Stablecoin supply and TVL moving together — capital rotating in or out of the chain.

## Solana Pulse — sentiment (experimental)

**48/100 — Neutral** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 66.0 |
| fear greed | 12 |
| momentum | 44.4 |
| news | 82 |

Crypto Fear & Greed: 12 (Extreme Fear) · CoinGecko votes bullish: 66.0% · headline tone (48h): +4

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 1,500 |
| Raydium AMM v4 | 1,500 |
| Orca Whirlpool | 1,500 |
| Pump.fun | 1,500 |
| Tensor | 0 |
| Magic Eden v2 | 165 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,300,003 |
| Binance (cold) | 66 |
| OKX (attributed) | 120,740 |
| Coinbase (hot) | 22,709 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 214ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 100.0% of stake.
- **Agave**: latest release v4.4.1 · running 4.4.0 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 14286 ms |
| solana_rpc_validators | OK | 205 ms |
| coingecko | OK | 1680 ms |
| defillama_tvl | OK | 699 ms |
| defillama_dex | OK | 1016 ms |
| defillama_fees | OK | 108 ms |
| defillama_stablecoins | OK | 1030 ms |
| defillama_xstocks | FAILED | 625 ms |
| jito_kobe | OK | 387 ms |
| stakewiz | OK | 1130 ms |
| github | OK | 805 ms |
| solana_com_news | FAILED | 90 ms |
| sentiment | OK | 2187 ms |
| solana_status_page | OK | 289 ms |
| solana_rpc_whales | OK | 2929 ms |
| solana_rpc_programs | OK | 3705 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*