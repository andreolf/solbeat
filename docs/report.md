# Solbeat — State of the Solana Network

> Generated 2026-10-13T08:06:53Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1056 is 41% complete (~15h remaining), with the cluster processing ~4,340 TPS (1,283 non-vote). Measured slot time is 218ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $1.0M of Real Economic Value over the last 24h ($725/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $108.49 (-3.3% / 24h). Decentralization: Nakamoto coefficient 18, 672 active validators, 0.0% of stake delinquent. Alpenglow readiness: validators holding 99% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: all clear across every monitored metric.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 456,370,225 |
| Block height | 434,406,833 |
| Epoch | 1056 (41.26% complete, ~15.4h left) |
| TPS (10 min avg) | 4,340 |
| Non-vote TPS | 1,283 |
| Slot time (measured) | 218.4 ms |
| Est. daily transactions | 396,434,422 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0063 |
| Node version | 4.3.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $108.49 (-3.3%/24h) |
| Market cap | $63.9B |
| **REV (24h)** | **$1.0M** (fees $830.2K + Jito tips $214.4K) |
| Chain TVL | $6.1B |
| Stablecoin supply | $16.2B |
| DEX volume (24h) | $1.9B (46.2%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 589,162,884 SOL |
| Inflation | 3.6% |

Top DEXs by 24h volume: PumpSwap ($411.9M), Orca DEX ($297.4M), Raydium AMM ($173.9M), BisonFi ($163.2M), pump.fun ($160.8M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 672 / 8 |
| Delinquent stake | 0.01% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.6% |
| Avg / median commission | 12.8% / 5.0% |
| Alpenglow BLS-key readiness | 707 validators, 99.4% of stake |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L43ZWjwCHART3o…` | 17,789,243 | 4.05% | 7% |
| 2 | `he1iusunGwqrNtafDtLd…` | 15,958,932 | 3.64% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5…` | 12,305,752 | 2.8% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxb…` | 11,149,129 | 2.54% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxA…` | 10,758,268 | 2.45% | 5% |
| 6 | `51JBzSTU5rAM8gLAVQKg…` | 9,401,788 | 2.14% | 10% |
| 7 | `26pV97Ce83ZQ6Kz9XT4t…` | 9,237,163 | 2.11% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2Fp…` | 7,681,229 | 1.75% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJn…` | 6,812,456 | 1.55% | 5% |
| 10 | `3JD3jMmnR6g88qff2WZ3…` | 6,638,148 | 1.51% | 0% |

## Signals (anomaly detection)

All clear — no anomalies across monitored metrics.

## Solana Pulse — sentiment (experimental)

**47/100 — Neutral** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| momentum | 47.1 |
## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 181 |
| Raydium AMM v4 | 133 |
| Orca Whirlpool | 181 |
| Pump.fun | 206 |
| Tensor | 0 |
| Magic Eden v2 | 82 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 10,572,652 |
| Binance (cold) | 1,586,129 |
| OKX (attributed) | 308,798 |
| Coinbase (hot) | 35,237 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 218ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 99.4% of stake.
- **Agave**: latest release v4.3.0 · running 4.3.0 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

### Latest ecosystem news (solana.com)

- [Payments on Solana: September 2026 in Five Stories](https://solana.com/news/payments-on-solana-september-2026-in-five-stories) — Fri, 09 Oct 2026
- [Breakpoint 2026: Booked Breakpoint? Let's Get You Prepped (Part 2)](https://solana.com/news/breakpoint-guide-part2) — Thu, 08 Oct 2026
- [Solana Changelog: October 8, 2026](https://solana.com/news/solana-changelog-october-8-2026) — Thu, 08 Oct 2026
- [Samsung Partners with Solana to Natively Deliver Stablecoins in Samsung Wallet to 82 Million U.S. Galaxy Devices](https://solana.com/news/samsung-wallet) — Wed, 07 Oct 2026
- [Solana Ecosystem Roundup: September 2026](https://solana.com/news/solana-ecosystem-roundup-september-2026) — Tue, 06 Oct 2026
- [Solana Foundation Launches Solana DvP, an Atomic Settlement Program Built for Financial Institutions](https://solana.com/news/solana-foundation-launches-solana-dv-p-an-atomic-settlement-program-built-for-financial-institutions) — Tue, 06 Oct 2026

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 8242 ms |
| solana_rpc_validators | OK | 115 ms |
| coingecko | OK | 1619 ms |
| defillama_tvl | OK | 75 ms |
| defillama_dex | OK | 59 ms |
| defillama_fees | OK | 106 ms |
| defillama_stablecoins | OK | 103 ms |
| defillama_xstocks | OK | 36 ms |
| jito_kobe | OK | 180 ms |
| stakewiz | OK | 899 ms |
| github | OK | 613 ms |
| solana_com_news | OK | 61 ms |
| sentiment | FAILED | 8021 ms |
| solana_status_page | OK | 210 ms |
| solana_rpc_whales | OK | 862 ms |
| solana_rpc_programs | OK | 1398 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*