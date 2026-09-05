# Direct programmable testing of Waring components

2026-09-05. Independent derivation of the orchestrator's shorter upper bound for
the exact terminal promise in `scouting/waring-terminal-baseline.md`. This uses
the standard tensor Hermitian norm, departing from C1. The construction is a
composition of antisymmetric comparison/programming measurements and a supplied
point-property measurement. Displayed I denotes identity, a local departure
from C6. Canonical access is D-WARING-DIRECT-POINT-TEST in
`definitions/waring-components.md`; status is recorded only at C-347--C-348
in the claims register. The independent review is
`verdicts/waring-programmable-tester-r1.md`; no historical novelty is claimed.

The result replaces recursive balanced-packet preparation by a fixed experiment
on `r+1` original source copies. It preserves the terminal bit, including its
exact zero case. It does not prepare a balanced component mixture or estimate
the average point residual without bias.

## 1. Source, point property, and the actual event

Use copies of the normalized Waring source

`T=sum_(a=1)^r c_a u_a^(tensor k)`, `||u_a||=1`, `k>=3`, `r>=2`,

with independent components, Gram matrix `G`, and all `c_a!=0`. Assume the
known promises `G>=eta 1`, `0<eta<=1`, and `p_seed>=p_*>0`, where

`p_seed=|product_a c_a|^2 det G det G_(k-1)`,

and `G_m=G^(circ m)` is the entrywise power Gram matrix. These are the same
promises used in the earlier Waring construction, not new component oracles.

Let `Q` be the accepting positive-contraction POVM effect of a supplied,
implemented two-outcome measurement on `h` local
component slots, where `1<=h<=2k-2`. Define

`f_a=<u_a^h,Q u_a^h>`, `Gamma=(1/r)sum_a f_a`.

The terminal problem is to distinguish `Gamma=0` from `Gamma>=gamma`, with
known `gamma>0`. All costs of implementing `Q` must be included. No query
state, component coordinate description, or inverse source preparation is supplied.

In the rank-four terminal problem, `r=k=4`, `q=d^2`, `h=5`, and `Q` alternates
the five internal `A` registers and acts as the identity on their `B` registers.
Then `f_a=e_5(Tr_B |u_a><u_a|)` is exactly the squared-minor residual already
defined in the baseline memo. No change to that problem's output or promise occurs.

### 1.1 Register map for one shot

Take `r+1` original copies, with the first `r` designated as source rows and
the last as the data row.

1. Apply `P_(wedge^r)` to slot one of each of the first `r` source rows.
2. Apply another `P_(wedge^r)` to slot two of rows `2,...,r`, followed by slot
   one of the data row, in that order.
3. The target consists of slots `2,...,k` of source row one and slots
   `2,...,k` of the data row, for `2k-2` target slots. Apply `Q` to any `h`
   of those slots. Ignore all other unmeasured slots.

The output event requires acceptance of both alternating measurements and
the `Q` outcome. Otherwise the shot outputs zero. Each shot consumes exactly
`r+1` original copies, regardless of its outcomes.

These three measurements act on disjoint physical registers and commute. Their
analysis can be ordered as above, but the implementation does not need to
normalize, retain, or rebuild a successful intermediate packet. The probability
below is the joint probability of the complete event.

## 2. Exact unnormalized state, with both factorials and the sign

Let `omega` be the normalized wedge of all components, and put
`c_prod=product_a c_a`. For every permutation `pi`,

`P_(wedge^r)(u_(pi1) tensor ... tensor u_(pir))`
`=sgn(pi) sqrt(det G/r!) omega`.

ASSUME the register map of 1.1. PROVE that after the two alternating outcomes,
the unnormalized state, with registers regrouped, is

`(-1)^(r-1) c_prod (det G/r!) omega tensor omega`
` tensor sum_(pi in S_r) c_(pi1) u_(pi1)^(tensor (2k-2))`
`                              tensor_(i=2)^r u_(pii)^(tensor (k-2))`.

