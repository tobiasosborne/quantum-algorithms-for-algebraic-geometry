# Independent audit: coefficient-state Schur reduction and disk count

Root owns shared files and tracking (`qaag-7kv`). Read CLAUDE.md, PRD
criterion 6, and `scouting/problem-first-r8.md`. No new subagents.
Write only `verdicts/problem-first-r8.md`.

Audit the actual operations and exact input/output scopes, not merely the
fact that the candidate failed. In particular:

- Derive the two-copy K and its coisometry identity after deleting/reindexing
  the zero constant coordinate. Verify its action on all allowed product
  inputs, its normalizer and its finite gate cost.
- The Schur--Cohn count recurrence uses real coefficients here. Do not
  replace complex reciprocal-conjugation by an unphysical conjugation gate.
- Derive both strict endpoint branches by Rouche. Equal endpoint modulus
  need not imply a unit-circle root: specify any recursive nondegeneracy
  promise and charge the gap required to learn each branch from copies.
- Keep the unit-disk recurrence distinct from the actual radius-5/8
  lower-bound query. On z^D-R^D with R=1/2,3/4, the unit-disk counts agree.
  Coefficient rescaling in the copies model is a charged filter.
- Independently verify the pure-state infidelity bound and the matching
  single-copy rare-outcome test for the promised separated-root family.
  Its target is a robust disk-count bit/approximation, not total variation
  against an unrounded atomic root distribution.
- Separate explicit coefficient-list input, copies, and coherent
  preparation-and-inverse access. Tree copy growth is a cost of the
  displayed construction, not a universal lower bound on every algorithm.

Use primary sources for targeted historical checks after deriving the map.
Every objection needs FIX DEMAND and SURVIVING STATEMENT. Bound probes,
fail nonzero on actual violations, and avoid unrelated test suites. A
mathematical PASS must not be presented as an original-algorithm success.
