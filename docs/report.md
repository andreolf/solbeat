# Solbeat — State of the Solana Network

> Generated 2026-10-16T03:54:16Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1059 is 1% complete (~26h remaining), with the cluster processing ~5,179 TPS (2,078 non-vote). Measured slot time is 216ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $993.2K of Real Economic Value over the last 24h ($690/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $105.21 (+2.9% / 24h). Decentralization: Nakamoto coefficient 18, 672 active validators, 0.0% of stake delinquent. Alpenglow readiness: validators holding 99% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: all clear across every monitored metric.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 457,494,409 |
| Block height | 435,530,239 |
| Epoch | 1059 (1.48% complete, ~25.5h left) |
| TPS (10 min avg) | 5,179 |
| Non-vote TPS | 2,078 |
| Slot time (measured) | 215.7 ms |
| Est. daily transactions | 452,722,111 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0044 |
| Node version | 4.3.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $105.21 (+2.9%/24h) |
| Market cap | $62.0B |
| **REV (24h)** | **$993.2K** (fees $811.0K + Jito tips $182.2K) |
| Chain TVL | $6.0B |
| Stablecoin supply | $16.2B |
| DEX volume (24h) | $2.4B (14.3%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 589,324,875 SOL |
| Inflation | 3.6% |

Top DEXs by 24h volume: BisonFi ($381.4M), Orca DEX ($381.2M), PumpSwap ($252.5M), Raydium AMM ($232.6M), Meteora DLMM ($166.6M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 672 / 9 |
| Delinquent stake | 0.0% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.3% |
| Avg / median commission | 12.7% / 5.0% |
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

**58/100 — Neutral** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 75.0 |
| fear greed | 63 |
| momentum | 50.4 |
| news | 34 |

Crypto Fear & Greed: 63 (Greed) · CoinGecko votes bullish: 75.0% · headline tone (48h): -2

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 169 |
| Raydium AMM v4 | 169 |
| Orca Whirlpool | 191 |
| Pump.fun | 218 |
| Tensor | 0 |
| Magic Eden v2 | 24 |
| Marinade | 1 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 11,175,972 |
| Binance (cold) | 1,388,379 |
| OKX (attributed) | 308,814 |
| Coinbase (hot) | 56,417 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 216ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 99.4% of stake.
- **Agave**: latest release v4.3.0 · running 4.3.0 on the polled node.
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
| solana_rpc | OK | 8431 ms |
| solana_rpc_validators | OK | 245 ms |
| coingecko | OK | 1803 ms |
| defillama_tvl | OK | 1641 ms |
| defillama_dex | OK | 1350 ms |
| defillama_fees | OK | 1957 ms |
| defillama_stablecoins | OK | 580 ms |
| defillama_xstocks | OK | 59 ms |
| jito_kobe | OK | 377 ms |
| stakewiz | OK | 1368 ms |
| github | OK | 689 ms |
| solana_com_news | OK | 124 ms |
| sentiment | OK | 2479 ms |
| solana_status_page | OK | 433 ms |
| solana_rpc_whales | OK | 1301 ms |
| solana_rpc_programs | OK | 6954 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*