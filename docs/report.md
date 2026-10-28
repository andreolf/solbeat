# Solbeat — State of the Solana Network

> Generated 2026-10-28T19:16:21Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1070 is 81% complete (~5h remaining), with the cluster processing ~2,285 TPS (2,285 non-vote). Measured slot time is 215ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $673.4K of Real Economic Value over the last 24h ($468/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $102.08 (+1.1% / 24h). Decentralization: Nakamoto coefficient 18, 661 active validators, 0.9% of stake delinquent. Alpenglow readiness: validators holding 100% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: all clear across every monitored metric.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 462,591,258 |
| Block height | 440,615,691 |
| Epoch | 1070 (81.31% complete, ~4.8h left) |
| TPS (10 min avg) | 2,285 |
| Non-vote TPS | 2,285 |
| Slot time (measured) | 214.8 ms |
| Confirmation time (measured) | 0.21 s |
| Finality time (measured) | 0.21 s — **Alpenglow active** |
| Est. daily transactions | 181,915,738 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0030 |
| Node version | 4.3.2 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $102.08 (+1.1%/24h) |
| Market cap | $60.2B |
| **REV (24h)** | **$673.4K** (fees $538.0K + Jito tips $135.4K) |
| Chain TVL | $5.7B |
| Stablecoin supply | $15.7B |
| DEX volume (24h) | $1.6B (-23.6%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 589,928,263 SOL |
| Inflation | 3.58% |

Top DEXs by 24h volume: PumpSwap ($193.3M), BisonFi ($191.2M), Manifest Trade ($178.1M), Orca DEX ($161.9M), Tessera V ($142.3M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 661 / 30 |
| Delinquent stake | 0.89% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.6% |
| Avg / median commission | 13.0% / 5% |
| Alpenglow BLS-key readiness | 675 validators, 100.0% of stake |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L43ZWjwCHART3o…` | 17,006,422 | 3.89% | 7% |
| 2 | `he1iusunGwqrNtafDtLd…` | 16,661,096 | 3.81% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5…` | 12,791,931 | 2.93% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxb…` | 10,815,143 | 2.47% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxA…` | 9,718,548 | 2.22% | 5% |
| 6 | `51JBzSTU5rAM8gLAVQKg…` | 9,464,443 | 2.16% | 10% |
| 7 | `26pV97Ce83ZQ6Kz9XT4t…` | 9,208,877 | 2.11% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2Fp…` | 7,757,994 | 1.77% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJn…` | 7,041,146 | 1.61% | 5% |
| 10 | `DumiCKHVqoCQKD8roLAp…` | 6,997,044 | 1.6% | 0% |

## Signals (anomaly detection)

All clear — no anomalies across monitored metrics.

## Solana Pulse — sentiment (experimental)

**55/100 — Neutral** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 70.4 |
| fear greed | 51 |
| momentum | 29.1 |
| news | 82 |

Crypto Fear & Greed: 51 (Neutral) · CoinGecko votes bullish: 70.37% · headline tone (48h): +4

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 921 |
| Raydium AMM v4 | 570 |
| Orca Whirlpool | 570 |
| Pump.fun | 1,500 |
| Tensor | 0 |
| Magic Eden v2 | 49 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 11,175,975 |
| Binance (cold) | 1,559,168 |
| OKX (attributed) | 330,877 |
| Coinbase (hot) | 1,704 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 215ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 100.0% of stake.
- **Agave**: latest release v4.3.2 · running 4.3.2 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 10066 ms |
| solana_rpc_validators | OK | 208 ms |
| coingecko | OK | 1756 ms |
| defillama_tvl | OK | 139 ms |
| defillama_dex | OK | 83 ms |
| defillama_fees | OK | 130 ms |
| defillama_stablecoins | OK | 344 ms |
| defillama_xstocks | FAILED | 814 ms |
| jito_kobe | OK | 190 ms |
| stakewiz | OK | 1314 ms |
| github | OK | 993 ms |
| solana_com_news | FAILED | 121 ms |
| sentiment | OK | 2304 ms |
| solana_status_page | OK | 245 ms |
| solana_rpc_whales | OK | 1006 ms |
| solana_rpc_programs | OK | 2061 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*