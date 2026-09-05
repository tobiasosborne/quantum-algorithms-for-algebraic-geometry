<!-- ROLE: current state + fast restart. Live goal checkpoint; <=150 lines. -->

# HANDOFF — 2026-09-05, interactive report and active research

The user asks for relentless construction and adversarial verification until a
GENUINELY NOVEL quantum algorithm is found. All classical and modern algebraic
geometry is in scope. The goal remains ACTIVE AND UNACHIEVED: a formal quantum
copy advantage is now proved, but the displayed mechanisms fail strict D22.
Do not mark the goal complete because a mathematical claim is PROVED.

## Interactive report

The requested report is `reports/research-report.html`, a self-contained offline
HTML artifact with seven explainers, 69 routes, 364 claims, 137 sources and glossary.
`reports/README.md` documents its reproducible build and browser verification.
The 57-check offline browser suite passes; independent targeted checks cover
navigation, high-refresh-rate animations and source-reader presentation.
Run `bd prime`, then read qaag-47l/qaag-tzn to resume the original research goal.

## Binding steering and workflow

- Run `bd prime`; use CLAUDE.md, PRD criteria 1–6 and D22–D24.
- New means an original problem-level result AND an original quantum mechanism.
  New applications, encodings and compositions of described algorithms do not
  qualify. Basic gates are allowed. No Grover/QFT/DQI reapplications; DQI and
  extensions are excluded. Derive before targeted primary-source verification.
- Only Astra/Sol subagents, at most two concurrently. Native collaboration is
  used; assigned lane files are disjoint and root owns shared registers.
- Use bd for tracking/memory; serialize its commands because even reads lock Dolt.
- Seed is read-only. No new full seed-suite run is warranted by these changes.
- Do not repeat familiarization or relaunch completed negative probes.

## Completed Waring same-bit-output copy separation

The clean algorithm is `scouting/waring-programmable-tester.md`, independently
accepted in `verdicts/waring-programmable-tester-r1.md`.
The lower bound is `scouting/waring-terminal-baseline.md`, independently
accepted in `verdicts/waring-terminal-baseline-r1.md`.
Canonical definitions: `definitions/waring-components.md`.

Source: copies of normalized T=sum_(a=1)^4 c_a u_a^tensor4, independent unit
components in C^q=C^d_A tensor C^d_B, q=d^2,d>=20, unknown components/coefficients,
with G>=1/2 and determinant-seed probability p0>=1/512. Decide whether
Gamma=(1/4)sum_a e5(Tr_B |u_a><u_a|) is zero or at least 10^(-6).
This tests a determinantal condition on the unique Waring points, not an explicit
component list or quantum-output-versus-tomography comparison.

The direct event uses FIVE original copies per trial: one r-copy antisymmetric
seed, one fixed-index programmable guard using the extra source, and the point
measurement on five A registers of the selected six-slot component row.
Joint event probability is at least (9/2^31)Gamma and is exactly zero on YES.
A sufficient source budget including an implementation margin is
2,137,652,311,842,450 copies. This is formal and impractical at this bound.
The general operator proof allows a supplied two-outcome measurement with effect
Q; sqrt(Q) is only a proof factorization, not a free oracle or a Q-block encoding.

Every adaptive global-single-original-copy POVM strategy needs at least
q^(1/4)/(4 sqrt24) copies. The proof uses moment-matched rank-four/rank-five
component spectra, hidden local Haar frames, positive Haar/Gaussian polynomial
norm comparison, and the Fock product inequality at each complete transcript.
Gaussian polynomial extensions are NOT renormalized as quantum states.
The lower bound permits arbitrary within-copy global measurements and unlimited
classical computation/memory; it is not a classical coefficient-list theorem.

The direct five-copy batch is also minimal among nontrivial batches with EXACT
perfect completeness. This does not establish total-copy or two-sided optimality.
Known universal comparison/programmable-discrimination operations implement the
mechanism: this formal separation DOES NOT establish the requested originality.

## Related proved mathematics and rejected mechanisms

- C-339--C-341: general secant pair-support identity, exact S4 compression and
  sharp uniform four-copy nonzero gap 1/12. Source `scouting/secant-pair-support.md`;
  independent PASS `verdicts/secant-pair-support-r1.md`. Generic filtering applies.
- C-342--C-344: coded Waring synchronization, seed ceiling and resource bound.
  Binary subsets reduce guards r-1 -> ceil(log2 r), but the seed costs at least
  r^(r+1) copies. See `scouting/waring-coded-fusion.md` and its PASS verdict.
- C-345: the formal terminal separation; C-347: the shorter direct upper;
  C-348: the scoped five-copy batch lower bound. These are PROVED.
