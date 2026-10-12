# Solbeat — State of the Solana Network

> Generated 2026-10-12T12:18:33Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1055 is 66% complete (~9h remaining), with the cluster processing ~4,831 TPS (1,769 non-vote). Measured slot time is 218ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $927.8K of Real Economic Value over the last 24h ($644/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $110.85 (+1.1% / 24h). Decentralization: Nakamoto coefficient 18, 672 active validators, 0.0% of stake delinquent. Alpenglow readiness: validators holding 99% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: all clear across every monitored metric.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 456,044,077 |
| Block height | 434,081,079 |
| Epoch | 1055 (65.76% complete, ~9.0h left) |
| TPS (10 min avg) | 4,831 |
| Non-vote TPS | 1,769 |
| Slot time (measured) | 218.2 ms |
| Est. daily transactions | 407,560,532 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0053 |
| Node version | 4.3.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $110.85 (+1.1%/24h) |
| Market cap | $65.3B |
| **REV (24h)** | **$927.8K** (fees $753.3K + Jito tips $174.5K) |
| Chain TVL | $6.3B |
| Stablecoin supply | $16.3B |
| DEX volume (24h) | $1.3B (-0.7%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 589,106,922 SOL |
| Inflation | 3.61% |

Top DEXs by 24h volume: Orca DEX ($197.3M), BisonFi ($163.2M), pump.fun ($160.8M), PumpSwap ($135.5M), Raydium AMM ($129.7M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 672 / 9 |
| Delinquent stake | 0.03% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.5% |
| Avg / median commission | 13.1% / 5.0% |
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

**69/100 — Bullish** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 92.0 |
| fear greed | 69 |
| momentum | 34.6 |
| news | 95 |

Crypto Fear & Greed: 69 (Greed) · CoinGecko votes bullish: 92.0% · headline tone (48h): +6

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 168 |
| Raydium AMM v4 | 168 |
| Orca Whirlpool | 190 |
| Pump.fun | 217 |
| Tensor | 2 |
| Magic Eden v2 | 94 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 10,572,652 |
| Binance (cold) | 1,566,262 |
| OKX (attributed) | 307,250 |
| Coinbase (hot) | 4,105 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 218ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 99.4% of stake.
- **Agave**: latest release v4.3.0 · running 4.3.0 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

### Latest ecosystem news (solana.com)

- [Breakpoint 2026: Booked Breakpoint? Let's Get You Prepped (Part 2)](https://solana.com/news/breakpoint-guide-part2) — Thu, 08 Oct 2026
- [Solana Changelog: October 8, 2026](https://solana.com/news/solana-changelog-october-8-2026) — Thu, 08 Oct 2026
- [Samsung Partners with Solana to Natively Deliver Stablecoins in Samsung Wallet to 82 Million U.S. Galaxy Devices](https://solana.com/news/samsung-wallet) — Wed, 07 Oct 2026
- [Solana Ecosystem Roundup: September 2026](https://solana.com/news/solana-ecosystem-roundup-september-2026) — Tue, 06 Oct 2026
- [Solana Foundation Launches Solana DvP, an Atomic Settlement Program Built for Financial Institutions](https://solana.com/news/solana-foundation-launches-solana-dv-p-an-atomic-settlement-program-built-for-financial-institutions) — Tue, 06 Oct 2026
- [Introducing Solana Microscope: Program Monitoring and Alerts](https://solana.com/news/solana-microscope) — Mon, 05 Oct 2026

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 8112 ms |
| solana_rpc_validators | OK | 296 ms |
| coingecko | OK | 1759 ms |
| defillama_tvl | OK | 976 ms |
| defillama_dex | OK | 2123 ms |
| defillama_fees | OK | 2304 ms |
| defillama_stablecoins | OK | 1472 ms |
| defillama_xstocks | OK | 85 ms |
| jito_kobe | OK | 244 ms |
| stakewiz | OK | 2557 ms |
| github | OK | 769 ms |
| solana_com_news | OK | 112 ms |
| sentiment | OK | 2419 ms |
| solana_status_page | OK | 424 ms |
| solana_rpc_whales | OK | 1157 ms |
| solana_rpc_programs | OK | 2014 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*