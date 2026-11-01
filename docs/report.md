# Solbeat — State of the Solana Network

> Generated 2026-11-01T05:07:11Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1074 is 0% complete (~26h remaining), with the cluster processing ~1,078 TPS (1,078 non-vote). Measured slot time is 216ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $460.1K of Real Economic Value over the last 24h ($320/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $95.48 (-0.4% / 24h). Decentralization: Nakamoto coefficient 18, 663 active validators, 1.1% of stake delinquent. Alpenglow readiness: validators holding 100% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 1 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 463,968,415 |
| Block height | 441,990,166 |
| Epoch | 1074 (0.1% complete, ~25.9h left) |
| TPS (10 min avg) | 1,078 |
| Non-vote TPS | 1,078 |
| Slot time (measured) | 215.9 ms |
| Confirmation time (measured) | 0.0 s |
| Finality time (measured) | 0.0 s — **Alpenglow active** |
| Est. daily transactions | 122,515,558 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0030 |
| Node version | 4.3.2 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $95.48 (-0.4%/24h) |
| Market cap | $56.3B |
| **REV (24h)** | **$460.1K** (fees $364.2K + Jito tips $95.8K) |
| Chain TVL | $5.4B |
| Stablecoin supply | $15.4B |
| DEX volume (24h) | $1.4B (-31.9%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 590,140,609 SOL |
| Inflation | 3.58% |

Top DEXs by 24h volume: BisonFi ($182.9M), Tessera V ($181.4M), PumpSwap ($130.7M), pump.fun ($113.6M), GoonFi ($108.0M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 663 / 33 |
| Delinquent stake | 1.05% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.7% |
| Avg / median commission | 12.8% / 5% |
| Alpenglow BLS-key readiness | 678 validators, 100.0% of stake |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L43ZWjwCHART3o…` | 17,028,800 | 3.92% | 7% |
| 2 | `he1iusunGwqrNtafDtLd…` | 16,694,602 | 3.85% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5…` | 12,943,195 | 2.98% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxb…` | 10,426,732 | 2.4% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxA…` | 9,582,401 | 2.21% | 5% |
| 6 | `51JBzSTU5rAM8gLAVQKg…` | 9,451,018 | 2.18% | 10% |
| 7 | `26pV97Ce83ZQ6Kz9XT4t…` | 9,224,837 | 2.13% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2Fp…` | 7,791,470 | 1.8% | 7% |
| 9 | `DumiCKHVqoCQKD8roLAp…` | 7,001,245 | 1.61% | 0% |
| 10 | `CvSb7wdQAFpHuSpTYTJn…` | 6,976,876 | 1.61% | 5% |

## Signals (anomaly detection)

- **[WARNING]** Real Economic Value deviating from its run-history baseline (z=-2.2)

## Solana Pulse — sentiment (experimental)

**48/100 — Neutral** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 75.9 |
| fear greed | 34 |
| momentum | 23.2 |
| news | 66 |

Crypto Fear & Greed: 34 (Fear) · CoinGecko votes bullish: 75.86% · headline tone (48h): +2

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 1,215 |
| Raydium AMM v4 | 241 |
| Orca Whirlpool | 671 |
| Pump.fun | 1,500 |
| Tensor | 1 |
| Magic Eden v2 | 68 |
| Marinade | 1 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 11,890,003 |
| Binance (cold) | 4 |
| OKX (attributed) | 339,500 |
| Coinbase (hot) | 78,258 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 216ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 100.0% of stake.
- **Agave**: latest release v4.4.0 · running 4.3.2 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 11445 ms |
| solana_rpc_validators | OK | 292 ms |
| coingecko | OK | 1675 ms |
| defillama_tvl | OK | 393 ms |
| defillama_dex | OK | 971 ms |
| defillama_fees | OK | 1194 ms |
| defillama_stablecoins | OK | 175 ms |
| defillama_xstocks | FAILED | 72 ms |
| jito_kobe | OK | 224 ms |
| stakewiz | OK | 1176 ms |
| github | OK | 859 ms |
| solana_com_news | FAILED | 194 ms |
| sentiment | OK | 2156 ms |
| solana_status_page | OK | 355 ms |
| solana_rpc_whales | OK | 1219 ms |
| solana_rpc_programs | OK | 2227 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*