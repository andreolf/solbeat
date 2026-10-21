# Solbeat — State of the Solana Network

> Generated 2026-10-21T22:45:52Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1064 is 36% complete (~16h remaining), with the cluster processing ~3,324 TPS (3,324 non-vote). Measured slot time is 215ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $942.9K of Real Economic Value over the last 24h ($655/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $107.53 (+0.6% / 24h). Decentralization: Nakamoto coefficient 18, 667 active validators, 0.0% of stake delinquent. Alpenglow readiness: validators holding 99% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: all clear across every monitored metric.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 459,802,928 |
| Block height | 437,837,018 |
| Epoch | 1064 (35.86% complete, ~16.5h left) |
| TPS (10 min avg) | 3,324 |
| Non-vote TPS | 3,324 |
| Slot time (measured) | 214.9 ms |
| Confirmation time (measured) | 0.0 s |
| Finality time (measured) | 0.0 s — **Alpenglow active** |
| Est. daily transactions | 206,534,812 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0039 |
| Node version | 4.3.2 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $107.53 (+0.6%/24h) |
| Market cap | $63.4B |
| **REV (24h)** | **$942.9K** (fees $799.6K + Jito tips $143.3K) |
| Chain TVL | $6.0B |
| Stablecoin supply | $15.9B |
| DEX volume (24h) | $2.4B (33.7%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 589,604,707 SOL |
| Inflation | 3.59% |

Top DEXs by 24h volume: PumpSwap ($397.0M), BisonFi ($341.0M), Orca DEX ($236.7M), Raydium AMM ($194.6M), pump.fun ($166.4M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 667 / 9 |
| Delinquent stake | 0.01% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.4% |
| Avg / median commission | 12.9% / 5% |
| Alpenglow BLS-key readiness | 710 validators, 99.3% of stake |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L43ZWjwCHART3o…` | 17,130,984 | 3.9% | 7% |
| 2 | `he1iusunGwqrNtafDtLd…` | 15,955,653 | 3.64% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5…` | 12,545,894 | 2.86% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxb…` | 10,933,491 | 2.49% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxA…` | 9,728,193 | 2.22% | 5% |
| 6 | `51JBzSTU5rAM8gLAVQKg…` | 9,480,474 | 2.16% | 10% |
| 7 | `26pV97Ce83ZQ6Kz9XT4t…` | 9,252,296 | 2.11% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2Fp…` | 7,808,122 | 1.78% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJn…` | 7,035,085 | 1.6% | 5% |
| 10 | `DumiCKHVqoCQKD8roLAp…` | 7,001,557 | 1.6% | 0% |

## Signals (anomaly detection)

All clear — no anomalies across monitored metrics.

## Solana Pulse — sentiment (experimental)

**76/100 — Bullish** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 96.3 |
| fear greed | 63 |
| momentum | 68.3 |
| news | 74 |

Crypto Fear & Greed: 63 (Greed) · CoinGecko votes bullish: 96.3% · headline tone (48h): +3

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 1,319 |
| Raydium AMM v4 | 1,319 |
| Orca Whirlpool | 1,319 |
| Pump.fun | 1,500 |
| Tensor | 0 |
| Magic Eden v2 | 71 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 11,175,975 |
| Binance (cold) | 1,384,246 |
| OKX (attributed) | 330,778 |
| Coinbase (hot) | 13,975 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 215ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 99.3% of stake.
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
| solana_rpc | OK | 10696 ms |
| solana_rpc_validators | OK | 338 ms |
| coingecko | OK | 1704 ms |
| defillama_tvl | OK | 131 ms |
| defillama_dex | OK | 1249 ms |
| defillama_fees | OK | 1993 ms |
| defillama_stablecoins | OK | 100 ms |
| defillama_xstocks | FAILED | 809 ms |
| jito_kobe | OK | 458 ms |
| stakewiz | OK | 1534 ms |
| github | OK | 686 ms |
| solana_com_news | OK | 129 ms |
| sentiment | OK | 2289 ms |
| solana_status_page | OK | 4030 ms |
| solana_rpc_whales | OK | 1194 ms |
| solana_rpc_programs | OK | 2201 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*