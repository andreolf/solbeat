# Solbeat — State of the Solana Network

> Generated 2026-10-20T17:27:36Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1063 is 22% complete (~20h remaining), with the cluster processing ~5,373 TPS (2,326 non-vote). Measured slot time is 218ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $942.4K of Real Economic Value over the last 24h ($654/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $106.39 (+2.2% / 24h). Decentralization: Nakamoto coefficient 18, 668 active validators, 0.0% of stake delinquent. Alpenglow readiness: validators holding 99% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: all clear across every monitored metric.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 459,312,479 |
| Block height | 437,347,508 |
| Epoch | 1063 (22.33% complete, ~20.3h left) |
| TPS (10 min avg) | 5,373 |
| Non-vote TPS | 2,326 |
| Slot time (measured) | 218.0 ms |
| Est. daily transactions | 493,604,121 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0034 |
| Node version | 4.3.2 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $106.39 (+2.2%/24h) |
| Market cap | $62.7B |
| **REV (24h)** | **$942.4K** (fees $781.5K + Jito tips $160.9K) |
| Chain TVL | $5.9B |
| Stablecoin supply | $15.8B |
| DEX volume (24h) | $1.8B (7.4%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 589,549,554 SOL |
| Inflation | 3.59% |

Top DEXs by 24h volume: Orca DEX ($280.7M), BisonFi ($249.6M), Raydium AMM ($183.6M), pump.fun ($168.2M), PumpSwap ($142.1M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 668 / 11 |
| Delinquent stake | 0.03% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.3% |
| Avg / median commission | 12.8% / 5.0% |
| Alpenglow BLS-key readiness | 710 validators, 99.4% of stake |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L43ZWjwCHART3o…` | 17,103,015 | 3.9% | 7% |
| 2 | `he1iusunGwqrNtafDtLd…` | 15,937,532 | 3.63% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5…` | 12,537,315 | 2.86% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxb…` | 10,930,434 | 2.49% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxA…` | 9,717,707 | 2.22% | 5% |
| 6 | `51JBzSTU5rAM8gLAVQKg…` | 9,482,037 | 2.16% | 10% |
| 7 | `26pV97Ce83ZQ6Kz9XT4t…` | 9,253,756 | 2.11% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2Fp…` | 7,792,210 | 1.78% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJn…` | 7,034,138 | 1.6% | 5% |
| 10 | `DumiCKHVqoCQKD8roLAp…` | 7,000,331 | 1.6% | 0% |

## Signals (anomaly detection)

All clear — no anomalies across monitored metrics.

## Solana Pulse — sentiment (experimental)

**56/100 — Neutral** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 52.2 |
| fear greed | 55 |
| momentum | 52.0 |
| news | 74 |

Crypto Fear & Greed: 55 (Greed) · CoinGecko votes bullish: 52.17% · headline tone (48h): +3

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 190 |
| Raydium AMM v4 | 152 |
| Orca Whirlpool | 190 |
| Pump.fun | 218 |
| Tensor | 1 |
| Magic Eden v2 | 54 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 11,175,975 |
| Binance (cold) | 1,483,493 |
| OKX (attributed) | 330,778 |
| Coinbase (hot) | 30,499 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 218ms · proposal merged.
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
| solana_rpc | OK | 8574 ms |
| solana_rpc_validators | OK | 253 ms |
| coingecko | OK | 1868 ms |
| defillama_tvl | OK | 451 ms |
| defillama_dex | OK | 1028 ms |
| defillama_fees | OK | 1779 ms |
| defillama_stablecoins | OK | 240 ms |
| defillama_xstocks | OK | 1253 ms |
| jito_kobe | OK | 256 ms |
| stakewiz | OK | 1220 ms |
| github | OK | 929 ms |
| solana_com_news | OK | 181 ms |
| sentiment | OK | 2367 ms |
| solana_status_page | OK | 386 ms |
| solana_rpc_whales | OK | 1282 ms |
| solana_rpc_programs | OK | 2169 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*