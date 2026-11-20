# Solbeat — State of the Solana Network

> Generated 2026-11-20T08:34:15Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1091 is 83% complete (~4h remaining), with the cluster processing ~1,351 TPS (1,351 non-vote). Measured slot time is 216ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $607.8K of Real Economic Value over the last 24h ($422/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $72.65 (-2.4% / 24h). Decentralization: Nakamoto coefficient 18, 659 active validators, 0.0% of stake delinquent. Alpenglow readiness: validators holding 100% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 3 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 471,671,916 |
| Block height | 449,686,009 |
| Epoch | 1091 (83.31% complete, ~4.3h left) |
| TPS (10 min avg) | 1,351 |
| Non-vote TPS | 1,351 |
| Slot time (measured) | 215.9 ms |
| Confirmation time (measured) | 0.22 s |
| Finality time (measured) | 0.22 s — **Alpenglow active** |
| Est. daily transactions | 138,317,805 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0034 |
| Node version | 4.4.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $72.65 (-2.4%/24h) |
| Market cap | $43.0B |
| **REV (24h)** | **$607.8K** (fees $470.0K + Jito tips $137.9K) |
| Chain TVL | $4.7B |
| Stablecoin supply | $13.4B |
| DEX volume (24h) | $1.8B (1.8%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 591,851,236 SOL |
| Inflation | 3.55% |

Top DEXs by 24h volume: Orca DEX ($253.2M), Meteora DLMM ($246.2M), PumpSwap ($207.8M), BisonFi ($154.0M), Raydium AMM ($146.6M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 659 / 26 |
| Delinquent stake | 0.03% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.8% |
| Avg / median commission | 12.8% / 5% |
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

- **[WARNING]** Solana TVL contraction (z=-2.3 vs its recent baseline)
- **[SERIOUS]** Stablecoin supply contraction (z=-3.2 vs its recent baseline)
- **[WARNING · liquidity_rotation]** Stablecoin supply and TVL moving together — capital rotating in or out of the chain.

## Solana Pulse — sentiment (experimental)

**45/100 — Neutral** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 62.5 |
| fear greed | 12 |
| momentum | 37.5 |
| news | 82 |

Crypto Fear & Greed: 12 (Extreme Fear) · CoinGecko votes bullish: 62.5% · headline tone (48h): +4

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 692 |
| Raydium AMM v4 | 474 |
| Orca Whirlpool | 290 |
| Pump.fun | 1,500 |
| Tensor | 0 |
| Magic Eden v2 | 114 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,300,003 |
| Binance (cold) | 66 |
| OKX (attributed) | 133,487 |
| Coinbase (hot) | 69,562 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 216ms.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 100.0% of stake.
- **Agave**: latest release None · running 4.4.0 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 8935 ms |
| solana_rpc_validators | OK | 244 ms |
| coingecko | OK | 1724 ms |
| defillama_tvl | OK | 41 ms |
| defillama_dex | OK | 1190 ms |
| defillama_fees | OK | 1979 ms |
| defillama_stablecoins | OK | 823 ms |
| defillama_xstocks | FAILED | 761 ms |
| jito_kobe | OK | 141 ms |
| stakewiz | OK | 1001 ms |
| github | FAILED | 6146 ms |
| solana_com_news | FAILED | 60 ms |
| sentiment | OK | 2180 ms |
| solana_status_page | OK | 311 ms |
| solana_rpc_whales | OK | 1018 ms |
| solana_rpc_programs | OK | 1846 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*