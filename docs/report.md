# Solbeat — State of the Solana Network

> Generated 2026-11-08T17:30:42Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1081 is 2% complete (~25h remaining), with the cluster processing ~1,724 TPS (1,724 non-vote). Measured slot time is 214ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $503.8K of Real Economic Value over the last 24h ($350/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $88.97 (-0.7% / 24h). Decentralization: Nakamoto coefficient 18, 661 active validators, 0.1% of stake delinquent. Alpenglow readiness: validators holding 100% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 2 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 466,999,607 |
| Block height | 445,017,824 |
| Epoch | 1081 (1.76% complete, ~25.3h left) |
| TPS (10 min avg) | 1,724 |
| Non-vote TPS | 1,724 |
| Slot time (measured) | 214.2 ms |
| Confirmation time (measured) | 0.21 s |
| Finality time (measured) | 0.21 s — **Alpenglow active** |
| Est. daily transactions | 111,536,590 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0035 |
| Node version | 4.4.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $88.97 (-0.7%/24h) |
| Market cap | $52.6B |
| **REV (24h)** | **$503.8K** (fees $392.5K + Jito tips $111.3K) |
| Chain TVL | $5.2B |
| Stablecoin supply | $14.9B |
| DEX volume (24h) | $917.4M (-38.0%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 591,093,923 SOL |
| Inflation | 3.57% |

Top DEXs by 24h volume: PumpSwap ($217.3M), pump.fun ($87.5M), BisonFi ($80.2M), Raydium AMM ($79.3M), Meteora DLMM ($79.2M)

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

**41/100 — Neutral** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 56.7 |
| fear greed | 28 |
| momentum | 25.2 |
| news | 66 |

Crypto Fear & Greed: 28 (Fear) · CoinGecko votes bullish: 56.67% · headline tone (48h): +2

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 918 |
| Raydium AMM v4 | 413 |
| Orca Whirlpool | 1,500 |
| Pump.fun | 1,500 |
| Tensor | 0 |
| Magic Eden v2 | 85 |
| Marinade | 2 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,300,003 |
| Binance (cold) | 66 |
| OKX (attributed) | 97,596 |
| Coinbase (hot) | 23,585 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 214ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 100.0% of stake.
- **Agave**: latest release v4.4.1 · running 4.4.0 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 9848 ms |
| solana_rpc_validators | OK | 319 ms |
| coingecko | OK | 1754 ms |
| defillama_tvl | OK | 91 ms |
| defillama_dex | OK | 1193 ms |
| defillama_fees | OK | 1984 ms |
| defillama_stablecoins | OK | 120 ms |
| defillama_xstocks | FAILED | 738 ms |
| jito_kobe | OK | 11964 ms |
| stakewiz | OK | 1319 ms |
| github | OK | 646 ms |
| solana_com_news | FAILED | 96 ms |
| sentiment | OK | 2297 ms |
| solana_status_page | OK | 377 ms |
| solana_rpc_whales | OK | 1126 ms |
| solana_rpc_programs | OK | 2113 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*