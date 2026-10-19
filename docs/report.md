# Solbeat — State of the Solana Network

> Generated 2026-10-19T14:56:15Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1062 is 21% complete (~20h remaining), with the cluster processing ~6,109 TPS (3,041 non-vote). Measured slot time is 216ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $769.5K of Real Economic Value over the last 24h ($534/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $104.41 (+2.4% / 24h). Decentralization: Nakamoto coefficient 18, 667 active validators, 0.0% of stake delinquent. Alpenglow readiness: validators holding 99% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 1 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 458,874,298 |
| Block height | 436,909,482 |
| Epoch | 1062 (20.9% complete, ~20.5h left) |
| TPS (10 min avg) | 6,109 |
| Non-vote TPS | 3,041 |
| Slot time (measured) | 216.5 ms |
| Est. daily transactions | 445,376,153 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0035 |
| Node version | 4.3.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $104.41 (+2.4%/24h) |
| Market cap | $61.5B |
| **REV (24h)** | **$769.5K** (fees $641.3K + Jito tips $128.1K) |
| Chain TVL | $5.9B |
| Stablecoin supply | $15.8B |
| DEX volume (24h) | $1.7B (35.5%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 589,493,965 SOL |
| Inflation | 3.6% |

Top DEXs by 24h volume: PumpSwap ($467.3M), BisonFi ($236.0M), Orca DEX ($205.4M), pump.fun ($140.8M), Raydium AMM ($122.5M)

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

- **[WARNING]** TPS spike: 6,109 vs 12h mean 5,112 (z=+2.0)

## Solana Pulse — sentiment (experimental)

**63/100 — Bullish** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 70.0 |
| fear greed | 59 |
| momentum | 58.1 |
| news | 66 |

Crypto Fear & Greed: 59 (Greed) · CoinGecko votes bullish: 70.0% · headline tone (48h): +2

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 194 |
| Raydium AMM v4 | 140 |
| Orca Whirlpool | 172 |
| Pump.fun | 223 |
| Tensor | 0 |
| Magic Eden v2 | 154 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 11,175,972 |
| Binance (cold) | 1,427,541 |
| OKX (attributed) | 328,740 |
| Coinbase (hot) | 22,735 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 216ms · proposal merged.
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
| solana_rpc | OK | 9358 ms |
| solana_rpc_validators | OK | 290 ms |
| coingecko | OK | 1763 ms |
| defillama_tvl | OK | 805 ms |
| defillama_dex | OK | 910 ms |
| defillama_fees | OK | 1581 ms |
| defillama_stablecoins | OK | 183 ms |
| defillama_xstocks | OK | 588 ms |
| jito_kobe | OK | 332 ms |
| stakewiz | OK | 1036 ms |
| github | OK | 828 ms |
| solana_com_news | OK | 409 ms |
| sentiment | OK | 2304 ms |
| solana_status_page | OK | 242 ms |
| solana_rpc_whales | OK | 1171 ms |
| solana_rpc_programs | OK | 2174 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*