# Solbeat — State of the Solana Network

> Generated 2026-09-19T02:11:06Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1037 is 66% complete (~11h remaining), with the cluster processing ~4,275 TPS (1,740 non-vote). Measured slot time is 266ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $1.1M of Real Economic Value over the last 24h ($737/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $113.45 (+11.0% / 24h). Decentralization: Nakamoto coefficient 18, 677 active validators, 0.0% of stake delinquent. Alpenglow readiness: validators holding 99% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 3 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 448,268,364 |
| Block height | 426,309,231 |
| Epoch | 1037 (65.83% complete, ~10.9h left) |
| TPS (10 min avg) | 4,275 |
| Non-vote TPS | 1,740 |
| Slot time (measured) | 266.1 ms |
| Est. daily transactions | 396,950,175 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0046 |
| Node version | 4.3.0-rc.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $113.45 (+11.0%/24h) |
| Market cap | $66.6B |
| **REV (24h)** | **$1.1M** (fees $813.1K + Jito tips $247.8K) |
| Chain TVL | $6.4B |
| Stablecoin supply | $15.8B |
| DEX volume (24h) | $3.1B (19.5%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 587,296,612 SOL |
| Inflation | 3.64% |

Top DEXs by 24h volume: Raydium AMM ($430.5M), BisonFi ($378.3M), Orca DEX ($354.5M), PumpSwap ($329.3M), HumidiFi ($281.6M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 677 / 11 |
| Delinquent stake | 0.04% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.3% |
| Avg / median commission | 12.5% / 5% |
| Alpenglow BLS-key readiness | 699 validators, 99.4% of stake |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L43ZWjwCHART3o…` | 17,815,472 | 4.05% | 7% |
| 2 | `he1iusunGwqrNtafDtLd…` | 15,816,148 | 3.6% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5…` | 12,510,308 | 2.85% | 0% |
| 4 | `CatzoSMUkTRidT5DwBxA…` | 11,398,202 | 2.59% | 5% |
| 5 | `8GbwASqdpw4dVcwbWUxb…` | 9,784,908 | 2.23% | 0% |
| 6 | `26pV97Ce83ZQ6Kz9XT4t…` | 9,254,526 | 2.11% | 7% |
| 7 | `51JBzSTU5rAM8gLAVQKg…` | 9,077,527 | 2.06% | 10% |
| 8 | `9QU2QSxhb24FUX3Tu2Fp…` | 7,397,869 | 1.68% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJn…` | 7,085,578 | 1.61% | 5% |
| 10 | `DumiCKHVqoCQKD8roLAp…` | 6,557,940 | 1.49% | 0% |

## Signals (anomaly detection)

- **[WARNING]** Solana TVL surge (z=+2.6 vs its recent baseline)
- **[WARNING]** SOL moved +11.0% in 24h
- **[WARNING · market_move]** Market-wide move: SOL price anomaly accompanied by liquidity/volume shifts — an ecosystem-level repricing rather than an isolated metric.

## Solana Pulse — sentiment (experimental)

**80/100 — Bullish** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| momentum | 79.7 |
## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 161 |
| Raydium AMM v4 | 161 |
| Orca Whirlpool | 161 |
| Pump.fun | 205 |
| Tensor | 0 |
| Magic Eden v2 | 78 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,188,448 |
| Binance (cold) | 2,008,964 |
| OKX (attributed) | 235,077 |
| Coinbase (hot) | 32,021 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 266ms.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 99.4% of stake.
- **Agave**: latest release None · running 4.3.0-rc.0 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

### Latest ecosystem news (solana.com)

- [Project Harmonia Brings Institutional Tokenized Funds to Solana](https://solana.com/news/project-harmonia-brings-institutional-tokenized-funds-to-solana) — Wed, 16 Sep 2026
- [Solana: Building, Proving and Earning Trust in Public](https://solana.com/news/solana-building-trust-in-public) — Mon, 14 Sep 2026
- [Solana Changelog: September 10, 2026](https://solana.com/news/solana-changelog-september-10-2026) — Thu, 10 Sep 2026
- [Solana Changelog: September 3, 2026](https://solana.com/news/solana-changelog-september-3-2026) — Thu, 10 Sep 2026
- [Report: Stablecoins Are Reshaping Remittances](https://solana.com/news/report-stablecoins-are-reshaping-remittances) — Tue, 08 Sep 2026
- [How BitRobot Crowdsources Real-World Data for Embodied AI, with Jonathan Victor](https://solana.com/news/bits-to-bricks-bitrobot-jonathan-victor) — Mon, 07 Sep 2026

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 10223 ms |
| solana_rpc_validators | OK | 969 ms |
| coingecko | OK | 1888 ms |
| defillama_tvl | OK | 43 ms |
| defillama_dex | OK | 1119 ms |
| defillama_fees | OK | 851 ms |
| defillama_stablecoins | OK | 59 ms |
| defillama_xstocks | OK | 23 ms |
| jito_kobe | OK | 338 ms |
| stakewiz | OK | 1441 ms |
| github | FAILED | 6186 ms |
| solana_com_news | OK | 67 ms |
| sentiment | FAILED | 8293 ms |
| solana_status_page | OK | 365 ms |
| solana_rpc_whales | OK | 1991 ms |
| solana_rpc_programs | OK | 3581 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*