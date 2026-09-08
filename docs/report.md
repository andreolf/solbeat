# Solbeat — State of the Solana Network

> Generated 2026-09-08T00:00:29Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1030 is 55% complete (~17h remaining), with the cluster processing ~3,675 TPS (1,526 non-vote). Measured slot time is 314ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $756.0K of Real Economic Value over the last 24h ($525/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $103.87 (-2.5% / 24h). Decentralization: Nakamoto coefficient 18, 677 active validators, 0.0% of stake delinquent. Alpenglow readiness: validators holding 99% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 1 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 445,196,436 |
| Block height | 423,240,600 |
| Epoch | 1030 (54.73% complete, ~17.0h left) |
| TPS (10 min avg) | 3,675 |
| Non-vote TPS | 1,526 |
| Slot time (measured) | 313.8 ms |
| Est. daily transactions | 342,046,507 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0041 |
| Node version | 4.2.2 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $103.87 (-2.5%/24h) |
| Market cap | $60.9B |
| **REV (24h)** | **$756.0K** (fees $653.1K + Jito tips $102.9K) |
| Chain TVL | $5.9B |
| Stablecoin supply | $16.7B |
| DEX volume (24h) | $2.9B (55.8%/1d) |
| Tokenized equities (xStocks TVL) | $447.0M |
| Circulating supply | 586,165,670 SOL |
| Inflation | 3.66% |

Top DEXs by 24h volume: PumpSwap ($677.9M), Raydium AMM ($307.8M), BisonFi ($241.5M), Orca DEX ($236.6M), Meteora DLMM ($223.1M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 677 / 11 |
| Delinquent stake | 0.01% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.2% |
| Avg / median commission | 12.8% / 5% |
| Alpenglow BLS-key readiness | 690 validators, 99.0% of stake |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L43ZWjwCHART3o…` | 17,438,541 | 3.97% | 7% |
| 2 | `he1iusunGwqrNtafDtLd…` | 16,336,964 | 3.72% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5…` | 12,517,399 | 2.85% | 0% |
| 4 | `CatzoSMUkTRidT5DwBxA…` | 11,397,824 | 2.59% | 5% |
| 5 | `8GbwASqdpw4dVcwbWUxb…` | 9,564,412 | 2.18% | 0% |
| 6 | `26pV97Ce83ZQ6Kz9XT4t…` | 9,181,909 | 2.09% | 7% |
| 7 | `51JBzSTU5rAM8gLAVQKg…` | 9,038,443 | 2.06% | 10% |
| 8 | `9QU2QSxhb24FUX3Tu2Fp…` | 7,384,461 | 1.68% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJn…` | 6,858,929 | 1.56% | 5% |
| 10 | `DumiCKHVqoCQKD8roLAp…` | 6,595,421 | 1.5% | 0% |

## Signals (anomaly detection)

- **[WARNING]** Solana TVL surge (z=+2.4 vs its recent baseline)

## Solana Pulse — sentiment (experimental)

**69/100 — Bullish** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 78.4 |
| fear greed | 69 |
| momentum | 68.0 |
| news | 50 |

Crypto Fear & Greed: 69 (Greed) · CoinGecko votes bullish: 78.38% · headline tone (48h): +0

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 134 |
| Raydium AMM v4 | 134 |
| Orca Whirlpool | 134 |
| Pump.fun | 163 |
| Tensor | 1 |
| Magic Eden v2 | 33 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,188,448 |
| Binance (cold) | 1,732,306 |
| OKX (attributed) | 210,992 |
| Coinbase (hot) | 30,936 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 314ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 99.0% of stake.
- **Agave**: latest release v4.2.2 · running 4.2.2 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

### Latest ecosystem news (solana.com)

- [# How BitRobot Crowdsources Real-World Data for Embodied AI, with Jonathan Victor](https://solana.com/news/bits-to-bricks-bitrobot-jonathan-victor) — Mon, 07 Sep 2026
- [Solana Ecosystem Roundup: August 2026](https://solana.com/news/solana-ecosystem-roundup-august-2026) — Fri, 04 Sep 2026
- [Payment Channels: 1 Million Payments Per Second](https://solana.com/news/payment-channels-1-million-payments-per-second) — Thu, 03 Sep 2026
- [How to Reclaim Excess SOL After Rent Reduction](https://solana.com/news/how-to-reclaim-excess-sol-after-rent-reduction) — Thu, 03 Sep 2026
- [The Token Supercycle: Everything of Value is Becoming Programmable](https://solana.com/news/the-token-supercycle-oped) — Wed, 02 Sep 2026
- [Webinar Recap: Cross-Border Payments in Latin America](https://solana.com/news/webinar-recap-cross-border-payments-in-latin-america) — Tue, 01 Sep 2026

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 13404 ms |
| solana_rpc_validators | OK | 1384 ms |
| coingecko | OK | 1874 ms |
| defillama_tvl | OK | 250 ms |
| defillama_dex | OK | 4851 ms |
| defillama_fees | OK | 5776 ms |
| defillama_stablecoins | OK | 173 ms |
| defillama_xstocks | OK | 138 ms |
| jito_kobe | OK | 143 ms |
| stakewiz | OK | 1090 ms |
| github | OK | 946 ms |
| solana_com_news | OK | 139 ms |
| sentiment | OK | 2376 ms |
| solana_status_page | OK | 472 ms |
| solana_rpc_whales | OK | 2862 ms |
| solana_rpc_programs | OK | 4985 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*