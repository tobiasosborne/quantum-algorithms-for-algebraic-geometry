# Independent verdict: thermal/CP and root R11 portfolios

Reviewer: Sol, independent of both proposer files, 2026-09-07.  Scope is
`scouting/thermal-cp-frontiers-r11.md` and `scouting/root-frontiers-r11.md`.
Claim status remains canonical only in `claims/CLAIMS.md`; this verdict promotes
nothing.  I independently derived the identities below before using the supplied
checker.  Ordinary finite-dimensional Hermitian metrics in the root memo are
accepted as declared departures from C1; the thermal Fock calculation is audited
under C1 and C3.

## Verdict

**PASS after repair as a scoped construction/control portfolio; no north-star
hit.**  The initial review was FAIL because T03 was not a defined invariant
algorithm.  The live repair fixes its degree, sign, quotient output,
normalisation and error budget.  T01's bath-Gram and absorption identities and
the scoped root controls R01/R02/R03/R06 also survive.  Broad classical-match
statements are now restricted to classically applicable matvec access.

No T or R candidate currently proves a true quantum advantage.  The user's
later novelty clarification makes QSVT, supersymmetric, CP, adiabatic, Zeno and
other non-Grover/non-QFT/non-DQI mechanisms eligible; prior-operation reductions
below are comparators rather than automatic novelty failures.  Under that rule
T01 ranks first and repaired T03 second.  This does not support a broad
impossibility claim.

## 1. Independent derivations

### 1.1 T01: Fock bath Gram and absorbing survival

Let `p_a=g f_j in R_d` and `A_a=a(p_a):R_N->R_(N-d)`.  With the environment
coefficient convention of the proposer,

`<a|sigma_E|b>=(M_N alpha^2)^(-1) Tr(A_b^dag A_a)`.                    (1)

The map `p -> a(p)=bar p(partial)` is conjugate-linear.  Hence the right side
is conjugate-linear in `p_a`, linear in `p_b`, and has the orientation
`<p_a,p_b>_F`, exactly the `(a,b)` entry of `F_d^dag F_d`; it is not its
transpose.  Unitary invariance on the irreducible `R_d` makes the scalar
independent of `p`.  At `p=z_0^d/sqrt(d!)`,

`||a(p)||_HS^2=sum_(|nu|=N) binom(nu_0,d)
                =binom(N+n,N-d)=c_(N,d)`.                              (2)

Thus

`sigma_E=c_(N,d)(M_N alpha^2)^(-1)F_d^dag F_d`.                       (3)

Equations (1)--(3) and the syzygy-kernel statement are correct.  The operational
direction matters: the bath state has support on `(ker F_d)^perp`; syzygies are
zero-weight directions and cannot be sampled or projected out of copies of this
state alone.

For `B=F_d/alpha_F`, put the live and sink spaces in a direct sum and take
`J=|sink><live| tensor B`, zero on the sink.  The Lindbladian no-jump block is
`exp(-tB^dag B/2)`, and the live probability from `I_L/L` is

`q(t)=L^(-1)Tr exp(-tB^dag B)`.                                       (4)

If `lambda_min^+(B^dag B)>=eta`, spectral decomposition gives
`0<=q(t)-dim ker(F_d)/L<=e^(-eta t)`.  The full jump/no-jump process is CPTP.
This absorption experiment, rather than the conditional bath state, supplies
the nullity bit samples.

The same derivation for two ordered emissions yields a Gram matrix of product
columns because bosonic annihilators commute.  It is a larger Macaulay map; no
Yoneda quotient or signed higher operation appears without another construction.

### 1.2 T02: reset channel and Kato scope

For `K_0=P` and `K_(ab)=r^(-1/2)|g_a><e_b|`, direct summation gives

`sum K_i^dag K_i=P+Q=1`,
`E_P(rho)=P rho P+Tr(Qrho)P/r`.                                       (5)

Positivity shows that its fixed densities are exactly those supported on `P`.
The monitored all-zero branch along `P_0,...,P_m` is
`P_m...P_1P_0`, independent of how the failed branch is reset.  On a unit
interval with `||dot P||<=Lambda` and a uniform second-derivative bound, the
per-step leakage is `O(Lambda^2/m^2)`, total leakage is `O(Lambda^2/m)`, and the
projection product converges to metric Kato transport at first order in `1/m`.

This establishes neither Gauss--Manin transport nor an advantage.  A
two-outcome projective instrument with termination on failure already produces
the same accepted product; preparing `P_j/r` is necessary only for the chosen
reset-completed channel.  A coherent trace interferometer also needs dilations
and reference-state preparation, rather than measured environment records that
have already decohered.

### 1.3 T03: the sign, quotient, and best Green normalisation

