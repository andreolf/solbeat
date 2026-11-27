# Solbeat — State of the Solana Network

> Generated 2026-11-27T12:06:37Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1098 is 48% complete (~13h remaining), with the cluster processing ~1,187 TPS (1,187 non-vote). Measured slot time is 214ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $424.1K of Real Economic Value over the last 24h ($294/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $73.07 (+2.9% / 24h). Decentralization: Nakamoto coefficient 18, 652 active validators, 0.1% of stake delinquent. Alpenglow readiness: validators holding 100% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 1 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 474,544,142 |
| Block height | 452,556,814 |
| Epoch | 1098 (48.18% complete, ~13.3h left) |
| TPS (10 min avg) | 1,187 |
| Non-vote TPS | 1,187 |
| Slot time (measured) | 214.2 ms |
| Confirmation time (measured) | 0.21 s |
| Finality time (measured) | 0.21 s — **Alpenglow active** |
| Est. daily transactions | 99,961,716 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0033 |
| Node version | 4.4.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $73.07 (+2.9%/24h) |
| Market cap | $43.3B |
| **REV (24h)** | **$424.1K** (fees $332.6K + Jito tips $91.4K) |
| Chain TVL | $4.7B |
| Stablecoin supply | $12.6B |
| DEX volume (24h) | $870.6M (-42.4%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 592,238,283 SOL |
| Inflation | 3.54% |

Top DEXs by 24h volume: Orca DEX ($132.9M), pump.fun ($108.0M), Raydium AMM ($98.2M), PumpSwap ($86.7M), BisonFi ($81.4M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 652 / 36 |
| Delinquent stake | 0.1% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 25.0% |
| Avg / median commission | 13.0% / 5.0% |
| Alpenglow BLS-key readiness | 669 validators, 100.0% of stake |

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

**46/100 — Neutral** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 74.3 |
| fear greed | 12 |
| momentum | 40.5 |
| news | 58 |

Crypto Fear & Greed: 12 (Extreme Fear) · CoinGecko votes bullish: 74.29% · headline tone (48h): +1

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 1,500 |
| Raydium AMM v4 | 1,500 |
| Orca Whirlpool | 1,500 |
| Pump.fun | 1,500 |
| Tensor | 0 |
| Magic Eden v2 | 34 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,300,003 |
| Binance (cold) | 66 |
| OKX (attributed) | 59,503 |
| Coinbase (hot) | 44,526 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 214ms.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 100.0% of stake.
- **Agave**: latest release None · running 4.4.0 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 9451 ms |
| solana_rpc_validators | OK | 167 ms |
| coingecko | OK | 1636 ms |
| defillama_tvl | OK | 557 ms |
| defillama_dex | OK | 34 ms |
| defillama_fees | OK | 700 ms |
| defillama_stablecoins | OK | 187 ms |
| defillama_xstocks | FAILED | 39 ms |
| jito_kobe | OK | 140 ms |
| stakewiz | OK | 892 ms |
| github | FAILED | 6038 ms |
| solana_com_news | FAILED | 32 ms |
| sentiment | OK | 2123 ms |
| solana_status_page | OK | 146 ms |
| solana_rpc_whales | OK | 886 ms |
| solana_rpc_programs | OK | 1493 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*