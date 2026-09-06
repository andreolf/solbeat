# Solbeat — State of the Solana Network

> Generated 2026-09-06T16:09:12Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1029 is 71% complete (~11h remaining), with the cluster processing ~3,806 TPS (1,705 non-vote). Measured slot time is 321ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $465.2K of Real Economic Value over the last 24h ($323/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $105.67 (+2.6% / 24h). Decentralization: Nakamoto coefficient 18, 677 active validators, 0.0% of stake delinquent. Alpenglow readiness: validators holding 99% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 4 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 444,834,483 |
| Block height | 422,878,832 |
| Epoch | 1029 (70.95% complete, ~11.2h left) |
| TPS (10 min avg) | 3,806 |
| Non-vote TPS | 1,705 |
| Slot time (measured) | 320.6 ms |
| Est. daily transactions | 326,392,084 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0027 |
| Node version | 4.2.2 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $105.67 (+2.6%/24h) |
| Market cap | $61.9B |
| **REV (24h)** | **$465.2K** (fees $381.1K + Jito tips $84.0K) |
| Chain TVL | $5.9B |
| Stablecoin supply | $16.6B |
| DEX volume (24h) | $2.0B (4.2%/1d) |
| Tokenized equities (xStocks TVL) | $450.3M |
| Circulating supply | 585,445,025 SOL |
| Inflation | 3.66% |

Top DEXs by 24h volume: PumpSwap ($693.2M), BisonFi ($251.9M), Orca DEX ($129.4M), Raydium AMM ($125.3M), Manifest Trade ($123.3M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 677 / 16 |
| Delinquent stake | 0.02% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.3% |
| Avg / median commission | 12.8% / 5% |
| Alpenglow BLS-key readiness | 690 validators, 99.0% of stake |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L43ZWjwCHART3o…` | 17,421,941 | 3.97% | 7% |
| 2 | `he1iusunGwqrNtafDtLd…` | 16,321,581 | 3.72% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5…` | 12,507,097 | 2.85% | 0% |
| 4 | `CatzoSMUkTRidT5DwBxA…` | 11,374,756 | 2.59% | 5% |
| 5 | `8GbwASqdpw4dVcwbWUxb…` | 9,561,892 | 2.18% | 0% |
| 6 | `26pV97Ce83ZQ6Kz9XT4t…` | 9,268,042 | 2.11% | 7% |
| 7 | `51JBzSTU5rAM8gLAVQKg…` | 9,037,668 | 2.06% | 10% |
| 8 | `9QU2QSxhb24FUX3Tu2Fp…` | 7,352,604 | 1.67% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJn…` | 7,128,761 | 1.62% | 5% |
| 10 | `DumiCKHVqoCQKD8roLAp…` | 6,594,606 | 1.5% | 0% |

## Signals (anomaly detection)

- **[WARNING]** SOL price surge (z=+2.0 vs its recent baseline)
- **[WARNING]** Solana TVL surge (z=+2.5 vs its recent baseline)
- **[WARNING]** Real Economic Value deviating from its run-history baseline (z=-2.4)
- **[WARNING · market_move]** Market-wide move: SOL price anomaly accompanied by liquidity/volume shifts — an ecosystem-level repricing rather than an isolated metric.

## Solana Pulse — sentiment (experimental)

**68/100 — Bullish** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 80.4 |
| fear greed | 73 |
| momentum | 56.2 |
| news | 58 |

Crypto Fear & Greed: 73 (Greed) · CoinGecko votes bullish: 80.43% · headline tone (48h): +1

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 126 |
| Raydium AMM v4 | 151 |
| Orca Whirlpool | 151 |
| Pump.fun | 168 |
| Tensor | 0 |
| Magic Eden v2 | 79 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,188,448 |
| Binance (cold) | 1,794,513 |
| OKX (attributed) | 227,994 |
| Coinbase (hot) | 28,357 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 321ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 99.0% of stake.
- **Agave**: latest release v4.2.2 · running 4.2.2 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

### Latest ecosystem news (solana.com)

- [Payment Channels: 1 Million Payments Per Second](https://solana.com/news/payment-channels-1-million-payments-per-second) — Thu, 03 Sep 2026
- [How to Reclaim Excess SOL After Rent Reduction](https://solana.com/news/how-to-reclaim-excess-sol-after-rent-reduction) — Thu, 03 Sep 2026
- [The Token Supercycle: Everything of Value is Becoming Programmable](https://solana.com/news/the-token-supercycle-oped) — Wed, 02 Sep 2026
- [Webinar Recap: Cross-Border Payments in Latin America](https://solana.com/news/webinar-recap-cross-border-payments-in-latin-america) — Tue, 01 Sep 2026
- [Solana Changelog: August 27, 2026](https://solana.com/news/solana-changelog-august-27-2026) — Fri, 28 Aug 2026
- [The Token Supercycle Is Here: Solana Brings Breakpoint 2026 to London](https://solana.com/news/breakpoint-2026-london-speakers) — Thu, 27 Aug 2026

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 12808 ms |
| solana_rpc_validators | OK | 1598 ms |
| coingecko | OK | 1897 ms |
| defillama_tvl | OK | 136 ms |
| defillama_dex | OK | 116 ms |
| defillama_fees | OK | 1282 ms |
| defillama_stablecoins | OK | 381 ms |
| defillama_xstocks | OK | 225 ms |
| jito_kobe | OK | 251 ms |
| stakewiz | OK | 1192 ms |
| github | OK | 879 ms |
| solana_com_news | OK | 172 ms |
| sentiment | OK | 2408 ms |
| solana_status_page | OK | 556 ms |
| solana_rpc_whales | OK | 3170 ms |
| solana_rpc_programs | OK | 5262 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*