# Classical landscape memo

## Purpose and decision rule

This memo defines the classical baselines against which candidate quantum speedups must be compared.

A valid speedup claim must hold for the same:

- input encoding;
- coefficient field and precision model;
- output object;
- error guarantee;
- conditioning promise;
- truncation degree;
- root distribution, if sampling is requested.

Exact membership is not the same task as additive distance estimation.

Exact Hilbert function is not the same task as estimating a normalized Hilbert function.

Producing all roots is not the same task as preparing a state supported on roots.

Computing a Gröbner basis is not the same task as implementing an implicit projector onto an ideal component.

Arithmetic-operation bounds over a field are not bit-complexity bounds over \(\mathbb Q\).

The most credible quantum targets below are therefore compact scalar observables, samples, or implicit state representations whose classical competitors must process an exponentially large Macaulay space.

Claims requiring an explicit exponentially long output cannot yield an end-to-end exponential speedup.

## 1. Common input and cost model

Let

\[
R=K[x_1,\ldots,x_n],
\]

where \(K=\mathbb Q\), a finite field \(\mathbb F_q\), or \(\mathbb C\) with rational real and imaginary parts.

For projective problems, the same notation describes \(n\) homogeneous coordinates and a subvariety of \(\mathbb P^{n-1}\).

The seed instead writes \(z_0,\ldots,z_n\); its formulas are recovered by replacing this memo's \(n\) with \(n+1\).

The input ideal is

\[
I=(f_1,\ldots,f_s),\qquad d_i=\deg f_i,\qquad d=\max_i d_i.
\]

Let \(t_i\) be the number of explicitly stored monomials of \(f_i\), and let \(t=\sum_i t_i\).

Let \(\tau\) bound coefficient bit length.

A sparse explicit encoding has bit length

\[
L=O\!\left(\sum_i t_i(n\log(d+1)+\tau)\right).
\]

Dense degree-\(d\) encoding has \(\binom{n+d}{d}\) coefficient slots per polynomial.

Straight-line-program and black-box encodings are smaller but give different algorithms and must be declared separately.

For homogeneous degree \(N\),

\[
M_N=\dim_K R_N=\binom{n+N-1}{N}.
\]

The degree-\(N\) Macaulay map is

\[
\Phi_N:\bigoplus_{i=1}^sR_{N-d_i}\longrightarrow R_N,
\qquad
(h_i)\longmapsto\sum_i f_i h_i.
\]

Its column-space dimension is bounded by

\[
C_N=\sum_{i=1}^s\binom{n+N-d_i-1}{N-d_i}.
\]

In a sparse monomial representation,

\[
\operatorname{nnz}(\Phi_N)
   \leq \sum_i t_i\binom{n+N-d_i-1}{N-d_i}.
\]

The Hamiltonian considered in the seed is

\[
H_N=\Phi_N\Phi_N^\dagger.
\]

With the Fock inner product, the elementary kernel identity is

\[
\ker H_N=(I_N)^\perp,
\qquad
\dim\ker H_N=\operatorname{HF}_{R/I}(N).
\]

The same space is the degree-\(N\) Macaulay inverse system.

Define

\[
\Delta_N=\lambda_{\min}^{\neq0}(H_N)
        =\sigma_{\min}^{\neq0}(\Phi_N)^2.
\]

A sparse-access block encoding has some normalization \(\alpha_N\geq\|H_N\|\).

The relevant spectral parameter is

\[
\gamma_N=\frac{\Delta_N}{\alpha_N},
\]

not the unnormalized gap \(\Delta_N\).

A QSVT approximation to the kernel projector has query complexity

\[
\widetilde O\!\left(\gamma_N^{-1}\log(1/\epsilon)\right).
\]

This excludes row-oracle construction, reversible arithmetic, preparation of the input state, overlap amplification, and readout.

The occupation-number register needs \(O(n\log(N+1))\) qubits.

That compact register does not imply running time polynomial in \(\log N\): entries and normalization generally grow as \(N^{O(d)}\).

A classical sparse matrix-vector multiplication by \(\Phi_N\), \(\Phi_N^\dagger\), or \(H_N\) costs \(O(\operatorname{nnz})\) arithmetic operations if the matrix is materialized.

An implicit implementation can cost \(O(t\,M_N)\), or less when convolution, symmetry, or monomial structure is available.

Dense rank computation for an \(M_N\times C_N\) matrix costs at most

\[
O\!\left(M_NC_N\min(M_N,C_N)^{\omega-2}\right)
\]

field operations, where \(2\leq\omega<2.373\).

Dense storage is \(O(M_NC_N)\).

Black-box Wiedemann or block-Wiedemann methods reduce storage to a few vectors and sparse matrix data, but may require a number of matrix-vector products proportional to the relevant dimension.

All proposed quantum trace or rank estimates must also be compared with stochastic Lanczos quadrature, randomized numerical-rank estimation, Hutchinson estimators, and Hutch++ [R54, R55].

## 2. Practical-size convention

There is no meaningful universal statement such as “software X solves \(n=20\).”

A sparse structured system in hundreds of variables may be easier than eight dense, badly conditioned equations.

The useful size parameters are:

- Macaulay degree or solving degree;
- largest Macaulay row and column count;
- nonzero count;
- quotient dimension \(D\);
- Bézout or mixed-volume path count;
- coefficient height;
- numerical condition and root separation.

The strongest reproducible exact benchmark used here is from `msolve`.

It solved Katsura-14, with \(8192\) complex solutions, over \(\mathbb Q\) in about 15 days on one 2 GHz Xeon core; the resulting rational parametrization had bit size about \(2^{32.37}\) [R11].

In the same paper, Katsura-11, of degree \(1024\), took hundreds of seconds exactly, while the older tested Singular version took much longer on smaller instances [R11].

A numerical 2018 benchmark found that HomotopyContinuation.jl tracked all \(2048\) paths of Katsura-11 in about 9 seconds and all \(924\) cyclic-7 paths in about 8 seconds on a laptop [R19].

These are comparison anchors, not current hardware limits.

For exact positive-dimensional ideals, syzygies, radicals, and elimination orders, no similarly portable “typical maximum” exists.

The largest intermediate Macaulay matrix is a more honest predictor than \(n\) alone.

For example,

\[
\binom{19}{9}=92\,378
\]

degree-10 monomials in ten variables already make a dense square matrix require about 68 GB at eight bytes per entry.

For twenty variables and degree ten,

\[
\binom{29}{10}=20\,030\,010,
\]

so only sparse or implicit methods are possible.

## 3. Ideal membership

### Problem statements

Exact ideal membership asks whether a given \(g\in K[x_1,\ldots,x_n]\), of degree \(e\), lies in \(I\).

The output is one bit, optionally accompanied by a certificate

\[
g=\sum_i h_i f_i.
\]

Homogeneous degree-local membership assumes \(g\in R_N\) and asks whether \(g\in I_N\).

Approximate degree-local membership fixes an inner product and promises either

\[
g\in I_N
\]

or

\[
\operatorname{dist}(g,I_N)\geq\epsilon\|g\|.
\]

Estimating

\[
\delta_I(g)^2
 =\frac{\|(I-P_{I_N})g\|^2}{\|g\|^2}
 =\frac{\langle g|P_{\ker H_N}|g\rangle}{\|g\|^2}
\]

is a different numerical problem.

### Best classical algorithms

Given a Gröbner basis \(G\), exact membership is decided by reducing \(g\) to its unique normal form.

The expensive step is normally computing \(G\).

Buchberger, F4, F5, and signature-based algorithms are the standard general methods.

Macaulay2 and Singular provide robust general ideal and module operations.

FGb and `msolve` provide high-performance F4-style linear algebra for suitable fields and systems [R08, R11, R64].

At fixed homogeneous degree, membership is simply column-space membership for \(\Phi_N\).

Exact Gaussian elimination gives the rectangular rank bound above.

Sparse Wiedemann methods, modular arithmetic, and Chinese remaindering are preferable when coefficients and sparsity permit.

For approximate membership over \(\mathbb C\), sparse QR, LSQR, LSMR, randomized range finding, or a polynomial filter for \(H_N\) are the direct classical competitors.

A Krylov method returns the residual distance without producing a Gröbner basis.

This is the correct baseline for the seed's distance observable.

### Worst-case hardness and degree growth

General ideal membership over \(\mathbb Q\) is EXPSPACE-complete [R01].

Mayr-Meyer ideals force doubly exponential intermediate degree and space phenomena [R02].

NP-hardness persists in restricted presentations, including examples with at most four variables when exponents are succinctly encoded [R03].

Dubé's general Gröbner-degree bound is

\[
2\left(\frac{d^2}{2}+d\right)^{2^{n-1}},
\]

and doubly exponential behavior is unavoidable in the worst case [R04].

Dimension-dependent refinements still give double-exponential dependence on the dimension of the ideal [R05].

These bounds concern unrestricted exact membership.

They do not imply that fixed-\(N\) numerical distance estimation is EXPSPACE-hard.

### Seed structure and quantum assessment

The seed exposes degree-local membership as projection against \(\ker H_N\).

For a sparse normalized \(|g\rangle\), amplitude estimation can estimate \(\delta_I(g)^2\).

The schematic cost is

\[
\widetilde O\!\left(
 T_{\rm oracle}\,
 \gamma_N^{-1}\,
 \epsilon^{-1}
\right),
\]

plus state preparation.

This could beat a classical \(O(M_N)\)-scale Krylov computation in time and space when:

- \(N=\operatorname{poly}(n)\);
- \(t=\operatorname{poly}(n)\);
- sparse row access is genuinely reversible in \(\operatorname{poly}(n,\log N,\tau)\);
- \(\gamma_N^{-1}=\operatorname{poly}(n,N)\);
- \(|g\rangle\) is sparse or otherwise efficiently preparable;
- only the scalar distance is required.

