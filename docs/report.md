# Solbeat — State of the Solana Network

> Generated 2026-10-19T18:30:09Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1062 is 35% complete (~17h remaining), with the cluster processing ~5,223 TPS (2,161 non-vote). Measured slot time is 217ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $768.3K of Real Economic Value over the last 24h ($534/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $103.66 (+1.4% / 24h). Decentralization: Nakamoto coefficient 18, 668 active validators, 0.0% of stake delinquent. Alpenglow readiness: validators holding 99% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: all clear across every monitored metric.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 458,933,273 |
| Block height | 436,968,457 |
| Epoch | 1062 (34.55% complete, ~17.0h left) |
| TPS (10 min avg) | 5,223 |
| Non-vote TPS | 2,161 |
| Slot time (measured) | 216.9 ms |
| Est. daily transactions | 458,901,309 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0033 |
| Node version | 4.3.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $103.66 (+1.4%/24h) |
| Market cap | $61.1B |
| **REV (24h)** | **$768.3K** (fees $641.3K + Jito tips $127.0K) |
| Chain TVL | $5.8B |
| Stablecoin supply | $15.8B |
| DEX volume (24h) | $1.7B (35.5%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 589,493,788 SOL |
| Inflation | 3.6% |

Top DEXs by 24h volume: PumpSwap ($467.3M), Orca DEX ($242.7M), BisonFi ($236.0M), Raydium AMM ($143.4M), pump.fun ($140.8M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 668 / 11 |
| Delinquent stake | 0.0% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.3% |
| Avg / median commission | 12.9% / 5.0% |
| Alpenglow BLS-key readiness | 708 validators, 99.4% of stake |

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

**65/100 — Bullish** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 81.5 |
| fear greed | 59 |
| momentum | 56.7 |
| news | 58 |

Crypto Fear & Greed: 59 (Greed) · CoinGecko votes bullish: 81.48% · headline tone (48h): +1

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 178 |
| Raydium AMM v4 | 178 |
| Orca Whirlpool | 202 |
| Pump.fun | 202 |
| Tensor | 0 |
| Magic Eden v2 | 112 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 11,175,972 |
| Binance (cold) | 1,394,274 |
| OKX (attributed) | 328,740 |
| Coinbase (hot) | 15,899 |

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
| solana_rpc | OK | 10702 ms |
| solana_rpc_validators | OK | 326 ms |
| coingecko | OK | 1727 ms |
| defillama_tvl | OK | 932 ms |
| defillama_dex | OK | 1988 ms |
| defillama_fees | OK | 3584 ms |
| defillama_stablecoins | OK | 211 ms |
| defillama_xstocks | OK | 635 ms |
| jito_kobe | OK | 186 ms |
| stakewiz | OK | 951 ms |
| github | OK | 872 ms |
| solana_com_news | OK | 138 ms |
| sentiment | OK | 2397 ms |
| solana_status_page | OK | 340 ms |
| solana_rpc_whales | OK | 1094 ms |
| solana_rpc_programs | OK | 1990 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*