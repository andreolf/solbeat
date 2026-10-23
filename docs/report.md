# Solbeat — State of the Solana Network

> Generated 2026-10-23T13:49:19Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1065 is 89% complete (~3h remaining), with the cluster processing ~2,968 TPS (2,968 non-vote). Measured slot time is 213ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $776.3K of Real Economic Value over the last 24h ($539/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $104.71 (+0.1% / 24h). Decentralization: Nakamoto coefficient 18, 654 active validators, 0.4% of stake delinquent. Anomaly scan: 1 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 460,465,950 |
| Block height | 438,498,176 |
| Epoch | 1065 (89.34% complete, ~2.7h left) |
| TPS (10 min avg) | 2,968 |
| Non-vote TPS | 2,968 |
| Slot time (measured) | 212.9 ms |
| Confirmation time (measured) | 0.21 s |
| Finality time (measured) | 0.21 s — **Alpenglow active** |
| Est. daily transactions | 148,584,147 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0042 |
| Node version | 4.3.2 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $104.71 (+0.1%/24h) |
| Market cap | $61.8B |
| **REV (24h)** | **$776.3K** (fees $631.0K + Jito tips $145.3K) |
| Chain TVL | $5.8B |
| Stablecoin supply | $15.9B |
| DEX volume (24h) | $2.0B (-10.2%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 589,653,215 SOL |
| Inflation | 3.59% |

Top DEXs by 24h volume: BisonFi ($312.0M), PumpSwap ($259.0M), Orca DEX ($200.7M), Tessera V ($187.5M), pump.fun ($142.2M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 654 / 22 |
| Delinquent stake | 0.37% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.4% |
| Avg / median commission | 13.2% / 5.0% |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L43ZWjwCHART3o…` | 17,133,144 | 3.91% | 7% |
| 2 | `he1iusunGwqrNtafDtLd…` | 15,968,621 | 3.64% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5…` | 12,556,096 | 2.86% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxb…` | 10,936,237 | 2.5% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxA…` | 9,726,420 | 2.22% | 5% |
| 6 | `51JBzSTU5rAM8gLAVQKg…` | 9,476,174 | 2.16% | 10% |
| 7 | `26pV97Ce83ZQ6Kz9XT4t…` | 9,244,629 | 2.11% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2Fp…` | 7,797,559 | 1.78% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJn…` | 7,036,293 | 1.61% | 5% |
| 10 | `DumiCKHVqoCQKD8roLAp…` | 7,002,101 | 1.6% | 0% |

## Signals (anomaly detection)

- **[SERIOUS]** TPS spike: 2,968 vs 12h mean 1,685 (z=+3.7)

## Solana Pulse — sentiment (experimental)

**43/100 — Neutral** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| momentum | 43.0 |
## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 1,500 |
| Raydium AMM v4 | 790 |
| Orca Whirlpool | 1,500 |
| Pump.fun | 1,500 |
| Tensor | 1 |
| Magic Eden v2 | 37 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 11,175,975 |
| Binance (cold) | 1,487,743 |
| OKX (attributed) | 330,778 |
| Coinbase (hot) | 7,375 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 213ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at ?% of stake.
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
| solana_rpc | OK | 10158 ms |
| solana_rpc_validators | OK | 307 ms |
| coingecko | OK | 1725 ms |
| defillama_tvl | OK | 170 ms |
| defillama_dex | OK | 6103 ms |
| defillama_fees | OK | 1681 ms |
| defillama_stablecoins | OK | 273 ms |
| defillama_xstocks | FAILED | 655 ms |
| jito_kobe | OK | 487 ms |
| stakewiz | FAILED | 574 ms |
| github | OK | 786 ms |
| solana_com_news | OK | 187 ms |
| sentiment | FAILED | 2256 ms |
| solana_status_page | OK | 435 ms |
| solana_rpc_whales | OK | 1174 ms |
| solana_rpc_programs | OK | 1874 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*