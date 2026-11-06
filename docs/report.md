# Solbeat — State of the Solana Network

> Generated 2026-11-06T16:28:52Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1079 is 11% complete (~23h remaining), with the cluster processing ~2,619 TPS (2,619 non-vote). Measured slot time is 214ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $623.0K of Real Economic Value over the last 24h ($433/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $90.52 (-0.5% / 24h). Decentralization: Nakamoto coefficient 18, 658 active validators, 0.3% of stake delinquent. Alpenglow readiness: validators holding 100% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 1 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 466,176,830 |
| Block height | 444,196,011 |
| Epoch | 1079 (11.3% complete, ~22.8h left) |
| TPS (10 min avg) | 2,619 |
| Non-vote TPS | 2,619 |
| Slot time (measured) | 214.4 ms |
| Confirmation time (measured) | 0.21 s |
| Finality time (measured) | 0.21 s — **Alpenglow active** |
| Est. daily transactions | 142,994,468 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0035 |
| Node version | 4.4.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $90.52 (-0.5%/24h) |
| Market cap | $53.4B |
| **REV (24h)** | **$623.0K** (fees $499.4K + Jito tips $123.6K) |
| Chain TVL | $5.3B |
| Stablecoin supply | $15.0B |
| DEX volume (24h) | $2.2B (-7.8%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 590,342,676 SOL |
| Inflation | 3.57% |

Top DEXs by 24h volume: Orca DEX ($314.3M), BisonFi ($231.1M), Tessera V ($197.0M), PumpSwap ($188.6M), Meteora DLMM ($172.6M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 658 / 38 |
| Delinquent stake | 0.31% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.6% |
| Avg / median commission | 12.7% / 5.0% |
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

- **[WARNING]** Stablecoin supply contraction (z=-2.7 vs its recent baseline)

## Solana Pulse — sentiment (experimental)

**44/100 — Neutral** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 62.9 |
| fear greed | 28 |
| momentum | 39.3 |
| news | 42 |

Crypto Fear & Greed: 28 (Fear) · CoinGecko votes bullish: 62.86% · headline tone (48h): -1

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 1,226 |
| Raydium AMM v4 | 674 |
| Orca Whirlpool | 1,500 |
| Pump.fun | 1,500 |
| Tensor | 0 |
| Magic Eden v2 | 36 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,300,003 |
| Binance (cold) | 66 |
| OKX (attributed) | 97,314 |
| Coinbase (hot) | 25,039 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 214ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 100.0% of stake.
- **Agave**: latest release v4.4.1 · running 4.4.0 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 11248 ms |
| solana_rpc_validators | OK | 287 ms |
| coingecko | OK | 1760 ms |
| defillama_tvl | OK | 63 ms |
| defillama_dex | OK | 1183 ms |
| defillama_fees | OK | 1038 ms |
| defillama_stablecoins | OK | 88 ms |
| defillama_xstocks | FAILED | 793 ms |
| jito_kobe | OK | 282 ms |
| stakewiz | OK | 1492 ms |
| github | OK | 710 ms |
| solana_com_news | FAILED | 69 ms |
| sentiment | OK | 2305 ms |
| solana_status_page | OK | 356 ms |
| solana_rpc_whales | OK | 1191 ms |
| solana_rpc_programs | OK | 2192 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*