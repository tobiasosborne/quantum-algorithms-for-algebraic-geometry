# Lane: claims DAG

Work fully autonomously; do not ask questions. Repo root: /home/tobias/Projects/quantum-algorithms-for-algebraic-geometry. Read first, in order: CLAUDE.md (laws, north star), seed/analysis-2026-09-01/report.md (the seed analysis; treat as an untrusted proposer document, NOT as established truth), seed/analysis-2026-09-01/referee/round1.md and round2.md (prior critic verdicts), HANDOFF.md, seed/page81.tex (the original notebook page). No emoji, no marketing prose. Mark any citation you cannot resolve to an arXiv id or DOI you are confident of as [UNVERIFIED]. Do not touch seed/ or any file outside your lane.

## Your lane (writable files, nothing else)
- claims/CLAIMS.md
- claims/EXTRACTION-NOTES.md

## Task
Extract EVERY claim in the seed report (all sections, including §9 corrections and every numbered Fact/Prop/Conj) and every claim on the notebook page into the campaign claims DAG (rk-light law L1).

Row format in CLAIMS.md (one per claim, in a markdown table or one block per claim; blocks preferred for long statements):
- id: C-<nnn> (three digits, in order of appearance)
- statement: EXACT, all quantifiers explicit, all normalization conventions explicit (which norm, which generating tuple, which N range). Rewrite seed prose into a precise statement; if the seed statement is ambiguous, record the strongest precise reading the seed's proof actually supports and note the ambiguity.
- status: one of PROVED / SKETCH / CONJECTURE / REFUTED. RULE: nothing enters as PROVED. Seed "theorem-level" items enter as SKETCH (proof exists in the seed but no converged critic verdict in this campaign). Seed §8 conjectures enter as CONJECTURE. Anything the seed or referee rounds refuted enters as REFUTED with the surviving weaker statement as a separate row.
- depends-on: list of C-ids and D-ids (definition slugs; use the scheme D-<kebab-slug>, e.g. D-fock-basis, D-macaulay-gap; another lane is building definitions/ concurrently, so cite by best-guess slug and list all slugs you used in EXTRACTION-NOTES.md so they can be reconciled).
- where-proved: seed file + section, or "none".
- where-tested: seed numerics file(s) under seed/analysis-2026-09-01/numerics/ if any, else "none".
- referee: what round1.md / round2.md said about this claim, one line, or "not addressed".
- north-star relevance: one line — how this row bears on the north star in CLAUDE.md §1 (speedup over classical; heuristic hardware attack), or "infrastructure".

After the rows, add a "## DAG" section: a mermaid or plain adjacency list of depends-on edges, and a "## Critical claims for the north star" section: the <=8 rows whose promotion would most move the campaign, with one line each on what a critic must recompute to promote them.

EXTRACTION-NOTES.md: ambiguities you hit, claims you split or merged, D-slugs used, and anything in the seed that looks wrong (with file:line).

## Output
The two files. End CLAIMS.md with "## Lane report" (<=15 lines) including any MERGE PROPOSAL text for PRD.md.
