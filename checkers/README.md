<!-- ROLE: red-capable checker suite for the seed analysis (rk-light law L4).
     UPDATE POLICY: add a checker only with a recorded red mutation in MUTATIONS.md.
     TRIGGER: read before running or citing any checker. -->

# `checkers/` — red-capable checker suite

Sixteen checkers turning the seed numerics
(`seed/analysis-2026-09-01/numerics/`) into tests that can **fail**. Each one
states at the top which seed claim it tests (report section plus the numbered
Fact / Prop / Conjecture), exits `0` only when every tested property holds
within a stated tolerance, and exits `1` with a printed reason otherwise. Every
checker has a recorded red mutation in `MUTATIONS.md`.

The seed report is a **proposer document**, not established truth. Nothing here
promotes any of its claims; a PASS says "the stated numerical property holds on
the tested range at the stated tolerance", nothing more. In particular all the
Section 8 items remain conjectures: what is checked is the *numerical evidence
the report cites for them*, not the conjectures.

## Running

```bash
cd checkers
timeout 2400 ./run_all.sh                       # all 16, PASS/FAIL + wall time
timeout 600  ./run_all.sh check_fact72_takagi.py  # a subset
timeout 1800 python3 run_mutations.py           # the red mutations (MUTATIONS.md)
timeout 300  python3 explore/explore_dynrange.py  # exploration, no exit code
```

`run_all.sh` runs every checker under `timeout` with a per-script budget (about
5x the measured wall time), prints PASS/FAIL and wall time per checker, writes
per-checker output to `logs/`, and exits nonzero if any checker fails.

Python on this machine: 3.12.3, numpy 2.4.6, scipy 1.17.0, sympy 1.14.0. All
three are present; nothing is missing. `scipy` is used only by
`check_task8_cnf.py` (sparse `a(f)`, deflated LOBPCG); `sympy` only by
`check_task1_conic.py` and `check_task2_hilbert.py` (exact symbolic ranks and
the symbolic form of Fact 2.3).

## Discipline (rk-light L4)

- **No bare `assert`.** `grep -rn assert *.py` finds only two occurrences, both
  inside comments/docstrings. `python3 -O check_*.py` behaves exactly like
  `python3 check_*.py`; spot-checked on three checkers.
- **Fail-fast with a printed reason.** `checkharness.py` raises `CheckFailure`
  on the first violation; the last line of output is always `FAIL: <reason>`
  (or `PASS: <k> checks in <t>s wall`). Exit `2` is reserved for "the checker
  could not run at all" (unexpected exception).
- **Bounded.** Every checker declares its dimension caps at the top of the file
  and every run in `run_all.sh` and `run_mutations.py` goes under `timeout`.
- **Seed is read-only.** `bf.py`, `ideals.py` and `gaps.py` here are byte-for-
  byte copies of `seed/analysis-2026-09-01/numerics/`; the task scripts were
  copied and refactored for exit codes with their numerical content preserved
  (same ideals, same seeds, same N ranges except where a cap is listed below).

## Conventions

`definitions/definitions.md` is the single source (L2). Objects used here:
`D-fock-space`, `D-fock-basis`, `D-annihilation-of-form`, `D-hamiltonian`,
`D-macaulay-matrix`, `D-macaulay-gap`, `D-hilbert-function`, `D-inverse-system`,
`D-toric-ideal`, `D-boolean-ideal`, `D-clause-ideal`, `D-initial-ideal`,
`D-groebner-deformation-path`, `D-coherent-state`, `D-coherent-gram-matrix`,
`D-multidegree-sector`, `D-cone`, `D-kostlan-random-form`,
`D-takagi-factorisation`.

**Departure from convention C5.** C5 fixes gap statements to *unit
Bombieri-Weyl* generators. The seed's numerical survey does not use that
normalisation (this is OPEN-1 in the definitions register), and this suite
reproduces the seed, so every `Delta_N` here is the gap of the presentation
**as written** (unit coefficients on the monomials of each generator). Every
checker docstring repeats this. Consequences that matter: `Delta_N` of the
conic is `N+1` in this normalisation, not the unit-BW value; the boolean
`Delta = 2` is likewise presentation-dependent. Convention C9 (Takagi values
written `tau_j`, `tau_min`) is followed in `check_fact72_takagi.py`.

## What each checker tests

