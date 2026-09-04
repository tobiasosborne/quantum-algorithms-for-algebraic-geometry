# Round 2: original collective geometry

## Verdict

No north-star candidate survives this lane.

The strongest result derived here is a finite-copy normal form: a heralded pure-state operation on
`r` identical copies is a projective rational map of degree at most `r`, and a
degree-`r` map has an exact `r`-copy realization.  For coprime minimal coordinates,
`r` copies are necessary and the best success profile at that copy count is fixed by
the coefficient-operator norm.  This is an algebraic lower bound on quantum state
conversion, not a speedup.  Historical novelty is unverified because this round uses
no web or literature search.

Two more geometric operations were constructed and attacked:

1. chart-aligned occupation spectroscopy returns the multiplicity and tangent-cone
   state of a hypersurface at a coherently supplied point;
2. a fermionic regressive product returns the Plucker state of a transverse linear
   intersection.

The first has an exact single-copy measurement comparator and a conservative
`O(Sm^2+D)` exact-arithmetic baseline for its scalar multiplicity output.  The second is exterior multiplication (antisymmetric/Schur
projection) with an unavoidable binomial success denominator and is classically
tractable on its decomposable inputs.  Neither meets D22.

## 0. Scope, conventions, and access ledgers

This memo works in algebraic geometry broadly and does not use the Fock/Macaulay
ground-space construction.  It obeys definitions conventions C1--C12 when their
objects occur.  In particular, the point seen by a coefficient ket is conjugated as
specified below; no antiunitary is treated as a physical gate.

Let `H = C^D` and `K = C^E`, with their displayed orthonormal bases.  Input size is
not `log D` unless the data supplying an operation are also succinct.

Three access cases are kept separate.

- **Sparse classical coefficients:** all nonzero tensor entries are listed; `S` is
  the list length.  State preparation or compilation costs at least the cost of
  reading this list.
- **Preparation circuit:** a gate list for `U_x|0> = |x>` or `U_F|0> = |F>` is part
  of the input.  A quantum call to that circuit is not compared with a classical
  amplitude-array lookup.
- **Uncontrolled copies:** copies may be measured but do not provide `U`, `U^dag`,
  controlled preparation, or reflections (D-QN-PHYSICAL-DATA-ACCESS).

A classical copy-access comparator may choose adaptive single-copy measurements and
then post-process classically.  Full tomography is not the default comparator.

No use is made of Grover search, amplitude amplification, QFT, DQI, phase estimation,
QSVT, or a generic spectral filter.  Postselection probabilities are charged as
ordinary repetitions.

## 1. Finite-copy rational-map transduction and its obstruction

### 1.1 Exact problem and operation

Let

`Phi : P(H) -->> P(K)`, `Phi([x]) = [F_0(x):...:F_{E-1}(x)]`,

be a projective rational map written in coprime homogeneous coordinates of common,
minimal degree `r`.  Let

`A_Phi : Sym^r(H) -> K`

be the coefficient operator defined by

`A_Phi |x>^{tensor r} = sum_a F_a(x)|a> =: |F(x)>`.

The computational task **Q-RATIONAL-MAP** is: from `r` copies of an unknown unit
`|x>` and a compiled description of `A_Phi`, herald failure on the base locus and,
away from it, output the normalized ket

`|Phi(x)> = |F(x)>/||F(x)||`.

Choose any known `alpha >= ||A_Phi||` and implement the contraction
`K_Phi = A_Phi/alpha` as the successful Kraus block of a Stinespring isometry.
One trial has

`K_Phi |x>^{tensor r} = |F(x)>/alpha`,

`p_Phi(x) = ||F(x)||^2/alpha^2`.

Thus the conditional output is exact.  This is a nonlinear map of the projective
input, but the physical operation is linear on its `r`-copy Veronese lift.

### 1.2 Converse and copy-degree lower bound

Fix one accepted measurement record of any circuit using `t` identical input copies.
Its Kraus operator `B : H^{tensor t} -> K` has output coordinates

`G_a(x) = <a|B|x>^{tensor t}`,

which are homogeneous polynomials of degree `t`.  If its conditional ray equals
`Phi([x])` on a Zariski-dense open set, then

