# Solbeat — State of the Solana Network

> Generated 2026-11-11T01:10:51Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1083 is 18% complete (~21h remaining), with the cluster processing ~2,001 TPS (2,001 non-vote). Measured slot time is 215ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $524.7K of Real Economic Value over the last 24h ($364/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $82.92 (-4.2% / 24h). Decentralization: Nakamoto coefficient 18, 658 active validators, 0.2% of stake delinquent. Alpenglow readiness: validators holding 100% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 2 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 467,933,964 |
| Block height | 445,950,594 |
| Epoch | 1083 (18.05% complete, ~21.1h left) |
| TPS (10 min avg) | 2,001 |
| Non-vote TPS | 2,001 |
| Slot time (measured) | 215.0 ms |
| Confirmation time (measured) | 0.0 s |
| Finality time (measured) | 0.0 s — **Alpenglow active** |
| Est. daily transactions | 171,849,738 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0024 |
| Node version | 4.4.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $82.92 (-4.2%/24h) |
| Market cap | $49.0B |
| **REV (24h)** | **$524.7K** (fees $408.0K + Jito tips $116.7K) |
| Chain TVL | $5.0B |
| Stablecoin supply | $14.7B |
| DEX volume (24h) | $1.5B (-2.2%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 591,408,570 SOL |
| Inflation | 3.56% |

Top DEXs by 24h volume: PumpSwap ($256.1M), Orca DEX ($220.3M), BisonFi ($157.1M), Raydium AMM ($143.7M), Meteora DLMM ($122.7M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 658 / 41 |
| Delinquent stake | 0.23% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.6% |
| Avg / median commission | 12.6% / 5.0% |
| Alpenglow BLS-key readiness | 685 validators, 100.0% of stake |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `he1iusunGwqrNtafDtLd…` | 16,764,485 | 3.87% | 0% |
| 2 | `CcaHc2L43ZWjwCHART3o…` | 16,564,685 | 3.82% | 7% |
| 3 | `3N7s9zXMZ4QqvHQR15t5…` | 13,031,625 | 3.01% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxb…` | 10,117,254 | 2.33% | 0% |
| 5 | `51JBzSTU5rAM8gLAVQKg…` | 9,644,051 | 2.23% | 10% |
| 6 | `CatzoSMUkTRidT5DwBxA…` | 9,571,015 | 2.21% | 5% |
| 7 | `26pV97Ce83ZQ6Kz9XT4t…` | 9,231,999 | 2.13% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2Fp…` | 7,814,330 | 1.8% | 7% |
| 9 | `DumiCKHVqoCQKD8roLAp…` | 6,987,248 | 1.61% | 0% |
| 10 | `CvSb7wdQAFpHuSpTYTJn…` | 6,729,845 | 1.55% | 5% |

## Signals (anomaly detection)

- **[WARNING]** SOL price contraction (z=-2.2 vs its recent baseline)
- **[WARNING]** Stablecoin supply contraction (z=-2.8 vs its recent baseline)

## Solana Pulse — sentiment (experimental)

**47/100 — Neutral** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 72.7 |
| fear greed | 29 |
| momentum | 29.2 |
| news | 58 |

Crypto Fear & Greed: 29 (Fear) · CoinGecko votes bullish: 72.73% · headline tone (48h): +1

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 1,500 |
| Raydium AMM v4 | 1,500 |
| Orca Whirlpool | 1,500 |
| Pump.fun | 1,500 |
| Tensor | 0 |
| Magic Eden v2 | 44 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,300,003 |
| Binance (cold) | 66 |
| OKX (attributed) | 97,639 |
| Coinbase (hot) | 39,973 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 215ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 100.0% of stake.
- **Agave**: latest release v4.4.1 · running 4.4.0 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 11692 ms |
| solana_rpc_validators | OK | 421 ms |
| coingecko | OK | 1782 ms |
| defillama_tvl | OK | 825 ms |
| defillama_dex | OK | 1020 ms |
| defillama_fees | OK | 1738 ms |
| defillama_stablecoins | OK | 1226 ms |
| defillama_xstocks | FAILED | 79 ms |
| jito_kobe | OK | 167 ms |
| stakewiz | OK | 1231 ms |
| github | OK | 978 ms |
| solana_com_news | FAILED | 134 ms |
| sentiment | OK | 2260 ms |
| solana_status_page | OK | 433 ms |
| solana_rpc_whales | OK | 1231 ms |
| solana_rpc_programs | OK | 2282 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*