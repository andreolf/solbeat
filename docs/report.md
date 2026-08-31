# Solbeat — State of the Solana Network

> Generated 2026-08-31T18:28:13Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1025 is 97% complete (~1h remaining), with the cluster processing ~4,113 TPS (1,965 non-vote). Measured slot time is 314ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $857.9K of Real Economic Value over the last 24h ($596/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $103.60 (-2.8% / 24h). Decentralization: Nakamoto coefficient 18, 679 active validators, 0.0% of stake delinquent. Alpenglow readiness: validators holding 99% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 1 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 443,219,380 |
| Block height | 421,267,039 |
| Epoch | 1025 (97.08% complete, ~1.1h left) |
| TPS (10 min avg) | 4,113 |
| Non-vote TPS | 1,965 |
| Slot time (measured) | 314.5 ms |
| Est. daily transactions | 396,526,478 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0032 |
| Node version | 4.3.0-beta.2 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $103.60 (-2.8%/24h) |
| Market cap | $60.6B |
| **REV (24h)** | **$857.9K** (fees $677.1K + Jito tips $180.8K) |
| Chain TVL | $5.8B |
| Stablecoin supply | $16.1B |
| DEX volume (24h) | $1.9B (15.5%/1d) |
| Tokenized equities (xStocks TVL) | $440.3M |
| Circulating supply | 585,120,771 SOL |
| Inflation | 3.67% |

Top DEXs by 24h volume: PumpSwap ($732.1M), Orca DEX ($274.3M), BisonFi ($184.5M), Meteora DLMM ($142.7M), Manifest Trade ($130.7M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 679 / 18 |
| Delinquent stake | 0.03% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.3% |
| Avg / median commission | 12.5% / 5% |
| Alpenglow BLS-key readiness | 698 validators, 99.3% of stake |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L43ZWjwCHART3o…` | 17,203,741 | 3.94% | 7% |
| 2 | `he1iusunGwqrNtafDtLd…` | 16,085,807 | 3.68% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5…` | 12,389,824 | 2.83% | 0% |
| 4 | `CatzoSMUkTRidT5DwBxA…` | 11,479,512 | 2.63% | 5% |
| 5 | `8GbwASqdpw4dVcwbWUxb…` | 9,452,658 | 2.16% | 0% |
| 6 | `26pV97Ce83ZQ6Kz9XT4t…` | 9,293,056 | 2.13% | 7% |
| 7 | `51JBzSTU5rAM8gLAVQKg…` | 9,023,631 | 2.06% | 10% |
| 8 | `CvSb7wdQAFpHuSpTYTJn…` | 7,295,972 | 1.67% | 5% |
| 9 | `9QU2QSxhb24FUX3Tu2Fp…` | 7,201,762 | 1.65% | 7% |
| 10 | `DumiCKHVqoCQKD8roLAp…` | 6,589,845 | 1.51% | 0% |

## Signals (anomaly detection)

- **[WARNING]** Solana TVL surge (z=+2.8 vs its recent baseline)

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 120 |
| Raydium AMM v4 | 120 |
| Orca Whirlpool | 120 |
| Pump.fun | 143 |
| Tensor | 0 |
| Magic Eden v2 | 49 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,188,448 |
| Binance (cold) | 1,695,934 |
| OKX (attributed) | 335,571 |
| Coinbase (hot) | 21,852 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 315ms · proposal merged.
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
| solana_rpc | OK | 6802 ms |
| solana_rpc_validators | OK | 218 ms |
| coingecko | OK | 1554 ms |
| defillama_tvl | OK | 37 ms |
| defillama_dex | OK | 37 ms |
| defillama_fees | OK | 81 ms |
| defillama_stablecoins | OK | 223 ms |
| defillama_xstocks | OK | 1610 ms |
| jito_kobe | OK | 222 ms |
| stakewiz | OK | 1041 ms |
| github | OK | 747 ms |
| solana_com_news | OK | 60 ms |
| solana_status_page | OK | 5948 ms |
| solana_rpc_whales | OK | 1039 ms |
| solana_rpc_programs | OK | 1651 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*