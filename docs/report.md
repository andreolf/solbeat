# Solbeat — State of the Solana Network

> Generated 2026-11-09T02:14:14Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1081 is 36% complete (~17h remaining), with the cluster processing ~1,510 TPS (1,510 non-vote). Measured slot time is 214ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $511.5K of Real Economic Value over the last 24h ($355/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $87.92 (-1.1% / 24h). Decentralization: Nakamoto coefficient 18, 661 active validators, 0.1% of stake delinquent. Alpenglow readiness: validators holding 100% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 1 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 467,145,910 |
| Block height | 445,164,011 |
| Epoch | 1081 (35.63% complete, ~16.6h left) |
| TPS (10 min avg) | 1,510 |
| Non-vote TPS | 1,510 |
| Slot time (measured) | 214.3 ms |
| Confirmation time (measured) | 0.21 s |
| Finality time (measured) | 0.21 s — **Alpenglow active** |
| Est. daily transactions | 153,228,413 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0027 |
| Node version | 4.4.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $87.92 (-1.1%/24h) |
| Market cap | $52.0B |
| **REV (24h)** | **$511.5K** (fees $408.0K + Jito tips $103.4K) |
| Chain TVL | $5.1B |
| Stablecoin supply | $15.0B |
| DEX volume (24h) | $995.3M (8.5%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 591,093,747 SOL |
| Inflation | 3.57% |

Top DEXs by 24h volume: PumpSwap ($165.3M), Orca DEX ($160.7M), Raydium AMM ($125.2M), pump.fun ($87.5M), BisonFi ($80.2M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 661 / 36 |
| Delinquent stake | 0.14% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.6% |
| Avg / median commission | 12.9% / 5% |
| Alpenglow BLS-key readiness | 685 validators, 100.0% of stake |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L43ZWjwCHART3o…` | 17,050,553 | 3.93% | 7% |
| 2 | `he1iusunGwqrNtafDtLd…` | 16,720,131 | 3.85% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5…` | 13,021,912 | 3.0% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxb…` | 10,279,070 | 2.37% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxA…` | 9,553,388 | 2.2% | 5% |
| 6 | `51JBzSTU5rAM8gLAVQKg…` | 9,550,278 | 2.2% | 10% |
| 7 | `26pV97Ce83ZQ6Kz9XT4t…` | 9,222,876 | 2.13% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2Fp…` | 7,775,137 | 1.79% | 7% |
| 9 | `DumiCKHVqoCQKD8roLAp…` | 6,980,319 | 1.61% | 0% |
| 10 | `CvSb7wdQAFpHuSpTYTJn…` | 6,711,284 | 1.55% | 5% |

## Signals (anomaly detection)

- **[WARNING]** Stablecoin supply contraction (z=-2.4 vs its recent baseline)

## Solana Pulse — sentiment (experimental)

**49/100 — Neutral** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 64.3 |
| fear greed | 29 |
| momentum | 43.3 |
| news | 66 |

Crypto Fear & Greed: 29 (Fear) · CoinGecko votes bullish: 64.29% · headline tone (48h): +2

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 761 |
| Raydium AMM v4 | 505 |
| Orca Whirlpool | 1,500 |
| Pump.fun | 1,500 |
| Tensor | 0 |
| Magic Eden v2 | 32 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,300,003 |
| Binance (cold) | 66 |
| OKX (attributed) | 97,596 |
| Coinbase (hot) | 25,993 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 214ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 100.0% of stake.
- **Agave**: latest release v4.4.1 · running 4.4.0 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 10037 ms |
| solana_rpc_validators | OK | 331 ms |
| coingecko | OK | 1759 ms |
| defillama_tvl | OK | 1076 ms |
| defillama_dex | OK | 1128 ms |
| defillama_fees | OK | 1936 ms |
| defillama_stablecoins | OK | 96 ms |
| defillama_xstocks | FAILED | 66 ms |
| jito_kobe | OK | 130 ms |
| stakewiz | OK | 1484 ms |
| github | OK | 682 ms |
| solana_com_news | FAILED | 93 ms |
| sentiment | OK | 2422 ms |
| solana_status_page | OK | 265 ms |
| solana_rpc_whales | OK | 1288 ms |
| solana_rpc_programs | OK | 2109 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*