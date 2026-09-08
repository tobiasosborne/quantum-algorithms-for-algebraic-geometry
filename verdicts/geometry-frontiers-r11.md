# Independent verdict: geometry frontiers R11

2026-09-07. Reviewer: Sol, independent of the geometry proposer. Scope:
`scouting/geometry-frontiers-r11.md` and the later finite diagnostic
`scouting/ce-scattering-r11.md`. This verdict assigns no canonical claim status.

**Steering update, later 2026-09-07.** The user has narrowed the mechanism
exclusion: QSVT, supersymmetric, CP, dissipative, adiabatic, BosonSampling and
other mechanisms are eligible unless they are QFT, Grover or DQI in disguise;
adiabatic Feynman--Kitaev encodings of those excluded algorithms remain
ineligible. Section 8 is the controlling re-review under that rule. Earlier
sentences which reject a candidate merely because its operation was previously
known are superseded. The mathematical, access and same-output classical
objections remain in force.

**VERDICT: FAIL as a north-star portfolio; PASS the scoped finite identities
listed in section 7 subject to the stated wording.** None of G01--G17 currently
meets PRD criteria 1--6. G08 remains the strongest unresolved problem target,
but its written LCU is an exponentially normalised implementation of a
polynomial classical recurrence, and no compiled natural family is supplied.
The CE four-state continuation is mathematically correct and experimentally
clean; at its unit-success resonance it is exactly a known perfect-transfer
spin chain and has no asymptotic problem. G06 and G15 also contain correct
finite mathematics, with decisive same-output and prior-operation attacks.

The review found no fatal falsehood in the three finalist derivations. It found
two material input/output defects, two scope defects in eliminated candidates,
and several claims which must stay conditional. Every objection below includes
the required repair and the statement that survives it.

## 1. Candidate-by-candidate audit

