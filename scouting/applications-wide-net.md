# Applications scout, wide net (lane output, 2026-09-02)

Scope: application areas where a problem about polynomial ideals or varieties is the practical computational bottleneck, screened against the seed construction (`seed/analysis-2026-09-01/report.md`, treated here as an untrusted proposer document, not as established truth). Robotics is excluded by the brief; adjacent kinematics is §2.2. Nothing below is a claim for `claims/CLAIMS.md`. Two quantitative findings are marked LANE RESULT; both are reproducible from the formulas given inline (scripts were written to the session scratchpad only, not to the repo).

Notation follows the seed: `R = C[z_0..z_n]`, `H_N = sum_j a†(f_j) a(f_j)` on `R_N = Sym^N(C^{n+1})`, `ker H_N = (I_N)^perp` of dimension `HF_{R/I}(N)`, coherent state `|p>^{⊗N}` in the kernel iff `conj(p) in V(I)`. Cost is set by three factors: the normalised gap `Δ_N/α`, the overlap of a preparable state on the ground space, and readout.

---

## 1. Screening filters

Filters F1-F6 are what decide the scores in §2. F2, and Observations A and B, are new here.

### F1 — field

The construction is complex projective and its compression is `C`-linear algebra on `Sym^N(C^{n+1})`. Seed Conjecture 8.8 argues there is no compact `F_q` analogue: Macaulay duality survives over `F_q` via divided powers, but the amplitude encoding does not, because `F_q` does not embed in `C` as a field.

Independently, almost every applied question is about **real** or **positive** solutions: chemical steady states, power-flow operating points, Nash equilibria in a simplex, control certificates, statistical models. Complex Hilbert functions do not see the real locus. This filter alone moves most of §2 to "structurally interesting, practically off-target".

### F2 — codimension, not ambient dimension (LANE RESULT)

The seed's DQC1-style primitive returns `HF(N)/dim R_N` to additive `eps` at cost `~1/eps^2`, and the seed asserts this is informative for `codim V = O(1)` (Conjecture 8.7). The true scaling is exponential in the **codimension** and essentially flat in `n`. For a complete intersection of `c` quadrics in `P^n` at `N = n`, using `HF(N) = sum_i (-1)^i binom(c,i) binom(N-2i+n, n)`:

| n | c=1 | c=2 | c=4 | c=8 | c=16 |
|---|---|---|---|---|---|
| 20 | 0.756 | 0.566 | 0.305 | 0.0733 | 9.7e-4 |
| 40 | 0.753 | 0.564 | 0.311 | 0.0873 | 4.6e-3 |
| 80 | 0.752 | 0.563 | 0.314 | 0.0939 | 7.2e-3 |

The ratio behaves like `rho^c` with `rho ~ 0.75` at `N = n`, and is independent of `n` to three digits. So the normalised Hilbert function is `>= 1/poly(n)` exactly when `codim V = O(log n)`. This sharpens seed Conjecture 8.7 from `O(1)` to `O(log n)`, but it does not soften the operative conclusion: **every square system (zero-dimensional variety, `codim = n`) is out of reach of this primitive**, and square systems are what nearly every application in §2 solves.

The same computation settles Hodge theory (§2.16e). Griffiths' residue theorem (DOI 10.2307/1970746) gives, for a smooth hypersurface `X = V(f) subset P^n` of degree `d` with Jacobian ideal `J = (∂_0 f, .., ∂_n f)`,

`h^{n-1-q,q}_prim(X) = HF_{R/J}((q+1)d - n - 1)`,

so Hodge numbers are literally ground-state degeneracies of the seed Hamiltonian built from the partials of `f`. Check on the quintic threefold (`n=4, d=5, q=1, N=5`, Fermat, so `J = (z_j^4)`): the degree-5 monomials in 5 variables with all exponents `<= 3` number `126 - 25 = 101 = h^{2,1}`. But the **normalised** value decays exponentially. Taking the middle Hodge degree `q = floor((n-1)/2)` with Fermat `J`, so `HF_{R/J}(N) = sum_i (-1)^i binom(n+1,i) binom(N-i(d-1)+n, n)`, over `n = 6..40`:

| family | best exponential fit | R^2 | best power fit | R^2 |
|---|---|---|---|---|
| cubics `d=3` | `exp(-0.249 n)` | 1.000 | `n^-4.6` | 0.927 |
| quartics `d=4` | `exp(-0.279 n)` | 1.000 | `n^-5.1` | 0.932 |
| quintics `d=5` | `exp(-0.288 n)` | 1.000 | `n^-5.3` | 0.933 |
| Calabi-Yau `d=n+1` | `exp(-0.299 n)` | 1.000 | `n^-3.4` | 0.934 |

Reason: at the middle Hodge degree `N ~ n(d-2)/2`, the ratio `HF/dim R_N` is the probability that a uniform random composition of `N` into `n+1` parts has all parts `<= d-2`, a large-deviation event. **Hodge numbers via the normalised Hilbert function are exponentially expensive.**

### F3 — degree must grow with the number of variables

The register is `O(n log N)` qubits and `dim R_N = binom(N+n, n)`. If the relevant degree `N` is bounded, `dim R_N` is polynomial in `n` and classical linear algebra on the Macaulay matrix wins up to polynomial factors: there is nothing to compress. Exponential compression needs `N = Theta(n)` or more. The only areas where the relevant degree grows linearly in the number of variables are Boolean and combinatorial ideals (§2.12), algebraic cryptanalysis at the degree of regularity (§2.8), and Artinian ideals with growing socle degree (§2.16). Everywhere else `N` is a small constant.

### F4 — readout

Roots are Grover-limited (seed Conjecture 8.6: the coherent-state superposition over the hypercube has ground-space weight `D/2^n`, giving `sqrt(2^n/D)`; the maximally mixed state is worse than Grover). Only global linear-algebraic quantities are cheap: quotient norms, normalised dimensions, traces of products of projectors, Toeplitz traces. Any application whose deliverable is a **list of solutions** is out.

### F5 — gap and symmetry

