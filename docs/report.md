# Solbeat — State of the Solana Network

> Generated 2026-10-17T04:17:08Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1059 is 96% complete (~1h remaining), with the cluster processing ~4,588 TPS (1,499 non-vote). Measured slot time is 216ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $983.2K of Real Economic Value over the last 24h ($683/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $104.66 (-0.4% / 24h). Decentralization: Nakamoto coefficient 18, 671 active validators, 0.0% of stake delinquent. Alpenglow readiness: validators holding 99% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: all clear across every monitored metric.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 457,900,555 |
| Block height | 435,935,954 |
| Epoch | 1059 (95.5% complete, ~1.2h left) |
| TPS (10 min avg) | 4,588 |
| Non-vote TPS | 1,499 |
| Slot time (measured) | 216.3 ms |
| Est. daily transactions | 407,997,477 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0054 |
| Node version | 4.3.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $104.66 (-0.4%/24h) |
| Market cap | $61.7B |
| **REV (24h)** | **$983.2K** (fees $774.6K + Jito tips $208.6K) |
| Chain TVL | $5.9B |
| Stablecoin supply | $16.0B |
| DEX volume (24h) | $1.9B (-16.0%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 589,328,515 SOL |
| Inflation | 3.6% |

Top DEXs by 24h volume: BisonFi ($410.4M), Orca DEX ($268.6M), Raydium AMM ($175.1M), pump.fun ($155.0M), Tessera V ($132.8M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 671 / 10 |
| Delinquent stake | 0.01% |
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

**53/100 — Neutral** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 69.2 |
| fear greed | 55 |
| momentum | 33.4 |
| news | 58 |

Crypto Fear & Greed: 55 (Greed) · CoinGecko votes bullish: 69.23% · headline tone (48h): +1

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 167 |
| Raydium AMM v4 | 150 |
| Orca Whirlpool | 214 |
| Pump.fun | 214 |
| Tensor | 0 |
| Magic Eden v2 | 107 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 11,175,972 |
| Binance (cold) | 1,402,225 |
| OKX (attributed) | 308,814 |
| Coinbase (hot) | 31,768 |

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
| solana_rpc | OK | 9157 ms |
| solana_rpc_validators | OK | 320 ms |
| coingecko | OK | 1696 ms |
| defillama_tvl | OK | 277 ms |
| defillama_dex | OK | 923 ms |
| defillama_fees | OK | 2138 ms |
| defillama_stablecoins | OK | 954 ms |
| defillama_xstocks | OK | 78 ms |
| jito_kobe | OK | 457 ms |
| stakewiz | OK | 1134 ms |
| github | OK | 785 ms |
| solana_com_news | OK | 141 ms |
| sentiment | OK | 2366 ms |
| solana_status_page | OK | 421 ms |
| solana_rpc_whales | OK | 1222 ms |
| solana_rpc_programs | OK | 1979 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*