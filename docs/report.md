# Solbeat — State of the Solana Network

> Generated 2026-08-31T20:15:08Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1026 is 2% complete (~37h remaining), with the cluster processing ~4,063 TPS (1,919 non-vote). Measured slot time is 316ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $857.2K of Real Economic Value over the last 24h ($595/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $103.69 (-2.0% / 24h). Decentralization: Nakamoto coefficient 18, 680 active validators, 0.0% of stake delinquent. Alpenglow readiness: validators holding 99% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 3 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 443,239,605 |
| Block height | 421,287,238 |
| Epoch | 1026 (1.76% complete, ~37.3h left) |
| TPS (10 min avg) | 4,063 |
| Non-vote TPS | 1,919 |
| Slot time (measured) | 316.0 ms |
| Est. daily transactions | 379,199,847 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0035 |
| Node version | 4.3.0-beta.2 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $103.69 (-2.0%/24h) |
| Market cap | $60.7B |
| **REV (24h)** | **$857.2K** (fees $677.1K + Jito tips $180.1K) |
| Chain TVL | $5.8B |
| Stablecoin supply | $16.1B |
| DEX volume (24h) | $1.9B (15.5%/1d) |
| Tokenized equities (xStocks TVL) | $440.3M |
| Circulating supply | 585,207,307 SOL |
| Inflation | 3.67% |

Top DEXs by 24h volume: PumpSwap ($732.1M), Orca DEX ($274.3M), BisonFi ($184.5M), Meteora DLMM ($142.7M), Raydium AMM ($136.8M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 680 / 14 |
| Delinquent stake | 0.01% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.2% |
| Avg / median commission | 12.2% / 5.0% |
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

- **[WARNING]** SOL price surge (z=+2.5 vs its recent baseline)
- **[WARNING]** Solana TVL surge (z=+2.9 vs its recent baseline)
- **[WARNING · market_move]** Market-wide move: SOL price anomaly accompanied by liquidity/volume shifts — an ecosystem-level repricing rather than an isolated metric.

## Solana Pulse — sentiment (experimental)

**70/100 — Bullish** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 67.3 |
| fear greed | 62 |
| momentum | 66.9 |
| news | 95 |

Crypto Fear & Greed: 62 (Greed) · CoinGecko votes bullish: 67.27% · headline tone (48h): +6

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 116 |
| Raydium AMM v4 | 116 |
| Orca Whirlpool | 116 |
| Pump.fun | 136 |
| Tensor | 1 |
| Magic Eden v2 | 54 |
| Marinade | 1 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,188,448 |
| Binance (cold) | 1,786,717 |
| OKX (attributed) | 330,927 |
| Coinbase (hot) | 33,430 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 316ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 99.3% of stake.
- **Agave**: latest release v4.2.2 · running 4.3.0-beta.2 on the polled node.
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
| solana_rpc | OK | 7282 ms |
| solana_rpc_validators | OK | 222 ms |
| coingecko | OK | 1699 ms |
| defillama_tvl | OK | 240 ms |
| defillama_dex | OK | 1118 ms |
| defillama_fees | OK | 61 ms |
| defillama_stablecoins | OK | 93 ms |
| defillama_xstocks | OK | 53 ms |
| jito_kobe | OK | 256 ms |
| stakewiz | OK | 1225 ms |
| github | OK | 760 ms |
| solana_com_news | OK | 68 ms |
| sentiment | OK | 2235 ms |
| solana_status_page | OK | 329 ms |
| solana_rpc_whales | OK | 931 ms |
| solana_rpc_programs | OK | 1779 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*