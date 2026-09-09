# Solbeat — State of the Solana Network

> Generated 2026-09-09T05:18:22Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1031 is 32% complete (~26h remaining), with the cluster processing ~3,979 TPS (1,856 non-vote). Measured slot time is 317ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $886.8K of Real Economic Value over the last 24h ($616/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $104.58 (+1.3% / 24h). Decentralization: Nakamoto coefficient 18, 676 active validators, 0.0% of stake delinquent. Alpenglow readiness: validators holding 99% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 1 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 445,529,425 |
| Block height | 423,573,244 |
| Epoch | 1031 (31.81% complete, ~25.9h left) |
| TPS (10 min avg) | 3,979 |
| Non-vote TPS | 1,856 |
| Slot time (measured) | 316.9 ms |
| Est. daily transactions | 352,234,989 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0046 |
| Node version | 4.2.2 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $104.58 (+1.3%/24h) |
| Market cap | $61.3B |
| **REV (24h)** | **$886.8K** (fees $772.7K + Jito tips $114.1K) |
| Chain TVL | $6.0B |
| Stablecoin supply | $16.6B |
| DEX volume (24h) | $2.6B (-5.2%/1d) |
| Tokenized equities (xStocks TVL) | $444.4M |
| Circulating supply | 586,250,771 SOL |
| Inflation | 3.66% |

Top DEXs by 24h volume: PumpSwap ($737.1M), Raydium AMM ($346.1M), Meteora DLMM ($237.8M), BisonFi ($204.1M), Tessera V ($149.5M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 676 / 11 |
| Delinquent stake | 0.01% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.2% |
| Avg / median commission | 12.5% / 5.0% |
| Alpenglow BLS-key readiness | 691 validators, 99.0% of stake |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L43ZWjwCHART3o…` | 17,436,766 | 3.98% | 7% |
| 2 | `he1iusunGwqrNtafDtLd…` | 16,345,792 | 3.73% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5…` | 12,527,540 | 2.86% | 0% |
| 4 | `CatzoSMUkTRidT5DwBxA…` | 11,388,333 | 2.6% | 5% |
| 5 | `8GbwASqdpw4dVcwbWUxb…` | 9,566,721 | 2.18% | 0% |
| 6 | `26pV97Ce83ZQ6Kz9XT4t…` | 9,286,723 | 2.12% | 7% |
| 7 | `51JBzSTU5rAM8gLAVQKg…` | 9,027,481 | 2.06% | 10% |
| 8 | `9QU2QSxhb24FUX3Tu2Fp…` | 7,322,728 | 1.67% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJn…` | 6,860,585 | 1.56% | 5% |
| 10 | `DumiCKHVqoCQKD8roLAp…` | 6,604,066 | 1.51% | 0% |

## Signals (anomaly detection)

- **[WARNING]** Solana TVL surge (z=+2.3 vs its recent baseline)

## Solana Pulse — sentiment (experimental)

**67/100 — Bullish** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 75.0 |
| fear greed | 66 |
| momentum | 56.8 |
| news | 74 |

Crypto Fear & Greed: 66 (Greed) · CoinGecko votes bullish: 75.0% · headline tone (48h): +3

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 136 |
| Raydium AMM v4 | 136 |
| Orca Whirlpool | 150 |
| Pump.fun | 167 |
| Tensor | 0 |
| Magic Eden v2 | 58 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,188,448 |
| Binance (cold) | 1,771,353 |
| OKX (attributed) | 211,872 |
| Coinbase (hot) | 33,883 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 317ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 99.0% of stake.
- **Agave**: latest release v4.2.2 · running 4.2.2 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

### Latest ecosystem news (solana.com)

- [Report: Stablecoins Are Reshaping Remittances](https://solana.com/news/report-stablecoins-are-reshaping-remittances) — Tue, 08 Sep 2026
- [How BitRobot Crowdsources Real-World Data for Embodied AI, with Jonathan Victor](https://solana.com/news/bits-to-bricks-bitrobot-jonathan-victor) — Mon, 07 Sep 2026
- [Solana Ecosystem Roundup: August 2026](https://solana.com/news/solana-ecosystem-roundup-august-2026) — Fri, 04 Sep 2026
- [Payment Channels: 1 Million Payments Per Second](https://solana.com/news/payment-channels-1-million-payments-per-second) — Thu, 03 Sep 2026
- [How to Reclaim Excess SOL After Rent Reduction](https://solana.com/news/how-to-reclaim-excess-sol-after-rent-reduction) — Thu, 03 Sep 2026
- [The Token Supercycle: Everything of Value is Becoming Programmable](https://solana.com/news/the-token-supercycle-oped) — Wed, 02 Sep 2026

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 10745 ms |
| solana_rpc_validators | OK | 764 ms |
| coingecko | OK | 1556 ms |
| defillama_tvl | OK | 48 ms |
| defillama_dex | OK | 886 ms |
| defillama_fees | OK | 754 ms |
| defillama_stablecoins | OK | 128 ms |
| defillama_xstocks | OK | 72 ms |
| jito_kobe | OK | 200 ms |
| stakewiz | OK | 1122 ms |
| github | OK | 722 ms |
| solana_com_news | OK | 99 ms |
| sentiment | OK | 1980 ms |
| solana_status_page | OK | 312 ms |
| solana_rpc_whales | OK | 2002 ms |
| solana_rpc_programs | OK | 3252 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*