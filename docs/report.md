# Solbeat — State of the Solana Network

> Generated 2026-10-16T19:04:20Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1059 is 60% complete (~10h remaining), with the cluster processing ~6,129 TPS (3,064 non-vote). Measured slot time is 218ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $1.0M of Real Economic Value over the last 24h ($705/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $102.82 (-3.0% / 24h). Decentralization: Nakamoto coefficient 18, 671 active validators, 0.0% of stake delinquent. Alpenglow readiness: validators holding 99% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: all clear across every monitored metric.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 457,747,234 |
| Block height | 435,783,023 |
| Epoch | 1059 (60.01% complete, ~10.4h left) |
| TPS (10 min avg) | 6,129 |
| Non-vote TPS | 3,064 |
| Slot time (measured) | 217.7 ms |
| Est. daily transactions | 482,201,545 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0037 |
| Node version | 4.3.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $102.82 (-3.0%/24h) |
| Market cap | $60.6B |
| **REV (24h)** | **$1.0M** (fees $811.0K + Jito tips $203.6K) |
| Chain TVL | $5.9B |
| Stablecoin supply | $16.2B |
| DEX volume (24h) | $2.5B (19.8%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 589,323,946 SOL |
| Inflation | 3.6% |

Top DEXs by 24h volume: BisonFi ($410.4M), PumpSwap ($252.5M), Orca DEX ($247.3M), Raydium AMM ($202.1M), Meteora DLMM ($166.6M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 671 / 9 |
| Delinquent stake | 0.0% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.3% |
| Avg / median commission | 13.0% / 5% |
| Alpenglow BLS-key readiness | 708 validators, 99.4% of stake |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L43ZWjwCHART3o…` | 17,561,701 | 4.01% | 7% |
| 2 | `he1iusunGwqrNtafDtLd…` | 15,460,528 | 3.53% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5…` | 12,362,555 | 2.82% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxb…` | 11,093,074 | 2.53% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxA…` | 10,200,312 | 2.33% | 5% |
| 6 | `51JBzSTU5rAM8gLAVQKg…` | 9,428,271 | 2.15% | 10% |
| 7 | `26pV97Ce83ZQ6Kz9XT4t…` | 9,248,874 | 2.11% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2Fp…` | 7,743,557 | 1.77% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJn…` | 6,910,886 | 1.58% | 5% |
| 10 | `DumiCKHVqoCQKD8roLAp…` | 6,417,148 | 1.47% | 0% |

## Signals (anomaly detection)

All clear — no anomalies across monitored metrics.

## Solana Pulse — sentiment (experimental)

**63/100 — Bullish** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 73.9 |
| fear greed | 63 |
| momentum | 49.8 |
| news | 66 |

Crypto Fear & Greed: 63 (Greed) · CoinGecko votes bullish: 73.91% · headline tone (48h): +2

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 162 |
| Raydium AMM v4 | 162 |
| Orca Whirlpool | 181 |
| Pump.fun | 181 |
| Tensor | 1 |
| Magic Eden v2 | 64 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 11,175,972 |
| Binance (cold) | 1,357,962 |
| OKX (attributed) | 308,814 |
| Coinbase (hot) | 34,244 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 218ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 99.4% of stake.
- **Agave**: latest release v4.3.2 · running 4.3.0 on the polled node.
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
| solana_rpc | OK | 7320 ms |
| solana_rpc_validators | OK | 318 ms |
| coingecko | OK | 1787 ms |
| defillama_tvl | OK | 122 ms |
| defillama_dex | OK | 1134 ms |
| defillama_fees | OK | 1968 ms |
| defillama_stablecoins | OK | 1157 ms |
| defillama_xstocks | OK | 96 ms |
| jito_kobe | OK | 245 ms |
| stakewiz | OK | 1452 ms |
| github | OK | 1046 ms |
| solana_com_news | OK | 185 ms |
| sentiment | OK | 2460 ms |
| solana_status_page | OK | 309 ms |
| solana_rpc_whales | OK | 1121 ms |
| solana_rpc_programs | OK | 1629 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*