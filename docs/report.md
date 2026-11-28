# Solbeat — State of the Solana Network

> Generated 2026-11-28T00:41:25Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1098 is 97% complete (~1h remaining), with the cluster processing ~1,286 TPS (1,286 non-vote). Measured slot time is 214ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $422.3K of Real Economic Value over the last 24h ($293/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $71.69 (+0.7% / 24h). Decentralization: Nakamoto coefficient 18, 653 active validators, 3.0% of stake delinquent. Alpenglow readiness: validators holding 100% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 1 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 474,754,945 |
| Block height | 452,767,543 |
| Epoch | 1098 (96.98% complete, ~0.8h left) |
| TPS (10 min avg) | 1,286 |
| Non-vote TPS | 1,286 |
| Slot time (measured) | 214.4 ms |
| Confirmation time (measured) | 0.21 s |
| Finality time (measured) | 0.21 s — **Alpenglow active** |
| Est. daily transactions | 157,709,847 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0021 |
| Node version | 4.4.2 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $71.69 (+0.7%/24h) |
| Market cap | $42.5B |
| **REV (24h)** | **$422.3K** (fees $332.6K + Jito tips $89.6K) |
| Chain TVL | $4.6B |
| Stablecoin supply | $12.6B |
| DEX volume (24h) | $885.2M (1.7%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 592,375,200 SOL |
| Inflation | 3.54% |

Top DEXs by 24h volume: Orca DEX ($139.5M), Raydium AMM ($112.0M), pump.fun ($108.0M), PumpSwap ($86.7M), BisonFi ($81.4M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 653 / 35 |
| Delinquent stake | 2.99% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 25.0% |
| Avg / median commission | 13.2% / 5% |
| Alpenglow BLS-key readiness | 669 validators, 100.0% of stake |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `he1iusunGwqrNtafDtLd…` | 16,815,245 | 3.96% | 0% |
| 2 | `CcaHc2L43ZWjwCHART3o…` | 15,826,052 | 3.73% | 7% |
| 3 | `3N7s9zXMZ4QqvHQR15t5…` | 12,437,388 | 2.93% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxb…` | 10,238,108 | 2.41% | 0% |
| 5 | `51JBzSTU5rAM8gLAVQKg…` | 9,920,637 | 2.34% | 10% |
| 6 | `CatzoSMUkTRidT5DwBxA…` | 9,617,109 | 2.27% | 5% |
| 7 | `26pV97Ce83ZQ6Kz9XT4t…` | 9,296,651 | 2.19% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2Fp…` | 8,037,877 | 1.89% | 7% |
| 9 | `DumiCKHVqoCQKD8roLAp…` | 6,972,141 | 1.64% | 0% |
| 10 | `CvSb7wdQAFpHuSpTYTJn…` | 6,741,351 | 1.59% | 5% |

## Signals (anomaly detection)

- **[SERIOUS]** Stablecoin supply contraction (z=-3.4 vs its recent baseline)

## Solana Pulse — sentiment (experimental)

**47/100 — Neutral** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 65.5 |
| fear greed | 10 |
| momentum | 50.8 |
| news | 66 |

Crypto Fear & Greed: 10 (Extreme Fear) · CoinGecko votes bullish: 65.52% · headline tone (48h): +2

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 665 |
| Raydium AMM v4 | 461 |
| Orca Whirlpool | 1,195 |
| Pump.fun | 1,500 |
| Tensor | 0 |
| Magic Eden v2 | 38 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,300,003 |
| Binance (cold) | 66 |
| OKX (attributed) | 59,503 |
| Coinbase (hot) | 22,831 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 214ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 100.0% of stake.
- **Agave**: latest release v4.4.2 · running 4.4.2 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 9827 ms |
| solana_rpc_validators | OK | 393 ms |
| coingecko | OK | 1869 ms |
| defillama_tvl | OK | 212 ms |
| defillama_dex | OK | 51 ms |
| defillama_fees | OK | 1045 ms |
| defillama_stablecoins | OK | 949 ms |
| defillama_xstocks | FAILED | 840 ms |
| jito_kobe | OK | 302 ms |
| stakewiz | OK | 1375 ms |
| github | OK | 647 ms |
| solana_com_news | FAILED | 80 ms |
| sentiment | OK | 2190 ms |
| solana_status_page | OK | 297 ms |
| solana_rpc_whales | OK | 1140 ms |
| solana_rpc_programs | OK | 6759 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*