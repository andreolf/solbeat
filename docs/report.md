# Solbeat — State of the Solana Network

> Generated 2026-10-08T19:55:51Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1052 is 42% complete (~18h remaining), with the cluster processing ~5,052 TPS (2,524 non-vote). Measured slot time is 264ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $1.2M of Real Economic Value over the last 24h ($825/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $109.14 (-5.7% / 24h). Decentralization: Nakamoto coefficient 18, 668 active validators, 0.1% of stake delinquent. Alpenglow readiness: validators holding 99% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: all clear across every monitored metric.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 454,644,297 |
| Block height | 432,681,686 |
| Epoch | 1052 (41.74% complete, ~18.5h left) |
| TPS (10 min avg) | 5,052 |
| Non-vote TPS | 2,524 |
| Slot time (measured) | 264.0 ms |
| Est. daily transactions | 445,627,716 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0042 |
| Node version | 4.3.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $109.14 (-5.7%/24h) |
| Market cap | $64.3B |
| **REV (24h)** | **$1.2M** (fees $970.3K + Jito tips $218.2K) |
| Chain TVL | $6.3B |
| Stablecoin supply | $16.5B |
| DEX volume (24h) | $2.2B (7.5%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 589,152,060 SOL |
| Inflation | 3.61% |

Top DEXs by 24h volume: Orca DEX ($295.2M), PumpSwap ($280.5M), Raydium AMM ($244.9M), BisonFi ($230.6M), Manifest Trade ($166.6M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 668 / 11 |
| Delinquent stake | 0.05% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.6% |
| Avg / median commission | 12.6% / 5.0% |
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
| community | 78.3 |
| fear greed | 64 |
| momentum | 43.6 |
| news | 50 |

Crypto Fear & Greed: 64 (Greed) · CoinGecko votes bullish: 78.26% · headline tone (48h): +0

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 144 |
| Raydium AMM v4 | 160 |
| Orca Whirlpool | 179 |
| Pump.fun | 179 |
| Tensor | 0 |
| Magic Eden v2 | 40 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 10,572,652 |
| Binance (cold) | 1,179,958 |
| OKX (attributed) | 304,366 |
| Coinbase (hot) | 16,406 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 264ms · proposal merged.
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
| solana_rpc | OK | 9543 ms |
| solana_rpc_validators | OK | 219 ms |
| coingecko | OK | 1786 ms |
| defillama_tvl | OK | 201 ms |
| defillama_dex | OK | 862 ms |
| defillama_fees | OK | 1181 ms |
| defillama_stablecoins | OK | 1197 ms |
| defillama_xstocks | OK | 683 ms |
| jito_kobe | OK | 332 ms |
| stakewiz | OK | 1219 ms |
| github | OK | 804 ms |
| solana_com_news | OK | 133 ms |
| sentiment | OK | 2306 ms |
| solana_status_page | OK | 391 ms |
| solana_rpc_whales | OK | 1669 ms |
| solana_rpc_programs | OK | 2036 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*