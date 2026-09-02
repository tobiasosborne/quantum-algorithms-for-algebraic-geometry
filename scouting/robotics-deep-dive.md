# Robotics deep dive: where varieties and ideals actually bite, and whether the seed construction can beat classical practice

Lane: robotics (brief `briefs/lane-robotics.md`). Date 2026-09-02. Author: Opus subagent.
Read: `CLAUDE.md`, `seed/analysis-2026-09-01/report.md` (treated as an untrusted proposer
document), `seed/.../referee/round1.md`, `round2.md`, `HANDOFF.md`, `seed/page81.tex`.
Citations are arXiv ids or DOIs that were resolved during this pass; anything not resolved is
marked `[UNVERIFIED]`.

---

## 0. Bottom line, stated before the evidence

Robotics is full of polynomial ideals, and almost none of them are the *kind* of ideal the seed
construction is good at. Three facts decide the lane:

1. **Robotics kinematics is zero-dimensional.** Inverse kinematics, forward kinematics of parallel
   platforms, minimal problems in vision, calibration, rigidity realisations, synthesis - every one
   is a system with finitely many solutions, i.e. codimension *n*, the maximal value. The seed's two
   readable observables (normalised Hilbert function, normalised traces) are informative only when
   `codim V = O(1)` (seed §5 task 2, Conj. 8.7). At `codim = n` the signal `HF(N)/dim R_N =
   D/binom(N+n,n)` is exponentially small and additive estimation is hopeless. This kills the direct
   route for the entire classical kinematics canon.
2. **Robotics is real algebraic geometry.** A 6R arm has 16 complex IK solutions and typically 0, 2,
   4, ... real ones; a nine-point synthesis problem has 8652 complex roots and a handful of usable
   real, defect-free linkages. The seed encodes the complex variety. `H_N` does commute with the
   antiunitary conjugation `K` when the generators have real coefficients, and the real points of `V`
   are exactly the `K`-invariant coherent states - but a real form of a complex Hilbert space is not
   the range of a projector, so there is no quantum operation that selects them. The one classical
   bridge (Hermite's quadratic form: `#real roots = signature` of the matrix of traces of
   multiplication operators) needs the *signature* of a `D x D` matrix, i.e. integer resolution out
   of a trace, which is exactly what additive quantum trace estimation cannot deliver.
3. **The sizes are small and the classical solvers are already at the hardware floor.** IKFast emits
   closed-form 6R solvers running in about 5 microseconds; P3P runs in well under a microsecond;
   the general Stewart-Gough platform is a 69x69 generalised eigenproblem. A quantum coprocessor
   cannot enter a 1 kHz control loop, let alone a RANSAC inner loop called 10^4 times per frame.

What survives is narrow and specific: (i) the *offline* end of kinematic synthesis, where root counts
are 10^5 to 10^7 and classical cost is CPU-weeks; (ii) certifiable perception, where the classical
wall is the *size of the moment matrix* and is therefore a genuine space wall; (iii) positive-dimensional
closure/self-motion varieties of many-joint mechanisms, the only robotics family with fixed low
codimension, which is the seed's one good regime. These are the three bets in §16. None of them is
a clean exponential; the honest colour is "one plausible space separation and one plausible quadratic
time separation, both contingent on a Macaulay gap nobody has measured".

The one structural contribution this lane can make regardless of speedup: **the multigraded
dictionary of §1.3**, which turns mechanism kinematics into a bosonic/qudit frustration-free
Hamiltonian with one site per joint. That is the only place in robotics where the seed's Hamiltonian
becomes genuinely local, and it is what makes the heuristic-hardware requirement of the north star
even discussable.

---

## 1. Three structural facts, worked out once

### 1.1 Zero-dimensionality kills the Hilbert-function readout

Let `I` be zero-dimensional in `C[z_0..z_n]` with scheme length `D`, and `N >= reg(I)`. Then
`HF(N) = D`, `dim R_N = binom(N+n,n)`, and the seed's DQC1-style observable is `D/binom(N+n,n)`.
Estimating it to the additive precision needed to read `D` costs `1/eps^2` repetitions with
`eps ~ 1/(2 binom(N+n,n))`. Numbers:

| problem | n | D | N used | `dim R_N` | ratio | reps needed | classical |
|---|---|---|---|---|---|---|---|
| general 6R IK | 8 | 16 | 12 | 1.26e5 | 1.3e-4 | ~6e7 | 16x16 eig, 5 us |
| Stewart-Gough FK | 7 | 40 | 10 | 1.9e4 | 2.1e-3 | ~2e5 | 69x69 eig, sub-ms |
| Watt II 8-point synthesis | 22 | 92736 | ~25 | 1.5e13 | 6e-9 | ~3e16 | 9.3e4 path tracks |

The last column is the fair classical baseline and it is not close. This is not a defect of the
estimator; it is the seed's own §6 hardness anchor (exact Hilbert function is #P-hard; a
multiplicative estimate gives `NP ⊆ BQP`). Counting solutions of a polynomial system over `C` is
#P-hard in general, so no efficient exact route should be expected. **Every "count the IK solutions
/ count the assembly modes / count the realisations" idea dies here.** Approximate counting to
*relative* error `eps` is the only survivor and costs `sqrt(dim/D)/eps` by quantum counting; exact
counting costs `sqrt(dim * D)`, which is worse than the classical `D`.

### 1.2 The real/complex gap

Every robotics deliverable is a real object: a real joint vector, a real linkage with real link
lengths, a real pose. The classical pipelines are built around this - `msolve` and real root
isolation, Descartes/Sturm, Hermite forms, certified real solutions via alphaCertified. The seed has
no real-algebraic content. Two partial bridges exist and both fail:

- *Antiunitary symmetry.* With real generator coefficients, `[H_N, K] = 0` for `K` complex
  conjugation in the monomial basis; the real points of `V` are the `K`-fixed coherent states. But
  `Fix(K)` is a real form, not a complex subspace, so `P_{real}` does not exist. One can measure
  `<psi|K psi>`-type quantities only via a SWAP-like test on two copies, which gives an overlap, not
  a selection.
- *Hermite's method.* For zero-dimensional `I` with real coefficients, the number of distinct real
  roots is the signature of the bilinear form `h(p,q) = Tr(m_{pq})` on `R/I`, and the seed gives
  exactly quantum access to `Tr(P_0 T_g)` (§5.7, Conj. 8.10(c)). But the signature requires resolving
  `D_+ - D_-` to `+-1` out of `D`, i.e. relative precision `1/D`. Dead by the same argument as §1.1.

### 1.3 The multigraded dictionary: one site per joint (the good news)

This is the one genuinely clean structural fit and it is worth recording independently of any
speedup claim. Take a mechanism with `j` revolute joints. In tangent-half-angle coordinates
`t_i = tan(theta_i/2)`, or equivalently in the homogeneous pairs `(c_i : s_i : w_i)` with the
conic constraint `c_i^2 + s_i^2 = w_i^2`, every loop-closure equation is **multi-affine of degree
at most 2 in each joint block**. Group the variables into `j` blocks of size 3 (or size 4 using unit
quaternions / Study coordinates per joint). Then:

- The configuration variety lives in `(P^2)^j` (or `(P^3)^j`), a multiprojective space.
- In the seed's Segre/multigraded setting (report §3), the multidegree-`(1,...,1)` sector of
  `C[z_{i,s}]` is exactly `(C^q)^{\otimes j}` with orthonormal monomials, and a multilinear form `f`
  on a subset `S` of sites gives `a^dagger(f) a(f) = |f><f|_S ⊗ 1` **exactly, with no factorials**.
