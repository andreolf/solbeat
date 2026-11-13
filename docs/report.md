# Solbeat — State of the Solana Network

> Generated 2026-11-13T20:54:37Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1085 is 80% complete (~5h remaining), with the cluster processing ~2,291 TPS (2,291 non-vote). Measured slot time is 217ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $561.4K of Real Economic Value over the last 24h ($390/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $80.09 (-1.6% / 24h). Decentralization: Nakamoto coefficient 18, 661 active validators, 0.1% of stake delinquent. Alpenglow readiness: validators holding 100% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 1 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 469,067,416 |
| Block height | 447,082,586 |
| Epoch | 1085 (80.42% complete, ~5.1h left) |
| TPS (10 min avg) | 2,291 |
| Non-vote TPS | 2,291 |
| Slot time (measured) | 216.8 ms |
| Confirmation time (measured) | 0.22 s |
| Finality time (measured) | 0.22 s — **Alpenglow active** |
| Est. daily transactions | 173,236,006 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0026 |
| Node version | 4.4.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $80.09 (-1.6%/24h) |
| Market cap | $47.4B |
| **REV (24h)** | **$561.4K** (fees $447.4K + Jito tips $114.0K) |
| Chain TVL | $4.9B |
| Stablecoin supply | $14.3B |
| DEX volume (24h) | $1.5B (-7.1%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 591,511,221 SOL |
| Inflation | 3.56% |

Top DEXs by 24h volume: PumpSwap ($290.2M), Orca DEX ($227.1M), BisonFi ($147.3M), Meteora DLMM ($144.7M), Raydium AMM ($136.2M)

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

**43/100 — Neutral** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 69.4 |
| fear greed | 20 |
| momentum | 29.2 |
| news | 58 |

Crypto Fear & Greed: 20 (Extreme Fear) · CoinGecko votes bullish: 69.44% · headline tone (48h): +1

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 1,500 |
| Raydium AMM v4 | 1,500 |
| Orca Whirlpool | 1,500 |
| Pump.fun | 1,500 |
| Tensor | 0 |
| Magic Eden v2 | 13 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,300,003 |
| Binance (cold) | 66 |
| OKX (attributed) | 47,546 |
| Coinbase (hot) | 16,908 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 217ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 100.0% of stake.
- **Agave**: latest release v4.4.1 · running 4.4.0 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 9697 ms |
| solana_rpc_validators | OK | 322 ms |
| coingecko | OK | 1795 ms |
| defillama_tvl | OK | 317 ms |
| defillama_dex | OK | 1131 ms |
| defillama_fees | OK | 1055 ms |
| defillama_stablecoins | OK | 958 ms |
| defillama_xstocks | FAILED | 41 ms |
| jito_kobe | OK | 8992 ms |
| stakewiz | OK | 1549 ms |
| github | OK | 678 ms |
| solana_com_news | FAILED | 70 ms |
| sentiment | OK | 2239 ms |
| solana_status_page | OK | 281 ms |
| solana_rpc_whales | OK | 1263 ms |
| solana_rpc_programs | OK | 2243 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*