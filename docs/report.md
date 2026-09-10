# Solbeat — State of the Solana Network

> Generated 2026-09-10T23:27:20Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

The network earned $978.5K of Real Economic Value over the last 24h ($680/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $99.08 (-2.3% / 24h). Alpenglow readiness: validators holding 99% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: all clear across every monitored metric.

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
| SOL price | $99.08 (-2.3%/24h) |
| Market cap | $58.1B |
| **REV (24h)** | **$978.5K** (fees $978.5K + Jito tips n/a) |
| Chain TVL | $5.8B |
| Stablecoin supply | $16.5B |
| DEX volume (24h) | $3.0B (10.7%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 0 SOL |
| Inflation | None% |

Top DEXs by 24h volume: BisonFi ($402.8M), Raydium AMM ($363.3M), PumpSwap ($341.0M), Meteora DLMM ($322.2M), HumidiFi ($285.6M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | None / None |
| Delinquent stake | None% |
| Nakamoto coefficient | None |
| Top-10 stake share | None% |
| Avg / median commission | None% / None% |
| Alpenglow BLS-key readiness | 694 validators, 99.0% of stake |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|

## Signals (anomaly detection)

All clear — no anomalies across monitored metrics.

## Solana Pulse — sentiment (experimental)

**66/100 — Bullish** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 76.1 |
| fear greed | 69 |
| momentum | 52.1 |
| news | 66 |

Crypto Fear & Greed: 69 (Greed) · CoinGecko votes bullish: 76.09% · headline tone (48h): +2

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 127 |
| Raydium AMM v4 | 127 |
| Orca Whirlpool | 139 |
| Pump.fun | 127 |
| Tensor | 0 |
| Magic Eden v2 | 56 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | n/a |
| Binance (cold) | n/a |
| OKX (attributed) | 211,983 |
| Coinbase (hot) | 21,624 |

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
| solana_rpc | FAILED | 66149 ms |
| solana_rpc_validators | FAILED | 66235 ms |
| coingecko | OK | 1670 ms |
| defillama_tvl | OK | 158 ms |
| defillama_dex | OK | 800 ms |
| defillama_fees | OK | 1237 ms |
| defillama_stablecoins | OK | 56 ms |
| defillama_xstocks | OK | 10898 ms |
| jito_kobe | OK | 157 ms |
| stakewiz | OK | 736 ms |
| github | OK | 627 ms |
| solana_com_news | OK | 91 ms |
| sentiment | OK | 2117 ms |
| solana_status_page | OK | 290 ms |
| solana_rpc_whales | OK | 154057 ms |
| solana_rpc_programs | OK | 1395 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*