- Hence: *a mechanism whose loop-closure equations are multilinear across joint blocks is literally
  a quantum k-SAT instance on j qudits of dimension 3 or 4, with one rank-one projector per scalar
  loop-closure equation, and its product-state zero-energy solutions are precisely the mechanism's
  configurations.* For degree-2-per-block equations one passes to the multidegree `(2,...,2)` sector,
  where the same identification holds up to fixed `2!` factors per block.

Consequences that matter:

- The Hamiltonian is `k`-local on qutrits with `k` = the number of joints appearing in one equation
  (for a single serial loop, all `j`; for a chain written with intermediate frames as auxiliary
  sites, `k = 2` or `3`). Writing the chain with per-link auxiliary pose sites gives a **2-local
  frustration-free chain Hamiltonian on `O(j)` sites** whose zero-energy space is the closure
  variety. That is the object the heuristic-hardware clause of the north star wants.
- It also imports every pathology: the seed's Prop. 8.3(d) says multigraded sectors realise
  Levine-Movassagh area-weighted Motzkin chains and therefore gaps as small as `t^{-n^2/3}`
  (arXiv:1611.03147). A 2-local frustration-free chain built from mechanism constraints is not
  obviously benign, and the seed's own numerics put random frustration-free 2-local chains at
  `Delta ~ m^{-3.5}`.
- The sector dimension is `prod_i binom(d_i + q_i - 1, q_i - 1)`, e.g. `6^j` for multidegree
  `(2,...,2)` with `q=3`, versus `binom(N+n,n)` for the total-degree grading. For the Watt II problem
  (22 variables) that is `6^11 = 3.6e8` versus `1.5e13` - five orders of magnitude smaller. Every
  overlap argument in this memo should be run in the multigraded sector, not the total-degree one.
  This is the single most useful technical point in the lane.

---

## 2. Inverse kinematics of serial manipulators (general 6R)

Given DH parameters and a target pose, solve `A_1(t_1)...A_6(t_6) = T`. Raghavan-Roth reduce this by
dialytic elimination to 14 equations in 8 unknowns and then to a 12x12 matrix polynomial of degree 16
in `tan(theta_3/2)`; the generic root count is 16 and the bound is tight (Lee-Liang 1988;
Primrose 1986) `[UNVERIFIED DOIs]`. Best classical: Manocha-Canny's generalised eigenproblem, 24x24
reducible to 16x16 (DOI 10.1109/70.326569). In practice nobody solves the general 6R: industrial arms
have spherical wrists, and IKFast compiles a closed-form solver per robot running in about **5
microseconds**; numerical solvers (TRAC-IK, LM) take tens of microseconds to milliseconds. Modern
reformulations: distance-geometric IK as low-rank EDM completion with Riemannian optimisation
(arXiv:2108.13720, IEEE T-RO 38(3):1703-1722, 2022), SOS IK for serial chains `[UNVERIFIED DOI]`,
IK as a QP (arXiv:2312.15569).

*Where practice hurts:* it does not. IK is solved at 1 kHz. The residual difficulty is choosing among
16 branches under obstacles and joint limits, a discrete continuation problem, not an algebraic one.
*Seed fit:* zero-dimensional, `n = 8`, `D = 16`; a 16-dimensional ground space inside a
125970-dimensional `R_12`. The multigraded fit of §1.3 is clean but the instance is trivially small.
*Quantum angle:* none, in either time or space (the classical solver is a few kilobytes of generated
C). Prior quantum work (quantum annealing IK, Sci. Rep. 2025 `[UNVERIFIED DOI]`; QML plus Grover,
arXiv:2509.07216) benchmarks against numerical IK, not IKFast, and is not a north-star speedup.
**Score 1/5.**

## 3. Forward kinematics of parallel manipulators (Stewart-Gough)

Given six leg lengths, find the platform pose: in Study coordinates, six quadrics in `P^7` cut with
the Study quadric, generic root count **40** (Husty 1996, MMT 31(4):365-380 `[UNVERIFIED DOI]`; count
first observed numerically by Raghavan; Dietmaier 1998 exhibited a platform with 40 *real* postures
`[UNVERIFIED DOI]`). Best classical: Martyushev's sparse elimination template of size 293x362,
PLU-reduced to a **69x69 generalised eigenproblem** returning all 40 solutions
(arXiv:2505.00634, MMT 215:106170, 2025; MATLAB/Julia/Python released). Real machines never solve it:
redundant sensing plus Newton from the previous pose gives the branch in microseconds.

*Where practice hurts:* only in design certification - singularity-free workspace (§5) and the
classification of *architecturally singular* platforms with self-motions (Borel-Bricard; Husty,
Karger, Nawratil), genuinely heavy Groebner computations with cases still open `[UNVERIFIED]`.
*Seed fit:* zero-dimensional, `n = 7`, `D = 40`. The Study quadric is the seed's best-understood case
(Fact 7.2 gives `Delta_N >= 4 d_min^2 (N-2) + ||f||^2`), but the payoff is a 69x69 eigenproblem.
**Score 1/5 for FK; 2/5 for the self-motion classification** (see §5 and Bet R3).

## 4. Kinematic synthesis (Burmester, four-bar, Alt-Burmester, six-bar)

**Formulation.** Given a task (poses, path points, function values), solve for link dimensions. The
classical instances:

- Burmester five-pose four-bar motion generation: small, closed form.
- Alt's nine-point path synthesis for four-bars: 8 equations in 8 complex unknowns in isotropic
  coordinates; **8652 nondegenerate roots**, which by a two-fold symmetry and Roberts cognates give
  **1442 distinct four-bar linkages** (Wampler-Morgan-Sommese, ASME JMD 114(1):153-159, 1992; the
  1992 run was a landmark supercomputer homotopy). The whole Alt-Burmester family (mixtures of poses
  and path points) has been tabulated for dimension and degree by numerical algebraic geometry
  (Brake, Hauenstein, Murray, Myszka, Wampler, J. Mech. Rob. 8(4):041018, 2016,
  DOI 10.1115/1.4033251).
- Six-bar synthesis (Plecnik-McCarthy). Stephenson II and III eleven-position function generators:
  multihomogeneous degrees **264,241,152** and **55,050,240**, with numerically estimated root counts
  **1,521,037** and **834,441**. Watt II eight-accuracy-point: **22 equations in 22 unknowns**,
  multihomogeneous degree **705,432**, **92,736 nonsingular solutions** found with Bertini
  `[counts from Plecnik-McCarthy, UNVERIFIED DOIs; see also the parallelised solver in
  Springer ARK 2018, DOI 10.1007/978-3-319-93188-3_16 UNVERIFIED]`.

**Sizes and where practice hurts.** This is the only robotics problem family at a size where
asymptotics matter. Three costs: (a) the *ab initio* solve of a new synthesis formulation, done once,
historically days to weeks on clusters, now largely replaced by monodromy plus a trace test
(Duff-Hill-Jensen-Lee-Leykin-Sommars, arXiv:1609.08722, IMA J. Numer. Anal. 39(3):1421-1446, 2019),
whose expected path count is linear in the number of solutions; (b) the *parameter homotopy* per new
design query, `D` path tracks with `D = 10^5..10^6`, minutes to hours, embarrassingly parallel, GPU
implementations exist (GPU-HC, arXiv:2112.03444, reports up to 26x over CPU HC); (c) *filtering*:
of the `D` roots, only the real, branch-defect-free, circuit-defect-free, order-correct ones are
usable, typically a handful - so 10^6 expensive tracks yield ~10 designs.

