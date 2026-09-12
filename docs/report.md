# Solbeat — State of the Solana Network

> Generated 2026-09-12T13:15:13Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1033 is 42% complete (~22h remaining), with the cluster processing ~3,552 TPS (1,436 non-vote). Measured slot time is 318ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $970.9K of Real Economic Value over the last 24h ($674/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $102.02 (+0.5% / 24h). Decentralization: Nakamoto coefficient 18, 677 active validators, 0.4% of stake delinquent. Alpenglow readiness: validators holding 99% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: all clear across every monitored metric.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 446,438,337 |
| Block height | 424,481,130 |
| Epoch | 1033 (42.21% complete, ~22.1h left) |
| TPS (10 min avg) | 3,552 |
| Non-vote TPS | 1,436 |
| Slot time (measured) | 318.5 ms |
| Est. daily transactions | 286,993,185 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0081 |
| Node version | 4.3.0-rc.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $102.02 (+0.5%/24h) |
| Market cap | $59.8B |
| **REV (24h)** | **$970.9K** (fees $835.7K + Jito tips $135.2K) |
| Chain TVL | $5.9B |
| Stablecoin supply | $16.5B |
| DEX volume (24h) | $3.2B (9.0%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 586,632,887 SOL |
| Inflation | 3.65% |

Top DEXs by 24h volume: BisonFi ($471.7M), Raydium AMM ($399.4M), Meteora DLMM ($363.0M), PumpSwap ($294.2M), Orca DEX ($231.8M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 677 / 13 |
| Delinquent stake | 0.41% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.4% |
| Avg / median commission | 12.7% / 5% |
| Alpenglow BLS-key readiness | 695 validators, 99.0% of stake |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L43ZWjwCHART3o…` | 17,557,397 | 4.02% | 7% |
| 2 | `he1iusunGwqrNtafDtLd…` | 16,359,842 | 3.75% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5…` | 12,516,388 | 2.87% | 0% |
| 4 | `CatzoSMUkTRidT5DwBxA…` | 11,367,276 | 2.6% | 5% |
| 5 | `8GbwASqdpw4dVcwbWUxb…` | 9,667,435 | 2.21% | 0% |
| 6 | `26pV97Ce83ZQ6Kz9XT4t…` | 9,234,081 | 2.11% | 7% |
| 7 | `51JBzSTU5rAM8gLAVQKg…` | 9,021,415 | 2.07% | 10% |
| 8 | `9QU2QSxhb24FUX3Tu2Fp…` | 7,357,834 | 1.68% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJn…` | 6,941,562 | 1.59% | 5% |
| 10 | `DumiCKHVqoCQKD8roLAp…` | 6,551,099 | 1.5% | 0% |

## Signals (anomaly detection)

All clear — no anomalies across monitored metrics.

## Solana Pulse — sentiment (experimental)

**62/100 — Bullish** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 76.3 |
| fear greed | 63 |
| momentum | 53.8 |
| news | 50 |

Crypto Fear & Greed: 63 (Greed) · CoinGecko votes bullish: 76.32% · headline tone (48h): +0

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 120 |
| Raydium AMM v4 | 131 |
| Orca Whirlpool | 131 |
| Pump.fun | 120 |
| Tensor | 0 |
| Magic Eden v2 | 36 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,188,448 |
| Binance (cold) | 1,911,323 |
| OKX (attributed) | 232,182 |
| Coinbase (hot) | 25,863 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 318ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 99.0% of stake.
- **Agave**: latest release v4.2.2 · running 4.3.0-rc.0 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

### Latest ecosystem news (solana.com)

- [Report: Stablecoins Are Reshaping Remittances](https://solana.com/news/report-stablecoins-are-reshaping-remittances) — Tue, 08 Sep 2026
- [How BitRobot Crowdsources Real-World Data for Embodied AI, with Jonathan Victor](https://solana.com/news/bits-to-bricks-bitrobot-jonathan-victor) — Mon, 07 Sep 2026
- [Solana Ecosystem Roundup: August 2026](https://solana.com/news/solana-ecosystem-roundup-august-2026) — Fri, 04 Sep 2026
- [Payment Channels: 1 Million Payments Per Second](https://solana.com/news/payment-channels-1-million-payments-per-second) — Thu, 03 Sep 2026
- [How to Reclaim Excess SOL After Rent Reduction](https://solana.com/news/how-to-reclaim-excess-sol-after-rent-reduction) — Thu, 03 Sep 2026
- [The Token Supercycle: Everything of Value is Becoming Programmable](https://solana.com/news/the-token-supercycle-oped) — Wed, 02 Sep 2026

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 9065 ms |
| solana_rpc_validators | OK | 453 ms |
| coingecko | OK | 1765 ms |
| defillama_tvl | OK | 110 ms |
| defillama_dex | OK | 5632 ms |
| defillama_fees | OK | 5435 ms |
| defillama_stablecoins | OK | 1206 ms |
| defillama_xstocks | OK | 49 ms |
| jito_kobe | OK | 217 ms |
| stakewiz | OK | 2326 ms |
| github | OK | 942 ms |
| solana_com_news | OK | 114 ms |
| sentiment | OK | 2352 ms |
| solana_status_page | OK | 415 ms |
| solana_rpc_whales | OK | 1358 ms |
| solana_rpc_programs | OK | 2330 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*