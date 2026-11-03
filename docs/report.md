# Solbeat — State of the Solana Network

> Generated 2026-11-03T13:29:13Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1076 is 19% complete (~21h remaining), with the cluster processing ~1,956 TPS (1,956 non-vote). Measured slot time is 214ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $593.3K of Real Economic Value over the last 24h ($412/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $92.58 (-1.3% / 24h). Decentralization: Nakamoto coefficient 18, 664 active validators, 0.5% of stake delinquent. Alpenglow readiness: validators holding 100% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 1 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 464,915,946 |
| Block height | 442,936,722 |
| Epoch | 1076 (19.43% complete, ~20.7h left) |
| TPS (10 min avg) | 1,956 |
| Non-vote TPS | 1,956 |
| Slot time (measured) | 214.4 ms |
| Confirmation time (measured) | 0.21 s |
| Finality time (measured) | 0.21 s — **Alpenglow active** |
| Est. daily transactions | 119,932,867 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0040 |
| Node version | 4.3.2 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $92.58 (-1.3%/24h) |
| Market cap | $54.7B |
| **REV (24h)** | **$593.3K** (fees $482.2K + Jito tips $111.1K) |
| Chain TVL | $5.4B |
| Stablecoin supply | $15.3B |
| DEX volume (24h) | $1.8B (102.2%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 590,262,005 SOL |
| Inflation | 3.57% |

Top DEXs by 24h volume: PumpSwap ($261.1M), BisonFi ($250.5M), Orca DEX ($212.2M), Tessera V ($149.8M), pump.fun ($123.1M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 664 / 29 |
| Delinquent stake | 0.51% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.7% |
| Avg / median commission | 12.7% / 5.0% |
| Alpenglow BLS-key readiness | 680 validators, 100.0% of stake |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L43ZWjwCHART3o…` | 17,030,641 | 3.92% | 7% |
| 2 | `he1iusunGwqrNtafDtLd…` | 16,704,340 | 3.84% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5…` | 13,043,664 | 3.0% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxb…` | 10,431,126 | 2.4% | 0% |
| 5 | `CatzoSMUkTRidT5DwBxA…` | 9,561,007 | 2.2% | 5% |
| 6 | `51JBzSTU5rAM8gLAVQKg…` | 9,435,905 | 2.17% | 10% |
| 7 | `26pV97Ce83ZQ6Kz9XT4t…` | 9,232,746 | 2.12% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2Fp…` | 7,814,810 | 1.8% | 7% |
| 9 | `DumiCKHVqoCQKD8roLAp…` | 7,008,986 | 1.61% | 0% |
| 10 | `CvSb7wdQAFpHuSpTYTJn…` | 6,979,031 | 1.61% | 5% |

## Signals (anomaly detection)

- **[WARNING]** TPS spike: 1,956 vs 12h mean 1,375 (z=+2.8)

## Solana Pulse — sentiment (experimental)

**50/100 — Neutral** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 69.7 |
| fear greed | 26 |
| momentum | 51.8 |
| news | 50 |

Crypto Fear & Greed: 26 (Fear) · CoinGecko votes bullish: 69.7% · headline tone (48h): +0

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 1,500 |
| Raydium AMM v4 | 1,500 |
| Orca Whirlpool | 1,500 |
| Pump.fun | 1,500 |
| Tensor | 2 |
| Magic Eden v2 | 63 |
| Marinade | 1 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,890,003 |
| Binance (cold) | 4 |
| OKX (attributed) | 339,403 |
| Coinbase (hot) | 15,054 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 214ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 100.0% of stake.
- **Agave**: latest release v4.4.0 · running 4.3.2 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 11403 ms |
| solana_rpc_validators | OK | 219 ms |
| coingecko | OK | 1777 ms |
| defillama_tvl | OK | 135 ms |
| defillama_dex | OK | 515 ms |
| defillama_fees | OK | 275 ms |
| defillama_stablecoins | OK | 309 ms |
| defillama_xstocks | FAILED | 3184 ms |
| jito_kobe | OK | 173 ms |
| stakewiz | OK | 1066 ms |
| github | OK | 901 ms |
| solana_com_news | FAILED | 97 ms |
| sentiment | OK | 2232 ms |
| solana_status_page | OK | 261 ms |
| solana_rpc_whales | OK | 1152 ms |
| solana_rpc_programs | OK | 1941 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*