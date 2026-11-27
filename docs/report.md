# Solbeat — State of the Solana Network

> Generated 2026-11-27T16:41:36Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1098 is 66% complete (~9h remaining), with the cluster processing ~2,291 TPS (2,291 non-vote). Measured slot time is 215ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $422.6K of Real Economic Value over the last 24h ($293/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $72.24 (+2.1% / 24h). Decentralization: Nakamoto coefficient 18, 654 active validators, 0.1% of stake delinquent. Alpenglow readiness: validators holding 100% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 1 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 474,620,914 |
| Block height | 452,633,565 |
| Epoch | 1098 (65.95% complete, ~8.8h left) |
| TPS (10 min avg) | 2,291 |
| Non-vote TPS | 2,291 |
| Slot time (measured) | 215.2 ms |
| Confirmation time (measured) | 0.22 s |
| Finality time (measured) | 0.22 s — **Alpenglow active** |
| Est. daily transactions | 143,129,670 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0023 |
| Node version | 4.4.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $72.24 (+2.1%/24h) |
| Market cap | $42.8B |
| **REV (24h)** | **$422.6K** (fees $332.6K + Jito tips $90.0K) |
| Chain TVL | $4.6B |
| Stablecoin supply | $12.6B |
| DEX volume (24h) | $870.6M (-42.4%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 592,238,200 SOL |
| Inflation | 3.54% |

Top DEXs by 24h volume: Orca DEX ($139.5M), Raydium AMM ($112.0M), pump.fun ($108.0M), PumpSwap ($86.7M), BisonFi ($81.4M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 654 / 34 |
| Delinquent stake | 0.06% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 25.0% |
| Avg / median commission | 13.2% / 5.0% |
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
| community | 74.2 |
| fear greed | 12 |
| momentum | 38.0 |
| news | 66 |

Crypto Fear & Greed: 12 (Extreme Fear) · CoinGecko votes bullish: 74.19% · headline tone (48h): +2

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 1,500 |
| Raydium AMM v4 | 1,116 |
| Orca Whirlpool | 1,500 |
| Pump.fun | 1,500 |
| Tensor | 0 |
| Magic Eden v2 | 29 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,300,003 |
| Binance (cold) | 66 |
| OKX (attributed) | 59,503 |
| Coinbase (hot) | 35,605 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 215ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 100.0% of stake.
- **Agave**: latest release v4.4.1 · running 4.4.0 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 11568 ms |
| solana_rpc_validators | OK | 253 ms |
| coingecko | OK | 1674 ms |
| defillama_tvl | OK | 236 ms |
| defillama_dex | OK | 859 ms |
| defillama_fees | OK | 1534 ms |
| defillama_stablecoins | OK | 624 ms |
| defillama_xstocks | FAILED | 574 ms |
| jito_kobe | OK | 100 ms |
| stakewiz | OK | 1021 ms |
| github | OK | 675 ms |
| solana_com_news | FAILED | 86 ms |
| sentiment | OK | 2112 ms |
| solana_status_page | OK | 268 ms |
| solana_rpc_whales | OK | 1026 ms |
| solana_rpc_programs | OK | 1703 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*