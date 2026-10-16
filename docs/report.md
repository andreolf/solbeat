# Solbeat — State of the Solana Network

> Generated 2026-10-16T01:21:24Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1058 is 92% complete (~2h remaining), with the cluster processing ~6,355 TPS (3,280 non-vote). Measured slot time is 218ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $934.3K of Real Economic Value over the last 24h ($649/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $105.58 (+1.3% / 24h). Decentralization: Nakamoto coefficient 18, 672 active validators, 0.0% of stake delinquent. Alpenglow readiness: validators holding 99% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 1 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 457,452,042 |
| Block height | 435,487,876 |
| Epoch | 1058 (91.68% complete, ~2.2h left) |
| TPS (10 min avg) | 6,355 |
| Non-vote TPS | 3,280 |
| Slot time (measured) | 217.6 ms |
| Est. daily transactions | 442,500,584 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0043 |
| Node version | 4.3.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $105.58 (+1.3%/24h) |
| Market cap | $62.2B |
| **REV (24h)** | **$934.3K** (fees $753.1K + Jito tips $181.2K) |
| Chain TVL | $6.0B |
| Stablecoin supply | $16.2B |
| DEX volume (24h) | $2.4B (13.7%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 589,267,984 SOL |
| Inflation | 3.6% |

Top DEXs by 24h volume: BisonFi ($381.4M), Orca DEX ($380.9M), PumpSwap ($252.5M), Raydium AMM ($241.7M), Meteora DLMM ($166.6M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 672 / 9 |
| Delinquent stake | 0.0% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.5% |
| Avg / median commission | 13.0% / 5.0% |
| Alpenglow BLS-key readiness | 708 validators, 99.4% of stake |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L43ZWjwCHART3o…` | 17,556,681 | 4.01% | 7% |
| 2 | `he1iusunGwqrNtafDtLd…` | 15,475,284 | 3.53% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5…` | 12,340,406 | 2.82% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxb…` | 11,132,168 | 2.54% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxA…` | 10,777,829 | 2.46% | 5% |
| 6 | `51JBzSTU5rAM8gLAVQKg…` | 9,409,309 | 2.15% | 10% |
| 7 | `26pV97Ce83ZQ6Kz9XT4t…` | 9,227,345 | 2.11% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2Fp…` | 7,737,484 | 1.77% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJn…` | 6,912,081 | 1.58% | 5% |
| 10 | `3JD3jMmnR6g88qff2WZ3…` | 6,640,641 | 1.52% | 0% |

## Signals (anomaly detection)

- **[SERIOUS]** TPS spike: 6,355 vs 12h mean 5,063 (z=+3.9)

## Solana Pulse — sentiment (experimental)

**57/100 — Neutral** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 69.2 |
| fear greed | 63 |
| momentum | 47.0 |
| news | 42 |

Crypto Fear & Greed: 63 (Greed) · CoinGecko votes bullish: 69.23% · headline tone (48h): -1

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 165 |
| Raydium AMM v4 | 165 |
| Orca Whirlpool | 186 |
| Pump.fun | 186 |
| Tensor | 0 |
| Magic Eden v2 | 53 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 11,175,972 |
| Binance (cold) | 1,309,210 |
| OKX (attributed) | 308,814 |
| Coinbase (hot) | 57,228 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 218ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 99.4% of stake.
- **Agave**: latest release v4.3.0 · running 4.3.0 on the polled node.
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
| solana_rpc | OK | 7911 ms |
| solana_rpc_validators | OK | 303 ms |
| coingecko | OK | 1796 ms |
| defillama_tvl | OK | 123 ms |
| defillama_dex | OK | 1168 ms |
| defillama_fees | OK | 9005 ms |
| defillama_stablecoins | OK | 149 ms |
| defillama_xstocks | OK | 837 ms |
| jito_kobe | OK | 242 ms |
| stakewiz | OK | 1341 ms |
| github | OK | 682 ms |
| solana_com_news | OK | 121 ms |
| sentiment | OK | 2351 ms |
| solana_status_page | OK | 438 ms |
| solana_rpc_whales | OK | 1146 ms |
| solana_rpc_programs | OK | 2198 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*