# Solbeat — State of the Solana Network

> Generated 2026-10-29T20:54:07Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1071 is 81% complete (~5h remaining), with the cluster processing ~4,218 TPS (4,218 non-vote). Measured slot time is 213ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $653.1K of Real Economic Value over the last 24h ($454/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $96.54 (-5.5% / 24h). Decentralization: Nakamoto coefficient 18, 666 active validators, 0.7% of stake delinquent. Alpenglow readiness: validators holding 100% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 1 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 463,022,810 |
| Block height | 441,046,058 |
| Epoch | 1071 (81.21% complete, ~4.8h left) |
| TPS (10 min avg) | 4,218 |
| Non-vote TPS | 4,218 |
| Slot time (measured) | 212.9 ms |
| Confirmation time (measured) | 0.21 s |
| Finality time (measured) | 0.21 s — **Alpenglow active** |
| Est. daily transactions | 214,217,526 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0025 |
| Node version | 4.3.2 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $96.54 (-5.5%/24h) |
| Market cap | $57.1B |
| **REV (24h)** | **$653.1K** (fees $527.1K + Jito tips $126.0K) |
| Chain TVL | $5.7B |
| Stablecoin supply | $15.6B |
| DEX volume (24h) | $1.7B (9.5%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 589,983,619 SOL |
| Inflation | 3.58% |

Top DEXs by 24h volume: Orca DEX ($245.7M), BisonFi ($205.5M), Raydium AMM ($171.3M), Manifest Trade ($155.0M), Tessera V ($148.2M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 666 / 23 |
| Delinquent stake | 0.74% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.5% |
| Avg / median commission | 13.0% / 5.0% |
| Alpenglow BLS-key readiness | 679 validators, 100.0% of stake |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L43ZWjwCHART3o…` | 17,028,574 | 3.9% | 7% |
| 2 | `he1iusunGwqrNtafDtLd…` | 16,665,444 | 3.82% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5…` | 12,878,826 | 2.95% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxb…` | 10,762,073 | 2.46% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxA…` | 9,705,356 | 2.22% | 5% |
| 6 | `51JBzSTU5rAM8gLAVQKg…` | 9,466,646 | 2.17% | 10% |
| 7 | `26pV97Ce83ZQ6Kz9XT4t…` | 9,218,110 | 2.11% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2Fp…` | 7,761,555 | 1.78% | 7% |
| 9 | `DumiCKHVqoCQKD8roLAp…` | 6,998,037 | 1.6% | 0% |
| 10 | `CvSb7wdQAFpHuSpTYTJn…` | 6,646,428 | 1.52% | 5% |

## Signals (anomaly detection)

- **[WARNING]** TPS spike: 4,218 vs 12h mean 2,412 (z=+2.9)

## Solana Pulse — sentiment (experimental)

**60/100 — Bullish** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 85.7 |
| fear greed | 51 |
| momentum | 42.8 |
| news | 58 |

Crypto Fear & Greed: 51 (Neutral) · CoinGecko votes bullish: 85.71% · headline tone (48h): +1

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 1,331 |
| Raydium AMM v4 | 1,331 |
| Orca Whirlpool | 1,331 |
| Pump.fun | 1,500 |
| Tensor | 0 |
| Magic Eden v2 | 293 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 11,734,974 |
| Binance (cold) | 127,798 |
| OKX (attributed) | 330,876 |
| Coinbase (hot) | 11,657 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 213ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 100.0% of stake.
- **Agave**: latest release v4.4.0 · running 4.3.2 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 10734 ms |
| solana_rpc_validators | OK | 95 ms |
| coingecko | OK | 1642 ms |
| defillama_tvl | OK | 153 ms |
| defillama_dex | OK | 778 ms |
| defillama_fees | OK | 946 ms |
| defillama_stablecoins | OK | 195 ms |
| defillama_xstocks | FAILED | 40 ms |
| jito_kobe | OK | 181 ms |
| stakewiz | OK | 668 ms |
| github | OK | 578 ms |
| solana_com_news | FAILED | 162 ms |
| sentiment | OK | 2013 ms |
| solana_status_page | OK | 565 ms |
| solana_rpc_whales | OK | 833 ms |
| solana_rpc_programs | OK | 1423 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*