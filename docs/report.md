# Solbeat — State of the Solana Network

> Generated 2026-08-31T21:31:14Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1026 is 5% complete (~36h remaining), with the cluster processing ~4,179 TPS (2,067 non-vote). Measured slot time is 319ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $823.7K of Real Economic Value over the last 24h ($572/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $103.55 (-0.8% / 24h). Decentralization: Nakamoto coefficient 18, 679 active validators, 0.0% of stake delinquent. Alpenglow readiness: validators holding 99% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 4 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 443,253,958 |
| Block height | 421,301,579 |
| Epoch | 1026 (5.08% complete, ~36.4h left) |
| TPS (10 min avg) | 4,179 |
| Non-vote TPS | 2,067 |
| Slot time (measured) | 319.4 ms |
| Est. daily transactions | 370,234,393 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0036 |
| Node version | 4.2.1 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $103.55 (-0.8%/24h) |
| Market cap | $60.6B |
| **REV (24h)** | **$823.7K** (fees $677.1K + Jito tips $146.6K) |
| Chain TVL | $5.9B |
| Stablecoin supply | $16.1B |
| DEX volume (24h) | $1.9B (15.5%/1d) |
| Tokenized equities (xStocks TVL) | $443.1M |
| Circulating supply | 585,207,171 SOL |
| Inflation | 3.67% |

Top DEXs by 24h volume: PumpSwap ($732.1M), Orca DEX ($275.5M), BisonFi ($184.5M), Meteora DLMM ($142.7M), Raydium AMM ($139.2M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 679 / 15 |
| Delinquent stake | 0.03% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.2% |
| Avg / median commission | 12.2% / 5% |
| Alpenglow BLS-key readiness | 698 validators, 99.3% of stake |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L43ZWjwCHART3o…` | 17,174,436 | 3.92% | 7% |
| 2 | `he1iusunGwqrNtafDtLd…` | 16,281,426 | 3.72% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5…` | 12,434,730 | 2.84% | 0% |
| 4 | `CatzoSMUkTRidT5DwBxA…` | 11,480,709 | 2.62% | 5% |
| 5 | `8GbwASqdpw4dVcwbWUxb…` | 9,455,250 | 2.16% | 0% |
| 6 | `26pV97Ce83ZQ6Kz9XT4t…` | 9,285,506 | 2.12% | 7% |
| 7 | `51JBzSTU5rAM8gLAVQKg…` | 9,044,016 | 2.06% | 10% |
| 8 | `9QU2QSxhb24FUX3Tu2Fp…` | 7,216,300 | 1.65% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJn…` | 6,930,213 | 1.58% | 5% |
| 10 | `DumiCKHVqoCQKD8roLAp…` | 6,591,885 | 1.5% | 0% |

## Signals (anomaly detection)

- **[WARNING]** SOL price surge (z=+2.4 vs its recent baseline)
- **[SERIOUS]** Solana TVL surge (z=+3.1 vs its recent baseline)
- **[SERIOUS]** Real Economic Value deviating from its run-history baseline (z=-3.4)
- **[WARNING · market_move]** Market-wide move: SOL price anomaly accompanied by liquidity/volume shifts — an ecosystem-level repricing rather than an isolated metric.

## Solana Pulse — sentiment (experimental)

**70/100 — Bullish** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 66.7 |
| fear greed | 62 |
| momentum | 67.8 |
| news | 95 |

Crypto Fear & Greed: 62 (Greed) · CoinGecko votes bullish: 66.67% · headline tone (48h): +6

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 131 |
| Raydium AMM v4 | 120 |
| Orca Whirlpool | 131 |
| Pump.fun | 144 |
| Tensor | 1 |
| Magic Eden v2 | 77 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,188,448 |
| Binance (cold) | 1,791,499 |
| OKX (attributed) | 329,619 |
| Coinbase (hot) | 32,427 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 319ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 99.3% of stake.
- **Agave**: latest release v4.2.2 · running 4.2.1 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

### Latest ecosystem news (solana.com)

- [The Token Supercycle Is Here: Solana Brings Breakpoint 2026 to London](https://solana.com/news/breakpoint-2026-london-speakers) — Thu, 27 Aug 2026
- [Solana Changelog: August 20, 2026](https://solana.com/news/solana-changelog-august-20-2026) — Mon, 24 Aug 2026
- [Lowering Slot Time and Validators Economic](https://solana.com/news/lowering-slot-time-and-validators-economic) — Wed, 19 Aug 2026
- [Transaction v1 and the ALT Trade-off](https://solana.com/news/transaction-v1-and-the-alt-trade-off) — Mon, 17 Aug 2026
- [Solana Changelog: August 13, 2026](https://solana.com/news/solana-changelog-august-13-2026) — Thu, 13 Aug 2026
- [How Meow Built Agentic Banking and Agent Payment Rails, with Brandon Arvanaghi](https://solana.com/news/how-meow-built-agentic-banking-and-agent-payment-rails-with-brandon-arvanaghi) — Thu, 13 Aug 2026

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 9366 ms |
| solana_rpc_validators | OK | 178 ms |
| coingecko | OK | 1580 ms |
| defillama_tvl | OK | 522 ms |
| defillama_dex | OK | 761 ms |
| defillama_fees | OK | 1571 ms |
| defillama_stablecoins | OK | 77 ms |
| defillama_xstocks | OK | 69 ms |
| jito_kobe | OK | 315 ms |
| stakewiz | OK | 896 ms |
| github | OK | 715 ms |
| solana_com_news | OK | 96 ms |
| sentiment | OK | 2065 ms |
| solana_status_page | OK | 379 ms |
| solana_rpc_whales | OK | 956 ms |
| solana_rpc_programs | OK | 1607 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*