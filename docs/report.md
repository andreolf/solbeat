# Solbeat — State of the Solana Network

> Generated 2026-10-07T20:28:31Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1051 is 69% complete (~10h remaining), with the cluster processing ~5,206 TPS (2,731 non-vote). Measured slot time is 270ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $1.3M of Real Economic Value over the last 24h ($932/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $116.20 (-4.0% / 24h). Decentralization: Nakamoto coefficient 18, 670 active validators, 0.1% of stake delinquent. Alpenglow readiness: validators holding 99% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: all clear across every monitored metric.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 454,329,855 |
| Block height | 432,367,387 |
| Epoch | 1051 (68.95% complete, ~10.1h left) |
| TPS (10 min avg) | 5,206 |
| Non-vote TPS | 2,731 |
| Slot time (measured) | 269.8 ms |
| Est. daily transactions | 439,144,966 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0047 |
| Node version | 4.3.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $116.20 (-4.0%/24h) |
| Market cap | $68.4B |
| **REV (24h)** | **$1.3M** (fees $1.1M + Jito tips $291.3K) |
| Chain TVL | $6.5B |
| Stablecoin supply | $16.8B |
| DEX volume (24h) | $2.1B (-0.2%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 589,094,110 SOL |
| Inflation | 3.61% |

Top DEXs by 24h volume: Orca DEX ($310.8M), PumpSwap ($302.9M), Raydium AMM ($225.6M), BisonFi ($220.6M), pump.fun ($185.0M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 670 / 11 |
| Delinquent stake | 0.08% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.6% |
| Avg / median commission | 13.0% / 5.0% |
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
| community | 86.7 |
| fear greed | 71 |
| momentum | 47.5 |
| news | 82 |

Crypto Fear & Greed: 71 (Greed) · CoinGecko votes bullish: 86.67% · headline tone (48h): +4

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 147 |
| Raydium AMM v4 | 147 |
| Orca Whirlpool | 147 |
| Pump.fun | 163 |
| Tensor | 7 |
| Magic Eden v2 | 78 |
| Marinade | 1 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 10,572,652 |
| Binance (cold) | 1,089,131 |
| OKX (attributed) | 304,345 |
| Coinbase (hot) | 20,942 |

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
| solana_rpc | OK | 7821 ms |
| solana_rpc_validators | OK | 208 ms |
| coingecko | OK | 1660 ms |
| defillama_tvl | OK | 186 ms |
| defillama_dex | OK | 10088 ms |
| defillama_fees | OK | 12135 ms |
| defillama_stablecoins | OK | 244 ms |
| defillama_xstocks | OK | 820 ms |
| jito_kobe | OK | 209 ms |
| stakewiz | OK | 1406 ms |
| github | FAILED | 6198 ms |
| solana_com_news | OK | 47 ms |
| sentiment | OK | 2295 ms |
| solana_status_page | OK | 355 ms |
| solana_rpc_whales | OK | 1157 ms |
| solana_rpc_programs | OK | 1936 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*