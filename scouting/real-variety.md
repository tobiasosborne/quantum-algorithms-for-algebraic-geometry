# Real and positive varieties in the Fock/Macaulay framework

Lane: real-variety scout, PRD D11.  
Date: 2026-09-02.  
Status: scouting only; no claim below is ratcheted.

Conventions C1–C12 are binding.

The polynomial ring, grading, Hamiltonian, coherent states, Macaulay map, inverse system, and input model are those of D-polynomial-ring, D-hamiltonian, D-coherent-state, D-macaulay-map, D-inverse-system, and D-input-model.

I use \(D\) only for a zero-dimensional quotient dimension or scheme length, consistently with C8.

The seed report is treated as an untrusted proposer document.

## Bottom line

There is no complex-linear projector onto “the real part” of a Fock-space ground space.

Complex conjugation \(K\) is antiunitary, and its fixed set is a real vector space, not a complex Hilbert subspace.

Changing from the complex Bargmann measure to a Gaussian measure on \(\mathbb R^{n+1}\) does not repair this.

It either gives a representation unitarily equivalent to the ordinary Segal–Bargmann space, or turns multiplication into an \(L^2\) multiplication operator whose kernel is zero whenever the real variety has Lebesgue measure zero.

There is nevertheless an exact algebraic replacement.

If \(J=I(V_{\mathbb R}(I))\) is the real radical, complexified to \(\mathbb C[z_0,\ldots,z_n]\), then

\[
\operatorname{span}_{\mathbb C}
 \{|x\rangle^{\otimes N}:x\in V_{\mathbb R}(I)\}
 = (J_N)^\perp .
\]

Thus the desired ground space is the inverse system of the complexified real radical.

The obstruction is circular: computing generators of \(J\) is already a real-algebraic problem, normally attacked by moment matrices, semidefinite programming, real-root isolation, or quantifier elimination.

Hermite’s trace form gives the cleanest scalar observable.

For a radical zero-dimensional real ideal and quotient dimension \(D\),

\[
\operatorname{sig} \mathcal H_1=\#V_{\mathbb R}(I),
\qquad
\frac{\operatorname{sig}\mathcal H_1}{D}
 =\text{fraction of complex roots that are real}.
\]

A block encoding of \(\mathcal H_1\) would make the normalized signature additively estimable by applying the matrix sign function and estimating its normalized trace.

This is meaningful only when a constant fraction of roots is real.

It does not answer the robotics regime in which \(D\) may be \(10^4\)–\(10^6\) and only \(O(1)\) roots are usable.

Exact counting requires additive error below \(1/(2D)\), losing the exponential compression.

No classical-hardness result was found for constant-additive normalized Hermite signature under the polynomial-system input model.

The obvious Boolean reductions dequantize: a constant-gap estimate of the satisfying fraction is obtained by uniform classical sampling.

The moment/SOS route contains a load-bearing correction to robotics bet R1.

For a homogeneous objective of degree \(2m\), Lasserre order \(r\) corresponds to the \(r\)-boson sector, not the \(2r\)-boson sector.

The matrix rows have degree \(r\), while their products carry moments through degree \(2r\).

A level-3 relaxation in 100 affine variables therefore corresponds after homogenization to

\[
N=r=3,\qquad
\dim R_3=\binom{103}{3}=176\,851,
\]

not \(N=6\).

More importantly, the full Lasserre relaxation is not the ground energy of the seed Hamiltonian.

It optimizes over positive semidefinite moment matrices satisfying Hankel/maximal-symmetry and localizing constraints.

The normalized seed Hamiltonian gives a weaker, presentation-dependent spectral relaxation obtained by dropping those linear moment constraints.

For equal-degree real residuals \(f_j\) of degree \(m\), put

\[
c(x)=\sum_j f_j(x)^2,\qquad
A_N=\frac{(N-m)!}{N!}H_N .
\]

Then

\[
\langle x^{\otimes N}|A_N|x^{\otimes N}\rangle=c(x)
\]

on the real unit sphere, and

\[
\lambda_{\min}(A_N)\leq \operatorname{sos}_N(c)\leq
\min_{\|x\|=1}c(x).
\]

The first inequality can be strict.

The seed Hamiltonian therefore yields a valid spectral lower bound, but not “the Lasserre level-\(N\) value.”

This also destroys the claimed 250 GB versus 300 qubit comparison for the seed Hamiltonian.

The 250 GB figure is the dense storage of the full \(176\,851\times176\,851\) moment matrix.

The spectral surrogate \(A_3\) is sparse and can be attacked classically by Lanczos while storing \(O(\dim R_3)\) numbers: one double-precision vector is about 1.4 MB.

The full SDP retains a memory problem, but solving it quantumly requires a quantum SDP algorithm, not QPE on \(H_N\).

Positive toric varieties have the best natural hardware fit.

For a binomial \(z^u-z^v\), the corresponding term has negative off-diagonal hopping amplitudes, and the toric fibre blocks are stoquastic weighted graph Laplacians.

Their kernel vectors have positive occupation-basis amplitudes.

This is Perron–Frobenius positivity, not positivity of the coherent-state label.

The nonnegative toric part is a nonlinear subset of the ground space, and in the usual irreducible case it is Zariski dense, so its coherent-state span is the same as the span of the whole complex toric variety.

The Hamiltonian does not select it.

The strongest surviving north-star candidate is consequently modest:

> Estimate the value of a fixed, sparse, real spectral hierarchy on a symmetric sector, with a supplied guiding state and inverse-polynomial normalized eigenvalue separation, when the corresponding classical implicit eigensolver still requires \(n^{\Omega(r)}\) time or memory.

This is a possible polynomial-exponent or space improvement.

It is not yet a speedup claim, is not full Lasserre, and at robotics sizes the fair classical sparse-eigensolver comparison is presently unfavorable.

## Common size and output model

For polynomial-system routes, the input follows D-input-model:

- \(n+1\) homogeneous variables;
- maximum generator degree \(m=O(1)\), unless stated otherwise;
- \(d\) generators;
- at most \(t=\mathrm{poly}(n)\) monomials per generator;
- coefficient bit size \(\tau=\mathrm{poly}(n)\);
- sector degree \(N\) in unary;
- \(M_N=\dim R_N=\binom{N+n}{n}\);
- normalized spectral promises use \(\Delta_N/\alpha_{\mathrm{BE}}\), by D-normalised-gap.

For a zero-dimensional affine quotient, \(D\) denotes

\[
D=\dim_{\mathbb R}\mathbb R[x_1,\ldots,x_n]/I,
\]

including multiplicity unless radicality is promised.

For polynomial optimization, \(r\) denotes Lasserre order.

The dense affine moment matrix has

\[
B_r=\binom{n+r}{r}
\]

rows and columns.

The outputs must be distinguished:

- exact number of real roots;
- constant-additive real-root density;
- one real root;
- isolating boxes for all real roots;
- a fixed-order spectral lower bound;
- a fixed-order Lasserre value;
- an explicit SOS or Positivstellensatz certificate;
- an approximate optimizer;
- a heuristic low-energy state.

Only the scalar outputs plausibly avoid an output-size lower bound.

## Route 1: Hermite trace forms and normalized inertia

### Precise problem

Input:

- a zero-dimensional radical ideal
  \(I\subset\mathbb Q[x_1,\ldots,x_n]\);
- a quotient basis \(\mathcal B=\{b_1,\ldots,b_D\}\), or an oracle from which quotient multiplication can be performed;
- a polynomial \(g\in\mathbb Q[x]\);
- optionally a promise that every nonzero eigenvalue of the Hermite matrix is separated from zero by at least \(\eta\alpha_{\mathcal H}\).

Define

\[
\mathcal H_g(i,j)
 =\operatorname{Tr}_A(M_{g b_i b_j}),
\qquad
A=\mathbb R[x]/I .
\]

The multivariate Hermite theorem states

\[
\operatorname{sig}\mathcal H_g
 =
 \#\{x\in V_{\mathbb R}(I):g(x)>0\}
 -
 \#\{x\in V_{\mathbb R}(I):g(x)<0\}.
\]

For \(g=1\), the signature is the number of distinct real roots.

