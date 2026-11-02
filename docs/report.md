# Solbeat — State of the Solana Network

> Generated 2026-11-02T05:05:54Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1074 is 93% complete (~2h remaining), with the cluster processing ~1,171 TPS (1,171 non-vote). Measured slot time is 216ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $441.2K of Real Economic Value over the last 24h ($306/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $94.89 (-0.6% / 24h). Decentralization: Nakamoto coefficient 18, 662 active validators, 1.1% of stake delinquent. Alpenglow readiness: validators holding 100% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 2 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 464,371,356 |
| Block height | 442,392,735 |
| Epoch | 1074 (93.37% complete, ~1.7h left) |
| TPS (10 min avg) | 1,171 |
| Non-vote TPS | 1,171 |
| Slot time (measured) | 215.6 ms |
| Confirmation time (measured) | 0.22 s |
| Finality time (measured) | 0.22 s — **Alpenglow active** |
| Est. daily transactions | 143,656,240 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0026 |
| Node version | 4.3.2 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $94.89 (-0.6%/24h) |
| Market cap | $56.0B |
| **REV (24h)** | **$441.2K** (fees $367.7K + Jito tips $73.5K) |
| Chain TVL | $5.5B |
| Stablecoin supply | $15.4B |
| DEX volume (24h) | $832.7M (-12.7%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 590,150,135 SOL |
| Inflation | 3.58% |

Top DEXs by 24h volume: PumpSwap ($122.9M), Orca DEX ($112.2M), pump.fun ($103.8M), GoonFi ($73.9M), Raydium AMM ($71.6M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 662 / 34 |
| Delinquent stake | 1.05% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.7% |
| Avg / median commission | 13.1% / 5.0% |
| Alpenglow BLS-key readiness | 677 validators, 100.0% of stake |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L43ZWjwCHART3o…` | 17,029,196 | 3.92% | 7% |
| 2 | `he1iusunGwqrNtafDtLd…` | 16,695,127 | 3.85% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5…` | 12,943,199 | 2.98% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxb…` | 10,426,987 | 2.4% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxA…` | 9,583,157 | 2.21% | 5% |
| 6 | `51JBzSTU5rAM8gLAVQKg…` | 9,451,197 | 2.18% | 10% |
| 7 | `26pV97Ce83ZQ6Kz9XT4t…` | 9,225,053 | 2.13% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2Fp…` | 7,791,639 | 1.8% | 7% |
| 9 | `DumiCKHVqoCQKD8roLAp…` | 7,001,293 | 1.61% | 0% |
| 10 | `CvSb7wdQAFpHuSpTYTJn…` | 6,977,108 | 1.61% | 5% |

## Signals (anomaly detection)

- **[WARNING]** DEX volume contraction (z=-2.1 vs its recent baseline)
- **[WARNING]** Real Economic Value deviating from its run-history baseline (z=-2.1)

## Solana Pulse — sentiment (experimental)

**50/100 — Neutral** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 71.4 |
| fear greed | 37 |
| momentum | 34.3 |
| news | 58 |

Crypto Fear & Greed: 37 (Fear) · CoinGecko votes bullish: 71.43% · headline tone (48h): +1

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 580 |
| Raydium AMM v4 | 418 |
| Orca Whirlpool | 418 |
| Pump.fun | 1,500 |
| Tensor | 0 |
| Magic Eden v2 | 129 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,890,003 |
| Binance (cold) | 4 |
| OKX (attributed) | 339,502 |
| Coinbase (hot) | 45,304 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 216ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 100.0% of stake.
- **Agave**: latest release v4.4.0 · running 4.3.2 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 9680 ms |
| solana_rpc_validators | OK | 261 ms |
| coingecko | OK | 1669 ms |
| defillama_tvl | OK | 106 ms |
| defillama_dex | OK | 1168 ms |
| defillama_fees | OK | 2083 ms |
| defillama_stablecoins | OK | 1230 ms |
| defillama_xstocks | FAILED | 31 ms |
| jito_kobe | OK | 256 ms |
| stakewiz | OK | 1359 ms |
| github | OK | 749 ms |
| solana_com_news | FAILED | 69 ms |
| sentiment | OK | 2160 ms |
| solana_status_page | OK | 371 ms |
| solana_rpc_whales | OK | 1046 ms |
| solana_rpc_programs | OK | 1744 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*