This is the strongest direct candidate in the seed.

It does not yield a faster exact membership algorithm.

If the promise gap is below coefficient-rounding error, numerical projection cannot distinguish exact zero.

If \(g\) is supplied as a dense coefficient list, loading it already costs \(\Omega(M_N)\).

Tang-style dequantization does not immediately apply because \(H_N\) can be sparse and high rank.

It becomes relevant if the projector or data have low stable rank and length-square sample/query access is granted [R49–R51].

The Boolean Macaulay analysis of Ding et al. is a direct warning: condition numbers can erase the claimed HHL advantage, leaving Grover search faster [R52].

### Cheapest hardware attack

For quadratic generators, \(H_N\) is quartic in creation and annihilation operators and resembles spin-mixing or Bose-Hubbard interactions.

The conic \(x_1x_2-x_3^2\) is the clearest spinor-BEC test case [R59].

Passive linear optics alone implements quadratic number-preserving mode transformations, not generic quartic \(H_N\).

KLM-style postselection or photonic MBQC can implement the needed non-Gaussian operation, but success and fault-tolerance overhead must be counted [R57].

Boson sampling has no generic advantage here: its native quantities are permanents, not Macaulay column-space distances.

## 4. Radical membership and Nullstellensatz

### Problem statements

Radical membership asks whether

\[
g\in\sqrt I,
\]

equivalently whether \(g\) vanishes on every point of \(V(I)\).

Hilbert-Nullstellensatz feasibility asks whether

\[
V_{\mathbb C}(f_1,\ldots,f_s)\neq\varnothing.
\]

The infeasibility certificate problem asks for \(h_i\) satisfying

\[
1=\sum_i h_i f_i.
\]

Input size must include \(n,s,d,t,\tau\), and output size must include the degrees and coefficient heights of the \(h_i\).

### Best classical algorithms

Rabinowitsch's trick gives

\[
g\in\sqrt I
\iff
1\in I+(1-y g)
\subset K[x_1,\ldots,x_n,y].
\]

Thus radical membership reduces to ordinary ideal membership in one more variable.

General algorithms use Gröbner bases, saturation, elimination, primary decomposition, or triangular decompositions.

Singular and Macaulay2 implement radical, saturation, associated-prime, and primary-decomposition workflows.

For zero-dimensional ideals, one can construct quotient multiplication matrices and remove nilpotent structure by square-free factorization or compute the radical during FGLM conversion.

`msolve` computes a lexicographic representation of the radical in its generic zero-dimensional solving pipeline [R11].

### Complexity and certificates

Complex feasibility with integer coefficients is NP-hard.

It is unconditionally in PSPACE.

Under the generalized Riemann hypothesis it lies in \(\mathrm{AM}\), more precisely in \(\mathrm{RP}^{\mathrm{NP}}\) in Koiran's formulation [R07].

Therefore emptiness is coNP-hard and is in coAM under the same hypothesis.

Setting \(g=1\) shows that radical membership is coNP-hard.

Kollár's effective Nullstellensatz gives certificate degrees bounded singly exponentially in \(n\); a safe uniform scale for degree-\(d\) inputs is \(d^{O(n)}\), with sharp product-of-degrees versions [R06].

The resulting Macaulay matrix can therefore have

\[
\binom{n+d^{\Theta(n)}}{n}
\]

columns.

Its succinct occupation encoding does not make the corresponding QSVT runtime polynomial, because normalization and arithmetic depend polynomially on the exponentially large degree.

### Seed structure and quantum assessment

The Hamiltonian kernel represents \(I_N^\perp\), not \(\sqrt I_N^\perp\).

Nilpotent scheme structure produces additional, generally entangled, inverse-system vectors.

Coherent product states correspond only to geometric points.

The coherent-state expectation

\[
\langle p^{\otimes N}|H_N|p^{\otimes N}\rangle
=
\sum_i\frac{N!}{(N-d_i)!}|f_i(\bar p)|^2
\]

does not give a quantum speedup for testing a supplied point.

The right side is classically evaluable in \(O(t)\) arithmetic operations.

A radical-membership algorithm would have to prove that \(g\) vanishes on all coherent ground states, while distinguishing them from nilpotent inverse-system states.

No efficient operation supplied by the seed performs that separation.

General Nullstellensatz feasibility also reaches truncation degrees \(d^{\Theta(n)}\), making the seed construction exponentially costly in time.

A quantum advantage remains conceivable for a promise version with:

- polynomial certificate degree;
- inverse-polynomial normalized gap;
- an efficiently prepared witness distribution;
- additive rather than exact output.

No such general promise class is currently established.

### Cheapest hardware attack

A variational coherent-state search minimizes \(\sum_i|f_i(p)|^2\) directly.

For quadratics this maps naturally to spinor condensates or coupled Bose-Hubbard modes.

It is a heuristic nonconvex optimizer, not a Nullstellensatz certificate algorithm.

MBQC is the most flexible route for an actual decision circuit.

Linear optics with postselection can test small certificate matrices, but an exponentially small postselection probability would merely re-express the classical hardness.

## 5. Hilbert function, Hilbert polynomial, dimension, and degree

### Problem statements

For a homogeneous ideal \(I\), compute

\[
\operatorname{HF}_{R/I}(N)=\dim_K(R/I)_N.
\]

The exact Hilbert-series problem asks for

\[
\operatorname{HS}_{R/I}(z)
 =\sum_{N\geq0}\operatorname{HF}_{R/I}(N)z^N.
\]

The eventual polynomial \(P_I(N)\) determines projective dimension and degree:

\[
\deg P_I=\dim\operatorname{Proj}(R/I),
\]

and the leading coefficient is \(\deg(V)/(\dim V)!\).

The normalized approximate problem asks for

\[
h_N=\frac{\operatorname{HF}_{R/I}(N)}{M_N}
\]

to additive error \(\epsilon\).

These outputs have radically different complexity.

### Best classical algorithms

At a fixed \(N\),

\[
\operatorname{HF}_{R/I}(N)=M_N-\operatorname{rank}\Phi_N.
\]

This can be computed by exact dense or sparse rank.

For many values of \(N\), standard practice computes a Gröbner basis, replaces \(I\) by its initial monomial ideal, and counts standard monomials.

Macaulay2 and Singular compute Hilbert functions, series, polynomials, dimension, multiplicity, and degree from this data.

For monomial ideals, combinatorial algorithms, Stanley decompositions, lcm structures, and rational generating functions can avoid general Gröbner work.

For a complete intersection of degrees \(d_1,\ldots,d_s\), the Hilbert series is known explicitly:

\[
\operatorname{HS}_{R/I}(z)
=
\frac{\prod_i(1-z^{d_i})}{(1-z)^n}.
\]

A quantum algorithm has no baseline advantage on such inputs.

For generic overdetermined forms, the analogous truncation predicted by Fröberg remains conjectural in full generality [R14].

### Complexity and hardness

Exact evaluation of Hilbert series is #P-hard even for initial ideals associated with radical zero-dimensional complete intersections [R15].

Computing the general Hilbert polynomial is polynomial-space hard [R16].

Boolean equations \(x_i^2-x_i=0\) and clause polynomials give a direct parsimonious route from #SAT to eventual quotient dimension.

Thus exact stable Hilbert function, exact degree of a zero-dimensional radical ideal, and exact root count can encode #P-hard counting.

The output itself can require \(\Theta(n)\) bits even when the root count is \(2^n\), so this is not merely an output-length obstruction.

### Seed structure and quantum assessment

The kernel degeneracy is exactly the Hilbert function.

A DQC1-style trace estimate of a QSVT kernel projector targets

\[
\frac{\operatorname{Tr}P_{\ker H_N}}{M_N}=h_N.
\]

The schematic quantum sample cost is \(O(\epsilon^{-2})\), or \(O(\epsilon^{-1})\) with coherent amplitude estimation, times the projector cost.

This must be compared with classical stochastic trace estimation.

Given an efficient routine for \(v\mapsto P_{\ker H_N}v\), Hutchinson, Hutch++, or stochastic Lanczos also avoids explicit diagonalization [R54, R55].

Hutch++ obtains relative trace error with \(O(1/\epsilon)\) matrix-vector products for PSD inputs [R55].

The possible advantage is therefore in the cost of applying the filter, not simply in “quantum trace estimation.”

For a codimension-\(c\) projective variety of degree \(D\) in the stable range,

\[
h_N\asymp
D\,\frac{(n-1)!}{(n-1-c)!}\,N^{-c}.
\]

Recovering \(D\) requires error below roughly half the change caused by incrementing \(D\), hence \(\epsilon=O(N^{-c})\).

This eliminates polylogarithmic dependence on \(N\).

A plausible speedup remains for structured low-codimension ideals where \(N=\operatorname{poly}(n)\), \(c=O(1)\), and classical methods still require vectors of length \(M_N\).

Exact Hilbert functions and multiplicative estimates that distinguish zero from nonzero remain #P/NP-hard targets and are not credible general BQP tasks.

### Cheapest hardware attack

Ground-space spectroscopy is the direct condensed-matter experiment.

The difficulty is that degeneracy counting requires temperature and energy resolution below \(\Delta_N\), and readout of an exponentially large degeneracy is not automatic.

For small quadratic ideals, Bose-Hubbard or spinor-BEC platforms are natural.

A photonic experiment could estimate normalized traces through randomized measurements or interferometric overlap tests, but generic \(H_N\) still needs non-Gaussian interactions.

Boson sampling does not natively return kernel dimension.

## 6. Gröbner basis computation

### Problem statement

