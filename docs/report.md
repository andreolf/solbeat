# Solbeat — State of the Solana Network

> Generated 2026-11-13T17:19:04Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1085 is 67% complete (~9h remaining), with the cluster processing ~2,200 TPS (2,200 non-vote). Measured slot time is 214ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $562.3K of Real Economic Value over the last 24h ($390/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $79.50 (-2.0% / 24h). Decentralization: Nakamoto coefficient 18, 661 active validators, 0.1% of stake delinquent. Alpenglow readiness: validators holding 100% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 1 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 469,007,360 |
| Block height | 447,022,554 |
| Epoch | 1085 (66.52% complete, ~8.6h left) |
| TPS (10 min avg) | 2,200 |
| Non-vote TPS | 2,200 |
| Slot time (measured) | 213.6 ms |
| Confirmation time (measured) | 0.21 s |
| Finality time (measured) | 0.21 s — **Alpenglow active** |
| Est. daily transactions | 167,740,907 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0027 |
| Node version | 4.4.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $79.50 (-2.0%/24h) |
| Market cap | $47.0B |
| **REV (24h)** | **$562.3K** (fees $447.4K + Jito tips $114.8K) |
| Chain TVL | $4.9B |
| Stablecoin supply | $14.3B |
| DEX volume (24h) | $1.5B (-7.1%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 591,510,932 SOL |
| Inflation | 3.56% |

Top DEXs by 24h volume: PumpSwap ($290.2M), Orca DEX ($242.9M), BisonFi ($147.3M), Meteora DLMM ($144.7M), Raydium AMM ($136.8M)

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

## Solana Pulse — sentiment (experimental)

**36/100 — Bearish** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 60.5 |
| fear greed | 20 |
| momentum | 28.7 |
| news | 26 |

Crypto Fear & Greed: 20 (Extreme Fear) · CoinGecko votes bullish: 60.53% · headline tone (48h): -3

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 1,034 |
| Raydium AMM v4 | 1,034 |
| Orca Whirlpool | 1,034 |
| Pump.fun | 1,500 |
| Tensor | 0 |
| Magic Eden v2 | 53 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,300,003 |
| Binance (cold) | 66 |
| OKX (attributed) | 47,546 |
| Coinbase (hot) | 20,521 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 214ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 100.0% of stake.
- **Agave**: latest release v4.4.1 · running 4.4.0 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 10330 ms |
| solana_rpc_validators | OK | 321 ms |
| coingecko | OK | 1906 ms |
| defillama_tvl | OK | 188 ms |
| defillama_dex | OK | 1264 ms |
| defillama_fees | OK | 420 ms |
| defillama_stablecoins | OK | 1004 ms |
| defillama_xstocks | FAILED | 891 ms |
| jito_kobe | OK | 14760 ms |
| stakewiz | OK | 1012 ms |
| github | OK | 683 ms |
| solana_com_news | FAILED | 118 ms |
| sentiment | OK | 2325 ms |
| solana_status_page | OK | 295 ms |
| solana_rpc_whales | OK | 1397 ms |
| solana_rpc_programs | OK | 2418 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*