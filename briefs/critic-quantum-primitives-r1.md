# Critic brief: scouting/quantum-primitives.md, round 1 (attack)

You are the adversarial critic. ATTACK; do not summarise. Work fully autonomously; do not ask questions. Repo root: /home/tobias/Projects/quantum-algorithms-for-algebraic-geometry. Your lane: the single writable file verdicts/quantum-primitives-r1.md. Do not edit anything else; do not commit. No emoji.

Read order: CLAUDE.md (laws L1-L5, rule 6 on citations), PRD.md (§2 success criteria, §3 scope, §4 arms), definitions/definitions.md (conventions C1-C12; D-ids), claims/CLAIMS.md §5, §6, 'Critical claims', then the TARGET scouting/quantum-primitives.md, then briefs/lane-quantum-primitives.md (the brief the proposer answered; the brief is NOT evidence). Also scouting/classical-landscape.md (§1-§2 and the 'Best classical algorithms' subsections the memo cites).

## Obligations (each one produces objections or an explicit 'checked, holds' line)
1. **Reference verification.** You have web access. For EVERY reference in the memo's reference list: fetch the arXiv abstract page or DOI landing page; confirm the authors, title and year match; confirm the resource bound or theorem the memo attributes to it is what the source states (read the abstract, and the relevant statement if the abstract is not enough). Produce a table: ref, id, resolves (Y/N), attribution correct (Y/N/partial), note. Any [UNVERIFIED] mark the memo left: try to resolve it. A wrong attribution of a resource bound is MAJOR; a fabricated reference is FATAL for the row that rests on it.
2. **Recompute the honest speedups.** For each primitive's 'Score' and 'sharpest killer': check the arithmetic and the logic. In particular: (a) the HHL/Macaulay condition-number and Boolean-Macaulay arguments (Chen-Gao versus Ding et al.); (b) whether Kedlaya's point-counting algorithm is polynomial in the genus and log q as stated and what it implies for hypersurfaces; (c) whether any hidden-nonlinear-structure problem is an algebraic-geometry problem in the north star's sense; (d) the SUSY/Landau-Ginzburg Jacobian-ring statement (ground states of {Q,Q^dag} for an isolated singularity: is the count the Milnor number, and under what conditions); (e) the quantum TDA dequantization claims; (f) every place the memo says 'quadratic', 'exponential' or 'none'.
3. **Quantifier audit** of every proposed claim row: quantifiers, input model, promise stated; depends-on D-ids and C-ids exist in the repo (grep); no reliance on REFUTED C-rows; CONJECTURE or REFUTED only, never higher.
4. **Lockstep audit.** Ranked table, per-primitive sections and proposed rows must agree with each other; flag any score or sentence that claims more than the corresponding row.
5. **Coverage audit.** Name any quantum primitive with a published application to varieties/ideals/polynomial systems that the memo omitted (with id), and any omitted dequantization result that changes a score.
6. **Combinations audit.** For each of the three 'Combinations': is the proposed one-week probe well-defined (what is computed, what would falsify it), and is it disjoint from work already in the DAG.

## Output format (mandatory)
- Header: target, date 2026-09-02, critic model, files read, URLs fetched (count), commands run with exit codes.
- Reference table (obligation 1).
- Numbered objections O1, O2, ...; each with: severity FATAL / MAJOR / MINOR / NOTE; exact location (section, primitive number, row id); your independent computation, fetched source statement, or counterexample; FIX DEMAND (one line, concrete); SURVIVING STATEMENT (the weaker statement that still holds, or 'none').
- A table 'Proposed rows adjudication': for each C-NEW-QP-* id: ACCEPT AS CONJECTURE / ACCEPT AS REFUTED / ACCEPT WITH REWORDING (exact rewording) / REJECT (reason) / HOLD (missing step).
- A table 'Proposed definitions adjudication': ACCEPT / REWORD / REJECT with reason.
- 'Revised ranked table': your own scores where they differ from the memo's, one line of reason each.
- Final line: exactly `VERDICT: PASS` (no FATAL/MAJOR) or `VERDICT: FAIL(O1, O3, ...)`.
