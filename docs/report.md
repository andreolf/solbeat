# Solbeat — State of the Solana Network

> Generated 2026-09-11T02:57:44Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1032 is 52% complete (~18h remaining), with the cluster processing ~4,348 TPS (2,240 non-vote). Measured slot time is 318ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $872.4K of Real Economic Value over the last 24h ($606/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $99.27 (-2.5% / 24h). Decentralization: Nakamoto coefficient 18, 676 active validators, 0.1% of stake delinquent. Alpenglow readiness: validators holding 99% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 1 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 446,048,790 |
| Block height | 424,092,089 |
| Epoch | 1032 (52.03% complete, ~18.3h left) |
| TPS (10 min avg) | 4,348 |
| Non-vote TPS | 2,240 |
| Slot time (measured) | 318.4 ms |
| Est. daily transactions | 333,260,096 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0047 |
| Node version | 4.2.2 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $99.27 (-2.5%/24h) |
| Market cap | $58.2B |
| **REV (24h)** | **$872.4K** (fees $709.3K + Jito tips $163.1K) |
| Chain TVL | $5.8B |
| Stablecoin supply | $16.3B |
| DEX volume (24h) | $2.9B (-1.7%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 586,537,799 SOL |
| Inflation | 3.65% |

Top DEXs by 24h volume: PumpSwap ($468.1M), BisonFi ($402.8M), Raydium AMM ($376.6M), HumidiFi ($285.6M), Tessera V ($248.0M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 676 / 13 |
| Delinquent stake | 0.08% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.2% |
| Avg / median commission | 12.8% / 5.0% |
| Alpenglow BLS-key readiness | 694 validators, 99.0% of stake |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L43ZWjwCHART3o…` | 17,441,456 | 3.97% | 7% |
| 2 | `he1iusunGwqrNtafDtLd…` | 16,324,959 | 3.72% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5…` | 12,523,951 | 2.85% | 0% |
| 4 | `CatzoSMUkTRidT5DwBxA…` | 11,380,651 | 2.59% | 5% |
| 5 | `8GbwASqdpw4dVcwbWUxb…` | 9,569,332 | 2.18% | 0% |
| 6 | `26pV97Ce83ZQ6Kz9XT4t…` | 9,279,795 | 2.11% | 7% |
| 7 | `51JBzSTU5rAM8gLAVQKg…` | 9,036,257 | 2.06% | 10% |
| 8 | `9QU2QSxhb24FUX3Tu2Fp…` | 7,344,636 | 1.67% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJn…` | 6,880,702 | 1.57% | 5% |
| 10 | `DumiCKHVqoCQKD8roLAp…` | 6,550,397 | 1.49% | 0% |

## Signals (anomaly detection)

- **[WARNING]** TPS spike: 4,348 vs 12h mean 3,842 (z=+2.2)

## Solana Pulse — sentiment (experimental)

**60/100 — Bullish** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 76.1 |
| fear greed | 56 |
| momentum | 44.0 |
| news | 66 |

Crypto Fear & Greed: 56 (Greed) · CoinGecko votes bullish: 76.09% · headline tone (48h): +2

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 127 |
| Raydium AMM v4 | 139 |
| Orca Whirlpool | 127 |
| Pump.fun | 139 |
| Tensor | 5 |
| Magic Eden v2 | 27 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,188,448 |
| Binance (cold) | 1,853,094 |
| OKX (attributed) | 232,174 |
| Coinbase (hot) | 21,221 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 318ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 99.0% of stake.
- **Agave**: latest release v4.2.2 · running 4.2.2 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

### Latest ecosystem news (solana.com)

- [Report: Stablecoins Are Reshaping Remittances](https://solana.com/news/report-stablecoins-are-reshaping-remittances) — Tue, 08 Sep 2026
- [How BitRobot Crowdsources Real-World Data for Embodied AI, with Jonathan Victor](https://solana.com/news/bits-to-bricks-bitrobot-jonathan-victor) — Mon, 07 Sep 2026
- [Solana Ecosystem Roundup: August 2026](https://solana.com/news/solana-ecosystem-roundup-august-2026) — Fri, 04 Sep 2026
- [Payment Channels: 1 Million Payments Per Second](https://solana.com/news/payment-channels-1-million-payments-per-second) — Thu, 03 Sep 2026
- [How to Reclaim Excess SOL After Rent Reduction](https://solana.com/news/how-to-reclaim-excess-sol-after-rent-reduction) — Thu, 03 Sep 2026
- [The Token Supercycle: Everything of Value is Becoming Programmable](https://solana.com/news/the-token-supercycle-oped) — Wed, 02 Sep 2026

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 7927 ms |
| solana_rpc_validators | OK | 178 ms |
| coingecko | OK | 1714 ms |
| defillama_tvl | OK | 40 ms |
| defillama_dex | OK | 414 ms |
| defillama_fees | OK | 294 ms |
| defillama_stablecoins | OK | 60 ms |
| defillama_xstocks | OK | 24 ms |
| jito_kobe | OK | 292 ms |
| stakewiz | OK | 902 ms |
| github | OK | 568 ms |
| solana_com_news | OK | 73 ms |
| sentiment | OK | 2095 ms |
| solana_status_page | OK | 216 ms |
| solana_rpc_whales | OK | 829 ms |
| solana_rpc_programs | OK | 1353 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*