We need `Δ_N/α >= 1/poly`. Fact 7.2: a quadric's gap grows with slope `4 d_min^2`, where `d_min` is the Bombieri-Weyl distance to the cones, so cones and near-cones are flat; applied systems are frequently near-degenerate by construction, which is exactly why homotopy-continuation practitioners track condition numbers.

Conversely, a large group symmetry (determinantal `GL x GL`, toric torus, permutation-symmetric statistical models) block-diagonalises `H_N` by Schur-Weyl or by the `A`-grading. That makes the Hamiltonian physically clean, but it usually also makes the classical problem easy (compare Anschuetz-Bauer-Kiani-Lloyd, Quantum 7, 1189 (2023), for permutation-invariant Hamiltonians at fixed local dimension). The interesting targets have low symmetry and sparse generators.

### F6 — hardware sectors

Only three ideal classes carry a natural heuristic device.

- *Multilinear generators across `n` blocks of `q` variables*, in multidegree `(1,..,1)`: one boson per site, i.e. dual-rail linear optics with post-selection (KLM, DOI 10.1038/35051009) or MBQC. Seed §3 shows this identification is exact, with no factorials. Cleanest hook in the memo.
- *Quadratic generators in few modes*: parametric and spin-mixing processes. The conic `z_0 z_1 - z_2^2` is exactly the Law-Pu-Bigelow spin-1 spinor-BEC Hamiltonian (DOI 10.1103/PhysRevLett.81.5257), whose ferromagnetic ground manifold has `2N+1` states, the Hilbert function of the conic. Already realised in the laboratory.
- *Monomial and binomial (toric) generators*: number-conserving multi-boson hopping. `H_N` is block diagonal with weighted graph Laplacians on the `A`-graded fibres (seed §7), i.e. Bose-Hubbard-like.

An ideal outside these three classes has no heuristic-hardware angle, only fault-tolerant QSVT.

### Observation A — the dual, point-set Hamiltonian

A one-line corollary of the seed that is not in it. Since `span{|conj(p)>^{⊗N} : p in V} = (I(V)_N)^perp`, for a finite set `X = {p_1..p_r} subset P^n` the positive operator

`G = sum_i |conj(p_i)>^{⊗N} <conj(p_i)|^{⊗N}`

has `ker G = I(X)_N` **exactly**: the vanishing ideal of a point set is a ground space, not an orthogonal complement. This does not contradict Fact 4.1 (no `k`-body parent for `I_N`), because each term is a product operator `⊗^N |p><p|`, not a `k`-body term. Its gap is the least nonzero eigenvalue of the coherent-state Gram matrix, i.e. the constant in a Marcinkiewicz-Zygmund sampling inequality for the kernel `(x·y)^N` on `X`.

This is the natural Hamiltonian for interpolation-flavoured applications: Guruswami-Sudan interpolation (§2.7), Prony and super-resolution (§2.14), approximate vanishing ideals (§2.11), design ideals (§2.3c). It costs `r` terms, so it needs polynomially many points or a structured sum; the Boolean hypercube of seed Conjecture 8.6 is the structured case already studied.

### Observation B — coherent-state energy as batch invariant evaluation

The seed's `<p^{⊗N}|H_N|p^{⊗N}> = sum_j (N!/(N-m_j)!) |f_j(conj(p))|^2` evaluates a weighted sum of squares of **all** generators at a point, at a cost set by the block encoding of `H_N` rather than by the number of generators `d`. Wherever an application has exponentially many low-degree invariants but a structured generating set (determinantal ideals, phylogenetic invariants, tensor-network varieties), this is a genuine primitive: "total invariant violation at a point".

The caveat is F5: the structure that makes `H_N` block-encodable is usually a symmetry that also gives the classical sum in closed form. Testing this trade-off on one concrete determinantal ideal is the cheapest experiment this memo suggests.

---

## 2. Areas

Score is 1-5: plausibility of a real speedup over the best-in-class classical method for the same problem.

### 2.1 Computer vision: minimal problems and Groebner-basis solvers — score 1

- *Polynomial problem.* Square systems from minimal RANSAC configurations: 5-point relative pose (10 solutions), 6-point focal length (15), P3P (4), 7-point fundamental matrix (3), calibrated trifocal and point-line problems (up to 312, and 3040 for the hardest catalogued families).
- *Sizes that matter.* 3-30 unknowns; elimination templates (Macaulay matrices) of size `10^2`-`10^5`; wall-clock target microseconds, because RANSAC calls the solver `10^3`-`10^6` times per image pair.
- *Classical tool.* Automatic minimal-solver generators (DOI 10.1007/978-3-540-88690-7_23), syzygy-based reduction (DOI 10.1109/CVPR.2017.256), basis selection beyond Groebner bases (DOI 10.1109/cvpr.2018.00415); classification and Galois/monodromy decomposition of minimal problems (arXiv:1903.10008, arXiv:2105.04460, arXiv:1611.05947); learned start-solution selection for the hard cases (arXiv:2112.03424).
- *Gap / ground-state structure.* Zero-dimensional, `codim = n`, constant degree. Fails F2 and F3 outright.
- *Quantum angle.* The seed's Stickelberger direction (§5.4) applies formally, but its whole point is that the solution count `D` can be exponential while the register stays small; here `D <= 3040` and the classical dense eigendecomposition takes milliseconds.
- *Hardware angle.* None: the ideals are neither multilinear across blocks nor toric.
- *Justification.* Both the register compression and the readout advantage are empty at these sizes, against a microsecond classical target.

### 2.2 Kinematics of mechanisms outside robotics — score 1

- *Polynomial problem.* Loop closure and mechanism synthesis. Protein backbone tripeptide loop closure is algebraically the 6R serial-chain inverse-kinematics problem, degree 16 (DOI 10.1002/jcc.10416; resultant formulation DOI 10.1002/qua.20751). Also Burmester-type synthesis of four-bar and Stephenson linkages, and molecular ring closure in conformational search.
- *Sizes.* 3-16 unknowns, 16 to `10^4` solutions, called millions of times inside sampling loops.
- *Classical tool.* Dixon and Sylvester resultants; numerical homotopy (HomotopyContinuation.jl arXiv:1711.10911, Bertini).
- *Gap structure, quantum angle, hardware.* As §2.1: zero-dimensional at constant degree, nothing to compress, no hardware sector.
- *Justification.* Recorded to note that the seed's structure does not improve on microsecond root solving even where the algebra is elegant.

