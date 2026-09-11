# Solbeat — State of the Solana Network

> Generated 2026-09-11T15:29:19Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1032 is 85% complete (~6h remaining), with the cluster processing ~4,382 TPS (2,272 non-vote). Measured slot time is 318ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $879.3K of Real Economic Value over the last 24h ($611/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $103.37 (+3.6% / 24h). Decentralization: Nakamoto coefficient 18, 674 active validators, 0.5% of stake delinquent. Alpenglow readiness: validators holding 99% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: all clear across every monitored metric.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 446,191,207 |
| Block height | 424,234,357 |
| Epoch | 1032 (85.0% complete, ~5.7h left) |
| TPS (10 min avg) | 4,382 |
| Non-vote TPS | 2,272 |
| Slot time (measured) | 318.1 ms |
| Est. daily transactions | 381,074,896 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0036 |
| Node version | 4.3.0-rc.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $103.37 (+3.6%/24h) |
| Market cap | $60.6B |
| **REV (24h)** | **$879.3K** (fees $709.3K + Jito tips $170.0K) |
| Chain TVL | $5.8B |
| Stablecoin supply | $16.3B |
| DEX volume (24h) | $2.9B (-2.6%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 586,537,335 SOL |
| Inflation | 3.65% |

Top DEXs by 24h volume: PumpSwap ($468.1M), Raydium AMM ($432.3M), BisonFi ($395.8M), HumidiFi ($322.7M), Tessera V ($232.0M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 674 / 16 |
| Delinquent stake | 0.45% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.2% |
| Avg / median commission | 12.9% / 5.0% |
| Alpenglow BLS-key readiness | 695 validators, 99.0% of stake |

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

**67/100 — Bullish** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 82.5 |
| fear greed | 56 |
| momentum | 48.4 |
| news | 90 |

Crypto Fear & Greed: 56 (Greed) · CoinGecko votes bullish: 82.5% · headline tone (48h): +5

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 126 |
| Raydium AMM v4 | 126 |
| Orca Whirlpool | 138 |
| Pump.fun | 138 |
| Tensor | 1 |
| Magic Eden v2 | 48 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,188,448 |
| Binance (cold) | 1,809,462 |
| OKX (attributed) | 232,182 |
| Coinbase (hot) | 18,979 |

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
| solana_rpc | OK | 7368 ms |
| solana_rpc_validators | OK | 106 ms |
| coingecko | OK | 1652 ms |
| defillama_tvl | OK | 191 ms |
| defillama_dex | OK | 776 ms |
| defillama_fees | OK | 688 ms |
| defillama_stablecoins | OK | 102 ms |
| defillama_xstocks | OK | 9450 ms |
| jito_kobe | OK | 70 ms |
| stakewiz | OK | 967 ms |
| github | OK | 551 ms |
| solana_com_news | OK | 70 ms |
| sentiment | OK | 2184 ms |
| solana_status_page | OK | 369 ms |
| solana_rpc_whales | OK | 754 ms |
| solana_rpc_programs | OK | 1356 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*