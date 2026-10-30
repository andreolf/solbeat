# Solbeat — State of the Solana Network

> Generated 2026-10-30T00:46:57Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1071 is 96% complete (~1h remaining), with the cluster processing ~2,343 TPS (2,343 non-vote). Measured slot time is 213ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $649.3K of Real Economic Value over the last 24h ($451/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $93.73 (-8.1% / 24h). Decentralization: Nakamoto coefficient 18, 664 active validators, 0.8% of stake delinquent. Alpenglow readiness: validators holding 100% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: all clear across every monitored metric.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 463,088,021 |
| Block height | 441,111,173 |
| Epoch | 1071 (96.3% complete, ~0.9h left) |
| TPS (10 min avg) | 2,343 |
| Non-vote TPS | 2,343 |
| Slot time (measured) | 213.1 ms |
| Confirmation time (measured) | 0.21 s |
| Finality time (measured) | 0.21 s — **Alpenglow active** |
| Est. daily transactions | 239,575,749 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0022 |
| Node version | 4.3.2 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $93.73 (-8.1%/24h) |
| Market cap | $55.2B |
| **REV (24h)** | **$649.3K** (fees $527.1K + Jito tips $122.2K) |
| Chain TVL | $5.5B |
| Stablecoin supply | $15.6B |
| DEX volume (24h) | $1.9B (7.4%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 589,984,457 SOL |
| Inflation | 3.58% |

Top DEXs by 24h volume: Orca DEX ($357.0M), Raydium AMM ($209.0M), BisonFi ($205.5M), Manifest Trade ($159.0M), Tessera V ($148.2M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 664 / 25 |
| Delinquent stake | 0.83% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.5% |
| Avg / median commission | 13.1% / 5.0% |
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

**48/100 — Neutral** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 75.9 |
| fear greed | 30 |
| momentum | 36.5 |
| news | 42 |

Crypto Fear & Greed: 30 (Fear) · CoinGecko votes bullish: 75.86% · headline tone (48h): -1

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 1,500 |
| Raydium AMM v4 | 815 |
| Orca Whirlpool | 1,500 |
| Pump.fun | 1,500 |
| Tensor | 0 |
| Magic Eden v2 | 63 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 11,890,003 |
| Binance (cold) | 4 |
| OKX (attributed) | 332,364 |
| Coinbase (hot) | 12,521 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 213ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 100.0% of stake.
- **Agave**: latest release v4.4.0 · running 4.3.2 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 11026 ms |
| solana_rpc_validators | OK | 381 ms |
| coingecko | OK | 1713 ms |
| defillama_tvl | OK | 185 ms |
| defillama_dex | OK | 954 ms |
| defillama_fees | OK | 1686 ms |
| defillama_stablecoins | OK | 283 ms |
| defillama_xstocks | FAILED | 575 ms |
| jito_kobe | OK | 312 ms |
| stakewiz | OK | 1140 ms |
| github | OK | 816 ms |
| solana_com_news | FAILED | 94 ms |
| sentiment | OK | 2303 ms |
| solana_status_page | OK | 494 ms |
| solana_rpc_whales | OK | 1227 ms |
| solana_rpc_programs | OK | 1985 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*