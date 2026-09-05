# Independent critic: octonionic associator mechanisms

2026-09-05. Independent review for `qaag-62k` of
`scouting/spinor-mechanism-r7.md`. The completed author memo has been read.
Verdict: PASS after the two MINOR repairs below were applied and verified.
No outstanding FATAL, MAJOR, or MINOR objections remain. No quantum advantage
or originality is accepted.
No claim status is changed by this review.

## 1. Multiplication convention and retained phase

1.1. Use the author's Cayley--Dickson convention
(a,b)(c,d)=(ac-conjugate(d)b, da+b conjugate(c)). For binary labels
a=(a_0,a_1,a_2), b=(b_0,b_1,b_2), the sign exponent is

    F(a,b)=a_0 b_0+a_1 b_0+a_2 b_0+a_1 b_1+a_2 b_1
            +a_2 b_0 b_1+a_2 b_2+a_1 b_0 b_2+a_0 b_1 b_2.

The basis law e_a e_b=(-1)^F(a,b)e_(a+b) has unit label zero,
imaginary squares -1, and the real octonion norm-composition identity.
The two bracketings have respective sign exponents
F(a,b)+F(a+b,c) and F(b,c)+F(a,b+c).

1.2. Expanding their difference over F_2 gives

    delta F(a,b,c)=sum_(pi in S_3) a_(pi(0)) b_(pi(1)) c_(pi(2))
                 =det(a,b,c).

With input labels retained, the ratio of bracketings is therefore the
unitary diagonal phase (-1)^det(a,b,c). It is implemented by six CCZ gates
on nine label bits, or by explicitly computing and uncomputing the
intermediate sum labels. It has success probability one. No map erasing
three labels to their sum is part of this conclusion.

## 2. Coboundary and closed-complex cancellation

2.1. The displayed associator is explicitly a coboundary. Its determinant
formula does not turn it into a nontrivial class of H^3((Z/2)^3,U(1)).
In particular, the fully alternating sum of six cubic monomials must not
be identified with a single-monomial type-III cocycle representative.

2.2. Give a branched triangulation compatible flat edge labels g_ij, so
g_ij+g_jk=g_ik on every triangle. Define the face phase
b_ijk=(-1)^F(g_ij,g_jk). For a tetrahedron 0123 its associator phase is

    b_123 b_023^(-1) b_013 b_012^(-1).

This follows by substituting flatness into delta F. Every interior face
cancels in the product over tetrahedra. On a closed complex the product
is exactly one, even for flat labels with nontrivial global holonomy.
On a manifold with boundary only the known boundary face factors remain.
No cancellation claim is made for incompatible non-flat labels.

## 3. Continuous octonions require a different operation

3.1. The retained phase does not test whether (xy)z=x(yz) for continuous
real octonions. Set x=y=z=8^(-1/2)sum_a e_a. Alternativity gives zero
continuous associator. Nevertheless independent basis measurements have
determinant one with probability |GL_3(F_2)|/8^3=168/512=21/64.
The retained phase mean is then 11/32, not one.

3.2. The actual coefficient map A for the continuous associator has

    A|a,b,c>=[(-1)^(F(a,b)+F(a+b,c))
                 -(-1)^(F(b,c)+F(a,b+c))]|a+b+c>.

Its nonzero columns occur exactly at independent triples. Every nonzero
sum label has 24 such triples, each with coefficient of modulus two;
the zero sum has none. Different rows have disjoint supports. Therefore

    A A^dagger=96*(1-|0><0|),       ||A||=4 sqrt(6).

For the uniform linear implementation K=cA, contractivity requires
|c|<=1/sqrt(96). On real unit product inputs the associator norm is at
most two, by norm composition and the triangle inequality, and that bound
is attained on a suitable independent basis triple. Hence K=A/sqrt(96)
has success probability at most 1/24 on those inputs.
This is a statement about that linear contraction, not a universal
lower bound on every procedure using arbitrary extra input copies.

3.3. The proposed row-isometry implementation is mathematically valid.
Its seven normalized signed 24-term rows are orthonormal; extending their
preparation to a nine-qubit unitary and inverting it realizes K when the
workspace is clean and the coarse output is nonzero. The flag must not
measure which nonzero output label occurred. If P=K^dagger K, the failure
effect is 1-P, not a restored unknown product input. The stated trials
prepare fresh source triples and do not claim free recovery.

3.4. P is a real rank-seven projector. Pairing two sites within each
of the three sources produces, after reordering, the maximally entangled
vector in C^512 tensor C^512. Its two-filter acceptance is
Tr(P P^T)/512=7/512, as claimed. This changes the across-use input
correlations; it does not contradict the scoped real-product one-use bound
or describe two independent copies of an arbitrary unknown triple.

