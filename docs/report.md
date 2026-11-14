# Solbeat — State of the Solana Network

> Generated 2026-11-14T01:29:00Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1085 is 98% complete (~0h remaining), with the cluster processing ~1,650 TPS (1,650 non-vote). Measured slot time is 216ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $558.1K of Real Economic Value over the last 24h ($388/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $77.36 (-5.2% / 24h). Decentralization: Nakamoto coefficient 18, 661 active validators, 0.1% of stake delinquent. Alpenglow readiness: validators holding 100% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 5 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 469,143,913 |
| Block height | 447,159,058 |
| Epoch | 1085 (98.13% complete, ~0.5h left) |
| TPS (10 min avg) | 1,650 |
| Non-vote TPS | 1,650 |
| Slot time (measured) | 215.6 ms |
| Confirmation time (measured) | 0.22 s |
| Finality time (measured) | 0.22 s — **Alpenglow active** |
| Est. daily transactions | 174,727,059 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0026 |
| Node version | 4.4.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $77.36 (-5.2%/24h) |
| Market cap | $45.8B |
| **REV (24h)** | **$558.1K** (fees $447.4K + Jito tips $110.7K) |
| Chain TVL | $4.9B |
| Stablecoin supply | $14.1B |
| DEX volume (24h) | $1.6B (4.2%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 591,519,903 SOL |
| Inflation | 3.56% |

Top DEXs by 24h volume: PumpSwap ($290.2M), Orca DEX ($241.3M), BisonFi ($147.3M), Meteora DLMM ($144.7M), Raydium AMM ($134.8M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 661 / 38 |
| Delinquent stake | 0.13% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.5% |
| Avg / median commission | 12.7% / 5% |
| Alpenglow BLS-key readiness | 686 validators, 100.0% of stake |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `he1iusunGwqrNtafDtLd…` | 16,815,755 | 3.89% | 0% |
| 2 | `CcaHc2L43ZWjwCHART3o…` | 16,140,175 | 3.73% | 7% |
| 3 | `3N7s9zXMZ4QqvHQR15t5…` | 12,976,229 | 3.0% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxb…` | 10,117,722 | 2.34% | 0% |
| 5 | `51JBzSTU5rAM8gLAVQKg…` | 9,699,456 | 2.24% | 10% |
| 6 | `CatzoSMUkTRidT5DwBxA…` | 9,578,398 | 2.22% | 5% |
| 7 | `26pV97Ce83ZQ6Kz9XT4t…` | 9,240,076 | 2.14% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2Fp…` | 7,863,387 | 1.82% | 7% |
| 9 | `DumiCKHVqoCQKD8roLAp…` | 6,989,060 | 1.62% | 0% |
| 10 | `CvSb7wdQAFpHuSpTYTJn…` | 6,712,617 | 1.55% | 5% |

## Signals (anomaly detection)

- **[WARNING]** SOL price contraction (z=-2.3 vs its recent baseline)
- **[WARNING]** Solana TVL contraction (z=-2.1 vs its recent baseline)
- **[WARNING]** Stablecoin supply contraction (z=-2.3 vs its recent baseline)
- **[WARNING · market_move]** Market-wide move: SOL price anomaly accompanied by liquidity/volume shifts — an ecosystem-level repricing rather than an isolated metric.
- **[WARNING · liquidity_rotation]** Stablecoin supply and TVL moving together — capital rotating in or out of the chain.

## Solana Pulse — sentiment (experimental)

**32/100 — Bearish** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| momentum | 31.6 |
## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 1,500 |
| Raydium AMM v4 | 779 |
| Orca Whirlpool | 1,500 |
| Pump.fun | 1,500 |
| Tensor | 0 |
| Magic Eden v2 | 44 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,300,003 |
| Binance (cold) | 66 |
| OKX (attributed) | 47,546 |
| Coinbase (hot) | 14,548 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 216ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 100.0% of stake.
- **Agave**: latest release v4.4.1 · running 4.4.0 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 13224 ms |
| solana_rpc_validators | OK | 72 ms |
| coingecko | OK | 1668 ms |
| defillama_tvl | OK | 69 ms |
| defillama_dex | OK | 396 ms |
| defillama_fees | OK | 58 ms |
| defillama_stablecoins | OK | 81 ms |
| defillama_xstocks | FAILED | 146 ms |
| jito_kobe | OK | 72 ms |
| stakewiz | OK | 695 ms |
| github | OK | 572 ms |
| solana_com_news | FAILED | 65 ms |
| sentiment | FAILED | 7687 ms |
| solana_status_page | OK | 414 ms |
| solana_rpc_whales | OK | 914 ms |
| solana_rpc_programs | OK | 1563 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*