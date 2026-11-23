# Solbeat — State of the Solana Network

> Generated 2026-11-23T05:44:43Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1094 is 51% complete (~13h remaining), with the cluster processing ~1,359 TPS (1,359 non-vote). Measured slot time is 215ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $362.8K of Real Economic Value over the last 24h ($252/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $71.75 (+4.5% / 24h). Decentralization: Nakamoto coefficient 18, 662 active validators, 0.0% of stake delinquent. Alpenglow readiness: validators holding 100% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 3 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 472,829,998 |
| Block height | 450,843,542 |
| Epoch | 1094 (51.39% complete, ~12.6h left) |
| TPS (10 min avg) | 1,359 |
| Non-vote TPS | 1,359 |
| Slot time (measured) | 215.3 ms |
| Confirmation time (measured) | 0.22 s |
| Finality time (measured) | 0.22 s — **Alpenglow active** |
| Est. daily transactions | 137,696,624 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0021 |
| Node version | 4.4.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $71.75 (+4.5%/24h) |
| Market cap | $42.5B |
| **REV (24h)** | **$362.8K** (fees $287.1K + Jito tips $75.7K) |
| Chain TVL | $4.6B |
| Stablecoin supply | $13.3B |
| DEX volume (24h) | $1.2B (-11.8%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 592,016,771 SOL |
| Inflation | 3.54% |

Top DEXs by 24h volume: BisonFi ($153.4M), Orca DEX ($149.9M), Scorch ($127.9M), PumpSwap ($109.8M), Raydium AMM ($104.7M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 662 / 23 |
| Delinquent stake | 0.01% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 25.0% |
| Avg / median commission | 13.0% / 5.0% |
| Alpenglow BLS-key readiness | 670 validators, 100.0% of stake |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `he1iusunGwqrNtafDtLd…` | 16,918,440 | 3.97% | 0% |
| 2 | `CcaHc2L43ZWjwCHART3o…` | 16,346,959 | 3.84% | 7% |
| 3 | `3N7s9zXMZ4QqvHQR15t5…` | 12,401,889 | 2.91% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxb…` | 10,243,005 | 2.41% | 0% |
| 5 | `51JBzSTU5rAM8gLAVQKg…` | 9,842,253 | 2.31% | 10% |
| 6 | `CatzoSMUkTRidT5DwBxA…` | 9,612,896 | 2.26% | 5% |
| 7 | `26pV97Ce83ZQ6Kz9XT4t…` | 9,269,555 | 2.18% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2Fp…` | 7,998,895 | 1.88% | 7% |
| 9 | `DumiCKHVqoCQKD8roLAp…` | 6,987,495 | 1.64% | 0% |
| 10 | `CvSb7wdQAFpHuSpTYTJn…` | 6,775,083 | 1.59% | 5% |

## Signals (anomaly detection)

- **[WARNING]** Solana TVL contraction (z=-2.1 vs its recent baseline)
- **[WARNING]** Stablecoin supply contraction (z=-2.7 vs its recent baseline)
- **[WARNING · liquidity_rotation]** Stablecoin supply and TVL moving together — capital rotating in or out of the chain.

## Solana Pulse — sentiment (experimental)

**43/100 — Neutral** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 64.7 |
| fear greed | 11 |
| momentum | 43.7 |
| news | 50 |

Crypto Fear & Greed: 11 (Extreme Fear) · CoinGecko votes bullish: 64.71% · headline tone (48h): +0

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 1,130 |
| Raydium AMM v4 | 451 |
| Orca Whirlpool | 1,130 |
| Pump.fun | 1,500 |
| Tensor | 0 |
| Magic Eden v2 | 23 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,300,003 |
| Binance (cold) | 66 |
| OKX (attributed) | 120,739 |
| Coinbase (hot) | 33,960 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 215ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 100.0% of stake.
- **Agave**: latest release v4.4.1 · running 4.4.0 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 9620 ms |
| solana_rpc_validators | OK | 261 ms |
| coingecko | OK | 1740 ms |
| defillama_tvl | OK | 209 ms |
| defillama_dex | OK | 1194 ms |
| defillama_fees | OK | 1075 ms |
| defillama_stablecoins | OK | 1707 ms |
| defillama_xstocks | FAILED | 845 ms |
| jito_kobe | OK | 245 ms |
| stakewiz | OK | 1465 ms |
| github | OK | 674 ms |
| solana_com_news | FAILED | 65 ms |
| sentiment | OK | 2648 ms |
| solana_status_page | OK | 318 ms |
| solana_rpc_whales | OK | 1131 ms |
| solana_rpc_programs | OK | 2806 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*