Take degree-one cocycles `a,b,c`, and suppose `ab=du`, `bc=dv`, with
`u=h(ab)`, `v=h(bc)`.  The graded Leibniz rule gives

`d(uc)=abc`, `d(av)=-abc`.                                             (6)

Therefore `z=uc+av` is closed; the minus sign displayed in thermal equation
(15) gives derivative `2abc` in characteristic zero.  Saying “up to the usual
degree signs” is insufficient for an executable exact map.

The class is a Massey coset in

`H^2 / ([a]H^1+H^1[c])`                                                (7)

for degree-one inputs.  A norm requires a declared Hodge metric and an
orthogonal quotient projector.  A phase requires a supplied reference
`w` in the quotient, for example the complex scalar `<w,z>`.  Neither “the
phase” nor the unprojected norm is an intrinsic common output.

The regularised homotopy

`h_zeta=d^dag(H+zeta)^(-1)(1-P_0)`                                    (8)

is legal but does not solve `dh_zeta(ab)=ab` exactly.  Its error bound
`||h_zeta-h||<=zeta/Delta^(3/2)` is correct under the positive gap `Delta`.
The proposed Kraus scale `1/(2sqrt(zeta))` is safe but unnecessarily severe.
On the nonzero spectrum,

`||h_zeta||=max_lambda sqrt(lambda)/(lambda+zeta)`;                     (9)

when `0<zeta<=Delta<=lambda`, this is at most
`sqrt(Delta)/(Delta+zeta)<=1/sqrt(Delta)`.  A resource statement should use
(9) or a justified block-encoding normalisation, not turn regularisation error
into a spurious inverse square root of `zeta`.  Final harmonic/quotient
projection and its access cost remain even after this repair.

### 1.4 Root controls R01--R06

R01 is correct in its stated star-algebra scope.  If `P` is the harmonic
projector, then `dP=d^dag P=Pd=Pd^dag=0`.  Every element of the unital star
algebra acts as a scalar on `P` and has no cross block, so Lindblad generators
and TP Kraus families in that algebra satisfy `L^*(P)=0` or `E^*(P)=P`.
This proves conservation of harmonic population, not impossibility after adding
geometric jumps outside that algebra.

R02's dual-number matrix has singular values `sqrt(2),1`; `mu/sqrt(2)` is the
optimal globally scaled contraction.  On two identical copies with
`x=|a|^2`, success is `2x-3x^2/2`, maximised by `x=2/3` at `2/3`.  The displayed
dagger-Frobenius counterexample on `e tensor e` is correct.  The cited
dagger-Frobenius/C*-algebra comparison must retain its finite-dimensional,
unital, associative and relevant normalisability hypotheses.  It excludes a
positive dagger-Frobenius structure on this commutative nonreduced algebra; it
does not exclude nilpotent elements of noncommutative operator algebras.

R03's Born cancellation is exact for the displayed instrument.  Multiplying
`p_i=w_i(s_i^dag Hs_i)/(c Tr H)` by
`|H^(1/2)s_i><H^(1/2)s_i|/(s_i^dag Hs_i)` removes the desired inverse
denominator.  Rejection with `a/(s_i^dag Hs_i)` has the stated acceptance and
exposes the minimum evaluation norm.  This refutes that implementation only;
coherent inverse weighting or another matrix-scaling channel remains open with
its condition cost.

R05's scope correction is correct.  For a full-rank density family in a fixed
ambient space, `sqrt(rho)` is a global purification-amplitude section, so the
ordinary Uhlmann bundle is topologically trivial and its ordinary Chern
character vanishes.  Its connection can still have nontrivial holonomy.
Spectral subbundles, rank-deficient families, families on a pre-existing
nontrivial bundle, and modified thermal functionals are different targets.

R06's peripheral obstruction is correct and can be strengthened to positive
trace-preserving maps.  Trace-norm power boundedness excludes a nontrivial
Jordan block at `|lambda|=1` by linear-or-higher growth of `E^n` on a Jordan
chain.  It gives no lower bound for interior transients and no classical
simulation theorem for succinct channels.

## 2. Objections and repair demands

### O1 — FATAL: T03 is not an exact invariant algorithm

The displayed degree-one representative has the wrong relative sign, “phase”
has no reference, and neither the harmonic projection nor the indeterminacy
quotient (7) is part of the completed channel.  The table's phrase “exact
obstruction output” is false as written.

**FIX DEMAND.**  Restrict to stated degrees; use the sign forced by (6); define
the output as `||Pi_Q P_0 z||^2` or `<w,Pi_QP_0z>` for a supplied quotient
reference `w`; specify, implement, normalise, and charge `P_0` and `Pi_Q`;
state whether (8) approximates this exact Hodge-selected output or instead
defines a separate regularised scalar.

