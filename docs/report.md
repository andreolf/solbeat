# Solbeat — State of the Solana Network

> Generated 2026-09-03T12:46:41Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1027 is 72% complete (~11h remaining), with the cluster processing ~3,528 TPS (1,408 non-vote). Measured slot time is 314ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $778.5K of Real Economic Value over the last 24h ($541/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $100.96 (+3.2% / 24h). Decentralization: Nakamoto coefficient 18, 675 active validators, 0.1% of stake delinquent. Alpenglow readiness: validators holding 99% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 1 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 443,974,689 |
| Block height | 422,021,790 |
| Epoch | 1027 (71.92% complete, ~10.6h left) |
| TPS (10 min avg) | 3,528 |
| Non-vote TPS | 1,408 |
| Slot time (measured) | 313.9 ms |
| Est. daily transactions | 301,494,153 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0054 |
| Node version | 4.2.2 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $100.96 (+3.2%/24h) |
| Market cap | $59.1B |
| **REV (24h)** | **$778.5K** (fees $612.6K + Jito tips $165.9K) |
| Chain TVL | $5.8B |
| Stablecoin supply | $16.0B |
| DEX volume (24h) | $2.3B (5.4%/1d) |
| Tokenized equities (xStocks TVL) | $436.0M |
| Circulating supply | 585,274,855 SOL |
| Inflation | 3.67% |

Top DEXs by 24h volume: PumpSwap ($1.0B), Orca DEX ($218.3M), BisonFi ($194.4M), Manifest Trade ($175.5M), Meteora DLMM ($137.8M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 675 / 20 |
| Delinquent stake | 0.06% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.2% |
| Avg / median commission | 12.5% / 5% |
| Alpenglow BLS-key readiness | 689 validators, 99.4% of stake |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L43ZWjwCHART3o…` | 17,348,904 | 3.96% | 7% |
| 2 | `he1iusunGwqrNtafDtLd…` | 16,325,737 | 3.72% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5…` | 12,462,274 | 2.84% | 0% |
| 4 | `CatzoSMUkTRidT5DwBxA…` | 11,304,498 | 2.58% | 5% |
| 5 | `8GbwASqdpw4dVcwbWUxb…` | 9,565,273 | 2.18% | 0% |
| 6 | `26pV97Ce83ZQ6Kz9XT4t…` | 9,285,486 | 2.12% | 7% |
| 7 | `51JBzSTU5rAM8gLAVQKg…` | 9,040,435 | 2.06% | 10% |
| 8 | `9QU2QSxhb24FUX3Tu2Fp…` | 7,220,140 | 1.65% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJn…` | 7,125,475 | 1.63% | 5% |
| 10 | `DumiCKHVqoCQKD8roLAp…` | 6,590,653 | 1.5% | 0% |

## Signals (anomaly detection)

- **[WARNING]** Solana TVL surge (z=+2.4 vs its recent baseline)

## Solana Pulse — sentiment (experimental)

**61/100 — Bullish** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 75.0 |
| fear greed | 65 |
| momentum | 45.0 |

Crypto Fear & Greed: 65 (Greed) · CoinGecko votes bullish: 75.0% · headline tone (48h): +0

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 129 |
| Raydium AMM v4 | 129 |
| Orca Whirlpool | 155 |
| Pump.fun | 173 |
| Tensor | 0 |
| Magic Eden v2 | 58 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,188,448 |
| Binance (cold) | 1,963,768 |
| OKX (attributed) | 315,396 |
| Coinbase (hot) | 75,139 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 314ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 99.4% of stake.
- **Agave**: latest release v4.2.2 · running 4.2.2 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

### Latest ecosystem news (solana.com)

- [The Token Supercycle: Everything of Value is Becoming Programmable](https://solana.com/news/the-token-supercycle-oped) — Wed, 02 Sep 2026
- [Solana Changelog: August 27, 2026](https://solana.com/news/solana-changelog-august-27-2026) — Fri, 28 Aug 2026
- [The Token Supercycle Is Here: Solana Brings Breakpoint 2026 to London](https://solana.com/news/breakpoint-2026-london-speakers) — Thu, 27 Aug 2026
- [Solana Changelog: August 20, 2026](https://solana.com/news/solana-changelog-august-20-2026) — Mon, 24 Aug 2026
- [Lowering Slot Time and Validator Economics](https://solana.com/news/lowering-slot-time-and-validators-economic) — Wed, 19 Aug 2026
- [v1 Transactions and the ALT Trade-off](https://solana.com/news/transaction-v1-and-the-alt-trade-off) — Mon, 17 Aug 2026

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 11097 ms |
| solana_rpc_validators | OK | 1277 ms |
| coingecko | OK | 1823 ms |
| defillama_tvl | OK | 231 ms |
| defillama_dex | OK | 59 ms |
| defillama_fees | OK | 114 ms |
| defillama_stablecoins | OK | 95 ms |
| defillama_xstocks | OK | 115 ms |
| jito_kobe | OK | 368 ms |
| stakewiz | OK | 1492 ms |
| github | OK | 738 ms |
| solana_com_news | OK | 82 ms |
| sentiment | OK | 2162 ms |
| solana_status_page | OK | 535 ms |
| solana_rpc_whales | OK | 2424 ms |
| solana_rpc_programs | OK | 4267 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*