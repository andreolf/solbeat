# Solbeat — State of the Solana Network

> Generated 2026-09-21T01:07:48Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1039 is 13% complete (~28h remaining), with the cluster processing ~4,647 TPS (2,125 non-vote). Measured slot time is 267ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $984.5K of Real Economic Value over the last 24h ($684/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $112.32 (+1.4% / 24h). Decentralization: Nakamoto coefficient 18, 676 active validators, 0.1% of stake delinquent. Alpenglow readiness: validators holding 99% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 1 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 448,902,152 |
| Block height | 426,942,797 |
| Epoch | 1039 (12.54% complete, ~28.0h left) |
| TPS (10 min avg) | 4,647 |
| Non-vote TPS | 2,125 |
| Slot time (measured) | 267.0 ms |
| Est. daily transactions | 411,492,831 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0043 |
| Node version | 4.3.0-rc.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $112.32 (+1.4%/24h) |
| Market cap | $65.9B |
| **REV (24h)** | **$984.5K** (fees $826.3K + Jito tips $158.2K) |
| Chain TVL | $6.2B |
| Stablecoin supply | $15.7B |
| DEX volume (24h) | $2.8B (-4.3%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 587,437,844 SOL |
| Inflation | 3.64% |

Top DEXs by 24h volume: PumpSwap ($482.8M), BisonFi ($386.8M), Raydium AMM ($297.8M), Orca DEX ($244.1M), HumidiFi ($228.9M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 676 / 14 |
| Delinquent stake | 0.05% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.3% |
| Avg / median commission | 12.2% / 5.0% |
| Alpenglow BLS-key readiness | 699 validators, 99.4% of stake |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L43ZWjwCHART3o…` | 17,856,583 | 4.06% | 7% |
| 2 | `he1iusunGwqrNtafDtLd…` | 15,828,384 | 3.6% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5…` | 12,518,302 | 2.85% | 0% |
| 4 | `CatzoSMUkTRidT5DwBxA…` | 11,252,588 | 2.56% | 5% |
| 5 | `8GbwASqdpw4dVcwbWUxb…` | 9,788,818 | 2.23% | 0% |
| 6 | `26pV97Ce83ZQ6Kz9XT4t…` | 9,251,354 | 2.1% | 7% |
| 7 | `51JBzSTU5rAM8gLAVQKg…` | 9,106,985 | 2.07% | 10% |
| 8 | `9QU2QSxhb24FUX3Tu2Fp…` | 7,443,840 | 1.69% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJn…` | 7,088,079 | 1.61% | 5% |
| 10 | `DumiCKHVqoCQKD8roLAp…` | 6,572,007 | 1.49% | 0% |

## Signals (anomaly detection)

- **[WARNING]** Solana TVL surge (z=+2.1 vs its recent baseline)

## Solana Pulse — sentiment (experimental)

**69/100 — Bullish** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 75.0 |
| fear greed | 70 |
| momentum | 64.0 |
| news | 66 |

Crypto Fear & Greed: 70 (Greed) · CoinGecko votes bullish: 75.0% · headline tone (48h): +2

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 140 |
| Raydium AMM v4 | 154 |
| Orca Whirlpool | 172 |
| Pump.fun | 172 |
| Tensor | 2 |
| Magic Eden v2 | 44 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,943,926 |
| Binance (cold) | 1,252,519 |
| OKX (attributed) | 251,398 |
| Coinbase (hot) | 12,752 |

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
| solana_rpc | OK | 7456 ms |
| solana_rpc_validators | OK | 136 ms |
| coingecko | OK | 1788 ms |
| defillama_tvl | OK | 124 ms |
| defillama_dex | OK | 1165 ms |
| defillama_fees | OK | 1401 ms |
| defillama_stablecoins | OK | 124 ms |
| defillama_xstocks | OK | 65 ms |
| jito_kobe | OK | 226 ms |
| stakewiz | OK | 1493 ms |
| github | OK | 950 ms |
| solana_com_news | OK | 149 ms |
| sentiment | OK | 2520 ms |
| solana_status_page | OK | 444 ms |
| solana_rpc_whales | OK | 875 ms |
| solana_rpc_programs | OK | 1724 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*