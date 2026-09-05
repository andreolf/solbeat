# Solbeat — State of the Solana Network

> Generated 2026-09-05T21:17:37Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1029 is 21% complete (~30h remaining), with the cluster processing ~3,310 TPS (1,172 non-vote). Measured slot time is 314ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $615.2K of Real Economic Value over the last 24h ($427/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $103.44 (+1.7% / 24h). Decentralization: Nakamoto coefficient 18, 675 active validators, 0.0% of stake delinquent. Alpenglow readiness: validators holding 99% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 1 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 444,619,991 |
| Block height | 422,664,405 |
| Epoch | 1029 (21.29% complete, ~29.7h left) |
| TPS (10 min avg) | 3,310 |
| Non-vote TPS | 1,172 |
| Slot time (measured) | 314.2 ms |
| Est. daily transactions | 301,418,746 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0045 |
| Node version | 4.2.2 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $103.44 (+1.7%/24h) |
| Market cap | $60.6B |
| **REV (24h)** | **$615.2K** (fees $531.2K + Jito tips $84.0K) |
| Chain TVL | $5.9B |
| Stablecoin supply | $16.5B |
| DEX volume (24h) | $1.9B (-23.5%/1d) |
| Tokenized equities (xStocks TVL) | $450.0M |
| Circulating supply | 585,445,663 SOL |
| Inflation | 3.66% |

Top DEXs by 24h volume: PumpSwap ($310.7M), BisonFi ($251.9M), Meteora DLMM ($180.7M), Manifest Trade ($118.7M), Raydium AMM ($116.9M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 675 / 18 |
| Delinquent stake | 0.02% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.3% |
| Avg / median commission | 12.5% / 5% |
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

- **[WARNING]** Solana TVL surge (z=+2.6 vs its recent baseline)

## Solana Pulse — sentiment (experimental)

**61/100 — Bullish** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 71.7 |
| fear greed | 73 |
| momentum | 37.0 |
| news | 66 |

Crypto Fear & Greed: 73 (Greed) · CoinGecko votes bullish: 71.74% · headline tone (48h): +2

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 128 |
| Raydium AMM v4 | 118 |
| Orca Whirlpool | 118 |
| Pump.fun | 128 |
| Tensor | 1 |
| Magic Eden v2 | 49 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,188,448 |
| Binance (cold) | 1,906,847 |
| OKX (attributed) | 227,994 |
| Coinbase (hot) | 27,198 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 314ms · proposal merged.
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
| solana_rpc | OK | 8110 ms |
| solana_rpc_validators | OK | 96 ms |
| coingecko | OK | 1660 ms |
| defillama_tvl | OK | 67 ms |
| defillama_dex | OK | 809 ms |
| defillama_fees | OK | 740 ms |
| defillama_stablecoins | OK | 212 ms |
| defillama_xstocks | OK | 114 ms |
| jito_kobe | OK | 289 ms |
| stakewiz | OK | 927 ms |
| github | OK | 579 ms |
| solana_com_news | OK | 92 ms |
| sentiment | OK | 2141 ms |
| solana_status_page | OK | 360 ms |
| solana_rpc_whales | OK | 915 ms |
| solana_rpc_programs | OK | 1539 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*