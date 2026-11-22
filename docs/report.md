# Solbeat — State of the Solana Network

> Generated 2026-11-22T17:06:32Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1094 is 2% complete (~25h remaining), with the cluster processing ~1,801 TPS (1,801 non-vote). Measured slot time is 214ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $426.2K of Real Economic Value over the last 24h ($296/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $70.33 (-0.5% / 24h). Decentralization: Nakamoto coefficient 18, 661 active validators, 0.7% of stake delinquent. Alpenglow readiness: validators holding 100% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 4 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 472,618,519 |
| Block height | 450,632,272 |
| Epoch | 1094 (2.43% complete, ~25.1h left) |
| TPS (10 min avg) | 1,801 |
| Non-vote TPS | 1,801 |
| Slot time (measured) | 214.2 ms |
| Confirmation time (measured) | 0.21 s |
| Finality time (measured) | 0.21 s — **Alpenglow active** |
| Est. daily transactions | 110,972,593 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0029 |
| Node version | 4.4.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $70.33 (-0.5%/24h) |
| Market cap | $41.6B |
| **REV (24h)** | **$426.2K** (fees $317.1K + Jito tips $109.2K) |
| Chain TVL | $4.6B |
| Stablecoin supply | $13.3B |
| DEX volume (24h) | $1.3B (-28.6%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 592,017,133 SOL |
| Inflation | 3.54% |

Top DEXs by 24h volume: BisonFi ($153.4M), Orca DEX ($147.9M), Scorch ($127.9M), PumpSwap ($124.0M), Raydium AMM ($98.2M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 661 / 24 |
| Delinquent stake | 0.7% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 25.0% |
| Avg / median commission | 12.8% / 5% |
| Alpenglow BLS-key readiness | 670 validators, 100.0% of stake |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `he1iusunGwqrNtafDtLd…` | 16,918,440 | 3.97% | 0% |
| 2 | `CcaHc2L43ZWjwCHART3o…` | 16,346,959 | 3.84% | 7% |
| 3 | `3N7s9zXMZ4QqvHQR15t5…` | 12,401,889 | 2.91% | 0% |
| 4 | `8GbwASqdpw4dVcwbWUxb…` | 10,243,005 | 2.41% | 0% |
| 5 | `51JBzSTU5rAM8gLAVQKg…` | 9,842,253 | 2.31% | 10% |
| 6 | `CatzoSMUkTRidT5DwBxA…` | 9,612,896 | 2.26% | 5% |
| 7 | `26pV97Ce83ZQ6Kz9XT4t…` | 9,269,555 | 2.18% | 7% |
| 8 | `9QU2QSxhb24FUX3Tu2Fp…` | 7,998,895 | 1.88% | 7% |
| 9 | `DumiCKHVqoCQKD8roLAp…` | 6,987,495 | 1.64% | 0% |
| 10 | `CvSb7wdQAFpHuSpTYTJn…` | 6,775,083 | 1.59% | 5% |

## Signals (anomaly detection)

- **[WARNING]** TPS spike: 1,801 vs 12h mean 1,273 (z=+2.1)
- **[WARNING]** Solana TVL contraction (z=-2.2 vs its recent baseline)
- **[WARNING]** Stablecoin supply contraction (z=-3.0 vs its recent baseline)
- **[WARNING · liquidity_rotation]** Stablecoin supply and TVL moving together — capital rotating in or out of the chain.

## Solana Pulse — sentiment (experimental)

**44/100 — Neutral** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 71.9 |
| fear greed | 11 |
| momentum | 32.3 |
| news | 66 |

Crypto Fear & Greed: 11 (Extreme Fear) · CoinGecko votes bullish: 71.88% · headline tone (48h): +2

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 1,124 |
| Raydium AMM v4 | 450 |
| Orca Whirlpool | 1,124 |
| Pump.fun | 1,500 |
| Tensor | 0 |
| Magic Eden v2 | 18 |
| Marinade | 1 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,300,003 |
| Binance (cold) | 66 |
| OKX (attributed) | 120,739 |
| Coinbase (hot) | 53,064 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 214ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 100.0% of stake.
- **Agave**: latest release v4.4.1 · running 4.4.0 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 10953 ms |
| solana_rpc_validators | OK | 302 ms |
| coingecko | OK | 1686 ms |
| defillama_tvl | OK | 102 ms |
| defillama_dex | OK | 890 ms |
| defillama_fees | OK | 684 ms |
| defillama_stablecoins | OK | 123 ms |
| defillama_xstocks | FAILED | 58 ms |
| jito_kobe | OK | 376 ms |
| stakewiz | OK | 1059 ms |
| github | OK | 778 ms |
| solana_com_news | FAILED | 95 ms |
| sentiment | OK | 2306 ms |
| solana_status_page | OK | 265 ms |
| solana_rpc_whales | OK | 1275 ms |
| solana_rpc_programs | OK | 2002 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*