# Solbeat — State of the Solana Network

> Generated 2026-10-19T03:35:42Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1061 is 77% complete (~6h remaining), with the cluster processing ~5,487 TPS (2,431 non-vote). Measured slot time is 217ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $760.2K of Real Economic Value over the last 24h ($528/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $105.31 (+1.2% / 24h). Decentralization: Nakamoto coefficient 18, 667 active validators, 0.0% of stake delinquent. Alpenglow readiness: validators holding 99% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 1 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 458,685,645 |
| Block height | 436,720,883 |
| Epoch | 1061 (77.23% complete, ~5.9h left) |
| TPS (10 min avg) | 5,487 |
| Non-vote TPS | 2,431 |
| Slot time (measured) | 217.3 ms |
| Est. daily transactions | 419,074,594 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0041 |
| Node version | 4.3.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $105.31 (+1.2%/24h) |
| Market cap | $62.1B |
| **REV (24h)** | **$760.2K** (fees $641.3K + Jito tips $118.9K) |
| Chain TVL | $5.9B |
| Stablecoin supply | $15.8B |
| DEX volume (24h) | $1.6B (25.0%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 589,437,653 SOL |
| Inflation | 3.6% |

Top DEXs by 24h volume: PumpSwap ($467.3M), BisonFi ($182.3M), Orca DEX ($180.4M), pump.fun ($127.8M), Raydium AMM ($110.8M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 667 / 13 |
| Delinquent stake | 0.0% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.3% |
| Avg / median commission | 13.2% / 5% |
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

- **[WARNING]** TPS spike: 5,487 vs 12h mean 4,824 (z=+2.3)

## Solana Pulse — sentiment (experimental)

**67/100 — Bullish** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 85.7 |
| fear greed | 59 |
| momentum | 56.3 |
| news | 66 |

Crypto Fear & Greed: 59 (Greed) · CoinGecko votes bullish: 85.71% · headline tone (48h): +2

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 204 |
| Raydium AMM v4 | 160 |
| Orca Whirlpool | 180 |
| Pump.fun | 236 |
| Tensor | 1 |
| Magic Eden v2 | 67 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 11,175,972 |
| Binance (cold) | 1,412,853 |
| OKX (attributed) | 328,740 |
| Coinbase (hot) | 24,682 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 217ms · proposal merged.
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
| solana_rpc | OK | 8508 ms |
| solana_rpc_validators | OK | 450 ms |
| coingecko | OK | 1809 ms |
| defillama_tvl | OK | 171 ms |
| defillama_dex | OK | 1608 ms |
| defillama_fees | OK | 20120 ms |
| defillama_stablecoins | OK | 709 ms |
| defillama_xstocks | OK | 710 ms |
| jito_kobe | OK | 360 ms |
| stakewiz | OK | 1258 ms |
| github | OK | 887 ms |
| solana_com_news | OK | 148 ms |
| sentiment | OK | 2530 ms |
| solana_status_page | OK | 427 ms |
| solana_rpc_whales | OK | 1259 ms |
| solana_rpc_programs | OK | 2290 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*