### 2.3 Algebraic statistics — score 2 overall (3 for phylogenetics alone)

**(a) ML degree and likelihood equations — 1.**
- *Problem.* The ML degree counts critical points of the likelihood function on a variety (math/0406533; topological characterisation arXiv:1207.0553; practice DOI 10.1007/s10208-004-0156-8; the same equations arise as scattering amplitudes, arXiv:2012.05041).
- *Sizes.* 10-100 parameters; ML degrees up to `10^5`-`10^6` for small models.
- *Classical tool.* Monodromy-driven numerical homotopy with certification.
- *Verdict.* Zero-dimensional, and the answer wanted is the real and positive critical points. Fails F1, F2, F4.

**(b) Phylogenetic invariants — 3.**
- *Problem.* The general Markov model on a `k`-taxon tree is a variety of dimension `O(k)` inside `(C^4)^{⊗k}`, ambient dimension `4^k` (math/0410604; tree tensor-network equations arXiv:2608.19071; dimension results arXiv:2101.03148). Practical question: model selection — given an empirical distribution `p_hat`, which topology is it closest to, judged by evaluating invariants.
- *Sizes.* `k = 4` in classical quartet methods; `k = 10-20` would be scientifically valuable, and `4^k = 10^6`-`10^12` there.
- *Classical tool.* Evaluate a hand-chosen set of `3x3` flattening minors, or run full likelihood by EM.
- *Gap structure.* The one classical area with a genuinely exponential ambient space, a low-degree structured generating set, and a distance-to-variety question.
- *Quantum angle.* Observation B makes the total invariant violation over all flattening minors a single coherent-state energy. Failure mode: `p_hat` is classical data, so preparing `|p_hat>^{⊗N}` is amplitude encoding of a `4^k`-vector — the input-model objection that kills most quantum linear algebra. It is a real primitive only if the state is produced physically, which is the bridge to §2.15.
- *Hardware angle.* The model lives in a multigraded tensor space, so a dual-rail encoding of the `(1,..,1)` sector is natural. But the invariants are not multilinear (minors have multidegree `(3,3,..)`), so the exact projector identification of seed §3 does not apply and the terms are genuine multi-boson interactions.

**(c) Graphical and Gaussian models, design ideals — 1.**
- *Problem.* Conditional-independence ideals of Gaussian Bayesian networks (arXiv:0704.0918); vanishing ideals of experimental designs.
- *Sizes.* 10-100 variables at degree 2-3, so `dim R_N` is polynomial (F3).
- *Verdict.* Observation A is the right encoding for design ideals and buys nothing at these sizes.

### 2.4 Chemistry and materials — score 1

- *Polynomial problem.* Molecular distance geometry (realise a partial distance matrix in `R^3`, arXiv:1205.0349); conformation spaces of cyclic molecules cut out by bond-length and bond-angle equations; crystal-structure prediction; equilibrium geometries as critical points of a potential.
- *Sizes.* `10^2`-`10^5` atoms; `10^4` distance constraints.
- *Classical tool.* Not algebraic geometry: semidefinite relaxations, branch-and-prune for discretizable instances, stochastic global optimisation, molecular dynamics. Groebner bases appear only in the small ring-closure sub-problems of §2.2.
- *Gap structure.* The question is existence of a **real** embedding. Fails F1 at the first step.
- *Quantum angle.* Nothing from the seed. The credible quantum angle in this area is simulating the chemistry itself, which is a different programme.
- *Hardware angle.* None from the ideal side.

### 2.5 Systems biology: reaction networks and multistationarity — score 1

- *Polynomial problem.* For a mass-action chemical reaction network, decide whether the steady-state system admits more than one **positive** solution for some parameter values, and describe the parameter region (DOI 10.1137/S0036139904440278; arXiv:1608.03993).
- *Sizes.* 5-50 species, 10-100 reactions; the object is a parametric family, not a single ideal.
- *Classical tool.* Deficiency theory, injectivity and sign conditions on determinants, real-algebraic certificates, CAD or Groebner bases for small networks.
- *Gap structure.* Positivity is the entire question, and parametricity has no counterpart in the seed. Fails F1 decisively.
- *Quantum angle.* None. A serious attempt needs a real/positive analogue of the whole construction.
- *Hardware angle.* Worth recording as an oddity: steady states of complex-balanced networks are **binomial**, i.e. toric, which is precisely the Bose-Hubbard-friendly class of F6. A hardware hook attached to a question the construction cannot answer.

### 2.6 Power systems — score 2

- *Polynomial problem.* Power flow: `2m` real quadratic equations in `2m` unknowns for an `m`-bus grid, sparse with the network graph. The algebraically interesting questions are not "find one operating point" (Newton does that) but "how many solutions are there, where is the nearest one, how far is the operating point from voltage collapse" (survey arXiv:1510.00073; solution counts versus topology DOI 10.1109/tpwrs.2017.2724030; monodromy arXiv:2011.14977; number of real solutions arXiv:2010.03069; Kuramoto analogue arXiv:1708.09246).
- *Sizes.* Real grids `m = 10^3`-`7x10^4` buses. Exhaustive solution counting by polyhedral homotopy with an adjacency-polytope-tailored start system reaches `m <= 20-40`.
- *Classical tool.* Newton-Raphson and continuation for operating points; polyhedral homotopy for exhaustive counts; monodromy for partial counts.
- *Gap structure.* Square and zero-dimensional (`codim = 2m`); the solution count grows exponentially, so the normalised Hilbert function is exponentially small (F2), and the wanted solutions are real with one distinguished (F1, F4).
- *Quantum angle.* Weak. The one favourable feature is that the generators are sparse graph-structured quadrics, so `H_N` is a genuinely sparse, physically natural operator; but every question actually asked has the wrong shape.
- *Hardware angle.* Best fit in the classical half of the memo: sparse quadratic generators over `2m` modes give a number-conserving extended Bose-Hubbard Hamiltonian on the network graph, whose ground-space degeneracy for a small network is the Hilbert function. That is a demonstration, not a speedup.

