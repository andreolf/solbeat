# Solbeat — State of the Solana Network

> Generated 2026-11-14T15:41:10Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1086 is 53% complete (~12h remaining), with the cluster processing ~2,010 TPS (2,010 non-vote). Measured slot time is 216ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $551.0K of Real Economic Value over the last 24h ($383/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $73.47 (-6.9% / 24h). Decentralization: Nakamoto coefficient 18, 663 active validators, 0.1% of stake delinquent. Alpenglow readiness: validators holding 100% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 5 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 469,381,682 |
| Block height | 447,396,769 |
| Epoch | 1086 (53.17% complete, ~12.2h left) |
| TPS (10 min avg) | 2,010 |
| Non-vote TPS | 2,010 |
| Slot time (measured) | 216.2 ms |
| Confirmation time (measured) | 0.22 s |
| Finality time (measured) | 0.22 s — **Alpenglow active** |
| Est. daily transactions | 113,692,314 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0039 |
| Node version | 4.4.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $73.47 (-6.9%/24h) |
| Market cap | $43.5B |
| **REV (24h)** | **$551.0K** (fees $448.8K + Jito tips $102.2K) |
| Chain TVL | $4.8B |
| Stablecoin supply | $14.1B |
| DEX volume (24h) | $1.6B (3.8%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 591,573,794 SOL |
| Inflation | 3.56% |

Top DEXs by 24h volume: Orca DEX ($228.3M), BisonFi ($186.9M), PumpSwap ($177.3M), Meteora DLMM ($164.8M), Raydium AMM ($113.8M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 663 / 36 |
| Delinquent stake | 0.09% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.7% |
| Avg / median commission | 12.9% / 5% |
| Alpenglow BLS-key readiness | 685 validators, 100.0% of stake |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `he1iusunGwqrNtafDtLd…` | 16,955,905 | 3.95% | 0% |
| 2 | `CcaHc2L43ZWjwCHART3o…` | 16,374,909 | 3.81% | 7% |
| 3 | `3N7s9zXMZ4QqvHQR15t5…` | 12,611,498 | 2.94% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxb…` | 10,140,468 | 2.36% | 0% |
| 5 | `51JBzSTU5rAM8gLAVQKg…` | 9,736,890 | 2.27% | 10% |
| 6 | `CatzoSMUkTRidT5DwBxA…` | 9,574,439 | 2.23% | 5% |
| 7 | `26pV97Ce83ZQ6Kz9XT4t…` | 9,199,377 | 2.14% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2Fp…` | 7,914,792 | 1.84% | 7% |
| 9 | `DumiCKHVqoCQKD8roLAp…` | 6,990,062 | 1.63% | 0% |
| 10 | `CvSb7wdQAFpHuSpTYTJn…` | 6,707,745 | 1.56% | 5% |

## Signals (anomaly detection)

- **[WARNING]** SOL price contraction (z=-2.7 vs its recent baseline)
- **[WARNING]** Solana TVL contraction (z=-2.3 vs its recent baseline)
- **[WARNING]** Stablecoin supply contraction (z=-2.3 vs its recent baseline)
- **[WARNING · market_move]** Market-wide move: SOL price anomaly accompanied by liquidity/volume shifts — an ecosystem-level repricing rather than an isolated metric.
- **[WARNING · liquidity_rotation]** Stablecoin supply and TVL moving together — capital rotating in or out of the chain.

## Solana Pulse — sentiment (experimental)

**41/100 — Neutral** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 68.8 |
| fear greed | 13 |
| momentum | 28.5 |
| news | 58 |

Crypto Fear & Greed: 13 (Extreme Fear) · CoinGecko votes bullish: 68.85% · headline tone (48h): +1

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 989 |
| Raydium AMM v4 | 989 |
| Orca Whirlpool | 989 |
| Pump.fun | 1,500 |
| Tensor | 0 |
| Magic Eden v2 | 37 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,300,003 |
| Binance (cold) | 66 |
| OKX (attributed) | 23,817 |
| Coinbase (hot) | 97,059 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 216ms.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 100.0% of stake.
- **Agave**: latest release None · running 4.4.0 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 12375 ms |
| solana_rpc_validators | OK | 84 ms |
| coingecko | OK | 1646 ms |
| defillama_tvl | OK | 27 ms |
| defillama_dex | OK | 845 ms |
| defillama_fees | OK | 61 ms |
| defillama_stablecoins | OK | 73 ms |
| defillama_xstocks | FAILED | 509 ms |
| jito_kobe | OK | 87 ms |
| stakewiz | OK | 646 ms |
| github | FAILED | 6030 ms |
| solana_com_news | FAILED | 23 ms |
| sentiment | OK | 2030 ms |
| solana_status_page | OK | 107 ms |
| solana_rpc_whales | OK | 853 ms |
| solana_rpc_programs | OK | 1432 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*