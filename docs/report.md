# Solbeat — State of the Solana Network

> Generated 2026-11-23T04:43:47Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1094 is 47% complete (~14h remaining), with the cluster processing ~1,306 TPS (1,306 non-vote). Measured slot time is 213ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $363.0K of Real Economic Value over the last 24h ($252/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $71.23 (+2.6% / 24h). Decentralization: Nakamoto coefficient 18, 662 active validators, 0.0% of stake delinquent. Alpenglow readiness: validators holding 100% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 3 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 472,812,963 |
| Block height | 450,826,543 |
| Epoch | 1094 (47.45% complete, ~13.5h left) |
| TPS (10 min avg) | 1,306 |
| Non-vote TPS | 1,306 |
| Slot time (measured) | 213.3 ms |
| Confirmation time (measured) | 0.21 s |
| Finality time (measured) | 0.21 s — **Alpenglow active** |
| Est. daily transactions | 143,813,867 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0020 |
| Node version | 4.4.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $71.23 (+2.6%/24h) |
| Market cap | $42.2B |
| **REV (24h)** | **$363.0K** (fees $287.1K + Jito tips $75.8K) |
| Chain TVL | $4.6B |
| Stablecoin supply | $13.3B |
| DEX volume (24h) | $1.2B (-11.8%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 592,016,784 SOL |
| Inflation | 3.54% |

Top DEXs by 24h volume: BisonFi ($153.4M), Orca DEX ($132.4M), Scorch ($127.9M), PumpSwap ($109.8M), Raydium AMM ($99.4M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 662 / 23 |
| Delinquent stake | 0.01% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 25.0% |
| Avg / median commission | 12.9% / 5.0% |
| Alpenglow BLS-key readiness | 671 validators, 100.0% of stake |

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

- **[WARNING]** Solana TVL contraction (z=-2.2 vs its recent baseline)
- **[WARNING]** Stablecoin supply contraction (z=-2.7 vs its recent baseline)
- **[WARNING · liquidity_rotation]** Stablecoin supply and TVL moving together — capital rotating in or out of the chain.

## Solana Pulse — sentiment (experimental)

**43/100 — Neutral** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 63.6 |
| fear greed | 11 |
| momentum | 42.2 |
| news | 58 |

Crypto Fear & Greed: 11 (Extreme Fear) · CoinGecko votes bullish: 63.64% · headline tone (48h): +1

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 401 |
| Raydium AMM v4 | 548 |
| Orca Whirlpool | 401 |
| Pump.fun | 1,500 |
| Tensor | 0 |
| Magic Eden v2 | 31 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,300,003 |
| Binance (cold) | 66 |
| OKX (attributed) | 120,739 |
| Coinbase (hot) | 34,148 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 213ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 100.0% of stake.
- **Agave**: latest release v4.4.1 · running 4.4.0 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 9279 ms |
| solana_rpc_validators | OK | 325 ms |
| coingecko | OK | 1740 ms |
| defillama_tvl | OK | 488 ms |
| defillama_dex | OK | 1171 ms |
| defillama_fees | OK | 1041 ms |
| defillama_stablecoins | OK | 942 ms |
| defillama_xstocks | FAILED | 869 ms |
| jito_kobe | OK | 178 ms |
| stakewiz | OK | 1369 ms |
| github | OK | 617 ms |
| solana_com_news | FAILED | 120 ms |
| sentiment | OK | 2201 ms |
| solana_status_page | OK | 252 ms |
| solana_rpc_whales | OK | 1158 ms |
| solana_rpc_programs | OK | 2044 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*