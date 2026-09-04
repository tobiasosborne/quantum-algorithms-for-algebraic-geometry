# A compressed three-copy measurement for the second Segre secant

2026-09-05. Exact measurement and soundness derivations; the proposed original
mechanism is refuted by a concrete reduction to random-cut rank testing in
`verdicts/secant-three-copy-r1.md`. This is not a north-star hit. Definitions
are in `definitions/secant-three-copy.md`; its departures from C1/C2 apply.
Claims are C-335--C-338. The representation-theoretic geometry is established
prior work; the candidate contribution is an explicit coherent measurement of
its surviving multiplicity lines. Historical novelty and D22 qualification are
not established by independent derivation or by an unsuccessful search.

## 1. Computational result proposed

Given the copy access of D-S3-SECANT, distinguish `psi in X_2` from
`distance_2(psi)>=epsilon`. The proposed procedure has perfect completeness
with ideal gates. For fixed `k,epsilon`, it uses a constant number of copies
independent of all local dimensions, and a number of gates polynomial in
`sum_i log q_i` and `log(1/delta)`. Constants depend on computable finite
dimensional quantities in D-S3-ROBUSTNESS-CONSTANT. No polynomial dependence
on growing `k` or on `1/epsilon` is asserted for this distance-testing result.

The single-trial measurement is meaningful also for growing `k`: it measures
`r_3` in `O(sum_i log q_i + k)` ideal elementary operations and three copies,
up to deterministic compilation of constant-size rotations. Thus a separately
promised residual `r_3>=eta` is detected using `O(log(1/delta)/eta)` trials.
The residual promise must not silently replace geometric distance.

## 2. Exact cubic span

ASSUME D-S3-SECANT and D-S3-LOCAL-REPRESENTATION.
PROVE: In the local Schur decomposition, the span D-S3-CUBIC-SPAN has exactly
these blocks: no alternating local type; in a block with `m` standard local
types it is `tensor_i U_{lambda_i,i} tensor span{w_m}`. The block `m=1` is zero.

2.1 It is enough to span cubes of actual sums of two product tensors. Cubing is
continuous, so passing to their closure does not change their linear span.
Nonzero normalization also does not change this span. [D-S3-SECANT]

2.2 Expand `(a+b)^{tensor 3}` for product tensors `a,b`. At each site every term
has at most two distinct local vectors. Its projection onto the alternating
representation is zero. The terms `a^{tensor 3},b^{tensor 3}` have only symmetric
local types. [Expansion; D-S3-LOCAL-REPRESENTATION]

2.3 At a standard local type, the three placements of the distinct vector in
`a_i,a_i,b_i` have Schur components `u_i(a_i,b_i) tensor v_j`, with the same
`u_i` and a common scalar absorbed into it. To verify, first take `a_i=e_0,
b_i=e_1`: the weight-one plane is the permutation representation on three
positions, and the standard projection is exactly the stated sum-zero plane.
Apply a linear map taking `e_0,e_1` to `a_i,b_i`; it commutes with replica
permutations. The same argument applies to the three `a_i,b_i,b_i` placements.
[D-S3-LOCAL-REPRESENTATION; explicit plane calculation]

2.4 The three global `aab` placements therefore have standard multiplicity
factor `sum_j v_j^{tensor m}`; the `abb` contribution lies on the same line.
The symmetric sites add no multiplicity. This proves containment in the
stated block. The sum vanishes at `m=1`; for `m>=2` its squared norm is
`3+6(-1/2)^m>0`. [2.2--2.3; trine inner products]

2.5 For the converse, use the local `GL(H_i)` orbit of
`e_0^{tensor k}+e_1^{tensor k}`. For every `m=0` or `m>=2`, its projection onto
the displayed block is nonzero: the `aab` and `abb` parts have different
local weight vectors and cannot cancel. Each `tensor_i U_{lambda_i,i}` is
an irreducible representation of the product group. Its orbit span is the
whole factor. Distinct tuples of partitions are inequivalent representations,
so an invariant subspace decomposes into their isotypic blocks. This gives
equality in every block. [2.4; finite-dimensional Schur-Weyl decomposition]

2.6 The dual annihilator is precisely the cubic ideal of the secant. The
multiplicity-one surviving module agrees with Landsberg--Manivel, Theorem 4.7.
The zero set of these cubics is exactly the secant, by the flattening-minor
theorem of Raicu, Theorem 4.1 and Corollary 4.2. These are cited geometry,
not new campaign theorems. [Primary references in section 8]

