# Independent verdict: direct programmable Waring point test

2026-09-05. Reviewed the completed `scouting/waring-programmable-tester.md`,
the updated D-WARING-DIRECT-POINT-TEST definition and C-347, and the literal
checker `checkers/explore/waring_programmable_test.py`. The classical lower
bound is imported from the previously adjudicated C-345 task. Only this
verdict is written by the reviewer; no claim status is changed.

**VERDICT: PASS after the positive-effect repair P1.** No FATAL or MAJOR
objection remains. The direct experiment has the stated exact zero case,
uniform event lower bound, deterministic source count, and unchanged terminal
output. It substantially improves the quantum upper bound without preparing
a balanced mixture or growing coded packets. Its mechanism remains a
composition of known comparison/programming and point-test operations; this
verdict does not establish D22 originality or global optimality.

## 1. Exact source expansion and register accounting

1.1 The source assumptions are the independent-component, normalized Waring
family with `r>=2`, `k>=3`. The first alternation uses slot one from each
of the first r originals. The second uses slot two of source rows 2 through r
and slot one of the extra original. The target uses slots 2 through k of
source row one and of that extra original. These are disjoint physical
register sets. The target therefore has exactly `2k-2` slots; every remaining
program row has `k-2`. A chosen h-slot point effect is allowed when
`1<=h<=2k-2` and does not overlap either alternating measurement.

1.2 For a permutation pi of the r component labels,

`P_alt,r(u_(pi1) tensor ... tensor u_(pir))`
` =sgn(pi) sqrt(det G/r!) omega`,

where omega is the normalized ordered wedge of all components. The first
alternation therefore gives the unnormalized coefficient
`c_prod sqrt(det G/r!)` times omega and an alternating permutation sum
of the remaining `k-1`-slot rows. No packet normalization is performed.

1.3 The second alternating input has component order
`pi(2),...,pi(r),a`. It vanishes unless `a=pi(1)`. For that surviving
label its sign is `(-1)^(r-1)sgn(pi)`, cancelling the first permutation
sign up to the stated fixed global factor. Its wedge factor is again
`sqrt(det G/r!)`.

1.4 Consequently the state after both accepting projector outcomes is
exactly

`(-1)^(r-1)c_prod(det G/r!) omega tensor omega`
` tensor sum_pi c_(pi1) u_(pi1)^(2k-2)`
`                         tensor_(i=2)^r u_(pii)^(k-2)`.

The determinant prefactor is neither its square root nor divided by a
second factorial. Both wedge registers factor from the retained data and
may be discarded. The identity and the remaining coherent sum hold for
complex coefficients and nonorthogonal components.

1.5 The actual algorithm can simply take all `r+1` copies and record the
three accepting flags. Because the measurements have disjoint support,
their order does not affect the event probability. Intermediate conditional
states are proof devices, not unprovided reference states or preparation
oracles. There is no stochastic packet-building subroutine in one shot.

## 2. Point effects and prevention of coherent cancellation

2.1 The canonical statement now correctly permits a positive contraction Q
as a supplied measurement's accepting POVM effect. In the proof put

`t_pi=(sqrt(Q)u_(pi1)^h) tensor u_(pi1)^(2k-2-h)`,
`v_pi=tensor_(i=2)^r u_(pii)^(k-2)`.

Then `||t_pi||^2=f_(pi1)`. The square root is only a factorization of
the effect; the algorithm does not receive or require its preparation or
block encoding. The exact joint probability is

`p_event=|c_prod|^2(det G/r!)^2`
`                    ||sum_pi c_(pi1)t_pi tensor v_pi||^2`.

If all f_a vanish, every proof vector vanishes and the event is exactly
impossible. This gives ideal perfect completeness for the terminal YES case.

2.2 For every integer m>=1, the unit-diagonal Gram promise gives
`G_m>=eta I`. At the induction step,
`G_m-eta I=(G-eta I) circ G_(m-1)>=0` by the Schur product theorem.

2.3 The ordered program tuples `(pi(2),...,pi(r))` are all distinct; each
determines its missing first label. Their Gram matrix is a principal
submatrix of `G_(k-2)^tensor(r-1)`, so it is at least
`eta^(r-1)I_(r!)`. This is where `k>=3` is essential: at k=2 all program
vectors would be scalar and the full-rank bound would fail.

2.4 If A maps an orthonormal permutation label to its program vector, then
`A^dag A>=eta^(r-1)I`. Apply `I tensor A` to the labeled target sum to get

`||sum_pi c_(pi1)t_pi tensor v_pi||^2`
` >=eta^(r-1)(r-1)! sum_a |c_a|^2 f_a`.

This lower bound controls all complex cross terms as an operator inequality.
It does not assume they are individually positive. It proves that a violated
component cannot be hidden by cancellation in the coherent program sum.

## 3. The uniform coefficient and exact zero characterization

