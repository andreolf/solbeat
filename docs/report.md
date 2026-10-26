# Solbeat — State of the Solana Network

> Generated 2026-10-26T23:36:46Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1069 is 10% complete (~23h remaining), with the cluster processing ~2,512 TPS (2,512 non-vote). Measured slot time is 213ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $573.9K of Real Economic Value over the last 24h ($399/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $100.60 (-0.6% / 24h). Decentralization: Nakamoto coefficient 18, 664 active validators, 0.5% of stake delinquent. Alpenglow readiness: validators holding 100% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 1 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 461,852,767 |
| Block height | 439,878,821 |
| Epoch | 1069 (10.36% complete, ~22.9h left) |
| TPS (10 min avg) | 2,512 |
| Non-vote TPS | 2,512 |
| Slot time (measured) | 212.9 ms |
| Confirmation time (measured) | 0.21 s |
| Finality time (measured) | 0.21 s — **Alpenglow active** |
| Est. daily transactions | 174,321,730 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0025 |
| Node version | 4.3.2 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $100.60 (-0.6%/24h) |
| Market cap | $59.3B |
| **REV (24h)** | **$573.9K** (fees $434.1K + Jito tips $139.9K) |
| Chain TVL | $5.7B |
| Stablecoin supply | $15.8B |
| DEX volume (24h) | $1.4B (1.8%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 589,874,744 SOL |
| Inflation | 3.58% |

Top DEXs by 24h volume: PumpSwap ($310.9M), Manifest Trade ($296.4M), Orca DEX ($245.8M), BisonFi ($184.8M), Raydium AMM ($146.7M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 664 / 21 |
| Delinquent stake | 0.52% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.6% |
| Avg / median commission | 12.8% / 5.0% |
| Alpenglow BLS-key readiness | 677 validators, 100.0% of stake |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L43ZWjwCHART3o…` | 17,059,304 | 3.9% | 7% |
| 2 | `he1iusunGwqrNtafDtLd…` | 16,636,453 | 3.81% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5…` | 12,660,117 | 2.9% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxb…` | 10,812,577 | 2.47% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxA…` | 9,716,980 | 2.22% | 5% |
| 6 | `51JBzSTU5rAM8gLAVQKg…` | 9,494,053 | 2.17% | 10% |
| 7 | `26pV97Ce83ZQ6Kz9XT4t…` | 9,206,552 | 2.11% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2Fp…` | 7,754,189 | 1.77% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJn…` | 7,040,177 | 1.61% | 5% |
| 10 | `DumiCKHVqoCQKD8roLAp…` | 6,996,375 | 1.6% | 0% |

## Signals (anomaly detection)

- **[WARNING]** Real Economic Value deviating from its run-history baseline (z=-2.0)

## Solana Pulse — sentiment (experimental)

**54/100 — Neutral** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 73.9 |
| fear greed | 50 |
| momentum | 43.9 |
| news | 42 |

Crypto Fear & Greed: 50 (Neutral) · CoinGecko votes bullish: 73.91% · headline tone (48h): -1

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 1,500 |
| Raydium AMM v4 | 989 |
| Orca Whirlpool | 1,500 |
| Pump.fun | 1,500 |
| Tensor | 0 |
| Magic Eden v2 | 73 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 11,175,975 |
| Binance (cold) | 1,223,843 |
| OKX (attributed) | 330,874 |
| Coinbase (hot) | 14,134 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 213ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 100.0% of stake.
- **Agave**: latest release v4.3.2 · running 4.3.2 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

### Latest ecosystem news (solana.com)

- [Solana Changelog: October 22, 2026](https://solana.com/news/solana-changelog-october-22-2026) — Fri, 23 Oct 2026
- [Solana Changelog: October 16, 2026](https://solana.com/news/solana-changelog-october-16-2026) — Fri, 16 Oct 2026
- [Geo-Aware Leader Schedule](https://solana.com/news/geo-aware-leader-schedule) — Wed, 14 Oct 2026
- [More Breakpoint 2026 Speakers Confirmed for London](https://solana.com/news/breakpoint-2026-london-speakers-2) — Mon, 12 Oct 2026
- [Payments on Solana: September 2026 in Five Stories](https://solana.com/news/payments-on-solana-september-2026-in-five-stories) — Fri, 09 Oct 2026
- [Breakpoint 2026: Booked Breakpoint? Let's Get You Prepped (Part 2)](https://solana.com/news/breakpoint-guide-part2) — Thu, 08 Oct 2026

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 9999 ms |
| solana_rpc_validators | OK | 83 ms |
| coingecko | OK | 1612 ms |
| defillama_tvl | OK | 159 ms |
| defillama_dex | OK | 48 ms |
| defillama_fees | OK | 699 ms |
| defillama_stablecoins | OK | 103 ms |
| defillama_xstocks | FAILED | 527 ms |
| jito_kobe | OK | 182 ms |
| stakewiz | OK | 998 ms |
| github | OK | 567 ms |
| solana_com_news | OK | 88 ms |
| sentiment | OK | 2084 ms |
| solana_status_page | OK | 214 ms |
| solana_rpc_whales | OK | 814 ms |
| solana_rpc_programs | OK | 1367 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*