# Independent audit of the theta-isogeny operation

Root owns shared registers and tracking. Read CLAUDE.md, PRD criterion 6,
`briefs/theta-isogeny-r6.md`, and the author's completed memo
`scouting/theta-isogeny-r6.md` when it appears. No new subagents.
Write only `verdicts/theta-isogeny-r6.md`.

Derive the genus-one and general-period-matrix identity independently.
The author reports a period-independent sector isometry using finite theta
indices, a Gaussian cubist metric, normalized Haar measure and nonuniform
Bergman-kernel sector weights. Check signs, conjugated evaluation states,
all flat twists, branch labels and normalization. In particular:

- The level-n theta norm squared should be `det(2n Im Omega)^(-1/2)`
  with the stated metric, and pullback must be an actual isometry.
- Both lower-level factors carry twists; identify precisely which ones.
  Do not silently turn twisted states into ordinary point states.
- Audit a non-diagonal genus-two period matrix as well as genus one,
  and include odd k so parity and wrap phases are exercised.
- Zero low-level theta evaluations must have zero probability rather
  than an undefined normalized output claimed on every branch.
- Verify the exact simultaneous finite-Weyl measurement reduction.
  Compilation into universal gates alone is not a novelty refutation.
- Separate period-dependent input state preparation and evaluation
  costs from the arithmetic gate list. Test the same classical output.

Use primary sources only for historical checks after the derivation.
Every objection needs FIX DEMAND and SURVIVING STATEMENT. An accepted
identity does not establish historical novelty or a computational advantage.
Bound any numerical probes, with explicit nonzero failure; do not add a
full checker or run unrelated repository tests merely for this audit.
