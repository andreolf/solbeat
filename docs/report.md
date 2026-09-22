# Solbeat — State of the Solana Network

> Generated 2026-09-22T03:04:46Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1039 is 93% complete (~2h remaining), with the cluster processing ~4,579 TPS (2,063 non-vote). Measured slot time is 268ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $1.3M of Real Economic Value over the last 24h ($875/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $116.56 (+4.5% / 24h). Decentralization: Nakamoto coefficient 18, 677 active validators, 0.1% of stake delinquent. Alpenglow readiness: validators holding 99% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 4 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 449,251,870 |
| Block height | 427,292,394 |
| Epoch | 1039 (93.49% complete, ~2.1h left) |
| TPS (10 min avg) | 4,579 |
| Non-vote TPS | 2,063 |
| Slot time (measured) | 267.8 ms |
| Est. daily transactions | 398,279,717 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0061 |
| Node version | 4.3.0-rc.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $116.56 (+4.5%/24h) |
| Market cap | $68.5B |
| **REV (24h)** | **$1.3M** (fees $1.1M + Jito tips $163.7K) |
| Chain TVL | $6.5B |
| Stablecoin supply | $17.1B |
| DEX volume (24h) | $3.4B (20.6%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 587,436,725 SOL |
| Inflation | 3.64% |

Top DEXs by 24h volume: Raydium AMM ($576.3M), Orca DEX ($444.7M), BisonFi ($424.3M), PumpSwap ($390.1M), Meteora DLMM ($259.6M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 677 / 14 |
| Delinquent stake | 0.05% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.3% |
| Avg / median commission | 12.7% / 5% |
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

- **[WARNING]** Solana TVL surge (z=+2.6 vs its recent baseline)
- **[WARNING]** Stablecoin supply surge (z=+2.5 vs its recent baseline)
- **[WARNING]** Real Economic Value deviating from its run-history baseline (z=+2.4)
- **[WARNING · liquidity_rotation]** Stablecoin supply and TVL moving together — capital rotating in or out of the chain.

## Solana Pulse — sentiment (experimental)

**82/100 — Bullish** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 77.9 |
| fear greed | 78 |
| momentum | 84.8 |
| news | 90 |

Crypto Fear & Greed: 78 (Extreme Greed) · CoinGecko votes bullish: 77.91% · headline tone (48h): +5

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 151 |
| Raydium AMM v4 | 151 |
| Orca Whirlpool | 151 |
| Pump.fun | 151 |
| Tensor | 1 |
| Magic Eden v2 | 60 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,943,926 |
| Binance (cold) | 1,304,197 |
| OKX (attributed) | 258,247 |
| Coinbase (hot) | 35,201 |

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
| solana_rpc | OK | 7055 ms |
| solana_rpc_validators | OK | 288 ms |
| coingecko | OK | 1812 ms |
| defillama_tvl | OK | 303 ms |
| defillama_dex | OK | 1133 ms |
| defillama_fees | OK | 1095 ms |
| defillama_stablecoins | OK | 1271 ms |
| defillama_xstocks | OK | 63 ms |
| jito_kobe | OK | 263 ms |
| stakewiz | OK | 1140 ms |
| github | OK | 948 ms |
| solana_com_news | OK | 128 ms |
| sentiment | OK | 2467 ms |
| solana_status_page | OK | 435 ms |
| solana_rpc_whales | OK | 908 ms |
| solana_rpc_programs | OK | 1646 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*