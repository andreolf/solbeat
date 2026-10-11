# Solbeat — State of the Solana Network

> Generated 2026-10-11T22:42:06Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1055 is 14% complete (~22h remaining), with the cluster processing ~5,053 TPS (1,976 non-vote). Measured slot time is 218ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $916.0K of Real Economic Value over the last 24h ($636/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $111.09 (+0.6% / 24h). Decentralization: Nakamoto coefficient 18, 672 active validators, 0.0% of stake delinquent. Alpenglow readiness: validators holding 99% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: all clear across every monitored metric.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 455,819,530 |
| Block height | 433,856,647 |
| Epoch | 1055 (13.78% complete, ~22.5h left) |
| TPS (10 min avg) | 5,053 |
| Non-vote TPS | 1,976 |
| Slot time (measured) | 217.6 ms |
| Est. daily transactions | 435,842,415 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0043 |
| Node version | 4.3.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $111.09 (+0.6%/24h) |
| Market cap | $65.5B |
| **REV (24h)** | **$916.0K** (fees $740.7K + Jito tips $175.3K) |
| Chain TVL | $6.3B |
| Stablecoin supply | $16.3B |
| DEX volume (24h) | $1.3B (-35.0%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 589,107,525 SOL |
| Inflation | 3.61% |

Top DEXs by 24h volume: PumpSwap ($235.3M), pump.fun ($156.8M), BisonFi ($156.5M), Orca DEX ($136.1M), Raydium AMM ($126.4M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 672 / 9 |
| Delinquent stake | 0.02% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.5% |
| Avg / median commission | 12.8% / 5.0% |
| Alpenglow BLS-key readiness | 707 validators, 99.4% of stake |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L43ZWjwCHART3o…` | 17,781,885 | 4.05% | 7% |
| 2 | `he1iusunGwqrNtafDtLd…` | 15,956,122 | 3.64% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5…` | 12,320,023 | 2.81% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxb…` | 11,147,729 | 2.54% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxA…` | 10,755,463 | 2.45% | 5% |
| 6 | `51JBzSTU5rAM8gLAVQKg…` | 9,332,199 | 2.13% | 10% |
| 7 | `26pV97Ce83ZQ6Kz9XT4t…` | 9,248,710 | 2.11% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2Fp…` | 7,607,284 | 1.73% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJn…` | 6,811,094 | 1.55% | 5% |
| 10 | `3JD3jMmnR6g88qff2WZ3…` | 6,422,658 | 1.46% | 0% |

## Signals (anomaly detection)

All clear — no anomalies across monitored metrics.

## Solana Pulse — sentiment (experimental)

**59/100 — Neutral** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 75.9 |
| fear greed | 61 |
| momentum | 21.0 |
| news | 95 |

Crypto Fear & Greed: 61 (Greed) · CoinGecko votes bullish: 75.86% · headline tone (48h): +6

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 169 |
| Raydium AMM v4 | 169 |
| Orca Whirlpool | 169 |
| Pump.fun | 191 |
| Tensor | 0 |
| Magic Eden v2 | 89 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 10,572,652 |
| Binance (cold) | 1,507,289 |
| OKX (attributed) | 307,250 |
| Coinbase (hot) | 5,203 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 218ms · proposal merged.
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
| solana_rpc | OK | 9284 ms |
| solana_rpc_validators | OK | 411 ms |
| coingecko | OK | 1701 ms |
| defillama_tvl | OK | 315 ms |
| defillama_dex | OK | 812 ms |
| defillama_fees | OK | 1389 ms |
| defillama_stablecoins | OK | 716 ms |
| defillama_xstocks | OK | 3754 ms |
| jito_kobe | OK | 243 ms |
| stakewiz | OK | 1163 ms |
| github | OK | 782 ms |
| solana_com_news | OK | 255 ms |
| sentiment | OK | 2273 ms |
| solana_status_page | OK | 566 ms |
| solana_rpc_whales | OK | 1086 ms |
| solana_rpc_programs | OK | 2119 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*