# Solbeat — State of the Solana Network

> Generated 2026-10-19T08:02:28Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1061 is 94% complete (~2h remaining), with the cluster processing ~5,402 TPS (2,345 non-vote). Measured slot time is 217ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $760.6K of Real Economic Value over the last 24h ($528/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $105.61 (+2.4% / 24h). Decentralization: Nakamoto coefficient 18, 667 active validators, 0.0% of stake delinquent. Alpenglow readiness: validators holding 99% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 1 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 458,759,594 |
| Block height | 436,794,820 |
| Epoch | 1061 (94.35% complete, ~1.5h left) |
| TPS (10 min avg) | 5,402 |
| Non-vote TPS | 2,345 |
| Slot time (measured) | 217.2 ms |
| Est. daily transactions | 404,694,249 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0046 |
| Node version | 4.3.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $105.61 (+2.4%/24h) |
| Market cap | $62.3B |
| **REV (24h)** | **$760.6K** (fees $641.3K + Jito tips $119.3K) |
| Chain TVL | $5.9B |
| Stablecoin supply | $15.8B |
| DEX volume (24h) | $1.6B (25.0%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 589,437,460 SOL |
| Inflation | 3.6% |

Top DEXs by 24h volume: PumpSwap ($467.3M), Orca DEX ($189.5M), BisonFi ($182.3M), pump.fun ($127.8M), Raydium AMM ($114.6M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 667 / 13 |
| Delinquent stake | 0.03% |
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

- **[WARNING]** TPS spike: 5,402 vs 12h mean 4,656 (z=+2.4)

## Solana Pulse — sentiment (experimental)

**67/100 — Bullish** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 84.8 |
| fear greed | 59 |
| momentum | 57.1 |
| news | 66 |

Crypto Fear & Greed: 59 (Greed) · CoinGecko votes bullish: 84.85% · headline tone (48h): +2

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 152 |
| Raydium AMM v4 | 117 |
| Orca Whirlpool | 127 |
| Pump.fun | 219 |
| Tensor | 0 |
| Magic Eden v2 | 58 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 11,175,972 |
| Binance (cold) | 1,351,049 |
| OKX (attributed) | 328,740 |
| Coinbase (hot) | 23,698 |

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
| solana_rpc | OK | 7240 ms |
| solana_rpc_validators | OK | 381 ms |
| coingecko | OK | 1747 ms |
| defillama_tvl | OK | 118 ms |
| defillama_dex | OK | 1162 ms |
| defillama_fees | OK | 2045 ms |
| defillama_stablecoins | OK | 122 ms |
| defillama_xstocks | OK | 47 ms |
| jito_kobe | OK | 293 ms |
| stakewiz | OK | 1375 ms |
| github | OK | 964 ms |
| solana_com_news | OK | 145 ms |
| sentiment | OK | 2667 ms |
| solana_status_page | OK | 303 ms |
| solana_rpc_whales | OK | 1047 ms |
| solana_rpc_programs | OK | 1842 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*