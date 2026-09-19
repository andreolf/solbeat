# Solbeat — State of the Solana Network

> Generated 2026-09-19T18:56:46Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1038 is 18% complete (~26h remaining), with the cluster processing ~4,747 TPS (2,223 non-vote). Measured slot time is 266ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $1.1M of Real Economic Value over the last 24h ($780/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $110.95 (-1.2% / 24h). Decentralization: Nakamoto coefficient 18, 677 active validators, 0.0% of stake delinquent. Alpenglow readiness: validators holding 99% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 2 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 448,494,898 |
| Block height | 426,535,674 |
| Epoch | 1038 (18.26% complete, ~26.1h left) |
| TPS (10 min avg) | 4,747 |
| Non-vote TPS | 2,223 |
| Slot time (measured) | 266.4 ms |
| Est. daily transactions | 403,330,905 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0052 |
| Node version | 4.3.0-rc.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $110.95 (-1.2%/24h) |
| Market cap | $65.2B |
| **REV (24h)** | **$1.1M** (fees $966.0K + Jito tips $157.9K) |
| Chain TVL | $6.2B |
| Stablecoin supply | $15.8B |
| DEX volume (24h) | $3.5B (36.4%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 587,367,740 SOL |
| Inflation | 3.64% |

Top DEXs by 24h volume: BisonFi ($532.7M), PumpSwap ($488.3M), HumidiFi ($334.9M), Raydium AMM ($330.6M), Orca DEX ($300.7M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 677 / 13 |
| Delinquent stake | 0.04% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.3% |
| Avg / median commission | 12.2% / 5% |
| Alpenglow BLS-key readiness | 699 validators, 99.4% of stake |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L43ZWjwCHART3o…` | 17,849,776 | 4.05% | 7% |
| 2 | `he1iusunGwqrNtafDtLd…` | 15,819,247 | 3.59% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5…` | 12,500,805 | 2.84% | 0% |
| 4 | `CatzoSMUkTRidT5DwBxA…` | 11,362,749 | 2.58% | 5% |
| 5 | `8GbwASqdpw4dVcwbWUxb…` | 9,786,807 | 2.22% | 0% |
| 6 | `26pV97Ce83ZQ6Kz9XT4t…` | 9,252,843 | 2.1% | 7% |
| 7 | `51JBzSTU5rAM8gLAVQKg…` | 9,116,740 | 2.07% | 10% |
| 8 | `9QU2QSxhb24FUX3Tu2Fp…` | 7,434,776 | 1.69% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJn…` | 7,086,871 | 1.61% | 5% |
| 10 | `HZKopZYvv8v6un2H6KUN…` | 6,627,951 | 1.51% | 100% |

## Signals (anomaly detection)

- **[WARNING]** Solana TVL surge (z=+2.4 vs its recent baseline)
- **[WARNING]** DEX volume surge (z=+2.1 vs its recent baseline)

## Solana Pulse — sentiment (experimental)

**80/100 — Bullish** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| momentum | 79.9 |
## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 152 |
| Raydium AMM v4 | 138 |
| Orca Whirlpool | 152 |
| Pump.fun | 152 |
| Tensor | 0 |
| Magic Eden v2 | 76 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,943,926 |
| Binance (cold) | 1,302,379 |
| OKX (attributed) | 243,904 |
| Coinbase (hot) | 26,113 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 266ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 99.4% of stake.
- **Agave**: latest release v4.2.2 · running 4.3.0-rc.0 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

### Latest ecosystem news (solana.com)

- [Solana Changelog: September 18, 2026](https://solana.com/news/solana-changelog-september-18-2026) — Sat, 19 Sep 2026
- [Project Harmonia Brings Institutional Tokenized Funds to Solana](https://solana.com/news/project-harmonia-brings-institutional-tokenized-funds-to-solana) — Wed, 16 Sep 2026
- [Solana: Building, Proving and Earning Trust in Public](https://solana.com/news/solana-building-trust-in-public) — Mon, 14 Sep 2026
- [Solana Changelog: September 10, 2026](https://solana.com/news/solana-changelog-september-10-2026) — Thu, 10 Sep 2026
- [Solana Changelog: September 3, 2026](https://solana.com/news/solana-changelog-september-3-2026) — Thu, 10 Sep 2026
- [Report: Stablecoins Are Reshaping Remittances](https://solana.com/news/report-stablecoins-are-reshaping-remittances) — Tue, 08 Sep 2026

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 7773 ms |
| solana_rpc_validators | OK | 104 ms |
| coingecko | OK | 1672 ms |
| defillama_tvl | OK | 247 ms |
| defillama_dex | OK | 771 ms |
| defillama_fees | OK | 111 ms |
| defillama_stablecoins | OK | 292 ms |
| defillama_xstocks | OK | 36 ms |
| jito_kobe | OK | 302 ms |
| stakewiz | OK | 529 ms |
| github | OK | 604 ms |
| solana_com_news | OK | 76 ms |
| sentiment | FAILED | 10998 ms |
| solana_status_page | OK | 311 ms |
| solana_rpc_whales | OK | 804 ms |
| solana_rpc_programs | OK | 1438 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*