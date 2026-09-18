# Solbeat — State of the Solana Network

> Generated 2026-09-18T05:05:32Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1036 is 100% complete, with the cluster processing ~4,478 TPS (2,356 non-vote). Measured slot time is 318ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $957.9K of Real Economic Value over the last 24h ($665/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $105.51 (+5.7% / 24h). Decentralization: Nakamoto coefficient 18, 678 active validators, 0.0% of stake delinquent. Alpenglow readiness: validators holding 99% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: all clear across every monitored metric.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 447,983,753 |
| Block height | 426,024,783 |
| Epoch | 1036 (99.94% complete, ~0.0h left) |
| TPS (10 min avg) | 4,478 |
| Non-vote TPS | 2,356 |
| Slot time (measured) | 318.3 ms |
| Est. daily transactions | 358,782,625 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0046 |
| Node version | 4.3.0-rc.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $105.51 (+5.7%/24h) |
| Market cap | $62.0B |
| **REV (24h)** | **$957.9K** (fees $813.1K + Jito tips $144.8K) |
| Chain TVL | $5.9B |
| Stablecoin supply | $15.6B |
| DEX volume (24h) | $2.6B (-8.8%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 587,211,491 SOL |
| Inflation | 3.64% |

Top DEXs by 24h volume: BisonFi ($440.1M), PumpSwap ($329.3M), HumidiFi ($301.8M), Raydium AMM ($289.1M), fomo Wallet ($216.2M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 678 / 12 |
| Delinquent stake | 0.04% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.3% |
| Avg / median commission | 12.5% / 5.0% |
| Alpenglow BLS-key readiness | 699 validators, 99.4% of stake |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L43ZWjwCHART3o…` | 17,767,428 | 4.04% | 7% |
| 2 | `he1iusunGwqrNtafDtLd…` | 16,352,114 | 3.72% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5…` | 12,485,145 | 2.84% | 0% |
| 4 | `CatzoSMUkTRidT5DwBxA…` | 11,383,247 | 2.59% | 5% |
| 5 | `8GbwASqdpw4dVcwbWUxb…` | 9,740,877 | 2.22% | 0% |
| 6 | `26pV97Ce83ZQ6Kz9XT4t…` | 9,256,273 | 2.1% | 7% |
| 7 | `51JBzSTU5rAM8gLAVQKg…` | 9,049,051 | 2.06% | 10% |
| 8 | `9QU2QSxhb24FUX3Tu2Fp…` | 7,386,183 | 1.68% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJn…` | 7,076,306 | 1.61% | 5% |
| 10 | `DumiCKHVqoCQKD8roLAp…` | 6,558,592 | 1.49% | 0% |

## Signals (anomaly detection)

All clear — no anomalies across monitored metrics.

## Solana Pulse — sentiment (experimental)

**63/100 — Bullish** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 72.2 |
| fear greed | 56 |
| momentum | 51.5 |
| news | 82 |

Crypto Fear & Greed: 56 (Greed) · CoinGecko votes bullish: 72.22% · headline tone (48h): +4

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 137 |
| Raydium AMM v4 | 150 |
| Orca Whirlpool | 167 |
| Pump.fun | 167 |
| Tensor | 0 |
| Magic Eden v2 | 68 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,188,448 |
| Binance (cold) | 2,022,652 |
| OKX (attributed) | 235,077 |
| Coinbase (hot) | 30,481 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 318ms · proposal merged.
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
| solana_rpc | OK | 11788 ms |
| solana_rpc_validators | OK | 1219 ms |
| coingecko | OK | 1652 ms |
| defillama_tvl | OK | 107 ms |
| defillama_dex | OK | 902 ms |
| defillama_fees | OK | 1586 ms |
| defillama_stablecoins | OK | 947 ms |
| defillama_xstocks | OK | 69 ms |
| jito_kobe | OK | 515 ms |
| stakewiz | OK | 891 ms |
| github | OK | 786 ms |
| solana_com_news | OK | 135 ms |
| sentiment | OK | 2369 ms |
| solana_status_page | OK | 386 ms |
| solana_rpc_whales | OK | 2880 ms |
| solana_rpc_programs | OK | 5025 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*