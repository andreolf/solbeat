# Solbeat — State of the Solana Network

> Generated 2026-09-10T12:08:39Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1032 is 13% complete (~33h remaining), with the cluster processing ~3,908 TPS (1,773 non-vote). Measured slot time is 315ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $1.1M of Real Economic Value over the last 24h ($796/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $101.03 (-3.1% / 24h). Decentralization: Nakamoto coefficient 18, 676 active validators, 0.0% of stake delinquent. Alpenglow readiness: validators holding 99% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 1 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 445,880,371 |
| Block height | 423,923,748 |
| Epoch | 1032 (13.05% complete, ~32.9h left) |
| TPS (10 min avg) | 3,908 |
| Non-vote TPS | 1,773 |
| Slot time (measured) | 315.3 ms |
| Est. daily transactions | 310,095,683 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0078 |
| Node version | 4.2.2 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $101.03 (-3.1%/24h) |
| Market cap | $59.2B |
| **REV (24h)** | **$1.1M** (fees $978.5K + Jito tips $167.6K) |
| Chain TVL | $5.8B |
| Stablecoin supply | $16.5B |
| DEX volume (24h) | $3.0B (10.7%/1d) |
| Tokenized equities (xStocks TVL) | $435.6M |
| Circulating supply | 586,335,665 SOL |
| Inflation | 3.65% |

Top DEXs by 24h volume: BisonFi ($402.8M), Raydium AMM ($355.6M), PumpSwap ($341.0M), Meteora DLMM ($322.2M), HumidiFi ($285.6M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 676 / 12 |
| Delinquent stake | 0.02% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.2% |
| Avg / median commission | 12.5% / 5.0% |
| Alpenglow BLS-key readiness | 693 validators, 99.0% of stake |

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

- **[WARNING]** TPS spike: 3,908 vs 12h mean 3,580 (z=+2.1)

## Solana Pulse — sentiment (experimental)

**65/100 — Bullish** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 77.8 |
| fear greed | 69 |
| momentum | 54.8 |
| news | 50 |

Crypto Fear & Greed: 69 (Greed) · CoinGecko votes bullish: 77.78% · headline tone (48h): +0

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 121 |
| Raydium AMM v4 | 132 |
| Orca Whirlpool | 132 |
| Pump.fun | 144 |
| Tensor | 0 |
| Magic Eden v2 | 86 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,188,448 |
| Binance (cold) | 1,838,868 |
| OKX (attributed) | 211,983 |
| Coinbase (hot) | 25,902 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 315ms · proposal merged.
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
| solana_rpc | OK | 12945 ms |
| solana_rpc_validators | OK | 1344 ms |
| coingecko | OK | 1668 ms |
| defillama_tvl | OK | 4088 ms |
| defillama_dex | OK | 876 ms |
| defillama_fees | OK | 1447 ms |
| defillama_stablecoins | OK | 67 ms |
| defillama_xstocks | OK | 71 ms |
| jito_kobe | OK | 282 ms |
| stakewiz | OK | 830 ms |
| github | OK | 677 ms |
| solana_com_news | OK | 147 ms |
| sentiment | OK | 2060 ms |
| solana_status_page | OK | 196 ms |
| solana_rpc_whales | OK | 2820 ms |
| solana_rpc_programs | OK | 5161 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*