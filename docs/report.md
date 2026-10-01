# Solbeat — State of the Solana Network

> Generated 2026-10-01T11:45:59Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1046 is 94% complete (~2h remaining), with the cluster processing ~3,824 TPS (1,324 non-vote). Measured slot time is 268ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $1.3M of Real Economic Value over the last 24h ($876/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $117.91 (-1.5% / 24h). Decentralization: Nakamoto coefficient 18, 672 active validators, 0.1% of stake delinquent. Alpenglow readiness: validators holding 99% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: all clear across every monitored metric.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 452,278,136 |
| Block height | 430,317,117 |
| Epoch | 1046 (94.01% complete, ~1.9h left) |
| TPS (10 min avg) | 3,824 |
| Non-vote TPS | 1,324 |
| Slot time (measured) | 267.9 ms |
| Est. daily transactions | 342,619,445 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0083 |
| Node version | 4.3.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $117.91 (-1.5%/24h) |
| Market cap | $69.3B |
| **REV (24h)** | **$1.3M** (fees $1.0M + Jito tips $211.3K) |
| Chain TVL | $6.5B |
| Stablecoin supply | $16.3B |
| DEX volume (24h) | $2.6B (1.4%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 588,004,909 SOL |
| Inflation | 3.62% |

Top DEXs by 24h volume: Orca DEX ($411.3M), BisonFi ($285.0M), Raydium AMM ($254.4M), PumpSwap ($207.0M), Meteora DLMM ($205.4M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 672 / 11 |
| Delinquent stake | 0.05% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.5% |
| Avg / median commission | 13% / 5.0% |
| Alpenglow BLS-key readiness | 704 validators, 99.4% of stake |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L43ZWjwCHART3o…` | 17,227,376 | 3.91% | 7% |
| 2 | `he1iusunGwqrNtafDtLd…` | 15,893,945 | 3.61% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5…` | 12,330,668 | 2.8% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxb…` | 11,384,141 | 2.58% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxA…` | 11,206,135 | 2.54% | 5% |
| 6 | `26pV97Ce83ZQ6Kz9XT4t…` | 9,257,721 | 2.1% | 7% |
| 7 | `51JBzSTU5rAM8gLAVQKg…` | 9,232,740 | 2.1% | 10% |
| 8 | `9QU2QSxhb24FUX3Tu2Fp…` | 7,652,675 | 1.74% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJn…` | 7,092,577 | 1.61% | 5% |
| 10 | `DumiCKHVqoCQKD8roLAp…` | 6,513,562 | 1.48% | 0% |

## Signals (anomaly detection)

All clear — no anomalies across monitored metrics.

## Solana Pulse — sentiment (experimental)

**65/100 — Bullish** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 73.0 |
| fear greed | 74 |
| momentum | 53.4 |
| news | 58 |

Crypto Fear & Greed: 74 (Greed) · CoinGecko votes bullish: 72.97% · headline tone (48h): +1

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 134 |
| Raydium AMM v4 | 134 |
| Orca Whirlpool | 122 |
| Pump.fun | 162 |
| Tensor | 0 |
| Magic Eden v2 | 64 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 10,572,652 |
| Binance (cold) | 1,091,007 |
| OKX (attributed) | 387,517 |
| Coinbase (hot) | 13,171 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 268ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 99.4% of stake.
- **Agave**: latest release v4.3.0 · running 4.3.0 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

### Latest ecosystem news (solana.com)

- [Open USD Is Live on Solana](https://solana.com/news/open-usd-is-live-on-solana) — Wed, 30 Sep 2026
- [Slot Time Reduction Effects](https://solana.com/news/slot-time-reduction-effects) — Mon, 28 Sep 2026
- [Solana Foundation Appoints Rachel Conlan as Chief Strategy Officer and Jamal Raees as General Manager of Payments](https://solana.com/news/solana-foundation-appoints-2026) — Thu, 24 Sep 2026
- [Stocks Go Onchain: What the SEC's Innovation Exemption Means for Solana](https://solana.com/news/stocks-sec-innovation-exemption) — Wed, 23 Sep 2026
- [Solana Changelog: September 18, 2026](https://solana.com/news/solana-changelog-september-18-2026) — Sat, 19 Sep 2026
- [How AI Is Reshaping Crypto Security, with Michael Coates](https://solana.com/news/bits-to-bricks-crypto-security-michael-coates) — Sat, 19 Sep 2026

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 7222 ms |
| solana_rpc_validators | OK | 145 ms |
| coingecko | OK | 1714 ms |
| defillama_tvl | OK | 106 ms |
| defillama_dex | OK | 1195 ms |
| defillama_fees | OK | 2043 ms |
| defillama_stablecoins | OK | 764 ms |
| defillama_xstocks | OK | 244 ms |
| jito_kobe | OK | 260 ms |
| stakewiz | OK | 1409 ms |
| github | OK | 1013 ms |
| solana_com_news | OK | 123 ms |
| sentiment | OK | 2362 ms |
| solana_status_page | OK | 481 ms |
| solana_rpc_whales | OK | 899 ms |
| solana_rpc_programs | OK | 1709 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*