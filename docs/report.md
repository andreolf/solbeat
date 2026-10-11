# Solbeat — State of the Solana Network

> Generated 2026-10-11T23:43:01Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1055 is 18% complete (~21h remaining), with the cluster processing ~4,494 TPS (1,396 non-vote). Measured slot time is 216ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $917.2K of Real Economic Value over the last 24h ($637/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $111.19 (+1.1% / 24h). Decentralization: Nakamoto coefficient 18, 673 active validators, 0.0% of stake delinquent. Alpenglow readiness: validators holding 99% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: all clear across every monitored metric.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 455,836,328 |
| Block height | 433,873,445 |
| Epoch | 1055 (17.67% complete, ~21.4h left) |
| TPS (10 min avg) | 4,494 |
| Non-vote TPS | 1,396 |
| Slot time (measured) | 216.3 ms |
| Est. daily transactions | 430,467,038 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0045 |
| Node version | 4.3.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $111.19 (+1.1%/24h) |
| Market cap | $65.5B |
| **REV (24h)** | **$917.2K** (fees $740.7K + Jito tips $176.5K) |
| Chain TVL | $6.2B |
| Stablecoin supply | $16.3B |
| DEX volume (24h) | $1.3B (-35.0%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 589,107,479 SOL |
| Inflation | 3.61% |

Top DEXs by 24h volume: PumpSwap ($235.3M), pump.fun ($156.8M), BisonFi ($156.5M), Orca DEX ($145.8M), Raydium AMM ($129.4M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 673 / 8 |
| Delinquent stake | 0.02% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.5% |
| Avg / median commission | 12.8% / 5% |
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

**57/100 — Neutral** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 76.7 |
| fear greed | 61 |
| momentum | 20.9 |
| news | 82 |

Crypto Fear & Greed: 61 (Greed) · CoinGecko votes bullish: 76.67% · headline tone (48h): +4

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 186 |
| Raydium AMM v4 | 186 |
| Orca Whirlpool | 186 |
| Pump.fun | 212 |
| Tensor | 0 |
| Magic Eden v2 | 65 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 10,572,652 |
| Binance (cold) | 1,507,966 |
| OKX (attributed) | 307,250 |
| Coinbase (hot) | 4,999 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 216ms · proposal merged.
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
| solana_rpc | OK | 9863 ms |
| solana_rpc_validators | OK | 358 ms |
| coingecko | OK | 1689 ms |
| defillama_tvl | OK | 258 ms |
| defillama_dex | OK | 847 ms |
| defillama_fees | OK | 1396 ms |
| defillama_stablecoins | OK | 672 ms |
| defillama_xstocks | OK | 245 ms |
| jito_kobe | OK | 576 ms |
| stakewiz | OK | 948 ms |
| github | OK | 782 ms |
| solana_com_news | OK | 100 ms |
| sentiment | OK | 2327 ms |
| solana_status_page | OK | 769 ms |
| solana_rpc_whales | OK | 1142 ms |
| solana_rpc_programs | OK | 2055 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*