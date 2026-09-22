# Solbeat — State of the Solana Network

> Generated 2026-09-22T16:12:28Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1040 is 35% complete (~21h remaining), with the cluster processing ~4,922 TPS (2,401 non-vote). Measured slot time is 266ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $1.3M of Real Economic Value over the last 24h ($924/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $117.03 (-0.7% / 24h). Decentralization: Nakamoto coefficient 18, 677 active validators, 0.1% of stake delinquent. Alpenglow readiness: validators holding 99% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 4 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 449,429,153 |
| Block height | 427,469,502 |
| Epoch | 1040 (34.53% complete, ~20.9h left) |
| TPS (10 min avg) | 4,922 |
| Non-vote TPS | 2,401 |
| Slot time (measured) | 265.9 ms |
| Est. daily transactions | 397,923,325 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0061 |
| Node version | 4.3.0-rc.0 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $117.03 (-0.7%/24h) |
| Market cap | $68.8B |
| **REV (24h)** | **$1.3M** (fees $1.1M + Jito tips $234.1K) |
| Chain TVL | $6.4B |
| Stablecoin supply | $17.1B |
| DEX volume (24h) | $3.4B (22.7%/1d) |
| Tokenized equities (xStocks TVL) | n/a |
| Circulating supply | 587,507,618 SOL |
| Inflation | 3.64% |

Top DEXs by 24h volume: Raydium AMM ($466.0M), BisonFi ($446.8M), Orca DEX ($419.0M), PumpSwap ($390.1M), Meteora DLMM ($259.6M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | 677 / 12 |
| Delinquent stake | 0.05% |
| Nakamoto coefficient | 18 |
| Top-10 stake share | 24.3% |
| Avg / median commission | 12.3% / 5% |
| Alpenglow BLS-key readiness | 699 validators, 99.4% of stake |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|
| 1 | `CcaHc2L43ZWjwCHART3o…` | 17,826,722 | 4.05% | 7% |
| 2 | `he1iusunGwqrNtafDtLd…` | 15,840,698 | 3.6% | 0% |
| 3 | `3N7s9zXMZ4QqvHQR15t5…` | 12,354,353 | 2.81% | 0% |
| 4 | `CatzoSMUkTRidT5DwBxA…` | 11,265,429 | 2.56% | 5% |
| 5 | `8GbwASqdpw4dVcwbWUxb…` | 10,210,832 | 2.32% | 0% |
| 6 | `26pV97Ce83ZQ6Kz9XT4t…` | 9,211,356 | 2.09% | 7% |
| 7 | `51JBzSTU5rAM8gLAVQKg…` | 9,144,102 | 2.08% | 10% |
| 8 | `9QU2QSxhb24FUX3Tu2Fp…` | 7,458,789 | 1.7% | 7% |
| 9 | `CvSb7wdQAFpHuSpTYTJn…` | 7,089,342 | 1.61% | 5% |
| 10 | `DumiCKHVqoCQKD8roLAp…` | 6,555,722 | 1.49% | 0% |

## Signals (anomaly detection)

- **[WARNING]** Solana TVL surge (z=+2.5 vs its recent baseline)
- **[WARNING]** Stablecoin supply surge (z=+2.5 vs its recent baseline)
- **[WARNING]** Real Economic Value deviating from its run-history baseline (z=+2.5)
- **[WARNING · liquidity_rotation]** Stablecoin supply and TVL moving together — capital rotating in or out of the chain.

## Solana Pulse — sentiment (experimental)

**80/100 — Bullish** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 72.0 |
| fear greed | 78 |
| momentum | 85.3 |
| news | 90 |

Crypto Fear & Greed: 78 (Extreme Greed) · CoinGecko votes bullish: 72.0% · headline tone (48h): +5

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 149 |
| Raydium AMM v4 | 135 |
| Orca Whirlpool | 149 |
| Pump.fun | 165 |
| Tensor | 1 |
| Magic Eden v2 | 58 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,943,926 |
| Binance (cold) | 1,483,061 |
| OKX (attributed) | 263,047 |
| Coinbase (hot) | 21,770 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 266ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 99.4% of stake.
- **Agave**: latest release v4.3.0 · running 4.3.0-rc.0 on the polled node.
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
| solana_rpc | OK | 9910 ms |
| solana_rpc_validators | OK | 301 ms |
| coingecko | OK | 2128 ms |
| defillama_tvl | OK | 9358 ms |
| defillama_dex | OK | 4065 ms |
| defillama_fees | OK | 1438 ms |
| defillama_stablecoins | OK | 393 ms |
| defillama_xstocks | OK | 21222 ms |
| jito_kobe | OK | 448 ms |
| stakewiz | OK | 1637 ms |
| github | OK | 793 ms |
| solana_com_news | OK | 127 ms |
| sentiment | OK | 2517 ms |
| solana_status_page | OK | 354 ms |
| solana_rpc_whales | OK | 1183 ms |
| solana_rpc_programs | OK | 2070 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*