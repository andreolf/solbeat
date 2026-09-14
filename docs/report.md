# Solbeat — State of the Solana Network

> Generated 2026-09-14T21:53:58Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1034 is 92% complete (~3h remaining), with the cluster processing ~3,880 TPS (1,741 non-vote). Measured slot time is 316ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $705.2K of Real Economic Value over the last 24h ($490/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $103.25 (+2.0% / 24h). Decentralization: Nakamoto coefficient 18, 679 active validators, 0.0% of stake delinquent. Alpenglow readiness: validators holding 99% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: all clear across every monitored metric.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 447,083,849 |
| Block height | 425,126,199 |
| Epoch | 1034 (91.63% complete, ~3.2h left) |
| TPS (10 min avg) | 3,880 |
| Non-vote TPS | 1,741 |
| Slot time (measured) | 316.0 ms |
| Est. daily transactions | 361,732,450 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0034 |
| Node version | 4.3.0-rc.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $103.25 (+2.0%/24h) |
| Market cap | $60.6B |
| **REV (24h)** | **$705.2K** (fees $608.1K + Jito tips $97.1K) |
| Chain TVL | $6.0B |
| Stablecoin supply | $16.3B |
| DEX volume (24h) | $1.8B (2.7%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 586,892,389 SOL |
| Inflation | 3.65% |

Top DEXs by 24h volume: PumpSwap ($315.7M), Raydium AMM ($294.1M), BisonFi ($201.5M), Orca DEX ($178.7M), fomo Wallet ($160.9M)

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

**61/100 — Bullish** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 71.4 |
| fear greed | 57 |
| momentum | 50.1 |
| news | 66 |

Crypto Fear & Greed: 57 (Greed) · CoinGecko votes bullish: 71.43% · headline tone (48h): +2

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 137 |
| Raydium AMM v4 | 137 |
| Orca Whirlpool | 151 |
| Pump.fun | 168 |
| Tensor | 2 |
| Magic Eden v2 | 75 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,188,448 |
| Binance (cold) | 1,794,132 |
| OKX (attributed) | 232,082 |
| Coinbase (hot) | 31,561 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 316ms · proposal merged.
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
| solana_rpc | OK | 11808 ms |
| solana_rpc_validators | OK | 1677 ms |
| coingecko | OK | 1650 ms |
| defillama_tvl | OK | 206 ms |
| defillama_dex | OK | 415 ms |
| defillama_fees | OK | 671 ms |
| defillama_stablecoins | OK | 52 ms |
| defillama_xstocks | OK | 65 ms |
| jito_kobe | OK | 230 ms |
| stakewiz | OK | 793 ms |
| github | OK | 582 ms |
| solana_com_news | OK | 192 ms |
| sentiment | OK | 2071 ms |
| solana_status_page | OK | 290 ms |
| solana_rpc_whales | OK | 2882 ms |
| solana_rpc_programs | OK | 5154 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*