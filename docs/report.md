# Solbeat — State of the Solana Network

> Generated 2026-10-27T07:34:18Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1069 is 42% complete (~15h remaining), with the cluster processing ~1,199 TPS (1,199 non-vote). Measured slot time is 212ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $707.6K of Real Economic Value over the last 24h ($491/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $99.63 (-1.0% / 24h). Decentralization: Nakamoto coefficient 18, 665 active validators, 0.1% of stake delinquent. Alpenglow readiness: validators holding 100% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: all clear across every monitored metric.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 461,987,576 |
| Block height | 440,013,373 |
| Epoch | 1069 (41.57% complete, ~14.9h left) |
| TPS (10 min avg) | 1,199 |
| Non-vote TPS | 1,199 |
| Slot time (measured) | 211.8 ms |
| Confirmation time (measured) | 0.21 s |
| Finality time (measured) | 0.21 s — **Alpenglow active** |
| Est. daily transactions | 134,572,512 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0042 |
| Node version | 4.3.2 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $99.63 (-1.0%/24h) |
| Market cap | $58.8B |
| **REV (24h)** | **$707.6K** (fees $568.3K + Jito tips $139.2K) |
| Chain TVL | $5.7B |
| Stablecoin supply | $15.7B |
| DEX volume (24h) | $1.7B (18.4%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 589,874,647 SOL |
| Inflation | 3.58% |

Top DEXs by 24h volume: Manifest Trade ($298.6M), Orca DEX ($214.3M), BisonFi ($184.8M), PumpSwap ($167.0M), Raydium AMM ($141.2M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 665 / 20 |
| Delinquent stake | 0.09% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.6% |
| Avg / median commission | 12.8% / 5% |
| Alpenglow BLS-key readiness | 676 validators, 100.0% of stake |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L43ZWjwCHART3o…` | 17,059,304 | 3.9% | 7% |
| 2 | `he1iusunGwqrNtafDtLd…` | 16,636,453 | 3.81% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5…` | 12,660,117 | 2.9% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxb…` | 10,812,577 | 2.47% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxA…` | 9,716,980 | 2.22% | 5% |
| 6 | `51JBzSTU5rAM8gLAVQKg…` | 9,494,053 | 2.17% | 10% |
| 7 | `26pV97Ce83ZQ6Kz9XT4t…` | 9,206,552 | 2.11% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2Fp…` | 7,754,189 | 1.77% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJn…` | 7,040,177 | 1.61% | 5% |
| 10 | `DumiCKHVqoCQKD8roLAp…` | 6,996,375 | 1.6% | 0% |

## Signals (anomaly detection)

All clear — no anomalies across monitored metrics.

## Solana Pulse — sentiment (experimental)

**56/100 — Neutral** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 75.0 |
| fear greed | 48 |
| momentum | 50.1 |
| news | 42 |

Crypto Fear & Greed: 48 (Neutral) · CoinGecko votes bullish: 75.0% · headline tone (48h): -1

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 513 |
| Raydium AMM v4 | 513 |
| Orca Whirlpool | 513 |
| Pump.fun | 1,500 |
| Tensor | 0 |
| Magic Eden v2 | 58 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 11,175,975 |
| Binance (cold) | 1,266,001 |
| OKX (attributed) | 330,874 |
| Coinbase (hot) | 15,178 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 212ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 100.0% of stake.
- **Agave**: latest release v4.3.2 · running 4.3.2 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

### Latest ecosystem news (solana.com)

- [Solana Changelog: October 22, 2026](https://solana.com/news/solana-changelog-october-22-2026) — Fri, 23 Oct 2026
- [Solana Changelog: October 16, 2026](https://solana.com/news/solana-changelog-october-16-2026) — Fri, 16 Oct 2026
- [Geo-Aware Leader Schedule](https://solana.com/news/geo-aware-leader-schedule) — Wed, 14 Oct 2026
- [More Breakpoint 2026 Speakers Confirmed for London](https://solana.com/news/breakpoint-2026-london-speakers-2) — Mon, 12 Oct 2026
- [Payments on Solana: September 2026 in Five Stories](https://solana.com/news/payments-on-solana-september-2026-in-five-stories) — Fri, 09 Oct 2026
- [Breakpoint 2026: Booked Breakpoint? Let's Get You Prepped (Part 2)](https://solana.com/news/breakpoint-guide-part2) — Thu, 08 Oct 2026

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 9855 ms |
| solana_rpc_validators | OK | 332 ms |
| coingecko | OK | 1730 ms |
| defillama_tvl | OK | 986 ms |
| defillama_dex | OK | 675 ms |
| defillama_fees | OK | 2058 ms |
| defillama_stablecoins | OK | 741 ms |
| defillama_xstocks | FAILED | 838 ms |
| jito_kobe | OK | 388 ms |
| stakewiz | OK | 1041 ms |
| github | OK | 698 ms |
| solana_com_news | OK | 121 ms |
| sentiment | OK | 2258 ms |
| solana_status_page | OK | 289 ms |
| solana_rpc_whales | OK | 1153 ms |
| solana_rpc_programs | OK | 2281 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*