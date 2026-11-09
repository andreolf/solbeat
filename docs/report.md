# Solbeat — State of the Solana Network

> Generated 2026-11-09T08:21:37Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1081 is 59% complete (~10h remaining), with the cluster processing ~1,224 TPS (1,224 non-vote). Measured slot time is 215ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $508.9K of Real Economic Value over the last 24h ($353/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $86.05 (-3.3% / 24h). Decentralization: Nakamoto coefficient 18, 663 active validators, 0.1% of stake delinquent. Alpenglow readiness: validators holding 100% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 2 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 467,248,540 |
| Block height | 445,266,537 |
| Epoch | 1081 (59.38% complete, ~10.5h left) |
| TPS (10 min avg) | 1,224 |
| Non-vote TPS | 1,224 |
| Slot time (measured) | 215.0 ms |
| Confirmation time (measured) | 0.21 s |
| Finality time (measured) | 0.21 s — **Alpenglow active** |
| Est. daily transactions | 119,429,513 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0034 |
| Node version | 4.4.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $86.05 (-3.3%/24h) |
| Market cap | $50.9B |
| **REV (24h)** | **$508.9K** (fees $408.0K + Jito tips $100.9K) |
| Chain TVL | $5.1B |
| Stablecoin supply | $15.0B |
| DEX volume (24h) | $997.1M (8.7%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 591,093,668 SOL |
| Inflation | 3.57% |

Top DEXs by 24h volume: Orca DEX ($189.9M), PumpSwap ($165.3M), Raydium AMM ($125.5M), pump.fun ($87.5M), BisonFi ($80.2M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 663 / 34 |
| Delinquent stake | 0.13% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.6% |
| Avg / median commission | 13.0% / 5% |
| Alpenglow BLS-key readiness | 684 validators, 100.0% of stake |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L43ZWjwCHART3o…` | 17,050,553 | 3.93% | 7% |
| 2 | `he1iusunGwqrNtafDtLd…` | 16,720,131 | 3.85% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5…` | 13,021,912 | 3.0% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxb…` | 10,279,070 | 2.37% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxA…` | 9,553,388 | 2.2% | 5% |
| 6 | `51JBzSTU5rAM8gLAVQKg…` | 9,550,278 | 2.2% | 10% |
| 7 | `26pV97Ce83ZQ6Kz9XT4t…` | 9,222,876 | 2.13% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2Fp…` | 7,775,137 | 1.79% | 7% |
| 9 | `DumiCKHVqoCQKD8roLAp…` | 6,980,319 | 1.61% | 0% |
| 10 | `CvSb7wdQAFpHuSpTYTJn…` | 6,711,284 | 1.55% | 5% |

## Signals (anomaly detection)

- **[WARNING]** SOL price contraction (z=-2.1 vs its recent baseline)
- **[WARNING]** Stablecoin supply contraction (z=-2.4 vs its recent baseline)

## Solana Pulse — sentiment (experimental)

**49/100 — Neutral** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 68.8 |
| fear greed | 29 |
| momentum | 41.0 |
| news | 58 |

Crypto Fear & Greed: 29 (Fear) · CoinGecko votes bullish: 68.75% · headline tone (48h): +1

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 753 |
| Raydium AMM v4 | 501 |
| Orca Whirlpool | 753 |
| Pump.fun | 1,500 |
| Tensor | 0 |
| Magic Eden v2 | 72 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,300,003 |
| Binance (cold) | 66 |
| OKX (attributed) | 97,596 |
| Coinbase (hot) | 24,370 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 215ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 100.0% of stake.
- **Agave**: latest release v4.4.1 · running 4.4.0 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 9025 ms |
| solana_rpc_validators | OK | 131 ms |
| coingecko | OK | 1785 ms |
| defillama_tvl | OK | 88 ms |
| defillama_dex | OK | 1221 ms |
| defillama_fees | OK | 127 ms |
| defillama_stablecoins | OK | 135 ms |
| defillama_xstocks | FAILED | 764 ms |
| jito_kobe | OK | 320 ms |
| stakewiz | OK | 1367 ms |
| github | OK | 985 ms |
| solana_com_news | FAILED | 152 ms |
| sentiment | OK | 2290 ms |
| solana_status_page | OK | 309 ms |
| solana_rpc_whales | OK | 977 ms |
| solana_rpc_programs | OK | 1657 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*