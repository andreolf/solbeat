# Solbeat — State of the Solana Network

> Generated 2026-10-20T01:03:39Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1062 is 60% complete (~11h remaining), with the cluster processing ~4,782 TPS (1,753 non-vote). Measured slot time is 220ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $767.8K of Real Economic Value over the last 24h ($533/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $104.57 (+0.3% / 24h). Decentralization: Nakamoto coefficient 18, 668 active validators, 0.0% of stake delinquent. Alpenglow readiness: validators holding 99% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: all clear across every monitored metric.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 459,041,445 |
| Block height | 437,076,561 |
| Epoch | 1062 (59.59% complete, ~10.7h left) |
| TPS (10 min avg) | 4,782 |
| Non-vote TPS | 1,753 |
| Slot time (measured) | 219.7 ms |
| Est. daily transactions | 448,323,312 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0037 |
| Node version | 4.3.2 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $104.57 (+0.3%/24h) |
| Market cap | $61.7B |
| **REV (24h)** | **$767.8K** (fees $641.3K + Jito tips $126.5K) |
| Chain TVL | $5.8B |
| Stablecoin supply | $15.8B |
| DEX volume (24h) | $1.6B (-5.0%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 589,493,474 SOL |
| Inflation | 3.6% |

Top DEXs by 24h volume: Orca DEX ($240.0M), BisonFi ($236.0M), Raydium AMM ($167.0M), PumpSwap ($142.1M), pump.fun ($140.8M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 668 / 11 |
| Delinquent stake | 0.0% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.3% |
| Avg / median commission | 13.2% / 5.0% |
| Alpenglow BLS-key readiness | 709 validators, 99.4% of stake |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L43ZWjwCHART3o…` | 17,095,415 | 3.9% | 7% |
| 2 | `he1iusunGwqrNtafDtLd…` | 15,730,365 | 3.59% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5…` | 12,524,168 | 2.86% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxb…` | 10,975,836 | 2.51% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxA…` | 9,717,890 | 2.22% | 5% |
| 6 | `51JBzSTU5rAM8gLAVQKg…` | 9,481,609 | 2.17% | 10% |
| 7 | `26pV97Ce83ZQ6Kz9XT4t…` | 9,252,107 | 2.11% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2Fp…` | 7,785,119 | 1.78% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJn…` | 6,993,888 | 1.6% | 5% |
| 10 | `DumiCKHVqoCQKD8roLAp…` | 6,731,556 | 1.54% | 0% |

## Signals (anomaly detection)

All clear — no anomalies across monitored metrics.

## Solana Pulse — sentiment (experimental)

**55/100 — Neutral** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 70.0 |
| fear greed | 55 |
| momentum | 39.3 |
| news | 58 |

Crypto Fear & Greed: 55 (Greed) · CoinGecko votes bullish: 70.0% · headline tone (48h): +1

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 204 |
| Raydium AMM v4 | 179 |
| Orca Whirlpool | 204 |
| Pump.fun | 236 |
| Tensor | 0 |
| Magic Eden v2 | 59 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 11,175,972 |
| Binance (cold) | 1,394,996 |
| OKX (attributed) | 330,778 |
| Coinbase (hot) | 16,285 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 220ms · proposal merged.
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
| solana_rpc | OK | 11991 ms |
| solana_rpc_validators | OK | 222 ms |
| coingecko | OK | 1907 ms |
| defillama_tvl | OK | 362 ms |
| defillama_dex | OK | 1230 ms |
| defillama_fees | OK | 1929 ms |
| defillama_stablecoins | OK | 326 ms |
| defillama_xstocks | OK | 679 ms |
| jito_kobe | OK | 296 ms |
| stakewiz | OK | 791 ms |
| github | OK | 792 ms |
| solana_com_news | OK | 95 ms |
| sentiment | OK | 2389 ms |
| solana_status_page | OK | 254 ms |
| solana_rpc_whales | OK | 1213 ms |
| solana_rpc_programs | OK | 1888 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*