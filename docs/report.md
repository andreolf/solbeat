# Solbeat — State of the Solana Network

> Generated 2026-11-26T06:55:06Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1097 is 35% complete (~17h remaining), with the cluster processing ~1,292 TPS (1,292 non-vote). Measured slot time is 216ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $520.4K of Real Economic Value over the last 24h ($361/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $70.56 (+2.5% / 24h). Decentralization: Nakamoto coefficient 18, 657 active validators, 0.0% of stake delinquent. Alpenglow readiness: validators holding 100% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 1 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 474,055,153 |
| Block height | 452,068,045 |
| Epoch | 1097 (34.99% complete, ~16.9h left) |
| TPS (10 min avg) | 1,292 |
| Non-vote TPS | 1,292 |
| Slot time (measured) | 216.3 ms |
| Confirmation time (measured) | 0.22 s |
| Finality time (measured) | 0.22 s — **Alpenglow active** |
| Est. daily transactions | 133,463,663 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0031 |
| Node version | 4.4.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $70.56 (+2.5%/24h) |
| Market cap | $41.8B |
| **REV (24h)** | **$520.4K** (fees $415.3K + Jito tips $105.0K) |
| Chain TVL | $4.6B |
| Stablecoin supply | $13.3B |
| DEX volume (24h) | $1.5B (0.9%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 592,183,275 SOL |
| Inflation | 3.54% |

Top DEXs by 24h volume: Orca DEX ($217.1M), BisonFi ($190.5M), Raydium AMM ($161.6M), Scorch ($134.1M), Meteora DLMM ($113.0M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 657 / 31 |
| Delinquent stake | 0.03% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 25.0% |
| Avg / median commission | 13.1% / 5% |
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

**46/100 — Neutral** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 68.4 |
| fear greed | 11 |
| momentum | 44.4 |
| news | 66 |

Crypto Fear & Greed: 11 (Extreme Fear) · CoinGecko votes bullish: 68.42% · headline tone (48h): +2

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 902 |
| Raydium AMM v4 | 563 |
| Orca Whirlpool | 902 |
| Pump.fun | 1,500 |
| Tensor | 1 |
| Magic Eden v2 | 16 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,300,003 |
| Binance (cold) | 66 |
| OKX (attributed) | 59,504 |
| Coinbase (hot) | 51,300 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 216ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 100.0% of stake.
- **Agave**: latest release v4.4.1 · running 4.4.0 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 9964 ms |
| solana_rpc_validators | OK | 161 ms |
| coingecko | OK | 1674 ms |
| defillama_tvl | OK | 165 ms |
| defillama_dex | OK | 787 ms |
| defillama_fees | OK | 703 ms |
| defillama_stablecoins | OK | 660 ms |
| defillama_xstocks | FAILED | 36 ms |
| jito_kobe | OK | 292 ms |
| stakewiz | OK | 683 ms |
| github | OK | 876 ms |
| solana_com_news | FAILED | 52 ms |
| sentiment | OK | 2190 ms |
| solana_status_page | OK | 234 ms |
| solana_rpc_whales | OK | 909 ms |
| solana_rpc_programs | OK | 1495 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*