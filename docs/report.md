# Solbeat — State of the Solana Network

> Generated 2026-09-03T03:09:22Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1027 is 46% complete (~20h remaining), with the cluster processing ~3,645 TPS (1,499 non-vote). Measured slot time is 314ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $1.1M of Real Economic Value over the last 24h ($740/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $100.86 (+0.9% / 24h). Decentralization: Nakamoto coefficient 18, 677 active validators, 0.1% of stake delinquent. Alpenglow readiness: validators holding 99% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 1 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 443,864,584 |
| Block height | 421,911,829 |
| Epoch | 1027 (46.43% complete, ~20.2h left) |
| TPS (10 min avg) | 3,645 |
| Non-vote TPS | 1,499 |
| Slot time (measured) | 314.5 ms |
| Est. daily transactions | 319,234,408 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0067 |
| Node version | 4.2.1 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $100.86 (+0.9%/24h) |
| Market cap | $59.0B |
| **REV (24h)** | **$1.1M** (fees $899.8K + Jito tips $165.4K) |
| Chain TVL | $5.7B |
| Stablecoin supply | $16.0B |
| DEX volume (24h) | $2.3B (7.2%/1d) |
| Tokenized equities (xStocks TVL) | $434.4M |
| Circulating supply | 585,275,175 SOL |
| Inflation | 3.67% |

Top DEXs by 24h volume: PumpSwap ($1.0B), Orca DEX ($202.6M), BisonFi ($194.4M), Manifest Trade ($169.9M), Meteora DLMM ($137.8M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 677 / 18 |
| Delinquent stake | 0.05% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.2% |
| Avg / median commission | 12.3% / 5% |
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

- **[WARNING]** Solana TVL surge (z=+2.2 vs its recent baseline)

## Solana Pulse — sentiment (experimental)

**65/100 — Bullish** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 80.0 |
| fear greed | 65 |
| momentum | 44.7 |
| news | 74 |

Crypto Fear & Greed: 65 (Greed) · CoinGecko votes bullish: 80.0% · headline tone (48h): +3

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 137 |
| Raydium AMM v4 | 126 |
| Orca Whirlpool | 137 |
| Pump.fun | 137 |
| Tensor | 0 |
| Magic Eden v2 | 63 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,188,448 |
| Binance (cold) | 1,904,568 |
| OKX (attributed) | 173,179 |
| Coinbase (hot) | 25,203 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 314ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 99.4% of stake.
- **Agave**: latest release v4.2.2 · running 4.2.1 on the polled node.
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
| solana_rpc | OK | 9136 ms |
| solana_rpc_validators | OK | 387 ms |
| coingecko | OK | 1733 ms |
| defillama_tvl | OK | 149 ms |
| defillama_dex | OK | 971 ms |
| defillama_fees | OK | 1549 ms |
| defillama_stablecoins | OK | 211 ms |
| defillama_xstocks | OK | 177 ms |
| jito_kobe | OK | 2324 ms |
| stakewiz | OK | 1058 ms |
| github | OK | 762 ms |
| solana_com_news | OK | 116 ms |
| sentiment | OK | 2282 ms |
| solana_status_page | OK | 415 ms |
| solana_rpc_whales | OK | 1236 ms |
| solana_rpc_programs | OK | 2148 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*