# Solbeat — State of the Solana Network

> Generated 2026-10-23T21:58:51Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1066 is 21% complete (~20h remaining), with the cluster processing ~1,940 TPS (1,940 non-vote). Measured slot time is 212ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $768.2K of Real Economic Value over the last 24h ($533/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $103.50 (-0.1% / 24h). Decentralization: Nakamoto coefficient 18, 664 active validators, 0.1% of stake delinquent. Alpenglow readiness: validators holding 99% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: all clear across every monitored metric.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 460,604,507 |
| Block height | 438,635,216 |
| Epoch | 1066 (21.41% complete, ~20.0h left) |
| TPS (10 min avg) | 1,940 |
| Non-vote TPS | 1,940 |
| Slot time (measured) | 212.0 ms |
| Confirmation time (measured) | 0.21 s |
| Finality time (measured) | 0.21 s — **Alpenglow active** |
| Est. daily transactions | 187,602,048 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0034 |
| Node version | 4.3.2 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $103.50 (-0.1%/24h) |
| Market cap | $61.0B |
| **REV (24h)** | **$768.2K** (fees $631.0K + Jito tips $137.2K) |
| Chain TVL | $5.8B |
| Stablecoin supply | $15.9B |
| DEX volume (24h) | $2.0B (-10.2%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 589,708,964 SOL |
| Inflation | 3.59% |

Top DEXs by 24h volume: BisonFi ($312.0M), PumpSwap ($259.0M), Orca DEX ($200.0M), Tessera V ($187.5M), Raydium AMM ($142.6M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 664 / 14 |
| Delinquent stake | 0.07% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.4% |
| Avg / median commission | 12.9% / 5.0% |
| Alpenglow BLS-key readiness | 711 validators, 99.4% of stake |

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

**61/100 — Bullish** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 87.5 |
| fear greed | 50 |
| momentum | 41.4 |
| news | 66 |

Crypto Fear & Greed: 50 (Neutral) · CoinGecko votes bullish: 87.5% · headline tone (48h): +2

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 1,041 |
| Raydium AMM v4 | 1,041 |
| Orca Whirlpool | 614 |
| Pump.fun | 1,500 |
| Tensor | 0 |
| Magic Eden v2 | 121 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 11,175,975 |
| Binance (cold) | 1,528,904 |
| OKX (attributed) | 330,965 |
| Coinbase (hot) | 10,184 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 212ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 99.4% of stake.
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
| solana_rpc | OK | 9136 ms |
| solana_rpc_validators | OK | 141 ms |
| coingecko | OK | 1789 ms |
| defillama_tvl | OK | 122 ms |
| defillama_dex | OK | 1155 ms |
| defillama_fees | OK | 1983 ms |
| defillama_stablecoins | OK | 218 ms |
| defillama_xstocks | FAILED | 801 ms |
| jito_kobe | OK | 259 ms |
| stakewiz | OK | 1534 ms |
| github | OK | 1023 ms |
| solana_com_news | OK | 134 ms |
| sentiment | OK | 2390 ms |
| solana_status_page | OK | 335 ms |
| solana_rpc_whales | OK | 842 ms |
| solana_rpc_programs | OK | 1588 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*