Given \(f_1,\ldots,f_s\) and a monomial order, output a Gröbner basis \(G\) of \(I\), optionally reduced.

Parameters include \(n,s,d,t,\tau\), the monomial order, coefficient field, output degree, output support, and coefficient height.

Changing from degree-reverse-lexicographic order to lexicographic order is a separate problem.

### Best classical algorithms

Buchberger's algorithm reduces critical pairs.

F4 batches reductions into sparse Macaulay matrices [R08].

F5 and signature algorithms remove reductions that are provably redundant; for regular sequences, F5 avoids reductions to zero [R09].

Modern exact implementations combine:

- modular images;
- sparse symbolic preprocessing;
- dense or sparse linear algebra;
- signatures;
- tracers across primes;
- rational reconstruction;
- order conversion.

FGb, `msolve`, Magma, Maple, Singular, and Macaulay2 are the relevant baselines.

For a homogeneous regular sequence of \(n\) equations of degrees \(d_i\), the degree of regularity is

\[
d_{\rm reg}=1+\sum_{i=1}^n(d_i-1).
\]

The decisive Macaulay dimension is approximately

\[
M_{\rm reg}=\binom{n+d_{\rm reg}-1}{d_{\rm reg}}.
\]

Dense F4/F5 linear algebra then costs roughly

\[
\widetilde O(M_{\rm reg}^{\omega})
\]

field operations and \(O(M_{\rm reg}^2)\) dense memory.

For semi-regular overdetermined equal-degree systems, \(d_{\rm reg}\) is predicted from the first nonpositive coefficient of

\[
\frac{(1-z^d)^s}{(1-z)^n}.
\]

Complexity analyses of F5 make these assumptions explicit [R10].

For zero-dimensional ideals of degree \(D\), classical FGLM order conversion costs \(O(nD^3)\) field operations [R12].

Fast or sparse variants reduce this toward \(O(nD^\omega)\) or exploit sparse multiplication matrices [R13].

### Worst-case hardness

Reduced Gröbner bases can contain polynomials of doubly exponential degree and doubly exponential output size [R02, R04].

The best general algorithms cannot avoid writing that output.

Mayr-Ritscher show that the double-exponential behavior is tied more precisely to ideal dimension [R05].

F4 and F5 improve practical behavior but not this worst-case output barrier.

### Seed structure and quantum assessment

Each F4 reduction is linear algebra on a Macaulay matrix, suggesting quantum linear algebra locally.

That observation does not yield a fast Gröbner basis algorithm.

The computation is adaptive:

- new leading monomials determine future columns;
- symbolic preprocessing depends on earlier pivots;
- signatures and syzygy criteria change the matrix;
- the required output may itself be exponential.

The seed's \(H_N\) contains degree-\(N\) column-space information but contains no monomial order.

It cannot identify a leading-term ideal without additional computation.

An adiabatic path from a monomial ideal is circular if constructing the path requires a Gröbner basis first.

Even with a valid flat Gröbner degeneration, adiabatic evolution transports one state at a time and does not output the basis.

Quantum subroutines could plausibly reduce memory for isolated rank or membership queries inside F4.

They cannot give an end-to-end exponential speedup for explicitly outputting a general Gröbner basis.

### Cheapest hardware attack

MBQC or a gate model is the natural implementation of adaptive symbolic linear algebra.

A Bose-Hubbard realization may explore the spectrum of one fixed Macaulay block but does not implement term-order updates.

Passive or Gaussian boson sampling is a poor fit.

Permanent or hafnian samples do not reveal leading monomials or S-pair closure.

## 7. Polynomial system solving, root counting, and real roots

### Problem statements

For a square zero-dimensional system \(F=(f_1,\ldots,f_n)\), possible outputs are:

- one approximate complex root;
- all isolated complex roots;
- the number of roots, with or without multiplicity;
- an exact rational univariate representation;
- all real roots with isolating boxes;
- one point on every real connected component.

For positive-dimensional systems, the standard numerical output is a witness-set or numerical irreducible decomposition.

The requested precision and treatment of singular roots must be explicit.

### Best classical algorithms

Exact solving typically uses:

1. a degree-reverse-lexicographic Gröbner basis;
2. multiplication matrices or FGLM;
3. a rational univariate representation;
4. univariate real or complex root isolation.

`msolve` is a strong exact zero-dimensional baseline [R11].

Macaulay2, Singular, FGb, Magma, and Maple cover broader symbolic workflows.

Numerical homotopy continuation tracks paths from a start system.

The total-degree path count is at most

\[
D_{\rm Bezout}=\prod_i d_i.
\]

For generic dense equal-degree systems this is \(d^n\).

For sparse Laurent systems, the BKK count is the mixed volume of Newton polytopes [R17].

Polyhedral homotopy tracks that many generic paths rather than the often larger total-degree count [R18].

Bertini, HomotopyContinuation.jl, and PHCpack are the principal practical baselines [R19, R22, R23].

Parameter homotopy amortizes a solved generic instance across many parameter values.

Monodromy can find solutions without tracking every start path when the family structure is favorable.

For one approximate root of a random dense system, classical homotopy has average polynomial-time algorithms.

Lairez gave a deterministic average-polynomial algorithm [R20].

Rigid continuation attains a near-linear input-size average bound and \(O(n^5d^2)\) average continuation steps in its stated random model [R21].

Any quantum claim for “find one generic approximate root” must beat these baselines, not all-root enumeration.

For real semialgebraic feasibility and component sampling, critical-point and roadmap methods have singly exponential \((sd)^{O(n)}\) arithmetic complexity.

General cylindrical algebraic decomposition can be doubly exponential.

Basu-Pollack-Roy is the standard complexity reference [R24].

### Hardness

Complex feasibility is NP-hard and in PSPACE, with the conditional upper bound described in Section 4 [R07].

Exact root counting is #P-hard through Boolean polynomial encodings.

All-root output requires \(\Omega(D)\) time merely to write \(D\) roots.

The generic count can be \(d^n\).

Real feasibility contains the existential theory of the reals and is NP-hard.

Singular roots can require precision proportional to inverse separation and condition number.

### Seed structure and quantum assessment

For a zero-dimensional saturated ideal in the stable range, \(\dim\ker H_N=D\), the scheme length.

Projection can in principle prepare a mixed state on the quotient space.

It does not automatically prepare a uniform classical root.

The coherent root states are generally nonorthogonal.

Their Gram matrix may be exponentially ill-conditioned.

A maximally mixed state on \(R_N\) has ground-space weight \(D/M_N\), producing amplification cost

\[
\sqrt{M_N/D}.
\]

For Boolean systems this can be worse than Grover.

A specially structured initial state can improve the overlap, but preparing it must be included.

Ding et al. show the analogous conditioning obstruction for the HHL Macaulay solver [R52].

For generic dense systems, classical homotopy already finds one root in average polynomial time.

The plausible quantum target is instead a sample from exponentially many well-conditioned roots without enumerating them.

That target still needs a precise distribution and a proof that state preparation and decoding are efficient.

### Cheapest hardware attack

For low-degree systems, a Bose-Hubbard or spinor-BEC device can minimize the residual energy on coherent states.

It is a heuristic root finder.

Photonic postselection can implement amplitude amplification over discretized candidate roots, giving at most Grover scaling without additional structure.

Boson sampling is relevant only where the polynomial system itself encodes a permanent or hafnian.

It is not a generic polynomial solver.

## 8. Distance to a variety and nearest points

### Problem statements

Given a real algebraic variety

\[
X=\{x\in\mathbb R^n:f_1(x)=\cdots=f_s(x)=0\}
\]

and \(u\in\mathbb Q^n\), compute

\[
\operatorname{dist}(u,X)^2
 =\min_{x\in X}\|x-u\|_2^2.
\]

Possible outputs are:

- the global minimum value to additive error;
- a nearest real point;
- all complex critical points;
- the Euclidean-distance degree of \(X\).

The Euclidean-distance degree is the number of complex critical points for generic \(u\) [R25].

### Best classical algorithms

For smooth complete intersections, Lagrange multipliers give

\[
f_i(x)=0,\qquad
x-u=J_f(x)^\top\lambda.
\]

Symbolic Gröbner or resultant methods solve this critical system exactly.

Numerical homotopy tracks its ED-degree many solutions.

Monodromy and local critical-point methods can reduce path work in families [R26].

Macaulay2 has an `EuclideanDistanceDegree` package.

Bertini and HomotopyContinuation.jl solve the critical systems numerically.

For a generic affine hypersurface of degree \(d\) in \(\mathbb C^n\),

\[
\operatorname{EDdeg}(X)
 =d\sum_{i=0}^{n-1}(d-1)^i,
\]

so the all-critical-point problem is already exponential in \(n\) at fixed \(d>2\) [R25].

Special varieties can be much easier.

For unconstrained low-rank matrices, the nearest rank-\(r\) point is given by truncated SVD.

No quantum algorithm should be compared with generic polynomial solving on that case.

### Hardness

General polynomial distance minimization contains polynomial optimization and is NP-hard.

Nearest rank-one approximation and spectral norm for order-three tensors are NP-hard, including approximation variants [R27].

There may be no well-separated unique nearest point.

Near the ED discriminant, critical points collide and the condition number diverges.

### Seed structure and quantum assessment

For a coherent state, \(H_N\)'s energy is a weighted residual sum of squares.

Thus coherent-state energy minimization approximates distance to the zero set after normalization and metric corrections.

The full ground space is larger than the coherent-state manifold.

Ground-state preparation therefore does not solve nearest-point optimization.

A plausible construction forms the Lagrange critical ideal and applies the zero-dimensional quotient machinery.

