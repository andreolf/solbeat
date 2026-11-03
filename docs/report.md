# Solbeat — State of the Solana Network

> Generated 2026-11-03T03:32:50Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1075 is 81% complete (~5h remaining), with the cluster processing ~1,617 TPS (1,617 non-vote). Measured slot time is 213ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. SOL trades at $91.80 (-3.9% / 24h). Decentralization: Nakamoto coefficient 18, 665 active validators, 1.0% of stake delinquent. Alpenglow readiness: validators holding 100% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: all clear across every monitored metric.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 464,748,591 |
| Block height | 442,769,665 |
| Epoch | 1075 (80.69% complete, ~4.9h left) |
| TPS (10 min avg) | 1,617 |
| Non-vote TPS | 1,617 |
| Slot time (measured) | 212.6 ms |
| Confirmation time (measured) | 0.21 s |
| Finality time (measured) | 0.21 s — **Alpenglow active** |
| Est. daily transactions | 146,505,991 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0000 |
| Node version | 4.3.2 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $91.80 (-3.9%/24h) |
| Market cap | $54.2B |
| **REV (24h)** | **n/a** (fees n/a + Jito tips n/a) |
| Chain TVL | n/a |
| Stablecoin supply | n/a |
| DEX volume (24h) | n/a (None%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 590,206,261 SOL |
| Inflation | 3.57% |

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 665 / 28 |
| Delinquent stake | 1.01% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.7% |
| Avg / median commission | 12.8% / 5% |
| Alpenglow BLS-key readiness | 680 validators, 100.0% of stake |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L43ZWjwCHART3o…` | 17,034,354 | 3.92% | 7% |
| 2 | `he1iusunGwqrNtafDtLd…` | 16,710,199 | 3.85% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5…` | 13,037,180 | 3.0% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxb…` | 10,429,501 | 2.4% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxA…` | 9,580,109 | 2.21% | 5% |
| 6 | `51JBzSTU5rAM8gLAVQKg…` | 9,453,055 | 2.18% | 10% |
| 7 | `26pV97Ce83ZQ6Kz9XT4t…` | 9,226,805 | 2.13% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2Fp…` | 7,803,392 | 1.8% | 7% |
| 9 | `DumiCKHVqoCQKD8roLAp…` | 7,001,891 | 1.61% | 0% |
| 10 | `CvSb7wdQAFpHuSpTYTJn…` | 6,978,080 | 1.61% | 5% |

## Signals (anomaly detection)

All clear — no anomalies across monitored metrics.

## Solana Pulse — sentiment (experimental)

**42/100 — Neutral** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 71.4 |
| fear greed | 26 |
| momentum | 22.1 |
| news | 50 |

Crypto Fear & Greed: 26 (Fear) · CoinGecko votes bullish: 71.43% · headline tone (48h): +0

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 959 |
| Raydium AMM v4 | 585 |
| Orca Whirlpool | 959 |
| Pump.fun | 1,500 |
| Tensor | 0 |
| Magic Eden v2 | 54 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,890,003 |
| Binance (cold) | 4 |
| OKX (attributed) | 339,502 |
| Coinbase (hot) | 14,638 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 213ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 100.0% of stake.
- **Agave**: latest release v4.4.0 · running 4.3.2 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 9300 ms |
| solana_rpc_validators | OK | 176 ms |
| coingecko | OK | 1897 ms |
| defillama_tvl | FAILED | 85538 ms |
| defillama_dex | FAILED | 66134 ms |
| defillama_fees | FAILED | 66129 ms |
| defillama_stablecoins | FAILED | 66934 ms |
| defillama_xstocks | FAILED | 66189 ms |
| jito_kobe | OK | 474 ms |
| stakewiz | OK | 1118 ms |
| github | OK | 941 ms |
| solana_com_news | FAILED | 147 ms |
| sentiment | OK | 2385 ms |
| solana_status_page | OK | 295 ms |
| solana_rpc_whales | OK | 1097 ms |
| solana_rpc_programs | OK | 1659 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*