| objection | severity and candidate | finding | FIX DEMAND | SURVIVING STATEMENT |
|---|---|---|---|---|
| O1 | MAJOR, G01 | The reduction to sparse Hodge-Laplacian nullity estimation is sound. The displayed polynomial cost is only schematic and must include maximally-mixed/block-state preparation, block-encoding normalisation and the positive gap. | Replace `poly(...)` by a declared access theorem or leave the row explicitly qualitative. Do not infer a domain-wide impossibility for Čech methods. | This particular supplied-complex construction is eligible under the later mechanism rule, but no same-input advantage is proved. |
| O2 | MAJOR, G02 | A finite discretisation does not exactly output algebraic Hodge numbers merely from a mesh-error symbol. One needs a certified discretisation theorem separating true zero modes from spurious near-zero modes. The novelty rejection remains valid even if that promise is granted. | State the certification oracle/theorem and both analytic and discrete gaps, or call the output the discretised nullity distribution. | Generic cooling/filtering of a supplied Dolbeault matrix is prior spectral estimation; this does not reject every quantum approach to Hodge diamonds. |
| O3 | MINOR, G03 | The cup evaluation and its classical local contraction are correctly matched. A prior cup-gate construction identifies the operation, but does not disqualify it under the later steering and does not cover every sheaf/Dolbeault observable. | Scope the rejection to the supplied local DGA/cellular tensor and exact scalar. | The listed circuit has no speedup over direct sparse cup evaluation. |
| O4 | MAJOR, G04 | The row correctly notices that a supplied quotient projector contains the hard indeterminacy calculation. With only `u,v` supplied, the representative depends on choices; without a projector onto cohomology modulo `aH+Hc`, the promised distance is not defined operationally. | Define the Hermitian quotient, gauge, indeterminacy projector construction and access cost. Separate a supplied-projector problem from an equation-input problem. | A quotient-aware Massey-distance problem is meaningful, but no noncircular algorithm is given. |
| O5 | MINOR, G05 | The derived-intersection output is exactly a harmonic-degree distribution of a supplied resolution. The sparse-rank attack and the gap, truncation and harmonic-weight costs are substantive; the Laplacian/Koszul mechanism itself is now eligible. | Retain only the absent-advantage conclusion; do not extend it to all Tor problems or all resolutions. | G05 is an eligible supersymmetric/QSVT route, but no family beats its same-input classical baseline. |
| O6 | MAJOR, G06 | The first-loss identities are correct, but the title's word “recover” overstates a TV-approximate sample. Exact integer Jordan strings require resolution on a `1/D` lattice and worst-case order `D^2` samples by this histogram route. The intrinsic monomial successor access also gives an identical classical path sampler. | Change the primary output to the death-time distribution at stated TV error. State exact profile recovery only with its precision/sample cost. | Equations (1)--(5) are valid; for monomial quotients the law is the conjugate Jordan partition divided by `D`, and the same-access classical sampler exactly matches it. |
| O7 | MAJOR, G07 | Nested projector measurements telescope correctly because the projectors commute, but circuits for all `P_k` already encode the row spaces of the powers. | Give a construction of `P_k` from equation or multiplication access without rank elimination, or retain the circular-access rejection. | Given the projectors, the layer law is exact and classically matched by trace probes. |
| O8 | FATAL to the current advantage claim, G08 | “A unit `a`” does not specify common access. A source of copies of an unknown quantum state and a classical coordinate vector/preparation circuit lead to different problems. The classical `O(m^2)` recurrence is valid for explicit vectors, while no free classical coefficients may be granted in a state-only model. | Define two problems: (A) explicit/sparse coefficient access to `a` and all maps, with vector recurrence baseline; (B) a supplied preparation unitary for `|a>` and compiled coherent maps, with a classical circuit/query comparator and source-copy accounting. Do not mix their bounds. | The recurrence and tree map are algebraically valid in either representation once the access model is fixed; no advantage follows yet in either. |
| O9 | MAJOR, G08 | The LCU cost omits PREPARE/SELECT for the Catalan tree distribution. A succinct tree ranking/unranking circuit may be polynomial in `m`, but it is not supplied. Replacing the safe `Lambda_m` by `||A_m||` would in turn hide compilation of the summed map. | Supply a reversible Catalan-tree PREPARE and a uniform controlled evaluator with gate/workspace bounds, or hold the LCU gate complexity. Keep every local block normalisation and flag. | Conditional on these circuits, the successful Kraus block is `A_m/Lambda_m` and its probability is the stated squared norm ratio. |
| O10 | MAJOR, G09 | The K3 lattice has indefinite intersection form. A bound on self-intersection does not define a finite set: there are infinitely many integral vectors of bounded indefinite norm. A positive Euclidean height in a fixed marking is finite but basis dependent. | Replace “norm” with an explicit positive-definite height in the marked coordinates, state primitivity and encoding, and update the candidate count. | With coordinate height `||v||_2<=B` in rank 22, enumeration is finite of order at most `B^22`; the proposed quantum wrapper is still Grover-style and fails D22. |
| O11 | MINOR, G10 | The spectral-inertia reduction is correct. For a smooth projective surface, Hodge theory already determines `b_2^+=1+2h^{2,0}` and `b_2^-=h^{1,1}-1`, so the proposed output may be input-level once the Hodge diamond is supplied. | State whether the input supplies Hodge numbers or only a chain/cup model. | Under the latter model it is generic spectral density; no D22 mechanism survives. |
| O12 | MINOR, G11 | The Heisenberg-correspondence map and partition-DP comparator are correctly identified. | Keep the rejection scoped to these established ladder maps and stated fixed-point output. | No D22 claim survives for G11 as written. |
| O13 | MAJOR, G12 | “Pull--tensor--push maps” and a normalised hypercohomology state do not specify a single TP instrument; arbitrary derived equivalence need not preserve the chosen metrics, and every dilation factor can dominate. | Give one metric-explicit finite kernel, Kraus completion, success law and same scalar classical contraction before retaining this as a candidate. | Fourier--Mukai problems remain open; the listed three-stage sketch establishes no algorithm. |
| O14 | MAJOR, G13 | A symplectic transvection on a stored vector in `(Z/M)^r` is an ordinary reversible modular linear permutation. A metaplectic/Clifford representation instead acts on a phase-space Hilbert space of a different dimension. The row conflates these encodings, and “normalised fixed-space dimension” is ambiguous: a maximally mixed return of the permutation measures `|ker(T-I)|/M^r`, not `dim ker(T-I)/r`. | Specify the register and output. For the stated charge-vector register, compile reversible modular transvections and call the return output the fixed-vector fraction. | Matrix multiplication and kernel computation are polynomial in `L,r,log M`; the rejection remains, more directly than by stabilizer simulation. |
| O15 | MINOR, G14 | Given the entire candidate-curve intersection table, active-set linear algebra is a valid polynomial attack. Omitting the list hides curve enumeration. | Preserve that input distinction. | The written problem has no speedup or D22 mechanism; other surface cone-enumeration problems are not excluded. |
| O16 | FATAL to factor recovery, G15 | Charge probabilities from `A|0>` do not identify the complex coefficient vector, much less a chamber factorisation. Even full truncated coefficients require ray order, support, integrality and a no-aliasing specialisation before recursive factor recovery is defined. | Split the output into (i) finite charge sampling, (ii) normalised complex-amplitude estimation, and (iii) DT-factor recovery. Give a uniqueness theorem and enough coherent queries for (iii). | Equations (15)--(22) define a valid finite quantum-torus scattering distribution; that distribution alone is not a DT-invariant recovery algorithm. |
| O17 | MAJOR, G16 | Agreement on numerical K-theory removes the only specified canonical finite output. Object-level cone states depend on resolutions, quasi-isomorphism handling and selected metrics; “squared distance” is not a derived invariant as written. | Define a presentation-independent observable or an explicit metric/presentation problem, and charge cone normalisation and normal-form access. | The spherical-twist domain remains open, but G16 currently has no exact common problem. |
| O18 | MINOR, G17 | With graded bases and multiplication tensors supplied, forward multiplication and relation testing have direct tensor contractions; with only equations supplied, basis construction is hidden. | Keep these access cases separate. | The displayed multiplication transducer fails D22 and proves no domain-wide negative about canonical rings. |

