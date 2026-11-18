# Solbeat — State of the Solana Network

> Generated 2026-11-18T15:58:37Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1090 is 26% complete (~19h remaining), with the cluster processing ~2,668 TPS (2,668 non-vote). Measured slot time is 217ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $555.9K of Real Economic Value over the last 24h ($386/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $73.57 (+2.4% / 24h). Decentralization: Nakamoto coefficient 17, 660 active validators, 0.0% of stake delinquent. Alpenglow readiness: validators holding 100% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 5 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 470,993,192 |
| Block height | 449,007,778 |
| Epoch | 1090 (26.2% complete, ~19.2h left) |
| TPS (10 min avg) | 2,668 |
| Non-vote TPS | 2,668 |
| Slot time (measured) | 216.9 ms |
| Confirmation time (measured) | 0.22 s |
| Finality time (measured) | 0.22 s — **Alpenglow active** |
| Est. daily transactions | 189,340,038 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0024 |
| Node version | 4.4.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $73.57 (+2.4%/24h) |
| Market cap | $43.5B |
| **REV (24h)** | **$555.9K** (fees $445.2K + Jito tips $110.7K) |
| Chain TVL | $4.7B |
| Stablecoin supply | $13.9B |
| DEX volume (24h) | $1.5B (2.0%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 591,794,833 SOL |
| Inflation | 3.55% |

Top DEXs by 24h volume: Orca DEX ($229.5M), Meteora DLMM ($172.7M), PumpSwap ($155.3M), BisonFi ($149.6M), Raydium AMM ($146.2M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 660 / 25 |
| Delinquent stake | 0.02% |
| Nakamoto coefficient | 17 |
| Top-10 stake share | 25.0% |
| Avg / median commission | 12.6% / 5.0% |
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

- **[WARNING]** SOL price contraction (z=-2.1 vs its recent baseline)
- **[WARNING]** Solana TVL contraction (z=-2.3 vs its recent baseline)
- **[WARNING]** Stablecoin supply contraction (z=-2.6 vs its recent baseline)
- **[WARNING · market_move]** Market-wide move: SOL price anomaly accompanied by liquidity/volume shifts — an ecosystem-level repricing rather than an isolated metric.
- **[WARNING · liquidity_rotation]** Stablecoin supply and TVL moving together — capital rotating in or out of the chain.

## Solana Pulse — sentiment (experimental)

**42/100 — Neutral** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 69.4 |
| fear greed | 11 |
| momentum | 33.9 |
| news | 58 |

Crypto Fear & Greed: 11 (Extreme Fear) · CoinGecko votes bullish: 69.39% · headline tone (48h): +1

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 1,500 |
| Raydium AMM v4 | 1,356 |
| Orca Whirlpool | 1,500 |
| Pump.fun | 1,500 |
| Tensor | 0 |
| Magic Eden v2 | 31 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,300,003 |
| Binance (cold) | 66 |
| OKX (attributed) | 8,207 |
| Coinbase (hot) | 19,194 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 217ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 100.0% of stake.
- **Agave**: latest release v4.4.1 · running 4.4.0 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 11371 ms |
| solana_rpc_validators | OK | 485 ms |
| coingecko | OK | 1729 ms |
| defillama_tvl | OK | 127 ms |
| defillama_dex | OK | 920 ms |
| defillama_fees | OK | 733 ms |
| defillama_stablecoins | OK | 907 ms |
| defillama_xstocks | FAILED | 65 ms |
| jito_kobe | OK | 359 ms |
| stakewiz | OK | 1126 ms |
| github | OK | 812 ms |
| solana_com_news | FAILED | 97 ms |
| sentiment | OK | 2336 ms |
| solana_status_page | OK | 306 ms |
| solana_rpc_whales | OK | 1124 ms |
| solana_rpc_programs | OK | 3084 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*