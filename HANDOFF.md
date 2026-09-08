# HANDOFF — 2026-09-08, timed research round closed

The user requested work until about03:00 Berlin (01:00UTC2026-09-08), then
commit, push and STOP. At the later status check,05:03UTC, the cutoff had
passed and both Sol runs had hit their service usage limits. Research stopped;
only final verification, integration and synchronization followed. Do not
resume exploration automatically without a new user instruction.

## Current success criterion

PRD D25 supersedes D22's strict historical-originality gate. New means not
QFT/Grover/DQI in disguise. QSVT qualifies. Adiabatic QC qualifies unless it
only Feynman--Kitaev-encodes Grover/QFT; quantum walks qualify for useful AG
problems. Supersymmetry and syzygies are specifically encouraged. Known
nonexcluded mechanisms are not automatically disqualified. This round used
Sol xhigh proposer/critic agents, at most two concurrently.

## Proved useful result: choose original generators

C-374--C-376 are PROVED after `verdicts/syzygy-advantage-r12.md`.
Canonical input: `definitions/syzygy-plucker-r12.md`.
Readable proof: `argument/syzygy-generator-selection.md`.
Construction and scope: `scouting/syzygy-plucker-r12.md`.

An unknown 2-by-q row coisometry gives a based redundant quadratic tuple
spanning `(z0²,z1²)`. Its fixed Fock-emission source delivers `rho=C†C/2`.
The task returns ANY two ORIGINAL labels generating the same ideal.
Four ordinary two-copy swap trials use at most8copies and succeed with
probability175/256>2/3. For q=2d,d>=3, every adaptive separate-copy POVM
strategy with fixed capT obeys T(T-1)>=d(d-2)/(3(d-1)). Strict cap-eight
separation starts at evenq=340. No prescribed DPP law is required for this
stronger useful theorem; the additional twenty-copy volume sampler is C-376.

Scope is essential: independent fixed quantum-source copies, no coefficient
list, purification, public hidden partition, preparation inverse, controllable
incident state, or cross-copy quantum memory for the classical comparator.
A two-photon HOM experiment tests the instrument at small q. One-time device
construction and per-copy delivery are charged; no practical hardware or
explicit-coefficient-list advantage is claimed.

The accepted classical upper is O(q logq) copies via two-design tomography;
the lower is Omega(sqrt q). A CONTROLLABLE incident source changes the problem:
a two-query classical controller succeeds with probability>=2/3. Both facts
are proved in scouting sections5B/6A and independently audited. The source-only
assumption must never be hidden in a future write-up.

## Proved growing-rank QSVT extension

C-377--C-381 are PROVED after `verdicts/syzygy-basis-r13.md`.
Canonical definitions: `definitions/syzygy-basis-r13.md`.
Full construction: `scouting/syzygy-basis-r13.md`.

For rankr>=3 the based degree-(r-1) tuple generates `(z0,z1)^(r-1)`, a
nonreduced fat point of lengthr(r-1)/2. The fixed emitter is an isometry,
with success1 and sourceC†C/r. QSVT integer-content windows replace Fourier
measurements. The exact padded retry bank gives a Lueders instrument; its
failed branches and all approximation errors are charged. Permutations keep
exact source support. A correct exterior column survives every failed signed
certificate, so retries consume ancillas/time but no fresh source copies.

Per-batch acceptance>=103/256>3/8. Three batches at delta1/3 use6r² copies.
For q=rd,d>=2, classicalT(T-1)>=4q/(9r). A sufficient strict-copy threshold
is q>(9r/4)(6r²)(6r²-1), leading81r^5. This is a COPY comparison throughout
that regime. The full quantum compiler/gate count is polynomial in r,logq;
it is polynomial in logq when r<=poly(logq). Do not equate the whole q/r^5
regime with an unqualified wall-clock advantage. The simpler direct fallback
has overlap1/r^r, not r!/r^r, and severe rank cost.

## Tournament and remaining scientific work

The initial R11 portfolio registered42 candidates:17 geometry,16 thermal/CP,
8 root alternatives and the finite CE continuation. The portfolios and
independent verdicts are in `scouting/*frontiers-r11.md` and matching verdicts.
R11 C-365--C-373 remain SKETCH controls; no extra promotion was inferred from
finite checks. The CE cubic supercharge is exact but fixed size, and its
resonance is a known spin-3/2 transfer chain. D25 permits that mechanism; it
still has no asymptotic advantage.

`scouting/syzygy-bosonsampling-r12.md` is retained as a HOLD: correct syzygy/
optical algebra and conditional hardness reductions, but no established useful
syzygy-specific consumer or unconditional classical-input speedup. Some finite
approximate-ensemble and loss assumptions remain explicit.

Follow-up qaag-gff records the classical source-only generator-selection gap.
A Sol run suggested an O(q) Haar-covariant upper but hit the service limit
before producing an artifact or independent review. That suggestion is NOT
registered as proved. The accepted upper remains O(q logq).

The six inherited R10 higher-obstruction files are archived unchanged. Their
interim audit and Gramian repair are not completed or promoted. Existing
qaag-bd6/qaag-6xn retain that outstanding scope. Do not restart their known
monitored-return mechanism as unexplored novelty.

## Verification and publication

The new checker suites pass289+1032+241=1562 finite checks and19 red mutations.
They support finite identities, not the uniform Haar lower bounds or QSVT
compiler theorem. The broad historical seed suite was not rerun.
The maintained offline report contains77routes,381claims and162sources;
57browser checks and9Git-hook tests pass. Build commands are in reports/README.md.
The report now states current D25 and the fixed-source generator-selection hit;
historical D22 verdicts retain their old scope. Public repository is
`tobiasosborne/quantum-algorithms-for-algebraic-geometry`, branch master,
AGPLv3. Final workflow commits and pushes Git plus Beads before stopping.