3.1 Normalization of the original source means `c^dag G_k c=1`, hence
`sum_a|c_a|^2<=1/eta`. Also both unit-diagonal Gram determinants in
`p_seed=|c_prod|^2 det G det G_(k-1)` are at most one, so
`|c_prod|^2>=p_seed>=p_*`.

3.2 For each a, arithmetic--geometric means on the other r-1 coefficients
gives

`prod_(b!=a)|c_b|^2 <= [1/(eta(r-1))]^(r-1)`,
`min_a |c_a|^2 >= p_*[eta(r-1)]^(r-1)`.

This uses the promised seed probability and normalized coefficient bound;
it does not assume bounded coefficients before normalization or ignore
destructive cancellation in the source.

3.3 Keep one seed factor intact:

`|c_prod|^2(det G)^2=p_seed det G/det G_(k-1)>=p_* eta^r`.

Combining this with §2.4 and the minimum-coefficient bound, then using
`sum_a f_a=r Gamma` and `r(r-1)!/(r!)^2=1/r!`, yields exactly

`p_event >= Kappa Gamma`,
`Kappa=p_*^2 eta^(3r-2)(r-1)^(r-1)/r!`.

The exponent `3r-2` comes from `r+(r-1)+(r-1)`. Bounding the two determinant
factors separately would lose an unnecessary power of eta. Since Kappa is
positive, this also proves the registered iff statement: the event vanishes
exactly when every f_a vanishes under the supplied promises.

3.4 For general overlapping components, the event is not an unbiased known
multiple of Gamma. Only its zero case and lower bound are used in the
decision rule. The memo and C-347 correctly preserve this distinction.

## 4. Deterministic runtime, precision, and numerical constants

4.1 For `0<delta<1`,
`S=ceil(log(1/delta)/(Kappa gamma))` independent shots give zero ideal
YES error and at most delta ideal NO error. Each shot consumes exactly
`r+1` originals. There is no unknown-success stopping threshold, Markov
budget, or omitted seed-retry cost: every unsuccessful seed or guard is
already included as a zero-event shot.

4.2 Per shot, count two alternating measurements, the supplied point
measurement, source generation when provided, and the declared register
handling. In symbols, its non-source work is bounded by
`2 C_alt(r,q)+C_Q+O((r+1)k log q)`, with all measurement precision included.
At the terminal fixed values r=k=4 and h=5, the point measurement is the
known five-register exterior test and this dependence is polynomial in
`log q`. No generic efficient implementation for an arbitrary costly Q is
being inferred. Optional source workspace/cost retains the source definition's
separate accounting.

4.3 The finite-precision rule is sound: set ideal miss error delta/2 and
allocate at most delta/2 to the entire fixed circuit's output-distribution
error. The known shot count bounds the total number of internal operations.
All three flags are retained in the event definition, so this comparison
does not divide the simulation error by a tiny conditional success probability.
Ideal perfect completeness becomes bounded two-sided error after synthesis.

4.4 Exact rational simplification gives `Kappa=9/2^31` in the C-345 setting.
Independent 90-digit recomputation verifies all displayed ceiling counts:

| Setting | Shots | Original source copies |
|---|---:|---:|
| Uniform promises, ideal miss 1/3 | 262,139,102,822,958 | 1,310,695,514,114,790 |
| Uniform promises, ideal miss 1/6 plus implementation budget | 427,530,462,368,490 | 2,137,652,311,842,450 |
| Orthogonal balanced family, ideal miss 1/3 | 26,999,495,607 | 134,997,478,035 |

4.5 For orthogonal balanced components the program vectors are orthonormal.
The residual squared norm becomes `(r-1)! Gamma`, and
`|c_prod|^2=r^(-r)`. Thus

`p_event=Gamma/[r^(r+1)r!]`,

including the rank-four denominator 24,576. This is an exact special-family
formula; it cannot replace the general coefficient Kappa. The new constants
are much smaller than the recursive-packet budget but remain impractical
for a direct experiment at the stated tiny residual threshold.

## 5. Same terminal problem and known mechanism

5.1 With h=5 and Q alternating the internal A registers, f_a is exactly
`e_5(Tr_B |u_a><u_a|)`. The source promises, supplied internal bipartition,
Gamma threshold, and one-bit output are the same as D-WARING-TERMINAL-QUERY.
The method works for the general allowed overlapping/nonorthogonal sources,
not merely the hard subfamily. Internally obtained program registers are
charged source data, not externally supplied component references.

5.2 Therefore the previously audited C-345 lower bound transfers unchanged:
any stipulated adaptive global single-original-copy comparator needs
`N>=q^(1/4)/(4sqrt(24))`. This proof does not need to be redone or strengthened
because the quantum upper changed. The current joint measurements cross
original source copies, while the lower-bound comparator cannot preserve
quantum information between them. Its arbitrary within-copy global POVMs
remain allowed. No tomography, coordinate-list, or altered-output comparison
has been substituted.

