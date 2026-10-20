# Solbeat — State of the Solana Network

> Generated 2026-10-20T03:05:26Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1062 is 67% complete (~9h remaining), with the cluster processing ~4,928 TPS (1,894 non-vote). Measured slot time is 219ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $908.9K of Real Economic Value over the last 24h ($631/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $105.09 (-0.2% / 24h). Decentralization: Nakamoto coefficient 18, 668 active validators, 0.0% of stake delinquent. Alpenglow readiness: validators holding 99% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: all clear across every monitored metric.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 459,074,875 |
| Block height | 437,109,991 |
| Epoch | 1062 (67.33% complete, ~8.6h left) |
| TPS (10 min avg) | 4,928 |
| Non-vote TPS | 1,894 |
| Slot time (measured) | 219.2 ms |
| Est. daily transactions | 420,500,369 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0050 |
| Node version | 4.3.2 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $105.09 (-0.2%/24h) |
| Market cap | $62.0B |
| **REV (24h)** | **$908.9K** (fees $781.5K + Jito tips $127.4K) |
| Chain TVL | $5.8B |
| Stablecoin supply | $15.8B |
| DEX volume (24h) | $1.6B (-5.1%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 589,493,382 SOL |
| Inflation | 3.6% |

Top DEXs by 24h volume: BisonFi ($236.0M), Orca DEX ($235.1M), Raydium AMM ($167.5M), PumpSwap ($142.1M), pump.fun ($140.8M)

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
| community | 65.0 |
| fear greed | 55 |
| momentum | 43.6 |
| news | 58 |

Crypto Fear & Greed: 55 (Greed) · CoinGecko votes bullish: 65.0% · headline tone (48h): +1

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 194 |
| Raydium AMM v4 | 172 |
| Orca Whirlpool | 194 |
| Pump.fun | 223 |
| Tensor | 0 |
| Magic Eden v2 | 76 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 11,175,972 |
| Binance (cold) | 1,410,528 |
| OKX (attributed) | 330,778 |
| Coinbase (hot) | 16,100 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 219ms · proposal merged.
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
| solana_rpc | OK | 8435 ms |
| solana_rpc_validators | OK | 295 ms |
| coingecko | OK | 1653 ms |
| defillama_tvl | OK | 259 ms |
| defillama_dex | OK | 861 ms |
| defillama_fees | OK | 3211 ms |
| defillama_stablecoins | OK | 999 ms |
| defillama_xstocks | OK | 65 ms |
| jito_kobe | OK | 260 ms |
| stakewiz | OK | 1584 ms |
| github | OK | 903 ms |
| solana_com_news | OK | 179 ms |
| sentiment | OK | 2247 ms |
| solana_status_page | OK | 239 ms |
| solana_rpc_whales | OK | 1330 ms |
| solana_rpc_programs | OK | 2186 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*