# Solbeat — State of the Solana Network

> Generated 2026-09-21T17:59:24Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1039 is 65% complete (~11h remaining), with the cluster processing ~4,960 TPS (2,429 non-vote). Measured slot time is 266ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $952.3K of Real Economic Value over the last 24h ($661/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $116.91 (+6.5% / 24h). Decentralization: Nakamoto coefficient 18, 676 active validators, 0.1% of stake delinquent. Alpenglow readiness: validators holding 99% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 1 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 449,129,415 |
| Block height | 427,170,026 |
| Epoch | 1039 (65.14% complete, ~11.1h left) |
| TPS (10 min avg) | 4,960 |
| Non-vote TPS | 2,429 |
| Slot time (measured) | 266.0 ms |
| Est. daily transactions | 448,392,918 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0034 |
| Node version | 4.3.0-rc.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $116.91 (+6.5%/24h) |
| Market cap | $68.6B |
| **REV (24h)** | **$952.3K** (fees $787.0K + Jito tips $165.3K) |
| Chain TVL | $6.5B |
| Stablecoin supply | $15.8B |
| DEX volume (24h) | $2.8B (-2.8%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 587,437,129 SOL |
| Inflation | 3.64% |

Top DEXs by 24h volume: PumpSwap ($482.8M), Raydium AMM ($427.4M), BisonFi ($424.3M), Orca DEX ($301.6M), HumidiFi ($253.1M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 676 / 14 |
| Delinquent stake | 0.05% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.3% |
| Avg / median commission | 12.5% / 5.0% |
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

- **[WARNING]** Solana TVL surge (z=+2.7 vs its recent baseline)

## Solana Pulse — sentiment (experimental)

**75/100 — Bullish** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 80.6 |
| fear greed | 70 |
| momentum | 73.8 |
| news | 74 |

Crypto Fear & Greed: 70 (Greed) · CoinGecko votes bullish: 80.6% · headline tone (48h): +3

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 150 |
| Raydium AMM v4 | 150 |
| Orca Whirlpool | 167 |
| Pump.fun | 167 |
| Tensor | 0 |
| Magic Eden v2 | 75 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,943,926 |
| Binance (cold) | 1,313,693 |
| OKX (attributed) | 258,247 |
| Coinbase (hot) | 51,642 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 266ms · proposal merged.
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
| solana_rpc | OK | 7759 ms |
| solana_rpc_validators | OK | 340 ms |
| coingecko | OK | 1725 ms |
| defillama_tvl | OK | 105 ms |
| defillama_dex | OK | 1152 ms |
| defillama_fees | OK | 2058 ms |
| defillama_stablecoins | OK | 62 ms |
| defillama_xstocks | OK | 42 ms |
| jito_kobe | OK | 345 ms |
| stakewiz | OK | 1452 ms |
| github | OK | 800 ms |
| solana_com_news | OK | 66 ms |
| sentiment | OK | 2483 ms |
| solana_status_page | OK | 364 ms |
| solana_rpc_whales | OK | 964 ms |
| solana_rpc_programs | OK | 1674 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*