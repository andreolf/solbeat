# Solbeat — State of the Solana Network

> Generated 2026-10-22T22:02:00Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1065 is 27% complete (~18h remaining), with the cluster processing ~1,652 TPS (1,652 non-vote). Measured slot time is 211ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $877.1K of Real Economic Value over the last 24h ($609/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $103.58 (-4.1% / 24h). Decentralization: Nakamoto coefficient 18, 655 active validators, 0.3% of stake delinquent. Alpenglow readiness: validators holding 99% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: all clear across every monitored metric.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 460,197,449 |
| Block height | 438,229,803 |
| Epoch | 1065 (27.19% complete, ~18.4h left) |
| TPS (10 min avg) | 1,652 |
| Non-vote TPS | 1,652 |
| Slot time (measured) | 211.0 ms |
| Confirmation time (measured) | 0.21 s |
| Finality time (measured) | 0.21 s — **Alpenglow active** |
| Est. daily transactions | 224,747,892 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0033 |
| Node version | 4.3.2 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $103.58 (-4.1%/24h) |
| Market cap | $61.1B |
| **REV (24h)** | **$877.1K** (fees $732.1K + Jito tips $145.0K) |
| Chain TVL | $5.8B |
| Stablecoin supply | $16.1B |
| DEX volume (24h) | $2.3B (-6.9%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 589,653,486 SOL |
| Inflation | 3.59% |

Top DEXs by 24h volume: BisonFi ($380.5M), PumpSwap ($293.4M), Orca DEX ($240.8M), Tessera V ($191.5M), Raydium AMM ($161.4M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 655 / 21 |
| Delinquent stake | 0.33% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.4% |
| Avg / median commission | 12.9% / 5% |
| Alpenglow BLS-key readiness | 711 validators, 99.4% of stake |

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

All clear — no anomalies across monitored metrics.

## Solana Pulse — sentiment (experimental)

**65/100 — Bullish** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 84.8 |
| fear greed | 68 |
| momentum | 43.4 |
| news | 66 |

Crypto Fear & Greed: 68 (Greed) · CoinGecko votes bullish: 84.85% · headline tone (48h): +2

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 1,500 |
| Raydium AMM v4 | 756 |
| Orca Whirlpool | 1,500 |
| Pump.fun | 1,500 |
| Tensor | 3 |
| Magic Eden v2 | 60 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 11,175,975 |
| Binance (cold) | 1,467,047 |
| OKX (attributed) | 330,778 |
| Coinbase (hot) | 7,854 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 211ms · proposal merged.
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
| solana_rpc | OK | 10104 ms |
| solana_rpc_validators | OK | 316 ms |
| coingecko | OK | 1695 ms |
| defillama_tvl | OK | 139 ms |
| defillama_dex | OK | 96 ms |
| defillama_fees | OK | 901 ms |
| defillama_stablecoins | OK | 675 ms |
| defillama_xstocks | FAILED | 658 ms |
| jito_kobe | OK | 242 ms |
| stakewiz | OK | 1339 ms |
| github | OK | 865 ms |
| solana_com_news | OK | 142 ms |
| sentiment | OK | 2272 ms |
| solana_status_page | OK | 202 ms |
| solana_rpc_whales | OK | 1087 ms |
| solana_rpc_programs | OK | 2000 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*