## 3. The circuit and its costs

ASSUME three copies and the known tensor registers; no reflections about the
unknown input, amplitude oracle, or tensor decomposition are supplied.
PROVE the block projector of section 2 can be measured efficiently.

3.1 Extract the `S_3` irrep at each site while retaining its representation
coordinate coherently. An explicit generalized Fourier extraction is
`|u,b> -> d_lambda^(-1/2) sum_a |lambda,a,b> |u,a>`, up to a fixed choice of
Fourier conventions. Prepare the uniform register on the six permutations,
apply the controlled replica permutation, then the fixed group Fourier
transform. Matrix-element orthogonality gives the displayed isometry.
The residual data and `a` contain the `U` factor and a fixed maximally
entangled representation pair; `b` retains the original standard coordinate.
Thus it can be measured jointly with other sites' `b` registers.
[D-S3-LOCAL-REPRESENTATION; finite group matrix-element orthogonality]

3.2 Measure the local types. Reject if any is alternating. Let `m` be the
number of standard types. Accept if `m=0`; reject if `m=1`; otherwise measure
`{|w_m><w_m|, 1-|w_m><w_m|}` on their retained representation registers.
This preserves all coherence needed inside a type block. Section 2 proves
that on `psi^{tensor 3}` the acceptance probability is `1-r_3(psi)`.
Every accepted multiplicity line is invariant under simultaneous replica
permutations, so this effect also equals the zero extension of `P_3` on
arbitrary three-copy vectors. The input-copy promise matters for its
interpretation as variety testing.
[2.1--2.5; D-S3-CUBIC-SPAN]

3.3 The trine cat has Schmidt rank at most three across every sequential cut,
since it is the sum of three product vectors. Its Gram matrices consist of
`(v_a^*v_b)^ell`, all known scalars. Sequential Schmidt decompositions therefore
give a deterministic preparation circuit with a memory of dimension at most
three and `O(m)` constant-size isometries. Reverse that preparation and test
the all-zero result to implement its rank-one projector. There is no
postselection preparation penalty. [D-S3-LOCAL-REPRESENTATION; Schmidt decomposition]

3.4 The finite group circuit uses `O(log q_i)` gates for controlled swaps of
three binary-encoded local registers and constant ancillary size. Padding a
local register to a power of two preserves its supplied subspace. The total
ideal-operation cost per trial is `O(sum_i log q_i+k)` and memory is
`O(sum_i log q_i+k)`. Computing the cat Gram matrices and sequential small
isometries costs polynomial time in `k` and requested bit precision.
With a fixed finite universal gate set, include rotation synthesis factors
polynomial in `log(k/xi)` for total trial error `xi`. [3.1--3.3]

3.5 For a residual lower bound `eta`, use
`R=ceil(log(1/delta)/eta)` independent trials and reject at the first failure.
The ideal false acceptance probability is at most `exp(-R eta)`. Compile each
trial to error at most `delta/(4R)` and adjust the repetition error budget;
the resulting circuit has bounded two-sided error. Copy preparation is a
charged input resource: precisely three copies per trial, no quantum loading
claim about classically supplied amplitude arrays. [3.2; Bernoulli repetition]

## 4. Minimal copies and optimal rejection

The abstract optimal-span argument is known: Lovitz--Lowe,
arXiv:2410.21417v2, Lemma 2.1. The proof below is included for completeness,
not claimed as a new algorithmic principle.
ASSUME exact perfect completeness for all `X_2` states.
PROVE the proposed measurement maximizes rejection among three-copy tests,
and every test using at most two copies is trivial.

4.1 If an acceptance effect `E` satisfies `0<=E<=1` and
`<phi^3,E phi^3>=1`, positivity implies `E phi^3=phi^3`. It acts as the
identity on their span, has no cross terms with that span, and hence
`E>=P_3`. The proposed projector minimizes acceptance for every pure input.
[D-S3-CUBIC-SPAN; positivity]

4.2 Every computational product basis vector is in `X_2`, and every sum of
two such basis vectors is in its affine cone. Polarization shows that their
squares span all of `Sym^2(H)`. The same positivity argument forces any
one- or two-copy perfect-completeness tester to accept every pure state.
This lower bound does not apply to two-sided-error tests. [D-S3-SECANT; 4.1]

## 5. A dimension-independent soundness theorem for fixed factor count

ASSUME `distance_2(psi)>=epsilon`; abbreviate `r=r_3(psi)` and use
D-S3-ROBUSTNESS-CONSTANT. PROVE `r>=eta_k(epsilon)>0`.