2.1 The first alternation kills every repeated-label term among the first `r`
sources. The coefficient product is `c_prod` for every surviving permutation,
so its output is

`c_prod sqrt(det G/r!) omega tensor`
`sum_pi sgn(pi) tensor_(i=1)^r u_(pii)^(tensor (k-1))`.

2.2 Expand the extra source as `sum_b c_b u_b^k`. In the second alternating
register, the program labels are `pi(2),...,pi(r)` and the data label is `b`.
If `b` equals any program label, alternation is zero. The only surviving data
label is consequently `b=pi(1)`.

2.3 On that term the second wedge order is
`pi(2),...,pi(r),pi(1)`. Its sign is `(-1)^(r-1)sgn(pi)`, and its norm factor
is again `sqrt(det G/r!)`. The two permutation signs cancel. The remaining
global sign is independent of the unknown labels and coefficients.

2.4 Source row one and the data row each retain `k-1` copies of the same
component, giving `2k-2` target slots. Every other source row retains `k-2`
slots. The two wedge states factor out because each contains the same complete
component set. This proves the displayed identity.

In particular, the prefactor is `det G/r!`, not its square root and not
`det G/(r!)^2`. Its absolute square is used when computing probabilities.

## 3. Program conditioning prevents destructive cancellation

Write `L=2k-2` and define, for `pi in S_r`,

`v_pi=tensor_(i=2)^r u_(pii)^(tensor (k-2))`,

`t_pi=(sqrt(Q) u_(pi1)^h) tensor u_(pi1)^(tensor (L-h))`.

The square root is a proof factorization of the supplied measurement effect;
the algorithm does not require a square-root oracle or a block encoding of Q.
A heralded block of the linear operator Q would instead measure Q squared and
is not the stated access model. The given point-measurement cost is charged.

These are proof vectors. Their preparation is not an extra step or access
assumption. The squared norm of `t_pi` is `f_(pi1)`.

### 3.1 The exact joint event formula

Section 2 gives

`p_event=|c_prod|^2 (det G/r!)^2`
`                  ||sum_pi c_(pi1) t_pi tensor v_pi||^2`.       (1)

If `Gamma=0`, positivity implies `sqrt(Q) u_a^h=0` for every component. Every term
in (1) then vanishes, so YES inputs have exact zero event probability. No
balanced-mixture approximation or small-coherence approximation is used.

### 3.2 Uniform lower bound on the program Gram matrix

3.2.1 The Schur product theorem gives `G_m>=eta 1` for every integer `m>=1`:
`G_m-eta 1=(G-eta 1) circ G_(m-1)` is positive for `m>1`, since the latter
Gram matrix has unit diagonal. The case `m=1` is the promise itself.

3.2.2 The Gram matrix of the `v_pi` is a principal submatrix of
`G_(k-2)^(tensor (r-1))`, indexed by ordered injective `(r-1)`-tuples.
These tuples uniquely specify their missing first label, so there are exactly
`r!` indices, one for each permutation. Therefore this Gram matrix is at least
`eta^(r-1)` times the identity.

3.2.3 Let `A` map an abstract orthonormal label `|pi>` to `v_pi`.
Then `A^dag A>=eta^(r-1)1`. Applying `1 tensor A` to
`sum_pi c_(pi1)t_pi tensor |pi>` proves

`||sum_pi c_(pi1)t_pi tensor v_pi||^2`
`>=eta^(r-1) sum_pi |c_(pi1)|^2 f_(pi1)`
`=eta^(r-1)(r-1)! sum_a |c_a|^2 f_a`.

This argument permits arbitrary complex coefficients, component overlaps, and
point-effect Gram matrix elements. It does not assume that cross terms are positive.
The condition `k>=3` matters: at `k=2` there would be no remaining program
slots and the asserted full-rank Gram bound would not follow.

## 4. Converting the source promises into a terminal probability bound

Combining (1) and 3.2 yields the first, sharper instance-dependent bound

`p_event>=|c_prod|^2(det G/r!)^2 eta^(r-1)(r-1)!`
`                                             sum_a |c_a|^2 f_a`.       (2)

