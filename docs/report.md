# Solbeat — State of the Solana Network

> Generated 2026-09-20T21:13:33Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1039 is 0% complete (~32h remaining), with the cluster processing ~5,268 TPS (2,743 non-vote). Measured slot time is 267ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $982.0K of Real Economic Value over the last 24h ($682/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $109.52 (-1.2% / 24h). Decentralization: Nakamoto coefficient 18, 676 active validators, 0.1% of stake delinquent. Alpenglow readiness: validators holding 99% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 1 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 448,849,579 |
| Block height | 426,890,240 |
| Epoch | 1039 (0.37% complete, ~31.9h left) |
| TPS (10 min avg) | 5,268 |
| Non-vote TPS | 2,743 |
| Slot time (measured) | 266.7 ms |
| Est. daily transactions | 422,815,445 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0040 |
| Node version | 4.3.0-rc.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $109.52 (-1.2%/24h) |
| Market cap | $64.3B |
| **REV (24h)** | **$982.0K** (fees $826.3K + Jito tips $155.7K) |
| Chain TVL | $6.2B |
| Stablecoin supply | $15.7B |
| DEX volume (24h) | $2.9B (-18.7%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 587,438,210 SOL |
| Inflation | 3.64% |

Top DEXs by 24h volume: PumpSwap ($606.4M), BisonFi ($386.8M), Raydium AMM ($277.1M), HumidiFi ($228.9M), Orca DEX ($203.7M)

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

**70/100 — Bullish** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 78.0 |
| fear greed | 71 |
| momentum | 55.5 |
| news | 82 |

Crypto Fear & Greed: 71 (Greed) · CoinGecko votes bullish: 78.05% · headline tone (48h): +4

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 164 |
| Raydium AMM v4 | 164 |
| Orca Whirlpool | 184 |
| Pump.fun | 210 |
| Tensor | 1 |
| Magic Eden v2 | 57 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,943,926 |
| Binance (cold) | 1,272,185 |
| OKX (attributed) | 243,904 |
| Coinbase (hot) | 16,931 |

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
| solana_rpc | OK | 12697 ms |
| solana_rpc_validators | OK | 1410 ms |
| coingecko | OK | 1709 ms |
| defillama_tvl | OK | 266 ms |
| defillama_dex | OK | 963 ms |
| defillama_fees | OK | 1622 ms |
| defillama_stablecoins | OK | 1097 ms |
| defillama_xstocks | OK | 63 ms |
| jito_kobe | OK | 310 ms |
| stakewiz | OK | 2194 ms |
| github | OK | 768 ms |
| solana_com_news | OK | 660 ms |
| sentiment | OK | 2315 ms |
| solana_status_page | OK | 446 ms |
| solana_rpc_whales | OK | 2768 ms |
| solana_rpc_programs | OK | 5353 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*