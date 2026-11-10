# Solbeat — State of the Solana Network

> Generated 2026-11-10T12:09:29Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1082 is 67% complete (~8h remaining), with the cluster processing ~1,357 TPS (1,356 non-vote). Measured slot time is 213ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $516.6K of Real Economic Value over the last 24h ($359/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $84.56 (-2.0% / 24h). Decentralization: Nakamoto coefficient 18, 657 active validators, 0.2% of stake delinquent. Alpenglow readiness: validators holding 100% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 2 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 467,715,257 |
| Block height | 445,732,727 |
| Epoch | 1082 (67.42% complete, ~8.3h left) |
| TPS (10 min avg) | 1,357 |
| Non-vote TPS | 1,356 |
| Slot time (measured) | 212.7 ms |
| Confirmation time (measured) | 0.21 s |
| Finality time (measured) | 0.21 s — **Alpenglow active** |
| Est. daily transactions | 103,200,003 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0040 |
| Node version | 4.4.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $84.56 (-2.0%/24h) |
| Market cap | $50.0B |
| **REV (24h)** | **$516.6K** (fees $408.0K + Jito tips $108.6K) |
| Chain TVL | $5.0B |
| Stablecoin supply | $14.8B |
| DEX volume (24h) | $1.5B (42.6%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 591,149,083 SOL |
| Inflation | 3.56% |

Top DEXs by 24h volume: PumpSwap ($256.1M), Orca DEX ($188.3M), BisonFi ($157.1M), Raydium AMM ($129.0M), Meteora DLMM ($122.7M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 657 / 41 |
| Delinquent stake | 0.22% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.6% |
| Avg / median commission | 12.8% / 5% |
| Alpenglow BLS-key readiness | 684 validators, 100.0% of stake |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L43ZWjwCHART3o…` | 16,898,208 | 3.88% | 7% |
| 2 | `he1iusunGwqrNtafDtLd…` | 16,746,254 | 3.85% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5…` | 13,034,244 | 3.0% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxb…` | 10,280,950 | 2.36% | 0% |
| 5 | `51JBzSTU5rAM8gLAVQKg…` | 9,598,549 | 2.21% | 10% |
| 6 | `CatzoSMUkTRidT5DwBxA…` | 9,553,851 | 2.2% | 5% |
| 7 | `26pV97Ce83ZQ6Kz9XT4t…` | 9,233,159 | 2.12% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2Fp…` | 7,813,316 | 1.8% | 7% |
| 9 | `DumiCKHVqoCQKD8roLAp…` | 6,987,971 | 1.61% | 0% |
| 10 | `CvSb7wdQAFpHuSpTYTJn…` | 6,712,231 | 1.54% | 5% |

## Signals (anomaly detection)

- **[WARNING]** SOL price contraction (z=-2.1 vs its recent baseline)
- **[WARNING]** Stablecoin supply contraction (z=-2.8 vs its recent baseline)

## Solana Pulse — sentiment (experimental)

**50/100 — Neutral** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 70.6 |
| fear greed | 32 |
| momentum | 48.8 |
| news | 42 |

Crypto Fear & Greed: 32 (Fear) · CoinGecko votes bullish: 70.59% · headline tone (48h): -1

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 1,259 |
| Raydium AMM v4 | 470 |
| Orca Whirlpool | 684 |
| Pump.fun | 1,500 |
| Tensor | 0 |
| Magic Eden v2 | 48 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,300,003 |
| Binance (cold) | 66 |
| OKX (attributed) | 97,639 |
| Coinbase (hot) | 93,706 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 213ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 100.0% of stake.
- **Agave**: latest release v4.4.1 · running 4.4.0 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 8950 ms |
| solana_rpc_validators | OK | 244 ms |
| coingecko | OK | 1759 ms |
| defillama_tvl | OK | 788 ms |
| defillama_dex | OK | 82 ms |
| defillama_fees | OK | 1907 ms |
| defillama_stablecoins | OK | 112 ms |
| defillama_xstocks | FAILED | 45 ms |
| jito_kobe | OK | 170 ms |
| stakewiz | OK | 1396 ms |
| github | OK | 1022 ms |
| solana_com_news | FAILED | 94 ms |
| sentiment | OK | 2292 ms |
| solana_status_page | OK | 278 ms |
| solana_rpc_whales | OK | 984 ms |
| solana_rpc_programs | OK | 1606 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*