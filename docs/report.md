# Solbeat — State of the Solana Network

> Generated 2026-11-25T09:20:05Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1096 is 51% complete (~12h remaining), with the cluster processing ~1,408 TPS (1,408 non-vote). Measured slot time is 215ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $471.3K of Real Economic Value over the last 24h ($327/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $67.66 (-4.5% / 24h). Decentralization: Nakamoto coefficient 18, 659 active validators, 0.1% of stake delinquent. Alpenglow readiness: validators holding 100% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 3 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 473,693,909 |
| Block height | 451,706,988 |
| Epoch | 1096 (51.37% complete, ~12.5h left) |
| TPS (10 min avg) | 1,408 |
| Non-vote TPS | 1,408 |
| Slot time (measured) | 214.9 ms |
| Confirmation time (measured) | 0.43 s |
| Finality time (measured) | 0.43 s — **Alpenglow active** |
| Est. daily transactions | 140,458,254 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0026 |
| Node version | 4.4.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $67.66 (-4.5%/24h) |
| Market cap | $40.0B |
| **REV (24h)** | **$471.3K** (fees $366.0K + Jito tips $105.4K) |
| Chain TVL | $4.5B |
| Stablecoin supply | $13.4B |
| DEX volume (24h) | $1.6B (-8.9%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 592,128,280 SOL |
| Inflation | 3.54% |

Top DEXs by 24h volume: BisonFi ($204.1M), Orca DEX ($184.7M), Meteora DLMM ($166.9M), Scorch ($159.2M), Manifest Trade ($155.9M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 659 / 28 |
| Delinquent stake | 0.07% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 25.0% |
| Avg / median commission | 13.1% / 5% |
| Alpenglow BLS-key readiness | 670 validators, 100.0% of stake |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `he1iusunGwqrNtafDtLd…` | 17,003,542 | 4.0% | 0% |
| 2 | `CcaHc2L43ZWjwCHART3o…` | 15,962,658 | 3.76% | 7% |
| 3 | `3N7s9zXMZ4QqvHQR15t5…` | 12,418,812 | 2.92% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxb…` | 10,242,949 | 2.41% | 0% |
| 5 | `51JBzSTU5rAM8gLAVQKg…` | 9,885,209 | 2.33% | 10% |
| 6 | `CatzoSMUkTRidT5DwBxA…` | 9,615,269 | 2.26% | 5% |
| 7 | `26pV97Ce83ZQ6Kz9XT4t…` | 9,283,847 | 2.19% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2Fp…` | 8,016,085 | 1.89% | 7% |
| 9 | `DumiCKHVqoCQKD8roLAp…` | 6,968,432 | 1.64% | 0% |
| 10 | `CvSb7wdQAFpHuSpTYTJn…` | 6,779,378 | 1.6% | 5% |

## Signals (anomaly detection)

- **[WARNING]** Solana TVL contraction (z=-2.2 vs its recent baseline)
- **[WARNING]** Stablecoin supply contraction (z=-2.4 vs its recent baseline)
- **[WARNING · liquidity_rotation]** Stablecoin supply and TVL moving together — capital rotating in or out of the chain.

## Solana Pulse — sentiment (experimental)

**36/100 — Bearish** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 61.0 |
| fear greed | 13 |
| momentum | 31.0 |
| news | 34 |

Crypto Fear & Greed: 13 (Extreme Fear) · CoinGecko votes bullish: 60.98% · headline tone (48h): -2

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 809 |
| Raydium AMM v4 | 526 |
| Orca Whirlpool | 1,500 |
| Pump.fun | 1,500 |
| Tensor | 0 |
| Magic Eden v2 | 56 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,300,003 |
| Binance (cold) | 66 |
| OKX (attributed) | 67,692 |
| Coinbase (hot) | 12,940 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 215ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 100.0% of stake.
- **Agave**: latest release v4.4.1 · running 4.4.0 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 11885 ms |
| solana_rpc_validators | OK | 69 ms |
| coingecko | OK | 1573 ms |
| defillama_tvl | OK | 36 ms |
| defillama_dex | OK | 596 ms |
| defillama_fees | OK | 677 ms |
| defillama_stablecoins | OK | 78 ms |
| defillama_xstocks | FAILED | 155 ms |
| jito_kobe | OK | 79 ms |
| stakewiz | OK | 692 ms |
| github | OK | 669 ms |
| solana_com_news | FAILED | 31 ms |
| sentiment | OK | 1973 ms |
| solana_status_page | OK | 274 ms |
| solana_rpc_whales | OK | 1398 ms |
| solana_rpc_programs | OK | 2329 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*