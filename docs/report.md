# Solbeat — State of the Solana Network

> Generated 2026-11-06T03:06:43Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1078 is 59% complete (~10h remaining), with the cluster processing ~1,839 TPS (1,839 non-vote). Measured slot time is 213ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $623.0K of Real Economic Value over the last 24h ($433/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $90.29 (-6.3% / 24h). Decentralization: Nakamoto coefficient 18, 661 active validators, 0.5% of stake delinquent. Alpenglow readiness: validators holding 100% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 1 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 465,951,828 |
| Block height | 443,971,577 |
| Epoch | 1078 (59.22% complete, ~10.4h left) |
| TPS (10 min avg) | 1,839 |
| Non-vote TPS | 1,839 |
| Slot time (measured) | 213.2 ms |
| Confirmation time (measured) | 0.21 s |
| Finality time (measured) | 0.21 s — **Alpenglow active** |
| Est. daily transactions | 169,202,340 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0030 |
| Node version | 4.4.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $90.29 (-6.3%/24h) |
| Market cap | $53.3B |
| **REV (24h)** | **$623.0K** (fees $499.4K + Jito tips $123.6K) |
| Chain TVL | $5.3B |
| Stablecoin supply | $15.0B |
| DEX volume (24h) | $2.2B (-8.5%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 590,287,346 SOL |
| Inflation | 3.57% |

Top DEXs by 24h volume: Orca DEX ($311.1M), BisonFi ($241.3M), Raydium AMM ($207.8M), Meteora DLMM ($198.5M), PumpSwap ($188.6M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 661 / 33 |
| Delinquent stake | 0.53% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.7% |
| Avg / median commission | 12.9% / 5% |
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

- **[WARNING]** Stablecoin supply contraction (z=-2.7 vs its recent baseline)

## Solana Pulse — sentiment (experimental)

**51/100 — Neutral** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 67.6 |
| fear greed | 28 |
| momentum | 38.0 |
| news | 82 |

Crypto Fear & Greed: 28 (Fear) · CoinGecko votes bullish: 67.57% · headline tone (48h): +4

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 1,171 |
| Raydium AMM v4 | 350 |
| Orca Whirlpool | 1,500 |
| Pump.fun | 1,500 |
| Tensor | 1 |
| Magic Eden v2 | 31 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,300,003 |
| Binance (cold) | 66 |
| OKX (attributed) | 346,932 |
| Coinbase (hot) | 21,872 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 213ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 100.0% of stake.
- **Agave**: latest release v4.4.1 · running 4.4.0 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 9676 ms |
| solana_rpc_validators | OK | 232 ms |
| coingecko | OK | 1681 ms |
| defillama_tvl | OK | 155 ms |
| defillama_dex | OK | 888 ms |
| defillama_fees | OK | 719 ms |
| defillama_stablecoins | OK | 197 ms |
| defillama_xstocks | FAILED | 85 ms |
| jito_kobe | OK | 354 ms |
| stakewiz | OK | 1017 ms |
| github | OK | 842 ms |
| solana_com_news | FAILED | 81 ms |
| sentiment | OK | 2282 ms |
| solana_status_page | OK | 206 ms |
| solana_rpc_whales | OK | 1067 ms |
| solana_rpc_programs | OK | 1961 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*