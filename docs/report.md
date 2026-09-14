# Solbeat — State of the Solana Network

> Generated 2026-09-14T23:49:37Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1034 is 97% complete (~1h remaining), with the cluster processing ~3,829 TPS (1,679 non-vote). Measured slot time is 314ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $705.1K of Real Economic Value over the last 24h ($490/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $102.59 (+3.0% / 24h). Decentralization: Nakamoto coefficient 18, 679 active validators, 0.0% of stake delinquent. Alpenglow readiness: validators holding 99% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: all clear across every monitored metric.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 447,105,751 |
| Block height | 425,148,081 |
| Epoch | 1034 (96.7% complete, ~1.2h left) |
| TPS (10 min avg) | 3,829 |
| Non-vote TPS | 1,679 |
| Slot time (measured) | 314.5 ms |
| Est. daily transactions | 355,616,763 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0035 |
| Node version | 4.3.0-rc.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $102.59 (+3.0%/24h) |
| Market cap | $60.2B |
| **REV (24h)** | **$705.1K** (fees $608.1K + Jito tips $97.0K) |
| Chain TVL | $6.0B |
| Stablecoin supply | $16.3B |
| DEX volume (24h) | $1.8B (2.7%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 586,892,305 SOL |
| Inflation | 3.65% |

Top DEXs by 24h volume: Raydium AMM ($321.4M), PumpSwap ($315.7M), BisonFi ($201.5M), Orca DEX ($176.7M), fomo Wallet ($166.8M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 679 / 11 |
| Delinquent stake | 0.04% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.3% |
| Avg / median commission | 12.8% / 5% |
| Alpenglow BLS-key readiness | 697 validators, 99.3% of stake |

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

**62/100 — Bullish** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 73.5 |
| fear greed | 57 |
| momentum | 49.5 |
| news | 74 |

Crypto Fear & Greed: 57 (Greed) · CoinGecko votes bullish: 73.53% · headline tone (48h): +3

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 133 |
| Raydium AMM v4 | 122 |
| Orca Whirlpool | 162 |
| Pump.fun | 162 |
| Tensor | 2 |
| Magic Eden v2 | 59 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,188,448 |
| Binance (cold) | 1,772,545 |
| OKX (attributed) | 232,082 |
| Coinbase (hot) | 30,998 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 314ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 99.3% of stake.
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
| solana_rpc | OK | 10590 ms |
| solana_rpc_validators | OK | 923 ms |
| coingecko | OK | 1721 ms |
| defillama_tvl | OK | 95 ms |
| defillama_dex | OK | 1187 ms |
| defillama_fees | OK | 2076 ms |
| defillama_stablecoins | OK | 180 ms |
| defillama_xstocks | OK | 860 ms |
| jito_kobe | OK | 243 ms |
| stakewiz | OK | 1106 ms |
| github | OK | 985 ms |
| solana_com_news | OK | 119 ms |
| sentiment | OK | 2408 ms |
| solana_status_page | OK | 571 ms |
| solana_rpc_whales | OK | 2374 ms |
| solana_rpc_programs | OK | 3837 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*