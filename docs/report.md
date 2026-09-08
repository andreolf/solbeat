# Solbeat — State of the Solana Network

> Generated 2026-09-08T17:20:39Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1031 is 0% complete (~38h remaining), with the cluster processing ~4,596 TPS (2,473 non-vote). Measured slot time is 317ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $852.6K of Real Economic Value over the last 24h ($592/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $104.01 (-0.1% / 24h). Decentralization: Nakamoto coefficient 18, 676 active validators, 0.0% of stake delinquent. Alpenglow readiness: validators holding 99% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 1 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 445,393,704 |
| Block height | 423,437,662 |
| Epoch | 1031 (0.39% complete, ~37.9h left) |
| TPS (10 min avg) | 4,596 |
| Non-vote TPS | 2,473 |
| Slot time (measured) | 317.0 ms |
| Est. daily transactions | 375,849,856 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0039 |
| Node version | 4.2.2 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $104.01 (-0.1%/24h) |
| Market cap | $61.0B |
| **REV (24h)** | **$852.6K** (fees $750.7K + Jito tips $102.0K) |
| Chain TVL | $5.9B |
| Stablecoin supply | $16.6B |
| DEX volume (24h) | $2.7B (-6.3%/1d) |
| Tokenized equities (xStocks TVL) | $444.6M |
| Circulating supply | 586,251,418 SOL |
| Inflation | 3.66% |

Top DEXs by 24h volume: PumpSwap ($873.4M), Raydium AMM ($294.9M), Orca DEX ($218.8M), BisonFi ($204.1M), Meteora DLMM ($195.3M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 676 / 11 |
| Delinquent stake | 0.01% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.2% |
| Avg / median commission | 12.5% / 5.0% |
| Alpenglow BLS-key readiness | 691 validators, 99.0% of stake |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L43ZWjwCHART3o…` | 17,436,766 | 3.98% | 7% |
| 2 | `he1iusunGwqrNtafDtLd…` | 16,345,792 | 3.73% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5…` | 12,527,540 | 2.86% | 0% |
| 4 | `CatzoSMUkTRidT5DwBxA…` | 11,388,333 | 2.6% | 5% |
| 5 | `8GbwASqdpw4dVcwbWUxb…` | 9,566,721 | 2.18% | 0% |
| 6 | `26pV97Ce83ZQ6Kz9XT4t…` | 9,286,723 | 2.12% | 7% |
| 7 | `51JBzSTU5rAM8gLAVQKg…` | 9,027,481 | 2.06% | 10% |
| 8 | `9QU2QSxhb24FUX3Tu2Fp…` | 7,322,728 | 1.67% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJn…` | 6,860,585 | 1.56% | 5% |
| 10 | `DumiCKHVqoCQKD8roLAp…` | 6,604,066 | 1.51% | 0% |

## Signals (anomaly detection)

- **[WARNING]** Solana TVL surge (z=+2.2 vs its recent baseline)

## Solana Pulse — sentiment (experimental)

**70/100 — Bullish** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 80.6 |
| fear greed | 69 |
| momentum | 49.7 |
| news | 90 |

Crypto Fear & Greed: 69 (Greed) · CoinGecko votes bullish: 80.56% · headline tone (48h): +5

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 125 |
| Raydium AMM v4 | 137 |
| Orca Whirlpool | 137 |
| Pump.fun | 137 |
| Tensor | 0 |
| Magic Eden v2 | 75 |
| Marinade | 4 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,188,448 |
| Binance (cold) | 1,741,204 |
| OKX (attributed) | 210,992 |
| Coinbase (hot) | 30,715 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 317ms.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 99.0% of stake.
- **Agave**: latest release None · running 4.2.2 on the polled node.
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
| solana_rpc | OK | 8173 ms |
| solana_rpc_validators | OK | 79 ms |
| coingecko | OK | 1638 ms |
| defillama_tvl | OK | 44 ms |
| defillama_dex | OK | 1225 ms |
| defillama_fees | OK | 118 ms |
| defillama_stablecoins | OK | 59 ms |
| defillama_xstocks | OK | 86 ms |
| jito_kobe | OK | 227 ms |
| stakewiz | OK | 663 ms |
| github | FAILED | 6045 ms |
| solana_com_news | OK | 51 ms |
| sentiment | OK | 2245 ms |
| solana_status_page | OK | 239 ms |
| solana_rpc_whales | OK | 824 ms |
| solana_rpc_programs | OK | 1357 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*