- C-338 and C-346 are REFUTED novelty assertions. C-335--C-337 remain SKETCH.
- Rank-two Waring fusion is the GL-covariant redundant-Bell-fusion network,
  not an original algorithm. Its repaired mathematics passes its own verdict.
- Earlier trine-cat secant measurement reduces to random-cut rank tests within
  factor eight. Strassen testing reduces to known Schur/invariant networks.

## Other completed construction lanes

`verdicts/original-round2-r1.md` reviews the four old memos; five major
access/output/resource repairs were applied. Remaining minor conventions and
definitions are tracked by qaag-kdj before merging those old proposed rows.

Other completed files, all with no qualifying mechanism:
- `scouting/original-astra-round2.md`: nilpotent transport and bundle sewing;
  `scouting/original-enumerative-round3.md`: Hecke/flag-gallery classical attacks.
- `scouting/original-recovery-round3.md`: scoped triangular/mixed/Koszul recoveries;
  `scouting/chow-foulkes-audit.md`: Foulkes gap and exact-recovery obstructions.
- `scouting/original-residue-round3.md` and `verdicts/residue-packets-r1.md`:
  corrected residue metrics and classical attacks; high-energy gates remain held.
- `scouting/intrinsic-geometry-round4.md`: incidence/Fourier reduction and sampler.
- `scouting/degeneration-mechanism-r5.md`, same-name verdict: C-349--C-350
  give the rare-jet copy bound and retained-bath arithmetic/monodromy discrepancy.
- `scouting/reconstruction-mechanism-r5.md`, same-name verdict: C-351 compiles
  sparse trinomial multiplication and classically samples its tree output.
- `scouting/grassmann-streaming-r5.md`, independent same-name verdict:
  C-352 uses bilinear four-wise sign sketches with variance <=9k; full
  working bits O(m(b+log(kq)+log m)). Single/fixed queries only.
  These four rows are PROVED scoped mathematics, not an original algorithm.
  Canonical inputs: `definitions/mechanism-r5.md`.
- `scouting/theta-isogeny-r6.md`, independent same-name verdict: C-353--C-354
  prove exact cubist-metric theta transport with twisted, nonuniform sectors.
  Even k: exact separate-source sector sampler by local Weyl measurements/XOR.
  Odd k: logical Bell measurement, w_sector<=2^(-g). Full decoded classical
  sampling under explicit sample-and-query access costs O(g 2^g).
  Canonical inputs: `definitions/theta-isogeny.md`. D22 still fails.
- `scouting/hall-extension-r7.md`, independent same-name verdict: C-355--C-356
  fix Hall measures and flag-erasure norms, then derive an exact retained-order
  Yoneda obstruction with a matched classical matrix-vector test.
  Canonical inputs: `definitions/hall-extension.md`. No speedup.
- `scouting/spinor-mechanism-r7.md`, independent same-name verdict: C-357--C-358
  separate a six-CCZ coboundary phase/IQP circuit from the continuous associator
  filter (norm sqrt96). Classical scalar tests match. One-use real p<=1/24
  is not multiplicative: paired internal entanglement gives 7/512 for two uses.
  Canonical inputs: `definitions/octonionic-operations.md`. No north-star hit.
- `scouting/problem-first-r8.md`, same-name verdict: C-359--C-360 give the
  real Schur coisometry, p<=1/2 and expected fresh-child cost >=4^t, plus
  matching Theta((16/9)^D) quantum/classical copy costs for disk radius5/8.
  Geometric separation does not cure coefficient-state conditioning.
  Canonical inputs: `definitions/schur-disk-count.md`.

R9: C-361 proves exact support-to-Slater conversion with polynomial-rank/log-q
resources; C-362 proves approximate DPP sampling needs Omega(sqrt(q)) classical
copies versus a q-independent quantum cap (flat rank2, TV1/16: 15copies suffice).
C-363 excludes exact universal separable samplers for 2<=r<q. C-364 rejects
originality via known GPE, multiplicity reset and the same exact certificate.
Sources: `scouting/support-plucker*.md`, `verdicts/support-plucker-r9.md`;
canonical inputs: `definitions/support-plucker.md`. Exact support/gates matter.
Do not reopen known root-extraction, moment-map or pure-spinor probes (bd memory).

## Verification, tracking and repository

Four bounded checkers total 2018 checks and twelve red mutations; see
`checkers/MUTATIONS.md`. Numerical probes support, rather than replace, proofs.

Active: qaag-47l (persistent original-algorithm exploration), qaag-tzn (synthesis).
Open minor reconciliation: qaag-kdj. Blocked remote setup: qaag-9t7.
Register ends C-364; the r9 construction and independent audit are integrated.

Completed artifacts are committed locally. Git and Beads Dolt have NO remotes;
required pushes were attempted and failed. A remote URL question is pending
with the user. Do not invent a destination or create a hosted repository.