If the ED degree \(D_{\rm ED}\) is exponential, a quantum spectral sampler might return one critical point without enumerating all \(D_{\rm ED}\) paths.

The gain survives only if:

- the critical ideal is polynomially gapped;
- a root-supported state has nonnegligible overlap;
- roots are well separated;
- the desired nearest real critical point can be identified without reading all roots.

Finding the minimum among \(D_{\rm ED}\) opaque critical values is at best a quadratic Grover-type improvement without further geometry.

### Cheapest hardware attack

The most direct heuristic is variational coherent-state minimization in a Bose-Hubbard or spinor-condensate emulator.

Quadratic varieties are the practical first test.

Photonic MBQC can implement the Lagrange-system projector for small examples.

Boson sampling is relevant for distance to special determinantal or matching varieties only when the critical equations reduce to permanent or hafnian statistics.

## 9. Zero-dimensional ideals and eigenvalue methods

### Problem statements

Let \(I\) be zero-dimensional and

\[
D=\dim_K R/I.
\]

Construct multiplication matrices

\[
M_{x_i}:R/I\to R/I,
\]

or return one or all points of \(V(I)\).

For nonradical ideals, the output may also include local multiplicity and Jordan structure.

### Best classical algorithms

A Gröbner or border basis supplies a basis of \(R/I\).

FGLM constructs multiplication matrices and converts monomial orders in \(O(nD^3)\) field operations [R12].

Fast dense variants approach \(O(nD^\omega)\).

Sparse FGLM uses Krylov sequences and sparse multiplication matrices [R13].

A generic linear combination of the multiplication matrices is diagonalized.

For radical ideals, its joint eigenvalues give point coordinates.

For nonradical ideals, Jordan blocks encode local algebra.

This eigenvalue formulation and its multiple-root extension are classical [R28].

Border-basis and stabilized normal-form methods improve numerical behavior under perturbation [R29].

`msolve` combines F4, sparse FGLM, rational reconstruction, and real-root isolation.

Its degree-\(8192\) Katsura-14 result is a useful exact scale anchor [R11].

Numerical homotopy is normally superior when floating approximations to all nonsingular roots suffice.

### Hardness

The quotient dimension \(D\) can be \(d^n\).

Constructing \(n\) dense \(D\times D\) matrices costs \(\Omega(nD^2)\) storage.

Writing all roots costs \(\Omega(nD)\).

Exact root counting is #P-hard.

Nonnormal eigenproblems can have exponentially sensitive eigenvectors even when coordinate separation is moderate.

### Seed structure and quantum assessment

For stable homogeneous degree \(N\), the quotient is represented by \((I_N)^\perp\).

Compressed creation maps realize multiplication between adjacent degrees.

After choosing a non-zero-divisor \(x_0\), affine multiplication is formally

\[
X_i=\mu_{x_0}^{-1}\mu_{x_i}.
\]

This suggests quantum access to a \(D\)-dimensional quotient using only \(O(n\log N)\) qubits.

It is one of the most interesting possible space advantages.

The obstruction is that \(X_i\) is generally nonnormal.

Ordinary phase estimation does not apply.

A singular-value scan of \(Z_i-\lambda Z_0\) is controlled by pseudospectral conditioning, Jordan blocks, and eigenvector conditioning.

Even for a reduced ideal, coherent evaluation vectors can form an ill-conditioned basis.

A credible speedup requires radical, well-separated, quantitatively well-conditioned families.

The output should be one sampled root or a spectral statistic, not all \(D\) roots.

### Cheapest hardware attack

MBQC is the cleanest implementation of QSVT and singular-value scans.

A multimode bosonic device naturally realizes inter-degree creation maps, but quotient compression requires engineered interactions or postselection.

Spectroscopy of a few quotient modes is plausible for small \(D\).

Passive boson sampling does not diagonalize nonnormal multiplication tuples.

## 10. Syzygies and graded Betti numbers

### Problem statements

The first syzygy module is

\[
\operatorname{Syz}(f_1,\ldots,f_s)
=
\{(h_i):\sum_i h_if_i=0\}.
\]

At degree \(N\),

\[
\operatorname{Syz}_N=\ker\Phi_N.
\]

A minimal graded free resolution has Betti numbers

\[
\beta_{p,q}
 =\dim_K\operatorname{Tor}^{R}_p(R/I,K)_q.
\]

Possible outputs are:

- a basis for \(\operatorname{Syz}_N\);
- all maps in a minimal free resolution;
- one Betti number;
- a normalized Betti number.

### Best classical algorithms

Fixed-degree syzygies are nullspaces of \(\Phi_N\).

Schreyer's algorithm computes Gröbner bases of syzygy modules recursively.

Signature algorithms already exploit syzygies to suppress zero reductions.

Macaulay2 is the principal practical platform for minimal free resolutions.

Singular also supplies module Gröbner bases and resolutions.

Modern Macaulay2 strategies exploit Schreyer frames and Hilbert-function information [R30].

If quotient multiplication matrices of dimension \(D\) are known, finite-dimensional syzygies can be computed in

\[
O(mD^{\omega-1}+nD^\omega\log D)
\]

field operations under the assumptions of the cited algorithm [R31].

Minimalization adds rank computations over the coefficient field.

Resolution output can itself be exponential.

### Hardness

Syzygy degree bounds inherit doubly exponential ideal-theoretic behavior.

For Stanley-Reisner ideals, Hochster's formula relates graded Betti numbers to homology of induced subcomplexes.

Exact Betti-number computation for clique complexes is #P-hard, and multiplicative approximation is NP-hard [R32].

Thus no general efficient exact quantum Betti-number algorithm is credible.

### Seed structure and quantum assessment

The seed directly exposes

\[
\ker\Phi_N=\operatorname{Syz}_N
\]

on the domain side and

\[
\ker\Phi_N^\dagger=(I_N)^\perp
\]

on the codomain side.

QSVT can estimate normalized nullity or prepare a syzygy state under a singular-value gap promise.

Higher syzygies suggest a chain complex and Hodge Laplacians.

This parallels quantum topological-data-analysis algorithms [R33].

The classical baseline is again sparse rank and stochastic trace estimation.

A quantum advantage is plausible for a normalized Betti fraction bounded below by \(1/\operatorname{poly}(n)\), with succinct boundary maps and inverse-polynomial gaps.

If the Betti number is exponentially small relative to chain dimension, multiplicative estimation requires exponentially many samples.

An explicit basis of syzygies cannot be output faster than its size.

### Cheapest hardware attack

MBQC is the strongest fit for a sequence of sparse boundary maps.

A supersymmetric or frustration-free Hamiltonian whose zero modes are homology classes is a possible condensed-matter experiment.

Linear optics can implement quadratic boundary operators only in special free-particle encodings.

Higher polynomial syzygies require non-Gaussian interactions.

## 11. Sampling roots or points on a variety

### Problem statements

A sampling task is incomplete until it specifies the distribution.

Relevant possibilities are:

- uniform over distinct roots of a zero-dimensional radical ideal;
- multiplicity-weighted over a zero-dimensional scheme;
- Fubini-Study volume on a smooth projective variety;
- a witness-point distribution induced by random slices;
- a Gibbs distribution proportional to \(e^{-\beta\sum|f_i|^2}\);
- a local distribution near a supplied component.

Precision and treatment of disconnected components must be specified.

### Best classical algorithms

For zero-dimensional systems, solve all roots and sample from the list.

This costs \(O(D)\) output but supports arbitrarily many subsequent samples.

Parameter homotopy amortizes repeated samples across changing coefficients.

Monodromy can explore roots in a family without constructing an exact Gröbner basis.

For positive-dimensional complex varieties, Bertini, PHCpack, HomotopyContinuation.jl, and NAG4M2 use random slices and witness sets.

For smooth real varieties, constrained Hamiltonian Monte Carlo, geodesic walks, and local parameterizations are practical heuristics.

There is no general polynomial mixing theorem across arbitrary singular, disconnected real varieties.

### Hardness

Uniform root sampling for Boolean polynomial systems contains uniform satisfying-assignment generation.

Black-box projection from a state whose root weight is \(p\) costs \(\Theta(p^{-1/2})\) with amplitude amplification.

This is not a universal lower bound on every algorithm, but it is unavoidable for that projection method.

Producing all roots remains output-limited.

### Seed structure and quantum assessment

The mixed state

\[
P_{\ker H_N}/\operatorname{HF}(N)
\]

is uniform on a linear inverse-system subspace.

It is not uniform on geometric points.

Measuring in the monomial basis samples occupation patterns, not roots.

A coherent-state POVM would produce a Husimi-type distribution smeared at angular scale \(N^{-1/2}\).

Implementing and decoding that POVM is an additional algorithmic task.

For finite radical varieties, coherent root states become closer to orthogonal as \(N\) grows, but the required \(N\) can scale as inverse separation and \(\log D\).

That growth also worsens normalization and Hamiltonian cost.

The plausible target is a structured family with:

- well-separated roots;
- a known high-overlap initial state;
- an inverse-polynomial gap;
- a root-decoding map from occupation statistics.

Boolean projection appears Grover-limited rather than exponentially faster [R52].

### Cheapest hardware attack

A bosonic coherent-state measurement is the most natural experiment.

Linear optics followed by heterodyne or photon-number measurement can probe Husimi distributions.

Postselection can filter low-energy states but must not have exponentially small acceptance.

For positive-dimensional varieties, analogue Langevin dynamics in a Bose-Hubbard energy landscape may be a useful heuristic sampler.

Boson sampling does not by itself define a geometrically natural root distribution.

## 12. Tensor rank and secant varieties

### Problem statements

Given

\[
T\in K^{n_1}\otimes\cdots\otimes K^{n_k},
\]

decide whether

