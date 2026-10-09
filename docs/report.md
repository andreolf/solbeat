# Solbeat — State of the Solana Network

> Generated 2026-10-09T20:48:02Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1053 is 23% complete (~20h remaining), with the cluster processing ~5,556 TPS (2,486 non-vote). Measured slot time is 219ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $1.2M of Real Economic Value over the last 24h ($841/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $108.71 (-0.8% / 24h). Decentralization: Nakamoto coefficient 18, 674 active validators, 0.0% of stake delinquent. Alpenglow readiness: validators holding 99% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: all clear across every monitored metric.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 454,996,751 |
| Block height | 433,033,999 |
| Epoch | 1053 (23.32% complete, ~20.1h left) |
| TPS (10 min avg) | 5,556 |
| Non-vote TPS | 2,486 |
| Slot time (measured) | 218.8 ms |
| Est. daily transactions | 456,048,171 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0049 |
| Node version | 4.3.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $108.71 (-0.8%/24h) |
| Market cap | $64.0B |
| **REV (24h)** | **$1.2M** (fees $940.1K + Jito tips $270.8K) |
| Chain TVL | $6.2B |
| Stablecoin supply | $16.3B |
| DEX volume (24h) | $2.6B (19.9%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 588,768,252 SOL |
| Inflation | 3.61% |

Top DEXs by 24h volume: PumpSwap ($364.6M), BisonFi ($297.2M), Orca DEX ($284.7M), Meteora DLMM ($215.9M), Raydium AMM ($170.3M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 674 / 6 |
| Delinquent stake | 0.0% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.6% |
| Avg / median commission | 12.8% / 5.0% |
| Alpenglow BLS-key readiness | 707 validators, 99.4% of stake |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L43ZWjwCHART3o…` | 17,788,627 | 4.06% | 7% |
| 2 | `he1iusunGwqrNtafDtLd…` | 15,954,195 | 3.64% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5…` | 12,299,759 | 2.81% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxb…` | 11,178,787 | 2.55% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxA…` | 10,972,770 | 2.51% | 5% |
| 6 | `51JBzSTU5rAM8gLAVQKg…` | 9,315,835 | 2.13% | 10% |
| 7 | `26pV97Ce83ZQ6Kz9XT4t…` | 9,251,552 | 2.11% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2Fp…` | 7,589,922 | 1.73% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJn…` | 6,809,494 | 1.56% | 5% |
| 10 | `3JD3jMmnR6g88qff2WZ3…` | 6,692,115 | 1.53% | 0% |

## Signals (anomaly detection)

All clear — no anomalies across monitored metrics.

## Solana Pulse — sentiment (experimental)

**66/100 — Bullish** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 78.6 |
| fear greed | 59 |
| momentum | 45.8 |
| news | 90 |

Crypto Fear & Greed: 59 (Greed) · CoinGecko votes bullish: 78.57% · headline tone (48h): +5

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 174 |
| Raydium AMM v4 | 174 |
| Orca Whirlpool | 174 |
| Pump.fun | 197 |
| Tensor | 2 |
| Magic Eden v2 | 48 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 10,572,652 |
| Binance (cold) | 1,337,472 |
| OKX (attributed) | 307,248 |
| Coinbase (hot) | 12,850 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 219ms · proposal merged.
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
| solana_rpc | OK | 7488 ms |
| solana_rpc_validators | OK | 149 ms |
| coingecko | OK | 1798 ms |
| defillama_tvl | OK | 92 ms |
| defillama_dex | OK | 5588 ms |
| defillama_fees | OK | 2512 ms |
| defillama_stablecoins | OK | 724 ms |
| defillama_xstocks | OK | 845 ms |
| jito_kobe | OK | 219 ms |
| stakewiz | OK | 982 ms |
| github | OK | 982 ms |
| solana_com_news | OK | 119 ms |
| sentiment | OK | 2348 ms |
| solana_status_page | OK | 442 ms |
| solana_rpc_whales | OK | 886 ms |
| solana_rpc_programs | OK | 1761 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*