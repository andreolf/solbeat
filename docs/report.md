# Solbeat — State of the Solana Network

> Generated 2026-09-03T08:03:07Z · zero API keys · Python stdlib + public endpoints

## Analyst commentary

Epoch 1027 is 59% complete (~15h remaining), with the cluster processing ~3,507 TPS (1,358 non-vote). Measured slot time is 314ms — live on-chain evidence that SIMD-0525's first slot-time reduction step (350ms target) is active on mainnet. The network earned $777.7K of Real Economic Value over the last 24h ($540/minute), computed as base + priority fees plus Jito MEV tips. SOL trades at $100.41 (+0.7% / 24h). Alpenglow readiness: validators holding 99% of stake have registered BLS keys ahead of the consensus upgrade. Anomaly scan: 1 signal(s) flagged — see Signals below.

## Network performance

| Metric | Value |
|---|---|
| Health | ok |
| Slot | 443,920,634 |
| Block height | 421,967,871 |
| Epoch | 1027 (59.41% complete, ~15.3h left) |
| TPS (10 min avg) | 3,507 |
| Non-vote TPS | 1,358 |
| Slot time (measured) | 313.8 ms |
| Est. daily transactions | 304,125,694 |
| Median priority fee | 0.0 µ-lamports/CU |
| Avg fee per user tx (24h) | $0.0053 |
| Node version | 4.2.2 |

## Economic indicators

| Metric | Value |
|---|---|
| SOL price | $100.41 (+0.7%/24h) |
| Market cap | $58.8B |
| **REV (24h)** | **$777.7K** (fees $612.6K + Jito tips $165.1K) |
| Chain TVL | $5.7B |
| Stablecoin supply | $16.0B |
| DEX volume (24h) | $2.3B (7.2%/1d) |
| Tokenized equities (xStocks TVL) | $433.4M |
| Circulating supply | 585,275,016 SOL |
| Inflation | 3.67% |

Top DEXs by 24h volume: PumpSwap ($1.0B), Orca DEX ($206.2M), BisonFi ($194.4M), Manifest Trade ($165.1M), Meteora DLMM ($137.8M)

## Validators

| Metric | Value |
|---|---|
| Active / delinquent | None / None |
| Delinquent stake | None% |
| Nakamoto coefficient | None |
| Top-10 stake share | None% |
| Avg / median commission | None% / None% |
| Alpenglow BLS-key readiness | 689 validators, 99.4% of stake |

### Top validators by stake

| # | Vote account | Stake (SOL) | Share | Commission |
|---|---|---|---|---|

## Signals (anomaly detection)

- **[WARNING]** Solana TVL surge (z=+2.2 vs its recent baseline)

## Solana Pulse — sentiment (experimental)

**64/100 — Bullish** · composite of keyless signals (not financial advice)

| Component | Score |
|---|---|
| community | 76.9 |
| fear greed | 65 |
| momentum | 44.8 |
| news | 74 |

Crypto Fear & Greed: 65 (Greed) · CoinGecko votes bullish: 76.92% · headline tone (48h): +3

## Ecosystem pulse

| Program | Activity (tx/min, sampled) |
|---|---|
| Jupiter v6 | 126 |
| Raydium AMM v4 | 168 |
| Orca Whirlpool | 217 |
| Pump.fun | 514 |
| Tensor | 0 |
| Magic Eden v2 | 189 |
| Marinade | 0 |

| Exchange wallet | Balance (SOL) |
|---|---|
| Binance (hot) | 9,188,448 |
| Binance (cold) | 1,936,304 |
| OKX (attributed) | 315,396 |
| Coinbase (hot) | 86,479 |

## Upgrades & news

- **SIMD-0525 (slot-time reduction)**: first step (350ms) confirmed ACTIVE — measured slot time 314ms · proposal merged.
- **Alpenglow (SIMD-0236)**: consensus overhaul (~150ms finality) targeted for activation via Agave v4.3; BLS-key registration at 99.4% of stake.
- **Agave**: latest release v4.2.2 · running 4.2.2 on the polled node.
- **Status page**: All Systems Operational (0 unresolved incidents).

### Latest ecosystem news (solana.com)

- [The Token Supercycle: Everything of Value is Becoming Programmable](https://solana.com/news/the-token-supercycle-oped) — Wed, 02 Sep 2026
- [Solana Changelog: August 27, 2026](https://solana.com/news/solana-changelog-august-27-2026) — Fri, 28 Aug 2026
- [The Token Supercycle Is Here: Solana Brings Breakpoint 2026 to London](https://solana.com/news/breakpoint-2026-london-speakers) — Thu, 27 Aug 2026
- [Solana Changelog: August 20, 2026](https://solana.com/news/solana-changelog-august-20-2026) — Mon, 24 Aug 2026
- [Lowering Slot Time and Validator Economics](https://solana.com/news/lowering-slot-time-and-validators-economic) — Wed, 19 Aug 2026
- [v1 Transactions and the ALT Trade-off](https://solana.com/news/transaction-v1-and-the-alt-trade-off) — Mon, 17 Aug 2026

## Data sources & provenance

| Source | Status | Latency |
|---|---|---|
| solana_rpc | OK | 24574 ms |
| solana_rpc_validators | FAILED | 13665 ms |
| coingecko | OK | 1738 ms |
| defillama_tvl | OK | 271 ms |
| defillama_dex | OK | 1062 ms |
| defillama_fees | OK | 1916 ms |
| defillama_stablecoins | OK | 261 ms |
| defillama_xstocks | OK | 198 ms |
| jito_kobe | OK | 243 ms |
| stakewiz | OK | 1351 ms |
| github | OK | 974 ms |
| solana_com_news | OK | 206 ms |
| sentiment | OK | 2486 ms |
| solana_status_page | OK | 464 ms |
| solana_rpc_whales | OK | 4127 ms |
| solana_rpc_programs | OK | 19007 ms |

*REV methodology: chain base+priority fees (DeFiLlama) + Jito MEV tips (Kobe API), following the Blockworks definition. All endpoints keyless.*