\[
\operatorname{rank}(T)\leq r,
\]

or find a decomposition into \(r\) simple tensors.

Geometrically, border rank at most \(r\) is membership in the \(r\)-th secant variety of the Segre variety.

For symmetric tensors, replace Segre by Veronese and tensor rank by Waring rank.

Approximation asks for

\[
\min_{\operatorname{rank}(S)\leq r}\|T-S\|.
\]

The input may be a dense array, a sparse array, an arithmetic circuit, or a quantum state; these encodings are not interchangeable.

### Best classical algorithms

Dense numerical practice uses alternating least squares, nonlinear least squares, Riemannian methods, and structured packages such as Tensorlab.

These methods find local optima and scale roughly linearly in the number of stored tensor entries per sweep.

Exact or certified small cases use flattening minors, catalecticants, Gröbner bases, eigenvector methods, and numerical algebraic geometry.

Bertini and HomotopyContinuation.jl can solve secant parameterizations or decomposition equations.

Homotopy methods for tensor decomposition are developed in [R36].

The practical dense baseline can handle millions of entries when the rank is modest, because it never forms secant ideals.

Any quantum proposal using a Gröbner baseline in that regime is miscalibrated.

### Hardness and pathology

Tensor rank is NP-complete over finite fields and NP-hard over \(\mathbb Q\) [R34].

Best rank-one approximation, tensor spectral norm, and related approximation problems are NP-hard [R27].

For tensors of order at least three, a best rank-\(r\) approximation may fail to exist [R35].

Border-rank geometry can therefore be better behaved algebraically than numerical tensor rank while representing a different problem.

### Seed structure and quantum assessment

A rank-one symmetric tensor is a coherent state.

Distance to the Veronese variety is therefore closely related to maximum coherent-state overlap.

For multipartite tensors, product-state overlap is the analogous Segre problem.

This is physically natural but computationally hard.

Amplitude encoding a dense tensor costs \(\Omega(\prod_i n_i)\) without QRAM or a preparation circuit.

If \(T\) is already a quantum state, estimating maximum product overlap may be meaningful, but the classical input problem has changed.

Low-rank and length-square accessible tensors are particularly exposed to Tang-style dequantization.

The Hamiltonian inverse-system construction can test polynomial equations defining a secant variety when those equations are known sparsely.

For many ranks, those defining equations are themselves difficult to construct.

### Cheapest hardware attack

Photonic multipartite states naturally represent symmetric tensors and coherent products.

Variational separability or product-overlap measurements are the cheapest heuristic.

Gaussian boson sampling gives hafnians, and ordinary boson sampling gives permanents [R58].

Those quantities are relevant to particular tensor contractions, not general tensor rank.

MBQC is required for a systematic secant-membership circuit.

## 13. Algebraic statistics and maximum-likelihood degree

### Problem statements

Let \(X\) be an algebraic statistical model in a probability simplex.

Given counts \(u=(u_1,\ldots,u_m)\), maximize

\[
L(p)=\prod_i p_i^{u_i}
\]

over the real nonnegative part of \(X\).

The likelihood equations define a rational critical-point system.

The maximum-likelihood degree is the number of complex critical points for generic data [R37].

Outputs may be:

- the global real MLE;
- all complex critical points;
- the ML degree;
- a sample from likelihood-weighted model points.

### Best classical algorithms

Decomposable graphical and toric models often have closed forms, iterative proportional fitting, or convex dual formulations.

General models use Gröbner bases, elimination, numerical homotopy, EM, or local nonlinear optimization.

Symbolic likelihood equations were systematized in [R38].

Macaulay2 supplies `GraphicalModels`, `GraphicalModelsMLE`, and `LikelihoodGeometry`.

Bertini and HomotopyContinuation.jl track all critical points when the ML degree is manageable.

Monodromy and parameter homotopy are natural when many datasets share the same model.

The cost of all-critical-point methods is at least linear in ML degree.

### Hardness

General probabilistic inference in Bayesian networks is NP-hard [R39].

Exact counting and marginalization versions are #P-hard in standard Boolean encodings.

Latent-variable likelihoods are nonconvex and may contain many local maxima.

These results do not imply every fixed algebraic model is hard.

Models of ML degree one are classically trivial from the algebraic perspective.

### Seed structure and quantum assessment

The likelihood critical equations can be converted into a polynomial ideal and treated as a zero-dimensional quotient.

A quantum sampler might return a critical point without enumerating every one.

The same nonnormal multiplication-matrix and overlap obstacles apply.

Alternatively, one could form a Gibbs state for minus log-likelihood, but logarithms and boundary singularities are not polynomial Hamiltonian terms.

The most credible regime is a structured model family with large ML degree, well-conditioned isolated critical points, and many repeated datasets.

Parameter-homotopy preprocessing is then the strongest classical competitor.

A one-shot quantum advantage that ignores this amortization is not real.

### Cheapest hardware attack

Photonic circuits naturally produce multinomial count data but do not automatically solve likelihood equations.

MBQC can implement a critical-ideal projector.

Analogue Gibbs preparation in a bosonic model is a heuristic fit, particularly for toric models.

Boson sampling is relevant only when the statistical model is itself a permanent or hafnian model.

## 14. Low-rank matrix completion and determinantal varieties

### Problem statements

Given observed entries

\[
\{M_{ij}:(i,j)\in\Omega\},
\]

find a matrix \(X\in\mathbb R^{n_1\times n_2}\) satisfying those entries and

\[
\operatorname{rank}(X)\leq r.
\]

Algebraically, rank at most \(r\) is the determinantal variety cut out by all \((r+1)\)-minors.

Variants request exact feasibility, noisy least squares, minimum rank, PSD completion, or uniqueness.

Parameters are \(n_1,n_2,r,m=|\Omega|,\tau\), noise, incoherence, and condition number.

### Best classical algorithms

For random observations and incoherent low-rank matrices, nuclear-norm minimization gives exact recovery guarantees [R40].

Spectral initialization plus manifold or factorized optimization is the large-scale practical baseline.

OptSpace has complexity

\[
O(mr\log n)
\]

in its stated model and recovery from \(O(rn\log n)\) entries for bounded rank [R41].

Riemannian completion methods cost roughly \(O(mr+(n_1+n_2)r^2)\) per iteration [R42].

These methods routinely process matrices with millions to hundreds of millions of observations.

Writing all determinantal minors is almost never competitive.

Symbolic algebra is appropriate for identifiability, algebraic matroids, or very small exact instances.

### Hardness

Arbitrary minimum-rank completion is NP-hard.

Rank-constrained PSD completion remains NP-hard for every fixed \(r\geq2\) in the cited formulation [R43].

These worst-case results coexist with strong polynomial algorithms under random incoherence assumptions.

### Seed structure and quantum assessment

The determinantal ideal can be inserted into \(H_N\), but its generator count

\[
\binom{n_1}{r+1}\binom{n_2}{r+1}
\]

may already be large.

The resulting Macaulay formulation discards the factorized structure exploited by classical solvers.

Quantum singular-value transformation is natural for low-rank matrices, but this is precisely the regime where quantum-inspired sample/query algorithms are strongest [R49–R51].

A claim of exponential speedup under QRAM or length-square access is therefore at extreme dequantization risk.

A credible target would need a structured determinantal query not already answered by randomized SVD or factorized optimization.

Exact worst-case rank-constrained feasibility might offer only Grover-type improvements and remains vulnerable to conditioning.

### Cheapest hardware attack

Variational photonic or superconducting linear algebra can test small low-rank factorizations.

Gaussian optics naturally implements linear transformations and singular-mode analysis.

It does not enforce missing-entry constraints and rank simultaneously without a hybrid optimizer.

Boson sampling is not a natural matrix-completion primitive.

## 15. Polynomial optimization and SOS/Lasserre hierarchies

### Problem statements

Given polynomial \(p\) and constraints

\[
g_j(x)\geq0,\qquad h_k(x)=0,
\]

compute

\[
p^\star=\inf_{x\in K}p(x)
\]

or certify a lower bound.

At Lasserre order \(r\), the moment matrix has size

\[
B_r=\binom{n+r}{r}.
\]

The output may be:

- the exact global optimum;
- an \(\epsilon\)-additive optimum;
- the order-\(r\) SDP value;
- an SOS certificate;
- an optimizer extracted from a flat moment matrix.

These must not be conflated.

### Best classical algorithms

The Lasserre hierarchy solves a sequence of SDPs converging under standard compactness assumptions [R44].

At order \(r\), dense storage of one PSD block is \(O(B_r^2)\).

Dense factorization is \(O(B_r^3)\) per major linear-algebra step before accounting for the Schur complement and constraint count.

For \(n=20,r=4\),

\[
B_r=\binom{24}{4}=10\,626.
\]

One dense double-precision block occupies about 0.9 GB, and a cubic factorization is about \(1.2\times10^{12}\) floating-point operations.

This explains why practical dense SOS calculations usually stop at low orders.

Sparse correlative sparsity, chordal decomposition, symmetry, DSOS/SDSOS restrictions, and first-order SDP solvers extend the range.

The practical software baseline includes MOSEK, SDPA, CSDP, SOSTOOLS, GloptiPoly, YALMIP, SumOfSquares.jl, and ncpol2sdpa.

For Boolean degree-\(d\) optimization, exactness may require order

\[
\left\lceil\frac{n+d-1}{2}\right\rceil,
\]

which is exponential-size in \(n\) [R45].

### Hardness

Boolean quadratic optimization already contains MAX-CUT.

General polynomial optimization is NP-hard even at low fixed degree with polynomial constraints.

Exact nonnegativity and exact rational SOS certificates have additional bit-complexity and weak-feasibility issues.

No fixed low level of the hierarchy solves all instances.

