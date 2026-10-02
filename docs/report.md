# Solbeat — State of the Solana Network

> Generated 2026-10-02T19:15:07Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1047 is 92% complete (~3h remaining), with the cluster processing ~4,933 TPS (2,462 non-vote). Measured slot time is 271ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $1.3M of Real Economic Value over the last 24h ($933/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $117.87 (-0.5% / 24h). Decentralization: Nakamoto coefficient 18, 672 active validators, 0.0% of stake delinquent. Alpenglow readiness: validators holding 99% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 1 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 452,701,339 |
| Block height | 430,739,990 |
| Epoch | 1047 (91.98% complete, ~2.6h left) |
| TPS (10 min avg) | 4,933 |
| Non-vote TPS | 2,462 |
| Slot time (measured) | 270.6 ms |
| Est. daily transactions | 430,154,537 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0052 |
| Node version | 4.3.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $117.87 (-0.5%/24h) |
| Market cap | $69.4B |
| **REV (24h)** | **$1.3M** (fees $1.1M + Jito tips $222.7K) |
| Chain TVL | $6.7B |
| Stablecoin supply | $16.5B |
| DEX volume (24h) | $2.5B (-3.2%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 588,074,928 SOL |
| Inflation | 3.62% |

Top DEXs by 24h volume: Orca DEX ($404.2M), PumpSwap ($371.2M), Raydium AMM ($261.4M), BisonFi ($216.9M), Meteora DLMM ($195.5M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 672 / 12 |
| Delinquent stake | 0.02% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.6% |
| Avg / median commission | 13% / 5.0% |
| Alpenglow BLS-key readiness | 703 validators, 99.4% of stake |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L43ZWjwCHART3o…` | 17,839,408 | 4.05% | 7% |
| 2 | `he1iusunGwqrNtafDtLd…` | 15,905,145 | 3.61% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5…` | 12,328,203 | 2.8% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxb…` | 11,357,265 | 2.58% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxA…` | 11,209,121 | 2.54% | 5% |
| 6 | `26pV97Ce83ZQ6Kz9XT4t…` | 9,267,704 | 2.1% | 7% |
| 7 | `51JBzSTU5rAM8gLAVQKg…` | 9,246,451 | 2.1% | 10% |
| 8 | `9QU2QSxhb24FUX3Tu2Fp…` | 7,601,711 | 1.72% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJn…` | 7,063,975 | 1.6% | 5% |
| 10 | `3JD3jMmnR6g88qff2WZ3…` | 6,682,305 | 1.52% | 0% |

## Signals (anomaly detection)

- **[WARNING]** Solana TVL surge (z=+2.0 vs its recent baseline)

## Solana Pulse — sentiment (experimental)

**66/100 — Bullish** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 82.5 |
| fear greed | 72 |
| momentum | 47.7 |
| news | 58 |

Crypto Fear & Greed: 72 (Greed) · CoinGecko votes bullish: 82.46% · headline tone (48h): +1

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 158 |
| Raydium AMM v4 | 143 |
| Orca Whirlpool | 158 |
| Pump.fun | 158 |
| Tensor | 0 |
| Magic Eden v2 | 49 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 10,572,652 |
| Binance (cold) | 1,294,044 |
| OKX (attributed) | 359,929 |
| Coinbase (hot) | 137,900 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 271ms · proposal merged.
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
| solana_rpc | OK | 7048 ms |
| solana_rpc_validators | OK | 242 ms |
| coingecko | OK | 1741 ms |
| defillama_tvl | OK | 316 ms |
| defillama_dex | OK | 1198 ms |
| defillama_fees | OK | 2528 ms |
| defillama_stablecoins | OK | 178 ms |
| defillama_xstocks | OK | 47 ms |
| jito_kobe | OK | 251 ms |
| stakewiz | OK | 1513 ms |
| github | OK | 969 ms |
| solana_com_news | OK | 112 ms |
| sentiment | OK | 2316 ms |
| solana_status_page | OK | 642 ms |
| solana_rpc_whales | OK | 957 ms |
| solana_rpc_programs | OK | 1666 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*