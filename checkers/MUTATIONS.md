# MUTATIONS.md — one recorded red mutation per checker (rk-light law L4)

## Round-2 quotient-growth exploration (2026-09-04)

`explore/quotient_growth.py` has three model mutations, each selected by `--mutate`:
`fock` removes the Fock square root from the lowering matrix; `temperature` replaces
the upward jump amplitude `sqrt(t)` by `t`; `recycling` replaces the non-scalar
acceptance effect by its scalar average. Each must exit 1. These affect only the
in-process model, never tracked file contents. This exploration is excluded from
`run_all.sh`; it tests identities and obstructions, not a speedup or novelty claim.
Run each under `timeout 60 python3 -B explore/quotient_growth.py --mutate <name>`.
Recorded 2026-09-04: baseline exit 0 (137 checks); all three mutations exit 1.
Last failure reasons respectively: addition-channel normalization error 2.83;
Hilbert-series stationary-state error 0.202; acceptance-effect error 0.471.

"A checker with no red mutation does not exist."  Every checker in this tree has
at least one recorded mutation: an exact textual edit applied to a **copy** of
the suite in a fresh temporary directory (never to the tracked tree), after
which that checker must exit `1` with a printed reason.

## How these were produced

```
cd checkers
timeout 1800 python3 run_mutations.py          # plain summary, one line per mutation
timeout 1800 python3 run_mutations.py --md     # regenerates the sections below
timeout 600  python3 run_mutations.py task7    # substring filter
```

`run_mutations.py` holds the mutation table (target file, exact old text, exact
new text, and what the defect is).  It copies `checkers/` into a temp directory
with `shutil.copytree`, applies exactly one substitution (refusing to run if the
pattern does not occur exactly once), runs the single checker there under
`timeout 600`, and records the exit code and the last line of output.  It exits
nonzero itself if any mutation fails to turn its checker red.

Mutations are chosen to be *defects in the mathematics*, not in the assertions:
wrong Fock normalisation, a missing conjugation, a wrong initial ideal, a wrong
A-grading, a lost factor of 1/2 in the matrix of a quadratic form, a clause form
with the wrong sign, an ideal that is no longer a cone.  Eight of the seventeen
edit `bf.py` or `ideals.py` (the shared numerical core copied from the seed);
the rest edit the model set up inside the checker itself.

## Result of the recorded run (2026-09-02, this machine)

```
17 mutations run, 0 did NOT turn the checker red
```

Every entry below shows `Exit code: 1`.  A `0` in this file would mean the
checker does not test what it says it tests.

## Mutations

### `check_task1_conic.py`

- **Mutation** (in `bf.py`): drop the square root in the Fock matrix element of a(f): the falling factorial enters unsquare-rooted, so |k> = z^k/sqrt(k!) is no longer the orthonormal basis.
- **Exit code**: `1`
- **Last line**: `FAIL: N=2: Delta_N (Fact 7.1, conic Delta_N = N+1): got 5.0, expected 3 (rtol 1e-09, |diff| = 2 > 3e-09)`

### `check_task2_hilbert.py`

- **Mutation** (in `ideals.py`): change the twisted cubic's Hilbert function by one, 3N+1 -> 3N+2.
- **Exit code**: `1`
- **Last line**: `FAIL: twisted cubic P^3, N=1: dim ker H_N vs Hilbert function (Fact 2.1): got 4, expected 5`

### `check_task2b_subspace.py`

- **Mutation** (in `check_task2b_subspace.py`): write the spanning set of I_N in the UNNORMALISED monomial basis, i.e. forget that z^e = sqrt(e!) |e>; orthogonality to ker H_N is then a statement in the wrong inner product.
- **Exit code**: `1`
- **Last line**: `FAIL: twisted cubic P^3, N=2: max |<normalised I_N row, ker H_N>|: got 0.1691019787257628, expected <= 1e-10`

### `check_task3_gaps.py`

