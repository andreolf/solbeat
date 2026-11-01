# Solbeat — State of the Solana Network

> Generated 2026-11-01T03:35:52Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1073 is 94% complete (~2h remaining), with the cluster processing ~1,138 TPS (1,138 non-vote). Measured slot time is 214ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $461.1K of Real Economic Value over the last 24h ($320/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $95.55 (-1.0% / 24h). Decentralization: Nakamoto coefficient 18, 664 active validators, 1.4% of stake delinquent. Alpenglow readiness: validators holding 100% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 1 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 463,942,858 |
| Block height | 441,964,628 |
| Epoch | 1073 (94.18% complete, ~1.5h left) |
| TPS (10 min avg) | 1,138 |
| Non-vote TPS | 1,138 |
| Slot time (measured) | 213.8 ms |
| Confirmation time (measured) | 0.21 s |
| Finality time (measured) | 0.21 s — **Alpenglow active** |
| Est. daily transactions | 134,520,264 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0027 |
| Node version | 4.3.2 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $95.55 (-1.0%/24h) |
| Market cap | $56.7B |
| **REV (24h)** | **$461.1K** (fees $364.2K + Jito tips $96.9K) |
| Chain TVL | $5.4B |
| Stablecoin supply | $15.4B |
| DEX volume (24h) | $1.4B (-31.9%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 590,094,900 SOL |
| Inflation | 3.58% |

Top DEXs by 24h volume: BisonFi ($182.9M), Tessera V ($181.4M), PumpSwap ($130.7M), Orca DEX ($117.7M), pump.fun ($113.6M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 664 / 28 |
| Delinquent stake | 1.42% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.7% |
| Avg / median commission | 13.1% / 5.0% |
| Alpenglow BLS-key readiness | 679 validators, 100.0% of stake |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L43ZWjwCHART3o…` | 17,020,574 | 3.92% | 7% |
| 2 | `he1iusunGwqrNtafDtLd…` | 16,688,715 | 3.85% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5…` | 12,931,864 | 2.98% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxb…` | 10,425,467 | 2.4% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxA…` | 9,651,671 | 2.23% | 5% |
| 6 | `51JBzSTU5rAM8gLAVQKg…` | 9,449,481 | 2.18% | 10% |
| 7 | `26pV97Ce83ZQ6Kz9XT4t…` | 9,227,526 | 2.13% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2Fp…` | 7,778,595 | 1.79% | 7% |
| 9 | `DumiCKHVqoCQKD8roLAp…` | 7,000,338 | 1.61% | 0% |
| 10 | `CvSb7wdQAFpHuSpTYTJn…` | 6,976,145 | 1.61% | 5% |

## Signals (anomaly detection)

- **[WARNING]** Real Economic Value deviating from its run-history baseline (z=-2.2)

## Solana Pulse — sentiment (experimental)

**48/100 — Neutral** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 78.6 |
| fear greed | 34 |
| momentum | 23.3 |
| news | 58 |

Crypto Fear & Greed: 34 (Fear) · CoinGecko votes bullish: 78.57% · headline tone (48h): +1

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 1,402 |
| Raydium AMM v4 | 489 |
| Orca Whirlpool | 1,500 |
| Pump.fun | 1,500 |
| Tensor | 0 |
| Magic Eden v2 | 50 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 11,890,003 |
| Binance (cold) | 4 |
| OKX (attributed) | 339,500 |
| Coinbase (hot) | 80,266 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 214ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 100.0% of stake.
- **Agave**: latest release v4.4.0 · running 4.3.2 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 9735 ms |
| solana_rpc_validators | OK | 386 ms |
| coingecko | OK | 1719 ms |
| defillama_tvl | OK | 245 ms |
| defillama_dex | OK | 985 ms |
| defillama_fees | OK | 1640 ms |
| defillama_stablecoins | OK | 149 ms |
| defillama_xstocks | FAILED | 652 ms |
| jito_kobe | OK | 249 ms |
| stakewiz | OK | 1161 ms |
| github | OK | 860 ms |
| solana_com_news | FAILED | 136 ms |
| sentiment | OK | 2299 ms |
| solana_status_page | OK | 376 ms |
| solana_rpc_whales | OK | 1384 ms |
| solana_rpc_programs | OK | 2427 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*