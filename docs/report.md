# Solbeat — State of the Solana Network

> Generated 2026-09-11T09:21:57Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1032 is 69% complete (~12h remaining), with the cluster processing ~3,449 TPS (1,312 non-vote). Measured slot time is 314ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $875.4K of Real Economic Value over the last 24h ($608/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $99.68 (-1.6% / 24h). Decentralization: Nakamoto coefficient 18, 674 active validators, 0.4% of stake delinquent. Alpenglow readiness: validators holding 99% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: all clear across every monitored metric.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 446,121,743 |
| Block height | 424,164,957 |
| Epoch | 1032 (68.92% complete, ~11.7h left) |
| TPS (10 min avg) | 3,449 |
| Non-vote TPS | 1,312 |
| Slot time (measured) | 314.0 ms |
| Est. daily transactions | 317,405,859 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0055 |
| Node version | 4.3.0-rc.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $99.68 (-1.6%/24h) |
| Market cap | $58.5B |
| **REV (24h)** | **$875.4K** (fees $709.3K + Jito tips $166.1K) |
| Chain TVL | $5.8B |
| Stablecoin supply | $16.3B |
| DEX volume (24h) | $2.9B (-1.7%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 586,537,580 SOL |
| Inflation | 3.65% |

Top DEXs by 24h volume: PumpSwap ($468.1M), Raydium AMM ($403.4M), BisonFi ($402.8M), HumidiFi ($285.6M), Tessera V ($248.0M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 674 / 15 |
| Delinquent stake | 0.44% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.2% |
| Avg / median commission | 12.9% / 5.0% |
| Alpenglow BLS-key readiness | 694 validators, 99.0% of stake |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L43ZWjwCHART3o…` | 17,441,456 | 3.97% | 7% |
| 2 | `he1iusunGwqrNtafDtLd…` | 16,324,959 | 3.72% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5…` | 12,523,951 | 2.85% | 0% |
| 4 | `CatzoSMUkTRidT5DwBxA…` | 11,380,651 | 2.59% | 5% |
| 5 | `8GbwASqdpw4dVcwbWUxb…` | 9,569,332 | 2.18% | 0% |
| 6 | `26pV97Ce83ZQ6Kz9XT4t…` | 9,279,795 | 2.11% | 7% |
| 7 | `51JBzSTU5rAM8gLAVQKg…` | 9,036,257 | 2.06% | 10% |
| 8 | `9QU2QSxhb24FUX3Tu2Fp…` | 7,344,636 | 1.67% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJn…` | 6,880,702 | 1.57% | 5% |
| 10 | `DumiCKHVqoCQKD8roLAp…` | 6,550,397 | 1.49% | 0% |

## Signals (anomaly detection)

All clear — no anomalies across monitored metrics.

## Solana Pulse — sentiment (experimental)

**59/100 — Neutral** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 75.5 |
| fear greed | 56 |
| momentum | 44.8 |
| news | 58 |

Crypto Fear & Greed: 56 (Greed) · CoinGecko votes bullish: 75.51% · headline tone (48h): +1

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 131 |
| Raydium AMM v4 | 144 |
| Orca Whirlpool | 144 |
| Pump.fun | 144 |
| Tensor | 0 |
| Magic Eden v2 | 41 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,188,448 |
| Binance (cold) | 1,846,956 |
| OKX (attributed) | 232,174 |
| Coinbase (hot) | 23,475 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 314ms · proposal merged.
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
| solana_rpc | OK | 10506 ms |
| solana_rpc_validators | OK | 1012 ms |
| coingecko | OK | 1764 ms |
| defillama_tvl | OK | 659 ms |
| defillama_dex | OK | 491 ms |
| defillama_fees | OK | 2456 ms |
| defillama_stablecoins | OK | 196 ms |
| defillama_xstocks | OK | 639 ms |
| jito_kobe | OK | 337 ms |
| stakewiz | OK | 1120 ms |
| github | OK | 801 ms |
| solana_com_news | OK | 129 ms |
| sentiment | OK | 2324 ms |
| solana_status_page | OK | 410 ms |
| solana_rpc_whales | OK | 2238 ms |
| solana_rpc_programs | OK | 4009 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*