### 2.7 Coding theory — score 1

- *Polynomial problem.* List decoding of Reed-Solomon and algebraic-geometry codes: interpolate `Q(x,y)` vanishing to multiplicity `m` at `n` points under a weighted-degree bound, then factor (DOI 10.1109/18.782097); decoding AG codes via Riemann-Roch spaces; syndrome decoding via Groebner bases of error-locator ideals.
- *Sizes.* `n = 255`-`10^5` code positions; interpolation matrices `10^3`-`10^6`; target throughput Gbit/s in hardware.
- *Classical tool.* Berlekamp-Massey, Koetter iterative interpolation, structured (Hankel and displacement-rank) linear algebra at quasi-linear cost.
- *Gap structure.* The interpolation step is exactly Observation A: the kernel of a sum of jets of coherent-state projectors at the code positions is the vanishing ideal of a fat-point scheme, hence a ground space. A pretty match.
- *Quantum angle.* Destroyed by F1 (the points live in `F_q`) and by the fact that the classical algorithm is already quasi-linear.
- *Hardware angle.* None.

### 2.8 Multivariate cryptography and algebraic attacks — score 2

- *Polynomial problem.* Solve `m` quadratic equations in `n` variables over `F_2` or `F_q` (the MQ problem): key recovery for UOV/HFE-type signature schemes, MinRank attacks, algebraic attacks on stream and block ciphers via low-degree annihilators.
- *Sizes.* The one area where astronomically large Macaulay matrices are actually built. `n = 60`-`160` variables for MQ challenges; the degree of regularity `d_reg` grows linearly in `n` for semi-regular systems, so the Macaulay matrix at `d_reg` has `binom(n+d_reg, d_reg)` columns, routinely `10^7`-`10^{10}`. Recent breaks: Rainbow (IACR ePrint 2022/214), UOV/Rainbow improvements (ePrint 2020/1343), crossbred (ePrint 2017/372).
- *Classical tool.* F4 and F5 (DOI 10.1016/S0022-4049(99)00005-5, DOI 10.1145/780506.780516), XL and crossbred, complexity governed by `d_reg` (arXiv:1312.1655); sparse `F_2` linear algebra (Wiedemann, block Lanczos).
- *Gap structure.* Structurally the **best** fit in the memo: the bottleneck is literally the rank and kernel of a Macaulay matrix at a degree growing linearly in the number of variables, which is exactly F3's requirement and exactly the seed's `Phi_N`. The seed's Boolean encoding over `C` (§6) even reproduces the counting version, `HF_{R/K}(N) = #SAT` for `N >= n+3`.
- *Quantum angle.* Blocked twice. (i) F1: seed Conjecture 8.8. (ii) The `C`-lift route is Grover-limited — seed Conjecture 8.6 gives ground-space weight `D/2^n` and cost `sqrt(2^n/D)`, matching known quantum MQ results (arXiv:1712.07211); the Chen-Gao HHL-on-Macaulay line meets the same fate via the condition-number obstruction (Ding-Gheorghiu-Gilyen-Hallgren-Li, Quantum 7, 1069 (2023)).
- *Hardware angle.* The Boolean part is monomial-plus-binomial, hence toric-adjacent and Bose-Hubbard-implementable in principle; the clause cubics are not.
- *Justification.* Best structural match with two independent known obstructions. Keeping it on the list defines the bar any speedup claim in this campaign must clear.

### 2.9 Control theory — score 1

- *Polynomial problem.* Stability and performance certificates: nonnegativity of a polynomial Lyapunov function on a semialgebraic set; static output feedback; polynomial matrix equations for `H_infinity` design.
- *Sizes.* State dimension 5-100; SOS relaxations of order 2-4 give SDPs with `10^3`-`10^6` variables.
- *Classical tool.* Lasserre-Parrilo sums-of-squares hierarchies (DOI 10.1137/S1052623400366802, DOI 10.1007/s10107-003-0387-5) solved by interior-point SDP.
- *Gap structure.* Real and semialgebraic. Moment matrices and catalecticants are close cousins of `H_N` (both are Gram matrices of the apolarity pairing), but the question is positivity, not dimension. Fails F1.
- *Quantum angle.* Not from the seed. The credible angle is quantum SDP solvers on the Lasserre hierarchy (arXiv:1609.05537, arXiv:1804.05058), whose speedups sit in the wrong regime for these SDPs: they want many constraints and low rank, and pay heavily in `1/eps` and in the trace bounds. Kept as a contrast case.
- *Hardware angle.* None.

### 2.10 Economics: Nash equilibria as polynomial systems — score 2

- *Polynomial problem.* Totally mixed Nash equilibria of an `n`-player, `q`-strategy game solve a **multilinear** system: each player's indifference conditions are linear in every other player's mixed strategy (maximal counts DOI 10.1006/jeth.1996.2214; universality of Nash equilibria as real algebraic sets DOI 10.1287/moor.28.3.424.16397).
- *Sizes.* Full payoff tensors have `n q^n` entries, so only succinct games are interesting: graphical and polymatrix games with bounded neighbourhood, `n = 10^2`-`10^4` players.
- *Classical tool.* Lemke-Howson for two players, homotopy and simplicial methods, support enumeration. PPAD-complete, so nobody expects polynomial time.
- *Gap structure.* Exactly the seed's multigraded setting: variables `z_{i,s}`, sites `i = 1..n`, levels `s = 0..q-1`, multidegree `(1,..,1)`, multilinear generators, and `V(I) subset (P^{q-1})^n` the totally mixed equilibria in complex projective coordinates. The Hamiltonian is a sum of local rank-one projectors, i.e. a quantum `k`-SAT instance; for a graphical game with bounded neighbourhood it is genuinely `k`-local.
- *Quantum angle.* The existence question maps onto product-state QSAT, QMA_1-hard for `k >= 3`, so no speedup on the decision problem. Less obviously hopeless is counting: the maximal number of regular totally mixed equilibria is a BKK/mixed-volume quantity for a multilinear system, and the number of equilibria is the Hilbert function of the multigraded ideal in the stabilised multidegree. It fails F1 in the end, since only real equilibria in the simplex are economically meaningful.
- *Hardware angle.* Among the best in the memo: one photon per player in dual-rail encoding, multilinear constraints as post-selected linear-optical projectors. Separately, BKK counts for multilinear systems are permanent-like, and Gaussian boson sampling natively produces permanents and hafnians (arXiv:1011.3245), suggesting a heuristic sampler for equilibrium counts. I found no prior art for that link [UNVERIFIED].

