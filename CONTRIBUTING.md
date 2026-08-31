# Contributing to Solbeat

Thanks for wanting to make the heartbeat stronger. Solbeat is deliberately
small and deliberately boring to operate — contributions should keep it that way.

## Ground rules

1. **Python standard library only.** No pip dependencies, ever. If a feature
   needs a library, it needs a different design.
2. **Zero API keys by default.** Every data source must be public and keyless.
   Key-gated extractors are acceptable only as optional, env-gated integrations
   that are invisible when unconfigured (see the Dune extractor for the pattern).
3. **Self-contained output.** `docs/index.html` must render identically from a
   `file://` URL — no CDNs, no external scripts (the Vercel analytics snippet is
   conditionally injected and skipped elsewhere), no runtime fetches required
   for first paint.
4. **Honest data.** Every metric carries provenance. Computed metrics (REV,
   fee/tx, activity proxies) are labeled as computed with their methodology.
   A failing source degrades gracefully and reports as failed — never silently.

## Good first contributions

- New keyless data sources (verify the endpoint works without auth first)
- New derived metrics or upgrade-evidence checks
- Better anomaly heuristics or new correlation incident classes
- Additional exchange wallets / program IDs (include attribution evidence,
  e.g. explorer labels)
- Accessibility, mobile, and dark-theme polish

## Workflow

1. Open an issue describing the source/metric and its keyless endpoint.
2. Fork, branch, implement.
3. Before opening the PR, run:

   ```bash
   python3 solbeat.py run      # must complete with your source reporting ok
   python3 solbeat.py verify   # must pass 7/7
   ```

4. PRs should keep the two-file layout: collection/analysis in `solbeat.py`,
   rendering in `solbeat_html.py`.

## Style

Match the existing code: small functions, docstrings that explain *why*,
comments only for non-obvious constraints. Rendering follows the design tokens
at the top of `solbeat_html.py` — text wears text colors, marks wear data
colors, status colors are reserved for status.
