# Solbeat — State of the Solana Network

> Generated 2026-11-18T05:38:13Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1089 is 86% complete (~4h remaining), with the cluster processing ~1,911 TPS (1,911 non-vote). Measured slot time is 217ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $571.7K of Real Economic Value over the last 24h ($397/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $75.25 (+3.2% / 24h). Decentralization: Nakamoto coefficient 18, 660 active validators, 0.0% of stake delinquent. Alpenglow readiness: validators holding 100% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 3 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 470,820,595 |
| Block height | 448,835,265 |
| Epoch | 1089 (86.25% complete, ~3.6h left) |
| TPS (10 min avg) | 1,911 |
| Non-vote TPS | 1,911 |
| Slot time (measured) | 216.9 ms |
| Confirmation time (measured) | 0.22 s |
| Finality time (measured) | 0.22 s — **Alpenglow active** |
| Est. daily transactions | 144,382,553 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0031 |
| Node version | 4.4.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $75.25 (+3.2%/24h) |
| Market cap | $44.5B |
| **REV (24h)** | **$571.7K** (fees $445.2K + Jito tips $126.4K) |
| Chain TVL | $4.8B |
| Stablecoin supply | $13.9B |
| DEX volume (24h) | $1.5B (1.2%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 591,739,425 SOL |
| Inflation | 3.55% |

Top DEXs by 24h volume: Orca DEX ($233.5M), Meteora DLMM ($155.8M), PumpSwap ($155.3M), BisonFi ($148.8M), Raydium AMM ($132.6M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 660 / 6 |
| Delinquent stake | 0.04% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.8% |
| Avg / median commission | 12.9% / 5.0% |
| Alpenglow BLS-key readiness | 686 validators, 100.0% of stake |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `he1iusunGwqrNtafDtLd…` | 16,834,343 | 3.93% | 0% |
| 2 | `CcaHc2L43ZWjwCHART3o…` | 16,442,668 | 3.83% | 7% |
| 3 | `3N7s9zXMZ4QqvHQR15t5…` | 12,432,778 | 2.9% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxb…` | 10,144,846 | 2.37% | 0% |
| 5 | `51JBzSTU5rAM8gLAVQKg…` | 9,802,677 | 2.29% | 10% |
| 6 | `CatzoSMUkTRidT5DwBxA…` | 9,625,021 | 2.24% | 5% |
| 7 | `26pV97Ce83ZQ6Kz9XT4t…` | 9,218,745 | 2.15% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2Fp…` | 7,970,891 | 1.86% | 7% |
| 9 | `DumiCKHVqoCQKD8roLAp…` | 6,996,288 | 1.63% | 0% |
| 10 | `CvSb7wdQAFpHuSpTYTJn…` | 6,730,472 | 1.57% | 5% |

## Signals (anomaly detection)

- **[WARNING]** Solana TVL contraction (z=-2.2 vs its recent baseline)
- **[WARNING]** Stablecoin supply contraction (z=-2.6 vs its recent baseline)
- **[WARNING · liquidity_rotation]** Stablecoin supply and TVL moving together — capital rotating in or out of the chain.

## Solana Pulse — sentiment (experimental)

**47/100 — Neutral** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 78.7 |
| fear greed | 11 |
| momentum | 36.0 |
| news | 66 |

Crypto Fear & Greed: 11 (Extreme Fear) · CoinGecko votes bullish: 78.72% · headline tone (48h): +2

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 701 |
| Raydium AMM v4 | 1,317 |
| Orca Whirlpool | 1,317 |
| Pump.fun | 1,500 |
| Tensor | 0 |
| Magic Eden v2 | 21 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,300,003 |
| Binance (cold) | 66 |
| OKX (attributed) | 55,682 |
| Coinbase (hot) | 47,065 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 217ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 100.0% of stake.
- **Agave**: latest release v4.4.1 · running 4.4.0 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 9774 ms |
| solana_rpc_validators | OK | 130 ms |
| coingecko | OK | 1634 ms |
| defillama_tvl | OK | 137 ms |
| defillama_dex | OK | 42 ms |
| defillama_fees | OK | 304 ms |
| defillama_stablecoins | OK | 627 ms |
| defillama_xstocks | FAILED | 21 ms |
| jito_kobe | OK | 80 ms |
| stakewiz | OK | 723 ms |
| github | OK | 578 ms |
| solana_com_news | FAILED | 26 ms |
| sentiment | OK | 1966 ms |
| solana_status_page | OK | 207 ms |
| solana_rpc_whales | OK | 857 ms |
| solana_rpc_programs | OK | 1531 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*