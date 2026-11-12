# Solbeat — State of the Solana Network

> Generated 2026-11-12T20:19:56Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1084 is 85% complete (~4h remaining), with the cluster processing ~2,292 TPS (2,292 non-vote). Measured slot time is 214ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $625.7K of Real Economic Value over the last 24h ($434/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $81.40 (-4.1% / 24h). Decentralization: Nakamoto coefficient 18, 660 active validators, 0.2% of stake delinquent. Alpenglow readiness: validators holding 100% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 2 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 468,656,819 |
| Block height | 446,672,385 |
| Epoch | 1084 (85.37% complete, ~3.8h left) |
| TPS (10 min avg) | 2,292 |
| Non-vote TPS | 2,292 |
| Slot time (measured) | 214.5 ms |
| Confirmation time (measured) | 0.21 s |
| Finality time (measured) | 0.21 s — **Alpenglow active** |
| Est. daily transactions | 185,072,477 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0027 |
| Node version | 4.4.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $81.40 (-4.1%/24h) |
| Market cap | $48.1B |
| **REV (24h)** | **$625.7K** (fees $500.9K + Jito tips $124.8K) |
| Chain TVL | $5.0B |
| Stablecoin supply | $14.1B |
| DEX volume (24h) | $1.6B (20.8%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 591,455,657 SOL |
| Inflation | 3.56% |

Top DEXs by 24h volume: PumpSwap ($395.7M), Orca DEX ($204.5M), Meteora DLMM ($163.4M), Raydium AMM ($149.0M), BisonFi ($144.7M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 660 / 38 |
| Delinquent stake | 0.16% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.5% |
| Avg / median commission | 12.7% / 5.0% |
| Alpenglow BLS-key readiness | 686 validators, 100.0% of stake |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `he1iusunGwqrNtafDtLd…` | 16,789,054 | 3.87% | 0% |
| 2 | `CcaHc2L43ZWjwCHART3o…` | 16,119,194 | 3.72% | 7% |
| 3 | `3N7s9zXMZ4QqvHQR15t5…` | 13,026,247 | 3.01% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxb…` | 10,116,092 | 2.33% | 0% |
| 5 | `51JBzSTU5rAM8gLAVQKg…` | 9,681,376 | 2.23% | 10% |
| 6 | `CatzoSMUkTRidT5DwBxA…` | 9,580,180 | 2.21% | 5% |
| 7 | `26pV97Ce83ZQ6Kz9XT4t…` | 9,230,504 | 2.13% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2Fp…` | 7,840,792 | 1.81% | 7% |
| 9 | `DumiCKHVqoCQKD8roLAp…` | 6,987,981 | 1.61% | 0% |
| 10 | `CvSb7wdQAFpHuSpTYTJn…` | 6,730,421 | 1.55% | 5% |

## Signals (anomaly detection)

- **[WARNING]** SOL price contraction (z=-2.2 vs its recent baseline)
- **[WARNING]** Stablecoin supply contraction (z=-2.4 vs its recent baseline)

## Solana Pulse — sentiment (experimental)

**52/100 — Neutral** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 82.3 |
| fear greed | 28 |
| momentum | 41.2 |
| news | 50 |

Crypto Fear & Greed: 28 (Fear) · CoinGecko votes bullish: 82.35% · headline tone (48h): +0

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 1,014 |
| Raydium AMM v4 | 605 |
| Orca Whirlpool | 1,500 |
| Pump.fun | 1,500 |
| Tensor | 0 |
| Magic Eden v2 | 20 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,300,003 |
| Binance (cold) | 66 |
| OKX (attributed) | 97,546 |
| Coinbase (hot) | 29,236 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 214ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 100.0% of stake.
- **Agave**: latest release v4.4.1 · running 4.4.0 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 10656 ms |
| solana_rpc_validators | OK | 259 ms |
| coingecko | OK | 1724 ms |
| defillama_tvl | OK | 4504 ms |
| defillama_dex | OK | 132 ms |
| defillama_fees | OK | 938 ms |
| defillama_stablecoins | OK | 766 ms |
| defillama_xstocks | FAILED | 85 ms |
| jito_kobe | OK | 8673 ms |
| stakewiz | OK | 1103 ms |
| github | OK | 817 ms |
| solana_com_news | FAILED | 87 ms |
| sentiment | OK | 2274 ms |
| solana_status_page | OK | 429 ms |
| solana_rpc_whales | OK | 1143 ms |
| solana_rpc_programs | OK | 2077 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*