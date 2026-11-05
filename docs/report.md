# Solbeat — State of the Solana Network

> Generated 2026-11-05T16:18:46Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1078 is 17% complete (~21h remaining), with the cluster processing ~4,027 TPS (4,027 non-vote). Measured slot time is 215ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $703.1K of Real Economic Value over the last 24h ($488/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $90.70 (-6.5% / 24h). Decentralization: Nakamoto coefficient 18, 662 active validators, 0.2% of stake delinquent. Alpenglow readiness: validators holding 100% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 1 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 465,770,242 |
| Block height | 443,790,169 |
| Epoch | 1078 (17.19% complete, ~21.3h left) |
| TPS (10 min avg) | 4,027 |
| Non-vote TPS | 4,027 |
| Slot time (measured) | 214.7 ms |
| Confirmation time (measured) | 0.21 s |
| Finality time (measured) | 0.21 s — **Alpenglow active** |
| Est. daily transactions | 193,133,228 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0030 |
| Node version | 4.4.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $90.70 (-6.5%/24h) |
| Market cap | $53.5B |
| **REV (24h)** | **$703.1K** (fees $579.8K + Jito tips $123.3K) |
| Chain TVL | $5.5B |
| Stablecoin supply | $15.1B |
| DEX volume (24h) | $2.4B (26.8%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 590,317,611 SOL |
| Inflation | 3.57% |

Top DEXs by 24h volume: PumpSwap ($315.4M), Orca DEX ($269.1M), BisonFi ($241.3M), Meteora DLMM ($198.5M), Raydium AMM ($188.4M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 662 / 32 |
| Delinquent stake | 0.24% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.7% |
| Avg / median commission | 12.5% / 5.0% |
| Alpenglow BLS-key readiness | 681 validators, 100.0% of stake |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L43ZWjwCHART3o…` | 17,063,613 | 3.96% | 7% |
| 2 | `he1iusunGwqrNtafDtLd…` | 16,736,546 | 3.88% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5…` | 13,020,024 | 3.02% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxb…` | 10,434,901 | 2.42% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxA…` | 9,530,733 | 2.21% | 5% |
| 6 | `51JBzSTU5rAM8gLAVQKg…` | 9,459,109 | 2.2% | 10% |
| 7 | `26pV97Ce83ZQ6Kz9XT4t…` | 9,222,692 | 2.14% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2Fp…` | 7,860,096 | 1.82% | 7% |
| 9 | `DumiCKHVqoCQKD8roLAp…` | 6,991,477 | 1.62% | 0% |
| 10 | `3JD3jMmnR6g88qff2WZ3…` | 6,293,076 | 1.46% | 0% |

## Signals (anomaly detection)

- **[WARNING]** Stablecoin supply contraction (z=-2.4 vs its recent baseline)

## Solana Pulse — sentiment (experimental)

**59/100 — Neutral** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 75.0 |
| fear greed | 50 |
| momentum | 55.1 |
| news | 50 |

Crypto Fear & Greed: 50 (Neutral) · CoinGecko votes bullish: 75.0% · headline tone (48h): +0

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 1,500 |
| Raydium AMM v4 | 1,500 |
| Orca Whirlpool | 1,500 |
| Pump.fun | 1,500 |
| Tensor | 0 |
| Magic Eden v2 | 29 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,300,003 |
| Binance (cold) | 66 |
| OKX (attributed) | 346,932 |
| Coinbase (hot) | 19,921 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 215ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 100.0% of stake.
- **Agave**: latest release v4.4.0 · running 4.4.0 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 38375 ms |
| solana_rpc_validators | OK | 2003 ms |
| coingecko | OK | 1737 ms |
| defillama_tvl | OK | 277 ms |
| defillama_dex | OK | 857 ms |
| defillama_fees | OK | 874 ms |
| defillama_stablecoins | OK | 167 ms |
| defillama_xstocks | FAILED | 104 ms |
| jito_kobe | OK | 213 ms |
| stakewiz | OK | 1059 ms |
| github | OK | 1040 ms |
| solana_com_news | FAILED | 91 ms |
| sentiment | OK | 2424 ms |
| solana_status_page | OK | 462 ms |
| solana_rpc_whales | OK | 7069 ms |
| solana_rpc_programs | OK | 4449 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*