**Best classical, precisely.** Ab initio: monodromy, expected `O(D)` paths. Per query: parameter
homotopy, exactly `D` paths, each a predictor-corrector track costing `O(n^3)` per step and `10^2`
to `10^4` steps. Total per design query `~ D * n^3 * steps` flops, i.e. `10^12` to `10^14` flops for
a six-bar problem. This is the number a quantum claim has to beat.

**Seed fit.** Zero-dimensional (bad for the Hilbert-function readout), but *large* `D` and, crucially,
a rich multihomogeneous structure. The ground space of `H_N` in the appropriate multidegree sector is
spanned by the coherent states of the roots (report §3, and this is a theorem, not a conjecture, when
`I_N = I(V)_N`). Overlap of the maximally mixed sector state on the ground space is `D/dim(sector)`.
With the multigraded sector dimension `6^11 = 3.6e8` for Watt II and `D = 92736`, amplitude
amplification costs `sqrt(3.6e8/9.3e4) = 62` ground-space projections. That is the arithmetic behind
Bet R2.

**Honest caveats that could kill it.** (i) The synthesis ideals are notoriously *non-radical and
non-saturated*: the formulations carry large degenerate components (coincident points, links of zero
length, solutions at infinity) which inflate `dim ker H_N` far above the useful `D`. The seed's
Conj. 8.5 "entangled defect" is exactly this and it is not a small correction here. (ii) `alpha/Delta_N`
for a 22-variable synthesis ideal is completely unknown. (iii) Reading a root out of the ground state
requires `O(1/eps^2)` copies of a coherent state to estimate the point coordinates.

**Score 3/5** - the highest in the lane, and the only one where the classical baseline is measured in
CPU-days rather than microseconds.

## 5. Singularity loci, workspace boundaries, self-motions

The singularity locus of a parallel manipulator is `{det J = 0}`; for a Gough-Stewart platform at
fixed orientation it is a **cubic surface** in translation space `[UNVERIFIED DOI]`. Workspace
boundaries are semialgebraic (discriminant, joint limits, self-collision). Singularity *distance* has
exact algebraic treatments for special architectures (arXiv:1701.09107, arXiv:1712.06952). Practice
hurts only in offline design certification: certified singularity-free volumes, trajectory-wide
guarantees, architectural-singularity classification.

Two seed observables map here and both are dominated. The Berezin symbol
`<p^{⊗N}|P_0|p^{⊗N}>` is a smoothed indicator of `V` at Fubini-Study resolution `N^{-1/2}`, i.e.
"how close is this configuration to the singularity variety" - classical competitor: evaluate
`det J(p)`, microseconds. `Tr(P_I P_J)`, whose growth exponent is `dim(V ∩ W)` (Conj. 8.10(a)), would
answer "does this path meet the singularity variety" - classical competitor: substitute the path into
`det J` and isolate real roots of a univariate, microseconds. The one non-trivial item is the
self-motion test `dim V > 0`, and additive estimation cannot separate `HF = const` from
`HF = Theta(N)` when both are negligible against `binom(N+n,n)`. The only route avoiding relative
precision is a slicing test: intersect with a generic linear space of codimension `k` and detect
non-emptiness through polynomial-versus-`cos^{2N}` behaviour of `Tr(P_I P_L)`, at cost `N^{k/2}` by
amplitude estimation, cheap for the small `k` (1 or 2) of interest. **Score 2/5.**

## 6. Configuration-space topology and motion planning

The generalised movers' problem: decide connectivity of the free space for a robot with `k` DOF among
semialgebraic obstacles. Schwartz-Sharir cell decomposition is doubly exponential in `k` (via CAD,
Collins); Canny's roadmap is singly exponential and PSPACE (Canny, *The Complexity of Robot Motion
Planning*, MIT Press 1988); Reif proved PSPACE-hardness; the current roadmap complexity is
`d^{O(k sqrt k)}` (arXiv:1201.6439); task-and-motion planning is also PSPACE-complete `[UNVERIFIED]`.
**Nobody uses any of these**: practice is sampling-based (PRM, RRT, RRT*, arXiv:1105.1186) with
millisecond budgets and probabilistic completeness only.

There is a clean impossibility here. For the decision problem no space speedup exists, because
`BQPSPACE = PSPACE` (Watrous `[UNVERIFIED DOI]`), so a quantum machine cannot use asymptotically less
space than the classical PSPACE algorithm already does; and no quantum speedup for PSPACE-complete
problems is known or expected. For the practical problem the classical method is a randomised
heuristic running in milliseconds. Grover over a discretised configuration grid gives `sqrt(|grid|)`
but the grid is exponential in `k` and RRT never enumerates it. **Score 1/5.** This is the largest
theory-practice gap in robotics and quantum computing has nothing to say about it.

## 7. Calibration (hand-eye `AX = XB`, kinematic calibration)

`AX = XB` in SE(3) with `n` motion pairs; the dual-quaternion form reduces it to a small structured
SVD (Daniilidis, IJRR 1999, DOI 10.1177/02783649922066213). Global-optimality treatments: hand-eye and
robot-world by global polynomial optimisation (arXiv:1402.3261); optimal least squares by a 1-D convex
line search (arXiv:2002.10838). Kinematic calibration is polynomial least squares in 20-100
DH/compliance parameters solved by Levenberg-Marquardt. Practice hurts in data (parameter
observability, noise, thermal drift), not in the algebra. Because the data are noisy the ideal is the
unit ideal and `ker H_N = 0`: the relevant object is the *ground energy* of `H_N`, which is the
polynomial-optimisation reading of §10 and Bet R1, not a variety reading. **Score 1/5** standalone;
folded into Bet R1 as an instance family.

## 8. Multi-robot formations, rigidity, bar-joint frameworks

A bar-joint framework is `V(I)` for `I` generated by `|E|` quadrics `|p_u - p_v|^2 - d_{uv}^2` in `dn`
variables; Laman's theorem characterises generic 2-D rigidity combinatorially; the *number of
realisations* is the degree of a zero-dimensional variety after fixing an edge. Best classical for 2-D
is a recursion via algebraic and tropical geometry that computes the Laman number **without solving
the system** (Capco-Gallet-Grasegger-Koutschan-Lubbes-Schicho, arXiv:1701.05500; summary
arXiv:1707.03633; all Laman graphs to 12 vertices, Zenodo 1245517); for 3-D, bounds and constructions
via algebraic methods and homotopy (arXiv:1802.05860; JSC 102:189-208, 2021, arXiv:1811.12800; upper
bounds arXiv:2010.10578). Realisation counts grow exponentially in `n`.

Practice hurts in *research* (the maximum realisation number is open), not in deployment: deployed
multi-robot systems need generic rigidity, decided by the pebble game in `O(n^2)`, and global
rigidity, decided by a randomised polynomial-time rank test (Connelly; Gortler-Healy-Thurston)
`[UNVERIFIED DOIs]`. Zero-dimensional again: quantum counting of realisations costs `sqrt(dim/D)` for
relative error and `sqrt(dim*D)` for the exact integer, worse than a classical recursion that is not
even a solve. **Score 2/5**, and only for the pure-mathematics counting question - where the classical
baseline is exactly the kind of structural insight quantum linear algebra cannot match.

## 9. Grasp synthesis and force closure

Force closure is a system of polynomial *inequalities* (contact wrenches must positively span `R^6`
under friction cones); grasp synthesis is bilinear in contact point and force, hence a BMI, solved by
sequential SDP / SOS (Dai-Majumdar-Tedrake, DOI 10.1007/978-3-319-51532-8_18). Sizes: 3-10 contacts,
SDPs with a few hundred variables, milliseconds to seconds. This is real semialgebraic feasibility;
the seed's ground-space construction has no inequality content, and the only entry point is the
moment/SOS mechanism of Bet R1, at sizes where the classical SDP is trivial. **Score 1/5.**