ASSUME only the supplied promises in section 1. PROVE

`p_event >= Kappa(r,eta,p_*) Gamma`,

`Kappa(r,eta,p_*)=p_*^2 eta^(3r-2)(r-1)^(r-1)/r!`.             (3)

4.1 The normalized source satisfies
`1=c^dag G_k c>=eta sum_a |c_a|^2`, so `sum_a |c_a|^2<=1/eta`.
Hadamard's determinant bound gives `det G<=1`, `det G_(k-1)<=1`, hence
`|c_prod|^2>=p_seed>=p_*`.

4.2 Fix any label `a`. Arithmetic--geometric mean applied to the other `r-1`
coefficient magnitudes gives

`product_(b!=a)|c_b|^2 <= [1/(eta(r-1))]^(r-1)`.

Consequently

`min_a |c_a|^2 >= p_* [eta(r-1)]^(r-1)`.                      (4)

4.3 To avoid losing an unnecessary factor of `eta^r`, combine the seed and
determinant factors before bounding them:

`|c_prod|^2 (det G)^2`
`=p_seed det G/det G_(k-1) >= p_* eta^r`.                     (5)

Here `det G>=eta^r` and `det G_(k-1)<=1`. Bounding `|c_prod|^2` and the
two determinants separately would give a weaker exponent; it is not the
calculation underlying (3).

4.4 Substitute (4)--(5) into (2), use `sum_a f_a=r Gamma`, and simplify
`r(r-1)!/(r!)^2=1/r!`. The powers of `eta` are
`r+(r-1)+(r-1)=3r-2`, proving (3).

The event is not, in general, an unbiased estimator of `Gamma` times a known
constant. The exact zero case and the uniform positive lower bound are what
the promised one-bit test requires.

## 5. Deterministic repetition and resources

Run

`S=ceil(log(1/delta)/(Kappa gamma))`

independent shots and report NO exactly when at least one joint event occurs.
In the ideal measurement model, YES is always correct. On a NO input the
probability of no event is at most `exp(-S Kappa gamma)<=delta`.
The source count is deterministically `(r+1)S`. There is no expected-time
packet recursion, source-count Markov cap, or conditioning by an unknown success
probability in this algorithm.

Each shot uses two known `r`-register alternating measurements, the declared
`Q` measurement, and `O((r+1)k log q)` register handling. Its source preparation
work is `(r+1)G_T` if a physical source cost is supplied. A permutation-ancilla
implementation costs `poly(r)log q` for an alternation; the normalized effect
is the actual orthogonal projector, without an uncharged wedge oracle.

For finite gate synthesis, take ideal miss probability `delta/2` and allocate
at most `delta/2` total output-distribution error to the full fixed circuit.
Per-shot and per-gate precisions are chosen against the known finite number
of shots. No division by a heralding probability is needed in that error
analysis: the circuit's output is the complete three-flag joint event.
Exact perfect completeness becomes an appropriately bounded two-sided error
after approximate gate compilation.

### 5.1 Numerical constants for the existing terminal problem

For `r=k=4`, `eta=1/2`, `p_*=1/512`, and `gamma=10^(-6)`,

`Kappa=9/2^31=4.190951585769653...*10^(-9)`.

The displayed miss-probability bound gives the sufficient ideal-error-`1/3` budget

`S=262,139,102,822,958` shots,

`5S=1,310,695,514,114,790` original source copies.

To reserve a separate `1/6` implementation-error budget, take ideal miss
probability `1/6`. Then

`S=427,530,462,368,490`,

`5S=2,137,652,311,842,450`.

The resulting total error is at most `1/3`. These are still large numbers.
The improvement over the earlier roughly `10^54` worst-case source budget
comes from asking only for the terminal witness rather than constructing large
balanced component mixtures and synchronizing all rows.

### 5.2 Exact orthogonal balanced-family probability

When `G=1` and `|c_a|^2=1/r`, all `v_pi` are orthonormal and
`|c_prod|^2=r^(-r)`. Equation (1) becomes exactly

