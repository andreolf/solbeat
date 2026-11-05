# Solbeat — State of the Solana Network

> Generated 2026-11-05T11:13:05Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1077 is 97% complete (~1h remaining), with the cluster processing ~1,235 TPS (1,235 non-vote). Measured slot time is 213ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $720.3K of Real Economic Value over the last 24h ($500/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $96.47 (+3.1% / 24h). Decentralization: Nakamoto coefficient 17, 661 active validators, 0.5% of stake delinquent. Alpenglow readiness: validators holding 100% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 1 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 465,684,274 |
| Block height | 443,704,442 |
| Epoch | 1077 (97.29% complete, ~0.7h left) |
| TPS (10 min avg) | 1,235 |
| Non-vote TPS | 1,235 |
| Slot time (measured) | 212.6 ms |
| Confirmation time (measured) | 0.21 s |
| Finality time (measured) | 0.21 s — **Alpenglow active** |
| Est. daily transactions | 111,643,603 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0052 |
| Node version | 4.4.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $96.47 (+3.1%/24h) |
| Market cap | $56.9B |
| **REV (24h)** | **$720.3K** (fees $579.8K + Jito tips $140.6K) |
| Chain TVL | $5.6B |
| Stablecoin supply | $15.1B |
| DEX volume (24h) | $2.2B (18.1%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 590,261,999 SOL |
| Inflation | 3.57% |

Top DEXs by 24h volume: PumpSwap ($315.4M), Orca DEX ($276.2M), BisonFi ($257.1M), Raydium AMM ($202.8M), Tessera V ($154.4M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 661 / 32 |
| Delinquent stake | 0.5% |
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

- **[WARNING]** Stablecoin supply contraction (z=-2.4 vs its recent baseline)

## Solana Pulse — sentiment (experimental)

**63/100 — Bullish** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 77.1 |
| fear greed | 50 |
| momentum | 57.6 |
| news | 66 |

Crypto Fear & Greed: 50 (Neutral) · CoinGecko votes bullish: 77.14% · headline tone (48h): +2

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 886 |
| Raydium AMM v4 | 557 |
| Orca Whirlpool | 557 |
| Pump.fun | 1,500 |
| Tensor | 0 |
| Magic Eden v2 | 32 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,300,003 |
| Binance (cold) | 66 |
| OKX (attributed) | 346,929 |
| Coinbase (hot) | 22,817 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 213ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 100.0% of stake.
- **Agave**: latest release v4.4.0 · running 4.4.0 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 9523 ms |
| solana_rpc_validators | OK | 383 ms |
| coingecko | OK | 1710 ms |
| defillama_tvl | OK | 109 ms |
| defillama_dex | OK | 1117 ms |
| defillama_fees | OK | 981 ms |
| defillama_stablecoins | OK | 182 ms |
| defillama_xstocks | FAILED | 63 ms |
| jito_kobe | OK | 234 ms |
| stakewiz | OK | 1274 ms |
| github | OK | 927 ms |
| solana_com_news | FAILED | 185 ms |
| sentiment | OK | 2296 ms |
| solana_status_page | OK | 357 ms |
| solana_rpc_whales | OK | 1315 ms |
| solana_rpc_programs | OK | 2044 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*