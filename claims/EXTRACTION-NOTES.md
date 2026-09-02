<!-- ROLE: audit trail for the extraction that produced claims/CLAIMS.md.
     Ambiguities, splits/merges, definition slugs used, and everything in the seed that
     looks wrong. Not a claims file: nothing here carries a status. 2026-09-02. -->

# Extraction notes — claims/CLAIMS.md

Sources, read in the order the brief gives: `CLAUDE.md`,
`seed/analysis-2026-09-01/report.md` (treated as an untrusted proposer document),
`seed/analysis-2026-09-01/referee/round1.md` and `round2.md`, `HANDOFF.md`,
`seed/page81.tex`. Numerics under `seed/analysis-2026-09-01/numerics/` were read for the
`where-tested` column. Nothing under `seed/` was modified.

Result: 254 rows — 157 SKETCH, 40 CONJECTURE, 57 REFUTED, 0 PROVED. 529 claim-to-claim
edges, verified acyclic.

## 1. Ordering and id scheme

Ids are assigned in order of appearance across three passes, because the sources are three
documents and "order of appearance" is not otherwise defined:

- C-001–C-180: `report.md`, §1 through §9, in document order.
- C-181–C-208: `page81.tex`, in sheet order s01–s08.
- C-209–C-254: draft claims refuted by `referee/round1.md` then `round2.md`, in finding
  order within each round.

`page81.tex` is logically PRIOR to the report, so its rows carry the higher ids only for
readability of the report section. Where a report row and a page row state the same thing,
the report row is the one other rows depend on, and the page row carries a
`surviving statement:` pointer. Page rows never depend on report rows (that would make the
DAG cyclic; four such edges were removed, see §6).

## 2. Which referee findings became REFUTED rows, and which did not

The brief says anything the seed or a referee round refuted enters as REFUTED with the
surviving weaker statement as a separate row. The seed's `report.md` is the REVISED draft:
it has already absorbed round 1 and round 2, so almost every referee finding names a claim
that no longer appears anywhere in the seed. Policy actually applied, and the reason:

