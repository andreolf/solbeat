# Solbeat — State of the Solana Network

> Generated 2026-09-10T03:00:35Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1031 is 89% complete (~4h remaining), with the cluster processing ~4,074 TPS (1,949 non-vote). Measured slot time is 315ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $1.1M of Real Economic Value over the last 24h ($757/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $101.82 (-1.6% / 24h). Decentralization: Nakamoto coefficient 18, 675 active validators, 0.1% of stake delinquent. Alpenglow readiness: validators holding 99% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: all clear across every monitored metric.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 445,776,043 |
| Block height | 423,819,457 |
| Epoch | 1031 (88.9% complete, ~4.2h left) |
| TPS (10 min avg) | 4,074 |
| Non-vote TPS | 1,949 |
| Slot time (measured) | 315.3 ms |
| Est. daily transactions | 361,441,380 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0055 |
| Node version | 4.2.2 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $101.82 (-1.6%/24h) |
| Market cap | $59.7B |
| **REV (24h)** | **$1.1M** (fees $978.5K + Jito tips $111.6K) |
| Chain TVL | $5.9B |
| Stablecoin supply | $16.5B |
| DEX volume (24h) | $2.6B (-5.7%/1d) |
| Tokenized equities (xStocks TVL) | $437.8M |
| Circulating supply | 586,249,923 SOL |
| Inflation | 3.66% |

Top DEXs by 24h volume: Raydium AMM ($421.1M), PumpSwap ($341.0M), Meteora DLMM ($322.2M), BisonFi ($249.3M), Orca DEX ($169.5M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 675 / 13 |
| Delinquent stake | 0.05% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.2% |
| Avg / median commission | 12.8% / 5% |
| Alpenglow BLS-key readiness | 693 validators, 99.0% of stake |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L43ZWjwCHART3o…` | 17,436,766 | 3.98% | 7% |
| 2 | `he1iusunGwqrNtafDtLd…` | 16,345,792 | 3.73% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5…` | 12,527,540 | 2.86% | 0% |
| 4 | `CatzoSMUkTRidT5DwBxA…` | 11,388,333 | 2.6% | 5% |
| 5 | `8GbwASqdpw4dVcwbWUxb…` | 9,566,721 | 2.18% | 0% |
| 6 | `26pV97Ce83ZQ6Kz9XT4t…` | 9,286,723 | 2.12% | 7% |
| 7 | `51JBzSTU5rAM8gLAVQKg…` | 9,027,481 | 2.06% | 10% |
| 8 | `9QU2QSxhb24FUX3Tu2Fp…` | 7,322,728 | 1.67% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJn…` | 6,860,585 | 1.56% | 5% |
| 10 | `DumiCKHVqoCQKD8roLAp…` | 6,604,066 | 1.51% | 0% |

## Signals (anomaly detection)

All clear — no anomalies across monitored metrics.

## Solana Pulse — sentiment (experimental)

**63/100 — Bullish** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 77.1 |
| fear greed | 69 |
| momentum | 47.6 |
| news | 58 |

Crypto Fear & Greed: 69 (Greed) · CoinGecko votes bullish: 77.14% · headline tone (48h): +1

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 119 |
| Raydium AMM v4 | 129 |
| Orca Whirlpool | 129 |
| Pump.fun | 129 |
| Tensor | 0 |
| Magic Eden v2 | 61 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,188,448 |
| Binance (cold) | 1,835,652 |
| OKX (attributed) | 211,871 |
| Coinbase (hot) | 25,876 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 315ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 99.0% of stake.
- **Agave**: latest release v4.2.2 · running 4.2.2 on the polled node.
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
| solana_rpc | OK | 8303 ms |
| solana_rpc_validators | OK | 309 ms |
| coingecko | OK | 1602 ms |
| defillama_tvl | OK | 66 ms |
| defillama_dex | OK | 782 ms |
| defillama_fees | OK | 721 ms |
| defillama_stablecoins | OK | 96 ms |
| defillama_xstocks | OK | 110 ms |
| jito_kobe | OK | 70 ms |
| stakewiz | OK | 730 ms |
| github | OK | 589 ms |
| solana_com_news | OK | 60 ms |
| sentiment | OK | 2248 ms |
| solana_status_page | OK | 280 ms |
| solana_rpc_whales | OK | 1082 ms |
| solana_rpc_programs | OK | 1956 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*