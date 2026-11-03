# Solbeat — State of the Solana Network

> Generated 2026-11-03T00:48:26Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1075 is 70% complete (~8h remaining), with the cluster processing ~1,703 TPS (1,703 non-vote). Measured slot time is 215ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $453.3K of Real Economic Value over the last 24h ($315/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $92.43 (-1.7% / 24h). Decentralization: Nakamoto coefficient 18, 665 active validators, 1.0% of stake delinquent. Alpenglow readiness: validators holding 100% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: all clear across every monitored metric.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 464,702,425 |
| Block height | 442,723,503 |
| Epoch | 1075 (70.01% complete, ~7.7h left) |
| TPS (10 min avg) | 1,703 |
| Non-vote TPS | 1,703 |
| Slot time (measured) | 215.3 ms |
| Confirmation time (measured) | 0.22 s |
| Finality time (measured) | 0.22 s — **Alpenglow active** |
| Est. daily transactions | 169,273,249 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0022 |
| Node version | 4.3.2 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $92.43 (-1.7%/24h) |
| Market cap | $54.5B |
| **REV (24h)** | **$453.3K** (fees $367.7K + Jito tips $85.6K) |
| Chain TVL | $5.3B |
| Stablecoin supply | $15.4B |
| DEX volume (24h) | $1.2B (31.8%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 590,206,306 SOL |
| Inflation | 3.57% |

Top DEXs by 24h volume: Orca DEX ($210.2M), Raydium AMM ($139.2M), PumpSwap ($122.9M), Manifest Trade ($110.0M), pump.fun ($104.8M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 665 / 28 |
| Delinquent stake | 1.01% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.7% |
| Avg / median commission | 12.8% / 5% |
| Alpenglow BLS-key readiness | 680 validators, 100.0% of stake |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L43ZWjwCHART3o…` | 17,034,354 | 3.92% | 7% |
| 2 | `he1iusunGwqrNtafDtLd…` | 16,710,199 | 3.85% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5…` | 13,037,180 | 3.0% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxb…` | 10,429,501 | 2.4% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxA…` | 9,580,109 | 2.21% | 5% |
| 6 | `51JBzSTU5rAM8gLAVQKg…` | 9,453,055 | 2.18% | 10% |
| 7 | `26pV97Ce83ZQ6Kz9XT4t…` | 9,226,805 | 2.13% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2Fp…` | 7,803,392 | 1.8% | 7% |
| 9 | `DumiCKHVqoCQKD8roLAp…` | 7,001,891 | 1.61% | 0% |
| 10 | `CvSb7wdQAFpHuSpTYTJn…` | 6,978,080 | 1.61% | 5% |

## Signals (anomaly detection)

All clear — no anomalies across monitored metrics.

## Solana Pulse — sentiment (experimental)

**49/100 — Neutral** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 72.2 |
| fear greed | 26 |
| momentum | 50.1 |
| news | 42 |

Crypto Fear & Greed: 26 (Fear) · CoinGecko votes bullish: 72.22% · headline tone (48h): -1

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 1,194 |
| Raydium AMM v4 | 665 |
| Orca Whirlpool | 1,194 |
| Pump.fun | 1,500 |
| Tensor | 0 |
| Magic Eden v2 | 87 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,890,003 |
| Binance (cold) | 4 |
| OKX (attributed) | 339,502 |
| Coinbase (hot) | 12,635 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 215ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 100.0% of stake.
- **Agave**: latest release v4.4.0 · running 4.3.2 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 10845 ms |
| solana_rpc_validators | OK | 332 ms |
| coingecko | OK | 1653 ms |
| defillama_tvl | OK | 149 ms |
| defillama_dex | OK | 975 ms |
| defillama_fees | OK | 763 ms |
| defillama_stablecoins | OK | 365 ms |
| defillama_xstocks | FAILED | 217 ms |
| jito_kobe | OK | 253 ms |
| stakewiz | OK | 1131 ms |
| github | OK | 771 ms |
| solana_com_news | FAILED | 94 ms |
| sentiment | OK | 2188 ms |
| solana_status_page | OK | 328 ms |
| solana_rpc_whales | OK | 1135 ms |
| solana_rpc_programs | OK | 1850 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*