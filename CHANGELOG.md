# Changelog

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