### Seed structure and quantum assessment

SOS is already Hamiltonian-like: moment and localizing matrices are PSD constraints, while dual SOS certificates are Gram matrices.

Quantum SDP solvers can have square-root or dimension advantages in sparse-oracle models, but their costs depend polynomially on accuracy, width, trace bounds, Gibbs preparation, and oracle parameters [R46].

Worst-case lower bounds eliminate a generic polylogarithmic SDP solver [R46].

Quantum solvers also tend to return a quantum state or value estimate, not an explicit moment matrix or SOS decomposition.

Classical output requirements can erase the speedup.

Low-rank SDP structure is exposed to quantum-inspired dequantization [R51].

A plausible target is the value of a fixed sparse SOS relaxation with succinct localizing matrices and no need to output the certificate.

It is not a general global polynomial optimizer.

### Cheapest hardware attack

This family has the strongest condensed-matter fit.

Boolean quadratic instances are Ising models.

Polynomial interactions map to higher-body spin or bosonic couplings, with gadget overhead for reducing locality.

Bose-Hubbard ground-energy estimation is QMA-complete in general [R60].

Variational analogue optimization is cheap experimentally but has no general accuracy guarantee.

Photonic MBQC can implement sparse SDP or QSVT routines.

Boson sampling does not solve an SDP merely because both involve PSD matrices.

## 16. Projector overlaps, intersections, and integration

### Problem statements

Given two homogeneous ideals \(I,J\) and a degree \(N\), estimate

\[
\frac1{M_N}\operatorname{Tr}(P_I P_J),
\]

where \(P_I\) and \(P_J\) project onto their inverse-system spaces.

Given an observable \(T_g\), estimate

\[
\frac{\operatorname{Tr}(P_I T_g)}
     {\operatorname{Tr}P_I}.
\]

Potential geometric interpretations include intersection concentration, distance between disjoint varieties, and integration over a smooth variety.

These interpretations require separate theorems and stable-range hypotheses; the seed's asymptotic formulas are not established by this memo.

### Best classical algorithms

Classical alternatives are:

- compute both Macaulay projectors explicitly;
- use stochastic Lanczos and randomized trace products;
- compute witness sets and intersect them numerically;
- sample random slices and perform Monte Carlo;
- use local charts or differential geometry for smooth varieties.

For implicit sparse projectors, Hutchinson and Hutch++ are the immediate baselines [R54, R55].

For geometric intersections, numerical algebraic geometry is often much cheaper than building \(M_N\times M_N\) projectors.

The fair comparison depends on whether the output is an ambient trace or a geometric invariant.

### Hardness and limitations

No general hardness theorem is known for the normalized projector observables in the seed's precise input model.

Exact intersection degree inherits #P-hard counting behavior.

Additive normalized estimates can be much easier and may lose all information when the intersection is low-dimensional.

If two varieties are disjoint and overlap decays exponentially in \(N\), resolving it requires exponentially small additive error.

### Seed structure and quantum assessment

Controlled kernel projectors and a SWAP or Hadamard test give a compact quantum route to normalized overlaps.

This may offer both time and space savings over explicit projectors.

Classical stochastic trace estimators are a strong threat.

The quantum advantage must come from cheaper coherent application of the projector, not from the trace identity.

This is a plausible campaign target because the output is scalar and no exponential classical object is requested.

It needs a proven geometric interpretation and a classical benchmark based on implicit filters, not Gröbner bases alone.

### Cheapest hardware attack

Two-copy interferometry is natural for projector overlap.

A bosonic simulator with independently prepared ground-space ensembles could estimate overlaps through randomized measurements.

For small mode counts, linear-optical interference followed by number detection is appropriate.

Generic preparation of the two ground-space ensembles remains the main cost.

## 17. Cross-family hardware assessment

Passive linear optics implements mode unitaries generated by \(a_i^\dagger a_j\).

It exactly preserves total boson number and the Fock-sector encoding.

It does not implement generic

\[
f(a^\dagger)\overline f(a)
\]

when \(\deg f>1\).

Postselection, feed-forward, non-Gaussian ancillas, or genuine interactions are required [R57].

Ordinary boson sampling produces probabilities proportional to squared permanents.

Gaussian boson sampling produces hafnians [R58].

Neither supplies generic Macaulay ranks, Gröbner bases, Hilbert functions, or quotient multiplication spectra.

A claimed mapping must exhibit an explicit permanent or hafnian identity for the target observable.

MBQC is universal and can implement sparse-oracle QSVT, amplitude estimation, and arithmetic.

Its relevance is algorithmic rather than algebraically specific.

Bose-Hubbard and spinor-BEC systems are the most natural analogue models because degree-two generators yield quartic number-conserving interactions.

The conic spin-mixing example has a direct physical precedent [R59].

Higher-degree generators require increasingly nonlocal many-boson interactions or perturbative gadgets.

The formal complexity of unrestricted bosonic computation depends critically on energy and non-Gaussian resources [R61].

“Bosonic encoding” alone is therefore not evidence of an efficient physical implementation.

## Ranked candidates

### 1. Additive distance to a fixed degree piece of an ideal

Problem: estimate \(\delta_I(g)^2\) for a sparse \(g\in R_N\), with inverse-polynomial promise gap and normalized Macaulay gap.

Quantum primitive: sparse block encoding of \(H_N\), QSVT kernel projection, and amplitude estimation.

Classical baseline: sparse LSQR/LSMR, randomized range finding, or a Krylov polynomial filter on the same implicit Macaulay matrix.

Plausible speedup: both time and space, potentially exponential in \(\log M_N\), but only for a scalar additive output.

Dequantization risk: medium; \(H_N\) is not generally low rank, but sample/query access and structured convolution may support classical sublinear algorithms.

Hardware fit: strong for quadratic Bose-Hubbard or spinor-BEC examples; MBQC for the general sparse oracle.

This candidate should be tested first because it matches the seed construction exactly and avoids exponential output.

### 2. Normalized Hilbert function in structured low codimension

Problem: estimate \(\operatorname{HF}(N)/M_N\) to the precision needed to distinguish degrees or codimensions in a promised stable family.

Quantum primitive: DQC1-style or amplitude-estimated trace of the QSVT kernel projector.

Classical baseline: Hutch++, stochastic Lanczos quadrature, randomized numerical-rank estimation, and Gröbner/Hilbert-series computation.

Plausible speedup: both time and space when projector application is quantumly polylogarithmic in \(M_N\) but classically requires full-length vectors.

Dequantization risk: high because stochastic trace estimation already avoids diagonalization and may need few probes.

Hardware fit: ground-space spectroscopy or two-copy interferometry in small bosonic systems.

The campaign must benchmark projector-application cost, not compare quantum trace estimation with dense exact rank.

### 3. One spectral sample from a well-conditioned zero-dimensional quotient

Problem: sample one coordinate tuple or a smooth spectral statistic from a radical degree-\(D\) quotient without constructing all \(D\) roots.

Quantum primitive: kernel preparation, compressed coordinate multiplication, and singular-value or Hermitian-dilation spectral estimation.

Classical baseline: `msolve` F4 plus sparse FGLM, multiplication matrices, or parameter homotopy.

Plausible speedup: both time and space when \(D\) is exponential but a sampled output is meaningful.

Dequantization risk: medium to high; Krylov methods can also sample spectral measures if comparable vector access is available.

Hardware fit: MBQC is strongest; multimode bosonic spectroscopy is plausible for small reduced quotients.

This candidate is conditional on proving polynomial eigenvector and Gram conditioning for a nontrivial family.

### 4. Normalized syzygy or Betti fractions

Problem: estimate the normalized nullity of a degree-\(N\) syzygy map or a normalized Betti number of a succinct chain complex.

Quantum primitive: QSVT on \(\Phi_N\) or a Hodge Laplacian, followed by trace estimation.

Classical baseline: sparse rank, block Wiedemann, Schreyer-frame resolutions, and stochastic trace filtering.

Plausible speedup: both time and space for large Betti fractions and polynomial spectral gaps.

Dequantization risk: medium; sparse boundary matrices admit strong classical iterative methods, but are not necessarily low rank.

Hardware fit: MBQC or a frustration-free supersymmetric Hamiltonian.

Exact or multiplicative Betti computation is excluded by known #P/NP hardness [R32].

### 5. Projector-overlap observables for intersections

Problem: additively estimate \(\operatorname{Tr}(P_I P_J)/M_N\) or a normalized Toeplitz trace.

Quantum primitive: two controlled projectors, Hadamard/SWAP tests, and trace estimation.

Classical baseline: stochastic trace products, numerical witness-set intersection, and Monte Carlo on the varieties.

Plausible speedup: both time and space for scalar observables when neither variety is cheaply parameterized.

Dequantization risk: high because randomized trace estimation is directly applicable.

Hardware fit: two-copy bosonic interference and randomized measurements.

The candidate becomes valuable only after a rigorous theorem connects the normalized observable to a geometric quantity at polynomially resolvable scale.

### 6. Sampling an ED critical point in a structured high-ED-degree family

Problem: return one well-conditioned critical point of distance to a variety, rather than all ED-degree critical points.

Quantum primitive: projector onto the Lagrange critical ideal plus amplitude amplification and root decoding.

Classical baseline: structured homotopy, monodromy, and parameter homotopy tracking \(D_{\rm ED}\) paths.

Plausible speedup: time and possibly space if the quantum method avoids enumeration.

Dequantization risk: high because homotopy can find selected solutions, and minimum selection remains Grover-limited.

Hardware fit: strong heuristic fit to coherent-state Bose-Hubbard minimization; MBQC for a controlled algorithm.

The nearest-real-point problem is harder than sampling an arbitrary complex critical point and must be evaluated separately.

