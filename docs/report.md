# Solbeat — State of the Solana Network

> Generated 2026-10-14T12:41:27Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1057 is 50% complete (~13h remaining), with the cluster processing ~5,839 TPS (2,764 non-vote). Measured slot time is 218ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $999.2K of Real Economic Value over the last 24h ($694/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $105.95 (-0.4% / 24h). Decentralization: Nakamoto coefficient 18, 673 active validators, 0.0% of stake delinquent. Alpenglow readiness: validators holding 99% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 1 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 456,842,030 |
| Block height | 434,878,289 |
| Epoch | 1057 (50.47% complete, ~13.0h left) |
| TPS (10 min avg) | 5,839 |
| Non-vote TPS | 2,764 |
| Slot time (measured) | 217.9 ms |
| Est. daily transactions | 396,156,570 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0061 |
| Node version | 4.3.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $105.95 (-0.4%/24h) |
| Market cap | $62.5B |
| **REV (24h)** | **$999.2K** (fees $790.5K + Jito tips $208.7K) |
| Chain TVL | $6.0B |
| Stablecoin supply | $16.3B |
| DEX volume (24h) | $2.5B (11.8%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 589,218,939 SOL |
| Inflation | 3.6% |

Top DEXs by 24h volume: PumpSwap ($451.8M), BisonFi ($411.5M), Orca DEX ($241.7M), pump.fun ($164.4M), Raydium AMM ($145.5M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 673 / 5 |
| Delinquent stake | 0.0% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.6% |
| Avg / median commission | 13.1% / 5% |
| Alpenglow BLS-key readiness | 708 validators, 99.4% of stake |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L43ZWjwCHART3o…` | 17,794,097 | 4.06% | 7% |
| 2 | `he1iusunGwqrNtafDtLd…` | 15,830,160 | 3.61% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5…` | 12,313,027 | 2.81% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxb…` | 11,142,984 | 2.54% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxA…` | 10,763,192 | 2.46% | 5% |
| 6 | `51JBzSTU5rAM8gLAVQKg…` | 9,407,225 | 2.15% | 10% |
| 7 | `26pV97Ce83ZQ6Kz9XT4t…` | 9,240,434 | 2.11% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2Fp…` | 7,700,931 | 1.76% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJn…` | 6,906,931 | 1.58% | 5% |
| 10 | `3JD3jMmnR6g88qff2WZ3…` | 6,638,868 | 1.52% | 0% |

## Signals (anomaly detection)

- **[SERIOUS]** TPS spike: 5,839 vs 12h mean 4,540 (z=+3.6)

## Solana Pulse — sentiment (experimental)

**63/100 — Bullish** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 75.9 |
| fear greed | 62 |
| momentum | 38.5 |
| news | 90 |

Crypto Fear & Greed: 62 (Greed) · CoinGecko votes bullish: 75.86% · headline tone (48h): +5

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 216 |
| Raydium AMM v4 | 189 |
| Orca Whirlpool | 216 |
| Pump.fun | 252 |
| Tensor | 0 |
| Magic Eden v2 | 72 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 11,175,972 |
| Binance (cold) | 1,144,093 |
| OKX (attributed) | 308,798 |
| Coinbase (hot) | 19,895 |

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
| solana_rpc | OK | 9678 ms |
| solana_rpc_validators | OK | 397 ms |
| coingecko | OK | 1753 ms |
| defillama_tvl | OK | 288 ms |
| defillama_dex | OK | 2525 ms |
| defillama_fees | OK | 1586 ms |
| defillama_stablecoins | OK | 622 ms |
| defillama_xstocks | OK | 1316 ms |
| jito_kobe | OK | 626 ms |
| stakewiz | OK | 1257 ms |
| github | OK | 803 ms |
| solana_com_news | OK | 121 ms |
| sentiment | OK | 2321 ms |
| solana_status_page | OK | 417 ms |
| solana_rpc_whales | OK | 1152 ms |
| solana_rpc_programs | OK | 2196 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*