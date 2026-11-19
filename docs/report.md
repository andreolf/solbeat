# Solbeat — State of the Solana Network

> Generated 2026-11-19T15:22:09Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1091 is 17% complete (~21h remaining), with the cluster processing ~2,424 TPS (2,424 non-vote). Measured slot time is 214ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $703.5K of Real Economic Value over the last 24h ($489/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $74.65 (+0.8% / 24h). Decentralization: Nakamoto coefficient 18, 659 active validators, 0.0% of stake delinquent. Alpenglow readiness: validators holding 100% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 4 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 471,384,279 |
| Block height | 449,398,537 |
| Epoch | 1091 (16.73% complete, ~21.4h left) |
| TPS (10 min avg) | 2,424 |
| Non-vote TPS | 2,424 |
| Slot time (measured) | 213.8 ms |
| Confirmation time (measured) | 0.43 s |
| Finality time (measured) | 0.43 s — **Alpenglow active** |
| Est. daily transactions | 140,631,267 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0040 |
| Node version | 4.4.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $74.65 (+0.8%/24h) |
| Market cap | $44.2B |
| **REV (24h)** | **$703.5K** (fees $560.5K + Jito tips $143.0K) |
| Chain TVL | $4.8B |
| Stablecoin supply | $13.0B |
| DEX volume (24h) | $1.8B (20.2%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 591,851,577 SOL |
| Inflation | 3.55% |

Top DEXs by 24h volume: PumpSwap ($330.7M), Orca DEX ($254.5M), Meteora DLMM ($246.2M), Raydium AMM ($194.4M), BisonFi ($154.0M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 659 / 26 |
| Delinquent stake | 0.03% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.8% |
| Avg / median commission | 12.6% / 5% |
| Alpenglow BLS-key readiness | 670 validators, 100.0% of stake |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `he1iusunGwqrNtafDtLd…` | 17,028,960 | 3.97% | 0% |
| 2 | `CcaHc2L43ZWjwCHART3o…` | 16,375,745 | 3.82% | 7% |
| 3 | `3N7s9zXMZ4QqvHQR15t5…` | 12,422,025 | 2.9% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxb…` | 10,299,570 | 2.4% | 0% |
| 5 | `51JBzSTU5rAM8gLAVQKg…` | 9,815,431 | 2.29% | 10% |
| 6 | `CatzoSMUkTRidT5DwBxA…` | 9,573,248 | 2.23% | 5% |
| 7 | `26pV97Ce83ZQ6Kz9XT4t…` | 9,225,578 | 2.15% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2Fp…` | 7,980,784 | 1.86% | 7% |
| 9 | `DumiCKHVqoCQKD8roLAp…` | 6,997,844 | 1.63% | 0% |
| 10 | `CvSb7wdQAFpHuSpTYTJn…` | 6,772,455 | 1.58% | 5% |

## Signals (anomaly detection)

- **[WARNING]** TPS spike: 2,424 vs 12h mean 1,604 (z=+2.0)
- **[WARNING]** Solana TVL contraction (z=-2.2 vs its recent baseline)
- **[SERIOUS]** Stablecoin supply contraction (z=-4.6 vs its recent baseline)
- **[WARNING · liquidity_rotation]** Stablecoin supply and TVL moving together — capital rotating in or out of the chain.

## Solana Pulse — sentiment (experimental)

**47/100 — Neutral** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 67.7 |
| fear greed | 10 |
| momentum | 46.0 |
| news | 66 |

Crypto Fear & Greed: 10 (Extreme Fear) · CoinGecko votes bullish: 67.65% · headline tone (48h): +2

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 1,013 |
| Raydium AMM v4 | 1,500 |
| Orca Whirlpool | 1,500 |
| Pump.fun | 1,500 |
| Tensor | 1 |
| Magic Eden v2 | 21 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,300,003 |
| Binance (cold) | 66 |
| OKX (attributed) | 133,487 |
| Coinbase (hot) | 90,870 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 214ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 100.0% of stake.
- **Agave**: latest release v4.4.1 · running 4.4.0 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 11196 ms |
| solana_rpc_validators | OK | 349 ms |
| coingecko | OK | 1739 ms |
| defillama_tvl | OK | 1485 ms |
| defillama_dex | OK | 49 ms |
| defillama_fees | OK | 3342 ms |
| defillama_stablecoins | OK | 1019 ms |
| defillama_xstocks | FAILED | 896 ms |
| jito_kobe | OK | 352 ms |
| stakewiz | OK | 1026 ms |
| github | OK | 713 ms |
| solana_com_news | FAILED | 103 ms |
| sentiment | OK | 2355 ms |
| solana_status_page | OK | 290 ms |
| solana_rpc_whales | OK | 1233 ms |
| solana_rpc_programs | OK | 2138 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*