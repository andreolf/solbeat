# Solbeat — State of the Solana Network

> Generated 2026-11-02T21:45:06Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1075 is 58% complete (~11h remaining), with the cluster processing ~1,765 TPS (1,765 non-vote). Measured slot time is 215ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $453.0K of Real Economic Value over the last 24h ($315/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $91.93 (-2.6% / 24h). Decentralization: Nakamoto coefficient 18, 664 active validators, 1.0% of stake delinquent. Alpenglow readiness: validators holding 100% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 1 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 464,651,042 |
| Block height | 442,672,124 |
| Epoch | 1075 (58.11% complete, ~10.8h left) |
| TPS (10 min avg) | 1,765 |
| Non-vote TPS | 1,765 |
| Slot time (measured) | 214.7 ms |
| Confirmation time (measured) | 0.21 s |
| Finality time (measured) | 0.21 s — **Alpenglow active** |
| Est. daily transactions | 202,251,678 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0018 |
| Node version | 4.3.2 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $91.93 (-2.6%/24h) |
| Market cap | $54.2B |
| **REV (24h)** | **$453.0K** (fees $367.7K + Jito tips $85.3K) |
| Chain TVL | $5.3B |
| Stablecoin supply | $15.4B |
| DEX volume (24h) | $905.6M (-5.0%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 590,205,720 SOL |
| Inflation | 3.57% |

Top DEXs by 24h volume: Orca DEX ($203.7M), Raydium AMM ($128.7M), PumpSwap ($122.9M), pump.fun ($104.8M), Manifest Trade ($104.5M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 664 / 30 |
| Delinquent stake | 1.04% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.7% |
| Avg / median commission | 12.8% / 5.0% |
| Alpenglow BLS-key readiness | 680 validators, 100.0% of stake |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L43ZWjwCHART3o…` | 17,034,354 | 3.92% | 7% |
| 2 | `he1iusunGwqrNtafDtLd…` | 16,710,199 | 3.85% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5…` | 13,037,180 | 3.0% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxb…` | 10,429,501 | 2.4% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxA…` | 9,580,109 | 2.21% | 5% |
| 6 | `51JBzSTU5rAM8gLAVQKg…` | 9,453,055 | 2.18% | 10% |
| 7 | `26pV97Ce83ZQ6Kz9XT4t…` | 9,226,805 | 2.13% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2Fp…` | 7,803,392 | 1.8% | 7% |
| 9 | `DumiCKHVqoCQKD8roLAp…` | 7,001,891 | 1.61% | 0% |
| 10 | `CvSb7wdQAFpHuSpTYTJn…` | 6,978,080 | 1.61% | 5% |

## Signals (anomaly detection)

- **[WARNING]** DEX volume contraction (z=-2.0 vs its recent baseline)

## Solana Pulse — sentiment (experimental)

**44/100 — Neutral** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 66.7 |
| fear greed | 37 |
| momentum | 32.4 |
| news | 34 |

Crypto Fear & Greed: 37 (Fear) · CoinGecko votes bullish: 66.67% · headline tone (48h): -2

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 1,500 |
| Raydium AMM v4 | 1,135 |
| Orca Whirlpool | 1,500 |
| Pump.fun | 1,500 |
| Tensor | 0 |
| Magic Eden v2 | 347 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,890,003 |
| Binance (cold) | 4 |
| OKX (attributed) | 339,502 |
| Coinbase (hot) | 13,839 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 215ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 100.0% of stake.
- **Agave**: latest release v4.4.0 · running 4.3.2 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 11311 ms |
| solana_rpc_validators | OK | 301 ms |
| coingecko | OK | 1677 ms |
| defillama_tvl | OK | 324 ms |
| defillama_dex | OK | 912 ms |
| defillama_fees | OK | 1205 ms |
| defillama_stablecoins | OK | 345 ms |
| defillama_xstocks | FAILED | 690 ms |
| jito_kobe | OK | 412 ms |
| stakewiz | OK | 1202 ms |
| github | OK | 820 ms |
| solana_com_news | FAILED | 110 ms |
| sentiment | OK | 2117 ms |
| solana_status_page | OK | 297 ms |
| solana_rpc_whales | OK | 1259 ms |
| solana_rpc_programs | OK | 1874 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*