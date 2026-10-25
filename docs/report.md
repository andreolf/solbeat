# Solbeat — State of the Solana Network

> Generated 2026-10-25T05:36:08Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1067 is 46% complete (~14h remaining), with the cluster processing ~1,316 TPS (1,316 non-vote). Measured slot time is 213ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $607.5K of Real Economic Value over the last 24h ($422/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $102.21 (-0.0% / 24h). Decentralization: Nakamoto coefficient 18, 665 active validators, 0.1% of stake delinquent. Alpenglow readiness: validators holding 100% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 1 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 461,140,841 |
| Block height | 439,169,741 |
| Epoch | 1067 (45.57% complete, ~13.9h left) |
| TPS (10 min avg) | 1,316 |
| Non-vote TPS | 1,316 |
| Slot time (measured) | 212.6 ms |
| Confirmation time (measured) | 0.21 s |
| Finality time (measured) | 0.21 s — **Alpenglow active** |
| Est. daily transactions | 144,480,374 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0033 |
| Node version | 4.3.2 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $102.21 (-0.0%/24h) |
| Market cap | $60.3B |
| **REV (24h)** | **$607.5K** (fees $477.3K + Jito tips $130.2K) |
| Chain TVL | $5.8B |
| Stablecoin supply | $15.8B |
| DEX volume (24h) | $1.7B (-13.2%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 589,764,278 SOL |
| Inflation | 3.59% |

Top DEXs by 24h volume: BisonFi ($342.5M), Tessera V ($162.4M), pump.fun ($142.8M), Orca DEX ($141.9M), Manifest Trade ($125.8M)

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

- **[WARNING]** Real Economic Value deviating from its run-history baseline (z=-2.1)

## Solana Pulse — sentiment (experimental)

**56/100 — Neutral** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 68.3 |
| fear greed | 54 |
| momentum | 39.6 |
| news | 66 |

Crypto Fear & Greed: 54 (Neutral) · CoinGecko votes bullish: 68.29% · headline tone (48h): +2

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 961 |
| Raydium AMM v4 | 586 |
| Orca Whirlpool | 961 |
| Pump.fun | 1,500 |
| Tensor | 0 |
| Magic Eden v2 | 24 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 11,175,975 |
| Binance (cold) | 1,538,814 |
| OKX (attributed) | 330,964 |
| Coinbase (hot) | 12,624 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 213ms · proposal merged.
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
| solana_rpc | OK | 8977 ms |
| solana_rpc_validators | OK | 341 ms |
| coingecko | OK | 1714 ms |
| defillama_tvl | OK | 235 ms |
| defillama_dex | OK | 1171 ms |
| defillama_fees | OK | 6399 ms |
| defillama_stablecoins | OK | 675 ms |
| defillama_xstocks | FAILED | 784 ms |
| jito_kobe | OK | 244 ms |
| stakewiz | OK | 1380 ms |
| github | OK | 998 ms |
| solana_com_news | OK | 148 ms |
| sentiment | OK | 2367 ms |
| solana_status_page | OK | 345 ms |
| solana_rpc_whales | OK | 968 ms |
| solana_rpc_programs | OK | 1608 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*