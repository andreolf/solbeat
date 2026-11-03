# Solbeat — State of the Solana Network

> Generated 2026-11-03T04:09:04Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1075 is 83% complete (~4h remaining), with the cluster processing ~1,432 TPS (1,432 non-vote). Measured slot time is 215ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. SOL trades at $91.93 (-3.6% / 24h). Decentralization: Nakamoto coefficient 18, 664 active validators, 1.1% of stake delinquent. Anomaly scan: all clear across every monitored metric.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 464,758,718 |
| Block height | 442,779,792 |
| Epoch | 1075 (83.04% complete, ~4.4h left) |
| TPS (10 min avg) | 1,432 |
| Non-vote TPS | 1,432 |
| Slot time (measured) | 215.3 ms |
| Confirmation time (measured) | 0.22 s |
| Finality time (measured) | 0.22 s — **Alpenglow active** |
| Est. daily transactions | 143,531,653 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0000 |
| Node version | 4.3.2 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $91.93 (-3.6%/24h) |
| Market cap | $54.2B |
| **REV (24h)** | **n/a** (fees n/a + Jito tips n/a) |
| Chain TVL | $5.4B |
| Stablecoin supply | $15.3B |
| DEX volume (24h) | n/a (None%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 590,206,252 SOL |
| Inflation | 3.57% |

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 664 / 29 |
| Delinquent stake | 1.09% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.7% |
| Avg / median commission | 12.8% / 5.0% |

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
| momentum | 29.7 |
| news | 50 |

Crypto Fear & Greed: 26 (Fear) · CoinGecko votes bullish: 70.0% · headline tone (48h): +0

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 1,500 |
| Raydium AMM v4 | 869 |
| Orca Whirlpool | 869 |
| Pump.fun | 1,500 |
| Tensor | 0 |
| Magic Eden v2 | 47 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,890,003 |
| Binance (cold) | 4 |
| OKX (attributed) | 339,502 |
| Coinbase (hot) | 15,358 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 215ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at ?% of stake.
- **Agave**: latest release v4.4.0 · running 4.3.2 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 8881 ms |
| solana_rpc_validators | OK | 211 ms |
| coingecko | OK | 1832 ms |
| defillama_tvl | OK | 109 ms |
| defillama_dex | FAILED | 113709 ms |
| defillama_fees | FAILED | 66158 ms |
| defillama_stablecoins | OK | 1157 ms |
| defillama_xstocks | FAILED | 65 ms |
| jito_kobe | OK | 271 ms |
| stakewiz | FAILED | 248626 ms |
| github | OK | 975 ms |
| solana_com_news | FAILED | 101 ms |
| sentiment | OK | 2317 ms |
| solana_status_page | OK | 314 ms |
| solana_rpc_whales | OK | 906 ms |
| solana_rpc_programs | OK | 1530 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*