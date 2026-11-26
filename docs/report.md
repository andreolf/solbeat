# Solbeat — State of the Solana Network

> Generated 2026-11-26T20:32:58Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1097 is 88% complete (~3h remaining), with the cluster processing ~2,141 TPS (2,141 non-vote). Measured slot time is 215ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $522.2K of Real Economic Value over the last 24h ($363/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $71.33 (+1.6% / 24h). Decentralization: Nakamoto coefficient 18, 657 active validators, 0.0% of stake delinquent. Alpenglow readiness: validators holding 100% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 1 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 474,283,354 |
| Block height | 452,296,164 |
| Epoch | 1097 (87.81% complete, ~3.1h left) |
| TPS (10 min avg) | 2,141 |
| Non-vote TPS | 2,141 |
| Slot time (measured) | 214.9 ms |
| Confirmation time (measured) | 0.21 s |
| Finality time (measured) | 0.21 s — **Alpenglow active** |
| Est. daily transactions | 166,128,003 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0025 |
| Node version | 4.4.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $71.33 (+1.6%/24h) |
| Market cap | $42.2B |
| **REV (24h)** | **$522.2K** (fees $415.3K + Jito tips $106.9K) |
| Chain TVL | $4.6B |
| Stablecoin supply | $13.3B |
| DEX volume (24h) | $1.5B (3.7%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 592,183,069 SOL |
| Inflation | 3.54% |

Top DEXs by 24h volume: BisonFi ($190.6M), Orca DEX ($168.5M), Raydium AMM ($127.0M), Meteora DLMM ($119.4M), Scorch ($104.6M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 657 / 31 |
| Delinquent stake | 0.03% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 25.0% |
| Avg / median commission | 13.2% / 5% |
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

**45/100 — Neutral** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 69.6 |
| fear greed | 11 |
| momentum | 47.5 |
| news | 50 |

Crypto Fear & Greed: 11 (Extreme Fear) · CoinGecko votes bullish: 69.57% · headline tone (48h): +0

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 1,217 |
| Raydium AMM v4 | 464 |
| Orca Whirlpool | 1,500 |
| Pump.fun | 1,500 |
| Tensor | 0 |
| Magic Eden v2 | 22 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,300,003 |
| Binance (cold) | 66 |
| OKX (attributed) | 59,504 |
| Coinbase (hot) | 56,155 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 215ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 100.0% of stake.
- **Agave**: latest release v4.4.1 · running 4.4.0 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 8449 ms |
| solana_rpc_validators | OK | 137 ms |
| coingecko | OK | 1808 ms |
| defillama_tvl | OK | 83 ms |
| defillama_dex | OK | 1144 ms |
| defillama_fees | OK | 113 ms |
| defillama_stablecoins | OK | 146 ms |
| defillama_xstocks | FAILED | 779 ms |
| jito_kobe | OK | 130 ms |
| stakewiz | OK | 1400 ms |
| github | OK | 969 ms |
| solana_com_news | FAILED | 96 ms |
| sentiment | OK | 2565 ms |
| solana_status_page | OK | 330 ms |
| solana_rpc_whales | OK | 942 ms |
| solana_rpc_programs | OK | 1684 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*