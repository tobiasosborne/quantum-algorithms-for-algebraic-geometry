# Round 2 Astra construction: nilpotent transport and coherent descent

2026-09-05. This is a constructive attempt with explicit physical implementations,
followed by adversarial resource audits. It does not establish a north-star algorithm.
No literature search or historical novelty certification was performed. The memo
departs from convention C1: finite quotient algebras and vector-bundle fibres carry
the displayed computational-basis Hermitian metric, supplied as part of the input.
It does not identify that metric with a canonical metric of the algebraic object.
Definitions below are provisional and are collected for orchestrator merge at the end.

## 1. Nilpotent coordinate transport

The proposed mechanism was to propagate an entire infinitesimal neighbourhood
coherently through coordinate changes, and recycle unsuccessful outcomes as other
known coordinate charts. This differs from extracting jets by finite differences:
the nilpotent algebra and its coordinate changes are given explicitly, and the
operation acts on an existing coefficient state. No inverse system projector is used.

### 1.1 Actual task and input

Use the length-`3^r` affine scheme

`X_r = Spec A_r`, `A_r = C[x_1,...,x_r]/(x_1^3,...,x_r^3)`.

The ordered monomial basis is orthonormal. Each coordinate is represented by a qutrit
with labels `0,1,2`. The substitution `x_i -> x_i+x_i^2` is an automorphism, whose
inverse is `x_i -> x_i-x_i^2`. Let `T_r` be its simultaneous pullback on coefficients.
On one factor, in coefficient-column convention,

`T = [[1,0,0],[0,1,0],[0,1,1]]`, and `T_r = T^(tensor r)`.

**Nilpotent-coordinate coefficient sampling:** given a preparation circuit `U_u`
of cost `C_u` for an unknown normalized coefficient state `|u>`, output a monomial
index `b` with law `|<b|T_r u>|^2 / ||T_r u||^2`. The classical input is the same
circuit description, not a free list of its amplitudes. An explicit coefficient
list is a separate input model and is charged at its full length.

This is a precise scheme calculation, but its displayed probability law depends
on the chosen metric. It is not asserted to be an intrinsic invariant of `X_r`.

### 1.2 Implementable transport and its exact cost

ASSUME arbitrary qutrit gates and heralding are available. PROVE an exact sampler.

1.2.1 Let `phi=(1+sqrt(5))/2`. The singular values of `T` are `phi,1,phi^(-1)`:
the nontrivial block of `T^dag T` is `[[2,1],[1,1]]`.

1.2.2 Form `K=T/phi`. A singular-value decomposition compiles a constant-size
unitary dilation with successful Kraus operator `K`. Explicitly, diagonal singular
values are implemented by a qutrit-controlled rotation of a flag qubit, between
the two fixed qutrit unitaries from the decomposition. This is an ordinary physical
operation, not an assumed nonlinear normalized map.

1.2.3 Apply that dilation to every qutrit with separate flags. Accept only when
all flags succeed, then measure the coefficient register. The accepted Kraus
operator is `T_r/phi^r`; the success probability is

`a(u)=||T_r u||^2 / phi^(2r)`.

1.2.4 Repeating fresh preparations until success gives exactly the requested law.
The expected gate cost is `O((C_u+r)/a(u))` and the workspace is `O(r)` plus the
preparation workspace. To bound runtime with failure probability at most `eta`,
an advertised lower bound `a_0<=a(u)` gives
`O((C_u+r) log(1/eta)/a_0)` gates. Finite gate synthesis must be included for an
approximate universal discrete gate set; no constant-cost exact irrational gate
assumption is being hidden in that model.

### 1.3 A universal normalization obstruction

ASSUME a heralded instrument gives the pure projective map
`|u> -> T_r|u>/||T_r u||` exactly for every pure input. Multiple accepted outcomes
and recorded outcome-dependent unitary corrections are allowed. PROVE that its
worst-input success probability is at most `phi^(-4r)`.

1.3.1 After including any specified corrections, every accepted Kraus operator
`L_a` has `L_a u` parallel to `T_r u` for all `u`. Since `T_r` is invertible,
`T_r^(-1)L_a` preserves every one-dimensional subspace. Applying this statement
to basis vectors and their pairwise sums gives `L_a=c_a T_r`.

1.3.2 Trace nonincrease gives
`sum_a |c_a|^2 T_r^dag T_r <= 1`, hence
`sum_a |c_a|^2 <= ||T_r||^(-2)=phi^(-2r)`.

1.3.3 A minimum-right-singular-vector input has squared image norm `phi^(-2r)`.
Its acceptance probability is therefore at most `phi^(-4r)`. The implementation
in 1.2 attains the bound. This argument concerns exact universal transformations;
it does not establish an approximate or promised-input lower bound.

