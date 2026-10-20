# Solbeat — State of the Solana Network

> Generated 2026-10-20T15:25:37Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1063 is 15% complete (~22h remaining), with the cluster processing ~6,222 TPS (3,168 non-vote). Measured slot time is 218ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $940.5K of Real Economic Value over the last 24h ($653/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $105.25 (+0.2% / 24h). Decentralization: Nakamoto coefficient 18, 669 active validators, 0.0% of stake delinquent. Alpenglow readiness: validators holding 99% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: all clear across every monitored metric.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 459,278,868 |
| Block height | 437,313,913 |
| Epoch | 1063 (14.55% complete, ~22.4h left) |
| TPS (10 min avg) | 6,222 |
| Non-vote TPS | 3,168 |
| Slot time (measured) | 218.2 ms |
| Est. daily transactions | 455,150,442 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0041 |
| Node version | 4.3.2 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $105.25 (+0.2%/24h) |
| Market cap | $62.1B |
| **REV (24h)** | **$940.5K** (fees $781.5K + Jito tips $159.0K) |
| Chain TVL | $5.9B |
| Stablecoin supply | $15.8B |
| DEX volume (24h) | $1.8B (7.4%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 589,549,662 SOL |
| Inflation | 3.59% |

Top DEXs by 24h volume: BisonFi ($249.6M), Orca DEX ($241.8M), pump.fun ($168.2M), Raydium AMM ($159.2M), PumpSwap ($142.1M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 669 / 10 |
| Delinquent stake | 0.0% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.3% |
| Avg / median commission | 12.8% / 5% |
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

**57/100 — Neutral** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 54.2 |
| fear greed | 55 |
| momentum | 50.6 |
| news | 82 |

Crypto Fear & Greed: 55 (Greed) · CoinGecko votes bullish: 54.17% · headline tone (48h): +4

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 174 |
| Raydium AMM v4 | 174 |
| Orca Whirlpool | 174 |
| Pump.fun | 196 |
| Tensor | 0 |
| Magic Eden v2 | 54 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 11,175,975 |
| Binance (cold) | 1,362,554 |
| OKX (attributed) | 330,778 |
| Coinbase (hot) | 34,862 |

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
| solana_rpc | OK | 9765 ms |
| solana_rpc_validators | OK | 387 ms |
| coingecko | OK | 1825 ms |
| defillama_tvl | OK | 117 ms |
| defillama_dex | OK | 2490 ms |
| defillama_fees | OK | 4535 ms |
| defillama_stablecoins | OK | 258 ms |
| defillama_xstocks | OK | 7568 ms |
| jito_kobe | OK | 337 ms |
| stakewiz | OK | 1253 ms |
| github | OK | 1054 ms |
| solana_com_news | OK | 214 ms |
| sentiment | OK | 2469 ms |
| solana_status_page | OK | 499 ms |
| solana_rpc_whales | OK | 1741 ms |
| solana_rpc_programs | OK | 2460 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*