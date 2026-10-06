# Solbeat — State of the Solana Network

> Generated 2026-10-06T22:04:52Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1050 is 100% complete (~0h remaining), with the cluster processing ~5,148 TPS (2,674 non-vote). Measured slot time is 270ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $1.3M of Real Economic Value over the last 24h ($893/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $121.07 (-0.1% / 24h). Decentralization: Nakamoto coefficient 18, 671 active validators, 0.1% of stake delinquent. Alpenglow readiness: validators holding 99% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: all clear across every monitored metric.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 454,029,901 |
| Block height | 432,067,519 |
| Epoch | 1050 (99.51% complete, ~0.2h left) |
| TPS (10 min avg) | 5,148 |
| Non-vote TPS | 2,674 |
| Slot time (measured) | 269.5 ms |
| Est. daily transactions | 438,521,290 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0046 |
| Node version | 4.3.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $121.07 (-0.1%/24h) |
| Market cap | $71.3B |
| **REV (24h)** | **$1.3M** (fees $1.0M + Jito tips $244.6K) |
| Chain TVL | $6.6B |
| Stablecoin supply | $17.0B |
| DEX volume (24h) | $2.1B (20.4%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 588,384,872 SOL |
| Inflation | 3.62% |

Top DEXs by 24h volume: PumpSwap ($306.6M), Orca DEX ($295.1M), BisonFi ($234.2M), pump.fun ($187.5M), Raydium AMM ($182.7M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 671 / 14 |
| Delinquent stake | 0.09% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.6% |
| Avg / median commission | 13.0% / 5% |
| Alpenglow BLS-key readiness | 703 validators, 99.4% of stake |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L43ZWjwCHART3o…` | 17,915,070 | 4.06% | 7% |
| 2 | `he1iusunGwqrNtafDtLd…` | 15,937,333 | 3.61% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5…` | 12,292,997 | 2.78% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxb…` | 11,310,013 | 2.56% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxA…` | 11,144,638 | 2.52% | 5% |
| 6 | `26pV97Ce83ZQ6Kz9XT4t…` | 9,258,566 | 2.1% | 7% |
| 7 | `51JBzSTU5rAM8gLAVQKg…` | 9,254,450 | 2.1% | 10% |
| 8 | `9QU2QSxhb24FUX3Tu2Fp…` | 7,629,486 | 1.73% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJn…` | 7,062,716 | 1.6% | 5% |
| 10 | `3JD3jMmnR6g88qff2WZ3…` | 6,687,904 | 1.51% | 0% |

## Signals (anomaly detection)

All clear — no anomalies across monitored metrics.

## Solana Pulse — sentiment (experimental)

**74/100 — Bullish** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 84.4 |
| fear greed | 73 |
| momentum | 64.4 |
| news | 74 |

Crypto Fear & Greed: 73 (Greed) · CoinGecko votes bullish: 84.38% · headline tone (48h): +3

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 148 |
| Raydium AMM v4 | 164 |
| Orca Whirlpool | 164 |
| Pump.fun | 184 |
| Tensor | 1 |
| Magic Eden v2 | 71 |
| Marinade | 1 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 10,572,652 |
| Binance (cold) | 1,137,494 |
| OKX (attributed) | 304,343 |
| Coinbase (hot) | 20,379 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 270ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 99.4% of stake.
- **Agave**: latest release v4.3.0 · running 4.3.0 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

### Latest ecosystem news (solana.com)

- [Solana Foundation Launches Solana DvP, an Atomic Settlement Program Built for Financial Institutions](https://solana.com/news/solana-foundation-launches-solana-dv-p-an-atomic-settlement-program-built-for-financial-institutions) — Tue, 06 Oct 2026
- [Solana x AI: The Democratization Layer](https://solana.com/news/solana-ai-the-democratization-layer) — Fri, 02 Oct 2026
- [Open USD Is Live on Solana](https://solana.com/news/open-usd-is-live-on-solana) — Wed, 30 Sep 2026
- [Slot Time Reduction Effects](https://solana.com/news/slot-time-reduction-effects) — Mon, 28 Sep 2026
- [Solana Foundation Appoints Rachel Conlan as Chief Strategy Officer and Jamal Raees as General Manager of Payments](https://solana.com/news/solana-foundation-appoints-2026) — Thu, 24 Sep 2026
- [Stocks Go Onchain: What the SEC's Innovation Exemption Means for Solana](https://solana.com/news/stocks-sec-innovation-exemption) — Wed, 23 Sep 2026

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 9270 ms |
| solana_rpc_validators | OK | 408 ms |
| coingecko | OK | 1804 ms |
| defillama_tvl | OK | 171 ms |
| defillama_dex | OK | 3613 ms |
| defillama_fees | OK | 1267 ms |
| defillama_stablecoins | OK | 1073 ms |
| defillama_xstocks | OK | 1697 ms |
| jito_kobe | OK | 499 ms |
| stakewiz | OK | 1000 ms |
| github | OK | 802 ms |
| solana_com_news | OK | 216 ms |
| sentiment | OK | 2361 ms |
| solana_status_page | OK | 835 ms |
| solana_rpc_whales | OK | 1458 ms |
| solana_rpc_programs | OK | 2313 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*