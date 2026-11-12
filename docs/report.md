# Solbeat — State of the Solana Network

> Generated 2026-11-12T05:52:10Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1084 is 29% complete (~18h remaining), with the cluster processing ~1,270 TPS (1,270 non-vote). Measured slot time is 216ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $627.2K of Real Economic Value over the last 24h ($436/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $82.87 (-0.5% / 24h). Decentralization: Nakamoto coefficient 18, 661 active validators, 0.2% of stake delinquent. Alpenglow readiness: validators holding 100% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 2 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 468,414,689 |
| Block height | 446,430,588 |
| Epoch | 1084 (29.33% complete, ~18.3h left) |
| TPS (10 min avg) | 1,270 |
| Non-vote TPS | 1,270 |
| Slot time (measured) | 215.7 ms |
| Confirmation time (measured) | 0.22 s |
| Finality time (measured) | 0.22 s — **Alpenglow active** |
| Est. daily transactions | 147,678,155 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0034 |
| Node version | 4.4.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $82.87 (-0.5%/24h) |
| Market cap | $49.0B |
| **REV (24h)** | **$627.2K** (fees $500.9K + Jito tips $126.3K) |
| Chain TVL | $5.0B |
| Stablecoin supply | $14.1B |
| DEX volume (24h) | $1.6B (22.2%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 591,457,029 SOL |
| Inflation | 3.56% |

Top DEXs by 24h volume: PumpSwap ($395.7M), Orca DEX ($205.1M), BisonFi ($152.6M), Raydium AMM ($144.8M), Meteora DLMM ($129.4M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 661 / 37 |
| Delinquent stake | 0.16% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.5% |
| Avg / median commission | 12.7% / 5% |
| Alpenglow BLS-key readiness | 686 validators, 100.0% of stake |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `he1iusunGwqrNtafDtLd…` | 16,789,054 | 3.87% | 0% |
| 2 | `CcaHc2L43ZWjwCHART3o…` | 16,119,194 | 3.72% | 7% |
| 3 | `3N7s9zXMZ4QqvHQR15t5…` | 13,026,247 | 3.01% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxb…` | 10,116,092 | 2.33% | 0% |
| 5 | `51JBzSTU5rAM8gLAVQKg…` | 9,681,376 | 2.23% | 10% |
| 6 | `CatzoSMUkTRidT5DwBxA…` | 9,580,180 | 2.21% | 5% |
| 7 | `26pV97Ce83ZQ6Kz9XT4t…` | 9,230,504 | 2.13% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2Fp…` | 7,840,792 | 1.81% | 7% |
| 9 | `DumiCKHVqoCQKD8roLAp…` | 6,987,981 | 1.61% | 0% |
| 10 | `CvSb7wdQAFpHuSpTYTJn…` | 6,730,421 | 1.55% | 5% |

## Signals (anomaly detection)

- **[WARNING]** SOL price contraction (z=-2.1 vs its recent baseline)
- **[WARNING]** Stablecoin supply contraction (z=-2.4 vs its recent baseline)

## Solana Pulse — sentiment (experimental)

**58/100 — Neutral** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 76.2 |
| fear greed | 28 |
| momentum | 44.8 |
| news | 95 |

Crypto Fear & Greed: 28 (Fear) · CoinGecko votes bullish: 76.19% · headline tone (48h): +6

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 708 |
| Raydium AMM v4 | 708 |
| Orca Whirlpool | 481 |
| Pump.fun | 1,500 |
| Tensor | 0 |
| Magic Eden v2 | 47 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,300,003 |
| Binance (cold) | 66 |
| OKX (attributed) | 97,546 |
| Coinbase (hot) | 31,617 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 216ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 100.0% of stake.
- **Agave**: latest release v4.4.1 · running 4.4.0 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 9038 ms |
| solana_rpc_validators | OK | 212 ms |
| coingecko | OK | 1676 ms |
| defillama_tvl | OK | 203 ms |
| defillama_dex | OK | 1166 ms |
| defillama_fees | OK | 1045 ms |
| defillama_stablecoins | OK | 816 ms |
| defillama_xstocks | FAILED | 31 ms |
| jito_kobe | OK | 230 ms |
| stakewiz | OK | 1396 ms |
| github | OK | 787 ms |
| solana_com_news | FAILED | 38 ms |
| sentiment | OK | 2251 ms |
| solana_status_page | OK | 216 ms |
| solana_rpc_whales | OK | 1100 ms |
| solana_rpc_programs | OK | 1746 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*