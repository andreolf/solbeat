# Solbeat — State of the Solana Network

> Generated 2026-09-15T01:21:39Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1035 is 1% complete (~38h remaining), with the cluster processing ~3,754 TPS (1,624 non-vote). Measured slot time is 317ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $704.1K of Real Economic Value over the last 24h ($489/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $102.33 (+3.0% / 24h). Decentralization: Nakamoto coefficient 18, 678 active validators, 0.1% of stake delinquent. Alpenglow readiness: validators holding 99% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: all clear across every monitored metric.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 447,123,229 |
| Block height | 425,165,543 |
| Epoch | 1035 (0.75% complete, ~37.8h left) |
| TPS (10 min avg) | 3,754 |
| Non-vote TPS | 1,624 |
| Slot time (measured) | 317.0 ms |
| Est. daily transactions | 345,822,336 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0038 |
| Node version | 4.3.0-rc.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $102.33 (+3.0%/24h) |
| Market cap | $60.1B |
| **REV (24h)** | **$704.1K** (fees $608.1K + Jito tips $96.0K) |
| Chain TVL | $5.9B |
| Stablecoin supply | $16.3B |
| DEX volume (24h) | $2.1B (15.5%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 587,028,560 SOL |
| Inflation | 3.65% |

Top DEXs by 24h volume: Raydium AMM ($322.0M), PumpSwap ($315.7M), BisonFi ($201.5M), Meteora DLMM ($198.8M), Orca DEX ($172.3M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 678 / 11 |
| Delinquent stake | 0.08% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.3% |
| Avg / median commission | 12.5% / 5.0% |
| Alpenglow BLS-key readiness | 697 validators, 99.3% of stake |

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

**63/100 — Bullish** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 71.9 |
| fear greed | 69 |
| momentum | 57.0 |
| news | 50 |

Crypto Fear & Greed: 69 (Greed) · CoinGecko votes bullish: 71.88% · headline tone (48h): +0

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 134 |
| Raydium AMM v4 | 134 |
| Orca Whirlpool | 147 |
| Pump.fun | 147 |
| Tensor | 0 |
| Magic Eden v2 | 55 |
| Marinade | 4 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,188,448 |
| Binance (cold) | 1,778,716 |
| OKX (attributed) | 232,082 |
| Coinbase (hot) | 29,419 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 317ms · proposal merged.
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
| solana_rpc | OK | 9680 ms |
| solana_rpc_validators | OK | 475 ms |
| coingecko | OK | 1955 ms |
| defillama_tvl | OK | 366 ms |
| defillama_dex | OK | 742 ms |
| defillama_fees | OK | 341 ms |
| defillama_stablecoins | OK | 382 ms |
| defillama_xstocks | OK | 826 ms |
| jito_kobe | OK | 242 ms |
| stakewiz | OK | 1435 ms |
| github | OK | 989 ms |
| solana_com_news | OK | 132 ms |
| sentiment | OK | 2414 ms |
| solana_status_page | OK | 365 ms |
| solana_rpc_whales | OK | 1427 ms |
| solana_rpc_programs | OK | 2396 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*