This statement, including the trace construction, is given explicitly in [arXiv:2110.10313](https://arxiv.org/abs/2110.10313).

Possible outputs are:

1. exact \(\operatorname{sig}\mathcal H_g\);
2. normalized signature
   \(\operatorname{sig}\mathcal H_g/D\) to additive error \(\epsilon\);
3. sign-condition statistics for a fixed number of inequalities \(g_1,\ldots,g_k\).

For positive-orthant counting, the classical Tarski-query construction uses signatures for products of the \(g_i\).

The number of required sign queries can itself grow exponentially with \(k\).

### Classical baseline

Once \(\mathcal H_g\) is explicit, exact \(LDL^{\mathsf T}\) inertia costs \(O(D^3)\) arithmetic operations by ordinary elimination, or \(O(D^\omega)\) with fast matrix arithmetic.

Exact rational bit complexity also depends on coefficient growth and pivot sizes.

The cited Hermite implementation gives the \(O(D^3)\) baseline and an alternative \(O(D^4)\) characteristic-polynomial route.

The expensive prior step is normally obtaining a quotient basis and multiplication matrices.

The practical baselines are:

- `msolve`, using Gröbner bases, change of ordering, and univariate real solving [arXiv:2104.03572](https://arxiv.org/abs/2104.03572);
- Maple `RegularChains`;
- Magma and Singular;
- numerical homotopy followed by `alphaCertified`, which can certify whether an approximate root corresponds to a real root [arXiv:1011.1091](https://arxiv.org/abs/1011.1091);
- certified Hermite matrices reconstructed from approximate complex roots [arXiv:2110.10313](https://arxiv.org/abs/2110.10313).

For a succinct matrix-vector oracle, classical Chebyshev or stochastic-Lanczos filtering estimates spectral densities without forming the matrix.

Hutch++ gives \(O(1/\epsilon)\) matrix-vector products for relative trace estimation of positive semidefinite matrices, while an indefinite sign trace normally falls back to Hutchinson-type \(O(1/\epsilon^2)\) sampling plus polynomial approximation [arXiv:2010.09649](https://arxiv.org/abs/2010.09649).

### Quantum observable and precision

Assume a block encoding of

\[
Q=\mathcal H_g/\alpha_{\mathcal H}
\]

and the spectral promise

\[
\operatorname{spec}(Q)\cap(-\eta,\eta)\subseteq\{0\}.
\]

QSVT approximates \(\operatorname{sgn}(Q)\) with degree

\[
O\!\left(\eta^{-1}\log\delta^{-1}\right)
\]

using the matrix-function framework of [arXiv:1806.01838](https://arxiv.org/abs/1806.01838).

The normalized observable is

\[
s_g=\frac1D\operatorname{Tr}\operatorname{sgn}(\mathcal H_g).
\]

Mixed-state trace estimation gives additive error \(\epsilon\) in \(O(\epsilon^{-2})\) samples.

Coherent amplitude estimation can reduce the \(\epsilon\) dependence to \(O(\epsilon^{-1})\), assuming controlled state preparation and controlled block encodings.

Suppressing logarithms, the optimistic query cost is

\[
\widetilde O\!\left(
 T_{\mathcal H}\eta^{-1}\epsilon^{-1}
 \right).
\]

Exact signature needs

\[
\epsilon<\frac1{2D},
\]

and therefore at least \(O(D)\) coherent estimation calls in this model.

The robotics use case with ten real roots among \(10^6\) complex roots needs \(\epsilon=O(10^{-6})\), not \(O(1)\).

### Is constant-additive normalized signature meaningful?

Yes, for dense-real families.

It estimates the fraction of roots that are real, or a signed fraction satisfying a fixed sign predicate.

No, for root existence, exact counts, or rare feasible roots.

A constant-additive estimate cannot distinguish zero real roots from one real root among exponentially many complex roots.

No classically hard constant-gap family was verified.

The obvious Boolean construction does not suffice.

If real versus nonreal root pairs are attached independently to Boolean assignments, then the normalized signature becomes an average of an efficiently evaluable Boolean predicate.

A \(2/3\) versus \(1/3\) promise is classically decidable by random sampling.

Hardness near a threshold separated only by \(2^{-n}\) restores PP/#P behavior but also restores exponential precision.

### Hidden input cost

The seed supplies compressed multiplication only after access to the stabilized quotient ground space and a non-zero-divisor, per D-compressed-multiplication.

It does not directly supply a sparse block encoding of the Hermite matrix.

Constructing \(\mathcal H_g\) from traces of \(D^2\) quotient multiplications may cost at least as much as solving the original system.

The factorization

\[
\mathcal H_g=V^{\mathsf T}\operatorname{diag}(g(\xi))V
\]

also shows the conditioning risk.

Near-colliding roots make the Vandermonde matrix \(V\) ill-conditioned and can make \(\eta\) exponentially small.

### Dequantization risk

High.

Given the same efficient Hermite matrix-vector product, classical polynomial filtering and stochastic trace estimation approximate the same normalized inertia.

The plausible quantum gain is at most:

- a quadratic improvement in \(\epsilon\);
- a dimension advantage in applying the matrix function.

Neither survives if the Hermite oracle requires an explicit quotient basis of size \(D\).

### Hardware fit

Poor.

A Hermite matrix is a dense, basis-dependent real symmetric form, not a natural few-mode bosonic Hamiltonian.

MBQC or postselected linear optics can implement the fault-tolerant block-encoding algorithm in principle, but that is universality rather than a native physical attack.

Boson sampling has no native signature or inertia observable.

An annealer can encode an eigenvalue variational problem only with continuous-to-binary discretization and many coefficient-precision gadgets.

### Plausibility score

**2/5.** Normalized inertia is the correct scalar, but no non-dequantized hard input family or cheap Hermite oracle is known.

## Route 2: complex conjugation \(K\), real Hilbert spaces, and the no-projector obstruction

### Precise problem

Assume the generators have real coefficients.

Then \(H_N\) is real in the D-fock-basis and

\[
KH_N=H_NK
\]

for coefficientwise conjugation \(K\).

A coherent state represents a real projective point precisely when its ray has a representative fixed by \(K\).

The desired operation would project the ground space onto those coherent states.

### Why \(K\) does not give a Hamiltonian sector

The fixed set

\[
\operatorname{Fix}(K)=\{\psi:K\psi=\psi\}
\]

is closed under real scalars but not under multiplication by \(i\).

If a complex-linear subspace \(W\) is contained in \(\operatorname{Fix}(K)\), then \(W=\{0\}\), because \(\psi\in W\) implies \(i\psi\in W\), while \(K(i\psi)=-i\psi\).

Therefore no ordinary quantum projector has range \(\operatorname{Fix}(K)\).

A real symmetric Hamiltonian can have a basis of real eigenvectors, but every degenerate eigenspace also contains arbitrary complex superpositions.

Commutation with \(K\) does not turn the ground space into the set of real vectors.

### Two-copy “reality” observables

For a pure state, the nonlinear quantity

\[
\mathcal R(\psi)=|\langle\psi|K\psi\rangle|^2
               =|\psi^{\mathsf T}\psi|^2
\]

equals one exactly when the ray has a real representative.

For a coherent state,

\[
\mathcal R(p^{\otimes N})=|p^{\mathsf T}p|^{2N}.
\]

This is a realness witness for a supplied state.

It does not define a linear one-copy observable.

A two-copy projection onto a maximally entangled vector measures a probability proportional to \(|\psi^{\mathsf T}\psi|^2/M_N\).

That normalization is exponentially small when \(M_N\) is exponential.

If the preparation circuit for \(\psi\) is known and its conjugate can be compiled, a SWAP-type comparison is cheaper, but then the amplitudes are classically specified and realness is trivial to test.

Universal deterministic phase conjugation is antiunitary and is not a physical quantum channel.

### Real Fischer and real Segal–Bargmann alternatives

The real Fischer space of real polynomials with the factorial inner product is a real Hilbert space.

Its complexification is exactly the existing space of D-fock-space.

The kernel of the real Macaulay operator complexifies to D-inverse-system.

Its dimension is still the complex quotient dimension and does not count real points.

The Segal–Bargmann transform is a unitary equivalence between an \(L^2(\mathbb R^{n+1})\) oscillator representation and the ordinary holomorphic Fock space, not a projection onto real coherent labels [DOI 10.1002/cpa.3160140303](https://doi.org/10.1002/cpa.3160140303).

If one instead equips restrictions of polynomials to \(\mathbb R^{n+1}\) with

\[
\langle u,v\rangle_{\mathbb R}
 =\int_{\mathbb R^{n+1}}\overline{u(x)}v(x)e^{-\|x\|^2}\,dx,
\]

multiplication by a real polynomial is an \(L^2\) multiplication operator.

Its positive square is multiplication by \(f(x)^2\).

For a proper algebraic variety of Lebesgue measure zero, the \(L^2\) kernel is zero.

Thus this inner product loses the Macaulay inverse system rather than making it real.

At fixed degree, real Veronese vectors already span the complex symmetric sector:

\[
\operatorname{span}_{\mathbb C}
 \{x^{\otimes N}:x\in\mathbb R^{n+1}\}
 =\operatorname{Sym}^N(\mathbb C^{n+1}).
\]

“Restrict the coherent labels to real vectors” therefore does not produce a smaller complex-linear ambient sector.

### Classical baseline

Testing whether a supplied state-preparation vector has real amplitudes is linear in its explicit description.

Testing whether a real polynomial system has a real point is the real-feasibility problem discussed below, with singly exponential classical algorithms and PSPACE containment.

### Quantum observable and precision

There is no one-copy projector.

The two-copy scalar \(\mathcal R(\psi)\) can be estimated to additive error \(\epsilon\), but it only classifies a supplied state.

For an unknown state drawn from a degenerate ground space, it neither prepares nor projects onto a real coherent component.

### Dequantization risk

Complete for explicitly prepared coherent states: calculate \(p^{\mathsf T}p\) classically in \(O(n)\).

For general unknown states, the obstacle is physical implementability rather than dequantization.

### Hardware fit

Real optical interferometers naturally prepare single-particle vectors with phases \(0\) or \(\pi\), and hence real coherent product states.

They do not project an arbitrary state onto the real locus.

Homodyne measurement sees real quadratures, but restricting a quadrature expectation is not the same as requiring a projective coherent label to be real.

### Plausibility score

**1/5.** \(K\) is a useful symmetry label and reality witness, not an algorithmic selector.

## Route 3: the real-radical inverse system

### Precise problem

Input:

- a homogeneous ideal \(I\subset\mathbb R[z_0,\ldots,z_n]\);
- a degree \(N\);
- either generators of its real radical or only generators of \(I\).

Let

\[
J=I(V_{\mathbb R}(I))\otimes_{\mathbb R}\mathbb C.
\]

The desired state space is

\[
\mathcal G^{\mathbb R}_N
 =\operatorname{span}_{\mathbb C}
   \{|x\rangle^{\otimes N}:x\in V_{\mathbb R}(I)\}.
\]

Evaluation duality gives the exact identity

\[
\mathcal G^{\mathbb R}_N=(J_N)^\perp.
\]

If a generating tuple for \(J\) is supplied, the ordinary construction D-hamiltonian applied to that tuple has ground space \(\mathcal G_N^{\mathbb R}\) once its degree-\(N\) piece equals \(J_N\).

This is the direct answer to “what replaces the Macaulay inverse system?”:

> the Macaulay inverse system of the complexified real radical.

### Real Nullstellensatz cost

The real radical satisfies

\[
q\in\sqrt[\mathbb R]{I}
\iff
\exists k\geq1,\ \exists \sigma\text{ SOS}:
q^{2k}+\sigma\in I .
\]

This is an ordered-field condition, not complex-linear algebra.

The standard algorithms use:

- Gröbner or border bases;
- moment matrices;
- semidefinite facial reduction;
- real-root isolation;
- Positivstellensatz searches.

Moment-matrix and border-basis algorithms for zero-dimensional real radicals are described in [arXiv:1112.3197](https://arxiv.org/abs/1112.3197).

Truncated real-radical generators in positive dimension can be computed using maximal-rank moment matrices and facial reduction [arXiv:1606.00491](https://arxiv.org/abs/1606.00491).

### Why the route is circular

If \(J\) is supplied explicitly, the Hamiltonian construction is immediate but the real-algebraic work has already been performed.

If only \(I\) is supplied, producing \(J_N\) is at least a real-radical-membership problem.

An algorithm that first runs a classical real-radical SDP and then builds the Fock Hamiltonian does not accelerate real feasibility.

A quantum algorithm could try to prepare a moment state whose kernel contains \(J_N\).

However, extracting generators from that kernel is an extensive classical-output problem.

### Positive-dimensional collapse

If \(V_{\mathbb R}(I)\) is Zariski dense in the relevant complex component, then

\[
J=\sqrt{I_{\mathbb C}}
\]

on that component.

The real-point coherent span is then the same as the complex-point coherent span.

This occurs for many smooth real varieties with a nonsingular real point, and for the positive part of an irreducible toric variety.

In this common case, even the exact real-radical ground space does not distinguish individual real points from complex ones.

It only removes complex components having no real points.

### Classical baseline

For zero-dimensional systems:

- moment SDP plus border-basis extraction;
- `msolve`;
- Maple `RegularChains`;
- homotopy plus `alphaCertified`.

For positive-dimensional systems:

- truncated moment matrices and facial reduction;
- real witness-point and roadmap methods;
- quantifier elimination.

At moment order \(r\), the dense PSD block has size \(B_r\) and dense factorization cost \(O(B_r^3)\).

### Quantum observable and precision

If generators of \(J\) are given, all observables of D-projectors apply.

If generators are not given, the relevant quantum task is an SDP or kernel-learning problem, not QPE on the original \(H_N\).

Normalized rank of a moment matrix can be estimated additively.

Recovering an exact real radical requires resolving small singular values and outputting a basis, so precision and output scale with \(B_r\).

### Dequantization risk

High.

The moment matrix is positive semidefinite and often low rank when it admits a finitely atomic measure.

That is exactly the regime where randomized low-rank factorization, facial reduction, and quantum-inspired sampling are strongest.

### Hardware fit

Weak.

Continuous-variable photonics can measure Gaussian moments, but non-Gaussian polynomial moment constraints and exact flatness need substantial resources.

MBQC can implement the SDP algorithm generically.

No boson-sampling primitive outputs a real radical.

### Plausibility score

**2/5.** Mathematically exact, but it moves the entire difficulty into computing the real radical.

## Route 4: the residual spectral hierarchy on the real sphere

### Precise problem

Input:

- real homogeneous residual forms \(f_1,\ldots,f_d\) of common degree \(m\);
- \(N\geq m\);
- sparse access as in D-input-model;
- additive target \(\epsilon\);
- a guiding state with squared ground-space overlap \(w\);
- a normalized spectral separation promise \(\gamma_N/\alpha_A\geq1/\mathrm{poly}(n,N)\), where \(\gamma_N\) is the gap above the lowest eigenvalue of the normalized operator below.

Define

\[
c(x)=\sum_{j=1}^d f_j(x)^2
\]

on the real unit sphere and

\[
A_N=\frac{(N-m)!}{N!}H_N.
\]

Using D-coherent-state,

\[
\langle x^{\otimes N}|A_N|x^{\otimes N}\rangle=c(x).
\]

Under D-symmetric-tensor-of-a-form,

\[
A_N
 =
 P_{\mathrm{sym}}
 \left[
   \left(\sum_j|F_j\rangle\langle F_j|\right)
   \otimes\mathbb 1^{\otimes(N-m)}
 \right]
 P_{\mathrm{sym}} .
\]

Therefore

\[
\lambda_{\min}(A_N)
 \leq c^\star
 :=\min_{\|x\|=1,\ x\in\mathbb R^{n+1}}c(x).
\]

This is a genuine real-polynomial lower bound even though the Hilbert space is complex: \(A_N\) is real symmetric, so a lowest eigenvector can be chosen real.

It is not generally a coherent state.

### Relation to SOS

Let \(s(x)=\sum_i x_i^2\).

If \(A_N-\lambda\mathbb 1\succeq0\), then evaluating its positive Gram decomposition on \(x^{\otimes N}\) gives an SOS representation of

\[
s^{N-m}c-\lambda s^N.
\]

Consequently,

\[
\lambda_{\min}(A_N)
 \leq \operatorname{sos}_N(c)
 \leq c^\star .
\]

The residual representation matters.

Replacing \((f_1,\ldots,f_d)\) by another SOS decomposition of the same \(c\) can change \(A_N\).

This is analogous to the presentation dependence of D-macaulay-gap.

For different residual degrees, either homogenize them to a common degree or scale each term by its own falling factorial.

The normalization must be stated explicitly.

### Classical baseline

The fair classical problem is the smallest eigenvalue of a sparse implicit matrix of dimension \(M_N\).

Lanczos or LOBPCG requires approximately

\[
O(k\,\mathrm{nnz}(A_N))
\]

work for \(k\) iterations and stores \(O(kM_N)\) numbers, with convergence governed by the same spectral separation and guiding vector.

It is not fair to compare with dense \(M_N^3\) diagonalization.

At fixed \(N\), \(M_N=\Theta(n^N)\), so this is polynomial in \(n\).

At \(n=100,N=3\),

- \(M_N=176\,851\);
- one double vector is 1.4 MB;
- twenty Krylov vectors are about 28 MB;
- the operator can be applied without storing a dense matrix.

### Quantum observable and precision

QPE or qubitization estimates \(\lambda_{\min}(A_N)\) to additive error \(\epsilon\) in the objective’s natural scale.

An optimistic guided cost is

\[
\widetilde O\!\left(
 \frac{\alpha_A}{\epsilon\sqrt w}
 \right)
\]

block-encoding uses, plus whatever dependence is needed to distinguish the lowest band from the next eigenvalue.

Here

\[
\alpha_A=\frac{(N-m)!}{N!}\alpha_{\mathrm{BE}}.
\]

A variational method measures \(\langle\psi|A_N|\psi\rangle\) but provides no certified lower bound.

A Gibbs method needs inverse temperature at least on the order of

\[
\beta
 \gtrsim
 \frac{\log(M_N/w)+\log\epsilon^{-1}}{\gamma_N},
\]

so the compact Hilbert-space encoding does not eliminate low-temperature preparation.

Guided Local Hamiltonian is BQP-complete even with strong guiding fidelity promises, which is a hardness anchor rather than an algorithmic speedup [arXiv:2207.10250](https://arxiv.org/abs/2207.10250).

### Dequantization risk

Medium to high.

The matrix is sparse and high rank, so low-rank sample-and-query dequantization is not automatic.

But classical Lanczos receives exactly the same sparsity, polynomial filtering, guide, and preconditioner.

For a classical input, any advantage must be a proven improvement in the cost of one implicit filter application or in the exponent of \(M_N\).

### Hardware fit

Good for heuristics.

A real coherent ansatz is prepared by a real mode rotation followed by placing all \(N\) bosons in the resulting mode.

The terms are number-conserving \(m\)-boson interactions.

Few-mode quadrics may be implemented in spinor BECs, with D-spin-mixing-hamiltonian as the known example.

Linear optics prepares the ansatz but does not implement the nonlinear residual Hamiltonian without measurement-induced interactions.

MBQC can implement the block encoding.

### Plausibility score

**3/5.** This is the cleanest real scalar accessible to the seed, but the likely advantage is only a polynomial-exponent improvement over sparse Lanczos.

## Route 5: full Lasserre moment/SOS and the exact \(r\leftrightarrow N\) dictionary

### Sphere problem and exact level mapping

Let \(c\) be a real homogeneous form of degree \(2m\).

The sphere problem is

\[
c^\star=\min_{\|x\|=1}c(x).
\]

For every \(r\geq m\), the order-\(r\) SOS lower bound is

\[
\operatorname{sos}_r(c)
 =
 \max_\lambda
 \left\{
 \lambda:
 s^{r-m}c-\lambda s^r\text{ is SOS}
 \right\}.
\]

Equivalently, in the nonhomogeneous sphere quotient,

\[
c-\lambda=\sigma+u(1-s),
\qquad
\deg\sigma\leq2r .
\]

This is the convention in [arXiv:1908.05155](https://arxiv.org/abs/1908.05155) and [DOI 10.1137/24M1717750](https://doi.org/10.1137/24M1717750).

The corresponding moment functional contains moments through degree \(2r\).

Its PSD moment matrix is indexed by degree-\(r\) homogeneous monomials after homogenization.

Therefore the Fock sector is

\[
\boxed{N=r},
\]

not \(N=2r\).

The moment matrix is an operator on

\[
R_r\simeq\operatorname{Sym}^r(\mathbb R^{n+1}),
\]

but it is not an arbitrary density operator.

It must be maximally symmetric/Hankel: entries with the same sum of row and column multiindices are equal.

In the tensor formulation,

\[
\operatorname{sos}_r(c)
 =
 \min_A
 \left\{
 \langle Q(c)\otimes\mathbb 1^{\otimes(r-m)},A\rangle:
 A\succeq0,\ 
 A\in\operatorname{MaxSym}_r,\ 
 \operatorname{Tr}A=1
 \right\}.
\]

A general quantum state on \(R_r\) is only doubly symmetric as an operator supported on the Bose sector.

Maximal symmetry is a much stronger linear constraint.

### General constrained Lasserre level

For

\[
K=\{x:g_j(x)\geq0,\ h_k(x)=0\},
\]

order \(r\) uses:

\[
M_r(y)\succeq0,
\]

\[
M_{r-\lceil\deg g_j/2\rceil}(g_jy)\succeq0,
\]

and

\[
M_{r-\lceil\deg h_k/2\rceil}(h_ky)=0.
\]

The objective is \(L_y(c)\).

The dual searches for

\[
c-\lambda
 =
 \sigma_0+\sum_j\sigma_jg_j+\sum_k u_kh_k
\]

with the order-\(r\) degree bounds.

This is the Lasserre hierarchy introduced in [DOI 10.1137/S1052623400366802](https://doi.org/10.1137/S1052623400366802).

There is no fixed seed Hamiltonian whose ground energy automatically enforces all moment, equality, and localizing constraints.

One can form a Hamiltonian after choosing dual multipliers.

Finding those multipliers is the SDP.

### Relation to the spectral hierarchy

Lovitz and Johnston define a weaker order-\(r\) generalized-eigenvalue bound.

For the maximally symmetric representation \(Q(c)\) and the corresponding representation \(M\) of \(s^m\), put

\[
Q_r=P_{\mathrm{sym}}
 (Q(c)\otimes\mathbb 1^{\otimes(r-m)})
 P_{\mathrm{sym}},
\]

\[
M_r=P_{\mathrm{sym}}
 (M\otimes\mathbb 1^{\otimes(r-m)})
 P_{\mathrm{sym}}.
\]

Then

\[
\operatorname{sp}_r(c)
 =
 \lambda_{\min}(Q_r,M_r)
 \leq
 \operatorname{sos}_r(c)
 \leq c^\star .
\]

This is a single generalized eigenproblem [arXiv:2310.17827](https://arxiv.org/abs/2310.17827).

Known results include:

- an \(O(1/r)\) convergence upper bound for the spectral hierarchy;
- an explicit quartic in five variables with \(\Omega(1/r^2)\) error;
- no generic finite convergence for the spectral hierarchy;
- \(O(1/r^2)\) convergence for the homogeneous moment-SOS hierarchy in the stated regime.

The comparison and lower-bound example are in [DOI 10.1137/24M1717750](https://doi.org/10.1137/24M1717750).

The seed residual Hamiltonian is another presentation-dependent spectral lift.

It should not be identified automatically with the canonical \(\operatorname{sp}_r\), and neither spectral construction equals \(\operatorname{sos}_r\).

### Relation to DPS

The DPS hierarchy concerns separability and symmetric extensions.

For a bipartite Hermitian form \(p_M(x,y)\) of bidegree \((2,2)\), the dual of DPS level \(\ell\) is characterized by

\[
\|y\|^{2(\ell-1)}p_M(x,y)
\]

being a real SOS polynomial.

This is the precise DPS/SOS duality stated in [arXiv:1908.05155](https://arxiv.org/abs/1908.05155).

DPS level \(\ell\) extends one subsystem by \(\ell\) symmetric copies.

It is not, without an additional derivation, the same as total-degree Fock sector \(N=\ell\) for a general robotics polynomial.

The phrase “DPS/Lasserre ground energy” therefore hides two different hierarchies.

### Dense classical cost

For \(n\) affine variables,

\[
B_r=\binom{n+r}{r}.
\]

Dense storage is \(8B_r^2\) bytes in double precision.

Representative values are:

| \(n\) | \(r\) | \(B_r\) | dense PSD block |
|---:|---:|---:|---:|
| 20 | 4 | 10,626 | 0.90 GB |
| 100 | 2 | 5,151 | 0.21 GB |
| 100 | 3 | 176,851 | 250 GB |
| 100 | 4 | 4,598,126 | 169 TB |

Dense factorization is \(O(B_r^3)\) per major step.

But dense storage is not the best-in-class baseline.

Classical competitors include:

- correlative sparsity;
- chordal decomposition;
- term sparsity;
- TSSOS and CS-TSSOS;
- Burer–Monteiro factorization;
- first-order conic solvers;
- STRIDE plus local search;
- MOSEK, SDPA, CSDP, SOSTOOLS, GloptiPoly, YALMIP, SumOfSquares.jl, and `ncpol2sdpa`.

TSSOS combines correlative and term sparsity and reports problems with thousands to tens of thousands of variables or constraints [arXiv:2103.00915](https://arxiv.org/abs/2103.00915).

CS-TSSOS reports instances with up to six thousand variables [arXiv:2005.02828](https://arxiv.org/abs/2005.02828).

STRIDE handles sparse robotics SDPs with hundreds of thousands of constraints and was reported up to \(100\times\) faster than prior SDP solvers [arXiv:2109.03349](https://arxiv.org/abs/2109.03349).

Even fixed-level polynomial-size SDPs can have exponential coefficient bit complexity, so “\(B_r\) is polynomial” does not by itself give a polynomial bit-complexity bound [arXiv:2305.14944](https://arxiv.org/abs/2305.14944).

### Quantum SDP route

A genuine quantum Lasserre solver must solve the structured SDP.

It cannot merely estimate \(\lambda_{\min}(H_r)\).

Quantum SDP algorithms offer dimension or constraint-count improvements in sparse-oracle or quantum-state input models, but retain polynomial dependence on:

- accuracy;
- primal and dual radius;
- width;
- sparsity;
- trace bounds;
- Gibbs preparation;
- oracle cost.

Representative bounds and matching limitations appear in [arXiv:1705.01843](https://arxiv.org/abs/1705.01843) and [arXiv:1710.02581](https://arxiv.org/abs/1710.02581).

Worst-case lower bounds rule out a generic polylogarithmic dependence on all SDP dimensions.

The output is normally a value estimate or quantum state, not an explicit moment matrix or SOS decomposition.

### Robotics R1 audit

For 100 affine variables at level 3:

- the correct sector is \(N=3\);
- a compact basis register needs \(\lceil\log_2 176851\rceil=18\) qubits;
- a first-quantized symmetric encoding uses about \(3\lceil\log_2 101\rceil=21\) data qubits;
- a naive occupation encoding uses 202 data qubits;
- substantial oracle and algorithm ancillas are additional.

The dense 250 GB contrast is valid only for the full moment matrix.

For the seed spectral Hamiltonian, sparse Lanczos needs tens of megabytes, not 250 GB.

For the full Lasserre SDP, the vector of distinct degree-\(\leq6\) moments already has

\[
\binom{106}{6}=1\,705\,904\,746
\]

entries before exploiting sparsity.

A quantum SDP solver may access these implicitly, but its constraint-oracle and width costs must be counted.

The robotics objective and manifold constraints also cannot simply be put into one residual sum and called the constrained Lasserre relaxation.

A penalty objective

\[
c(x)+\rho\sum_k h_k(x)^2
\]

has a global minimum no larger than the constrained optimum, but its tightness depends on \(\rho\), and it does not reproduce the localizing constraints.

The current R1 equality claim should therefore be rejected.

A surviving version is:

> quantumly estimate a sparse spectral lower bound associated with a chosen penalty/SOS representation, and compare it with classical implicit Lanczos and with sparse Lasserre bounds.

### Dequantization risk

Very high for low-rank or chordally sparse moment solutions.

Medium for a high-rank, sparse spectral operator.

Any preconditioner, sparsity pattern, or guiding state available to the quantum algorithm must also be given to classical Lanczos or first-order SDP solvers.

### Hardware fit

Full Lasserre: poor without universal MBQC.

Spectral surrogate: good for Bose-Hubbard/spinor-BEC heuristics.

Boolean localizing constraints: natural on Ising hardware, but high-degree terms require ancilla gadgets.

Boson sampling does not solve an SDP merely because its moment matrix is positive semidefinite.

### Plausibility score

**2/5 for full Lasserre; 3/5 for the weaker spectral hierarchy.** The full SDP has a genuine memory wall, but no complete quantum resource advantage; the seed Hamiltonian is cheaper classically than R1 assumed.

## Route 6: real coherent-state variational search and quadrature Hamiltonians

### Real coherent ansatz

Restrict the variational ansatz to

\[
|x\rangle^{\otimes N},
\qquad x\in\mathbb R^{n+1},\quad\|x\|=1.
\]

By D-coherent-state, measuring \(H_N\) evaluates the sum of squared residuals.

This directly searches over real points.

For a supplied classical \(x\), however, sparse evaluation and differentiation of all residuals is classical polynomial time.

The quantum variational landscape is the same explicit landscape used by Gauss–Newton, Levenberg–Marquardt, Riemannian trust-region, and sequential quadratic programming.

No speedup follows from measuring an energy that is classically evaluable.

### Position-quadrature construction

Let

\[
Q_j=\frac{a_j+a_j^\dagger}{\sqrt2}.
\]

The \(Q_j\) commute, so a real polynomial system can be represented by

\[
V(Q)=\sum_j f_j(Q)^2.
\]

In the Schrödinger representation this is multiplication by

\[
V(x)=\sum_j f_j(x)^2.
\]

It sees the real coordinates directly.

But if \(V_{\mathbb R}(I)\) has Lebesgue measure zero, then

\[
\ker_{L^2}V(Q)=\{0\}.
\]

Zero may lie in the continuous spectrum without a normalizable zero-energy state.

Adding kinetic confinement,

\[
H_\varepsilon
 =
 \varepsilon\sum_j P_j^2+V(Q),
\]

produces localized wave packets near real minima.

It also introduces zero-point energy, tunneling splittings, and an \(\varepsilon\to0\) extrapolation.

The ground space is no longer a Macaulay inverse system.

### Precise problem

Input:

- sparse real residuals of degree at most \(m\);
- a bounded domain or confining term;
- thresholds \(a<b\);
- required spatial resolution \(\delta_x\).

Output:

- a heuristic approximate real minimizer;
- or a promised ground-energy decision for \(H_\varepsilon\).

### Classical baseline

Local residual minimization costs \(O(dt)\) per value/gradient evaluation and is highly optimized.

Global optimization is NP-hard already for quartics.

Classical baselines include multistart local methods, branch-and-bound, interval arithmetic, and moment/SOS relaxations.

### Quantum observable and precision

The observable is the energy of \(H_\varepsilon\) or \(H_N\) on a real coherent ansatz.

To localize coordinates to \(\delta_x\), the oscillator cutoff and squeezing energy grow with \(\delta_x^{-1}\).

To certify feasibility, one must separate the zero-point contribution from the residual minimum.

Near-degenerate wells can have exponentially small tunneling gaps.

### Dequantization risk

Complete for the product-state ansatz.

It has only \(O(n)\) real parameters, and its energy and gradient are explicit classical functions.

A non-product variational ansatz may lower the energy below the real polynomial minimum and therefore weakens the certificate.

### Hardware fit

This is the most natural continuous-variable hardware construction.

Gaussian preparation and homodyne readout are native.

Polynomial potentials beyond quadratics require non-Gaussian interactions or digital simulation.

Spinor BECs naturally implement selected low-degree residual Hamiltonians.

### Plausibility score

**1/5 as an algorithm; 3/5 as a heuristic hardware demonstration.**

## Route 7: toric and binomial ideals with positive real points

### Precise problem

Input:

- an integer matrix \(A\);
- a bounded-degree Markov basis of binomials \(z^u-z^v\);
- total degree \(N\);
- an \(A\)-graded fibre;
- optionally additional likelihood or inequality constraints.

Pure toric positivity asks for points in

\[
V(I_A)\cap\mathbb R_{>0}^{n+1}.
\]

The positive torus parameterization has coordinates proportional to monomials in positive parameters.

The closure of the nonnegative part maps homeomorphically to the defining polytope under the algebraic moment map [arXiv:math/0212044](https://arxiv.org/abs/math/0212044).

### What the bosonic Hamiltonian sees

By D-toric-ideal, \(H_N\) decomposes into fibre graph Laplacians.

For a binomial \(z^u-z^v\),

\[
a^\dagger(z^u-z^v)a(z^u-z^v)
\]

has negative cross-hopping terms in the occupation basis.

When all phases can be gauged consistently, each fibre block is stoquastic.

Its kernel vector

\[
q_a=\sum_{Ak=a}\frac{z^k}{k!}
\]

has strictly positive coefficients.

This is natural Perron–Frobenius positivity.

It means the occupation-basis ground vector is positive.

It does not mean its coherent label is a positive point of the toric variety.

A positive coherent state has multiplicative amplitudes across all relevant fibres.

An arbitrary nonnegative linear combination of the \(q_a\) need not be coherent.

The Hamiltonian enforces the binomial relations but not the rank-one/coherent-state condition.

### Zariski-density obstruction

For an irreducible toric variety, the positive torus is Zariski dense.

Hence

\[
I(V_{>0}(I_A))=I_A
\]

over characteristic zero, and

\[
\operatorname{span}_{\mathbb C}
 \{|x\rangle^{\otimes N}:x\in V(I_A)\cap\mathbb R_{>0}^{n+1}\}
 =(I_A{}_N)^\perp
\]

whenever the degree piece is saturated.

Positive and complex toric coherent states therefore have the same complex-linear span.

No ground-space projector can distinguish them.

### Algebraic-statistics interpretation

Projective toric varieties describe discrete exponential families.

The positive point is the statistically meaningful distribution.

Likelihood critical points on the complex closure define the ML degree [arXiv:1305.7462](https://arxiv.org/abs/1305.7462).

For standard toric models, the positive MLE is frequently found by convex optimization in log-parameters, iterative proportional fitting, or moment matching.

The hard complex critical-point count is not the same output as the unique positive statistical estimate.

Moment maps and ML-degree-one models are connected in [arXiv:1810.03672](https://arxiv.org/abs/1810.03672).

### Classical baseline

For the pure positive toric parameterization:

- convex optimization in logarithmic parameters;
- iterative proportional fitting;
- Newton or mirror descent;
- polytope computations.

For conditional fibre sampling:

- Markov-basis MCMC using `4ti2`;
- dynamic programming for decomposable models;
- specialized sequential samplers.

For ML degree and all critical points:

- Gröbner bases;
- homotopy continuation;
- parameter homotopy.

### Quantum observable and precision

Natural observables include:

- fibre-block ground energy;
- spectral gap \(\lambda_2\);
- occupation means \(N^{-1}\langle\hat n_i\rangle\), which map to moment-polytope coordinates;
- overlap with a supplied positive coherent state;
- quantum-walk hitting or mixing statistics.

None alone projects onto the positive toric locus.

The same fibre Poincaré constant controls classical Markov-chain mixing and quantum spectral filtering.

### Dequantization risk

High.

Stoquasticity removes the sign problem and supports probabilistic simulation.

Stoquastic frustration-free Hamiltonians have strong classical simulation and complexity upper bounds [arXiv:0806.1746](https://arxiv.org/abs/0806.1746).

The Markov-basis graph is already the classical object used for fibre sampling.

### Hardware fit

Excellent.

The terms are number-conserving multi-boson hopping.

Bose-Hubbard and parametric mixing hardware can implement small-degree binomials with few-mode couplings.

Passive linear optics prepares positive coherent labels by setting relative phases to zero.

Boson sampling samples occupation patterns but does not enforce toric positivity or compute a moment-map inverse.

### Plausibility score

**2/5 for speedup; 4/5 for hardware.** Positivity is physically natural but algorithmically collapses toward stoquastic Markov-chain structure.

## Route 8: Boolean ideals and totally real varieties

### Precise problem

Use D-boolean-ideal or its \(\{\pm1\}\) analogue.

The coordinate equations

\[
x_i^2-x_i=0
\quad\text{or}\quad
x_i^2-1=0
\]

have only real roots.

Adding polynomial constraints over these coordinates cannot introduce nonreal Boolean assignments.

For these families the original complex variety is already totally real.

The field mismatch disappears without changing the Hamiltonian.

Possible outputs are:

- satisfiability;
- one satisfying assignment;
- the number of satisfying assignments;
- a constant-additive satisfying fraction;
- the minimum of a Boolean polynomial.

### Classical baseline

SAT and QUBO solvers exploit:

- clause learning;
- branch-and-bound;
- cutting planes;
- tensor-network contraction;
- integer programming;
- problem-specific dynamic programming.

For counting, approximate model counters use hashing and SAT oracles.

For dense, unstructured search, brute force costs \(O(2^n)\).

### Quantum observable and precision

The D-hamiltonian ground space represents satisfying Boolean points once irrelevant torsion is controlled.

Projection from a uniform Boolean superposition has success weight

\[
D_{\mathrm{sat}}/2^n.
\]

Amplitude amplification costs

\[
O\!\left(\sqrt{2^n/D_{\mathrm{sat}}}\right),
\]

matching Grover scaling.

Exact counting still requires exponentially fine phase or amplitude resolution.

A constant-additive estimate of \(D_{\mathrm{sat}}/2^n\) is classically obtained by sampling random assignments.

The normalized Hermite signature of the clause ideal equals one whenever normalized by its own radical quotient dimension, because every remaining root is real.

To recover the satisfying fraction, one must normalize against the full Boolean cube or implement the Boolean predicate as an observable.

That again becomes ordinary approximate counting.

### Dequantization risk

High.

The problem has been reduced to standard Boolean search or optimization.

The real-variety vocabulary adds no additional structure.

### Hardware fit

Excellent for Ising/annealers.

Standard NP problems have QUBO/Ising encodings, sometimes with up to cubic auxiliary-spin overhead [arXiv:1302.5843](https://arxiv.org/abs/1302.5843).

Higher-degree clauses require quadratization gadgets and large penalty scales.

Dual-rail photonics needs hard-core constraints and postselection.

Boson sampling is not a SAT solver.

### Plausibility score

**2/5.** This is an exact real embedding and a useful calibration family, but the surviving speedup is Grover-like.

## Route 9: Sturm, Budan–Fourier, real-root isolation, and critical ideals

### Univariate problem

Input:

- a square-free \(F\in\mathbb Z[x]\);
- degree \(D\);
- coefficient bit size \(\tau\);
- optionally an interval \((a,b)\).

Outputs:

- the exact number of roots in \((a,b)\);
- isolating rational intervals for every real root;
- one sampled real root.

Sturm sequences give the exact count from sign variations.

Budan–Fourier and Descartes methods give subdivision bounds and parity information.

Modern certified Descartes-style isolation achieves, for integer input in the cited analysis,

\[
\widetilde O(D^3\tau^2)
\]

bit complexity [arXiv:1011.0344](https://arxiv.org/abs/1011.0344).

The output itself contains \(\Omega(k)\) intervals for \(k\) real roots.

### Quantum formulation

The companion matrix is generally nonnormal, so ordinary QPE does not apply.

A Hermite or Bézout matrix is real symmetric and its shifted inertia gives interval root counts.

This reduces to Route 1.

For exact interval counts, the required normalized-trace precision is \(O(1/D)\).

For all isolating intervals, output size removes an exponential speedup.

For a supplied real-rootedness promise, symmetric Jacobi-type linearizations may be used, but classical root algorithms are already nearly linear or low-degree polynomial in the input/output size.

### Multivariate critical ideals

For distance to a real variety, form the Lagrange critical ideal as in the classical memo.

Its complex root count is the Euclidean-distance degree \(D_{\mathrm{ED}}\).

Classical homotopy tracks \(D_{\mathrm{ED}}\) paths, then evaluates objective values and certifies reality.

HomotopyContinuation.jl is a current implementation [arXiv:1711.10911](https://arxiv.org/abs/1711.10911).

A Fock/Macaulay algorithm can project onto the complex critical inverse system.

It still must:

- select real critical points;
- compare their objective values;
- resolve the closest value;
- read out coordinates.

If a root state can be prepared, quantum minimum finding over \(D_{\mathrm{ED}}\) opaque values offers at most an \(O(\sqrt{D_{\mathrm{ED}}})\) query count.

Root-state preparation and reality filtering can already cost \(\sqrt{M_N/D_{\mathrm{ED}}}\) or worse.

Near the ED discriminant, root separation and Hermite conditioning collapse.

### Classical baseline

- univariate Sturm/Descartes/subresultant isolation;
- `msolve`;
- Maple `RegularChains`;
- MPSolve for numerical univariate roots;
- homotopy continuation;
- `alphaCertified`;
- interval Newton and Krawczyk methods.

### Quantum observable and precision

- normalized Hermite inertia for counts;
- QSVT scans of nonnormal compressed multiplication pencils for coordinates;
- coherent-state energy for residual values;
- amplitude amplification or minimum finding over prepared critical states.

Exact nearest-point certification needs objective separation and coordinate precision in the resource bound.

### Dequantization risk

High.

Classical homotopy is small-space and parallel.

A quantum sample from complex critical points is not the nearest real point.

A coherent residual minimization is classically explicit.

### Hardware fit

A BEC or continuous-variable device can minimize the residual heuristic.

It cannot certify the nearest real critical point without the same spectral and precision machinery.

MBQC can implement the digital algorithm.

Boson sampling has no general critical-point primitive.

### Plausibility score

**1/5 for root isolation; 2/5 for design-time minimum finding over a prepared critical set.**

## Route 10: real feasibility, CAD, Tarski–Seidenberg, and Positivstellensatz certificates

### Precise problem

Input a quantifier-free formula in \(n\) real variables built from \(s\) integer polynomials of degree at most \(m\) and coefficient bit size \(\tau\).

The existential problem asks whether

\[
\exists x\in\mathbb R^n:
f_i(x)=0,\quad g_j(x)>0,\quad q_k(x)\geq0 .
\]

The general first-order problem allows alternating quantifiers.

Tarski–Seidenberg guarantees that projections of semialgebraic sets are semialgebraic and hence that quantifier elimination exists.

### Classical complexity

For existential formulas, critical-point and roadmap methods have singly exponential dependence

\[
(sm)^{O(n)}
\]

up to coefficient-bit factors.

Real feasibility lies in PSPACE by Canny [DOI 10.1145/62212.62257](https://doi.org/10.1145/62212.62257).

The existential theory of the reals defines the class \(\exists\mathbb R\), with many geometric problems complete for it; a current compendium is [arXiv:2407.18006](https://arxiv.org/abs/2407.18006).

General quantifier elimination and CAD have doubly exponential worst-case behavior in the number of variables.

Davenport–Heintz show that doubly exponential output size is intrinsic for general real quantifier elimination [DOI 10.1016/S0747-7171(88)80004-X](https://doi.org/10.1016/S0747-7171(88)80004-X).

The practical software baseline includes:

- Mathematica `Reduce`;
- Maple `RegularChains`;
- QEPCAD B;
- Redlog;
- `msolve`;
- CAD and virtual-substitution implementations;
- roadmap and critical-point implementations from real-algebraic-geometry libraries.

The standard reference for algorithms and singly versus doubly exponential regimes is [DOI 10.1007/3-540-33099-2](https://doi.org/10.1007/3-540-33099-2).

### Why direct amplitude search fails

A real algebraic variety defined by equalities has measure zero in the ambient continuous domain.

Uniform continuous sampling never hits it exactly.

A discretized Grover search requires a robustness promise:

- a bounded search box;
- a feasible ball or tube of known radius;
- enough grid bits to represent a witness;
- residual separation away from feasibility.

Without that promise, roots may require exponentially many bits and may be arbitrarily ill-conditioned.

A robust grid with \(L\) points per coordinate has \(L^n\) cells.

Grover reduces enumeration to \(L^{n/2}\), still exponential and generally not competitive with geometry-aware singly exponential algorithms.

### CAD and quantum search

One could amplitude-amplify over projection cells or sign conditions.

But constructing the projection polynomials and cell adjacency is already the CAD bottleneck.

The number of cells may be doubly exponential.

If the output is a full CAD or quantifier-free formula, the Davenport–Heintz output lower bound applies to quantum algorithms as well.

For an existential Boolean answer, a quantum method might avoid outputting the decomposition, but no Fock-space observable presently represents all sign conditions.

### PSPACE interpretation

\(\mathrm{BQPSPACE}=\mathrm{PSPACE}\) [DOI 10.1006/jcss.1999.1655](https://doi.org/10.1006/jcss.1999.1655).

This rules out a quantum-versus-classical complexity-class separation based only on polynomial space.

It does not prove that no particular real-feasibility instance can have a polynomial or practical space improvement.

An efficient general BQP algorithm for \(\exists\mathbb R\)-complete feasibility would nevertheless be a major, presently unsupported complexity collapse.

### Positivstellensatz route

For an infeasible basic semialgebraic set, Stengle-type certificates express \(-1\) using the ideal of equality constraints and the preordering generated by inequalities.

Under an Archimedean quadratic module, Putinar-type certificates express every polynomial strictly positive on the feasible set as

\[
c-\lambda
 =
 \sigma_0+\sum_j\sigma_jg_j+\sum_k u_kh_k.
\]

Truncating degrees gives Lasserre.

Degree bounds can be extremely large and depend on the positivity margin; quantitative bounds for Putinar certificates are studied in [arXiv:0812.2657](https://arxiv.org/abs/0812.2657).

SOS lower bounds for random CSP refutation can require degree growing linearly in \(n\) in relevant density regimes [arXiv:1701.04521](https://arxiv.org/abs/1701.04521).

### Quantum observable and precision

For a fixed certificate degree \(2r\), a quantum SDP solver can estimate the relaxation value.

It does not output the SOS polynomials unless their Gram matrices are read out.

A scalar estimate can be meaningful if the task accepts a trusted quantum value.

For an independently checkable certificate, the classical output may have \(\Theta(B_r^2)\) entries.

Weak feasibility and exponentially small positivity margins force high precision.

### Dequantization risk

High.

Chordal and term-sparse SOS methods are designed precisely to avoid the dense matrix.

Low-rank certificate matrices admit Burer–Monteiro and sketching attacks.

If a certificate is sparse enough to load cheaply, it may also be sparse enough to compute classically.

### Hardware fit

Boolean semialgebraic problems map naturally to Ising models.

Continuous inequalities require slack variables, discretization, or penalty gadgets.

The real slack substitutions

\[
g(x)=y^2
\quad\text{or}\quad
g(x)y^2=1
\]

encode nonnegativity or strict positivity only when \(x,y\) are already restricted to real values.

Over \(\mathbb C\), every nonzero number has a square root, so the order information disappears.

Annealers can attack the discretized Boolean problem heuristically.

MBQC can implement a digital quantum SDP or amplitude search.

Boson sampling supplies permanents, not quantifier elimination or Positivstellensatz certificates.

### Plausibility score

**1/5 for general ETR/CAD; 2/5 for a fixed sparse SOS value with no certificate output.**

## Hardware comparison

| Route | cheapest heuristic hardware | is real/positive structure native? | decisive overhead |
|---|---|---|---|
| Hermite signature | MBQC/QSVT | real symmetric matrix is natural; signature is not | quotient/Hermite oracle and sign gap |
| \(K\)-fixed states | real interferometer, two-copy test | real amplitudes natural to prepare | antiunitary selection impossible |
| real-radical inverse system | CV moment measurement, MBQC SDP | PSD moments are natural | radical extraction and readout |
| residual spectral hierarchy | spinor BEC, Bose-Hubbard, MBQC | real coherent ansatz natural | nonlinear interactions, cooling, guide overlap |
| full Lasserre | universal MBQC or quantum SDP | moment positivity is natural | maximal-symmetry/localizing constraints |
| quadrature potential | CV photonics/oscillators | yes, position is real | no normalizable zero modes; non-Gaussian terms |
| positive toric | Bose-Hubbard, parametric hopping | Perron positivity is native | does not enforce coherent-label positivity |
| Boolean/totally real | Ising annealer, QAOA | yes | gadgets, small gaps, Grover ceiling |
| critical-point search | BEC/VQE plus digital filtering | real ansatz is natural | real selection and minimum readout |
| CAD/ETR | MBQC or annealer after discretization | no | exponential grid/CAD and postselection |

Passive linear optics implements unitary changes of variables and prepares coherent product states.

It does not implement general \(m\)-boson terms.

KLM-style postselected linear optics is universal [DOI 10.1038/35051009](https://doi.org/10.1038/35051009), but an exponentially unlikely postselection event is an exponential runtime.

Boson sampling natively estimates samples whose amplitudes contain permanents [arXiv:1011.3245](https://arxiv.org/abs/1011.3245).

No route above reduces a Hermite signature, real radical, Lasserre value, or CAD projection to that native permanent observable.

The spinor-BEC conic remains the cleanest condensed-matter demonstration through D-spin-mixing-hamiltonian.

It has fixed mode number and therefore is not an asymptotic speedup family.

## Ranked routes

1. **Sparse residual or canonical spectral hierarchy on the real sphere — 3/5.**  
   It yields a real optimization lower bound from one symmetric-sector eigenvalue and has a direct bosonic realization. The target must be compared with implicit classical Lanczos, not dense SDP.

2. **Normalized Hermite signature with a genuinely succinct Hermite oracle — 2/5.**  
   This is the right coarse real-root observable. It survives only for dense-real families with constant additive precision and currently lacks a hard, non-dequantized polynomial-system family.

3. **Real-radical inverse system obtained from a truncated moment state — 2/5.**  
   It is the exact ground-space answer and could expose a quantum space advantage if only scalar kernel information is required. Computing or reading the real radical is otherwise circular.

4. **Positive toric fibre Hamiltonians — 2/5 for speedup, 4/5 for hardware.**  
   The Bose-Hubbard picture sees Perron positivity and the moment polytope naturally. That same stoquastic structure gives the strongest classical simulation route.

5. **Totally real Boolean varieties — 2/5.**  
   They remove the real/complex mismatch exactly and are Ising-native, but reproduce standard Grover, counting, and annealing limitations.

No general CAD, Sturm, quadrature, or coherent-state variational route reaches a north-star score above 2.

## Killers

### K-RV1: real and positive states are not complex-linear sectors

Reality and entrywise positivity define cones or real forms, not complex subspaces.

Ordinary Hamiltonian ground spaces and projectors are complex-linear.

An antiunitary symmetry does not create the missing projector.

### K-RV2: the positive or real locus is often Zariski dense

For smooth real components and positive toric varieties, real or positive points can have the same vanishing ideal as the complex variety.

Their coherent states then span the same inverse system.

No linear observable on the span remembers which labels were positive.

### K-RV3: exact real counts consume the compression in precision

A signature changes in units of one.

Normalized trace estimation must use error \(O(1/D)\) to recover the count.

Amplitude estimation then costs \(O(D)\), while shot-based estimation costs \(O(D^2)\).

This is robotics K2 and K3 in spectral language.

### K-RV4: real points are usually the rare points applications care about

Robotics, statistics, and power systems often have exponentially or combinatorially many complex critical points but only a few feasible real-positive ones.

Constant-additive real-root density is then zero for all practical purposes.

### K-RV5: a Hermite block encoding presupposes quotient algebra access

The seed gives a Macaulay Hamiltonian, not a Hermite matrix oracle.

Building the trace form needs a quotient basis, multiplication access, and stable transport between degrees.

Those are already central outputs of Gröbner, border-basis, or root-solving algorithms.

### K-RV6: Hermite conditioning contains the root-separation problem

The Hermite matrix factors through a Vandermonde matrix.

Near-conjugate roots and root collisions produce small eigenvalues.

The QSVT sign cost then inherits an exponentially small normalized inertia gap.

### K-RV7: \(H_N\) is not the Lasserre relaxation

The seed ground energy drops the Hankel/maximal-symmetry and localizing constraints.

It is a spectral relaxation below the order-\(N\) SOS value.

Any claimed Lasserre or DPS equivalence must be withdrawn unless those constraints are explicitly enforced.

### K-RV8: the R1 memory comparison changes the problem

The 250 GB number belongs to a dense moment matrix.

The seed spectral Hamiltonian is sparse and admits an \(O(M_N)\)-memory classical Krylov method.

A quantum space claim cannot compare the spectral problem with dense SDP storage.

### K-RV9: sparse and chordal classical solvers attack the real bottleneck

TSSOS, CS-TSSOS, Burer–Monteiro, STRIDE, and first-order SDP solvers routinely avoid the dense block.

A quantum algorithm must beat the largest sparse clique or implicit matvec baseline, not \(B_r^3\).

### K-RV10: scalar quantum output is not a real-algebraic certificate

A Lasserre value estimated by a trusted device is not an SOS decomposition.

A real root sample is not an isolating box.

A low-energy state is not a Positivstellensatz refutation.

Certification culture in robotics and optimization may reject the weaker output.

### K-RV11: positive toric Hamiltonians are stoquastic

Their sign-free hopping is the best hardware feature and the largest dequantization warning.

The same fibre gap controls classical Markov-chain methods.

### K-RV12: real coherent variational search is classically parameterized

A real coherent state has only \(O(n)\) parameters.

Its residual energy and derivatives are explicit.

Entangling the ansatz can lower the relaxation value but moves it away from the real variety.

### K-RV13: general real feasibility has no robust sampling measure

Equality varieties have ambient measure zero.

Grid search requires a thickness and coordinate-bit promise absent from ETR.

Without robustness, amplitude amplification has no finite target fraction.

### K-RV14: full quantifier elimination may have doubly exponential output

A quantum computer cannot output a doubly exponential CAD or quantifier-free formula in polynomial time.

Only decision, scalar, or sample outputs remain candidates.

### K-RV15: hardware universality is not a cheap heuristic attack

Postselected photonics and MBQC can implement universal algorithms, but their success probability, loss, feed-forward, nonlinear resource count, and precision remain part of runtime.

A bosonic notation alone does not make a real-algebraic observable native.

## Proposed definitions

MERGE PROPOSAL (`definitions/definitions.md`, new entry):

### D-real-locus-and-real-radical
For a homogeneous ideal \(I\subseteq\mathbb R[z_0,\ldots,z_n]\), its real projective locus is
\[
V_{\mathbb R}(I)=\{[x]\in\mathbb P^n(\mathbb R):f(x)=0\ \forall f\in I\},
\]
and its real radical is
\[
\sqrt[\mathbb R]{I}=I(V_{\mathbb R}(I))
=\{q\in\mathbb R[z]:q(x)=0\ \forall[x]\in V_{\mathbb R}(I)\}.
\]
Equivalently, \(q\in\sqrt[\mathbb R]{I}\) iff there exist \(k\ge1\) and a sum of squares \(\sigma\) with \(q^{2k}+\sigma\in I\). Its complexification is \(J=\sqrt[\mathbb R]{I}\otimes_{\mathbb R}\mathbb C\).
Source: Real Nullstellensatz; Basu–Pollack–Roy, DOI 10.1007/3-540-33099-2.
Pitfalls: \(\sqrt[\mathbb R]{I}\) is not generally the ordinary radical \(\sqrt I\); computing it is a real-algebraic problem. If \(V_{\mathbb R}(I)\) is Zariski dense in \(V(I_{\mathbb C})\), complexification removes no complex component.

MERGE PROPOSAL (`definitions/definitions.md`, new entry):

### D-real-coherent-span
For \(I\subseteq\mathbb R[z_0,\ldots,z_n]\), \(J=\sqrt[\mathbb R]{I}\otimes_{\mathbb R}\mathbb C\), and degree \(N\),
\[
\mathcal G_N^{\mathbb R}:=
\operatorname{span}_{\mathbb C}\{|x\rangle^{\otimes N}:[x]\in V_{\mathbb R}(I),\ \|x\|=1\}
=(J_N)^\perp.
\]
Thus a D-hamiltonian built from generators whose degree-\(N\) ideal piece is \(J_N\) has ground space equal to the complex span of real-point coherent states.
Source: the reproducing identity in D-coherent-state applied to the vanishing ideal of \(V_{\mathbb R}(I)\).
Pitfalls: the set of real coherent states is nonlinear; only its complex span is a ground space. When the real locus is Zariski dense, \(\mathcal G_N^{\mathbb R}\) equals the ordinary radical complex ground space and does not select real labels.

MERGE PROPOSAL (`definitions/definitions.md`, new entry):

### D-real-structure
For a complex Hilbert space with a fixed real orthonormal basis, \(K\) is coefficientwise conjugation, an antiunitary involution. Its fixed set \(\operatorname{Fix}(K)\) is a real Hilbert space but not a complex-linear subspace. A real-coefficient D-hamiltonian commutes with \(K\), so each eigenspace has a real basis, but degenerate eigenspaces contain complex superpositions and there is no complex-linear projector with range \(\operatorname{Fix}(K)\).
Source: elementary antiunitary linear algebra.
Pitfalls: \(K\)-invariance of an operator does not project onto real points. The scalar \(|\langle\psi|K\psi\rangle|^2\) is nonlinear in a one-copy state and is not the expectation of a one-copy observable.

MERGE PROPOSAL (`definitions/definitions.md`, new entry):

### D-hermite-trace-form
Let \(I\subseteq\mathbb R[x_1,\ldots,x_n]\) be zero dimensional, \(A=\mathbb R[x]/I\), \(\mathcal B=(b_1,\ldots,b_D)\) a basis, and \(M_h\) multiplication by \(h\) on \(A\). For \(g\in\mathbb R[x]\), the Hermite trace form and its matrix are
\[
\mathfrak h_g(u,v)=\operatorname{Tr}_A(M_{guv}),\qquad
\mathcal H_g(\mathcal B)_{ij}=\operatorname{Tr}_A(M_{g b_i b_j}).
\]
Its signature is
\[
\operatorname{sig}\mathcal H_g
=\#\{x\in V_{\mathbb R}(I):g(x)>0\}
-\#\{x\in V_{\mathbb R}(I):g(x)<0\}.
\]
In particular \(\operatorname{sig}\mathcal H_1=\#V_{\mathbb R}(I)\) as a count of distinct real roots.
Source: multivariate Hermite theorem, arXiv:2110.10313.
Pitfalls: this is an algebraic trace form, not D-toeplitz-operator and not merely \(\operatorname{Tr}M_g\). The matrix is basis-dependent by congruence although its inertia is invariant. Exact signature requires integer resolution and can be ill-conditioned numerically.

MERGE PROPOSAL (`definitions/definitions.md`, new entry):

### D-lasserre-order
For a real homogeneous form \(c\) of degree \(2m\) on the unit sphere and an integer \(r\ge m\), the order-\(r\) sphere SOS bound is
\[
\operatorname{sos}_r(c)=
\max\{\lambda:(\sum_i x_i^2)^{r-m}c-\lambda(\sum_i x_i^2)^r\text{ is SOS}\}.
\]
Its dual moment matrix is indexed by homogeneous monomials of degree \(r\), hence acts on \(\operatorname{Sym}^r(\mathbb R^{n+1})\); moments extend through degree \(2r\). Therefore the corresponding D-symmetric-sector has boson number \(N=r\), not \(2r\). For inequalities and equalities, order \(r\) additionally imposes the usual localizing-matrix PSD and equality constraints.
Source: Lasserre, DOI 10.1137/S1052623400366802; Fang–Fawzi, arXiv:1908.05155.
Pitfalls: a general density operator on the symmetric sector is not a moment matrix; the latter has Hankel/maximal-symmetry constraints. A fixed Hamiltonian ground energy is therefore not automatically the Lasserre value.

MERGE PROPOSAL (`definitions/definitions.md`, new entry):

### D-residual-spectral-hierarchy
For real homogeneous residuals \(f_1,\ldots,f_d\) of common degree \(m\), set \(c(x)=\sum_j f_j(x)^2\) and, for \(N\ge m\),
\[
A_N=\frac{(N-m)!}{N!}H_N.
\]
Then \(\langle x^{\otimes N}|A_N|x^{\otimes N}\rangle=c(x)\) for every real unit \(x\), and
\[
\lambda_{\min}(A_N)\le\operatorname{sos}_N(c)\le\min_{\|x\|=1}c(x).
\]
The first value is a presentation-dependent spectral relaxation obtained from the supplied residual Gram representation.
Source: D-coherent-state and D-symmetric-tensor-of-a-form; comparison with the sphere spectral/SOS hierarchies in arXiv:2310.17827 and DOI 10.1137/24M1717750.
Pitfalls: \(\lambda_{\min}(A_N)\) is not generally the order-\(N\) Lasserre value or the canonical Lovitz–Johnston spectral value. The relevant gap for ground-energy estimation is the gap above \(\lambda_{\min}(A_N)\), not D-macaulay-gap unless the minimum is zero.

MERGE PROPOSAL (`definitions/definitions.md`, new entry):

### D-positive-toric-part
For a projective toric ideal \(I_A\), the positive part is \(V(I_A)\cap\mathbb P^n(\mathbb R_{>0})\) and the nonnegative part is its closure in \(\mathbb P^n(\mathbb R_{\ge0})\). The algebraic moment map identifies the nonnegative part with the defining polytope under the standard toric hypotheses. In D-toric-ideal, consistently signed binomial generators produce stoquastic weighted fibre Laplacians whose kernel vectors have nonnegative occupation-basis amplitudes.
Source: Sottile, arXiv:math/0212044.
Pitfalls: occupation-basis positivity is not positivity of a coherent-state label. The positive torus is normally Zariski dense, so its coherent-state span equals the complex toric inverse system and is not selected by a projector.

## Proposed claim rows

### C-NEW-RV-REAL-SPAN
- statement: For every homogeneous ideal \(I\subseteq\mathbb R[z_0,\ldots,z_n]\), every \(N\ge0\), and \(J=\sqrt[\mathbb R]{I}\otimes_{\mathbb R}\mathbb C\),
  \[
  \operatorname{span}_{\mathbb C}\{|x\rangle^{\otimes N}:[x]\in V_{\mathbb R}(I),\|x\|=1\}=(J_N)^\perp.
  \]
- status: CONJECTURE
- depends-on: D-coherent-state, D-real-locus-and-real-radical, D-real-coherent-span
- where-proved: proposed in `scouting/real-variety.md`, Route 3
- where-tested: none
- north-star relevance: exact identification of the ground space that sees all real points.
- traps audited: treating the ground space as the point set; real locus may be Zariski dense; real-radical preprocessing.

### C-NEW-RV-NO-K-PROJECTOR
- statement: For every nonzero complex Hilbert space \(\mathcal H\) with conjugation \(K\), there is no nonzero complex-linear orthogonal projector \(P\) with \(\operatorname{ran}P=\operatorname{Fix}(K)\); consequently, for every real-coefficient D-hamiltonian, commutation with \(K\) alone cannot define a Hamiltonian sector consisting of real ground states.
- status: CONJECTURE
- depends-on: D-real-structure, D-hamiltonian
- where-proved: proposed in `scouting/real-variety.md`, Route 2
- where-tested: none
- north-star relevance: rules out the cheapest proposed real-locus selector.
- traps audited: changing a nonlinear state property into a linear projector.

### C-NEW-RV-HERMITE-SIGNATURE
- statement: For every zero-dimensional ideal \(I\subseteq\mathbb R[x_1,\ldots,x_n]\), every quotient basis \(\mathcal B\), and every \(g\in\mathbb R[x]\),
  \[
  \operatorname{sig}\mathcal H_g(\mathcal B)
  =
  \#\{x\in V_{\mathbb R}(I):g(x)>0\}
  -
  \#\{x\in V_{\mathbb R}(I):g(x)<0\},
  \]
  and for \(g=1\) this is the number of distinct real roots.
- status: CONJECTURE
- depends-on: D-hermite-trace-form
- where-proved: cited in `scouting/real-variety.md`, Route 1; arXiv:2110.10313
- where-tested: none
- north-star relevance: supplies the correct real-root observable.
- traps audited: algebraic trace versus Hilbert-space trace; multiplicities; exact integer output.

### C-NEW-RV-NORMALISED-INERTIA
- statement: For every family of radical zero-dimensional real ideals whose Hermite matrices \(\mathcal H_g\) have block encodings of cost \(T_{\mathcal H}\), normalization \(\alpha_{\mathcal H}\), dimension \(D\), and no nonzero eigenvalue in \((-\eta\alpha_{\mathcal H},\eta\alpha_{\mathcal H})\), the normalized signature \(D^{-1}\operatorname{sig}\mathcal H_g\) can be estimated to additive error \(\epsilon\) with \(\widetilde O(T_{\mathcal H}/(\eta\epsilon))\) coherent block-encoding uses; recovering the exact integer by this estimator requires \(\epsilon<1/(2D)\).
- status: CONJECTURE
- depends-on: D-hermite-trace-form, D-qsvt, D-dqc1-style-estimate
- where-proved: proposed in `scouting/real-variety.md`, Route 1
- where-tested: none
- north-star relevance: isolates the only plausible additive real-root statistic.
- traps audited: precision, Hermite-oracle construction, stochastic trace dequantization, root separation.

### C-NEW-RV-LASSERRE-INDEX
- statement: For every real homogeneous form \(c\) of degree \(2m\) and every sphere SOS order \(r\ge m\), the primal moment matrix is indexed by degree-\(r\) monomials and acts on \(\operatorname{Sym}^r(\mathbb R^{n+1})\), while its entries contain moments through degree \(2r\); hence the corresponding total-degree Fock sector is \(N=r\).
- status: CONJECTURE
- depends-on: D-lasserre-order, D-symmetric-sector
- where-proved: cited in `scouting/real-variety.md`, Route 5; arXiv:1908.05155
- where-tested: none
- north-star relevance: corrects the resource count for robotics R1.
- traps audited: hiding a factor-two indexing change; dense versus symmetric storage.

### C-NEW-RV-RESIDUAL-SPECTRAL
- statement: For every tuple of real homogeneous forms \(f_1,\ldots,f_d\) of common degree \(m\), every \(N\ge m\), and \(c(x)=\sum_jf_j(x)^2\), the normalized operator \(A_N=((N-m)!/N!)H_N\) satisfies
  \[
  \langle x^{\otimes N}|A_N|x^{\otimes N}\rangle=c(x)
  \]
  for all real unit \(x\), and
  \[
  \lambda_{\min}(A_N)\le\operatorname{sos}_N(c)\le\min_{\|x\|=1}c(x).
  \]
- status: CONJECTURE
- depends-on: D-coherent-state, D-symmetric-tensor-of-a-form, D-residual-spectral-hierarchy, D-lasserre-order
- where-proved: proposed in `scouting/real-variety.md`, Routes 4–5
- where-tested: none
- north-star relevance: surviving corrected form of robotics R1.
- traps audited: changing the output; presentation dependence; spectral versus SDP relaxation.

### C-NEW-RV-R1-NONEQUIVALENCE
- statement: For every Lasserre order \(r\), the full real moment relaxation optimizes over maximally symmetric/Hankel positive semidefinite matrices satisfying equality and localizing constraints, whereas minimization of a fixed D-hamiltonian over \(R_r\) optimizes over all density operators on that symmetric sector; therefore equality between the seed ground energy and the order-\(r\) Lasserre value does not hold without additional operators enforcing all moment and localizing constraints.
- status: CONJECTURE
- depends-on: D-lasserre-order, D-residual-spectral-hierarchy, D-hamiltonian
- where-proved: proposed in `scouting/real-variety.md`, Route 5
- where-tested: proposed numerical counterexample search on quartic sphere objectives
- north-star relevance: rejects the current statement of robotics bet R1 while preserving the spectral subroute.
- traps audited: comparing different optimization problems; dense SDP versus sparse eigenproblem.

### C-NEW-RV-TORIC-POSITIVITY
- statement: For every projective toric variety whose positive torus is Zariski dense and every degree \(N\),
  \[
  \operatorname{span}_{\mathbb C}
  \{|x\rangle^{\otimes N}:x\in V(I_A)\cap\mathbb R_{>0}^{n+1}\}
  =(I(V(I_A))_N)^\perp;
  \]
  hence no complex-linear projector on the coherent-state span distinguishes positive toric labels from general complex toric labels.
- status: CONJECTURE
- depends-on: D-positive-toric-part, D-toric-ideal, D-coherent-state
- where-proved: proposed in `scouting/real-variety.md`, Route 7
- where-tested: none
- north-star relevance: identifies both the best hardware fit and its linear-algebraic no-go.
- traps audited: Perron positivity versus label positivity; stoquastic dequantization.

### C-NEW-RV-BOOLEAN-TOTALLY-REAL
- statement: For every ideal containing \(x_i^2-x_i\) for all affine variables \(x_i\), every complex point of its affine variety is real and lies in \(\{0,1\}^n\); consequently the ordinary D-hamiltonian has no real/complex point mismatch on its coherent product ground states, although projection and exact counting retain the D-coherent-gram-matrix and \(\#\mathrm P\) precision costs.
- status: CONJECTURE
- depends-on: D-boolean-ideal, D-coherent-state, D-hardness-anchors
- where-proved: proposed in `scouting/real-variety.md`, Route 8
- where-tested: existing Boolean numerics
- north-star relevance: exact real calibration family and Ising hardware hook.
- traps audited: Grover-limited overlap; exact versus additive count; irrelevant torsion.

## Questions for TJO

1. **Ratchet the R1 correction now?**  
   The claim that the seed ground energy is the Lasserre/DPS value is structurally false without maximal-symmetry and localizing constraints. Recommendation: enter C-NEW-RV-LASSERRE-INDEX, C-NEW-RV-RESIDUAL-SPECTRAL, and C-NEW-RV-R1-NONEQUIVALENCE together before funding the R1 experiment.

2. **Does a quantum-only scalar lower bound count as certification?**  
   If an explicit SOS dual certificate is required, the full moment/SOS route loses most of its output advantage. If a trusted scalar estimate is acceptable, a quantum SDP or spectral-value target remains open.

3. **Is normalized real-root density an acceptable problem?**  
   It is the only Hermite output compatible with constant additive precision. It does not answer existence or rare-real-root applications. Recommendation: accept it only if a natural dense-real input family and a hardness result are found first.

4. **Should the Hermite route receive one bounded oracle-construction probe?**  
   The decisive question is whether \(\mathcal H_g\) can be block-encoded from D-macaulay-map access without first computing a \(D\)-element quotient basis. Recommendation: one analytic day; close the route if the construction is circular.

5. **Should robotics R1 be reframed as a spectral-hierarchy comparison?**  
   The corrected competitor is implicit Lanczos on \(A_N\), not dense Lasserre. Recommendation: test \(N=2,3,4\) on a small robust-perception instance and compare bounds, matvec counts, guide overlap, and spectral gap against LOBPCG and STRIDE.

6. **Does the positive-toric hardware demonstration count as a product?**  
   It is the most natural Bose-Hubbard realization but probably the most dequantizable. Recommendation: treat it as an analogue demonstration or dictionary theorem, not a speedup candidate.

7. **May a real-radical oracle be part of the input promise?**  
   Supplying it makes the real coherent-span theorem operational but removes the hard real-algebraic step. Recommendation: allow it only for studying downstream observables, never in a real-feasibility speedup claim.

8. **Which real output matters most: count, value, sample, or certificate?**  
   These lead to different complexity regimes. Recommendation: prioritize a fixed-order scalar lower bound; exact count and full certificate are blocked by precision and output size, while samples are blocked by overlap and real selection.

9. **Correct the robotics space statement?**  
   The dense level-3 SDP block is 250 GB, but the seed spectral matrix admits \(O(B_3)\)-space Lanczos. Recommendation: remove “250 GB versus 300 qubits” from R1 unless the target is explicitly the full structured SDP.

10. **Close general ETR/CAD as a Fock-space arm?**  
    No route found a real/positive projector, robust sampling measure, or output model compatible with the north star. Recommendation: retain ETR only as a hardness boundary and focus D11 on Hermite inertia, the corrected spectral hierarchy, and real-radical moment kernels.