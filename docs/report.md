# Solbeat — State of the Solana Network

> Generated 2026-11-25T22:53:17Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1097 is 4% complete (~25h remaining), with the cluster processing ~3,050 TPS (3,050 non-vote). Measured slot time is 215ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $471.3K of Real Economic Value over the last 24h ($327/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $70.49 (+0.9% / 24h). Decentralization: Nakamoto coefficient 18, 655 active validators, 0.1% of stake delinquent. Alpenglow readiness: validators holding 100% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 3 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 473,920,685 |
| Block height | 451,933,623 |
| Epoch | 1097 (3.86% complete, ~24.8h left) |
| TPS (10 min avg) | 3,050 |
| Non-vote TPS | 3,050 |
| Slot time (measured) | 215.4 ms |
| Confirmation time (measured) | 0.22 s |
| Finality time (measured) | 0.22 s — **Alpenglow active** |
| Est. daily transactions | 212,068,587 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0017 |
| Node version | 4.4.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $70.49 (+0.9%/24h) |
| Market cap | $41.8B |
| **REV (24h)** | **$471.3K** (fees $366.0K + Jito tips $105.4K) |
| Chain TVL | $4.6B |
| Stablecoin supply | $13.4B |
| DEX volume (24h) | $1.5B (-19.3%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 592,183,465 SOL |
| Inflation | 3.54% |

Top DEXs by 24h volume: Orca DEX ($210.4M), BisonFi ($190.5M), Raydium AMM ($183.9M), Manifest Trade ($139.7M), Scorch ($134.1M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 655 / 33 |
| Delinquent stake | 0.06% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 25.0% |
| Avg / median commission | 13.0% / 5% |
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

- **[WARNING]** Solana TVL contraction (z=-2.1 vs its recent baseline)
- **[WARNING]** Stablecoin supply contraction (z=-2.4 vs its recent baseline)
- **[WARNING · liquidity_rotation]** Stablecoin supply and TVL moving together — capital rotating in or out of the chain.

## Solana Pulse — sentiment (experimental)

**43/100 — Neutral** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 67.4 |
| fear greed | 13 |
| momentum | 31.2 |
| news | 66 |

Crypto Fear & Greed: 13 (Extreme Fear) · CoinGecko votes bullish: 67.44% · headline tone (48h): +2

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 1,316 |
| Raydium AMM v4 | 362 |
| Orca Whirlpool | 1,500 |
| Pump.fun | 1,500 |
| Tensor | 0 |
| Magic Eden v2 | 18 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,300,003 |
| Binance (cold) | 66 |
| OKX (attributed) | 59,504 |
| Coinbase (hot) | 15,800 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 215ms.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 100.0% of stake.
- **Agave**: latest release None · running 4.4.0 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 10155 ms |
| solana_rpc_validators | OK | 249 ms |
| coingecko | OK | 1754 ms |
| defillama_tvl | OK | 58 ms |
| defillama_dex | OK | 595 ms |
| defillama_fees | OK | 1022 ms |
| defillama_stablecoins | OK | 809 ms |
| defillama_xstocks | FAILED | 35 ms |
| jito_kobe | OK | 119 ms |
| stakewiz | OK | 1436 ms |
| github | FAILED | 6142 ms |
| solana_com_news | FAILED | 53 ms |
| sentiment | OK | 2316 ms |
| solana_status_page | OK | 201 ms |
| solana_rpc_whales | OK | 1067 ms |
| solana_rpc_programs | OK | 1866 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*