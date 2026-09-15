# Solbeat — State of the Solana Network

> Generated 2026-09-15T13:01:36Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1035 is 32% complete (~26h remaining), with the cluster processing ~3,708 TPS (1,570 non-vote). Measured slot time is 316ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $757.5K of Real Economic Value over the last 24h ($526/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $100.97 (-0.3% / 24h). Decentralization: Nakamoto coefficient 18, 677 active validators, 0.1% of stake delinquent. Alpenglow readiness: validators holding 99% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: all clear across every monitored metric.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 447,256,295 |
| Block height | 425,298,167 |
| Epoch | 1035 (31.55% complete, ~25.9h left) |
| TPS (10 min avg) | 3,708 |
| Non-vote TPS | 1,570 |
| Slot time (measured) | 315.5 ms |
| Est. daily transactions | 303,092,473 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0055 |
| Node version | 4.3.0-rc.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $100.97 (-0.3%/24h) |
| Market cap | $59.2B |
| **REV (24h)** | **$757.5K** (fees $647.0K + Jito tips $110.5K) |
| Chain TVL | $5.9B |
| Stablecoin supply | $16.3B |
| DEX volume (24h) | $2.5B (41.3%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 587,028,011 SOL |
| Inflation | 3.65% |

Top DEXs by 24h volume: PumpSwap ($445.4M), BisonFi ($315.8M), Raydium AMM ($240.2M), Meteora DLMM ($198.8M), fomo Wallet ($192.0M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 677 / 12 |
| Delinquent stake | 0.1% |
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

**65/100 — Bullish** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 76.3 |
| fear greed | 69 |
| momentum | 61.5 |
| news | 42 |

Crypto Fear & Greed: 69 (Greed) · CoinGecko votes bullish: 76.32% · headline tone (48h): -1

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 134 |
| Raydium AMM v4 | 134 |
| Orca Whirlpool | 134 |
| Pump.fun | 147 |
| Tensor | 0 |
| Magic Eden v2 | 57 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,188,448 |
| Binance (cold) | 1,796,216 |
| OKX (attributed) | 232,082 |
| Coinbase (hot) | 48,469 |

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
| solana_rpc | OK | 7493 ms |
| solana_rpc_validators | OK | 168 ms |
| coingecko | OK | 1678 ms |
| defillama_tvl | OK | 40 ms |
| defillama_dex | OK | 803 ms |
| defillama_fees | OK | 1280 ms |
| defillama_stablecoins | OK | 64 ms |
| defillama_xstocks | OK | 36 ms |
| jito_kobe | OK | 189 ms |
| stakewiz | OK | 694 ms |
| github | OK | 593 ms |
| solana_com_news | OK | 97 ms |
| sentiment | OK | 2059 ms |
| solana_status_page | OK | 215 ms |
| solana_rpc_whales | OK | 782 ms |
| solana_rpc_programs | OK | 1874 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*