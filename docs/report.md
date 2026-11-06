# Solbeat — State of the Solana Network

> Generated 2026-11-06T08:24:18Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1078 is 80% complete (~5h remaining), with the cluster processing ~1,304 TPS (1,304 non-vote). Measured slot time is 213ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $622.6K of Real Economic Value over the last 24h ($432/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $89.72 (-7.0% / 24h). Decentralization: Nakamoto coefficient 18, 663 active validators, 0.1% of stake delinquent. Alpenglow readiness: validators holding 100% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 1 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 466,041,015 |
| Block height | 444,060,636 |
| Epoch | 1078 (79.86% complete, ~5.1h left) |
| TPS (10 min avg) | 1,304 |
| Non-vote TPS | 1,304 |
| Slot time (measured) | 212.7 ms |
| Confirmation time (measured) | 0.21 s |
| Finality time (measured) | 0.21 s — **Alpenglow active** |
| Est. daily transactions | 135,012,345 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0037 |
| Node version | 4.4.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $89.72 (-7.0%/24h) |
| Market cap | $53.0B |
| **REV (24h)** | **$622.6K** (fees $499.4K + Jito tips $123.1K) |
| Chain TVL | $5.3B |
| Stablecoin supply | $15.0B |
| DEX volume (24h) | $2.2B (-8.5%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 590,287,267 SOL |
| Inflation | 3.57% |

Top DEXs by 24h volume: Orca DEX ($310.4M), BisonFi ($241.3M), Meteora DLMM ($198.5M), PumpSwap ($188.6M), Tessera V ($185.3M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 663 / 31 |
| Delinquent stake | 0.13% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.7% |
| Avg / median commission | 12.8% / 5% |
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

**49/100 — Neutral** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 61.9 |
| fear greed | 28 |
| momentum | 37.5 |
| news | 82 |

Crypto Fear & Greed: 28 (Fear) · CoinGecko votes bullish: 61.9% · headline tone (48h): +4

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 1,050 |
| Raydium AMM v4 | 1,500 |
| Orca Whirlpool | 1,050 |
| Pump.fun | 1,500 |
| Tensor | 0 |
| Magic Eden v2 | 73 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,300,003 |
| Binance (cold) | 66 |
| OKX (attributed) | 96,932 |
| Coinbase (hot) | 20,685 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 213ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 100.0% of stake.
- **Agave**: latest release v4.4.1 · running 4.4.0 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 10027 ms |
| solana_rpc_validators | OK | 307 ms |
| coingecko | OK | 1628 ms |
| defillama_tvl | OK | 470 ms |
| defillama_dex | OK | 483 ms |
| defillama_fees | OK | 1107 ms |
| defillama_stablecoins | OK | 1187 ms |
| defillama_xstocks | FAILED | 184 ms |
| jito_kobe | OK | 423 ms |
| stakewiz | OK | 1143 ms |
| github | OK | 851 ms |
| solana_com_news | FAILED | 108 ms |
| sentiment | OK | 2131 ms |
| solana_status_page | OK | 440 ms |
| solana_rpc_whales | OK | 1030 ms |
| solana_rpc_programs | OK | 1926 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*