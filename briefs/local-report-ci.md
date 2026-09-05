# Local report CI/CD

User explicitly requests maintaining the HTML explainer as part of local CI/CD while
publishing a public AGPL repo. Own ONLY scripts/report_ci.py, scripts/install_hooks.py,
Makefile, reports/requirements.txt, reports/README.md, and .beads/hooks/pre-commit
(outside its managed Beads marker block only). You may add small bounded test fixtures
under scripts/tests/ for actual staged-tree or hook regressions; do not use checkers/
(the mathematical checker laws differ). Do not alter report template/build/verify or
GitHub workflows; root owns those. No further agents or bd calls.

Create clear local commands to setup/report/build/check/CI, a single noninteractive
entry point that rebuilds the report and runs its existing validation/browser verifier,
and a pre-commit integration that preserves the current Beads hook. Current
core.hooksPath is absolute .beads/hooks; tracked hook has Beads marker block. Provide
an installer setting a portable relative .beads/hooks path and executable modes.
No hidden network access or dependency installs during commits. Explicit setup may
install pinned dependencies (Python venv ignored; npm ci reports; optional browser
install). Recognize existing Python3 markdown/bs4 and /tmp/qaag-report-tools packages,
and QAAG_CHROMIUM_PATH for current cached Chromium; do not hardcode user's path in
tracked scripts. Select available matching browser or clearly document override.

Local commit behavior: when report inputs are staged, regenerate and stage only the
report artifact, validate reproducibility, and fail clearly on missing inputs/errors.
Do not accidentally bundle unstaged scientific changes. Either build from staged tree
or detect relevant partially-staged/unstaged inputs and stop with a concrete repair
message. Preserve unrelated staged/unstaged changes. An unchanged-report README-only
commit need not run the entire browser suite; a full `make ci` must. Avoid recursion,
no automatic commits/pushes from hook, bound subprocesses and fail nonzero. Build must
still work without bd installed (existing hook guards it). Document clone/setup and
what runs automatically vs full CI. Current report source fingerprints include
HANDOFF/PRD and scientific docs, template, inventories; dependency/build changes must
be covered too. Root will add a coverage check to ensure every new scouting memo has
an atlas route; your pipeline should expose build errors, not swallow them.

Report needs only KaTeX0.16.22/Playwright1.55.0 plus Python Markdown3.5.2 and bs44.12.3.
Keep entrypoints compatible with clean Ubuntu GitHub Actions; no repository absolute
paths. Communicate target commands early so root can wire hosted workflow and README
agent can document. Verify staged behavior with an isolated temporary test repository,
including a deliberate stale report and partial staging; do not mutate this repo's
index for a test. Root installs hook into this current checkout and runs final CI.