| checker | seed claim | headline property checked |
|---|---|---|
| `check_task1_conic.py` | Facts 2.1, 2.3, 7.1; Sect. 9 item 4 | conic: three independent ranks agree, `dim ker H_N = 2N+1`, `Delta_N = N+1`, `\|\|f\|\|^2_Fock = 3`, and the notes' hand computations symbolically |
| `check_task2_hilbert.py` | Fact 2.1 | `dim ker H_N = HF_{R/I}(N)` for 8 ideals at every N, versus an independent exact Macaulay rank (GF(p) and sympy) |
| `check_task2b_subspace.py` | Fact 2.1 (subspace form) | `span{z^b f_j}` is exactly orthogonal to `ker H_N`, and `rank I_N + dim ker = dim R_N` |
| `check_task3_gaps.py` | Sect. 7 survey table | kernel dim = HF at every N of the survey; `Delta_N` bounded below per family; the seven published power laws for `Delta_N` and `\|\|H_N\|\|/Delta_N` |
| `check_task3b_hard.py` | Sect. 3 multigraded; Sect. 7 / Conj. 8.3(d) | sector identity `a^dag(f)a(f)\|_{(1..1)} = \|f><f\|(x)1` exactly; singlet chain kernel `m+1`, `m^2 Delta -> pi^2` from below, `Delta ~ 9.13 m^-1.97` |
| `check_task3c_exact.py` | Fact 7.1; Sect. 7 monomial bullet | conic `Delta_N = N+1` for `N <= 30`; monomial `H_N` exactly diagonal with the closed-form integer entries, `Delta_N = 1`, `\|\|H_N\|\| = N(N-1)(N-2)` |
| `check_task3d_nscale.py` | Sect. 7 n-scaling; Conj. 8.3(c) | boolean `Delta_{n+1} = 2` exactly for `n = 2..6`; random quadrics flat in `n` (`\|d log Delta/dn\| <= 0.1`) |
| `check_task3e_ffstats.py` | Sect. 7 last paragraph | random frustration-free chains: kernel `m+1`, median `Delta ~ m^-3.5`, power law beats exponential |
| `check_task4_toric.py` | Sect. 7 toric bullet; Conj. 8.3(b) | `H_N` exactly block diagonal over the A-graded fibres; fibre sums span the kernel; `Delta_N = min_u lambda_2(H_u)`; twisted cubic `Delta_N/N -> 0.854` |
| `check_task5_groebner.py` | Sect. 5.5; Conj. 8.4(a) | `in_w(I) = (z0z2, z0z3, z1z3)` with `HF = 3N+1`; kernel constant `3N+1` along the whole path; `Delta_N(t)` monotone; `min_t Delta_N = Delta_N(0) = 1`; `min_t Delta/\|\|H\|\| ~ 2.5 N^-1.75` |
| `check_task6_2sat.py` | Sect. 3; Prop. 3.1 | 23 instances: sector identity exact, kernel dim = multigraded HF, singlet/generic inverse systems of dimension 4 / 6 / 2 / 4 |
| `check_task7_coherent.py` | Sect. 3 consequences; Sect. 9 item 3 | coherent-state energy `sum_j N!/(N-m_j)! \|f_j(conj p)\|^2` to relative 1e-12; in the kernel iff `conj(p) in V`; the UNconjugated formula demonstrably fails |
| `check_task8_cnf.py` | Sect. 6; Conj. 8.6(i),(ii) | boolean `HF = 2^n` from `N = n`; `HF_{R/K}(N) = #SAT` for `N >= n+3`; `Delta_{n+3}` in band; SAT coherent states in the kernel; both Gram fits; overlap gain 1-12 |
| `check_task9_pyramid.py` | Sect. 7; Conj. 8.3(b) | pyramid and twisted-cubic-plus-dummy have `Delta_N = 2` exactly; the same ideals without the unused variable have `Delta_N = N` and `~0.85N`; the pyramid minimiser sits in `y^{N-2}`(x-quadrics) |
| `check_fact71_bombieri.py` | Fact 7.1 (**new**) | `Delta_N >= \|\|f\|\|^2_Fock` for principal ideals of degree 1-4 in 1-5 variables; equality exactly where the seed says; one variable `Delta_N = N!/(N-m)!` |
| `check_fact72_takagi.py` | Fact 7.2 (**new**) | Takagi two-sided bound `4 tau_min^2 (N-2) + \|\|f\|\|^2 <= Delta_N <= tau_min^2 N(N-1) + \|\|f\|\|^2 - 2 tau_min^2` for 8 quadrics; cones pinch to equality; `tau_min` explains the flat P^4 survey row |