### 7. Sparse fixed-level SOS value estimation

Problem: estimate the optimum of one specified sparse Lasserre relaxation, without outputting the moment matrix or SOS certificate.

Quantum primitive: sparse quantum SDP solving, Gibbs preparation, or QSVT on moment/localizing operators.

Classical baseline: chordal sparse SDP, first-order methods, low-rank factorization, and commercial interior-point solvers.

Plausible speedup: time, with a possible space advantage from not storing the \(B_r\times B_r\) moment block.

Dequantization risk: high because low-rank and sample/query SDP algorithms dequantize readily and quantum accuracy dependence is severe.

Hardware fit: strongest condensed-matter fit of the list; Ising for Boolean quadratics and Bose-Hubbard for polynomial interactions.

The claim must be restricted to the fixed relaxation value, not global polynomial optimization.

### 8. Algebraic-statistics critical-point sampling across repeated data

Problem: after model-specific preprocessing, sample a likelihood critical point for each of many datasets.

Quantum primitive: reusable quotient projector or block encoding, followed by state-dependent spectral sampling.

Classical baseline: parameter homotopy, monodromy, EM, and model-specific convex algorithms.

Plausible speedup: time amortized across many datasets; possible quantum space advantage.

Dequantization risk: medium to high because classical parameter homotopy also amortizes most algebraic work.

Hardware fit: MBQC; analogue Gibbs preparation is heuristic.

Only models with demonstrably large ML degree and no closed-form or convex solution should be considered.

### 9. Structured toric-fibre spectral observables

Problem: estimate fibre-Laplacian gaps, normalized fibre counts, or mixing observables for sparse binomial ideals.

Quantum primitive: quantum walk or QSVT on the fibre graph induced by the toric Macaulay block.

Classical baseline: combinatorial fibre enumeration, Markov-basis walks, sparse Laplacian solvers, and dynamic programming.

Plausible speedup: time and space on succinct exponentially large fibres.

Dequantization risk: medium; graph Laplacians have strong classical nearly-linear solvers when the graph is explicitly or locally accessible.

Hardware fit: number-conserving bosonic hopping is natural.

This is more promising than generic boson sampling because the relevant graph and observable arise directly from the ideal.

## Traps

### Comparing against the wrong classical algorithm

Do not compare QSVT with dense Gaussian elimination when sparse Krylov, Wiedemann, F4/F5, homotopy, or stochastic trace methods solve the same promised problem.

Do not compare a quantum approximate root finder with symbolic Gröbner output if numerical homotopy is acceptable.

Do not compare a quantum matrix-completion method with determinantal Gröbner bases; compare it with factorized and Riemannian solvers.

### Changing the output

A quantum state proportional to a solution vector is not an explicit solution vector.

A mixed state on the inverse system is not a list of roots.

Normalized additive Hilbert estimation is not exact Hilbert-function computation.

A sample from critical points is not the nearest real point.

Border rank is not tensor rank.

An order-\(r\) SOS value is not the global optimum unless exactness is proved.

### Hidden state preparation

Dense polynomial or tensor coefficients require linear input time unless a preparation circuit or QRAM is part of the input model.

Preparing a maximally mixed state on valid weak compositions is not identical to starting with arbitrary mixed qubits.

Preparing a coherent sum over Boolean assignments and uncomputing the assignment must include decoding error and normalization.

### Exponentially small overlap

Projection cost includes the inverse square root of the initial weight on the desired subspace.

For a maximally mixed degree-\(N\) state, the relevant weight can be \(\operatorname{HF}(N)/M_N\).

For isolated roots this may be exponentially small.

Amplitude amplification then reproduces Grover scaling or worse.

### Confusing absolute and normalized gaps

Rescaling generators rescales \(\Delta_N\).

Runtime depends on \(\Delta_N/\alpha_N\).

A constant absolute gap with \(\alpha_N=N^{d}\) gives inverse-polynomial normalized gap in \(N\), not in \(\log N\).

### Hiding exponential \(N\)

Encoding \(N\) in binary makes the occupation register compact.

It does not make \(N^d\), precision \(N^{-c}\), or certificate degree \(d^n\) cheap.

Any runtime polynomial in \(N\) is exponential in \(\log N\).

### Ignoring gap closing

No general lower bound on \(\gamma_N\) is known for arbitrary generator tuples.

Multigraded embeddings include frustration-free Hamiltonians with exponentially small gaps.

Presentation changes and nearly redundant generators can make the gap arbitrarily small without changing the ideal.

### Ignoring classical preconditioning

A preconditioner that improves the quantum Macaulay condition number may also accelerate classical Krylov or F4 linear algebra.

The speedup must be measured after giving the same algebraic preconditioner to the classical baseline.

### Treating the ground space as the variety

\(\ker H_N=(I_N)^\perp\) is a linear inverse system.

Only its coherent product states correspond to geometric points.

Nonradical and nonsaturated structure contributes entangled ground states.

Ground-state preparation is therefore not root preparation.

### Claiming the coherent-state test as a quantum algorithm

For a supplied point \(p\), coherent-state energy is a weighted sum of \(|f_i(p)|^2\).

Sparse classical evaluation costs \(O(t)\).

The quantum experiment is useful as a physical demonstration, not as a computational speedup.

### Treating nonnormal multiplication matrices as unitaries

Compressed coordinate multipliers commute but need not be normal.

Ordinary phase estimation does not apply.

Jordan blocks, pseudospectra, and eigenvector condition numbers must appear in the runtime.

### Circular Gröbner deformation

A flat deformation to a monomial initial ideal generally requires a Gröbner basis or equivalent initial-ideal information.

Using that classical Gröbner basis to define a quantum path cannot then be advertised as a Gröbner-basis speedup.

Flatness also does not imply a lower bound on the spectral gap along the path.

### Assuming sparse means quantum-fast only

The Macaulay matrix is sparse and structured.

That supports efficient quantum row access.

It also supports classical sparse matvecs, Wiedemann, block Krylov, modular F4, convolution, and graph methods.

Sparsity cuts both ways.

### Ignoring dequantization

Low-rank QSVT applications with length-square sample/query access are exposed to Tang-style and Gilyén-Lloyd-Tang algorithms [R49–R51].

This is especially serious for matrix completion, tensor approximation, and low-rank SDP.

High-rank sparse projectors are less directly covered, but a specific dequantization audit is still required.

### Mistaking DQC1-style trace estimation for an uncontested advantage

Classical Hutch++ obtains strong trace estimates using only matrix-vector products [R55].

Stochastic Lanczos estimates traces of matrix functions without diagonalization [R54].

The quantum advantage must reduce the cost of each filter application or exploit a genuinely quantum input.

### Ignoring output lower bounds

An explicit Gröbner basis, free resolution, multiplication table, or list of \(D\) roots requires time at least proportional to its output length.

An exponential improvement is possible only for implicit access, scalar summaries, or samples.

### Treating boson sampling as a universal algebraic accelerator

Boson sampling supplies permanents.

Gaussian boson sampling supplies hafnians.

A generic Macaulay rank, Hilbert function, ideal membership question, or Gröbner basis is neither.

An explicit reduction to the native matrix function is required.

### Ignoring postselection probability

Postselected linear optics is computationally universal in principle [R57].

If the selected event has probability \(2^{-\Theta(n)}\), the physical runtime is exponential.

Loss, number resolution, and feed-forward overhead also belong in the resource count.

### Confusing analogue minimization with certification

A Bose-Hubbard device may find a low-energy coherent state.

It does not prove global optimality, radical membership, emptiness, or an SOS bound without a certified error and gap analysis.

Finite temperature can populate exponentially many near-ground states.

### Comparing exact arithmetic with floating-point output

`msolve` produces exact rational parametrizations and isolating data.

Homotopy packages produce floating approximations, with adaptive precision and certification available at additional cost.

A quantum approximate output must be compared with numerical homotopy, not automatically with exact rational reconstruction.

### Ignoring repeated-instance preprocessing

Parameter homotopy, learned F4 traces, modular templates, and precomputed quotient bases can amortize classical work.

A quantum method aimed at many instances must compare amortized costs on both sides.

## Reference ledger

[R01] E. W. Mayr, “Membership in polynomial ideals over \(\mathbb Q\) is exponential space complete,” DOI: `10.1007/BFb0029002`.

[R02] E. W. Mayr and A. R. Meyer, “The complexity of the word problems for commutative semigroups and polynomial ideals,” DOI: `10.1016/0001-8708(82)90048-2`.

[R03] D. T. Huynh, “The complexity of the membership problem for two subclasses of polynomial ideals,” DOI: `10.1137/0215042`.

[R04] T. W. Dubé, “The structure of polynomial ideals and Gröbner bases,” DOI: `10.1137/0219053`.

[R05] E. W. Mayr and S. Ritscher, “Dimension-dependent bounds for Gröbner bases of polynomial ideals,” DOI: `10.1016/j.jsc.2011.12.018`.

[R06] J. Kollár, “Sharp effective Nullstellensatz,” DOI: `10.1090/S0894-0347-1988-0944576-7`.

[R07] P. Koiran, “Hilbert's Nullstellensatz is in the polynomial hierarchy,” DOI: `10.1006/jcom.1996.0019`.

[R08] J.-C. Faugère, “A new efficient algorithm for computing Gröbner bases (F4),” DOI: `10.1016/S0022-4049(99)00005-5`.

[R09] J.-C. Faugère, “A new efficient algorithm for computing Gröbner bases without reduction to zero (F5),” DOI: `10.1145/780506.780516`.

[R10] M. Bardet, J.-C. Faugère, and B. Salvy, “On the complexity of the F5 Gröbner basis algorithm,” arXiv:`1312.1655`.

