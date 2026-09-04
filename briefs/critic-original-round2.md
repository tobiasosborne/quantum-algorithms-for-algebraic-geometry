# Independent adversarial review: original-construction round 2

Act as an independent mathematical critic (Astra), not a proposer. No web search or
reference lookup. Use file reads and your own mathematical derivations. Read-only
shell commands are allowed to access local files; bounded mathematical recomputations
are allowed with a timeout and one BLAS thread. Do not spawn agents. Write only
verdicts/original-round2-r1.md, or the subsequent verdict file assigned by the root.

Read CLAUDE.md; PRD.md (criteria 1--6, D21--D22); the conventions in
definitions/definitions.md; then these four memos completely:
- scouting/original-growth-round2.md
- scouting/original-algebra-round2.md
- scouting/original-geometry-round2.md
- scouting/original-broad-round2.md
If the final geometry memo is not yet present, review the other two and say explicitly
that the geometry review is pending; do not infer its contents.

The user demands both an unsolved problem-level result and an original quantum
mechanism, not a reapplication/equivalent of Grover, QFT, DQI, generic spectral
filtering or other established algorithms. Algebraic geometry is broad; the existing
project construction is optional. No candidate is claimed to meet this bar yet.
Historical novelty cannot be certified in this no-web pass.

Check every proposed claim's mathematical quantifiers, hypotheses and resource costs.
Do not mistake conditional identities, new task names, unfamiliar encodings or
unimplemented oracles for new algorithms. Criticize substantive equivalences, not
the vacuous fact that any circuit can be compiled to a universal gate set.

Specific risks to audit:
1. Growth: correct n+1 mode/Fock factors; Lüders failure example is not an impossibility
   theorem for arbitrary recovery. Hilbert reservoir stationarity does not prove mixing.
   Radical two-component monomial example: cutoff, invariant classical sector, gap
   upper bound and worst-start/vacuum-start distinction.
2. Algebra: associativity/tree independence, rectangular block encodings, postselection
   costs, trace pairing vs positive Hermitian metric; unzipping does not provide roots
   unless the required access/measurement exists. Exterior adjugate transposes/signs,
   determinant products, finite-difference jet phases and probabilities.
3. Geometry: C3 conjugation; single-copy jet measurement is available to the single-copy
   comparator. Linear Poincare duality is not an antilinear Hodge oracle. Exterior merge
   normalization and angle factors. Rational-map copy lower bound must distinguish one
   branch from multiple accepted branches and raw iterate degree from reduced degree.
4. Broad pass: positive correspondence fusion vs classical two-history collisions;
   path/history access costs; signed fusion and known LCU equivalence; birational
   pullback order and whether the defect circuit is a known quantum switch.

For each objection provide severity FATAL/MAJOR/MINOR, exact location, FIX DEMAND,
and SURVIVING STATEMENT. Supply exact corrected wording where possible.
Give a final per-proposed-row decision (ACCEPT AS CONJECTURE, ACCEPT AS REFUTED, HOLD,
or REJECT), and definition decisions. Do not promote any row to PROVED.
Require statement/status/surviving-statement consistency. Mark findings not checked.
Conclude VERDICT: PASS only if no FATAL or MAJOR objections remain; otherwise FAIL.
Keep the verdict within roughly 250 lines and make it self-contained enough to merge
without pretending an algorithm or global novelty result has been established.
