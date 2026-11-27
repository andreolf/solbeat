# Solbeat — State of the Solana Network

> Generated 2026-11-27T08:34:05Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1098 is 34% complete (~17h remaining), with the cluster processing ~1,071 TPS (1,071 non-vote). Measured slot time is 216ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $423.6K of Real Economic Value over the last 24h ($294/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $73.18 (+3.3% / 24h). Decentralization: Nakamoto coefficient 18, 654 active validators, 0.1% of stake delinquent. Anomaly scan: 1 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 474,484,739 |
| Block height | 452,497,427 |
| Epoch | 1098 (34.43% complete, ~17.0h left) |
| TPS (10 min avg) | 1,071 |
| Non-vote TPS | 1,071 |
| Slot time (measured) | 215.7 ms |
| Confirmation time (measured) | 0.22 s |
| Finality time (measured) | 0.22 s — **Alpenglow active** |
| Est. daily transactions | 113,620,571 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0029 |
| Node version | 4.4.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $73.18 (+3.3%/24h) |
| Market cap | $43.3B |
| **REV (24h)** | **$423.6K** (fees $332.6K + Jito tips $90.9K) |
| Chain TVL | $4.7B |
| Stablecoin supply | $12.6B |
| DEX volume (24h) | $1.2B (-18.5%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 592,238,321 SOL |
| Inflation | 3.54% |

Top DEXs by 24h volume: BisonFi ($190.6M), Orca DEX ($136.0M), Meteora DLMM ($119.4M), Raydium AMM ($106.0M), Scorch ($104.6M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 654 / 34 |
| Delinquent stake | 0.06% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 25.0% |
| Avg / median commission | 13.0% / 5.0% |
| Alpenglow BLS-key readiness | 0 validators, 0.0% of stake |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `he1iusunGwqrNtafDtLd…` | 16,815,245 | 3.96% | 0% |
| 2 | `CcaHc2L43ZWjwCHART3o…` | 15,826,052 | 3.73% | 7% |
| 3 | `3N7s9zXMZ4QqvHQR15t5…` | 12,437,388 | 2.93% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxb…` | 10,238,108 | 2.41% | 0% |
| 5 | `51JBzSTU5rAM8gLAVQKg…` | 9,920,637 | 2.34% | 10% |
| 6 | `CatzoSMUkTRidT5DwBxA…` | 9,617,109 | 2.27% | 5% |
| 7 | `26pV97Ce83ZQ6Kz9XT4t…` | 9,296,651 | 2.19% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2Fp…` | 8,037,877 | 1.89% | 7% |
| 9 | `DumiCKHVqoCQKD8roLAp…` | 6,972,141 | 1.64% | 0% |
| 10 | `CvSb7wdQAFpHuSpTYTJn…` | 6,741,351 | 1.59% | 5% |

## Signals (anomaly detection)

- **[SERIOUS]** Stablecoin supply contraction (z=-3.4 vs its recent baseline)

## Solana Pulse — sentiment (experimental)

**48/100 — Neutral** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 74.2 |
| fear greed | 12 |
| momentum | 46.5 |
| news | 58 |

Crypto Fear & Greed: 12 (Extreme Fear) · CoinGecko votes bullish: 74.19% · headline tone (48h): +1

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 671 |
| Raydium AMM v4 | 463 |
| Orca Whirlpool | 1,213 |
| Pump.fun | 1,500 |
| Tensor | 0 |
| Magic Eden v2 | 48 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,300,003 |
| Binance (cold) | 66 |
| OKX (attributed) | 59,503 |
| Coinbase (hot) | 50,227 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 216ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 0.0% of stake.
- **Agave**: latest release v4.4.1 · running 4.4.0 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 9578 ms |
| solana_rpc_validators | OK | 124 ms |
| coingecko | OK | 1631 ms |
| defillama_tvl | OK | 543 ms |
| defillama_dex | OK | 777 ms |
| defillama_fees | OK | 665 ms |
| defillama_stablecoins | OK | 69 ms |
| defillama_xstocks | FAILED | 25 ms |
| jito_kobe | OK | 66 ms |
| stakewiz | OK | 192 ms |
| github | OK | 604 ms |
| solana_com_news | FAILED | 35 ms |
| sentiment | OK | 1954 ms |
| solana_status_page | OK | 145 ms |
| solana_rpc_whales | OK | 914 ms |
| solana_rpc_programs | OK | 1390 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*