# Solbeat — State of the Solana Network

> Generated 2026-09-23T14:26:28Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1041 is 4% complete (~31h remaining), with the cluster processing ~5,266 TPS (2,744 non-vote). Measured slot time is 266ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $1.3M of Real Economic Value over the last 24h ($908/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $113.50 (-3.2% / 24h). Decentralization: Nakamoto coefficient 18, 675 active validators, 0.1% of stake delinquent. Alpenglow readiness: validators holding 99% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 2 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 449,730,083 |
| Block height | 427,770,316 |
| Epoch | 1041 (4.19% complete, ~30.6h left) |
| TPS (10 min avg) | 5,266 |
| Non-vote TPS | 2,744 |
| Slot time (measured) | 266.0 ms |
| Est. daily transactions | 367,425,920 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0074 |
| Node version | 4.3.0-rc.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $113.50 (-3.2%/24h) |
| Market cap | $66.7B |
| **REV (24h)** | **$1.3M** (fees $1.1M + Jito tips $211.0K) |
| Chain TVL | $6.5B |
| Stablecoin supply | $16.8B |
| DEX volume (24h) | $3.2B (-6.8%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 587,578,198 SOL |
| Inflation | 3.63% |

Top DEXs by 24h volume: PumpSwap ($634.1M), Raydium AMM ($371.5M), BisonFi ($368.2M), Orca DEX ($327.9M), Meteora DLMM ($266.8M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 675 / 12 |
| Delinquent stake | 0.07% |
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

- **[WARNING]** TPS spike: 5,266 vs 12h mean 4,217 (z=+2.6)
- **[WARNING]** Solana TVL surge (z=+2.5 vs its recent baseline)

## Solana Pulse — sentiment (experimental)

**81/100 — Bullish** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 87.3 |
| fear greed | 71 |
| momentum | 74.9 |
| news | 95 |

Crypto Fear & Greed: 71 (Greed) · CoinGecko votes bullish: 87.27% · headline tone (48h): +6

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 160 |
| Raydium AMM v4 | 160 |
| Orca Whirlpool | 160 |
| Pump.fun | 160 |
| Tensor | 0 |
| Magic Eden v2 | 59 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,943,926 |
| Binance (cold) | 1,133,542 |
| OKX (attributed) | 256,018 |
| Coinbase (hot) | 23,260 |

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
| solana_rpc | OK | 8105 ms |
| solana_rpc_validators | OK | 115 ms |
| coingecko | OK | 1709 ms |
| defillama_tvl | OK | 87 ms |
| defillama_dex | OK | 182 ms |
| defillama_fees | OK | 1064 ms |
| defillama_stablecoins | OK | 132 ms |
| defillama_xstocks | OK | 517 ms |
| jito_kobe | OK | 2664 ms |
| stakewiz | OK | 741 ms |
| github | OK | 651 ms |
| solana_com_news | OK | 105 ms |
| sentiment | OK | 2136 ms |
| solana_status_page | OK | 479 ms |
| solana_rpc_whales | OK | 809 ms |
| solana_rpc_programs | OK | 1463 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*