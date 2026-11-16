# Solbeat — State of the Solana Network

> Generated 2026-11-16T17:15:04Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1088 is 45% complete (~14h remaining), with the cluster processing ~2,116 TPS (2,116 non-vote). Measured slot time is 215ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $451.2K of Real Economic Value over the last 24h ($313/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $71.46 (+0.4% / 24h). Decentralization: Nakamoto coefficient 18, 661 active validators, 0.0% of stake delinquent. Alpenglow readiness: validators holding 100% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 3 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 470,211,754 |
| Block height | 448,226,630 |
| Epoch | 1088 (45.31% complete, ~14.1h left) |
| TPS (10 min avg) | 2,116 |
| Non-vote TPS | 2,116 |
| Slot time (measured) | 214.7 ms |
| Confirmation time (measured) | 0.21 s |
| Finality time (measured) | 0.21 s — **Alpenglow active** |
| Est. daily transactions | 162,208,328 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0022 |
| Node version | 4.4.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $71.46 (+0.4%/24h) |
| Market cap | $42.3B |
| **REV (24h)** | **$451.2K** (fees $353.0K + Jito tips $98.2K) |
| Chain TVL | $4.7B |
| Stablecoin supply | $14.3B |
| DEX volume (24h) | $1.4B (-20.1%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 591,684,396 SOL |
| Inflation | 3.55% |

Top DEXs by 24h volume: Orca DEX ($189.8M), BisonFi ($158.8M), PumpSwap ($142.8M), Raydium AMM ($126.4M), Meteora DLMM ($119.7M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 661 / 38 |
| Delinquent stake | 0.04% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.8% |
| Avg / median commission | 12.6% / 5% |
| Alpenglow BLS-key readiness | 687 validators, 100.0% of stake |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `he1iusunGwqrNtafDtLd…` | 16,936,855 | 3.95% | 0% |
| 2 | `CcaHc2L43ZWjwCHART3o…` | 16,432,361 | 3.83% | 7% |
| 3 | `3N7s9zXMZ4QqvHQR15t5…` | 12,486,687 | 2.91% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxb…` | 10,142,842 | 2.36% | 0% |
| 5 | `51JBzSTU5rAM8gLAVQKg…` | 9,787,748 | 2.28% | 10% |
| 6 | `CatzoSMUkTRidT5DwBxA…` | 9,620,150 | 2.24% | 5% |
| 7 | `26pV97Ce83ZQ6Kz9XT4t…` | 9,212,350 | 2.15% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2Fp…` | 7,959,108 | 1.85% | 7% |
| 9 | `DumiCKHVqoCQKD8roLAp…` | 6,992,227 | 1.63% | 0% |
| 10 | `CvSb7wdQAFpHuSpTYTJn…` | 6,709,566 | 1.56% | 5% |

## Signals (anomaly detection)

- **[WARNING]** SOL price contraction (z=-2.5 vs its recent baseline)
- **[WARNING]** Solana TVL contraction (z=-2.5 vs its recent baseline)
- **[WARNING · market_move]** Market-wide move: SOL price anomaly accompanied by liquidity/volume shifts — an ecosystem-level repricing rather than an isolated metric.

## Solana Pulse — sentiment (experimental)

**37/100 — Bearish** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 76.2 |
| fear greed | 10 |
| momentum | 16.9 |
| news | 42 |

Crypto Fear & Greed: 10 (Extreme Fear) · CoinGecko votes bullish: 76.19% · headline tone (48h): -1

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 1,304 |
| Raydium AMM v4 | 1,500 |
| Orca Whirlpool | 1,500 |
| Pump.fun | 1,500 |
| Tensor | 0 |
| Magic Eden v2 | 55 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,300,003 |
| Binance (cold) | 66 |
| OKX (attributed) | 67,807 |
| Coinbase (hot) | 25,510 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 215ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 100.0% of stake.
- **Agave**: latest release v4.4.1 · running 4.4.0 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 10281 ms |
| solana_rpc_validators | OK | 279 ms |
| coingecko | OK | 1684 ms |
| defillama_tvl | OK | 673 ms |
| defillama_dex | OK | 1208 ms |
| defillama_fees | OK | 1204 ms |
| defillama_stablecoins | OK | 271 ms |
| defillama_xstocks | FAILED | 343 ms |
| jito_kobe | OK | 177 ms |
| stakewiz | OK | 2959 ms |
| github | OK | 630 ms |
| solana_com_news | FAILED | 65 ms |
| sentiment | OK | 4054 ms |
| solana_status_page | OK | 224 ms |
| solana_rpc_whales | OK | 1860 ms |
| solana_rpc_programs | OK | 2807 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*