## 10. SLAM, bundle adjustment, rotation averaging, certifiable perception

**Formulation.** Pose-graph SLAM: minimise `sum_{(i,j)} w_ij ||R_i R_ij - R_j||^2 + ...` over
`(R_i, t_i) in SE(3)^n`. This is polynomial optimisation over a real variety (`R^T R = I`,
`det R = 1`). Outlier-robust versions (truncated least squares) add binary variables `theta_i^2 = 1`
per measurement - which is *exactly* the seed's Boolean ideal `(z_i^2 - z_i z_0)` from report §6,
tensored with a rotation-group ideal.

**Best classical.** Three tiers:
- Local: Gauss-Newton / Levenberg on the manifold (g2o, GTSAM, Ceres). Near-linear per iteration on
  sparse graphs; `10^4`-`10^6` poses in seconds.
- Certifiably correct, low rank: SE-Sync (arXiv:1612.07386, IJRR 2019) and Shonan rotation averaging
  (arXiv:2008.02737, ECCV 2020) solve the *first-order* SDP relaxation by Burer-Monteiro Riemannian
  staircase, exploiting rank-`r` factorisation; cost is near-linear in the number of poses, with a
  global optimality certificate from the dual.
- Outlier-robust: Yang-Carlone (arXiv:2109.03349, IEEE TPAMI 2022) reformulate TLS/Geman-McClure as a
  polynomial optimisation problem, use a *sparse* second-order moment relaxation much smaller than
  the dense Lasserre level 2, and solve it with STRIDE (SDP + local search). Reported: up to 100x
  faster than existing SDP solvers, and the only solver reaching SDPs with hundreds of thousands of
  constraints; exact up to 60-90% outliers.

**Where practice hurts - and it is a SPACE wall.** The bottleneck is the *size of the moment matrix*.
For `n` scalar variables the dense Lasserre level-`kappa` moment matrix has size `binom(n+kappa,
kappa)`: for `n = 100`, level 2 gives 5151 (a 5151x5151 SDP block, ~200 MB, feasible) and level 3
gives 176851 (a 176851x176851 block, ~2.5e11 doubles, ~250 GB, infeasible). The entire sparse-SDP
literature in robotics exists to dodge this wall. When the level-2 relaxation is *not* tight - which
happens with high outlier rates, poor initialisation, or matrix-weighted measurements
(arXiv:2308.07275) - there is currently no practical recourse. That is a real, documented,
space-limited failure mode in a first-class robotics problem.

**Seed fit - this is the tightest fit in the lane.** The seed's `H_N = sum_j a^dagger(f_j) a(f_j)` on
`Sym^N(C^{n+1})` has coherent-state expectation
`<p^{⊗N}|H_N|p^{⊗N}> = sum_j (N!/(N-m_j)!) |f_j(pbar)|^2`,
i.e. exactly the weighted sum of squared residuals at the point `p`. Therefore
`lambda_min(H_N) <= min over product states` is a **relaxation of the robotics least-squares
objective**, and minimising over all of `Sym^N` rather than over coherent states is precisely the
Doherty-Parrilo-Spedalieri / sum-of-squares-on-the-sphere hierarchy at level `N`, whose convergence
rate to the true optimum is `O(d^2/N^2)` for degree-`d` forms in the regime `N >= Omega(d)`
(Fang-Fawzi, arXiv:1908.05155). In other words: **the seed Hamiltonian's ground energy *is* the
moment relaxation bound that certifiable robot perception already uses, and its ground state is the
moment matrix's leading eigenvector.** When the data are noiseless the ideal is proper and the ground
space is the inverse system; when the data are noisy the ideal is `(1)` and the ground energy is the
certificate. This is a clean, checkable identification and it was not in the seed report.

**Quantum angle.** Space: `Sym^N(C^{n+1})` needs `O(n log N)` qubits (occupation encoding) or
`log binom(N+n,n)` in a dense encoding - for `n = 100, N = 6` that is 31 to 300 qubits versus 250 GB
classically. Time: ground-energy estimation needs a guiding state with non-negligible overlap; robotics
supplies one for free (the Gauss-Newton local solution, lifted to a coherent state), which puts this
squarely in the guided-local-Hamiltonian setting, BQP-complete for inverse-polynomial precision even
at 2-locality (Gharibian-Le Gall, arXiv:2111.09079; improved hardness arXiv:2207.10250). That is a
genuine hardness anchor, not a speedup proof.
**Score 3/5.** See Bet R1.

## 11. Minimal problems in robot vision

Small zero-dimensional systems solved inside RANSAC: P3P (4 solutions), five-point relative pose (10
solutions; Nister, IEEE TPAMI 26(6):756-770, 2004, DOI 10.1109/TPAMI.2004.17), homography, PnP,
generalised relative pose, radial distortion variants; trifocal relative pose from points and lines
has 312 solutions (arXiv:1903.09755). Best classical: elimination templates generated automatically
*offline* (Kukelova-Bujnak-Pajdla 2008, DOI 10.1007/978-3-540-88690-7_23; syzygy-based and
basis-selection improvements, Larsson-Astrom-Oskarsson CVPR 2017/2018 `[UNVERIFIED DOIs]`; GAPS
arXiv:2004.11765; sparse-resultant solvers arXiv:2301.06443; FFT-based interpolation solvers
arXiv:2605.06572). Where templates blow up, homotopy continuation replaces them: MINUS
(arXiv:1903.09755), GPU-HC (arXiv:2112.03444, up to 26x over CPU), learned start pairs
(arXiv:2411.03745). Runtimes: sub-microsecond (P3P) to tens of microseconds (five-point) to
milliseconds (trifocal HC).

Practice hurts in template size and numerical stability for the harder problems, and in the fact that
RANSAC calls the solver `10^3`-`10^5` times per frame, so the per-call budget is microseconds - the
worst possible environment for a quantum coprocessor. Zero-dimensional, `n <= 20`, `D <= 312`. The
action-matrix method the whole field uses *is* Stickelberger on `R/I`, i.e. the seed's §5.4 object,
already reduced to a `D x D` eigenproblem with `D <= 312`; the seed's quantum version cannot use phase
estimation (non-normal compressed multiplication operators) and would need a singular-value scan whose
cost is set by eigenvector conditioning. **Score 1/5.** One thing worth recording: this community has
already industrialised "precompute the Macaulay structure offline, run cheap linear algebra online".
Any quantum proposal must beat that, not beat naive Groebner.

## 12. Contact, mode enumeration, legged locomotion

With `N` contacts and `d` effective DOF, contact modes (separating / sticking / sliding) partition
configuration-velocity space by sign conditions on polynomials; enumeration costs `O(N^d)` and yields
50-400 modes in practice (Huang-Cheng-Mason, DOI 10.1007/978-3-030-66723-8_29 `[UNVERIFIED]`).
Contact-implicit trajectory optimisation is a complementarity problem or a MIQP over modes, with
recent sparsity-rich SDP relaxations (arXiv:2502.02829). Practice hurts badly here - contact-rich
planning is a genuine open problem and the `3^N` mode combinatorics is why - but the structure is
semialgebraic sign conditions plus integer programming, not ideal membership. Grover over modes gives
`sqrt(3^N)` with `N ~ 10`, a factor of 200 on a millisecond problem. **Score 1/5** for the seed
construction; 2/5 for generic quantum optimisation, which is outside this campaign's north star.

