# Solbeat — State of the Solana Network

> Generated 2026-09-20T07:32:20Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1038 is 58% complete (~14h remaining), with the cluster processing ~3,861 TPS (1,312 non-vote). Measured slot time is 265ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $981.9K of Real Economic Value over the last 24h ($682/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $108.70 (-2.9% / 24h). Decentralization: Nakamoto coefficient 18, 678 active validators, 0.0% of stake delinquent. Alpenglow readiness: validators holding 99% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 1 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 448,664,869 |
| Block height | 426,705,592 |
| Epoch | 1038 (57.61% complete, ~13.5h left) |
| TPS (10 min avg) | 3,861 |
| Non-vote TPS | 1,312 |
| Slot time (measured) | 264.9 ms |
| Est. daily transactions | 351,773,443 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0062 |
| Node version | 4.3.0-rc.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $108.70 (-2.9%/24h) |
| Market cap | $63.8B |
| **REV (24h)** | **$981.9K** (fees $826.3K + Jito tips $155.6K) |
| Chain TVL | $6.1B |
| Stablecoin supply | $15.7B |
| DEX volume (24h) | $3.2B (-8.6%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 587,367,016 SOL |
| Inflation | 3.64% |

Top DEXs by 24h volume: PumpSwap ($606.4M), BisonFi ($532.7M), HumidiFi ($334.9M), Raydium AMM ($304.1M), Orca DEX ($213.5M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 678 / 12 |
| Delinquent stake | 0.01% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.3% |
| Avg / median commission | 12.5% / 5.0% |
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

- **[WARNING]** Solana TVL surge (z=+2.0 vs its recent baseline)

## Solana Pulse — sentiment (experimental)

**69/100 — Bullish** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 75.0 |
| fear greed | 71 |
| momentum | 59.2 |
| news | 74 |

Crypto Fear & Greed: 71 (Greed) · CoinGecko votes bullish: 75.0% · headline tone (48h): +3

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 141 |
| Raydium AMM v4 | 141 |
| Orca Whirlpool | 141 |
| Pump.fun | 156 |
| Tensor | 0 |
| Magic Eden v2 | 69 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,943,926 |
| Binance (cold) | 1,298,172 |
| OKX (attributed) | 243,904 |
| Coinbase (hot) | 20,045 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 265ms · proposal merged.
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
| solana_rpc | OK | 6930 ms |
| solana_rpc_validators | OK | 281 ms |
| coingecko | OK | 1783 ms |
| defillama_tvl | OK | 89 ms |
| defillama_dex | OK | 1203 ms |
| defillama_fees | OK | 2219 ms |
| defillama_stablecoins | OK | 131 ms |
| defillama_xstocks | OK | 53 ms |
| jito_kobe | OK | 233 ms |
| stakewiz | OK | 723 ms |
| github | OK | 1002 ms |
| solana_com_news | OK | 156 ms |
| sentiment | OK | 2282 ms |
| solana_status_page | OK | 413 ms |
| solana_rpc_whales | OK | 924 ms |
| solana_rpc_programs | OK | 1512 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*