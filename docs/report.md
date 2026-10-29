# Solbeat — State of the Solana Network

> Generated 2026-10-29T02:52:12Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1071 is 11% complete (~23h remaining), with the cluster processing ~1,599 TPS (1,599 non-vote). Measured slot time is 214ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $656.5K of Real Economic Value over the last 24h ($456/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $99.78 (-1.8% / 24h). Decentralization: Nakamoto coefficient 18, 666 active validators, 0.7% of stake delinquent. Alpenglow readiness: validators holding 100% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: all clear across every monitored metric.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 462,719,184 |
| Block height | 440,742,779 |
| Epoch | 1071 (10.92% complete, ~22.9h left) |
| TPS (10 min avg) | 1,599 |
| Non-vote TPS | 1,599 |
| Slot time (measured) | 214.3 ms |
| Confirmation time (measured) | 0.21 s |
| Finality time (measured) | 0.21 s — **Alpenglow active** |
| Est. daily transactions | 153,464,278 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0034 |
| Node version | 4.3.2 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $99.78 (-1.8%/24h) |
| Market cap | $58.8B |
| **REV (24h)** | **$656.5K** (fees $527.1K + Jito tips $129.3K) |
| Chain TVL | $5.7B |
| Stablecoin supply | $15.6B |
| DEX volume (24h) | $1.6B (2.6%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 589,983,928 SOL |
| Inflation | 3.58% |

Top DEXs by 24h volume: Orca DEX ($235.7M), BisonFi ($191.2M), Manifest Trade ($181.9M), Raydium AMM ($163.6M), Tessera V ($142.3M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 666 / 23 |
| Delinquent stake | 0.74% |
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

All clear — no anomalies across monitored metrics.

## Solana Pulse — sentiment (experimental)

**59/100 — Neutral** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 80.8 |
| fear greed | 51 |
| momentum | 43.4 |
| news | 58 |

Crypto Fear & Greed: 51 (Neutral) · CoinGecko votes bullish: 80.77% · headline tone (48h): +1

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 1,368 |
| Raydium AMM v4 | 484 |
| Orca Whirlpool | 1,368 |
| Pump.fun | 1,500 |
| Tensor | 0 |
| Magic Eden v2 | 114 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 11,175,975 |
| Binance (cold) | 1,581,946 |
| OKX (attributed) | 330,877 |
| Coinbase (hot) | 13,825 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 214ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 100.0% of stake.
- **Agave**: latest release v4.3.2 · running 4.3.2 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 10347 ms |
| solana_rpc_validators | OK | 319 ms |
| coingecko | OK | 1631 ms |
| defillama_tvl | OK | 89 ms |
| defillama_dex | OK | 956 ms |
| defillama_fees | OK | 702 ms |
| defillama_stablecoins | OK | 991 ms |
| defillama_xstocks | FAILED | 652 ms |
| jito_kobe | OK | 527 ms |
| stakewiz | OK | 1059 ms |
| github | OK | 830 ms |
| solana_com_news | FAILED | 156 ms |
| sentiment | OK | 2181 ms |
| solana_status_page | OK | 21441 ms |
| solana_rpc_whales | OK | 1201 ms |
| solana_rpc_programs | OK | 2209 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*