**SURVIVING STATEMENT.**  With corrected signs and supplied Hodge/quotient
access, two multiplication branches and a Green homotopy give a standard
representative of the triple Massey coset.  No advantage follows; QSVT/LCU is
eligible under the user's clarified novelty rule.

### O2 — MAJOR: T03's Kraus scale obscures the actual gap dependence

The global `1/(2sqrt(zeta))` bound ignores that `(1-P_0)` restricts the spectrum
to `lambda>=Delta`; for `zeta<=Delta`, (9) is parametrically tighter.  The memo
therefore mixes regularisation accuracy with physical contraction probability.

**FIX DEMAND.**  Replace the scale by the exact spectral maximum in (9), or a
computable upper bound such as `1/sqrt(Delta)`, and propagate the chosen
block-encoding normalisations through multiplication, final quotient
projection, repetitions, and precision.

**SURVIVING STATEMENT.**  The resolvent error
`||h_zeta-h||<=zeta/Delta^(3/2)` and the existence of a legal complementary
Kraus map survive.

### O3 — MAJOR: T01's bath state does not operationally expose syzygies

Equation (3) places every syzygy in the zero eigenspace of the emitted state.
Copies of a density matrix never sample their zero-weight directions.  The
one-shot bath identity is mathematically useful, but it does not by itself
avoid a kernel-overlap/readout problem.

**FIX DEMAND.**  Separate the bath-Gram theorem from the coefficient-register
absorption algorithm.  State explicitly that (4), applied to a maximally mixed
domain state, is the proposed nullity estimator; do not attribute that output
to measurements of the bath state without an additional complement operation.

**SURVIVING STATEMENT.**  The unnormalised bath state is exactly (3), including
the Fock/binomial factor and C3 conjugation, and its algebraic kernel is the
tuple-syzygy space.

### O4 — MAJOR: T01 lacks a same-access end-to-end comparison

Sparse polynomial coefficients do not automatically provide a unit-cost
block encoding or Lindblad jump.  Row/column sparsity normalisation, reversible
indexing, `alpha_F`, simulator precision, and total physical time must be tied
to the actual Macaulay access.  Conversely, classical Chebyshev/Krylov heat-
trace estimation often needs only `O(eta^(-1/2) log(1/epsilon))` polynomial
degree, while literal dissipative evolution takes
`eta^(-1)log(1/epsilon)` time.  A dense `2^q` circuit description does not give
the classical side a sparse matvec, so the comparison must not switch access
models.

**FIX DEMAND.**  Give one growing non-squarefree family, explicit row/column
oracles and their normalisation, syzygy fraction, `eta`, simulation cost, and
  the best classical method under that identical oracle.  Classify the absorbing
  algorithm as heat-kernel/QSVT nullity estimation; this is now novelty-eligible,
  but the reclassification supplies no advantage theorem.

**SURVIVING STATEMENT.**  Under a supplied implementation of `B` and the gap
promise, (4) estimates normalised tuple-syzygy nullity with the stated
finite-time bias and Bernoulli sample count.

### O5 — MAJOR: T08's dequantisation conclusion exceeds its access proof

Hutchinson sampling applies `B_w` and its adjoint to classical random vectors.
That is a matched attack for explicit or classically applicable sparse
multiplication maps.  A compiled quantum circuit for a succinct contraction
does not itself give an efficient classical matvec.  The phrase “rejected
generally” is therefore unsupported.

**FIX DEMAND.**  Restrict the rejection to classically applicable sparse/table
access.  Hold the succinct-circuit version pending a same-output lower bound,
while refusing to infer an advantage merely from generic circuit simulation.

**SURVIVING STATEMENT.**  Persistent-state recycling gives success
`Tr(B_w^dag B_w)/D` from a maximally mixed input and removes no Hutchinson cost
in the explicit-matvec model.

### O6 — MAJOR: T13 conflates a full reset channel with its no-reset branch

Principal-angle powers govern products of orthogonal projectors on the
conditioned no-reset trajectory.  The spectrum and stationary state of the
reset-completed CPTP composition also depend on the chosen reset densities;
they are not determined only by principal angles.

**FIX DEMAND.**  Define the output either for the heralded product
`P_JP_I...` and charge its survival probability, or for the full CPTP channel
and derive its reset-dependent spectrum.  Do not transfer the former decay
law to the latter.

**SURVIVING STATEMENT.**  The monitored no-reset branch reduces to alternating
projections and reproduces the earlier principal-angle/intersection mechanism.

### O7 — MAJOR: T02's reset resource is not the source of Kato holonomy

