# Solbeat — State of the Solana Network

> Generated 2026-11-07T09:01:09Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1079 is 76% complete (~6h remaining), with the cluster processing ~998 TPS (998 non-vote). Measured slot time is 214ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $590.4K of Real Economic Value over the last 24h ($410/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $90.24 (+0.8% / 24h). Decentralization: Nakamoto coefficient 18, 659 active validators, 0.3% of stake delinquent. Alpenglow readiness: validators holding 100% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 1 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 466,454,306 |
| Block height | 444,473,015 |
| Epoch | 1079 (75.53% complete, ~6.3h left) |
| TPS (10 min avg) | 998 |
| Non-vote TPS | 998 |
| Slot time (measured) | 214.0 ms |
| Confirmation time (measured) | 0.21 s |
| Finality time (measured) | 0.21 s — **Alpenglow active** |
| Est. daily transactions | 110,061,352 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0042 |
| Node version | 4.4.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $90.24 (+0.8%/24h) |
| Market cap | $53.3B |
| **REV (24h)** | **$590.4K** (fees $466.9K + Jito tips $123.4K) |
| Chain TVL | $5.2B |
| Stablecoin supply | $14.8B |
| DEX volume (24h) | $1.9B (-15.6%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 590,982,559 SOL |
| Inflation | 3.57% |

Top DEXs by 24h volume: BisonFi ($231.1M), Orca DEX ($209.9M), Tessera V ($197.0M), Meteora DLMM ($172.6M), Scorch ($147.4M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 659 / 37 |
| Delinquent stake | 0.28% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.6% |
| Avg / median commission | 12.8% / 5% |
| Alpenglow BLS-key readiness | 682 validators, 100.0% of stake |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L43ZWjwCHART3o…` | 17,039,556 | 3.92% | 7% |
| 2 | `he1iusunGwqrNtafDtLd…` | 16,722,209 | 3.84% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5…` | 13,017,562 | 2.99% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxb…` | 10,436,420 | 2.4% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxA…` | 9,531,946 | 2.19% | 5% |
| 6 | `51JBzSTU5rAM8gLAVQKg…` | 9,519,642 | 2.19% | 10% |
| 7 | `26pV97Ce83ZQ6Kz9XT4t…` | 9,240,519 | 2.12% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2Fp…` | 7,741,933 | 1.78% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJn…` | 6,982,918 | 1.61% | 5% |
| 10 | `DumiCKHVqoCQKD8roLAp…` | 6,971,614 | 1.6% | 0% |

## Signals (anomaly detection)

- **[SERIOUS]** Stablecoin supply contraction (z=-3.0 vs its recent baseline)

## Solana Pulse — sentiment (experimental)

**41/100 — Neutral** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 70.6 |
| fear greed | 25 |
| momentum | 32.5 |
| news | 26 |

Crypto Fear & Greed: 25 (Extreme Fear) · CoinGecko votes bullish: 70.59% · headline tone (48h): -3

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 900 |
| Raydium AMM v4 | 563 |
| Orca Whirlpool | 563 |
| Pump.fun | 1,500 |
| Tensor | 0 |
| Magic Eden v2 | 31 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,300,003 |
| Binance (cold) | 66 |
| OKX (attributed) | 97,315 |
| Coinbase (hot) | 23,633 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 214ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 100.0% of stake.
- **Agave**: latest release v4.4.1 · running 4.4.0 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 9904 ms |
| solana_rpc_validators | OK | 112 ms |
| coingecko | OK | 1692 ms |
| defillama_tvl | OK | 161 ms |
| defillama_dex | OK | 413 ms |
| defillama_fees | OK | 4954 ms |
| defillama_stablecoins | OK | 113 ms |
| defillama_xstocks | FAILED | 34 ms |
| jito_kobe | OK | 94 ms |
| stakewiz | OK | 665 ms |
| github | OK | 587 ms |
| solana_com_news | FAILED | 44 ms |
| sentiment | OK | 2044 ms |
| solana_status_page | OK | 334 ms |
| solana_rpc_whales | OK | 1010 ms |
| solana_rpc_programs | OK | 1746 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*