### 2.11 Tensor decomposition and machine learning — score 2

- *Polynomial problem.* Border rank and membership in secant varieties of Segre and Veronese varieties, and identifiability of decompositions (arXiv:1609.00123); best rank-`r` approximation; critical points of neural-network loss landscapes as polynomial systems (arXiv:1810.07716) and the geometry of linear-network function spaces (arXiv:1910.01671); approximate vanishing ideals of data (DOI 10.1016/j.jsc.2008.11.010; Vanishing Component Analysis, Livni et al. 2013 [UNVERIFIED, PMLR, no DOI located]).
- *Sizes.* Tensors from `30^3` to `10^3` cubed; networks with `10^6`-`10^9` parameters; VCA on `10^3`-`10^5` features at degree 2-4.
- *Classical tool.* ALS and Riemannian optimisation for decompositions; flattening and catalecticant ranks for identifiability certificates; SVD wherever there is matrix structure. Most tensor decision problems are NP-hard (arXiv:0911.1393), so practice is local.
- *Gap structure.* Two mismatches. First, the applied question is the distance from a **point** (the data tensor) to a variety, whereas the seed's estimable `delta(f)^2 = <f|P_0|f>/||f||^2` is the distance from a **form** to an ideal, a quotient norm in `(R/I)_N`; point-to-variety distance in the seed's framework is the coherent-state energy, i.e. evaluation of the equations, classically trivial once the generators are known. Second, at fixed degree, catalecticant and flattening matrices are polynomial-sized (F3).
- *Quantum angle.* The one non-trivial version is quantum-native: if the tensor is a state of `k` qudits rather than a classical array, the ambient dimension is `q^k` and "distance to the `r`-th secant of the Segre" is an entanglement measure. See §2.15(iii).
- *Hardware angle.* Only through that quantum-native version.

### 2.12 Combinatorial optimization via Boolean ideals — score 2

- *Polynomial problem.* Encode combinatorial infeasibility (graph `k`-colourability, SAT, stable sets) as a polynomial system and search for a bounded-degree Nullstellensatz certificate; the certificate degree is the parameter of interest (arXiv:0801.3788, arXiv:0706.0578). Separately, Hilbert series of squarefree monomial (Stanley-Reisner) ideals count independent sets and are `#P`-hard to evaluate (DOI 10.1142/s0218196711006819).
- *Sizes.* `n = 10^2`-`10^3` variables; the NulLA linear system at certificate degree `d` has `binom(n+d,d)` columns, `10^6`-`10^9` at `d = 3-4`.
- *Classical tool.* Sparse `F_2` or `Q` linear algebra on the Macaulay matrix. In practice SAT solvers beat the algebraic route badly on satisfiable instances.
- *Gap structure.* The seed's own anchor (§6): the Boolean ideal `(z_i^2 - z_i z_0)` is a radical saturated complete intersection with `HF = 2^n` from `N = n`, and adjoining clause cubics gives `HF_{R/K}(N) = #SAT` for `N >= n+3`. The degree grows linearly in `n` (F3 satisfied) and the ambient dimension is `binom(2n+3,n) ~ 4^n`, so the compression is genuinely exponential. The gap looks benign numerically (`Delta` in `[0.29, 2.3]` over 54 instances, `n = 3..8`).
- *Quantum angle.* Bounded by the seed's own analysis: exact `HF` gives `#P subset FBQP`, multiplicative approximation gives `NP subset BQP`, and the normalised additive version has `HF/dim R_N ~ D 4^{-n}`, consistent with F2 since `codim = n`. Root sampling reaches Grover scaling and no better. Correct structure, no speedup.
- *Hardware angle.* The Boolean part is toric-adjacent; the clause part is a three-boson interaction. A small analogue realisation would demonstrate the `HF = #SAT` identity at `n = 3-4`.

### 2.13 Geometric modelling and CAD — score 1

- *Polynomial problem.* Implicitization of rational parametric surfaces, surface-surface intersection, offsets and blends, self-intersection detection.
- *Sizes.* 2-4 variables, degrees 3-12, but called on `10^4`-`10^6` patches per model.
- *Classical tool.* Moving curves and surfaces / mu-bases (DOI 10.1145/218380.218460), resultants, subdivision with interval arithmetic. The syzygy computations here are small and heavily optimised.
- *Gap structure.* Two to four variables means no compression at all (F3).
- *Quantum angle, hardware angle.* None.

### 2.14 Signal processing: Prony, super-resolution, Hankel varieties — score 1

- *Polynomial problem.* Recover `r` frequencies from `n` samples: the kernel of a Hankel (Prony) matrix is the ideal of the frequency points, so the classical algorithms are kernel computations for the vanishing ideal of a point set on the torus (ESPRIT DOI 10.1109/29.32276; resolution limits and convex relaxation arXiv:1203.5871).
- *Sizes.* `r = 10`-`10^3` frequencies, `n = 10^2`-`10^5` samples; multidimensional versions have 2-4 variables.
- *Classical tool.* ESPRIT, matrix pencil, MUSIC — an SVD of a Hankel matrix; total-variation minimisation in the super-resolution regime.
- *Gap structure.* Observation A is precisely the Prony structure, and its gap is the conditioning that the super-resolution literature already studies (the minimum-separation condition). An exact dictionary entry worth recording.
- *Quantum angle.* None: 1-4 variables means `dim R_N` is small (F3) and the classical method is an SVD.
- *Hardware angle.* The one-mode case is literally a bosonic Hamiltonian, so an analogue demonstration is trivially available and equally uninformative.