1.3.4 This bad input can be a tensor product of the same one-qutrit singular
vector. There is no difficult input preparation or large local nilpotence order
behind the obstruction. For `r=8` the bound is approximately `2.05e-7`; for `r=16`
it is approximately `4.21e-14`.

### 1.4 Same-output classical attacks

For product coefficient input, transform each three-entry vector and sample each
factor independently. This costs `O(r)` arithmetic operations, including for the
worst-input family in 1.3. The proposed universal speedup is therefore absent.

For an explicit length-`3^r` coefficient array, tensor-axis transforms cost
`O(r 3^r)` arithmetic operations; normalization and one sample cost `O(3^r)`.
For a general succinct preparation circuit, the elementary matched classical
attack simulates that circuit and applies these transforms. Exponential cost of
that attack is not a lower bound or evidence for best-in-class hardness.

For a matrix-product coefficient input of polynomial bond dimension, one-site
filters preserve the bond dimensions. Standard contractions give its norm and
sequential conditional probabilities in polynomial time. Thus the apparent
state-compression advantage disappears on this accessible structured family too.

The surviving implementable sampler is a normalized local-filter procedure.
It is not asserted to be an original algorithmic mechanism under PRD criterion 6.

## 2. Can algebraic chart labels rescue rejected branches?

The attempted repair was to accept every full-rank local outcome and record its
`GL` coordinate change. Such outcomes preserve membership in a tensor orbit, so
it initially looks as if a calculation of moduli could ignore the bad branches.
The following exact calculation identifies a quantitative obstruction.

### 2.1 Operation and proposed use

Let a normalized tensor `v` belong to `C^q tensor H`. A local quantum instrument
has operators `K_a` on `C^q` with `sum_a K_a^dag K_a=1`. Outcome `a` occurs with
`w_a=||(K_a tensor 1)v||^2` and produces its normalized image `v_a`.
Full-rank `K_a` supply honest invertible coordinate changes. The proposed use was
to repeat such measurements, retaining the accumulated chart, until the tensor
is in a well-balanced representative where an invariant can be read robustly.

Let `f` be a nonzero homogeneous degree-`d` polynomial invariant under
`SL(q)` on this tensor factor. Define the normalized invariant magnitude
`J_f(v)=|f(v)|^(2/d)`. These are provisional local definitions, not new claim statuses.

### 2.2 Exact branch identity

ASSUME the preceding instrument and invariant. PROVE

`sum_a w_a J_f(v_a) = J_f(v) sum_a |det K_a|^(2/q) <= J_f(v)`.

2.2.1 For invertible `K`, choose a complex `q`th root of `det K` and write
`K=c S` with `S in SL(q)`. Homogeneity gives
`|f((K tensor 1)v)|=|det K|^(d/q)|f(v)|`.
Absolute values remove the root choice. Continuity gives the same magnitude
identity for singular `K`.

2.2.2 Homogeneity under state normalization therefore gives
`w_a J_f(v_a)=|det K_a|^(2/q) J_f(v)` for nonzero-probability outcomes.
Zero-probability outcomes contribute zero by continuity.

2.2.3 The geometric mean of the eigenvalues of `K_a^dag K_a` is at most their
arithmetic mean. Thus
`|det K_a|^(2/q)<=Tr(K_a^dag K_a)/q`; summing gives the claimed inequality.

2.2.4 Conditional application proves that `J_f` is a nonnegative supermartingale
under adaptive instruments on the displayed factor. The same applies to several
factors if `f` is invariant under each corresponding special-linear group.
For any finite stopping protocol, the probability
of reaching `J_f>=tau` is at most `J_f(v_initial)/tau`. The same hitting bound for
an unbounded protocol follows by taking increasing finite horizons.

### 2.3 Consequence and limits

Outcome-dependent coordinate labels do not provide a free route from arbitrarily
small invariant magnitude to a representative of fixed positive magnitude. The
probability cost remains, even if every full-rank branch stays in the same orbit.
This calculation is an obstruction to the proposed balancing procedure; it is
not a theorem that every invariant decision problem is quantumly difficult.
It allows nonlocal operations, extra resource states, multiple input copies, or
tasks that never require increasing this invariant magnitude as possible escapes.

A bounded exploratory calculation checked the identity using the determinant of
a two-qubit coefficient matrix and diagonal two-outcome filters. Input magnitude
`0.2065523948` became expected magnitude `0.1784744238`, matching the determinant
formula. This was an in-memory calculation, not a registered red-capable checker.
The proof above, rather than that numerical example, supports the obstruction.

## 3. A different construction: sew bundle fibres by teleportation