The accepted path (11) is independent of the reset completion.  A terminating
two-outcome projector instrument implements the same accepted map without
preparing `P_j/r`; using measured bath records also destroys the coherence
needed for a character interferometer unless a coherent dilation is retained.

**FIX DEMAND.**  Separate (i) the exact CPTP reset channel and fixed-state
theorem, (ii) the heralded/coherent product-of-projections holonomy algorithm,
and (iii) the resource for preparing the reference maximally mixed/entangled
state in `P_0`.  State the parameter interval and derivative constants in the
Kato error theorem.

**SURVIVING STATEMENT.**  Equations (5) and the first-order Kato projection
limit survive.  The geometric output is the Fock-metric Kato holonomy unless an
explicit Gauss--Manin intertwiner is proved.

### O8 — MINOR: per-trial simulation error is overcharged in T01

Requiring probability error `O(epsilon/R)` in each of `R` independent
Bernoulli trials is sufficient but unnecessary for estimating one expectation.
A uniform per-trial bias at most a fixed fraction of `epsilon` suffices; the
sampling variance is handled by `R`.

**FIX DEMAND.**  Use an expectation-bias error budget, or label the union-bound
choice as deliberately nonoptimal and include its resulting simulator cost.

**SURVIVING STATEMENT.**  `R=O(epsilon^(-2)log(1/delta))` ideal Bernoulli trials
and `t=eta^(-1)log(2/epsilon)` suffice.

### O9 — MAJOR: R02, R04, R07, and R08 lack complete problem-level algorithms

R02 proves a two-dimensional fusion control but gives no growing common output;
R04 is an implementation question; R07 and R08 have neither full channels nor
resource theorems.  Calling these constructive follow-ups is appropriate, but
they cannot enter a speedup tournament as completed algorithms.

**FIX DEMAND.**  Keep the exact R02 matrix result as a control.  For any route
advanced, supply a growing algebraic family, common access/output, full CP or
Hamiltonian instrument, success/mixing/time/precision, and matched classical
algorithm.  Do not generalise an undeveloped route's failure to its domain.

**SURVIVING STATEMENT.**  Retained-environment fusion, coherent higher-product
response, metric-explicit Fourier--Mukai kernels, and signed torsion differences
remain valid areas for new constructions.

### O10 — MINOR: source scopes must be attached to the root controls

The root memo is careful in prose, but its merge statements should carry the
hypotheses that make the cited comparisons exact: the star-algebra restriction
for R01, the finite unital associative dagger-Frobenius/C*-algebra setting for
R02, fixed global ambient frame and full rank for R05, and finite-dimensional
CPTP power boundedness for R06.

**FIX DEMAND.**  Copy these hypotheses into every proposed canonical statement,
including explicit exclusions of added geometric jumps, rank-deficient limits,
and interior Jordan blocks.

**SURVIVING STATEMENT.**  With those scopes, all four negative/control results
are correct.

### O11 — MAJOR for canonicalisation: the repaired definitions still have notation/interface defects

`D-R11-TRIPLE-QUOTIENT-QUERY` defines `P_2` but later writes the regularised
homotopy with `(1-P)`, where `P` is undefined in that definition.  The thermal
candidate table also retains the stale “norm/phase of a regularised” output,
although the repaired section now asks only for the exact degree-one quotient
norm.  Finally, the new definitions use bare `alpha`, decorated `alpha_mu`,
`alpha_h`, and `beta` for block/Kraus normalisations despite binding convention
C7, which reserves these symbols and requires `alpha_BE` notation.  The thermal
memo uses `D` as Hilbert dimension without declaring its C8 departure in its
opening paragraph.

**FIX DEMAND.**  Replace the undefined `P` by the harmonic projector on the
relevant degree (or omit it on promised exact inputs with a proof); make the T03
table input/output match D-R11-TRIPLE-QUOTIENT-QUERY; rename all block/Kraus
scales consistently with C7 or declare a local departure at the beginning; and
declare/repair the C8 dimension notation.

**SURVIVING STATEMENT.**  The repaired degree-one plus-sign quotient norm is a
well-defined finite problem once the harmonic projector symbol and compiled
interfaces are made consistent.

## 3. Audit of every thermal candidate

