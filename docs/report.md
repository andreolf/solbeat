# Solbeat — State of the Solana Network

> Generated 2026-11-06T19:31:35Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1079 is 23% complete (~20h remaining), with the cluster processing ~1,845 TPS (1,845 non-vote). Measured slot time is 214ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $622.2K of Real Economic Value over the last 24h ($432/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $89.96 (+0.8% / 24h). Decentralization: Nakamoto coefficient 18, 660 active validators, 0.3% of stake delinquent. Alpenglow readiness: validators holding 100% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 1 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 466,227,845 |
| Block height | 444,246,870 |
| Epoch | 1079 (23.11% complete, ~19.8h left) |
| TPS (10 min avg) | 1,845 |
| Non-vote TPS | 1,845 |
| Slot time (measured) | 214.5 ms |
| Confirmation time (measured) | 0.21 s |
| Finality time (measured) | 0.21 s — **Alpenglow active** |
| Est. daily transactions | 193,688,500 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0026 |
| Node version | 4.4.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $89.96 (+0.8%/24h) |
| Market cap | $53.1B |
| **REV (24h)** | **$622.2K** (fees $499.4K + Jito tips $122.8K) |
| Chain TVL | $5.2B |
| Stablecoin supply | $15.0B |
| DEX volume (24h) | $2.2B (-7.8%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 590,342,612 SOL |
| Inflation | 3.57% |

Top DEXs by 24h volume: Orca DEX ($285.0M), BisonFi ($231.1M), Tessera V ($197.0M), PumpSwap ($188.6M), Meteora DLMM ($172.6M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 660 / 36 |
| Delinquent stake | 0.32% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.6% |
| Avg / median commission | 12.7% / 5.0% |
| Alpenglow BLS-key readiness | 682 validators, 100.0% of stake |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L43ZWjwCHART3o…` | 17,039,556 | 3.92% | 7% |
| 2 | `he1iusunGwqrNtafDtLd…` | 16,722,209 | 3.84% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5…` | 13,017,562 | 2.99% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxb…` | 10,436,420 | 2.4% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxA…` | 9,531,946 | 2.19% | 5% |
| 6 | `51JBzSTU5rAM8gLAVQKg…` | 9,519,642 | 2.19% | 10% |
| 7 | `26pV97Ce83ZQ6Kz9XT4t…` | 9,240,519 | 2.12% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2Fp…` | 7,741,933 | 1.78% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJn…` | 6,982,918 | 1.61% | 5% |
| 10 | `DumiCKHVqoCQKD8roLAp…` | 6,971,614 | 1.6% | 0% |

## Signals (anomaly detection)

- **[WARNING]** Stablecoin supply contraction (z=-2.7 vs its recent baseline)

## Solana Pulse — sentiment (experimental)

**43/100 — Neutral** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 65.5 |
| fear greed | 28 |
| momentum | 37.2 |
| news | 34 |

Crypto Fear & Greed: 28 (Fear) · CoinGecko votes bullish: 65.52% · headline tone (48h): -2

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 889 |
| Raydium AMM v4 | 407 |
| Orca Whirlpool | 1,500 |
| Pump.fun | 1,500 |
| Tensor | 0 |
| Magic Eden v2 | 37 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,300,003 |
| Binance (cold) | 66 |
| OKX (attributed) | 97,314 |
| Coinbase (hot) | 24,679 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 214ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 100.0% of stake.
- **Agave**: latest release v4.4.1 · running 4.4.0 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 9650 ms |
| solana_rpc_validators | OK | 315 ms |
| coingecko | OK | 1699 ms |
| defillama_tvl | OK | 1654 ms |
| defillama_dex | OK | 1158 ms |
| defillama_fees | OK | 1009 ms |
| defillama_stablecoins | OK | 1278 ms |
| defillama_xstocks | FAILED | 771 ms |
| jito_kobe | OK | 373 ms |
| stakewiz | OK | 1532 ms |
| github | OK | 697 ms |
| solana_com_news | FAILED | 115 ms |
| sentiment | OK | 2248 ms |
| solana_status_page | OK | 244 ms |
| solana_rpc_whales | OK | 1173 ms |
| solana_rpc_programs | OK | 2253 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*