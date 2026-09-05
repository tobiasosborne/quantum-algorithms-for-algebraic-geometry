# Independent audit of the theta-isogeny construction

2026-09-05. Reviewed scouting/theta-isogeny-r6.md and the three entries in
definitions/theta-isogeny.md. The normalization and sector map were derived
independently before reading the completed author memo or browsing prior art.
Root owns tracking and any claims-register promotion.

**Verdict: PASS for the exact operation, parity split, and scoped
scalar/sampling attacks, including the canonical definitions and C-353/C-354.**
No outstanding FATAL, MAJOR, or MINOR remains. The three phase/scope/margin
repairs in §7 have been applied and independently verified.
This verdict does not establish an original quantum mechanism or a speedup.

## 1. Gaussian metric and actual pullback normalization

Use the author's half-integer characteristics $\alpha,\beta$, with
$\sigma=2\alpha$ and $\delta=2\beta$ binary. In a theta series write the
frequency as $n m+j+\alpha$. Integrating the squared norm over the real
$x$ coordinates annihilates every cross-frequency term. For a fixed basis
index, completing the square leaves

\[
 \sum_{m\in\mathbb Z^g}\int_{[0,1]^g}
 \exp[-2\pi n(m+y+(j+\alpha)/n)^TY(m+y+(j+\alpha)/n)]\,dy.
\]

The translated integration cells tile $\mathbb R^g$. The integral is
$\det(2nY)^{-1/2}$, independent of the index and the unitary flat twist.
Different basis indices are orthogonal by the same frequency argument.
Thus multiplying each theta section by $\det(2nY)^{1/4}$ gives the stated
orthonormal basis under normalized Haar measure.

The Gaussian metrics satisfy the parallelogram identity under
$\mu(P,Q)=(P+Q,P-Q)$. Haar probability measure pushes forward to Haar
probability measure under this finite surjective torus homomorphism.
Pullback is consequently an isometry within each stated flat sector.
No factor equal to the degree $4^g$ is inserted into this probability-measure
normalization.

Both level-$k$ factors carry the same twist
$F_{(\alpha,\beta)}$. Pullback makes their flat factors trivial because their
multipliers square or cancel along the two input lattice directions.
This proves the claimed twist placement; replacing only one factor by a
twisted section would not give the displayed map.

## 2. Independently derived finite matrix, including odd levels

Take lower-level frequencies
$p=km+j+\alpha$ and $q=kn+l+\alpha$, and put $a=p+q$, $b=p-q$.
The quadratic form splits as

\[
 p^T\Omega p+q^T\Omega q
 =\tfrac12(a^T\Omega a+b^T\Omega b).
\]

This uses symmetry of $\Omega$ and does not require a diagonal period matrix.
The integers $m+n$ and $m-n$ have the same parity $\epsilon$.
The flat-character contribution is
$\exp[\pi i\,\delta\cdot(j+l+\sigma+k\epsilon)/k]$.
The ratio of the two orthonormalization factors is $2^{-g/2}$.
These calculations give exactly the columns in the author's equation (4).

For any input indices $a,b$, the inverse arithmetic is

\[
 \sigma=(a+b)\bmod2,\quad
 j=((a+b-\sigma)/2)\bmod k,\quad
 l=((a-b-\sigma)/2)\bmod k.
\]

The remaining canonical bit is
$\epsilon=[a-j-l-\sigma]_{2k}/k$. Its numerator is zero or $k$.
These equations give a bijection of the computational bases for even and
odd $k$ alike. The phase and a binary Walsh transform complete the unitary.
In particular, no modular inverse of two modulo even $k$ is assumed.

The phase can be compiled by reversibly accumulating
$\delta\cdot(j+l+\sigma)$ modulo $2k$ and applying the resulting rational
phase. Thus period-independent arithmetic and phase-synthesis costs are
consistent with the memo; a period-dependent matrix is not hidden inside
an abstract change of theta basis.

## 3. Conjugated evaluation states and sector weights

Conjugating the section pullback identity, with the declared fibre frames,
gives

\[
 J^\dagger(e_{2k}(P)\otimes e_{2k}(Q))
 =\bigoplus_\xi e_k^\xi(P+Q)\otimes e_k^\xi(P-Q).
\]

The direction is $J^\dagger$, as the memo states. Squared norms then give
the exact Bergman-density identity and the probabilities