- **Mutation** (in `bf.py`): drop the Kostlan normalisation of random forms, so every random-quadric gap is rescaled and the published prefactors no longer apply.
- **Exit code**: `1`
- **Last line**: `FAIL: 2 generic quadrics: Delta_N prefactor (table 0.11): got 2.289843756738585, expected 0.11 +- 0.04 (|diff| = 2.17984)`

### `check_task3b_hard.py`

- **Mutation** (in `check_task3b_hard.py`): unbalance the singlet to 2|01> - |10>: still a rank-one 2-local projector, but no longer the ferromagnetic Heisenberg chain, so m^2 Delta -> pi^2 must fail.  (A pure sign flip to |01> + |10> is NOT a valid mutation: it is a local unitary conjugation by Z on alternate sites and leaves the whole spectrum invariant.).
- **Exit code**: `1`
- **Last line**: `FAIL: singlet chain m=2: m^2 Delta below pi^2: got 20.0, expected <= 9.869604402089358`

### `check_task3c_exact.py`

- **Mutation** (in `check_task3c_exact.py`): rescale one coefficient of the conic (z0z1 - 2 z2^2): the ideal is the same variety but the presentation changes, so Delta_N = N+1 must fail.
- **Exit code**: `1`
- **Last line**: `FAIL: conic N=2: Delta_N = N+1 exactly (Fact 7.1): got 9.000000000000002, expected 3 (rtol 1e-09, |diff| = 6 > 3e-09)`

### `check_task3d_nscale.py`

- **Mutation** (in `ideals.py`): scale the random quadrics by 2^(-n/4), so Delta decays exponentially in the number of variables instead of being flat.
- **Exit code**: `1`
- **Last line**: `FAIL: 1 random quadrics P^4, N=3: Delta in range: got np.float64(0.318294410096265), expected in [0.5, 5]`

### `check_task3e_ffstats.py`

- **Mutation** (in `check_task3e_ffstats.py`): stop projecting the forbidden state off the product state, so the chains are no longer frustration free.
- **Exit code**: `1`
- **Last line**: `FAIL: median Delta: fitted power-law exponent (published -3.5): got -2.238359661849822, expected in [-4.2, -2.9]`

### `check_task4_toric.py`

- **Mutation** (in `check_task4_toric.py`): use the wrong A-grading (i^2 instead of i) for the rational normal curve, so the claimed block decomposition is not the right one.
- **Exit code**: `1`
- **Last line**: `FAIL: rat normal curve deg4 P^4, N=2: H_N block diagonal over the A-grading: got 1.4142135623730951, expected <= 1e-12`

### `check_task5_groebner.py`

- **Mutation** (in `check_task5_groebner.py`): take the MINIMAL-weight terms as the initial form: the t=0 fibre is then not in_w(I) and the family is not flat (referee round 1, item 27).
- **Exit code**: `1`
- **Last line**: `FAIL: in_w(I) generators are (z0z2, z0z3, z1z3): got [(0, 0, 2, 0), (0, 1, 1, 0), (0, 2, 0, 0)], expected [(0, 1, 0, 1), (1, 0, 0, 1), (1, 0, 1, 0)]`

### `check_task6_2sat.py`

- **Mutation** (in `bf.py`): drop the conjugate in H_N = a^dag(f) a(f), so H_N is no longer the positive operator sum_j |f_j><f_j| on the multilinear sector.
- **Exit code**: `1`
- **Last line**: `FAIL: 3 generic forms, seed 0: multidegree-(1,1,1) sector identity (Sect. 3): got 15.72404652571691, expected <= 1e-12`

### `check_task7_coherent.py`

- **Mutation** (in `bf.py`): define a(f) = f(partial) instead of conj(f)(partial) -- exactly the notes' error corrected in report Sect. 9, item 3 (convention C3).
- **Exit code**: `1`
- **Last line**: `FAIL: random complex quadric in P^2, p=[1.    +0.j     1.    +0.j     1.0592+0.8497j], N=2: coherent-state energy formula (Sect. 3): got 8.771196299648457, expected 2.5268200870360534e-31 (rtol 1e-12, |diff| = 8.7712 > 1e-12)`

