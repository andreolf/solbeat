# Solbeat — State of the Solana Network

> Generated 2026-10-26T17:46:12Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1068 is 87% complete (~3h remaining), with the cluster processing ~2,915 TPS (2,915 non-vote). Measured slot time is 214ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $535.8K of Real Economic Value over the last 24h ($372/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $101.20 (-0.7% / 24h). Decentralization: Nakamoto coefficient 18, 663 active validators, 0.1% of stake delinquent. Alpenglow readiness: validators holding 100% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 1 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 461,753,924 |
| Block height | 439,781,023 |
| Epoch | 1068 (87.48% complete, ~3.2h left) |
| TPS (10 min avg) | 2,915 |
| Non-vote TPS | 2,915 |
| Slot time (measured) | 214.2 ms |
| Confirmation time (measured) | 0.21 s |
| Finality time (measured) | 0.21 s — **Alpenglow active** |
| Est. daily transactions | 233,371,316 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0019 |
| Node version | 4.3.2 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $101.20 (-0.7%/24h) |
| Market cap | $59.7B |
| **REV (24h)** | **$535.8K** (fees $434.1K + Jito tips $101.7K) |
| Chain TVL | $5.7B |
| Stablecoin supply | $15.8B |
| DEX volume (24h) | $1.4B (1.8%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 589,819,510 SOL |
| Inflation | 3.59% |

Top DEXs by 24h volume: PumpSwap ($310.9M), Orca DEX ($227.6M), Manifest Trade ($224.0M), BisonFi ($184.8M), Raydium AMM ($133.0M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 663 / 27 |
| Delinquent stake | 0.15% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.5% |
| Avg / median commission | 13.1% / 5% |
| Alpenglow BLS-key readiness | 677 validators, 100.0% of stake |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L43ZWjwCHART3o…` | 17,102,487 | 3.91% | 7% |
| 2 | `he1iusunGwqrNtafDtLd…` | 16,635,523 | 3.8% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5…` | 12,594,585 | 2.88% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxb…` | 10,882,967 | 2.49% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxA…` | 9,720,520 | 2.22% | 5% |
| 6 | `51JBzSTU5rAM8gLAVQKg…` | 9,492,382 | 2.17% | 10% |
| 7 | `26pV97Ce83ZQ6Kz9XT4t…` | 9,187,388 | 2.1% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2Fp…` | 7,787,018 | 1.78% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJn…` | 7,039,209 | 1.61% | 5% |
| 10 | `DumiCKHVqoCQKD8roLAp…` | 6,989,716 | 1.6% | 0% |

## Signals (anomaly detection)

- **[WARNING]** Real Economic Value deviating from its run-history baseline (z=-2.2)

## Solana Pulse — sentiment (experimental)

**58/100 — Neutral** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 76.7 |
| fear greed | 50 |
| momentum | 45.0 |
| news | 58 |

Crypto Fear & Greed: 50 (Neutral) · CoinGecko votes bullish: 76.67% · headline tone (48h): +1

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 814 |
| Raydium AMM v4 | 390 |
| Orca Whirlpool | 814 |
| Pump.fun | 1,500 |
| Tensor | 1 |
| Magic Eden v2 | 43 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 11,175,975 |
| Binance (cold) | 1,163,116 |
| OKX (attributed) | 330,874 |
| Coinbase (hot) | 14,059 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 214ms · proposal merged.
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
| solana_rpc | OK | 9936 ms |
| solana_rpc_validators | OK | 177 ms |
| coingecko | OK | 1973 ms |
| defillama_tvl | OK | 304 ms |
| defillama_dex | OK | 1016 ms |
| defillama_fees | OK | 1284 ms |
| defillama_stablecoins | OK | 749 ms |
| defillama_xstocks | FAILED | 734 ms |
| jito_kobe | OK | 342 ms |
| stakewiz | OK | 1555 ms |
| github | OK | 1032 ms |
| solana_com_news | OK | 115 ms |
| sentiment | OK | 2460 ms |
| solana_status_page | OK | 232 ms |
| solana_rpc_whales | OK | 903 ms |
| solana_rpc_programs | OK | 1836 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*