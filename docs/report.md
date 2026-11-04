# Solbeat — State of the Solana Network

> Generated 2026-11-04T03:49:25Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1076 is 75% complete (~6h remaining), with the cluster processing ~1,832 TPS (1,832 non-vote). Measured slot time is 214ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $588.6K of Real Economic Value over the last 24h ($409/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $90.68 (-1.5% / 24h). Decentralization: Nakamoto coefficient 18, 666 active validators, 0.4% of stake delinquent. Alpenglow readiness: validators holding 100% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 1 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 465,156,596 |
| Block height | 443,177,177 |
| Epoch | 1076 (75.14% complete, ~6.4h left) |
| TPS (10 min avg) | 1,832 |
| Non-vote TPS | 1,832 |
| Slot time (measured) | 214.5 ms |
| Confirmation time (measured) | 0.21 s |
| Finality time (measured) | 0.21 s — **Alpenglow active** |
| Est. daily transactions | 190,612,103 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0025 |
| Node version | 4.4.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $90.68 (-1.5%/24h) |
| Market cap | $53.5B |
| **REV (24h)** | **$588.6K** (fees $479.8K + Jito tips $108.8K) |
| Chain TVL | $5.4B |
| Stablecoin supply | $14.8B |
| DEX volume (24h) | $1.9B (1.1%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 590,206,751 SOL |
| Inflation | 3.57% |

Top DEXs by 24h volume: PumpSwap ($321.8M), BisonFi ($250.5M), Orca DEX ($193.6M), Raydium AMM ($152.4M), Tessera V ($149.8M)

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
| community | 69.0 |
| fear greed | 34 |
| momentum | 33.6 |
| news | 74 |

Crypto Fear & Greed: 34 (Fear) · CoinGecko votes bullish: 68.97% · headline tone (48h): +3

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 943 |
| Raydium AMM v4 | 418 |
| Orca Whirlpool | 1,500 |
| Pump.fun | 1,500 |
| Tensor | 0 |
| Magic Eden v2 | 579 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,300,003 |
| Binance (cold) | 4 |
| OKX (attributed) | 339,402 |
| Coinbase (hot) | 21,261 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 214ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 100.0% of stake.
- **Agave**: latest release v4.4.0 · running 4.4.0 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 14016 ms |
| solana_rpc_validators | OK | 690 ms |
| coingecko | OK | 1693 ms |
| defillama_tvl | OK | 824 ms |
| defillama_dex | OK | 832 ms |
| defillama_fees | OK | 1642 ms |
| defillama_stablecoins | OK | 980 ms |
| defillama_xstocks | FAILED | 652 ms |
| jito_kobe | OK | 264 ms |
| stakewiz | OK | 1016 ms |
| github | OK | 817 ms |
| solana_com_news | FAILED | 115 ms |
| sentiment | OK | 2483 ms |
| solana_status_page | OK | 255 ms |
| solana_rpc_whales | OK | 1169 ms |
| solana_rpc_programs | OK | 2050 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*