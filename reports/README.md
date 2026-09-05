# Offline research report and local CI

Open [research-report.html](research-report.html) directly in a browser. The
article, interactive illustrations, research atlas, complete claim register,
scientific source library, glossary, notebook scan and formula fonts are embedded.
Rendering requires no network requests; external citations open only when clicked.
The report and build output state the current snapshot counts.

From a fresh clone, with Python 3, Node and npm installed:

```bash
make setup
make setup-browser
make ci
```

`make setup` creates the ignored `.venv-report/`, installs
[pinned Python requirements](requirements.txt), runs `npm ci` with the report
lockfile, and installs the tracked hooks using the portable relative
`.beads/hooks` path. It preserves the Beads-managed hook section. Setup is the
explicit dependency-install step and requires network access. Browser installation
is separate; skip `make setup-browser` when Playwright's matching Chromium is
already available.

The local entry points are:

- `make report` or `make report-build`: regenerate the HTML from the working tree.
- `make report-check`: validate coverage, links and exact build reproducibility;
  fail if the artifact is stale.
- `make ci`: rebuild, check reproducibility, run the isolated Git-index regression
  tests, and run the full offline browser suite.
- `make hooks`: install the portable hooks without installing dependencies.

On commits that stage report inputs, the report integration first checks that
all report inputs match the Git index. Partially staged scientific files and
untracked report inputs stop the commit with a concrete repair message. It then
rebuilds, runs the complete checks and stages only `reports/research-report.html`.
Unrelated staged and unstaged edits are preserved. A README-only commit skips
these report checks. The report integration installs nothing, performs no network
requests and never commits or pushes; the existing Beads hook retains its own
separate behavior.

Edit the template, route inventories and scientific sources, then stage the
intended input versions before committing. The generated HTML is maintained by
the hook. A failed build, uncovered scouting memo, broken source link, browser
failure or concurrent index change prevents automatic staging of the artifact.

The pipeline accepts an existing Python interpreter with Markdown 3.5.2 and
beautifulsoup4 4.12.3, or an explicit `QAAG_REPORT_PYTHON`. It finds KaTeX 0.16.22
and Playwright 1.55.0 in `reports/node_modules/`, with the existing
`/tmp/qaag-report-tools/node_modules/` installation as a fallback.
`QAAG_KATEX_DIR` can select another KaTeX package directory. To use an existing
Chromium executable, set `QAAG_CHROMIUM_PATH` for both CI and commits. Otherwise
the pipeline requires the matching browser installed by Playwright; it never
downloads a browser implicitly. Every subprocess has a time limit.

The browser suite checks the mathematical illustrations, source reader,
navigation, responsive layout and absence of runtime errors or network requests.
The Git-index tests use isolated temporary repositories, including stale output,
partial staging, failed validation and hooks without `bd`. Run them alone with
`python3 -m unittest discover -s scripts/tests -v` from the repository root.

Historical documents retain their original wording; only `claims/CLAIMS.md`
assigns current formal statuses. Operational logs are excluded, and embedded
source code is readable evidence rather than executable report content.
The AGPL repository license and the bundled KaTeX MIT notice are available in
the report and [third-party notices](THIRD_PARTY_NOTICES.md).
