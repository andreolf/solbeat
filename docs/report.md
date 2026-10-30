# Solbeat — State of the Solana Network

> Generated 2026-10-30T01:50:08Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1072 is 0% complete (~25h remaining), with the cluster processing ~1,859 TPS (1,859 non-vote). Measured slot time is 212ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $687.4K of Real Economic Value over the last 24h ($477/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $93.71 (-6.3% / 24h). Decentralization: Nakamoto coefficient 18, 666 active validators, 0.8% of stake delinquent. Alpenglow readiness: validators holding 100% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: all clear across every monitored metric.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 463,105,795 |
| Block height | 441,128,757 |
| Epoch | 1072 (0.42% complete, ~25.3h left) |
| TPS (10 min avg) | 1,859 |
| Non-vote TPS | 1,859 |
| Slot time (measured) | 211.8 ms |
| Confirmation time (measured) | 0.21 s |
| Finality time (measured) | 0.21 s — **Alpenglow active** |
| Est. daily transactions | 211,523,765 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0027 |
| Node version | 4.3.2 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $93.71 (-6.3%/24h) |
| Market cap | $55.3B |
| **REV (24h)** | **$687.4K** (fees $564.5K + Jito tips $122.9K) |
| Chain TVL | $5.4B |
| Stablecoin supply | $15.4B |
| DEX volume (24h) | $1.9B (11.0%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 590,040,180 SOL |
| Inflation | 3.58% |

Top DEXs by 24h volume: Orca DEX ($382.6M), Raydium AMM ($217.1M), BisonFi ($205.5M), Manifest Trade ($181.1M), Tessera V ($148.2M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 666 / 25 |
| Delinquent stake | 0.77% |
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

All clear — no anomalies across monitored metrics.

## Solana Pulse — sentiment (experimental)

**47/100 — Neutral** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 75.0 |
| fear greed | 30 |
| momentum | 38.2 |
| news | 34 |

Crypto Fear & Greed: 30 (Fear) · CoinGecko votes bullish: 75.0% · headline tone (48h): -2

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 1,480 |
| Raydium AMM v4 | 498 |
| Orca Whirlpool | 1,480 |
| Pump.fun | 1,500 |
| Tensor | 0 |
| Magic Eden v2 | 83 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 11,890,003 |
| Binance (cold) | 4 |
| OKX (attributed) | 332,364 |
| Coinbase (hot) | 11,589 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 212ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 100.0% of stake.
- **Agave**: latest release v4.4.0 · running 4.3.2 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 11498 ms |
| solana_rpc_validators | OK | 128 ms |
| coingecko | OK | 1859 ms |
| defillama_tvl | OK | 365 ms |
| defillama_dex | OK | 1095 ms |
| defillama_fees | OK | 1416 ms |
| defillama_stablecoins | OK | 383 ms |
| defillama_xstocks | FAILED | 753 ms |
| jito_kobe | OK | 311 ms |
| stakewiz | OK | 1256 ms |
| github | OK | 974 ms |
| solana_com_news | FAILED | 97 ms |
| sentiment | OK | 2271 ms |
| solana_status_page | OK | 418 ms |
| solana_rpc_whales | OK | 1182 ms |
| solana_rpc_programs | OK | 2128 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*