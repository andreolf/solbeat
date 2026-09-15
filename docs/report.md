# Solbeat — State of the Solana Network

> Generated 2026-09-15T16:54:16Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1035 is 42% complete (~22h remaining), with the cluster processing ~4,016 TPS (1,892 non-vote). Measured slot time is 317ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $754.9K of Real Economic Value over the last 24h ($524/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $99.14 (-3.5% / 24h). Decentralization: Nakamoto coefficient 18, 678 active validators, 0.1% of stake delinquent. Alpenglow readiness: validators holding 99% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: all clear across every monitored metric.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 447,300,439 |
| Block height | 425,342,254 |
| Epoch | 1035 (41.77% complete, ~22.2h left) |
| TPS (10 min avg) | 4,016 |
| Non-vote TPS | 1,892 |
| Slot time (measured) | 317.3 ms |
| Est. daily transactions | 346,656,669 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0040 |
| Node version | 4.3.0-rc.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $99.14 (-3.5%/24h) |
| Market cap | $58.2B |
| **REV (24h)** | **$754.9K** (fees $647.0K + Jito tips $107.9K) |
| Chain TVL | $5.8B |
| Stablecoin supply | $16.3B |
| DEX volume (24h) | $2.5B (41.3%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 587,027,858 SOL |
| Inflation | 3.65% |

Top DEXs by 24h volume: PumpSwap ($445.4M), BisonFi ($315.8M), Raydium AMM ($241.6M), Meteora DLMM ($198.8M), fomo Wallet ($187.2M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 678 / 11 |
| Delinquent stake | 0.06% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.3% |
| Avg / median commission | 12.3% / 5.0% |
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
| community | 71.4 |
| fear greed | 69 |
| momentum | 58.6 |
| news | 58 |

Crypto Fear & Greed: 69 (Greed) · CoinGecko votes bullish: 71.43% · headline tone (48h): +1

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 132 |
| Raydium AMM v4 | 132 |
| Orca Whirlpool | 145 |
| Pump.fun | 145 |
| Tensor | 0 |
| Magic Eden v2 | 46 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,188,448 |
| Binance (cold) | 1,773,078 |
| OKX (attributed) | 232,082 |
| Coinbase (hot) | 39,764 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 317ms · proposal merged.
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
| solana_rpc | OK | 10187 ms |
| solana_rpc_validators | OK | 461 ms |
| coingecko | OK | 1706 ms |
| defillama_tvl | OK | 465 ms |
| defillama_dex | OK | 1226 ms |
| defillama_fees | OK | 2103 ms |
| defillama_stablecoins | OK | 691 ms |
| defillama_xstocks | OK | 64 ms |
| jito_kobe | OK | 460 ms |
| stakewiz | OK | 1435 ms |
| github | OK | 996 ms |
| solana_com_news | OK | 106 ms |
| sentiment | OK | 3116 ms |
| solana_status_page | OK | 428 ms |
| solana_rpc_whales | OK | 1501 ms |
| solana_rpc_programs | OK | 2678 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*