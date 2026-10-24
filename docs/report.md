# Solbeat — State of the Solana Network

> Generated 2026-10-24T20:36:58Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1067 is 10% complete (~23h remaining), with the cluster processing ~2,396 TPS (2,396 non-vote). Measured slot time is 211ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $690.3K of Real Economic Value over the last 24h ($479/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $101.39 (-2.1% / 24h). Decentralization: Nakamoto coefficient 18, 665 active validators, 0.1% of stake delinquent. Alpenglow readiness: validators holding 100% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: all clear across every monitored metric.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 460,988,514 |
| Block height | 439,017,714 |
| Epoch | 1067 (10.3% complete, ~22.8h left) |
| TPS (10 min avg) | 2,396 |
| Non-vote TPS | 2,396 |
| Slot time (measured) | 211.4 ms |
| Confirmation time (measured) | 0.21 s |
| Finality time (measured) | 0.21 s — **Alpenglow active** |
| Est. daily transactions | 172,459,578 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0032 |
| Node version | 4.3.2 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $101.39 (-2.1%/24h) |
| Market cap | $59.8B |
| **REV (24h)** | **$690.3K** (fees $560.4K + Jito tips $129.9K) |
| Chain TVL | $5.7B |
| Stablecoin supply | $15.8B |
| DEX volume (24h) | $2.0B (-2.1%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 589,764,427 SOL |
| Inflation | 3.59% |

Top DEXs by 24h volume: BisonFi ($342.5M), PumpSwap ($266.4M), Orca DEX ($183.8M), Tessera V ($162.4M), Manifest Trade ($149.7M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 665 / 25 |
| Delinquent stake | 0.05% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.6% |
| Avg / median commission | 12.9% / 5% |
| Alpenglow BLS-key readiness | 676 validators, 100.0% of stake |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L43ZWjwCHART3o…` | 17,099,113 | 3.91% | 7% |
| 2 | `he1iusunGwqrNtafDtLd…` | 16,646,121 | 3.81% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5…` | 12,588,035 | 2.88% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxb…` | 10,881,430 | 2.49% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxA…` | 9,721,918 | 2.22% | 5% |
| 6 | `51JBzSTU5rAM8gLAVQKg…` | 9,483,244 | 2.17% | 10% |
| 7 | `26pV97Ce83ZQ6Kz9XT4t…` | 9,216,837 | 2.11% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2Fp…` | 7,785,036 | 1.78% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJn…` | 7,038,249 | 1.61% | 5% |
| 10 | `DumiCKHVqoCQKD8roLAp…` | 7,006,653 | 1.6% | 0% |

## Signals (anomaly detection)

All clear — no anomalies across monitored metrics.

## Solana Pulse — sentiment (experimental)

**56/100 — Neutral** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 62.2 |
| fear greed | 51 |
| momentum | 43.4 |
| news | 74 |

Crypto Fear & Greed: 51 (Neutral) · CoinGecko votes bullish: 62.16% · headline tone (48h): +3

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 1,291 |
| Raydium AMM v4 | 694 |
| Orca Whirlpool | 694 |
| Pump.fun | 1,500 |
| Tensor | 0 |
| Magic Eden v2 | 32 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 11,175,975 |
| Binance (cold) | 1,542,158 |
| OKX (attributed) | 330,964 |
| Coinbase (hot) | 11,066 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 211ms · proposal merged.
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
| solana_rpc | OK | 10639 ms |
| solana_rpc_validators | OK | 319 ms |
| coingecko | OK | 1673 ms |
| defillama_tvl | OK | 110 ms |
| defillama_dex | OK | 934 ms |
| defillama_fees | OK | 1573 ms |
| defillama_stablecoins | OK | 996 ms |
| defillama_xstocks | FAILED | 672 ms |
| jito_kobe | OK | 315 ms |
| stakewiz | OK | 1116 ms |
| github | OK | 783 ms |
| solana_com_news | OK | 124 ms |
| sentiment | OK | 2264 ms |
| solana_status_page | OK | 420 ms |
| solana_rpc_whales | OK | 1146 ms |
| solana_rpc_programs | OK | 1927 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*