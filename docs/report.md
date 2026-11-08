# Solbeat — State of the Solana Network

> Generated 2026-11-08T03:49:23Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1080 is 49% complete (~13h remaining), with the cluster processing ~1,300 TPS (1,300 non-vote). Measured slot time is 216ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $503.4K of Real Economic Value over the last 24h ($350/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $89.24 (-0.6% / 24h). Decentralization: Nakamoto coefficient 18, 664 active validators, 0.1% of stake delinquent. Alpenglow readiness: validators holding 100% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 1 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 466,769,885 |
| Block height | 444,788,301 |
| Epoch | 1080 (48.58% complete, ~13.3h left) |
| TPS (10 min avg) | 1,300 |
| Non-vote TPS | 1,300 |
| Slot time (measured) | 215.6 ms |
| Confirmation time (measured) | 0.22 s |
| Finality time (measured) | 0.22 s — **Alpenglow active** |
| Est. daily transactions | 131,223,360 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0030 |
| Node version | 4.4.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $89.24 (-0.6%/24h) |
| Market cap | $52.7B |
| **REV (24h)** | **$503.4K** (fees $392.5K + Jito tips $110.9K) |
| Chain TVL | $5.2B |
| Stablecoin supply | $14.9B |
| DEX volume (24h) | $1.3B (-12.2%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 591,038,157 SOL |
| Inflation | 3.57% |

Top DEXs by 24h volume: PumpSwap ($217.3M), BisonFi ($170.2M), Tessera V ($153.4M), Meteora DLMM ($128.6M), pump.fun ($108.3M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 664 / 33 |
| Delinquent stake | 0.14% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.6% |
| Avg / median commission | 13.0% / 5.0% |
| Alpenglow BLS-key readiness | 685 validators, 100.0% of stake |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L43ZWjwCHART3o…` | 17,043,402 | 3.92% | 7% |
| 2 | `he1iusunGwqrNtafDtLd…` | 16,729,016 | 3.85% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5…` | 13,015,291 | 2.99% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxb…` | 10,277,563 | 2.36% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxA…` | 9,558,411 | 2.2% | 5% |
| 6 | `51JBzSTU5rAM8gLAVQKg…` | 9,520,070 | 2.19% | 10% |
| 7 | `26pV97Ce83ZQ6Kz9XT4t…` | 9,242,930 | 2.13% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2Fp…` | 7,750,589 | 1.78% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJn…` | 6,983,623 | 1.61% | 5% |
| 10 | `DumiCKHVqoCQKD8roLAp…` | 6,973,337 | 1.6% | 0% |

## Signals (anomaly detection)

- **[WARNING]** Stablecoin supply contraction (z=-2.6 vs its recent baseline)

## Solana Pulse — sentiment (experimental)

**45/100 — Neutral** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 56.2 |
| fear greed | 28 |
| momentum | 34.0 |
| news | 74 |

Crypto Fear & Greed: 28 (Fear) · CoinGecko votes bullish: 56.25% · headline tone (48h): +3

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 738 |
| Raydium AMM v4 | 495 |
| Orca Whirlpool | 495 |
| Pump.fun | 1,500 |
| Tensor | 0 |
| Magic Eden v2 | 71 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,300,003 |
| Binance (cold) | 66 |
| OKX (attributed) | 97,596 |
| Coinbase (hot) | 23,704 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 216ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 100.0% of stake.
- **Agave**: latest release v4.4.1 · running 4.4.0 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 10318 ms |
| solana_rpc_validators | OK | 138 ms |
| coingecko | OK | 1647 ms |
| defillama_tvl | OK | 81 ms |
| defillama_dex | OK | 806 ms |
| defillama_fees | OK | 986 ms |
| defillama_stablecoins | OK | 99 ms |
| defillama_xstocks | FAILED | 529 ms |
| jito_kobe | OK | 402 ms |
| stakewiz | OK | 964 ms |
| github | OK | 758 ms |
| solana_com_news | FAILED | 59 ms |
| sentiment | OK | 2117 ms |
| solana_status_page | OK | 122 ms |
| solana_rpc_whales | OK | 881 ms |
| solana_rpc_programs | OK | 1818 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*