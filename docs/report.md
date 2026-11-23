# Solbeat — State of the Solana Network

> Generated 2026-11-23T18:32:34Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1095 is 1% complete (~26h remaining), with the cluster processing ~2,082 TPS (2,082 non-vote). Measured slot time is 215ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $364.9K of Real Economic Value over the last 24h ($253/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $73.53 (+4.7% / 24h). Decentralization: Nakamoto coefficient 18, 661 active validators, 0.0% of stake delinquent. Alpenglow readiness: validators holding 100% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 1 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 473,044,247 |
| Block height | 451,057,559 |
| Epoch | 1095 (0.98% complete, ~25.5h left) |
| TPS (10 min avg) | 2,082 |
| Non-vote TPS | 2,082 |
| Slot time (measured) | 214.6 ms |
| Confirmation time (measured) | 0.21 s |
| Finality time (measured) | 0.21 s — **Alpenglow active** |
| Est. daily transactions | 237,860,895 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0012 |
| Node version | 4.4.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $73.53 (+4.7%/24h) |
| Market cap | $43.5B |
| **REV (24h)** | **$364.9K** (fees $287.1K + Jito tips $77.8K) |
| Chain TVL | $4.7B |
| Stablecoin supply | $13.3B |
| DEX volume (24h) | $975.7M (-27.5%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 592,072,193 SOL |
| Inflation | 3.54% |

Top DEXs by 24h volume: Orca DEX ($219.4M), Raydium AMM ($201.5M), BisonFi ($115.0M), PumpSwap ($109.8M), Scorch ($93.2M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 661 / 25 |
| Delinquent stake | 0.01% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 25.0% |
| Avg / median commission | 12.9% / 5% |
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

**39/100 — Bearish** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 63.8 |
| fear greed | 11 |
| momentum | 40.0 |
| news | 34 |

Crypto Fear & Greed: 11 (Extreme Fear) · CoinGecko votes bullish: 63.83% · headline tone (48h): -2

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 1,500 |
| Raydium AMM v4 | 868 |
| Orca Whirlpool | 1,500 |
| Pump.fun | 1,500 |
| Tensor | 0 |
| Magic Eden v2 | 21 |
| Marinade | 3 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,300,003 |
| Binance (cold) | 66 |
| OKX (attributed) | 120,894 |
| Coinbase (hot) | 21,434 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 215ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 100.0% of stake.
- **Agave**: latest release v4.4.1 · running 4.4.0 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 16336 ms |
| solana_rpc_validators | OK | 182 ms |
| coingecko | OK | 1981 ms |
| defillama_tvl | OK | 151 ms |
| defillama_dex | OK | 69 ms |
| defillama_fees | OK | 85 ms |
| defillama_stablecoins | OK | 210 ms |
| defillama_xstocks | FAILED | 172 ms |
| jito_kobe | OK | 311 ms |
| stakewiz | OK | 1041 ms |
| github | OK | 635 ms |
| solana_com_news | FAILED | 153 ms |
| sentiment | OK | 2155 ms |
| solana_status_page | OK | 228 ms |
| solana_rpc_whales | OK | 1194 ms |
| solana_rpc_programs | OK | 1864 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*