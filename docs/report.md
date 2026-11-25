# Solbeat — State of the Solana Network

> Generated 2026-11-25T21:12:43Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1096 is 97% complete (~1h remaining), with the cluster processing ~2,193 TPS (2,193 non-vote). Measured slot time is 214ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $475.9K of Real Economic Value over the last 24h ($330/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $70.41 (+1.7% / 24h). Decentralization: Nakamoto coefficient 18, 658 active validators, 0.0% of stake delinquent. Alpenglow readiness: validators holding 100% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 3 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 473,892,683 |
| Block height | 451,905,651 |
| Epoch | 1096 (97.38% complete, ~0.7h left) |
| TPS (10 min avg) | 2,193 |
| Non-vote TPS | 2,193 |
| Slot time (measured) | 214.4 ms |
| Confirmation time (measured) | 0.21 s |
| Finality time (measured) | 0.21 s — **Alpenglow active** |
| Est. daily transactions | 224,538,715 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0016 |
| Node version | 4.4.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $70.41 (+1.7%/24h) |
| Market cap | $41.7B |
| **REV (24h)** | **$475.9K** (fees $366.0K + Jito tips $109.9K) |
| Chain TVL | $4.5B |
| Stablecoin supply | $13.4B |
| DEX volume (24h) | $1.5B (-19.3%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 592,128,033 SOL |
| Inflation | 3.54% |

Top DEXs by 24h volume: BisonFi ($190.5M), Orca DEX ($183.5M), Raydium AMM ($178.0M), Manifest Trade ($150.8M), Scorch ($134.1M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 658 / 29 |
| Delinquent stake | 0.04% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 25.0% |
| Avg / median commission | 13.1% / 5.0% |
| Alpenglow BLS-key readiness | 670 validators, 100.0% of stake |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `he1iusunGwqrNtafDtLd…` | 17,003,542 | 4.0% | 0% |
| 2 | `CcaHc2L43ZWjwCHART3o…` | 15,962,658 | 3.76% | 7% |
| 3 | `3N7s9zXMZ4QqvHQR15t5…` | 12,418,812 | 2.92% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxb…` | 10,242,949 | 2.41% | 0% |
| 5 | `51JBzSTU5rAM8gLAVQKg…` | 9,885,209 | 2.33% | 10% |
| 6 | `CatzoSMUkTRidT5DwBxA…` | 9,615,269 | 2.26% | 5% |
| 7 | `26pV97Ce83ZQ6Kz9XT4t…` | 9,283,847 | 2.19% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2Fp…` | 8,016,085 | 1.89% | 7% |
| 9 | `DumiCKHVqoCQKD8roLAp…` | 6,968,432 | 1.64% | 0% |
| 10 | `CvSb7wdQAFpHuSpTYTJn…` | 6,779,378 | 1.6% | 5% |

## Signals (anomaly detection)

- **[WARNING]** Solana TVL contraction (z=-2.1 vs its recent baseline)
- **[WARNING]** Stablecoin supply contraction (z=-2.4 vs its recent baseline)
- **[WARNING · liquidity_rotation]** Stablecoin supply and TVL moving together — capital rotating in or out of the chain.

## Solana Pulse — sentiment (experimental)

**43/100 — Neutral** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 65.0 |
| fear greed | 13 |
| momentum | 30.9 |
| news | 74 |

Crypto Fear & Greed: 13 (Extreme Fear) · CoinGecko votes bullish: 65.0% · headline tone (48h): +3

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 891 |
| Raydium AMM v4 | 891 |
| Orca Whirlpool | 891 |
| Pump.fun | 1,500 |
| Tensor | 0 |
| Magic Eden v2 | 28 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,300,003 |
| Binance (cold) | 66 |
| OKX (attributed) | 59,504 |
| Coinbase (hot) | 18,184 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 214ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 100.0% of stake.
- **Agave**: latest release v4.4.1 · running 4.4.0 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 9699 ms |
| solana_rpc_validators | OK | 362 ms |
| coingecko | OK | 1743 ms |
| defillama_tvl | OK | 128 ms |
| defillama_dex | OK | 1034 ms |
| defillama_fees | OK | 1772 ms |
| defillama_stablecoins | OK | 134 ms |
| defillama_xstocks | FAILED | 61 ms |
| jito_kobe | OK | 167 ms |
| stakewiz | OK | 1233 ms |
| github | OK | 946 ms |
| solana_com_news | FAILED | 138 ms |
| sentiment | OK | 2250 ms |
| solana_status_page | OK | 393 ms |
| solana_rpc_whales | OK | 1520 ms |
| solana_rpc_programs | OK | 2192 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*