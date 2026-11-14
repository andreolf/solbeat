# Solbeat — State of the Solana Network

> Generated 2026-11-14T02:12:55Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1086 is 1% complete (~26h remaining), with the cluster processing ~1,863 TPS (1,863 non-vote). Measured slot time is 215ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $558.8K of Real Economic Value over the last 24h ($388/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $76.67 (-5.2% / 24h). Decentralization: Nakamoto coefficient 18, 663 active validators, 0.1% of stake delinquent. Alpenglow readiness: validators holding 100% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 5 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 469,156,167 |
| Block height | 447,171,309 |
| Epoch | 1086 (0.96% complete, ~25.5h left) |
| TPS (10 min avg) | 1,863 |
| Non-vote TPS | 1,863 |
| Slot time (measured) | 214.9 ms |
| Confirmation time (measured) | 0.21 s |
| Finality time (measured) | 0.21 s — **Alpenglow active** |
| Est. daily transactions | 169,150,228 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0027 |
| Node version | 4.4.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $76.67 (-5.2%/24h) |
| Market cap | $45.4B |
| **REV (24h)** | **$558.8K** (fees $448.8K + Jito tips $110.1K) |
| Chain TVL | $4.9B |
| Stablecoin supply | $14.1B |
| DEX volume (24h) | $1.5B (-3.4%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 591,574,564 SOL |
| Inflation | 3.56% |

Top DEXs by 24h volume: Orca DEX ($241.3M), PumpSwap ($177.3M), BisonFi ($147.3M), Meteora DLMM ($144.7M), Raydium AMM ($134.8M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 663 / 36 |
| Delinquent stake | 0.09% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.7% |
| Avg / median commission | 12.7% / 5% |
| Alpenglow BLS-key readiness | 686 validators, 100.0% of stake |

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

- **[WARNING]** SOL price contraction (z=-2.4 vs its recent baseline)
- **[WARNING]** Solana TVL contraction (z=-2.1 vs its recent baseline)
- **[WARNING]** Stablecoin supply contraction (z=-2.3 vs its recent baseline)
- **[WARNING · market_move]** Market-wide move: SOL price anomaly accompanied by liquidity/volume shifts — an ecosystem-level repricing rather than an isolated metric.
- **[WARNING · liquidity_rotation]** Stablecoin supply and TVL moving together — capital rotating in or out of the chain.

## Solana Pulse — sentiment (experimental)

**27/100 — Bearish** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| momentum | 26.9 |
## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 1,500 |
| Raydium AMM v4 | 1,026 |
| Orca Whirlpool | 1,500 |
| Pump.fun | 1,500 |
| Tensor | 0 |
| Magic Eden v2 | 17 |
| Marinade | 3 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,300,003 |
| Binance (cold) | 66 |
| OKX (attributed) | 47,546 |
| Coinbase (hot) | 6,662 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 215ms.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 100.0% of stake.
- **Agave**: latest release None · running 4.4.0 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 14188 ms |
| solana_rpc_validators | OK | 89 ms |
| coingecko | OK | 1606 ms |
| defillama_tvl | OK | 29 ms |
| defillama_dex | OK | 414 ms |
| defillama_fees | OK | 57 ms |
| defillama_stablecoins | OK | 64 ms |
| defillama_xstocks | FAILED | 23 ms |
| jito_kobe | OK | 155 ms |
| stakewiz | OK | 880 ms |
| github | FAILED | 6036 ms |
| solana_com_news | FAILED | 21 ms |
| sentiment | FAILED | 19605 ms |
| solana_status_page | OK | 53 ms |
| solana_rpc_whales | OK | 3104 ms |
| solana_rpc_programs | OK | 2366 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*