`G_a F_b - G_b F_a = 0` for every `a,b`.

Because the `F_a` are coprime in the polynomial UFD, there is a homogeneous
polynomial `h` with `G_a = h F_a` for every `a`.  Hence `deg h = t-r` and `t >= r`.
If `D >= 2`, a **single fixed branch** with `t>r` has the additional zero locus of
`h`; it cannot be nonzero everywhere `Phi` is defined.  This does not force an
arbitrary multi-branch protocol to use `t=r`: several `h_l` can cover one another's
zeros, and extra input copies can simply be measured and discarded.  The conclusion
that survives is the lower bound `t>=r` for every nonzero exact branch.

At `t=r`, `h` is constant.  Therefore every accepted Kraus operator that gives the
same pure output ray has, on `Sym^r(H)`, the form `c_l A_Phi`.  For any collection of
accepted records, trace nonincrease gives

`(sum_l |c_l|^2) A_Phi^dag A_Phi <= 1`,

and therefore

`p_success(x) <= ||F(x)||^2 / ||A_Phi||^2`.

The scaled coefficient contraction with `alpha=||A_Phi||` attains this bound.  Extra
ancillas, accepted labels, and feed-forward cannot cancel a small image norm at the
minimal copy count.

This proof is algebraic and self-contained.  What remains unverified is whether this
normal form and optimal-success statement already appear in the literature.

### 1.3 Resource ledger

Without amplitude amplification, failure probability at most `delta` needs

`R = ceil(log(1/delta)/p_Phi(x))`

independent trials.  The ledger is:

- input copies: `rR`, expected `r/p_Phi(x)` until first success;
- live data: `r ceil(log D)` input qubits, `ceil(log E)` output qubits, and the
  Stinespring ancilla;
- gates: `R L_A`, where `L_A` is the explicit compilation length of the contraction;
- sparse no-QRAM LCU compilation: `L_A = O(S poly(r,log D,log E,b))` using one
  controlled block per listed coefficient to `b` bits, but generally with the larger
  normalization `alpha_LCU=sum |A_entry|`; an operator-norm-optimal Stinespring
  dilation exists abstractly but may require dense synthesis and is not assigned this
  `O(S)` cost;
- readout: one herald bit plus the output ket; tomography of that ket is not included.

For the **direct stage-by-stage construction** of `x_{j+1}=Phi(x_j)`, no-cloning
removes the tempting reuse claim.  If `C_j` is the expected number of original copies
needed for one copy of `x_j`, then

`C_{j+1} = r C_j/p_Phi(x_j)`,

and consequently

`C_T = r^T / product_{j=0}^{T-1} p_Phi(x_j)`.

This is a construction cost, not a universal lower bound.  Let `d_T` be the degree of
`Phi^T` after removing common coordinate factors.  Section 1.2 instead gives the
representation-independent lower bound `t>=d_T` for every nonzero exact branch that
implements the iterate.  Algebraically stable maps have `d_T=r^T`; maps with degree
drop can be cheaper and suggest a research question only after coefficient-circuit
size, success normalization, and a matched classical baseline are charged.

### 1.4 Classical and known-quantum attacks

With an explicit `x` and `S` listed tensor coefficients, direct monomial evaluation
costs `O(Sr)` arithmetic operations and already returns the same normalized vector.
The quantum circuit reads/compiles the same `S` coefficients and has no asymptotic
time advantage.

With copy-only `x`, the quantum output is a quantum state while a classical explicit
vector is a different output.  For any proposed scalar downstream observable, a
separation from adaptive single-copy measurement remains to be proved; tomography is
not a legitimate substitute for that proof.

Most importantly, this transducer is the coherent-output version of the same tensor
contraction underlying C-318.  Relabeling the contraction output as a rational map
does not supply a new quantum mechanism under D22.  The copy-degree theorem is a new
negative/instrument candidate; **Q-RATIONAL-MAP is not a north-star algorithm**.

Physical small-instance attack: a sparse `A_Phi` can be a postselected linear-optical
or MBQC Kraus gadget.  This demonstrates the identity but inherits `p_Phi`; it does
not make coefficient-state preparation free.

## 2. Chart-aligned jet and tangent-cone spectroscopy

### 2.1 Exact problem