- **A separate REFUTED row** for every round-1 FATAL (#14, #17, #20, #21, #26, #27, #40,
  #45, #49, #51, #56, #61, #62, #67, #74, #77) and every round-2 FATAL (#4, #13), plus
  those "significant"/"minor" findings whose surviving statement is materially weaker or
  whose refutation a future proposer could plausibly re-derive (#1, #2, #3, #4, #6, #8, #9,
  #10, #12, #13, #22, #23, #25, #29+#30, #31, #32, #33, #36, #37, #38, #42, #43+round2 #6,
  #44, #64, #65+#66; round2 #1, #7, #18). 46 rows, C-209–C-254.
- **Recorded in the `referee:` line of the surviving row, not as a separate REFUTED row**,
  for findings that are corrections of exposition rather than of a claim, or that the report
  answers by ADDING material rather than by withdrawing a claim: round1 #5, #7, #11, #15,
  #16, #18, #19, #24, #28, #34, #35, #39, #41, #46, #47, #48, #50, #52, #53, #54, #55, #57,
  #58, #59, #60, #63, #66, #68, #69, #70, #71, #72, #73, #75, #76; round2 #2, #3, #5, #8,
  #9, #10, #11, #12, #14, #15, #16, #17. Every one of these is quoted in the `referee:` line
  of the row it bears on, so no finding is lost.
- Round 1 lists 77 findings, round 2 lists 18. Every one is accounted for in exactly one of
  the two categories above.

**The standing overall verdict.** Round 1 finding #77 is a FATAL verdict on the whole
quantum-algorithmic programme. Round 2's opening line says "All requested points omitted
below are correctly fixed", but it then raises 18 further findings including two FATALs and
never retracts #77, and there is no round 3. C-250 records this. It is the reason no row
enters as SKETCH-plus: the seed arrives with an unretracted FATAL.

## 3. Claims split, merged, or promoted from prose

- **Split.** Proposition 3.1 became six rows (C-034–C-039): the `k=2,q=2` P result, the
  `(2,5)` `QMA_1`-completeness, the `k=3,q=2` `QMA_1`-completeness, the monomial/`k`-SAT
  case, the "no NO-gap promise" caveat, and the Nullstellensatz remark. They have different
  citations, different truth status, and round2 #1 refuted one of them alone.
- **Split.** Fact 4.2 became C-044 (forward) + C-045 (converse) + C-046 (non-invariance),
  because round2 #4 refuted the converse alone.
- **Split.** Fact 7.1 became C-103 (the bound) + C-104 (the equality condition), because
  round1 #43 and round2 #6 refuted the equality claim alone.
- **Split.** Fact 7.2 became C-107 (Takagi normal form) + C-108 (the two-sided bound) +
  C-109 (the cone interpretation): (i) is a normal form, (ii) is checkable arithmetic, (iii)
  is an interpretation. None is tested.
- **Split.** Conjecture 8.3 became C-132–C-143; 8.4 became C-144–C-146; 8.6 became
  C-150–C-156; 8.8 became C-159–C-162; 8.9 became C-163–C-165; 8.10 became C-166–C-169;
  8.11 became C-170–C-172. Each sub-part is separately checkable and several have different
  status (8.3(d) is essentially a theorem; 8.3(e) is a question).
- **Merged.** The report's §1 remark that the notebook's `L^2(CP^n)` should be a holomorphic
  space and its §9.2 correction are one claim, C-006, with C-174 as the §9 pointer.
- **Promoted from prose to a row.** C-024 (the conic Hamiltonian IS the Law–Pu–Bigelow
  spin-mixing Hamiltonian, already realised in the laboratory) appears only as a subordinate
  clause in report §3 and in HANDOFF.md, yet it is the campaign's only contact with real
  hardware and therefore with the north star's second requirement. C-075 (the "looks
  genuinely new" assessment) and C-110 ("no such inequality seems to be in the literature")
  were likewise promoted: both are novelty claims, both are load-bearing for the north star,
  and neither is a mathematical statement, so both are marked CONJECTURE and flagged as
  needing a literature scout rather than a proof.
- **Numerics folded, not split.** Numerical confirmations were put in the `where-tested`
  field of the claim they confirm, EXCEPT where the numerical statement is itself the claim
  and has no proof (C-073, C-090, C-113, C-117, C-118, C-119, C-120, C-142, C-151), which
  are separate rows so that a critic can attack the data independently of the theory.

## 4. Ambiguities in the seed, and the reading recorded

Where the seed is ambiguous the brief asks for the strongest precise reading its own proof
supports. The non-obvious cases:

1. **Conjecture 8.3(a)'s constant** (report L226). The preamble fixes unit Bombieri–Weyl
   generators; the monomial case is stated with monic generators and `c = min_j α^{(j)}!`.
   These are different normalisations. C-133 records BOTH, marked as such, and does not
   choose. Matches definitions lane OPEN-2 and referee round2 #9.
2. **What the survey measures** (report L200–L212). The table says "unit-coefficient
   generators as written"; the conjectures it is evidence for fix unit Bombieri–Weyl
   generators; and the table reports `||H_N||/Δ_N` while every promise is on `Δ_N/α_BE`.
   C-117 records the table verbatim with its stated normalisation and C-058 records that the
   promises are on a different quantity. The numerics therefore do not directly measure what
   the conjectures promise. Matches definitions lane OPEN-1 and OPEN-3.
3. **Fact 4.2's title versus its proof.** Titled as a statement about IDEALS; proved from a
   GENERATOR support condition, which the same paragraph shows is not ideal-invariant.
   C-045 records the narrowed (monomial, uncoverable-support) form actually proved and C-046
   records the non-invariance. Matches OPEN-6 and round2 #4.
4. **`Δ_N(0)` equality versus lower bound** (report L204). Stated as `≥`, then used as if
   `=` in the `N`-independence claim. C-072 records the `≥` and the explicit
   `f = x^2y + xy^2` counterexample to equality; C-144 records the conjecture with the
   `≥` reading only.
5. **"Task 5.4 (direction, not a claim)".** The report explicitly declines to claim it.
   Recorded as CONJECTURE (C-065, C-067, C-068), not SKETCH, since no proof is offered.
6. **Conjecture 8.5's "theorem part".** The report says the theorem part is in its §8 list
   and only the descriptive part is conjectural. C-028/C-029 carry the theorem part
   (SKETCH); C-147/C-148 carry the conjectural part; C-149 carries the negative.
7. **`page81` computes in a basis it did not define.** The page defines the sphere
   orthonormal basis (C-184) but every worked example is correct only in the unnormalised
   monomial basis. Each affected row (C-190, C-192, C-193, C-194) says which basis it is
   read in. Matches OPEN-8.

## 5. Things in the seed that look wrong (file:line)

Ordered by severity. Items 1–3 are NEW here or in the concurrent definitions lane: neither
referee round caught them, and the report's §9 does not list them.

1. **`report.md` L228 (Conjecture 8.3(b) forward direction): the inequality goes the wrong
   way for `d ≥ 2`.** The report says `h_j = w^{N-m_j}` shows `Δ_N ≤ min_j ||f_j||^2` "up to
   the syzygy correction". `Δ_N` is a minimum over vectors ORTHOGONAL to `Syz(I)_N`. The
   test vector `w^{N-m_j} e_j` is not in general orthogonal to `Syz(I)_N`; writing `P` for
   the projection onto `Syz(I)_N^⊥`, `Φ_N v = Φ_N Pv` while `||Pv|| ≤ ||v||`, so the
   Rayleigh quotient of `Pv` is `≥` that of `v`, i.e. the projection RAISES it. The bound is
   therefore established only where `Syz(I)_N = 0`, i.e. `d = 1` — which is exactly the
   pyramid example the report offers, a principal ideal. C-135 has been restated
   accordingly and downgraded to CONJECTURE for `d ≥ 2`. (Same finding as definitions lane
   OPEN-5 and, in weaker form, referee round2 #10.)
2. **`page81.tex` L174–L176: a false vanishing criterion, not in the seed's §9 corrections
   list.** The page asserts `a(f_0)|k_0 ... k_n> = 0` if `Σ_{j≥2} k_j = 1`. With
   `a(f_0) = ∂_0∂_1 - ∂_2^2` one has
   `a(f_0) z^k = k_0 k_1 z^{k-e_0-e_1} - k_2(k_2-1) z^{k-2e_2}`, so `k = (1,1,1)` satisfies
   the hypothesis yet `a(f_0) z_0z_1z_2 = z_2 ≠ 0`. Verified independently here. The correct
   condition is `k_2 ∈ {0,1}` AND (`k_0 = 0` or `k_1 = 0`). C-193 is REFUTED on the second
   clause. (Same as OPEN-11.)
3. **`report.md` L146 (§5.7): `δ(f) = ||[f]||` is off by `||f||`.** L144 defines
   `δ(f)^2 = <f|P_0|f>/||f||^2`, so `δ(f) = ||[f]||/||f||`. Harmless inside Conjecture 8.1,
   which imposes a unit `f`; not harmless in §5.7, which does not. The same omission
   propagates to the RKHS reading. C-078 states the corrected identity. (Same as OPEN-7.)
4. **`page81.tex` L65: `ℓ_j ∝ a_j` is false as an operator statement.** In the Fock basis
   `a_j^†|k> = sqrt(k_j+1)|k+e_j>` while `ℓ_j^†|k> = |k+e_j>`; the ratio is occupation
   dependent. The correct relation is `a_j^† = J_j sqrt(n̂_j+1)` (report L116). C-187 is
   REFUTED. Every later page construction that uses `J` rather than `a` (C-203, C-208)
   inherits this. (Same as OPEN-9.)
5. **`report.md` L184: "in one variable `Δ_N = N!/(N-m)!`" has ambiguous scope.** True for
   the monomial `f = z^m`; for a general one-variable `f` of degree `m` the value is
   `Σ_j |f_j|^2 (j+N-m)!/(N-m)!`. C-104 carries the scope restriction. (Same as OPEN-13.)
6. **`page81.tex` L207–L219: `H'` is used inconsistently.** L208 defines
   `H + L_f^† L_f = H'`; L213, L228, L245 then use `ker(H + H')` as if
   `H' = L_f^† L_f`. Recorded on C-195. (Same as OPEN-10.)
7. **`report.md` §7 numerical survey versus `task3e_out.txt`.** The report says of random
   frustration-free 2-local chains that "a power law fits better than an exponential";
   `task3e_out.txt` reports only an exponential fit, `median Δ ~ 0.805 e^{-0.556 m}` with
   per-site ratio `0.574`. The report's own caveat ("`m ≤ 11` cannot exclude a slow
   exponential") is the weaker and defensible reading and is what C-120 and C-142 record.
   A critic should re-run the comparison before either reading is used.
8. **`report.md` §6, Anschuetz–Bauer–Kiani–Lloyd 2023 (C-099) carries no identifier**, and
   neither referee round addressed it, although it is the sharpest classical-competitor
   claim in the seed. Marked `[UNVERIFIED]`.
9. **`report.md` §1 versus §5.1 on which norm the distance is measured in.** §1 fixes Fock;
   L137 writes `dist_BW`. The ratio is the same in all three norms (degreewise
   proportionality, C-002), so this is harmless, but it should be fixed once. (Same as
   OPEN-4.)
10. **`page81.tex` transcription defects** (L184 `a(f_1)|11>` where `f_0` and a 3-mode ket
    are meant; L286 "`(1) = R`"; L280 and L348 malformed; L367 `m+1` where `n+1` is meant).
    Recorded so that any argument citing page81 cites the corrected object. (Same as
    OPEN-12.)

## 6. Structural edits made to keep the DAG a DAG

Eleven back-edges arose from rows that cross-reference each other (a parent conjecture and
its containment/hardness sub-rows, a task and its geometric identification, a report row
and the notebook row it sharpens). In each case the edge from the PRIOR object to the
DERIVED one was kept and the reverse removed, leaving the cross-reference in the prose:
`C-187 -/-> C-049`, `C-056 -/-> C-047`, `C-078 -/-> C-059`, `C-096 -/-> C-150`,
`C-083 -/-> C-124`, `C-124 -/-> C-125, C-126`, `C-085 -/-> C-166, C-167`,
`C-086 -/-> C-168`, `C-121 -/-> C-140`, `C-129 -/-> C-130, C-131`.

## 7. Definition slugs used

The definitions lane merged into `definitions/definitions.md` while this extraction was in
progress. All slugs below were reconciled against that register; every slug cited in
`CLAIMS.md` resolves there EXCEPT the two listed as requested-new.

Resolved against the register (65 in use): `D-adiabatic-groebner-complexity`,
`D-annihilation-of-form`, `D-bergman-projector`, `D-block-encoding-normalisation`,
`D-bombieri-weyl-norm`, `D-boolean-ideal`, `D-clause-ideal`, `D-coherent-gram-matrix`,
`D-coherent-state`, `D-compressed-multiplication`, `D-condition-number`, `D-cone`,
`D-creation-of-form`, `D-distance-to-ideal`, `D-distance-to-ideal-problem`,
`D-dqc1-style-estimate`, `D-drury-arveson-space`, `D-entangled-defect`, `D-few-mode`,
`D-fock-basis`, `D-frustration-free`, `D-groebner-deformation-path`, `D-hard-core-generators`,
`D-hard-gap-instances`, `D-hilbert-function`, `D-history-state`, `D-homogeneous-ideal`,
`D-initial-ideal`, `D-input-model`, `D-inverse-system`, `D-k-body`, `D-kostlan-random-form`,
`D-macaulay-gap`, `D-macaulay-matrix`, `D-multidegree-sector`, `D-normalised-gap`,
`D-parent-hamiltonian`, `D-polynomial-ring`, `D-projectors`, `D-qsvt`, `D-quantum-k-sat`,
`D-saturation-regularity-stable-range`, `D-shift-operator`, `D-sphere-norm`,
`D-spin-mixing-hamiltonian`, `D-symmetric-sector`, `D-syzygy-module`,
`D-takagi-factorisation`, `D-toeplitz-operator`, `D-toric-ideal`, `D-variety`.

Slugs this extraction guessed that the register spells differently; the mapping applied
(guess -> register), recorded so the reconciliation is auditable: `D-graded-ring` ->
`D-polynomial-ring`; `D-arveson-d-shift` -> `D-drury-arveson-space`;
`D-veronese-symmetric-sector` -> `D-symmetric-sector`; `D-hilbert-polynomial` ->
`D-hilbert-function`; `D-regularity`, `D-saturation` ->
`D-saturation-regularity-stable-range`; `D-macaulay-inverse-system` -> `D-inverse-system`;
`D-ground-space-projector` -> `D-projectors`; `D-compressed-shift`,
`D-stickelberger-multiplication` -> `D-compressed-multiplication`; `D-multigraded-sector` ->
`D-multidegree-sector`; `D-quantum-ksat` -> `D-quantum-k-sat`; `D-k-body-locality` ->
`D-k-body`; `D-few-mode-locality` -> `D-few-mode`; `D-shift-operator-J` ->
`D-shift-operator`; `D-unary-degree-encoding` -> `D-input-model`;
`D-dqc1-trace-estimation` -> `D-dqc1-style-estimate`; `D-scheme-length`,
`D-radical-ideal`, `D-vanishing-ideal`, `D-fubini-study-distance` -> `D-variety`;
`D-groebner-basis`, `D-standard-monomial` -> `D-initial-ideal`; `D-groebner-degeneration` ->
`D-groebner-deformation-path`; `D-groebner-fan` -> `D-adiabatic-groebner-complexity`;
`D-rkhs-restriction-norm`, `D-berezin-symbol` -> `D-bergman-projector`;
`D-gram-matrix-coherent` -> `D-coherent-gram-matrix`; `D-guided-local-hamiltonian` ->
`D-distance-to-ideal-problem`; `D-berezin-toeplitz` -> `D-toeplitz-operator`;
`D-feynman-kitaev` -> `D-history-state`; `D-motzkin-chain` -> `D-hard-gap-instances`;
`D-condition-number-bc` -> `D-condition-number`; `D-cone-locus` -> `D-cone`;
`D-takagi-values` -> `D-takagi-factorisation`; `D-a-grading-fibre`, `D-fibre-sum` ->
`D-toric-ideal`.

**Two slugs requested but absent from the register**, used in C-016, C-017, C-163 and
C-249: `D-arveson-curvature` (Arveson's curvature invariant; needed for the
curvature = leading multiplicity of the Hilbert polynomial statement) and
`D-essential-normality` (Schatten-`p` membership of `[Z_i, Z_j^†]`, the Arveson–Douglas
conjecture, with the affine-cone dimension threshold). The register has
`D-drury-arveson-space` and `D-compressed-multiplication` but neither invariant. Definitions
lane: please add, or tell this lane which existing slug to fold them into.

Register conventions this file follows: C1 (Fock default), C3 (`a(f) = conj(f)(∂)`), C5
(unit Bombieri–Weyl generators for gap statements), C7 (`α_BE`, never bare `α`) — with one
departure, noted next.

**Convention C7 (`α_BE`, never bare `α`).** Applied throughout `CLAIMS.md`: every
occurrence of the block-encoding normalisation is written `α_BE` (patterns `α_BE/Δ`,
`Δ_N/α_BE`, `α_BE`-normalised, `α_BE(t)`). The bare `α` survives ONLY as a multi-index —
`z^α`, `f_α`, `α^{(j)}!`, `Σ_α`, `J^α`, `w·α` — which is the standard algebraic-geometry
use and does not collide. Conventions C1, C3, C5, C8, C10 and C12 are followed as written.
C9 is NOT followed in the Fact 7.2 rows: they use the report's `d_j`, `d_min` for the Takagi
values rather than the register's `τ_j`, `τ_min`, because those rows quote the report's
displayed inequality verbatim and a silent symbol substitution inside a quoted formula would
be worse than the departure. C-107/C-108/C-109 say `Takagi values` in words; the critical-
claims section uses `τ_min`. Flagged here so the orchestrator can decide.

## 8. What this extraction deliberately did not do

- No status was raised. Every seed "theorem-level" item is SKETCH, including the ones the
  report's §8 list calls theorems (that list is itself a row, C-123).
- No citation was fetched. Identifiers appearing in `CLAIMS.md` are those the referee rounds
  themselves resolved (Bravyi quant-ph/0602108; Gosset–Nagaj 1302.0290;
  Rudolph–Gharibian–Nagaj 2401.02368; Dickenstein–Tobis 1003.3508; Levine–Movassagh
  1611.03147; Chabaud et al. 2410.04274; Ding et al. DOI 10.22331/q-2023-07-26-1069).
  Koiran 1996 (DIMACS TR 96-27), Anschuetz–Bauer–Kiani–Lloyd 2023, Beauzamy–Bombieri–Enflo–
  Montgomery, Law–Pu–Bigelow 1998, Fang 2003, Eisenbud Thm 15.17, Engliš–Eschmeier,
  Douglas–Tang–Yu, Gharibian–Le Gall 2022, Chen–Gao, Beltrán–Pardo, Lairez,
  Bordemann–Meinrenken–Schlichenmaier and the Tian–Zelditch–Catlin/Ohsawa–Takegoshi
  pointers are all `[UNVERIFIED]` in this campaign and must not enter `refs/` until fetched.
- No numerics were re-run. `where-tested` records which script covers a row and at which
  range; it does NOT assert the script is correct. `checkers/MUTATIONS.md` is empty, so
  under L4 none of the seed numerics is yet a red-capable checker.
- `PRD.md` was absent when this extraction began and was created by another lane while it
  ran; the MERGE PROPOSAL at the end of `CLAIMS.md` is therefore written as an APPEND to its
  §6 Decision record, per that file's stated update policy (decision rows are appended,
  never rewritten). PRD §2 criterion 2 ("best-known classical baseline, adjudicated by a
  critic") is the criterion C-087 and C-172 exist to satisfy, and no row in this file yet
  meets it; PRD §2 criterion 5 (heuristic hardware attack) is met in outline only by C-024.
