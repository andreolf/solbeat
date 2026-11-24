# Solbeat — State of the Solana Network

> Generated 2026-11-24T23:05:46Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1096 is 12% complete (~23h remaining), with the cluster processing ~1,554 TPS (1,554 non-vote). Measured slot time is 214ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $533.4K of Real Economic Value over the last 24h ($370/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $69.85 (-3.0% / 24h). Decentralization: Nakamoto coefficient 18, 660 active validators, 0.0% of stake delinquent. Alpenglow readiness: validators holding 100% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 1 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 473,522,345 |
| Block height | 451,535,463 |
| Epoch | 1096 (11.65% complete, ~22.7h left) |
| TPS (10 min avg) | 1,554 |
| Non-vote TPS | 1,554 |
| Slot time (measured) | 213.8 ms |
| Confirmation time (measured) | 0.21 s |
| Finality time (measured) | 0.21 s — **Alpenglow active** |
| Est. daily transactions | 167,920,376 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0025 |
| Node version | 4.4.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $69.85 (-3.0%/24h) |
| Market cap | $41.4B |
| **REV (24h)** | **$533.4K** (fees $424.1K + Jito tips $109.3K) |
| Chain TVL | $4.5B |
| Stablecoin supply | $13.8B |
| DEX volume (24h) | $1.8B (85.1%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 592,126,871 SOL |
| Inflation | 3.54% |

Top DEXs by 24h volume: Orca DEX ($208.7M), BisonFi ($204.1M), Meteora DLMM ($166.9M), Scorch ($159.2M), Raydium AMM ($153.4M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 660 / 27 |
| Delinquent stake | 0.02% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 25.0% |
| Avg / median commission | 12.9% / 5.0% |
| Alpenglow BLS-key readiness | 670 validators, 100.0% of stake |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `he1iusunGwqrNtafDtLd…` | 17,003,542 | 4.0% | 0% |
| 2 | `CcaHc2L43ZWjwCHART3o…` | 15,962,658 | 3.76% | 7% |
| 3 | `3N7s9zXMZ4QqvHQR15t5…` | 12,418,812 | 2.92% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxb…` | 10,242,949 | 2.41% | 0% |
| 5 | `51JBzSTU5rAM8gLAVQKg…` | 9,885,209 | 2.33% | 10% |
| 6 | `CatzoSMUkTRidT5DwBxA…` | 9,615,269 | 2.26% | 5% |
| 7 | `26pV97Ce83ZQ6Kz9XT4t…` | 9,283,847 | 2.19% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2Fp…` | 8,016,085 | 1.89% | 7% |
| 9 | `DumiCKHVqoCQKD8roLAp…` | 6,968,432 | 1.64% | 0% |
| 10 | `CvSb7wdQAFpHuSpTYTJn…` | 6,779,378 | 1.6% | 5% |

## Signals (anomaly detection)

- **[WARNING]** Solana TVL contraction (z=-2.2 vs its recent baseline)

## Solana Pulse — sentiment (experimental)

**39/100 — Bearish** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 58.6 |
| fear greed | 11 |
| momentum | 52.2 |
| news | 18 |

Crypto Fear & Greed: 11 (Extreme Fear) · CoinGecko votes bullish: 58.62% · headline tone (48h): -4

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 1,500 |
| Raydium AMM v4 | 1,500 |
| Orca Whirlpool | 1,500 |
| Pump.fun | 1,500 |
| Tensor | 0 |
| Magic Eden v2 | 26 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,300,003 |
| Binance (cold) | 66 |
| OKX (attributed) | 88,910 |
| Coinbase (hot) | 34,778 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 214ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 100.0% of stake.
- **Agave**: latest release v4.4.1 · running 4.4.0 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 12235 ms |
| solana_rpc_validators | OK | 218 ms |
| coingecko | OK | 1828 ms |
| defillama_tvl | OK | 80 ms |
| defillama_dex | OK | 414 ms |
| defillama_fees | OK | 111 ms |
| defillama_stablecoins | OK | 80 ms |
| defillama_xstocks | FAILED | 115 ms |
| jito_kobe | OK | 191 ms |
| stakewiz | OK | 927 ms |
| github | OK | 646 ms |
| solana_com_news | FAILED | 49 ms |
| sentiment | OK | 2075 ms |
| solana_status_page | OK | 249 ms |
| solana_rpc_whales | OK | 2063 ms |
| solana_rpc_programs | OK | 3168 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*