## 13. Planning under polynomial dynamics, SOS control

Region-of-attraction and funnel computations: find `V(x)` with `V` and `-Vdot` SOS on a semialgebraic
set; state dimension 4-20, SOS degree 2-6, SDPs with `10^3`-`10^5` variables, solved by bilinear
alternation. Same situation as §10, except that these problems are *inequality*-dominated (positivity
on a set) rather than ideal-dominated, and Putinar certificates with multipliers have no obvious
frustration-free Fock realisation. One possible extension: the multipliers `sigma_i` in a
Positivstellensatz certificate correspond to sums of squares of annihilation operators
`sum_i a^dagger(g_i) a(g_i)` with the `g_i` *unknown*, which turns certificate search into a
Hamiltonian *learning* problem rather than a ground-state problem. **Score 1/5** now; flagged as the
natural extension if Bet R1 works.

## 14. Learning-based robotics where a variety appears

Normalising-flow IK (IKFlow, arXiv:2111.08933), neural-ODE IK (arXiv:2209.00498), learned
Groebner-solver stabilisation (arXiv:2401.09328) and learned monomial orders (arXiv:2602.02972). The
"variety" is the data manifold of a kinematic chain - the same closure variety as Bet R3 - and the
learning task is density estimation on it. There is a legitimate seed connection: `delta(f)^2` is the
polynomial-kernel / approximate-vanishing-ideal objective (report §5.7, citing
Heldt-Kreuzer-Pokutta-Poulisse and Livni et al. `[UNVERIFIED DOIs]`), i.e. Vanishing Component
Analysis is literally distance-to-the-approximate-vanishing-ideal. But the practical method is a small
SVD on a data matrix and the kernel trick already dequantises the interesting part. **Score 1/5.**

## 15. Scorecard

| # | problem | n | D or size | classical best and cost | seed regime | speedup type if any | score |
|---|---|---|---|---|---|---|---|
| 2 | 6R IK | 8 | 16 | 16x16 eig / IKFast 5 us | 0-dim, codim n | none | 1 |
| 3 | Stewart-Gough FK | 7 | 40 | 69x69 eig, sub-ms | 0-dim | none | 1 |
| 3b | architectural singularity / self-motion | 7 | dim test | heavy Groebner, open cases | dim test | slicing test | 2 |
| 4 | kinematic synthesis (6-bar) | 22-40 | 1e5-1.5e6 | D parameter-homotopy paths, CPU-days | 0-dim, multigraded | time, quadratic | 3 |
| 5 | singularity loci / workspace | 6-7 | hypersurface | evaluate det J | codim 1 | none | 2 |
| 6 | motion planning | 3-20 | PSPACE-complete | RRT ms (incomplete) | semialgebraic | none (BQPSPACE=PSPACE) | 1 |
| 7 | hand-eye / kinematic calibration | 8-100 | small LS | SVD / LM, us-ms | unit ideal | none | 1 |
| 8 | rigidity, realisation counting | 2n-3 | exp(n) | combinatorial recursion | 0-dim | none (counting) | 2 |
| 9 | force closure / grasping | ~30 | small SDP | sequential SDP, ms | inequalities | none | 1 |
| 10 | SLAM / certifiable perception | 1e2-1e6 | moment matrix | SE-Sync, Shonan, STRIDE | ground energy | space | 3 |
| 11 | vision minimal problems | <=20 | <=312 | elimination templates, us | 0-dim | none | 1 |
| 12 | contact modes | 10-20 | 3^N | enumeration, ms | sign conditions | none | 1 |
| 13 | SOS control | 4-20 | SDP | bilinear alternation | inequalities | none | 1 |
| 14 | learned IK / vanishing ideals | any | data | SVD, NN | approx. ideal | none | 1 |
| R3 | closure / self-motion varieties of many-joint chains | 10-100 | codim 6 | numerical irreducible decomposition | **codim O(1)** | space, maybe time | 3 |

---

## 16. The three best bets

### Bet R1 - Certified lower bounds for robot-perception polynomial optimisation via the bosonic moment hierarchy

**Input.** A robot-perception polynomial optimisation problem in Lagrange/homogeneous form: real
residual forms `f_1,...,f_d` of degree `m` in `n+1` real variables (rotation entries with
`R^T R = I`, translations, and TLS binary indicators `theta_i^2 = 1`), a relaxation order `N`, and a
guiding state (the Gauss-Newton local solution `p*`, lifted to the coherent state `|p*>^{⊗N}`).

**Output.** An estimate of `lambda_min(H_N)` with `H_N = sum_j a^dagger(f_j) a(f_j)` restricted to
`Sym^N(C^{n+1})`, to additive error `eps * alpha`. This is a valid lower bound on
`min_{||p||=1} sum_j w_j |f_j(p)|^2`, i.e. a certificate of global optimality (or of a bounded
suboptimality gap) for the perception problem, at hierarchy level `N`.

**Classical best.** SE-Sync / Shonan for the outlier-free case (arXiv:1612.07386, arXiv:2008.02737):
Burer-Monteiro on the rank-restricted first-order relaxation, near-linear per iteration, with a dual
certificate - *this is already near-optimal and Bet R1 does not attack it*. The target is the case
where the first- and second-order relaxations are not tight: outlier-robust TLS and matrix-weighted
estimation (arXiv:2109.03349, arXiv:2308.07275). There, the dense Lasserre level-3 moment matrix has
size `binom(n+3,3) = 176851` for `n = 100` (about 250 GB in double precision) and no solver exists;
STRIDE with a *sparse* level-2 relaxation is the state of the art and fails when level 2 is loose.

**Proposed quantum route.** Identify the level-`N` moment relaxation with the ground energy of the
seed Hamiltonian on the `N`-boson symmetric sector: `<p^{⊗N}|H_N|p^{⊗N}> = sum_j (N!/(N-m_j)!)
|f_j(pbar)|^2`, so minimising over `Sym^N` rather than over coherent states is the DPS /
sum-of-squares-on-the-sphere hierarchy, with convergence `O(m^2/N^2)` for `N >= Omega(m)`
(arXiv:1908.05155). Estimate `lambda_min(H_N)` by QSVT/phase estimation with the guiding state
`|p*>^{⊗N}`, using the sparse block encoding of `H_N` from report §5 (row-sparse, reversibly
computable entries, `alpha = poly(n) N^m max ||f_j||^2`). Space: `O(n log N)` qubits, i.e. about
300 qubits at `n = 100, N = 6`, versus 250 GB.

**What would have to be true for a real speedup.** (i) The overlap `|<p*^{⊗N}|psi_0>|` must be at
least `1/poly`, i.e. the Gauss-Newton solution must be within Fubini-Study distance `O(N^{-1/2})` of
the relaxation optimiser - plausible in the tight regime, and *implausible exactly when the relaxation
is loose*, which is the interesting case. This tension is the main risk. (ii) `alpha/Delta` for the
*shifted* Hamiltonian must be `poly(n)`; for an inconsistent system there is no frustration-free
kernel and the relevant quantity is the spectral gap above `lambda_min`, which is not the seed's
`Delta_N` and is unstudied. (iii) The certificate must be usable without trusting the quantum device;
a quantum-only bound is scientifically weaker than an SOS certificate a classical checker can verify.
A partial answer: run the quantum estimate to locate the bound, then extract a classical dual
certificate by a low-rank fit - untested. (iv) The classical baseline must not be dequantisable: at
*fixed* `N`, `dim Sym^N(C^{n+1}) = binom(N+n,n)` is polynomial in `n`, so the classical problem is in
P; the separation, if any, is a polynomial space-and-time separation with a large exponent, not an
exponential one. State it that way or not at all.

