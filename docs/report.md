# Solbeat — State of the Solana Network

> Generated 2026-10-30T13:34:41Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1072 is 46% complete (~14h remaining), with the cluster processing ~2,090 TPS (2,090 non-vote). Measured slot time is 212ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $711.7K of Real Economic Value over the last 24h ($494/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $95.49 (-4.9% / 24h). Decentralization: Nakamoto coefficient 18, 666 active validators, 0.7% of stake delinquent. Alpenglow readiness: validators holding 100% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 1 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 463,303,823 |
| Block height | 441,326,182 |
| Epoch | 1072 (46.26% complete, ~13.7h left) |
| TPS (10 min avg) | 2,090 |
| Non-vote TPS | 2,090 |
| Slot time (measured) | 212.3 ms |
| Confirmation time (measured) | 0.21 s |
| Finality time (measured) | 0.21 s — **Alpenglow active** |
| Est. daily transactions | 110,532,606 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0051 |
| Node version | 4.3.2 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $95.49 (-4.9%/24h) |
| Market cap | $56.6B |
| **REV (24h)** | **$711.7K** (fees $564.5K + Jito tips $147.2K) |
| Chain TVL | $5.4B |
| Stablecoin supply | $15.4B |
| DEX volume (24h) | $2.3B (32.4%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 590,039,877 SOL |
| Inflation | 3.58% |

Top DEXs by 24h volume: Orca DEX ($456.3M), BisonFi ($301.3M), Manifest Trade ($253.6M), Tessera V ($209.3M), Raydium AMM ($200.3M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 666 / 25 |
| Delinquent stake | 0.69% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.6% |
| Avg / median commission | 12.7% / 5.0% |
| Alpenglow BLS-key readiness | 679 validators, 100.0% of stake |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L43ZWjwCHART3o…` | 16,965,456 | 3.9% | 7% |
| 2 | `he1iusunGwqrNtafDtLd…` | 16,678,000 | 3.83% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5…` | 12,919,680 | 2.97% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxb…` | 10,502,229 | 2.41% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxA…` | 9,659,910 | 2.22% | 5% |
| 6 | `51JBzSTU5rAM8gLAVQKg…` | 9,473,552 | 2.18% | 10% |
| 7 | `26pV97Ce83ZQ6Kz9XT4t…` | 9,222,406 | 2.12% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2Fp…` | 7,780,140 | 1.79% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJn…` | 7,045,150 | 1.62% | 5% |
| 10 | `DumiCKHVqoCQKD8roLAp…` | 7,001,506 | 1.61% | 0% |

## Signals (anomaly detection)

- **[SERIOUS]** TPS spike: 2,090 vs 12h mean 1,263 (z=+4.3)

## Solana Pulse — sentiment (experimental)

**50/100 — Neutral** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 66.7 |
| fear greed | 30 |
| momentum | 50.1 |
| news | 50 |

Crypto Fear & Greed: 30 (Fear) · CoinGecko votes bullish: 66.67% · headline tone (48h): +0

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 1,500 |
| Raydium AMM v4 | 785 |
| Orca Whirlpool | 1,500 |
| Pump.fun | 1,500 |
| Tensor | 0 |
| Magic Eden v2 | 101 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 11,890,003 |
| Binance (cold) | 4 |
| OKX (attributed) | 339,483 |
| Coinbase (hot) | 15,894 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 212ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 100.0% of stake.
- **Agave**: latest release v4.4.0 · running 4.3.2 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 10491 ms |
| solana_rpc_validators | OK | 391 ms |
| coingecko | OK | 1821 ms |
| defillama_tvl | OK | 391 ms |
| defillama_dex | OK | 1062 ms |
| defillama_fees | OK | 1776 ms |
| defillama_stablecoins | OK | 246 ms |
| defillama_xstocks | FAILED | 726 ms |
| jito_kobe | OK | 184 ms |
| stakewiz | OK | 1210 ms |
| github | OK | 997 ms |
| solana_com_news | FAILED | 122 ms |
| sentiment | OK | 2316 ms |
| solana_status_page | OK | 329 ms |
| solana_rpc_whales | OK | 1277 ms |
| solana_rpc_programs | OK | 2526 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*