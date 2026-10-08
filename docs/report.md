# Solbeat — State of the Solana Network

> Generated 2026-10-08T18:24:31Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1052 is 37% complete (~20h remaining), with the cluster processing ~5,041 TPS (2,577 non-vote). Measured slot time is 270ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $1.2M of Real Economic Value over the last 24h ($819/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $107.07 (-8.1% / 24h). Decentralization: Nakamoto coefficient 18, 670 active validators, 0.0% of stake delinquent. Alpenglow readiness: validators holding 99% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: all clear across every monitored metric.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 454,624,036 |
| Block height | 432,661,445 |
| Epoch | 1052 (37.05% complete, ~20.4h left) |
| TPS (10 min avg) | 5,041 |
| Non-vote TPS | 2,577 |
| Slot time (measured) | 269.7 ms |
| Est. daily transactions | 439,932,216 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0043 |
| Node version | 4.3.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $107.07 (-8.1%/24h) |
| Market cap | $62.9B |
| **REV (24h)** | **$1.2M** (fees $970.3K + Jito tips $209.5K) |
| Chain TVL | $6.3B |
| Stablecoin supply | $16.5B |
| DEX volume (24h) | $2.2B (7.5%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 589,152,137 SOL |
| Inflation | 3.61% |

Top DEXs by 24h volume: Orca DEX ($295.2M), PumpSwap ($280.5M), Raydium AMM ($233.1M), BisonFi ($230.6M), Manifest Trade ($179.1M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 670 / 9 |
| Delinquent stake | 0.03% |
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

**60/100 — Bullish** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 74.5 |
| fear greed | 64 |
| momentum | 42.5 |
| news | 58 |

Crypto Fear & Greed: 64 (Greed) · CoinGecko votes bullish: 74.47% · headline tone (48h): +1

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 154 |
| Raydium AMM v4 | 172 |
| Orca Whirlpool | 172 |
| Pump.fun | 172 |
| Tensor | 0 |
| Magic Eden v2 | 40 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 10,572,652 |
| Binance (cold) | 1,189,318 |
| OKX (attributed) | 304,366 |
| Coinbase (hot) | 16,780 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 270ms · proposal merged.
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
| solana_rpc | OK | 9655 ms |
| solana_rpc_validators | OK | 364 ms |
| coingecko | OK | 1807 ms |
| defillama_tvl | OK | 180 ms |
| defillama_dex | OK | 3139 ms |
| defillama_fees | OK | 1430 ms |
| defillama_stablecoins | OK | 925 ms |
| defillama_xstocks | OK | 1317 ms |
| jito_kobe | OK | 444 ms |
| stakewiz | OK | 935 ms |
| github | OK | 798 ms |
| solana_com_news | OK | 153 ms |
| sentiment | OK | 2582 ms |
| solana_status_page | OK | 403 ms |
| solana_rpc_whales | OK | 1136 ms |
| solana_rpc_programs | OK | 2219 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*