**First experiment (numerical, <= 1 day).** Take the smallest genuinely hard instance:
single rotation averaging with `n = 10-20` TLS measurements and 60-80% outliers, from the
`MIT-SPARK/CertifiablyRobustPerception` benchmark family. (a) Build `H_N` for `N = 4, 6` with the
seed's `bf.py` machinery on the homogenised residuals plus the Boolean generators `theta_i^2 -
theta_i z_0`; (b) exact-diagonalise and compare `lambda_min(H_N)` against the classical level-1 and
level-2 SDP bounds computed with a standard solver, verifying numerically that the bosonic ground
energy reproduces (or dominates) the moment bound - this is the checkable content of the
identification; (c) compute the overlap `|<p*^{⊗N}|psi_0>|^2` where `p*` is the Gauss-Newton
solution, separately for instances where level 2 is tight and where it is loose. If the overlap
collapses exactly on the loose instances, Bet R1 is dead and should be recorded as REFUTED.

### Bet R2 - Amplitude amplification over the design set of a large kinematic-synthesis system

**Input.** A six-bar or eight-bar synthesis system in multihomogeneous form: `n` variables partitioned
into `m` blocks with per-block degrees `(d_1,...,d_m)`; the generic root count `D` (known for the
tabulated families: `D = 8652` for nine-point four-bar, `92736` for Watt II eight-point, `1.5e6` for
Stephenson II eleven-position); a design predicate `P` (real, link lengths in range, no branch or
circuit defect, order-correct) implemented as a reversible classical circuit on a candidate point.

**Output.** A sample from `{roots satisfying P}`, or the report that none exists.

**Classical best.** Ab initio monodromy solve once (expected `O(D)` paths, arXiv:1609.08722), then a
parameter homotopy per design query tracking exactly `D` paths, followed by filtering. For Watt II
that is `9.3e4` tracks; for Stephenson II, `1.5e6`. Each track is `10^2`-`10^4` predictor-corrector
steps of `O(n^3)`, so `10^{12}`-`10^{14}` flops per query, hours on a CPU, minutes on a GPU
(arXiv:2112.03444). Filtering discards all but a handful.

**Proposed quantum route.** Work in the multidegree-`(d_1,...,d_m)` sector, whose dimension is
`prod_i binom(d_i + q_i - 1, q_i - 1)` - for Watt II with 11 blocks of two variables at degree 2,
`6^11 = 3.6e8`, five orders of magnitude below the total-degree sector `binom(47,22) ~ 1.5e13`. In
that sector, `ker H` is spanned by the coherent states of the roots (a theorem when `I` agrees with
`I(V)` in that multidegree). Start from the maximally mixed state on the sector (trivially
preparable), apply the QSVT ground-space projector `P_0 = 1 - Theta(H)`, and amplitude-amplify against
the predicate `P` implemented on the occupation register. Cost:
`sqrt(dim(sector) / |{roots satisfying P}|)` ground-space projections, each costing `alpha/Delta`
block-encoding uses; plus `O(1/eps^2)` copies to read the root's coordinates off repeated coherent-state
measurements. For Watt II with 10 acceptable designs: `sqrt(3.6e8/10) ~ 6000` projections versus
`9.3e4` classical path tracks - only a factor 15 in *operation count*, and each quantum operation is
vastly more expensive. For Stephenson II the ratio is more favourable but still not dramatic.

**What would have to be true for a real speedup.** (i) `Delta/alpha >= 1/poly` in the multigraded
sector - completely unknown, and the seed's Prop. 8.3(d) shows multigraded sectors admit
exponentially small gaps. (ii) The synthesis ideal must be close to radical and saturated in that
multidegree; in practice these formulations carry massive degenerate components (zero-length links,
coincident precision points, solutions at infinity) which inflate `dim ker H` and destroy the overlap
computation above. This is the seed's Conj. 8.5 defect and here it is first-order, not a correction.
(iii) The design predicate must be checkable *coherently* on a coherent state, which for a branch-defect
test means simulating the linkage through a full crank rotation inside the oracle - expensive and
possibly the dominant cost. (iv) The quantum operation count must be compared to the *right* classical
baseline (parameter homotopy after monodromy, `D` paths), never to the multihomogeneous degree
(`7e5` for Watt II, `2.6e8` for Stephenson II), which no one tracks any more.

**First experiment (numerical, <= 1 day).** Use the nine-point four-bar problem, the smallest instance
with a large `D`. (a) Write the eight isotropic-coordinate equations in multihomogeneous form and
build the multigraded `H` on the relevant sector; the sector dimension should be small enough for
sparse eigensolvers. (b) Measure `Delta` (smallest nonzero eigenvalue), `alpha`, and
`dim ker H`, and compare `dim ker H` with the expected `8652` - the gap between them *is* the
degenerate-component defect and is the number that decides the bet. (c) Fit `Delta/alpha` as the
formulation is varied (isotropic coordinates versus real coordinates versus Study coordinates) to
see whether any formulation is benign. A single afternoon with `bf.py` plus `HomotopyContinuation.jl`
for ground truth.

### Bet R3 - Degree and dimension of closure and self-motion varieties of many-joint mechanisms

**Input.** A mechanism with `j` joints (hyper-redundant or continuum manipulator, `j = 10..100`;
modular reconfigurable robot; deployable structure; closed-chain molecular loop) given by its loop-closure
equations in tangent-half-angle or per-joint quaternion coordinates: **6 equations (per loop) in `j`
variables**, i.e. `codim V = 6` fixed while `n = j` grows.

**Output.** `dim V` and `deg V`. Robotics meaning: the dimension of the self-motion / redundancy
manifold, and the number of inverse-kinematics branches on a generic 6-dimensional slice - i.e. the
number of distinct assembly modes the mechanism can reach, which controls redundancy resolution,
reconfiguration planning and workspace connectivity.

**Classical best.** Numerical irreducible decomposition: witness sets computed by slicing with a
generic linear space of complementary dimension and tracking a homotopy (Bertini,
HomotopyContinuation.jl, PHCpack). Cost is at least `deg V` path tracks, and the start system must
be a root count that dominates `deg V`; the naive multihomogeneous bound for 6 equations of multidegree
`(2,...,2)` in `(P^1)^j` sliced by `j-6` hyperplanes is `2^6 * j!`, which is astronomical and 3000x
loose already at `j = 6` (it gives 46080 where the answer is 16). Consequently *nobody computes these
for `j > 8`*, and the growth rate of `deg V` in `j` is, as far as this pass could determine, not known
in closed form `[UNVERIFIED - worth a dedicated literature check]`.

**Proposed quantum route.** This is the seed's *only* good regime: `codim = 6 = O(1)`. With `N ~ n`,
`HF(N)/binom(N+n,n) ≈ deg V * (n/N)^6 = Theta(deg V)` - an order-one quantity, so the DQC1-style
normalised-trace estimator reads `deg V` off with `O(1)` additive precision and `O(alpha/Delta_N)`
cost, using `O(n log N)` qubits to address a space of dimension `binom(2n,n) ~ 4^n`. Reading `dim V`
is the same measurement at two values of `N`. This is Conjecture 8.7 of the seed applied to the one
robotics family that satisfies its hypothesis.

**What would have to be true for a real speedup.** (i) `deg V` must actually grow super-polynomially
in `j`; if it is `O(j^6)` (which the projective Bezout bound `(2j)^6` permits), the classical witness
set is polynomial and the bet collapses to a constant-factor argument. **This is the single decisive
unknown and it is cheap to test.** (ii) `Delta_N/alpha >= 1/poly(n,N)` at `N ~ n` for this family -
the seed's Conj. 8.3(a) and (c). Note the danger: a kinematic chain with an unactuated or decoupled
joint makes `V` a cone, and Fact 7.2 / Conj. 8.3(b) then *pin the gap to a constant*, which is
favourable, whereas a redundant generator (two loop equations that nearly coincide, i.e. a
near-singular architecture) drives `Delta_N` to zero - so the Macaulay gap is plausibly a
*kinematic conditioning number*, which is an interesting claim in its own right. (iii) The regularity
must be `poly(j)` so that `N ~ n` is in the stable range. (iv) The variety must be reduced enough that
`HF` counts what we want; chains with permanently coincident axes give non-reduced structure.

**First experiment (numerical, <= 1 day).** Purely classical and decisive: for `j = 7,8,9,10,11,12`,
build the loop-closure ideal of a generic spatial `jR` chain in tangent-half-angle coordinates,
compute `deg V` (and `dim V`, to confirm `j-6`) with `HomotopyContinuation.jl` witness sets or with a
Groebner/Hilbert-series computation in Macaulay2 for the smaller `j`, and fit the growth of `deg V`.
If `deg V` grows polynomially, record Bet R3 as REFUTED and say so. If it grows exponentially,
proceed to measure `Delta_N` on the same ideals at `N = 6..10` with `bf.py` - that second step is a
second day, not the first.

---

## 17. Killers

Stated sharply, in decreasing order of how much they hurt.

**K1. Robotics kinematics is zero-dimensional, and the seed is only good in low codimension.**
Every canonical robotics polynomial problem - IK, parallel FK, minimal vision problems, calibration,
rigidity realisations, synthesis - has finitely many solutions, i.e. `codim = n`. The seed's readable
observables are the normalised Hilbert function and normalised traces, and both are informative only
when `codim = O(1)`. At `codim = n` the signal is `D/binom(N+n,n)`, exponentially small, and additive
estimation is hopeless (§1.1). Only Bet R3 escapes, and only because redundant chains are the one
family whose codimension is fixed by the number of loop equations rather than by the number of joints.

**K2. Robotics wants real solutions; the construction sees only the complex variety.**
16 complex IK solutions, 0-8 real ones. 8652 complex synthesis roots, ~10 usable linkages. There is no
projector onto a real form, and the classical real-root machinery (Hermite signatures, Descartes,
subresultants) needs integer resolution out of a trace, which additive quantum estimation cannot give
(§1.2). Any quantum robotics claim that quietly counts complex solutions is answering the wrong
question.

**K3. Every quantum counting primitive gives additive precision on a normalised quantity; every
robotics count is an exact small integer.** The number of IK branches, of assembly modes, of
realisations, of real roots - all are integers to be known exactly, and all require relative precision
`1/D`. Exact quantum counting costs `sqrt(dim * D)`, worse than the classical `D`. This is a corollary
of the seed's own #P-hardness anchor and it recurs in §2, §3, §4, §8 and §11 independently.

**K4. The problem sizes are fixed and small, and the offline/online split already ate the advantage.**
6R IK: 16 solutions, 5 microseconds. Stewart-Gough: 40 solutions, a 69x69 eigenproblem. Five-point
relative pose: 10 solutions, tens of microseconds, called 10^4 times per frame inside RANSAC. The
vision community *already* does exactly what a quantum-linear-algebra proposal would propose:
precompute the Macaulay/elimination structure offline, then run cheap fixed-size linear algebra
online. There is no asymptotics to exploit and no latency budget for a coprocessor.

**K5. The classical best-in-class in robotics is homotopy continuation, which is a small-space,
embarrassingly parallel algorithm.** The "quantum saves space on the Macaulay matrix" argument is an
argument against a strawman: robotics abandoned resultant and Macaulay-matrix methods for large
systems decades ago precisely because they do not fit in memory, and uses path tracking, which needs
`O(n)` memory per path and scales linearly on GPUs. A space speedup over a method nobody uses is not a
speedup.

**K6. For motion planning there is a proof that no space speedup exists.** The generalised movers'
problem is PSPACE-complete (Reif; Canny) and `BQPSPACE = PSPACE`, so quantum offers no asymptotic
space advantage for exactly the robotics problem where classical space is the bottleneck. And in
practice the field abandoned complete planners for sampling-based heuristics running in milliseconds.

**K7. Noise-tolerant heuristics already win, and robotics does not need exactness.** Perception is
noisy; a certificate is a nicety, a fast local solution is the product. SE-Sync and Shonan get global
optimality *and* near-linear cost by exploiting low rank (Burer-Monteiro). Quantum SDP solvers do not
beat near-linear-time classical solvers, and their width and precision dependences are worst exactly in
the high-accuracy regime that certificates require.

**K8. The heuristic-hardware clause cuts against the applications, not for them.** The natural analog
attack on a frustration-free rank-one-projector Hamiltonian is "prepare a product state, postselect on
all constraints" - which for a mechanism is rejection sampling on the configuration variety, classically
trivial. The other natural fit, boson sampling, computes permanents, and the robotics permanents that
appear (multihomogeneous Bezout numbers are permanent-type coefficients of the degree matrix) are
permanents of *nonnegative integer* matrices, for which a classical FPRAS exists (Jerrum-Sinclair-Vigoda)
`[UNVERIFIED DOI]`, and exact evaluation is #P-hard for quantum too.

**K9. Fixed mode number is classically easy.** The seed's own §6 anchor: permutation-invariant
Hamiltonians on `N` qudits of fixed local dimension are classically solvable in `poly(N)` via
Schur-Weyl (Anschuetz-Bauer-Kiani-Lloyd, arXiv:2211.16998, Quantum 7:1189). "Fixed mechanism, growing
degree `N`" is therefore classically easy, which removes the most natural robotics framing ("one robot,
push `N` up"). Any advantage must come from growing `n`, i.e. growing the number of joints, variables
or measurements - which points at exactly the three bets and at nothing else.

**K10. The seed's own prior-art warning applies verbatim.** Chen-Gao ran HHL on a Macaulay system;
Ding-Gheorghiu-Gilyen-Hallgren-Li showed the condition number is exponential unless the solution has
logarithmic Hamming weight (Quantum 7:1069, 2023). The lesson transfers: in the hard instances the cost
hides in a normalisation, not in a spectral gap. Every number in §16 that is written as
`alpha/Delta` is an unmeasured quantity, and the honest state of this lane is that no robotics ideal
has ever had its Macaulay gap computed.

---

## 18. Questions for TJO

1. **Is an offline speedup acceptable?** The only robotics problem at a size where asymptotics could
   matter is kinematic synthesis, which is a design-time computation taking CPU-days. If "robotics
   application" means something that runs on a robot, the honest answer for this lane is no, and the
   lane should be closed after Bet R3's one-day experiment. If a design-time speedup counts, Bet R2 is
   the target.
2. **Space or time?** Bet R1 is a space claim (moment matrix: 250 GB versus ~300 qubits) with no
   plausible time claim. Bet R2 is a time claim (quadratic) with no space claim. They cannot both be
   pursued at the current lane budget. Which does the north star prefer?
3. **How much does the "genuinely new" clause bind?** The identification in §10 - the seed Hamiltonian's
   ground energy *is* the DPS/sum-of-squares moment bound used by certifiable robot perception - looks
   new *as a statement*, but the underlying hierarchy is classical (Doherty-Parrilo-Spedalieri,
   Fang-Fawzi) and so is its use in robotics (Yang-Carlone). Is "new bridge, old objects on both ends"
   enough, or does the campaign need a new algorithm?
4. **Is a quantum-only certificate acceptable?** Robotics certification culture wants a dual/SOS
   certificate a classical checker can verify. A quantum ground-energy estimate is a number you must
   trust the device for. If that is unacceptable, Bet R1 loses most of its value and should be
   reframed as "find the bound quickly, then certify classically".
5. **Should the multigraded mechanism dictionary (§1.3) be developed for its own sake?** It gives a
   2-local frustration-free qutrit chain whose zero-energy product states are a mechanism's
   configurations - the cleanest hardware-facing object this lane found, and the only one that meets
   the north star's linear-optics / Bose-Hubbard clause. It is not a speedup, but it might be the
   right physics paper.
6. **Do we accept `[UNVERIFIED]` on the robotics-specific classical baselines?** Several load-bearing
   numbers (Plecnik-McCarthy root counts, Husty and Dietmaier DOIs, Raghavan-Roth DOI, Primrose bound)
   were confirmed by secondary sources only. A half-day of DOI resolution would harden §4 and §2; say
   whether that is worth the budget before Bet R2 is quoted anywhere.

---

## 19. MERGE PROPOSAL (for the orchestrator; no shared file was edited by this lane)

Candidate claim rows for `claims/CLAIMS.md`, all at CONJECTURE or below:

- `qaag-rob-1` (SKETCH, checkable in one day): For real residual forms `f_j` of degree `m`,
  `min_{psi in Sym^N} <psi|H_N|psi>` equals the level-`N` sum-of-squares-on-the-sphere / DPS bound for
  `min_{||p||=1} sum_j (N!/(N-m_j)!) |f_j(pbar)|^2`, with convergence `O(m^2/N^2)` for `N >= Omega(m)`
  by arXiv:1908.05155. Where-tested: Bet R1 first experiment.
- `qaag-rob-2` (REFUTED-candidate, i.e. propose to record the negative): For every zero-dimensional
  robotics ideal (IK, parallel FK, minimal vision problems, rigidity realisations, synthesis), the
  seed's normalised-Hilbert-function readout requires additive precision `1/binom(N+n,n)` and is
  therefore dominated by the classical eigenvalue or homotopy method by more than ten orders of
  magnitude at real sizes. Evidence: §1.1 table.
- `qaag-rob-3` (CONJECTURE): For the loop-closure variety of a generic spatial `jR` chain in
  tangent-half-angle coordinates, `codim V = 6` and `deg V` grows super-polynomially in `j`.
  Decisive one-day experiment specified in Bet R3. If false, Bet R3 is REFUTED.
- `qaag-rob-4` (CONJECTURE): The Macaulay gap `Delta_N` of a mechanism's loop-closure ideal is a
  kinematic conditioning number: it is pinned to a constant when the mechanism has a decoupled joint
  (cone case, Fact 7.2 / Conj. 8.3(b)) and tends to zero as the architecture approaches an
  architecturally singular design (redundant generators). Untested.
- `qaag-rob-5` (definition request for `definitions/`): the multigraded mechanism dictionary of §1.3
  (sites = joints, levels = `{1, c_i, s_i}` or unit quaternions, constraints = rank-one projectors),
  which several of the above rows depend on.

## 20. References resolved in this pass

Kinematics and synthesis. Manocha-Canny, general 6R IK, IEEE T-RA 10(5):648-657, 1994,
DOI 10.1109/70.326569. Raghavan-Roth, ASME JMD 115(3):502, 1993, DOI 10.1115/1.2919218 [UNVERIFIED];
Lee-Liang 1988 and Primrose 1986 for the bound 16 [UNVERIFIED]. Husty, Mech. Mach. Theory
31(4):365-380, 1996 [UNVERIFIED DOI]; Dietmaier 1998, 40 real postures [UNVERIFIED DOI]. Martyushev,
arXiv:2505.00634 (MMT 215:106170, 2025). Wampler-Morgan-Sommese, ASME JMD 114(1):153-159, 1992
[UNVERIFIED DOI] (8652 roots, 1442 linkages). Brake-Hauenstein-Murray-Myszka-Wampler,
DOI 10.1115/1.4033251. Plecnik-McCarthy six-bar root counts [UNVERIFIED DOIs]; parallelised solver
DOI 10.1007/978-3-319-93188-3_16 [UNVERIFIED]. Nawratil et al., arXiv:1701.09107, arXiv:1712.06952.

Numerical algebraic geometry. Duff-Hill-Jensen-Lee-Leykin-Sommars, arXiv:1609.08722 (IMA JNA
39(3):1421-1446, 2019). Chien et al. GPU-HC, arXiv:2112.03444. Fabbri et al., arXiv:1903.09755.
Basu-Roy-Safey El Din-Schost, arXiv:1201.6439 (`d^{O(k sqrt k)}`).

Rigidity. Capco-Gallet-Grasegger-Koutschan-Lubbes-Schicho, arXiv:1701.05500; summary arXiv:1707.03633;
data Zenodo 1245517. Bartzos-Emiris-Legersky-Tsigaridas, arXiv:1802.05860, arXiv:1811.12800
(JSC 102:189-208, 2021), arXiv:2010.10578.

Perception, SLAM, optimisation. Rosen-Carlone-Bandeira-Leonard SE-Sync, arXiv:1612.07386.
Dellaert-Rosen-Wu-Mahony-Carlone Shonan, arXiv:2008.02737. Yang-Carlone, arXiv:2109.03349
(IEEE TPAMI 2022). Matrix-weighted relaxations, arXiv:2308.07275. Contact-rich SDP,
arXiv:2502.02829. Dai-Majumdar-Tedrake, DOI 10.1007/978-3-319-51532-8_18. Contact mode enumeration,
DOI 10.1007/978-3-030-66723-8_29 [UNVERIFIED].

Vision minimal solvers. Nister, DOI 10.1109/TPAMI.2004.17. Kukelova-Bujnak-Pajdla,
DOI 10.1007/978-3-540-88690-7_23. GAPS arXiv:2004.11765; sparse resultants arXiv:2301.06443;
FFT-based arXiv:2605.06572; learned start pairs arXiv:2411.03745; learned Groebner stabilisation
arXiv:2401.09328.

IK and learning. Maric et al., arXiv:2108.13720 (IEEE T-RO 38(3):1703-1722, 2022). Globally optimal
IK as a QP, arXiv:2312.15569. IKFlow arXiv:2111.08933; NODE IK arXiv:2209.00498. Comprehensive
Groebner systems for IK, arXiv:2305.12451, arXiv:2509.00823.

Quantum-side anchors. Fang-Fawzi, arXiv:1908.05155. Gharibian-Le Gall, arXiv:2111.09079; improved
hardness arXiv:2207.10250. Anschuetz-Bauer-Kiani-Lloyd, arXiv:2211.16998 (Quantum 7:1189, 2023).
Levine-Movassagh, arXiv:1611.03147. Ding-Gheorghiu-Gilyen-Hallgren-Li, Quantum 7:1069, 2023.
Watrous, `BQPSPACE = PSPACE` [UNVERIFIED DOI]. Prior quantum-robotics work, as a baseline of what not
to repeat: quantum annealing for IK, Sci. Rep. 2025 [UNVERIFIED DOI]; QML plus Grover for manipulator
posture, arXiv:2509.07216 - both compare against numerical IK rather than IKFast and do not meet the
north star's best-in-class requirement.
