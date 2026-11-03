# Solbeat — State of the Solana Network

> Generated 2026-11-03T08:54:41Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1076 is 2% complete (~25h remaining), with the cluster processing ~1,226 TPS (1,226 non-vote). Measured slot time is 213ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $567.8K of Real Economic Value over the last 24h ($394/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $91.65 (-3.2% / 24h). Decentralization: Nakamoto coefficient 18, 667 active validators, 0.4% of stake delinquent. Alpenglow readiness: validators holding 100% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: all clear across every monitored metric.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 464,839,021 |
| Block height | 442,859,905 |
| Epoch | 1076 (1.63% complete, ~25.2h left) |
| TPS (10 min avg) | 1,226 |
| Non-vote TPS | 1,226 |
| Slot time (measured) | 213.4 ms |
| Confirmation time (measured) | 0.21 s |
| Finality time (measured) | 0.21 s — **Alpenglow active** |
| Est. daily transactions | 123,461,537 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0039 |
| Node version | 4.3.2 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $91.65 (-3.2%/24h) |
| Market cap | $54.1B |
| **REV (24h)** | **$567.8K** (fees $482.2K + Jito tips $85.6K) |
| Chain TVL | $5.4B |
| Stablecoin supply | $15.3B |
| DEX volume (24h) | $1.4B (55.1%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 590,262,123 SOL |
| Inflation | 3.57% |

Top DEXs by 24h volume: PumpSwap ($261.1M), Orca DEX ($203.0M), Raydium AMM ($121.8M), pump.fun ($104.8M), Manifest Trade ($100.6M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 667 / 26 |
| Delinquent stake | 0.42% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.7% |
| Avg / median commission | 12.6% / 5% |
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
| community | 76.0 |
| fear greed | 26 |
| momentum | 50.5 |
| news | 58 |

Crypto Fear & Greed: 26 (Fear) · CoinGecko votes bullish: 76.0% · headline tone (48h): +1

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 972 |
| Raydium AMM v4 | 423 |
| Orca Whirlpool | 972 |
| Pump.fun | 1,500 |
| Tensor | 0 |
| Magic Eden v2 | 53 |
| Marinade | 2 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,890,003 |
| Binance (cold) | 4 |
| OKX (attributed) | 339,502 |
| Coinbase (hot) | 18,015 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 213ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 100.0% of stake.
- **Agave**: latest release v4.4.0 · running 4.3.2 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 8678 ms |
| solana_rpc_validators | OK | 114 ms |
| coingecko | OK | 1689 ms |
| defillama_tvl | OK | 45 ms |
| defillama_dex | OK | 401 ms |
| defillama_fees | OK | 654 ms |
| defillama_stablecoins | OK | 156 ms |
| defillama_xstocks | FAILED | 21 ms |
| jito_kobe | OK | 164 ms |
| stakewiz | OK | 649 ms |
| github | OK | 683 ms |
| solana_com_news | FAILED | 26 ms |
| sentiment | OK | 1990 ms |
| solana_status_page | OK | 92 ms |
| solana_rpc_whales | OK | 896 ms |
| solana_rpc_programs | OK | 1445 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*