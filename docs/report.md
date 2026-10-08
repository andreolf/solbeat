# Solbeat — State of the Solana Network

> Generated 2026-10-08T20:26:19Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1052 is 43% complete (~18h remaining), with the cluster processing ~5,015 TPS (2,553 non-vote). Measured slot time is 272ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $1.2M of Real Economic Value over the last 24h ($821/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $109.25 (-6.0% / 24h). Decentralization: Nakamoto coefficient 18, 672 active validators, 0.1% of stake delinquent. Alpenglow readiness: validators holding 99% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: all clear across every monitored metric.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 454,651,081 |
| Block height | 432,688,462 |
| Epoch | 1052 (43.31% complete, ~18.5h left) |
| TPS (10 min avg) | 5,015 |
| Non-vote TPS | 2,553 |
| Slot time (measured) | 272.0 ms |
| Est. daily transactions | 450,355,771 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0041 |
| Node version | 4.3.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $109.25 (-6.0%/24h) |
| Market cap | $64.4B |
| **REV (24h)** | **$1.2M** (fees $970.3K + Jito tips $212.0K) |
| Chain TVL | $6.3B |
| Stablecoin supply | $16.5B |
| DEX volume (24h) | $2.2B (7.5%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 589,152,035 SOL |
| Inflation | 3.61% |

Top DEXs by 24h volume: Orca DEX ($295.2M), PumpSwap ($280.5M), Raydium AMM ($244.9M), BisonFi ($230.6M), Manifest Trade ($171.9M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 672 / 9 |
| Delinquent stake | 0.08% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.6% |
| Avg / median commission | 12.7% / 5.0% |
| Alpenglow BLS-key readiness | 706 validators, 99.4% of stake |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L43ZWjwCHART3o…` | 17,819,094 | 4.06% | 7% |
| 2 | `he1iusunGwqrNtafDtLd…` | 15,944,778 | 3.63% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5…` | 12,318,266 | 2.81% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxb…` | 11,224,868 | 2.56% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxA…` | 11,075,222 | 2.52% | 5% |
| 6 | `51JBzSTU5rAM8gLAVQKg…` | 9,267,423 | 2.11% | 10% |
| 7 | `26pV97Ce83ZQ6Kz9XT4t…` | 9,257,645 | 2.11% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2Fp…` | 7,512,076 | 1.71% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJn…` | 6,812,500 | 1.55% | 5% |
| 10 | `3JD3jMmnR6g88qff2WZ3…` | 6,691,194 | 1.52% | 0% |

## Signals (anomaly detection)

All clear — no anomalies across monitored metrics.

## Solana Pulse — sentiment (experimental)

**60/100 — Bullish** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 77.8 |
| fear greed | 64 |
| momentum | 43.6 |
| news | 50 |

Crypto Fear & Greed: 64 (Greed) · CoinGecko votes bullish: 77.78% · headline tone (48h): +0

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 157 |
| Raydium AMM v4 | 142 |
| Orca Whirlpool | 142 |
| Pump.fun | 176 |
| Tensor | 3 |
| Magic Eden v2 | 142 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 10,572,652 |
| Binance (cold) | 1,169,489 |
| OKX (attributed) | 304,366 |
| Coinbase (hot) | 16,393 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 272ms · proposal merged.
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
| solana_rpc | OK | 9019 ms |
| solana_rpc_validators | OK | 261 ms |
| coingecko | OK | 1770 ms |
| defillama_tvl | OK | 245 ms |
| defillama_dex | OK | 950 ms |
| defillama_fees | OK | 1159 ms |
| defillama_stablecoins | OK | 911 ms |
| defillama_xstocks | OK | 13100 ms |
| jito_kobe | OK | 298 ms |
| stakewiz | OK | 1089 ms |
| github | OK | 1809 ms |
| solana_com_news | OK | 170 ms |
| sentiment | OK | 2338 ms |
| solana_status_page | OK | 354 ms |
| solana_rpc_whales | OK | 1002 ms |
| solana_rpc_programs | OK | 2042 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*