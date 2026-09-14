# Solbeat — State of the Solana Network

> Generated 2026-09-14T02:36:20Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1034 is 41% complete (~22h remaining), with the cluster processing ~3,947 TPS (1,809 non-vote). Measured slot time is 316ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $703.1K of Real Economic Value over the last 24h ($488/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $100.86 (-1.1% / 24h). Decentralization: Nakamoto coefficient 18, 678 active validators, 0.6% of stake delinquent. Alpenglow readiness: validators holding 99% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: all clear across every monitored metric.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 446,863,935 |
| Block height | 424,906,480 |
| Epoch | 1034 (40.73% complete, ~22.5h left) |
| TPS (10 min avg) | 3,947 |
| Non-vote TPS | 1,809 |
| Slot time (measured) | 315.8 ms |
| Est. daily transactions | 343,396,206 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0038 |
| Node version | 4.3.0-rc.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $100.86 (-1.1%/24h) |
| Market cap | $59.2B |
| **REV (24h)** | **$703.1K** (fees $608.1K + Jito tips $95.0K) |
| Chain TVL | $5.8B |
| Stablecoin supply | $16.3B |
| DEX volume (24h) | $1.6B (-6.1%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 586,893,092 SOL |
| Inflation | 3.65% |

Top DEXs by 24h volume: PumpSwap ($315.7M), Raydium AMM ($265.0M), fomo Wallet ($169.8M), BisonFi ($162.7M), Meteora DLMM ($157.7M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 678 / 12 |
| Delinquent stake | 0.61% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.3% |
| Avg / median commission | 12.5% / 5.0% |
| Alpenglow BLS-key readiness | 696 validators, 99.0% of stake |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L43ZWjwCHART3o…` | 17,568,189 | 4.0% | 7% |
| 2 | `he1iusunGwqrNtafDtLd…` | 16,361,599 | 3.73% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5…` | 12,501,349 | 2.85% | 0% |
| 4 | `CatzoSMUkTRidT5DwBxA…` | 11,372,391 | 2.59% | 5% |
| 5 | `8GbwASqdpw4dVcwbWUxb…` | 9,619,665 | 2.19% | 0% |
| 6 | `26pV97Ce83ZQ6Kz9XT4t…` | 9,252,712 | 2.11% | 7% |
| 7 | `51JBzSTU5rAM8gLAVQKg…` | 9,025,175 | 2.06% | 10% |
| 8 | `9QU2QSxhb24FUX3Tu2Fp…` | 7,367,885 | 1.68% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJn…` | 6,943,003 | 1.58% | 5% |
| 10 | `DumiCKHVqoCQKD8roLAp…` | 6,552,506 | 1.49% | 0% |

## Signals (anomaly detection)

All clear — no anomalies across monitored metrics.

## Solana Pulse — sentiment (experimental)

**58/100 — Neutral** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 78.8 |
| fear greed | 57 |
| momentum | 41.1 |
| news | 50 |

Crypto Fear & Greed: 57 (Greed) · CoinGecko votes bullish: 78.79% · headline tone (48h): +0

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 124 |
| Raydium AMM v4 | 107 |
| Orca Whirlpool | 124 |
| Pump.fun | 149 |
| Tensor | 1 |
| Magic Eden v2 | 45 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,188,448 |
| Binance (cold) | 1,893,897 |
| OKX (attributed) | 232,082 |
| Coinbase (hot) | 24,459 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 316ms · proposal merged.
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
| solana_rpc | OK | 9150 ms |
| solana_rpc_validators | OK | 480 ms |
| coingecko | OK | 1841 ms |
| defillama_tvl | OK | 237 ms |
| defillama_dex | OK | 1198 ms |
| defillama_fees | OK | 2101 ms |
| defillama_stablecoins | OK | 131 ms |
| defillama_xstocks | OK | 57 ms |
| jito_kobe | OK | 295 ms |
| stakewiz | OK | 1407 ms |
| github | OK | 940 ms |
| solana_com_news | OK | 124 ms |
| sentiment | OK | 2559 ms |
| solana_status_page | OK | 371 ms |
| solana_rpc_whales | OK | 1348 ms |
| solana_rpc_programs | OK | 2362 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*