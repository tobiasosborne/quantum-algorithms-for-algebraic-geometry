# Decision rule

This memo follows conventions C1–C12 in `definitions/definitions.md`.

In particular, \(R=\mathbb C[z_0,\ldots,z_n]\), \(N\) is unary, \(H_N=\Phi_N\Phi_N^\dagger\), and every spectral promise uses \(\Delta_N/\alpha_{\mathrm{BE}}\), not \(\Delta_N\) alone.

A score awards one point for each PRD §2 requirement:

1. a precise algebraic-geometric problem with explicit input and output;
2. a quantum bound beating the best classical bound for that same input and output;
3. an advantage surviving state preparation, conditioning, overlap, precision, and readout;
4. resistance to the relevant dequantization;
5. a plausible cheap hardware route using postselected linear optics, MBQC, boson sampling, Bose–Hubbard, spinor-BEC, or a comparably natural device.

Interpretation:

- \(0\): no relevant algorithmic problem remains.
- \(1\): a dictionary or negative result only.
- \(2\): a conditional polynomial or Grover-type improvement, or a good hardware experiment without an asymptotic advantage.
- \(3\): a real quantum speedup exists, but either the input model is artificial or the required hardware hook is absent.
- \(4\): four PRD criteria are credible; one decisive gap remains.
- \(5\): a north-star-quality route, ready for a proposer/critic cycle.

No primitive scores \(4\) or \(5\) in this round.

The strongest existing quantum speedup is Kedlaya’s curve-zeta algorithm, but it has no natural cheap hardware attack and does not combine with the seed’s complex-amplitude compression.

The strongest hardware fits are boson sampling and the seed’s analogue Hamiltonians, but neither presently computes a useful algebraic-geometric invariant faster than its classical baseline.

The recurring killers are:

- condition numbers and normalized spectral gaps;
- state-preparation or ground-space overlap;
- replacing an explicit classical input by a much stronger coherent oracle;
- returning a quantum state or sample instead of the requested root, count, or certificate;
- estimating a normalized quantity whose geometric signal is exponentially small;
- mistaking a natural physical realization for an algorithm that reads its degeneracy efficiently;
- mistaking permanent-weighted sampling for permanent evaluation.

# 1. QLSA, HHL, and QSVT on Macaulay matrices

### Problem P

Input: \(m\) Boolean polynomials in \(n\) variables, represented sparsely over \(\mathbb F_2\), together with Boolean field equations.

Chen–Gao lift the system to a Macaulay linear system over \(\mathbb C\).

The requested output is either a decision that a Boolean solution exists or an explicit Boolean solution.

This lives in `scouting/classical-landscape.md` §3, §6, §7, and §9.

It must be distinguished from the seed’s tasks:

- estimating \(\langle f|P_0|f\rangle\);
- estimating \(\operatorname{Tr}P_0/M_N\);
- applying the spectral projector \(P_0\);
- sampling from an inverse-system state.

Those are rows C-052–C-068 and are not repetitions of the Chen–Gao solve.

### Quantum resource bound as literally stated in the source

Chen–Gao state a runtime polynomial in the encoded Boolean-system size and the condition number of their Macaulay system.

Their result is therefore polynomial only under a polynomial-condition-number promise.

They do not return the full linear-system vector; repeated state preparation and measurement are used to recover Boolean coordinates.

The original matrix analyzed by Ding et al. has approximately

\[
(m+n)(3n+1)^n
\times
(3n+1)^n
\]

dimensions.

For a unique Boolean solution of Hamming weight \(h\), Ding et al. prove a condition-number lower bound of order

\[
\kappa=\Omega\!\left(\sqrt{\binom nh}\right)
\]

for the relevant truncated QLS condition number.

For the original maximum degree \(3n\), they also give stronger evidence that the lower bound grows at least like \(h^h/2\); the paper reports symbolic verification only through \(n=300\), so that strengthening is not a theorem for all \(n\).

Their reduced Boolean Macaulay matrix has size \(m2^n\times2^n\).

Their improved algorithm runs in

\[
\widetilde O(\operatorname{poly}(n)\kappa(M))
\]

time, uses \(O(\log n)\) solution-state copies after isolation, and incurs \(O(n\log n)\) trials from the Valiant–Vazirani isolation step.

They explicitly leave open a useful regime when the solution Hamming weight is logarithmic.

