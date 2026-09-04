# Solbeat — State of the Solana Network

> Generated 2026-09-04T18:17:55Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1028 is 50% complete (~19h remaining), with the cluster processing ~3,616 TPS (1,487 non-vote). Measured slot time is 314ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $698.2K of Real Economic Value over the last 24h ($485/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $101.38 (-3.3% / 24h). Decentralization: Nakamoto coefficient 18, 677 active validators, 0.0% of stake delinquent. Alpenglow readiness: validators holding 99% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 1 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 444,311,471 |
| Block height | 422,357,020 |
| Epoch | 1028 (49.88% complete, ~18.9h left) |
| TPS (10 min avg) | 3,616 |
| Non-vote TPS | 1,487 |
| Slot time (measured) | 313.5 ms |
| Est. daily transactions | 349,574,147 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0036 |
| Node version | 4.2.2 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $101.38 (-3.3%/24h) |
| Market cap | $59.3B |
| **REV (24h)** | **$698.2K** (fees $594.5K + Jito tips $103.7K) |
| Chain TVL | $5.8B |
| Stablecoin supply | $16.6B |
| DEX volume (24h) | $2.5B (7.4%/1d) |
| Tokenized equities (xStocks TVL) | $448.5M |
| Circulating supply | 585,360,114 SOL |
| Inflation | 3.66% |

Top DEXs by 24h volume: PumpSwap ($838.7M), Orca DEX ($279.9M), BisonFi ($232.5M), Meteora DLMM ($186.5M), Raydium AMM ($168.2M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 677 / 18 |
| Delinquent stake | 0.03% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.4% |
| Avg / median commission | 12.5% / 5% |
| Alpenglow BLS-key readiness | 690 validators, 99.3% of stake |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L43ZWjwCHART3o…` | 17,393,318 | 3.98% | 7% |
| 2 | `he1iusunGwqrNtafDtLd…` | 16,324,259 | 3.74% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5…` | 12,459,602 | 2.85% | 0% |
| 4 | `CatzoSMUkTRidT5DwBxA…` | 11,379,843 | 2.6% | 5% |
| 5 | `8GbwASqdpw4dVcwbWUxb…` | 9,567,623 | 2.19% | 0% |
| 6 | `26pV97Ce83ZQ6Kz9XT4t…` | 9,278,151 | 2.12% | 7% |
| 7 | `51JBzSTU5rAM8gLAVQKg…` | 9,042,760 | 2.07% | 10% |
| 8 | `9QU2QSxhb24FUX3Tu2Fp…` | 7,376,879 | 1.69% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJn…` | 7,127,366 | 1.63% | 5% |
| 10 | `DumiCKHVqoCQKD8roLAp…` | 6,593,517 | 1.51% | 0% |

## Signals (anomaly detection)

- **[WARNING]** Solana TVL surge (z=+2.4 vs its recent baseline)

## Solana Pulse — sentiment (experimental)

**66/100 — Bullish** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 78.7 |
| fear greed | 74 |
| momentum | 47.9 |
| news | 66 |

Crypto Fear & Greed: 74 (Greed) · CoinGecko votes bullish: 78.72% · headline tone (48h): +2

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 140 |
| Raydium AMM v4 | 110 |
| Orca Whirlpool | 128 |
| Pump.fun | 140 |
| Tensor | 0 |
| Magic Eden v2 | 66 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,188,448 |
| Binance (cold) | 1,974,083 |
| OKX (attributed) | 274,768 |
| Coinbase (hot) | 25,723 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 314ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 99.3% of stake.
- **Agave**: latest release v4.2.2 · running 4.2.2 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

### Latest ecosystem news (solana.com)

- [Payment Channels: 1 Million Payments Per Second](https://solana.com/news/payment-channels-1-million-payments-per-second) — Thu, 03 Sep 2026
- [How to Reclaim Excess SOL After Rent Reduction](https://solana.com/news/how-to-reclaim-excess-sol-after-rent-reduction) — Thu, 03 Sep 2026
- [The Token Supercycle: Everything of Value is Becoming Programmable](https://solana.com/news/the-token-supercycle-oped) — Wed, 02 Sep 2026
- [Webinar Recap: Cross-Border Payments in Latin America](https://solana.com/news/webinar-recap-cross-border-payments-in-latin-america) — Tue, 01 Sep 2026
- [Solana Changelog: August 27, 2026](https://solana.com/news/solana-changelog-august-27-2026) — Fri, 28 Aug 2026
- [The Token Supercycle Is Here: Solana Brings Breakpoint 2026 to London](https://solana.com/news/breakpoint-2026-london-speakers) — Thu, 27 Aug 2026

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 8684 ms |
| solana_rpc_validators | OK | 357 ms |
| coingecko | OK | 1987 ms |
| defillama_tvl | OK | 183 ms |
| defillama_dex | OK | 1008 ms |
| defillama_fees | OK | 521 ms |
| defillama_stablecoins | OK | 230 ms |
| defillama_xstocks | OK | 214 ms |
| jito_kobe | OK | 264 ms |
| stakewiz | OK | 1363 ms |
| github | OK | 929 ms |
| solana_com_news | OK | 146 ms |
| sentiment | OK | 2293 ms |
| solana_status_page | OK | 474 ms |
| solana_rpc_whales | OK | 1211 ms |
| solana_rpc_programs | OK | 2092 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*