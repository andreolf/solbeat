# Solbeat — State of the Solana Network

> Generated 2026-10-10T23:55:27Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1054 is 27% complete (~19h remaining), with the cluster processing ~4,547 TPS (1,488 non-vote). Measured slot time is 220ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $1.0M of Real Economic Value over the last 24h ($700/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $110.15 (+0.9% / 24h). Decentralization: Nakamoto coefficient 18, 675 active validators, 0.0% of stake delinquent. Alpenglow readiness: validators holding 99% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: all clear across every monitored metric.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 455,443,994 |
| Block height | 433,481,164 |
| Epoch | 1054 (26.85% complete, ~19.3h left) |
| TPS (10 min avg) | 4,547 |
| Non-vote TPS | 1,488 |
| Slot time (measured) | 219.8 ms |
| Est. daily transactions | 418,937,844 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0053 |
| Node version | 4.3.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $110.15 (+0.9%/24h) |
| Market cap | $64.9B |
| **REV (24h)** | **$1.0M** (fees $808.7K + Jito tips $199.1K) |
| Chain TVL | $6.2B |
| Stablecoin supply | $16.4B |
| DEX volume (24h) | $2.0B (-25.2%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 588,848,249 SOL |
| Inflation | 3.61% |

Top DEXs by 24h volume: PumpSwap ($389.9M), BisonFi ($258.7M), pump.fun ($175.6M), Orca DEX ($118.9M), Meteora DLMM ($110.7M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 675 / 5 |
| Delinquent stake | 0.0% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.5% |
| Avg / median commission | 12.9% / 5% |
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

**58/100 — Neutral** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 76.0 |
| fear greed | 64 |
| momentum | 23.4 |
| news | 82 |

Crypto Fear & Greed: 64 (Greed) · CoinGecko votes bullish: 76.0% · headline tone (48h): +4

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 168 |
| Raydium AMM v4 | 168 |
| Orca Whirlpool | 168 |
| Pump.fun | 190 |
| Tensor | 0 |
| Magic Eden v2 | 75 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 10,572,652 |
| Binance (cold) | 1,386,129 |
| OKX (attributed) | 307,250 |
| Coinbase (hot) | 7,901 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 220ms · proposal merged.
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
| solana_rpc | OK | 7261 ms |
| solana_rpc_validators | OK | 150 ms |
| coingecko | OK | 1791 ms |
| defillama_tvl | OK | 132 ms |
| defillama_dex | OK | 1221 ms |
| defillama_fees | OK | 1949 ms |
| defillama_stablecoins | OK | 123 ms |
| defillama_xstocks | OK | 50 ms |
| jito_kobe | OK | 526 ms |
| stakewiz | OK | 1419 ms |
| github | OK | 1003 ms |
| solana_com_news | OK | 127 ms |
| sentiment | OK | 2385 ms |
| solana_status_page | OK | 536 ms |
| solana_rpc_whales | OK | 1013 ms |
| solana_rpc_programs | OK | 1820 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*