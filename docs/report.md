# Solbeat — State of the Solana Network

> Generated 2026-09-04T11:26:41Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1028 is 32% complete (~26h remaining), with the cluster processing ~3,327 TPS (1,181 non-vote). Measured slot time is 314ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $700.9K of Real Economic Value over the last 24h ($487/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $104.17 (+3.5% / 24h). Decentralization: Nakamoto coefficient 18, 676 active validators, 0.0% of stake delinquent. Alpenglow readiness: validators holding 99% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 3 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 444,233,437 |
| Block height | 422,279,416 |
| Epoch | 1028 (31.81% complete, ~25.7h left) |
| TPS (10 min avg) | 3,327 |
| Non-vote TPS | 1,181 |
| Slot time (measured) | 313.8 ms |
| Est. daily transactions | 287,956,883 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0057 |
| Node version | 4.2.2 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $104.17 (+3.5%/24h) |
| Market cap | $61.0B |
| **REV (24h)** | **$700.9K** (fees $594.5K + Jito tips $106.4K) |
| Chain TVL | $5.9B |
| Stablecoin supply | $16.6B |
| DEX volume (24h) | $2.5B (7.4%/1d) |
| Tokenized equities (xStocks TVL) | $458.8M |
| Circulating supply | 585,360,374 SOL |
| Inflation | 3.66% |

Top DEXs by 24h volume: PumpSwap ($838.7M), Orca DEX ($282.4M), BisonFi ($232.5M), Meteora DLMM ($186.5M), Manifest Trade ($177.8M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 676 / 18 |
| Delinquent stake | 0.03% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.4% |
| Avg / median commission | 12.2% / 5.0% |
| Alpenglow BLS-key readiness | 689 validators, 99.3% of stake |

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

- **[WARNING]** SOL price surge (z=+2.0 vs its recent baseline)
- **[WARNING]** Solana TVL surge (z=+2.7 vs its recent baseline)
- **[WARNING · market_move]** Market-wide move: SOL price anomaly accompanied by liquidity/volume shifts — an ecosystem-level repricing rather than an isolated metric.

## Solana Pulse — sentiment (experimental)

**66/100 — Bullish** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 77.8 |
| fear greed | 74 |
| momentum | 52.1 |
| news | 58 |

Crypto Fear & Greed: 74 (Greed) · CoinGecko votes bullish: 77.78% · headline tone (48h): +1

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 106 |
| Raydium AMM v4 | 99 |
| Orca Whirlpool | 134 |
| Pump.fun | 123 |
| Tensor | 0 |
| Magic Eden v2 | 48 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,188,448 |
| Binance (cold) | 1,977,678 |
| OKX (attributed) | 316,836 |
| Coinbase (hot) | 22,859 |

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
| solana_rpc | OK | 9118 ms |
| solana_rpc_validators | OK | 336 ms |
| coingecko | OK | 1766 ms |
| defillama_tvl | OK | 97 ms |
| defillama_dex | OK | 1182 ms |
| defillama_fees | OK | 73 ms |
| defillama_stablecoins | OK | 1163 ms |
| defillama_xstocks | OK | 2780 ms |
| jito_kobe | OK | 211 ms |
| stakewiz | OK | 1577 ms |
| github | OK | 741 ms |
| solana_com_news | OK | 102 ms |
| sentiment | OK | 2333 ms |
| solana_status_page | OK | 319 ms |
| solana_rpc_whales | OK | 1159 ms |
| solana_rpc_programs | OK | 2103 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*