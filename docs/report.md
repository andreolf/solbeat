# Solbeat — State of the Solana Network

> Generated 2026-09-24T13:25:58Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1041 is 76% complete (~8h remaining), with the cluster processing ~4,483 TPS (1,958 non-vote). Measured slot time is 266ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $1.2M of Real Economic Value over the last 24h ($850/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $114.43 (-1.8% / 24h). Decentralization: Nakamoto coefficient 18, 674 active validators, 0.1% of stake delinquent. Alpenglow readiness: validators holding 99% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 1 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 450,041,912 |
| Block height | 428,082,015 |
| Epoch | 1041 (76.37% complete, ~7.5h left) |
| TPS (10 min avg) | 4,483 |
| Non-vote TPS | 1,958 |
| Slot time (measured) | 265.9 ms |
| Est. daily transactions | 365,179,212 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0069 |
| Node version | 4.3.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $114.43 (-1.8%/24h) |
| Market cap | $67.2B |
| **REV (24h)** | **$1.2M** (fees $1.0M + Jito tips $212.8K) |
| Chain TVL | $6.3B |
| Stablecoin supply | $16.4B |
| DEX volume (24h) | $2.6B (-20.1%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 587,577,156 SOL |
| Inflation | 3.63% |

Top DEXs by 24h volume: Orca DEX ($350.0M), Raydium AMM ($335.8M), BisonFi ($323.9M), PumpSwap ($270.2M), Meteora DLMM ($233.7M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 674 / 12 |
| Delinquent stake | 0.05% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.4% |
| Avg / median commission | 12.6% / 5.0% |
| Alpenglow BLS-key readiness | 699 validators, 99.4% of stake |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L43ZWjwCHART3o…` | 17,843,203 | 4.06% | 7% |
| 2 | `he1iusunGwqrNtafDtLd…` | 15,838,937 | 3.6% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5…` | 12,360,465 | 2.81% | 0% |
| 4 | `CatzoSMUkTRidT5DwBxA…` | 11,264,812 | 2.56% | 5% |
| 5 | `8GbwASqdpw4dVcwbWUxb…` | 10,335,638 | 2.35% | 0% |
| 6 | `26pV97Ce83ZQ6Kz9XT4t…` | 9,226,124 | 2.1% | 7% |
| 7 | `51JBzSTU5rAM8gLAVQKg…` | 9,158,950 | 2.08% | 10% |
| 8 | `9QU2QSxhb24FUX3Tu2Fp…` | 7,600,816 | 1.73% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJn…` | 7,090,585 | 1.61% | 5% |
| 10 | `DumiCKHVqoCQKD8roLAp…` | 6,557,340 | 1.49% | 0% |

## Signals (anomaly detection)

- **[WARNING]** Solana TVL surge (z=+2.1 vs its recent baseline)

## Solana Pulse — sentiment (experimental)

**68/100 — Bullish** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 63.0 |
| fear greed | 71 |
| momentum | 62.2 |
| news | 82 |

Crypto Fear & Greed: 71 (Greed) · CoinGecko votes bullish: 62.96% · headline tone (48h): +4

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 151 |
| Raydium AMM v4 | 137 |
| Orca Whirlpool | 168 |
| Pump.fun | 168 |
| Tensor | 0 |
| Magic Eden v2 | 126 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,943,926 |
| Binance (cold) | 1,221,246 |
| OKX (attributed) | 235,362 |
| Coinbase (hot) | 17,294 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 266ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 99.4% of stake.
- **Agave**: latest release v4.3.0 · running 4.3.0 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

### Latest ecosystem news (solana.com)

- [Stocks Go Onchain: What the SEC's Innovation Exemption Means for Solana](https://solana.com/news/stocks-sec-innovation-exemption) — Wed, 23 Sep 2026
- [Solana Changelog: September 18, 2026](https://solana.com/news/solana-changelog-september-18-2026) — Sat, 19 Sep 2026
- [How AI Is Reshaping Crypto Security, with Michael Coates](https://solana.com/news/bits-to-bricks-crypto-security-michael-coates) — Sat, 19 Sep 2026
- [Project Harmonia Brings Institutional Tokenized Funds to Solana](https://solana.com/news/project-harmonia-brings-institutional-tokenized-funds-to-solana) — Wed, 16 Sep 2026
- [Solana: Building, Proving and Earning Trust in Public](https://solana.com/news/solana-building-trust-in-public) — Mon, 14 Sep 2026
- [Solana Changelog: September 10, 2026](https://solana.com/news/solana-changelog-september-10-2026) — Thu, 10 Sep 2026

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 7624 ms |
| solana_rpc_validators | OK | 230 ms |
| coingecko | OK | 1645 ms |
| defillama_tvl | OK | 39 ms |
| defillama_dex | OK | 1160 ms |
| defillama_fees | OK | 3238 ms |
| defillama_stablecoins | OK | 63 ms |
| defillama_xstocks | OK | 910 ms |
| jito_kobe | OK | 207 ms |
| stakewiz | OK | 1822 ms |
| github | OK | 754 ms |
| solana_com_news | OK | 163 ms |
| sentiment | OK | 2236 ms |
| solana_status_page | OK | 397 ms |
| solana_rpc_whales | OK | 994 ms |
| solana_rpc_programs | OK | 1665 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*