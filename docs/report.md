# Solbeat — State of the Solana Network

> Generated 2026-09-02T00:53:05Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1026 is 77% complete (~9h remaining), with the cluster processing ~3,781 TPS (1,644 non-vote). Measured slot time is 316ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $978.8K of Real Economic Value over the last 24h ($680/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $99.65 (-3.6% / 24h). Decentralization: Nakamoto coefficient 18, 678 active validators, 0.0% of stake delinquent. Alpenglow readiness: validators holding 99% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 2 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 443,564,224 |
| Block height | 421,611,719 |
| Epoch | 1026 (76.9% complete, ~8.8h left) |
| TPS (10 min avg) | 3,781 |
| Non-vote TPS | 1,644 |
| Slot time (measured) | 316.2 ms |
| Est. daily transactions | 361,380,487 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0047 |
| Node version | 4.2.1 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $99.65 (-3.6%/24h) |
| Market cap | $58.3B |
| **REV (24h)** | **$978.8K** (fees $836.3K + Jito tips $142.5K) |
| Chain TVL | $5.7B |
| Stablecoin supply | $15.9B |
| DEX volume (24h) | $2.4B (-5.7%/1d) |
| Tokenized equities (xStocks TVL) | $432.0M |
| Circulating supply | 585,206,354 SOL |
| Inflation | 3.67% |

Top DEXs by 24h volume: PumpSwap ($939.2M), Orca DEX ($219.0M), BisonFi ($204.8M), Raydium AMM ($152.2M), Manifest Trade ($147.2M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 678 / 16 |
| Delinquent stake | 0.04% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.2% |
| Avg / median commission | 12.5% / 5.0% |
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

- **[WARNING]** Solana TVL surge (z=+2.2 vs its recent baseline)
- **[WARNING]** Real Economic Value deviating from its run-history baseline (z=+2.1)

## Solana Pulse — sentiment (experimental)

**66/100 — Bullish** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 72.5 |
| fear greed | 63 |
| momentum | 46.2 |
| news | 95 |

Crypto Fear & Greed: 63 (Greed) · CoinGecko votes bullish: 72.5% · headline tone (48h): +6

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 125 |
| Raydium AMM v4 | 125 |
| Orca Whirlpool | 88 |
| Pump.fun | 136 |
| Tensor | 0 |
| Magic Eden v2 | 88 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,188,448 |
| Binance (cold) | 1,843,442 |
| OKX (attributed) | 182,399 |
| Coinbase (hot) | 22,090 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 316ms · proposal merged.
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
| solana_rpc | OK | 9046 ms |
| solana_rpc_validators | OK | 321 ms |
| coingecko | OK | 1706 ms |
| defillama_tvl | OK | 138 ms |
| defillama_dex | OK | 984 ms |
| defillama_fees | OK | 1678 ms |
| defillama_stablecoins | OK | 207 ms |
| defillama_xstocks | OK | 905 ms |
| jito_kobe | OK | 378 ms |
| stakewiz | OK | 1118 ms |
| github | OK | 781 ms |
| solana_com_news | OK | 272 ms |
| sentiment | OK | 2314 ms |
| solana_status_page | OK | 443 ms |
| solana_rpc_whales | OK | 1126 ms |
| solana_rpc_programs | OK | 2065 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*