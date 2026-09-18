# Solbeat — State of the Solana Network

> Generated 2026-09-18T22:37:00Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1037 is 55% complete (~14h remaining), with the cluster processing ~4,794 TPS (2,257 non-vote). Measured slot time is 265ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $1.1M of Real Economic Value over the last 24h ($737/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $112.96 (+11.6% / 24h). Decentralization: Nakamoto coefficient 18, 676 active validators, 0.0% of stake delinquent. Alpenglow readiness: validators holding 99% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 3 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 448,220,187 |
| Block height | 426,261,078 |
| Epoch | 1037 (54.67% complete, ~14.4h left) |
| TPS (10 min avg) | 4,794 |
| Non-vote TPS | 2,257 |
| Slot time (measured) | 265.3 ms |
| Est. daily transactions | 424,127,912 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0039 |
| Node version | 4.3.0-rc.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $112.96 (+11.6%/24h) |
| Market cap | $66.4B |
| **REV (24h)** | **$1.1M** (fees $813.1K + Jito tips $247.5K) |
| Chain TVL | $6.3B |
| Stablecoin supply | $15.6B |
| DEX volume (24h) | $2.6B (-7.4%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 587,296,760 SOL |
| Inflation | 3.64% |

Top DEXs by 24h volume: Raydium AMM ($420.2M), BisonFi ($378.3M), PumpSwap ($329.3M), HumidiFi ($281.6M), Orca DEX ($235.2M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 676 / 12 |
| Delinquent stake | 0.04% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.3% |
| Avg / median commission | 12.5% / 5.0% |
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

- **[WARNING]** Solana TVL surge (z=+2.5 vs its recent baseline)
- **[WARNING]** SOL moved +11.6% in 24h
- **[WARNING · market_move]** Market-wide move: SOL price anomaly accompanied by liquidity/volume shifts — an ecosystem-level repricing rather than an isolated metric.

## Solana Pulse — sentiment (experimental)

**70/100 — Bullish** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 80.2 |
| fear greed | 56 |
| momentum | 65.9 |
| news | 82 |

Crypto Fear & Greed: 56 (Greed) · CoinGecko votes bullish: 80.22% · headline tone (48h): +4

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 151 |
| Raydium AMM v4 | 151 |
| Orca Whirlpool | 168 |
| Pump.fun | 168 |
| Tensor | 1 |
| Magic Eden v2 | 54 |
| Marinade | 1 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,188,448 |
| Binance (cold) | 2,006,542 |
| OKX (attributed) | 235,077 |
| Coinbase (hot) | 32,036 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 265ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 99.4% of stake.
- **Agave**: latest release v4.2.2 · running 4.3.0-rc.0 on the polled node.
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
| solana_rpc | OK | 8188 ms |
| solana_rpc_validators | OK | 150 ms |
| coingecko | OK | 1680 ms |
| defillama_tvl | OK | 66 ms |
| defillama_dex | OK | 753 ms |
| defillama_fees | OK | 683 ms |
| defillama_stablecoins | OK | 53 ms |
| defillama_xstocks | OK | 528 ms |
| jito_kobe | OK | 186 ms |
| stakewiz | OK | 655 ms |
| github | OK | 536 ms |
| solana_com_news | OK | 208 ms |
| sentiment | OK | 2063 ms |
| solana_status_page | OK | 311 ms |
| solana_rpc_whales | OK | 814 ms |
| solana_rpc_programs | OK | 1372 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*