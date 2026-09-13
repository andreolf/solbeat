# Solbeat — State of the Solana Network

> Generated 2026-09-13T03:22:15Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1033 is 79% complete (~8h remaining), with the cluster processing ~3,907 TPS (1,764 non-vote). Measured slot time is 314ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $845.8K of Real Economic Value over the last 24h ($587/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $101.90 (+0.2% / 24h). Decentralization: Nakamoto coefficient 18, 677 active validators, 0.4% of stake delinquent. Anomaly scan: all clear across every monitored metric.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 446,598,920 |
| Block height | 424,641,632 |
| Epoch | 1033 (79.38% complete, ~7.8h left) |
| TPS (10 min avg) | 3,907 |
| Non-vote TPS | 1,764 |
| Slot time (measured) | 314.0 ms |
| Est. daily transactions | 311,844,641 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0056 |
| Node version | 4.3.0-rc.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $101.90 (+0.2%/24h) |
| Market cap | $59.8B |
| **REV (24h)** | **$845.8K** (fees $708.8K + Jito tips $137.0K) |
| Chain TVL | $5.9B |
| Stablecoin supply | $16.5B |
| DEX volume (24h) | $2.5B (-22.3%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 586,644,878 SOL |
| Inflation | 3.65% |

Top DEXs by 24h volume: BisonFi ($471.7M), PumpSwap ($377.2M), Raydium AMM ($322.2M), Tessera V ($202.0M), Meteora DLMM ($161.1M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 677 / 13 |
| Delinquent stake | 0.42% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.4% |
| Avg / median commission | 12.9% / 5% |

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

**55/100 — Neutral** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 70.3 |
| fear greed | 61 |
| momentum | 34.4 |
| news | 58 |

Crypto Fear & Greed: 61 (Greed) · CoinGecko votes bullish: 70.27% · headline tone (48h): +1

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 120 |
| Raydium AMM v4 | 131 |
| Orca Whirlpool | 144 |
| Pump.fun | 144 |
| Tensor | 1 |
| Magic Eden v2 | 70 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,188,448 |
| Binance (cold) | 1,907,923 |
| OKX (attributed) | 232,182 |
| Coinbase (hot) | 23,264 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 314ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at ?% of stake.
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
| solana_rpc | OK | 8975 ms |
| solana_rpc_validators | OK | 392 ms |
| coingecko | OK | 1797 ms |
| defillama_tvl | OK | 128 ms |
| defillama_dex | OK | 1486 ms |
| defillama_fees | OK | 1932 ms |
| defillama_stablecoins | OK | 224 ms |
| defillama_xstocks | OK | 773 ms |
| jito_kobe | OK | 313 ms |
| stakewiz | FAILED | 7655 ms |
| github | OK | 910 ms |
| solana_com_news | OK | 129 ms |
| sentiment | OK | 2431 ms |
| solana_status_page | OK | 473 ms |
| solana_rpc_whales | OK | 1256 ms |
| solana_rpc_programs | OK | 2183 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*