5.3 The operational prior comparison is correctly scoped. The second guard
is the fixed-index antisymmetric effect used in programmable unambiguous
discrimination; [Zhang--Ying, equation (4) and Theorem 1](https://arxiv.org/pdf/quant-ph/0606189)
provide the determinant law and the relevant support condition. The complete
multi-index discriminator's scaling is not invoked: a single chosen projector
and its complement form a valid binary measurement. Its action on coherent
program permutations follows by linearity. The first comparison and the
terminal exterior measurement are likewise known operations.

The direct experiment is therefore a valid, shorter mathematical upper bound,
not an originality certificate, a claim that programmable references were
provided for free, or a proof of optimal original-copy complexity. This audit
does not reconsider or reverse the campaign's D22 disposition.

## 6. Additional scoped perfect-completeness batch lower bound

The root proposed this additional statement during the review. It concerns
the existing rank-four/order-four terminal problem only; it is separate from
the total-copy lower bound and is not a claim about two-sided-error tests.

6.1 Let `V=C^d tensor C^d`, `W=Sym^4 V`, and let X be the cone of matrices
of rank at most four. Put `Y={u^4:u in X}`. This Y spans W: choose any
four rank-one matrix units. Every linear combination of them has matrix
rank at most four, and polarization of its fourth power gives their
symmetrized tensor product. Such products span W.

6.2 For `ell<=4`, powers of sums of at most ell spanning Y points polarize
to every elementary symmetric tensor on W. Thus the ellth-power span of
`sigma_4(Y)` is all of `Sym^ell W`: this secant has no nonzero homogeneous
equations of degrees one through four.

6.3 The conditioning promises do not defeat this algebraic statement.
The parameter space `X^4 times C^4` is irreducible. Choose four normalized
rank-exactly-four bipartite components on mutually disjoint four-dimensional
supports, with equal coefficients. This is a smooth component-parameter
point with `G=I` and `p_seed=1/256`, strictly inside both promises.
A relative Euclidean-open neighborhood stays inside the promises after
normalizing components/source and absorbing their scales into the coefficients.
All its components still belong to X. Homogeneous polynomials in T which
vanish on promised YES sources consequently vanish on this open parameter
set, hence identically on the irreducible parameterization and its secant
closure. Zero coefficients and dependent limits may enter that closure;
they need not themselves satisfy the operational promises.

6.4 An ell-copy effect with exact perfect completeness has rejecting square
root K satisfying `K T^ell=0` on every promised YES input. Each coordinate
of this vector is a homogeneous degree-ell polynomial in T. By 6.3 and 6.2,
K vanishes on `Sym^ell W` for `ell<=4`. Therefore the test accepts every
pure vector of W. The direct five-copy event is nontrivial and has ideal
perfect completeness, so five is the minimum nontrivial batch size under
that restriction. This is not a minimum total number of copies for bounded
error, nor a lower bound for tests allowed nonzero completeness error.

The argument uses the established perfect-completeness span principle of
[Lovitz--Lowe, Lemma 2.1](https://arxiv.org/html/2410.21417v2#S2.SS3.SSS1);
it supplies no new mechanism or historical-priority claim.

## 7. Resolved objection and claim decision

**P1 — MAJOR, RESOLVED. Location:** the original §1/§3 proof versus the new
canonical positive-contraction definition. The first memo restricted Q to an
orthogonal projector and used `Q u^h` as a proof vector; C-347's definition
had already broadened it to any positive contraction. Its squared norm would
then be `<u^h,Q^2u^h>`, not the claimed f_a.

**FIX DEMAND:** Specify a supplied accepting POVM effect Q with charged
measurement implementation, and use `sqrt(Q)u^h` only in the proof. A block
encoding of the linear operator Q by itself measures Q squared on heralding.
**SURVIVING STATEMENT:** The general-effect event formula and lower bound
hold without a square-root oracle; the terminal projector case was already
correct. **VERIFIED REPAIR:** The final memo and canonical definition now
make precisely these distinctions.

Accept D-WARING-DIRECT-POINT-TEST and C-347 as mathematically supported for
the claims ratchet, including their general positive-effect scope after P1.
The shorter upper uses no coded-packet growth or approximate marginal lemma.
The C-345 lower bound remains the same. No source-state generation advantage,
unbiased general residual estimator, balanced-mixture output, historical
novelty, or new-mechanism claim is included in this acceptance.

Independent bounded verification used one BLAS thread and a 60-second timeout.
41 checks passed for literal full source vectors and their global signs,
factorials, Gram floors, coefficient bounds, and shot counts. A further
nonprojector-effect fixture gave literal event `0.020064912155526103`,
matching the repaired sqrt(Q) proof `0.020064912155526114`; the unrepaired
Q-vector formula instead gives `0.013617766826806404`. The root's registered
73-check script and recorded three red mutations were inspected, not silently
represented as the reviewer's own rerun. No noisy implementation was tested.

**VERDICT: PASS — C-347's direct terminal upper bound is supported at the
stated access and promises; no D22 promotion follows.**
