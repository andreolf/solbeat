# Solbeat — State of the Solana Network

> Generated 2026-09-21T11:36:54Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1039 is 45% complete (~18h remaining), with the cluster processing ~4,046 TPS (1,522 non-vote). Measured slot time is 267ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $950.9K of Real Economic Value over the last 24h ($660/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $116.41 (+7.7% / 24h). Alpenglow readiness: validators holding 99% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 1 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 449,043,795 |
| Block height | 427,084,432 |
| Epoch | 1039 (45.32% complete, ~17.5h left) |
| TPS (10 min avg) | 4,046 |
| Non-vote TPS | 1,522 |
| Slot time (measured) | 267.1 ms |
| Est. daily transactions | 353,190,226 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0059 |
| Node version | 4.3.0-rc.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $116.41 (+7.7%/24h) |
| Market cap | $68.4B |
| **REV (24h)** | **$950.9K** (fees $787.0K + Jito tips $163.9K) |
| Chain TVL | $6.4B |
| Stablecoin supply | $15.8B |
| DEX volume (24h) | $2.8B (-2.8%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 587,437,429 SOL |
| Inflation | 3.64% |

Top DEXs by 24h volume: PumpSwap ($482.8M), BisonFi ($424.3M), Raydium AMM ($337.3M), Orca DEX ($301.6M), HumidiFi ($253.1M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | None / None |
| Delinquent stake | None% |
| Nakamoto coefficient | None |
| Top-10 stake share | None% |
| Avg / median commission | None% / None% |
| Alpenglow BLS-key readiness | 699 validators, 99.4% of stake |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|

## Signals (anomaly detection)

- **[WARNING]** Solana TVL surge (z=+2.5 vs its recent baseline)

## Solana Pulse — sentiment (experimental)

**74/100 — Bullish** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 83.7 |
| fear greed | 70 |
| momentum | 71.5 |
| news | 66 |

Crypto Fear & Greed: 70 (Greed) · CoinGecko votes bullish: 83.67% · headline tone (48h): +2

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 151 |
| Raydium AMM v4 | 168 |
| Orca Whirlpool | 216 |
| Pump.fun | 216 |
| Tensor | 0 |
| Magic Eden v2 | 68 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,943,926 |
| Binance (cold) | 1,416,574 |
| OKX (attributed) | 251,400 |
| Coinbase (hot) | 79,759 |

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
| solana_rpc | OK | 12829 ms |
| solana_rpc_validators | FAILED | 7600 ms |
| coingecko | OK | 1659 ms |
| defillama_tvl | OK | 66 ms |
| defillama_dex | OK | 399 ms |
| defillama_fees | OK | 666 ms |
| defillama_stablecoins | OK | 162 ms |
| defillama_xstocks | OK | 325 ms |
| jito_kobe | OK | 158 ms |
| stakewiz | OK | 648 ms |
| github | OK | 687 ms |
| solana_com_news | OK | 71 ms |
| sentiment | OK | 2127 ms |
| solana_status_page | OK | 225 ms |
| solana_rpc_whales | OK | 3052 ms |
| solana_rpc_programs | OK | 6280 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*