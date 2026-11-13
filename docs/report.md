# Solbeat — State of the Solana Network

> Generated 2026-11-13T19:53:44Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1085 is 76% complete (~6h remaining), with the cluster processing ~1,873 TPS (1,873 non-vote). Measured slot time is 215ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $562.4K of Real Economic Value over the last 24h ($391/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $80.03 (-2.0% / 24h). Decentralization: Nakamoto coefficient 18, 661 active validators, 0.1% of stake delinquent. Alpenglow readiness: validators holding 100% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 1 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 469,050,455 |
| Block height | 447,065,641 |
| Epoch | 1085 (76.49% complete, ~6.1h left) |
| TPS (10 min avg) | 1,873 |
| Non-vote TPS | 1,873 |
| Slot time (measured) | 214.8 ms |
| Confirmation time (measured) | 0.21 s |
| Finality time (measured) | 0.21 s — **Alpenglow active** |
| Est. daily transactions | 180,300,044 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0025 |
| Node version | 4.4.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $80.03 (-2.0%/24h) |
| Market cap | $47.3B |
| **REV (24h)** | **$562.4K** (fees $447.4K + Jito tips $115.0K) |
| Chain TVL | $4.9B |
| Stablecoin supply | $14.3B |
| DEX volume (24h) | $1.5B (-7.1%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 591,510,882 SOL |
| Inflation | 3.56% |

Top DEXs by 24h volume: PumpSwap ($290.2M), Orca DEX ($235.1M), BisonFi ($147.3M), Meteora DLMM ($144.7M), Raydium AMM ($136.8M)

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

- **[WARNING]** SOL price contraction (z=-2.2 vs its recent baseline)

## Solana Pulse — sentiment (experimental)

**42/100 — Neutral** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 64.9 |
| fear greed | 20 |
| momentum | 29.1 |
| news | 58 |

Crypto Fear & Greed: 20 (Extreme Fear) · CoinGecko votes bullish: 64.86% · headline tone (48h): +1

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 1,158 |
| Raydium AMM v4 | 1,158 |
| Orca Whirlpool | 1,158 |
| Pump.fun | 1,500 |
| Tensor | 0 |
| Magic Eden v2 | 16 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,300,003 |
| Binance (cold) | 66 |
| OKX (attributed) | 47,546 |
| Coinbase (hot) | 17,956 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 215ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 100.0% of stake.
- **Agave**: latest release v4.4.1 · running 4.4.0 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 10867 ms |
| solana_rpc_validators | OK | 302 ms |
| coingecko | OK | 1711 ms |
| defillama_tvl | OK | 113 ms |
| defillama_dex | OK | 1233 ms |
| defillama_fees | OK | 1012 ms |
| defillama_stablecoins | OK | 119 ms |
| defillama_xstocks | FAILED | 42 ms |
| jito_kobe | OK | 403 ms |
| stakewiz | OK | 1177 ms |
| github | OK | 723 ms |
| solana_com_news | FAILED | 89 ms |
| sentiment | OK | 2306 ms |
| solana_status_page | OK | 266 ms |
| solana_rpc_whales | OK | 1250 ms |
| solana_rpc_programs | OK | 2183 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*