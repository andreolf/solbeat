# Solbeat — State of the Solana Network

> Generated 2026-11-08T20:04:25Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1081 is 12% complete (~23h remaining), with the cluster processing ~1,613 TPS (1,613 non-vote). Measured slot time is 215ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $497.6K of Real Economic Value over the last 24h ($346/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $89.44 (-0.1% / 24h). Decentralization: Nakamoto coefficient 18, 661 active validators, 0.1% of stake delinquent. Alpenglow readiness: validators holding 100% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 2 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 467,042,533 |
| Block height | 445,060,706 |
| Epoch | 1081 (11.7% complete, ~22.8h left) |
| TPS (10 min avg) | 1,613 |
| Non-vote TPS | 1,613 |
| Slot time (measured) | 214.7 ms |
| Confirmation time (measured) | 0.21 s |
| Finality time (measured) | 0.21 s — **Alpenglow active** |
| Est. daily transactions | 134,379,832 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0029 |
| Node version | 4.4.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $89.44 (-0.1%/24h) |
| Market cap | $52.9B |
| **REV (24h)** | **$497.6K** (fees $392.5K + Jito tips $105.0K) |
| Chain TVL | $5.2B |
| Stablecoin supply | $14.9B |
| DEX volume (24h) | $917.4M (-38.0%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 591,093,756 SOL |
| Inflation | 3.57% |

Top DEXs by 24h volume: PumpSwap ($217.3M), pump.fun ($87.5M), BisonFi ($80.2M), Meteora DLMM ($79.2M), Raydium AMM ($78.5M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 661 / 36 |
| Delinquent stake | 0.14% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.6% |
| Avg / median commission | 12.9% / 5% |
| Alpenglow BLS-key readiness | 685 validators, 100.0% of stake |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L43ZWjwCHART3o…` | 17,050,553 | 3.93% | 7% |
| 2 | `he1iusunGwqrNtafDtLd…` | 16,720,131 | 3.85% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5…` | 13,021,912 | 3.0% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxb…` | 10,279,070 | 2.37% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxA…` | 9,553,388 | 2.2% | 5% |
| 6 | `51JBzSTU5rAM8gLAVQKg…` | 9,550,278 | 2.2% | 10% |
| 7 | `26pV97Ce83ZQ6Kz9XT4t…` | 9,222,876 | 2.13% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2Fp…` | 7,775,137 | 1.79% | 7% |
| 9 | `DumiCKHVqoCQKD8roLAp…` | 6,980,319 | 1.61% | 0% |
| 10 | `CvSb7wdQAFpHuSpTYTJn…` | 6,711,284 | 1.55% | 5% |

## Signals (anomaly detection)

- **[WARNING]** Stablecoin supply contraction (z=-2.6 vs its recent baseline)
- **[WARNING]** DEX volume contraction (z=-2.0 vs its recent baseline)

## Solana Pulse — sentiment (experimental)

**40/100 — Bearish** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 56.7 |
| fear greed | 28 |
| momentum | 25.7 |
| news | 58 |

Crypto Fear & Greed: 28 (Fear) · CoinGecko votes bullish: 56.67% · headline tone (48h): +1

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 673 |
| Raydium AMM v4 | 464 |
| Orca Whirlpool | 1,220 |
| Pump.fun | 1,220 |
| Tensor | 0 |
| Magic Eden v2 | 60 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,300,003 |
| Binance (cold) | 66 |
| OKX (attributed) | 97,596 |
| Coinbase (hot) | 28,520 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 215ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 100.0% of stake.
- **Agave**: latest release v4.4.1 · running 4.4.0 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 9849 ms |
| solana_rpc_validators | OK | 326 ms |
| coingecko | OK | 1709 ms |
| defillama_tvl | OK | 87 ms |
| defillama_dex | OK | 1167 ms |
| defillama_fees | OK | 1976 ms |
| defillama_stablecoins | OK | 1335 ms |
| defillama_xstocks | FAILED | 34 ms |
| jito_kobe | OK | 137 ms |
| stakewiz | OK | 1366 ms |
| github | OK | 730 ms |
| solana_com_news | FAILED | 110 ms |
| sentiment | OK | 2358 ms |
| solana_status_page | OK | 226 ms |
| solana_rpc_whales | OK | 1176 ms |
| solana_rpc_programs | OK | 2127 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*