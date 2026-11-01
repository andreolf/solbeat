# Solbeat — State of the Solana Network

> Generated 2026-11-01T06:08:05Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1074 is 4% complete (~25h remaining), with the cluster processing ~1,066 TPS (1,066 non-vote). Measured slot time is 214ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $438.8K of Real Economic Value over the last 24h ($305/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $95.73 (-0.3% / 24h). Decentralization: Nakamoto coefficient 18, 661 active validators, 1.4% of stake delinquent. Alpenglow readiness: validators holding 100% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 1 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 463,985,467 |
| Block height | 442,007,044 |
| Epoch | 1074 (4.04% complete, ~24.7h left) |
| TPS (10 min avg) | 1,066 |
| Non-vote TPS | 1,066 |
| Slot time (measured) | 214.3 ms |
| Confirmation time (measured) | 0.21 s |
| Finality time (measured) | 0.21 s — **Alpenglow active** |
| Est. daily transactions | 115,604,282 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0032 |
| Node version | 4.3.2 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $95.73 (-0.3%/24h) |
| Market cap | $56.4B |
| **REV (24h)** | **$438.8K** (fees $364.2K + Jito tips $74.6K) |
| Chain TVL | $5.4B |
| Stablecoin supply | $15.4B |
| DEX volume (24h) | $1.4B (-31.9%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 590,150,530 SOL |
| Inflation | 3.58% |

Top DEXs by 24h volume: BisonFi ($182.9M), Tessera V ($181.4M), PumpSwap ($130.7M), pump.fun ($113.6M), GoonFi ($108.0M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 661 / 35 |
| Delinquent stake | 1.4% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.7% |
| Avg / median commission | 12.7% / 5% |
| Alpenglow BLS-key readiness | 678 validators, 100.0% of stake |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L43ZWjwCHART3o…` | 17,029,196 | 3.92% | 7% |
| 2 | `he1iusunGwqrNtafDtLd…` | 16,695,127 | 3.85% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5…` | 12,943,199 | 2.98% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxb…` | 10,426,987 | 2.4% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxA…` | 9,583,157 | 2.21% | 5% |
| 6 | `51JBzSTU5rAM8gLAVQKg…` | 9,451,197 | 2.18% | 10% |
| 7 | `26pV97Ce83ZQ6Kz9XT4t…` | 9,225,053 | 2.13% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2Fp…` | 7,791,639 | 1.8% | 7% |
| 9 | `DumiCKHVqoCQKD8roLAp…` | 7,001,293 | 1.61% | 0% |
| 10 | `CvSb7wdQAFpHuSpTYTJn…` | 6,977,108 | 1.61% | 5% |

## Signals (anomaly detection)

- **[WARNING]** Real Economic Value deviating from its run-history baseline (z=-2.3)

## Solana Pulse — sentiment (experimental)

**49/100 — Neutral** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 75.9 |
| fear greed | 34 |
| momentum | 23.5 |
| news | 74 |

Crypto Fear & Greed: 34 (Fear) · CoinGecko votes bullish: 75.86% · headline tone (48h): +3

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 914 |
| Raydium AMM v4 | 323 |
| Orca Whirlpool | 568 |
| Pump.fun | 1,500 |
| Tensor | 0 |
| Magic Eden v2 | 76 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 11,890,003 |
| Binance (cold) | 4 |
| OKX (attributed) | 339,500 |
| Coinbase (hot) | 78,193 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 214ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 100.0% of stake.
- **Agave**: latest release v4.4.0 · running 4.3.2 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 9994 ms |
| solana_rpc_validators | OK | 392 ms |
| coingecko | OK | 1737 ms |
| defillama_tvl | OK | 227 ms |
| defillama_dex | OK | 1033 ms |
| defillama_fees | OK | 1228 ms |
| defillama_stablecoins | OK | 260 ms |
| defillama_xstocks | FAILED | 66 ms |
| jito_kobe | OK | 237 ms |
| stakewiz | OK | 1209 ms |
| github | OK | 832 ms |
| solana_com_news | FAILED | 167 ms |
| sentiment | OK | 4047 ms |
| solana_status_page | OK | 277 ms |
| solana_rpc_whales | OK | 1106 ms |
| solana_rpc_programs | OK | 2265 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*