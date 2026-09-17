# Solbeat — State of the Solana Network

> Generated 2026-09-17T02:19:06Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1036 is 30% complete (~27h remaining), with the cluster processing ~4,016 TPS (1,881 non-vote). Measured slot time is 316ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $830.0K of Real Economic Value over the last 24h ($576/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $98.95 (+2.0% / 24h). Decentralization: Nakamoto coefficient 18, 679 active validators, 0.0% of stake delinquent. Alpenglow readiness: validators holding 99% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: all clear across every monitored metric.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 447,679,673 |
| Block height | 425,720,957 |
| Epoch | 1036 (29.55% complete, ~26.7h left) |
| TPS (10 min avg) | 4,016 |
| Non-vote TPS | 1,881 |
| Slot time (measured) | 315.8 ms |
| Est. daily transactions | 358,204,044 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0040 |
| Node version | 4.3.0-rc.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $98.95 (+2.0%/24h) |
| Market cap | $58.1B |
| **REV (24h)** | **$830.0K** (fees $693.2K + Jito tips $136.8K) |
| Chain TVL | $5.7B |
| Stablecoin supply | $15.7B |
| DEX volume (24h) | $2.7B (1.1%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 587,212,555 SOL |
| Inflation | 3.64% |

Top DEXs by 24h volume: PumpSwap ($441.4M), BisonFi ($353.6M), fomo Wallet ($267.6M), Raydium AMM ($263.6M), Orca DEX ($256.0M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 679 / 12 |
| Delinquent stake | 0.04% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.3% |
| Avg / median commission | 12.5% / 5% |
| Alpenglow BLS-key readiness | 698 validators, 99.4% of stake |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L43ZWjwCHART3o…` | 17,767,428 | 4.04% | 7% |
| 2 | `he1iusunGwqrNtafDtLd…` | 16,352,114 | 3.72% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5…` | 12,485,145 | 2.84% | 0% |
| 4 | `CatzoSMUkTRidT5DwBxA…` | 11,383,247 | 2.59% | 5% |
| 5 | `8GbwASqdpw4dVcwbWUxb…` | 9,740,877 | 2.22% | 0% |
| 6 | `26pV97Ce83ZQ6Kz9XT4t…` | 9,256,273 | 2.1% | 7% |
| 7 | `51JBzSTU5rAM8gLAVQKg…` | 9,049,051 | 2.06% | 10% |
| 8 | `9QU2QSxhb24FUX3Tu2Fp…` | 7,386,183 | 1.68% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJn…` | 7,076,306 | 1.61% | 5% |
| 10 | `DumiCKHVqoCQKD8roLAp…` | 6,558,592 | 1.49% | 0% |

## Signals (anomaly detection)

All clear — no anomalies across monitored metrics.

## Solana Pulse — sentiment (experimental)

**57/100 — Neutral** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 71.9 |
| fear greed | 50 |
| momentum | 48.8 |
| news | 58 |

Crypto Fear & Greed: 50 (Neutral) · CoinGecko votes bullish: 71.88% · headline tone (48h): +1

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 130 |
| Raydium AMM v4 | 119 |
| Orca Whirlpool | 130 |
| Pump.fun | 142 |
| Tensor | 0 |
| Magic Eden v2 | 59 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,188,448 |
| Binance (cold) | 1,997,072 |
| OKX (attributed) | 235,077 |
| Coinbase (hot) | 16,999 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 316ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 99.4% of stake.
- **Agave**: latest release v4.2.2 · running 4.3.0-rc.0 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

### Latest ecosystem news (solana.com)

- [Solana: Building, Proving and Earning Trust in Public](https://solana.com/news/solana-building-trust-in-public) — Mon, 14 Sep 2026
- [Report: Stablecoins Are Reshaping Remittances](https://solana.com/news/report-stablecoins-are-reshaping-remittances) — Tue, 08 Sep 2026
- [How BitRobot Crowdsources Real-World Data for Embodied AI, with Jonathan Victor](https://solana.com/news/bits-to-bricks-bitrobot-jonathan-victor) — Mon, 07 Sep 2026
- [Solana Ecosystem Roundup: August 2026](https://solana.com/news/solana-ecosystem-roundup-august-2026) — Fri, 04 Sep 2026
- [Payment Channels: 1 Million Payments Per Second](https://solana.com/news/payment-channels-1-million-payments-per-second) — Thu, 03 Sep 2026
- [How to Reclaim Excess SOL After Rent Reduction](https://solana.com/news/how-to-reclaim-excess-sol-after-rent-reduction) — Thu, 03 Sep 2026

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 9223 ms |
| solana_rpc_validators | OK | 353 ms |
| coingecko | OK | 1672 ms |
| defillama_tvl | OK | 289 ms |
| defillama_dex | OK | 493 ms |
| defillama_fees | OK | 3975 ms |
| defillama_stablecoins | OK | 655 ms |
| defillama_xstocks | OK | 58 ms |
| jito_kobe | OK | 257 ms |
| stakewiz | OK | 1226 ms |
| github | OK | 754 ms |
| solana_com_news | OK | 138 ms |
| sentiment | OK | 2270 ms |
| solana_status_page | OK | 443 ms |
| solana_rpc_whales | OK | 1124 ms |
| solana_rpc_programs | OK | 2504 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*