[R11] J. Berthomieu, C. Eder, and M. Safey El Din, “msolve: A library for solving polynomial systems,” DOI: `10.1145/3452143.3465545`, arXiv:`2104.03572`.

[R12] J.-C. Faugère, P. Gianni, D. Lazard, and T. Mora, “Efficient computation of zero-dimensional Gröbner bases by change of ordering,” DOI: `10.1006/jsco.1993.1051`.

[R13] J.-C. Faugère and C. Mou, “Sparse FGLM algorithms,” arXiv:`1304.1238`.

[R14] R. Fröberg and J. Hollman, “Hilbert series for ideals generated by generic forms,” DOI: `10.1006/jsco.1994.1008`.

[R15] A. Dickenstein and E. A. Tobis, “Independent sets from an algebraic perspective,” DOI: `10.1142/S0218196711006819`, arXiv:`1003.3508`.

[R16] P. Bürgisser and F. Cucker, “The complexity of computing the Hilbert polynomial of smooth equidimensional complex projective varieties,” arXiv:`cs/0502044`.

[R17] D. N. Bernshtein, “The number of roots of a system of equations,” DOI: `10.1007/BF01075595`.

[R18] B. Huber and B. Sturmfels, “A polyhedral method for solving sparse polynomial systems,” DOI: `10.2307/2153370`; extended version arXiv:`alg-geom/9401001`, DOI: `10.1215/S0012-7094-96-08401-X`.

[R19] P. Breiding and S. Timme, “HomotopyContinuation.jl,” DOI: `10.1007/978-3-319-96418-8_54`, arXiv:`1711.10911`.

[R20] P. Lairez, “A deterministic algorithm to compute approximate roots of polynomial systems in polynomial average time,” DOI: `10.1007/S10208-016-9319-7`, arXiv:`1507.05485`.

[R21] P. Lairez, “Rigid continuation paths I: quasilinear average complexity for solving polynomial systems,” arXiv:`1711.03420`.

[R22] D. Bates, A. Sommese, J. Hauenstein, and C. Wampler, *Numerically Solving Polynomial Systems with Bertini*, DOI: `10.1137/1.9781611972702`.

[R23] J. Otto, A. Forbes, and J. Verschelde, “Solving polynomial systems with phcpy,” arXiv:`1907.00096`.

[R24] S. Basu, R. Pollack, and M.-F. Roy, *Algorithms in Real Algebraic Geometry*, DOI: `10.1007/978-3-662-05355-3`.

[R25] J. Draisma, E. Horobeţ, G. Ottaviani, B. Sturmfels, and R. Thomas, “The Euclidean distance degree of an algebraic variety,” DOI: `10.1007/s10208-014-9240-x`.

[R26] J. Hauenstein, J. Rodriguez, and B. Sturmfels, “Critical points via monodromy and local methods,” DOI: `10.1016/j.jsc.2016.07.019`.

[R27] C. Hillar and L.-H. Lim, “Most tensor problems are NP-hard,” DOI: `10.1145/2512329`, arXiv:`0911.1393`.

[R28] H. M. Möller and H. J. Stetter, “Multivariate polynomial equations with multiple zeros solved by matrix eigenproblems,” DOI: `10.1007/s002110050122`.

[R29] B. Mourrain and P. Trébuchet, “Stable normal forms for polynomial system solving,” arXiv:`0812.0067`.

[R30] R. La Scala and M. Stillman, “Strategies for computing minimal free resolutions,” DOI: `10.1006/jsco.1998.0221`.

[R31] V. Neiger et al., “Computing syzygies in finite dimension using fast linear algebra,” DOI: `10.1016/j.jco.2020.101502`.

[R32] A. Schmidhuber and S. Lloyd, “Complexity-theoretic limitations on quantum algorithms for topological data analysis,” DOI: `10.1103/PRXQuantum.4.040349`, arXiv:`2209.14286`.

[R33] S. Lloyd, S. Garnerone, and P. Zanardi, “Quantum algorithms for topological and geometric analysis of data,” DOI: `10.1038/ncomms10138`, arXiv:`1408.3106`.

[R34] J. Håstad, “Tensor rank is NP-complete,” DOI: `10.1016/0196-6774(90)90014-6`.

[R35] V. de Silva and L.-H. Lim, “Tensor rank and the ill-posedness of the best low-rank approximation problem,” DOI: `10.1137/06066518X`, arXiv:`math/0607647`.

[R36] A. Bernardi, N. Daleo, J. Hauenstein, and B. Mourrain, “Tensor decomposition and homotopy continuation,” DOI: `10.1016/j.difgeo.2017.07.009`, arXiv:`1512.04312`.

[R37] F. Catanese, S. Hoşten, A. Khetan, and B. Sturmfels, “The maximum likelihood degree,” DOI: `10.1353/ajm.2006.0019`, arXiv:`math/0406533`.

[R38] S. Hoşten, A. Khetan, and B. Sturmfels, “Solving the likelihood equations,” DOI: `10.1007/s10208-004-0156-8`.

[R39] G. F. Cooper, “The computational complexity of probabilistic inference using Bayesian belief networks,” DOI: `10.1016/0004-3702(90)90060-D`.

[R40] E. Candès and B. Recht, “Exact matrix completion via convex optimization,” DOI: `10.1007/s10208-009-9045-5`, arXiv:`0805.4471`.

[R41] R. Keshavan, A. Montanari, and S. Oh, “Matrix completion from a few entries,” arXiv:`0901.3150`.

[R42] B. Vandereycken, “Low-rank matrix completion by Riemannian optimization,” DOI: `10.1137/110845768`.

[R43] M. Eisenberg-Nagy, M. Laurent, and A. Varvitsiotis, “Complexity of the positive semidefinite matrix completion problem with a rank constraint,” arXiv:`1203.6602`.

[R44] J. B. Lasserre, “Global optimization with polynomials and the problem of moments,” DOI: `10.1137/S1052623400366802`.

[R45] S. Sakaue, A. Takeda, S. Kim, and N. Ito, “Exact semidefinite programming relaxations with truncated moment matrix for binary polynomial optimization problems,” DOI: `10.1137/16M105544X`.

[R46] J. van Apeldoorn, A. Gilyén, S. Gribling, and R. de Wolf, “Quantum SDP-solvers: better upper and lower bounds,” DOI: `10.22331/q-2020-02-14-230`, arXiv:`1705.01843`.

[R47] A. Gilyén, Y. Su, G. H. Low, and N. Wiebe, “Quantum singular value transformation and beyond,” DOI: `10.1145/3313276.3316366`, arXiv:`1806.01838`.

[R48] A. Harrow, A. Hassidim, and S. Lloyd, “Quantum algorithm for linear systems of equations,” DOI: `10.1103/PhysRevLett.103.150502`.

[R49] E. Tang, “A quantum-inspired classical algorithm for recommendation systems,” DOI: `10.1145/3313276.3316310`, arXiv:`1807.04271`.

[R50] A. Gilyén, S. Lloyd, and E. Tang, “Quantum-inspired low-rank stochastic regression with logarithmic dependence on the dimension,” arXiv:`1811.04909`.

[R51] N.-H. Chia et al., “Sampling-based sublinear low-rank matrix arithmetic framework for dequantizing quantum machine learning,” DOI: `10.1145/3357713.3384314`.

[R52] J. Ding, V. Gheorghiu, A. Gilyén, S. Hallgren, and J. Li, “Limitations of the Macaulay matrix approach for using HHL to solve multivariate polynomial systems,” DOI: `10.22331/q-2023-07-26-1069`, arXiv:`2111.00405`.

[R53] Y.-A. Chen and X.-S. Gao, “Quantum algorithms for Boolean equation solving and quantum algebraic attack on cryptosystems,” DOI: `10.1007/s11424-020-0028-6`, arXiv:`1712.06239`.

[R54] S. Ubaru, J. Chen, and Y. Saad, “Fast estimation of \(\operatorname{tr}(f(A))\) via stochastic Lanczos quadrature,” DOI: `10.1137/16M1104974`.

[R55] R. Meyer, C. Musco, C. Musco, and D. Woodruff, “Hutch++: optimal stochastic trace estimation,” DOI: `10.1137/1.9781611976496.16`, arXiv:`2010.09649`.

[R56] E. Knill and R. Laflamme, “Power of one bit of quantum information,” DOI: `10.1103/PhysRevLett.81.5672`, arXiv:`quant-ph/9802037`.

[R57] E. Knill, R. Laflamme, and G. Milburn, “A scheme for efficient quantum computation with linear optics,” DOI: `10.1038/35051009`.

[R58] C. Hamilton et al., “Gaussian boson sampling,” DOI: `10.1103/PhysRevLett.119.170501`, arXiv:`1612.01199`.

[R59] C. K. Law, H. Pu, and N. P. Bigelow, “Quantum spins mixing in spinor Bose-Einstein condensates,” DOI: `10.1103/PhysRevLett.81.5257`, arXiv:`cond-mat/9807258`.

[R60] A. Childs, D. Gosset, and Z. Webb, “The Bose-Hubbard model is QMA-complete,” DOI: `10.4086/toc.2015.v011a020`.

[R61] U. Chabaud, M. Joseph, S. Mehraban, and A. Motamedi, “Bosonic quantum computational complexity,” DOI: `10.22331/q-2026-05-20-2110`, arXiv:`2410.04274`.

[R62] J.-C. Faugère, “FGb: a library for computing Gröbner bases,” DOI: `10.1007/978-3-642-15582-6_17`.

[R63] M. Stillman, “Computing in algebraic geometry and commutative algebra using Macaulay 2,” DOI: `10.1016/S0747-7171(03)00096-8`.