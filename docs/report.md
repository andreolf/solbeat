# Solbeat — State of the Solana Network

> Generated 2026-11-06T22:20:01Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1079 is 34% complete (~17h remaining), with the cluster processing ~2,131 TPS (2,131 non-vote). Measured slot time is 213ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $623.3K of Real Economic Value over the last 24h ($433/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $90.22 (+0.2% / 24h). Decentralization: Nakamoto coefficient 18, 659 active validators, 0.3% of stake delinquent. Alpenglow readiness: validators holding 100% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 1 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 466,274,813 |
| Block height | 444,293,746 |
| Epoch | 1079 (33.98% complete, ~16.9h left) |
| TPS (10 min avg) | 2,131 |
| Non-vote TPS | 2,131 |
| Slot time (measured) | 213.2 ms |
| Confirmation time (measured) | 0.21 s |
| Finality time (measured) | 0.21 s — **Alpenglow active** |
| Est. daily transactions | 181,813,620 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0027 |
| Node version | 4.4.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $90.22 (+0.2%/24h) |
| Market cap | $53.2B |
| **REV (24h)** | **$623.3K** (fees $499.4K + Jito tips $123.9K) |
| Chain TVL | $5.2B |
| Stablecoin supply | $15.0B |
| DEX volume (24h) | $2.2B (-7.8%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 590,342,556 SOL |
| Inflation | 3.57% |

Top DEXs by 24h volume: Orca DEX ($267.2M), BisonFi ($231.1M), Tessera V ($197.0M), PumpSwap ($188.6M), Raydium AMM ($172.8M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 659 / 37 |
| Delinquent stake | 0.32% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.6% |
| Avg / median commission | 12.7% / 5% |
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

**40/100 — Bearish** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 64.0 |
| fear greed | 28 |
| momentum | 37.4 |
| news | 18 |

Crypto Fear & Greed: 28 (Fear) · CoinGecko votes bullish: 64.0% · headline tone (48h): -4

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 1,464 |
| Raydium AMM v4 | 741 |
| Orca Whirlpool | 1,464 |
| Pump.fun | 1,500 |
| Tensor | 0 |
| Magic Eden v2 | 56 |
| Marinade | 1 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,300,003 |
| Binance (cold) | 66 |
| OKX (attributed) | 97,314 |
| Coinbase (hot) | 23,188 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 213ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 100.0% of stake.
- **Agave**: latest release v4.4.1 · running 4.4.0 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 10354 ms |
| solana_rpc_validators | OK | 233 ms |
| coingecko | OK | 1729 ms |
| defillama_tvl | OK | 95 ms |
| defillama_dex | OK | 1144 ms |
| defillama_fees | OK | 1991 ms |
| defillama_stablecoins | OK | 1164 ms |
| defillama_xstocks | FAILED | 46 ms |
| jito_kobe | OK | 185 ms |
| stakewiz | OK | 1335 ms |
| github | OK | 992 ms |
| solana_com_news | FAILED | 91 ms |
| sentiment | OK | 2428 ms |
| solana_status_page | OK | 287 ms |
| solana_rpc_whales | OK | 995 ms |
| solana_rpc_programs | OK | 1638 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*