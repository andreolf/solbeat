# Solbeat — State of the Solana Network

> Generated 2026-10-21T10:59:38Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1063 is 90% complete (~3h remaining), with the cluster processing ~4,995 TPS (1,899 non-vote). Measured slot time is 215ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $963.2K of Real Economic Value over the last 24h ($669/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $106.53 (+2.3% / 24h). Decentralization: Nakamoto coefficient 18, 668 active validators, 0.0% of stake delinquent. Alpenglow readiness: validators holding 99% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 1 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 459,604,398 |
| Block height | 437,639,194 |
| Epoch | 1063 (89.91% complete, ~2.6h left) |
| TPS (10 min avg) | 4,995 |
| Non-vote TPS | 1,899 |
| Slot time (measured) | 214.6 ms |
| Est. daily transactions | 395,251,904 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0062 |
| Node version | 4.3.2 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $106.53 (+2.3%/24h) |
| Market cap | $62.8B |
| **REV (24h)** | **$963.2K** (fees $799.6K + Jito tips $163.6K) |
| Chain TVL | $6.0B |
| Stablecoin supply | $15.9B |
| DEX volume (24h) | $2.4B (33.7%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 589,548,757 SOL |
| Inflation | 3.59% |

Top DEXs by 24h volume: PumpSwap ($397.0M), BisonFi ($341.0M), Orca DEX ($278.4M), Raydium AMM ($177.0M), pump.fun ($166.4M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 668 / 11 |
| Delinquent stake | 0.0% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.3% |
| Avg / median commission | 13.2% / 5.0% |
| Alpenglow BLS-key readiness | 710 validators, 99.4% of stake |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L43ZWjwCHART3o…` | 17,103,015 | 3.9% | 7% |
| 2 | `he1iusunGwqrNtafDtLd…` | 15,937,532 | 3.63% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5…` | 12,537,315 | 2.86% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxb…` | 10,930,434 | 2.49% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxA…` | 9,717,707 | 2.22% | 5% |
| 6 | `51JBzSTU5rAM8gLAVQKg…` | 9,482,037 | 2.16% | 10% |
| 7 | `26pV97Ce83ZQ6Kz9XT4t…` | 9,253,756 | 2.11% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2Fp…` | 7,792,210 | 1.78% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJn…` | 7,034,138 | 1.6% | 5% |
| 10 | `DumiCKHVqoCQKD8roLAp…` | 7,000,331 | 1.6% | 0% |

## Signals (anomaly detection)

- **[WARNING]** TPS spike: 4,995 vs 12h mean 4,559 (z=+2.1)

## Solana Pulse — sentiment (experimental)

**70/100 — Bullish** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 77.3 |
| fear greed | 63 |
| momentum | 66.6 |
| news | 74 |

Crypto Fear & Greed: 63 (Greed) · CoinGecko votes bullish: 77.27% · headline tone (48h): +3

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 197 |
| Raydium AMM v4 | 174 |
| Orca Whirlpool | 197 |
| Pump.fun | 197 |
| Tensor | 0 |
| Magic Eden v2 | 49 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 11,175,975 |
| Binance (cold) | 1,337,414 |
| OKX (attributed) | 330,778 |
| Coinbase (hot) | 17,761 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 215ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 99.4% of stake.
- **Agave**: latest release v4.3.2 · running 4.3.2 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

### Latest ecosystem news (solana.com)

- [Geo-Aware Leader Schedule](https://solana.com/news/geo-aware-leader-schedule) — Wed, 14 Oct 2026
- [More Breakpoint 2026 Speakers Confirmed for London](https://solana.com/news/breakpoint-2026-london-speakers-2) — Mon, 12 Oct 2026
- [Payments on Solana: September 2026 in Five Stories](https://solana.com/news/payments-on-solana-september-2026-in-five-stories) — Fri, 09 Oct 2026
- [Breakpoint 2026: Booked Breakpoint? Let's Get You Prepped (Part 2)](https://solana.com/news/breakpoint-guide-part2) — Thu, 08 Oct 2026
- [Solana Changelog: October 8, 2026](https://solana.com/news/solana-changelog-october-8-2026) — Thu, 08 Oct 2026
- [Samsung Partners with Solana to Natively Deliver Stablecoins in Samsung Wallet to 82 Million U.S. Galaxy Devices](https://solana.com/news/samsung-wallet) — Wed, 07 Oct 2026

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 7476 ms |
| solana_rpc_validators | OK | 104 ms |
| coingecko | OK | 1691 ms |
| defillama_tvl | OK | 176 ms |
| defillama_dex | OK | 406 ms |
| defillama_fees | OK | 698 ms |
| defillama_stablecoins | OK | 103 ms |
| defillama_xstocks | OK | 36 ms |
| jito_kobe | OK | 190 ms |
| stakewiz | OK | 1015 ms |
| github | OK | 653 ms |
| solana_com_news | OK | 278 ms |
| sentiment | OK | 2073 ms |
| solana_status_page | OK | 321 ms |
| solana_rpc_whales | OK | 898 ms |
| solana_rpc_programs | OK | 1568 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*