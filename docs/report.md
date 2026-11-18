# Solbeat — State of the Solana Network

> Generated 2026-11-18T07:09:35Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1089 is 92% complete (~2h remaining), with the cluster processing ~1,426 TPS (1,426 non-vote). Measured slot time is 214ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $572.5K of Real Economic Value over the last 24h ($398/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $74.91 (+2.8% / 24h). Decentralization: Nakamoto coefficient 18, 661 active validators, 0.0% of stake delinquent. Alpenglow readiness: validators holding 100% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 3 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 470,846,105 |
| Block height | 448,860,751 |
| Epoch | 1089 (92.15% complete, ~2.0h left) |
| TPS (10 min avg) | 1,426 |
| Non-vote TPS | 1,426 |
| Slot time (measured) | 214.5 ms |
| Confirmation time (measured) | 0.21 s |
| Finality time (measured) | 0.21 s — **Alpenglow active** |
| Est. daily transactions | 136,785,584 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0033 |
| Node version | 4.4.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $74.91 (+2.8%/24h) |
| Market cap | $44.3B |
| **REV (24h)** | **$572.5K** (fees $445.2K + Jito tips $127.3K) |
| Chain TVL | $4.8B |
| Stablecoin supply | $13.9B |
| DEX volume (24h) | $1.5B (1.2%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 591,739,405 SOL |
| Inflation | 3.55% |

Top DEXs by 24h volume: Orca DEX ($231.6M), Meteora DLMM ($155.8M), PumpSwap ($155.3M), BisonFi ($148.8M), Raydium AMM ($130.8M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 661 / 5 |
| Delinquent stake | 0.01% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.8% |
| Avg / median commission | 12.8% / 5% |
| Alpenglow BLS-key readiness | 686 validators, 100.0% of stake |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `he1iusunGwqrNtafDtLd…` | 16,834,343 | 3.93% | 0% |
| 2 | `CcaHc2L43ZWjwCHART3o…` | 16,442,668 | 3.83% | 7% |
| 3 | `3N7s9zXMZ4QqvHQR15t5…` | 12,432,778 | 2.9% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxb…` | 10,144,846 | 2.37% | 0% |
| 5 | `51JBzSTU5rAM8gLAVQKg…` | 9,802,677 | 2.29% | 10% |
| 6 | `CatzoSMUkTRidT5DwBxA…` | 9,625,021 | 2.24% | 5% |
| 7 | `26pV97Ce83ZQ6Kz9XT4t…` | 9,218,745 | 2.15% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2Fp…` | 7,970,891 | 1.86% | 7% |
| 9 | `DumiCKHVqoCQKD8roLAp…` | 6,996,288 | 1.63% | 0% |
| 10 | `CvSb7wdQAFpHuSpTYTJn…` | 6,730,472 | 1.57% | 5% |

## Signals (anomaly detection)

- **[WARNING]** Solana TVL contraction (z=-2.2 vs its recent baseline)
- **[WARNING]** Stablecoin supply contraction (z=-2.6 vs its recent baseline)
- **[WARNING · liquidity_rotation]** Stablecoin supply and TVL moving together — capital rotating in or out of the chain.

## Solana Pulse — sentiment (experimental)

**46/100 — Neutral** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 77.1 |
| fear greed | 11 |
| momentum | 35.7 |
| news | 66 |

Crypto Fear & Greed: 11 (Extreme Fear) · CoinGecko votes bullish: 77.08% · headline tone (48h): +2

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 1,110 |
| Raydium AMM v4 | 1,110 |
| Orca Whirlpool | 1,500 |
| Pump.fun | 1,500 |
| Tensor | 0 |
| Magic Eden v2 | 46 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,300,003 |
| Binance (cold) | 66 |
| OKX (attributed) | 34,418 |
| Coinbase (hot) | 43,698 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 214ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 100.0% of stake.
- **Agave**: latest release v4.4.1 · running 4.4.0 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 9196 ms |
| solana_rpc_validators | OK | 93 ms |
| coingecko | OK | 1692 ms |
| defillama_tvl | OK | 43 ms |
| defillama_dex | OK | 29 ms |
| defillama_fees | OK | 297 ms |
| defillama_stablecoins | OK | 49 ms |
| defillama_xstocks | FAILED | 20 ms |
| jito_kobe | OK | 188 ms |
| stakewiz | OK | 676 ms |
| github | OK | 602 ms |
| solana_com_news | FAILED | 29 ms |
| sentiment | OK | 2117 ms |
| solana_status_page | OK | 216 ms |
| solana_rpc_whales | OK | 810 ms |
| solana_rpc_programs | OK | 1401 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*