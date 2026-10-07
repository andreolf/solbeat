# Solbeat — State of the Solana Network

> Generated 2026-10-07T09:32:29Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1051 is 35% complete (~21h remaining), with the cluster processing ~3,905 TPS (1,397 non-vote). Measured slot time is 268ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $1.3M of Real Economic Value over the last 24h ($937/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $118.10 (-0.9% / 24h). Decentralization: Nakamoto coefficient 18, 673 active validators, 0.0% of stake delinquent. Alpenglow readiness: validators holding 99% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: all clear across every monitored metric.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 454,183,628 |
| Block height | 432,221,212 |
| Epoch | 1051 (35.1% complete, ~20.8h left) |
| TPS (10 min avg) | 3,905 |
| Non-vote TPS | 1,397 |
| Slot time (measured) | 267.5 ms |
| Est. daily transactions | 352,122,462 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0077 |
| Node version | 4.3.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $118.10 (-0.9%/24h) |
| Market cap | $69.6B |
| **REV (24h)** | **$1.3M** (fees $1.1M + Jito tips $298.6K) |
| Chain TVL | $6.5B |
| Stablecoin supply | $16.8B |
| DEX volume (24h) | $2.0B (-0.9%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 589,094,595 SOL |
| Inflation | 3.61% |

Top DEXs by 24h volume: Orca DEX ($316.5M), PumpSwap ($302.9M), BisonFi ($234.2M), pump.fun ($187.5M), Raydium AMM ($183.9M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 673 / 8 |
| Delinquent stake | 0.0% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.6% |
| Avg / median commission | 12.7% / 5% |
| Alpenglow BLS-key readiness | 703 validators, 99.4% of stake |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L43ZWjwCHART3o…` | 17,653,055 | 4.02% | 7% |
| 2 | `he1iusunGwqrNtafDtLd…` | 15,968,869 | 3.63% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5…` | 12,308,201 | 2.8% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxb…` | 11,264,081 | 2.56% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxA…` | 11,149,017 | 2.54% | 5% |
| 6 | `26pV97Ce83ZQ6Kz9XT4t…` | 9,259,685 | 2.11% | 7% |
| 7 | `51JBzSTU5rAM8gLAVQKg…` | 9,251,538 | 2.11% | 10% |
| 8 | `9QU2QSxhb24FUX3Tu2Fp…` | 7,508,703 | 1.71% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJn…` | 7,113,963 | 1.62% | 5% |
| 10 | `3JD3jMmnR6g88qff2WZ3…` | 6,690,032 | 1.52% | 0% |

## Signals (anomaly detection)

All clear — no anomalies across monitored metrics.

## Solana Pulse — sentiment (experimental)

**70/100 — Bullish** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 83.3 |
| fear greed | 71 |
| momentum | 49.9 |
| news | 82 |

Crypto Fear & Greed: 71 (Greed) · CoinGecko votes bullish: 83.33% · headline tone (48h): +4

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 157 |
| Raydium AMM v4 | 142 |
| Orca Whirlpool | 157 |
| Pump.fun | 176 |
| Tensor | 0 |
| Magic Eden v2 | 81 |
| Marinade | 1 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 10,572,652 |
| Binance (cold) | 1,073,662 |
| OKX (attributed) | 304,343 |
| Coinbase (hot) | 16,341 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 268ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 99.4% of stake.
- **Agave**: latest release v4.3.0 · running 4.3.0 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

### Latest ecosystem news (solana.com)

- [Solana Foundation Launches Solana DvP, an Atomic Settlement Program Built for Financial Institutions](https://solana.com/news/solana-foundation-launches-solana-dv-p-an-atomic-settlement-program-built-for-financial-institutions) — Tue, 06 Oct 2026
- [Solana x AI: The Democratization Layer](https://solana.com/news/solana-ai-the-democratization-layer) — Fri, 02 Oct 2026
- [Solana Changelog: October 1, 2026](https://solana.com/news/solana-changelog-october-1-2026) — Thu, 01 Oct 2026
- [Open USD Is Live on Solana](https://solana.com/news/open-usd-is-live-on-solana) — Wed, 30 Sep 2026
- [Slot Time Reduction Effects](https://solana.com/news/slot-time-reduction-effects) — Mon, 28 Sep 2026
- [Solana Changelog: September 24, 2026](https://solana.com/news/solana-changelog-september-24-2026) — Thu, 24 Sep 2026

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 9216 ms |
| solana_rpc_validators | OK | 350 ms |
| coingecko | OK | 1638 ms |
| defillama_tvl | OK | 103 ms |
| defillama_dex | OK | 835 ms |
| defillama_fees | OK | 3188 ms |
| defillama_stablecoins | OK | 838 ms |
| defillama_xstocks | OK | 182 ms |
| jito_kobe | OK | 297 ms |
| stakewiz | OK | 816 ms |
| github | OK | 842 ms |
| solana_com_news | OK | 125 ms |
| sentiment | OK | 2250 ms |
| solana_status_page | OK | 491 ms |
| solana_rpc_whales | OK | 1285 ms |
| solana_rpc_programs | OK | 2249 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*