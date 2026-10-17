# Solbeat — State of the Solana Network

> Generated 2026-10-17T07:51:22Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1060 is 9% complete (~24h remaining), with the cluster processing ~4,351 TPS (1,291 non-vote). Measured slot time is 218ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $910.7K of Real Economic Value over the last 24h ($632/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $104.94 (-1.4% / 24h). Decentralization: Nakamoto coefficient 18, 670 active validators, 0.0% of stake delinquent. Alpenglow readiness: validators holding 99% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: all clear across every monitored metric.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 457,960,001 |
| Block height | 435,995,393 |
| Epoch | 1060 (9.26% complete, ~23.8h left) |
| TPS (10 min avg) | 4,351 |
| Non-vote TPS | 1,291 |
| Slot time (measured) | 218.3 ms |
| Est. daily transactions | 399,958,496 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0058 |
| Node version | 4.3.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $104.94 (-1.4%/24h) |
| Market cap | $61.9B |
| **REV (24h)** | **$910.7K** (fees $774.6K + Jito tips $136.1K) |
| Chain TVL | $5.9B |
| Stablecoin supply | $16.0B |
| DEX volume (24h) | $2.5B (-11.9%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 589,385,211 SOL |
| Inflation | 3.6% |

Top DEXs by 24h volume: PumpSwap ($545.0M), BisonFi ($410.4M), Orca DEX ($260.5M), Raydium AMM ($161.3M), pump.fun ($155.0M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 670 / 11 |
| Delinquent stake | 0.01% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.4% |
| Avg / median commission | 12.6% / 5.0% |
| Alpenglow BLS-key readiness | 708 validators, 99.4% of stake |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L43ZWjwCHART3o…` | 17,532,933 | 4.0% | 7% |
| 2 | `he1iusunGwqrNtafDtLd…` | 15,736,568 | 3.59% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5…` | 12,486,161 | 2.85% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxb…` | 10,972,883 | 2.5% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxA…` | 10,191,942 | 2.32% | 5% |
| 6 | `51JBzSTU5rAM8gLAVQKg…` | 9,445,787 | 2.15% | 10% |
| 7 | `26pV97Ce83ZQ6Kz9XT4t…` | 9,250,229 | 2.11% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2Fp…` | 7,759,724 | 1.77% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJn…` | 6,991,827 | 1.59% | 5% |
| 10 | `DumiCKHVqoCQKD8roLAp…` | 6,726,220 | 1.53% | 0% |

## Signals (anomaly detection)

All clear — no anomalies across monitored metrics.

## Solana Pulse — sentiment (experimental)

**56/100 — Neutral** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 68.2 |
| fear greed | 55 |
| momentum | 35.8 |
| news | 74 |

Crypto Fear & Greed: 55 (Greed) · CoinGecko votes bullish: 68.18% · headline tone (48h): +3

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 168 |
| Raydium AMM v4 | 151 |
| Orca Whirlpool | 189 |
| Pump.fun | 216 |
| Tensor | 0 |
| Magic Eden v2 | 151 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 11,175,972 |
| Binance (cold) | 1,384,669 |
| OKX (attributed) | 328,840 |
| Coinbase (hot) | 30,603 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 218ms · proposal merged.
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
| solana_rpc | OK | 8315 ms |
| solana_rpc_validators | OK | 111 ms |
| coingecko | OK | 1638 ms |
| defillama_tvl | OK | 74 ms |
| defillama_dex | OK | 774 ms |
| defillama_fees | OK | 86 ms |
| defillama_stablecoins | OK | 112 ms |
| defillama_xstocks | OK | 34 ms |
| jito_kobe | OK | 339 ms |
| stakewiz | OK | 943 ms |
| github | OK | 614 ms |
| solana_com_news | OK | 199 ms |
| sentiment | OK | 2238 ms |
| solana_status_page | OK | 201 ms |
| solana_rpc_whales | OK | 999 ms |
| solana_rpc_programs | OK | 1663 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*