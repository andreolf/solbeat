# Solbeat — State of the Solana Network

> Generated 2026-11-04T10:04:08Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1076 is 99% complete (~0h remaining), with the cluster processing ~1,121 TPS (1,121 non-vote). Measured slot time is 216ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $590.4K of Real Economic Value over the last 24h ($410/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $92.98 (+0.9% / 24h). Decentralization: Nakamoto coefficient 18, 666 active validators, 0.4% of stake delinquent. Alpenglow readiness: validators holding 100% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 1 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 465,261,600 |
| Block height | 443,282,132 |
| Epoch | 1076 (99.44% complete, ~0.1h left) |
| TPS (10 min avg) | 1,121 |
| Non-vote TPS | 1,121 |
| Slot time (measured) | 216.2 ms |
| Confirmation time (measured) | 0.22 s |
| Finality time (measured) | 0.22 s — **Alpenglow active** |
| Est. daily transactions | 138,389,752 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0035 |
| Node version | 4.4.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $92.98 (+0.9%/24h) |
| Market cap | $54.9B |
| **REV (24h)** | **$590.4K** (fees $479.8K + Jito tips $110.6K) |
| Chain TVL | $5.4B |
| Stablecoin supply | $14.8B |
| DEX volume (24h) | $1.9B (1.1%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 590,206,656 SOL |
| Inflation | 3.57% |

Top DEXs by 24h volume: PumpSwap ($321.8M), BisonFi ($250.5M), Orca DEX ($250.1M), Raydium AMM ($175.2M), Tessera V ($149.8M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 666 / 27 |
| Delinquent stake | 0.42% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.7% |
| Avg / median commission | 12.8% / 5.0% |
| Alpenglow BLS-key readiness | 680 validators, 100.0% of stake |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L43ZWjwCHART3o…` | 17,030,641 | 3.92% | 7% |
| 2 | `he1iusunGwqrNtafDtLd…` | 16,704,340 | 3.84% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5…` | 13,043,664 | 3.0% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxb…` | 10,431,126 | 2.4% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxA…` | 9,561,007 | 2.2% | 5% |
| 6 | `51JBzSTU5rAM8gLAVQKg…` | 9,435,905 | 2.17% | 10% |
| 7 | `26pV97Ce83ZQ6Kz9XT4t…` | 9,232,746 | 2.12% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2Fp…` | 7,814,810 | 1.8% | 7% |
| 9 | `DumiCKHVqoCQKD8roLAp…` | 7,008,986 | 1.61% | 0% |
| 10 | `CvSb7wdQAFpHuSpTYTJn…` | 6,979,031 | 1.61% | 5% |

## Signals (anomaly detection)

- **[SERIOUS]** Stablecoin supply contraction (z=-3.0 vs its recent baseline)

## Solana Pulse — sentiment (experimental)

**49/100 — Neutral** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 66.7 |
| fear greed | 34 |
| momentum | 36.6 |
| news | 66 |

Crypto Fear & Greed: 34 (Fear) · CoinGecko votes bullish: 66.67% · headline tone (48h): +2

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 1,201 |
| Raydium AMM v4 | 462 |
| Orca Whirlpool | 667 |
| Pump.fun | 1,500 |
| Tensor | 0 |
| Magic Eden v2 | 55 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,300,003 |
| Binance (cold) | 65 |
| OKX (attributed) | 339,406 |
| Coinbase (hot) | 24,014 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 216ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 100.0% of stake.
- **Agave**: latest release v4.4.0 · running 4.4.0 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 10148 ms |
| solana_rpc_validators | OK | 607 ms |
| coingecko | OK | 1682 ms |
| defillama_tvl | OK | 903 ms |
| defillama_dex | OK | 996 ms |
| defillama_fees | OK | 1246 ms |
| defillama_stablecoins | OK | 1156 ms |
| defillama_xstocks | FAILED | 39 ms |
| jito_kobe | OK | 617 ms |
| stakewiz | OK | 1177 ms |
| github | OK | 793 ms |
| solana_com_news | FAILED | 123 ms |
| sentiment | OK | 2199 ms |
| solana_status_page | OK | 424 ms |
| solana_rpc_whales | OK | 1146 ms |
| solana_rpc_programs | OK | 2163 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*