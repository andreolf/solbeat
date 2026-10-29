# Solbeat — State of the Solana Network

> Generated 2026-10-29T13:50:37Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1071 is 54% complete (~12h remaining), with the cluster processing ~2,084 TPS (2,084 non-vote). Measured slot time is 214ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $657.3K of Real Economic Value over the last 24h ($456/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $100.34 (-0.5% / 24h). Decentralization: Nakamoto coefficient 18, 665 active validators, 0.8% of stake delinquent. Alpenglow readiness: validators holding 100% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 1 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 462,904,114 |
| Block height | 440,927,531 |
| Epoch | 1071 (53.73% complete, ~11.9h left) |
| TPS (10 min avg) | 2,084 |
| Non-vote TPS | 2,084 |
| Slot time (measured) | 214.2 ms |
| Confirmation time (measured) | 0.21 s |
| Finality time (measured) | 0.21 s — **Alpenglow active** |
| Est. daily transactions | 118,018,348 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0045 |
| Node version | 4.3.2 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $100.34 (-0.5%/24h) |
| Market cap | $59.2B |
| **REV (24h)** | **$657.3K** (fees $527.1K + Jito tips $130.1K) |
| Chain TVL | $5.6B |
| Stablecoin supply | $15.6B |
| DEX volume (24h) | $1.7B (9.5%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 589,983,783 SOL |
| Inflation | 3.58% |

Top DEXs by 24h volume: Orca DEX ($246.1M), BisonFi ($205.5M), Manifest Trade ($157.9M), Tessera V ($148.2M), Raydium AMM ($144.6M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 665 / 24 |
| Delinquent stake | 0.79% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.5% |
| Avg / median commission | 13.1% / 5% |
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

- **[WARNING]** TPS spike: 2,084 vs 12h mean 1,350 (z=+2.3)

## Solana Pulse — sentiment (experimental)

**60/100 — Bullish** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 87.5 |
| fear greed | 51 |
| momentum | 45.9 |
| news | 50 |

Crypto Fear & Greed: 51 (Neutral) · CoinGecko votes bullish: 87.5% · headline tone (48h): +0

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 1,500 |
| Raydium AMM v4 | 1,500 |
| Orca Whirlpool | 1,500 |
| Pump.fun | 1,500 |
| Tensor | 0 |
| Magic Eden v2 | 441 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 11,734,974 |
| Binance (cold) | 1,021,040 |
| OKX (attributed) | 330,876 |
| Coinbase (hot) | 15,506 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 214ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 100.0% of stake.
- **Agave**: latest release v4.4.0 · running 4.3.2 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 15264 ms |
| solana_rpc_validators | OK | 239 ms |
| coingecko | OK | 1748 ms |
| defillama_tvl | OK | 130 ms |
| defillama_dex | OK | 1179 ms |
| defillama_fees | OK | 1527 ms |
| defillama_stablecoins | OK | 182 ms |
| defillama_xstocks | FAILED | 259 ms |
| jito_kobe | OK | 183 ms |
| stakewiz | OK | 1411 ms |
| github | OK | 1024 ms |
| solana_com_news | FAILED | 143 ms |
| sentiment | OK | 2324 ms |
| solana_status_page | OK | 291 ms |
| solana_rpc_whales | OK | 1038 ms |
| solana_rpc_programs | OK | 8631 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*