The second proposal left infinitesimal schemes entirely. Its intended task was
to compute a descent or holonomy observable of a high-rank vector bundle without
materializing its fibre vectors. The candidate ingredient was to interpret every
teleportation byproduct as a change of local trivialization, and adjust subsequent
gluing data in that chart. The construction is physically explicit, but the audit
separates a genuine transport task from a spurious invariant of gluing alone.

### 3.1 Input and operation

At successive overlap points, suppose one is supplied with unitary transition
matrices `G_1,...,G_L` on `C^h`, with `h=2^b`, each by a circuit of cost `C_i`.
Also supply preparation `U_v` and a final computational-basis measurement. The
precise output is a sample from `|<z|G_L...G_1 v>|^2`.

Prepare the normalized entangled resource
`|G_i>>=(1 tensor G_i) h^(-1/2) sum_j |j,j>`.
A Bell measurement of the incoming register and the first resource half has
`h^2` outcomes. With a fixed Bell convention, outcome `a` leaves
`G_i P_a v`, up to a known scalar, where `P_a` is a known tensor Pauli operator.
Every outcome has probability `1/h^2`; none is rejected.

The next resource can be changed using the known byproduct, or a physical
correction `G_i P_a^(-1) G_i^dag` can be applied. The latter is always implementable
from the supplied circuit and its inverse. Iterating gives a deterministic exact
transport circuit of cost `O(C_v+sum_i C_i+Lb)` up to constant gate-repetition
factors and synthesis precision. Preparing the Choi resources already requires
the transition circuits; the operation does not obtain them from equations.

### 3.2 Algebraic and computational audit

3.2.1 A vector-bundle cocycle is not a connection. At a common point `x`, honest
transitions obey `G_ij(x)G_jk(x)=G_ik(x)`, so a closed product along such chart
changes is the identity. There is no nontrivial holonomy to estimate there.
Evaluating successive transitions at different points requires identifications
of fibres within each chart. These are connection or trivialization data and
their effect must be included in the problem; they do not follow from descent.

3.2.2 Regular algebraic transition functions are usually `GL(h,C)`-valued rather
than unitary in the supplied metric. The Choi resource of a nonunitary `G` has
normalization `||G||_F`; Bell outcomes generally have input-dependent probabilities.
The correction `G P_a^(-1)G^(-1)` is generally nonunitary. Calling that correction
a chart relabeling does not physically perform a requested fixed-frame measurement.
Exact universal normalized transport again has the condition-number obstruction
of 1.3, with `T_r` replaced by `G`.

3.2.3 If all transition matrices are explicit, the matched classical task is
ordinary matrix-vector multiplication and sampling, costing `O(sum_i h^2)` for
dense matrices. Sparse and structured transitions give stronger classical attacks.
If matrices are instead succinct quantum circuits, an exponential array-simulation
baseline merely restates the general circuit-simulation problem.

3.2.4 The successful physical recipe is gate teleportation with feed-forward.
Interpreting byproducts as changes of trivialization supplies no new central
mechanism. Thus this construction fails criterion 6 even when a connection supplies
a meaningful output and a hard circuit family supplies a conditional advantage.

### 3.3 Exact missing ingredients for a future repair

A surviving descent proposal would need an intrinsic, explicitly encoded algebraic
output; an efficient construction of its transport from that algebraic input;
a mechanism beyond ordinary gate teleportation; and a matched classical analysis.
Unitarity of a chosen chart representation, a connection, and succinct Choi access
are separate assumptions. None has been established here for a hard geometric family.

## 4. MERGE PROPOSAL

No speedup, existence of a qualifying algorithm, or historical novelty assertion
is proposed for promotion. Suggested provisional definitions are:

- `D-OR-NILPOTENT-TRANSPORT`: the scheme, coefficient metric, automorphism, and
  coefficient-sampling task of 1.1.
- `D-OR-LOCAL-INVARIANT-MAGNITUDE`: the instrument and `J_f` of 2.1.
- `D-OR-DESCENT-TRANSPORT`: circuit-supplied transition/connection data and the
  fixed-frame output law of 3.1, including the caveats of 3.2.1.

Candidate claim statements for independent criticism are:

- The exact universal heralded realization of the `r`-factor nilpotent coordinate
  automorphism has optimal worst-input success `phi^(-4r)`; proof 1.3.
- Local trace-preserving instruments satisfy the invariant-magnitude identity and
  supermartingale inequality of 2.2, with the stated stopping bound.
- Cocycle data alone do not specify transport between distinct base points;
  at a common point the cocycle product telescopes; argument 3.2.1.
- The displayed unitary sewing protocol is deterministic gate teleportation,
  with the stated circuit cost and no free extraction of transitions from equations.

The first two assertions deserve a critic pass before any claims-DAG entry. The
descent observations primarily prevent a misleading future proposal. All four
are partial research products; none meets PRD criteria 1--6 together.