5.1 The antisymmetric projector on the three copies of any subset of sites
annihilates every tensor cube in `S_3(X_2)`. Therefore its expectation is at
most `r`. For a singleton with decreasing reduced eigenvalues `lambda_j`,
the expectation is `e_3(lambda)=sum_{a<b<c} lambda_a lambda_b lambda_c`.
[Every secant tensor has every flattening rank <=2; 2.1; exterior determinant]

5.2 Put `tau=1-lambda_1-lambda_2`. Three independent samples from the spectrum
are distinct with probability `6e_3`. Given the first sample, the chance the
second differs is at least `1-lambda_1>=tau`; given two distinct indices, the
chance the third avoids them is at least `tau`. Hence `6e_3>=tau^2` and every
singleton tail obeys `tau_i<=sqrt(6r)`. [5.1; elementary sampling identity]

5.3 Let `Q_i` project onto the top two local eigenvectors and `Q=tensor_i Q_i`.
The commuting projector union bound gives
`1-||Q psi||^2 <= sum_i tau_i <= k sqrt(6r)`.
If this is less than one, the normalized `phi=Q psi/||Q psi||` has
`d_tr(psi,phi)<=sqrt(k)(6r)^(1/4)`. The entire local-subspace projection is
used only in the proof, not as an unprovided operation in the algorithm.
[5.2; projective pure-state trace distance]

5.4 The distance of `phi` to the ambient secant equals its distance to the
secant inside `tensor_i range Q_i`: projecting any rank-two approximation
preserves border rank at most two, and normalizing the nonzero projection
can only increase its overlap with `phi`. The block measurement restricts
to the identical qubit measurement because it is built from local replica
permutations. [D-S3-SECANT; 3.1--3.2]

5.5 In fixed finite dimension `2^k`, the unit sphere and the secant are compact.
By 2.6 the continuous residual is strictly positive on the closed subset
at distance at least `t>0`, or that subset is empty. Thus `g_k(t)>0`.
It is possible to compute a certified positive rational lower bound by real
quantifier elimination: use real and imaginary coordinates, unit-norm equations,
the finite list of cubic flattening minors, and quantified overlap inequalities
for distance. The projector coefficients are algebraic, and rational `t` makes
this a finite first-order real-algebraic problem. No efficient bound in `k,t`
is claimed. [2.6; D-S3-ROBUSTNESS-CONSTANT; compactness]

5.6 If `r<epsilon^4/(96k^2)`, then 5.3 gives `d_tr(psi,phi)<epsilon/2`, so
`distance_2(phi)>=epsilon/2`. Choose phases with
`||psi-phi||<=sqrt(2)d_tr(psi,phi)`. The tensor telescoping inequality gives
`||psi^3-phi^3||<=3||psi-phi||`, and hence
`sqrt(r_3(phi)) <= sqrt(r) + 3 sqrt(2k)(6r)^(1/4) <= 8 sqrt(k) r^(1/4)`.
It follows that `g_k(epsilon/2)<=64k sqrt(r)` and
`r>=g_k(epsilon/2)^2/(4096k^2)`. If the premise fails, the other term in
`eta_k` already bounds `r`. [5.3--5.5; triangle inequality]

5.7 Computing a rational lower bound `eta_hat<=eta_k` costs a finite
preprocessing amount `T_pre(k,epsilon)`. With that cost included, total gates
are `T_pre + R O(sum_i log q_i + k polylog(kR/delta))` and copies are `3R`,
where `R=O(log(1/delta)/eta_hat)`. At fixed `k,epsilon`, both preprocessing
and `eta_hat` are constants independent of local dimension. This does not
give a useful numerical value for those constants or a uniform efficient
algorithm when `k` grows. [3.4--3.5; 5.5--5.6]

## 6. Classical comparison and originality boundary

The independent `scouting/secant-single-copy-baseline.md` derives
`T(T-1)>=14q/[27(k+1)]` for adaptive global single-copy measurements at fixed
`k>=4`, local dimension `q>=8`, and distance promise `epsilon=1/2`. It proves
that global Haar states are far from the larger secant, and audits the
product-Haar transcript bound. This is a genuine matched-input candidate
separation, with its proof awaiting a separate converged critic verdict.

There is no claim of a speedup for an explicitly listed classical tensor.
There is also no comparison against tomography as the required output.
The proposed mechanism was coherent projection of representation coordinates
onto the surviving trine-cat line. The critic found the following exact
substantive equivalence, independently reproduced by the baseline lane.