| ID | Independent disposition | Required scope or repair |
|---|---|---|
| **T01** | **ACTIVE conditional algorithm; accept (3)--(4) as scoped mathematics.** | Separate zero-support bath Gram from live-register absorption; specify Macaulay block access, normalisations and same-oracle classical heat trace. Heat/QSVT nullity estimation is novelty-eligible; a concrete hard family and advantage remain missing. |
| **T02** | **HOLD for advantage; accept the channel control.** | Separate reset completion, monitored Kato product, and coherent trace circuit. Keep metric Kato scope; no Gauss--Manin claim without an intertwiner. Zeno transport is eligible under the clarified novelty rule. |
| **T03** | **ACTIVE conditional compiled primitive after repair.** | Degree-one sign, exact quotient output, final projector access, Green normalisation, success and precision are now fixed. QSVT/matrix-function implementation is eligible; constructing the quotient projector and a hard family remain. |
| **T04** | **Accept scoped rejection.** | State that `G` is a degree-preserving chain endomorphism with the compatibility needed for the finite Lefschetz supertrace. Then heat evolution adds no information to the chain supertrace. This does not reject other torsion/refined invariants. |
| **T05** | **Accept scoped no-advantage disposition.** | It is the existing Koszul/Hodge problem plus Gibbs preparation and inherits its gap and harmonic-fraction failures. Its supersymmetric/Gibbs mechanism is novelty-eligible. |
| **T06** | **Accept stated-access rejection.** | With quotient projectors supplied, the stationary target is encoded in the jumps; without them the proposed detailed-balance proof is absent. Different local jump constructions remain open. |
| **T07** | **Accept matched-trajectory rejection.** | The rank-one Kraus channel is a classical Markov chain with exactly the same samples and mixing time. A coherent walk is a different eligible candidate, but is not this channel and still needs an advantage. |
| **T08** | **REPAIRED: reject explicit-matvec case; hold succinct case.** | Exact Hutchinson match holds for classically applicable matrix access. Succinct compiled channel access remains unresolved, without earning an advantage from generic simulation hardness. |
| **T09** | **HOLD only for coarse normalised profile.** | The absorption identity for each power is valid, but exact ranks need sub-`1/(2D)` error and order-`D^2` Bernoulli samples. Charge construction of `m_ell^k`, its normalisation and all `k<=r` gaps. |
| **T10** | **Accept no-advantage disposition as stated.** | Cold-bath harmonic/Jacobian selection is eligible, but no advantage is proved and this construction inherits the gap and overlap costs; it does not rule out a different critical-scheme observable. |
| **T11** | **Accept fold into repaired T03 for this scalar.** | Kubo/Laplace response is a Green operator; retaining signed amplitudes needs a coherent clock/dilation. A different nonlinear response remains open. |
| **T12** | **Accept no-advantage disposition for the displayed test.** | Choi-rank exterior power is eligible, but no separation from spectral/rank testing is proved. Keep `r+1` uses, elementary-symmetric signal, eigenvalue promise, and black-box process-query distinction explicit. |
| **T13** | **REPAIRED: reject matched no-reset case; hold general reset case.** | Principal angles govern the no-reset projector product. The full reset-channel spectrum is no longer claimed to obey that law. |
| **T14** | **Accept ordinary-Chern rejection.** | Preserve full rank and fixed global ambient frame. Uhlmann holonomy and modified thermal numbers are different outputs, not refuted. |
| **T15** | **HOLD as a problem source.** | Power iteration/trajectory Monte Carlo is matched only when the Kraus action is classically available. A succinct circuit still needs a natural geometric output and a true same-access advantage. |
| **T16** | **Accept generic-mechanism rejection.** | Pairwise gluing jumps that merely realize the Cech Hodge Laplacian inherit spectral gap and harmonic-weight costs. Additional geometric jumps outside that construction are not excluded. |

The table confirms the proposer's first cut only after revisions: T01 is the
strongest exact new identity, T03 is the strongest geometric target after its
definition is repaired, and T02 is a control.  T09 remains a coarse-output
instrument.  T01 and T03 earn continued construction seats under the clarified
novelty rule; neither yet earns a proved-advantage claim.

### 3.1 Repair review received during the critic turn

The proposer's live repair resolves the mathematical core of O1--O3 and the
scope of O5--O6 and O8:

- T01 now says explicitly that the bath's syzygies have zero weight and that
  absorption is a separate nullity estimator; its simulator error is budgeted
  as expectation bias rather than divided by the number of trials.
- T03 now fixes degree one, the plus sign, the quotient norm, a supplied
  projector `Pi`, two coherent branches, total scale
  `2 alpha_h alpha_mu^2`, and the exact regularisation error
  `2 alpha_mu^2 zeta/[sqrt(Delta_min)(Delta_min+zeta)]`.  Its separated
  Bernoulli intervals and conservative
  `O(beta^4 gamma^(-4)log(1/delta))` sampling bound are correct.  This
  earns **conditional compiled-primitive** status only: construction of `Pi`
  and an advantage are absent.  Its matrix-function/LCU mechanism is eligible
  under the clarified novelty rule.