### 2.15 Quantum information itself — score 4 (with the caveat stated below)

All variants have the input already in quantum form, which is the only way to escape the amplitude-encoding objection that blocks §2.3(b) and §2.11.

- *(i) Product-state satisfiability.* Seed §3: every quantum `k`-SAT instance is the multidegree-`(1,..,1)` block of an ideal generated by `k`-multilinear forms; product-state solutions are the points of `V(I) subset (P^{q-1})^n`, and the remaining ground states are the entangled part of the inverse system. Sizes `n = 10`-`10^2` qudits, `q = 2`-`5`. Classical tool: Bravyi's algorithm for `q=2,k=2` (quant-ph/0602108), dimension-counting heuristics, SDP relaxations. QMA_1-complete for `k=3,q=2` (arXiv:1302.0290) and already for bilinear forms across blocks of sizes `(2,5)` (arXiv:2401.02368).
- *(ii) Bosonic QSAT.* Seed Proposition 8.2: the symmetric-sector analogue is QMA_1-hard via hard-core generators, so the seed's own family is as complexity-theoretically rich as QSAT.
- *(iii) Entanglement classification and secant varieties.* Orbit closures and secants of Segre and Veronese varieties classify entanglement types (DOI 10.1103/PhysRevA.65.052112 for four qubits; catalecticant methods for symmetric states, Sanz-Braak-Solano-Egusquiza, J. Phys. A 50, 195303 (2017) [UNVERIFIED]). The data point is a state, the ambient dimension is `2^k`, and the equations (flattening and Strassen-type minors) are low degree. Observation B turns the total invariant violation into a single energy measurement: an experimental witness for "distance to border rank `r`" costing one Hamiltonian expectation value in place of exponentially many invariant evaluations.
- *(iv) Tensor-network varieties.* Matrix-product and tree-tensor-network states form varieties whose equations are being worked out (arXiv:2101.03148, arXiv:2608.19071); the same primitive applies, and the phylogenetic models of §2.3(b) are the classical-statistics image of the same objects.
- *(v) Spinor-BEC analogue realisation.* Seed §3: the conic ideal's Hamiltonian is Law-Pu-Bigelow spin mixing, whose ferromagnetic manifold already realises the Hilbert function `2N+1` experimentally. Extending to two generators (four or five modes) is the smallest interesting experiment in this memo.
- *Gap structure.* Native, and inheriting every frustration-free pathology, including exponentially small gaps (seed 8.3(d) via Levine-Movassagh area-weighted Motzkin chains, arXiv:1611.03147). Gap promises must therefore be imposed, not proved.
- *Hardware angle.* Strongest in the memo: (i) and (iii) live in the `(1,..,1)` sector, i.e. dual-rail linear optics with post-selection plus the measurement-induced-nonlinearity toolbox; (v) is a running cold-atom experiment.
- *Honest caveat on the score.* No speedup over a classical algorithm is on offer: these problems are QMA-hard and the classical competitor is not a bottleneck anyone is trying to beat. What is on offer is (a) an exact new dictionary between commutative algebra and frustration-free Hamiltonians, yielding new **statements** about QSAT — the inverse-system description of the entangled part of the ground space, and the Hilbert function as the linear-algebra relaxation of product-state satisfiability — and (b) an analogue demonstration. Strictly read against the north star this is a 2; read as new algorithmic structure plus the required heuristic-hardware attack, it is a 4.

### 2.16 Serious algebraic geometry: where a Hamiltonian view might be genuinely new — score 3

**(a) Graded Betti numbers as a supersymmetric Koszul Laplacian — 3.**
- *Idea.* The seed stops at `H_N = Phi_N Phi_N^dagger` with `ker Phi_N = Syz(I)_N`. The continuation is the whole free resolution: add `d` fermionic modes to the `n+1` bosonic ones, take the Koszul differential `partial = sum_j a^dagger(f_j) ⊗ c_j` (or the Koszul complex on the variables acting on `R/I`), and form `partial partial^dagger + partial^dagger partial`. Its harmonic space in homological degree `i` and internal degree `N` is the Koszul homology; for the complex on the variables it is `Tor_i^R(R/I,k)_N`, i.e. the graded Betti numbers `beta_{i,N}`. Hodge theory for free resolutions, as a positive Hamiltonian on a boson-fermion Fock space with a gap parameter per homological degree.
- *Classical status and sizes.* Betti tables are a genuine bottleneck in commutative algebra (Macaulay2, Singular); Boij-Soderberg theory (arXiv:0712.1843) describes the cone of Betti tables but does not compute them, and worst cases are doubly exponential (alg-geom/9304003; DOI 10.1016/0001-8708(82)90048-2). Sizes that matter: `n = 10`-`40` variables, resolutions with `10^3`-`10^6` syzygies.
- *Honest angle.* F2 applies to reading `beta_{i,N}` off as a normalised dimension, so the likely product is a theorem, not a speedup. Untouched by the seed; most attractive "new statement" direction in the memo.

**(b) A metric Castelnuovo-Mumford regularity — 3.**
- *Idea.* `Delta_N` is a quantitative syzygy constant: how close a non-syzygy can come to being one. Regularity is the degree past which the Hilbert function is polynomial and the resolution linear; the seed's numerics show `Delta_N` stabilising or growing linearly past a small degree in every family tested. Define spectral regularity as the least `N_0` with `inf_{N >= N_0} Delta_N/alpha >= c`, and relate it to `reg(I)`.
- *Status.* Well posed and apparently new; it is seed Conjecture 8.3(a)/(e) restated as geometry rather than as a promise, and it is the prerequisite for every runtime claim in seed §5.