Let `Abar` be the average exterior projector on a uniformly random subset of
sites, including the empty and full subsets. On the globally replica-invariant
subspace, a local Schur block with `m` standard and `ell` alternating factors
has `Abar=c_m(1-|w_m><w_m|)` when `ell=0`, and `Abar=c_m 1` when `ell>=1`,
where `c_m=(1+2(-1/2)^m)/6`. Nonzero rejection blocks have `1/8<=c_m<=1/2`.
Thus `(1-P_3)/8 <= Abar <= (1-P_3)/2` on that subspace. This comparison is
not asserted off the globally invariant subspace.

To derive it, expand the alternating character sum and average each site
independently into/out of the cut. The local factor becomes `(1+R(pi))/2`.
Transpositions give the three trine-line projectors, killed by any alternating
site. The two three-cycles sum on global invariants to `2(-1/2)^m 1`.
This gives the displayed scalar formula. The zero/inadmissible `m=0,1` cases
are detailed in the critic verdict and independent baseline memo.

Consequently a known random-cut, three-copy rank test has perfect completeness,
the same geometric soundness up to a factor eight, and the same gate and copy
asymptotics. Measuring local Schur types first and reporting the cut-rejection
bit divided by `c_m` gives an unbiased estimator of `r_3`, bounded by eight.
This is an explicit reduction to described quantum rank testing, not the
vacuous observation that the circuit uses known gates. It defeats D22 and
the north-star claim, while preserving the exact projector and soundness results.

## 7. Finite verification and hardware target

`checkers/explore/secant_three_copy.py`: the original 88 checks passed in 0.8 seconds on
2026-09-05, with a 60-second timeout and one BLAS thread. It checks complex
nonorthogonal sums, tangent `W` states, local-unitary invariance, trine cat
norm and bond dimension, and comparison with independently evaluated exterior
probabilities of all cuts. All three mutations exit 1; see MUTATIONS.md.
The checker now also compares the random-cut character formula against
independent Schmidt-spectrum calculations. The finite checks do not prove
section 5 or historical novelty.

At four qubit sites, two Bell pairs give rejection `1/12`; each single-site
rank-two test accepts, while the largest cut exterior rejection is `1/16`.
This supplies a nontrivial demonstration beyond local rank tests. Rank-two
GHZ states and the tangent `W` state give zero rejection. Three four-qubit
copies use 12 data qubits, with local three-replica Schur gadgets, constant
ancillas per site, and at most a four-qubit trine-cat projector. A small MBQC
implementation compiles these specified gadgets and tests the predicted
probabilities; no hardware noise or fault-tolerance advantage is inferred.

For `w_4`, the amplitudes are `sqrt(3/8)` on `0000,1111`, `1/sqrt(24)` on
the six weight-two words, and zero otherwise. Local type outcomes determine
whether the final cat projection is on zero, two, three, or four qubits.
At the ideal rejection rate `1/12`, 35 trials detect two Bell pairs with
probability exceeding 0.95. State-preparation and MBQC resource-state costs
remain physical costs of the experiment, not an asymptotic free resource.

## 8. Resolved primary sources and open novelty audit

- J. M. Landsberg and L. Manivel, *On the ideals of secant varieties of Segre
  varieties*, [arXiv:math/0311388](https://arxiv.org/abs/math/0311388), Theorem 4.7:
  [author-hosted paper](https://people.tamu.edu/~jml/LMsec111403.pdf).
  Fetched 2026-09-05. Its geometry predates this construction.
- C. Raicu, *Secant Varieties of Segre--Veronese Varieties*,
  [arXiv:1011.5867](https://arxiv.org/abs/1011.5867),
  [DOI:10.2140/ant.2012.6.1817](https://doi.org/10.2140/ant.2012.6.1817),
  Theorem 4.1 and Corollary 4.2. Abstract and primary full theorem fetched.
- J. Beckey et al., *Product testing with single-copy measurements*,
  [arXiv:2510.07820v1](https://arxiv.org/html/2510.07820v1).
  Fetched; transfer of its ensemble lower bound is undergoing separate review.
- B. Lovitz and A. Lowe, *Nearly tight bounds for testing tree tensor network
  states*, [arXiv:2410.21417v2](https://arxiv.org/html/2410.21417v2), Lemma 2.1
  and section 6. Fetched; abstract optimality and few-copy rank tests are prior work.

Even if this exact cat implementation has not appeared, the explicit random-cut
reduction prevents treating it as the original asymptotic mechanism requested.
