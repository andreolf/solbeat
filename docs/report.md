# Solbeat — State of the Solana Network

> Generated 2026-11-25T16:37:46Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1096 is 80% complete (~5h remaining), with the cluster processing ~3,017 TPS (3,017 non-vote). Measured slot time is 214ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $471.8K of Real Economic Value over the last 24h ($328/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $67.66 (-1.4% / 24h). Decentralization: Nakamoto coefficient 18, 659 active validators, 0.0% of stake delinquent. Alpenglow readiness: validators holding 100% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 3 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 473,816,012 |
| Block height | 451,829,034 |
| Epoch | 1096 (79.63% complete, ~5.2h left) |
| TPS (10 min avg) | 3,017 |
| Non-vote TPS | 3,017 |
| Slot time (measured) | 213.9 ms |
| Confirmation time (measured) | 0.21 s |
| Finality time (measured) | 0.21 s — **Alpenglow active** |
| Est. daily transactions | 178,716,705 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0020 |
| Node version | 4.4.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $67.66 (-1.4%/24h) |
| Market cap | $40.1B |
| **REV (24h)** | **$471.8K** (fees $366.0K + Jito tips $105.9K) |
| Chain TVL | $4.4B |
| Stablecoin supply | $13.4B |
| DEX volume (24h) | $1.5B (-19.3%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 592,128,149 SOL |
| Inflation | 3.54% |

Top DEXs by 24h volume: BisonFi ($190.5M), Orca DEX ($184.7M), Manifest Trade ($160.9M), Raydium AMM ($152.4M), Scorch ($134.1M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 659 / 28 |
| Delinquent stake | 0.04% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 25.0% |
| Avg / median commission | 13.1% / 5% |
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

- **[WARNING]** Solana TVL contraction (z=-2.4 vs its recent baseline)
- **[WARNING]** Stablecoin supply contraction (z=-2.4 vs its recent baseline)
- **[WARNING · liquidity_rotation]** Stablecoin supply and TVL moving together — capital rotating in or out of the chain.

## Solana Pulse — sentiment (experimental)

**38/100 — Bearish** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 59.1 |
| fear greed | 13 |
| momentum | 24.3 |
| news | 66 |

Crypto Fear & Greed: 13 (Extreme Fear) · CoinGecko votes bullish: 59.09% · headline tone (48h): +2

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 1,500 |
| Raydium AMM v4 | 1,500 |
| Orca Whirlpool | 1,500 |
| Pump.fun | 1,500 |
| Tensor | 9 |
| Magic Eden v2 | 34 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,300,003 |
| Binance (cold) | 66 |
| OKX (attributed) | 59,504 |
| Coinbase (hot) | 22,127 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 214ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 100.0% of stake.
- **Agave**: latest release v4.4.1 · running 4.4.0 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 18082 ms |
| solana_rpc_validators | OK | 290 ms |
| coingecko | OK | 1681 ms |
| defillama_tvl | OK | 346 ms |
| defillama_dex | OK | 1064 ms |
| defillama_fees | OK | 1620 ms |
| defillama_stablecoins | OK | 681 ms |
| defillama_xstocks | FAILED | 639 ms |
| jito_kobe | OK | 496 ms |
| stakewiz | OK | 896 ms |
| github | OK | 919 ms |
| solana_com_news | FAILED | 76 ms |
| sentiment | OK | 2300 ms |
| solana_status_page | OK | 252 ms |
| solana_rpc_whales | OK | 1107 ms |
| solana_rpc_programs | OK | 2033 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*