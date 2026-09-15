# Solbeat — State of the Solana Network

> Generated 2026-09-15T14:51:05Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1035 is 36% complete (~24h remaining), with the cluster processing ~4,522 TPS (2,404 non-vote). Measured slot time is 318ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $754.1K of Real Economic Value over the last 24h ($524/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $98.48 (-3.2% / 24h). Decentralization: Nakamoto coefficient 18, 677 active validators, 0.1% of stake delinquent. Alpenglow readiness: validators holding 99% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 1 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 447,277,077 |
| Block height | 425,318,925 |
| Epoch | 1035 (36.36% complete, ~24.2h left) |
| TPS (10 min avg) | 4,522 |
| Non-vote TPS | 2,404 |
| Slot time (measured) | 317.5 ms |
| Est. daily transactions | 323,998,000 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0046 |
| Node version | 4.3.0-rc.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $98.48 (-3.2%/24h) |
| Market cap | $57.8B |
| **REV (24h)** | **$754.1K** (fees $647.0K + Jito tips $107.1K) |
| Chain TVL | $5.8B |
| Stablecoin supply | $16.3B |
| DEX volume (24h) | $2.5B (41.3%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 587,027,940 SOL |
| Inflation | 3.65% |

Top DEXs by 24h volume: PumpSwap ($445.4M), BisonFi ($315.8M), Raydium AMM ($233.6M), Meteora DLMM ($198.8M), fomo Wallet ($192.0M)

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

- **[WARNING]** TPS spike: 4,522 vs 12h mean 3,727 (z=+2.2)

## Solana Pulse — sentiment (experimental)

**65/100 — Bullish** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 75.0 |
| fear greed | 69 |
| momentum | 59.0 |
| news | 50 |

Crypto Fear & Greed: 69 (Greed) · CoinGecko votes bullish: 75.0% · headline tone (48h): +0

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 131 |
| Raydium AMM v4 | 120 |
| Orca Whirlpool | 143 |
| Pump.fun | 143 |
| Tensor | 0 |
| Magic Eden v2 | 51 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,188,448 |
| Binance (cold) | 1,690,727 |
| OKX (attributed) | 232,082 |
| Coinbase (hot) | 46,859 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 318ms · proposal merged.
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
| solana_rpc | OK | 9823 ms |
| solana_rpc_validators | OK | 468 ms |
| coingecko | OK | 1754 ms |
| defillama_tvl | OK | 84 ms |
| defillama_dex | OK | 1198 ms |
| defillama_fees | OK | 2091 ms |
| defillama_stablecoins | OK | 1205 ms |
| defillama_xstocks | OK | 845 ms |
| jito_kobe | OK | 256 ms |
| stakewiz | OK | 1744 ms |
| github | OK | 1006 ms |
| solana_com_news | OK | 121 ms |
| sentiment | OK | 2470 ms |
| solana_status_page | OK | 43414 ms |
| solana_rpc_whales | OK | 1451 ms |
| solana_rpc_programs | OK | 2895 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*