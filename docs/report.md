# Solbeat — State of the Solana Network

> Generated 2026-11-25T00:37:49Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1096 is 18% complete (~21h remaining), with the cluster processing ~2,121 TPS (2,121 non-vote). Measured slot time is 215ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $532.4K of Real Economic Value over the last 24h ($370/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $69.61 (-3.2% / 24h). Decentralization: Nakamoto coefficient 18, 660 active validators, 0.0% of stake delinquent. Alpenglow readiness: validators holding 100% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 1 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 473,548,010 |
| Block height | 451,561,122 |
| Epoch | 1096 (17.59% complete, ~21.3h left) |
| TPS (10 min avg) | 2,121 |
| Non-vote TPS | 2,121 |
| Slot time (measured) | 215.2 ms |
| Confirmation time (measured) | 0.22 s |
| Finality time (measured) | 0.22 s — **Alpenglow active** |
| Est. daily transactions | 165,059,501 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0026 |
| Node version | 4.4.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $69.61 (-3.2%/24h) |
| Market cap | $41.2B |
| **REV (24h)** | **$532.4K** (fees $424.1K + Jito tips $108.3K) |
| Chain TVL | $4.5B |
| Stablecoin supply | $13.8B |
| DEX volume (24h) | $1.7B (-8.4%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 592,128,421 SOL |
| Inflation | 3.54% |

Top DEXs by 24h volume: BisonFi ($204.1M), Orca DEX ($200.6M), Meteora DLMM ($166.9M), Scorch ($159.2M), Raydium AMM ($144.0M)

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

**37/100 — Bearish** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 62.1 |
| fear greed | 13 |
| momentum | 34.8 |
| news | 34 |

Crypto Fear & Greed: 13 (Extreme Fear) · CoinGecko votes bullish: 62.07% · headline tone (48h): -2

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 579 |
| Raydium AMM v4 | 943 |
| Orca Whirlpool | 1,500 |
| Pump.fun | 1,500 |
| Tensor | 0 |
| Magic Eden v2 | 70 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,300,003 |
| Binance (cold) | 66 |
| OKX (attributed) | 88,910 |
| Coinbase (hot) | 31,517 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 215ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 100.0% of stake.
- **Agave**: latest release v4.4.1 · running 4.4.0 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 10316 ms |
| solana_rpc_validators | OK | 299 ms |
| coingecko | OK | 1821 ms |
| defillama_tvl | OK | 986 ms |
| defillama_dex | OK | 1140 ms |
| defillama_fees | OK | 146 ms |
| defillama_stablecoins | OK | 166 ms |
| defillama_xstocks | FAILED | 826 ms |
| jito_kobe | OK | 268 ms |
| stakewiz | OK | 779 ms |
| github | OK | 1025 ms |
| solana_com_news | FAILED | 125 ms |
| sentiment | OK | 2356 ms |
| solana_status_page | OK | 281 ms |
| solana_rpc_whales | OK | 919 ms |
| solana_rpc_programs | OK | 1882 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*