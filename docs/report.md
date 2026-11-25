# Solbeat — State of the Solana Network

> Generated 2026-11-25T23:54:18Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1097 is 8% complete (~24h remaining), with the cluster processing ~1,314 TPS (1,314 non-vote). Measured slot time is 215ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $471.6K of Real Economic Value over the last 24h ($328/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $70.41 (+1.1% / 24h). Decentralization: Nakamoto coefficient 18, 655 active validators, 0.1% of stake delinquent. Alpenglow readiness: validators holding 100% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 3 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 473,937,694 |
| Block height | 451,950,625 |
| Epoch | 1097 (7.8% complete, ~23.7h left) |
| TPS (10 min avg) | 1,314 |
| Non-vote TPS | 1,314 |
| Slot time (measured) | 214.6 ms |
| Confirmation time (measured) | 0.21 s |
| Finality time (measured) | 0.21 s — **Alpenglow active** |
| Est. daily transactions | 196,358,902 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0019 |
| Node version | 4.4.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $70.41 (+1.1%/24h) |
| Market cap | $41.7B |
| **REV (24h)** | **$471.6K** (fees $366.0K + Jito tips $105.7K) |
| Chain TVL | $4.6B |
| Stablecoin supply | $13.4B |
| DEX volume (24h) | $1.5B (-19.3%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 592,183,383 SOL |
| Inflation | 3.54% |

Top DEXs by 24h volume: Orca DEX ($211.9M), BisonFi ($190.5M), Raydium AMM ($182.4M), Manifest Trade ($139.7M), Scorch ($134.1M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 655 / 33 |
| Delinquent stake | 0.06% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 25.0% |
| Avg / median commission | 13.0% / 5% |
| Alpenglow BLS-key readiness | 670 validators, 100.0% of stake |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `he1iusunGwqrNtafDtLd…` | 16,805,000 | 3.97% | 0% |
| 2 | `CcaHc2L43ZWjwCHART3o…` | 15,814,431 | 3.73% | 7% |
| 3 | `3N7s9zXMZ4QqvHQR15t5…` | 12,430,859 | 2.93% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxb…` | 10,236,589 | 2.42% | 0% |
| 5 | `51JBzSTU5rAM8gLAVQKg…` | 9,910,258 | 2.34% | 10% |
| 6 | `CatzoSMUkTRidT5DwBxA…` | 9,615,394 | 2.27% | 5% |
| 7 | `26pV97Ce83ZQ6Kz9XT4t…` | 9,281,563 | 2.19% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2Fp…` | 8,032,075 | 1.9% | 7% |
| 9 | `DumiCKHVqoCQKD8roLAp…` | 6,971,305 | 1.65% | 0% |
| 10 | `CvSb7wdQAFpHuSpTYTJn…` | 6,740,287 | 1.59% | 5% |

## Signals (anomaly detection)

- **[WARNING]** Solana TVL contraction (z=-2.1 vs its recent baseline)
- **[WARNING]** Stablecoin supply contraction (z=-2.4 vs its recent baseline)
- **[WARNING · liquidity_rotation]** Stablecoin supply and TVL moving together — capital rotating in or out of the chain.

## Solana Pulse — sentiment (experimental)

**41/100 — Neutral** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 66.7 |
| fear greed | 13 |
| momentum | 31.1 |
| news | 58 |

Crypto Fear & Greed: 13 (Extreme Fear) · CoinGecko votes bullish: 66.67% · headline tone (48h): +1

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 1,365 |
| Raydium AMM v4 | 1,365 |
| Orca Whirlpool | 1,500 |
| Pump.fun | 1,500 |
| Tensor | 0 |
| Magic Eden v2 | 34 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,300,003 |
| Binance (cold) | 66 |
| OKX (attributed) | 59,504 |
| Coinbase (hot) | 15,573 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 215ms.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 100.0% of stake.
- **Agave**: latest release None · running 4.4.0 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 9523 ms |
| solana_rpc_validators | OK | 233 ms |
| coingecko | OK | 1693 ms |
| defillama_tvl | OK | 49 ms |
| defillama_dex | OK | 1152 ms |
| defillama_fees | OK | 1975 ms |
| defillama_stablecoins | OK | 73 ms |
| defillama_xstocks | FAILED | 34 ms |
| jito_kobe | OK | 109 ms |
| stakewiz | OK | 1316 ms |
| github | FAILED | 6142 ms |
| solana_com_news | FAILED | 61 ms |
| sentiment | OK | 2267 ms |
| solana_status_page | OK | 156 ms |
| solana_rpc_whales | OK | 1142 ms |
| solana_rpc_programs | OK | 1910 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*