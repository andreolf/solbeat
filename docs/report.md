# Solbeat — State of the Solana Network

> Generated 2026-09-20T05:31:54Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1038 is 51% complete (~16h remaining), with the cluster processing ~3,987 TPS (1,450 non-vote). Measured slot time is 266ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $981.3K of Real Economic Value over the last 24h ($681/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $108.86 (-3.5% / 24h). Decentralization: Nakamoto coefficient 18, 678 active validators, 0.0% of stake delinquent. Alpenglow readiness: validators holding 99% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 1 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 448,637,695 |
| Block height | 426,678,419 |
| Epoch | 1038 (51.32% complete, ~15.6h left) |
| TPS (10 min avg) | 3,987 |
| Non-vote TPS | 1,450 |
| Slot time (measured) | 266.2 ms |
| Est. daily transactions | 360,087,972 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0059 |
| Node version | 4.3.0-rc.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $108.86 (-3.5%/24h) |
| Market cap | $63.9B |
| **REV (24h)** | **$981.3K** (fees $826.3K + Jito tips $155.1K) |
| Chain TVL | $6.2B |
| Stablecoin supply | $15.7B |
| DEX volume (24h) | $3.2B (-8.6%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 587,367,091 SOL |
| Inflation | 3.64% |

Top DEXs by 24h volume: PumpSwap ($606.4M), BisonFi ($532.7M), HumidiFi ($334.9M), Raydium AMM ($313.4M), Tessera V ($205.6M)

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

- **[WARNING]** Solana TVL surge (z=+2.1 vs its recent baseline)

## Solana Pulse — sentiment (experimental)

**70/100 — Bullish** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 72.4 |
| fear greed | 71 |
| momentum | 59.9 |
| news | 82 |

Crypto Fear & Greed: 71 (Greed) · CoinGecko votes bullish: 72.41% · headline tone (48h): +4

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 153 |
| Raydium AMM v4 | 138 |
| Orca Whirlpool | 153 |
| Pump.fun | 170 |
| Tensor | 1 |
| Magic Eden v2 | 56 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,943,926 |
| Binance (cold) | 1,325,638 |
| OKX (attributed) | 243,904 |
| Coinbase (hot) | 18,469 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 266ms · proposal merged.
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
| solana_rpc | OK | 6964 ms |
| solana_rpc_validators | OK | 132 ms |
| coingecko | OK | 1827 ms |
| defillama_tvl | OK | 134 ms |
| defillama_dex | OK | 1210 ms |
| defillama_fees | OK | 2018 ms |
| defillama_stablecoins | OK | 1179 ms |
| defillama_xstocks | OK | 55 ms |
| jito_kobe | OK | 247 ms |
| stakewiz | OK | 815 ms |
| github | OK | 952 ms |
| solana_com_news | OK | 113 ms |
| sentiment | OK | 2395 ms |
| solana_status_page | OK | 489 ms |
| solana_rpc_whales | OK | 888 ms |
| solana_rpc_programs | OK | 1564 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*