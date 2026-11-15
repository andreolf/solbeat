# Solbeat — State of the Solana Network

> Generated 2026-11-15T03:16:15Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1086 is 98% complete (~0h remaining), with the cluster processing ~1,402 TPS (1,402 non-vote). Measured slot time is 215ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $457.4K of Real Economic Value over the last 24h ($318/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $71.81 (-5.5% / 24h). Decentralization: Nakamoto coefficient 18, 662 active validators, 0.1% of stake delinquent. Alpenglow readiness: validators holding 100% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 5 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 469,575,366 |
| Block height | 447,590,398 |
| Epoch | 1086 (98.0% complete, ~0.5h left) |
| TPS (10 min avg) | 1,402 |
| Non-vote TPS | 1,402 |
| Slot time (measured) | 215.4 ms |
| Confirmation time (measured) | 0.22 s |
| Finality time (measured) | 0.22 s — **Alpenglow active** |
| Est. daily transactions | 177,019,733 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0020 |
| Node version | 4.4.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $71.81 (-5.5%/24h) |
| Market cap | $42.5B |
| **REV (24h)** | **$457.4K** (fees $357.1K + Jito tips $100.3K) |
| Chain TVL | $4.6B |
| Stablecoin supply | $14.1B |
| DEX volume (24h) | $1.6B (2.5%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 591,573,559 SOL |
| Inflation | 3.56% |

Top DEXs by 24h volume: Orca DEX ($300.4M), BisonFi ($186.9M), Meteora DLMM ($164.8M), PumpSwap ($156.4M), Raydium AMM ($139.4M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 662 / 37 |
| Delinquent stake | 0.09% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.7% |
| Avg / median commission | 12.7% / 5.0% |
| Alpenglow BLS-key readiness | 685 validators, 100.0% of stake |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `he1iusunGwqrNtafDtLd…` | 16,955,905 | 3.95% | 0% |
| 2 | `CcaHc2L43ZWjwCHART3o…` | 16,374,909 | 3.81% | 7% |
| 3 | `3N7s9zXMZ4QqvHQR15t5…` | 12,611,498 | 2.94% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxb…` | 10,140,468 | 2.36% | 0% |
| 5 | `51JBzSTU5rAM8gLAVQKg…` | 9,736,890 | 2.27% | 10% |
| 6 | `CatzoSMUkTRidT5DwBxA…` | 9,574,439 | 2.23% | 5% |
| 7 | `26pV97Ce83ZQ6Kz9XT4t…` | 9,199,377 | 2.14% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2Fp…` | 7,914,792 | 1.84% | 7% |
| 9 | `DumiCKHVqoCQKD8roLAp…` | 6,990,062 | 1.63% | 0% |
| 10 | `CvSb7wdQAFpHuSpTYTJn…` | 6,707,745 | 1.56% | 5% |

## Signals (anomaly detection)

- **[WARNING]** SOL price contraction (z=-2.6 vs its recent baseline)
- **[WARNING]** Solana TVL contraction (z=-2.8 vs its recent baseline)
- **[WARNING]** Stablecoin supply contraction (z=-2.2 vs its recent baseline)
- **[WARNING · market_move]** Market-wide move: SOL price anomaly accompanied by liquidity/volume shifts — an ecosystem-level repricing rather than an isolated metric.
- **[WARNING · liquidity_rotation]** Stablecoin supply and TVL moving together — capital rotating in or out of the chain.

## Solana Pulse — sentiment (experimental)

**39/100 — Bearish** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 79.5 |
| fear greed | 10 |
| momentum | 24.6 |
| news | 34 |

Crypto Fear & Greed: 10 (Extreme Fear) · CoinGecko votes bullish: 79.49% · headline tone (48h): -2

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 1,500 |
| Raydium AMM v4 | 872 |
| Orca Whirlpool | 872 |
| Pump.fun | 1,500 |
| Tensor | 0 |
| Magic Eden v2 | 36 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,300,003 |
| Binance (cold) | 66 |
| OKX (attributed) | 4 |
| Coinbase (hot) | 29,169 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 215ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 100.0% of stake.
- **Agave**: latest release v4.4.1 · running 4.4.0 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 9513 ms |
| solana_rpc_validators | OK | 371 ms |
| coingecko | OK | 1680 ms |
| defillama_tvl | OK | 816 ms |
| defillama_dex | OK | 926 ms |
| defillama_fees | OK | 1620 ms |
| defillama_stablecoins | OK | 832 ms |
| defillama_xstocks | FAILED | 67 ms |
| jito_kobe | OK | 336 ms |
| stakewiz | OK | 1152 ms |
| github | OK | 795 ms |
| solana_com_news | FAILED | 95 ms |
| sentiment | OK | 2313 ms |
| solana_status_page | OK | 323 ms |
| solana_rpc_whales | OK | 1231 ms |
| solana_rpc_programs | OK | 2076 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*