- T08 and T15 now restrict their classical matvec claims, and T13 restricts the
  principal-angle law to the monitored no-reset branch.

O11 was subsequently fixed by defining the harmonic `P`, synchronising the T03
table, and declaring the local C7/C8 departures.  O4 remains a
research obligation, while the explicit family below gives a decisive negative
control rather than a general lower bound.  O7 is adequately scoped in the
detailed T02 derivation, although a final writeup should label the reset channel
and the conditioned holonomy as two linked constructions.

For the added family `I=(z_0^2,z_1^2)`, direct Fock calculation gives

`F_d F_d^dag|gamma>=[gamma_0(gamma_0-1)+gamma_1(gamma_1-1)]|gamma>`.       (10)

Thus `alpha_F^2=d(d-1)`, `eta=2/[d(d-1)]`,
`dim ker F_d=M_(d-4)`, and `L=2M_(d-2)`.  For `d~c n`, the kernel fraction
tends to `c^2/[2(c+1)^2]`.  At emitter level `N=d`,

`p_emit=||F_d||_F^2/[M_d d(d-1)]=4/[(n+1)(n+2)]`.                       (11)

The proposed classical live-bit sampler is exact.  In a fibre over `gamma`
there are `c_gamma` input columns, `c_gamma-1` dark eigenvectors, and one bright
eigenvalue `s_gamma/d(d-1)`.  Sampling a uniform column, choosing bright with
probability `1/c_gamma`, and retaining it with probability
`exp[-t s_gamma/d(d-1)]` reproduces the normalised trace contribution.  Hence
this non-squarefree family meets succinct indexing, polynomial gap and constant
syzygy-fraction tests while still having a direct classical sampler and a
closed Koszul kernel fraction.  It is strong negative evidence for T01, not a
universal dequantisation theorem.

## 4. Audit of the root portfolio

| ID | Independent disposition | Surviving scope / missing completion |
|---|---|---|
| **R01** | **ACCEPT exact conservation control.** | Channels generated inside the unital star algebra of `d,d^dag` conserve harmonic population. Additional jumps with cross block `PJ(1-P)!=0` are outside the theorem and are the constructive escape. |
| **R02** | **ACCEPT finite dual-number calculation; HOLD algorithm.** | Optimal global scaling, identical-input ceiling and dagger-Frobenius failure are exact. No growing output, recursion law, or advantage is supplied. |
| **R03** | **ACCEPT displayed cancellation only.** | The Born-weighted instrument loses inverse denominators and the rejection repair pays the minimum denominator. Other coherent reweighting/matrix-scaling operations remain open. |
| **R04** | **ADVANCE as the strongest construction question, not a result.** | Need a finite positive-Hilbert CE/coderivation scattering instrument with exact signed quotient output, evolution/leakage/precision, and a comparator to homotopy-transfer tree recursion. |
| **R05** | **ACCEPT scoped ordinary-Chern obstruction.** | Full-rank fixed-ambient Uhlmann bundle is trivial; holonomy, rank-deficient support bundles, and modified thermal invariants remain. |
| **R06** | **ACCEPT peripheral-Jordan exclusion.** | Finite CPTP maps have semisimple unit-circle spectrum. Interior transients and succinct-channel complexity remain open. |
| **R07** | **HOLD undeveloped.** | A derived equivalence is not a metric isometry; supply one surface kernel, exact CP/coherent output, normalisation and direct classical contraction. |
| **R08** | **HOLD undeveloped.** | Signed heat-trace cancellation needs an exact finite output, small-eigenvalue/truncation bounds and comparison to stochastic log-determinant/trace methods. |

No root control overclaims a universal impossibility in its detailed prose.  The
merge proposals should retain O10's hypotheses verbatim.  A checker extension
for an unmerged CE scattering example is evidence about that finite example,
not a substitute for adding its definitions, output and proof to a reviewed
artifact.

## 5. Finite verification

An independent bounded in-memory calculation checked the thermal identities,
without importing the supplied checker:

- 18 random complex Fock cases (`n=1,2`, `d=1,2,3`, `N=d,d+1,d+3`) verified
  `(1)--(3)` below `1e-9`, using annihilators assembled directly from occupation
  coefficients;
- the reset Kraus completeness relation was checked at `(D,r)=(7,3)`;
- (9) was checked on logarithmic spectral grids for three gaps and three
  `zeta/Delta` ratios.

The supplied checker was then run with `timeout 60`; it reported `PASS: 289
finite checks`.  Its six mutations test harmonic-projector choice, fusion
normalisation, Born weighting, absorbing boundary, and two signs/weights in a
new finite CE toy.  All six mutations were run separately under an outer
`timeout 180`; each exited one, so the red paths are active.  Those runs support
only their small matrices.  In particular,
it does not check T01's Fock/binomial Gram, T02's convergence rate, T03's
indeterminacy quotient, any asymptotic cost, or novelty.

