# Solbeat — State of the Solana Network

> Generated 2026-09-15T12:00:57Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1035 is 29% complete (~27h remaining), with the cluster processing ~3,488 TPS (1,342 non-vote). Measured slot time is 314ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $757.7K of Real Economic Value over the last 24h ($526/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $100.79 (-0.5% / 24h). Decentralization: Nakamoto coefficient 18, 679 active validators, 0.1% of stake delinquent. Alpenglow readiness: validators holding 99% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: all clear across every monitored metric.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 447,244,760 |
| Block height | 425,286,640 |
| Epoch | 1035 (28.88% complete, ~26.8h left) |
| TPS (10 min avg) | 3,488 |
| Non-vote TPS | 1,342 |
| Slot time (measured) | 314.3 ms |
| Est. daily transactions | 301,019,133 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0056 |
| Node version | 4.3.0-rc.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $100.79 (-0.5%/24h) |
| Market cap | $59.2B |
| **REV (24h)** | **$757.7K** (fees $647.0K + Jito tips $110.7K) |
| Chain TVL | $5.8B |
| Stablecoin supply | $16.3B |
| DEX volume (24h) | $2.5B (41.3%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 587,028,046 SOL |
| Inflation | 3.65% |

Top DEXs by 24h volume: PumpSwap ($445.4M), BisonFi ($315.8M), Raydium AMM ($247.9M), Meteora DLMM ($198.8M), fomo Wallet ($190.2M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 679 / 10 |
| Delinquent stake | 0.05% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.3% |
| Avg / median commission | 12.2% / 5% |
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

**64/100 — Bullish** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 73.7 |
| fear greed | 69 |
| momentum | 61.2 |
| news | 42 |

Crypto Fear & Greed: 69 (Greed) · CoinGecko votes bullish: 73.68% · headline tone (48h): -1

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 122 |
| Raydium AMM v4 | 122 |
| Orca Whirlpool | 132 |
| Pump.fun | 122 |
| Tensor | 0 |
| Magic Eden v2 | 78 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,188,448 |
| Binance (cold) | 1,766,022 |
| OKX (attributed) | 232,082 |
| Coinbase (hot) | 49,258 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 314ms · proposal merged.
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
| solana_rpc | OK | 7478 ms |
| solana_rpc_validators | OK | 98 ms |
| coingecko | OK | 1621 ms |
| defillama_tvl | OK | 43 ms |
| defillama_dex | OK | 474 ms |
| defillama_fees | OK | 698 ms |
| defillama_stablecoins | OK | 59 ms |
| defillama_xstocks | OK | 28 ms |
| jito_kobe | OK | 179 ms |
| stakewiz | OK | 760 ms |
| github | OK | 559 ms |
| solana_com_news | OK | 80 ms |
| sentiment | OK | 2010 ms |
| solana_status_page | OK | 397 ms |
| solana_rpc_whales | OK | 767 ms |
| solana_rpc_programs | OK | 1778 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*