# Solbeat — State of the Solana Network

> Generated 2026-09-16T18:14:21Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1036 is 8% complete (~35h remaining), with the cluster processing ~6,149 TPS (4,052 non-vote). Measured slot time is 321ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $826.9K of Real Economic Value over the last 24h ($574/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $98.30 (-1.5% / 24h). Decentralization: Nakamoto coefficient 18, 677 active validators, 0.0% of stake delinquent. Alpenglow readiness: validators holding 99% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 1 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 447,588,081 |
| Block height | 425,629,499 |
| Epoch | 1036 (8.35% complete, ~35.3h left) |
| TPS (10 min avg) | 6,149 |
| Non-vote TPS | 4,052 |
| Slot time (measured) | 321.2 ms |
| Est. daily transactions | 393,348,015 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0033 |
| Node version | 4.3.0-rc.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $98.30 (-1.5%/24h) |
| Market cap | $57.7B |
| **REV (24h)** | **$826.9K** (fees $693.2K + Jito tips $133.7K) |
| Chain TVL | $5.7B |
| Stablecoin supply | $15.9B |
| DEX volume (24h) | $2.7B (6.8%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 587,150,523 SOL |
| Inflation | 3.64% |

Top DEXs by 24h volume: PumpSwap ($519.3M), BisonFi ($353.6M), HumidiFi ($232.0M), fomo Wallet ($226.5M), Raydium AMM ($199.7M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 677 / 14 |
| Delinquent stake | 0.04% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.3% |
| Avg / median commission | 12.4% / 5% |
| Alpenglow BLS-key readiness | 698 validators, 99.4% of stake |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L43ZWjwCHART3o…` | 17,767,428 | 4.04% | 7% |
| 2 | `he1iusunGwqrNtafDtLd…` | 16,352,114 | 3.72% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5…` | 12,485,145 | 2.84% | 0% |
| 4 | `CatzoSMUkTRidT5DwBxA…` | 11,383,247 | 2.59% | 5% |
| 5 | `8GbwASqdpw4dVcwbWUxb…` | 9,740,877 | 2.22% | 0% |
| 6 | `26pV97Ce83ZQ6Kz9XT4t…` | 9,256,273 | 2.1% | 7% |
| 7 | `51JBzSTU5rAM8gLAVQKg…` | 9,049,051 | 2.06% | 10% |
| 8 | `9QU2QSxhb24FUX3Tu2Fp…` | 7,386,183 | 1.68% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJn…` | 7,076,306 | 1.61% | 5% |
| 10 | `DumiCKHVqoCQKD8roLAp…` | 6,558,592 | 1.49% | 0% |

## Signals (anomaly detection)

- **[SERIOUS]** TPS spike: 6,149 vs 12h mean 4,488 (z=+3.9)

## Solana Pulse — sentiment (experimental)

**58/100 — Neutral** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 75.8 |
| fear greed | 51 |
| momentum | 46.0 |
| news | 58 |

Crypto Fear & Greed: 51 (Neutral) · CoinGecko votes bullish: 75.76% · headline tone (48h): +1

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 128 |
| Raydium AMM v4 | 128 |
| Orca Whirlpool | 128 |
| Pump.fun | 128 |
| Tensor | 0 |
| Magic Eden v2 | 52 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,188,448 |
| Binance (cold) | 2,008,177 |
| OKX (attributed) | 232,949 |
| Coinbase (hot) | 19,161 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 321ms · proposal merged.
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
| solana_rpc | OK | 9800 ms |
| solana_rpc_validators | OK | 634 ms |
| coingecko | OK | 1733 ms |
| defillama_tvl | OK | 143 ms |
| defillama_dex | OK | 775 ms |
| defillama_fees | OK | 84 ms |
| defillama_stablecoins | OK | 158 ms |
| defillama_xstocks | OK | 38 ms |
| jito_kobe | OK | 226 ms |
| stakewiz | OK | 995 ms |
| github | OK | 568 ms |
| solana_com_news | OK | 67 ms |
| sentiment | OK | 2094 ms |
| solana_status_page | OK | 270 ms |
| solana_rpc_whales | OK | 1645 ms |
| solana_rpc_programs | OK | 2912 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*