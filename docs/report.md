# Solbeat — State of the Solana Network

> Generated 2026-09-19T22:32:30Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1038 is 29% complete (~23h remaining), with the cluster processing ~4,927 TPS (2,408 non-vote). Measured slot time is 267ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $1.1M of Real Economic Value over the last 24h ($779/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $110.15 (-2.7% / 24h). Decentralization: Nakamoto coefficient 18, 678 active validators, 0.0% of stake delinquent. Alpenglow readiness: validators holding 99% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 2 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 448,543,342 |
| Block height | 426,584,092 |
| Epoch | 1038 (29.48% complete, ~22.6h left) |
| TPS (10 min avg) | 4,927 |
| Non-vote TPS | 2,408 |
| Slot time (measured) | 267.1 ms |
| Est. daily transactions | 403,369,684 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0052 |
| Node version | 4.3.0-rc.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $110.15 (-2.7%/24h) |
| Market cap | $64.7B |
| **REV (24h)** | **$1.1M** (fees $966.0K + Jito tips $156.4K) |
| Chain TVL | $6.2B |
| Stablecoin supply | $15.8B |
| DEX volume (24h) | $3.5B (36.4%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 587,367,568 SOL |
| Inflation | 3.64% |

Top DEXs by 24h volume: BisonFi ($532.7M), PumpSwap ($488.3M), HumidiFi ($334.9M), Raydium AMM ($325.2M), Orca DEX ($300.7M)

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

- **[WARNING]** Solana TVL surge (z=+2.3 vs its recent baseline)
- **[WARNING]** DEX volume surge (z=+2.1 vs its recent baseline)

## Solana Pulse — sentiment (experimental)

**76/100 — Bullish** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 77.4 |
| fear greed | 71 |
| momentum | 78.7 |
| news | 74 |

Crypto Fear & Greed: 71 (Greed) · CoinGecko votes bullish: 77.42% · headline tone (48h): +3

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 180 |
| Raydium AMM v4 | 180 |
| Orca Whirlpool | 205 |
| Pump.fun | 205 |
| Tensor | 0 |
| Magic Eden v2 | 92 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,943,926 |
| Binance (cold) | 1,311,941 |
| OKX (attributed) | 243,904 |
| Coinbase (hot) | 24,955 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 267ms · proposal merged.
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
| solana_rpc | OK | 9404 ms |
| solana_rpc_validators | OK | 363 ms |
| coingecko | OK | 1720 ms |
| defillama_tvl | OK | 1134 ms |
| defillama_dex | OK | 1208 ms |
| defillama_fees | OK | 2011 ms |
| defillama_stablecoins | OK | 177 ms |
| defillama_xstocks | OK | 772 ms |
| jito_kobe | OK | 358 ms |
| stakewiz | OK | 1453 ms |
| github | OK | 679 ms |
| solana_com_news | OK | 91 ms |
| sentiment | OK | 2298 ms |
| solana_status_page | OK | 337 ms |
| solana_rpc_whales | OK | 2387 ms |
| solana_rpc_programs | OK | 3330 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*