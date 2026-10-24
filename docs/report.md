# Solbeat — State of the Solana Network

> Generated 2026-10-24T15:56:35Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1066 is 92% complete (~2h remaining), with the cluster processing ~1,941 TPS (1,941 non-vote). Measured slot time is 212ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $692.3K of Real Economic Value over the last 24h ($481/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $99.41 (-4.9% / 24h). Decentralization: Nakamoto coefficient 18, 664 active validators, 0.1% of stake delinquent. Alpenglow readiness: validators holding 100% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: all clear across every monitored metric.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 460,909,150 |
| Block height | 438,939,532 |
| Epoch | 1066 (91.93% complete, ~2.0h left) |
| TPS (10 min avg) | 1,941 |
| Non-vote TPS | 1,941 |
| Slot time (measured) | 211.7 ms |
| Confirmation time (measured) | 0.21 s |
| Finality time (measured) | 0.21 s — **Alpenglow active** |
| Est. daily transactions | 145,187,148 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0039 |
| Node version | 4.3.2 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $99.41 (-4.9%/24h) |
| Market cap | $58.6B |
| **REV (24h)** | **$692.3K** (fees $560.4K + Jito tips $132.0K) |
| Chain TVL | $5.7B |
| Stablecoin supply | $15.8B |
| DEX volume (24h) | $2.0B (-2.1%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 589,708,682 SOL |
| Inflation | 3.59% |

Top DEXs by 24h volume: BisonFi ($342.5M), PumpSwap ($266.4M), Orca DEX ($204.8M), Tessera V ($162.4M), Manifest Trade ($151.9M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 664 / 14 |
| Delinquent stake | 0.07% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.4% |
| Avg / median commission | 13.2% / 5.0% |
| Alpenglow BLS-key readiness | 687 validators, 100.0% of stake |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L43ZWjwCHART3o…` | 17,096,230 | 3.91% | 7% |
| 2 | `he1iusunGwqrNtafDtLd…` | 16,022,778 | 3.67% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5…` | 12,572,396 | 2.88% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxb…` | 10,882,511 | 2.49% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxA…` | 9,724,046 | 2.22% | 5% |
| 6 | `51JBzSTU5rAM8gLAVQKg…` | 9,478,407 | 2.17% | 10% |
| 7 | `26pV97Ce83ZQ6Kz9XT4t…` | 9,213,418 | 2.11% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2Fp…` | 7,782,539 | 1.78% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJn…` | 7,037,301 | 1.61% | 5% |
| 10 | `DumiCKHVqoCQKD8roLAp…` | 7,003,145 | 1.6% | 0% |

## Signals (anomaly detection)

All clear — no anomalies across monitored metrics.

## Solana Pulse — sentiment (experimental)

**60/100 — Bullish** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 70.3 |
| fear greed | 51 |
| momentum | 41.8 |
| news | 90 |

Crypto Fear & Greed: 51 (Neutral) · CoinGecko votes bullish: 70.27% · headline tone (48h): +5

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 1,307 |
| Raydium AMM v4 | 1,307 |
| Orca Whirlpool | 1,307 |
| Pump.fun | 1,500 |
| Tensor | 1 |
| Magic Eden v2 | 36 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 11,175,975 |
| Binance (cold) | 1,522,341 |
| OKX (attributed) | 330,964 |
| Coinbase (hot) | 8,610 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 212ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 100.0% of stake.
- **Agave**: latest release v4.3.2 · running 4.3.2 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

### Latest ecosystem news (solana.com)

- [Solana Changelog: October 16, 2026](https://solana.com/news/solana-changelog-october-16-2026) — Fri, 16 Oct 2026
- [Geo-Aware Leader Schedule](https://solana.com/news/geo-aware-leader-schedule) — Wed, 14 Oct 2026
- [More Breakpoint 2026 Speakers Confirmed for London](https://solana.com/news/breakpoint-2026-london-speakers-2) — Mon, 12 Oct 2026
- [Payments on Solana: September 2026 in Five Stories](https://solana.com/news/payments-on-solana-september-2026-in-five-stories) — Fri, 09 Oct 2026
- [Breakpoint 2026: Booked Breakpoint? Let's Get You Prepped (Part 2)](https://solana.com/news/breakpoint-guide-part2) — Thu, 08 Oct 2026
- [Solana Changelog: October 8, 2026](https://solana.com/news/solana-changelog-october-8-2026) — Thu, 08 Oct 2026

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 10067 ms |
| solana_rpc_validators | OK | 180 ms |
| coingecko | OK | 1618 ms |
| defillama_tvl | OK | 63 ms |
| defillama_dex | OK | 837 ms |
| defillama_fees | OK | 984 ms |
| defillama_stablecoins | OK | 114 ms |
| defillama_xstocks | FAILED | 26 ms |
| jito_kobe | OK | 199 ms |
| stakewiz | OK | 978 ms |
| github | OK | 718 ms |
| solana_com_news | OK | 111 ms |
| sentiment | OK | 2100 ms |
| solana_status_page | OK | 293 ms |
| solana_rpc_whales | OK | 829 ms |
| solana_rpc_programs | OK | 1489 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*