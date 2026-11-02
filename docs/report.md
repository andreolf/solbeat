# Solbeat — State of the Solana Network

> Generated 2026-11-02T10:36:46Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1075 is 15% complete (~22h remaining), with the cluster processing ~1,267 TPS (1,267 non-vote). Measured slot time is 214ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $455.3K of Real Economic Value over the last 24h ($316/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $94.11 (-1.3% / 24h). Decentralization: Nakamoto coefficient 18, 664 active validators, 1.1% of stake delinquent. Alpenglow readiness: validators holding 100% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 2 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 464,464,100 |
| Block height | 442,485,254 |
| Epoch | 1075 (14.84% complete, ~21.9h left) |
| TPS (10 min avg) | 1,267 |
| Non-vote TPS | 1,267 |
| Slot time (measured) | 214.2 ms |
| Confirmation time (measured) | 0.21 s |
| Finality time (measured) | 0.21 s — **Alpenglow active** |
| Est. daily transactions | 111,193,823 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0033 |
| Node version | 4.3.2 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $94.11 (-1.3%/24h) |
| Market cap | $55.5B |
| **REV (24h)** | **$455.3K** (fees $367.7K + Jito tips $87.6K) |
| Chain TVL | $5.5B |
| Stablecoin supply | $15.4B |
| DEX volume (24h) | $832.7M (-12.7%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 590,205,948 SOL |
| Inflation | 3.57% |

Top DEXs by 24h volume: PumpSwap ($122.9M), Orca DEX ($121.0M), pump.fun ($103.8M), Raydium AMM ($74.2M), GoonFi ($73.9M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 664 / 30 |
| Delinquent stake | 1.05% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.7% |
| Avg / median commission | 12.7% / 5.0% |
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

- **[WARNING]** DEX volume contraction (z=-2.1 vs its recent baseline)
- **[WARNING]** Real Economic Value deviating from its run-history baseline (z=-2.0)

## Solana Pulse — sentiment (experimental)

**51/100 — Neutral** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 73.1 |
| fear greed | 37 |
| momentum | 33.0 |
| news | 66 |

Crypto Fear & Greed: 37 (Fear) · CoinGecko votes bullish: 73.08% · headline tone (48h): +2

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 997 |
| Raydium AMM v4 | 599 |
| Orca Whirlpool | 1,500 |
| Pump.fun | 1,500 |
| Tensor | 1 |
| Magic Eden v2 | 86 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,890,003 |
| Binance (cold) | 4 |
| OKX (attributed) | 339,502 |
| Coinbase (hot) | 37,670 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 214ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 100.0% of stake.
- **Agave**: latest release v4.4.0 · running 4.3.2 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 10086 ms |
| solana_rpc_validators | OK | 299 ms |
| coingecko | OK | 1641 ms |
| defillama_tvl | OK | 827 ms |
| defillama_dex | OK | 964 ms |
| defillama_fees | OK | 1532 ms |
| defillama_stablecoins | OK | 694 ms |
| defillama_xstocks | FAILED | 631 ms |
| jito_kobe | OK | 245 ms |
| stakewiz | OK | 1074 ms |
| github | OK | 807 ms |
| solana_com_news | FAILED | 98 ms |
| sentiment | OK | 2155 ms |
| solana_status_page | OK | 223 ms |
| solana_rpc_whales | OK | 1084 ms |
| solana_rpc_programs | OK | 1861 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*