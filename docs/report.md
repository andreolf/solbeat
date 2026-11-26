# Solbeat — State of the Solana Network

> Generated 2026-11-26T13:01:04Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1097 is 59% complete (~11h remaining), with the cluster processing ~1,213 TPS (1,213 non-vote). Measured slot time is 215ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $521.6K of Real Economic Value over the last 24h ($362/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $70.92 (+4.6% / 24h). Decentralization: Nakamoto coefficient 18, 657 active validators, 0.0% of stake delinquent. Alpenglow readiness: validators holding 100% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 3 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 474,157,350 |
| Block height | 452,170,208 |
| Epoch | 1097 (58.65% complete, ~10.7h left) |
| TPS (10 min avg) | 1,213 |
| Non-vote TPS | 1,213 |
| Slot time (measured) | 215.0 ms |
| Confirmation time (measured) | 0.21 s |
| Finality time (measured) | 0.21 s — **Alpenglow active** |
| Est. daily transactions | 108,886,988 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0038 |
| Node version | 4.4.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $70.92 (+4.6%/24h) |
| Market cap | $42.0B |
| **REV (24h)** | **$521.6K** (fees $415.3K + Jito tips $106.2K) |
| Chain TVL | $4.6B |
| Stablecoin supply | $13.3B |
| DEX volume (24h) | $1.5B (3.7%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 592,183,203 SOL |
| Inflation | 3.54% |

Top DEXs by 24h volume: Orca DEX ($213.2M), BisonFi ($190.6M), Raydium AMM ($147.0M), Meteora DLMM ($119.4M), Scorch ($104.6M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 657 / 31 |
| Delinquent stake | 0.03% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 25.0% |
| Avg / median commission | 13.2% / 5% |
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

- **[WARNING]** Solana TVL contraction (z=-2.0 vs its recent baseline)
- **[WARNING]** Stablecoin supply contraction (z=-2.5 vs its recent baseline)
- **[WARNING · liquidity_rotation]** Stablecoin supply and TVL moving together — capital rotating in or out of the chain.

## Solana Pulse — sentiment (experimental)

**46/100 — Neutral** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| momentum | 46.0 |
## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 611 |
| Raydium AMM v4 | 434 |
| Orca Whirlpool | 1,500 |
| Pump.fun | 1,500 |
| Tensor | 0 |
| Magic Eden v2 | 31 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,300,003 |
| Binance (cold) | 66 |
| OKX (attributed) | 59,504 |
| Coinbase (hot) | 58,467 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 215ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 100.0% of stake.
- **Agave**: latest release v4.4.1 · running 4.4.0 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 9709 ms |
| solana_rpc_validators | OK | 218 ms |
| coingecko | OK | 1666 ms |
| defillama_tvl | OK | 80 ms |
| defillama_dex | OK | 56 ms |
| defillama_fees | OK | 682 ms |
| defillama_stablecoins | OK | 111 ms |
| defillama_xstocks | FAILED | 39 ms |
| jito_kobe | OK | 337 ms |
| stakewiz | OK | 1150 ms |
| github | OK | 829 ms |
| solana_com_news | FAILED | 72 ms |
| sentiment | FAILED | 2106 ms |
| solana_status_page | OK | 238 ms |
| solana_rpc_whales | OK | 1074 ms |
| solana_rpc_programs | OK | 2052 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*