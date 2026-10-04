# Solbeat — State of the Solana Network

> Generated 2026-10-04T08:42:20Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1049 is 9% complete (~29h remaining), with the cluster processing ~4,689 TPS (2,199 non-vote). Measured slot time is 269ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $1.1M of Real Economic Value over the last 24h ($777/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $120.85 (+1.4% / 24h). Decentralization: Nakamoto coefficient 18, 671 active validators, 0.0% of stake delinquent. Alpenglow readiness: validators holding 99% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: all clear across every monitored metric.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 453,205,772 |
| Block height | 431,244,204 |
| Epoch | 1049 (8.74% complete, ~29.4h left) |
| TPS (10 min avg) | 4,689 |
| Non-vote TPS | 2,199 |
| Slot time (measured) | 268.6 ms |
| Est. daily transactions | 365,656,695 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0060 |
| Node version | 4.3.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $120.85 (+1.4%/24h) |
| Market cap | $71.1B |
| **REV (24h)** | **$1.1M** (fees $902.9K + Jito tips $215.5K) |
| Chain TVL | $6.7B |
| Stablecoin supply | $16.8B |
| DEX volume (24h) | $2.1B (-22.8%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 588,216,414 SOL |
| Inflation | 3.62% |

Top DEXs by 24h volume: PumpSwap ($402.0M), BisonFi ($347.8M), pump.fun ($177.6M), Tessera V ($154.9M), fomo Wallet ($138.5M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 671 / 15 |
| Delinquent stake | 0.03% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.6% |
| Avg / median commission | 12.7% / 5% |
| Alpenglow BLS-key readiness | 703 validators, 99.4% of stake |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L43ZWjwCHART3o…` | 17,935,562 | 4.06% | 7% |
| 2 | `he1iusunGwqrNtafDtLd…` | 15,927,649 | 3.6% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5…` | 12,346,574 | 2.79% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxb…` | 11,305,935 | 2.56% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxA…` | 11,136,537 | 2.52% | 5% |
| 6 | `26pV97Ce83ZQ6Kz9XT4t…` | 9,254,655 | 2.09% | 7% |
| 7 | `51JBzSTU5rAM8gLAVQKg…` | 9,241,331 | 2.09% | 10% |
| 8 | `9QU2QSxhb24FUX3Tu2Fp…` | 7,616,097 | 1.72% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJn…` | 7,061,519 | 1.6% | 5% |
| 10 | `3JD3jMmnR6g88qff2WZ3…` | 6,686,111 | 1.51% | 0% |

## Signals (anomaly detection)

All clear — no anomalies across monitored metrics.

## Solana Pulse — sentiment (experimental)

**62/100 — Bullish** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 80.7 |
| fear greed | 65 |
| momentum | 38.7 |
| news | 66 |

Crypto Fear & Greed: 65 (Greed) · CoinGecko votes bullish: 80.65% · headline tone (48h): +2

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 147 |
| Raydium AMM v4 | 147 |
| Orca Whirlpool | 163 |
| Pump.fun | 163 |
| Tensor | 1 |
| Magic Eden v2 | 40 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 10,572,652 |
| Binance (cold) | 1,373,071 |
| OKX (attributed) | 301,675 |
| Coinbase (hot) | 13,816 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 269ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 99.4% of stake.
- **Agave**: latest release v4.3.0 · running 4.3.0 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

### Latest ecosystem news (solana.com)

- [Solana x AI: The Democratization Layer](https://solana.com/news/solana-ai-the-democratization-layer) — Fri, 02 Oct 2026
- [Open USD Is Live on Solana](https://solana.com/news/open-usd-is-live-on-solana) — Wed, 30 Sep 2026
- [Slot Time Reduction Effects](https://solana.com/news/slot-time-reduction-effects) — Mon, 28 Sep 2026
- [Solana Foundation Appoints Rachel Conlan as Chief Strategy Officer and Jamal Raees as General Manager of Payments](https://solana.com/news/solana-foundation-appoints-2026) — Thu, 24 Sep 2026
- [Stocks Go Onchain: What the SEC's Innovation Exemption Means for Solana](https://solana.com/news/stocks-sec-innovation-exemption) — Wed, 23 Sep 2026
- [Solana Changelog: September 18, 2026](https://solana.com/news/solana-changelog-september-18-2026) — Sat, 19 Sep 2026

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 9047 ms |
| solana_rpc_validators | OK | 341 ms |
| coingecko | OK | 1673 ms |
| defillama_tvl | OK | 196 ms |
| defillama_dex | OK | 1488 ms |
| defillama_fees | OK | 2012 ms |
| defillama_stablecoins | OK | 251 ms |
| defillama_xstocks | OK | 611 ms |
| jito_kobe | OK | 361 ms |
| stakewiz | OK | 1232 ms |
| github | OK | 869 ms |
| solana_com_news | OK | 169 ms |
| sentiment | OK | 2251 ms |
| solana_status_page | OK | 332 ms |
| solana_rpc_whales | OK | 1149 ms |
| solana_rpc_programs | OK | 2206 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*