Let normalized `|F> in Sym^m(H)` encode a degree-`m` form under the existing C3
convention

`overline{f(overline{x})} = <F|x>^{tensor m}`.

The input supplies `|F>` and a circuit `U_x|0>=|x>`.  The task **Q-TANGENT-CONE** is
to output the multiplicity `mu` of the hypersurface `f=0` at `[overline{x}]` and,
conditional on `mu`, a ket encoding its leading transverse form.

The conjugate point is essential.  Applying `U_x^dag` to the coefficient ket gives
all-zero amplitude

`<0|^{tensor m}(U_x^dag)^{tensor m}|F> = <x|^{tensor m}|F> = f(overline{x})`.

It does not evaluate `f(x)` in general.  Replacing this by `f(x)` would silently
implement conjugation and violate C3.

### 2.2 Orthogonal jet identity

Put `|F_x>=(U_x^dag)^{tensor m}|F>`.  Let `Q_k` project onto basis tensors having
exactly `k` legs outside `|0>`.  Symmetry makes these mutually orthogonal components.
For the transverse `k`-polar tensor

`T_k=(<0|^{tensor(m-k)} tensor Pi_perp^{tensor k})|F_x>`,

with positions symmetrized, one has exactly

`q_k := ||Q_k F_x||^2 = binom(m,k)||T_k||^2`,

`sum_{k=0}^m q_k = ||F||^2 = 1`.

In the affine chart `y_0=1`, the coefficient state of
`f(overline{U_x} y)` decomposes by transverse degree `k`.  Therefore

`mu = min{k:q_k>0}`.

Moreover `T_mu` annihilates the radial direction in every slot because all lower
polars vanish.  It descends to `Sym^mu(T_[overline{x}]^*)` and is the equation of the
scheme-theoretic tangent cone, up to its nonzero binomial scalar.

The useful cancellation is `sum q_k=1`: the protocol does not separately postselect
each derivative contraction and does not inherit a coefficient-operator norm for
every jet order.

### 2.3 Operation and resources

Each trial performs:

1. prepare one `|F>`;
2. apply `U_x^dag` independently to all `m` legs;
3. compute/measure the occupation number outside mode `0`;
4. retain the symmetric transverse registers if a tangent-cone ket is requested.

Under the promise `q_mu >= gamma`, the minimum of

`R = ceil(gamma^{-1} log(1/delta))`

observed occupation numbers equals `mu` with probability at least `1-delta`.
Resources are `R` coefficient-state preparations, `mR` calls to `U_x^dag`,
`O(m log D)` live data qubits, and `O(R m log D)` elementary occupation-count logic
in addition to the supplied circuits.  There is no hidden amplitude amplification.

In `D` optical modes, `|F>` is an `m`-photon relation state, `U_x^dag` is a mode
interferometer, and number resolution outside the reference mode reads `k`.  This is
a direct small-instance linear-optics experiment.

### 2.4 Fatal baseline and equivalence attacks

The multiplicity output is not collectively quantum.  An adaptive single-copy
comparator can apply the same `U_x^dag` to each supplied `|F>` and number-resolve it;
its distribution and sample complexity are exactly `q_k` and `R`.

If `f` and the point `p=overline{x}` are explicit, `f` has `S` listed monomials, and
exact arithmetic is available, choose a random transverse direction `v` and form the
univariate restriction `f(p+t v)`.  Naively multiplying the degree-at-most-`m`
univariate factors for each listed monomial and finding the first nonzero coefficient
costs `O(Sm^2+D)` arithmetic.  The order equals the multiplicity for a generic `v`;
sampling coordinates of `v` from a finite set of size `L` misses the nonzero leading
tangent form with probability at most `m/L` by the polynomial identity bound.  This
baseline returns only the scalar multiplicity, not the full tangent-cone ket.  If
`U_x` is an arbitrary succinct quantum circuit, a
claim based on the difficulty of classically simulating `U_x` is generic circuit
simulation, not an algebraic-geometric mechanism.

This is not merely the residual observable C-318: it resolves all jet orders and can
return the tangent-cone coefficient state.  Nevertheless its mechanism is only an
inverse coordinate rotation and an occupation measurement, and the allowed
single-copy comparator duplicates the classical output.  The identity is retained
as an instrument; the speedup claim is refuted.

