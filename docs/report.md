# Solbeat — State of the Solana Network

> Generated 2026-10-18T22:00:40Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1061 is 56% complete (~12h remaining), with the cluster processing ~5,261 TPS (2,186 non-vote). Measured slot time is 216ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $738.6K of Real Economic Value over the last 24h ($513/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $102.02 (-0.5% / 24h). Decentralization: Nakamoto coefficient 18, 667 active validators, 0.0% of stake delinquent. Alpenglow readiness: validators holding 99% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: all clear across every monitored metric.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 458,593,035 |
| Block height | 436,628,281 |
| Epoch | 1061 (55.8% complete, ~11.5h left) |
| TPS (10 min avg) | 5,261 |
| Non-vote TPS | 2,186 |
| Slot time (measured) | 216.0 ms |
| Est. daily transactions | 442,146,870 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0035 |
| Node version | 4.3.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $102.02 (-0.5%/24h) |
| Market cap | $60.1B |
| **REV (24h)** | **$738.6K** (fees $622.8K + Jito tips $115.9K) |
| Chain TVL | $5.7B |
| Stablecoin supply | $15.8B |
| DEX volume (24h) | $1.3B (-42.2%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 589,437,911 SOL |
| Inflation | 3.6% |

Top DEXs by 24h volume: PumpSwap ($194.5M), Orca DEX ($186.0M), BisonFi ($182.3M), pump.fun ($127.8M), Tessera V ($94.0M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 667 / 13 |
| Delinquent stake | 0.0% |
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

All clear — no anomalies across monitored metrics.

## Solana Pulse — sentiment (experimental)

**51/100 — Neutral** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 78.1 |
| fear greed | 53 |
| momentum | 19.3 |
| news | 58 |

Crypto Fear & Greed: 53 (Neutral) · CoinGecko votes bullish: 78.13% · headline tone (48h): +1

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 180 |
| Raydium AMM v4 | 180 |
| Orca Whirlpool | 204 |
| Pump.fun | 204 |
| Tensor | 1 |
| Magic Eden v2 | 55 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 11,175,972 |
| Binance (cold) | 1,394,055 |
| OKX (attributed) | 328,740 |
| Coinbase (hot) | 17,288 |

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
| solana_rpc | OK | 7358 ms |
| solana_rpc_validators | OK | 174 ms |
| coingecko | OK | 1756 ms |
| defillama_tvl | OK | 88 ms |
| defillama_dex | OK | 1167 ms |
| defillama_fees | OK | 9007 ms |
| defillama_stablecoins | OK | 208 ms |
| defillama_xstocks | OK | 90 ms |
| jito_kobe | OK | 462 ms |
| stakewiz | OK | 1438 ms |
| github | OK | 978 ms |
| solana_com_news | OK | 109 ms |
| sentiment | OK | 2363 ms |
| solana_status_page | OK | 441 ms |
| solana_rpc_whales | OK | 1002 ms |
| solana_rpc_programs | OK | 1596 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*