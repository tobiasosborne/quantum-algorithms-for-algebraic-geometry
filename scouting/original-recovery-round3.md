# Recovery round 3: algebraic syndromes, mixed sources, and exact inverse costs

2026-09-05. This memo constructs two genuine recovery procedures and separates
their guarantees from a third, failed, source-preserving recovery proposal. It
does not establish a qualifying new quantum algorithm. Finite-field point registers
use the counting metric; polynomial syndrome spaces use the campaign Fock metric.
These disjoint contexts explicitly depart from the original projective-variable
index convention C2 where necessary. All definitions here are provisional; only
the orchestrator may merge definitions or assign claims-DAG statuses.

No quantum memory source is freshly prepared to repair a failed branch. The
procedures specify what information they preserve or deliberately erase. In
particular, restoring one prescribed mixed state is substantially weaker than
restoring every unknown pure source state. The singular-value obstruction in
section 4 applies only to the latter task.

## 1. A rejected warm-up: symmetry can repair, but also directly prepare

If a compact group preserves `W_N` and acts irreducibly there, its Haar twirl
maps every supported density operator to `P_N/dim(W_N)`. This is legitimate
recovery of a failed quotient-growth posterior, provided the group action and
its randomization can actually be implemented. It does not require a source
reflection or a new copy of an unknown ket.

On projective homogeneous spaces, however, an easy highest-weight vector in
`W_N` is normally available. Twirling that vector directly prepares the same
mixed target, bypassing growth and its failed branches. This lane therefore
does not propose symmetry recovery as a speedup. In a reducible representation,
twirling only uniformizes irreducible blocks; it does not automatically restore
their correct relative weights. Section 3 supplies a separate weighted example.

## 2. Exact syndrome correction on a triangular complete intersection

### 2.1 Input, desired output, and instrument

Over an explicitly represented finite field `F_q`, supply arithmetic circuits
for polynomials `g_i(x_(i+1),...,x_n)`, `1<=i<=r<n`. Write

`f_i(x)=x_i-g_i(x_(i+1),...,x_n)`.

The common zero locus is a smooth affine graph over the free coordinates
`x_(r+1),...,x_n`; the equations form a regular sequence. The classical geometric
task is to sample uniformly from its `q^(n-r)` rational points.

For the coherent version, an arbitrary unknown ket `|v>` on the free-coordinate
register is permitted. Prepare the constrained coordinates in uniform states.
Process `i=r,r-1,...,1`. Compute `f_i` into a fresh syndrome register, measure
that register, record its field-valued outcome `s_i`, and subtract `s_i` from
the coordinate `x_i`.

No zero-syndrome postselection is performed. All syndrome values are accepted.
The correcting coordinate translation is a known reversible finite-field gate.

### 2.2 Exact progress invariant

ASSUME the preceding instrument. PROVE that every branch gives the same coherent
encoding of the free-coordinate ket and all completed equations remain solved.

2.2.1 Before processing coordinate `i`, the coordinates with index greater than
`i` already have their recursively evaluated values. The coordinate `x_i` is
uniform and independent of them. For each fixed value of the later coordinates,
the function `x_i -> x_i-g_i(...)` is a bijection of `F_q`.

2.2.2 Consequently each syndrome value has probability exactly `1/q`, independent
of the unknown ket. Conditional on outcome `s_i`, the constrained coordinate is
`x_i=g_i(...)+s_i`, coherently over all later coordinates.

2.2.3 Subtracting the known outcome gives `x_i=g_i(...)`. It does not change any
`f_j` with `j>i`, because those equations contain only coordinates of index at
least `j`. Thus after processing `i`, all `f_j=0` for `j>=i`.

2.2.4 Let `E` denote the isometric graph encoding of the free coordinates. The
corrected Kraus map of every full syndrome transcript is `q^(-r/2) E`. The
`q^r` transcripts therefore give the same normalized output `E|v>` and reveal
no information about `v`. This is exact recovery by a specified instrument,
not an assertion that failure outcomes happen to be harmless.

### 2.3 Resource benefit and fatal comparator

If reversible evaluation of `g_i` costs `C_i`, the total cost is
`O(sum_i C_i+r poly(log q))`, with the usual charged gate-synthesis precision.
Naively requiring all measured syndromes to vanish would succeed only with
probability `q^(-r)`. The correction procedure removes that artificial cost.

