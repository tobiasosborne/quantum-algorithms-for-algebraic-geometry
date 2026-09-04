# Independent verdict: four-copy Strassen/secant-three measurement

2026-09-05. Bounded review of the root's proposed mechanism, before a dedicated
manuscript/checker was supplied. Only this verdict is written by this lane.
Ordinary tensor Hilbert spaces are used, as in the D-S3 conventions; this is
not a Fock-space construction. No new claim is promoted to PROVED.

**VERDICT: FAIL as a D22 mechanism.** The proposal is a valid four-copy
measurement of the Strassen quartic module and, with the flattening blocks,
is the exact optimal perfect-completeness measurement at four copies for
three parties. It detects information that flattening ranks miss. However,
its complete circuit is three ordinary local weak-Schur measurements and
classical post-processing of their labels. An explicit bounded-normalization
permutation/LCU reduction also preserves its signal-dependent detection cost.
Thus leaving flattening-rank tests does not leave established mechanisms.

## 1. Exact representation and geometric checks

Let `H=A tensor B tensor C`, let `X_3` be its unit border-rank-at-most-three
states, and let `R_i(pi)` permute four replicas at party `i`. Write `P_lambda,i`
for the local `S_4` isotypic projector. The proposed rejected blocks are
any local `lambda=1111`, and the joint label `(211,211,211)`.
All statements about multiplicity below concern diagonal-`S_4` invariants,
the sector containing every `psi^tensor 4`.

1.1 The character of `V_211` is the sign twist of the three-dimensional
standard representation. On cycle types
`1^4, 2 1^2, 2^2, 3 1, 4`, with class sizes `1,6,3,8,6`, it has values
`3,-1,-1,0,1`. Therefore

`dim (V_211^tensor 3)^(S_4)=(27-6-3+6)/24=1`.

The sign-twisted standard representation has determinant one. Its invariant
volume tensor identifies this unique line with the three-dimensional epsilon
tensor; no antiunitary operation is involved.

1.2 Every four-copy term of a rank-three tensor uses at most three local
colors. Thus local `1111` blocks vanish. The only color content which can
contribute to a local `211` type is `211`: one color repeated and two other
colors occurring once. The transposition of the repeated positions fixes
the local vector. In `V_211` that transposition has eigenvalues `1,-1,-1`,
so its fixed subspace is one-dimensional. All three parties have the same
representation vector `v`, up to their separate Weyl factors. Contracting
`v tensor v tensor v` against epsilon gives zero. Varying local vectors and
taking border limits preserves this vanishing. Hence the proposed rejection
has ideal perfect completeness on `X_3`.

1.3 There is also a short finite certificate that these are exactly the
missing fourth-power blocks, not merely some valid equations. All triple
Kronecker multiplicities of `S_4` are zero or one. For normalized
`GHZ_3=(|000>+|111>+|222>)/sqrt(3)`, the nonalternating, invariant label
triples have the following weights; each row also applies to permutations
of its three displayed labels.

| Labels | Exact weight in `GHZ_3^tensor 4` |
|---|---|
| 4,4,4 | 7/108 |
| 4,31,31 | 5/54 |
| 4,22,22 | 1/54 |
| 4,211,211 | 1/108 |
| 31,31,31 | 11/72 |
| 31,31,22 | 13/216 |
| 31,31,211 | 1/36 |
| 31,22,211 | 1/72 |
| 31,211,211 | 1/72 |
| 22,22,22 | 1/54 |
| 22,211,211 | 1/216 |
| 211,211,211 | 0 |

These are finite integer character sums, not numerical conjectures. A way
to reproduce them is to form, on ternary words of length four,
`N_lambda=d_lambda sum_pi chi_lambda(pi)R(pi)=24 P_lambda`.
The weight for labels `lambda,mu,nu` is
`sum_(u,v) N_lambda[u,v]N_mu[u,v]N_nu[u,v]/(24^3*81)`.
The table accounts for 31 ordered invariant type triples. Every surviving
Weyl tensor factor is irreducible under `GL(A) x GL(B) x GL(C)`, and distinct
local partition tuples are inequivalent. The orbit of `GHZ_3`, whose closure
is the third secant, therefore spans every listed nonzero block. Embedding
the three local coordinates and acting by the larger general-linear groups
extends this conclusion to arbitrary local dimensions at least three.
Smaller dimensions simply remove partitions having too many rows.

