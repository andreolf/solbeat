# Solbeat — State of the Solana Network

> Generated 2026-11-03T20:45:34Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1076 is 48% complete (~14h remaining), with the cluster processing ~2,190 TPS (2,190 non-vote). Measured slot time is 215ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $594.1K of Real Economic Value over the last 24h ($413/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $93.40 (+2.3% / 24h). Decentralization: Nakamoto coefficient 18, 666 active validators, 0.4% of stake delinquent. Alpenglow readiness: validators holding 100% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: all clear across every monitored metric.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 465,037,909 |
| Block height | 443,058,555 |
| Epoch | 1076 (47.66% complete, ~13.5h left) |
| TPS (10 min avg) | 2,190 |
| Non-vote TPS | 2,190 |
| Slot time (measured) | 214.9 ms |
| Confirmation time (measured) | 0.21 s |
| Finality time (measured) | 0.21 s — **Alpenglow active** |
| Est. daily transactions | 204,602,681 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0024 |
| Node version | 4.4.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $93.40 (+2.3%/24h) |
| Market cap | $55.2B |
| **REV (24h)** | **$594.1K** (fees $482.2K + Jito tips $111.8K) |
| Chain TVL | $5.4B |
| Stablecoin supply | $15.3B |
| DEX volume (24h) | $1.9B (104.6%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 590,265,881 SOL |
| Inflation | 3.57% |

Top DEXs by 24h volume: PumpSwap ($261.1M), BisonFi ($250.5M), Orca DEX ($209.0M), Tessera V ($149.8M), Raydium AMM ($126.2M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 666 / 27 |
| Delinquent stake | 0.42% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.7% |
| Avg / median commission | 12.6% / 5.0% |
| Alpenglow BLS-key readiness | 680 validators, 100.0% of stake |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L43ZWjwCHART3o…` | 17,030,641 | 3.92% | 7% |
| 2 | `he1iusunGwqrNtafDtLd…` | 16,704,340 | 3.84% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5…` | 13,043,664 | 3.0% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxb…` | 10,431,126 | 2.4% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxA…` | 9,561,007 | 2.2% | 5% |
| 6 | `51JBzSTU5rAM8gLAVQKg…` | 9,435,905 | 2.17% | 10% |
| 7 | `26pV97Ce83ZQ6Kz9XT4t…` | 9,232,746 | 2.12% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2Fp…` | 7,814,810 | 1.8% | 7% |
| 9 | `DumiCKHVqoCQKD8roLAp…` | 7,008,986 | 1.61% | 0% |
| 10 | `CvSb7wdQAFpHuSpTYTJn…` | 6,979,031 | 1.61% | 5% |

## Signals (anomaly detection)

All clear — no anomalies across monitored metrics.

## Solana Pulse — sentiment (experimental)

**53/100 — Neutral** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 71.9 |
| fear greed | 26 |
| momentum | 53.4 |
| news | 58 |

Crypto Fear & Greed: 26 (Fear) · CoinGecko votes bullish: 71.88% · headline tone (48h): +1

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 958 |
| Raydium AMM v4 | 958 |
| Orca Whirlpool | 1,500 |
| Pump.fun | 1,500 |
| Tensor | 1 |
| Magic Eden v2 | 52 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,300,003 |
| Binance (cold) | 4 |
| OKX (attributed) | 339,403 |
| Coinbase (hot) | 17,094 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 215ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 100.0% of stake.
- **Agave**: latest release v4.4.0 · running 4.4.0 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 8930 ms |
| solana_rpc_validators | OK | 241 ms |
| coingecko | OK | 1645 ms |
| defillama_tvl | OK | 453 ms |
| defillama_dex | OK | 1154 ms |
| defillama_fees | OK | 2022 ms |
| defillama_stablecoins | OK | 1759 ms |
| defillama_xstocks | FAILED | 817 ms |
| jito_kobe | OK | 342 ms |
| stakewiz | OK | 1411 ms |
| github | OK | 1025 ms |
| solana_com_news | FAILED | 93 ms |
| sentiment | OK | 2580 ms |
| solana_status_page | OK | 312 ms |
| solana_rpc_whales | OK | 1201 ms |
| solana_rpc_programs | OK | 1960 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*