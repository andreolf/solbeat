# Solbeat — State of the Solana Network

> Generated 2026-10-19T11:05:06Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1062 is 6% complete (~24h remaining), with the cluster processing ~4,656 TPS (1,594 non-vote). Measured slot time is 217ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $769.4K of Real Economic Value over the last 24h ($534/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $104.68 (+0.7% / 24h). Decentralization: Nakamoto coefficient 18, 668 active validators, 0.0% of stake delinquent. Alpenglow readiness: validators holding 99% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: all clear across every monitored metric.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 458,810,283 |
| Block height | 436,845,503 |
| Epoch | 1062 (6.08% complete, ~24.5h left) |
| TPS (10 min avg) | 4,656 |
| Non-vote TPS | 1,594 |
| Slot time (measured) | 217.2 ms |
| Est. daily transactions | 407,881,174 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0045 |
| Node version | 4.3.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $104.68 (+0.7%/24h) |
| Market cap | $61.7B |
| **REV (24h)** | **$769.4K** (fees $641.3K + Jito tips $128.1K) |
| Chain TVL | $5.9B |
| Stablecoin supply | $15.8B |
| DEX volume (24h) | $1.7B (35.5%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 589,494,223 SOL |
| Inflation | 3.6% |

Top DEXs by 24h volume: PumpSwap ($467.3M), BisonFi ($236.0M), Orca DEX ($189.5M), pump.fun ($140.8M), Raydium AMM ($113.5M)

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

**63/100 — Bullish** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 71.9 |
| fear greed | 59 |
| momentum | 58.8 |
| news | 58 |

Crypto Fear & Greed: 59 (Greed) · CoinGecko votes bullish: 71.88% · headline tone (48h): +1

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 173 |
| Raydium AMM v4 | 155 |
| Orca Whirlpool | 173 |
| Pump.fun | 195 |
| Tensor | 4 |
| Magic Eden v2 | 42 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 11,175,972 |
| Binance (cold) | 1,393,933 |
| OKX (attributed) | 328,740 |
| Coinbase (hot) | 23,191 |

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
| solana_rpc | OK | 7615 ms |
| solana_rpc_validators | OK | 316 ms |
| coingecko | OK | 1681 ms |
| defillama_tvl | OK | 70 ms |
| defillama_dex | OK | 1140 ms |
| defillama_fees | OK | 1924 ms |
| defillama_stablecoins | OK | 1164 ms |
| defillama_xstocks | OK | 42 ms |
| jito_kobe | OK | 367 ms |
| stakewiz | OK | 1014 ms |
| github | OK | 1006 ms |
| solana_com_news | OK | 153 ms |
| sentiment | OK | 2300 ms |
| solana_status_page | OK | 229 ms |
| solana_rpc_whales | OK | 1255 ms |
| solana_rpc_programs | OK | 1789 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*