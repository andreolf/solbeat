# Solbeat — State of the Solana Network

> Generated 2026-09-20T16:27:27Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1038 is 86% complete (~5h remaining), with the cluster processing ~4,792 TPS (2,283 non-vote). Measured slot time is 268ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $980.4K of Real Economic Value over the last 24h ($681/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $109.09 (-2.3% / 24h). Decentralization: Nakamoto coefficient 18, 676 active validators, 0.1% of stake delinquent. Alpenglow readiness: validators holding 99% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 1 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 448,785,416 |
| Block height | 426,826,128 |
| Epoch | 1038 (85.51% complete, ~4.7h left) |
| TPS (10 min avg) | 4,792 |
| Non-vote TPS | 2,283 |
| Slot time (measured) | 268.4 ms |
| Est. daily transactions | 353,474,149 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0061 |
| Node version | 4.3.0-rc.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $109.09 (-2.3%/24h) |
| Market cap | $64.0B |
| **REV (24h)** | **$980.4K** (fees $826.3K + Jito tips $154.1K) |
| Chain TVL | $6.1B |
| Stablecoin supply | $15.7B |
| DEX volume (24h) | $2.9B (-18.7%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 587,366,680 SOL |
| Inflation | 3.64% |

Top DEXs by 24h volume: PumpSwap ($606.4M), BisonFi ($386.8M), Raydium AMM ($255.5M), HumidiFi ($228.9M), Orca DEX ($200.6M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 676 / 14 |
| Delinquent stake | 0.08% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.3% |
| Avg / median commission | 12.6% / 5.0% |
| Alpenglow BLS-key readiness | 699 validators, 99.4% of stake |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L43ZWjwCHART3o…` | 17,849,776 | 4.05% | 7% |
| 2 | `he1iusunGwqrNtafDtLd…` | 15,819,247 | 3.59% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5…` | 12,500,805 | 2.84% | 0% |
| 4 | `CatzoSMUkTRidT5DwBxA…` | 11,362,749 | 2.58% | 5% |
| 5 | `8GbwASqdpw4dVcwbWUxb…` | 9,786,807 | 2.22% | 0% |
| 6 | `26pV97Ce83ZQ6Kz9XT4t…` | 9,252,843 | 2.1% | 7% |
| 7 | `51JBzSTU5rAM8gLAVQKg…` | 9,116,740 | 2.07% | 10% |
| 8 | `9QU2QSxhb24FUX3Tu2Fp…` | 7,434,776 | 1.69% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJn…` | 7,086,871 | 1.61% | 5% |
| 10 | `HZKopZYvv8v6un2H6KUN…` | 6,627,951 | 1.51% | 100% |

## Signals (anomaly detection)

- **[WARNING]** TPS spike: 4,792 vs 12h mean 4,068 (z=+2.2)

## Solana Pulse — sentiment (experimental)

**73/100 — Bullish** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 81.2 |
| fear greed | 71 |
| momentum | 54.1 |
| news | 95 |

Crypto Fear & Greed: 71 (Greed) · CoinGecko votes bullish: 81.25% · headline tone (48h): +6

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 144 |
| Raydium AMM v4 | 159 |
| Orca Whirlpool | 159 |
| Pump.fun | 177 |
| Tensor | 0 |
| Magic Eden v2 | 97 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,943,926 |
| Binance (cold) | 1,322,878 |
| OKX (attributed) | 243,904 |
| Coinbase (hot) | 18,299 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 268ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 99.4% of stake.
- **Agave**: latest release v4.2.2 · running 4.3.0-rc.0 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

### Latest ecosystem news (solana.com)

- [Solana Changelog: September 18, 2026](https://solana.com/news/solana-changelog-september-18-2026) — Sat, 19 Sep 2026
- [How AI Is Reshaping Crypto Security, with Michael Coates](https://solana.com/news/bits-to-bricks-crypto-security-michael-coates) — Sat, 19 Sep 2026
- [Project Harmonia Brings Institutional Tokenized Funds to Solana](https://solana.com/news/project-harmonia-brings-institutional-tokenized-funds-to-solana) — Wed, 16 Sep 2026
- [Solana: Building, Proving and Earning Trust in Public](https://solana.com/news/solana-building-trust-in-public) — Mon, 14 Sep 2026
- [Solana Changelog: September 10, 2026](https://solana.com/news/solana-changelog-september-10-2026) — Thu, 10 Sep 2026
- [Solana Changelog: September 3, 2026](https://solana.com/news/solana-changelog-september-3-2026) — Thu, 10 Sep 2026

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 7900 ms |
| solana_rpc_validators | OK | 109 ms |
| coingecko | OK | 1751 ms |
| defillama_tvl | OK | 79 ms |
| defillama_dex | OK | 417 ms |
| defillama_fees | OK | 114 ms |
| defillama_stablecoins | OK | 518 ms |
| defillama_xstocks | OK | 524 ms |
| jito_kobe | OK | 304 ms |
| stakewiz | OK | 960 ms |
| github | OK | 556 ms |
| solana_com_news | OK | 71 ms |
| sentiment | OK | 2125 ms |
| solana_status_page | OK | 313 ms |
| solana_rpc_whales | OK | 872 ms |
| solana_rpc_programs | OK | 1540 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*