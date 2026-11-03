# Solbeat — State of the Solana Network

> Generated 2026-11-03T04:46:34Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1075 is 85% complete (~4h remaining), with the cluster processing ~1,377 TPS (1,377 non-vote). Measured slot time is 212ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. SOL trades at $92.21 (-3.0% / 24h). Decentralization: Nakamoto coefficient 18, 664 active validators, 2.1% of stake delinquent. Alpenglow readiness: validators holding 100% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: all clear across every monitored metric.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 464,769,288 |
| Block height | 442,790,334 |
| Epoch | 1075 (85.48% complete, ~3.7h left) |
| TPS (10 min avg) | 1,377 |
| Non-vote TPS | 1,377 |
| Slot time (measured) | 212.4 ms |
| Confirmation time (measured) | 0.21 s |
| Finality time (measured) | 0.21 s — **Alpenglow active** |
| Est. daily transactions | 140,815,970 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0000 |
| Node version | 4.3.2 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $92.21 (-3.0%/24h) |
| Market cap | $54.4B |
| **REV (24h)** | **n/a** (fees n/a + Jito tips n/a) |
| Chain TVL | $5.4B |
| Stablecoin supply | $15.3B |
| DEX volume (24h) | n/a (None%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 590,206,243 SOL |
| Inflation | 3.57% |

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 664 / 29 |
| Delinquent stake | 2.08% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.7% |
| Avg / median commission | 12.8% / 5.0% |
| Alpenglow BLS-key readiness | 680 validators, 100.0% of stake |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L43ZWjwCHART3o…` | 17,034,354 | 3.92% | 7% |
| 2 | `he1iusunGwqrNtafDtLd…` | 16,710,199 | 3.85% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5…` | 13,037,180 | 3.0% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxb…` | 10,429,501 | 2.4% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxA…` | 9,580,109 | 2.21% | 5% |
| 6 | `51JBzSTU5rAM8gLAVQKg…` | 9,453,055 | 2.18% | 10% |
| 7 | `26pV97Ce83ZQ6Kz9XT4t…` | 9,226,805 | 2.13% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2Fp…` | 7,803,392 | 1.8% | 7% |
| 9 | `DumiCKHVqoCQKD8roLAp…` | 7,001,891 | 1.61% | 0% |
| 10 | `CvSb7wdQAFpHuSpTYTJn…` | 6,978,080 | 1.61% | 5% |

## Signals (anomaly detection)

All clear — no anomalies across monitored metrics.

## Solana Pulse — sentiment (experimental)

**44/100 — Neutral** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 70.0 |
| fear greed | 26 |
| momentum | 30.1 |
| news | 50 |

Crypto Fear & Greed: 26 (Fear) · CoinGecko votes bullish: 70.0% · headline tone (48h): +0

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 808 |
| Raydium AMM v4 | 525 |
| Orca Whirlpool | 1,500 |
| Pump.fun | 1,500 |
| Tensor | 0 |
| Magic Eden v2 | 41 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,890,003 |
| Binance (cold) | 4 |
| OKX (attributed) | 339,502 |
| Coinbase (hot) | 15,888 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 212ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 100.0% of stake.
- **Agave**: latest release v4.4.0 · running 4.3.2 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 9330 ms |
| solana_rpc_validators | OK | 142 ms |
| coingecko | OK | 1803 ms |
| defillama_tvl | OK | 94 ms |
| defillama_dex | FAILED | 66145 ms |
| defillama_fees | FAILED | 66131 ms |
| defillama_stablecoins | OK | 3091 ms |
| defillama_xstocks | FAILED | 10261 ms |
| jito_kobe | OK | 164 ms |
| stakewiz | OK | 106551 ms |
| github | OK | 1025 ms |
| solana_com_news | FAILED | 153 ms |
| sentiment | OK | 2476 ms |
| solana_status_page | OK | 268 ms |
| solana_rpc_whales | OK | 1089 ms |
| solana_rpc_programs | OK | 1793 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*