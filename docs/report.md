# Solbeat — State of the Solana Network

> Generated 2026-11-27T00:12:02Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1098 is 2% complete (~26h remaining), with the cluster processing ~1,388 TPS (1,388 non-vote). Measured slot time is 217ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $520.5K of Real Economic Value over the last 24h ($361/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $70.96 (+0.4% / 24h). Decentralization: Nakamoto coefficient 18, 654 active validators, 0.1% of stake delinquent. Alpenglow readiness: validators holding 100% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 1 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 474,344,486 |
| Block height | 452,357,261 |
| Epoch | 1098 (1.96% complete, ~25.6h left) |
| TPS (10 min avg) | 1,388 |
| Non-vote TPS | 1,388 |
| Slot time (measured) | 217.2 ms |
| Confirmation time (measured) | 0.22 s |
| Finality time (measured) | 0.22 s — **Alpenglow active** |
| Est. daily transactions | 153,568,916 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0027 |
| Node version | 4.4.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $70.96 (+0.4%/24h) |
| Market cap | $42.0B |
| **REV (24h)** | **$520.5K** (fees $415.3K + Jito tips $105.2K) |
| Chain TVL | $4.6B |
| Stablecoin supply | $13.3B |
| DEX volume (24h) | $1.5B (3.7%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 592,238,592 SOL |
| Inflation | 3.54% |

Top DEXs by 24h volume: BisonFi ($190.6M), Orca DEX ($135.1M), Meteora DLMM ($119.4M), Raydium AMM ($117.2M), Scorch ($104.6M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 654 / 34 |
| Delinquent stake | 0.06% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 25.0% |
| Avg / median commission | 13.0% / 5.0% |
| Alpenglow BLS-key readiness | 670 validators, 100.0% of stake |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `he1iusunGwqrNtafDtLd…` | 16,815,245 | 3.96% | 0% |
| 2 | `CcaHc2L43ZWjwCHART3o…` | 15,826,052 | 3.73% | 7% |
| 3 | `3N7s9zXMZ4QqvHQR15t5…` | 12,437,388 | 2.93% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxb…` | 10,238,108 | 2.41% | 0% |
| 5 | `51JBzSTU5rAM8gLAVQKg…` | 9,920,637 | 2.34% | 10% |
| 6 | `CatzoSMUkTRidT5DwBxA…` | 9,617,109 | 2.27% | 5% |
| 7 | `26pV97Ce83ZQ6Kz9XT4t…` | 9,296,651 | 2.19% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2Fp…` | 8,037,877 | 1.89% | 7% |
| 9 | `DumiCKHVqoCQKD8roLAp…` | 6,972,141 | 1.64% | 0% |
| 10 | `CvSb7wdQAFpHuSpTYTJn…` | 6,741,351 | 1.59% | 5% |

## Signals (anomaly detection)

- **[WARNING]** Stablecoin supply contraction (z=-2.5 vs its recent baseline)

## Solana Pulse — sentiment (experimental)

**49/100 — Neutral** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 73.9 |
| fear greed | 12 |
| momentum | 53.2 |
| news | 50 |

Crypto Fear & Greed: 12 (Extreme Fear) · CoinGecko votes bullish: 73.91% · headline tone (48h): +0

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 1,298 |
| Raydium AMM v4 | 696 |
| Orca Whirlpool | 1,298 |
| Pump.fun | 1,500 |
| Tensor | 0 |
| Magic Eden v2 | 244 |
| Marinade | 1 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,300,003 |
| Binance (cold) | 66 |
| OKX (attributed) | 59,503 |
| Coinbase (hot) | 55,196 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 217ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 100.0% of stake.
- **Agave**: latest release v4.4.1 · running 4.4.0 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 8380 ms |
| solana_rpc_validators | OK | 129 ms |
| coingecko | OK | 1752 ms |
| defillama_tvl | OK | 711 ms |
| defillama_dex | OK | 1155 ms |
| defillama_fees | OK | 1068 ms |
| defillama_stablecoins | OK | 125 ms |
| defillama_xstocks | FAILED | 48 ms |
| jito_kobe | OK | 143 ms |
| stakewiz | OK | 991 ms |
| github | OK | 983 ms |
| solana_com_news | FAILED | 87 ms |
| sentiment | OK | 2336 ms |
| solana_status_page | OK | 385 ms |
| solana_rpc_whales | OK | 969 ms |
| solana_rpc_programs | OK | 1672 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*