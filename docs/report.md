# Solbeat — State of the Solana Network

> Generated 2026-10-20T21:40:26Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1063 is 39% complete (~16h remaining), with the cluster processing ~5,317 TPS (2,308 non-vote). Measured slot time is 217ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $943.2K of Real Economic Value over the last 24h ($655/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $106.54 (+1.8% / 24h). Decentralization: Nakamoto coefficient 18, 665 active validators, 1.1% of stake delinquent. Alpenglow readiness: validators holding 99% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: all clear across every monitored metric.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 459,382,609 |
| Block height | 437,417,569 |
| Epoch | 1063 (38.57% complete, ~16.0h left) |
| TPS (10 min avg) | 5,317 |
| Non-vote TPS | 2,308 |
| Slot time (measured) | 217.2 ms |
| Est. daily transactions | 474,273,671 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0037 |
| Node version | 4.3.2 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $106.54 (+1.8%/24h) |
| Market cap | $62.8B |
| **REV (24h)** | **$943.2K** (fees $781.5K + Jito tips $161.7K) |
| Chain TVL | $5.9B |
| Stablecoin supply | $15.8B |
| DEX volume (24h) | $1.8B (7.4%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 589,549,334 SOL |
| Inflation | 3.59% |

Top DEXs by 24h volume: Orca DEX ($286.6M), BisonFi ($249.6M), Raydium AMM ($191.9M), pump.fun ($168.2M), PumpSwap ($142.1M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 665 / 14 |
| Delinquent stake | 1.07% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.3% |
| Avg / median commission | 12.5% / 5% |
| Alpenglow BLS-key readiness | 710 validators, 99.4% of stake |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L43ZWjwCHART3o…` | 17,103,015 | 3.9% | 7% |
| 2 | `he1iusunGwqrNtafDtLd…` | 15,937,532 | 3.63% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5…` | 12,537,315 | 2.86% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxb…` | 10,930,434 | 2.49% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxA…` | 9,717,707 | 2.22% | 5% |
| 6 | `51JBzSTU5rAM8gLAVQKg…` | 9,482,037 | 2.16% | 10% |
| 7 | `26pV97Ce83ZQ6Kz9XT4t…` | 9,253,756 | 2.11% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2Fp…` | 7,792,210 | 1.78% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJn…` | 7,034,138 | 1.6% | 5% |
| 10 | `DumiCKHVqoCQKD8roLAp…` | 7,000,331 | 1.6% | 0% |

## Signals (anomaly detection)

All clear — no anomalies across monitored metrics.

## Solana Pulse — sentiment (experimental)

**58/100 — Neutral** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 50.0 |
| fear greed | 55 |
| momentum | 52.9 |
| news | 90 |

Crypto Fear & Greed: 55 (Greed) · CoinGecko votes bullish: 50.0% · headline tone (48h): +5

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 181 |
| Raydium AMM v4 | 162 |
| Orca Whirlpool | 181 |
| Pump.fun | 206 |
| Tensor | 1 |
| Magic Eden v2 | 122 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 11,175,975 |
| Binance (cold) | 1,388,974 |
| OKX (attributed) | 330,778 |
| Coinbase (hot) | 19,407 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 217ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 99.4% of stake.
- **Agave**: latest release v4.3.2 · running 4.3.2 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

### Latest ecosystem news (solana.com)

- [Geo-Aware Leader Schedule](https://solana.com/news/geo-aware-leader-schedule) — Wed, 14 Oct 2026
- [More Breakpoint 2026 Speakers Confirmed for London](https://solana.com/news/breakpoint-2026-london-speakers-2) — Mon, 12 Oct 2026
- [Payments on Solana: September 2026 in Five Stories](https://solana.com/news/payments-on-solana-september-2026-in-five-stories) — Fri, 09 Oct 2026
- [Breakpoint 2026: Booked Breakpoint? Let's Get You Prepped (Part 2)](https://solana.com/news/breakpoint-guide-part2) — Thu, 08 Oct 2026
- [Solana Changelog: October 8, 2026](https://solana.com/news/solana-changelog-october-8-2026) — Thu, 08 Oct 2026
- [Samsung Partners with Solana to Natively Deliver Stablecoins in Samsung Wallet to 82 Million U.S. Galaxy Devices](https://solana.com/news/samsung-wallet) — Wed, 07 Oct 2026

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 8927 ms |
| solana_rpc_validators | OK | 333 ms |
| coingecko | OK | 1702 ms |
| defillama_tvl | OK | 112 ms |
| defillama_dex | OK | 124 ms |
| defillama_fees | OK | 1511 ms |
| defillama_stablecoins | OK | 571 ms |
| defillama_xstocks | OK | 603 ms |
| jito_kobe | OK | 413 ms |
| stakewiz | OK | 1085 ms |
| github | OK | 800 ms |
| solana_com_news | OK | 154 ms |
| sentiment | OK | 2240 ms |
| solana_status_page | OK | 207 ms |
| solana_rpc_whales | OK | 1149 ms |
| solana_rpc_programs | OK | 1933 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*