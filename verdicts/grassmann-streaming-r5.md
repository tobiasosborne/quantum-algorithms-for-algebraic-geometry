# Independent verdict: streamed Grassmann query comparator

2026-09-05. Review of `scouting/grassmann-streaming-r5.md`.
Verdict: PASS for the stated single-query, real, orthonormal-input comparator.
No outstanding FATAL, MAJOR, or MINOR objections. The precision-accounting
clarification below was applied and verified. This verdict does not certify
any quantum separation or novelty.

## 1. The second moment and the constant 9k

1.1. Let P be the orthogonal projector of rank k, v a unit vector, and
beta=v^T P v. For independent four-wise sign families g,h, define
Z=(g^T P h)(g^T v)(h^T v). Second moments give E Z=beta.
The displayed Rademacher fourth-moment identity is exact under four-wise
independence: no stronger independence is used in any term below.

1.2. Conditional on g, apply that identity to a=P g and b=v:

    E_h Z^2 <= (v^T g)^2*(g^T P g+2(v^T P g)^2).

The first expectation is at most sum_i[1+2(v^T u_i)^2]=k+2 beta.
For the second use a=v, b=P v, whose squared norm and inner product
with v are beta and beta respectively. Its contribution is at most
2 beta+4 beta^2. Hence

    Var Z <= k+4 beta+3 beta^2 <= k+7 <= 8k <= 9k,

for k>=1. The memo's 9k upper bound is conservative and correct.
The statement would need separate handling for k=0, which its bound
already explicitly excludes.

1.3. A group of ceil(36k/epsilon^2) independent copies of the sketch
has mean within epsilon with probability at least 3/4 by Chebyshev.
A median of O(log(1/delta)) independent groups gives the claimed total
O(k epsilon^(-2) log(1/delta)) sketches. Only degree four in each of g,h
is needed; independence between sketches supplies the concentration step.

## 2. Seed storage is genuinely logarithmic in q

2.1. A concrete construction takes s=max(1,ceil(log_2 q)) and distinct
labels x_j in GF(2^s). Choose four uniform coefficients a_0,...,a_3 in
that field and set g_j=(-1)^(Tr(sum_(ell=0)^3 a_ell*x_j^ell)).
At up to four distinct coordinates, Vandermonde evaluation gives
independent uniform field values. Their absolute traces are independent
uniform bits. The seed has exactly 4s bits.

2.2. Use a separate seed for h and independent seed pairs for every
sketch: 8ms bits in total for m sketches. Coordinates can be regenerated
as needed, without storing length-q sign vectors. Straightforward field
arithmetic adds polylog(q) bit-operation overhead per generated sign.
Seed storage is not secretly O(q); a coordinate counter costs O(log q).

2.3. While a vector arrives, the algorithm needs its two running signed
dot products per sketch, in addition to the persistent A values. This
is a constant-factor increase in numeric storage, not O(kq) storage.
At the query it analogously accumulates two query dot products.

## 3. RESOLVED MINOR: make the full bit budget explicit

Observation: the memo correctly bounds each persistent A accumulator by
O(b+log(kq)) bits for exact dyadic data, but group sums and temporary
query products have larger constant denominator exponents and an
additional log(m) term if all accuracy parameters vary.

FIX DEMAND: add a complete conservative bound such as

    O(m*(b+log(kq)+log(m))) working bits,

including seeds, temporary dot products, final products and group sums.
For fixed epsilon,delta and k<=q this is O(k*(b+log q)) bits.
If b=O(log q), it matches the O(k log q) quantum data-register scale.
For larger b, any claim covering all precisions must also justify
rounding to the testing margin or separately account for quantum input
precision and compilation storage.

RESOLUTION: the memo now includes exactly this conservative working-bit
bound, its fixed-error specialization, and the stated large-precision
qualification. The correction satisfies the demand without broadening the
comparator beyond its demonstrated access model.

SURVIVING STATEMENT: the claimed O(m) numeric accumulators and O(m log q)
seed bits are correct. The text says that a memory separation has not
been established; it does not purport to prove a lower bound against
all quantum algorithms or a tight equality of bit budgets for every b.

## 4. Scope of the comparator and quantum description

4.1. The proof applies to a stream and one late query independent of
the private seeds. The query may depend arbitrarily on the input stream
if that stream is independent of the seeds. A fixed list of L such
queries is covered by replacing delta by delta/L, even with reused
sketches. The memo correctly limits its union-bound conclusion to that
situation. It proves no guarantee for unrestricted adaptive queries
chosen from earlier sketch outputs.

4.2. The comparator addresses a geometric incidence bit about a real
Grassmannian point under exact orthonormality and a constant testing
margin. Complex inputs, unstable insertion, nonlinear schemes, and
succinct rotation-circuit input require additional arguments. The memo
does not transfer its conclusion to them.

4.3. The Slater occupation statement is correct: the expectation is
v^T P v, and for incidence values zero or one the occupation measurement
preserves the state. Deterministic insertion requires the promised empty
mode and a proper antisymmetric encoding; the memo explicitly grants
efficient implementation rather than claiming distinguishable-register
appending suffices. Familiar fermionic operations do not establish D22.

The proof audit was algebraic; no unrelated numerical checks were rerun.
The conservative variance bound, explicit finite-field seeds, and finite
bit accounting suffice to accept the claimed comparator in its scope.

Canonical-definition follow-up: D-R5-GRASSMANN-QUERY in
`definitions/mechanism-r5.md` agrees with the reviewed real orthonormal
stream, late seed-independent query, independent four-wise sign pairs,
estimator, separately charged precision, and absence of adaptive-query
robustness. Its per-accumulator bit bound and the memo's complete working
bound are consistent; neither supplies a free quantum preparation inverse.