\[
 w_\xi=
 \frac{B_k^\xi(P+Q)B_k^\xi(P-Q)}
 {B_{2k}(P)B_{2k}(Q)}.
\]

No finite-level density is taken to be constant. Zero low-level evaluations
produce zero sector probability; normalized conditional states are asserted
only on positive-weight sectors. The normalized off-diagonal kernel identity
also follows, provided the common lift/frame conventions are retained.
At a zero weight it is interpreted via the unnormalized identity, as required.

For the elliptic period $\Omega=i$, $k=1$, and $P=Q=0$, independent evaluation
gave $(1/2,1/4,1/4,0)$ in the stated characteristic order.
The last entry is the odd theta zero, not an omitted failure branch.

Expansion of the characteristic shows that its interpretation as an ordinary
theta state is at
$z+d_\xi$, $d_\xi=(\Omega\alpha+\beta)/k$, up to a phase.
The Gaussian prefactors give $B_k^\xi(z)=B_k(z+d_\xi)$.
This is not a same-point correction. The global basepoint-free restriction
needed for the stronger correction obstruction is now explicit; see §7.

## 4. Exact Weyl reduction and the separate-source comparator

For one high-level coordinate, $Z^k$ and $X^k$ are Hermitian involutions,
with commutation sign $(-1)^k$. On the two sources the signs cancel.
The resulting $G_r,H_r$ therefore commute for every $k$, including odd $k$.
Every column of $J$ has their eigenvalues
$(-1)^{\sigma_r},(-1)^{\delta_r}$. Character orthogonality proves equation (12).
The remaining output labels are the explicit basis decoding, with its known
phase. This is a substantive simultaneous finite-Weyl measurement reduction.
At $k=1$ it is the usual Bell measurement.

The proposed single-source observable is also correct:

\[
 W_{s,t}=i^{k s\cdot t}Z^{ks}X^{kt},\qquad
 W_{s,t}^\dagger=W_{s,t},\qquad W_{s,t}^2=\mathbb1.
\]

Since $W_{s,t}\otimes W_{s,t}=(-1)^{k s\cdot t}G^sH^t$,
the signed product of the separately measured outcomes is unbiased for
$w_\xi$ after uniform averaging over $s,t$.
It has magnitude at most one, giving the stated
$O(\gamma^{-2}\log(1/\delta))$ additive-estimation cost.
This uses arbitrary within-source measurements and classical processing;
it does not require tomography or amplitude queries.

The direct joint event uses $O(\gamma^{-1}\log(1/\delta))$ pairs.
The separate-source estimator does not match its rare-event dependence,
sample the full sector law, or prove an optimal lower bound in $\gamma$.
The memo now states those limitations.

The stronger parity split added in §5.3a is exact. For even $k$, the local
operators $Z_r^k,X_r^k$ already commute on each individual source.
Let $Q_\lambda$ be their local joint spectral projectors. Then

\[
 \Pi_\nu=\sum_\lambda Q_\lambda\otimes Q_{\lambda\oplus\nu}.
\]

Separate local measurements followed by eigenbit XOR therefore sample the
entire sector string with one source pair. Refining the sector measurement
this way may destroy within-sector coherence; the result is correctly limited
to the classical sector distribution.

For odd $k$, the Chinese-remainder map is the phase-free permutation
$|a\rangle\mapsto|a\bmod2\rangle|a\bmod k\rangle$.
It sends $Z^k$ exactly to logical $Z$ and $X^k$ exactly to logical $X$:
adding odd $k$ flips parity and fixes the residue modulo $k$.
The spectator factor is untouched. For $g$ coordinates, the sector projector
is a Bell projector on the $g$ logical qubits, tensored with spectator
identity. Independent source registers give logical marginals $\rho,\sigma$
in a product state even when each is mixed from its own spectator.
For an appropriate known Pauli $V$ and $d=2^g$,

\[
 w_\xi=d^{-1}\operatorname{Tr}(\rho^T V\sigma V^\dagger)
 \le d^{-1}.
\]

The inequality follows from $0\le\rho^T\le\mathbb1$ and
$\operatorname{Tr}\sigma=1$. This extends the level-one probability ceiling
to every odd $k$. These are direct operator identities; no extra numerical
campaign was needed for the extension.

