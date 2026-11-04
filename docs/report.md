# Solbeat — State of the Solana Network

> Generated 2026-11-04T15:50:29Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1077 is 22% complete (~20h remaining), with the cluster processing ~3,638 TPS (3,638 non-vote). Measured slot time is 217ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $617.3K of Real Economic Value over the last 24h ($429/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $96.30 (+2.8% / 24h). Decentralization: Nakamoto coefficient 17, 662 active validators, 0.5% of stake delinquent. Alpenglow readiness: validators holding 100% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 2 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 465,358,437 |
| Block height | 443,378,855 |
| Epoch | 1077 (21.86% complete, ~20.3h left) |
| TPS (10 min avg) | 3,638 |
| Non-vote TPS | 3,638 |
| Slot time (measured) | 217.0 ms |
| Confirmation time (measured) | 0.22 s |
| Finality time (measured) | 0.22 s — **Alpenglow active** |
| Est. daily transactions | 161,732,990 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0030 |
| Node version | 4.4.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $96.30 (+2.8%/24h) |
| Market cap | $56.9B |
| **REV (24h)** | **$617.3K** (fees $479.8K + Jito tips $137.5K) |
| Chain TVL | $5.4B |
| Stablecoin supply | $14.8B |
| DEX volume (24h) | $1.9B (1.5%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 590,262,351 SOL |
| Inflation | 3.57% |

Top DEXs by 24h volume: PumpSwap ($321.8M), Orca DEX ($259.8M), BisonFi ($257.1M), Raydium AMM ($191.6M), Tessera V ($154.4M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 662 / 31 |
| Delinquent stake | 0.46% |
| Nakamoto coefficient | 17 |
| Top-10 stake share | 24.7% |
| Avg / median commission | 12.6% / 5.0% |
| Alpenglow BLS-key readiness | 680 validators, 100.0% of stake |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L43ZWjwCHART3o…` | 17,036,631 | 3.93% | 7% |
| 2 | `he1iusunGwqrNtafDtLd…` | 16,710,689 | 3.86% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5…` | 13,012,272 | 3.01% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxb…` | 10,433,406 | 2.41% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxA…` | 9,524,736 | 2.2% | 5% |
| 6 | `51JBzSTU5rAM8gLAVQKg…` | 9,439,186 | 2.18% | 10% |
| 7 | `26pV97Ce83ZQ6Kz9XT4t…` | 9,217,930 | 2.13% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2Fp…` | 7,826,697 | 1.81% | 7% |
| 9 | `DumiCKHVqoCQKD8roLAp…` | 6,981,457 | 1.61% | 0% |
| 10 | `CvSb7wdQAFpHuSpTYTJn…` | 6,980,105 | 1.61% | 5% |

## Signals (anomaly detection)

- **[WARNING]** TPS spike: 3,638 vs 12h mean 1,822 (z=+2.2)
- **[SERIOUS]** Stablecoin supply contraction (z=-3.3 vs its recent baseline)

## Solana Pulse — sentiment (experimental)

**50/100 — Neutral** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 73.9 |
| fear greed | 34 |
| momentum | 40.6 |
| news | 50 |

Crypto Fear & Greed: 34 (Fear) · CoinGecko votes bullish: 73.91% · headline tone (48h): +0

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 1,448 |
| Raydium AMM v4 | 1,448 |
| Orca Whirlpool | 1,448 |
| Pump.fun | 1,500 |
| Tensor | 0 |
| Magic Eden v2 | 79 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,300,003 |
| Binance (cold) | 65 |
| OKX (attributed) | 346,930 |
| Coinbase (hot) | 7,757 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 217ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 100.0% of stake.
- **Agave**: latest release v4.4.0 · running 4.4.0 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 11505 ms |
| solana_rpc_validators | OK | 203 ms |
| coingecko | OK | 1649 ms |
| defillama_tvl | OK | 755 ms |
| defillama_dex | OK | 1167 ms |
| defillama_fees | OK | 974 ms |
| defillama_stablecoins | OK | 109 ms |
| defillama_xstocks | FAILED | 39 ms |
| jito_kobe | OK | 368 ms |
| stakewiz | OK | 1107 ms |
| github | OK | 750 ms |
| solana_com_news | FAILED | 63 ms |
| sentiment | OK | 2038 ms |
| solana_status_page | OK | 114 ms |
| solana_rpc_whales | OK | 1369 ms |
| solana_rpc_programs | OK | 1910 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*