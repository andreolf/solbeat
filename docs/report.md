# Solbeat — State of the Solana Network

> Generated 2026-10-16T00:20:24Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1058 is 88% complete (~3h remaining), with the cluster processing ~5,022 TPS (1,930 non-vote). Measured slot time is 216ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $935.4K of Real Economic Value over the last 24h ($650/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $105.48 (+1.2% / 24h). Decentralization: Nakamoto coefficient 18, 672 active validators, 0.0% of stake delinquent. Alpenglow readiness: validators holding 99% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: all clear across every monitored metric.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 457,435,140 |
| Block height | 435,470,982 |
| Epoch | 1058 (87.76% complete, ~3.2h left) |
| TPS (10 min avg) | 5,022 |
| Non-vote TPS | 1,930 |
| Slot time (measured) | 216.1 ms |
| Est. daily transactions | 444,777,320 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0042 |
| Node version | 4.3.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $105.48 (+1.2%/24h) |
| Market cap | $62.1B |
| **REV (24h)** | **$935.4K** (fees $753.1K + Jito tips $182.3K) |
| Chain TVL | $6.0B |
| Stablecoin supply | $16.0B |
| DEX volume (24h) | $2.1B (-15.1%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 589,268,036 SOL |
| Inflation | 3.6% |

Top DEXs by 24h volume: BisonFi ($381.4M), Orca DEX ($380.9M), PumpSwap ($252.5M), Raydium AMM ($241.7M), pump.fun ($151.4M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 672 / 9 |
| Delinquent stake | 0.0% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.5% |
| Avg / median commission | 13.0% / 5.0% |
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

**53/100 — Neutral** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 70.0 |
| fear greed | 63 |
| momentum | 32.6 |
| news | 42 |

Crypto Fear & Greed: 63 (Greed) · CoinGecko votes bullish: 70.0% · headline tone (48h): -1

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 162 |
| Raydium AMM v4 | 182 |
| Orca Whirlpool | 182 |
| Pump.fun | 207 |
| Tensor | 0 |
| Magic Eden v2 | 28 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 11,175,972 |
| Binance (cold) | 1,324,403 |
| OKX (attributed) | 308,814 |
| Coinbase (hot) | 57,385 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 216ms · proposal merged.
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
| solana_rpc | OK | 8460 ms |
| solana_rpc_validators | OK | 376 ms |
| coingecko | OK | 1802 ms |
| defillama_tvl | OK | 497 ms |
| defillama_dex | OK | 83 ms |
| defillama_fees | OK | 3409 ms |
| defillama_stablecoins | OK | 181 ms |
| defillama_xstocks | OK | 746 ms |
| jito_kobe | OK | 187 ms |
| stakewiz | OK | 1442 ms |
| github | OK | 675 ms |
| solana_com_news | OK | 118 ms |
| sentiment | OK | 2279 ms |
| solana_status_page | OK | 306 ms |
| solana_rpc_whales | OK | 1439 ms |
| solana_rpc_programs | OK | 2341 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*