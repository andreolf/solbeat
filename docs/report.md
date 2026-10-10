# Solbeat — State of the Solana Network

> Generated 2026-10-10T14:32:31Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1053 is 91% complete (~2h remaining), with the cluster processing ~5,606 TPS (2,562 non-vote). Measured slot time is 221ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $1.1M of Real Economic Value over the last 24h ($751/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $110.26 (-0.1% / 24h). Decentralization: Nakamoto coefficient 18, 675 active validators, 0.0% of stake delinquent. Alpenglow readiness: validators holding 99% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 1 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 455,289,727 |
| Block height | 433,326,937 |
| Epoch | 1053 (91.14% complete, ~2.3h left) |
| TPS (10 min avg) | 5,606 |
| Non-vote TPS | 2,562 |
| Slot time (measured) | 220.6 ms |
| Est. daily transactions | 398,946,208 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0061 |
| Node version | 4.3.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $110.26 (-0.1%/24h) |
| Market cap | $64.9B |
| **REV (24h)** | **$1.1M** (fees $808.7K + Jito tips $272.4K) |
| Chain TVL | $6.2B |
| Stablecoin supply | $16.4B |
| DEX volume (24h) | $2.0B (-25.2%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 588,791,571 SOL |
| Inflation | 3.61% |

Top DEXs by 24h volume: PumpSwap ($389.9M), BisonFi ($258.7M), pump.fun ($175.6M), Orca DEX ($172.9M), Raydium AMM ($116.3M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 675 / 6 |
| Delinquent stake | 0.0% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.6% |
| Avg / median commission | 13.2% / 5% |
| Alpenglow BLS-key readiness | 707 validators, 99.4% of stake |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L43ZWjwCHART3o…` | 17,788,627 | 4.06% | 7% |
| 2 | `he1iusunGwqrNtafDtLd…` | 15,954,195 | 3.64% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5…` | 12,299,759 | 2.81% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxb…` | 11,178,787 | 2.55% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxA…` | 10,972,770 | 2.51% | 5% |
| 6 | `51JBzSTU5rAM8gLAVQKg…` | 9,315,835 | 2.13% | 10% |
| 7 | `26pV97Ce83ZQ6Kz9XT4t…` | 9,251,552 | 2.11% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2Fp…` | 7,589,922 | 1.73% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJn…` | 6,809,494 | 1.56% | 5% |
| 10 | `3JD3jMmnR6g88qff2WZ3…` | 6,692,115 | 1.53% | 0% |

## Signals (anomaly detection)

- **[SERIOUS]** TPS spike: 5,606 vs 12h mean 4,580 (z=+3.1)

## Solana Pulse — sentiment (experimental)

**57/100 — Neutral** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 72.2 |
| fear greed | 64 |
| momentum | 23.2 |
| news | 82 |

Crypto Fear & Greed: 64 (Greed) · CoinGecko votes bullish: 72.22% · headline tone (48h): +4

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 183 |
| Raydium AMM v4 | 183 |
| Orca Whirlpool | 183 |
| Pump.fun | 208 |
| Tensor | 0 |
| Magic Eden v2 | 26 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 10,572,652 |
| Binance (cold) | 1,382,995 |
| OKX (attributed) | 307,250 |
| Coinbase (hot) | 11,621 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 221ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 99.4% of stake.
- **Agave**: latest release v4.3.0 · running 4.3.0 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

### Latest ecosystem news (solana.com)

- [Samsung Partners with Solana to Natively Deliver Stablecoins in Samsung Wallet to 82 Million U.S. Galaxy Devices](https://solana.com/news/samsung-wallet) — Wed, 07 Oct 2026
- [Solana Ecosystem Roundup: September 2026](https://solana.com/news/solana-ecosystem-roundup-september-2026) — Tue, 06 Oct 2026
- [Solana Foundation Launches Solana DvP, an Atomic Settlement Program Built for Financial Institutions](https://solana.com/news/solana-foundation-launches-solana-dv-p-an-atomic-settlement-program-built-for-financial-institutions) — Tue, 06 Oct 2026
- [Introducing Solana Microscope: Program Monitoring and Alerts](https://solana.com/news/solana-microscope) — Mon, 05 Oct 2026
- [Solana x AI: The Democratization Layer](https://solana.com/news/solana-ai-the-democratization-layer) — Fri, 02 Oct 2026
- [Solana Changelog: October 1, 2026](https://solana.com/news/solana-changelog-october-1-2026) — Thu, 01 Oct 2026

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 8531 ms |
| solana_rpc_validators | OK | 306 ms |
| coingecko | OK | 1732 ms |
| defillama_tvl | OK | 144 ms |
| defillama_dex | OK | 932 ms |
| defillama_fees | OK | 1518 ms |
| defillama_stablecoins | OK | 969 ms |
| defillama_xstocks | OK | 61 ms |
| jito_kobe | OK | 143 ms |
| stakewiz | OK | 763 ms |
| github | OK | 808 ms |
| solana_com_news | OK | 216 ms |
| sentiment | OK | 2236 ms |
| solana_status_page | OK | 635 ms |
| solana_rpc_whales | OK | 1210 ms |
| solana_rpc_programs | OK | 1887 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*