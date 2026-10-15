# Solbeat — State of the Solana Network

> Generated 2026-10-15T12:17:47Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1058 is 41% complete (~15h remaining), with the cluster processing ~5,023 TPS (1,919 non-vote). Measured slot time is 215ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $930.6K of Real Economic Value over the last 24h ($646/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $102.17 (-5.0% / 24h). Decentralization: Nakamoto coefficient 18, 671 active validators, 0.0% of stake delinquent. Alpenglow readiness: validators holding 99% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: all clear across every monitored metric.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 457,234,686 |
| Block height | 435,270,566 |
| Epoch | 1058 (41.36% complete, ~15.1h left) |
| TPS (10 min avg) | 5,023 |
| Non-vote TPS | 1,919 |
| Slot time (measured) | 215.0 ms |
| Est. daily transactions | 406,165,861 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0055 |
| Node version | 4.3.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $102.17 (-5.0%/24h) |
| Market cap | $60.2B |
| **REV (24h)** | **$930.6K** (fees $753.1K + Jito tips $177.5K) |
| Chain TVL | $5.9B |
| Stablecoin supply | $16.0B |
| DEX volume (24h) | $2.1B (-15.1%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 589,268,634 SOL |
| Inflation | 3.6% |

Top DEXs by 24h volume: Orca DEX ($382.2M), BisonFi ($381.4M), PumpSwap ($252.5M), Raydium AMM ($187.7M), pump.fun ($151.4M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 671 / 9 |
| Delinquent stake | 0.01% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.5% |
| Avg / median commission | 12.7% / 5% |
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
| community | 61.9 |
| fear greed | 53 |
| momentum | 27.5 |
| news | 58 |

Crypto Fear & Greed: 53 (Neutral) · CoinGecko votes bullish: 61.9% · headline tone (48h): +1

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 162 |
| Raydium AMM v4 | 182 |
| Orca Whirlpool | 182 |
| Pump.fun | 182 |
| Tensor | 0 |
| Magic Eden v2 | 35 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 11,175,972 |
| Binance (cold) | 1,346,433 |
| OKX (attributed) | 308,814 |
| Coinbase (hot) | 116,501 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 215ms · proposal merged.
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
| solana_rpc | OK | 9861 ms |
| solana_rpc_validators | OK | 212 ms |
| coingecko | OK | 1707 ms |
| defillama_tvl | OK | 503 ms |
| defillama_dex | OK | 874 ms |
| defillama_fees | OK | 1145 ms |
| defillama_stablecoins | OK | 413 ms |
| defillama_xstocks | OK | 97 ms |
| jito_kobe | OK | 200 ms |
| stakewiz | OK | 953 ms |
| github | OK | 892 ms |
| solana_com_news | OK | 123 ms |
| sentiment | OK | 2445 ms |
| solana_status_page | OK | 312 ms |
| solana_rpc_whales | OK | 1075 ms |
| solana_rpc_programs | OK | 1983 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*