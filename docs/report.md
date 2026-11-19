# Solbeat — State of the Solana Network

> Generated 2026-11-19T02:54:08Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1090 is 68% complete (~8h remaining), with the cluster processing ~1,840 TPS (1,840 non-vote). Measured slot time is 215ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $671.5K of Real Economic Value over the last 24h ($466/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $73.10 (-1.6% / 24h). Decentralization: Nakamoto coefficient 17, 660 active validators, 0.0% of stake delinquent. Alpenglow readiness: validators holding 100% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 3 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 471,175,610 |
| Block height | 449,189,957 |
| Epoch | 1090 (68.43% complete, ~8.1h left) |
| TPS (10 min avg) | 1,840 |
| Non-vote TPS | 1,840 |
| Slot time (measured) | 214.8 ms |
| Confirmation time (measured) | 0.21 s |
| Finality time (measured) | 0.21 s — **Alpenglow active** |
| Est. daily transactions | 169,780,892 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0033 |
| Node version | 4.4.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $73.10 (-1.6%/24h) |
| Market cap | $43.3B |
| **REV (24h)** | **$671.5K** (fees $560.5K + Jito tips $111.0K) |
| Chain TVL | $4.7B |
| Stablecoin supply | $13.0B |
| DEX volume (24h) | $1.7B (12.7%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 591,796,321 SOL |
| Inflation | 3.55% |

Top DEXs by 24h volume: PumpSwap ($330.7M), Orca DEX ($252.8M), Meteora DLMM ($172.7M), Raydium AMM ($154.1M), BisonFi ($149.6M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 660 / 25 |
| Delinquent stake | 0.02% |
| Nakamoto coefficient | 17 |
| Top-10 stake share | 25.0% |
| Avg / median commission | 12.8% / 5.0% |
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

**39/100 — Bearish** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 62.2 |
| fear greed | 10 |
| momentum | 39.4 |
| news | 42 |

Crypto Fear & Greed: 10 (Extreme Fear) · CoinGecko votes bullish: 62.22% · headline tone (48h): -1

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 1,250 |
| Raydium AMM v4 | 682 |
| Orca Whirlpool | 1,500 |
| Pump.fun | 1,500 |
| Tensor | 0 |
| Magic Eden v2 | 25 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,300,003 |
| Binance (cold) | 66 |
| OKX (attributed) | 133,487 |
| Coinbase (hot) | 144,058 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 215ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 100.0% of stake.
- **Agave**: latest release v4.4.1 · running 4.4.0 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 8881 ms |
| solana_rpc_validators | OK | 247 ms |
| coingecko | OK | 1729 ms |
| defillama_tvl | OK | 42 ms |
| defillama_dex | OK | 584 ms |
| defillama_fees | OK | 838 ms |
| defillama_stablecoins | OK | 255 ms |
| defillama_xstocks | FAILED | 27 ms |
| jito_kobe | OK | 136 ms |
| stakewiz | OK | 1427 ms |
| github | OK | 767 ms |
| solana_com_news | FAILED | 65 ms |
| sentiment | OK | 2289 ms |
| solana_status_page | OK | 143 ms |
| solana_rpc_whales | OK | 1003 ms |
| solana_rpc_programs | OK | 1844 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*