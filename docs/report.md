# Solbeat — State of the Solana Network

> Generated 2026-09-21T13:38:33Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1039 is 52% complete (~16h remaining), with the cluster processing ~5,525 TPS (3,025 non-vote). Measured slot time is 270ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $950.7K of Real Economic Value over the last 24h ($660/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $117.36 (+8.7% / 24h). Decentralization: Nakamoto coefficient 18, 677 active validators, 0.0% of stake delinquent. Alpenglow readiness: validators holding 99% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 4 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 449,071,130 |
| Block height | 427,111,754 |
| Epoch | 1039 (51.65% complete, ~15.6h left) |
| TPS (10 min avg) | 5,525 |
| Non-vote TPS | 3,025 |
| Slot time (measured) | 269.6 ms |
| Est. daily transactions | 374,562,396 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0050 |
| Node version | 4.3.0-rc.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $117.36 (+8.7%/24h) |
| Market cap | $69.0B |
| **REV (24h)** | **$950.7K** (fees $787.0K + Jito tips $163.7K) |
| Chain TVL | $6.4B |
| Stablecoin supply | $15.8B |
| DEX volume (24h) | $2.8B (-2.8%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 587,437,342 SOL |
| Inflation | 3.64% |

Top DEXs by 24h volume: PumpSwap ($482.8M), BisonFi ($424.3M), Raydium AMM ($340.4M), Orca DEX ($301.6M), HumidiFi ($253.1M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 677 / 13 |
| Delinquent stake | 0.04% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.3% |
| Avg / median commission | 12.5% / 5% |
| Alpenglow BLS-key readiness | 699 validators, 99.4% of stake |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L43ZWjwCHART3o…` | 17,856,583 | 4.06% | 7% |
| 2 | `he1iusunGwqrNtafDtLd…` | 15,828,384 | 3.6% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5…` | 12,518,302 | 2.85% | 0% |
| 4 | `CatzoSMUkTRidT5DwBxA…` | 11,252,588 | 2.56% | 5% |
| 5 | `8GbwASqdpw4dVcwbWUxb…` | 9,788,818 | 2.23% | 0% |
| 6 | `26pV97Ce83ZQ6Kz9XT4t…` | 9,251,354 | 2.1% | 7% |
| 7 | `51JBzSTU5rAM8gLAVQKg…` | 9,106,985 | 2.07% | 10% |
| 8 | `9QU2QSxhb24FUX3Tu2Fp…` | 7,443,840 | 1.69% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJn…` | 7,088,079 | 1.61% | 5% |
| 10 | `DumiCKHVqoCQKD8roLAp…` | 6,572,007 | 1.49% | 0% |

## Signals (anomaly detection)

- **[SERIOUS]** TPS spike: 5,525 vs 12h mean 4,293 (z=+3.8)
- **[WARNING]** SOL price surge (z=+2.0 vs its recent baseline)
- **[WARNING]** Solana TVL surge (z=+2.5 vs its recent baseline)
- **[WARNING · market_move]** Market-wide move: SOL price anomaly accompanied by liquidity/volume shifts — an ecosystem-level repricing rather than an isolated metric.

## Solana Pulse — sentiment (experimental)

**74/100 — Bullish** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 81.5 |
| fear greed | 70 |
| momentum | 73.3 |
| news | 66 |

Crypto Fear & Greed: 70 (Greed) · CoinGecko votes bullish: 81.48% · headline tone (48h): +2

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 164 |
| Raydium AMM v4 | 148 |
| Orca Whirlpool | 164 |
| Pump.fun | 164 |
| Tensor | 0 |
| Magic Eden v2 | 44 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,943,926 |
| Binance (cold) | 1,424,551 |
| OKX (attributed) | 258,246 |
| Coinbase (hot) | 68,171 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 270ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 99.4% of stake.
- **Agave**: latest release v4.3.0 · running 4.3.0-rc.0 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

### Latest ecosystem news (solana.com)

- [Solana Changelog: September 18, 2026](https://solana.com/news/solana-changelog-september-18-2026) — Sat, 19 Sep 2026
- [How AI Is Reshaping Crypto Security, with Michael Coates](https://solana.com/news/bits-to-bricks-crypto-security-michael-coates) — Sat, 19 Sep 2026
- [Project Harmonia Brings Institutional Tokenized Funds to Solana](https://solana.com/news/project-harmonia-brings-institutional-tokenized-funds-to-solana) — Wed, 16 Sep 2026
- [Solana: Building, Proving and Earning Trust in Public](https://solana.com/news/solana-building-trust-in-public) — Mon, 14 Sep 2026
- [Solana Changelog: September 10, 2026](https://solana.com/news/solana-changelog-september-10-2026) — Thu, 10 Sep 2026
- [Solana Changelog: September 3, 2026](https://solana.com/news/solana-changelog-september-3-2026) — Thu, 10 Sep 2026

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 8195 ms |
| solana_rpc_validators | OK | 92 ms |
| coingecko | OK | 1625 ms |
| defillama_tvl | OK | 40 ms |
| defillama_dex | OK | 788 ms |
| defillama_fees | OK | 719 ms |
| defillama_stablecoins | OK | 71 ms |
| defillama_xstocks | OK | 40 ms |
| jito_kobe | OK | 348 ms |
| stakewiz | OK | 970 ms |
| github | OK | 569 ms |
| solana_com_news | OK | 52 ms |
| sentiment | OK | 2102 ms |
| solana_status_page | OK | 420 ms |
| solana_rpc_whales | OK | 749 ms |
| solana_rpc_programs | OK | 1461 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*