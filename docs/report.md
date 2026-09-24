# Solbeat — State of the Solana Network

> Generated 2026-09-24T00:06:08Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1041 is 34% complete (~21h remaining), with the cluster processing ~4,849 TPS (2,337 non-vote). Measured slot time is 267ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $1.3M of Real Economic Value over the last 24h ($910/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $115.09 (-2.8% / 24h). Decentralization: Nakamoto coefficient 18, 675 active validators, 0.1% of stake delinquent. Alpenglow readiness: validators holding 99% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 1 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 449,860,851 |
| Block height | 427,900,992 |
| Epoch | 1041 (34.46% complete, ~21.0h left) |
| TPS (10 min avg) | 4,849 |
| Non-vote TPS | 2,337 |
| Slot time (measured) | 267.4 ms |
| Est. daily transactions | 406,645,196 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0058 |
| Node version | 4.3.0-rc.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $115.09 (-2.8%/24h) |
| Market cap | $67.6B |
| **REV (24h)** | **$1.3M** (fees $1.1M + Jito tips $212.8K) |
| Chain TVL | $6.4B |
| Stablecoin supply | $16.8B |
| DEX volume (24h) | $3.2B (-6.8%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 587,577,688 SOL |
| Inflation | 3.63% |

Top DEXs by 24h volume: PumpSwap ($634.1M), Raydium AMM ($399.0M), BisonFi ($368.2M), Orca DEX ($363.7M), Meteora DLMM ($266.8M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 675 / 12 |
| Delinquent stake | 0.05% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.4% |
| Avg / median commission | 12.3% / 5% |
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

- **[WARNING]** Solana TVL surge (z=+2.3 vs its recent baseline)

## Solana Pulse — sentiment (experimental)

**77/100 — Bullish** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 78.0 |
| fear greed | 71 |
| momentum | 73.3 |
| news | 90 |

Crypto Fear & Greed: 71 (Greed) · CoinGecko votes bullish: 78.05% · headline tone (48h): +5

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 145 |
| Raydium AMM v4 | 145 |
| Orca Whirlpool | 160 |
| Pump.fun | 180 |
| Tensor | 0 |
| Magic Eden v2 | 98 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,943,926 |
| Binance (cold) | 1,117,964 |
| OKX (attributed) | 241,118 |
| Coinbase (hot) | 25,684 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 267ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 99.4% of stake.
- **Agave**: latest release v4.3.0 · running 4.3.0-rc.0 on the polled node.
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
| solana_rpc | OK | 8721 ms |
| solana_rpc_validators | OK | 235 ms |
| coingecko | OK | 1814 ms |
| defillama_tvl | OK | 116 ms |
| defillama_dex | OK | 78 ms |
| defillama_fees | OK | 147 ms |
| defillama_stablecoins | OK | 147 ms |
| defillama_xstocks | OK | 61 ms |
| jito_kobe | OK | 375 ms |
| stakewiz | OK | 1545 ms |
| github | OK | 973 ms |
| solana_com_news | OK | 293 ms |
| sentiment | OK | 2329 ms |
| solana_status_page | OK | 388 ms |
| solana_rpc_whales | OK | 932 ms |
| solana_rpc_programs | OK | 1592 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*