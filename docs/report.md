# Solbeat — State of the Solana Network

> Generated 2026-09-13T23:56:31Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1034 is 34% complete (~25h remaining), with the cluster processing ~3,866 TPS (1,728 non-vote). Measured slot time is 316ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $802.4K of Real Economic Value over the last 24h ($557/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $99.35 (-2.4% / 24h). Decentralization: Nakamoto coefficient 18, 678 active validators, 0.4% of stake delinquent. Alpenglow readiness: validators holding 99% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: all clear across every monitored metric.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 446,833,591 |
| Block height | 424,876,156 |
| Epoch | 1034 (33.7% complete, ~25.1h left) |
| TPS (10 min avg) | 3,866 |
| Non-vote TPS | 1,728 |
| Slot time (measured) | 315.8 ms |
| Est. daily transactions | 343,351,986 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0045 |
| Node version | 4.3.0-rc.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $99.35 (-2.4%/24h) |
| Market cap | $58.3B |
| **REV (24h)** | **$802.4K** (fees $708.8K + Jito tips $93.5K) |
| Chain TVL | $5.9B |
| Stablecoin supply | $16.5B |
| DEX volume (24h) | $1.7B (-45.2%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 586,730,694 SOL |
| Inflation | 3.65% |

Top DEXs by 24h volume: PumpSwap ($377.2M), Raydium AMM ($257.1M), fomo Wallet ($170.2M), BisonFi ($162.7M), Meteora DLMM ($161.1M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 678 / 12 |
| Delinquent stake | 0.44% |
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

**55/100 — Neutral** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 80.0 |
| fear greed | 61 |
| momentum | 27.5 |
| news | 50 |

Crypto Fear & Greed: 61 (Greed) · CoinGecko votes bullish: 80.0% · headline tone (48h): +0

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 124 |
| Raydium AMM v4 | 135 |
| Orca Whirlpool | 135 |
| Pump.fun | 148 |
| Tensor | 1 |
| Magic Eden v2 | 68 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,188,448 |
| Binance (cold) | 1,880,611 |
| OKX (attributed) | 232,082 |
| Coinbase (hot) | 24,137 |

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
| solana_rpc | OK | 8448 ms |
| solana_rpc_validators | OK | 410 ms |
| coingecko | OK | 1807 ms |
| defillama_tvl | OK | 400 ms |
| defillama_dex | OK | 1064 ms |
| defillama_fees | OK | 1784 ms |
| defillama_stablecoins | OK | 707 ms |
| defillama_xstocks | OK | 90 ms |
| jito_kobe | OK | 322 ms |
| stakewiz | OK | 1255 ms |
| github | OK | 905 ms |
| solana_com_news | OK | 134 ms |
| sentiment | OK | 2352 ms |
| solana_status_page | OK | 436 ms |
| solana_rpc_whales | OK | 1284 ms |
| solana_rpc_programs | OK | 2263 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*