The last two are new: no seed script tested Fact 7.1 or Fact 7.2 directly.
`check_fact72_takagi.py` is the check `HANDOFF.md` lists as suggested next step
1 ("compute Takagi values, compare slope of `Delta_N` with `4 d_min^2`").

## Exploration scripts (excluded from `run_all.sh`)

- `explore/explore_dynrange.py` — part (C) of the seed's `task3b_hard.py`
  (coefficient dynamic range `eps` in a single bilinear generator). **The seed
  report states no claim that these numbers support.** The nearest statement,
  Sect. 7's "`(f_1, f_1 + eps f_2)` ... has `Delta_N = O(eps^2)`", is about a
  two-generator tuple with a near-redundancy; this script perturbs a *single*
  generator and the ideal itself changes with `eps`. The observed behaviour is
  the opposite of a collapse: `Delta` is *smallest* at `eps = 1` (0.0833 at
  `m = 6`) and saturates at the `eps -> 0` value (0.1340) already by
  `eps = 1e-2`. There is no property here whose violation would refute anything
  in the report, so wrapping it in an exit code would be theatre. It is kept as
  an exploration script and excluded from `run_all.sh`.

Everything else in the seed's `numerics/` supports at least one checkable
property and has been promoted to a checker.

## `run_all.sh` summary (2026-09-02, this machine)

```
CHECKER                        STATUS   WALL(s)  LAST LINE
--------------------------------------------------------------------------------
check_task1_conic.py             PASS         0  PASS: 52 checks in 0.0s wall
check_task2_hilbert.py           PASS         8  PASS: 158 checks in 7.3s wall
check_task2b_subspace.py         PASS         0  PASS: 112 checks in 0.1s wall
check_task3_gaps.py              PASS        46  PASS: 710 checks in 45.6s wall
check_task3b_hard.py             PASS         3  PASS: 65 checks in 3.2s wall
check_task3c_exact.py            PASS         1  PASS: 107 checks in 0.3s wall
check_task3d_nscale.py           PASS        18  PASS: 123 checks in 18.1s wall
check_task3e_ffstats.py          PASS        22  PASS: 21 checks in 21.9s wall
check_task4_toric.py             PASS         1  PASS: 125 checks in 0.8s wall
check_task5_groebner.py          PASS         0  PASS: 459 checks in 0.6s wall
check_task6_2sat.py              PASS         0  PASS: 53 checks in 0.0s wall
check_task7_coherent.py          PASS         1  PASS: 108 checks in 0.0s wall
check_task8_cnf.py               PASS        99  PASS: 789 checks in 99.2s wall
check_task9_pyramid.py           PASS         2  PASS: 169 checks in 2.3s wall
check_fact71_bombieri.py         PASS         1  PASS: 336 checks in 0.2s wall
check_fact72_takagi.py           PASS         2  PASS: 330 checks in 1.9s wall
--------------------------------------------------------------------------------
16 checkers run, 0 failed, 204 s total wall
per-checker output in logs/
```

3717 individual checks, 204 s wall (an earlier identical run took 259 s;
timings vary by ~25% on this machine, verdicts and every printed number do
not). Mutation run: `17 mutations run, 0 did NOT turn the checker red`, 141 s.

## Reproduction of the seed `*_out.txt` numbers

