# Solbeat — State of the Solana Network

> Generated 2026-11-05T20:42:14Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1078 is 34% complete (~17h remaining), with the cluster processing ~2,792 TPS (2,792 non-vote). Measured slot time is 215ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $702.0K of Real Economic Value over the last 24h ($488/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $90.04 (-5.1% / 24h). Decentralization: Nakamoto coefficient 18, 663 active validators, 0.1% of stake delinquent. Alpenglow readiness: validators holding 100% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 2 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 465,844,014 |
| Block height | 443,863,871 |
| Epoch | 1078 (34.26% complete, ~17.0h left) |
| TPS (10 min avg) | 2,792 |
| Non-vote TPS | 2,792 |
| Slot time (measured) | 214.9 ms |
| Confirmation time (measured) | 0.21 s |
| Finality time (measured) | 0.21 s — **Alpenglow active** |
| Est. daily transactions | 229,903,911 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0025 |
| Node version | 4.4.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $90.04 (-5.1%/24h) |
| Market cap | $53.1B |
| **REV (24h)** | **$702.0K** (fees $579.8K + Jito tips $122.3K) |
| Chain TVL | $5.3B |
| Stablecoin supply | $15.1B |
| DEX volume (24h) | $2.4B (26.8%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 590,287,473 SOL |
| Inflation | 3.57% |

Top DEXs by 24h volume: PumpSwap ($315.4M), Orca DEX ($279.9M), BisonFi ($241.3M), Raydium AMM ($219.6M), Meteora DLMM ($198.5M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 663 / 31 |
| Delinquent stake | 0.13% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.7% |
| Avg / median commission | 12.7% / 5% |
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

- **[WARNING]** SOL price contraction (z=-2.0 vs its recent baseline)
- **[WARNING]** Stablecoin supply contraction (z=-2.4 vs its recent baseline)

## Solana Pulse — sentiment (experimental)

**57/100 — Neutral** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 68.4 |
| fear greed | 50 |
| momentum | 50.1 |
| news | 58 |

Crypto Fear & Greed: 50 (Neutral) · CoinGecko votes bullish: 68.42% · headline tone (48h): +1

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 1,500 |
| Raydium AMM v4 | 815 |
| Orca Whirlpool | 815 |
| Pump.fun | 1,500 |
| Tensor | 0 |
| Magic Eden v2 | 89 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,300,003 |
| Binance (cold) | 66 |
| OKX (attributed) | 346,932 |
| Coinbase (hot) | 16,012 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 215ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 100.0% of stake.
- **Agave**: latest release v4.4.1 · running 4.4.0 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 10933 ms |
| solana_rpc_validators | OK | 166 ms |
| coingecko | OK | 1602 ms |
| defillama_tvl | OK | 89 ms |
| defillama_dex | OK | 896 ms |
| defillama_fees | OK | 1349 ms |
| defillama_stablecoins | OK | 92 ms |
| defillama_xstocks | FAILED | 609 ms |
| jito_kobe | OK | 237 ms |
| stakewiz | OK | 984 ms |
| github | OK | 705 ms |
| solana_com_news | FAILED | 58 ms |
| sentiment | OK | 2156 ms |
| solana_status_page | OK | 196 ms |
| solana_rpc_whales | OK | 996 ms |
| solana_rpc_programs | OK | 1825 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*