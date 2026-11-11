# Solbeat — State of the Solana Network

> Generated 2026-11-11T15:01:10Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1083 is 72% complete (~7h remaining), with the cluster processing ~2,000 TPS (2,000 non-vote). Measured slot time is 214ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $563.3K of Real Economic Value over the last 24h ($391/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $84.03 (-0.3% / 24h). Decentralization: Nakamoto coefficient 18, 659 active validators, 0.2% of stake delinquent. Alpenglow readiness: validators holding 100% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 2 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 468,166,037 |
| Block height | 446,182,355 |
| Epoch | 1083 (71.77% complete, ~7.3h left) |
| TPS (10 min avg) | 2,000 |
| Non-vote TPS | 2,000 |
| Slot time (measured) | 214.0 ms |
| Confirmation time (measured) | 0.21 s |
| Finality time (measured) | 0.21 s — **Alpenglow active** |
| Est. daily transactions | 125,400,489 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0035 |
| Node version | 4.4.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $84.03 (-0.3%/24h) |
| Market cap | $49.7B |
| **REV (24h)** | **$563.3K** (fees $444.5K + Jito tips $118.8K) |
| Chain TVL | $5.1B |
| Stablecoin supply | $14.7B |
| DEX volume (24h) | $1.3B (-9.8%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 591,408,364 SOL |
| Inflation | 3.56% |

Top DEXs by 24h volume: Orca DEX ($230.4M), BisonFi ($152.6M), Meteora DLMM ($129.4M), Raydium AMM ($112.1M), PumpSwap ($94.4M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 659 / 40 |
| Delinquent stake | 0.22% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.6% |
| Avg / median commission | 12.8% / 5% |
| Alpenglow BLS-key readiness | 685 validators, 100.0% of stake |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `he1iusunGwqrNtafDtLd…` | 16,764,485 | 3.87% | 0% |
| 2 | `CcaHc2L43ZWjwCHART3o…` | 16,564,685 | 3.82% | 7% |
| 3 | `3N7s9zXMZ4QqvHQR15t5…` | 13,031,625 | 3.01% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxb…` | 10,117,254 | 2.33% | 0% |
| 5 | `51JBzSTU5rAM8gLAVQKg…` | 9,644,051 | 2.23% | 10% |
| 6 | `CatzoSMUkTRidT5DwBxA…` | 9,571,015 | 2.21% | 5% |
| 7 | `26pV97Ce83ZQ6Kz9XT4t…` | 9,231,999 | 2.13% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2Fp…` | 7,814,330 | 1.8% | 7% |
| 9 | `DumiCKHVqoCQKD8roLAp…` | 6,987,248 | 1.61% | 0% |
| 10 | `CvSb7wdQAFpHuSpTYTJn…` | 6,729,845 | 1.55% | 5% |

## Signals (anomaly detection)

- **[WARNING]** SOL price contraction (z=-2.1 vs its recent baseline)
- **[WARNING]** Stablecoin supply contraction (z=-2.8 vs its recent baseline)

## Solana Pulse — sentiment (experimental)

**48/100 — Neutral** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 78.7 |
| fear greed | 29 |
| momentum | 26.9 |
| news | 58 |

Crypto Fear & Greed: 29 (Fear) · CoinGecko votes bullish: 78.72% · headline tone (48h): +1

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 966 |
| Raydium AMM v4 | 966 |
| Orca Whirlpool | 966 |
| Pump.fun | 1,500 |
| Tensor | 0 |
| Magic Eden v2 | 51 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,300,003 |
| Binance (cold) | 66 |
| OKX (attributed) | 97,640 |
| Coinbase (hot) | 22,318 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 214ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 100.0% of stake.
- **Agave**: latest release v4.4.1 · running 4.4.0 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 9372 ms |
| solana_rpc_validators | OK | 191 ms |
| coingecko | OK | 1839 ms |
| defillama_tvl | OK | 258 ms |
| defillama_dex | OK | 1140 ms |
| defillama_fees | OK | 136 ms |
| defillama_stablecoins | OK | 129 ms |
| defillama_xstocks | FAILED | 62 ms |
| jito_kobe | OK | 153 ms |
| stakewiz | OK | 1381 ms |
| github | OK | 1200 ms |
| solana_com_news | FAILED | 92 ms |
| sentiment | OK | 2282 ms |
| solana_status_page | OK | 254 ms |
| solana_rpc_whales | OK | 1124 ms |
| solana_rpc_programs | OK | 1640 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*