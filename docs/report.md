# Solbeat — State of the Solana Network

> Generated 2026-11-02T03:34:20Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1074 is 87% complete (~3h remaining), with the cluster processing ~1,897 TPS (1,897 non-vote). Measured slot time is 214ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $442.1K of Real Economic Value over the last 24h ($307/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $95.44 (-0.1% / 24h). Decentralization: Nakamoto coefficient 18, 662 active validators, 1.1% of stake delinquent. Alpenglow readiness: validators holding 100% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 2 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 464,345,727 |
| Block height | 442,367,114 |
| Epoch | 1074 (87.44% complete, ~3.2h left) |
| TPS (10 min avg) | 1,897 |
| Non-vote TPS | 1,897 |
| Slot time (measured) | 214.2 ms |
| Confirmation time (measured) | 0.21 s |
| Finality time (measured) | 0.21 s — **Alpenglow active** |
| Est. daily transactions | 153,924,273 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0024 |
| Node version | 4.3.2 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $95.44 (-0.1%/24h) |
| Market cap | $56.3B |
| **REV (24h)** | **$442.1K** (fees $367.7K + Jito tips $74.4K) |
| Chain TVL | $5.5B |
| Stablecoin supply | $15.4B |
| DEX volume (24h) | $832.7M (-12.7%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 590,150,156 SOL |
| Inflation | 3.58% |

Top DEXs by 24h volume: PumpSwap ($122.9M), pump.fun ($103.8M), Orca DEX ($94.5M), GoonFi ($73.9M), Tessera V ($70.3M)

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

- **[WARNING]** DEX volume contraction (z=-2.1 vs its recent baseline)
- **[WARNING]** Real Economic Value deviating from its run-history baseline (z=-2.1)

## Solana Pulse — sentiment (experimental)

**49/100 — Neutral** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 69.0 |
| fear greed | 37 |
| momentum | 34.7 |
| news | 58 |

Crypto Fear & Greed: 37 (Fear) · CoinGecko votes bullish: 68.97% · headline tone (48h): +1

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 916 |
| Raydium AMM v4 | 324 |
| Orca Whirlpool | 916 |
| Pump.fun | 1,500 |
| Tensor | 0 |
| Magic Eden v2 | 52 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,890,003 |
| Binance (cold) | 4 |
| OKX (attributed) | 339,502 |
| Coinbase (hot) | 45,507 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 214ms.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 100.0% of stake.
- **Agave**: latest release None · running 4.3.2 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 9457 ms |
| solana_rpc_validators | OK | 257 ms |
| coingecko | OK | 1656 ms |
| defillama_tvl | OK | 104 ms |
| defillama_dex | OK | 1200 ms |
| defillama_fees | OK | 2050 ms |
| defillama_stablecoins | OK | 1330 ms |
| defillama_xstocks | FAILED | 837 ms |
| jito_kobe | OK | 150 ms |
| stakewiz | OK | 1087 ms |
| github | FAILED | 6187 ms |
| solana_com_news | FAILED | 29 ms |
| sentiment | OK | 2248 ms |
| solana_status_page | OK | 370 ms |
| solana_rpc_whales | OK | 1530 ms |
| solana_rpc_programs | OK | 1956 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*