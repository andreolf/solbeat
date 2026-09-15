# Solbeat — State of the Solana Network

> Generated 2026-09-15T11:00:11Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1035 is 26% complete (~28h remaining), with the cluster processing ~3,609 TPS (1,473 non-vote). Measured slot time is 316ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $757.4K of Real Economic Value over the last 24h ($526/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $100.97 (-0.8% / 24h). Decentralization: Nakamoto coefficient 18, 678 active validators, 0.1% of stake delinquent. Alpenglow readiness: validators holding 99% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: all clear across every monitored metric.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 447,233,219 |
| Block height | 425,275,119 |
| Epoch | 1035 (26.21% complete, ~28.0h left) |
| TPS (10 min avg) | 3,609 |
| Non-vote TPS | 1,473 |
| Slot time (measured) | 315.7 ms |
| Est. daily transactions | 302,250,377 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0055 |
| Node version | 4.3.0-rc.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $100.97 (-0.8%/24h) |
| Market cap | $59.3B |
| **REV (24h)** | **$757.4K** (fees $647.0K + Jito tips $110.4K) |
| Chain TVL | $5.8B |
| Stablecoin supply | $16.3B |
| DEX volume (24h) | $2.5B (41.3%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 587,028,078 SOL |
| Inflation | 3.65% |

Top DEXs by 24h volume: PumpSwap ($445.4M), BisonFi ($315.8M), Raydium AMM ($254.6M), Meteora DLMM ($198.8M), fomo Wallet ($190.2M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 678 / 11 |
| Delinquent stake | 0.07% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.3% |
| Avg / median commission | 12.2% / 5.0% |
| Alpenglow BLS-key readiness | 698 validators, 99.4% of stake |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L43ZWjwCHART3o…` | 17,757,712 | 4.04% | 7% |
| 2 | `he1iusunGwqrNtafDtLd…` | 16,373,377 | 3.73% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5…` | 12,492,605 | 2.84% | 0% |
| 4 | `CatzoSMUkTRidT5DwBxA…` | 11,369,566 | 2.59% | 5% |
| 5 | `8GbwASqdpw4dVcwbWUxb…` | 9,669,319 | 2.2% | 0% |
| 6 | `26pV97Ce83ZQ6Kz9XT4t…` | 9,256,225 | 2.11% | 7% |
| 7 | `51JBzSTU5rAM8gLAVQKg…` | 9,035,103 | 2.06% | 10% |
| 8 | `9QU2QSxhb24FUX3Tu2Fp…` | 7,372,355 | 1.68% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJn…` | 6,944,775 | 1.58% | 5% |
| 10 | `DumiCKHVqoCQKD8roLAp…` | 6,553,626 | 1.49% | 0% |

## Signals (anomaly detection)

All clear — no anomalies across monitored metrics.

## Solana Pulse — sentiment (experimental)

**65/100 — Bullish** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 74.3 |
| fear greed | 69 |
| momentum | 61.4 |
| news | 50 |

Crypto Fear & Greed: 69 (Greed) · CoinGecko votes bullish: 74.29% · headline tone (48h): +0

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 127 |
| Raydium AMM v4 | 109 |
| Orca Whirlpool | 139 |
| Pump.fun | 139 |
| Tensor | 0 |
| Magic Eden v2 | 36 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,188,448 |
| Binance (cold) | 1,761,905 |
| OKX (attributed) | 232,082 |
| Coinbase (hot) | 16,185 |

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
| solana_rpc | OK | 8443 ms |
| solana_rpc_validators | OK | 108 ms |
| coingecko | OK | 1572 ms |
| defillama_tvl | OK | 56 ms |
| defillama_dex | OK | 759 ms |
| defillama_fees | OK | 914 ms |
| defillama_stablecoins | OK | 251 ms |
| defillama_xstocks | OK | 30 ms |
| jito_kobe | OK | 74 ms |
| stakewiz | OK | 1009 ms |
| github | OK | 625 ms |
| solana_com_news | OK | 51 ms |
| sentiment | OK | 2066 ms |
| solana_status_page | OK | 305 ms |
| solana_rpc_whales | OK | 767 ms |
| solana_rpc_programs | OK | 1758 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*