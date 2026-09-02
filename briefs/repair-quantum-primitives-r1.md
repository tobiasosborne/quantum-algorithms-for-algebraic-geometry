# Repair brief: scouting/quantum-primitives.md, round 1 (proposer response to verdicts/quantum-primitives-r1.md)

Work fully autonomously; do not ask questions. You are in a read-only sandbox: your ENTIRE output is your final message, which the orchestrator saves VERBATIM as the new scouting/quantum-primitives.md (replacing the current file; git keeps the old version). So your output must be the COMPLETE revised memo, Markdown, no preamble, no emoji, same section structure as the current file, followed by one new final section `# Repair r1 response` (format below). Repo root: /home/tobias/Projects/quantum-algorithms-for-algebraic-geometry.

Read order: CLAUDE.md (laws L1-L5), the current memo scouting/quantum-primitives.md (you or a sibling wrote it), the verdict verdicts/quantum-primitives-r1.md (25 objections O1-O25, 10 MAJOR, VERDICT FAIL; plus a rows adjudication table §3, definitions adjudication §4, revised ranked table §5), definitions/definitions.md (D-ids; conventions C1-C12), claims/CLAIMS.md 'Critical claims' and any C-row the verdict names. You have web access; verify anything you add.

## Work order
The verdict is the work order. Strategy directive (law L5): downgrade over ambition. Where the critic offers 'downgrade or prove more', downgrade. Where the critic says REJECT, delete the row and say so. Where the critic gives an exact rewording, copy it verbatim, never paraphrase upward. Address EVERY objection O1-O25, MAJOR and MINOR and NOTE alike; no objection is silently ignored.

Specific obligations, restating the critic's FIX DEMANDS:
- O1: state the Ding et al. condition-number bound as the paper states it (kappa >= sqrt(((d+1)^h - 1)/t) and its consequences for Chen-Gao and the improved system); separate it from the Grover cost.
- O2: remove the classical bound falsely attributed to Kedlaya; state what Kedlaya actually says about Schoof-Pila-Adleman-Huang, with the correct attribution or [UNVERIFIED].
- O4: make the decision rule and the scores agree. Either re-score by the rubric (Kedlaya 4, primitive 6 per the critic) or change the rubric and say so in the decision rule; the ranked table, the per-primitive 'Score and killer' paragraphs and the proposed rows must all agree (lockstep).
- O5: correct the Witten-index row: for an isolated non-degenerate critical locus the LG Witten index equals +-mu; restate the killer for the case the brief asked about (isolated singularity) honestly, and give the answer to brief obligation 2(d) in full.
- O6: fix the TDA-on-real-varieties row's where-proved (Cech vs Vietoris-Rips do not compose) or downgrade to HOLD as the critic adjudicated.
- O7: add Schmidhuber-Lloyd's simplices-input escape clause and Gyurik-Cade-Dunjko (DOI 10.22331/q-2022-11-10-855) and re-score primitive 5 if they change it.
- O8: add a primitive section for Hallgren principal-ideal / unit-group (DOI 10.1145/1206035.1206039) and Eisentraeger-Hallgren-Kitaev-Song (DOI 10.1145/2591796.2591860) in the standard template, scored honestly against PRD §2 (the input is an ideal of a number field: say precisely whether that is an algebraic-geometry problem in the north star's sense and what the hardware hook is), with proposed rows.
- O9, O10: rewrite or replace Combination 1: it must be disjoint from arm E Route 7 / C-262, and its success criterion must be reachable by its mechanism; if no honest version exists, replace it by a different combination.
- O11: every proposed row's where-tested must name an existing checker or exploration script path, or say 'none'; remove descriptions of tests that were never run.
- O3, O12, O13, O14, O15, O16, O17, O18, O19, O20, O21: apply each fix as demanded (author corrections, DOI/title agreement, output size factor g, transcription fixes, row rename and correct D-id, delete C-NEW-QP-FINITE-FIELD-SEED and C-NEW-QP-ID-KEDLAYA, hypotheses of the cited Gibbs theorem, Kedlaya row assumptions, the status convention for imported published theorems: follow the DAG's existing convention exactly as the critic states it, reference hygiene).
- O22-O25: acknowledge; for O23 add one line to 'Questions for TJO' or a lockstep note that C-099's [UNVERIFIED] mark can be lifted with the id the critic verified; for O24 note it as a DAG hygiene item for the orchestrator (not your file).
- Apply the critic's §3 rows adjudication: every ACCEPT WITH REWORDING row gets the critic's exact wording; REFUTED rows carry status REFUTED and name the surviving weaker statement; the HOLD row is marked HOLD with the missing step; add the definition D-multihomogeneous-bezout as the critic demanded; apply the §4 definitions rewordings.
- Do not add new claims beyond what the objections require. Do not raise any score the critic lowered without a stated reason tied to a source.

## Final section format
`# Repair r1 response`, then a table with one row per objection: `| objection | severity | disposition (FIXED / RETRACTED / DOWNGRADED / RESIDUE) | exact location of the edit (section name, row id) | one-line note |`. RESIDUE means you could not fix it and explain why. Then a line `Rows after repair: <count> (CONJECTURE n, REFUTED n, HOLD n, deleted n)`.
