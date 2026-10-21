# Solbeat — State of the Solana Network

> Generated 2026-10-21T13:01:08Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1063 is 98% complete (~1h remaining), with the cluster processing ~4,578 TPS (1,510 non-vote). Measured slot time is 216ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $962.9K of Real Economic Value over the last 24h ($669/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $106.84 (+2.4% / 24h). Decentralization: Nakamoto coefficient 18, 664 active validators, 0.2% of stake delinquent. Alpenglow readiness: validators holding 99% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: all clear across every monitored metric.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 459,638,203 |
| Block height | 437,672,990 |
| Epoch | 1063 (97.73% complete, ~0.6h left) |
| TPS (10 min avg) | 4,578 |
| Non-vote TPS | 1,510 |
| Slot time (measured) | 215.7 ms |
| Est. daily transactions | 404,891,227 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0057 |
| Node version | 4.3.2 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $106.84 (+2.4%/24h) |
| Market cap | $63.0B |
| **REV (24h)** | **$962.9K** (fees $799.6K + Jito tips $163.3K) |
| Chain TVL | $6.0B |
| Stablecoin supply | $15.9B |
| DEX volume (24h) | $2.4B (33.7%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 589,548,668 SOL |
| Inflation | 3.59% |

Top DEXs by 24h volume: PumpSwap ($397.0M), BisonFi ($341.0M), Orca DEX ($278.4M), Raydium AMM ($172.3M), pump.fun ($166.4M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 664 / 13 |
| Delinquent stake | 0.16% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.3% |
| Avg / median commission | 13.2% / 5.0% |
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

**70/100 — Bullish** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 81.8 |
| fear greed | 63 |
| momentum | 66.9 |
| news | 66 |

Crypto Fear & Greed: 63 (Greed) · CoinGecko votes bullish: 81.82% · headline tone (48h): +2

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 184 |
| Raydium AMM v4 | 164 |
| Orca Whirlpool | 164 |
| Pump.fun | 210 |
| Tensor | 0 |
| Magic Eden v2 | 83 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 11,175,975 |
| Binance (cold) | 1,354,786 |
| OKX (attributed) | 330,778 |
| Coinbase (hot) | 17,508 |

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
| solana_rpc | OK | 7955 ms |
| solana_rpc_validators | OK | 126 ms |
| coingecko | OK | 1666 ms |
| defillama_tvl | OK | 190 ms |
| defillama_dex | OK | 802 ms |
| defillama_fees | OK | 5403 ms |
| defillama_stablecoins | OK | 121 ms |
| defillama_xstocks | OK | 41 ms |
| jito_kobe | OK | 326 ms |
| stakewiz | OK | 773 ms |
| github | OK | 678 ms |
| solana_com_news | OK | 79 ms |
| sentiment | OK | 2139 ms |
| solana_status_page | OK | 39148 ms |
| solana_rpc_whales | OK | 1239 ms |
| solana_rpc_programs | OK | 2147 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*