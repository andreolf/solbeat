# Solbeat — State of the Solana Network

> Generated 2026-11-24T13:00:19Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1095 is 73% complete (~7h remaining), with the cluster processing ~1,259 TPS (1,259 non-vote). Measured slot time is 215ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $529.8K of Real Economic Value over the last 24h ($368/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $70.63 (-2.1% / 24h). Decentralization: Nakamoto coefficient 18, 660 active validators, 0.0% of stake delinquent. Alpenglow readiness: validators holding 100% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 1 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 473,353,289 |
| Block height | 451,366,423 |
| Epoch | 1095 (72.52% complete, ~7.1h left) |
| TPS (10 min avg) | 1,259 |
| Non-vote TPS | 1,259 |
| Slot time (measured) | 215.1 ms |
| Confirmation time (measured) | 0.22 s |
| Finality time (measured) | 0.22 s — **Alpenglow active** |
| Est. daily transactions | 128,909,387 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0033 |
| Node version | 4.4.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $70.63 (-2.1%/24h) |
| Market cap | $41.8B |
| **REV (24h)** | **$529.8K** (fees $424.1K + Jito tips $105.7K) |
| Chain TVL | $4.6B |
| Stablecoin supply | $13.8B |
| DEX volume (24h) | $1.8B (85.1%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 592,071,669 SOL |
| Inflation | 3.54% |

Top DEXs by 24h volume: Orca DEX ($271.7M), BisonFi ($204.1M), Meteora DLMM ($166.9M), Raydium AMM ($163.2M), Scorch ($159.2M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 660 / 26 |
| Delinquent stake | 0.04% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 25.0% |
| Avg / median commission | 13.1% / 5.0% |
| Alpenglow BLS-key readiness | 670 validators, 100.0% of stake |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `he1iusunGwqrNtafDtLd…` | 17,028,046 | 4.0% | 0% |
| 2 | `CcaHc2L43ZWjwCHART3o…` | 16,091,420 | 3.78% | 7% |
| 3 | `3N7s9zXMZ4QqvHQR15t5…` | 12,412,158 | 2.91% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxb…` | 10,240,508 | 2.4% | 0% |
| 5 | `51JBzSTU5rAM8gLAVQKg…` | 9,856,366 | 2.31% | 10% |
| 6 | `CatzoSMUkTRidT5DwBxA…` | 9,634,022 | 2.26% | 5% |
| 7 | `26pV97Ce83ZQ6Kz9XT4t…` | 9,276,354 | 2.18% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2Fp…` | 8,005,660 | 1.88% | 7% |
| 9 | `DumiCKHVqoCQKD8roLAp…` | 6,987,776 | 1.64% | 0% |
| 10 | `CvSb7wdQAFpHuSpTYTJn…` | 6,778,434 | 1.59% | 5% |

## Signals (anomaly detection)

- **[WARNING]** Solana TVL contraction (z=-2.2 vs its recent baseline)

## Solana Pulse — sentiment (experimental)

**41/100 — Neutral** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 57.5 |
| fear greed | 11 |
| momentum | 56.1 |
| news | 26 |

Crypto Fear & Greed: 11 (Extreme Fear) · CoinGecko votes bullish: 57.5% · headline tone (48h): -3

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 748 |
| Raydium AMM v4 | 499 |
| Orca Whirlpool | 748 |
| Pump.fun | 1,500 |
| Tensor | 0 |
| Magic Eden v2 | 18 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,300,003 |
| Binance (cold) | 66 |
| OKX (attributed) | 95,407 |
| Coinbase (hot) | 57,611 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 215ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 100.0% of stake.
- **Agave**: latest release v4.4.1 · running 4.4.0 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 9823 ms |
| solana_rpc_validators | OK | 195 ms |
| coingecko | OK | 2602 ms |
| defillama_tvl | OK | 944 ms |
| defillama_dex | OK | 1130 ms |
| defillama_fees | OK | 128 ms |
| defillama_stablecoins | OK | 1454 ms |
| defillama_xstocks | FAILED | 46 ms |
| jito_kobe | OK | 283 ms |
| stakewiz | OK | 1321 ms |
| github | OK | 1030 ms |
| solana_com_news | FAILED | 102 ms |
| sentiment | OK | 2344 ms |
| solana_status_page | OK | 504 ms |
| solana_rpc_whales | OK | 985 ms |
| solana_rpc_programs | OK | 1857 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*