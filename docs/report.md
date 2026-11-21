# Solbeat — State of the Solana Network

> Generated 2026-11-21T15:10:11Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1093 is 2% complete (~25h remaining), with the cluster processing ~1,768 TPS (1,768 non-vote). Measured slot time is 215ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $505.5K of Real Economic Value over the last 24h ($351/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $70.76 (+0.7% / 24h). Decentralization: Nakamoto coefficient 18, 661 active validators, 0.0% of stake delinquent. Alpenglow readiness: validators holding 100% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 3 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 472,184,226 |
| Block height | 450,198,179 |
| Epoch | 1093 (1.9% complete, ~25.3h left) |
| TPS (10 min avg) | 1,768 |
| Non-vote TPS | 1,768 |
| Slot time (measured) | 215.0 ms |
| Confirmation time (measured) | 0.21 s |
| Finality time (measured) | 0.21 s — **Alpenglow active** |
| Est. daily transactions | 112,096,586 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0035 |
| Node version | 4.4.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $70.76 (+0.7%/24h) |
| Market cap | $41.9B |
| **REV (24h)** | **$505.5K** (fees $395.1K + Jito tips $110.5K) |
| Chain TVL | $4.6B |
| Stablecoin supply | $13.2B |
| DEX volume (24h) | $1.9B (-1.0%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 591,961,987 SOL |
| Inflation | 3.55% |

Top DEXs by 24h volume: Orca DEX ($283.3M), BisonFi ($206.4M), Meteora DLMM ($177.9M), Raydium AMM ($169.5M), PumpSwap ($166.1M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 661 / 24 |
| Delinquent stake | 0.02% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.9% |
| Avg / median commission | 12.7% / 5% |
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

- **[WARNING]** Solana TVL contraction (z=-2.5 vs its recent baseline)
- **[SERIOUS]** Stablecoin supply contraction (z=-3.4 vs its recent baseline)
- **[WARNING · liquidity_rotation]** Stablecoin supply and TVL moving together — capital rotating in or out of the chain.

## Solana Pulse — sentiment (experimental)

**45/100 — Neutral** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 63.5 |
| fear greed | 12 |
| momentum | 44.1 |
| news | 66 |

Crypto Fear & Greed: 12 (Extreme Fear) · CoinGecko votes bullish: 63.46% · headline tone (48h): +2

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 1,500 |
| Raydium AMM v4 | 1,500 |
| Orca Whirlpool | 1,500 |
| Pump.fun | 1,500 |
| Tensor | 0 |
| Magic Eden v2 | 22 |
| Marinade | 1 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,300,003 |
| Binance (cold) | 66 |
| OKX (attributed) | 120,804 |
| Coinbase (hot) | 23,029 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 215ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 100.0% of stake.
- **Agave**: latest release v4.4.1 · running 4.4.0 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 9713 ms |
| solana_rpc_validators | OK | 302 ms |
| coingecko | OK | 1734 ms |
| defillama_tvl | OK | 255 ms |
| defillama_dex | OK | 1254 ms |
| defillama_fees | OK | 459 ms |
| defillama_stablecoins | OK | 1512 ms |
| defillama_xstocks | FAILED | 55 ms |
| jito_kobe | OK | 161 ms |
| stakewiz | OK | 1454 ms |
| github | OK | 673 ms |
| solana_com_news | FAILED | 65 ms |
| sentiment | OK | 2288 ms |
| solana_status_page | OK | 482 ms |
| solana_rpc_whales | OK | 1246 ms |
| solana_rpc_programs | OK | 2060 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*