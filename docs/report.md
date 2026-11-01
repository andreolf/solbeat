# Solbeat — State of the Solana Network

> Generated 2026-11-01T04:06:18Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1073 is 96% complete (~1h remaining), with the cluster processing ~1,174 TPS (1,174 non-vote). Measured slot time is 215ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $460.5K of Real Economic Value over the last 24h ($320/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $95.39 (-0.8% / 24h). Decentralization: Nakamoto coefficient 18, 664 active validators, 1.4% of stake delinquent. Alpenglow readiness: validators holding 100% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 1 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 463,951,375 |
| Block height | 441,973,141 |
| Epoch | 1073 (96.15% complete, ~1.0h left) |
| TPS (10 min avg) | 1,174 |
| Non-vote TPS | 1,174 |
| Slot time (measured) | 214.7 ms |
| Confirmation time (measured) | 0.21 s |
| Finality time (measured) | 0.21 s — **Alpenglow active** |
| Est. daily transactions | 130,245,519 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0028 |
| Node version | 4.3.2 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $95.39 (-0.8%/24h) |
| Market cap | $56.3B |
| **REV (24h)** | **$460.5K** (fees $364.2K + Jito tips $96.3K) |
| Chain TVL | $5.4B |
| Stablecoin supply | $15.4B |
| DEX volume (24h) | $1.4B (-31.9%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 590,094,894 SOL |
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

**47/100 — Neutral** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 77.8 |
| fear greed | 34 |
| momentum | 23.1 |
| news | 58 |

Crypto Fear & Greed: 34 (Fear) · CoinGecko votes bullish: 77.78% · headline tone (48h): +1

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 777 |
| Raydium AMM v4 | 512 |
| Orca Whirlpool | 382 |
| Pump.fun | 1,500 |
| Tensor | 0 |
| Magic Eden v2 | 94 |
| Marinade | 1 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 11,890,003 |
| Binance (cold) | 4 |
| OKX (attributed) | 339,500 |
| Coinbase (hot) | 80,176 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 215ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 100.0% of stake.
- **Agave**: latest release v4.4.0 · running 4.3.2 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 10378 ms |
| solana_rpc_validators | OK | 368 ms |
| coingecko | OK | 1770 ms |
| defillama_tvl | OK | 123 ms |
| defillama_dex | OK | 1723 ms |
| defillama_fees | OK | 1202 ms |
| defillama_stablecoins | OK | 143 ms |
| defillama_xstocks | FAILED | 56 ms |
| jito_kobe | OK | 235 ms |
| stakewiz | OK | 1199 ms |
| github | OK | 859 ms |
| solana_com_news | FAILED | 164 ms |
| sentiment | OK | 2215 ms |
| solana_status_page | OK | 395 ms |
| solana_rpc_whales | OK | 1289 ms |
| solana_rpc_programs | OK | 2065 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*