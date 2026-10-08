# Solbeat — State of the Solana Network

> Generated 2026-10-08T02:47:51Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1051 is 89% complete (~4h remaining), with the cluster processing ~4,490 TPS (2,001 non-vote). Measured slot time is 269ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $1.3M of Real Economic Value over the last 24h ($878/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $116.58 (-1.5% / 24h). Decentralization: Nakamoto coefficient 18, 671 active validators, 0.0% of stake delinquent. Alpenglow readiness: validators holding 99% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: all clear across every monitored metric.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 454,414,572 |
| Block height | 432,452,059 |
| Epoch | 1051 (88.56% complete, ~3.7h left) |
| TPS (10 min avg) | 4,490 |
| Non-vote TPS | 2,001 |
| Slot time (measured) | 268.7 ms |
| Est. daily transactions | 385,826,168 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0057 |
| Node version | 4.3.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $116.58 (-1.5%/24h) |
| Market cap | $68.7B |
| **REV (24h)** | **$1.3M** (fees $970.3K + Jito tips $293.5K) |
| Chain TVL | $6.5B |
| Stablecoin supply | $16.5B |
| DEX volume (24h) | $2.1B (4.4%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 589,094,069 SOL |
| Inflation | 3.61% |

Top DEXs by 24h volume: Orca DEX ($298.4M), PumpSwap ($280.5M), Raydium AMM ($225.9M), BisonFi ($220.6M), pump.fun ($185.0M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 671 / 10 |
| Delinquent stake | 0.01% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.6% |
| Avg / median commission | 13.0% / 5% |
| Alpenglow BLS-key readiness | 704 validators, 99.4% of stake |

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

**69/100 — Bullish** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 79.4 |
| fear greed | 64 |
| momentum | 51.0 |
| news | 90 |

Crypto Fear & Greed: 64 (Greed) · CoinGecko votes bullish: 79.41% · headline tone (48h): +5

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 146 |
| Raydium AMM v4 | 133 |
| Orca Whirlpool | 162 |
| Pump.fun | 162 |
| Tensor | 0 |
| Magic Eden v2 | 67 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 10,572,652 |
| Binance (cold) | 1,104,582 |
| OKX (attributed) | 304,366 |
| Coinbase (hot) | 19,397 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 269ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 99.4% of stake.
- **Agave**: latest release v4.3.0 · running 4.3.0 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

### Latest ecosystem news (solana.com)

- [Samsung Partners with Solana to Natively Deliver Stablecoins in Samsung Wallet to 82 Million U.S. Galaxy Devices](https://solana.com/news/samsung-wallet) — Wed, 07 Oct 2026
- [Solana Ecosystem Roundup: September 2026](https://solana.com/news/solana-ecosystem-roundup-september-2026) — Tue, 06 Oct 2026
- [Solana Foundation Launches Solana DvP, an Atomic Settlement Program Built for Financial Institutions](https://solana.com/news/solana-foundation-launches-solana-dv-p-an-atomic-settlement-program-built-for-financial-institutions) — Tue, 06 Oct 2026
- [Introducing Solana Microscope: Program Monitoring and Alerts](https://solana.com/news/solana-microscope) — Mon, 05 Oct 2026
- [Solana x AI: The Democratization Layer](https://solana.com/news/solana-ai-the-democratization-layer) — Fri, 02 Oct 2026
- [Solana Changelog: October 1, 2026](https://solana.com/news/solana-changelog-october-1-2026) — Thu, 01 Oct 2026

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 8980 ms |
| solana_rpc_validators | OK | 159 ms |
| coingecko | OK | 1704 ms |
| defillama_tvl | OK | 73 ms |
| defillama_dex | OK | 1672 ms |
| defillama_fees | OK | 989 ms |
| defillama_stablecoins | OK | 503 ms |
| defillama_xstocks | OK | 162 ms |
| jito_kobe | OK | 210 ms |
| stakewiz | OK | 864 ms |
| github | OK | 714 ms |
| solana_com_news | OK | 183 ms |
| sentiment | OK | 2092 ms |
| solana_status_page | OK | 406 ms |
| solana_rpc_whales | OK | 889 ms |
| solana_rpc_programs | OK | 1656 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*