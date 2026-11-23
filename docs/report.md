# Solbeat — State of the Solana Network

> Generated 2026-11-23T21:42:18Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1095 is 13% complete (~22h remaining), with the cluster processing ~1,906 TPS (1,906 non-vote). Measured slot time is 215ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $395.5K of Real Economic Value over the last 24h ($275/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $72.46 (+3.0% / 24h). Decentralization: Nakamoto coefficient 18, 659 active validators, 0.1% of stake delinquent. Alpenglow readiness: validators holding 100% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 1 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 473,097,184 |
| Block height | 451,110,458 |
| Epoch | 1095 (13.24% complete, ~22.4h left) |
| TPS (10 min avg) | 1,906 |
| Non-vote TPS | 1,906 |
| Slot time (measured) | 215.2 ms |
| Confirmation time (measured) | 0.22 s |
| Finality time (measured) | 0.22 s — **Alpenglow active** |
| Est. daily transactions | 202,210,107 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0014 |
| Node version | 4.4.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $72.46 (+3.0%/24h) |
| Market cap | $42.9B |
| **REV (24h)** | **$395.5K** (fees $287.1K + Jito tips $108.4K) |
| Chain TVL | $4.7B |
| Stablecoin supply | $13.3B |
| DEX volume (24h) | $975.7M (-27.5%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 592,071,910 SOL |
| Inflation | 3.54% |

Top DEXs by 24h volume: Orca DEX ($219.4M), Raydium AMM ($205.7M), Manifest Trade ($116.4M), BisonFi ($115.0M), PumpSwap ($109.8M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 659 / 27 |
| Delinquent stake | 0.11% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 25.0% |
| Avg / median commission | 12.8% / 5% |
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

- **[WARNING]** Stablecoin supply contraction (z=-2.7 vs its recent baseline)

## Solana Pulse — sentiment (experimental)

**42/100 — Neutral** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 70.2 |
| fear greed | 11 |
| momentum | 38.3 |
| news | 42 |

Crypto Fear & Greed: 11 (Extreme Fear) · CoinGecko votes bullish: 70.21% · headline tone (48h): -1

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 1,500 |
| Raydium AMM v4 | 834 |
| Orca Whirlpool | 1,500 |
| Pump.fun | 1,500 |
| Tensor | 0 |
| Magic Eden v2 | 33 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,300,003 |
| Binance (cold) | 66 |
| OKX (attributed) | 120,894 |
| Coinbase (hot) | 18,457 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 215ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 100.0% of stake.
- **Agave**: latest release v4.4.1 · running 4.4.0 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 15537 ms |
| solana_rpc_validators | OK | 523 ms |
| coingecko | OK | 1705 ms |
| defillama_tvl | OK | 222 ms |
| defillama_dex | OK | 65 ms |
| defillama_fees | OK | 701 ms |
| defillama_stablecoins | OK | 273 ms |
| defillama_xstocks | FAILED | 30 ms |
| jito_kobe | OK | 99 ms |
| stakewiz | OK | 1220 ms |
| github | OK | 708 ms |
| solana_com_news | FAILED | 58 ms |
| sentiment | OK | 2078 ms |
| solana_status_page | OK | 212 ms |
| solana_rpc_whales | OK | 3880 ms |
| solana_rpc_programs | OK | 8179 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*