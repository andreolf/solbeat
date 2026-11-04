# Solbeat — State of the Solana Network

> Generated 2026-11-04T04:51:00Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1076 is 79% complete (~5h remaining), with the cluster processing ~1,905 TPS (1,905 non-vote). Measured slot time is 214ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $590.6K of Real Economic Value over the last 24h ($410/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $91.95 (-0.3% / 24h). Decentralization: Nakamoto coefficient 18, 666 active validators, 0.4% of stake delinquent. Alpenglow readiness: validators holding 100% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 1 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 465,173,900 |
| Block height | 443,194,477 |
| Epoch | 1076 (79.14% complete, ~5.3h left) |
| TPS (10 min avg) | 1,905 |
| Non-vote TPS | 1,905 |
| Slot time (measured) | 213.5 ms |
| Confirmation time (measured) | 0.21 s |
| Finality time (measured) | 0.21 s — **Alpenglow active** |
| Est. daily transactions | 188,171,231 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0026 |
| Node version | 4.4.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $91.95 (-0.3%/24h) |
| Market cap | $54.3B |
| **REV (24h)** | **$590.6K** (fees $479.8K + Jito tips $110.8K) |
| Chain TVL | $5.4B |
| Stablecoin supply | $14.8B |
| DEX volume (24h) | $1.9B (1.1%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 590,206,732 SOL |
| Inflation | 3.57% |

Top DEXs by 24h volume: PumpSwap ($321.8M), BisonFi ($250.5M), Orca DEX ($193.6M), Raydium AMM ($156.8M), Tessera V ($149.8M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 666 / 27 |
| Delinquent stake | 0.42% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.7% |
| Avg / median commission | 12.8% / 5.0% |
| Alpenglow BLS-key readiness | 680 validators, 100.0% of stake |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L43ZWjwCHART3o…` | 17,030,641 | 3.92% | 7% |
| 2 | `he1iusunGwqrNtafDtLd…` | 16,704,340 | 3.84% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5…` | 13,043,664 | 3.0% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxb…` | 10,431,126 | 2.4% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxA…` | 9,561,007 | 2.2% | 5% |
| 6 | `51JBzSTU5rAM8gLAVQKg…` | 9,435,905 | 2.17% | 10% |
| 7 | `26pV97Ce83ZQ6Kz9XT4t…` | 9,232,746 | 2.12% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2Fp…` | 7,814,810 | 1.8% | 7% |
| 9 | `DumiCKHVqoCQKD8roLAp…` | 7,008,986 | 1.61% | 0% |
| 10 | `CvSb7wdQAFpHuSpTYTJn…` | 6,979,031 | 1.61% | 5% |

## Signals (anomaly detection)

- **[SERIOUS]** Stablecoin supply contraction (z=-3.0 vs its recent baseline)

## Solana Pulse — sentiment (experimental)

**50/100 — Neutral** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 71.4 |
| fear greed | 34 |
| momentum | 34.6 |
| news | 66 |

Crypto Fear & Greed: 34 (Fear) · CoinGecko votes bullish: 71.43% · headline tone (48h): +2

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 1,500 |
| Raydium AMM v4 | 815 |
| Orca Whirlpool | 1,500 |
| Pump.fun | 1,500 |
| Tensor | 0 |
| Magic Eden v2 | 66 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,300,003 |
| Binance (cold) | 4 |
| OKX (attributed) | 339,402 |
| Coinbase (hot) | 22,200 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 214ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 100.0% of stake.
- **Agave**: latest release v4.4.0 · running 4.4.0 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 10561 ms |
| solana_rpc_validators | OK | 302 ms |
| coingecko | OK | 1701 ms |
| defillama_tvl | OK | 212 ms |
| defillama_dex | OK | 1010 ms |
| defillama_fees | OK | 196 ms |
| defillama_stablecoins | OK | 119 ms |
| defillama_xstocks | FAILED | 701 ms |
| jito_kobe | OK | 133 ms |
| stakewiz | OK | 1241 ms |
| github | OK | 869 ms |
| solana_com_news | FAILED | 154 ms |
| sentiment | OK | 2277 ms |
| solana_status_page | OK | 320 ms |
| solana_rpc_whales | OK | 1269 ms |
| solana_rpc_programs | OK | 2558 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*