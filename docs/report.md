# Solbeat — State of the Solana Network

> Generated 2026-11-23T17:31:39Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1094 is 97% complete (~1h remaining), with the cluster processing ~2,906 TPS (2,906 non-vote). Measured slot time is 216ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $364.9K of Real Economic Value over the last 24h ($253/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $73.92 (+5.1% / 24h). Decentralization: Nakamoto coefficient 18, 661 active validators, 0.0% of stake delinquent. Alpenglow readiness: validators holding 100% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 1 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 473,027,224 |
| Block height | 451,040,544 |
| Epoch | 1094 (97.04% complete, ~0.8h left) |
| TPS (10 min avg) | 2,906 |
| Non-vote TPS | 2,906 |
| Slot time (measured) | 215.8 ms |
| Confirmation time (measured) | 0.22 s |
| Finality time (measured) | 0.22 s — **Alpenglow active** |
| Est. daily transactions | 261,705,899 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0011 |
| Node version | 4.4.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $73.92 (+5.1%/24h) |
| Market cap | $43.8B |
| **REV (24h)** | **$364.9K** (fees $287.1K + Jito tips $77.8K) |
| Chain TVL | $4.7B |
| Stablecoin supply | $13.3B |
| DEX volume (24h) | $975.7M (-27.5%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 592,016,570 SOL |
| Inflation | 3.54% |

Top DEXs by 24h volume: Raydium AMM ($178.4M), Orca DEX ($134.0M), BisonFi ($115.0M), PumpSwap ($109.8M), Scorch ($93.2M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 661 / 24 |
| Delinquent stake | 0.01% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 25.0% |
| Avg / median commission | 13.1% / 5% |
| Alpenglow BLS-key readiness | 670 validators, 100.0% of stake |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `he1iusunGwqrNtafDtLd…` | 16,918,440 | 3.97% | 0% |
| 2 | `CcaHc2L43ZWjwCHART3o…` | 16,346,959 | 3.84% | 7% |
| 3 | `3N7s9zXMZ4QqvHQR15t5…` | 12,401,889 | 2.91% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxb…` | 10,243,005 | 2.41% | 0% |
| 5 | `51JBzSTU5rAM8gLAVQKg…` | 9,842,253 | 2.31% | 10% |
| 6 | `CatzoSMUkTRidT5DwBxA…` | 9,612,896 | 2.26% | 5% |
| 7 | `26pV97Ce83ZQ6Kz9XT4t…` | 9,269,555 | 2.18% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2Fp…` | 7,998,895 | 1.88% | 7% |
| 9 | `DumiCKHVqoCQKD8roLAp…` | 6,987,495 | 1.64% | 0% |
| 10 | `CvSb7wdQAFpHuSpTYTJn…` | 6,775,083 | 1.59% | 5% |

## Signals (anomaly detection)

- **[WARNING]** Stablecoin supply contraction (z=-2.7 vs its recent baseline)

## Solana Pulse — sentiment (experimental)

**39/100 — Bearish** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 63.0 |
| fear greed | 11 |
| momentum | 41.0 |
| news | 34 |

Crypto Fear & Greed: 11 (Extreme Fear) · CoinGecko votes bullish: 63.04% · headline tone (48h): -2

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 1,500 |
| Raydium AMM v4 | 751 |
| Orca Whirlpool | 1,500 |
| Pump.fun | 1,500 |
| Tensor | 0 |
| Magic Eden v2 | 43 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,300,003 |
| Binance (cold) | 66 |
| OKX (attributed) | 120,894 |
| Coinbase (hot) | 21,815 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 216ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 100.0% of stake.
- **Agave**: latest release v4.4.1 · running 4.4.0 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 9714 ms |
| solana_rpc_validators | OK | 119 ms |
| coingecko | OK | 1668 ms |
| defillama_tvl | OK | 462 ms |
| defillama_dex | OK | 99 ms |
| defillama_fees | OK | 1417 ms |
| defillama_stablecoins | OK | 311 ms |
| defillama_xstocks | FAILED | 668 ms |
| jito_kobe | OK | 210 ms |
| stakewiz | OK | 1037 ms |
| github | OK | 635 ms |
| solana_com_news | FAILED | 48 ms |
| sentiment | OK | 2253 ms |
| solana_status_page | OK | 144 ms |
| solana_rpc_whales | OK | 1548 ms |
| solana_rpc_programs | OK | 1848 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*