It nevertheless does not yield a new algorithmic mechanism. Initialize the
constrained coordinates to zero and reversibly evaluate the `g_i` in the same
descending order: this implements exactly `E`, without syndrome measurements.
For the classical point-sampling output, choose the free coordinates uniformly
and evaluate those same circuits. That is an exact matched classical algorithm
with the same polynomial resource dependence.

More generally, a coherently prepared classical distribution followed only by
computational-basis syndrome measurements, efficiently computable basis
permutations, and final basis measurement has a direct classical simulation.
Sampling the initial classical label and tracking it through those same
measurements and permutations gives the identical output law. Arbitrary diagonal
phases do not change this argument. It does not cover genuinely interfering
operations, or an unknown quantum input whose initial distribution is unavailable
to the comparator.

### 2.4 Why flatness does not provide the missing correction by itself

2.4.1 The family `t=xy` is flat. Explicitly, `C[x,y]` is a free `C[t]`-module
with basis `1,x,x^2,...,y,y^2,...`: remove the common power of `x,y` from every
monomial and replace it by a power of `t`. This representation is unique.
Over `F_q`, nonzero fibres have `q-1` rational points while the zero fibre has
`2q-1`. Thus flatness does not imply uniform syndrome probabilities, constant
rational-point counts, or a point-permutation correction between all fibres.

2.4.2 Even finite étale flatness does not provide a global rational section.
For `G_m -> G_m`, `z -> z^2`, a rational trivialization of the double cover
would give `a(t) in C(t)` with `a(t)^2=t`. Taking order at `t=0` gives the
impossible equality `2 ord_0(a)=1`.

This last argument refutes only the proposed global rational fibre-correction
recipe. It does not exclude analytic local charts, digital or arbitrary quantum
corrections, copy-access transformations, or efficient finite-field square-root
algorithms. Their costs and data would have to be supplied separately.

## 3. An explicit mixed-source repair with unknown component weights

This construction addresses a different question from pure-state restoration.
The target is a uniform mixed state on a reducible, generally nonhomogeneous
zero set, and the input may be any supported failure posterior. The channel
erases its coherence and repairs the diagonal weights. Its implementation never
uses the unknown component intersection count.

### 3.1 Equation-level access and target

Supply an arithmetic circuit `h:F_q -> F_q` of evaluation cost `C_h`. Define

`X_h={(x,y) in F_q^2 : y(y-h(x))=0}`,

with components `A={(x,0)}` and `B={(x,h(x))}`. Put
`t_h=|{x:h(x)=0}|` and `M_h=|X_h|=2q-t_h`. Both components contain `q` points;
their intersection contains `t_h` points, counted only once in `X_h`.

The target is `rho_X=(1/M_h) sum_{z in X_h}|z><z|`, on the ordinary point
register. A density operator `rho` supported on the span of `X_h` is supplied.
For `0<delta<1`, the task returns a state within trace distance `delta` of `rho_X`.
The scalar `t_h`, its roots, a uniform sampler for the union, and a target-state
preparation oracle are not supplied to the channel.

### 3.2 Physical maps, all explicitly computable

3.2.1 Dephase the two-coordinate register in the computational basis, forgetting
the outcome. This leaves `rho_X` unchanged. It is allowed here because the
task asks for one specified mixed state, not for the original unknown ket.

3.2.2 With probability one half, apply the involution

`sigma(x,y)=(x,h(x)-y)`.

It swaps the two graph components and fixes every intersection point. Denote
the resulting average channel by `S`.

3.2.3 Choose a field element `a` uniformly. The graph-`A` translation is

`T_A(a)(x,y)=(x+a,0)` when `y=0`, and `(x,y)` otherwise.

The graph-`B` translation is

`T_B(a)(x,y)=(x+a,h(x+a))` when `y=h(x)`, and `(x,y)` otherwise.

Each is a bijection of the entire ambient point set: it permutes its indicated
graph and fixes its complement. Its inverse uses `-a`. Thus each induces an
ordinary permutation unitary, implementable using a constant number of circuit
evaluations and reversible finite-field operations. In particular, no membership
oracle for an unspecified component or root-finding subroutine is required.

3.2.4 Let `E_A,E_B` be the average channels over these translations, and set
`C=(E_A+E_B)/2`. One recovery round is `K=C o S o Dephase`.
All three operations preserve the support in `X_h`. Every permutation restricts
to a permutation of `X_h`, so `K(rho_X)=rho_X`, with the correct union weights.
This invariance does not assume `t_h=0` or treat the components as disjoint.

