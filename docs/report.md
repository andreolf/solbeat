# Solbeat — State of the Solana Network

> Generated 2026-10-08T12:20:59Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1052 is 18% complete (~26h remaining), with the cluster processing ~4,158 TPS (1,674 non-vote). Measured slot time is 269ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $1.2M of Real Economic Value over the last 24h ($828/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $112.97 (-3.5% / 24h). Decentralization: Nakamoto coefficient 18, 670 active validators, 0.0% of stake delinquent. Alpenglow readiness: validators holding 99% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: all clear across every monitored metric.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 454,543,118 |
| Block height | 432,580,590 |
| Epoch | 1052 (18.31% complete, ~26.3h left) |
| TPS (10 min avg) | 4,158 |
| Non-vote TPS | 1,674 |
| Slot time (measured) | 268.6 ms |
| Est. daily transactions | 347,892,024 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0073 |
| Node version | 4.3.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $112.97 (-3.5%/24h) |
| Market cap | $66.6B |
| **REV (24h)** | **$1.2M** (fees $970.3K + Jito tips $222.0K) |
| Chain TVL | $6.4B |
| Stablecoin supply | $16.5B |
| DEX volume (24h) | $2.2B (7.5%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 589,164,989 SOL |
| Inflation | 3.61% |

Top DEXs by 24h volume: PumpSwap ($280.5M), Orca DEX ($277.3M), BisonFi ($230.6M), Raydium AMM ($200.5M), pump.fun ($161.0M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 670 / 9 |
| Delinquent stake | 0.02% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.6% |
| Avg / median commission | 12.7% / 5.0% |
| Alpenglow BLS-key readiness | 704 validators, 99.4% of stake |

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

**62/100 — Bullish** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 81.1 |
| fear greed | 64 |
| momentum | 48.2 |
| news | 50 |

Crypto Fear & Greed: 64 (Greed) · CoinGecko votes bullish: 81.08% · headline tone (48h): +0

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 156 |
| Raydium AMM v4 | 129 |
| Orca Whirlpool | 156 |
| Pump.fun | 175 |
| Tensor | 0 |
| Magic Eden v2 | 77 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 10,572,652 |
| Binance (cold) | 1,158,789 |
| OKX (attributed) | 304,366 |
| Coinbase (hot) | 20,954 |

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
| solana_rpc | OK | 7337 ms |
| solana_rpc_validators | OK | 315 ms |
| coingecko | OK | 1811 ms |
| defillama_tvl | OK | 80 ms |
| defillama_dex | OK | 8072 ms |
| defillama_fees | OK | 3018 ms |
| defillama_stablecoins | OK | 130 ms |
| defillama_xstocks | OK | 3067 ms |
| jito_kobe | OK | 227 ms |
| stakewiz | OK | 1386 ms |
| github | OK | 983 ms |
| solana_com_news | OK | 150 ms |
| sentiment | OK | 2339 ms |
| solana_status_page | OK | 43430 ms |
| solana_rpc_whales | OK | 990 ms |
| solana_rpc_programs | OK | 1772 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*