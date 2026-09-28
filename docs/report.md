# Solbeat — State of the Solana Network

> Generated 2026-09-28T18:19:39Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1044 is 90% complete (~3h remaining), with the cluster processing ~4,765 TPS (2,251 non-vote). Measured slot time is 268ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $1.2M of Real Economic Value over the last 24h ($823/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $119.85 (-2.4% / 24h). Decentralization: Nakamoto coefficient 18, 676 active validators, 0.0% of stake delinquent. Alpenglow readiness: validators holding 99% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 1 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 451,397,564 |
| Block height | 429,437,199 |
| Epoch | 1044 (90.18% complete, ~3.2h left) |
| TPS (10 min avg) | 4,765 |
| Non-vote TPS | 2,251 |
| Slot time (measured) | 267.9 ms |
| Est. daily transactions | 427,953,772 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0045 |
| Node version | 4.3.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $119.85 (-2.4%/24h) |
| Market cap | $70.5B |
| **REV (24h)** | **$1.2M** (fees $949.1K + Jito tips $236.3K) |
| Chain TVL | $6.6B |
| Stablecoin supply | $16.7B |
| DEX volume (24h) | $1.9B (-10.6%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 587,781,783 SOL |
| Inflation | 3.63% |

Top DEXs by 24h volume: Orca DEX ($386.1M), PumpSwap ($297.1M), BisonFi ($270.0M), Raydium AMM ($247.9M), Meteora DLMM ($158.3M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 676 / 7 |
| Delinquent stake | 0.01% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.5% |
| Avg / median commission | 12.9% / 5.0% |
| Alpenglow BLS-key readiness | 702 validators, 99.4% of stake |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L43ZWjwCHART3o…` | 17,867,779 | 4.06% | 7% |
| 2 | `he1iusunGwqrNtafDtLd…` | 15,840,792 | 3.6% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5…` | 12,330,570 | 2.8% | 0% |
| 4 | `CatzoSMUkTRidT5DwBxA…` | 11,215,732 | 2.55% | 5% |
| 5 | `8GbwASqdpw4dVcwbWUxb…` | 10,838,730 | 2.46% | 0% |
| 6 | `26pV97Ce83ZQ6Kz9XT4t…` | 9,238,854 | 2.1% | 7% |
| 7 | `51JBzSTU5rAM8gLAVQKg…` | 9,209,776 | 2.09% | 10% |
| 8 | `9QU2QSxhb24FUX3Tu2Fp…` | 7,623,407 | 1.73% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJn…` | 7,094,526 | 1.61% | 5% |
| 10 | `DumiCKHVqoCQKD8roLAp…` | 6,511,334 | 1.48% | 0% |

## Signals (anomaly detection)

- **[WARNING]** Solana TVL surge (z=+2.1 vs its recent baseline)

## Solana Pulse — sentiment (experimental)

**66/100 — Bullish** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 70.6 |
| fear greed | 74 |
| momentum | 51.0 |
| news | 74 |

Crypto Fear & Greed: 74 (Greed) · CoinGecko votes bullish: 70.59% · headline tone (48h): +3

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 161 |
| Raydium AMM v4 | 146 |
| Orca Whirlpool | 181 |
| Pump.fun | 181 |
| Tensor | 1 |
| Magic Eden v2 | 39 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 10,772,652 |
| Binance (cold) | 1,074,581 |
| OKX (attributed) | 387,383 |
| Coinbase (hot) | 21,229 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 268ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 99.4% of stake.
- **Agave**: latest release v4.3.0 · running 4.3.0 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

### Latest ecosystem news (solana.com)

- [Slot Time Reduction Effects](https://solana.com/news/slot-time-reduction-effects) — Mon, 28 Sep 2026
- [Solana Foundation Appoints Rachel Conlan as Chief Strategy Officer and Jamal Raees as General Manager of Payments](https://solana.com/news/solana-foundation-appoints-2026) — Thu, 24 Sep 2026
- [Stocks Go Onchain: What the SEC's Innovation Exemption Means for Solana](https://solana.com/news/stocks-sec-innovation-exemption) — Wed, 23 Sep 2026
- [Solana Changelog: September 18, 2026](https://solana.com/news/solana-changelog-september-18-2026) — Sat, 19 Sep 2026
- [How AI Is Reshaping Crypto Security, with Michael Coates](https://solana.com/news/bits-to-bricks-crypto-security-michael-coates) — Sat, 19 Sep 2026
- [Project Harmonia Brings Institutional Tokenized Funds to Solana](https://solana.com/news/project-harmonia-brings-institutional-tokenized-funds-to-solana) — Wed, 16 Sep 2026

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 8538 ms |
| solana_rpc_validators | OK | 453 ms |
| coingecko | OK | 1655 ms |
| defillama_tvl | OK | 121 ms |
| defillama_dex | OK | 934 ms |
| defillama_fees | OK | 903 ms |
| defillama_stablecoins | OK | 486 ms |
| defillama_xstocks | OK | 103 ms |
| jito_kobe | OK | 276 ms |
| stakewiz | OK | 1140 ms |
| github | OK | 820 ms |
| solana_com_news | OK | 229 ms |
| sentiment | OK | 2432 ms |
| solana_status_page | OK | 510 ms |
| solana_rpc_whales | OK | 1188 ms |
| solana_rpc_programs | OK | 2221 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*