`p_event=Gamma/[r^(r+1)r!]`.                                 (6)

Equivalently, seed success is `r^(-r)`, the extra data label matches the
missing program label with probability `1/r`, and its alternating measurement
accepts with probability `1/r!`. The terminal average contributes `Gamma`.

For rank four, the denominator in (6) is `24,576`. At `Gamma=10^(-6)`, the same
bound gives `26,999,495,607` sufficient shots or `134,997,478,035` original copies
for ideal error `1/3`; these are not global optimality claims.
Equation (6) is an exact special-family value, not the uniform bound for
arbitrary nonorthogonal inputs.

## 6. The terminal lower bound transfers unchanged

The algorithm tests exactly the `Gamma=0` versus `Gamma>=10^(-6)` problem
from `scouting/waring-terminal-baseline.md`. It retains the same source promises
and internal bipartition, and introduces no component reference states or labels.
That memo's Haar-frame hard ensembles therefore remain valid.

In particular, the moment-matched rank-four versus rank-five component spectra
give the same one-original-copy averaged state. The uniform adaptive transcript
bound remains

`TV <=8k^2 N^2/d` for a comparator using `N` original copies,

and hence `N>=q^(1/4)/(4 sqrt(24))` for success `2/3` at `k=4`, `q=d^2`.
The new upper bound only strengthens the formal classical-output separation.
Its cross-source measurements are outside the comparator's allowed operations;
each comparator may still measure globally across all four slots within one
original copy.

No lower bound for tomography or for classical descriptions is substituted.
The result still does not prove practical advantage at a reachable dimension,
nor an advantage for explicitly listed classical tensor coefficients.

## 7. Concrete prior-mechanism overlap

The second alternation is the standard programmable unambiguous-comparison
effect: alternation of the other program states together with the data state
vanishes whenever the data repeats one of those programs. It thereby identifies
the missing label without a classical description of the unknown states.

Zhang and Ying,
[Universal programmable devices for unambiguous discrimination, arXiv:quant-ph/0606189v1](https://arxiv.org/html/quant-ph/0606189v1),
equation (4) states the determinant-over-factorial acceptance law; Theorem 1
characterizes the relevant antisymmetric support on all registers other than
the putative matching program. The present guard is that same fixed-index
antisymmetric comparison, with the unused program row retained as target data.
Because it is a linear Kraus operation, its action extends to our coherent
superposition of program permutations exactly as in section 2.

The paper's complete multi-outcome discriminator may include additional scaling
to make all candidate-label effects fit in one POVM. Here only one fixed-index
projector is tested, so no such unimplemented simultaneous-discriminator claim
or extra scaling is invoked. The first alternation is also a standard universal
comparison operation, and `Q` is the explicitly known point-property test.

Thus this short circuit supplies a substantially better mathematical upper
bound, while using established programmable comparison and exterior testing
mechanisms. It is not a D22 novelty certificate. A literature claim about the
specific Waring terminal problem or any broader algorithm would require its own
adjudication; identifying this known mechanism is already enough to keep the
displayed construction from being promoted as an original primitive.

## 8. Independent checks and MERGE PROPOSAL

An in-memory direct tensor calculation used random complex nonorthogonal
components, complex coefficients, and random target projectors at
`(r,q,k,h)=(2,3,3,1)` and `(2,2,4,2)`. It applied the two actual alternating
projectors and the disjoint target projector to all original source registers.
The resulting event probabilities agreed with (1), with errors below `2e-19`.
The large shot counts were independently recomputed with 80-digit arithmetic.
These are exploratory checks; root's separate checker provides the registered
artifact and independent mathematical criticism remains required.

Candidate statements for review are the exact surviving-state identity of
section 2, the program-Gram bound and joint probability (1)--(2), the uniform
coefficient (3), and the deterministic repetition theorem. The existing terminal
lower bound is imported unchanged, not reproved or relabeled as a stronger bound.
No balanced-packet output, unbiased residual estimator on general sources,
historical originality, or complete north-star algorithm is proposed.
