# Solbeat — State of the Solana Network

> Generated 2026-11-04T16:51:48Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1077 is 26% complete (~19h remaining), with the cluster processing ~2,458 TPS (2,458 non-vote). Measured slot time is 214ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $619.5K of Real Economic Value over the last 24h ($430/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $96.74 (+3.7% / 24h). Decentralization: Nakamoto coefficient 17, 661 active validators, 0.5% of stake delinquent. Alpenglow readiness: validators holding 100% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 1 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 465,375,611 |
| Block height | 443,396,021 |
| Epoch | 1077 (25.84% complete, ~19.1h left) |
| TPS (10 min avg) | 2,458 |
| Non-vote TPS | 2,458 |
| Slot time (measured) | 214.5 ms |
| Confirmation time (measured) | 0.21 s |
| Finality time (measured) | 0.21 s — **Alpenglow active** |
| Est. daily transactions | 203,063,147 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0024 |
| Node version | 4.4.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $96.74 (+3.7%/24h) |
| Market cap | $57.1B |
| **REV (24h)** | **$619.5K** (fees $479.8K + Jito tips $139.7K) |
| Chain TVL | $5.5B |
| Stablecoin supply | $14.8B |
| DEX volume (24h) | $1.9B (1.5%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 590,262,319 SOL |
| Inflation | 3.57% |

Top DEXs by 24h volume: PumpSwap ($321.8M), Orca DEX ($259.8M), BisonFi ($257.1M), Raydium AMM ($216.1M), Tessera V ($154.4M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 661 / 32 |
| Delinquent stake | 0.53% |
| Nakamoto coefficient | 17 |
| Top-10 stake share | 24.7% |
| Avg / median commission | 12.6% / 5% |
| Alpenglow BLS-key readiness | 680 validators, 100.0% of stake |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L43ZWjwCHART3o…` | 17,036,631 | 3.93% | 7% |
| 2 | `he1iusunGwqrNtafDtLd…` | 16,710,689 | 3.86% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5…` | 13,012,272 | 3.01% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxb…` | 10,433,406 | 2.41% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxA…` | 9,524,736 | 2.2% | 5% |
| 6 | `51JBzSTU5rAM8gLAVQKg…` | 9,439,186 | 2.18% | 10% |
| 7 | `26pV97Ce83ZQ6Kz9XT4t…` | 9,217,930 | 2.13% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2Fp…` | 7,826,697 | 1.81% | 7% |
| 9 | `DumiCKHVqoCQKD8roLAp…` | 6,981,457 | 1.61% | 0% |
| 10 | `CvSb7wdQAFpHuSpTYTJn…` | 6,980,105 | 1.61% | 5% |

## Signals (anomaly detection)

- **[SERIOUS]** Stablecoin supply contraction (z=-3.3 vs its recent baseline)

## Solana Pulse — sentiment (experimental)

**53/100 — Neutral** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 71.4 |
| fear greed | 34 |
| momentum | 42.5 |
| news | 66 |

Crypto Fear & Greed: 34 (Fear) · CoinGecko votes bullish: 71.43% · headline tone (48h): +2

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 1,500 |
| Raydium AMM v4 | 1,500 |
| Orca Whirlpool | 1,500 |
| Pump.fun | 1,500 |
| Tensor | 0 |
| Magic Eden v2 | 72 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,300,003 |
| Binance (cold) | 65 |
| OKX (attributed) | 346,930 |
| Coinbase (hot) | 16,924 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 214ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 100.0% of stake.
- **Agave**: latest release v4.4.0 · running 4.4.0 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 57496 ms |
| solana_rpc_validators | OK | 3923 ms |
| coingecko | OK | 1848 ms |
| defillama_tvl | OK | 172 ms |
| defillama_dex | OK | 919 ms |
| defillama_fees | OK | 1119 ms |
| defillama_stablecoins | OK | 249 ms |
| defillama_xstocks | FAILED | 111 ms |
| jito_kobe | OK | 213 ms |
| stakewiz | OK | 1059 ms |
| github | OK | 782 ms |
| solana_com_news | FAILED | 61 ms |
| sentiment | OK | 2183 ms |
| solana_status_page | OK | 290 ms |
| solana_rpc_whales | OK | 16171 ms |
| solana_rpc_programs | OK | 28139 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*