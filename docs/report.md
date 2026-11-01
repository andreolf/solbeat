# Solbeat — State of the Solana Network

> Generated 2026-11-01T23:59:25Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1074 is 74% complete (~7h remaining), with the cluster processing ~1,896 TPS (1,896 non-vote). Measured slot time is 212ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $438.5K of Real Economic Value over the last 24h ($304/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $94.49 (-1.0% / 24h). Decentralization: Nakamoto coefficient 18, 662 active validators, 1.1% of stake delinquent. Alpenglow readiness: validators holding 100% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 2 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 464,285,571 |
| Block height | 442,307,002 |
| Epoch | 1074 (73.51% complete, ~6.8h left) |
| TPS (10 min avg) | 1,896 |
| Non-vote TPS | 1,896 |
| Slot time (measured) | 212.5 ms |
| Confirmation time (measured) | 0.21 s |
| Finality time (measured) | 0.21 s — **Alpenglow active** |
| Est. daily transactions | 172,266,313 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0021 |
| Node version | 4.3.2 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $94.49 (-1.0%/24h) |
| Market cap | $55.8B |
| **REV (24h)** | **$438.5K** (fees $364.2K + Jito tips $74.2K) |
| Chain TVL | $5.4B |
| Stablecoin supply | $15.4B |
| DEX volume (24h) | $953.6M (-55.0%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 590,150,217 SOL |
| Inflation | 3.58% |

Top DEXs by 24h volume: PumpSwap ($130.7M), pump.fun ($103.8M), Orca DEX ($92.1M), GoonFi ($73.9M), Tessera V ($70.3M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 662 / 34 |
| Delinquent stake | 1.05% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.7% |
| Avg / median commission | 13.1% / 5.0% |
| Alpenglow BLS-key readiness | 678 validators, 100.0% of stake |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L43ZWjwCHART3o…` | 17,029,196 | 3.92% | 7% |
| 2 | `he1iusunGwqrNtafDtLd…` | 16,695,127 | 3.85% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5…` | 12,943,199 | 2.98% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxb…` | 10,426,987 | 2.4% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxA…` | 9,583,157 | 2.21% | 5% |
| 6 | `51JBzSTU5rAM8gLAVQKg…` | 9,451,197 | 2.18% | 10% |
| 7 | `26pV97Ce83ZQ6Kz9XT4t…` | 9,225,053 | 2.13% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2Fp…` | 7,791,639 | 1.8% | 7% |
| 9 | `DumiCKHVqoCQKD8roLAp…` | 7,001,293 | 1.61% | 0% |
| 10 | `CvSb7wdQAFpHuSpTYTJn…` | 6,977,108 | 1.61% | 5% |

## Signals (anomaly detection)

- **[WARNING]** DEX volume contraction (z=-2.0 vs its recent baseline)
- **[WARNING]** Real Economic Value deviating from its run-history baseline (z=-2.2)

## Solana Pulse — sentiment (experimental)

**45/100 — Neutral** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 69.7 |
| fear greed | 34 |
| momentum | 22.6 |
| news | 58 |

Crypto Fear & Greed: 34 (Fear) · CoinGecko votes bullish: 69.7% · headline tone (48h): +1

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 732 |
| Raydium AMM v4 | 732 |
| Orca Whirlpool | 732 |
| Pump.fun | 1,500 |
| Tensor | 0 |
| Magic Eden v2 | 88 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,890,003 |
| Binance (cold) | 4 |
| OKX (attributed) | 339,502 |
| Coinbase (hot) | 46,025 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 212ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 100.0% of stake.
- **Agave**: latest release v4.4.0 · running 4.3.2 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 13900 ms |
| solana_rpc_validators | OK | 428 ms |
| coingecko | OK | 1745 ms |
| defillama_tvl | OK | 231 ms |
| defillama_dex | OK | 123 ms |
| defillama_fees | OK | 1501 ms |
| defillama_stablecoins | OK | 284 ms |
| defillama_xstocks | FAILED | 621 ms |
| jito_kobe | OK | 360 ms |
| stakewiz | OK | 1004 ms |
| github | OK | 750 ms |
| solana_com_news | FAILED | 83 ms |
| sentiment | OK | 2401 ms |
| solana_status_page | OK | 284 ms |
| solana_rpc_whales | OK | 1149 ms |
| solana_rpc_programs | OK | 2231 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*