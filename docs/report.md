# Solbeat — State of the Solana Network

> Generated 2026-09-11T00:32:49Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

The network earned $978.5K of Real Economic Value over the last 24h ($680/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $98.66 (-2.6% / 24h). Decentralization: Nakamoto coefficient 18, 676 active validators, 0.0% of stake delinquent. Alpenglow readiness: validators holding 99% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: all clear across every monitored metric.

## Network performance

| Metric | Value |
|---|---|
| Health | n/a |
| Slot | 0 |
| Block height | 0 |
| Epoch | None (None% complete, ~?h left) |
| TPS (10 min avg) | 0 |
| Non-vote TPS | 0 |
| Slot time (measured) | None ms |
| Est. daily transactions | 0 |
| Median priority fee | None µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0000 |
| Node version | None |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $98.66 (-2.6%/24h) |
| Market cap | $57.8B |
| **REV (24h)** | **$978.5K** (fees $978.5K + Jito tips n/a) |
| Chain TVL | $5.8B |
| Stablecoin supply | $16.5B |
| DEX volume (24h) | $3.0B (10.7%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 0 SOL |
| Inflation | None% |

Top DEXs by 24h volume: BisonFi ($402.8M), Raydium AMM ($361.8M), PumpSwap ($341.0M), Meteora DLMM ($322.2M), HumidiFi ($285.6M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 676 / 13 |
| Delinquent stake | 0.04% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.2% |
| Avg / median commission | 12.5% / 5.0% |
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

All clear — no anomalies across monitored metrics.

## Solana Pulse — sentiment (experimental)

**64/100 — Bullish** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 75.6 |
| fear greed | 56 |
| momentum | 53.7 |
| news | 74 |

Crypto Fear & Greed: 56 (Greed) · CoinGecko votes bullish: 75.56% · headline tone (48h): +3

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 128 |
| Raydium AMM v4 | 128 |
| Orca Whirlpool | 140 |
| Pump.fun | 154 |
| Tensor | 0 |
| Magic Eden v2 | 54 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,188,448 |
| Binance (cold) | 1,858,168 |
| OKX (attributed) | 232,174 |
| Coinbase (hot) | 22,802 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: tracking · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 99.0% of stake.
- **Agave**: latest release v4.2.2 · running None on the polled node.
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
| solana_rpc | FAILED | 229238 ms |
| solana_rpc_validators | OK | 22746 ms |
| coingecko | OK | 1652 ms |
| defillama_tvl | OK | 305 ms |
| defillama_dex | OK | 28060 ms |
| defillama_fees | OK | 816 ms |
| defillama_stablecoins | OK | 172 ms |
| defillama_xstocks | OK | 21241 ms |
| jito_kobe | OK | 400 ms |
| stakewiz | OK | 720 ms |
| github | OK | 552 ms |
| solana_com_news | OK | 65 ms |
| sentiment | OK | 2085 ms |
| solana_status_page | OK | 262 ms |
| solana_rpc_whales | OK | 1799 ms |
| solana_rpc_programs | OK | 3027 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*