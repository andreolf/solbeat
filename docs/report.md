# Solbeat — State of the Solana Network

> Generated 2026-11-05T14:46:28Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1078 is 11% complete (~23h remaining), with the cluster processing ~3,176 TPS (3,176 non-vote). Measured slot time is 213ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $709.2K of Real Economic Value over the last 24h ($492/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $94.26 (-0.5% / 24h). Decentralization: Nakamoto coefficient 18, 663 active validators, 0.1% of stake delinquent. Alpenglow readiness: validators holding 100% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 2 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 465,744,301 |
| Block height | 443,764,258 |
| Epoch | 1078 (11.18% complete, ~22.7h left) |
| TPS (10 min avg) | 3,176 |
| Non-vote TPS | 3,176 |
| Slot time (measured) | 212.6 ms |
| Confirmation time (measured) | 0.21 s |
| Finality time (measured) | 0.21 s — **Alpenglow active** |
| Est. daily transactions | 121,872,729 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0048 |
| Node version | 4.4.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $94.26 (-0.5%/24h) |
| Market cap | $55.6B |
| **REV (24h)** | **$709.2K** (fees $579.8K + Jito tips $129.4K) |
| Chain TVL | $5.5B |
| Stablecoin supply | $15.1B |
| DEX volume (24h) | $2.4B (26.8%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 590,317,666 SOL |
| Inflation | 3.57% |

Top DEXs by 24h volume: PumpSwap ($315.4M), Orca DEX ($269.1M), BisonFi ($241.3M), Meteora DLMM ($198.5M), Raydium AMM ($188.4M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 663 / 31 |
| Delinquent stake | 0.13% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.7% |
| Avg / median commission | 12.7% / 5% |
| Alpenglow BLS-key readiness | 681 validators, 100.0% of stake |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L43ZWjwCHART3o…` | 17,063,613 | 3.96% | 7% |
| 2 | `he1iusunGwqrNtafDtLd…` | 16,736,546 | 3.88% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5…` | 13,020,024 | 3.02% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxb…` | 10,434,901 | 2.42% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxA…` | 9,530,733 | 2.21% | 5% |
| 6 | `51JBzSTU5rAM8gLAVQKg…` | 9,459,109 | 2.2% | 10% |
| 7 | `26pV97Ce83ZQ6Kz9XT4t…` | 9,222,692 | 2.14% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2Fp…` | 7,860,096 | 1.82% | 7% |
| 9 | `DumiCKHVqoCQKD8roLAp…` | 6,991,477 | 1.62% | 0% |
| 10 | `3JD3jMmnR6g88qff2WZ3…` | 6,293,076 | 1.46% | 0% |

## Signals (anomaly detection)

- **[SERIOUS]** TPS spike: 3,176 vs 12h mean 1,370 (z=+6.3)
- **[WARNING]** Stablecoin supply contraction (z=-2.4 vs its recent baseline)

## Solana Pulse — sentiment (experimental)

**61/100 — Bullish** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 81.6 |
| fear greed | 50 |
| momentum | 58.7 |
| news | 42 |

Crypto Fear & Greed: 50 (Neutral) · CoinGecko votes bullish: 81.58% · headline tone (48h): -1

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 1,500 |
| Raydium AMM v4 | 1,500 |
| Orca Whirlpool | 1,500 |
| Pump.fun | 1,500 |
| Tensor | 0 |
| Magic Eden v2 | 40 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,300,003 |
| Binance (cold) | 66 |
| OKX (attributed) | 346,932 |
| Coinbase (hot) | 20,738 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 213ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 100.0% of stake.
- **Agave**: latest release v4.4.0 · running 4.4.0 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 12388 ms |
| solana_rpc_validators | OK | 617 ms |
| coingecko | OK | 1759 ms |
| defillama_tvl | OK | 230 ms |
| defillama_dex | OK | 1035 ms |
| defillama_fees | OK | 1704 ms |
| defillama_stablecoins | OK | 624 ms |
| defillama_xstocks | FAILED | 74 ms |
| jito_kobe | OK | 178 ms |
| stakewiz | OK | 1143 ms |
| github | OK | 966 ms |
| solana_com_news | FAILED | 173 ms |
| sentiment | OK | 2299 ms |
| solana_status_page | OK | 336 ms |
| solana_rpc_whales | OK | 3197 ms |
| solana_rpc_programs | OK | 5118 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*