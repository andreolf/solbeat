# Solbeat — State of the Solana Network

> Generated 2026-10-29T12:19:10Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1071 is 48% complete (~13h remaining), with the cluster processing ~1,762 TPS (1,762 non-vote). Measured slot time is 213ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $657.6K of Real Economic Value over the last 24h ($457/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $100.21 (-1.8% / 24h). Decentralization: Nakamoto coefficient 18, 664 active validators, 0.8% of stake delinquent. Alpenglow readiness: validators holding 100% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 1 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 462,878,453 |
| Block height | 440,901,904 |
| Epoch | 1071 (47.79% complete, ~13.4h left) |
| TPS (10 min avg) | 1,762 |
| Non-vote TPS | 1,762 |
| Slot time (measured) | 213.3 ms |
| Confirmation time (measured) | 0.21 s |
| Finality time (measured) | 0.21 s — **Alpenglow active** |
| Est. daily transactions | 108,736,770 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0048 |
| Node version | 4.3.2 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $100.21 (-1.8%/24h) |
| Market cap | $59.1B |
| **REV (24h)** | **$657.6K** (fees $527.1K + Jito tips $130.5K) |
| Chain TVL | $5.6B |
| Stablecoin supply | $15.6B |
| DEX volume (24h) | $1.7B (9.5%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 589,983,810 SOL |
| Inflation | 3.58% |

Top DEXs by 24h volume: Orca DEX ($248.0M), BisonFi ($205.5M), Manifest Trade ($159.7M), Tessera V ($148.2M), Raydium AMM ($147.9M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 664 / 25 |
| Delinquent stake | 0.76% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.5% |
| Avg / median commission | 12.8% / 5.0% |
| Alpenglow BLS-key readiness | 679 validators, 100.0% of stake |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L43ZWjwCHART3o…` | 17,028,574 | 3.9% | 7% |
| 2 | `he1iusunGwqrNtafDtLd…` | 16,665,444 | 3.82% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5…` | 12,878,826 | 2.95% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxb…` | 10,762,073 | 2.46% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxA…` | 9,705,356 | 2.22% | 5% |
| 6 | `51JBzSTU5rAM8gLAVQKg…` | 9,466,646 | 2.17% | 10% |
| 7 | `26pV97Ce83ZQ6Kz9XT4t…` | 9,218,110 | 2.11% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2Fp…` | 7,761,555 | 1.78% | 7% |
| 9 | `DumiCKHVqoCQKD8roLAp…` | 6,998,037 | 1.6% | 0% |
| 10 | `CvSb7wdQAFpHuSpTYTJn…` | 6,646,428 | 1.52% | 5% |

## Signals (anomaly detection)

- **[WARNING]** TPS spike: 1,762 vs 12h mean 1,248 (z=+2.4)

## Solana Pulse — sentiment (experimental)

**60/100 — Bullish** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 87.0 |
| fear greed | 51 |
| momentum | 45.9 |
| news | 50 |

Crypto Fear & Greed: 51 (Neutral) · CoinGecko votes bullish: 86.96% · headline tone (48h): +0

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 830 |
| Raydium AMM v4 | 258 |
| Orca Whirlpool | 830 |
| Pump.fun | 1,500 |
| Tensor | 0 |
| Magic Eden v2 | 534 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 11,734,974 |
| Binance (cold) | 993,021 |
| OKX (attributed) | 330,877 |
| Coinbase (hot) | 15,456 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 213ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 100.0% of stake.
- **Agave**: latest release v4.4.0 · running 4.3.2 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 10218 ms |
| solana_rpc_validators | OK | 136 ms |
| coingecko | OK | 1730 ms |
| defillama_tvl | OK | 70 ms |
| defillama_dex | OK | 1163 ms |
| defillama_fees | OK | 1968 ms |
| defillama_stablecoins | OK | 1165 ms |
| defillama_xstocks | FAILED | 47 ms |
| jito_kobe | OK | 136 ms |
| stakewiz | OK | 1376 ms |
| github | OK | 981 ms |
| solana_com_news | FAILED | 93 ms |
| sentiment | OK | 2342 ms |
| solana_status_page | OK | 312 ms |
| solana_rpc_whales | OK | 1367 ms |
| solana_rpc_programs | OK | 1801 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*