The elimination table therefore survives after the repairs, but G02, G09, G13
and G16 require wording corrections for mathematical/input precision. None of
those corrections promotes a candidate.

## 2. Independent derivation of G06

Let a string have orthonormal basis `e_0,...,e_(lambda-1)` and let
`S e_i=e_(i+1)` for `i<lambda-1`, `S e_(lambda-1)=0`. Complete it with
`E e_(lambda-1)=|lambda,string>` and `E e_i=0` otherwise. Then

`S^dag S+E^dag E=I`,

so the flagged map is an isometry. A starting basis element `e_i` first emits
at time `lambda-i`. Therefore each string of length `lambda` contributes one
initial basis element to every time bin `1,...,lambda`. If
`c_t=#{strings:lambda>=t}` and `D=sum lambda`, then

`Pr(tau=t)=c_t/D`,
`Pr(tau>k)=sum_strings max(lambda-k,0)/D=rank(S^k)/D`.                  (1)

For a general contraction `T`, use defect `E=(I-T^dag T)^(1/2)`. The
probability of surviving the first `t-1` calls and emitting at call `t` is

`Tr[(T^(t-1))^dag E^dag E T^(t-1)]/D`
` = (||T^(t-1)||_F^2-||T^t||_F^2)/D`.                                (2)

Equation (2) depends on singular values of powers, hence on the metric and
similarity representative; it is not a Jordan invariant. The monomial partial
shift makes it a Jordan statistic precisely because all surviving edges are
unit partial-isometry edges. That same structure makes the trajectory
classically sampleable from the promised uniform standard-monomial sampler.

**Disposition G06: ACCEPT equations (1)--(5) after O6's output wording; REJECT
advantage.** Its monitored CP mechanism is eligible under the later rule. It
ranks below G08 because no unresolved quantum-specific
operation remains in its declared intrinsic access model.

## 3. Independent derivation and scope of G08

From `ip=I-dh-hd`, Kuranishi gauge and the Maurer--Cartan equation, the fixed
point equation

`x=t i(a)-(1/2)h[x,x]`, `kappa=(1/2)p[x,x]`                            (3)

gives, coefficient by coefficient,

`x_1=i(a)`,
`x_n=-(1/2)h sum_(r=1)^(n-1)[x_r,x_(n-r)]`,
`kappa_n=(1/2)p sum_(r=1)^(n-1)[x_r,x_(n-r)]`.                         (4)

This is a dynamic program with `sum_(n=2)^m(n-1)=m(m-1)/2` ordered bracket
calls before symmetry savings, plus the homotopy and projection calls. It does
not enumerate trees.

Fully expanding (4), an `m`-leaf planar binary tree has `m-1` brackets,
`m-2` nonroot homotopies, `m` inclusions and one root projection. Its coefficient
has magnitude `2^(-(m-1))`. There are `Cat_(m-1)` trees. Thus the proposer's
safe triangle-inequality scale

