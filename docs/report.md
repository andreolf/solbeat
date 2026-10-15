# Solbeat — State of the Solana Network

> Generated 2026-10-15T11:16:54Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1058 is 37% complete (~16h remaining), with the cluster processing ~5,280 TPS (2,169 non-vote). Measured slot time is 215ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $930.7K of Real Economic Value over the last 24h ($646/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $102.29 (-4.3% / 24h). Decentralization: Nakamoto coefficient 18, 672 active validators, 0.0% of stake delinquent. Alpenglow readiness: validators holding 99% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 1 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 457,217,751 |
| Block height | 435,253,644 |
| Epoch | 1058 (37.44% complete, ~16.1h left) |
| TPS (10 min avg) | 5,280 |
| Non-vote TPS | 2,169 |
| Slot time (measured) | 215.1 ms |
| Est. daily transactions | 396,784,293 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0059 |
| Node version | 4.3.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $102.29 (-4.3%/24h) |
| Market cap | $60.2B |
| **REV (24h)** | **$930.7K** (fees $753.1K + Jito tips $177.6K) |
| Chain TVL | $5.9B |
| Stablecoin supply | $16.0B |
| DEX volume (24h) | $2.1B (-15.1%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 589,268,681 SOL |
| Inflation | 3.6% |

Top DEXs by 24h volume: Orca DEX ($382.2M), BisonFi ($381.4M), PumpSwap ($252.5M), Raydium AMM ($187.2M), pump.fun ($151.4M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 672 / 8 |
| Delinquent stake | 0.0% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.5% |
| Avg / median commission | 12.7% / 5.0% |
| Alpenglow BLS-key readiness | 708 validators, 99.4% of stake |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L43ZWjwCHART3o…` | 17,556,681 | 4.01% | 7% |
| 2 | `he1iusunGwqrNtafDtLd…` | 15,475,284 | 3.53% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5…` | 12,340,406 | 2.82% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxb…` | 11,132,168 | 2.54% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxA…` | 10,777,829 | 2.46% | 5% |
| 6 | `51JBzSTU5rAM8gLAVQKg…` | 9,409,309 | 2.15% | 10% |
| 7 | `26pV97Ce83ZQ6Kz9XT4t…` | 9,227,345 | 2.11% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2Fp…` | 7,737,484 | 1.77% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJn…` | 6,912,081 | 1.58% | 5% |
| 10 | `3JD3jMmnR6g88qff2WZ3…` | 6,640,641 | 1.52% | 0% |

## Signals (anomaly detection)

- **[WARNING]** TPS spike: 5,280 vs 12h mean 4,568 (z=+3.0)

## Solana Pulse — sentiment (experimental)

**49/100 — Neutral** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 62.8 |
| fear greed | 53 |
| momentum | 27.8 |
| news | 58 |

Crypto Fear & Greed: 53 (Neutral) · CoinGecko votes bullish: 62.79% · headline tone (48h): +1

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 173 |
| Raydium AMM v4 | 196 |
| Orca Whirlpool | 196 |
| Pump.fun | 196 |
| Tensor | 0 |
| Magic Eden v2 | 49 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 11,175,972 |
| Binance (cold) | 1,340,065 |
| OKX (attributed) | 308,798 |
| Coinbase (hot) | 116,862 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 215ms · proposal merged.
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
| solana_rpc | OK | 9116 ms |
| solana_rpc_validators | OK | 346 ms |
| coingecko | OK | 1676 ms |
| defillama_tvl | OK | 824 ms |
| defillama_dex | OK | 937 ms |
| defillama_fees | OK | 1640 ms |
| defillama_stablecoins | OK | 247 ms |
| defillama_xstocks | OK | 896 ms |
| jito_kobe | OK | 255 ms |
| stakewiz | OK | 1302 ms |
| github | OK | 853 ms |
| solana_com_news | OK | 182 ms |
| sentiment | OK | 2803 ms |
| solana_status_page | OK | 382 ms |
| solana_rpc_whales | OK | 1026 ms |
| solana_rpc_programs | OK | 1891 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*