# Solbeat — State of the Solana Network

> Generated 2026-10-20T06:37:46Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1062 is 81% complete (~5h remaining), with the cluster processing ~4,493 TPS (1,418 non-vote). Measured slot time is 216ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $909.9K of Real Economic Value over the last 24h ($632/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $104.59 (-1.1% / 24h). Decentralization: Nakamoto coefficient 18, 668 active validators, 0.0% of stake delinquent. Alpenglow readiness: validators holding 99% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: all clear across every monitored metric.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 459,133,350 |
| Block height | 437,168,453 |
| Epoch | 1062 (80.87% complete, ~5.0h left) |
| TPS (10 min avg) | 4,493 |
| Non-vote TPS | 1,418 |
| Slot time (measured) | 216.4 ms |
| Est. daily transactions | 406,964,503 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0054 |
| Node version | 4.3.2 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $104.59 (-1.1%/24h) |
| Market cap | $61.7B |
| **REV (24h)** | **$909.9K** (fees $781.5K + Jito tips $128.4K) |
| Chain TVL | $5.9B |
| Stablecoin supply | $15.8B |
| DEX volume (24h) | $1.6B (-5.1%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 589,493,228 SOL |
| Inflation | 3.6% |

Top DEXs by 24h volume: Orca DEX ($243.8M), BisonFi ($236.0M), Raydium AMM ($164.8M), PumpSwap ($142.1M), pump.fun ($140.8M)

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

**54/100 — Neutral** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 60.9 |
| fear greed | 55 |
| momentum | 43.8 |
| news | 58 |

Crypto Fear & Greed: 55 (Greed) · CoinGecko votes bullish: 60.87% · headline tone (48h): +1

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 191 |
| Raydium AMM v4 | 138 |
| Orca Whirlpool | 169 |
| Pump.fun | 218 |
| Tensor | 2 |
| Magic Eden v2 | 89 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 11,175,972 |
| Binance (cold) | 1,402,837 |
| OKX (attributed) | 330,778 |
| Coinbase (hot) | 17,187 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 216ms · proposal merged.
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
| solana_rpc | OK | 7627 ms |
| solana_rpc_validators | OK | 95 ms |
| coingecko | OK | 1692 ms |
| defillama_tvl | OK | 69 ms |
| defillama_dex | OK | 421 ms |
| defillama_fees | OK | 4031 ms |
| defillama_stablecoins | OK | 93 ms |
| defillama_xstocks | OK | 34 ms |
| jito_kobe | OK | 352 ms |
| stakewiz | OK | 1037 ms |
| github | OK | 656 ms |
| solana_com_news | OK | 82 ms |
| sentiment | OK | 2122 ms |
| solana_status_page | OK | 102 ms |
| solana_rpc_whales | OK | 956 ms |
| solana_rpc_programs | OK | 1646 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*