## 4. Matched scalar-output attacks

4.1. For any diagonal sign phase D and any input density operator rho,
Tr(rho D)=sum_z rho_(z,z) D_(z,z). Measuring z in the computational basis
and returning its classical sign reproduces the entire binary outcome
distribution of a fresh-copy Hadamard test of this real mean.
For product sources their labels can be measured separately. This does
not simulate a later arbitrary coherent readout or preserve the source.

4.2. If a classical hypergraph description gives a cubic phase f(z) and
a linear query ell(z), write B=E_z[(-1)^(f(z)+ell(z))]. The zero Fourier
output probability after H D_f H, with the linear query incorporated,
is B^2. For the promise B^2=0 versus B^2>=gamma, estimate B to additive
sqrt(gamma)/3 and threshold its absolute value at sqrt(gamma)/2.
Hoeffding gives O(gamma^(-1) log(1/delta)) classical samples, with the
same phase-evaluation cost as one circuit trial. This matches direct
rare-event sampling of B^2 up to constants. Estimating B^2 directly by a
generic gamma-precision bounded estimator would give a weaker baseline.

4.3. For an arbitrary additive epsilon estimate of B^2, independent of a
zero-versus-gap promise, estimating B to epsilon/2 is sufficient because
|B_hat^2-B^2|<=2|B_hat-B| when both estimates are in [-1,1].
The resulting uniform worst-case bound is O(epsilon^(-2) log(1/delta)).
The distinction between these two precision tasks must be preserved.

4.4. Full Fourier-output sampling is a different problem. A network of
the determinant phases is a commuting cubic diagonal circuit; sandwiching
it between Hadamards gives the established IQP construction. A scalar
Monte Carlo estimator does not sample its full distribution. Conversely,
calling the circuit an associator does not establish a new mechanism or
inherit a hardness theorem for every restricted determinant network.

4.5. The second growing problem averages squared associator norms over an
explicit list. Each row residual lies in [0,4], so a positive average at
least gamma implies at least a gamma/4 fraction of nonzero rows. Random
exact row evaluation therefore has the asserted O(gamma^(-1)) trial bound.
Fixed-degree rational expressions have O(B) coefficient bit-length growth;
this is not a unit-cost claim for arbitrarily long rational inputs.

4.6. The copies-only fixed-dimension comparator is also valid. Estimate
the real density entries of each source to a sufficiently small constant
times sqrt(gamma). Dimension eight makes this a fixed number of bounded
observables. The rank-one spectral gap gives a normalized real eigenvector
estimate with O(sqrt(gamma)) error, up to sign. Telescoping the associator
over the three unit inputs bounds its norm error by twice the sum of these
three errors. This distinguishes zero from norm at least sqrt(gamma)
with O(gamma^(-1) log(1/delta)) copies per source, with fixed constants.
It is an allowed separate-source strategy, not an optimality theorem.

## 5. RESOLVED MINOR repairs from the final read

5.1. Fixed-dimensional row preparation versus gate synthesis.

FIX DEMAND: the signed 24-term row unitary is constant-dimensional, but
the required amplitudes do not imply an exact constant-size Clifford+T
circuit. State a fixed ideal-rotation circuit and explicitly include
O(polylog(1/eta)) finite-gate-set synthesis cost per folded-filter trial,
with eta=O(delta/M) for M attempts. Retain the exact constant Clifford+T
statement for the separate six-CCZ phase construction.

SURVIVING STATEMENT: the ideal K=A/sqrt(96), its norm, success probability,
and the fresh-source trial bound are correct. The repair charges numerical
gate accuracy without changing the mathematical filter or its disposition.

RESOLUTION: section 6 now explicitly gives C_K(eta)=O(polylog(1/eta))
synthesis cost and O(eta) operator/instrument errors. Section 7 multiplies
indexed access, three source preparations, and C_K by the trial budget M,
with eta=O(delta/M). The correction satisfies the demand.

5.2. Parameter range in the nonempty star diagnostic.

FIX DEMAND: the star family has b_0=11/32 and p_0=121/1024; explicitly say
that its exhibited positive and zero alternatives instantiate the promise
for fixed 0<gamma<=121/1024. The displayed positive point does not meet a
larger threshold merely because the full problem allows gamma up to one.

SURVIVING STATEMENT: for v>=4, multilinearity gives
f=det(a_1,a_2,sum_(i>=3)a_i). The sum of the independently uniform leaves
is uniform, giving b_0=11/32. Unequal frequency labels on two leaves admit
a simultaneous translation that fixes f and flips the character, so the
corresponding Fourier mean is zero. The family is a valid growing diagnostic.