### `check_task8_cnf.py`

- **Mutation** (in `check_task8_cnf.py`): flip the sign in the positive-literal factor (z0 + z_i instead of z0 - z_i), so the clause form no longer vanishes exactly on the satisfying assignments.
- **Exit code**: `1`
- **Last line**: `FAIL: n=4 r2.0-0: dense and sparse solvers must agree on Delta_(n+3): got 0.05721545774870673, expected <= 1e-06`

### `check_task8_cnf.py::hf`

- **Mutation** (in `check_task8_cnf.py`): use the wrong multiplier-degree bound in the exact boolean-quotient Hilbert function (the clause forms are cubic, so multipliers run over degree N-3).  This leaves H_N untouched, so it isolates the HF claim: the checker must catch it by disagreeing with the independent GF(p) Macaulay rank and with the numerical kernel count.
- **Exit code**: `1`
- **Last line**: `FAIL: n=3 r4.2-0, N=3: exact boolean-quotient HF vs dim R_N - rank_GF(p)(full Macaulay): got 0, expected 8`

### `check_task9_pyramid.py`

- **Mutation** (in `check_task9_pyramid.py`): add a y^2 term to the pyramid relation, so the apex variable is no longer unused and the variety is no longer a cone.
- **Exit code**: `1`
- **Last line**: `FAIL: pyramid N=2: Delta_N = 2 exactly (unused variable pins the gap): got 4.0, expected 2.0 (rtol 1e-09, |diff| = 2 > 2e-09)`

### `check_fact71_bombieri.py`

- **Mutation** (in `bf.py`): rescale a(f) by 0.9, so H_N is scaled by 0.81 and the Bombieri lower bound Delta_N >= ||f||^2_Fock is violated by 19%.
- **Exit code**: `1`
- **Last line**: `FAIL: f = z0^1 in P^2, N=1: Fact 7.1 lower bound Delta_N >= ||f||^2_Fock: got 0.81, expected >= 0.999999999`

### `check_fact72_takagi.py`

- **Mutation** (in `check_fact72_takagi.py`): forget the factor 1/2 on the off-diagonal entries of the symmetric matrix of the quadric, so the Takagi values are wrong.
- **Exit code**: `1`
- **Last line**: `FAIL: conic z0z1 - z2^2 in P^2: ||f||^2_Fock = 2 sum_j tau_j^2 (Takagi form is norm preserving): got 6.0, expected 3.0 (rtol 1e-09, |diff| = 3 > 3e-09)`


## Notes on two of the mutations

- **`check_task3b_hard.py`.**  The first mutation tried was the obvious sign
  flip `|01> - |10>  ->  |01> + |10>`, and it did **not** turn the checker red
  (exit 0, `PASS: 65 checks`).  That is correct behaviour, not a hole: the two
  Hamiltonians are related by conjugation with `Z` on alternate sites, a local
  unitary, so kernel dimension, gap and `m^2 Delta` are identical.  The recorded
  mutation therefore unbalances the state to `2|01> - |10>`, which is a genuine
  change of model.
- **`check_task8_cnf.py`.**  Two mutations are recorded.  The sign flip in the
  clause form is caught by the dense-vs-sparse solver-agreement check, which
  runs first (the checkers are fail-fast).  To show that the headline claim
  `HF_{R/K}(N) = #SAT(phi)` is itself red-capable, a second mutation corrupts
  only the exact Hilbert-function routine (`tmax = min(N-3, n) -> min(N-4, n)`),
  leaving `H_N` untouched; it is caught by the disagreement with the independent
  GF(p) Macaulay rank.

## Secant three-copy exploration (2026-09-05)

