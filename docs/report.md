# Solbeat — State of the Solana Network

> Generated 2026-09-05T00:24:46Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1028 is 66% complete (~13h remaining), with the cluster processing ~3,307 TPS (1,171 non-vote). Measured slot time is 315ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $698.1K of Real Economic Value over the last 24h ($485/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $101.81 (-2.0% / 24h). Decentralization: Nakamoto coefficient 18, 677 active validators, 0.0% of stake delinquent. Alpenglow readiness: validators holding 99% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 1 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 444,381,367 |
| Block height | 422,426,548 |
| Epoch | 1028 (66.06% complete, ~12.8h left) |
| TPS (10 min avg) | 3,307 |
| Non-vote TPS | 1,171 |
| Slot time (measured) | 315.2 ms |
| Est. daily transactions | 300,838,077 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0051 |
| Node version | 4.2.2 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $101.81 (-2.0%/24h) |
| Market cap | $59.6B |
| **REV (24h)** | **$698.1K** (fees $594.5K + Jito tips $103.5K) |
| Chain TVL | $5.8B |
| Stablecoin supply | $16.6B |
| DEX volume (24h) | $2.4B (-3.1%/1d) |
| Tokenized equities (xStocks TVL) | $448.1M |
| Circulating supply | 585,359,911 SOL |
| Inflation | 3.66% |

Top DEXs by 24h volume: PumpSwap ($838.7M), Orca DEX ($250.3M), BisonFi ($232.5M), Meteora DLMM ($186.5M), Manifest Trade ($161.5M)

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

- **[WARNING]** Solana TVL surge (z=+2.5 vs its recent baseline)

## Solana Pulse — sentiment (experimental)

**66/100 — Bullish** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 80.5 |
| fear greed | 73 |
| momentum | 41.9 |
| news | 74 |

Crypto Fear & Greed: 73 (Greed) · CoinGecko votes bullish: 80.49% · headline tone (48h): +3

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 96 |
| Raydium AMM v4 | 90 |
| Orca Whirlpool | 80 |
| Pump.fun | 118 |
| Tensor | 0 |
| Magic Eden v2 | 69 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,188,448 |
| Binance (cold) | 1,794,417 |
| OKX (attributed) | 265,638 |
| Coinbase (hot) | 19,759 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 315ms · proposal merged.
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
| solana_rpc | OK | 7907 ms |
| solana_rpc_validators | OK | 190 ms |
| coingecko | OK | 1605 ms |
| defillama_tvl | OK | 74 ms |
| defillama_dex | OK | 2914 ms |
| defillama_fees | OK | 1890 ms |
| defillama_stablecoins | OK | 70 ms |
| defillama_xstocks | OK | 4254 ms |
| jito_kobe | OK | 337 ms |
| stakewiz | OK | 940 ms |
| github | OK | 669 ms |
| solana_com_news | OK | 81 ms |
| sentiment | OK | 2121 ms |
| solana_status_page | OK | 1026 ms |
| solana_rpc_whales | OK | 888 ms |
| solana_rpc_programs | OK | 1615 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*