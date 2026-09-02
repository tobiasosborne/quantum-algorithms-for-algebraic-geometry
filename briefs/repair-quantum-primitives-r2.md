# Repair brief: scouting/quantum-primitives.md, round 2 (proposer response to verdicts/quantum-primitives-r2.md)

Work fully autonomously; do not ask questions. Read-only sandbox: your ENTIRE output is your final message, saved VERBATIM as the new scouting/quantum-primitives.md. Output the COMPLETE revised memo (Markdown, no preamble, no emoji), keeping every section as is except where an objection requires a change, and replace the final section `# Repair r1 response` by `# Repair r2 response` (same table format; keep the r1 table above it under a sub-heading `## r1` and add `## r2` for O26-O36). Repo root: /home/tobias/Projects/quantum-algorithms-for-algebraic-geometry.

Read: CLAUDE.md (L1 statuses are exactly PROVED, SKETCH, CONJECTURE, REFUTED), the current scouting/quantum-primitives.md, verdicts/quantum-primitives-r2.md (new objections O26-O36; dispositions of O1-O25 with four NOT VERIFIED: O7, O9, O10, O21), scouting/koszul-betti.md §3 and §6 (the arm B memo that Combination 1 duplicates), claims/CLAIMS.md rows C-092 and C-099 and one REFUTED row (e.g. C-193) for the DAG's REFUTED-row format.

## Work order (law L5: downgrade over ambition; copy critic wording verbatim; no new claims)
- O26, O27 (MAJOR): DELETE Combination 1 (Koszul Laplacian + DQC1 probe). Replace it with a combination that is disjoint from arms A-E and from scouting/koszul-betti.md, with a falsifiable one-week probe whose classical comparator is the one classical-landscape.md actually names (Hutch++ O(1/eps) matvecs for PSD inputs; the advantage must be in filter cost), or, if you cannot produce an honest one, leave only two combinations and say so in the Combinations preamble.
- O28 (MAJOR): remove the words attributing "BQP-hard regimes" to Gyurik-Cade-Dunjko; state only DQC1-hardness/completeness as the paper does (Thms 1, 2, 5).
- O7, O9, O10, O21 NOT VERIFIED: apply the critic's stated residual fix for each.
- O29: restore the correct title of arXiv:2112.03444 (ref 35).
- O30: `status: HOLD` is not an L1 status. Mark the TDA-real-variety row `status: CONJECTURE` with a first line `HOLD (do not merge): missing step = VR-Cech interleaving` inside the statement's trap note, or move it out of 'Proposed claim rows' into a 'Held rows' subsection; the orchestrator will not merge it either way.
- O31: rewrite the two REFUTED rows in the DAG convention (statement = the refuted claim as stated, status REFUTED, then 'surviving weaker statement:'); delete the non-standard `refuted proposition:` field.
- O32: the Witten-index row is a composition, not a cited theorem: status CONJECTURE, and the +-mu display in D-jacobian-ring-susy needs a source or an [UNVERIFIED] mark (critic's definitions table).
- O33: fix the N=1 witness so the kernel is nontrivial (one extra variable, as the critic shows), and recompute the numbers you quote for it.
- O34-O36 (NOTE): acknowledge and apply if trivial.
- Lockstep: the ranked table, per-primitive scores, Combinations and rows must still agree after the edits.

## Final section
`# Repair r2 response` with `## r1` (the previous table, unchanged) and `## r2`: one row per objection O26-O36 and per NOT VERIFIED item (O7, O9, O10, O21): objection | severity | disposition (FIXED / RETRACTED / DOWNGRADED / RESIDUE) | exact location | note. Then `Rows after repair: <count> (SKETCH n, CONJECTURE n, REFUTED n, held n, deleted n)`.
