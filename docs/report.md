# Solbeat — State of the Solana Network

> Generated 2026-10-19T13:55:11Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1062 is 17% complete (~22h remaining), with the cluster processing ~5,816 TPS (2,767 non-vote). Measured slot time is 217ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $768.9K of Real Economic Value over the last 24h ($534/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $104.39 (+1.4% / 24h). Decentralization: Nakamoto coefficient 18, 667 active validators, 0.0% of stake delinquent. Alpenglow readiness: validators holding 99% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 1 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 458,857,362 |
| Block height | 436,892,548 |
| Epoch | 1062 (16.98% complete, ~21.7h left) |
| TPS (10 min avg) | 5,816 |
| Non-vote TPS | 2,767 |
| Slot time (measured) | 217.4 ms |
| Est. daily transactions | 424,225,405 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0040 |
| Node version | 4.3.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $104.39 (+1.4%/24h) |
| Market cap | $61.6B |
| **REV (24h)** | **$768.9K** (fees $641.3K + Jito tips $127.6K) |
| Chain TVL | $5.9B |
| Stablecoin supply | $15.8B |
| DEX volume (24h) | $1.7B (35.5%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 589,494,018 SOL |
| Inflation | 3.6% |

Top DEXs by 24h volume: PumpSwap ($467.3M), BisonFi ($236.0M), Orca DEX ($205.4M), pump.fun ($140.8M), Raydium AMM ($116.9M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 667 / 12 |
| Delinquent stake | 0.02% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.3% |
| Avg / median commission | 12.9% / 5% |
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

- **[WARNING]** TPS spike: 5,816 vs 12h mean 4,873 (z=+2.6)

## Solana Pulse — sentiment (experimental)

**63/100 — Bullish** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 70.0 |
| fear greed | 59 |
| momentum | 58.0 |
| news | 66 |

Crypto Fear & Greed: 59 (Greed) · CoinGecko votes bullish: 70.0% · headline tone (48h): +2

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 191 |
| Raydium AMM v4 | 169 |
| Orca Whirlpool | 169 |
| Pump.fun | 191 |
| Tensor | 0 |
| Magic Eden v2 | 66 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 11,175,972 |
| Binance (cold) | 1,422,785 |
| OKX (attributed) | 328,740 |
| Coinbase (hot) | 22,947 |

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
| solana_rpc | OK | 10010 ms |
| solana_rpc_validators | OK | 307 ms |
| coingecko | OK | 1726 ms |
| defillama_tvl | OK | 1349 ms |
| defillama_dex | OK | 980 ms |
| defillama_fees | OK | 1103 ms |
| defillama_stablecoins | OK | 1053 ms |
| defillama_xstocks | OK | 4048 ms |
| jito_kobe | OK | 349 ms |
| stakewiz | OK | 1164 ms |
| github | OK | 795 ms |
| solana_com_news | OK | 135 ms |
| sentiment | OK | 2295 ms |
| solana_status_page | OK | 412 ms |
| solana_rpc_whales | OK | 1190 ms |
| solana_rpc_programs | OK | 2071 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*