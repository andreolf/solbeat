# Solbeat — State of the Solana Network

> Generated 2026-10-15T22:05:04Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1058 is 79% complete (~5h remaining), with the cluster processing ~5,179 TPS (2,098 non-vote). Measured slot time is 217ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $935.7K of Real Economic Value over the last 24h ($650/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $106.05 (+1.3% / 24h). Decentralization: Nakamoto coefficient 18, 671 active validators, 0.0% of stake delinquent. Alpenglow readiness: validators holding 99% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: all clear across every monitored metric.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 457,397,580 |
| Block height | 435,433,427 |
| Epoch | 1058 (79.07% complete, ~5.4h left) |
| TPS (10 min avg) | 5,179 |
| Non-vote TPS | 2,098 |
| Slot time (measured) | 216.9 ms |
| Est. daily transactions | 461,513,462 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0039 |
| Node version | 4.3.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $106.05 (+1.3%/24h) |
| Market cap | $62.5B |
| **REV (24h)** | **$935.7K** (fees $753.1K + Jito tips $182.6K) |
| Chain TVL | $6.0B |
| Stablecoin supply | $16.0B |
| DEX volume (24h) | $2.1B (-15.1%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 589,268,141 SOL |
| Inflation | 3.6% |

Top DEXs by 24h volume: Orca DEX ($384.8M), BisonFi ($381.4M), PumpSwap ($252.5M), Raydium AMM ($243.2M), pump.fun ($151.4M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 671 / 10 |
| Delinquent stake | 0.02% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.5% |
| Avg / median commission | 13.0% / 5% |
| Alpenglow BLS-key readiness | 708 validators, 99.4% of stake |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L43ZWjwCHART3o…` | 17,556,681 | 4.01% | 7% |
| 2 | `he1iusunGwqrNtafDtLd…` | 15,475,284 | 3.53% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5…` | 12,340,406 | 2.82% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxb…` | 11,132,168 | 2.54% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxA…` | 10,777,829 | 2.46% | 5% |
| 6 | `51JBzSTU5rAM8gLAVQKg…` | 9,409,309 | 2.15% | 10% |
| 7 | `26pV97Ce83ZQ6Kz9XT4t…` | 9,227,345 | 2.11% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2Fp…` | 7,737,484 | 1.77% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJn…` | 6,912,081 | 1.58% | 5% |
| 10 | `3JD3jMmnR6g88qff2WZ3…` | 6,640,641 | 1.52% | 0% |

## Signals (anomaly detection)

All clear — no anomalies across monitored metrics.

## Solana Pulse — sentiment (experimental)

**49/100 — Neutral** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 65.8 |
| fear greed | 53 |
| momentum | 32.9 |
| news | 42 |

Crypto Fear & Greed: 53 (Neutral) · CoinGecko votes bullish: 65.85% · headline tone (48h): -1

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 182 |
| Raydium AMM v4 | 162 |
| Orca Whirlpool | 182 |
| Pump.fun | 182 |
| Tensor | 0 |
| Magic Eden v2 | 40 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 11,175,972 |
| Binance (cold) | 1,366,031 |
| OKX (attributed) | 308,814 |
| Coinbase (hot) | 112,490 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 217ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 99.4% of stake.
- **Agave**: latest release v4.3.0 · running 4.3.0 on the polled node.
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
| solana_rpc | OK | 8165 ms |
| solana_rpc_validators | OK | 237 ms |
| coingecko | OK | 1757 ms |
| defillama_tvl | OK | 133 ms |
| defillama_dex | OK | 1369 ms |
| defillama_fees | OK | 259 ms |
| defillama_stablecoins | OK | 202 ms |
| defillama_xstocks | OK | 283 ms |
| jito_kobe | OK | 461 ms |
| stakewiz | OK | 1841 ms |
| github | OK | 766 ms |
| solana_com_news | OK | 73 ms |
| sentiment | OK | 2386 ms |
| solana_status_page | OK | 299 ms |
| solana_rpc_whales | OK | 1013 ms |
| solana_rpc_programs | OK | 1912 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*