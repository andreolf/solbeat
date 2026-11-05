# Solbeat — State of the Solana Network

> Generated 2026-11-05T12:44:28Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1078 is 3% complete (~25h remaining), with the cluster processing ~1,672 TPS (1,672 non-vote). Measured slot time is 214ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $717.4K of Real Economic Value over the last 24h ($498/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $95.05 (+2.5% / 24h). Decentralization: Nakamoto coefficient 18, 663 active validators, 0.1% of stake delinquent. Alpenglow readiness: validators holding 100% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 2 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 465,709,960 |
| Block height | 443,730,059 |
| Epoch | 1078 (3.23% complete, ~24.8h left) |
| TPS (10 min avg) | 1,672 |
| Non-vote TPS | 1,672 |
| Slot time (measured) | 213.9 ms |
| Confirmation time (measured) | 0.21 s |
| Finality time (measured) | 0.21 s — **Alpenglow active** |
| Est. daily transactions | 109,442,289 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0053 |
| Node version | 4.4.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $95.05 (+2.5%/24h) |
| Market cap | $56.1B |
| **REV (24h)** | **$717.4K** (fees $579.8K + Jito tips $137.7K) |
| Chain TVL | $5.6B |
| Stablecoin supply | $15.1B |
| DEX volume (24h) | $2.4B (26.8%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 590,317,843 SOL |
| Inflation | 3.57% |

Top DEXs by 24h volume: PumpSwap ($315.4M), Orca DEX ($276.2M), BisonFi ($241.3M), Meteora DLMM ($198.5M), Raydium AMM ($191.4M)

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

- **[WARNING]** TPS spike: 1,672 vs 12h mean 1,258 (z=+2.5)
- **[WARNING]** Stablecoin supply contraction (z=-2.4 vs its recent baseline)

## Solana Pulse — sentiment (experimental)

**65/100 — Bullish** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 77.8 |
| fear greed | 50 |
| momentum | 60.6 |
| news | 74 |

Crypto Fear & Greed: 50 (Neutral) · CoinGecko votes bullish: 77.78% · headline tone (48h): +3

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 1,500 |
| Raydium AMM v4 | 1,500 |
| Orca Whirlpool | 1,500 |
| Pump.fun | 1,500 |
| Tensor | 0 |
| Magic Eden v2 | 66 |
| Marinade | 1 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,300,003 |
| Binance (cold) | 66 |
| OKX (attributed) | 346,932 |
| Coinbase (hot) | 21,024 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 214ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 100.0% of stake.
- **Agave**: latest release v4.4.0 · running 4.4.0 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 10229 ms |
| solana_rpc_validators | OK | 357 ms |
| coingecko | OK | 1691 ms |
| defillama_tvl | OK | 121 ms |
| defillama_dex | OK | 1079 ms |
| defillama_fees | OK | 1838 ms |
| defillama_stablecoins | OK | 144 ms |
| defillama_xstocks | FAILED | 737 ms |
| jito_kobe | OK | 1804 ms |
| stakewiz | OK | 1261 ms |
| github | OK | 898 ms |
| solana_com_news | FAILED | 194 ms |
| sentiment | OK | 2479 ms |
| solana_status_page | OK | 263 ms |
| solana_rpc_whales | OK | 1245 ms |
| solana_rpc_programs | OK | 2233 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*