## 6. Targeted primary-source comparison

- Burgarth--Facchi--Giovannetti--Nakazato--Pascazio--Yuasa,
  [arXiv:1305.6433](https://arxiv.org/abs/1305.6433), explicitly connects
  repeated projections with non-Abelian adiabatic/Zeno phases.
  Burgarth--Facchi--Nakazato--Pascazio--Yuasa,
  [arXiv:1809.09570](https://arxiv.org/abs/1809.09570), extends Zeno dynamics to
  general quantum operations.  These are substantive operation-level prior art
  for T02.
- Gilyen--Su--Low--Wiebe,
  [arXiv:1806.01838](https://arxiv.org/abs/1806.01838), supplies the
  singular-value/matrix-function and pseudoinverse machinery covering T03's
  compiled Green map.  The reduction is to the actual resolvent step, not merely
  to universal gates.
- Hallman--Troester,
  [arXiv:2103.10516](https://arxiv.org/abs/2103.10516), gives matrix-free
  stochastic trace estimation for analytic matrix functions using Hutchinson,
  Chebyshev and multilevel Monte Carlo.  It is a direct classical comparator for
  T01 under classical matvec access, with no implication for a circuit-only
  oracle.
- Vicary,
  [arXiv:0805.0432](https://arxiv.org/abs/0805.0432), establishes the stated
  correspondence between finite-dimensional C*-algebras and the relevant
  dagger-Frobenius monoids.  This supports R02 only with the hypotheses in O10.
- He--Guo--Chien,
  [DOI 10.1103/PhysRevB.97.235141](https://doi.org/10.1103/PhysRevB.97.235141),
  states that the global section makes the ordinary Uhlmann Chern character
  vanish and introduces modified thermal quantities.  This matches R05's
  distinction exactly.
- Wolf--Perez-Garcia,
  [arXiv:1005.4545](https://arxiv.org/abs/1005.4545), treats quantum-channel
  spectra and the peripheral eigensystem.  R06's simpler power-boundedness proof
  independently establishes the no-Jordan statement used here.
- Verstraete--Wolf--Cirac,
  [arXiv:0803.1447](https://arxiv.org/abs/0803.1447), proves that local
  Markovian dissipation can implement universal computation and state
  preparation.  Thus dissipative realization is eligible but proves neither an
  advantage nor classical simulability for T01/R04/R08.
- Arvanitakis--Hohm--Hull--Lekeu,
  [arXiv:2007.07942](https://arxiv.org/abs/2007.07942), formulates homotopy
  transfer through nilpotent coderivations and tree-level effective-field-theory
  elimination.  Bonezzi--Chiaffrino--Diaz-Jaramillo--Hohm,
  [arXiv:2312.09306](https://arxiv.org/abs/2312.09306), identifies transferred
  higher brackets with tree-level scattering recursion.  These are the required
  exact operation/resource comparators for the proposed R04 continuation; they
  do not themselves give a finite quantum algorithm.

## 7. Re-ranking under the clarified novelty rule

1. **T01 / syzygy absorption plus QSVT:** first.  It has an exact algebraic
   output, easy maximally mixed input, a gap-controlled CP implementation, and
   a QSVT singular-value-threshold alternative.  QSVT now counts as new.  The
   `(z_0^2,z_1^2)` family proves that exponential ambient dimension, polynomial
   gap and constant nullity fraction can coexist, but its direct classical
   sampler proves no advantage on that family.  A hard family is the missing
   gate.
2. **T03 / degree-one triple-quotient response:** second.  The repaired problem
   and conditional two-branch circuit are exact.  QSVT may construct both the
   Green map and the quotient projector under additional singular gaps.  No
   natural surface/sheaf family with all gaps, polynomial signal and a same-
   access lower bound is supplied.
3. **R04/R09 / growing CE scattering:** third.  The finite cubic diagnostic now
   has a positive-Hilbert Hamiltonian and exact amplitude, but is a fixed
   four-state spin-`3/2` transfer with a constant classical formula.  Its
   supersymmetric/perfect-transfer mechanism remains novelty-eligible; a growing
   interacting family and advantage are absent.
4. **T02 / Kato-Zeno holonomy:** fourth.  Zeno transport is eligible, but the
   metric connection lacks a useful hard algebraic output and supplied projector
   access may dominate.
5. **R01 geometric-jump escape:** fifth.  The conservation theorem sharply
   states what a successful autonomous cohomology pump must add, but supplies no
   such jump family.

### 7.1 Concrete QSVT route for T01

Given a block encoding of `B=F_d/alpha_F`, singular-value thresholding at the
promise `sigma_min^+(B)>=sqrt(eta)` can approximate the projector onto
`ker B` with degree

`O(eta^(-1/2) log(1/epsilon_filter))`.                                (12)

A DQC1-style normalised trace measurement on the domain estimates
`dim ker F_d/L` with `O(epsilon^(-2)log(1/delta))` repetitions.  All block-
encoding, mixed-state, clean-ancilla and filter errors remain charged.  This can
improve the `eta^(-1)` physical time of literal absorption and is eligible under
the new rule.  Classical Chebyshev trace estimation has comparable polynomial
degree when it has the same classical matvec; its vectors have length `L`.
Thus the only possible exponential separation is a succinct-access one, and it
requires a lower bound rather than an array-storage comparison.

There is a direct hardness-transfer target.  For a sparse two-term cochain map
`A`, encode its columns as homogeneous degree-`d` forms and evaluate the
Macaulay map at its minimal degree, where every multiplier space is `R_0`.
Then `F_d=A` after padding the codomain to `M_d`.  Choosing `n=d=Theta(q)`
makes `M_d=binom(2q,q)` exponential while the degree remains unary-polynomial.
This embeds succinct sparse matrix nullity into tuple syzygies.  It is not yet
a theorem of advantage: one must start from a proved DQC1/BQP-hard gapped
cohomology/nullity family, preserve row/column oracle cost and normalised gap,
and justify exponentially many generator labels as a legitimate succinct
algebraic input.  The DQC1-hard theorem of
[Cade--Crichigno, arXiv:2107.00011](https://arxiv.org/abs/2107.00011) is for quasi-Betti/
low-lying spectral density without the inverse-polynomial zero gap needed here;
their paper explicitly leaves hardness of true normalised Betti estimation under
that gap open.  It therefore cannot fill this obligation.  At present the
embedding is the strongest precise next reduction, not a concrete hard family.

### 7.2 End-to-end QSVT route for T03

The supplied `Pi` can be removed as an oracle under additional promises.  Let
`P_1,P_2` be Hodge projectors built by QSVT from the degree-one and degree-two
Laplacians.  Define the indeterminacy map

`M_ind=(P_2 L_a P_1, P_2 R_c P_1):H^1 direct-sum H^1 -> H^2`.          (13)

If its least nonzero singular value after normalisation is at least `xi`, a
second singular-value threshold constructs the range projector `P_ind`, and
on harmonic degree two

`Pi=P_2-P_ind`.                                                        (14)

Equations (13)--(14), combined with the repaired Green branches, give a fully
specified nested-QSVT algorithm.  Its cost depends polynomially on
`Delta_min^(-1/2)`, `xi^(-1)`, the multiplication/block normalisations,
`gamma^(-1)`, and logarithmic precision factors; direct Bernoulli readout in
the current repair is conservatively quartic in the inverse probability gap.
The classical comparator performs the same Hodge solves and an indeterminacy
least-squares/range computation.  A true advantage still needs a succinct
natural DGA family preserving both gaps and a classical lower bound.  Supplying
`Pi` remains a valid conditional primitive but cannot support the end-to-end
claim.

## 8. Final integration verdict

The repair conditions O1--O3, O5--O8 and O11 are satisfied in the current
thermal memo and `definitions/thermal-cp-r11.md`.  O4 is now sharpened by the
complete non-squarefree control, which is negative rather than hard.  O9 names
open constructions and does not block the scoped portfolio.  O10's hypotheses
are carried by the canonical finite-complex/channel definitions.

Claims C-365--C-371 and C-373 are mathematically consistent with the canonical
definitions and the independently derived scopes above at **SKETCH**.  C-372's
finite CE identities also check at SKETCH: `Q_g^2=0`, the weight-three chain,
cubic elimination, amplitude, `g^(-2)` small-coupling time and exact resonance
are correct.  Its statement must be read as a fixed diagnostic, not a growing
advantage.  The available checker passed 289 checks and all six mutations went
red; claim status still rests on the analytic arguments, not those finite runs.

The claims' north-star annotations and the older proposer language that say a
known non-Grover operation “rejects novelty” are stale under the user's clarified
rule.  They should instead say that T01, T03 and CE scattering are
**novelty-eligible but have no proved same-access advantage**.  C-371 and C-373
remain negative for their exact matched families.  No PROVED promotion is
recommended from this turn; the converged verdict supports the registered
SKETCH controls.

The next work should pursue T01's gapped cohomology-to-minimal-degree-syzygy
hardness transfer first, then T03's constructed indeterminacy projector.  The
global research goal remains active.