`explore/secant_three_copy.py` is excluded from the seed suite. Updated baseline:
112 checks PASS in 1.5 seconds, with one BLAS thread and `timeout 60`.
Run the same command with the following `--mutation` options:

| Mutation | Changed model | Observed failure | Exit |
|---|---|---|---|
| `trine-sign` | Flip one trine coordinate | m=2 cat squared norm 4/3 instead of 1 | 1 |
| `normalization` | Drop cross terms from cat norm | m=2 cat squared norm 3/2 instead of 1 | 1 |
| `dephase-cat` | Replace coherent line projection by incoherent orbit mixture | rank-two completeness falls to 0.8683033841695673 | 1 |
| `cut-coefficient` | Replace the exact Schur-dependent coefficient by 1/6 | independently computed four-site average 0.007960476138700595 differs from 0.007075978789956082 | 1 |

These checks verify finite identities and can reject meaningful mutations;
they do not establish robustness constants, lower bounds, or historical novelty.

## Pair-support spectral checker (2026-09-05)

`explore/secant_pair_support.py` is excluded from the seed suite. Baseline:
1415 checks PASS in 0.2 seconds under `timeout 60` with one BLAS thread.
It compares independent permutation matrices and full tensor powers with the
analytic Schur-block formulas; 425 bounded blocks satisfy the gap test.

| Mutation option | Changed model | Observed failure | Exit |
|---|---|---|---|
| `drop-kernel-term` | Remove the exceptional rank-one term | trivial full-group spectrum differs by 1/6 | 1 |
| `wrong-phase` | Change -1/2 to +1/2 in the interference coefficient | full-group spectrum at a,b,c=0,0,1 differs by 2/3 | 1 |

## Coded Waring fusion checker (2026-09-05)

`explore/waring_coded_fusion.py` is excluded from the seed suite. Baseline:
418 checks PASS in 0.2 seconds with one BLAS thread and `timeout 60`. Literal
alternating projections, including a three-copy source seed, are compared with
the determinant formulas and separate labeling/Gram calculations.

| Mutation option | Changed model | Observed failure | Exit |
|---|---|---|---|
| `drop-guard` | Delete the last binary guard at rank >=4 | rank-four survivors 96 instead of 24 | 1 |
| `drop-phase` | Drop the determinant sign at rank >=4 | a rank-five survivor has phase +1 instead of -1 | 1 |
| `drop-factorial` | Omit the exterior normalization r! | literal rank-two projector norm is 0.4587312138098242 rather than 0.9174624276196485 | 1 |

## Direct Waring point tester (2026-09-05)

`explore/waring_programmable_test.py` is excluded from the seed suite. Baseline:
73 checks PASS in 0.4 seconds under `timeout 60` and one BLAS thread. It uses
literal source tensors, two alternating projections and a point equation, with
at most 3^12 amplitudes, and compares the complete event with a label-Gram formula.
It checks the general point-test construction, not only the terminal rank example.

| Mutation option | Changed model | Observed failure | Exit |
|---|---|---|---|
| `skip-seed` | Remove the source-program seed | a YES input produces event probability 1/16 instead of zero | 1 |
| `drop-program-row` | Omit a reference from the matching guard | a YES input produces event probability 1/16 instead of zero | 1 |
| `drop-factorial` | Remove exterior normalization | literal event 0.002265420572404712 disagrees with 0.009061682289618851 | 1 |
# R11 CP and geometry diagnostics (2026-09-07)

## R12 syzygy generator selection (2026-09-08)

`timeout 30 python3 -B checkers/explore/syzygy_plucker_r12.py` passed 1032
finite checks. The separate asymptotic lower bound is the analytic argument
in `argument/syzygy-generator-selection.md`, not a consequence of these tests.
Each `--mutate NAME` below returned exit 1; mutations change only the in-process
model and leave files unchanged.