Reproduced **exactly** (identical digits to the seed's committed output):

| quantity | seed file | value |
|---|---|---|
| conic `Delta_N`, `N <= 30` | `task3c_out.txt` | `N+1` exactly; `\|\|H_30\|\| = 878.178727` |
| conic ranks and `dim ker H_N` | `task1_out.txt` | `2N+1`, all three ranks agreeing |
| twisted cubic fit | `task3_out.txt` | `Delta_N ~ 0.8004 N^(+1.026)`, `\|\|H\|\|/Delta ~ 1.077 N^(+1.013)` |
| monomial ideal fit | `task3_out.txt` | `Delta_N ~ 1 N^(+0.000)`, `\|\|H\|\|/Delta ~ 0.6188 N^(+3.110)` |
| rational normal quartic fit | `task3_out.txt` | `0.61 N^(+1.054)` / `1.518 N^(+0.971)` |
| two generic quadrics fit | `task3_out.txt` | `0.1145 N^(+0.663)` / `3.254 N^(+1.390)` |
| boolean P^2..P^5 fits | `task3_out.txt` | `0.5228 N^0.701`, `0.9052 N^0.398`, `1.426 N^0.173`, `1.832 N^0.047` |
| single random quadric P^2/P^3/P^4 | `task3_out.txt` | `0.8012 N^1.043` / `1.153 N^0.563` / `1.668 N^0.020` |
| boolean `Delta_{n+1}` and random-quadric `n`-sweeps | `task3d_out.txt` | every row identical |
| FF-chain medians and fits | `task3e_out.txt` | `12.45 m^(-3.549)`, `\|corr\|` 0.9652 / 0.9830 |
| toric fibre tables | `task4_out.txt` | every row identical |
| Groebner path | `task5_out.txt` | `min_t Delta/\|\|H\|\| ~ 2.539 N^(-1.754)`, `Delta_N(0) = 1` |
| 2-SAT sector | `task6_out.txt` | every kernel dimension and residual identical |
| coherent-state energies | `task7_out.txt` | every energy identical |
| pyramid / no-y / TC+dummy | `task9_out.txt` | `Delta_N` = 2 / N / 2 exactly, every row identical |
| task 8 gap extrema, boolean gaps, Gram `lam_min`, overlaps | `task8_out.txt` | every value for `n = 3..6` identical |

## Discrepancies with seed

1. **`||H_N|| = N(N-1)(N-2)` is stated without a degree range.** `report.md`
   Sect. 7, monomial bullet, says "`||H_N|| = N(N-1)(N-2)` exactly for
   `(z0^2, z0z1, z1^3)`". At `N = 2` the true value is `2` and the formula
   gives `0`; the identity holds for `N >= 3 = max_j m_j`. Files:
   `seed/.../report.md` Sect. 7; the value is visible in
   `seed/.../numerics/task3_out.txt`, block "(b) monomial", row `N=2`
   (`||H_N|| = 2`). `check_task3_gaps.py` and `check_task3c_exact.py` test the
   identity for `N >= 3` and say so.
2. **"random quadric ideals at `N = 3, 4` have `Delta ~ 0.7-1.2`" is too
   narrow.** `report.md` Sect. 7, closing paragraph. The seed's own
   `task3d_out.txt` shows `Delta = 3.69529` (`k=1, N=3, n=2`),
   `Delta = 4.61955` (`k=1, N=4, n=2`) and `Delta = 1.79538` (`k=1, N=3,
   n=8`); the full observed span over the sweep is `[0.6298, 4.6196]`, not
   `[0.7, 1.2]`. The *defensible* content, flatness in `n`, does hold: the
   fitted exponential rates are `-0.0565, -0.0671, +0.0271, +0.0171` per
   variable. `check_task3d_nscale.py` tests `Delta in [0.5, 5.0]` plus
   `|d log Delta / dn| <= 0.1` and records this discrepancy in its docstring.
3. **A seed script mislabels a point as being off the twisted cubic.**
   `seed/.../numerics/task7_coherent.py` line 57 lists `(1,1,1,1)` in the
   `off` list, but `(1,1,1,1) = tcp(1,1)` is *on* the curve (all three 2x2
   minors vanish). `task7_out.txt` duly prints `OFF V(I) p = [1,1,1,1] ...
   E = 1.066605397e-17`, i.e. a zero energy under an "off" label. The report's
   claim is unaffected (the energy formula is what is tested), but the script's
   off-variety evidence is one point weaker than it appears.
   `check_task7_coherent.py` uses `(1,1,1,2)` instead (`z0z3 - z1z2 = 1`).
4. **"checked to machine precision for 3 to 12 sites" is not supported by the
   shipped scripts.** `report.md` Sect. 3, multigraded paragraph. The only
   scripts that compare the polynomial-ring `H` against the direct qubit
   construction are `task3b_hard.py` (`m = 3, 4, 5`) and `task6_2sat.py`
   (`m = 3`). Nothing in `seed/.../numerics/` reaches 6 sites, and the full
   degree-`m` space at `m = 6` already has dimension 12376. The identity is
   elementary and almost certainly true at all `m`; the *numerical* support is
   `m <= 5`. `check_task3b_hard.py` checks `m = 3, 4, 5` and says so.
5. **The seed's own `run_all.sh` does not run three of its scripts.**
   `seed/.../numerics/run_all.sh` runs task1, 2, 2b, 3, 3b, 3c, 3d, 4, 5, 6, 7
   but not `task3e_ffstats.py`, `task8_cnf.py` or `task9_pyramid.py`, although
   `task3e_out.txt`, `task8_out.txt` and `task9_out.txt` exist and the report
   cites their numbers (Sect. 7 FF-chain medians, Sect. 6 and Conj. 8.6,
   Conj. 8.3(b)). This suite runs all of them.
6. **Caps reduced relative to the seed** (stated so the reproduced numbers are
   not over-read):
   - `check_task3b_hard.py`: singlet chain to `m = 11`, seed went to `m = 12`.
     Consequence: the fit is `9.093 m^(-1.968)` here versus `9.134 m^(-1.970)`
     in `task3b_out.txt`. Both agree with the published `9.13 m^-1.97`.
   - `check_task8_cnf.py`: `n = 3..6` (36 instances) and `N = n+3` only; the
     seed ran `n = 3..8` (54 instances) and also `N = n+4`, taking 7644 s. The
     observed gap band over the reduced set is `[0.36602, 2.26393]`, inside the
     report's `[0.29, 2.3]`, but Conjecture 8.6(i)'s statement "over 54
     instances with `n = 3..8`" is **not** fully re-run here; in particular the
     `n = 7, 8` values `0.45023` and `0.29390` are taken on trust from
     `task8_out.txt`. Dense `eigh` is used up to dimension 1400 and the seed's
     deflated LOBPCG above it, with the two cross-checked against each other at
     `n = 4, 5`.
   - `check_fact72_takagi.py`: the survey's P^4 random quadric is followed to
     `N = 12`, not `N = 14`.
7. **No numerical discrepancy was found anywhere else.** Every other number the
   report attributes to `numerics/` reproduced to the digits printed in the
   seed's `*_out.txt`. In particular Fact 7.2, which no seed script tested, is
   confirmed for all eight quadrics: both bounds hold at every `N`, the cones
   (`z0^2`, the pyramid) pinch to exact equality `Delta_N = ||f||^2_Fock`, and
   the identity `||f||^2_Fock = 2 sum_j tau_j^2` holds to 1e-15.

## Lane report

1. 16 checkers, 3717 checks, `run_all.sh` PASS in 204 s wall (budget 40 min); every run under `timeout`, caps declared in every file.
2. 17 recorded mutations, all red (exit 1), 141 s; `run_mutations.py` edits only temp-dir copies and refuses ambiguous patterns.
3. No bare `assert` (two docstring mentions only); `python3 -O` parity spot-checked; exit 2 reserved for "could not run".
4. Two NEW checkers: `check_fact71_bombieri.py` (Fact 7.1, degrees 1-4, 1-5 variables) and `check_fact72_takagi.py` (Fact 7.2 = HANDOFF next step 1).
5. Fact 7.2 holds on all eight quadrics tested; cones pinch to equality `Delta_N = ||f||^2_Fock`; `tau_min = 0.0165` quantitatively explains the flat P^4 survey row.
6. Four discrepancies with the seed, all minor, all recorded above: `||H_N|| = N(N-1)(N-2)` needs `N >= 3` (at `N = 2` it is 2, not 0); "Delta ~ 0.7-1.2" is too narrow (true span 0.63-4.62); `task7_coherent.py` labels the on-curve point `(1,1,1,1)` as off-curve; "checked for 3 to 12 sites" is supported only for `m <= 5`.
7. None of the four touches a Section 2-7 theorem; every other seed number reproduced to the printed digits.
8. One script demoted to exploration (`explore/explore_dynrange.py`, excluded from `run_all.sh`): the report states no claim its numbers support.
9. Conventions: whole suite departs from C5 (generators as written, not unit Bombieri-Weyl), matching the seed; C9 (`tau`) followed; stated in every docstring.
10. Not re-run under budget: task 8 at `n = 7, 8` (7644 s in the seed), so Conj. 8.6(i)'s 54-instance gap band is verified on 36 instances (`n = 3..6`, observed `[0.366, 2.264]`).
11. Nothing here promotes a claim: a PASS says only that the stated numerical property holds on the tested range at the stated tolerance.
