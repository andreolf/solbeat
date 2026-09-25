# Solbeat — State of the Solana Network

> Generated 2026-09-25T07:37:23Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1042 is 33% complete (~21h remaining), with the cluster processing ~3,911 TPS (1,366 non-vote). Measured slot time is 265ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $1.2M of Real Economic Value over the last 24h ($828/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $116.02 (+0.5% / 24h). Decentralization: Nakamoto coefficient 18, 677 active validators, 0.0% of stake delinquent. Alpenglow readiness: validators holding 99% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 3 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 450,287,266 |
| Block height | 428,327,174 |
| Epoch | 1042 (33.16% complete, ~21.2h left) |
| TPS (10 min avg) | 3,911 |
| Non-vote TPS | 1,366 |
| Slot time (measured) | 264.9 ms |
| Est. daily transactions | 350,197,563 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0072 |
| Node version | 4.3.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $116.02 (+0.5%/24h) |
| Market cap | $68.2B |
| **REV (24h)** | **$1.2M** (fees $952.7K + Jito tips $239.3K) |
| Chain TVL | $6.5B |
| Stablecoin supply | $17.6B |
| DEX volume (24h) | $2.3B (-11.4%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 587,647,826 SOL |
| Inflation | 3.63% |

Top DEXs by 24h volume: Orca DEX ($324.6M), BisonFi ($323.9M), Raydium AMM ($310.3M), Meteora DLMM ($191.0M), PumpSwap ($133.8M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 677 / 8 |
| Delinquent stake | 0.0% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.4% |
| Avg / median commission | 12.6% / 5% |
| Alpenglow BLS-key readiness | 699 validators, 99.3% of stake |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L43ZWjwCHART3o…` | 17,819,007 | 4.04% | 7% |
| 2 | `he1iusunGwqrNtafDtLd…` | 15,817,079 | 3.59% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5…` | 12,387,904 | 2.81% | 0% |
| 4 | `CatzoSMUkTRidT5DwBxA…` | 11,274,982 | 2.56% | 5% |
| 5 | `8GbwASqdpw4dVcwbWUxb…` | 10,595,499 | 2.4% | 0% |
| 6 | `26pV97Ce83ZQ6Kz9XT4t…` | 9,221,893 | 2.09% | 7% |
| 7 | `51JBzSTU5rAM8gLAVQKg…` | 9,163,088 | 2.08% | 10% |
| 8 | `9QU2QSxhb24FUX3Tu2Fp…` | 7,599,959 | 1.72% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJn…` | 7,091,911 | 1.61% | 5% |
| 10 | `DumiCKHVqoCQKD8roLAp…` | 6,557,887 | 1.49% | 0% |

## Signals (anomaly detection)

- **[WARNING]** Solana TVL surge (z=+2.2 vs its recent baseline)
- **[SERIOUS]** Stablecoin supply surge (z=+3.4 vs its recent baseline)
- **[WARNING · liquidity_rotation]** Stablecoin supply and TVL moving together — capital rotating in or out of the chain.

## Solana Pulse — sentiment (experimental)

**67/100 — Bullish** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 75.0 |
| fear greed | 71 |
| momentum | 56.7 |
| news | 66 |

Crypto Fear & Greed: 71 (Greed) · CoinGecko votes bullish: 75.0% · headline tone (48h): +2

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 158 |
| Raydium AMM v4 | 111 |
| Orca Whirlpool | 158 |
| Pump.fun | 158 |
| Tensor | 0 |
| Magic Eden v2 | 104 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,943,926 |
| Binance (cold) | 1,356,226 |
| OKX (attributed) | 208,200 |
| Coinbase (hot) | 25,835 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 265ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 99.3% of stake.
- **Agave**: latest release v4.3.0 · running 4.3.0 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

### Latest ecosystem news (solana.com)

- [Solana Foundation Appoints Rachel Conlan as Chief Strategy Officer and Jamal Raees as General Manager of Payments](https://solana.com/news/solana-foundation-appoints-2026) — Thu, 24 Sep 2026
- [Stocks Go Onchain: What the SEC's Innovation Exemption Means for Solana](https://solana.com/news/stocks-sec-innovation-exemption) — Wed, 23 Sep 2026
- [Solana Changelog: September 18, 2026](https://solana.com/news/solana-changelog-september-18-2026) — Sat, 19 Sep 2026
- [How AI Is Reshaping Crypto Security, with Michael Coates](https://solana.com/news/bits-to-bricks-crypto-security-michael-coates) — Sat, 19 Sep 2026
- [Project Harmonia Brings Institutional Tokenized Funds to Solana](https://solana.com/news/project-harmonia-brings-institutional-tokenized-funds-to-solana) — Wed, 16 Sep 2026
- [Solana: Building, Proving and Earning Trust in Public](https://solana.com/news/solana-building-trust-in-public) — Mon, 14 Sep 2026

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 6898 ms |
| solana_rpc_validators | OK | 139 ms |
| coingecko | OK | 1728 ms |
| defillama_tvl | OK | 103 ms |
| defillama_dex | OK | 1181 ms |
| defillama_fees | OK | 2115 ms |
| defillama_stablecoins | OK | 519 ms |
| defillama_xstocks | OK | 843 ms |
| jito_kobe | OK | 350 ms |
| stakewiz | OK | 1649 ms |
| github | OK | 932 ms |
| solana_com_news | OK | 108 ms |
| sentiment | OK | 2479 ms |
| solana_status_page | OK | 437 ms |
| solana_rpc_whales | OK | 968 ms |
| solana_rpc_programs | OK | 1584 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*