**(c) Intersection theory from overlaps — 3.**
- *Idea.* Seed Conjecture 8.10: `Tr(P_I P_J)` grows like `N^{dim(V cap W)}` with leading coefficient a positive combination of the degrees of the components of `V cap W`, and decays like `cos^{2N}` of the Fubini-Study distance when the varieties are disjoint. An analytic avatar of intersection theory needing neither `I + J` nor elimination, DQC1-estimable in normalised form.
- *Limits.* Exact enumerative counts are blocked by F4 (additive precision below 1). But "do these two varieties meet, and in what dimension" for low-codimension varieties in many variables is a real question with no cheap classical answer.

**(d) Hilbert schemes and Berry holonomy — 2.**
- *Idea.* A flat family is a path of Hamiltonians with constant kernel dimension; a Groebner degeneration is a path to a torus-fixed point of the Hilbert scheme. The seed's adiabatic Groebner deformation (§5.5, Conjecture 8.4) transports standard monomials to a basis of `(R/I)_N`, differing from a canonical basis by the non-abelian holonomy of the ground-space bundle. A Berry connection on the Hilbert scheme whose curvature is a new invariant of the family is a genuinely physicist's object, and I found no prior art.
- *Warning.* Whether it computes anything is open; Vakil's Murphy's-law results (math/0411469) say the base can be arbitrarily bad.

**(e) Hodge numbers — 1 for computation, retain as a dictionary entry.**
- Griffiths makes them ground-state degeneracies of the Jacobian-ideal Hamiltonian (statement and the `h^{2,1} = 101` quintic check are in F2); the Landau-Ginzburg chiral-ring version of this is standard in physics, so the dictionary is new only in the Macaulay-dual, positive-Hamiltonian form.
- LANE RESULT: the normalised Hilbert function at the middle Hodge degree decays like `exp(-0.25 n)` to `exp(-0.30 n)` with `R^2 = 1.000`, so the DQC1 route is exponentially expensive. Worse, for smooth hypersurfaces the Jacobian ideal is a complete intersection with a closed-form Hilbert series, so there is no computational content there at all; any content is in singular hypersurfaces and non-complete-intersection varieties. Periods (arXiv:1803.08068, arXiv:1404.5069) are a harder object the construction does not reach.

**(f) Moduli and enumerative geometry generally — 1.**
- No foothold beyond (c) and (d): Gromov-Witten and Donaldson-Thomas invariants are not Hilbert functions of an explicitly generated ideal in a fixed polynomial ring, so the construction does not apply without a new idea.

---

## 3. Cautions recorded by this lane

1. **Codimension law (LANE RESULT).** `HF(N)/dim R_N ~ rho^{codim}` with `rho ~ 0.75` at `N = n`, essentially independent of `n`. Sharpens seed Conjecture 8.7 to `codim = O(log n)` and rules the DQC1 primitive out for every square system.
2. **Hodge numbers (LANE RESULT).** Exponential decay `exp(-0.25 n)` to `exp(-0.30 n)` of the normalised Hilbert function at the middle Hodge degree, `R^2 = 1.000` versus `0.93` for the best power law. The attractive "Hodge numbers as ground-state degeneracies" route is closed by the normalisation, not by the algebra.
3. **Point-to-variety versus form-to-ideal.** The seed's estimable distance is a quotient norm in `(R/I)_N`, not the distance from a data point to `V`. Tensor decomposition, phylogenetic model selection and vision fitting all ask the latter, which in the seed's framework is the coherent-state energy, i.e. classical evaluation of the equations. Confusing the two is the easiest route to a false application claim.
4. **Symmetry cuts both ways.** Ideals whose `H_N` is cheaply block-encodable (determinantal, toric, permutation-symmetric) are usually those whose classical Hilbert functions are also known in closed form.
5. **Input model.** Any classical application needing `|p_hat>` for a `4^k`- or `2^k`-dimensional classical data vector is blocked at amplitude encoding. Only quantum-native inputs (§2.15) escape it.

---

## Ranked shortlist

1. **Quantum information itself: multigraded QSAT, entanglement and tensor-network varieties (4).** The only area where the input is already quantum, the structural identification is exact (seed §3, Prop 8.2), the hardware hook is native (dual-rail linear optics for the `(1,..,1)` sector; running spinor-BEC experiments for the conic), and the deliverables are new statements about QSAT ground spaces rather than a contested speedup. Concrete next object: the inverse-system description of the entangled part of a QSAT ground space, plus Observation B as a border-rank witness.
2. **Graded Betti numbers as a supersymmetric Koszul Laplacian (3).** Untouched by the seed, a genuinely new physicist's formulation of free resolutions, aimed at a real classical bottleneck, with its own gap parameter per homological degree. Likely product is a theorem, not a speedup.
3. **Spectral regularity: `Delta_N` as a metric Castelnuovo-Mumford invariant (3).** Recasts seed Conjecture 8.3(a)/(e) as a geometric question with a chance of a clean answer, and is the prerequisite for every runtime claim in seed §5.
4. **Intersection dimension and Fubini-Study distance from `Tr(P_I P_J)` (3).** The only enumerative-flavoured primitive that survives F2 and F4, answering a real question for low-codimension varieties without elimination.
5. **Algebraic statistics: phylogenetic and tree-tensor-network varieties (3).** The only classical application area with a genuinely exponential ambient space (`4^k`), a low-degree structured generating set and a distance-to-variety question. Blocked at the input model unless the data state is produced physically, which is exactly the bridge to entry 1.
6. **Multivariate cryptography and algebraic attacks (2).** Best structural match to the Macaulay-matrix bottleneck in the whole memo, with the degree of regularity playing the role of `N` and `10^7`-`10^{10}`-column matrices actually built. Two independent known obstructions (finite field; Grover and condition number). Keep it on the list because it defines the bar.
7. **Combinatorial optimization via Boolean ideals (2).** The seed's own anchor; satisfies F3 with exponential compression; conclusively Grover-limited by the seed's own analysis. Value is as a calibration instance, and as the smallest `HF = #SAT` system an analogue device could demonstrate.
8. **Economics: graphical games as multilinear multigraded ideals (2).** Exact fit to the seed's multigraded setting, native dual-rail hardware hook, and a speculative but checkable link between BKK counts of multilinear systems and permanents produced by boson sampling. Fails F1 in the end, since only real simplex equilibria matter.

