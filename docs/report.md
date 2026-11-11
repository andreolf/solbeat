# Solbeat — State of the Solana Network

> Generated 2026-11-11T23:16:20Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1084 is 4% complete (~25h remaining), with the cluster processing ~2,825 TPS (2,825 non-vote). Measured slot time is 215ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $560.3K of Real Economic Value over the last 24h ($389/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $82.35 (-0.6% / 24h). Decentralization: Nakamoto coefficient 18, 661 active validators, 0.2% of stake delinquent. Alpenglow readiness: validators holding 100% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 2 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 468,304,208 |
| Block height | 446,320,203 |
| Epoch | 1084 (3.75% complete, ~24.8h left) |
| TPS (10 min avg) | 2,825 |
| Non-vote TPS | 2,825 |
| Slot time (measured) | 215.1 ms |
| Confirmation time (measured) | 0.22 s |
| Finality time (measured) | 0.22 s — **Alpenglow active** |
| Est. daily transactions | 218,837,481 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0020 |
| Node version | 4.4.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $82.35 (-0.6%/24h) |
| Market cap | $48.7B |
| **REV (24h)** | **$560.3K** (fees $444.5K + Jito tips $115.8K) |
| Chain TVL | $5.1B |
| Stablecoin supply | $14.2B |
| DEX volume (24h) | $1.3B (-9.8%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 591,457,253 SOL |
| Inflation | 3.56% |

Top DEXs by 24h volume: Orca DEX ($184.4M), BisonFi ($152.6M), Raydium AMM ($130.0M), Meteora DLMM ($129.4M), Manifest Trade ($95.9M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 661 / 37 |
| Delinquent stake | 0.16% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.5% |
| Avg / median commission | 12.7% / 5% |
| Alpenglow BLS-key readiness | 686 validators, 100.0% of stake |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `he1iusunGwqrNtafDtLd…` | 16,789,054 | 3.87% | 0% |
| 2 | `CcaHc2L43ZWjwCHART3o…` | 16,119,194 | 3.72% | 7% |
| 3 | `3N7s9zXMZ4QqvHQR15t5…` | 13,026,247 | 3.01% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxb…` | 10,116,092 | 2.33% | 0% |
| 5 | `51JBzSTU5rAM8gLAVQKg…` | 9,681,376 | 2.23% | 10% |
| 6 | `CatzoSMUkTRidT5DwBxA…` | 9,580,180 | 2.21% | 5% |
| 7 | `26pV97Ce83ZQ6Kz9XT4t…` | 9,230,504 | 2.13% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2Fp…` | 7,840,792 | 1.81% | 7% |
| 9 | `DumiCKHVqoCQKD8roLAp…` | 6,987,981 | 1.61% | 0% |
| 10 | `CvSb7wdQAFpHuSpTYTJn…` | 6,730,421 | 1.55% | 5% |

## Signals (anomaly detection)

- **[WARNING]** SOL price contraction (z=-2.2 vs its recent baseline)
- **[WARNING]** Stablecoin supply contraction (z=-2.3 vs its recent baseline)

## Solana Pulse — sentiment (experimental)

**51/100 — Neutral** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 79.1 |
| fear greed | 29 |
| momentum | 25.9 |
| news | 82 |

Crypto Fear & Greed: 29 (Fear) · CoinGecko votes bullish: 79.07% · headline tone (48h): +4

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 1,500 |
| Raydium AMM v4 | 1,500 |
| Orca Whirlpool | 1,500 |
| Pump.fun | 1,500 |
| Tensor | 0 |
| Magic Eden v2 | 557 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,300,003 |
| Binance (cold) | 66 |
| OKX (attributed) | 97,546 |
| Coinbase (hot) | 19,639 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 215ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 100.0% of stake.
- **Agave**: latest release v4.4.1 · running 4.4.0 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 10269 ms |
| solana_rpc_validators | OK | 275 ms |
| coingecko | OK | 1776 ms |
| defillama_tvl | OK | 631 ms |
| defillama_dex | OK | 1010 ms |
| defillama_fees | OK | 1820 ms |
| defillama_stablecoins | OK | 456 ms |
| defillama_xstocks | FAILED | 77 ms |
| jito_kobe | OK | 253 ms |
| stakewiz | OK | 1226 ms |
| github | OK | 957 ms |
| solana_com_news | FAILED | 110 ms |
| sentiment | OK | 2215 ms |
| solana_status_page | OK | 425 ms |
| solana_rpc_whales | OK | 1681 ms |
| solana_rpc_programs | OK | 2735 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*