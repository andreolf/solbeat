# Solbeat — State of the Solana Network

> Generated 2026-09-21T14:39:15Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1039 is 55% complete (~14h remaining), with the cluster processing ~5,302 TPS (2,789 non-vote). Measured slot time is 268ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $953.5K of Real Economic Value over the last 24h ($662/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $118.64 (+9.6% / 24h). Decentralization: Nakamoto coefficient 18, 677 active validators, 0.0% of stake delinquent. Alpenglow readiness: validators holding 99% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 3 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 449,084,696 |
| Block height | 427,125,307 |
| Epoch | 1039 (54.79% complete, ~14.5h left) |
| TPS (10 min avg) | 5,302 |
| Non-vote TPS | 2,789 |
| Slot time (measured) | 268.1 ms |
| Est. daily transactions | 393,015,808 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0045 |
| Node version | 4.3.0-rc.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $118.64 (+9.6%/24h) |
| Market cap | $69.7B |
| **REV (24h)** | **$953.5K** (fees $787.0K + Jito tips $166.5K) |
| Chain TVL | $6.5B |
| Stablecoin supply | $15.8B |
| DEX volume (24h) | $2.8B (-2.8%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 587,437,292 SOL |
| Inflation | 3.64% |

Top DEXs by 24h volume: PumpSwap ($482.8M), BisonFi ($424.3M), Raydium AMM ($353.3M), Orca DEX ($301.6M), HumidiFi ($253.1M)

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

- **[WARNING]** SOL price surge (z=+2.1 vs its recent baseline)
- **[WARNING]** Solana TVL surge (z=+2.6 vs its recent baseline)
- **[WARNING · market_move]** Market-wide move: SOL price anomaly accompanied by liquidity/volume shifts — an ecosystem-level repricing rather than an isolated metric.

## Solana Pulse — sentiment (experimental)

**77/100 — Bullish** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 82.8 |
| fear greed | 70 |
| momentum | 74.2 |
| news | 82 |

Crypto Fear & Greed: 70 (Greed) · CoinGecko votes bullish: 82.76% · headline tone (48h): +4

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 159 |
| Raydium AMM v4 | 159 |
| Orca Whirlpool | 159 |
| Pump.fun | 159 |
| Tensor | 0 |
| Magic Eden v2 | 42 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,943,926 |
| Binance (cold) | 1,430,474 |
| OKX (attributed) | 258,246 |
| Coinbase (hot) | 66,907 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 268ms · proposal merged.
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
| solana_rpc | OK | 8094 ms |
| solana_rpc_validators | OK | 77 ms |
| coingecko | OK | 1619 ms |
| defillama_tvl | OK | 64 ms |
| defillama_dex | OK | 795 ms |
| defillama_fees | OK | 745 ms |
| defillama_stablecoins | OK | 169 ms |
| defillama_xstocks | OK | 79 ms |
| jito_kobe | OK | 182 ms |
| stakewiz | OK | 1151 ms |
| github | OK | 648 ms |
| solana_com_news | OK | 144 ms |
| sentiment | OK | 2113 ms |
| solana_status_page | OK | 350 ms |
| solana_rpc_whales | OK | 750 ms |
| solana_rpc_programs | OK | 1366 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*