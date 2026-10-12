# Solbeat — State of the Solana Network

> Generated 2026-10-12T20:46:39Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1055 is 98% complete (~0h remaining), with the cluster processing ~4,984 TPS (1,936 non-vote). Measured slot time is 219ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $924.0K of Real Economic Value over the last 24h ($642/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $108.60 (-2.4% / 24h). Decentralization: Nakamoto coefficient 18, 672 active validators, 0.1% of stake delinquent. Alpenglow readiness: validators holding 99% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 1 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 456,183,166 |
| Block height | 434,219,963 |
| Epoch | 1055 (97.96% complete, ~0.5h left) |
| TPS (10 min avg) | 4,984 |
| Non-vote TPS | 1,936 |
| Slot time (measured) | 218.6 ms |
| Est. daily transactions | 487,978,984 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0034 |
| Node version | 4.3.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $108.60 (-2.4%/24h) |
| Market cap | $64.0B |
| **REV (24h)** | **$924.0K** (fees $753.3K + Jito tips $170.6K) |
| Chain TVL | $6.1B |
| Stablecoin supply | $16.3B |
| DEX volume (24h) | $1.3B (-0.7%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 589,106,487 SOL |
| Inflation | 3.61% |

Top DEXs by 24h volume: Orca DEX ($250.9M), BisonFi ($163.2M), pump.fun ($160.8M), Raydium AMM ($160.6M), PumpSwap ($135.5M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 672 / 9 |
| Delinquent stake | 0.05% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.5% |
| Avg / median commission | 13.1% / 5.0% |
| Alpenglow BLS-key readiness | 707 validators, 99.4% of stake |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L43ZWjwCHART3o…` | 17,781,885 | 4.05% | 7% |
| 2 | `he1iusunGwqrNtafDtLd…` | 15,956,122 | 3.64% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5…` | 12,320,023 | 2.81% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxb…` | 11,147,729 | 2.54% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxA…` | 10,755,463 | 2.45% | 5% |
| 6 | `51JBzSTU5rAM8gLAVQKg…` | 9,332,199 | 2.13% | 10% |
| 7 | `26pV97Ce83ZQ6Kz9XT4t…` | 9,248,710 | 2.11% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2Fp…` | 7,607,284 | 1.73% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJn…` | 6,811,094 | 1.55% | 5% |
| 10 | `3JD3jMmnR6g88qff2WZ3…` | 6,422,658 | 1.46% | 0% |

## Signals (anomaly detection)

- **[WARNING]** TPS drop: 4,984 vs 12h mean 5,686 (z=-2.3)

## Solana Pulse — sentiment (experimental)

**61/100 — Bullish** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 85.2 |
| fear greed | 69 |
| momentum | 31.6 |
| news | 58 |

Crypto Fear & Greed: 69 (Greed) · CoinGecko votes bullish: 85.19% · headline tone (48h): +1

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 161 |
| Raydium AMM v4 | 161 |
| Orca Whirlpool | 205 |
| Pump.fun | 205 |
| Tensor | 0 |
| Magic Eden v2 | 67 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 10,572,652 |
| Binance (cold) | 1,629,292 |
| OKX (attributed) | 307,252 |
| Coinbase (hot) | 38,554 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 219ms · proposal merged.
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
| solana_rpc | OK | 6662 ms |
| solana_rpc_validators | OK | 144 ms |
| coingecko | OK | 1899 ms |
| defillama_tvl | OK | 222 ms |
| defillama_dex | OK | 1125 ms |
| defillama_fees | OK | 1024 ms |
| defillama_stablecoins | OK | 342 ms |
| defillama_xstocks | OK | 135 ms |
| jito_kobe | OK | 328 ms |
| stakewiz | OK | 1456 ms |
| github | OK | 1000 ms |
| solana_com_news | OK | 111 ms |
| sentiment | OK | 2444 ms |
| solana_status_page | OK | 465 ms |
| solana_rpc_whales | OK | 927 ms |
| solana_rpc_programs | OK | 1748 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*