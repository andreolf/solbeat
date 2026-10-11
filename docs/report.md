# Solbeat — State of the Solana Network

> Generated 2026-10-11T18:05:16Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1054 is 96% complete (~1h remaining), with the cluster processing ~5,344 TPS (2,313 non-vote). Measured slot time is 221ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $942.4K of Real Economic Value over the last 24h ($654/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $112.11 (+2.0% / 24h). Decentralization: Nakamoto coefficient 18, 672 active validators, 0.0% of stake delinquent. Alpenglow readiness: validators holding 99% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: all clear across every monitored metric.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 455,743,634 |
| Block height | 433,780,766 |
| Epoch | 1054 (96.21% complete, ~1.0h left) |
| TPS (10 min avg) | 5,344 |
| Non-vote TPS | 2,313 |
| Slot time (measured) | 220.8 ms |
| Est. daily transactions | 436,915,031 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0043 |
| Node version | 4.3.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $112.11 (+2.0%/24h) |
| Market cap | $66.0B |
| **REV (24h)** | **$942.4K** (fees $740.7K + Jito tips $201.7K) |
| Chain TVL | $6.3B |
| Stablecoin supply | $16.3B |
| DEX volume (24h) | $1.3B (-35.0%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 589,050,775 SOL |
| Inflation | 3.61% |

Top DEXs by 24h volume: PumpSwap ($235.3M), pump.fun ($156.8M), BisonFi ($156.5M), Raydium AMM ($117.6M), Orca DEX ($115.2M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 672 / 8 |
| Delinquent stake | 0.03% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.5% |
| Avg / median commission | 13.1% / 5.0% |
| Alpenglow BLS-key readiness | 707 validators, 99.4% of stake |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L43ZWjwCHART3o…` | 17,775,444 | 4.05% | 7% |
| 2 | `he1iusunGwqrNtafDtLd…` | 15,954,957 | 3.64% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5…` | 12,313,356 | 2.81% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxb…` | 11,145,934 | 2.54% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxA…` | 10,754,664 | 2.45% | 5% |
| 6 | `51JBzSTU5rAM8gLAVQKg…` | 9,328,689 | 2.13% | 10% |
| 7 | `26pV97Ce83ZQ6Kz9XT4t…` | 9,240,266 | 2.11% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2Fp…` | 7,603,786 | 1.73% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJn…` | 6,810,142 | 1.55% | 5% |
| 10 | `3JD3jMmnR6g88qff2WZ3…` | 6,421,774 | 1.46% | 0% |

## Signals (anomaly detection)

All clear — no anomalies across monitored metrics.

## Solana Pulse — sentiment (experimental)

**57/100 — Neutral** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 71.9 |
| fear greed | 61 |
| momentum | 23.1 |
| news | 90 |

Crypto Fear & Greed: 61 (Greed) · CoinGecko votes bullish: 71.88% · headline tone (48h): +5

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 186 |
| Raydium AMM v4 | 186 |
| Orca Whirlpool | 186 |
| Pump.fun | 186 |
| Tensor | 0 |
| Magic Eden v2 | 75 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 10,572,652 |
| Binance (cold) | 1,512,194 |
| OKX (attributed) | 307,250 |
| Coinbase (hot) | 4,667 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 221ms · proposal merged.
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
| solana_rpc | OK | 7301 ms |
| solana_rpc_validators | OK | 286 ms |
| coingecko | OK | 1815 ms |
| defillama_tvl | OK | 89 ms |
| defillama_dex | OK | 1152 ms |
| defillama_fees | OK | 1998 ms |
| defillama_stablecoins | OK | 1170 ms |
| defillama_xstocks | OK | 49 ms |
| jito_kobe | OK | 239 ms |
| stakewiz | OK | 1441 ms |
| github | OK | 940 ms |
| solana_com_news | OK | 108 ms |
| sentiment | OK | 2406 ms |
| solana_status_page | OK | 388 ms |
| solana_rpc_whales | OK | 964 ms |
| solana_rpc_programs | OK | 1627 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*