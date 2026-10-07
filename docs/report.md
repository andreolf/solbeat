# Solbeat — State of the Solana Network

> Generated 2026-10-07T19:26:54Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1051 is 66% complete (~11h remaining), with the cluster processing ~4,868 TPS (2,392 non-vote). Measured slot time is 270ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $1.3M of Real Economic Value over the last 24h ($932/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $116.08 (-3.6% / 24h). Decentralization: Nakamoto coefficient 18, 671 active validators, 0.0% of stake delinquent. Alpenglow readiness: validators holding 99% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: all clear across every monitored metric.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 454,316,202 |
| Block height | 432,353,766 |
| Epoch | 1051 (65.79% complete, ~11.1h left) |
| TPS (10 min avg) | 4,868 |
| Non-vote TPS | 2,392 |
| Slot time (measured) | 269.8 ms |
| Est. daily transactions | 424,724,863 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0050 |
| Node version | 4.3.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $116.08 (-3.6%/24h) |
| Market cap | $68.4B |
| **REV (24h)** | **$1.3M** (fees $1.1M + Jito tips $291.0K) |
| Chain TVL | $6.4B |
| Stablecoin supply | $16.8B |
| DEX volume (24h) | $2.1B (-0.2%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 589,094,161 SOL |
| Inflation | 3.61% |

Top DEXs by 24h volume: Orca DEX ($310.8M), PumpSwap ($302.9M), Raydium AMM ($225.1M), BisonFi ($220.6M), pump.fun ($185.0M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 671 / 10 |
| Delinquent stake | 0.01% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.6% |
| Avg / median commission | 13.0% / 5% |
| Alpenglow BLS-key readiness | 703 validators, 99.4% of stake |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L43ZWjwCHART3o…` | 17,653,055 | 4.02% | 7% |
| 2 | `he1iusunGwqrNtafDtLd…` | 15,968,869 | 3.63% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5…` | 12,308,201 | 2.8% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxb…` | 11,264,081 | 2.56% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxA…` | 11,149,017 | 2.54% | 5% |
| 6 | `26pV97Ce83ZQ6Kz9XT4t…` | 9,259,685 | 2.11% | 7% |
| 7 | `51JBzSTU5rAM8gLAVQKg…` | 9,251,538 | 2.11% | 10% |
| 8 | `9QU2QSxhb24FUX3Tu2Fp…` | 7,508,703 | 1.71% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJn…` | 7,113,963 | 1.62% | 5% |
| 10 | `3JD3jMmnR6g88qff2WZ3…` | 6,690,032 | 1.52% | 0% |

## Signals (anomaly detection)

All clear — no anomalies across monitored metrics.

## Solana Pulse — sentiment (experimental)

**70/100 — Bullish** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 89.7 |
| fear greed | 71 |
| momentum | 46.3 |
| news | 74 |

Crypto Fear & Greed: 71 (Greed) · CoinGecko votes bullish: 89.66% · headline tone (48h): +3

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 158 |
| Raydium AMM v4 | 143 |
| Orca Whirlpool | 158 |
| Pump.fun | 176 |
| Tensor | 0 |
| Magic Eden v2 | 64 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 10,572,652 |
| Binance (cold) | 1,109,618 |
| OKX (attributed) | 304,345 |
| Coinbase (hot) | 21,210 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 270ms.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 99.4% of stake.
- **Agave**: latest release None · running 4.3.0 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

### Latest ecosystem news (solana.com)

- [Solana Ecosystem Roundup: September 2026](https://solana.com/news/solana-ecosystem-roundup-september-2026) — Tue, 06 Oct 2026
- [Solana Foundation Launches Solana DvP, an Atomic Settlement Program Built for Financial Institutions](https://solana.com/news/solana-foundation-launches-solana-dv-p-an-atomic-settlement-program-built-for-financial-institutions) — Tue, 06 Oct 2026
- [Introducing Solana Microscope: Program Monitoring and Alerts](https://solana.com/news/solana-microscope) — Mon, 05 Oct 2026
- [Solana x AI: The Democratization Layer](https://solana.com/news/solana-ai-the-democratization-layer) — Fri, 02 Oct 2026
- [Solana Changelog: October 1, 2026](https://solana.com/news/solana-changelog-october-1-2026) — Thu, 01 Oct 2026
- [Open USD Is Live on Solana](https://solana.com/news/open-usd-is-live-on-solana) — Wed, 30 Sep 2026

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 8110 ms |
| solana_rpc_validators | OK | 228 ms |
| coingecko | OK | 1648 ms |
| defillama_tvl | OK | 44 ms |
| defillama_dex | OK | 4022 ms |
| defillama_fees | OK | 1796 ms |
| defillama_stablecoins | OK | 175 ms |
| defillama_xstocks | OK | 17026 ms |
| jito_kobe | OK | 198 ms |
| stakewiz | OK | 1637 ms |
| github | FAILED | 6169 ms |
| solana_com_news | OK | 60 ms |
| sentiment | OK | 2397 ms |
| solana_status_page | OK | 21298 ms |
| solana_rpc_whales | OK | 1024 ms |
| solana_rpc_programs | OK | 1982 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*