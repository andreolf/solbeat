# Solbeat — State of the Solana Network

> Generated 2026-10-18T20:29:14Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1061 is 50% complete (~13h remaining), with the cluster processing ~5,074 TPS (1,997 non-vote). Measured slot time is 216ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $737.5K of Real Economic Value over the last 24h ($512/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $101.05 (-2.9% / 24h). Decentralization: Nakamoto coefficient 18, 668 active validators, 0.0% of stake delinquent. Alpenglow readiness: validators holding 99% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: all clear across every monitored metric.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 458,567,803 |
| Block height | 436,603,049 |
| Epoch | 1061 (49.95% complete, ~13.0h left) |
| TPS (10 min avg) | 5,074 |
| Non-vote TPS | 1,997 |
| Slot time (measured) | 216.1 ms |
| Est. daily transactions | 445,813,520 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0034 |
| Node version | 4.3.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $101.05 (-2.9%/24h) |
| Market cap | $59.5B |
| **REV (24h)** | **$737.5K** (fees $622.8K + Jito tips $114.7K) |
| Chain TVL | $5.8B |
| Stablecoin supply | $15.8B |
| DEX volume (24h) | $1.3B (-42.2%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 589,437,983 SOL |
| Inflation | 3.6% |

Top DEXs by 24h volume: PumpSwap ($194.5M), BisonFi ($182.3M), Orca DEX ($168.7M), pump.fun ($127.8M), Tessera V ($94.0M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 668 / 12 |
| Delinquent stake | 0.0% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.3% |
| Avg / median commission | 13.2% / 5.0% |
| Alpenglow BLS-key readiness | 708 validators, 99.4% of stake |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L43ZWjwCHART3o…` | 17,091,304 | 3.91% | 7% |
| 2 | `he1iusunGwqrNtafDtLd…` | 15,762,758 | 3.6% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5…` | 12,523,730 | 2.86% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxb…` | 10,974,352 | 2.51% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxA…` | 9,718,484 | 2.22% | 5% |
| 6 | `51JBzSTU5rAM8gLAVQKg…` | 9,466,253 | 2.16% | 10% |
| 7 | `26pV97Ce83ZQ6Kz9XT4t…` | 9,251,164 | 2.12% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2Fp…` | 7,774,268 | 1.78% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJn…` | 6,992,811 | 1.6% | 5% |
| 10 | `DumiCKHVqoCQKD8roLAp…` | 6,730,670 | 1.54% | 0% |

## Signals (anomaly detection)

All clear — no anomalies across monitored metrics.

## Solana Pulse — sentiment (experimental)

**53/100 — Neutral** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 76.5 |
| fear greed | 53 |
| momentum | 20.5 |
| news | 74 |

Crypto Fear & Greed: 53 (Neutral) · CoinGecko votes bullish: 76.47% · headline tone (48h): +3

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 170 |
| Raydium AMM v4 | 192 |
| Orca Whirlpool | 192 |
| Pump.fun | 192 |
| Tensor | 0 |
| Magic Eden v2 | 60 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 11,175,972 |
| Binance (cold) | 1,368,142 |
| OKX (attributed) | 328,740 |
| Coinbase (hot) | 16,801 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 216ms · proposal merged.
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
| solana_rpc | OK | 8519 ms |
| solana_rpc_validators | OK | 138 ms |
| coingecko | OK | 1772 ms |
| defillama_tvl | OK | 83 ms |
| defillama_dex | OK | 1269 ms |
| defillama_fees | OK | 1051 ms |
| defillama_stablecoins | OK | 156 ms |
| defillama_xstocks | OK | 788 ms |
| jito_kobe | OK | 138 ms |
| stakewiz | OK | 1008 ms |
| github | OK | 961 ms |
| solana_com_news | OK | 182 ms |
| sentiment | OK | 2378 ms |
| solana_status_page | OK | 342 ms |
| solana_rpc_whales | OK | 921 ms |
| solana_rpc_programs | OK | 1620 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*