### 3.3 Uniform contraction independent of the unknown intersection

ASSUME a basis-state input `|z><z|` with `z in X_h`. Write `mu_A,mu_B` for
the uniform classical distributions on the two graphs. PROVE that the one-round
output distribution dominates `(1/4)` times the uniform distribution on `X_h`.

3.3.1 If `z` is outside the intersection, let `z'=sigma(z)`. Direct enumeration
of the component-swap coin and the graph-update coin gives

`K(z,.)=(mu_A+mu_B)/4 + (delta_z+delta_(z'))/4`.

3.3.2 If `z` lies in the intersection, the corresponding formula is

`K(z,.)=(mu_A+mu_B)/2`.

3.3.3 Every union point has mass at least `1/q` in `mu_A+mu_B`. Since
`M_h>=q`, both formulas imply

`K(z,w)>=1/(4q)>=1/(4M_h)` for all `z,w in X_h`.

Therefore `K=(1/4) Reset_(rho_X)+(3/4) J` on diagonal inputs, for a stochastic
kernel `J` which also preserves the uniform distribution. This is a proof
decomposition; implementing the unknown reset channel is not an algorithm step.

3.3.4 Total variation is contracted by stochastic maps, so after `s` rounds,

`(1/2)||K^s(rho)-rho_X||_1 <= (3/4)^s`

for every supported source density operator. The first dephasing makes all
subsequent states diagonal; the same argument therefore applies even when the
original posterior has off-diagonal entries.

3.3.5 Taking `s=ceil(log(1/delta)/log(4/3))` gives expected total recovery cost

`O((C_h+poly(log q)) log(1/delta))`

and `O(log q)` point-register space plus evaluation workspace. Uniform classical
random field elements can be generated with constant-expected-cost rejection
from a binary interval. No Haar sampling, Schur decomposition, source reflection,
global projector, spectral-gap oracle, or fresh unknown input is used.

The number of rounds is independent of `q`, `t_h`, and the initial posterior's
relative mass on the two components. This is an actual mixed-source recovery
theorem, including the troublesome component-intersection weights.

### 3.4 Fatal classical comparison

The channel itself is classically simulable: its source dephasing and all later
updates act on an ordinary point distribution. A stronger matched classical
sampler avoids mixing altogether. Choose a fair bit `b` and uniform `x in F_q`.
If `b=0`, output `(x,0)`. If `b=1`, evaluate `h(x)`, reject when `h(x)=0`, and
otherwise output `(x,h(x))`.

Every point of `X_h` has exactly one accepted preimage. The acceptance probability
is `M_h/(2q)>=1/2`, so the output is exactly uniform and the expected number of
trials is at most two. This uses the same equation circuit and never computes
`t_h`. It can also prepare the mixed quantum target by loading the sampled point.

Thus the recovery theorem is useful as a counterexample to blanket statements
that mixed-source restoration is impossible, and as a precise handling of overlap
weights. It does not beat the classical comparator or establish a new quantum
mechanism. Unknown component counts alone do not imply a hard sampling task.

## 4. Coherent Koszul syndromes do not ensure inexpensive pure-state recovery

The final attempt keeps the equation index coherent after a failed operation.
For commuting annihilators `F_i=bar(f_i)(partial)`, introduce fermionic creation
operators `c_i^dag` and the Koszul map `D=sum_i c_i^dag F_i`.
Commutativity and fermionic anticommutation give `D^2=0`. The proposed idea was
to use this syzygy structure to invert a retained syndrome without destroying
its unknown source information. The missing ingredient is a bounded inverse;
nilpotence and regularity do not provide one.

### 4.1 The exact universal inverse bound

Let `F:S -> E` be an injective contraction, realized as one known Kraus branch.
After observing that branch, allow any physical recovery instrument, any fresh
ancillas, multiple accepted outcomes, and outcome-dependent corrections. Require
that every accepted output restore every unknown pure source ket exactly.

ASSUME this requirement. PROVE the total joint probability of observing `F`
and then restoring the source is at most `lambda_min(F^dag F)`.

4.1.1 Include the final corrections in accepted recovery Kraus operators `R_a`.
Pure exact restoration implies `R_a F u` is parallel to `u` for every source
vector. A linear map preserving every one-dimensional subspace is scalar, as
seen by applying it to a basis and pairwise sums. Hence `R_a F=c_a 1`.

