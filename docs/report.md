# Solbeat — State of the Solana Network

> Generated 2026-09-04T01:24:47Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1028 is 5% complete (~36h remaining), with the cluster processing ~3,515 TPS (1,395 non-vote). Measured slot time is 316ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $717.9K of Real Economic Value over the last 24h ($499/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $103.76 (+3.5% / 24h). Decentralization: Nakamoto coefficient 18, 675 active validators, 0.1% of stake delinquent. Alpenglow readiness: validators holding 99% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 3 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 444,118,854 |
| Block height | 422,165,278 |
| Epoch | 1028 (5.29% complete, ~35.9h left) |
| TPS (10 min avg) | 3,515 |
| Non-vote TPS | 1,395 |
| Slot time (measured) | 315.9 ms |
| Est. daily transactions | 323,762,452 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0044 |
| Node version | 4.2.2 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $103.76 (+3.5%/24h) |
| Market cap | $60.7B |
| **REV (24h)** | **$717.9K** (fees $612.6K + Jito tips $105.3K) |
| Chain TVL | $6.0B |
| Stablecoin supply | $16.0B |
| DEX volume (24h) | $2.4B (3.6%/1d) |
| Tokenized equities (xStocks TVL) | $462.1M |
| Circulating supply | 585,360,759 SOL |
| Inflation | 3.66% |

Top DEXs by 24h volume: PumpSwap ($838.7M), Orca DEX ($285.6M), BisonFi ($232.5M), Meteora DLMM ($186.5M), Manifest Trade ($174.6M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 675 / 19 |
| Delinquent stake | 0.07% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.4% |
| Avg / median commission | 12.2% / 5% |
| Alpenglow BLS-key readiness | 689 validators, 99.3% of stake |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L43ZWjwCHART3o…` | 17,393,318 | 3.98% | 7% |
| 2 | `he1iusunGwqrNtafDtLd…` | 16,324,259 | 3.74% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5…` | 12,459,602 | 2.85% | 0% |
| 4 | `CatzoSMUkTRidT5DwBxA…` | 11,379,843 | 2.6% | 5% |
| 5 | `8GbwASqdpw4dVcwbWUxb…` | 9,567,623 | 2.19% | 0% |
| 6 | `26pV97Ce83ZQ6Kz9XT4t…` | 9,278,151 | 2.12% | 7% |
| 7 | `51JBzSTU5rAM8gLAVQKg…` | 9,042,760 | 2.07% | 10% |
| 8 | `9QU2QSxhb24FUX3Tu2Fp…` | 7,376,879 | 1.69% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJn…` | 7,127,366 | 1.63% | 5% |
| 10 | `DumiCKHVqoCQKD8roLAp…` | 6,593,517 | 1.51% | 0% |

## Signals (anomaly detection)

- **[WARNING]** SOL price surge (z=+2.0 vs its recent baseline)
- **[WARNING]** Solana TVL surge (z=+2.8 vs its recent baseline)
- **[WARNING · market_move]** Market-wide move: SOL price anomaly accompanied by liquidity/volume shifts — an ecosystem-level repricing rather than an isolated metric.

## Solana Pulse — sentiment (experimental)

**68/100 — Bullish** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 75.0 |
| fear greed | 74 |
| momentum | 50.4 |
| news | 82 |

Crypto Fear & Greed: 74 (Greed) · CoinGecko votes bullish: 75.0% · headline tone (48h): +4

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 111 |
| Raydium AMM v4 | 143 |
| Orca Whirlpool | 143 |
| Pump.fun | 158 |
| Tensor | 0 |
| Magic Eden v2 | 86 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,188,448 |
| Binance (cold) | 2,011,354 |
| OKX (attributed) | 316,836 |
| Coinbase (hot) | 30,265 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 316ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 99.3% of stake.
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
| solana_rpc | OK | 12672 ms |
| solana_rpc_validators | OK | 1152 ms |
| coingecko | OK | 1696 ms |
| defillama_tvl | OK | 98 ms |
| defillama_dex | OK | 1386 ms |
| defillama_fees | OK | 66 ms |
| defillama_stablecoins | OK | 67 ms |
| defillama_xstocks | OK | 7863 ms |
| jito_kobe | OK | 232 ms |
| stakewiz | OK | 1456 ms |
| github | OK | 764 ms |
| solana_com_news | OK | 51 ms |
| sentiment | OK | 2297 ms |
| solana_status_page | OK | 3157 ms |
| solana_rpc_whales | OK | 2442 ms |
| solana_rpc_programs | OK | 4162 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*