## 3. Fermionic regressive product for a linear intersection

### 3.1 Exact problem and the linear duality required

Let `U in Gr(a,H)`, `W in Gr(b,H)`, `a+b>=D`, and `c=a+b-D`.  Inputs are normalized
decomposable Plucker kets `|U> in exterior^a H` and `|W> in exterior^b H`.  Promise
transversality `U+W=H`.  The task **Q-GRASSMANN-MEET** is to output the normalized
Plucker ket of `U intersect W`.

Fix a volume form.  Let

`J_a : exterior^a H -> exterior^(D-a) H*`

be linear Poincare duality, `J_a e_S = sign(S)e^*_(S^c)`.  This is not the
conjugate-linear Hermitian Hodge star.  A physical implementation either uses a
separately labelled dual-mode register or implements the displayed coefficient-basis
permutation.  It never applies an unknown-state conjugation.

Put `p=D-a`, `q=D-b`.  The Grassmann-Cayley regressive product is

`M(U,W) = J_c^{-1}(J_a U wedge J_b W)`.

Because `J_aU` and `J_bW` represent the annihilators `U^0` and `W^0`,

`(U intersect W)^0 = U^0 + W^0`.

Transversality makes the wedge nonzero and proves that `M(U,W)` is a nonzero
decomposable representative of `U intersect W`.

### 3.2 Exact CP normalization and angle ledger

Exterior multiplication

`mu_(p,q): exterior^p H* tensor exterior^q H* -> exterior^(p+q) H*`

maps disjoint basis subsets to their signed union.  For every output subset there are
`binom(p+q,p)` orthogonal input splittings.  Hence

`mu mu^dag = binom(p+q,p) 1`,

`||mu||^2 = binom(p+q,p)`.

The valid heralded Kraus operator is therefore

`K_meet = mu/sqrt(binom(D-c,D-a))`.

Choose orthonormal covector frames for the annihilators `U^0,W^0`, and let `C` be
their cross-Gram matrix.  If `sigma_i` are its singular values, i.e. principal-angle
cosines in the dual annihilator spaces, then

`||J_aU wedge J_bW||^2`

`= det([[1,C],[C^dag,1]])`

`= product_{i=1}^{min(p,q)}(1-sigma_i^2)`.

Thus one attempt succeeds with the exact probability

`p_meet = product_i(1-sigma_i^2)/binom(D-c,D-a)`.

This charges both geometric near-nontransversality and coherent erasure of the two
input origins.  No favorable angle removes the binomial denominator.

For `p=q=D/4`, even orthogonal annihilators give
`p_meet=1/binom(D/2,D/4)=2^{-Theta(D)}`.  If `p,q=O(1)`, the denominator is harmless,
but the classical problem is correspondingly an ordinary low-codimension update.

Second-quantized occupation encoding uses `Theta(D)` modes.  A first-quantized
encoding initially uses `(a+b)log D` qubits, but linear Poincare duality materializes
`D-a` and `D-b` dual particles; it does not preserve a fictitious `O(log D)` space
bound.

### 3.3 Classical, known-quantum, and physical attacks

For explicit orbital frames, QR/SVD computes an intersection basis in polynomial
time, for example `O(D(a+b)^2)` dense arithmetic, and exterior/Plucker arithmetic is
also polynomial in the represented output size.

For decomposable inputs, Poincare particle-hole conversion and the wedge stay within
fermionic Gaussian/Slater structure.  Their evolution has an efficient classical
matrix representation.  Making the input a non-Gaussian superposition merely moves
the presumed hardness into preparation of quantum data.

As a quantum mechanism, `J` is a basis permutation/Bogoliubov particle-hole map and
`mu` is exactly antisymmetric (Schur) projection followed by label erasure.  The
geometric output is more informative than a symmetry-test bit, but the entire hard
operation is still the familiar antisymmetrization primitive.  It therefore fails
D22's substantive-equivalence test in addition to the success and baseline failures.

A small fermionic or dual-rail demonstration could fuse two Plucker states and verify
the returned intersection.  It would demonstrate Grassmann-Cayley algebra, not a
speedup.

## 4. D22 and north-star audit

