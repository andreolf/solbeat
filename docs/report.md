# Solbeat — State of the Solana Network

> Generated 2026-11-28T11:41:09Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1099 is 40% complete (~15h remaining), with the cluster processing ~951 TPS (951 non-vote). Measured slot time is 212ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $397.6K of Real Economic Value over the last 24h ($276/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $70.82 (-3.3% / 24h). Decentralization: Nakamoto coefficient 18, 655 active validators, 0.0% of stake delinquent. Alpenglow readiness: validators holding 100% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 1 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 474,939,758 |
| Block height | 452,952,195 |
| Epoch | 1099 (39.76% complete, ~15.3h left) |
| TPS (10 min avg) | 951 |
| Non-vote TPS | 951 |
| Slot time (measured) | 212.1 ms |
| Confirmation time (measured) | 0.21 s |
| Finality time (measured) | 0.21 s — **Alpenglow active** |
| Est. daily transactions | 103,792,987 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0030 |
| Node version | 4.4.2 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $70.82 (-3.3%/24h) |
| Market cap | $42.0B |
| **REV (24h)** | **$397.6K** (fees $309.6K + Jito tips $88.0K) |
| Chain TVL | $4.6B |
| Stablecoin supply | $13.3B |
| DEX volume (24h) | $1.0B (18.1%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 592,430,484 SOL |
| Inflation | 3.54% |

Top DEXs by 24h volume: Orca DEX ($168.6M), PumpSwap ($139.7M), BisonFi ($111.4M), Raydium AMM ($105.8M), pump.fun ($94.9M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 655 / 10 |
| Delinquent stake | 0.03% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.9% |
| Avg / median commission | 13.1% / 5% |
| Alpenglow BLS-key readiness | 669 validators, 100.0% of stake |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `he1iusunGwqrNtafDtLd…` | 16,820,639 | 3.97% | 0% |
| 2 | `CcaHc2L43ZWjwCHART3o…` | 15,937,964 | 3.76% | 7% |
| 3 | `3N7s9zXMZ4QqvHQR15t5…` | 12,430,259 | 2.93% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxb…` | 10,239,621 | 2.42% | 0% |
| 5 | `51JBzSTU5rAM8gLAVQKg…` | 9,920,125 | 2.34% | 10% |
| 6 | `CatzoSMUkTRidT5DwBxA…` | 9,625,966 | 2.27% | 5% |
| 7 | `26pV97Ce83ZQ6Kz9XT4t…` | 9,299,548 | 2.2% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2Fp…` | 8,045,358 | 1.9% | 7% |
| 9 | `DumiCKHVqoCQKD8roLAp…` | 6,973,110 | 1.65% | 0% |
| 10 | `CvSb7wdQAFpHuSpTYTJn…` | 6,346,579 | 1.5% | 5% |

## Signals (anomaly detection)

- **[WARNING]** Stablecoin supply contraction (z=-2.2 vs its recent baseline)

## Solana Pulse — sentiment (experimental)

**49/100 — Neutral** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 57.7 |
| fear greed | 10 |
| momentum | 60.4 |
| news | 74 |

Crypto Fear & Greed: 10 (Extreme Fear) · CoinGecko votes bullish: 57.69% · headline tone (48h): +3

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 620 |
| Raydium AMM v4 | 620 |
| Orca Whirlpool | 1,500 |
| Pump.fun | 1,500 |
| Tensor | 0 |
| Magic Eden v2 | 31 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,300,003 |
| Binance (cold) | 66 |
| OKX (attributed) | 59,503 |
| Coinbase (hot) | 142,123 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 212ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 100.0% of stake.
- **Agave**: latest release v4.4.2 · running 4.4.2 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 10018 ms |
| solana_rpc_validators | OK | 390 ms |
| coingecko | OK | 1757 ms |
| defillama_tvl | OK | 148 ms |
| defillama_dex | OK | 1036 ms |
| defillama_fees | OK | 1753 ms |
| defillama_stablecoins | OK | 196 ms |
| defillama_xstocks | FAILED | 719 ms |
| jito_kobe | OK | 156 ms |
| stakewiz | OK | 1271 ms |
| github | OK | 886 ms |
| solana_com_news | FAILED | 132 ms |
| sentiment | OK | 2294 ms |
| solana_status_page | OK | 354 ms |
| solana_rpc_whales | OK | 1223 ms |
| solana_rpc_programs | OK | 2035 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*