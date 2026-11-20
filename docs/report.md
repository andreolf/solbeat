# Solbeat — State of the Solana Network

> Generated 2026-11-20T16:53:20Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1092 is 16% complete (~22h remaining), with the cluster processing ~2,460 TPS (2,460 non-vote). Measured slot time is 217ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $577.2K of Real Economic Value over the last 24h ($401/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $69.40 (-5.3% / 24h). Decentralization: Nakamoto coefficient 18, 661 active validators, 0.0% of stake delinquent. Alpenglow readiness: validators holding 100% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 5 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 471,811,233 |
| Block height | 449,825,252 |
| Epoch | 1092 (15.56% complete, ~22.0h left) |
| TPS (10 min avg) | 2,460 |
| Non-vote TPS | 2,460 |
| Slot time (measured) | 217.3 ms |
| Confirmation time (measured) | 0.22 s |
| Finality time (measured) | 0.22 s — **Alpenglow active** |
| Est. daily transactions | 176,923,924 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0027 |
| Node version | 4.4.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $69.40 (-5.3%/24h) |
| Market cap | $41.1B |
| **REV (24h)** | **$577.2K** (fees $470.0K + Jito tips $107.2K) |
| Chain TVL | $4.6B |
| Stablecoin supply | $13.4B |
| DEX volume (24h) | $1.9B (4.9%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 591,906,633 SOL |
| Inflation | 3.55% |

Top DEXs by 24h volume: Orca DEX ($271.8M), Meteora DLMM ($237.0M), PumpSwap ($207.8M), BisonFi ($179.1M), Raydium AMM ($157.1M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 661 / 24 |
| Delinquent stake | 0.02% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.8% |
| Avg / median commission | 12.7% / 5% |
| Alpenglow BLS-key readiness | 671 validators, 100.0% of stake |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `he1iusunGwqrNtafDtLd…` | 17,041,638 | 3.97% | 0% |
| 2 | `CcaHc2L43ZWjwCHART3o…` | 16,354,101 | 3.81% | 7% |
| 3 | `3N7s9zXMZ4QqvHQR15t5…` | 12,422,891 | 2.9% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxb…` | 10,309,121 | 2.4% | 0% |
| 5 | `51JBzSTU5rAM8gLAVQKg…` | 9,779,397 | 2.28% | 10% |
| 6 | `CatzoSMUkTRidT5DwBxA…` | 9,564,403 | 2.23% | 5% |
| 7 | `26pV97Ce83ZQ6Kz9XT4t…` | 9,231,683 | 2.15% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2Fp…` | 7,986,182 | 1.86% | 7% |
| 9 | `DumiCKHVqoCQKD8roLAp…` | 6,985,765 | 1.63% | 0% |
| 10 | `CvSb7wdQAFpHuSpTYTJn…` | 6,773,182 | 1.58% | 5% |

## Signals (anomaly detection)

- **[WARNING]** SOL price contraction (z=-2.1 vs its recent baseline)
- **[WARNING]** Solana TVL contraction (z=-2.4 vs its recent baseline)
- **[SERIOUS]** Stablecoin supply contraction (z=-3.2 vs its recent baseline)
- **[WARNING · market_move]** Market-wide move: SOL price anomaly accompanied by liquidity/volume shifts — an ecosystem-level repricing rather than an isolated metric.
- **[WARNING · liquidity_rotation]** Stablecoin supply and TVL moving together — capital rotating in or out of the chain.

## Solana Pulse — sentiment (experimental)

**44/100 — Neutral** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 65.8 |
| fear greed | 12 |
| momentum | 33.9 |
| news | 74 |

Crypto Fear & Greed: 12 (Extreme Fear) · CoinGecko votes bullish: 65.85% · headline tone (48h): +3

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 1,500 |
| Raydium AMM v4 | 563 |
| Orca Whirlpool | 1,500 |
| Pump.fun | 1,500 |
| Tensor | 1 |
| Magic Eden v2 | 30 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,300,003 |
| Binance (cold) | 66 |
| OKX (attributed) | 133,487 |
| Coinbase (hot) | 53,020 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 217ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 100.0% of stake.
- **Agave**: latest release v4.4.1 · running 4.4.0 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 10071 ms |
| solana_rpc_validators | OK | 358 ms |
| coingecko | OK | 1781 ms |
| defillama_tvl | OK | 194 ms |
| defillama_dex | OK | 1020 ms |
| defillama_fees | OK | 1683 ms |
| defillama_stablecoins | OK | 840 ms |
| defillama_xstocks | FAILED | 74 ms |
| jito_kobe | OK | 291 ms |
| stakewiz | OK | 1197 ms |
| github | OK | 916 ms |
| solana_com_news | FAILED | 130 ms |
| sentiment | OK | 2176 ms |
| solana_status_page | OK | 329 ms |
| solana_rpc_whales | OK | 1220 ms |
| solana_rpc_programs | OK | 2318 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*