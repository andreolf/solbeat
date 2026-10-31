# Solbeat — State of the Solana Network

> Generated 2026-10-31T16:35:13Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1073 is 51% complete (~12h remaining), with the cluster processing ~2,152 TPS (2,152 non-vote). Measured slot time is 215ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $588.7K of Real Economic Value over the last 24h ($409/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $95.92 (+0.8% / 24h). Decentralization: Nakamoto coefficient 18, 665 active validators, 0.8% of stake delinquent. Alpenglow readiness: validators holding 100% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 1 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 463,757,685 |
| Block height | 441,779,523 |
| Epoch | 1073 (51.32% complete, ~12.5h left) |
| TPS (10 min avg) | 2,152 |
| Non-vote TPS | 2,152 |
| Slot time (measured) | 214.7 ms |
| Confirmation time (measured) | 0.21 s |
| Finality time (measured) | 0.21 s — **Alpenglow active** |
| Est. daily transactions | 111,659,283 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0044 |
| Node version | 4.3.2 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $95.92 (+0.8%/24h) |
| Market cap | $56.6B |
| **REV (24h)** | **$588.7K** (fees $491.9K + Jito tips $96.8K) |
| Chain TVL | $5.4B |
| Stablecoin supply | $15.4B |
| DEX volume (24h) | $2.1B (-7.8%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 590,095,074 SOL |
| Inflation | 3.58% |

Top DEXs by 24h volume: Orca DEX ($236.9M), PumpSwap ($221.7M), BisonFi ($182.9M), Tessera V ($181.4M), Meteora DLMM ($131.9M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 665 / 27 |
| Delinquent stake | 0.85% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.7% |
| Avg / median commission | 13.1% / 5% |
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

- **[WARNING]** TPS spike: 2,152 vs 12h mean 1,274 (z=+2.9)

## Solana Pulse — sentiment (experimental)

**52/100 — Neutral** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 80.0 |
| fear greed | 30 |
| momentum | 34.1 |
| news | 66 |

Crypto Fear & Greed: 30 (Fear) · CoinGecko votes bullish: 80.0% · headline tone (48h): +2

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 934 |
| Raydium AMM v4 | 1,500 |
| Orca Whirlpool | 934 |
| Pump.fun | 1,500 |
| Tensor | 2 |
| Magic Eden v2 | 66 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 11,890,003 |
| Binance (cold) | 4 |
| OKX (attributed) | 339,498 |
| Coinbase (hot) | 5,606 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 215ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 100.0% of stake.
- **Agave**: latest release v4.4.0 · running 4.3.2 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 10178 ms |
| solana_rpc_validators | OK | 157 ms |
| coingecko | OK | 1615 ms |
| defillama_tvl | OK | 83 ms |
| defillama_dex | OK | 768 ms |
| defillama_fees | OK | 74 ms |
| defillama_stablecoins | OK | 186 ms |
| defillama_xstocks | FAILED | 521 ms |
| jito_kobe | OK | 168 ms |
| stakewiz | OK | 902 ms |
| github | OK | 573 ms |
| solana_com_news | FAILED | 43 ms |
| sentiment | OK | 2094 ms |
| solana_status_page | OK | 76 ms |
| solana_rpc_whales | OK | 1092 ms |
| solana_rpc_programs | OK | 1498 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*