| proposal | new problem-level output | claimed new mechanism | fatal disposition |
|---|---|---|---|
| rational-map transducer | apply a projective rational map to a quantum point | finite-copy Veronese contraction | same contraction as C-318; explicit classical evaluation; output mismatch |
| jet spectrometer | multiplicity plus tangent-cone ket | coherent chart alignment and occupation stratification | identical single-copy measurement baseline; scalar multiplicity has an explicit `O(Sm^2+D)` generic-line baseline |
| Grassmann meet | Plucker ket of `U intersect W` | Poincare-dual/wedge/regressive product | antisymmetric/Schur projection; binomial heralding; Gaussian simulation |

Originality of the exact normal-form/lower-bound theorem and of the jet-state output
is historically unverified.  Even if both are historically new, neither is a new
speedup mechanism.  No row here should be promoted above CONJECTURE without a critic,
and no proposal merits a round-3 prover seat as currently stated.

The smallest missing results that could change this verdict are precise:

1. For rational transduction: a same-output scalar task and a lower bound against
   adaptive single-copy measurement under exactly the same state access.  The lower
   bound must exploit more than generic circuit-simulation hardness and must coexist
   with the optimal success bound above.
2. For tangent cones: none for the multiplicity bit under the stated access, because
   the comparator is identical.  A different task would be required, together with
   a lower bound for producing or using the tangent-cone ket without changing the
   classical output.
3. For the regressive meet: a non-antisymmetrization operation that avoids the proven
   `binom(p+q,p)` normalization, plus a matched classical lower bound on non-Gaussian
   inputs whose preparation is charged.  The displayed Kraus implementation cannot
   supply it.

## MERGE PROPOSAL

### Exact proposed definitions (with hypotheses)

Historical novelty of these definitions is unverified.

- **D-R2-RATIONAL-TRANSDUCER.** For finite-dimensional `H,K` and a rational map
  `Phi:P(H)-->>P(K)` with coprime homogeneous coordinates `F_a` of common minimal
  degree `r`, `A_Phi:Sym^r(H)->K` is defined by
  `A_Phi|x>^r=sum_a F_a(x)|a>`.  On `F(x) != 0`, scaling by
  `alpha>=||A_Phi||` gives an exact heralded output ray `[F(x)]` with success
  `||F(x)||^2/alpha^2`.
- **D-R2-ORTHOGONAL-JET.** For normalized `|F> in Sym^m(H)` obeying C3 and a supplied
  unitary `U_x|0>=|x>`, `Q_k(U_x^dag)^m|F>` is the component with exactly `k`
  registers orthogonal to `|0>`.  Its probability is
  `q_k=binom(m,k)||T_k||^2`, `sum_k q_k=1`; the base point is
  `[overline{x}]`, not `[x]`.
- **D-R2-REGRESSIVE-MEET.** For oriented finite-dimensional `H`,
  `U in Gr(a,H)`, `W in Gr(b,H)`, `a+b>=D`, and `U+W=H`, linear Poincare duality
  `J_s:exterior^s H->exterior^(D-s)H*` defines
  `J_c^{-1}(J_aU wedge J_bW)`, `c=a+b-D`, as a Plucker representative of
  `U intersect W`.  `J_s` is not an antilinear Hermitian Hodge star.

Provisional claim rows (CONJECTURE or REFUTED only):

### C-NEW-R2-GEO-1 — finite-copy rational-map normal form

- statement: Every accepted branch on `t` identical pure copies defines a
  degree-`t` homogeneous coordinate vector.  An exact realization of a coprime
  minimal degree-`r` rational map requires `t>=r`.  At `t=r`, total success obeys
  `p(x)<=||F(x)||^2/||A_Phi||^2`, with equality for the scaled coefficient map.
- status: CONJECTURE
- depends-on: D-R2-RATIONAL-TRANSDUCER
- where-proved: `scouting/original-geometry-round2.md` Section 1.2
- where-tested: not archived; no registered checker (scratch numerical recomputation did not test this algebraic proof)
- missing lemma: critic audit of the multi-Kraus proportionality argument and the
  domain qualification at base points.

### C-NEW-R2-GEO-2 — rational transduction gives a north-star speedup

