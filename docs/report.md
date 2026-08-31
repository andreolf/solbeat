# Solbeat — State of the Solana Network

> Generated 2026-08-31T17:34:11Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1025 is 95% complete (~2h remaining), with the cluster processing ~4,436 TPS (2,318 non-vote). Measured slot time is 320ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $853.6K of Real Economic Value over the last 24h ($593/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $102.79 (-2.9% / 24h). Decentralization: Nakamoto coefficient 18, 680 active validators, 0.0% of stake delinquent. Alpenglow readiness: validators holding 99% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 1 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 443,209,135 |
| Block height | 421,256,801 |
| Epoch | 1025 (94.71% complete, ~2.0h left) |
| TPS (10 min avg) | 4,436 |
| Non-vote TPS | 2,318 |
| Slot time (measured) | 319.6 ms |
| Est. daily transactions | 397,407,223 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0032 |
| Node version | 4.2.1 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $102.79 (-2.9%/24h) |
| Market cap | $60.2B |
| **REV (24h)** | **$853.6K** (fees $677.1K + Jito tips $176.5K) |
| Chain TVL | $5.8B |
| Stablecoin supply | $16.1B |
| DEX volume (24h) | $1.9B (15.5%/1d) |
| Tokenized equities (xStocks TVL) | $437.2M |
| Circulating supply | 585,120,808 SOL |
| Inflation | 3.67% |

Top DEXs by 24h volume: PumpSwap ($732.1M), Orca DEX ($274.3M), BisonFi ($184.5M), Meteora DLMM ($142.7M), Manifest Trade ($134.3M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 680 / 17 |
| Delinquent stake | 0.01% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.3% |
| Avg / median commission | 12.4% / 5.0% |
| Alpenglow BLS-key readiness | 698 validators, 99.3% of stake |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L43ZWjwCHART3o…` | 17,203,741 | 3.94% | 7% |
| 2 | `he1iusunGwqrNtafDtLd…` | 16,085,807 | 3.68% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5…` | 12,389,824 | 2.83% | 0% |
| 4 | `CatzoSMUkTRidT5DwBxA…` | 11,479,512 | 2.63% | 5% |
| 5 | `8GbwASqdpw4dVcwbWUxb…` | 9,452,658 | 2.16% | 0% |
| 6 | `26pV97Ce83ZQ6Kz9XT4t…` | 9,293,056 | 2.13% | 7% |
| 7 | `51JBzSTU5rAM8gLAVQKg…` | 9,023,631 | 2.06% | 10% |
| 8 | `CvSb7wdQAFpHuSpTYTJn…` | 7,295,972 | 1.67% | 5% |
| 9 | `9QU2QSxhb24FUX3Tu2Fp…` | 7,201,762 | 1.65% | 7% |
| 10 | `DumiCKHVqoCQKD8roLAp…` | 6,589,845 | 1.51% | 0% |

## Signals (anomaly detection)

- **[WARNING]** Solana TVL surge (z=+2.9 vs its recent baseline)

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 121 |
| Raydium AMM v4 | 131 |
| Orca Whirlpool | 121 |
| Pump.fun | 144 |
| Tensor | 0 |
| Magic Eden v2 | 70 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,188,448 |
| Binance (cold) | 1,698,810 |
| OKX (attributed) | 335,571 |
| Coinbase (hot) | 32,320 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 320ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 99.3% of stake.
- **Agave**: latest release v4.2.2 · running 4.2.1 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 7625 ms |
| solana_rpc_validators | OK | 92 ms |
| coingecko | OK | 1638 ms |
| defillama_tvl | OK | 41 ms |
| defillama_dex | OK | 782 ms |
| defillama_fees | OK | 682 ms |
| defillama_stablecoins | OK | 72 ms |
| defillama_xstocks | OK | 83 ms |
| jito_kobe | OK | 184 ms |
| stakewiz | OK | 1047 ms |
| github | OK | 605 ms |
| solana_status_page | OK | 342 ms |
| solana_rpc_whales | OK | 783 ms |
| solana_rpc_programs | OK | 1399 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*