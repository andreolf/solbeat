# Solbeat — State of the Solana Network

> Generated 2026-11-16T19:48:09Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1088 is 55% complete (~12h remaining), with the cluster processing ~2,462 TPS (2,462 non-vote). Measured slot time is 215ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $450.3K of Real Economic Value over the last 24h ($313/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $71.00 (-1.1% / 24h). Decentralization: Nakamoto coefficient 18, 662 active validators, 0.0% of stake delinquent. Alpenglow readiness: validators holding 100% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 3 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 470,254,484 |
| Block height | 448,269,357 |
| Epoch | 1088 (55.2% complete, ~11.6h left) |
| TPS (10 min avg) | 2,462 |
| Non-vote TPS | 2,462 |
| Slot time (measured) | 215.4 ms |
| Confirmation time (measured) | 0.22 s |
| Finality time (measured) | 0.22 s — **Alpenglow active** |
| Est. daily transactions | 201,731,040 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0018 |
| Node version | 4.4.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $71.00 (-1.1%/24h) |
| Market cap | $42.0B |
| **REV (24h)** | **$450.3K** (fees $353.0K + Jito tips $97.3K) |
| Chain TVL | $4.7B |
| Stablecoin supply | $14.3B |
| DEX volume (24h) | $1.4B (-20.1%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 591,684,336 SOL |
| Inflation | 3.55% |

Top DEXs by 24h volume: Orca DEX ($189.8M), BisonFi ($158.8M), PumpSwap ($142.8M), Raydium AMM ($129.7M), Meteora DLMM ($119.7M)

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

- **[WARNING]** SOL price contraction (z=-2.5 vs its recent baseline)
- **[WARNING]** Solana TVL contraction (z=-2.5 vs its recent baseline)
- **[WARNING · market_move]** Market-wide move: SOL price anomaly accompanied by liquidity/volume shifts — an ecosystem-level repricing rather than an isolated metric.

## Solana Pulse — sentiment (experimental)

**37/100 — Bearish** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 77.8 |
| fear greed | 10 |
| momentum | 17.0 |
| news | 42 |

Crypto Fear & Greed: 10 (Extreme Fear) · CoinGecko votes bullish: 77.78% · headline tone (48h): -1

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 688 |
| Raydium AMM v4 | 688 |
| Orca Whirlpool | 1,500 |
| Pump.fun | 1,500 |
| Tensor | 0 |
| Magic Eden v2 | 50 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,300,003 |
| Binance (cold) | 66 |
| OKX (attributed) | 67,813 |
| Coinbase (hot) | 26,732 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 215ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 100.0% of stake.
- **Agave**: latest release v4.4.1 · running 4.4.0 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 10333 ms |
| solana_rpc_validators | OK | 334 ms |
| coingecko | OK | 1723 ms |
| defillama_tvl | OK | 977 ms |
| defillama_dex | OK | 1102 ms |
| defillama_fees | OK | 1439 ms |
| defillama_stablecoins | OK | 776 ms |
| defillama_xstocks | FAILED | 769 ms |
| jito_kobe | OK | 13830 ms |
| stakewiz | OK | 1563 ms |
| github | OK | 630 ms |
| solana_com_news | FAILED | 104 ms |
| sentiment | OK | 2240 ms |
| solana_status_page | OK | 272 ms |
| solana_rpc_whales | OK | 1534 ms |
| solana_rpc_programs | OK | 2233 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*