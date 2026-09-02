# Lane: red-capable checkers

Work fully autonomously; do not ask questions. Repo root: /home/tobias/Projects/quantum-algorithms-for-algebraic-geometry. Read first, in order: CLAUDE.md (laws, north star), seed/analysis-2026-09-01/report.md (the seed analysis; treat as an untrusted proposer document, NOT as established truth), seed/analysis-2026-09-01/referee/round1.md and round2.md (prior critic verdicts), HANDOFF.md, seed/page81.tex (the original notebook page). No emoji, no marketing prose. Mark any citation you cannot resolve to an arXiv id or DOI you are confident of as [UNVERIFIED]. Do not touch seed/ or any file outside your lane.

Also read: seed/analysis-2026-09-01/numerics/*.py and the *_out.txt files, and seed/analysis-2026-09-01/numerics/run_all.sh.

## Your lane (writable files, nothing else)
- everything under checkers/ (create it as you like; you may COPY files from seed/analysis-2026-09-01/numerics/ into checkers/ and modify the copies; never edit seed/)
- checkers/MUTATIONS.md
- checkers/README.md

## Task
Turn the seed numerics into a red-capable checker suite (rk-light law L4).

1. Copy bf.py, ideals.py, gaps.py and every task script into checkers/. Keep the originals' numerical content; you may refactor for exit codes.
2. Every checker must (a) state at the top which seed claim it tests (cite seed report section and the numbered Fact/Prop/Conj), (b) exit 0 only when the tested property holds within a stated tolerance and exit 1 with a printed reason otherwise, (c) use no bare assert (python -O strips them), (d) be bounded: run under 'timeout' in run_all.sh with a per-script budget and a dimension cap.
3. Where a task script currently only prints numbers without checking anything, decide what property the seed report actually uses those numbers for, and check THAT property (e.g. kernel dimension equals Hilbert function for every N run; conic gap equals N+1 exactly; quadric gap lower bound 4 d_min^2 (N-2) + ||f||^2 holds; boolean-ideal gap ratio behaves as reported). If a script's numbers support no checkable claim, say so in README.md and leave it as an 'exploration' script that is excluded from run_all.sh.
4. MUTATIONS.md: for every checker, one recorded mutation (exact edit applied to a COPY in a temp dir, e.g. flip a sign, change the Hilbert function by one, weaken the bound) and evidence that the checker then exits 1. Actually run these mutations; paste the exit code and the last line of output. A checker with no red mutation does not exist.
5. run_all.sh: runs every checker under timeout, prints PASS/FAIL per checker with wall time, exits nonzero if any fails. Run it and paste the summary into README.md. Python: use whatever 'python3' on this machine provides (numpy, scipy, sympy are expected; if one is missing, say so).
6. Reproduce the seed *_out.txt numbers where feasible (N caps as in the seed) and note any discrepancy with file and value.

Bound every run: use 'timeout 600' per script, and keep total wall time under ~40 minutes; reduce N caps if needed and say so.

## Output
The checkers/ tree, MUTATIONS.md, README.md (with the run_all summary and a 'Discrepancies with seed' section). End README.md with "## Lane report" (<=15 lines).
