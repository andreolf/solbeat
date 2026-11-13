# Solbeat — State of the Solana Network

> Generated 2026-11-13T05:42:49Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1085 is 22% complete (~20h remaining), with the cluster processing ~1,772 TPS (1,772 non-vote). Measured slot time is 213ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $561.4K of Real Economic Value over the last 24h ($390/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $78.73 (-5.0% / 24h). Decentralization: Nakamoto coefficient 18, 660 active validators, 0.1% of stake delinquent. Alpenglow readiness: validators holding 100% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 3 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 468,813,411 |
| Block height | 446,828,861 |
| Epoch | 1085 (21.62% complete, ~20.0h left) |
| TPS (10 min avg) | 1,772 |
| Non-vote TPS | 1,772 |
| Slot time (measured) | 213.1 ms |
| Confirmation time (measured) | 0.43 s |
| Finality time (measured) | 0.43 s — **Alpenglow active** |
| Est. daily transactions | 178,422,210 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0025 |
| Node version | 4.4.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $78.73 (-5.0%/24h) |
| Market cap | $49.2B |
| **REV (24h)** | **$561.4K** (fees $447.4K + Jito tips $114.0K) |
| Chain TVL | $4.9B |
| Stablecoin supply | $14.3B |
| DEX volume (24h) | $1.5B (-6.6%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 591,511,122 SOL |
| Inflation | 3.56% |

Top DEXs by 24h volume: PumpSwap ($290.2M), Orca DEX ($218.1M), Meteora DLMM ($163.4M), Raydium AMM ($147.6M), BisonFi ($144.7M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 660 / 39 |
| Delinquent stake | 0.13% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.5% |
| Avg / median commission | 12.4% / 5.0% |
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

- **[WARNING]** SOL price contraction (z=-2.4 vs its recent baseline)
- **[WARNING]** Solana TVL contraction (z=-2.0 vs its recent baseline)
- **[WARNING · market_move]** Market-wide move: SOL price anomaly accompanied by liquidity/volume shifts — an ecosystem-level repricing rather than an isolated metric.

## Solana Pulse — sentiment (experimental)

**40/100 — Bearish** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 68.6 |
| fear greed | 20 |
| momentum | 27.5 |
| news | 42 |

Crypto Fear & Greed: 20 (Extreme Fear) · CoinGecko votes bullish: 68.57% · headline tone (48h): -1

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 733 |
| Raydium AMM v4 | 492 |
| Orca Whirlpool | 733 |
| Pump.fun | 1,500 |
| Tensor | 0 |
| Magic Eden v2 | 115 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,300,003 |
| Binance (cold) | 66 |
| OKX (attributed) | 97,546 |
| Coinbase (hot) | 26,926 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 213ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 100.0% of stake.
- **Agave**: latest release v4.4.1 · running 4.4.0 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 10856 ms |
| solana_rpc_validators | OK | 83 ms |
| coingecko | OK | 1641 ms |
| defillama_tvl | OK | 42 ms |
| defillama_dex | OK | 400 ms |
| defillama_fees | OK | 713 ms |
| defillama_stablecoins | OK | 68 ms |
| defillama_xstocks | FAILED | 511 ms |
| jito_kobe | OK | 79 ms |
| stakewiz | OK | 912 ms |
| github | OK | 704 ms |
| solana_com_news | FAILED | 25 ms |
| sentiment | OK | 1993 ms |
| solana_status_page | OK | 356 ms |
| solana_rpc_whales | OK | 796 ms |
| solana_rpc_programs | OK | 1440 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*