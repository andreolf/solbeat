# Solbeat — State of the Solana Network

> Generated 2026-11-26T23:35:28Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1097 is 100% complete (~0h remaining), with the cluster processing ~1,729 TPS (1,729 non-vote). Measured slot time is 216ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $521.1K of Real Economic Value over the last 24h ($362/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $70.87 (+0.8% / 24h). Decentralization: Nakamoto coefficient 18, 656 active validators, 0.0% of stake delinquent. Alpenglow readiness: validators holding 100% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 1 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 474,334,289 |
| Block height | 452,347,075 |
| Epoch | 1097 (99.6% complete, ~0.1h left) |
| TPS (10 min avg) | 1,729 |
| Non-vote TPS | 1,729 |
| Slot time (measured) | 215.8 ms |
| Confirmation time (measured) | 0.22 s |
| Finality time (measured) | 0.22 s — **Alpenglow active** |
| Est. daily transactions | 156,649,714 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0027 |
| Node version | 4.4.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $70.87 (+0.8%/24h) |
| Market cap | $42.0B |
| **REV (24h)** | **$521.1K** (fees $415.3K + Jito tips $105.8K) |
| Chain TVL | $4.6B |
| Stablecoin supply | $13.3B |
| DEX volume (24h) | $1.5B (3.7%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 592,183,016 SOL |
| Inflation | 3.54% |

Top DEXs by 24h volume: BisonFi ($190.6M), Orca DEX ($135.1M), Meteora DLMM ($119.4M), Raydium AMM ($117.2M), Scorch ($104.6M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 656 / 32 |
| Delinquent stake | 0.04% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 25.0% |
| Avg / median commission | 13.3% / 5.0% |
| Alpenglow BLS-key readiness | 670 validators, 100.0% of stake |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `he1iusunGwqrNtafDtLd…` | 16,805,000 | 3.97% | 0% |
| 2 | `CcaHc2L43ZWjwCHART3o…` | 15,814,431 | 3.73% | 7% |
| 3 | `3N7s9zXMZ4QqvHQR15t5…` | 12,430,859 | 2.93% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxb…` | 10,236,589 | 2.42% | 0% |
| 5 | `51JBzSTU5rAM8gLAVQKg…` | 9,910,258 | 2.34% | 10% |
| 6 | `CatzoSMUkTRidT5DwBxA…` | 9,615,394 | 2.27% | 5% |
| 7 | `26pV97Ce83ZQ6Kz9XT4t…` | 9,281,563 | 2.19% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2Fp…` | 8,032,075 | 1.9% | 7% |
| 9 | `DumiCKHVqoCQKD8roLAp…` | 6,971,305 | 1.65% | 0% |
| 10 | `CvSb7wdQAFpHuSpTYTJn…` | 6,740,287 | 1.59% | 5% |

## Signals (anomaly detection)

- **[WARNING]** Stablecoin supply contraction (z=-2.5 vs its recent baseline)

## Solana Pulse — sentiment (experimental)

**48/100 — Neutral** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 77.3 |
| fear greed | 11 |
| momentum | 47.0 |
| news | 50 |

Crypto Fear & Greed: 11 (Extreme Fear) · CoinGecko votes bullish: 77.27% · headline tone (48h): +0

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 715 |
| Raydium AMM v4 | 715 |
| Orca Whirlpool | 1,366 |
| Pump.fun | 1,500 |
| Tensor | 0 |
| Magic Eden v2 | 27 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,300,003 |
| Binance (cold) | 66 |
| OKX (attributed) | 59,503 |
| Coinbase (hot) | 55,324 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 216ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 100.0% of stake.
- **Agave**: latest release v4.4.1 · running 4.4.0 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 8861 ms |
| solana_rpc_validators | OK | 138 ms |
| coingecko | OK | 1752 ms |
| defillama_tvl | OK | 75 ms |
| defillama_dex | OK | 1138 ms |
| defillama_fees | OK | 1044 ms |
| defillama_stablecoins | OK | 855 ms |
| defillama_xstocks | FAILED | 782 ms |
| jito_kobe | OK | 130 ms |
| stakewiz | OK | 1337 ms |
| github | OK | 979 ms |
| solana_com_news | FAILED | 84 ms |
| sentiment | OK | 2330 ms |
| solana_status_page | OK | 245 ms |
| solana_rpc_whales | OK | 981 ms |
| solana_rpc_programs | OK | 1708 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*