4.1.2 Trace nonincrease implies `sum_a R_a^dag R_a<=1_E`. Multiplying by
`F^dag,F` gives

`sum_a |c_a|^2 1_S <= F^dag F`.

The joint restoration probability is `sum_a |c_a|^2`, independent of the ket,
so the claimed minimum-eigenvalue upper bound follows.

4.1.3 Let `lambda=lambda_min(F^dag F)`. The operator

`R_opt=sqrt(lambda) (F^dag F)^(-1) F^dag`

is a contraction on the syndrome space and obeys `R_opt F=sqrt(lambda)1`.
A unitary dilation therefore attains the bound. Conditional on the observed
syndrome branch, its success probability is `lambda/||Fu||^2`.

Adaptive finite protocols are covered by taking their complete accepted paths
as the Kraus labels. The claim assumes no additional copies of the unknown ket.

### 4.2 A normalized regular-sequence counterexample

Use the unit-norm linear forms

`f_1=x`, `f_2=(x+epsilon y)/sqrt(1+epsilon^2)`, `0<epsilon<=1`.

They form a regular sequence, generate the fixed affine ideal `(x,y)`, and
have commuting annihilators. On the Fock degree-one source with basis `x,y`,
retain the equation index coherently. Divide the syndrome map by `sqrt(2)`:

`F=(1/sqrt(2)) [[1,0],[1/sqrt(1+epsilon^2), epsilon/sqrt(1+epsilon^2)]]`.

4.2.1 Its squared singular values are

`lambda_plus/minus=[1 +/- 1/sqrt(1+epsilon^2)]/2`.

Thus it is an injective contraction, realized by a constant-size two-outcome
unitary dilation compiled from its explicit two-by-two singular-value decomposition.
The coherent equation label is retained; no premature measurement of that label
is responsible for the bound.

4.2.2 Section 4.1 gives optimal joint restoration probability

`lambda_minus=[1-1/sqrt(1+epsilon^2)]/2 = epsilon^2/4+O(epsilon^4)`.

For `epsilon=2^(-b)`, it is exponentially small in coefficient precision `b`,
although the sequence remains regular and each generator is normalized. The
formal Koszul identity holds throughout the family and does not change this cost.

4.2.3 This is a presentation-conditioned example, not classical hardness of
the ideal. The small displayed system can be preconditioned classically to `(x,y)`.
It refutes a recovery guarantee inferred solely from regularity, unit generator
norms, or `D^2=0`; it does not refute a separately proved preprocessing theorem.

### 4.3 Scope separation that must survive any merge

The inverse bound does not forbid a CP map that restores only the one prescribed
mixed state `P_N/dim(W_N)`. Such a map may intentionally forget its input. Section
3 explicitly constructs a fast map of this kind on a nontrivial reducible family.
Consequently no assertion that all quotient-growth recovery is impossible follows
from 4.1 or 4.2. A hard mixed-source proposal still needs actual equation-level
implementation, correct global weights, and a matched classical comparison.

## 5. Verification and MERGE PROPOSAL

Bounded in-memory calculations checked the mixed recovery kernel for fields of
sizes `2,3,5,7` and the polynomials `0`, `1`, `x(x-1)`, and `x^2+x+1`.
Every kernel preserved the uniform union distribution and its smallest entry
was at least `1/(4M_h)`. This included coincident components, disjoint components,
and nonempty proper intersections. The syndrome inverse formula was checked at
`epsilon=0.5,0.1,0.01`; its joint probabilities were approximately `0.0527864`,
`0.0024814`, and `0.0000249981`. These calculations are exploratory, not registered
red-capable checkers or independent adjudication.

Candidate claims for independent review are the branch identity `q^(-r/2)E`
and progress invariant in 2.2; the mixed recovery channel, correct stationary
weights, and `(3/4)^s` bound in 3.2--3.3; the exact matched classical sampler
in 3.4; and the scoped universal inverse bound and example in 4.1--4.2.

No useful-speedup claim is proposed. The positive repairs reduce respectively
to reversible classical evaluation and classical sampling of a union with bounded
multiplicity. The negative inverse theorem must never be promoted into a statement
about all fixed-mixed-state recovery. New information-recovery mechanisms and a
natural hard classical comparator remain unestablished by these constructions.
