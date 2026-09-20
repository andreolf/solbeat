# Solbeat — State of the Solana Network

> Generated 2026-09-20T00:57:51Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1038 is 37% complete (~20h remaining), with the cluster processing ~4,272 TPS (1,757 non-vote). Measured slot time is 268ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $1.1M of Real Economic Value over the last 24h ($780/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $110.88 (-2.3% / 24h). Decentralization: Nakamoto coefficient 18, 678 active validators, 0.0% of stake delinquent. Alpenglow readiness: validators holding 99% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 1 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 448,575,983 |
| Block height | 426,616,723 |
| Epoch | 1038 (37.03% complete, ~20.3h left) |
| TPS (10 min avg) | 4,272 |
| Non-vote TPS | 1,757 |
| Slot time (measured) | 268.5 ms |
| Est. daily transactions | 401,811,180 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0053 |
| Node version | 4.3.0-rc.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $110.88 (-2.3%/24h) |
| Market cap | $65.1B |
| **REV (24h)** | **$1.1M** (fees $966.0K + Jito tips $156.6K) |
| Chain TVL | $6.2B |
| Stablecoin supply | $15.8B |
| DEX volume (24h) | $3.2B (-8.6%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 587,367,270 SOL |
| Inflation | 3.64% |

Top DEXs by 24h volume: PumpSwap ($606.4M), BisonFi ($532.7M), HumidiFi ($334.9M), Raydium AMM ($317.3M), Orca DEX ($206.3M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 678 / 12 |
| Delinquent stake | 0.04% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.3% |
| Avg / median commission | 12.2% / 5.0% |
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

- **[WARNING]** Solana TVL surge (z=+2.1 vs its recent baseline)

## Solana Pulse — sentiment (experimental)

**74/100 — Bullish** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 77.2 |
| fear greed | 71 |
| momentum | 62.0 |
| news | 95 |

Crypto Fear & Greed: 71 (Greed) · CoinGecko votes bullish: 77.19% · headline tone (48h): +6

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 149 |
| Raydium AMM v4 | 149 |
| Orca Whirlpool | 165 |
| Pump.fun | 165 |
| Tensor | 0 |
| Magic Eden v2 | 75 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,943,926 |
| Binance (cold) | 1,334,584 |
| OKX (attributed) | 243,904 |
| Coinbase (hot) | 24,050 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 268ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 99.4% of stake.
- **Agave**: latest release v4.2.2 · running 4.3.0-rc.0 on the polled node.
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
| solana_rpc | OK | 7037 ms |
| solana_rpc_validators | OK | 131 ms |
| coingecko | OK | 1791 ms |
| defillama_tvl | OK | 94 ms |
| defillama_dex | OK | 1220 ms |
| defillama_fees | OK | 1991 ms |
| defillama_stablecoins | OK | 140 ms |
| defillama_xstocks | OK | 278 ms |
| jito_kobe | OK | 222 ms |
| stakewiz | OK | 1453 ms |
| github | OK | 959 ms |
| solana_com_news | OK | 117 ms |
| sentiment | OK | 2427 ms |
| solana_status_page | OK | 392 ms |
| solana_rpc_whales | OK | 825 ms |
| solana_rpc_programs | OK | 1476 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*