At $k=1$, the section defining each $D_\xi$ is symmetric up to its parity
sign. The union of the two pullback divisors is therefore invariant under
interchanging $P+Q,P-Q$ and simultaneous sign changes, so it respects the
stated level-two sign ambiguity.

## 5. Full classical sampler under explicitly different access

Let the two normalized coefficient vectors be $A,B$. Independently sampling
their computational indices selects a common $+k$-shift orbit with mass

\[
 S_{\sigma,j,l}=
 \sum_{\epsilon\in\{0,1\}^g}
 |A_{[j+l+\sigma+k\epsilon]_{2k}}
  B_{[j-l+k\epsilon]_{2k}}|^2.
\]

These are exactly the orbits of fixed $(\sigma,j,l)$. Querying their
$2^g$ product amplitudes and applying a normalized Walsh transform produces
the conditional distribution of $\delta$. The extra output phase has modulus
one. Multiplying this conditional law by the sampled orbit mass gives exactly
the complete decoded computational law of $J^\dagger(A\otimes B)$.
This proof applies to arbitrary product source vectors, not only theta states.

The canonical enumeration in current §5.4 is essential for its exact
amplitude formula. Enumerating from the initially sampled pair instead would
insert an additional known $\delta$-dependent sign. Probabilities would still
be correct; §7 records the repaired wording.

The $O(g2^g)$ arithmetic and $O(2^g)$ coefficient-query and numeric-memory
costs are valid, in addition to label arithmetic and access precision.
The dense finite-precision statement is sufficient: use consistently sampled
approximations to each normalized input vector with Euclidean error $O(\eta)$.
Their product state has error $O(\eta)$; unitarity and measurement cannot
increase the resulting trace-distance/total-variation bound.
Uniform entry error $O(\eta/\sqrt N)$ suffices for that input approximation.
No lower bound on each individual orbit mass is needed in this consistent
approximation model.

This sampler does not supply amplitude queries from quantum copies. Nor does
it simulate an arbitrary later quantum circuit or reproduce the coherent
output state. The dense-data cost comparison is an access audit, not a lower
bound against every amortized QRAM or state-preparation model.

## 6. Source, period and normalization costs

The cheap gate list contains neither $\Omega$ nor a lattice Gaussian
summation. The period, point data, marking, numerical conditioning and
coefficient normalization live in the supplied source or its preparation.
The memo charges this source cost for every fresh pair.
Copy access does not include an inverse preparation circuit.

For classical point/period input, normalization of a raw approximate theta
vector requires precision relative to its norm. This requirement is stated.
Direct classical theta evaluation provides the same weights where such
evaluation is efficient; no unproved best-classical complexity assertion is
made for general high-genus coupled sums.
An explicitly non-product $\Omega$ does not alter the finite matrix $J$.

The physical diagnostic is an MBQC Bell-basis circuit at level one.
It correctly charges input injection and does not assume a deterministic
passive-optical Bell analyzer without further resources.

## 7. Objections and repairs

**RESOLVED MINOR O1 — same-point correction requires a global morphism.**
The phrase about a complete linear series defining a projective morphism
could be read as only a rational map away from its base divisor.
At level one, the normalized section space is one-dimensional away from its
zero divisor and admits a trivial ray correction there.

**FIX DEMAND:** Require global basepoint-freeness for the pullback-of-$O(1)$
argument, and exclude the level-one space from that obstruction.
**RESOLUTION:** Current §4.2 contains both qualifications.
**SURVIVING STATEMENT:** For a globally basepoint-free complete series, a
universal same-point projective-unitary correction would imply preservation
of $L^k$ by the specified translation. The asserted nontrivial flat twists
do not satisfy that preservation condition.

**RESOLVED MINOR O2 — declare the orbit origin for the amplitude formula.**
A Walsh transform enumerated from a sampled pair differs from the canonical
enumeration by a sign $(-1)^{\delta\cdot\epsilon_0}$.
For example $g=1,k=3,(a,b)=(3,3)$ has canonical shift $\epsilon_0=1$.
The original sampler probabilities were correct, but its stated complex
amplitude omitted this possible sign.

**FIX DEMAND:** Enumerate the queried orbit from
$([j+l+\sigma]_{2k},[j-l]_{2k})$, or include the offset sign.
**RESOLUTION:** Current §5.4 explicitly chooses that canonical base.
**SURVIVING STATEMENT:** The exact amplitude formula and the full classical
computational-output sampler now use the same branch convention.

