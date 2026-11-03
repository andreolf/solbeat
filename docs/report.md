# Solbeat — State of the Solana Network

> Generated 2026-11-03T19:44:21Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1076 is 44% complete (~14h remaining), with the cluster processing ~1,904 TPS (1,904 non-vote). Measured slot time is 215ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $593.7K of Real Economic Value over the last 24h ($412/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $93.12 (+2.4% / 24h). Decentralization: Nakamoto coefficient 18, 666 active validators, 0.4% of stake delinquent. Alpenglow readiness: validators holding 100% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: all clear across every monitored metric.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 465,020,794 |
| Block height | 443,041,456 |
| Epoch | 1076 (43.7% complete, ~14.5h left) |
| TPS (10 min avg) | 1,904 |
| Non-vote TPS | 1,904 |
| Slot time (measured) | 214.9 ms |
| Confirmation time (measured) | 0.21 s |
| Finality time (measured) | 0.21 s — **Alpenglow active** |
| Est. daily transactions | 198,786,769 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0024 |
| Node version | 4.4.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $93.12 (+2.4%/24h) |
| Market cap | $55.0B |
| **REV (24h)** | **$593.7K** (fees $482.2K + Jito tips $111.5K) |
| Chain TVL | $5.4B |
| Stablecoin supply | $15.3B |
| DEX volume (24h) | $1.9B (104.6%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 590,265,904 SOL |
| Inflation | 3.57% |

Top DEXs by 24h volume: PumpSwap ($261.1M), BisonFi ($250.5M), Orca DEX ($209.0M), Tessera V ($149.8M), Raydium AMM ($126.7M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 666 / 27 |
| Delinquent stake | 0.42% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.7% |
| Avg / median commission | 12.6% / 5.0% |
| Alpenglow BLS-key readiness | 680 validators, 100.0% of stake |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L43ZWjwCHART3o…` | 17,030,641 | 3.92% | 7% |
| 2 | `he1iusunGwqrNtafDtLd…` | 16,704,340 | 3.84% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5…` | 13,043,664 | 3.0% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxb…` | 10,431,126 | 2.4% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxA…` | 9,561,007 | 2.2% | 5% |
| 6 | `51JBzSTU5rAM8gLAVQKg…` | 9,435,905 | 2.17% | 10% |
| 7 | `26pV97Ce83ZQ6Kz9XT4t…` | 9,232,746 | 2.12% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2Fp…` | 7,814,810 | 1.8% | 7% |
| 9 | `DumiCKHVqoCQKD8roLAp…` | 7,008,986 | 1.61% | 0% |
| 10 | `CvSb7wdQAFpHuSpTYTJn…` | 6,979,031 | 1.61% | 5% |

## Signals (anomaly detection)

All clear — no anomalies across monitored metrics.

## Solana Pulse — sentiment (experimental)

**55/100 — Neutral** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 70.6 |
| fear greed | 26 |
| momentum | 53.2 |
| news | 74 |

Crypto Fear & Greed: 26 (Fear) · CoinGecko votes bullish: 70.59% · headline tone (48h): +3

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 1,500 |
| Raydium AMM v4 | 589 |
| Orca Whirlpool | 970 |
| Pump.fun | 1,500 |
| Tensor | 0 |
| Magic Eden v2 | 51 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,890,003 |
| Binance (cold) | 4 |
| OKX (attributed) | 339,403 |
| Coinbase (hot) | 17,273 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 215ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 100.0% of stake.
- **Agave**: latest release v4.4.0 · running 4.4.0 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 9117 ms |
| solana_rpc_validators | OK | 209 ms |
| coingecko | OK | 1854 ms |
| defillama_tvl | OK | 237 ms |
| defillama_dex | OK | 1185 ms |
| defillama_fees | OK | 1946 ms |
| defillama_stablecoins | OK | 194 ms |
| defillama_xstocks | FAILED | 834 ms |
| jito_kobe | OK | 799 ms |
| stakewiz | OK | 1448 ms |
| github | OK | 1118 ms |
| solana_com_news | FAILED | 95 ms |
| sentiment | OK | 2382 ms |
| solana_status_page | OK | 262 ms |
| solana_rpc_whales | OK | 1512 ms |
| solana_rpc_programs | OK | 1963 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*