# Solbeat — State of the Solana Network

> Generated 2026-11-09T16:59:13Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1081 is 93% complete (~2h remaining), with the cluster processing ~1,941 TPS (1,941 non-vote). Measured slot time is 216ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $509.5K of Real Economic Value over the last 24h ($354/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $86.95 (-2.2% / 24h). Decentralization: Nakamoto coefficient 18, 660 active validators, 0.2% of stake delinquent. Alpenglow readiness: validators holding 100% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 1 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 467,393,268 |
| Block height | 445,411,120 |
| Epoch | 1081 (92.89% complete, ~1.8h left) |
| TPS (10 min avg) | 1,941 |
| Non-vote TPS | 1,941 |
| Slot time (measured) | 216.0 ms |
| Confirmation time (measured) | 0.22 s |
| Finality time (measured) | 0.22 s — **Alpenglow active** |
| Est. daily transactions | 153,834,745 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0027 |
| Node version | 4.4.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $86.95 (-2.2%/24h) |
| Market cap | $51.4B |
| **REV (24h)** | **$509.5K** (fees $408.0K + Jito tips $101.5K) |
| Chain TVL | $5.1B |
| Stablecoin supply | $15.0B |
| DEX volume (24h) | $1.0B (13.7%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 591,093,528 SOL |
| Inflation | 3.57% |

Top DEXs by 24h volume: Orca DEX ($235.0M), PumpSwap ($165.3M), Raydium AMM ($141.2M), BisonFi ($103.4M), Meteora DLMM ($98.0M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 660 / 37 |
| Delinquent stake | 0.18% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.6% |
| Avg / median commission | 12.9% / 5.0% |
| Alpenglow BLS-key readiness | 684 validators, 100.0% of stake |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L43ZWjwCHART3o…` | 17,050,553 | 3.93% | 7% |
| 2 | `he1iusunGwqrNtafDtLd…` | 16,720,131 | 3.85% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5…` | 13,021,912 | 3.0% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxb…` | 10,279,070 | 2.37% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxA…` | 9,553,388 | 2.2% | 5% |
| 6 | `51JBzSTU5rAM8gLAVQKg…` | 9,550,278 | 2.2% | 10% |
| 7 | `26pV97Ce83ZQ6Kz9XT4t…` | 9,222,876 | 2.13% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2Fp…` | 7,775,137 | 1.79% | 7% |
| 9 | `DumiCKHVqoCQKD8roLAp…` | 6,980,319 | 1.61% | 0% |
| 10 | `CvSb7wdQAFpHuSpTYTJn…` | 6,711,284 | 1.55% | 5% |

## Signals (anomaly detection)

- **[WARNING]** Stablecoin supply contraction (z=-2.3 vs its recent baseline)

## Solana Pulse — sentiment (experimental)

**46/100 — Neutral** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 63.2 |
| fear greed | 29 |
| momentum | 44.4 |
| news | 42 |

Crypto Fear & Greed: 29 (Fear) · CoinGecko votes bullish: 63.16% · headline tone (48h): -1

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 1,500 |
| Raydium AMM v4 | 910 |
| Orca Whirlpool | 1,500 |
| Pump.fun | 1,500 |
| Tensor | 0 |
| Magic Eden v2 | 34 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,300,003 |
| Binance (cold) | 66 |
| OKX (attributed) | 97,596 |
| Coinbase (hot) | 26,689 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 216ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 100.0% of stake.
- **Agave**: latest release v4.4.1 · running 4.4.0 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 11093 ms |
| solana_rpc_validators | OK | 203 ms |
| coingecko | OK | 1707 ms |
| defillama_tvl | OK | 160 ms |
| defillama_dex | OK | 73 ms |
| defillama_fees | OK | 733 ms |
| defillama_stablecoins | OK | 207 ms |
| defillama_xstocks | FAILED | 39 ms |
| jito_kobe | OK | 308 ms |
| stakewiz | OK | 949 ms |
| github | OK | 641 ms |
| solana_com_news | FAILED | 64 ms |
| sentiment | OK | 2122 ms |
| solana_status_page | OK | 319 ms |
| solana_rpc_whales | OK | 2348 ms |
| solana_rpc_programs | OK | 1381 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*