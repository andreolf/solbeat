# Solbeat — State of the Solana Network

> Generated 2026-11-10T14:41:48Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1082 is 77% complete (~6h remaining), with the cluster processing ~2,925 TPS (2,925 non-vote). Measured slot time is 214ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $515.7K of Real Economic Value over the last 24h ($358/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $84.36 (-3.1% / 24h). Decentralization: Nakamoto coefficient 18, 656 active validators, 0.7% of stake delinquent. Alpenglow readiness: validators holding 100% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 3 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 467,757,981 |
| Block height | 445,775,395 |
| Epoch | 1082 (77.31% complete, ~5.8h left) |
| TPS (10 min avg) | 2,925 |
| Non-vote TPS | 2,925 |
| Slot time (measured) | 214.0 ms |
| Confirmation time (measured) | 0.21 s |
| Finality time (measured) | 0.21 s — **Alpenglow active** |
| Est. daily transactions | 118,201,097 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0035 |
| Node version | 4.4.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $84.36 (-3.1%/24h) |
| Market cap | $49.9B |
| **REV (24h)** | **$515.7K** (fees $408.0K + Jito tips $107.7K) |
| Chain TVL | $5.0B |
| Stablecoin supply | $14.8B |
| DEX volume (24h) | $1.5B (42.6%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 591,149,039 SOL |
| Inflation | 3.56% |

Top DEXs by 24h volume: PumpSwap ($256.1M), Orca DEX ($178.9M), BisonFi ($157.1M), Raydium AMM ($127.8M), Meteora DLMM ($122.7M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 656 / 42 |
| Delinquent stake | 0.67% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.6% |
| Avg / median commission | 12.8% / 5.0% |
| Alpenglow BLS-key readiness | 684 validators, 100.0% of stake |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L43ZWjwCHART3o…` | 16,898,208 | 3.88% | 7% |
| 2 | `he1iusunGwqrNtafDtLd…` | 16,746,254 | 3.85% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5…` | 13,034,244 | 3.0% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxb…` | 10,280,950 | 2.36% | 0% |
| 5 | `51JBzSTU5rAM8gLAVQKg…` | 9,598,549 | 2.21% | 10% |
| 6 | `CatzoSMUkTRidT5DwBxA…` | 9,553,851 | 2.2% | 5% |
| 7 | `26pV97Ce83ZQ6Kz9XT4t…` | 9,233,159 | 2.12% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2Fp…` | 7,813,316 | 1.8% | 7% |
| 9 | `DumiCKHVqoCQKD8roLAp…` | 6,987,971 | 1.61% | 0% |
| 10 | `CvSb7wdQAFpHuSpTYTJn…` | 6,712,231 | 1.54% | 5% |

## Signals (anomaly detection)

- **[SERIOUS]** TPS spike: 2,925 vs 12h mean 1,333 (z=+4.2)
- **[WARNING]** SOL price contraction (z=-2.2 vs its recent baseline)
- **[WARNING]** Stablecoin supply contraction (z=-2.8 vs its recent baseline)

## Solana Pulse — sentiment (experimental)

**46/100 — Neutral** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 62.5 |
| fear greed | 32 |
| momentum | 48.2 |
| news | 34 |

Crypto Fear & Greed: 32 (Fear) · CoinGecko votes bullish: 62.5% · headline tone (48h): -2

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 1,500 |
| Raydium AMM v4 | 1,500 |
| Orca Whirlpool | 1,500 |
| Pump.fun | 1,500 |
| Tensor | 1 |
| Magic Eden v2 | 52 |
| Marinade | 4 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,300,003 |
| Binance (cold) | 66 |
| OKX (attributed) | 97,639 |
| Coinbase (hot) | 92,836 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 214ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 100.0% of stake.
- **Agave**: latest release v4.4.1 · running 4.4.0 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 10689 ms |
| solana_rpc_validators | OK | 360 ms |
| coingecko | OK | 1785 ms |
| defillama_tvl | OK | 88 ms |
| defillama_dex | OK | 1137 ms |
| defillama_fees | OK | 1415 ms |
| defillama_stablecoins | OK | 826 ms |
| defillama_xstocks | FAILED | 791 ms |
| jito_kobe | OK | 238 ms |
| stakewiz | OK | 1410 ms |
| github | OK | 1113 ms |
| solana_com_news | FAILED | 91 ms |
| sentiment | OK | 2362 ms |
| solana_status_page | OK | 323 ms |
| solana_rpc_whales | OK | 1074 ms |
| solana_rpc_programs | OK | 2103 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*