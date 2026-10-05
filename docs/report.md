# Solbeat — State of the Solana Network

> Generated 2026-10-05T21:28:27Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1050 is 23% complete (~25h remaining), with the cluster processing ~4,656 TPS (2,163 non-vote). Measured slot time is 268ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $1.3M of Real Economic Value over the last 24h ($871/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $120.70 (-0.6% / 24h). Decentralization: Nakamoto coefficient 18, 671 active validators, 0.1% of stake delinquent. Alpenglow readiness: validators holding 99% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: all clear across every monitored metric.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 453,699,856 |
| Block height | 431,737,753 |
| Epoch | 1050 (23.11% complete, ~24.7h left) |
| TPS (10 min avg) | 4,656 |
| Non-vote TPS | 2,163 |
| Slot time (measured) | 268.1 ms |
| Est. daily transactions | 411,997,643 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0051 |
| Node version | 4.3.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $120.70 (-0.6%/24h) |
| Market cap | $71.0B |
| **REV (24h)** | **$1.3M** (fees $1.0M + Jito tips $245.1K) |
| Chain TVL | $6.8B |
| Stablecoin supply | $16.8B |
| DEX volume (24h) | $1.7B (9.9%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 588,384,626 SOL |
| Inflation | 3.62% |

Top DEXs by 24h volume: PumpSwap ($397.8M), Orca DEX ($307.6M), BisonFi ($236.7M), pump.fun ($184.2M), Raydium AMM ($176.7M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 671 / 14 |
| Delinquent stake | 0.07% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.6% |
| Avg / median commission | 12.7% / 5% |
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

**72/100 — Bullish** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 82.9 |
| fear greed | 70 |
| momentum | 58.3 |
| news | 82 |

Crypto Fear & Greed: 70 (Greed) · CoinGecko votes bullish: 82.86% · headline tone (48h): +4

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 144 |
| Raydium AMM v4 | 144 |
| Orca Whirlpool | 159 |
| Pump.fun | 178 |
| Tensor | 0 |
| Magic Eden v2 | 42 |
| Marinade | 1 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 10,572,652 |
| Binance (cold) | 1,241,361 |
| OKX (attributed) | 303,366 |
| Coinbase (hot) | 11,803 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 268ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 99.4% of stake.
- **Agave**: latest release v4.3.0 · running 4.3.0 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

### Latest ecosystem news (solana.com)

- [Solana x AI: The Democratization Layer](https://solana.com/news/solana-ai-the-democratization-layer) — Fri, 02 Oct 2026
- [Open USD Is Live on Solana](https://solana.com/news/open-usd-is-live-on-solana) — Wed, 30 Sep 2026
- [Slot Time Reduction Effects](https://solana.com/news/slot-time-reduction-effects) — Mon, 28 Sep 2026
- [Solana Foundation Appoints Rachel Conlan as Chief Strategy Officer and Jamal Raees as General Manager of Payments](https://solana.com/news/solana-foundation-appoints-2026) — Thu, 24 Sep 2026
- [Stocks Go Onchain: What the SEC's Innovation Exemption Means for Solana](https://solana.com/news/stocks-sec-innovation-exemption) — Wed, 23 Sep 2026
- [Solana Changelog: September 18, 2026](https://solana.com/news/solana-changelog-september-18-2026) — Sat, 19 Sep 2026

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 7423 ms |
| solana_rpc_validators | OK | 262 ms |
| coingecko | OK | 1819 ms |
| defillama_tvl | OK | 264 ms |
| defillama_dex | OK | 21690 ms |
| defillama_fees | OK | 3403 ms |
| defillama_stablecoins | OK | 1237 ms |
| defillama_xstocks | OK | 2974 ms |
| jito_kobe | OK | 226 ms |
| stakewiz | OK | 1114 ms |
| github | OK | 1033 ms |
| solana_com_news | OK | 174 ms |
| sentiment | OK | 2411 ms |
| solana_status_page | OK | 401 ms |
| solana_rpc_whales | OK | 1042 ms |
| solana_rpc_programs | OK | 1718 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*