# Solbeat — State of the Solana Network

> Generated 2026-11-05T07:48:27Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1077 is 84% complete (~4h remaining), with the cluster processing ~1,248 TPS (1,248 non-vote). Measured slot time is 214ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $718.6K of Real Economic Value over the last 24h ($499/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $95.85 (+3.0% / 24h). Decentralization: Nakamoto coefficient 17, 662 active validators, 0.5% of stake delinquent. Alpenglow readiness: validators holding 100% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 1 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 465,626,616 |
| Block height | 443,646,817 |
| Epoch | 1077 (83.94% complete, ~4.1h left) |
| TPS (10 min avg) | 1,248 |
| Non-vote TPS | 1,248 |
| Slot time (measured) | 213.8 ms |
| Confirmation time (measured) | 0.21 s |
| Finality time (measured) | 0.21 s — **Alpenglow active** |
| Est. daily transactions | 123,782,184 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0047 |
| Node version | 4.4.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $95.85 (+3.0%/24h) |
| Market cap | $56.6B |
| **REV (24h)** | **$718.6K** (fees $579.8K + Jito tips $138.9K) |
| Chain TVL | $5.5B |
| Stablecoin supply | $15.1B |
| DEX volume (24h) | $2.2B (18.1%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 590,262,042 SOL |
| Inflation | 3.57% |

Top DEXs by 24h volume: PumpSwap ($315.4M), Orca DEX ($291.0M), BisonFi ($257.1M), Raydium AMM ($216.8M), Tessera V ($154.4M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 662 / 31 |
| Delinquent stake | 0.46% |
| Nakamoto coefficient | 17 |
| Top-10 stake share | 24.7% |
| Avg / median commission | 12.7% / 5.0% |
| Alpenglow BLS-key readiness | 680 validators, 100.0% of stake |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L43ZWjwCHART3o…` | 17,036,631 | 3.93% | 7% |
| 2 | `he1iusunGwqrNtafDtLd…` | 16,710,689 | 3.86% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5…` | 13,012,272 | 3.01% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxb…` | 10,433,406 | 2.41% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxA…` | 9,524,736 | 2.2% | 5% |
| 6 | `51JBzSTU5rAM8gLAVQKg…` | 9,439,186 | 2.18% | 10% |
| 7 | `26pV97Ce83ZQ6Kz9XT4t…` | 9,217,930 | 2.13% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2Fp…` | 7,826,697 | 1.81% | 7% |
| 9 | `DumiCKHVqoCQKD8roLAp…` | 6,981,457 | 1.61% | 0% |
| 10 | `CvSb7wdQAFpHuSpTYTJn…` | 6,980,105 | 1.61% | 5% |

## Signals (anomaly detection)

- **[WARNING]** Stablecoin supply contraction (z=-2.4 vs its recent baseline)

## Solana Pulse — sentiment (experimental)

**62/100 — Bullish** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 80.6 |
| fear greed | 50 |
| momentum | 56.7 |
| news | 58 |

Crypto Fear & Greed: 50 (Neutral) · CoinGecko votes bullish: 80.56% · headline tone (48h): +1

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 778 |
| Raydium AMM v4 | 1,500 |
| Orca Whirlpool | 1,500 |
| Pump.fun | 1,500 |
| Tensor | 0 |
| Magic Eden v2 | 31 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,300,003 |
| Binance (cold) | 66 |
| OKX (attributed) | 346,929 |
| Coinbase (hot) | 26,580 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 214ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 100.0% of stake.
- **Agave**: latest release v4.4.0 · running 4.4.0 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 9337 ms |
| solana_rpc_validators | OK | 165 ms |
| coingecko | OK | 1635 ms |
| defillama_tvl | OK | 72 ms |
| defillama_dex | OK | 850 ms |
| defillama_fees | OK | 814 ms |
| defillama_stablecoins | OK | 64 ms |
| defillama_xstocks | FAILED | 592 ms |
| jito_kobe | OK | 98 ms |
| stakewiz | OK | 986 ms |
| github | OK | 715 ms |
| solana_com_news | FAILED | 117 ms |
| sentiment | OK | 2058 ms |
| solana_status_page | OK | 325 ms |
| solana_rpc_whales | OK | 930 ms |
| solana_rpc_programs | OK | 1734 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*