Everything else scored 1: computer vision minimal problems, kinematics outside robotics, chemistry and materials, systems biology, coding theory, control theory, geometric modelling, signal processing, and the computational (as opposed to dictionary) reading of Hodge theory. Power systems (2) and tensor/ML (2) narrowly miss the list; power systems is the best analogue-demonstration target among classical applications.

## Questions for TJO

1. **Real versus complex.** Every classical area in §2.4-2.6, §2.9 and §2.10 asks a real or positive question, and the construction is complex projective. Do we open a lane on a real/positive analogue (the moment-and-SOS side, or a Hamiltonian whose ground space sees the real points), or accept that the applications half of the north star is effectively restricted to complex questions and quantum-native inputs? This is the largest scoping decision in the memo.
2. **Finite fields.** Seed Conjecture 8.8 declares that direction closed. It is also the only direction where astronomically large Macaulay matrices are in real use (§2.8). Do we treat 8.8 as settled, or fund one bounded attempt at a divided-power / `q`-deformed Fock model before writing cryptanalysis off?
3. **What counts as the product.** Shortlist entries 2-4 are new mathematical statements (a SUSY Laplacian for Betti numbers, a metric regularity, an analytic intersection theory), not speedups. The north star says "a real speedup", with BQP-completeness a bonus. Do new invariants and dictionary theorems count as deliverables in their own right, or only as instruments toward a speedup? Lane structure and the choice of critics differ.
4. **Is an analogue demonstration a product?** The smallest concrete experiment here is a two-generator extension of the existing spinor-BEC realisation (four or five modes), whose measured ground-state degeneracy would be a Hilbert function. It is not a speedup. In scope or not?
5. **Which area gets the second deep lane** (the treatment robotics is getting)? Recommendation: quantum-native varieties (shortlist 1, with 5 as its classical shadow), because it is the only place where the input model does not defeat the construction. If the campaign wants a classical application area at all costs, the alternative is algebraic statistics.
6. **Do Observations A and B get promoted?** Observation A (kernel of a sum of coherent-state projectors is the vanishing ideal of a point set, sidestepping Fact 4.1) and Observation B (coherent-state energy as batch evaluation of an exponentially large generating set) are one-line corollaries of the seed, but they are what place §2.3b, §2.7, §2.14 and §2.15(iii) where they are. Do they enter `definitions/` and `claims/CLAIMS.md` as CONJECTURE or SKETCH rows, or stay in scouting?
7. **Do the two lane numerics get ratcheted?** Both are negative results with clean numerics and short scripts; they constrain seed Conjecture 8.7 and close one advertised direction. Do you want them as weakened or REFUTED rows against 8.7, or left as scouting evidence for a checker lane to reproduce independently?

---

### Citation index

Every identifier below was resolved against the arXiv API or doi.org during this lane, except where marked [UNVERIFIED].

- Computer vision: DOI 10.1007/978-3-540-88690-7_23; DOI 10.1109/CVPR.2017.256; DOI 10.1109/cvpr.2018.00415; arXiv:1903.10008; arXiv:2105.04460; arXiv:2112.03424; arXiv:1611.05947.
- Kinematics: DOI 10.1002/jcc.10416; DOI 10.1002/qua.20751; arXiv:1711.10911.
- Algebraic statistics: math/0406533; arXiv:1207.0553; DOI 10.1007/s10208-004-0156-8; arXiv:2012.05041; math/0410604; arXiv:2101.03148; arXiv:2608.19071; arXiv:0704.0918; arXiv:0805.3602.
- Chemistry and biology: arXiv:1205.0349; DOI 10.1137/S0036139904440278; arXiv:1608.03993.
- Power systems: arXiv:1510.00073; DOI 10.1109/tpwrs.2017.2724030; arXiv:2011.14977; arXiv:2010.03069; arXiv:1708.09246.
- Coding theory: DOI 10.1109/18.782097.
- Cryptography: IACR ePrint 2022/214; ePrint 2020/1343; ePrint 2017/372; arXiv:1312.1655; DOI 10.1016/S0022-4049(99)00005-5; DOI 10.1145/780506.780516; arXiv:1712.07211.
- Control and SDP: DOI 10.1137/S1052623400366802; DOI 10.1007/s10107-003-0387-5; arXiv:1609.05537; arXiv:1804.05058.
- Economics: DOI 10.1006/jeth.1996.2214; DOI 10.1287/moor.28.3.424.16397; graphical games (Kearns-Littman-Singh) [UNVERIFIED].
- Tensors and machine learning: arXiv:1609.00123; arXiv:0911.1393; arXiv:1810.07716; arXiv:1910.01671; DOI 10.1016/j.jsc.2008.11.010; Vanishing Component Analysis (Livni et al. 2013) [UNVERIFIED].
- Combinatorial optimization: arXiv:0801.3788; arXiv:0706.0578; DOI 10.1142/s0218196711006819.
- Geometric modelling: DOI 10.1145/218380.218460.
- Signal processing: DOI 10.1109/29.32276; arXiv:1203.5871.
- Quantum information: quant-ph/0602108; arXiv:1302.0290; arXiv:2401.02368; arXiv:1611.03147; DOI 10.1103/PhysRevA.65.052112; DOI 10.1103/PhysRevLett.81.5257; DOI 10.1038/35051009; arXiv:1011.3245; Sanz-Braak-Solano-Egusquiza, J. Phys. A 50, 195303 (2017) [UNVERIFIED].
- Algebraic geometry: DOI 10.2307/1970746; alg-geom/9304003; DOI 10.1016/0001-8708(82)90048-2; arXiv:0712.1843; math/0411469; arXiv:1803.08068; arXiv:1404.5069.
- Complexity anchors quoted from the seed: Anschuetz-Bauer-Kiani-Lloyd, Quantum 7, 1189 (2023) [UNVERIFIED]; Ding-Gheorghiu-Gilyen-Hallgren-Li, Quantum 7, 1069 (2023) [UNVERIFIED]; Gharibian-Le Gall arXiv:2111.09079.
