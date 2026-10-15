# Solbeat — State of the Solana Network

> Generated 2026-10-15T02:24:48Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1058 is 3% complete (~25h remaining), with the cluster processing ~5,933 TPS (2,856 non-vote). Measured slot time is 218ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $956.0K of Real Economic Value over the last 24h ($664/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $102.82 (-4.3% / 24h). Decentralization: Nakamoto coefficient 18, 672 active validators, 0.0% of stake delinquent. Alpenglow readiness: validators holding 99% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 1 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 457,070,232 |
| Block height | 435,106,170 |
| Epoch | 1058 (3.29% complete, ~25.2h left) |
| TPS (10 min avg) | 5,933 |
| Non-vote TPS | 2,856 |
| Slot time (measured) | 217.5 ms |
| Est. daily transactions | 439,379,241 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0044 |
| Node version | 4.3.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $102.82 (-4.3%/24h) |
| Market cap | $60.6B |
| **REV (24h)** | **$956.0K** (fees $753.1K + Jito tips $202.9K) |
| Chain TVL | $6.0B |
| Stablecoin supply | $16.0B |
| DEX volume (24h) | $2.3B (-9.8%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 589,269,243 SOL |
| Inflation | 3.6% |

Top DEXs by 24h volume: BisonFi ($411.5M), Orca DEX ($292.0M), PumpSwap ($252.5M), Raydium AMM ($171.3M), pump.fun ($164.4M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 672 / 8 |
| Delinquent stake | 0.0% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.5% |
| Avg / median commission | 12.7% / 5.0% |
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

- **[SERIOUS]** TPS spike: 5,933 vs 12h mean 5,049 (z=+3.1)

## Solana Pulse — sentiment (experimental)

**55/100 — Neutral** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 73.3 |
| fear greed | 53 |
| momentum | 31.9 |
| news | 66 |

Crypto Fear & Greed: 53 (Neutral) · CoinGecko votes bullish: 73.33% · headline tone (48h): +2

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 216 |
| Raydium AMM v4 | 216 |
| Orca Whirlpool | 252 |
| Pump.fun | 252 |
| Tensor | 0 |
| Magic Eden v2 | 47 |
| Marinade | 1 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 11,175,972 |
| Binance (cold) | 1,204,436 |
| OKX (attributed) | 308,798 |
| Coinbase (hot) | 121,367 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 218ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 99.4% of stake.
- **Agave**: latest release v4.3.0 · running 4.3.0 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

### Latest ecosystem news (solana.com)

- [More Breakpoint 2026 Speakers Confirmed for London](https://solana.com/news/breakpoint-2026-london-speakers-2) — Mon, 12 Oct 2026
- [Payments on Solana: September 2026 in Five Stories](https://solana.com/news/payments-on-solana-september-2026-in-five-stories) — Fri, 09 Oct 2026
- [Breakpoint 2026: Booked Breakpoint? Let's Get You Prepped (Part 2)](https://solana.com/news/breakpoint-guide-part2) — Thu, 08 Oct 2026
- [Solana Changelog: October 8, 2026](https://solana.com/news/solana-changelog-october-8-2026) — Thu, 08 Oct 2026
- [Samsung Partners with Solana to Natively Deliver Stablecoins in Samsung Wallet to 82 Million U.S. Galaxy Devices](https://solana.com/news/samsung-wallet) — Wed, 07 Oct 2026
- [Solana Ecosystem Roundup: September 2026](https://solana.com/news/solana-ecosystem-roundup-september-2026) — Tue, 06 Oct 2026

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 9496 ms |
| solana_rpc_validators | OK | 333 ms |
| coingecko | OK | 1712 ms |
| defillama_tvl | OK | 967 ms |
| defillama_dex | OK | 872 ms |
| defillama_fees | OK | 3714 ms |
| defillama_stablecoins | OK | 993 ms |
| defillama_xstocks | OK | 2768 ms |
| jito_kobe | OK | 191 ms |
| stakewiz | OK | 1158 ms |
| github | OK | 835 ms |
| solana_com_news | OK | 244 ms |
| sentiment | OK | 2247 ms |
| solana_status_page | OK | 326 ms |
| solana_rpc_whales | OK | 1256 ms |
| solana_rpc_programs | OK | 2579 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*