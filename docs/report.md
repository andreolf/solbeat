# Solbeat — State of the Solana Network

> Generated 2026-10-29T02:08:55Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1071 is 8% complete (~24h remaining), with the cluster processing ~2,719 TPS (2,719 non-vote). Measured slot time is 214ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $656.6K of Real Economic Value over the last 24h ($456/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $99.63 (-1.8% / 24h). Decentralization: Nakamoto coefficient 18, 664 active validators, 3.8% of stake delinquent. Alpenglow readiness: validators holding 100% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 3 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 462,707,034 |
| Block height | 440,730,750 |
| Epoch | 1071 (8.11% complete, ~23.6h left) |
| TPS (10 min avg) | 2,719 |
| Non-vote TPS | 2,719 |
| Slot time (measured) | 213.8 ms |
| Confirmation time (measured) | 0.21 s |
| Finality time (measured) | 0.21 s — **Alpenglow active** |
| Est. daily transactions | 157,717,134 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0033 |
| Node version | 4.3.2 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $99.63 (-1.8%/24h) |
| Market cap | $58.8B |
| **REV (24h)** | **$656.6K** (fees $527.1K + Jito tips $129.4K) |
| Chain TVL | $5.7B |
| Stablecoin supply | $15.6B |
| DEX volume (24h) | $1.6B (2.6%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 589,983,954 SOL |
| Inflation | 3.58% |

Top DEXs by 24h volume: Orca DEX ($235.7M), BisonFi ($191.2M), Manifest Trade ($181.9M), Raydium AMM ($163.6M), Tessera V ($142.3M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 664 / 25 |
| Delinquent stake | 3.81% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.5% |
| Avg / median commission | 12.6% / 5.0% |
| Alpenglow BLS-key readiness | 679 validators, 100.0% of stake |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L43ZWjwCHART3o…` | 17,028,574 | 3.9% | 7% |
| 2 | `he1iusunGwqrNtafDtLd…` | 16,665,444 | 3.82% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5…` | 12,878,826 | 2.95% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxb…` | 10,762,073 | 2.46% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxA…` | 9,705,356 | 2.22% | 5% |
| 6 | `51JBzSTU5rAM8gLAVQKg…` | 9,466,646 | 2.17% | 10% |
| 7 | `26pV97Ce83ZQ6Kz9XT4t…` | 9,218,110 | 2.11% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2Fp…` | 7,761,555 | 1.78% | 7% |
| 9 | `DumiCKHVqoCQKD8roLAp…` | 6,998,037 | 1.6% | 0% |
| 10 | `CvSb7wdQAFpHuSpTYTJn…` | 6,646,428 | 1.52% | 5% |

## Signals (anomaly detection)

- **[WARNING]** TPS spike: 2,719 vs 12h mean 1,799 (z=+2.0)
- **[WARNING]** Elevated delinquency: 3.8% of stake delinquent
- **[SERIOUS · network_incident]** Correlated network incident: throughput anomaly coinciding with validator delinquency — consistent with cluster-level degradation, not a demand shift.

## Solana Pulse — sentiment (experimental)

**58/100 — Neutral** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 76.9 |
| fear greed | 51 |
| momentum | 43.5 |
| news | 58 |

Crypto Fear & Greed: 51 (Neutral) · CoinGecko votes bullish: 76.92% · headline tone (48h): +1

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 1,500 |
| Raydium AMM v4 | 1,500 |
| Orca Whirlpool | 1,500 |
| Pump.fun | 1,500 |
| Tensor | 1 |
| Magic Eden v2 | 63 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 11,175,975 |
| Binance (cold) | 1,584,859 |
| OKX (attributed) | 330,877 |
| Coinbase (hot) | 14,134 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 214ms.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 100.0% of stake.
- **Agave**: latest release None · running 4.3.2 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 9919 ms |
| solana_rpc_validators | OK | 235 ms |
| coingecko | OK | 1634 ms |
| defillama_tvl | OK | 71 ms |
| defillama_dex | OK | 786 ms |
| defillama_fees | OK | 1031 ms |
| defillama_stablecoins | OK | 92 ms |
| defillama_xstocks | FAILED | 56 ms |
| jito_kobe | OK | 472 ms |
| stakewiz | OK | 1017 ms |
| github | FAILED | 6183 ms |
| solana_com_news | FAILED | 54 ms |
| sentiment | OK | 2090 ms |
| solana_status_page | OK | 166 ms |
| solana_rpc_whales | OK | 894 ms |
| solana_rpc_programs | OK | 1581 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*