| Mutation | Deliberate defect | Observed failure |
|---|---|---|
| `emitter-conjugation` | Replace Fock adjoint by transpose | Bath Gram residual 0.45808090965108744 |
| `antisymmetry-scale` | Omit the half in the antisymmetric projector | Claimed quarter-success becomes 1 |
| `rank-promise` | Replace flat rank two by flat rank three | Success becomes 1/3 instead of 1/4 |
| `sorted-pair-factor` | Forget the second ordering of a pair | Probability 1/2 instead of 1 in the q=2 fixture |
| `hom-sign` | Remove the beamsplitter coincidence minus sign | Coincidence rate 3/4 instead of 1/4 |
| `public-partition` | Let reference output depend on the hidden partition | Reference success 1 instead of 3/5 at d=3 |

The last mutation checks a necessary input restriction: public partition
metadata invalidates the claimed reference-independence bound.

`explore/cp_geometry_r11.py` checks finite Hermitian identities from
`scouting/root-frontiers-r11.md`. It is excluded from the historical seed runner.
Baseline: `timeout 30 python3 -B checkers/explore/cp_geometry_r11.py`, exit 0,
183 checks. Each following `--mutate` run exited 1 with a mathematical failure:

| Mutation | Changed ingredient | Observed failure |
|---|---|---|
| `harmonic-projector` | Put a non-harmonic vector into the proposed harmonic projector | `||dP||=0.4`, expected zero |
| `fusion-normalization` | Omit `sqrt(2)` from dual-number multiplication normalization | `lambda_max(K†K)=2`, expected at most one |
| `born-weight` | Replace the instrument's Born distribution by the desired label weights | Ensemble cancellation residual `0.4055697361777374`, expected zero |
| `absorbing-boundary` | Replace the absorbing successor boundary by a cyclic boundary | Fixed-state residual `sqrt(2)`, expected zero |

All mutations affect only the in-process model, not files. Run each with
`timeout 30 python3 -B checkers/explore/cp_geometry_r11.py --mutate NAME`.
These diagnostics do not prove a uniform theorem, novelty or quantum advantage.

The CE scattering extension subsequently passed 289 checks, including supercharge
nilpotence in weighted sectors zero through eight, the independent occupation-rule
construction of the four-state matrix, and its exact complex scattering amplitude.
Two additional mutations exited 1: `ce-merge-weight` omits the Fock `sqrt(6)`
coefficient (matrix residual `0.020498880527646594`), and `ce-fermion-sign`
omits the second creator's fermionic sign (`||Q²||=0.028284978345404478`).
Sources: `definitions/ce-scattering.md`, `scouting/ce-scattering-r11.md`.

## R13 compiler diagnostics (2026-09-08)

`OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 timeout 45 python3 -B
checkers/explore/syzygy_basis_r13.py` passed 241 finite checks. All seven
in-process mutations returned exit 1: `source-scale`, `padded-block`,
`shift-sign`, `luders-failure`, `antisymmetry-normalization`, `certificate-sign`,
`certificate-invalid`. They detect, respectively, source normalization,
padding, signed shifts, complement coherence, the antisymmetry factorial,
valid permutation phases and invalid-branch data disturbance. Finite checks
support the reviewed identities, not QSVT phase-computation complexity or the
uniform classical transcript theorem.

## R15 classical Picard controls (2026-09-08)

`timeout 30 python3 -B checkers/explore/picard_boolean_encoding_r15.py`
passed12588 finite exact checks, on instances with at most four Boolean
variables. These test algebraic encoding and rational slabs, not a uniform
complexity theorem or a Picard-rank computation on arbitrary surfaces.
All three in-process mutations returned exit1:

| Mutation | Failure |
|---|---|
| `dummy-not-unique` | Ten points instead of the expected three |
| `only-first-chart` | Segre equations falsely accept an invalid point on another chart |
| `allow-zero` | A supposed nonzero relation is supplied by the zero vector |

Run each with the same bounded command and `--mutate NAME`. No mutation edits
tracked files. The corresponding new statements remain SKETCH pending review.