`Lambda_m=Cat_(m-1) P beta^(m-1) H^(m-2) I^m/2^(m-1)`                 (5)

is valid once the named operator norm bounds and tree-control circuits are
supplied. With successful block `A_m/Lambda_m`, one attempt on `a^tensor m`
has probability

`p_m=||kappa_m(a)||^2/Lambda_m^2`;                                    (6)

one-sided repetition under `0` versus norm at least `gamma` uses
`ceil(Lambda_m^2 gamma^-2 log(1/delta))` attempts and `m` times as many source
states. Since `Cat_(m-1)/2^(m-1)=Theta(2^m/m^(3/2))`, unit local norms do not
give polynomial success. Equations (3)--(6) pass.

The surface scope also needs a precise positive and a precise exclusion.
[Vakil's Murphy-law theorem](https://arxiv.org/abs/math/0411469) does support
arbitrary finite-type singularities, up to smooth parameters, on moduli of
smooth projective general-type surfaces and on stable-sheaf moduli. Hence the
existence of arbitrarily high first nonzero Kuranishi order in the broad
general-type domain is not refuted by a smoothness theorem. It supplies no
uniformly constructible dg Lie contraction, state circuit, gap, norm or hard
family.

K3 substitutions are much narrower. [Budur--Zhang,
arXiv:1803.03974](https://arxiv.org/abs/1803.03974) prove formality of
`RHom(F,F)` for polystable sheaves on a complex projective K3 surface (and for
specified Bridgeland-polystable objects). [Bandiera--Manetti--Meazzini,
arXiv:1902.06486](https://arxiv.org/abs/1902.06486) relate formality and
quadraticity of the Kuranishi family for polystable coherent sheaves on smooth
projective surfaces. Therefore the proposed high-order family must stay with
Vakil's general-type examples or another explicitly nonformal class. A K3
polystable-sheaf example cannot be substituted merely because K3 is a complex
surface.

**Disposition G08: FAIL pending O8--O9.** Retain KURANISHI-ORDER as a problem
definition only after splitting explicit-vector and preparation-circuit input
models. Retain the recurrence theorem and conditional LCU law. No quantum
advantage, natural compiled family, hardware score, dequantisation result or
D22 mechanism is established.

## 4. Independent derivation of G15

For odd `M`, define

`W_gamma|eta>=omega^(<gamma,eta>/2)|eta+gamma>`.

Skewness gives `<gamma,gamma>=0`, and direct composition gives

`W_alpha W_beta=omega^(<alpha,beta>/2)W_(alpha+beta)`.                 (7)

For `A=A_L...A_1`, expand `A_j=sum_(k=0)^K c_(j,k)W_(gamma_j)^k`.
At stage `j`, the accumulated charge is `sum_(i<j)k_i gamma_i`; therefore a
history has phase

`omega^[(1/2)sum_(i<j)k_i k_j<gamma_j,gamma_i>]`.                     (8)

Summing histories of total charge `eta` proves equation (20). The recurrence
(22) is the same expansion grouped by partial charge and costs
`O(L K R_ch)` arithmetic operations and `O(R_ch)` words. These finite-algebra
identities pass.

Let `A_norm=product_j alpha_j`. An LCU unitary supplies matrix element
`a_eta/A_norm`, not `a_eta`. Direct Hadamard sampling estimates this normalised
complex amplitude to error `zeta` in `O(zeta^-2 log(1/delta))` trials. Therefore
estimating the unnormalised `a_eta` to additive `epsilon` by direct sampling
costs

`O(A_norm^2 epsilon^-2 log(1/delta))`,                                (9)

regardless of a lower bound on total success. Conditional preparation under
`p_wall=||A|0>||^2/A_norm^2>=gamma` supports charge samples or amplitudes
normalised by `||A|0>||`, at `O(gamma^-1)` attempts per accepted state. These
are different outputs and must not share one resource line.

The finite root-of-unity operation is a diagnostic, not automatically the
formal motivic quantum torus. [Kontsevich--Soibelman,
arXiv:0811.2435](https://arxiv.org/abs/0811.2435) puts motivic DT wall crossing
in a quantum torus, while [Faddeev--Kashaev,
arXiv:hep-th/9310070](https://arxiv.org/abs/hep-th/9310070) already constructs
finite-dimensional quantum-dilogarithm/pentagon identities. Thus the prior
operation reduction is substantive. A no-wrap bound protects the chosen
finite polynomial computation but is not a specialisation theorem for DT
invariants.

**Disposition G15: ACCEPT the finite scattering and DP identities and, under
the later steering, mechanism eligibility; REJECT DT factor recovery, the
shared sample/amplitude complexity line and advantage.** It ranks third because
the DP comparator and missing specialisation are more decisive than historical
priority of the physical operation.

## 5. Separate review of CE scattering R09

The canonical definitions give

`Q_g=c_v^dag(a_u+g a_x^2/sqrt(6))+g c_w^dag a_x a_u`.

The bosonic polynomials commute and the fermionic creators anticommute, so the
two cross terms cancel and repeated-creator terms vanish: `Q_g^2=0`. On weight
three, occupation-number factors give

`Q_g e_0=g e_1`, `Q_g e_2=e_1+g e_3`,                                (10)

and zero on the odd states. Hence `H_g=Q_g+Q_g^dag` is exactly the four-site
chain with couplings `(g,1,g)`. The algebraic relations eliminate `U` to
`X^3=0` for every `g>0`, so the associated affine scheme is a length-three fat
point; `g=0` is correctly excluded from that statement.

Parity reduction of the chain gives the two `2x2` blocks with diagonal entries
`+1` and `-1`, and direct exponentiation yields

`<e_3|exp(-itH_g)|e_0>`
` = i[cos(t/2)sin(Omega t/2)/Omega-sin(t/2)cos(Omega t/2)]`,
`Omega=sqrt(1+4g^2)`.                                                  (11)

Its Taylor coefficient is `i g^2t^3/6`. Its slow frequency is
`(Omega-1)/2=g^2+O(g^4)`, so a fixed nonzero endpoint probability requires
time `Omega(g^-2)` as `g->0`; the fast component has only `O(g^2)` amplitude.
At `g=sqrt(3)/2`, `Omega=2` and `t=pi`, (11) equals `i`. The chain couplings
are exactly those of spin `3/2` `J_x`, so this is the perfect-state-transfer
rotation already covered by [Christandl--Datta--Ekert--Landahl,
quant-ph/0309131](https://arxiv.org/abs/quant-ph/0309131).

The claimed fixed identities also passed the available checker:
`PYTHONDONTWRITEBYTECODE=1 timeout 30s python3
checkers/explore/cp_geometry_r11.py` returned 289 checks, and all six mutations
(`harmonic-projector`, `fusion-normalization`, `born-weight`,
`absorbing-boundary`, `ce-merge-weight`, `ce-fermion-sign`) returned red.

**CE exact-statement approval.** Approve for later canonical registration the
scoped statements that the displayed `Q_g` squares to zero, its weight-three
restriction is (10), elimination gives `C[X]/(X^3)` for `g>0`, the endpoint
amplitude is (11), small-coupling constant transfer takes order `g^-2`, and the
listed resonance has unit success. Keep the energy scale, four-state input and
fixed common scalar in every statement.

**CE algorithmic disposition.** The supersymmetric scattering/PST mechanism is
eligible under the later steering, but there is no speedup for this family. It
is a constant-size chain with a constant-time classical formula. This does not
refute a growing CE/coderivation construction. For the
suggested irreversible jump
`J=sum mu^k_(ij)a_k^dag a_i a_j`, the conditional `m-1`-jump history includes
the ordered no-jump factors `exp[-Delta t J^dag J/2]`. They are not scalar on
particle sectors in general, so they reweight tree histories; resolving bath
labels can also reveal the merge order and destroy interference. A constructive
escape must neutralise these factors by a proved sectorwise identity or use a
coherent finite Hamiltonian whose exact scattering block equals the transferred
higher bracket. It must then beat the classical homotopy-transfer recurrence,
whose field-theory relationship is explicit in
[arXiv:2007.07942](https://arxiv.org/abs/2007.07942) and
[arXiv:2312.09306](https://arxiv.org/abs/2312.09306).

## 6. Ranking after direct attacks

| rank | candidate | exact content retained | decisive missing gate |
|---|---|---|---|
| 1 | G08 Kuranishi order / growing CE continuation | intrinsic changing-representative recurrence; conditional tree Kraus map; real high-order general-type existence | separate access models, tree compiler, natural compiled family, polynomial signal, lower bound against recurrence, and operation beyond generic LCU/scattering |
| 2 | G06 first loss | exact Jordan law for monomial partial shifts and exact Frobenius telescope generally | identical classical trajectory in invariant access; exact readout cost; no new mechanism |
| 3 | G15 finite wall scattering | exact finite Weyl phases, amplitude recurrence and LCU charge law | finite-to-motivic theorem, identifiable output, amplitude cost, classical lower bound, and known quantum-dilogarithm reduction |
| 4 | CE four-state diagnostic | exact cubic fat point, supercharge, amplitude and unit resonance | fixed size and exact spin-chain/PST reduction |

No row earns quantum-advantage or dequantisation credit. Mechanism eligibility
is reassessed in section 8; it is no longer withheld merely for known QSVT,
supersymmetric, CP, adiabatic or scattering processing.
G08 earns only a well-defined AG problem and an explicit classical baseline once
O8 is repaired. G06 and G15 likewise retain exact problems/baselines, not an
advantage. The remaining candidates are properly eliminated as their particular
constructions, subject to O1--O5 and O10--O18; their broader domains remain open.

## 7. Merge-safe statements and repair order

The following statements are safe to merge after adopting the exact scoping in
this verdict:

1. **G06 mathematics:** equations (1)--(2), the same-access classical sampler,
   and noninvariance of the general contraction law under similarity. Call the
   primary output a death-time distribution, not exact recovery.
2. **G08 mathematics:** recurrence (4), the Catalan tree count, safe scale (5),
   success law (6), and `O(m^2)` explicit-vector recurrence. Attach no advantage
   or D22 status and hold the gate bound until PREPARE/SELECT is specified.
3. **G15 mathematics:** finite Weyl relation (7), history phase (8), recurrence
   and charge-sampling success. Split unnormalised amplitude cost according to
   (9); attach no DT-specialisation, factor-recovery, advantage or D22 status.
4. **CE diagnostic:** the exact statements approved in section 5, together
   with the explicit perfect-state-transfer reduction and algorithmic rejection.

Repair order is O8, O9, O16, O10 and O14 first; these change problem/access
definitions or resource claims. O2, O4, O6, O7, O13, O17 and O18 then sharpen
scope. The other objections are wording constraints. After repair, the
portfolio is valuable scouting with correct bounded constructions, but its
north-star verdict remains FAIL.

## 8. Re-review under the narrowed mechanism exclusion

### 8.1 Repair acceptance and canonical rows

The proposer has repaired the five priority objections correctly.

- **O8 accepted.** G08 now distinguishes explicit/sparse vector Model A from
  preparation-unitary/compiled-map Model B, gives the classical side the same
  circuit or query description, charges `m` source preparations per attempt,
  and leaves an unknown-copy Model C unclaimed.
- **O9 accepted.** `C_tree(m,epsilon)` and `C_select(m,epsilon)` are now named
  per-attempt costs, and the memo states that no uniform polynomial compiler
  has been proved. The local `O(Rm)` call count is no longer presented as an
  end-to-end gate bound.
- **O16 accepted.** Conditional charge sampling and unnormalised complex
  amplitude estimation have separate resource formulas. In particular the
  latter pays `(product_j alpha_j)^2/epsilon^2` under direct sampling.
- **O10 and O14 accepted.** G09 now uses the finite positive marked-coordinate
  height `max_j|v_j|<=B`. G13 now uses reversible modular linear permutations
  and outputs the fixed-vector fraction `M^(k-r)`, rather than conflating this
  with a Clifford action or normalised nullity.

The appended scope-repair section also adopts O1--O7, O11, O13, O15, O17 and
O18 at the level appropriate to scouting. O2's certified analytic
discretisation and O4's noncircular quotient construction remain open
obligations rather than errors in the repaired memo.

**C-371 integration verdict: APPROVE AS SKETCH.** The canonical text matches
D-R11-MONOMIAL-FIRST-LOSS and equations (1)--(2): it states the timestamp law,
the identical same-access classical sampler, and the metric dependence of a
general contraction. It does not assert exact profile recovery or a speedup.

**C-372 integration verdict: APPROVE AS SKETCH.** The canonical text retains
`g>0` for the cubic scheme, the exact weight-three chain and amplitude, the
fixed-middle-coupling `Omega(g^-2)` time statement, the resonant unit transfer,
and the fixed-size classical/PST comparison. The checker evidence remains 289
green checks with all six named mutations red.

### 8.2 Eligibility changes

The earlier “known operation implies D22 failure” test is withdrawn. Under the
user's controlling rule:

- G01, G02, G05 and G10 are eligible spectral/QSVT or supersymmetric
  mechanisms. Their current rows still lack a family and resource comparison
  beating sparse stochastic spectral methods.
- G03, G06, G07, G08, G11--G13, G15--G17 and the CE diagnostic use eligible
  CP, coherent tensor, bosonic, wall-scattering or modular mechanisms. Their
  direct classical matches, circular inputs, missing outputs or normalisation
  costs still prevent an advantage.
- G09 remains ineligible because its only algorithmic saving is Grover-style
  search over marked lattice vectors. A materially different Noether--Lefschetz
  operation could re-enter.
- G14 implemented by a quantum linear solver is eligible in principle, but
  outputting the full support costs `Omega(R)` and explicit active-set linear
  algebra is polynomial, so its current construction has no speedup.

Thus known QSVT or supersymmetry is no longer an objection. The portfolio still
has no complete advantage because the same-input classical gate is independent
of the originality rule.

### 8.3 Revised ranking of the existing portfolio

| rank | candidate | reason after steering | exact next gate |
|---|---|---|---|
| 1 | **G01/G05 squarefree supersymmetric syzygies** | On a squarefree multidegree, Hochster identifies the Koszul harmonic space with clique homology, while QSVT and CP absorption are eligible. This has the cleanest route to a large succinct block and a normalised invariant. | Exhibit a natural dense graph family with inverse-polynomial clique-preparation weight, Hodge gap and nontrivial resolvable Betti fraction for which the best same-input classical estimator is superpolynomial. |
| 2 | **G08 Kuranishi/CE transfer** | The intrinsic obstruction recurrence is a stronger AG output than nullity, and coherent tree or CE processing is eligible. | Construct Catalan control or an exact growing positive-Hilbert CE block with polynomial signal, then beat the `O(m^2)` recurrence in Model B. |
| 3 | **G15 DT charge scattering** | Finite quantum-torus scattering is eligible and may have a sign/interference advantage at variable charge rank. | Prove the root-of-unity DT specialisation, an identifiable output, inverse-polynomial success and hardness against the reachable-charge recurrence. |
| 4 | **G06 first loss** | The CP trajectory is exact and eligible. | Escape the identical classical successor sampler without hiding a Jordan basis. |
| 5 | **CE cubic diagnostic** | Exact SUSY chain and direct experiment. | A growing family; the fixed model is classically constant size. |

For G01/G05, the exact AG dictionary is worth recording. If `G` has `v`
vertices, let

`I_G=(z_i z_j : {i,j} is a nonedge of G)`.

This is the Stanley--Reisner ideal of the clique complex. Hochster gives

`beta_(v-k-1,[v])(R/I_G)=dim H_tilde_k(Cl(G);C)`.                     (12)

Hence estimating the `k`th normalised clique Betti number is literally a
multigraded syzygy problem for a quadratic squarefree monomial ideal. Direct
access to this one squarefree sector avoids the total-degree non-squarefree
gap and the quotient-state `h_N/M_N` cost. Under clique-density and Hodge-gap
promises, QSVT or no-jump absorption estimates the harmonic fraction in
polynomial quantum time. The strongest current classical path-integral bound
quoted in the audited Koszul memo is
`v^{O(gamma^(-1/2) log(1/epsilon))}`; it is polynomial at constant gap and
constant error, and quasipolynomial at constant gap and inverse-polynomial
error. That leaves a possible superpolynomial best-known separation in the
latter regime, not a proved lower bound.

The hardness evidence must be used with care. [Berry et al.,
arXiv:2209.13581](https://arxiv.org/abs/2209.13581) give concrete large-Betti,
large-gap graph constructions and detailed QSVT resources, but their displayed
join families have closed spectra and therefore do not themselves establish an
AG computational advantage. [Hayakawa,
arXiv:2608.02726](https://arxiv.org/abs/2608.02726) proves unweighted gapped
clique homology QMA1-complete; that decision hardness does not make a BQP
normalised estimator for an exponentially small kernel. A new family must
simultaneously retain a resolvable fraction and hide its value from the known
classical estimators.

### 8.4 Stronger construction exposed by the re-ranking: minimal-syzygy
BosonSampling

The most complete positive construction found in this re-review lies just
outside G01--G17 and has been sent to root for a dedicated lane.

Let `R=C[z_1,...,z_q]`, `q>=2m`, and

`f_1=product_(i=1)^m z_i`,
`f_2=product_(i=m+1)^(2m) z_i`.                                      (13)

The forms are coprime, so they are a regular sequence. The complete
intersection `I_0=(f_1,f_2)` has minimal resolution

`0 -> R(-2m) --(f_2,-f_1)--> R(-m)^2 -> R -> R/I_0 -> 0`.             (14)

For a supplied `q`-mode unitary `U`, let `phi_U` be its linear change of
variables and `I_U=(phi_U(f_1),phi_U(f_2))`. Automorphism functoriality carries
the unique degree-`2m` first syzygy to

`s_U=(phi_U(f_2),-phi_U(f_1))`.                                      (15)

The squarefree monomials in (13) have unit Fock norm, and `Gamma_m(U)` is
unitary on `R_m`. Prepare

`|s_U>=(|1>Gamma_m(U)|S_2>-|2>Gamma_m(U)|S_1>)/sqrt(2)`               (16)

using `m` single photons, a label qubit and one controlled passive optical
network. Number measurement gives

`Pr(j,nu)=|Per(U[nu,S_(3-j)])|^2/[2 product_l nu_l!]`.                (17)

Thus, conditioned on the output label, (17) is standard BosonSampling. A
classical joint sampler also supplies a branch sampler because each label has
probability `1/2`. The based ideal is supplied succinctly by `U` and the two
input monomials; neither side receives the exponentially expanded coefficients.

One quantum sample uses `m` photons and a passive `q`-mode interferometer,
compiled with `O(q^2)` two-mode elements and no postselection, QFT, Grover,
DQI, QRAM or spectral gap. [Aaronson--Arkhipov,
arXiv:1011.3245](https://arxiv.org/abs/1011.3245) give the standard exact and
conjectural approximate classical-hardness consequences for Haar networks.
[Clifford--Clifford,
arXiv:1706.01260](https://arxiv.org/abs/1706.01260) give an exact classical
sampler using `O(m2^m+poly(q,m))` time and `O(q)` extra space. For approximate
hardness, `q` and the ensemble must satisfy the usual collision and
anti-concentration assumptions; those assumptions must be stated, not hidden
under “generic U.”

This candidate has a precise AG problem, a same-input quantum sampler, a
best-known exponential classical exact cost with a standard conditional
complexity obstruction, a direct dequantisation audit and the campaign's
preferred linear-optical hardware. It is a minimal syzygy of a codimension-two
complete intersection, rather than a generic state renamed as geometry. Its
weakness is conceptual: (15) is known in closed factored form and the quantum
work is exactly BosonSampling. Under the user's new rule that mechanism is
eligible, but artificial relabelling is not enough. The output explores the
Fock-weighted monomial support of a distinguished syzygy after a dense basis
change. No downstream task is presently shown to consume those samples faster
than it can use the known factors `U,f_1,f_2`, and no intrinsic invariant is
estimated: coefficient probabilities change with the coordinate basis. A
dedicated critic must decide whether this basis-sensitive distribution answers
a useful AG question, rather than merely being a valid AG sampling task, and
must pin the approximate-sampling ensemble. No utility claim is made here.

### 8.5 Revised final verdict

**The repaired G01--G17 portfolio and C-371/C-372 are approved for scoped
SKETCH integration. No existing finalist yet proves a same-input advantage.**
The previous rejection based solely on known QSVT, supersymmetric, CP,
adiabatic, quantum-dilogarithm or perfect-transfer processing is withdrawn.

The new minimal-syzygy construction (13)--(17) is the first R11 proposal in
this review with a complete polynomial quantum implementation and a standard
same-output classical hardness comparison. Its usefulness and intrinsic
motivation are unresolved, so it is not yet a north-star hit. It should receive
the next proposer and independent-critic cycle. The squarefree QSVT route (12)
is more directly an invariant-count problem, but still lacks the family needed
to turn its conditional resource window into an advantage.
