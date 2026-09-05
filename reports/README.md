# Offline research report

Open `research-report.html` directly in a browser. It embeds the article,
interactive illustrations, all 364 registered claims, 69 research routes,
137 scientific documents and code artifacts, 95 glossary entries, the notebook
scan, and 18 selected primary references. Rendering makes no network requests;
external citations open only when clicked.

Build dependencies: Python 3 with `Markdown==3.5.2` and
`beautifulsoup4==4.12.3`, plus Node/npm. Install the pinned JavaScript packages
with `npm ci --prefix reports`, then build from the repository root:

```bash
python3 reports/build_report.py
```

KaTeX can instead be located with `--katex-dir /path/to/node_modules/katex`
or `QAAG_KATEX_DIR`. The build also recognizes `/tmp/qaag-report-tools/node_modules/katex`.
Its MIT license, JavaScript, CSS and WOFF2 fonts are embedded in the artifact.

`python3 reports/build_report.py --check` validates source/claim links and
requires the artifact to match a fresh build. `node reports/verify_report.cjs`
runs browser checks with Playwright; install its Chromium browser or set
`QAAG_CHROMIUM_PATH` to an available Chromium executable.

Verified in Chromium 149: 57 offline browser checks passed with no JavaScript
errors or network requests. A separate targeted pass checked navigation,
144 Hz animation timing, pause behavior and source-reader headings.

The snapshot is dated 5 September 2026. Historical source documents preserve
their original wording; only `claims/CLAIMS.md` assigns current formal statuses.
The 24 proved claims include mathematical results and copy advantages using
known mechanisms. No candidate meets the project's original-algorithm goal.
Operational logs are excluded. Source code is readable evidence and is not
executed by the report; interactive simulations illustrate stated models.
