# Solbeat — State of the Solana Network

> Generated 2026-11-24T15:01:59Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1095 is 80% complete (~5h remaining), with the cluster processing ~2,091 TPS (2,091 non-vote). Measured slot time is 214ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $529.1K of Real Economic Value over the last 24h ($367/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $69.86 (-8.8% / 24h). Decentralization: Nakamoto coefficient 18, 661 active validators, 0.0% of stake delinquent. Alpenglow readiness: validators holding 100% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 1 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 473,387,309 |
| Block height | 451,400,439 |
| Epoch | 1095 (80.4% complete, ~5.0h left) |
| TPS (10 min avg) | 2,091 |
| Non-vote TPS | 2,091 |
| Slot time (measured) | 214.2 ms |
| Confirmation time (measured) | 0.21 s |
| Finality time (measured) | 0.21 s — **Alpenglow active** |
| Est. daily transactions | 158,385,854 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0027 |
| Node version | 4.4.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $69.86 (-8.8%/24h) |
| Market cap | $41.4B |
| **REV (24h)** | **$529.1K** (fees $424.1K + Jito tips $105.0K) |
| Chain TVL | $4.6B |
| Stablecoin supply | $13.8B |
| DEX volume (24h) | $1.8B (85.1%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 592,071,626 SOL |
| Inflation | 3.54% |

Top DEXs by 24h volume: Orca DEX ($282.0M), BisonFi ($204.1M), Meteora DLMM ($166.9M), Raydium AMM ($160.6M), Scorch ($159.2M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 661 / 25 |
| Delinquent stake | 0.01% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 25.0% |
| Avg / median commission | 13.1% / 5% |
| Alpenglow BLS-key readiness | 670 validators, 100.0% of stake |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `he1iusunGwqrNtafDtLd…` | 17,028,046 | 4.0% | 0% |
| 2 | `CcaHc2L43ZWjwCHART3o…` | 16,091,420 | 3.78% | 7% |
| 3 | `3N7s9zXMZ4QqvHQR15t5…` | 12,412,158 | 2.91% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxb…` | 10,240,508 | 2.4% | 0% |
| 5 | `51JBzSTU5rAM8gLAVQKg…` | 9,856,366 | 2.31% | 10% |
| 6 | `CatzoSMUkTRidT5DwBxA…` | 9,634,022 | 2.26% | 5% |
| 7 | `26pV97Ce83ZQ6Kz9XT4t…` | 9,276,354 | 2.18% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2Fp…` | 8,005,660 | 1.88% | 7% |
| 9 | `DumiCKHVqoCQKD8roLAp…` | 6,987,776 | 1.64% | 0% |
| 10 | `CvSb7wdQAFpHuSpTYTJn…` | 6,778,434 | 1.59% | 5% |

## Signals (anomaly detection)

- **[WARNING]** Solana TVL contraction (z=-2.2 vs its recent baseline)

## Solana Pulse — sentiment (experimental)

**42/100 — Neutral** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 54.8 |
| fear greed | 11 |
| momentum | 54.8 |
| news | 42 |

Crypto Fear & Greed: 11 (Extreme Fear) · CoinGecko votes bullish: 54.84% · headline tone (48h): -1

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 1,500 |
| Raydium AMM v4 | 1,500 |
| Orca Whirlpool | 1,500 |
| Pump.fun | 1,500 |
| Tensor | 0 |
| Magic Eden v2 | 36 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,300,003 |
| Binance (cold) | 66 |
| OKX (attributed) | 90,869 |
| Coinbase (hot) | 55,623 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 214ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 100.0% of stake.
- **Agave**: latest release v4.4.1 · running 4.4.0 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 23049 ms |
| solana_rpc_validators | OK | 1531 ms |
| coingecko | OK | 1838 ms |
| defillama_tvl | OK | 131 ms |
| defillama_dex | OK | 2199 ms |
| defillama_fees | OK | 1094 ms |
| defillama_stablecoins | OK | 113 ms |
| defillama_xstocks | FAILED | 61 ms |
| jito_kobe | OK | 252 ms |
| stakewiz | OK | 1301 ms |
| github | OK | 1044 ms |
| solana_com_news | FAILED | 87 ms |
| sentiment | OK | 2444 ms |
| solana_status_page | OK | 314 ms |
| solana_rpc_whales | OK | 4255 ms |
| solana_rpc_programs | OK | 9707 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*