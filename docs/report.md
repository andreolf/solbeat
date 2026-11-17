# Solbeat — State of the Solana Network

> Generated 2026-11-17T05:11:54Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1088 is 92% complete (~2h remaining), with the cluster processing ~1,378 TPS (1,378 non-vote). Measured slot time is 216ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $452.3K of Real Economic Value over the last 24h ($314/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $72.78 (+2.0% / 24h). Decentralization: Nakamoto coefficient 18, 662 active validators, 0.0% of stake delinquent. Alpenglow readiness: validators holding 100% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 3 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 470,411,849 |
| Block height | 448,426,689 |
| Epoch | 1088 (91.63% complete, ~2.2h left) |
| TPS (10 min avg) | 1,378 |
| Non-vote TPS | 1,378 |
| Slot time (measured) | 216.3 ms |
| Confirmation time (measured) | 0.22 s |
| Finality time (measured) | 0.22 s — **Alpenglow active** |
| Est. daily transactions | 146,877,747 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0024 |
| Node version | 4.4.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $72.78 (+2.0%/24h) |
| Market cap | $43.1B |
| **REV (24h)** | **$452.3K** (fees $353.0K + Jito tips $99.3K) |
| Chain TVL | $4.7B |
| Stablecoin supply | $14.3B |
| DEX volume (24h) | $1.4B (3.4%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 591,684,158 SOL |
| Inflation | 3.55% |

Top DEXs by 24h volume: Orca DEX ($212.4M), BisonFi ($158.8M), PumpSwap ($157.2M), Raydium AMM ($132.2M), Meteora DLMM ($119.7M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 662 / 37 |
| Delinquent stake | 0.04% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.8% |
| Avg / median commission | 12.8% / 5.0% |
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

- **[WARNING]** SOL price contraction (z=-2.2 vs its recent baseline)
- **[WARNING]** Solana TVL contraction (z=-2.4 vs its recent baseline)
- **[WARNING · market_move]** Market-wide move: SOL price anomaly accompanied by liquidity/volume shifts — an ecosystem-level repricing rather than an isolated metric.

## Solana Pulse — sentiment (experimental)

**33/100 — Bearish** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| momentum | 32.7 |
## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 1,082 |
| Raydium AMM v4 | 628 |
| Orca Whirlpool | 1,082 |
| Pump.fun | 1,500 |
| Tensor | 0 |
| Magic Eden v2 | 74 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,300,003 |
| Binance (cold) | 66 |
| OKX (attributed) | 67,901 |
| Coinbase (hot) | 34,587 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 216ms.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 100.0% of stake.
- **Agave**: latest release None · running 4.4.0 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 8813 ms |
| solana_rpc_validators | OK | 226 ms |
| coingecko | OK | 1735 ms |
| defillama_tvl | OK | 50 ms |
| defillama_dex | OK | 52 ms |
| defillama_fees | OK | 1480 ms |
| defillama_stablecoins | OK | 886 ms |
| defillama_xstocks | FAILED | 43 ms |
| jito_kobe | OK | 111 ms |
| stakewiz | OK | 1545 ms |
| github | FAILED | 6147 ms |
| solana_com_news | FAILED | 54 ms |
| sentiment | FAILED | 2285 ms |
| solana_status_page | OK | 177 ms |
| solana_rpc_whales | OK | 1075 ms |
| solana_rpc_programs | OK | 2054 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*