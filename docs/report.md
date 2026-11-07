# Solbeat — State of the Solana Network

> Generated 2026-11-07T14:23:35Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1079 is 96% complete (~1h remaining), with the cluster processing ~1,369 TPS (1,369 non-vote). Measured slot time is 213ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $590.3K of Real Economic Value over the last 24h ($410/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $89.88 (-0.2% / 24h). Decentralization: Nakamoto coefficient 18, 658 active validators, 0.4% of stake delinquent. Alpenglow readiness: validators holding 100% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 1 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 466,544,643 |
| Block height | 444,563,284 |
| Epoch | 1079 (96.45% complete, ~0.9h left) |
| TPS (10 min avg) | 1,369 |
| Non-vote TPS | 1,369 |
| Slot time (measured) | 213.2 ms |
| Confirmation time (measured) | 0.21 s |
| Finality time (measured) | 0.21 s — **Alpenglow active** |
| Est. daily transactions | 98,425,307 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0047 |
| Node version | 4.4.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $89.88 (-0.2%/24h) |
| Market cap | $53.1B |
| **REV (24h)** | **$590.3K** (fees $466.9K + Jito tips $123.4K) |
| Chain TVL | $5.2B |
| Stablecoin supply | $14.8B |
| DEX volume (24h) | $1.5B (-32.7%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 590,982,496 SOL |
| Inflation | 3.57% |

Top DEXs by 24h volume: BisonFi ($170.2M), Orca DEX ($169.5M), Tessera V ($153.4M), Meteora DLMM ($128.6M), Raydium AMM ($108.8M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 658 / 38 |
| Delinquent stake | 0.36% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.6% |
| Avg / median commission | 12.9% / 5.0% |
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

**37/100 — Bearish** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 56.2 |
| fear greed | 25 |
| momentum | 24.8 |
| news | 42 |

Crypto Fear & Greed: 25 (Extreme Fear) · CoinGecko votes bullish: 56.25% · headline tone (48h): -1

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 1,500 |
| Raydium AMM v4 | 584 |
| Orca Whirlpool | 1,500 |
| Pump.fun | 1,500 |
| Tensor | 0 |
| Magic Eden v2 | 35 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,300,003 |
| Binance (cold) | 66 |
| OKX (attributed) | 97,315 |
| Coinbase (hot) | 18,999 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 213ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 100.0% of stake.
- **Agave**: latest release v4.4.1 · running 4.4.0 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 8828 ms |
| solana_rpc_validators | OK | 217 ms |
| coingecko | OK | 1633 ms |
| defillama_tvl | OK | 42 ms |
| defillama_dex | OK | 1147 ms |
| defillama_fees | OK | 464 ms |
| defillama_stablecoins | OK | 56 ms |
| defillama_xstocks | FAILED | 776 ms |
| jito_kobe | OK | 144 ms |
| stakewiz | OK | 1443 ms |
| github | OK | 750 ms |
| solana_com_news | FAILED | 42 ms |
| sentiment | OK | 2111 ms |
| solana_status_page | OK | 177 ms |
| solana_rpc_whales | OK | 1309 ms |
| solana_rpc_programs | OK | 1932 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*