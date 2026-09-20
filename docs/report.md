# Solbeat — State of the Solana Network

> Generated 2026-09-20T04:00:31Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1038 is 47% complete (~17h remaining), with the cluster processing ~4,023 TPS (1,470 non-vote). Measured slot time is 265ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $982.0K of Real Economic Value over the last 24h ($682/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $108.89 (-3.8% / 24h). Decentralization: Nakamoto coefficient 18, 679 active validators, 0.0% of stake delinquent. Alpenglow readiness: validators holding 99% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 1 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 448,617,135 |
| Block height | 426,657,859 |
| Epoch | 1038 (46.56% complete, ~17.0h left) |
| TPS (10 min avg) | 4,023 |
| Non-vote TPS | 1,470 |
| Slot time (measured) | 265.1 ms |
| Est. daily transactions | 375,704,588 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0053 |
| Node version | 4.3.0-rc.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $108.89 (-3.8%/24h) |
| Market cap | $64.0B |
| **REV (24h)** | **$982.0K** (fees $826.3K + Jito tips $155.7K) |
| Chain TVL | $6.2B |
| Stablecoin supply | $15.7B |
| DEX volume (24h) | $3.2B (-8.6%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 587,367,148 SOL |
| Inflation | 3.64% |

Top DEXs by 24h volume: PumpSwap ($606.4M), BisonFi ($532.7M), HumidiFi ($334.9M), Raydium AMM ($317.9M), Tessera V ($205.6M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 679 / 11 |
| Delinquent stake | 0.0% |
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

- **[WARNING]** Solana TVL surge (z=+2.1 vs its recent baseline)

## Solana Pulse — sentiment (experimental)

**71/100 — Bullish** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 73.3 |
| fear greed | 71 |
| momentum | 60.1 |
| news | 90 |

Crypto Fear & Greed: 71 (Greed) · CoinGecko votes bullish: 73.33% · headline tone (48h): +5

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 147 |
| Raydium AMM v4 | 134 |
| Orca Whirlpool | 147 |
| Pump.fun | 147 |
| Tensor | 0 |
| Magic Eden v2 | 60 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,943,926 |
| Binance (cold) | 1,326,462 |
| OKX (attributed) | 243,904 |
| Coinbase (hot) | 17,765 |

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
| solana_rpc | OK | 7375 ms |
| solana_rpc_validators | OK | 139 ms |
| coingecko | OK | 1776 ms |
| defillama_tvl | OK | 141 ms |
| defillama_dex | OK | 10705 ms |
| defillama_fees | OK | 7562 ms |
| defillama_stablecoins | OK | 746 ms |
| defillama_xstocks | OK | 68 ms |
| jito_kobe | OK | 133 ms |
| stakewiz | OK | 384 ms |
| github | OK | 958 ms |
| solana_com_news | OK | 118 ms |
| sentiment | OK | 2361 ms |
| solana_status_page | OK | 399 ms |
| solana_rpc_whales | OK | 846 ms |
| solana_rpc_programs | OK | 1455 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*