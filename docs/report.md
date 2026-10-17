# Solbeat — State of the Solana Network

> Generated 2026-10-17T21:53:27Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1060 is 63% complete (~10h remaining), with the cluster processing ~5,056 TPS (1,988 non-vote). Measured slot time is 217ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $907.3K of Real Economic Value over the last 24h ($630/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $101.87 (-2.2% / 24h). Decentralization: Nakamoto coefficient 18, 670 active validators, 0.0% of stake delinquent. Alpenglow readiness: validators holding 99% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: all clear across every monitored metric.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 458,192,597 |
| Block height | 436,227,966 |
| Epoch | 1060 (63.1% complete, ~9.6h left) |
| TPS (10 min avg) | 5,056 |
| Non-vote TPS | 1,988 |
| Slot time (measured) | 217.4 ms |
| Est. daily transactions | 426,021,885 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0048 |
| Node version | 4.3.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $101.87 (-2.2%/24h) |
| Market cap | $60.1B |
| **REV (24h)** | **$907.3K** (fees $774.6K + Jito tips $132.7K) |
| Chain TVL | $5.9B |
| Stablecoin supply | $16.0B |
| DEX volume (24h) | $2.2B (-22.6%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 589,382,084 SOL |
| Inflation | 3.6% |

Top DEXs by 24h volume: PumpSwap ($545.4M), BisonFi ($283.4M), pump.fun ($155.6M), Meteora DLMM ($148.9M), Orca DEX ($119.4M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 670 / 11 |
| Delinquent stake | 0.01% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.4% |
| Avg / median commission | 13.0% / 5.0% |
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

**53/100 — Neutral** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 71.4 |
| fear greed | 55 |
| momentum | 27.3 |
| news | 66 |

Crypto Fear & Greed: 55 (Greed) · CoinGecko votes bullish: 71.43% · headline tone (48h): +2

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 175 |
| Raydium AMM v4 | 175 |
| Orca Whirlpool | 198 |
| Pump.fun | 198 |
| Tensor | 0 |
| Magic Eden v2 | 49 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 11,175,972 |
| Binance (cold) | 1,337,286 |
| OKX (attributed) | 328,740 |
| Coinbase (hot) | 23,682 |

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
| solana_rpc | OK | 8192 ms |
| solana_rpc_validators | OK | 160 ms |
| coingecko | OK | 1621 ms |
| defillama_tvl | OK | 72 ms |
| defillama_dex | OK | 808 ms |
| defillama_fees | OK | 1368 ms |
| defillama_stablecoins | OK | 100 ms |
| defillama_xstocks | OK | 63 ms |
| jito_kobe | OK | 95 ms |
| stakewiz | OK | 977 ms |
| github | OK | 690 ms |
| solana_com_news | OK | 97 ms |
| sentiment | OK | 2055 ms |
| solana_status_page | OK | 236 ms |
| solana_rpc_whales | OK | 944 ms |
| solana_rpc_programs | OK | 1524 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*