**RESOLVED MINOR O3 — state the level-one positive-margin ceiling.**
For $k=1$, every sector projector is a rank-one maximally entangled
projector on $\mathbb C^{2^g}\otimes\mathbb C^{2^g}$. On the product source
$A\otimes B$, Cauchy-Schwarz therefore gives

\[
 w_\xi\le 2^{-g}.
\]

Thus a nonempty positive-instance family at growing genus needs
$\gamma\le2^{-g}$. The statement about constant $\gamma$ is formally correct
but becomes vacuous in that regime. The displayed direct fixed-sector click
cannot occur with probability exceeding $2^{-g}$.

**FIX DEMAND:** Add this ceiling beside the level-one bit or its cost discussion
and qualify the constant-margin observation accordingly.
**RESOLUTION:** Current §5.2 explicitly gives the ceiling and its implication
for growing genus. Section 5.3a, the canonical definitions and C-353 additionally
extend it correctly to every odd $k$ using the audited logical Bell reduction.
**SURVIVING STATEMENT:** The existing $\gamma^{-1}$ and $\gamma^{-2}$ upper
bounds remain correct. The ceiling concerns the displayed product-input event,
not all collective measurements or all geometric readouts.

## 8. Independent bounded checks and canonical-definition audit

A 55-second, one-BLAS-thread inline probe passed 9713 checks.
It evaluated the full-series identities through truncated convergent sums
for genus one and a coupled genus-two matrix

\[
 \Omega=\begin{pmatrix}
 0.21+1.07i&0.16+0.19i\\
 0.16+0.19i&-0.13+0.91i
 \end{pmatrix},
\]

at each $k=1,2,3$. Checks included inverse indices with parity wraps,
conjugated evaluation pullback, sector weights, probability normalization,
Gaussian norm quadrature, and the orbit Walsh law on arbitrary complex
product source vectors. The maximum relative pullback residual was
$3.66\times10^{-15}$. The elliptic zero-sector test also passed.
Failures would terminate the probe with a nonzero exit; this was not installed
as a registered checker, and finite truncation does not replace the proofs.

D-THETA-ISOGENY agrees with the reviewed Gaussian metric, Haar normalization,
characteristics, conjugated evaluations and independent pair-copy access.
D-THETA-SECTOR-TRANSFORM agrees with $J$, its direction, both twists, sector
weights and simultaneous Weyl eigenvalues.
D-THETA-CLASSICAL-OUTPUTS separates the fixed-sector scalar protocol from
sample-and-query access to a full computational-output sampler.
No root, point, amplitude or preparation-inverse oracle is inferred from copies.
No mathematical mismatch was found in those canonical entries.

The final lockstep check also covered proposed C-353 and C-354.
C-353 contains exactly the accepted orthonormality, unitary sector map,
charged post-preparation gate cost, zero-sector convention, Weyl measurement,
and odd-level logical Bell ceiling. C-354 distinguishes the single-source
scalar estimator, the even-level exact sector sampler, and the stronger
sample-and-query full computational-output sampler. It makes neither an
optimal-margin assertion nor an odd-level copies-only sampler claim.
Both rows were still SKETCH during this audit; promotion remains root-owned.
Their statements are accepted in the displayed scope.

## 9. Targeted historical verification and scope

After the derivation, both cited primary PDFs were independently opened.
[Lubicz–Robert, arXiv:1001.2016](https://arxiv.org/abs/1001.2016), §4.2,
provides the classical theta addition and isogeny framework.
[Gelca–Uribe, arXiv:1006.3252](https://arxiv.org/abs/1006.3252), equation (2.1),
uses the same Gaussian inner product with the normalization moved into the
measure; equations (2.4)–(2.5) describe the finite Heisenberg action.
These agree with the derived normalization and the substantive Weyl reduction.

The audit does not identify a noninvertible isogeny with a single invertible
symplectic matrix. The explicit finite sector register resolves its kernel.
Nor does it refute originality merely because a circuit admits a universal
gate decomposition. The actual sector measurement is the established finite
character measurement, with an explicit arithmetic decoding.

The accepted product is exact twisted-sector theta transport and its scoped
resource/comparator analysis. It establishes neither historical priority of
every displayed formula nor the campaign's required original mechanism.
