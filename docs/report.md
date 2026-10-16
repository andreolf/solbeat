# Solbeat — State of the Solana Network

> Generated 2026-10-16T21:54:42Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1059 is 71% complete (~8h remaining), with the cluster processing ~5,368 TPS (2,284 non-vote). Measured slot time is 217ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $1.0M of Real Economic Value over the last 24h ($707/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $104.17 (-1.6% / 24h). Decentralization: Nakamoto coefficient 18, 671 active validators, 0.0% of stake delinquent. Alpenglow readiness: validators holding 99% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: all clear across every monitored metric.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 457,794,517 |
| Block height | 435,830,292 |
| Epoch | 1059 (70.95% complete, ~7.5h left) |
| TPS (10 min avg) | 5,368 |
| Non-vote TPS | 2,284 |
| Slot time (measured) | 216.6 ms |
| Est. daily transactions | 478,356,657 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0038 |
| Node version | 4.3.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $104.17 (-1.6%/24h) |
| Market cap | $61.4B |
| **REV (24h)** | **$1.0M** (fees $811.0K + Jito tips $207.3K) |
| Chain TVL | $5.9B |
| Stablecoin supply | $16.2B |
| DEX volume (24h) | $2.5B (19.8%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 589,323,802 SOL |
| Inflation | 3.6% |

Top DEXs by 24h volume: BisonFi ($410.4M), Orca DEX ($270.2M), PumpSwap ($252.5M), Raydium AMM ($204.2M), Meteora DLMM ($166.6M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 671 / 9 |
| Delinquent stake | 0.0% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.3% |
| Avg / median commission | 13.0% / 5% |
| Alpenglow BLS-key readiness | 708 validators, 99.4% of stake |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L43ZWjwCHART3o…` | 17,561,701 | 4.01% | 7% |
| 2 | `he1iusunGwqrNtafDtLd…` | 15,460,528 | 3.53% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5…` | 12,362,555 | 2.82% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxb…` | 11,093,074 | 2.53% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxA…` | 10,200,312 | 2.33% | 5% |
| 6 | `51JBzSTU5rAM8gLAVQKg…` | 9,428,271 | 2.15% | 10% |
| 7 | `26pV97Ce83ZQ6Kz9XT4t…` | 9,248,874 | 2.11% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2Fp…` | 7,743,557 | 1.77% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJn…` | 6,910,886 | 1.58% | 5% |
| 10 | `DumiCKHVqoCQKD8roLAp…` | 6,417,148 | 1.47% | 0% |

## Signals (anomaly detection)

All clear — no anomalies across monitored metrics.

## Solana Pulse — sentiment (experimental)

**62/100 — Bullish** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 70.8 |
| fear greed | 63 |
| momentum | 50.8 |
| news | 66 |

Crypto Fear & Greed: 63 (Greed) · CoinGecko votes bullish: 70.83% · headline tone (48h): +2

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 193 |
| Raydium AMM v4 | 171 |
| Orca Whirlpool | 193 |
| Pump.fun | 193 |
| Tensor | 0 |
| Magic Eden v2 | 69 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 11,175,972 |
| Binance (cold) | 1,371,714 |
| OKX (attributed) | 308,814 |
| Coinbase (hot) | 33,767 |

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
| solana_rpc | OK | 7596 ms |
| solana_rpc_validators | OK | 202 ms |
| coingecko | OK | 1754 ms |
| defillama_tvl | OK | 119 ms |
| defillama_dex | OK | 1212 ms |
| defillama_fees | OK | 2055 ms |
| defillama_stablecoins | OK | 68 ms |
| defillama_xstocks | OK | 20 ms |
| jito_kobe | OK | 130 ms |
| stakewiz | OK | 1437 ms |
| github | OK | 867 ms |
| solana_com_news | OK | 61 ms |
| sentiment | OK | 2331 ms |
| solana_status_page | OK | 352 ms |
| solana_rpc_whales | OK | 1062 ms |
| solana_rpc_programs | OK | 1859 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*