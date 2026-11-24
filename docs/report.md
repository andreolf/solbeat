# Solbeat — State of the Solana Network

> Generated 2026-11-24T16:34:26Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1095 is 86% complete (~4h remaining), with the cluster processing ~2,568 TPS (2,568 non-vote). Measured slot time is 215ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $527.7K of Real Economic Value over the last 24h ($366/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $69.07 (-7.9% / 24h). Decentralization: Nakamoto coefficient 18, 661 active validators, 0.0% of stake delinquent. Alpenglow readiness: validators holding 100% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 1 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 473,413,052 |
| Block height | 451,426,178 |
| Epoch | 1095 (86.35% complete, ~3.5h left) |
| TPS (10 min avg) | 2,568 |
| Non-vote TPS | 2,568 |
| Slot time (measured) | 214.6 ms |
| Confirmation time (measured) | 0.21 s |
| Finality time (measured) | 0.21 s — **Alpenglow active** |
| Est. daily transactions | 186,812,065 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0023 |
| Node version | 4.4.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $69.07 (-7.9%/24h) |
| Market cap | $40.9B |
| **REV (24h)** | **$527.7K** (fees $424.1K + Jito tips $103.6K) |
| Chain TVL | $4.5B |
| Stablecoin supply | $13.8B |
| DEX volume (24h) | $1.8B (85.1%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 592,071,588 SOL |
| Inflation | 3.54% |

Top DEXs by 24h volume: Orca DEX ($282.0M), BisonFi ($204.1M), Raydium AMM ($170.5M), Meteora DLMM ($166.9M), Scorch ($159.2M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 661 / 25 |
| Delinquent stake | 0.01% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 25.0% |
| Avg / median commission | 13.1% / 5% |
| Alpenglow BLS-key readiness | 670 validators, 100.0% of stake |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `he1iusunGwqrNtafDtLd…` | 17,028,046 | 4.0% | 0% |
| 2 | `CcaHc2L43ZWjwCHART3o…` | 16,091,420 | 3.78% | 7% |
| 3 | `3N7s9zXMZ4QqvHQR15t5…` | 12,412,158 | 2.91% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxb…` | 10,240,508 | 2.4% | 0% |
| 5 | `51JBzSTU5rAM8gLAVQKg…` | 9,856,366 | 2.31% | 10% |
| 6 | `CatzoSMUkTRidT5DwBxA…` | 9,634,022 | 2.26% | 5% |
| 7 | `26pV97Ce83ZQ6Kz9XT4t…` | 9,276,354 | 2.18% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2Fp…` | 8,005,660 | 1.88% | 7% |
| 9 | `DumiCKHVqoCQKD8roLAp…` | 6,987,776 | 1.64% | 0% |
| 10 | `CvSb7wdQAFpHuSpTYTJn…` | 6,778,434 | 1.59% | 5% |

## Signals (anomaly detection)

- **[WARNING]** Solana TVL contraction (z=-2.2 vs its recent baseline)

## Solana Pulse — sentiment (experimental)

**39/100 — Bearish** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 58.8 |
| fear greed | 11 |
| momentum | 53.2 |
| news | 18 |

Crypto Fear & Greed: 11 (Extreme Fear) · CoinGecko votes bullish: 58.82% · headline tone (48h): -4

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 1,500 |
| Raydium AMM v4 | 404 |
| Orca Whirlpool | 1,500 |
| Pump.fun | 1,500 |
| Tensor | 0 |
| Magic Eden v2 | 54 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,300,003 |
| Binance (cold) | 66 |
| OKX (attributed) | 88,910 |
| Coinbase (hot) | 51,614 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 215ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 100.0% of stake.
- **Agave**: latest release v4.4.1 · running 4.4.0 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 8883 ms |
| solana_rpc_validators | OK | 146 ms |
| coingecko | OK | 1759 ms |
| defillama_tvl | OK | 73 ms |
| defillama_dex | OK | 1241 ms |
| defillama_fees | OK | 1081 ms |
| defillama_stablecoins | OK | 107 ms |
| defillama_xstocks | FAILED | 255 ms |
| jito_kobe | OK | 257 ms |
| stakewiz | OK | 1246 ms |
| github | OK | 976 ms |
| solana_com_news | FAILED | 91 ms |
| sentiment | OK | 2296 ms |
| solana_status_page | OK | 249 ms |
| solana_rpc_whales | OK | 886 ms |
| solana_rpc_programs | OK | 1660 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*