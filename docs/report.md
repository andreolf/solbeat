# Solbeat — State of the Solana Network

> Generated 2026-11-05T00:48:45Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1077 is 57% complete (~11h remaining), with the cluster processing ~1,726 TPS (1,726 non-vote). Measured slot time is 216ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $617.3K of Real Economic Value over the last 24h ($429/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $95.85 (+4.0% / 24h). Decentralization: Nakamoto coefficient 17, 661 active validators, 0.9% of stake delinquent. Alpenglow readiness: validators holding 100% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 1 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 465,508,666 |
| Block height | 443,529,015 |
| Epoch | 1077 (56.64% complete, ~11.2h left) |
| TPS (10 min avg) | 1,726 |
| Non-vote TPS | 1,726 |
| Slot time (measured) | 215.9 ms |
| Confirmation time (measured) | 0.22 s |
| Finality time (measured) | 0.22 s — **Alpenglow active** |
| Est. daily transactions | 191,145,971 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0025 |
| Node version | 4.4.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $95.85 (+4.0%/24h) |
| Market cap | $56.6B |
| **REV (24h)** | **$617.3K** (fees $479.8K + Jito tips $137.5K) |
| Chain TVL | $5.5B |
| Stablecoin supply | $14.8B |
| DEX volume (24h) | $2.2B (16.9%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 590,262,140 SOL |
| Inflation | 3.57% |

Top DEXs by 24h volume: Orca DEX ($326.5M), PumpSwap ($321.8M), BisonFi ($257.1M), Raydium AMM ($236.0M), Tessera V ($154.4M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 661 / 32 |
| Delinquent stake | 0.9% |
| Nakamoto coefficient | 17 |
| Top-10 stake share | 24.7% |
| Avg / median commission | 12.7% / 5% |
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

**62/100 — Bullish** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 72.7 |
| fear greed | 50 |
| momentum | 55.7 |
| news | 74 |

Crypto Fear & Greed: 50 (Neutral) · CoinGecko votes bullish: 72.73% · headline tone (48h): +3

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 1,116 |
| Raydium AMM v4 | 1,116 |
| Orca Whirlpool | 1,500 |
| Pump.fun | 1,500 |
| Tensor | 0 |
| Magic Eden v2 | 41 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,300,003 |
| Binance (cold) | 66 |
| OKX (attributed) | 346,930 |
| Coinbase (hot) | 28,410 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 216ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 100.0% of stake.
- **Agave**: latest release v4.4.0 · running 4.4.0 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 11988 ms |
| solana_rpc_validators | OK | 342 ms |
| coingecko | OK | 1874 ms |
| defillama_tvl | OK | 211 ms |
| defillama_dex | OK | 1274 ms |
| defillama_fees | OK | 330 ms |
| defillama_stablecoins | OK | 232 ms |
| defillama_xstocks | FAILED | 939 ms |
| jito_kobe | OK | 311 ms |
| stakewiz | OK | 1411 ms |
| github | OK | 740 ms |
| solana_com_news | FAILED | 63 ms |
| sentiment | OK | 2284 ms |
| solana_status_page | OK | 391 ms |
| solana_rpc_whales | OK | 1346 ms |
| solana_rpc_programs | OK | 2402 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*