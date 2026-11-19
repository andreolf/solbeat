# Solbeat — State of the Solana Network

> Generated 2026-11-19T05:41:31Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1090 is 79% complete (~5h remaining), with the cluster processing ~1,471 TPS (1,471 non-vote). Measured slot time is 214ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $673.8K of Real Economic Value over the last 24h ($468/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $74.50 (-0.9% / 24h). Decentralization: Nakamoto coefficient 17, 659 active validators, 0.0% of stake delinquent. Alpenglow readiness: validators holding 100% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 3 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 471,222,411 |
| Block height | 449,236,742 |
| Epoch | 1090 (79.26% complete, ~5.3h left) |
| TPS (10 min avg) | 1,471 |
| Non-vote TPS | 1,471 |
| Slot time (measured) | 214.5 ms |
| Confirmation time (measured) | 0.21 s |
| Finality time (measured) | 0.21 s — **Alpenglow active** |
| Est. daily transactions | 148,452,329 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0038 |
| Node version | 4.4.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $74.50 (-0.9%/24h) |
| Market cap | $44.1B |
| **REV (24h)** | **$673.8K** (fees $560.5K + Jito tips $113.3K) |
| Chain TVL | $4.7B |
| Stablecoin supply | $13.0B |
| DEX volume (24h) | $1.7B (12.7%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 591,796,279 SOL |
| Inflation | 3.55% |

Top DEXs by 24h volume: PumpSwap ($330.7M), Orca DEX ($259.8M), Meteora DLMM ($172.7M), BisonFi ($149.6M), Raydium AMM ($145.1M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 659 / 26 |
| Delinquent stake | 0.03% |
| Nakamoto coefficient | 17 |
| Top-10 stake share | 25.0% |
| Avg / median commission | 12.8% / 5% |
| Alpenglow BLS-key readiness | 670 validators, 100.0% of stake |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `he1iusunGwqrNtafDtLd…` | 17,030,759 | 3.99% | 0% |
| 2 | `CcaHc2L43ZWjwCHART3o…` | 16,476,078 | 3.86% | 7% |
| 3 | `3N7s9zXMZ4QqvHQR15t5…` | 12,423,470 | 2.91% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxb…` | 10,297,722 | 2.41% | 0% |
| 5 | `51JBzSTU5rAM8gLAVQKg…` | 9,815,430 | 2.3% | 10% |
| 6 | `CatzoSMUkTRidT5DwBxA…` | 9,574,562 | 2.24% | 5% |
| 7 | `26pV97Ce83ZQ6Kz9XT4t…` | 9,222,715 | 2.16% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2Fp…` | 7,973,220 | 1.87% | 7% |
| 9 | `DumiCKHVqoCQKD8roLAp…` | 6,996,720 | 1.64% | 0% |
| 10 | `CvSb7wdQAFpHuSpTYTJn…` | 6,771,472 | 1.59% | 5% |

## Signals (anomaly detection)

- **[WARNING]** Solana TVL contraction (z=-2.3 vs its recent baseline)
- **[SERIOUS]** Stablecoin supply contraction (z=-4.6 vs its recent baseline)
- **[WARNING · liquidity_rotation]** Stablecoin supply and TVL moving together — capital rotating in or out of the chain.

## Solana Pulse — sentiment (experimental)

**41/100 — Neutral** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 65.2 |
| fear greed | 10 |
| momentum | 41.5 |
| news | 42 |

Crypto Fear & Greed: 10 (Extreme Fear) · CoinGecko votes bullish: 65.22% · headline tone (48h): -1

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 986 |
| Raydium AMM v4 | 986 |
| Orca Whirlpool | 986 |
| Pump.fun | 1,500 |
| Tensor | 0 |
| Magic Eden v2 | 59 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,300,003 |
| Binance (cold) | 66 |
| OKX (attributed) | 133,487 |
| Coinbase (hot) | 94,302 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 214ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 100.0% of stake.
- **Agave**: latest release v4.4.1 · running 4.4.0 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 10188 ms |
| solana_rpc_validators | OK | 250 ms |
| coingecko | OK | 1603 ms |
| defillama_tvl | OK | 42 ms |
| defillama_dex | OK | 32 ms |
| defillama_fees | OK | 661 ms |
| defillama_stablecoins | OK | 158 ms |
| defillama_xstocks | FAILED | 142 ms |
| jito_kobe | OK | 78 ms |
| stakewiz | OK | 671 ms |
| github | OK | 573 ms |
| solana_com_news | FAILED | 55 ms |
| sentiment | OK | 2023 ms |
| solana_status_page | OK | 318 ms |
| solana_rpc_whales | OK | 1083 ms |
| solana_rpc_programs | OK | 1579 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*