# Solbeat — State of the Solana Network

> Generated 2026-11-07T04:22:44Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1079 is 57% complete (~11h remaining), with the cluster processing ~1,507 TPS (1,507 non-vote). Measured slot time is 214ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $590.2K of Real Economic Value over the last 24h ($410/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $89.92 (+0.8% / 24h). Decentralization: Nakamoto coefficient 18, 657 active validators, 0.3% of stake delinquent. Alpenglow readiness: validators holding 100% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 1 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 466,376,332 |
| Block height | 444,395,109 |
| Epoch | 1079 (57.48% complete, ~10.9h left) |
| TPS (10 min avg) | 1,507 |
| Non-vote TPS | 1,507 |
| Slot time (measured) | 213.5 ms |
| Confirmation time (measured) | 0.21 s |
| Finality time (measured) | 0.21 s — **Alpenglow active** |
| Est. daily transactions | 138,522,502 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0034 |
| Node version | 4.4.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $89.92 (+0.8%/24h) |
| Market cap | $53.1B |
| **REV (24h)** | **$590.2K** (fees $466.9K + Jito tips $123.3K) |
| Chain TVL | $5.2B |
| Stablecoin supply | $14.8B |
| DEX volume (24h) | $1.9B (-15.6%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 590,982,612 SOL |
| Inflation | 3.57% |

Top DEXs by 24h volume: BisonFi ($231.1M), Orca DEX ($229.4M), Tessera V ($197.0M), Meteora DLMM ($172.6M), Raydium AMM ($155.6M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 657 / 39 |
| Delinquent stake | 0.3% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.6% |
| Avg / median commission | 12.6% / 5% |
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

- **[SERIOUS]** Stablecoin supply contraction (z=-3.0 vs its recent baseline)

## Solana Pulse — sentiment (experimental)

**40/100 — Bearish** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 70.0 |
| fear greed | 25 |
| momentum | 32.3 |
| news | 18 |

Crypto Fear & Greed: 25 (Extreme Fear) · CoinGecko votes bullish: 70.0% · headline tone (48h): -4

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 1,500 |
| Raydium AMM v4 | 530 |
| Orca Whirlpool | 1,500 |
| Pump.fun | 1,500 |
| Tensor | 0 |
| Magic Eden v2 | 40 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,300,003 |
| Binance (cold) | 66 |
| OKX (attributed) | 97,314 |
| Coinbase (hot) | 23,437 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 214ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 100.0% of stake.
- **Agave**: latest release v4.4.1 · running 4.4.0 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 8847 ms |
| solana_rpc_validators | OK | 94 ms |
| coingecko | OK | 1674 ms |
| defillama_tvl | OK | 137 ms |
| defillama_dex | OK | 772 ms |
| defillama_fees | OK | 2819 ms |
| defillama_stablecoins | OK | 158 ms |
| defillama_xstocks | FAILED | 143 ms |
| jito_kobe | OK | 82 ms |
| stakewiz | OK | 913 ms |
| github | OK | 567 ms |
| solana_com_news | FAILED | 32 ms |
| sentiment | OK | 2015 ms |
| solana_status_page | OK | 315 ms |
| solana_rpc_whales | OK | 918 ms |
| solana_rpc_programs | OK | 1676 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*