1.4 Thus the proposed accepted effect on identical copies is the projector
onto `span{phi^tensor 4:phi in X_3}`. Positivity gives the usual optimality
among four-copy tests with exact perfect completeness. At most three copies
give only trivial such tests: polarization of sums of at most three product
basis vectors spans the full corresponding symmetric powers. This is the
known optimal-span principle specialized to a new equation module, not a
new general testing principle.

1.5 The equations are quartic, not cubic. Their set-theoretic completeness
is supported by [Qi, Theorem 1.3 and Proposition 1.9](https://arxiv.org/pdf/1311.2566):
flattening minors restrict to local supports of dimension three, where
Strassen's original quartics define the required zero set. Qi's general
displayed construction also uses degree-seven minors; the support restriction
is needed when invoking their equivalent quartic version. Theorem 1.4 concerns
all relevant partitions for more parties, not just three fixed blocks.

## 2. A checked example beyond flattening ranks

Take a `3 x 3 x 3` tensor whose three matrix slices are
`I_3, E_12, E_21`, and normalize by `sqrt(5)`. All three flattenings have
rank exactly three. The slice commutator is
`[E_12,E_21]=diag(1,-1,0)`, so a Strassen equation is nonzero.

Independently applying the three exact character projectors gives

`<psi^4, P_211,A P_211,B P_211,C psi^4> = 3/1250`.

On `(C^3)^tensor 4`, `P_211=(1/8)sum_pi chi_211(pi)R(pi)` has rank nine.
The integer computation before normalization gave squared norm `393216`
and denominator `(8^3*25)^2=163840000`, giving the displayed rational value.
This confirms a geometric capability absent from flattening-rank detection.
It does not distinguish the proposal from general invariant measurements.

## 3. Exact known-mechanism reductions and resource costs

3.1 **Weak Schur sampling.** Measure the `S_4` isotypic label locally on each
party. Reject if any label is `1111` or if all three are `211`. This is
exactly the proposed probability distribution, not an approximation and
not a mixture with altered soundness. No coherent representation-coordinate
operation is required: the only decisions are classical OR and AND.
Four copies and a constant-group circuit give `O(log dim A+log dim B+
log dim C)` ideal gates. All these operations are existing Schur-testing
primitives, specialized to the stated partition labels.

3.2 **Sampled polynomial-invariant networks.** The projector coefficient
one-norm is

`L_local=(3+6+3+6)/8=9/4`,
`L=||coefficients of P_211,A P_211,B P_211,C||_1=(9/4)^3=729/64`.

Each term is a product of three known replica permutations. Sample a term
with probability proportional to the absolute value of its coefficient,
measure the real part of its expectation by a controlled-permutation
Hadamard network, and multiply the sign outcome by the coefficient sign
and `L`. The resulting estimator lies in `[-L,L]`, is unbiased for the
joint rejection `p`, and has variance at most `L^2`.
Consequently additive error `epsilon` needs
`O(L^2 epsilon^(-2) log(1/delta))` four-copy trials. Detecting `p>=eta` by
this estimator costs `O(L^2 eta^(-2) log(1/delta))` trials. Its extra power
of `eta^(-1)` must not be omitted when comparing it with rare-event detection.
The permutation networks are explicitly the established framework of
[Leifer--Linden--Winter, §III](https://mattleifer.info/wordpress/wp-content/uploads/2024/06/leifer-2004.pdf).

3.3 **Coherent LCU preserves the rare-signal scaling.** Prepare the constant
term-label distribution coherently, apply its signed controlled permutation,
and unprepare. The zero-flag block is exactly `P/L`, where
`P=P_211,A P_211,B P_211,C` is a projector. Thus its heralding probability
on the four supplied copies is

`||P psi^4||^2/L^2 = p/L^2`, with `L^2=531441/4096`.

Repeated heralding detects `p>=eta` using
`O(L^2 eta^(-1) log(1/delta))` trials, with perfect completeness at `p=0`.
This is constant overhead relative to the proposed projector for every
signal parameter. It needs no input-state inverse, reflection, amplitude
amplification, or uncharged loading oracle. Local alternating tests are
the same construction with coefficient one-norm one. Alternatively the
exact weak-Schur reduction in 3.1 implements their full OR directly.
This closes the signal-scaling loophole left by sampled invariant estimation.

## 4. Soundness and the growing-party boundary

For the exact three-party rejection `r`, local alternating weights satisfy
`e_4(lambda)<=r`. With `tau_3=1-lambda_1-lambda_2-lambda_3`, the probability
that four independent spectral samples are distinct is `24e_4`; each of
the last three fresh choices has conditional probability at least `tau_3`.
Therefore `24e_4>=tau_3^3`.

Projecting onto each top-three support is used only in the proof. For `k`
local factors whose alternating probabilities are each bounded by `r`, its
normalized result is within `sqrt(k)(24r)^(1/6)` in pure-state trace distance.
In the present three-party case `k=3`. Let `g(t)` be the minimum three-qutrit
rejection at distance at least `t` from the third secant, with value one
when that constraint set is empty. The zero-set theorem and compactness give
`g(t)>0`, and real quantifier elimination supplies a certified rational bound.
The same triangle argument as in the second-secant proof gives the valid,
conservative bound

`r >= min{epsilon^6/(1536 k^3), g(epsilon/2)^3/(12^6 k^3)}` for `k=3`.

Indeed the first smallness threshold puts the projected state within
`epsilon/2`, and `sqrt(g)<=sqrt(r)+4sqrt(2k)(24r)^(1/6)
<=12sqrt(k)r^(1/6)`. Constants and preprocessing are dimension-independent
for fixed distance and three parties, but not claimed numerically useful.
The adaptive single-copy lower bound requires a separately adjudicated
product-versus-Haar transfer to the larger third secant; it is not proved here.

For growing party count, choosing a bipartition or tripartition and applying
the corresponding local tests still uses only two or three grouped registers.
Its character coefficient norm remains constant, regardless of the number of
original factors. Random partition sampling therefore does not escape §3.
Qi supplies a zero-set theorem, not an inverse-polynomial lower bound on
the average randomly selected equation signal. If only exponentially few
partitions witness failure, a polynomial gate count per trial does not give
a polynomial-time tester. No such uniform robustness theorem is asserted here.

## 5. Objections and decisions

**T1 — FATAL to D22 originality. Location:** the proposed local-Schur/Strassen
mechanism. **FIX DEMAND:** State the exact reduction in §3, mark any proposed
original-mechanism claim REFUTED, and retain only the stated mathematical and
measurement results. Do not call the detection of non-flattening equations
an original quantum mechanism. **SURVIVING STATEMENT:** The Strassen quartic
projector is informative and efficiently measurable; the measurement is an
explicit application of known Schur or bounded-normalization LCU procedures.

**T2 — MAJOR if extended to a uniform many-party speedup. Location:** proposed
random tripartition generalization. **FIX DEMAND:** Keep it HOLD unless a
quantitative average-signal bound and matched-output comparison are proved.
Charge grouped-replica permutations and total repetitions. **SURVIVING
STATEMENT:** The equations have the cited common zero set and each selected
test is inexpensive; no uniform bound on their average signal follows.

**Constructive boundary, not a candidate algorithm:** a possible next bounded
question is an efficient *joint multiplicity-subspace* measurement when many
local `S_4` factors have type `31`. Unlike the three-party `211` event, its
accepted subspace need not be decided from local labels. To matter for D22 it
would need a proved growing-parameter resource improvement over sampled
constraints, weak-Schur post-processing, and their LCU/filtering realizations.
Neither increasing party count while retaining three grouped projectors nor
increasing degree alone proves such an improvement. The separately proposed
pair-product-span identity and its spectrum are outside this verdict.

Decisions: retain the quartic vanishing, exact three-party block projector,
explicit tensor witness, and fixed-three-party soundness as mathematical
claims for further ratchet/checker archival. ACCEPT the new-mechanism claim
AS REFUTED. HOLD the growing-party speedup and single-copy comparison pending
their actual theorems. No field-wide novelty theorem or impossibility theorem
for other mechanisms is claimed.

Verification used bounded, single-thread Python computations with exact
integer character sums and rational final probabilities. Projector rank,
idempotence, invariant multiplicity, all 64 nonalternating label triples,
and the explicit nonmember were checked. No dedicated registered checker,
mutation run, or hardware implementation was supplied for this review.

**VERDICT: FAIL for a new D22 algorithm; the narrower mathematics survives.**