RESOLUTION: the star paragraph now states the exact fixed range
0<gamma<=121/1024 and retains v>=4 for the two-leaf argument.

## 6. Independent verification and references

6.1. A bounded inline computation with one BLAS thread passed 34,580
exact checks: all 512 coboundary identities in the author's convention,
the real norm-composition quartic coefficients, the multiplication and
associator operator norms, the continuous-associator counterexample, and
all 8^5 vertex labellings of the boundary of a four-simplex. Violations
would terminate the computation nonzero. This is supporting evidence,
not a production checker or a global novelty certificate.

6.2. After the derivation, primary PDFs were fetched. Albuquerque--Majid,
[arXiv:math/9802116](https://arxiv.org/abs/math/9802116), explicitly identify
the octonion cocycle as a coboundary in the introduction and develop the
cochain twist. Bremner--Jozsa--Shepherd,
[arXiv:1005.1407](https://arxiv.org/abs/1005.1407), treat commuting IQP
computations. These sources support the specific known-mechanism checks;
they do not prove efficient sampling of every later quantum readout.
The author's more specific source, Bremner--Montanaro--Shepherd,
[arXiv:1504.07999](https://arxiv.org/abs/1504.07999), was also fetched: its
degree-three polynomial-gap construction directly matches the circuit and
normalized gap readout being identified here.

The accepted surviving content is the retained-label phase and its exact
IQP reduction, the matched scalar geometric comparator, and the separate
continuous associator contraction with its scoped activation and resource
accounting. The closed-flat bulk phase is trivial. The first construction
uses a known mechanism; the second establishes no matched advantage.
Nothing in this verdict completes the campaign's original-algorithm goal.

## 7. Canonical-definition and claim integration audit

2026-09-05. Scope-only follow-up, with no new numerical campaign.
Integration verdict: PASS for `definitions/octonionic-operations.md` and
the proposed C-357/C-358 statements in `claims/CLAIMS.md`. No outstanding
FATAL, MAJOR, or MINOR integration objections remain. The rows were SKETCH
when inspected; this audit edits neither their status nor any shared file.

7.1. D-OCTONION-CONVENTION preserves the accepted Cayley--Dickson basis,
bit ordering, polynomial F, complex-linear A, K=A/sqrt(96), and projector P.
The positive coefficient metric and restriction of real norm composition
are explicit. C-357 keeps the deterministic phase separate from the
continuous associator and restricts the closed-complex identity to
compatible flat labellings. No nontrivial bulk cohomology class is introduced.

7.2. D-OCTONION-PHASE-QUERY retains a sparse classical equation and fixed
frequency y, with p_y=b_y^2 and 0<gamma<=1. Its full sampling output is
separate from the scalar promise problem. C-357 preserves the unsquared-mean
classical attack and identifies the complete circuit as cubic-phase IQP,
without claiming a general sampler or transferring generic IQP hardness.
The memo separately handles y=0; its hyperplane formula requires y!=0.
The definition also preserves the attainable-margin qualification for
individual subfamilies, including the repaired star diagnostic.

7.3. D-OCTONION-CONTINUOUS-QUERY and C-358 keep three distinct access
models separate: one real-product use of K, the explicit rational list,
and the three sources with paired sites for the tensor diagnostic.
The 1/24 ceiling is not extended to complex/entangled inputs or declared
multiplicative. The 7/512 example retains its across-use correlations.
The list and one-triple copies-only comparators remain concrete upper
bounds, with 0<gamma<=4, rather than tomography optimality claims.
Indexed access, preparations, arithmetic and finite-gate synthesis remain
charged; no whole-list coherent oracle or preparation inverse was added.

7.4. RESOLVED MINOR: failure-probability quantifier.

FIX DEMAND: the initial phase definition allowed all 0<delta<1, whereas
the integrated rows quoted O(gamma^(-1) log(1/delta)) for the displayed
ceiling/Hoeffding budgets. That expression does not uniformly absorb the
constant sample overhead as delta approaches one. The continuous query
also needed its own explicit failure-probability range.

RESOLUTION: both canonical query definitions now explicitly impose
0<delta<=1/3, including the inherited one-triple copies-only variant.
On that range log(1/delta) is bounded below by a positive constant,
so the accepted trial/sample bounds have the quoted uniform asymptotic
form. The correction was read and verified in the canonical file.

SURVIVING STATEMENT: all displayed elementary formulas, algorithms,
success probabilities, and matched margin exponents are unchanged.
The narrower explicit failure range closes the quantifier issue without
expanding any input model or implying advantage or originality.
