# Solbeat — State of the Solana Network

> Generated 2026-10-02T13:57:22Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1047 is 76% complete (~8h remaining), with the cluster processing ~4,925 TPS (2,431 non-vote). Measured slot time is 267ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $1.4M of Real Economic Value over the last 24h ($941/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $122.23 (+3.8% / 24h). Decentralization: Nakamoto coefficient 18, 672 active validators, 0.0% of stake delinquent. Alpenglow readiness: validators holding 99% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 1 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 452,630,177 |
| Block height | 430,668,872 |
| Epoch | 1047 (75.5% complete, ~7.8h left) |
| TPS (10 min avg) | 4,925 |
| Non-vote TPS | 2,431 |
| Slot time (measured) | 266.7 ms |
| Est. daily transactions | 370,128,117 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0073 |
| Node version | 4.3.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $122.23 (+3.8%/24h) |
| Market cap | $71.9B |
| **REV (24h)** | **$1.4M** (fees $1.1M + Jito tips $234.4K) |
| Chain TVL | $6.7B |
| Stablecoin supply | $16.5B |
| DEX volume (24h) | $2.5B (-3.2%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 588,075,178 SOL |
| Inflation | 3.62% |

Top DEXs by 24h volume: PumpSwap ($371.2M), Orca DEX ($360.7M), Raydium AMM ($227.7M), BisonFi ($216.9M), Meteora DLMM ($195.5M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 672 / 12 |
| Delinquent stake | 0.02% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.6% |
| Avg / median commission | 13% / 5.0% |
| Alpenglow BLS-key readiness | 703 validators, 99.4% of stake |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L43ZWjwCHART3o…` | 17,839,408 | 4.05% | 7% |
| 2 | `he1iusunGwqrNtafDtLd…` | 15,905,145 | 3.61% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5…` | 12,328,203 | 2.8% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxb…` | 11,357,265 | 2.58% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxA…` | 11,209,121 | 2.54% | 5% |
| 6 | `26pV97Ce83ZQ6Kz9XT4t…` | 9,267,704 | 2.1% | 7% |
| 7 | `51JBzSTU5rAM8gLAVQKg…` | 9,246,451 | 2.1% | 10% |
| 8 | `9QU2QSxhb24FUX3Tu2Fp…` | 7,601,711 | 1.72% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJn…` | 7,063,975 | 1.6% | 5% |
| 10 | `3JD3jMmnR6g88qff2WZ3…` | 6,682,305 | 1.52% | 0% |

## Signals (anomaly detection)

- **[WARNING]** Solana TVL surge (z=+2.1 vs its recent baseline)

## Solana Pulse — sentiment (experimental)

**66/100 — Bullish** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 81.5 |
| fear greed | 72 |
| momentum | 52.0 |
| news | 50 |

Crypto Fear & Greed: 72 (Greed) · CoinGecko votes bullish: 81.48% · headline tone (48h): +0

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 147 |
| Raydium AMM v4 | 134 |
| Orca Whirlpool | 163 |
| Pump.fun | 163 |
| Tensor | 0 |
| Magic Eden v2 | 60 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 10,572,652 |
| Binance (cold) | 1,307,773 |
| OKX (attributed) | 378,338 |
| Coinbase (hot) | 8,876 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 267ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 99.4% of stake.
- **Agave**: latest release v4.3.0 · running 4.3.0 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

### Latest ecosystem news (solana.com)

- [Open USD Is Live on Solana](https://solana.com/news/open-usd-is-live-on-solana) — Wed, 30 Sep 2026
- [Slot Time Reduction Effects](https://solana.com/news/slot-time-reduction-effects) — Mon, 28 Sep 2026
- [Solana Foundation Appoints Rachel Conlan as Chief Strategy Officer and Jamal Raees as General Manager of Payments](https://solana.com/news/solana-foundation-appoints-2026) — Thu, 24 Sep 2026
- [Stocks Go Onchain: What the SEC's Innovation Exemption Means for Solana](https://solana.com/news/stocks-sec-innovation-exemption) — Wed, 23 Sep 2026
- [Solana Changelog: September 18, 2026](https://solana.com/news/solana-changelog-september-18-2026) — Sat, 19 Sep 2026
- [How AI Is Reshaping Crypto Security, with Michael Coates](https://solana.com/news/bits-to-bricks-crypto-security-michael-coates) — Sat, 19 Sep 2026

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 8913 ms |
| solana_rpc_validators | OK | 242 ms |
| coingecko | OK | 1617 ms |
| defillama_tvl | OK | 89 ms |
| defillama_dex | OK | 1316 ms |
| defillama_fees | OK | 989 ms |
| defillama_stablecoins | OK | 125 ms |
| defillama_xstocks | OK | 33 ms |
| jito_kobe | OK | 308 ms |
| stakewiz | OK | 878 ms |
| github | OK | 695 ms |
| solana_com_news | OK | 83 ms |
| sentiment | OK | 2126 ms |
| solana_status_page | OK | 506 ms |
| solana_rpc_whales | OK | 1052 ms |
| solana_rpc_programs | OK | 1849 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*