- statement: The coefficient contraction for Q-RATIONAL-MAP, by itself,
  establishes a new asymptotic quantum advantage for applying algebraic maps.
- status: REFUTED
- depends-on: D-R2-RATIONAL-TRANSDUCER, C-318, C-NEW-R2-GEO-1
- where-proved: `scouting/original-geometry-round2.md` Sections 1.3--1.4
- where-tested: not archived; no registered checker
- surviving statement: it is an exact state transducer and gives the lower bound
  in C-NEW-R2-GEO-1, but explicit sparse evaluation is `O(Sr)`, the copy-only output
  comparison is unresolved, and its operation is substantively C-318.

### C-NEW-R2-GEO-3 — free recycling in nonlinear projective iteration

- statement: Directly reusing transducer outputs implements `T` iterations of a
  degree-`r>1` projective map with polynomially many initial uncontrolled copies,
  without a promise on success or degree growth.
- status: REFUTED
- depends-on: D-R2-RATIONAL-TRANSDUCER, C-NEW-R2-GEO-1
- where-proved: `scouting/original-geometry-round2.md` Section 1.3
- where-tested: not archived; no registered checker
- surviving statement: the direct construction has
  `C_T=r^T/product_j p_Phi(x_j)` expected initial copies; any exact implementation of
  the composed map needs at least `deg(Phi^T)` copies per nonzero accepted branch
  after common factors are removed.  Low dynamical degree remains an unranked
  research question, not an advantage claim.

### C-NEW-R2-GEO-4 — orthogonal jet identity

- statement: In the C3 convention, chart alignment of a degree-`m` coefficient
  state gives `q_k=binom(m,k)||T_k||^2`, its first occupied transverse degree is the
  multiplicity at `[overline{x}]`, and the first occupied component represents the
  scheme-theoretic tangent cone.
- status: CONJECTURE
- depends-on: D-R2-ORTHOGONAL-JET, D-QN-PHYSICAL-DATA-ACCESS, C-318
- where-proved: `scouting/original-geometry-round2.md` Section 2.2
- where-tested: not archived; no registered checker (scratch random-tensor recomputation only)
- missing lemma: critic verification of tensor normalizations and the descent of
  `T_mu` to the projective tangent space.

### C-NEW-R2-GEO-5 — jet spectroscopy gives a collective speedup

- statement: Q-TANGENT-CONE has a quantum copy advantage over the permitted
  adaptive single-copy measurement baseline.
- status: REFUTED
- depends-on: D-R2-ORTHOGONAL-JET, D-QN-PHYSICAL-DATA-ACCESS, C-NEW-R2-GEO-4
- where-proved: `scouting/original-geometry-round2.md` Sections 2.3--2.4
- where-tested: not archived; no registered checker
- surviving statement: the exact jet/tangent-cone instrument uses
  `R=ceil(gamma^{-1}log(1/delta))` coefficient states, and the comparator performs
  the same rotation and occupation measurement with the same `R`.

### C-NEW-R2-GEO-6 — regressive-product identity and success

- statement: Under `U+W=H`, the linear-Poincare regressive product returns the
  Plucker ray of `U intersect W`, and its normalized wedge Kraus succeeds with
  `product_i(1-sigma_i^2)/binom(D-c,D-a)`.
- status: CONJECTURE
- depends-on: D-R2-REGRESSIVE-MEET
- where-proved: `scouting/original-geometry-round2.md` Sections 3.1--3.2
- where-tested: not archived; no registered checker (scratch enumeration verified the wedge normalization only)
- missing lemma: critic audit of the dual-space principal-angle normalization and
  the physical dual-register convention.

### C-NEW-R2-GEO-7 — regressive meet gives a north-star speedup

- statement: Q-GRASSMANN-MEET is a genuinely new quantum mechanism with an
  asymptotic advantage over classical linear-subspace intersection.
- status: REFUTED
- depends-on: D-R2-REGRESSIVE-MEET, C-NEW-R2-GEO-6
- where-proved: `scouting/original-geometry-round2.md` Section 3.3
- where-tested: not archived; no registered checker
- surviving statement: it is a geometric output interpretation of linear
  Poincare duality plus antisymmetric projection, with the exact binomial success
  penalty above; decomposable instances have efficient classical matrix simulation.