These statements are in [Ding–Gheorghiu–Gilyén–Hallgren–Li, arXiv:2111.00405, DOI 10.22331/q-2023-07-26-1069](https://arxiv.org/abs/2111.00405).

The generic HHL theorem prepares a state proportional to \(A^{-1}b\), rather than printing \(A^{-1}b\), with polynomial dependence on \(\kappa\), sparsity, and inverse accuracy and logarithmic dependence on matrix dimension under sparse coherent access [DOI 10.1103/PhysRevLett.103.150502](https://doi.org/10.1103/PhysRevLett.103.150502).

QSVT improves the functional-calculus machinery but does not remove the singular-value threshold or input/output qualifications [arXiv:1806.01838, DOI 10.1145/3313276.3316366](https://arxiv.org/abs/1806.01838).

### Best classical baseline

For the Boolean search problem, the baseline is not dense Gaussian elimination.

The relevant competitors are:

- BooleanSolve and hybrid guessing plus sparse linear algebra;
- F4/F5 at the degree of regularity;
- block Wiedemann or Lanczos over \(\mathbb F_2\);
- Grover search over assignments or fixed-Hamming-weight assignments;
- the quantum BooleanSolve variants that Groverize the classical outer search.

Under its regularity assumptions, classical BooleanSolve has expected complexity \(O(2^{0.792n})\) for \(m=n\) [arXiv:1112.6263](https://arxiv.org/abs/1112.6263).

A quantum BooleanSolve variant reports \(O(2^{0.462n})\) gates under a natural algebraic assumption [arXiv:1712.07211](https://arxiv.org/abs/1712.07211).

A separate area-time analysis gives time exponent \(0.45743\) and area exponent \(0.01467\) for square Boolean MQ, under its stated assumptions [DOI 10.1007/978-3-319-79063-3_23](https://doi.org/10.1007/978-3-319-79063-3_23).

For the seed’s degree-local distance problem, the correct classical comparison is sparse QR, LSQR, LSMR, Lanczos filtering, or randomized range finding on \(\Phi_N\) or \(H_N\), as stated in the classical memo §3.

### Dequantization and hidden costs

Low-rank dequantization applies when the matrix is close to low rank and the classical algorithm has length-square sample/query access.

Under those assumptions, a classical algorithm can sample from an approximate low-rank pseudoinverse solution [arXiv:1811.04909](https://arxiv.org/abs/1811.04909).

The broader sampling-based framework dequantizes low-rank QSVT in time independent of ambient dimension under suitable \(\ell^2\)-sampling access [arXiv:1910.06151](https://arxiv.org/abs/1910.06151).

The seed’s \(H_N\) is sparse and generally high rank, so those low-rank theorems do not directly dequantize C-056.

That is not a clean escape.

Sparse-matrix QSVT with constant precision admits classical simulation in important regimes, while inverse-polynomial precision can remain BQP-complete [arXiv:2111.09079](https://arxiv.org/abs/2111.09079).

The hidden costs are:

- construction of a reversible sparse-row oracle;
- block-encoding normalization;
- \(\kappa\) or \(\alpha_{\mathrm{BE}}/\Delta_N\);
- preparation of \(|b\rangle\) or \(|f\rangle\);
- probability of landing on the solution-carrying coordinates;
- repeated copies required to recover all Boolean variables;
- coefficient precision in the complex lift;
- Valiant–Vazirani repetition;
- loss of the finite-field arithmetic structure.

Ding et al. show that Grover already matches or beats the HHL route on the original construction in the relevant Hamming-weight regimes.

### Heuristic hardware hook

None for the QLSA itself.

Universal MBQC could implement the digital algorithm, but that is not a cheaper heuristic attack.

An annealer can instead encode the Boolean residual objective, but that is Primitive 9 and does not implement HHL.

### Combination with the seed

The seed replaces the inhomogeneous solve \(My=b\) by spectral access to

\[
H_N=\Phi_N\Phi_N^\dagger
\]

and its nullspace projector.

This changes the output and the governing condition number.

Rows C-052–C-058 correctly express the seed cost through \(\alpha_{\mathrm{BE}}/\Delta_N\).

Row C-097 correctly says that no reduction is known between the Ding et al. truncated QLS condition number and the seed’s normalized Macaulay gap.

Consequently, Ding et al. do not formally refute the seed’s distance-to-ideal estimator.

They do refute the inference that “Macaulay plus HHL/QSVT” is by itself a source of speedup.

A useful combination would require an observable such as C-078 or C-166 that avoids full solution readout and a family where both the normalized gap and input overlap are proven polynomial.

No such family is presently known.

### Score and killer

Score: **2/5**.

K-QP1: **The linear-system condition number or seed normalized gap absorbs the apparent exponential compression, while solution readout gives no advantage over Grover or quantum BooleanSolve.**

# 2. Kedlaya point counting, zeta functions, class groups, and Jacobians

### Identifier correction

The identifier supplied in the brief, `quant-ph/0608151`, is not Kedlaya’s paper.

It is an unrelated paper on identical bosonic systems, with DOI 10.1088/0305-4470/39/36/L01.

Kedlaya’s paper is [arXiv:math/0411623, DOI 10.1007/s00037-006-0204-7](https://arxiv.org/abs/math/0411623).

This is a verified correction, not an `[UNVERIFIED]` citation.

### Problem P

Input: a smooth, projective, geometrically irreducible genus-\(g\) curve \(C/\mathbb F_q\), \(q=p^a\).

Kedlaya’s concrete input is a possibly singular plane model \(C'\) of degree polynomial in \(g\), together with explicit data describing the singularities and their resolution so that arithmetic on the normalized curve is polynomial time.

Output: the exact numerator

\[
P_C(T)\in\mathbb Z[T],
\qquad
Z(C,T)=\frac{P_C(T)}{(1-T)(1-qT)},
\]

where \(\deg P_C=2g\).

This yields \(\#C(\mathbb F_{q^r})\) for all \(r\).

This lives in the finite-field branch of classical-landscape §7 and §9, outside the complex input convention D-input-model.

### Quantum resource bound as literally stated in the source

Kedlaya’s Theorem 1 states polynomial time in \(g\) and \(\log q\).

The exponent is not made into a practical gate estimate.

The algorithm constructs unique-encoding black-box presentations of

\[
\operatorname{Cl}(C_{\mathbb F_{q^e}})
\simeq
J_C(\mathbb F_{q^e})
\]

and invokes the quantum order algorithm for finite abelian groups.

For \(e\) satisfying \(16g<q^{e/2}\), Proposition 11 computes the class-group order in time polynomial in \(g\), \(\log q\), and \(e\).

The zeta reconstruction computes cyclic resultants for extension degrees through \(m=\max\{18,2g\}\) in the large-\(q\) part of the proof.

For small \(q\), two extension degrees \(m_1,m_2\), each polynomially bounded in \(g,\log q\), are used to reconstruct the Frobenius eigenvalues.

The output has only \(O(g\log q)\) bits, so the result is not defeated by an exponential-output objection.

### Best classical baseline

For fixed genus, Schoof–Pila type algorithms are polynomial in \(\log q\), but their genus dependence is exponential.

Kedlaya records a bound of the form

\[
(\log q)^{O(g^2\log g)}
\]

for the general classical approach then known.

Cohomological algorithms are polynomial in \(p\), \(g\), and \(a=\log_pq\), so they are effective in small characteristic but not polynomial in \(\log p\).

For fixed dimension and fixed small characteristic, Lauder–Wan compute zeta functions of arbitrary varieties in deterministic polynomial time [arXiv:math/0612147](https://arxiv.org/abs/math/0612147).

Modern \(p\)-adic algorithms are practical for structured curves and hypersurfaces but still retain characteristic, cohomology-dimension, or degree dependence.

For nondegenerate toric hypersurfaces, controlled reduction gives linear dependence on \(p\) in the cited algorithm [arXiv:1806.00368](https://arxiv.org/abs/1806.00368).

A 2025 result places verification of a curve zeta function and Jacobian group structure in \(\mathrm{AM}\cap\mathrm{coAM}\).

It also computes the \(P_1(T)\) factor for a smooth projective surface in quantum \(\operatorname{poly}(D\log q)\) time and classical \(\operatorname{poly}(\log q)\) time when the degree \(D\) is fixed [arXiv:2511.02262](https://arxiv.org/abs/2511.02262).

That result concerns \(P_1\), not the full higher-dimensional zeta function.

### What this says about hypersurfaces

Kedlaya’s curve method depends on realizing \(H^1\) through the Jacobian variety.

There is no analogous general abelian variety carrying all higher cohomology of a hypersurface.

Kedlaya explicitly identifies this as the obstruction in dimensions greater than one.

For diagonal and Fermat-type hypersurfaces, Frobenius eigenvalues can sometimes be reduced to Gauss sums and estimated quantumly [arXiv:quant-ph/0405081](https://arxiv.org/abs/quant-ph/0405081).

That is a structured exception, not a general hypersurface algorithm.

The 2025 \(P_1(T)\) result uses Lefschetz pencils and reduction to curves.

It still does not compute \(P_i(T)\) for arbitrary \(i>1\).

### Dequantization and hidden costs

This speedup is not a QRAM linear-algebra speedup.

It is based on abelian-group order finding, so Tang-style low-rank dequantization is not relevant.

The substantial promises are instead:

- unique encodings for divisor classes;
- polynomial-time group operations;
- polynomial-size curve and desingularization data;
- factorization of finite-field polynomials;
- provably adequate random class-group generators;
- coherent access to all black-box group operations.

The algorithm is exact at the level of the final Weil polynomial, even though its quantum subroutines are probabilistic.

The main practical hidden cost is constructing and fault-tolerantly evaluating Jacobian arithmetic for variable genus.

### Heuristic hardware hook

None.

Small demonstrations of abelian period finding are possible, but neither passive linear optics nor a natural Bose–Hubbard model computes the class-group orders required by the proof.

### Combination with the seed

D-finite-field-analogue explains why the seed does not transport.

Macaulay contraction duality exists over \(\mathbb F_q\), but a register holding every coefficient of a degree-\(N\) polynomial requires \(\dim R_N\log q\) qubits.

Complex amplitude encoding does not preserve finite-field multiplication or rank.

Kedlaya avoids this failure by using divisor-class groups rather than Macaulay coefficient vectors.

The useful lesson for PRD §7 Q7 is negative and sharp:

- do not fund a \(q\)-deformed Fock model merely to reproduce finite-field linear algebra;
- do fund finite-field work only if it identifies a compact geometric group or cohomological object analogous to a Jacobian.

### Score and killer

Score: **3/5**.

K-QP2: **A real superpolynomial quantum advantage exists for variable-genus curves, but it is established prior art with no credible cheap hardware hook and no compact combination with the seed.**

# 3. Hidden nonlinear structures over finite fields

### Problem P

There are three distinct problems.

First, the hidden-radius problem supplies quantum access to randomly shifted spheres

\[
S_r+t
=
\{x\in\mathbb F_q^d:\textstyle\sum_i x_i^2=r\}+t
\]

and asks for \(r\).

Second, the hidden-flat-of-centers problem fixes the radius and asks for an unknown affine flat containing the centers.

Third, the hidden-polynomial problem chooses a bounded-degree polynomial

\[
h\in\mathbb F_q[x_1,\ldots,x_d]
\]

and supplies an oracle whose level sets are exactly the fibers \(h^{-1}(y)\), with the output labels arbitrarily and injectively obfuscated.

The goal is to identify \(h\) up to the equivalence left invisible by the oracle.

These are finite-field variety-identification problems, adjacent to classical-landscape §7.

They are not explicit-equation polynomial solving.

### Quantum resource bound as literally stated in the source

For odd fixed \(d\), Childs–Schulman–Vazirani give a \(\operatorname{poly}(\log q)\)-query algorithm for the hidden radius.

Their classical lower bound is an expected exponential number of queries to obtain even \(1/\operatorname{poly}(d\log q)\) bias about one bit of the radius.

For the hidden flat of centers, the quantum algorithm uses a continuous-time walk on the finite-field unit-sphere graph.

At walk time

\[
t=\frac{1}{\sqrt{q^{d-1}\log q}},
\]

a point on the hidden flat is obtained with total probability approximately \(1/\log q\), followed by noisy linear reconstruction.

For typical bounded-degree hidden polynomials in fixed dimension, the same paper proves only \(\operatorname{poly}(\log q)\) quantum query complexity through distinguishability of level-set states.

It does not provide an efficient measurement for every such polynomial [arXiv:0705.2784, DOI 10.1109/FOCS.2007.18](https://arxiv.org/abs/0705.2784).

Decker–Draisma–Wocjan give the stronger end-to-end result for fixed numbers of variables and fixed total degree:

- classical query complexity \(\Omega(\sqrt q)\);
- quantum running time \(\operatorname{polylog}(q)\);
- constant success probability;
- all but finitely many field sizes \(q\).

See [arXiv:0706.1219](https://arxiv.org/abs/0706.1219).

Decker–Ivanyos–Santha–Wocjan give polynomial-time algorithms for multivariate quadratic hidden-polynomial problems in constant characteristic and for constant-degree polynomial function graphs over arbitrary fields [arXiv:1107.2189, DOI 10.1137/120864416](https://arxiv.org/abs/1107.2189).

Ivanyos–Santha reduce further hidden-structure problems to systems of diagonal polynomial equations and obtain polynomial time when the degree is constant and the number of variables is sufficiently large relative to the number of equations [arXiv:1503.09016](https://arxiv.org/abs/1503.09016).

### Best classical baseline

In the promised black-box model, the relevant baseline is oracle-query lower bounds, not Gröbner bases.

The \(\Omega(\sqrt q)\) lower bound for hidden polynomial function graphs is therefore a genuine exponential separation in the input length \(\log q\).

If \(h\) itself is supplied by its coefficients, classical interpolation is polynomial in the number of coefficients.

If only an ordinary value oracle \(x\mapsto h(x)\) is supplied without obfuscated fibers, bounded-degree interpolation again uses polynomially many evaluations.

The hardness comes from the deliberately forgotten correspondence between fiber labels and field values.

### Dequantization and hidden costs

Tang-style dequantization does not apply because the speedup comes from Fourier interference and hidden symmetry, not low-rank matrix inversion.

The decisive hidden cost is the oracle.

A coherent level-set oracle supplies more structure than:

- sparse equations defining a variety;
- a membership oracle for one variety;
- samples of points on one variety;
- a classical data set.

Implementing the oracle from explicit equations may require solving exactly the polynomial system one hoped to accelerate.

For the information-theoretic Childs–Schulman–Vazirani theorem, the optimal collective measurement on many hidden-polynomial states need not have an efficient circuit.

The Decker-family results close that gap only for their specified bounded-degree cases.

### Is this algebraic geometry in the north-star sense?

Formally, yes.

The fibers are affine hypersurfaces over \(\mathbb F_q\), and the hidden object is their polynomial pencil.

Algorithmically, the target is closer to oracle learning than to computing an invariant of an explicitly presented ideal.

It therefore satisfies the letter of “varieties or ideals” but not the campaign’s usual explicit-input cost model.

### Heuristic hardware hook

No natural analogue hook is known.

Finite-field Fourier transforms and the required oracle are digital.

Postselected linear optics or MBQC can implement them universally, but that supplies no problem-specific cheap experiment.

### Combination with the seed

The seed’s coherent-state frame is a complex projective construction.

It cannot represent \(\mathbb F_q\) level sets while preserving their field arithmetic, by D-finite-field-analogue.

One could complex-lift each level set and apply a point-set Hamiltonian, but the lift has different intersections, norms, and rank.

It also discards the Fourier symmetry that makes the hidden-polynomial algorithms fast.

The useful conceptual combination is narrower:

- hidden-polynomial algorithms show that a family of varieties can be learnable when quantum access preserves interference between fibers;
- the seed currently gives access to one inverse-system subspace, not coherent access to a labeled family of fibers.

Producing the latter from \(H_N\) would be a genuinely new primitive, but no construction is known.

### Score and killer

Score: **3/5**.

K-QP3: **The exponential separation relies on an obfuscated coherent fiber oracle that is strictly stronger than an explicit list of defining equations.**

# 4. Supersymmetric quantum mechanics and Landau–Ginzburg models

### Problem P

Let \(W\in\mathbb C[z_0,\ldots,z_n]\) be a superpotential with isolated critical locus.

The Jacobian or Milnor algebra is

\[
\operatorname{Jac}(W)
=
\mathbb C[z_0,\ldots,z_n]/
(\partial_0W,\ldots,\partial_nW).
\]

Its dimension is the total Milnor number when the critical scheme is zero-dimensional.

For a homogeneous smooth hypersurface \(X=V(W)\subset\mathbb P^n\), graded pieces of this algebra encode primitive Hodge numbers through Griffiths residues.

For a real Morse function \(W\) on a compact manifold, Witten’s deformed de Rham complex gives a supersymmetric Hamiltonian whose low-energy states localize near critical points and whose exact zero modes represent de Rham cohomology.

These problems live in classical-landscape §5, §7, and §10.

### Quantum resource bound as literally stated in the source

The foundational physics and geometry sources supply spectral identifications, not quantum gate algorithms.

Witten proves Morse inequalities using the supersymmetric Hamiltonian and deformed de Rham complex [DOI 10.4310/jdg/1214437492](https://doi.org/10.4310/jdg/1214437492).

The Landau–Ginzburg chiral-ring literature identifies the chiral ring with a Jacobian quotient in the isolated-singularity setting [DOI 10.1016/0550-3213(89)90474-4](https://doi.org/10.1016/0550-3213(89)90474-4).

Neither source states a circuit complexity for computing a Milnor number, Euler characteristic, or Hodge number.

Thus the literal quantum resource bound for the requested computational problem is: **none is given**.

A digital algorithm built now would still need:

- a finite-dimensional truncation;
- a block encoding of the supercharge or SUSY Hamiltonian;
- a spectral-gap promise;
- trace or kernel-dimension estimation;
- additive precision smaller than the normalized target;
- proof that the truncation preserves the desired algebra.

Those would be new results, not consequences of the cited SUSY literature.

### Algebraic caveat

Three objects must not be conflated.

The Landau–Ginzburg chiral ring is an algebraic supercharge cohomology.

The Witten Laplacian on a compact real manifold computes de Rham cohomology.

A finite-degree seed Hamiltonian built from \(\partial_iW\) has ground space

\[
(J_W)_N^\perp
\]

and is merely linearly isomorphic to the graded quotient \((R/J_W)_N\).

An analytic \(L^2\) ground-state theorem on \(\mathbb C^{n+1}\) needs confinement and domain hypotheses.

The slogan “the physical ground states equal the Jacobian algebra” is therefore model-dependent.

### Best classical baseline

For an isolated affine singularity, compute

\[
\mu(W)=
\dim_\mathbb C
\mathbb C[z]/(\partial W)
\]

by a local Gröbner or standard-basis computation.

For a homogeneous smooth degree-\(d\) hypersurface, the partial derivatives form a regular sequence of degree \(d-1\).

The Hilbert series is therefore explicitly

\[
\operatorname{HS}_{R/J_W}(t)
=
\frac{(1-t^{d-1})^{n+1}}{(1-t)^{n+1}}.
\]

There is no computational advantage available on this family.

Griffiths identifies the primitive Hodge pieces with graded Jacobian-ring pieces [DOI 10.2307/1970746](https://doi.org/10.2307/1970746).

For singular hypersurfaces, classical Gröbner bases, local algebra, vanishing-cycle methods, and singularity packages are the baseline.

For periods rather than Hodge dimensions, Griffiths–Dwork reduction and Picard–Fuchs equations are the correct classical comparison.

Over finite fields, \(p\)-adic cohomology computes Frobenius rather than SUSY ground-state degeneracy [arXiv:math/0403233](https://arxiv.org/abs/math/0403233).

### Dequantization and hidden costs

The normalized middle Hodge signal is exponentially small in the growing-\(n\) Fermat families examined in `scouting/applications-wide-net.md`.

The observed fits are approximately \(e^{-0.25n}\) to \(e^{-0.30n}\).

Amplitude estimation of the normalized degeneracy would therefore take exponential time.

A Witten index is an alternating signed count.

It can vanish through cancellation even when there are many ground states.

It does not recover individual Betti or Hodge numbers.

Exact ground-state counting is also exposed to the same #P-hardness anchors as C-091 and the TDA literature.

Low-rank dequantization is not the main issue.

The killers are precision, gap, and the fact that smooth hypersurface Hodge numbers already have closed formulas.

### Heuristic hardware hook

A Bose–Fermi simulator could realize a supercharge or Koszul-type Laplacian.

That is related to Arm B, which is being developed separately and is not reconstructed here.

For quadratic \(W\), Gaussian modes or spinor-BEC interactions can produce small demonstrations.

For a general degree-\(d\) \(W\), the required interactions are non-Gaussian and many-body.

No analogue protocol is known that reads \(\mu(W)\) without scanning or thermodynamically inferring the degeneracy.

### Combination with the seed

Take the seed ideal

\[
I=(\partial_0W,\ldots,\partial_nW).
\]

Then D-ground-space gives the inverse system of the Jacobian ideal degree by degree.

This is a clean dictionary.

It adds neither a better gap nor a better readout.

The seed’s \(H_N\) contains only the \(\partial\partial^\dagger\) side relevant to the quotient piece.

Arm B adds the complementary homological structure through a Koszul Laplacian.

The promising role of SUSY here is organizational: it may reveal which signed traces or protected indices survive perturbations.

It is not presently a speedup route for Milnor or Hodge numbers.

### Score and killer

Score: **1/5**.

K-QP4: **For smooth hypersurfaces the Jacobian Hilbert series is closed form, while for singular inputs no quantum algorithm or resolvable normalized ground-state count is known.**

# 5. Quantum topological data analysis on real varieties

### Problem P

Input:

- \(s\) points \(x_1,\ldots,x_s\in\mathbb R^a\), each with \(b\)-bit coordinates;
- two radii \(\epsilon_1\le\epsilon_2\);
- homological degree \(k\);
- a distance or adjacency oracle for the Vietoris–Rips complexes.

Output:

- the normalized Betti number \(\beta_k/|\mathrm{Cl}_{k+1}|\);
- or a persistent Betti number between two filtration scales;
- to additive or relative error.

When the points are sampled from \(V_{\mathbb R}(I)\), this is an approximation to the topology of the real locus only under reach, noise, and sampling-density promises.

It is not a direct computation from the equations of \(I\).

The sample-to-homology step has rigorous guarantees for sufficiently dense samples of smooth positive-reach manifolds [DOI 10.1007/s00454-006-1250-7](https://doi.org/10.1007/s00454-006-1250-7).

This lives in classical-landscape §7 and §11, with the simplicial-chain analogue of §10.

### Quantum resource bound as literally stated in the source

Lloyd–Garnerone–Zanardi prepare a mixture over simplices, simulate a Dirac or combinatorial Laplacian, perform phase estimation, and estimate the frequency of zero eigenvalues [arXiv:1408.3106, DOI 10.1038/ncomms10138](https://arxiv.org/abs/1408.3106).

The original exponential-speedup summary suppresses clique-state preparation, the Laplacian gap, and normalization.

Berry et al. give a more explicit bound.

For a graph \(G\) with \(s\) vertices, \(k\)-clique set \(\mathrm{Cl}_k(G)\), Betti number \(\beta_{k-1}\), Dirac gap \(\lambda_{\min}\), relative-error budget \(r=r_1+r_2+r_3\), and failure budget \(\delta=\delta_1+\delta_2\), their Lemma 1 gives a cost approximated by

\[
\frac{\log(1/\delta_2)}{r_2}
\sqrt{\frac{|\mathrm{Cl}_k(G)|}{\beta_{k-1}}}
\left[
\frac{\pi}{2}
\sqrt{\frac{\binom sk}{|\mathrm{Cl}_k(G)|}}
(6|E|+s\log^2s)
+
\frac{s}{\lambda_{\min}}
\log\!\left(
\frac{4|\mathrm{Cl}_k(G)|}{r_3\beta_{k-1}}
\right)
(6|E|+5s)
\right].
\]

They also give a second Dicke-state implementation replacing \(\binom sk\) by \(s^k/k!\) and altering the state-preparation gate factor.

The bound assumes a classical edge database accessible coherently [arXiv:2209.13581, DOI 10.1103/PRXQuantum.5.010319](https://arxiv.org/abs/2209.13581).

Their resource examples require tens of billions of Toffoli gates.

They prove that super-quadratic speedup is possible only in the relative-error regime with growing Betti number.

### Best classical baseline

Exact persistent homology uses sparse boundary-matrix reduction, cohomology algorithms, clearing, compression, and specialized packages.

For normalized additive estimation with a promised relative Laplacian gap \(\gamma\), Apers–Gribling–Sen–Szabó give

\[
s^{O\!\left(
\gamma^{-1/2}\log(1/\varepsilon)
\right)}
\]

time for a general simplicial complex.

For clique complexes they improve this to

\[
\left(
\frac{s}{\lambda_{\max}}
\right)^{
O\!\left(
\gamma^{-1/2}\log(1/\varepsilon)
\right)}
\operatorname{poly}(s).
\]

For constant \(\gamma\) and \(k=\Omega(s)\), this matches the quantum asymptotics in important regimes [arXiv:2211.09618](https://arxiv.org/abs/2211.09618).

### Dequantization and hidden costs

Berry et al. construct a path-integral Monte Carlo dequantization.

They conclude that exponentially large chain-space dimension and exponentially large Betti number are necessary but insufficient for superpolynomial advantage.

Schmidhuber–Lloyd prove:

- exact Betti computation is #P-hard;
- deciding whether the relevant Betti number is nonzero is NP-hard;
- both hardness statements persist in clique-dense regimes;
- the optimized LGZ multiplicative runtime contains

\[
\sqrt{\binom{s}{k+1}/\beta_k}.
\]

They conclude that the original algorithm gives only a quadratic advantage in asymptotically almost all cases [arXiv:2209.14286, DOI 10.1103/PRXQuantum.4.040349](https://arxiv.org/abs/2209.14286).

The hidden costs for a real variety are:

- obtaining a sufficiently dense point cloud;
- estimating or lower-bounding the reach;
- coherent construction of all pairwise distances;
- preparing the uniform clique mixture;
- inverse Dirac gap;
- normalization by an exponentially large clique count;
- persistence across two complexes rather than one;
- distinguishing sampling holes from genuine homology;
- inability to recover exact small Betti numbers from additive normalized estimates.

There is no general polynomial mixing or sampling theorem for singular or disconnected real varieties.

### Heuristic hardware hook

None specific.

MBQC can implement the digital boundary-operator circuit.

Fermionic simulators can mimic the chain complex, but preparing the Rips-complex simplex ensemble remains combinatorial.

Linear optics does not naturally build a Vietoris–Rips clique oracle from real coordinates.

### Combination with the seed

The seed does not sample \(V_{\mathbb R}(I)\).

A coherent-state POVM on \(P_0/\operatorname{HF}\) produces a smeared complex-projective distribution, not a certified real-locus sample.

D-real-structure and C-276/C-278 exclude the proposed two-copy filter as a real-point selector.

Thus “seed first, TDA second” lacks its first state-preparation step.

If an independent real-point sampler were supplied, TDA could estimate the topology of the sampled locus, but the seed would add no known asymptotic benefit.

### Score and killer

Score: **2/5**.

K-QP5: **Clique-state preparation and the factor \(\sqrt{\binom{s}{k+1}/\beta_k}\) erase the exponential claim precisely when the real variety has only a few topological features.**

# 6. Amplitude amplification, estimation, and quantum walks on continuation paths

### Problem P

Input:

- a polynomial family \(F(x;\lambda)\);
- a start parameter \(\lambda_0\) with known roots;
- a target parameter \(\lambda_1\);
- a reversible path tracker with precision and conditioning promises;
- a predicate \(P(x)\) selecting useful target roots.

Let \(D\) be the number of start paths and \(r\) the number whose endpoints satisfy \(P\).

Output: one acceptable target root, an estimate of \(r/D\), or a sample from acceptable roots.

This lives in classical-landscape §7, §9, §11, and §13.

The robotics specialization is Arm R bet R2 in `scouting/robotics-deep-dive.md`.

### Quantum resource bound as literally stated in the source

Amplitude amplification finds a marked item using

\[
O\!\left(\sqrt{D/r}\right)
\]

coherent predicate evaluations when the starting state is uniform over \(D\) candidates.

Amplitude estimation estimates a probability to additive error \(\varepsilon\) using \(O(1/\varepsilon)\) coherent uses, quadratically improving ordinary \(O(1/\varepsilon^2)\) sampling [arXiv:quant-ph/0005055](https://arxiv.org/abs/quant-ph/0005055).

These are oracle bounds.

Applied to continuation, each oracle evaluation must reversibly:

1. initialize a start solution;
2. track it to \(\lambda_1\);
3. control precision and branch switching;
4. evaluate the real/positive/design predicate;
5. uncompute the path workspace.

Hence the quantum cost is

\[
\widetilde O\!\left(
\sqrt{D/r}\,
C_{\mathrm{track}}(\mu,L,b)
\right),
\]

where \(L\) is the number of predictor-corrector steps, \(\mu\) is path conditioning, and \(b\) is arithmetic precision.

This formula is a direct composition of amplitude amplification with a path oracle; it is not an existing end-to-end homotopy theorem.

No verified source was found giving a quantum continuation algorithm with a proved improvement in \(C_{\mathrm{track}}\).

### Best classical baseline

Polyhedral homotopy tracks the BKK number of paths.

Parameter homotopy tracks exactly the generic root count \(D\) per new parameter instance.

Monodromy solvers, under a uniform-monodromy model, use an expected number of path tracks linear in \(D\) [arXiv:1609.08722](https://arxiv.org/abs/1609.08722).

For one approximate root of a random dense system, classical continuation already has average polynomial-time algorithms [arXiv:1507.05485, DOI 10.1007/S10208-016-9319-7](https://arxiv.org/abs/1507.05485).

Therefore the plausible quantum margin is only against enumeration or filtering over many paths.

It is not against generic one-root solving.

### Root counting and real-root isolation

Estimating a normalized fraction \(r/D\) has a quadratic improvement in accuracy.

Recovering the exact count \(r\) requires additive error below \(1/(2D)\).

Amplitude estimation then needs \(O(D)\) oracle uses in the worst case.

Exact counting therefore does not inherit an exponential advantage.

Real-root isolation additionally requires certified signs, separation bounds, and isolating boxes.

A quantum sample of a real root is not such a certificate.

### Nash equilibria

Enumerating support patterns and solving each support system can be Groverized.

This gives at most a square-root reduction in the number of supports.

The predicate must still solve a real polynomial system and check simplex inequalities.

Zero-sum games have separate quantum LP algorithms, including

\[
\widetilde O(\sqrt{n+m}/\varepsilon^3)
\]

for a dense \(n\times m\) payoff matrix [arXiv:1904.03180](https://arxiv.org/abs/1904.03180).

That is not an algorithm for general algebraic Nash equilibria.

### Robotics R2

For Watt II, the robotics memo estimates a multigraded sector of size \(6^{11}\approx3.6\times10^8\).

With approximately ten useful designs, black-box amplification would require about \(6000\) projector/predicate calls.

The classical parameter-homotopy baseline is \(92{,}736\) paths.

That is only about a factor \(15\) in outer iteration count.

The quantum projection, coherent path tracking, predicate, and root readout are all much more expensive than one classical path.

The cited monodromy baseline is [arXiv:1609.08722](https://arxiv.org/abs/1609.08722), and the GPU continuation baseline reports up to \(26\times\) CPU acceleration [arXiv:2112.03444](https://arxiv.org/abs/2112.03444).

### Dequantization and hidden costs

This is a genuine black-box quadratic speedup and is not Tang-dequantized.

Its costs are instead:

- reversible numerical continuation;
- path conditioning and adaptive step sizes;
- coherent handling of singular endpoints;
- precision needed for a real predicate;
- state preparation over start solutions;
- uncomputation of a long floating-point trajectory;
- \(r=0\) versus very small \(r\);
- output tomography for continuous coordinates.

A Szegedy-type quantum walk can quadratically improve dependence on the spectral gap of a reversible classical Markov chain.

No reversible Markov chain with a proved relation to monodromy-loop exploration was found.

Monodromy solvers are adaptive algorithms on a growing discovered set, not an immediately quantizable fixed chain.

### Heuristic hardware hook

MBQC can implement the reversible arithmetic in principle.

There is no analogue optical or condensed-matter device that naturally performs certified homotopy path tracking.

The seed’s multigraded projector offers a different, more hardware-native route to candidate states, but its overlap and gap are unmeasured.

### Combination with the seed

The strongest cross-product is:

\[
\text{seed ground-space projection}
+
\text{amplitude amplification of a useful-root predicate}.
\]

C-096 supplies the correct overlap accounting.

C-150/C-154 warn that Boolean roots reproduce Grover scaling.

For geometric root families, one additionally needs:

- \(I_N=I(V)_N\) in the chosen multidegree;
- controlled coherent-state conditioning;
- an inverse-polynomial normalized Macaulay gap;
- a coherent predicate acting on a root state without first measuring it.

Until those promises are proved for one family, this is a conditional quadratic wrapper rather than a new root solver.

### Score and killer

Score: **3/5**.

K-QP6: **The square-root saving applies only to the number of candidate paths; every marked-item query still contains a full reversible, precision-controlled path track or ground-space projection.**

# 7. Boson sampling, GBS, permanents, hafnians, and Torontonians

### Problem P

The cleanest algebraic-geometric problem is the generic root count of a multihomogeneous polynomial system.

For a square system with degree matrix \(A=(a_{ij})\), the multihomogeneous Bézout number is a coefficient of

\[
\prod_{i=1}^n
\left(
\sum_j a_{ij}t_j
\right).
\]

When the variable blocks are one-dimensional, this coefficient is \(\operatorname{per}(A)\).

For generic systems this is an intersection number and bounds, or under the appropriate genericity equals, the number of isolated projective roots.

The general sparse analogue is the BKK mixed volume.

This lives in classical-landscape §7 and applications shortlist item 8.

Other proposed targets are:

- Hilbert functions of monomial ideals;
- toric volumes and Ehrhart coefficients;
- matching or independence polynomials;
- graph-derived algebraic varieties.

No verified general identity was found turning those Hilbert functions into one hafnian or Torontonian.

### Quantum resource bound as literally stated in the source

For \(k\) indistinguishable single photons passing through an \(m\)-mode passive interferometer \(U\), the probability of a collision-free output pattern \(S\) is proportional to

\[
|\operatorname{per}(U_S)|^2.
\]

Approximate sampling hardness is conditional on average-case permanent hardness and anti-concentration [arXiv:1011.3245](https://arxiv.org/abs/1011.3245).

The device outputs one sample per optical shot.

It does not output \(\operatorname{per}(U_S)\).

For a zero-mean Gaussian state, photon-number-resolving outcome probabilities contain hafnians [arXiv:1612.01199, DOI 10.1103/PhysRevLett.119.170501](https://arxiv.org/abs/1612.01199).

With threshold detectors, probabilities contain the Torontonian [arXiv:1807.01639, DOI 10.1103/PhysRevA.98.062322](https://arxiv.org/abs/1807.01639).

These are sampling statements, not polynomial-time algorithms for evaluating the matrix functions.

### Best classical baseline

Exact mixed volume is #P-hard, including restricted families derived from permanent instances [DOI 10.1137/S0097539794278384](https://doi.org/10.1137/S0097539794278384).

Exact permanent evaluation is #P-hard.

For nonnegative matrices, however, the permanent has an FPRAS [DOI 10.1145/1008731.1008738](https://doi.org/10.1145/1008731.1008738).

That directly weakens the multilinear-BKK use case because degree matrices are nonnegative.

For arbitrary complex matrices, Gurvits-type estimators give additive error

\[
\varepsilon\|A\|^n
\]

in \(O(n^2/\varepsilon^2)\) time [arXiv:1212.0025](https://arxiv.org/abs/1212.0025).

Classical polyhedral homotopy computes mixed cells and then uses the count to organize root paths.

For Hilbert functions, the baseline is standard-monomial counting or a Gröbner basis.

Squarefree monomial Hilbert-series evaluation is #P-hard through independence polynomials, but that combinatorial object is not the GBS matching distribution of the same graph; see C-092 and [arXiv:1003.3508](https://arxiv.org/abs/1003.3508).

### What does “sample” buy?

A sample is useful when the requested output itself is a distribution over matchings or occupation patterns.

A BKK count is a scalar.

Estimating a specified optical event probability \(p\) from samples requires \(O(1/(p\varepsilon^2))\) shots for relative precision.

If the permanent-carrying event is exponentially rare, optical sampling does not evaluate it efficiently.

Moreover, boson sampling exposes \(|\operatorname{per}|^2\), losing the sign or phase needed by many coefficient identities.

Postselection on one output pattern converts a sampling advantage into exponentially small acceptance.

### Dequantization and hidden costs

This primitive is not dequantized by low-rank regression.

Its vulnerability is output mismatch and noise:

- embedding a nonunitary degree matrix into a larger unitary;
- normalization factors from the dilation;
- photon loss and partial distinguishability;
- collisions;
- exponentially small selected probabilities;
- estimation of a scalar from samples;
- FPRAS availability for nonnegative permanents;
- classical approximate GBS samplers in high-loss or positive-phase-space regimes.

A claimed algebraic speedup must specify the exact output distribution and show why samples from it answer the geometric question without exponentially precise probability estimation.

### Heuristic hardware hook

Excellent.

Passive linear optics realizes ordinary boson sampling.

Squeezed-light interferometers realize GBS.

Threshold detectors realize the Torontonian distribution.

This is the cheapest direct hardware primitive in the memo.

### Combination with the seed

Passive mode transformations act on the seed as unitary changes of variables.

They do not implement the nonlinear annihilation constraints \(a(f_j)\) for general \(f_j\).

Postselection can implement some multilinear or power-ideal filters, but success probabilities multiply.

A potentially useful combination is to use a seed-inspired multigraded encoding to define a physically meaningful family of degree matrices and then use the optical device only as a proposal sampler.

A classical verification step would test sampled matchings or start systems.

That could improve a heuristic homotopy initialization distribution.

It would not compute the BKK count exactly.

### Score and killer

Score: **2/5**.

K-QP7: **The natural optical output is a permanent-, hafnian-, or Torontonian-weighted sample, whereas algebraic geometry asks for a count, coefficient, root, or certificate.**

# 8. Quantum simulation of algebraic Hamiltonians as the output

### Problem P

Input: sparse homogeneous generators \(f_1,\ldots,f_d\), their degrees \(m_j\), and unary \(N\), under D-input-model.

Build or physically realize

\[
H_N
=
\sum_j
a^\dagger(f_j)a(f_j)
\]

on the \(N\)-boson sector.

Requested outputs may be:

- ground energy;
- ground-space degeneracy \(\operatorname{HF}_{R/I}(N)\);
- a low-energy sample;
- a response to a coherent input;
- a toric-fibre mixing observable;
- a projector overlap.

This lives in classical-landscape §5, §11, §15, and §16.

### Quantum resource bound as literally stated in the source

Generic local Hamiltonian simulation is polynomial in evolution time, inverse accuracy, and local-description size [DOI 10.1126/science.273.5278.1073](https://doi.org/10.1126/science.273.5278.1073).

That theorem does not imply efficient ground-state preparation.

The seed’s digital bound is C-056:

\[
\widetilde O\!\left(
\frac{\alpha_{\mathrm{BE}}}{\Delta_N}
\log(1/\varepsilon)
\right)
\]

block-encoding uses for a spectral projector.

No source gives a polynomial-time analogue procedure for reading the degeneracy of a general algebraic \(H_N\).

A physical simulator provides time evolution or thermal/ground-state samples.

Degeneracy remains a separate statistical inference problem.

### Best classical baseline

At fixed mode number \(n+1\), \(M_N=\binom{N+n}{n}\) is polynomial in \(N\).

Permutation-invariant Hamiltonians specified in the appropriate symmetrized basis can be classically block-diagonalized and their ground states and expectation values computed in polynomial time in system size [arXiv:2211.16998, DOI 10.22331/q-2023-11-28-1189](https://arxiv.org/abs/2211.16998).

For growing \(n\), the baseline is:

- implicit sparse Lanczos or LOBPCG for extremal eigenvalues;
- stochastic trace estimation for normalized degeneracy;
- exact or modular Macaulay rank;
- toric fibre decomposition;
- representation theory when symmetry is large.

Dense diagonalization is not the baseline.

### Dequantization and hidden costs

An analogue device can measure an energy expectation efficiently if the state is already prepared.

That does not determine a ground-space dimension.

To infer degeneracy thermodynamically requires:

- temperature below the spectral gap;
- calibrated partition functions or entropy;
- control of excited-state contamination;
- enough samples to resolve \(\operatorname{HF}/M_N\).

For low-codimension varieties the normalized fraction may be polynomially visible.

For zero-dimensional or Jacobian ideals it is commonly exponential.

State preparation remains governed by the initial ground-space overlap.

Symmetry can make the device simple and simultaneously make the classical problem easy.

### Heuristic hardware hook

Strong for narrow families.

For the conic \(z_0z_1-z_2^2\), the Hamiltonian is the spin-1 spin-mixing Hamiltonian of C-024 and D-spin-mixing-hamiltonian [arXiv:cond-mat/9807258, DOI 10.1103/PhysRevLett.81.5257](https://arxiv.org/abs/cond-mat/9807258).

Frustration-free Bose–Hubbard ground energy is QMA-hard in a different, lattice-local input model [DOI 10.4086/toc.2015.v011a020](https://doi.org/10.4086/toc.2015.v011a020).

Toric binomials produce weighted fibre Laplacians and number-conserving hopping.

The point-set dual Hamiltonian from applications Observation A uses \(N\)-body product projectors.

It is exact but not locally implementable without gadgets or exponentially small postselection.

### Combination with the seed

This primitive is the seed viewed as a simulator rather than an algorithm.

The seed contributes exact algebraic semantics:

\[
\ker H_N=(I_N)^\perp,
\qquad
\dim\ker H_N=\operatorname{HF}_{R/I}(N).
\]

It also supplies coherent-state probes and the toric fibre decomposition.

What it does not supply is an efficient degeneracy meter.

A worthwhile analogue demonstration can verify a small Hilbert function by spectroscopy.

It cannot be advertised as a speedup unless the same experiment reaches growing \(n,N\), retains a resolvable normalized signal, and beats implicit sparse classical methods.

### Score and killer

Score: **2/5**.

K-QP8: **Preparing or observing a ground state is not an efficient measurement of ground-space degeneracy, and the easiest fixed-mode devices fall under polynomial classical simulation.**

# 9. Quantum annealing, QAOA, and VQE for Boolean polynomial systems

### Problem P

Input: \(m\) quadratic polynomials

\[
p_1,\ldots,p_m\in\mathbb F_2[x_1,\ldots,x_n].
\]

Output: one Boolean common zero, all zeros, or a satisfiability decision.

The usual annealing construction converts the equations into an integer-valued residual Hamiltonian and quadratizes it using ancillas and penalties.

This lives in classical-landscape §6 and §7.

It is the real Boolean locus of an ideal, but the implemented diagonal Hamiltonian is not the seed’s complex inverse-system Hamiltonian.

### Quantum resource bound as literally stated in the source

The D-Wave MQ study supplies embedding sizes and experimental results, not an asymptotic solution-time theorem.

For direct conversion of a Boolean polynomial with many XOR terms, the numerical normal form may contain \(2^n-1\) monomials.

A fully general \(n\)-body diagonal term reduced to two-body form can require

\[
2^{(n+2)/2}-2
\]

total qubits for even \(n\), or \(3\cdot2^{(n-1)/2}-2\) for odd \(n\).

The paper gives a truncated embedding with worst-case logical-qubit count

\[
\sum_{i=1}^m
\left[
\frac{n_i-2}{k-2}
\left(
2^{(k+2)/2}-2-k
\right)
+
\frac{n_i-k}{k-2}
\right]
+
\binom n2+n,
\]

where \(n_i\) is the number of monomials in equation \(i\).

On D-Wave Advantage:

- a nine-variable direct instance used 46 logical and 179 physical qubits;
- a five-variable truncated instance used 67 logical and 167 physical qubits;
- a five-variable penalty instance used 114 logical and 221 physical qubits;
- 1000 samples and iterative variable fixing were used to reach the ground state.

The estimated 74-variable Fukuoka instance would require under \(80{,}000\) logical qubits.

The 105-variable instance would require under \(300{,}000\) logical qubits.

See [arXiv:2111.13224, DOI 10.1103/PhysRevResearch.4.013096](https://arxiv.org/abs/2111.13224).

No minimum-gap or success-probability scaling is proved.

QAOA work on random \(8\)-SAT predicts a better asymptotic success-probability exponent than the tested WalkSATlm baseline for depths above 14 layers.

This is an analytical average-instance comparison, not a hardware speedup and not a Gröbner-basis computation [arXiv:2208.06909, DOI 10.1103/PRXQuantum.5.030348](https://arxiv.org/abs/2208.06909).

### What the Gröbner literature actually demonstrated

The factorization experiment combining annealing and computational algebraic geometry factored biprimes slightly above \(200{,}000\).

Gröbner bases were used classically to preprocess and reduce the QUBO.

The annealer did not compute a Gröbner basis [arXiv:1604.05796, DOI 10.1038/srep43048](https://arxiv.org/abs/1604.05796).

The Graver-basis annealing work concerns Graver bases for integer programming, not Gröbner bases [arXiv:1902.04215](https://arxiv.org/abs/1902.04215).

A separate annealing paper demonstrated a small second-order real polynomial system and iterative linear solves down to \(10^{-8}\) tolerance.

It did not prove a speedup over Newton, Krylov, or Gröbner methods [arXiv:1812.06917](https://arxiv.org/abs/1812.06917).

No verified VQE paper was found that computes a nontrivial Gröbner basis with a proved resource advantage.

### Best classical baseline

For Boolean MQ:

- BooleanSolve has expected \(O(2^{0.792n})\) under its assumptions [arXiv:1112.6263](https://arxiv.org/abs/1112.6263);
- F4/F5 and XL variants exploit the degree of regularity;
- sparse Gaussian elimination, Wiedemann, and block Lanczos exploit the finite-field matrix;
- SAT solvers exploit logical structure;
- Groverized BooleanSolve reaches \(O(2^{0.462n})\) gates under its assumptions [arXiv:1712.07211](https://arxiv.org/abs/1712.07211).

Any annealing comparison must include classical preprocessing, embedding, programming, repeated reads, and postprocessing.

### Dequantization and hidden costs

The issue is not Tang-style low-rank dequantization.

The annealing Hamiltonian is diagonal and classically evaluable.

The hidden costs are:

- ANF-to-NNF term explosion;
- quadratization ancillas;
- minor embedding;
- coefficient-range compression;
- penalty selection;
- analog noise;
- exponentially small annealing gaps;
- repeated reads;
- classical iterative fixing;
- no certificate that a missed solution does not exist.

QAOA and VQE add:

- parameter optimization;
- barren or flat landscapes;
- shot complexity;
- circuit depth;
- no theorem connecting variational energy to exact root recovery on hard instances.

### Heuristic hardware hook

Excellent for Boolean residual objectives.

An Ising annealer directly represents the quadratized diagonal Hamiltonian.

QAOA is a gate-model version of the same heuristic objective.

This is a genuine cheap attack, but it currently offers no certified speedup.

### Combination with the seed

The seed’s Boolean ideal has an exponentially large symmetric degree sector and encodes all Boolean assignments as coherent states.

The annealing model uses one computational-basis state per assignment.

Combining them does not reduce the search space.

A possible hybrid is to use classical Gröbner preprocessing to simplify the constraints, build the seed projector for the remaining low-degree system, and variationally minimize its energy.

That replaces one heuristic Hamiltonian by another without improving the worst-case gap or overlap.

The Boolean calibration rows C-088–C-097 predict Grover-limited behavior.

### Score and killer

Score: **2/5**.

K-QP9: **Existing devices solved five- to nine-variable instances with large embedding overhead, while no annealing, QAOA, or VQE scaling theorem beats BooleanSolve, SAT, or Groverized algebraic search.**

# 10. Other primitives

## 10A. Quantum PCA and tensor/secant problems

### Problem P

Input: either a dense order-\(p\) tensor stored classically, sample/query access to it, or copies of a quantum state whose amplitudes form the tensor.

Output: tensor rank, border-rank membership in a secant variety, a CP/Waring decomposition, or a multilinear HOSVD.

This lives in classical-landscape §12 and §14.

### Quantum resource bound as literally stated in the source

Density-matrix exponentiation implements \(e^{-i\rho t}\) using copies of \(\rho\), enabling phase estimation on its principal components [arXiv:1307.0401](https://arxiv.org/abs/1307.0401).

The copy cost scales with simulation time and accuracy; eigenvector recovery also depends on eigenvalue weight and separation.

Quantum HOSVD proposals report exponential improvements under coherent amplitude access [arXiv:1908.00719](https://arxiv.org/abs/1908.00719).

HOSVD is not CP rank, Waring rank, or secant membership.

### Best classical baseline

Dense tensors use ALS, nonlinear least squares, Riemannian optimization, randomized sketching, and flattenings.

Low multilinear rank is exactly the regime where sample/query dequantization is strongest.

Tensor rank and best low-rank approximation are NP-hard in general [arXiv:0911.1393, DOI 10.1145/2512329](https://arxiv.org/abs/0911.1393).

### Dequantization and hidden costs

A dense classical tensor takes time proportional to its entry count merely to load.

Replacing it by a state-preparation circuit changes the problem.

With length-square sample/query access and low rank, classical randomized SVD and the Tang–Chia frameworks remove the exponential dimension advantage.

A quantum principal component is a state, not a classical tensor decomposition.

### Heuristic hardware hook

Photonic states naturally encode symmetric tensors.

Variational product-overlap measurements can witness entanglement or distance from the Segre variety.

They do not compute tensor rank.

### Combination with the seed

The seed can evaluate known secant-defining equations on a quantum-native state through Observation B.

That is an invariant-violation witness.

It does not construct the defining ideal or solve the secant-membership optimization.

### Score and killer

Score: **1/5**.

K-QP10A: **Quantum PCA computes matrix spectra under quantum-data access; tensor rank is a nonlinear secant-variety problem with a different output.**

## 10B. Quantum Gibbs and Metropolis sampling on real varieties

### Problem P

Given real polynomials \(f_j\), inverse temperature \(\beta\), and domain \(K\), sample from

\[
\pi_\beta(x)
\propto
e^{-\beta\sum_j f_j(x)^2}
\mathbf 1_K(x).
\]

At large \(\beta\), this distribution concentrates near the real variety.

This lives in classical-landscape §11 and §15.

### Quantum resource bound as literally stated in the source

Quantum Metropolis sampling supplies a quantum implementation of Metropolis transitions for quantum Hamiltonians but gives no universal fast-mixing theorem [arXiv:0911.3635](https://arxiv.org/abs/0911.3635).

Quantum simulated annealing and partition-function algorithms provide quadratic improvements in:

- inverse Markov-chain spectral gap;
- sample accuracy.

See [arXiv:0811.0596](https://arxiv.org/abs/0811.0596) and [arXiv:2009.11270](https://arxiv.org/abs/2009.11270).

### Best classical baseline

Constrained Hamiltonian Monte Carlo, Langevin dynamics, hit-and-run, tempering, and local parameterizations are the practical baselines.

No general polynomial mixing theorem exists for multimodal, singular, or disconnected real varieties.

### Dequantization and hidden costs

The quantum advantage is at most quadratic in the classical chain parameters.

If components are separated by an energy barrier \(B\), both classical and quantum costs may remain exponential in \(\beta B\).

To resolve an \(\eta\)-tube around the variety requires \(\beta\) set by residual curvature and conditioning.

The resulting partition-function ratio or postselection weight can be exponentially small.

### Heuristic hardware hook

A real bosonic residual-energy landscape is a natural analogue sampler.

Annealers and BECs can explore small instances.

The output is heuristic unless mixing and temperature are certified.

### Combination with the seed

D-residual-spectral-hierarchy provides a bosonic operator whose coherent-state expectation is the residual sum of squares.

This gives a clean energy oracle.

It does not make its Gibbs state a classical Gibbs distribution over coherent labels.

A Husimi measurement introduces an \(N^{-1/2}\) smoothing kernel.

### Score and killer

Score: **2/5**.

K-QP10B: **Quantum walks can quadratically improve mixing-gap dependence but do not remove exponentially slow mixing between disconnected or narrow real components.**

## 10C. Lattice points, Ehrhart polynomials, and toric ideals

### Problem P

Input: a rational polytope

\[
P=\{x\in\mathbb R^d:Ax\le b\},
\]

and optionally an integer \(N\).

Output:

\[
L_P(N)=|NP\cap\mathbb Z^d|,
\]

one coefficient of the Ehrhart polynomial, or a multiplicative volume estimate.

These are toric-algebra quantities and live near classical-landscape §5 and §15.

### Quantum resource bound as literally stated in the source

For volume estimation from a membership oracle, the quantum algorithm uses

\[
\widetilde O(d^3+d^{2.5}/\varepsilon)
\]

membership queries and

\[
\widetilde O(d^5+d^{4.5}/\varepsilon)
\]

additional arithmetic operations.

The corresponding classical bounds stated in that paper are

\[
\widetilde O(d^4+d^3/\varepsilon^2)
\]

queries and

\[
\widetilde O(d^6+d^5/\varepsilon^2)
\]

arithmetic operations [arXiv:1908.03903, DOI 10.1145/3588579](https://arxiv.org/abs/1908.03903).

This is a polynomial speedup for continuous volume.

It is not an exact lattice-point or Ehrhart algorithm.

### Best classical baseline

In fixed dimension, Barvinok counts lattice points exactly in polynomial time [DOI 10.1287/moor.19.4.769](https://doi.org/10.1287/moor.19.4.769).

Barvinok–Woods compute short rational generating functions for fixed-dimensional projections and monomial algebras [arXiv:math/0211146, DOI 10.1090/S0894-0347-03-00428-4](https://arxiv.org/abs/math/0211146).

In growing dimension, exact counting is #P-hard.

Volume does not determine lattice count without strong thickness assumptions.

### Dequantization and hidden costs

The speedup is polynomial and uses a coherent membership oracle.

Turning an explicit toric ideal into that oracle may require solving a separate inequality or moment-polytope problem.

Recovering exact \(L_P(N)\) from volume requires additive precision below one lattice cell, destroying the quantum accuracy advantage.

### Heuristic hardware hook

None for exact Ehrhart computation.

A toric Bose–Hubbard fibre can sample occupation vectors satisfying linear conservation laws.

It does not count all lattice points without a partition-function estimate.

### Combination with the seed

D-toric-ideal turns each \(A\)-graded fibre into a weighted graph Laplacian.

Quantum walks could quadratically improve mixing within a fibre.

This is more natural than applying generic volume estimation.

The missing theorem is a relation between fibre mixing, a toric Hilbert coefficient, and a polynomially visible observable.

### Score and killer

Score: **2/5**.

K-QP10C: **The proven quantum result estimates continuous volume, while exact Ehrhart and Hilbert data require integer precision.**

## 10D. Discrete logarithms on Jacobians

Given a Jacobian group with efficient unique encoding and group law, Shor’s abelian hidden-subgroup method solves discrete logarithms in quantum polynomial time [DOI 10.1137/S0097539795293172](https://doi.org/10.1137/S0097539795293172).

This is a real and cryptographically important speedup.

It is out of scope because the computational task is a group-theoretic discrete logarithm, not an invariant or construction problem about the variety or ideal.

Score: **0/5**.

K-QP10D: **The variety supplies the group, but the target problem is discrete logarithm rather than algebraic geometry.**

## 10E. Shor-type period finding on polynomial maps

A polynomial map yields a Shor-type speedup only when its iterates or translates define a coherently computable periodic function that is constant and distinct on cosets.

Generic polynomial evaluation does not have that promise.

Quadratic Boolean hidden shifts can be recovered efficiently, and a general shifted Boolean function has complexity governed by its Fourier structure and minimum influence [arXiv:0911.4724](https://arxiv.org/abs/0911.4724), [arXiv:1103.3017](https://arxiv.org/abs/1103.3017).

A 2025 symbolic-simulation result also shows that some shifted-bent-function circuits are classically simulable despite their oracle interpretation [DOI 10.22331/q-2025-12-02-1926](https://doi.org/10.22331/q-2025-12-02-1926).

The existence of a polynomial self-map, orbit, or algebraic dynamical system is therefore not enough.

The period must be hidden in an efficiently evaluable group action.

Score: **2/5**.

K-QP10E: **Period finding accelerates a promised coset structure; generic polynomial maps and their varieties do not supply one.**

# Ranked table

| rank | primitive | algebraic-geometric problem | honest speedup type | score | killer |
|---:|---|---|---|---:|---|
| 1 | Kedlaya class-group order finding | exact zeta numerator of a variable-genus curve over \(\mathbb F_q\) | superpolynomial over known uniform classical algorithms in \(g,\log q\) | 3 | K-QP2: no hardware or seed combination |
| 2 | hidden nonlinear structures | learn a hidden finite-field polynomial pencil or shifted quadric family | exponential oracle-query separation | 3 | K-QP3: oracle already hides the fibres coherently |
| 3 | amplitude amplification over paths | find one acceptable root among \(D\) continuation endpoints | quadratic in candidate-path count | 3 | K-QP6: a query is a full reversible path track |
| 4 | QLSA/QSVT on Macaulay matrices | Boolean solving or degree-local quotient observables | conditional exponential dimension compression; often no surviving end-to-end gain | 2 | K-QP1: condition number and readout |
| 5 | quantum TDA | normalized persistent Betti number of a cloud sampled from \(V_{\mathbb R}\) | quadratic broadly; superpolynomial only in special high-Betti regimes | 2 | K-QP5: clique preparation, gap, and normalization |
| 6 | GBS/boson sampling | multihomogeneous Bézout count or matching-derived invariant | hard sampling, not count evaluation | 2 | K-QP7: sample is the wrong output |
| 7 | analogue algebraic Hamiltonians | Hilbert-function degeneracy and toric fibre observables | possible experimental compression, no readout theorem | 2 | K-QP8: degeneracy measurement |
| 8 | annealing/QAOA | Boolean MQ and Boolean varieties | heuristic; Grover-like at best | 2 | K-QP9: no scaling guarantee |
| 9 | quantum Gibbs/walks | Gibbs sampling near a real variety | quadratic in mixing gap and precision | 2 | K-QP10B: metastability |
| 10 | quantum volume estimation | continuous volume of a toric or moment polytope | polynomial query improvement | 2 | K-QP10C: volume is not Ehrhart count |
| 11 | Shor-type polynomial periods | hidden shift or periodic algebraic map | exponential under explicit period promise | 2 | K-QP10E: promise absent generically |
| 12 | SUSY/Landau–Ginzburg | Milnor number and Hodge pieces from a Jacobian algebra | no quantum resource theorem | 1 | K-QP4: closed-form smooth baseline or unresolved count |
| 13 | quantum PCA/HOSVD | tensor flattening spectra | input-model speedup for quantum data | 1 | K-QP10A: HOSVD is not secant membership |
| 14 | Jacobian discrete log | discrete log in \(J_C(\mathbb F_q)\) | exponential | 0 | K-QP10D: out-of-scope output |

# Combinations

## 1. Toric fibre Hamiltonians plus quantum-walk mixing

D-toric-ideal turns each degree-\(N\) fibre \(\{k:Ak=u\}\) into a weighted graph Laplacian, while quantum-walk algorithms offer a quadratic dependence on a reversible chain’s spectral gap.

This is the cleanest combination in which the graph being quantized is produced canonically by the ideal rather than imposed afterward.

A one-week probe should choose three growing families of integer matrices \(A_n\): a bounded-treewidth family, a contingency-table family, and a family with known slow Markov-basis mixing.

For every fibre with at most \(10^6\) states, compute the exact seed block, its normalized gap, the Metropolis-chain gap, conductance estimates, and the variance of a normalized Hilbert or Toeplitz observable.

The probe succeeds only if it identifies an observable estimable in \(\operatorname{poly}(n)\) quantum time while the best classical chain requires superpolynomial mixing.

The likely negative outcome is that stoquasticity, fibre decomposition, or classical rapidly mixing chains remove the advantage.

## 2. Multigraded seed projection plus amplitude amplification for kinematic synthesis

Arm R bet R2 is the only classical application in the current campaign with \(D\sim10^5\)–\(10^6\) roots and a naturally expensive predicate.

A one-week probe should not begin with the full Watt or Stephenson system.

It should use the smallest available multihomogeneous four-bar subsystem for which equations and a root list are already reproducible.

Compute:

- the multigraded sector dimension;
- \(\dim\ker H\) versus the reduced root count;
- the smallest nonzero singular value of the Macaulay map;
- coherent-state Gram conditioning;
- the cost of a reversible interval predicate for link lengths;
- the number of classical path steps for the same accepted roots.

The candidate survives only if the kernel defect is below \(10\%\), \(\Delta/\alpha_{\mathrm{BE}}\ge10^{-3}\), and the estimated reversible predicate plus projection cost is below one classical path track by at least two orders of magnitude.

Those thresholds are intentionally severe because the nominal outer-loop advantage is only about \(15\times\) for Watt II.

## 3. GBS proposal sampling plus permanent-form BKK start systems

For a multihomogeneous degree matrix \(A\ge0\), the Bézout count is a permanent-type coefficient and individual permanent terms correspond to assignments of equations to variable blocks.

A one-week probe should embed normalized versions of \(A\) for ten benchmark systems into passive interferometers of at most 24 modes.

It should compare four quantities:

- exact permanent by Ryser;
- JSV-style multiplicative estimates for \(A\ge0\);
- optical output probabilities including the unitary-dilation normalization;
- the variance of using optical samples to propose high-weight start-system assignments.

The target is not exact counting.

It is a lower-variance proposal distribution for constructing multihomogeneous start systems or ordering continuation blocks.

The route survives only if the optical estimator needs fewer than \(10^{-2}\) times the samples of the best classical importance sampler after loss and postselection are included.

# Proposed claim rows

### C-NEW-QP-ID-KEDLAYA

- statement: The assertion “Kedlaya’s quantum curve-zeta algorithm is arXiv:quant-ph/0608151” is false; for every bibliographic use in this campaign the correct identifiers are arXiv:math/0411623 and DOI 10.1007/s00037-006-0204-7, while quant-ph/0608151 denotes an unrelated bosonic-entanglement paper.
- status: REFUTED
- depends-on: D-curve-zeta-problem
- where-proved: bibliographic verification in this memo
- where-tested: arXiv title and author records

### C-NEW-QP-MACAULAY-HHL-UNIFORM

- statement: The claim that the original Chen–Gao HHL-on-Macaulay algorithm runs in \(\operatorname{poly}(n)\) time for every uniquely solvable \(n\)-variable Boolean system is false: for every such instance with solution Hamming weight \(h\), the relevant truncated QLS condition number is \(\Omega(\sqrt{\binom nh})\), and the original construction is no faster than fixed-weight Grover search in the regimes specified by Ding et al.
- status: REFUTED
- depends-on: D-boolean-macaulay-solve, D-hardness-anchors, C-097
- where-proved: arXiv:2111.00405
- where-tested: none

### C-NEW-QP-MACAULAY-CONDITION-EQUALITY

- statement: The claim that for every homogeneous tuple \((f_j)\) and degree \(N\), the Chen–Gao truncated QLS condition number equals \(\alpha_{\mathrm{BE}}/\Delta_N\) for the seed Hamiltonian is false because the two constructions have different domains, right-hand sides, nullspaces, and normalizations.
- status: REFUTED
- depends-on: D-boolean-macaulay-solve, D-macaulay-map, D-normalised-gap, C-052, C-055, C-097
- where-proved: comparison in this memo
- where-tested: dimension and kernel comparison

### C-NEW-QP-ZETA-CURVE

- statement: For every smooth projective geometrically irreducible genus-\(g\) curve \(C/\mathbb F_q\) supplied by a plane model of degree \(\operatorname{poly}(g)\), explicit desingularization data, and polynomial-time unique-encoding Jacobian arithmetic, there is a bounded-error quantum algorithm computing the exact numerator \(P_C(T)\) of \(Z(C,T)\) in \(\operatorname{poly}(g,\log q)\) time.
- status: CONJECTURE
- depends-on: D-curve-zeta-problem
- where-proved: imported theorem, arXiv:math/0411623
- where-tested: none
- note: L1 requires an independent critic before promotion despite the published source

### C-NEW-QP-ZETA-HYPERSURFACE

- statement: The claim that Kedlaya’s curve algorithm computes the full zeta function of every smooth projective hypersurface of variable dimension and degree in time polynomial in the input length is false; the algorithm realizes only \(H^1\) through Jacobians, and no corresponding general realization of higher cohomology is supplied.
- status: REFUTED
- depends-on: D-curve-zeta-problem, D-finite-field-analogue
- where-proved: arXiv:math/0411623 §10
- where-tested: none

### C-NEW-QP-FINITE-FIELD-SEED

- statement: For every family with \(\dim R_N=2^{\Omega(n)}\), the divided-power finite-field analogue that explicitly stores a vector in \(\mathbb F_q^{\dim R_N}\) requires \(\Omega(\dim R_N\log q)\) qubits and therefore does not inherit the seed’s \(O(n\log N)\)-qubit complex-amplitude compression.
- status: CONJECTURE
- depends-on: D-finite-field-analogue, D-input-model, C-057
- where-proved: information-capacity argument in this memo
- where-tested: none

### C-NEW-QP-HIDDEN-POLYNOMIAL

- statement: For every fixed number \(a\) of variables and fixed total degree \(t\), and for all but finitely many field sizes \(q\), the hidden polynomial function graph problem of D-hidden-polynomial-structure has a bounded-error quantum algorithm running in \(\operatorname{polylog}(q)\) time, while every classical black-box algorithm needs \(\Omega(\sqrt q)\) queries for constant success probability.
- status: CONJECTURE
- depends-on: D-hidden-polynomial-structure
- where-proved: imported theorem, arXiv:0706.1219
- where-tested: none

### C-NEW-QP-HIDDEN-EXPLICIT-TRANSFER

- statement: The claim that an efficient hidden-polynomial function graph algorithm yields an efficient algorithm for solving every explicitly supplied sparse polynomial system over \(\mathbb F_q\) is false, because constructing the required obfuscated coherent fiber oracle is not furnished by sparse coefficient access and can require solving or enumerating the fibers.
- status: REFUTED
- depends-on: D-hidden-polynomial-structure, D-input-model, D-finite-field-analogue
- where-proved: oracle-separation audit in this memo
- where-tested: none

### C-NEW-QP-SUSY-HODGE-SPEEDUP

- statement: For the family of smooth degree-\(d\) hypersurfaces in \(\mathbb P^n\), the claim that SUSY ground-state counting supplies an asymptotic speedup for Hodge numbers is false: the Jacobian ideal is a complete intersection with Hilbert series \((1-t^{d-1})^{n+1}/(1-t)^{n+1}\), while the normalized middle-Hodge signal can be exponentially small.
- status: REFUTED
- depends-on: D-jacobian-ring-susy, D-hilbert-function, D-normalised-hilbert-function, C-061, C-091
- where-proved: complete-intersection formula and applications memo F2
- where-tested: Fermat-family computations in `scouting/applications-wide-net.md`

### C-NEW-QP-WITTEN-INDEX-COUNT

- statement: The claim that the Witten index determines every individual Betti number, Hodge number, or Milnor number is false, because it is an alternating supertrace and distinct graded degeneracy vectors can have the same index.
- status: REFUTED
- depends-on: D-jacobian-ring-susy
- where-proved: elementary cancellation argument
- where-tested: none

### C-NEW-QP-TDA-REAL-VARIETY

- statement: For every compact smooth positive-reach real variety \(V_{\mathbb R}\subset\mathbb R^a\), every sufficiently dense independent point sample, and every filtration interval satisfying the standard reconstruction hypotheses, quantum TDA estimates the corresponding normalized persistent Betti number with the Berry et al. resource bound, including clique-preparation and Dirac-gap factors.
- status: CONJECTURE
- depends-on: D-vr-betti-estimation, D-real-locus-and-real-radical
- where-proved: composition of DOI 10.1007/s00454-006-1250-7 with arXiv:2209.13581
- where-tested: none

### C-NEW-QP-TDA-GENERIC-EXPONENTIAL

- statement: The claim that LGZ gives an exponential end-to-end speedup for multiplicatively estimating Betti numbers on asymptotically almost all clique-complex inputs is false; its runtime contains \(\sqrt{\binom{s}{k+1}/\beta_k}\), which is exponential on asymptotically almost all inputs in the analyzed regime.
- status: REFUTED
- depends-on: D-vr-betti-estimation
- where-proved: arXiv:2209.14286
- where-tested: none

### C-NEW-QP-PATH-AA

- statement: For every family of \(D\) continuation paths with \(r\ge1\) marked endpoints, if one path and its predicate can be computed and uncomputed coherently in cost \(C_{\mathrm{track}}\) with total error \(O(1/\sqrt{D/r})\), amplitude amplification returns a marked endpoint using \(O(\sqrt{D/r}\,C_{\mathrm{track}})\) gates up to polylogarithmic overhead.
- status: CONJECTURE
- depends-on: D-coherent-path-oracle
- where-proved: conditional composition with amplitude amplification
- where-tested: none

### C-NEW-QP-PATH-INTERNAL-SPEEDUP

- statement: The claim that amplitude amplification by itself reduces the arithmetic cost of tracking one homotopy path is false; it reduces only the number of coherent path-oracle invocations and leaves \(C_{\mathrm{track}}\) unchanged.
- status: REFUTED
- depends-on: D-coherent-path-oracle
- where-proved: query-composition argument
- where-tested: none

### C-NEW-QP-BKK-PERMANENT

- statement: For every \(n\times n\) nonnegative degree matrix \(A\) describing a square multihomogeneous system with one-dimensional variable blocks, the multihomogeneous Bézout coefficient of \(\prod_i\sum_jA_{ij}t_j\) at \(t_1\cdots t_n\) equals \(\operatorname{per}(A)\).
- status: CONJECTURE
- depends-on: D-optical-counting-access
- where-proved: coefficient expansion
- where-tested: proposed \(n\le8\) symbolic checker

### C-NEW-QP-BOSON-COUNT

- statement: The claim that sample access to a boson-sampling distribution computes a specified BKK permanent to relative error \(\varepsilon\) using \(\operatorname{poly}(n,1/\varepsilon)\) shots for every embedded degree matrix is false; estimating an event of probability \(p\) requires \(\Omega(1/(p\varepsilon^2))\) independent shots, and the unitary embedding can make \(p\) exponentially small.
- status: REFUTED
- depends-on: D-optical-counting-access
- where-proved: Bernoulli sample-complexity bound
- where-tested: none

### C-NEW-QP-ANALOGUE-DEGENERACY

- statement: The claim that one ground-state energy measurement of \(H_N\) determines \(\operatorname{HF}_{R/I}(N)\) is false: all ground states return energy zero independently of the dimension of \(\ker H_N\).
- status: REFUTED
- depends-on: D-analogue-degeneracy-readout, D-ground-space, C-009
- where-proved: measurement-distribution identity
- where-tested: none

### C-NEW-QP-FIXED-MODE-HARDWARE

- statement: For every fixed \(n\), the family \(H_N\) has dimension \(\binom{N+n}{n}=\operatorname{poly}(N)\), so a fixed-mode analogue Hilbert-function experiment cannot yield an exponential asymptotic advantage merely by increasing \(N\).
- status: CONJECTURE
- depends-on: D-hamiltonian, D-symmetric-sector, C-057, C-099
- where-proved: binomial-dimension bound
- where-tested: none

### C-NEW-QP-ANNEALING-DEMONSTRATION

- statement: The claim that the D-Wave Boolean-MQ demonstrations establish an asymptotic quantum speedup is false: the experiments reach at most nine original variables, use iterative classical fixing, and supply neither a minimum-gap bound nor a scaling comparison with BooleanSolve, SAT, or Groverized algebraic search.
- status: REFUTED
- depends-on: D-boolean-residual-energy, D-hardness-anchors, C-097
- where-proved: resource audit of arXiv:2111.13224
- where-tested: reported device instances

### C-NEW-QP-GROEBNER-ANNEALER

- statement: The claim that the factorization experiment of arXiv:1604.05796 used a quantum annealer to compute a Gröbner basis is false; the Gröbner basis was computed classically and used to reduce the QUBO supplied to the annealer.
- status: REFUTED
- depends-on: D-boolean-residual-energy
- where-proved: method description in DOI 10.1038/srep43048
- where-tested: none

### C-NEW-QP-QPCA-SECANT

- statement: The claim that quantum PCA or HOSVD decides CP-rank-\(\le r\) or border-rank-\(\le r\) for every tensor is false, because those algorithms diagonalize matrix-valued reductions and do not solve membership in the \(r\)-th Segre or Veronese secant variety.
- status: REFUTED
- depends-on: D-tensor-secant-problem
- where-proved: output-type comparison
- where-tested: rank-two tensors with identical flattening ranks but different CP ranks

### C-NEW-QP-GIBBS-QUADRATIC

- statement: For every reversible classical Gibbs chain with spectral gap \(\delta\), efficiently implementable coherent transition oracle, and warm-start overlap bounded below by \(1/\operatorname{poly}(n)\), the corresponding quantum-walk preparation can improve the gap dependence from \(1/\delta\) to \(1/\sqrt\delta\), but makes no claim that \(\delta\) is polynomial for polynomial residuals.
- status: CONJECTURE
- depends-on: D-real-variety-gibbs
- where-proved: imported quantum-walk theorem, arXiv:0811.0596
- where-tested: none

### C-NEW-QP-VOLUME-EHRHART

- statement: The claim that a multiplicative quantum volume estimate for a rational polytope yields its exact Ehrhart value \(L_P(N)\) in polynomial time for every growing-dimensional input is false, because bodies of equal or multiplicatively close volume can have different lattice-point counts and exact recovery can require additive error below one lattice cell.
- status: REFUTED
- depends-on: D-toric-lattice-counting
- where-proved: precision and non-identifiability argument
- where-tested: translated thin-polytopes examples

# Proposed definitions

### D-boolean-macaulay-solve

For a Boolean polynomial system \(\mathcal F\subseteq\mathbb F_2[x_1,\ldots,x_n]\), a Boolean Macaulay solve is a complex linear system \(M_{\mathcal F}y=b\) constructed after adjoining Boolean field equations and, where required, lifting finite-field equations to complex equations.

Its truncated QLS condition number is the condition parameter governing preparation of a state proportional to a selected solution of \(M_{\mathcal F}y=b\).

Source: arXiv:1712.06239 and arXiv:2111.00405.

Pitfalls: this is not D-macaulay-map in Fock norms, its condition number is not D-macaulay-gap, and its output is a linear-system state rather than D-projectors.

### D-curve-zeta-problem

For a smooth projective geometrically irreducible curve \(C/\mathbb F_q\) of genus \(g\),

\[
Z(C,T)
=
\exp\!\left(
\sum_{r\ge1}
\#C(\mathbb F_{q^r})\frac{T^r}{r}
\right)
=
\frac{P_C(T)}{(1-T)(1-qT)},
\]

where \(P_C\in\mathbb Z[T]\) has degree \(2g\).

The computational problem is to output every coefficient of \(P_C\) from a polynomial-size plane model, explicit normalization/desingularization data, and finite-field arithmetic.

Source: arXiv:math/0411623, DOI 10.1007/s00037-006-0204-7.

Pitfalls: the input includes more than one polynomial equation; efficient Jacobian group operations and unique encodings are required.

### D-hidden-polynomial-structure

Fix a finite field \(\mathbb F_q\), variable count \(a\), and degree \(t\).

A hidden polynomial structure consists of an unknown \(h\in\mathbb F_q[x_1,\ldots,x_a]\) and a coherent oracle \(O\) whose level sets coincide with the fibers of \(h\), while distinct fibers receive distinct arbitrary labels.

The task is to identify \(h\) up to scalar or other equivalences invisible to the labeled partition.

Source: arXiv:0705.2784, arXiv:0706.1219, and arXiv:1107.2189.

Pitfalls: this oracle is stronger than coefficient access, value access, membership in one zero set, or classical samples from one fiber.

### D-jacobian-ring-susy

For \(W\in\mathbb C[z_0,\ldots,z_n]\),

\[
J_W=(\partial_0W,\ldots,\partial_nW),
\qquad
\operatorname{Jac}(W)=R/J_W.
\]

A Jacobian-ring SUSY model is a graded supercharge complex whose cohomology is \(\operatorname{Jac}(W)\) under isolated-critical-locus and regularity hypotheses.

Source: DOI 10.1016/0550-3213(89)90474-4.

Pitfalls: Landau–Ginzburg chiral-ring cohomology, Witten’s de Rham complex, and the finite-degree seed inverse system are related but not identical Hilbert-space models.

### D-vr-betti-estimation

For a graph \(G\) on \(s\) sampled points and clique complex \(\mathrm{Cl}(G)\), let \(\Delta_k\) be the \(k\)-th combinatorial Laplacian, \(\beta_k=\dim\ker\Delta_k\), and \(\Gamma_k\) its smallest nonzero eigenvalue.

Normalized VR Betti estimation returns \(\beta_k/|\mathrm{Cl}_{k+1}(G)|\) to stated additive or relative error, including clique-mixture preparation and spectral filtering in the cost.

Persistent estimation replaces one kernel by the image rank of the map between two filtration scales.

Source: arXiv:1408.3106 and arXiv:2209.13581.

Pitfalls: a point cloud approximates \(V_{\mathbb R}\) only with reach and sampling promises; normalized additive output need not reveal a small integer Betti number.

### D-coherent-path-oracle

For a homotopy with \(D\) indexed start solutions, a coherent path oracle is a reversible circuit

\[
|i\rangle|0\rangle
\longmapsto
|i\rangle|\widetilde x_i(1)\rangle|\mathrm{work}_i\rangle
\]

that tracks path \(i\) to the target parameter, bounds failure and branch-switching error, evaluates a marked-root predicate, and can be uncomputed.

Its cost \(C_{\mathrm{track}}(\mu,L,b)\) includes conditioning \(\mu\), predictor-corrector length \(L\), arithmetic precision \(b\), and every stored or recomputed checkpoint.

Source: proposed here from arXiv:1609.08722 and amplitude amplification.

Pitfalls: a classical adaptive tracker is not automatically reversible or coherent.

### D-optical-counting-access

Optical counting access to a matrix \(A\) means an efficiently prepared passive or Gaussian optical experiment whose specified outcome \(S\) has probability

\[
p_S=c(A,S)|\operatorname{per}(A_S)|^2,
\]

or the analogous hafnian or Torontonian expression, with the normalization \(c(A,S)\) known.

Source: arXiv:1011.3245, arXiv:1612.01199, and arXiv:1807.01639.

Pitfalls: sample access does not give signed amplitudes, relative estimation of a rare \(p_S\) costs \(\Omega(1/p_S)\) shots, and embedding a nonunitary matrix can make \(c(A,S)\) exponentially small.

### D-analogue-degeneracy-readout

For a physical realization of D-hamiltonian, an analogue degeneracy readout is a protocol estimating

\[
\dim\ker H_N
\quad\text{or}\quad
\frac{\dim\ker H_N}{\dim R_N}
\]

with specified confidence, temperature, state preparation, energy resolution, and shot count.

Source: proposed here; algebraic identity from D-ground-space.

Pitfalls: spectroscopy of one ground state, measurement of zero energy, and low-temperature occupation do not individually determine the degeneracy.

### D-boolean-residual-energy

For Boolean polynomials \(p_i\in\mathbb F_2[x_1,\ldots,x_n]\), a Boolean residual-energy Hamiltonian is a diagonal real Hamiltonian obtained by converting each Boolean function to an integer-valued numerical normal form and adding nonnegative penalties so that its zero-energy bit strings are precisely the common zeros.

Source: arXiv:2111.13224, DOI 10.1103/PhysRevResearch.4.013096.

Pitfalls: the ANF-to-integer conversion can have exponentially many terms; quadratization and minor embedding introduce ancillas and coefficient-range problems.

### D-tensor-secant-problem

For \(T\in V_1\otimes\cdots\otimes V_p\), CP rank at most \(r\) means that \(T\) is a sum of at most \(r\) simple tensors.

Border rank at most \(r\) means that \([T]\) lies in the \(r\)-th secant variety of the Segre variety; for symmetric tensors use the Veronese variety and Waring rank.

Source: arXiv:0911.1393 and arXiv:1512.04312.

Pitfalls: matrix flattening rank, Tucker rank, HOSVD rank, CP rank, and border rank are different outputs.

### D-real-variety-gibbs

For real polynomials \(f_1,\ldots,f_d\), compact domain \(K\), and \(\beta>0\),

\[
\pi_\beta(dx)
=
Z_\beta^{-1}
e^{-\beta\sum_jf_j(x)^2}
\mathbf1_K(x)\,dx.
\]

A real-variety Gibbs sampler returns a sample within stated total-variation distance of \(\pi_\beta\).

Source: proposed here; quantum-walk framework from arXiv:0811.0596.

Pitfalls: finite \(\beta\) samples a tube, not the variety; mixing can be exponentially slow across components, and a bosonic Gibbs state is not automatically this classical coherent-state distribution.

### D-toric-lattice-counting

For a rational polytope \(P\subset\mathbb R^d\),

\[
L_P(N)=|NP\cap\mathbb Z^d|
\]

is its Ehrhart counting function.

The exact task returns \(L_P(N)\) or the Ehrhart polynomial; the approximate-volume task returns \(\operatorname{vol}(P)\) multiplicatively.

Source: DOI 10.1287/moor.19.4.769 and arXiv:math/0211146.

Pitfalls: volume estimation, uniform lattice-point sampling, and exact Ehrhart evaluation are inequivalent.

# References

1. Y.-A. Chen and X.-S. Gao, “Quantum Algorithms for Boolean Equation Solving and Quantum Algebraic Attack on Cryptosystems,” [arXiv:1712.06239](https://arxiv.org/abs/1712.06239), DOI 10.1007/s11424-020-0028-6.

2. J. Ding, V. Gheorghiu, A. Gilyén, S. Hallgren, and J. Li, “Limitations of the Macaulay Matrix Approach for Using the HHL Algorithm to Solve Multivariate Polynomial Systems,” [arXiv:2111.00405](https://arxiv.org/abs/2111.00405), DOI 10.22331/q-2023-07-26-1069.

3. A. Harrow, A. Hassidim, and S. Lloyd, “Quantum Algorithm for Linear Systems of Equations,” DOI 10.1103/PhysRevLett.103.150502.

4. A. Gilyén, Y. Su, G. Low, and N. Wiebe, “Quantum Singular Value Transformation and Beyond,” [arXiv:1806.01838](https://arxiv.org/abs/1806.01838), DOI 10.1145/3313276.3316366.

5. M. Bardet, J.-C. Faugère, B. Salvy, and P.-J. Spaenlehauer, “On the Complexity of Solving Quadratic Boolean Systems,” [arXiv:1112.6263](https://arxiv.org/abs/1112.6263).

6. J.-C. Faugère et al., “Fast Quantum Algorithm for Solving Multivariate Quadratic Equations,” [arXiv:1712.07211](https://arxiv.org/abs/1712.07211).

7. D. Bernstein and B.-Y. Yang, “Asymptotically Faster Quantum Algorithms to Solve Multivariate Quadratic Equations,” DOI 10.1007/978-3-319-79063-3_23.

8. E. Tang, “A Quantum-Inspired Classical Algorithm for Recommendation Systems,” [arXiv:1807.04271](https://arxiv.org/abs/1807.04271), DOI 10.1145/3313276.3316310.

9. A. Gilyén, S. Lloyd, and E. Tang, “Quantum-Inspired Low-Rank Stochastic Regression,” [arXiv:1811.04909](https://arxiv.org/abs/1811.04909).

10. N.-H. Chia et al., “Sampling-Based Sublinear Low-Rank Matrix Arithmetic Framework,” [arXiv:1910.06151](https://arxiv.org/abs/1910.06151), DOI 10.1145/3357713.3384314.

11. S. Gharibian and F. Le Gall, “Dequantizing the Quantum Singular Value Transformation,” [arXiv:2111.09079](https://arxiv.org/abs/2111.09079).

12. K. Kedlaya, “Quantum Computation of Zeta Functions of Curves,” [arXiv:math/0411623](https://arxiv.org/abs/math/0411623), DOI 10.1007/s00037-006-0204-7.

13. A. Lauder and D. Wan, “Counting Points on Varieties over Finite Fields of Small Characteristic,” [arXiv:math/0612147](https://arxiv.org/abs/math/0612147).

14. E. Costa, D. Harvey, and K. Kedlaya, “Zeta Functions of Nondegenerate Hypersurfaces in Toric Varieties,” [arXiv:1806.00368](https://arxiv.org/abs/1806.00368).

15. D. Roy, N. Saxena, and M. Venkatesh, “Complexity of Counting Points on Curves and the Factor \(P_1(T)\) of the Zeta Function of Surfaces,” [arXiv:2511.02262](https://arxiv.org/abs/2511.02262).

16. W. van Dam, “Quantum Computing and Zeroes of Zeta Functions,” [arXiv:quant-ph/0405081](https://arxiv.org/abs/quant-ph/0405081).

17. X.-H. Wang, S.-M. Fei, and K. Wu, “Separability and Entanglement of Identical Bosonic Systems,” arXiv:quant-ph/0608151, DOI 10.1088/0305-4470/39/36/L01.

18. A. Childs, L. Schulman, and U. Vazirani, “Quantum Algorithms for Hidden Nonlinear Structures,” [arXiv:0705.2784](https://arxiv.org/abs/0705.2784), DOI 10.1109/FOCS.2007.18.

19. T. Decker, J. Draisma, and P. Wocjan, “Efficient Quantum Algorithm for Identifying Hidden Polynomials,” [arXiv:0706.1219](https://arxiv.org/abs/0706.1219).

20. T. Decker, G. Ivanyos, M. Santha, and P. Wocjan, “Hidden Symmetry Subgroup Problems,” [arXiv:1107.2189](https://arxiv.org/abs/1107.2189), DOI 10.1137/120864416.

21. G. Ivanyos and M. Santha, “On Solving Systems of Diagonal Polynomial Equations over Finite Fields,” [arXiv:1503.09016](https://arxiv.org/abs/1503.09016).

22. E. Witten, “Supersymmetry and Morse Theory,” DOI 10.4310/jdg/1214437492.

23. W. Lerche, C. Vafa, and N. Warner, “Chiral Rings in \(N=2\) Superconformal Theories,” DOI 10.1016/0550-3213(89)90474-4.

24. C. Vafa and N. Warner, “Catastrophes and the Classification of Conformal Theories,” DOI 10.1016/0370-2693(89)90473-5.

25. P. Griffiths, “On the Periods of Certain Rational Integrals II,” DOI 10.2307/1970746.

26. K. Kedlaya, “Computing Zeta Functions via \(p\)-Adic Cohomology,” [arXiv:math/0403233](https://arxiv.org/abs/math/0403233).

27. S. Lloyd, S. Garnerone, and P. Zanardi, “Quantum Algorithms for Topological and Geometric Analysis of Big Data,” [arXiv:1408.3106](https://arxiv.org/abs/1408.3106), DOI 10.1038/ncomms10138.

28. D. Berry et al., “Analyzing Prospects for Quantum Advantage in Topological Data Analysis,” [arXiv:2209.13581](https://arxiv.org/abs/2209.13581), DOI 10.1103/PRXQuantum.5.010319.

29. S. Apers, S. Gribling, S. Sen, and D. Szabó, “A (Simple) Classical Algorithm for Estimating Betti Numbers,” [arXiv:2211.09618](https://arxiv.org/abs/2211.09618).

30. A. Schmidhuber and S. Lloyd, “Complexity-Theoretic Limitations on Quantum Algorithms for Topological Data Analysis,” [arXiv:2209.14286](https://arxiv.org/abs/2209.14286), DOI 10.1103/PRXQuantum.4.040349.

31. P. Niyogi, S. Smale, and S. Weinberger, “Finding the Homology of Submanifolds with High Confidence from Random Samples,” DOI 10.1007/s00454-006-1250-7.

32. G. Brassard, P. Høyer, M. Mosca, and A. Tapp, “Quantum Amplitude Amplification and Estimation,” [arXiv:quant-ph/0005055](https://arxiv.org/abs/quant-ph/0005055).

33. T. Duff et al., “Solving Polynomial Systems via Homotopy Continuation and Monodromy,” [arXiv:1609.08722](https://arxiv.org/abs/1609.08722).

34. P. Lairez, “A Deterministic Algorithm to Compute Approximate Roots in Polynomial Average Time,” [arXiv:1507.05485](https://arxiv.org/abs/1507.05485), DOI 10.1007/S10208-016-9319-7.

35. C.-F. Chien et al., GPU homotopy continuation, [arXiv:2112.03444](https://arxiv.org/abs/2112.03444).

36. J. van Apeldoorn and A. Gilyén, “Quantum Algorithms for Zero-Sum Games,” [arXiv:1904.03180](https://arxiv.org/abs/1904.03180).

37. S. Aaronson and A. Arkhipov, “The Computational Complexity of Linear Optics,” [arXiv:1011.3245](https://arxiv.org/abs/1011.3245).

38. C. Hamilton et al., “Gaussian Boson Sampling,” [arXiv:1612.01199](https://arxiv.org/abs/1612.01199), DOI 10.1103/PhysRevLett.119.170501.

39. N. Quesada, J. Arrazola, and N. Killoran, “Gaussian Boson Sampling Using Threshold Detectors,” [arXiv:1807.01639](https://arxiv.org/abs/1807.01639), DOI 10.1103/PhysRevA.98.062322.

40. P. Gritzmann and V. Klee, “On the Complexity of Computing Mixed Volumes,” DOI 10.1137/S0097539794278384.

41. M. Jerrum, A. Sinclair, and E. Vigoda, “A Polynomial-Time Approximation Algorithm for the Permanent of a Matrix with Nonnegative Entries,” DOI 10.1145/1008731.1008738.

42. S. Aaronson and T. Hance, “Generalizing and Derandomizing Gurvits’s Approximation Algorithm for the Permanent,” [arXiv:1212.0025](https://arxiv.org/abs/1212.0025).

43. A. Dickenstein and E. Tobis, “Independent Sets from an Algebraic Perspective,” [arXiv:1003.3508](https://arxiv.org/abs/1003.3508), DOI 10.1142/S0218196711006819.

44. S. Lloyd, “Universal Quantum Simulators,” DOI 10.1126/science.273.5278.1073.

45. E. Anschuetz, A. Bauer, B. Kiani, and S. Lloyd, “Efficient Classical Algorithms for Simulating Symmetric Quantum Systems,” [arXiv:2211.16998](https://arxiv.org/abs/2211.16998), DOI 10.22331/q-2023-11-28-1189.

46. C. Law, H. Pu, and N. Bigelow, “Quantum Spins Mixing in Spinor Bose–Einstein Condensates,” [arXiv:cond-mat/9807258](https://arxiv.org/abs/cond-mat/9807258), DOI 10.1103/PhysRevLett.81.5257.

47. A. Childs, D. Gosset, and Z. Webb, “The Bose–Hubbard Model is QMA-Complete,” DOI 10.4086/toc.2015.v011a020.

48. S. Ramos-Calderer et al., “Solving Systems of Boolean Multivariate Equations with Quantum Annealing,” [arXiv:2111.13224](https://arxiv.org/abs/2111.13224), DOI 10.1103/PhysRevResearch.4.013096.

49. R. Dridi and H. Alghassi, “Prime Factorization Using Quantum Annealing and Computational Algebraic Geometry,” [arXiv:1604.05796](https://arxiv.org/abs/1604.05796), DOI 10.1038/srep43048.

50. H. Alghassi, R. Dridi, and S. Tayur, “Graver Bases via Quantum Annealing,” [arXiv:1902.04215](https://arxiv.org/abs/1902.04215).

51. C. Chang et al., “Quantum Annealing for Systems of Polynomial Equations,” [arXiv:1812.06917](https://arxiv.org/abs/1812.06917).

52. S. Boulebnane and A. Montanaro, “Solving Boolean Satisfiability Problems with QAOA,” [arXiv:2208.06909](https://arxiv.org/abs/2208.06909), DOI 10.1103/PRXQuantum.5.030348.

53. S. Lloyd, M. Mohseni, and P. Rebentrost, “Quantum Principal Component Analysis,” [arXiv:1307.0401](https://arxiv.org/abs/1307.0401).

54. L. Gu et al., “Quantum Higher Order Singular Value Decomposition,” [arXiv:1908.00719](https://arxiv.org/abs/1908.00719).

55. C. Hillar and L.-H. Lim, “Most Tensor Problems Are NP-Hard,” [arXiv:0911.1393](https://arxiv.org/abs/0911.1393), DOI 10.1145/2512329.

56. A. Bernardi et al., “Tensor Decomposition and Homotopy Continuation,” [arXiv:1512.04312](https://arxiv.org/abs/1512.04312), DOI 10.1016/j.difgeo.2017.07.009.

57. K. Temme et al., “Quantum Metropolis Sampling,” [arXiv:0911.3635](https://arxiv.org/abs/0911.3635).

58. P. Wocjan et al., “Quantum Speed-Up for Approximating Partition Functions,” [arXiv:0811.0596](https://arxiv.org/abs/0811.0596).

59. S. Arunachalam et al., “Simpler Classical and Faster Quantum Algorithms for Gibbs Partition Functions,” [arXiv:2009.11270](https://arxiv.org/abs/2009.11270).

60. S. Chakrabarti et al., “Quantum Algorithm for Estimating Volumes of Convex Bodies,” [arXiv:1908.03903](https://arxiv.org/abs/1908.03903), DOI 10.1145/3588579.

61. A. Barvinok, “A Polynomial Time Algorithm for Counting Integral Points in Polyhedra When the Dimension Is Fixed,” DOI 10.1287/moor.19.4.769.

62. A. Barvinok and K. Woods, “Short Rational Generating Functions for Lattice Point Problems,” [arXiv:math/0211146](https://arxiv.org/abs/math/0211146), DOI 10.1090/S0894-0347-03-00428-4.

63. P. Shor, “Polynomial-Time Algorithms for Prime Factorization and Discrete Logarithms,” DOI 10.1137/S0097539795293172.

64. M. Roetteler, “Quantum Algorithms to Solve the Hidden Shift Problem for Quadratics,” [arXiv:0911.4724](https://arxiv.org/abs/0911.4724).

65. D. Gavinsky, M. Roetteler, and J. Roland, “Quantum Algorithm for the Boolean Hidden Shift Problem,” [arXiv:1103.3017](https://arxiv.org/abs/1103.3017).

66. “Polynomial-Time Classical Simulation of Hidden Shift Circuits via Confluent Rewriting of Symbolic Sums,” DOI 10.22331/q-2025-12-02-1926.

# Questions for TJO

1. Should Kedlaya’s curve-zeta algorithm be treated as the benchmark example of what a genuine algebraic-geometric quantum speedup looks like, even though it cannot itself be a campaign novelty?

2. Does the absence of a cheap hardware hook automatically cap an otherwise rigorous route at score 3, or may a later hardware translation satisfy PRD §2 independently?

3. Should finite-field work be restricted to compact geometric groups and cohomological realizations, closing the divided-power Fock route under D-finite-field-analogue?

4. Does an oracle problem count as a north-star hit when the hidden object is a family of varieties but the oracle is strictly stronger than explicit equations?

5. Should a one-week toric-fibre quantum-walk probe be opened as a new arm, given that it is the only untried combination with both a canonical ideal-derived graph and a Bose–Hubbard hook?

6. Should the GBS–BKK probe optimize a proposal distribution for homotopy start systems rather than attempt permanent evaluation?

7. For Arm R2, is a conditional \(O(\sqrt D)\) reduction in path count worth pursuing when present constants suggest only a \(15\times\) outer-loop margin for Watt II?

8. Should SUSY/Landau–Ginzburg be retained only as a dictionary supporting Arm B, with the smooth-hypersurface Hodge-number computation formally closed?

9. Should the annealing literature be classified as hardware evidence only, with an explicit campaign rule that classical Gröbner preprocessing cannot be credited as quantum Gröbner computation?

10. Is normalized persistent homology of a sampled real variety an acceptable algebraic-geometry problem, or must the input remain the defining equations rather than an externally supplied point cloud?

11. Should the 2025 \(P_1(T)\) surface result, arXiv:2511.02262, receive a dedicated verification lane before it is used as the current point-counting baseline?

12. Should C-097 be strengthened into a campaign-wide rule that no Macaulay QLSA comparison is accepted until the exact matrix, right-hand side, condition number, state-preparation oracle, and readout observable are written side by side?