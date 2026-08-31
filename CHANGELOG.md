# Changelog

## v1.3 — 2026-08-31
- Real live mode: the dashboard polls a keyless browser-friendly RPC
  (PublicNode) — slot counter re-syncs every 10s (LIVE badge), TPS/slot time
  update from live performance samples, lifetime tx counter ticks at live TPS
- `python3 solbeat.py verify` — self-audit cross-checking price (vs Binance),
  market cap (vs RPC supply×price), slot time (vs live measurement), TVL
  (vs independent endpoint), REV/stake/epoch arithmetic
- SEO & agents: Open Graph/Twitter cards, JSON-LD Dataset, live llms.txt,
  robots.txt, sitemap.xml
- Hardening: null-safe RPC optional fields; run-history strip now includes
  correlation incidents


## v1.2 — 2026-08-31
- Redesigned Sources & methodology panel (per-source chips with friendly names,
  endpoint domains, live latency)
- Site footer: resources, changelog, credit
- Hero layout fix: slot-performance strip moved to its own full-width row
  (removes a text/strip overlap at narrow widths)

## v1.1 — 2026-08-31
- Ecosystem news via solana.com's official RSS feed
- On-chain clock using `getSlot` + `getBlockTime` (all nine RPC methods from
  the bounty brief now in use)
- Optional Dune Analytics extractor (`DUNE_API_KEY` + `DUNE_QUERY_ID`)
- Configurable refresh interval (`SOLBEAT_REFRESH`)
- Mobile polish (compressing anomaly strips, ≤600px layout)
- Bounty scope-coverage matrix in the README

## v1.0 — 2026-08-31
- Initial release: 14 keyless data sources, computed REV (Blockworks
  methodology), correlation-based anomaly incidents, dark HTML terminal +
  Markdown + JSON outputs, GitHub Actions 30-minute autopilot, Pages hosting
