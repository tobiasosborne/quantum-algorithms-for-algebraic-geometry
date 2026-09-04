# Enumerative round 3: coherent flag galleries and Demazure pushforward

2026-09-05. This lane develops a classical-input geometric sampler, obtains an
actual unitary implementation, and then identifies its exact known mechanism.
A second construction tries to turn K-theoretic pushforward into projective
measurement and encounters a precise algebraic obstruction. Neither is a
qualifying north-star algorithm. The finite flag Hilbert space has its counting
metric, explicitly departing from C1; `n` is the vector-space dimension over a
finite field in this disjoint context, rather than the campaign's projective index.
No tensor-state membership tester, quotient projector, or root-state oracle is used.

The operations were derived first. Primary literature was then consulted to check
the concrete Hecke formula, not to generate a menu of proposals. No claim status
is assigned here, and only this lane file is edited.

## 1. The geometric input and an actual sampling task

Let `q>=2` be a prime power. Supply an explicit finite-field representation, so
field arithmetic is polynomial in `log q`; any polynomial used to represent an
extension field is supplied as part of that representation. Let `Flag_n(q)` be
the complete flags in `F_q^n`, with `n>=3`. A flag is encoded by canonical row
reduction using `O(n^2 log q)` bits.

Two flags are `i`-adjacent when all their subspaces agree except the one of
dimension `i`. Omitting that subspace gives a partial flag with exactly `q+1`
refinements. Thus every complete flag has `q` distinct `i`-neighbours.
Let `A_i` be the symmetric adjacency matrix on this relation and `|F_0>` a
classically supplied initial flag, embedded as a computational basis state.

The input also contains a length-`L` word `i_1,...,i_L`, with `1<=i_t<n`,
and unit complex parameters `u_1,...,u_L`. These can be specified, for example,
by rational real and imaginary parts satisfying `|u_t|=1`, with at most `B`
bits per coordinate. Gate synthesis error and sampling error are parameters.

Define the weighted flag-gallery coefficient

`Z(F)=sum_{F_0,F_1,...,F_L=F} product_{t=1}^L omega_t(F_{t-1},F_t)`,

where a step either stays at its flag or makes the prescribed adjacency, with

`omega_t(F,F)=(q-1)u_t/(q-u_t)`,

`omega_t(F,F')=(1-u_t)/(q-u_t)` for distinct `i_t`-adjacent flags,

and all other step weights zero. The output is one classical flag with
probability `|Z(F)|^2`. Section 3 proves these probabilities sum to one.

The coefficients are weighted counts of configurations in iterated flag
correspondences. Unweighted prescribed-gallery configurations are the finite-field
incidence sets underlying Bott--Samelson-type constructions. This is a genuine
classical-input enumerative sampling task, but the complex weights are part of
the task. It is not ordinary integer point counting, a Schubert intersection
number, or an approximation to such a number without an additional reduction.

## 2. First attempt: preserve geometric braid identities by fixed unitary gates

### 2.1 Local correspondence algebra

ASSUME the flag adjacency operators of section 1. Their relations are

`A_i^2=(q-1)A_i+q 1`,

`A_i A_(i+1) A_i=A_(i+1) A_i A_(i+1)`,

and commutation when `|i-j|>1`.

2.1.1 The quadratic relation is elementary: within one refinement fibre,
`A_i=J_(q+1)-1`. Consequently its eigenvalues are `q` on the uniform vector
and `-1` on its orthogonal complement. In particular, `A_i` is Hermitian.

2.1.2 The adjacent relation is the type-A flag convolution braid relation.
The geometric normalization and counting interpretation are stated explicitly
in Fock, Tatitscheff, and Thomas,
[Topological quantum field theories from Hecke algebras, section 4.1, arXiv:2105.09622v3](https://arxiv.org/html/2105.09622v3).
Here it is used as a cited identity, not claimed as an original construction.
The complete `n=3`, `q=2,3` flag spaces were also enumerated in the bounded
exploration described in section 7.

### 2.2 An exact failure of constant affine unitarization

The first proposed local gate was `U_i=a 1+b A_i`, using the same complex
scalars at each adjacent simple modification. This would preserve the geometric
interpretation while introducing cancellation between stay and move histories.

ASSUME `b!=0`, `A_i!=A_(i+1)`, and the ordinary braid relation for these gates.
PROVE no such `U_i` is unitary when `q>1`.

2.2.1 Expanding the two triple products and using 2.1 gives

`U_i U_j U_i-U_j U_i U_j`
`=a b [a+b(q-1)](A_i-A_j)` for `j=i+1`.

Therefore either `a=0` or `a=-b(q-1)`.

2.2.2 In the first case, the two eigenvalues are `bq,-b`. In the second they
are `b,-bq`. Both cases require two different eigenvalue moduli, so neither
is unitary. A scalar gate (`b=0`) is the excluded trivial solution.

This is a narrowly quantified obstruction, not a no-go theorem for every
unitary realization of flag correspondences. Spectral parameters provide an
explicit escape, as the next section demonstrates.

## 3. Successful physical operation: spectral unitary transport

Define

`R_i(u)=[(1-u)A_i+(q-1)u 1]/(q-u)`, for `|u|=1`.

### 3.1 Unitarity without postselection

3.1.1 Put `P_i=(A_i+1)/(q+1)`. This is the orthogonal projector onto vectors
constant on each refinement fibre. The two eigenvalues of `R_i(u)` are

`1` on `range P_i`, and `zeta(u)=(q u-1)/(q-u)` on its complement.

3.1.2 For `|u|=1`, `|q u-1|=|q-u|`, so `|zeta(u)|=1`. Hence

`R_i(u)=zeta(u) 1+[1-zeta(u)]P_i`

is an exact unitary, including the removable special case `R_i(1)=1`.
There are no failed histories and no product of small success probabilities.

3.1.3 The amplitude of `F` in `R_(i_L)(u_L)...R_(i_1)(u_1)|F_0>` is
exactly `Z(F)`. This proves the normalization asserted in section 1.

### 3.2 The parameter-dependent local cancellation identity

ASSUME `|u|=|v|=1`. PROVE

`R_i(u)R_(i+1)(uv)R_i(v)=R_(i+1)(v)R_i(uv)R_(i+1)(u)`.

3.2.1 For `u,v,uv !=1`, remove the matching scalar prefactors and set
`c=q-1`, `x=cu/(1-u)`, `z=cv/(1-v)`, `y=cuv/(1-uv)`.
The difference between the remaining two sides is

`[y(c+x+z)-xz](A_i-A_(i+1))`.

3.2.2 Direct fraction arithmetic gives `y(c+x+z)=xz`, so the difference
vanishes. Continuity covers the omitted parameter values. This cancellation
holds before summing all endpoint amplitudes and is independent of Hilbert-space
size. It was the most promising part of the construction.

### 3.3 Circuit and resource ledger

3.3.1 Given a complete flag and `i`, compute reversibly its omitted partial
flag and a coordinate for the chosen line in `F_(i+1)/F_(i-1)`. Canonical
finite-field row reduction gives a bijective encoding of that fibre by
`P^1(F_q)`, a set of `q+1` labels, in polynomial time in `n,log q`.

3.3.2 On the coordinate register, compile a unitary `W` mapping zero to the
uniform superposition over those `q+1` labels. Binary-prefix state preparation
uses controlled rotations with probabilities determined by completion counts;
there is no amplitude database, Fourier transform, or rejection of `q` branches.
Apply `W^dag`, a phase to the zero label, and `W`, then undo the encoding.
Together with the common phase `zeta`, this implements the displayed `R_i(u)`.

3.3.3 Approximate every step to operator norm at most `epsilon/(2L)`. The
telescoping unitary error bound then makes the final measurement distribution
`epsilon`-close in total variation. All arithmetic and rotation synthesis cost
`poly(n,log q,B,log(L/epsilon))` per step, giving total gates

`L poly(n,log q,B,log(L/epsilon))`

and polynomial workspace. Initial preparation is classical basis-state loading;
the final output has `O(n^2 log q)` bits. No quantum input is assumed.

3.3.4 A small hardware experiment needs one mode per refinement label, or an
encoded register, a uniform-mode interferometer and a phase shift. Already
`n=3,q=2` has 21 complete flags. An implementation could test the equality of
the two three-gate words in 3.2 and interference between gallery histories.
This is a circuit identity experiment, not evidence of computational advantage.

## 4. Exact novelty audit: this is known Baxterization

Crampé and Poulain d'Andecy,
[Baxterisation of the fused Hecke algebra and R-matrices with gl(N)-symmetry, arXiv:2004.05035v1](https://arxiv.org/html/2004.05035),
recall the ordinary Hecke formula in Example 3.2, equation (9):

`B_i(v)=sigma_i-(t-t^(-1))/(1-v)`.

Their generators satisfy `sigma_i^2=(t-t^(-1))sigma_i+1`. Substitute

`t=sqrt(q)`, `sigma_i=A_i/sqrt(q)`, `v=u^(-1)`.

Then the operation constructed above is exactly

`R_i(u)=[sqrt(q)(1-u)/(q-u)] B_i(u^(-1))`.

Thus the central formula and spectral braid cancellation are established Hecke
Baxterization with a scalar unitary normalization. This is an exact reduction,
not a rejection merely because universal quantum circuits can express the gates.
The pointwise formula at `u=1` is obtained by continuity on both sides.

Unitary Yang--Baxterization as a source of quantum gates is also explicitly
studied by Zhang, Kauffman, and Ge,
[Yang--Baxterizations, Universal Quantum Gates and Hamiltonians, arXiv:quant-ph/0502015](https://arxiv.org/abs/quant-ph/0502015).
No particular TQFT complexity theorem from that work is imported: the exact
formula identification above already defeats the proposed new mechanism.

The flag sampling output could be a new application of that formula; historical
originality of this exact task was not certified. Under PRD D22, a new application
of the same construction would not establish a qualifying algorithm.

## 5. Same-output classical attacks

### 5.1 Compress to Bruhat cells before counting any flags

5.1.1 The stabilizer `B_0` of `F_0` fixes the initial ket, and all adjacency
operators commute with the `GL_n(F_q)` action. The entire evolving state is
therefore constant on each `B_0` orbit. These orbits are the Bruhat cells `C_w`,
indexed by permutations `w in S_n`, with `|C_w|=q^(length(w))`.

5.1.2 Use the normalized cell basis
`|w>=q^(-length(w)/2) sum_{F in C_w}|F>`.
For a pair `w,ws_i` with increasing length, the operator `A_i` has block

`[[0,sqrt(q)],[sqrt(q),q-1]]`.

Each lower-cell flag has `q` neighbours in the upper cell; each upper-cell
flag has one neighbour in the lower cell and `q-1` in its own cell. These
counts and the ratio of cell sizes give the displayed normalization.

5.1.3 Simulate the `n!` cell amplitudes with the two-by-two blocks from 5.1.2.
One step costs `O(n!)` arithmetic operations. Sample a final cell from its
squared amplitude, then sample its `length(w)` affine coordinates uniformly
over the field. This returns exactly the same flag output, with total cost
`O(L n! + poly(n,log q))` arithmetic operations and `O(n!)` coefficient memory.
Appropriate precision adds polynomial factors in the input bit sizes and error.

The full flag count, approximately `q^(n(n-1)/2)`, is therefore an invalid
classical baseline. The `n!` algorithm is an explicit attack, not a certified
best-in-class bound: further Hecke structure, a special word, or special parameters
may improve it. No classical hardness result for this sampling law is established.

### 5.2 At large field size, the sampler is close to trivial

ASSUME any word and unit parameters, starting from one classical flag. PROVE
that its endpoint law is within `min(1,4L^2/(q+1))` of returning `F_0`.

5.2.1 Every fibre-uniform projector obeys
`||P_i|F_0>||=1/sqrt(q+1)`. Compare step `R_i(u)` with the scalar gate
`zeta(u)1`; their difference on `F_0` has norm at most `2/sqrt(q+1)`.

5.2.2 Telescope the product against the product of these scalar gates. The
suffix factors have norm one and the reference prefix is scalar, so

`||R_(i_L)(u_L)...R_(i_1)(u_1)|F_0> - [product_t zeta(u_t)]|F_0>||`
`<=2L/sqrt(q+1)`.

5.2.3 Project onto the orthogonal complement of `F_0` and square. This gives
the bound on the probability of a different endpoint. That probability is
exactly the total variation from the deterministic classical sampler.

For `L=poly(log q)` at fixed `n`, returning the input is asymptotically accurate.
A nontrivial large-field regime requires at least order `sqrt(q)` steps under
this bound. Increasing `n` with fixed `q` is not addressed by this easy attack,
but section 4 still identifies the mechanism there as established Baxterization.

### 5.3 Ordinary enumerative counts are a different task

At `u=0`, formally `R_i(0)=A_i/q`, which is not unitary. Applying these
normalized correspondences and accepting their heralded branch restores the
usual normalization cost. For a reduced word of length `L`, its `q^L` minimal
galleries have distinct endpoints, so success from `F_0` is `q^(-L)`.
Their endpoints are uniformly distributed in a Bruhat cell and are classically
sampled by its affine coordinates. Moving to unit-circle weights changes the
task; no stable analytic-continuation reduction to integer counts is supplied.

## 6. Second construction: K-theoretic pushforward as measurement

The attempted replacement was to use idempotent Demazure operators instead of
braid generators, hoping successful geometric simplification could become an
ordinary projective measurement with accepted branches retained.

On polynomials in `x_1,...,x_n`, consider the explicit isobaric divided difference

`pi_i f=[x_i f-x_(i+1) s_i(f)]/(x_i-x_(i+1))`,

where `s_i` interchanges those variables. It preserves total degree, is
idempotent, and satisfies the adjacent braid relation. The intended output was
coefficient sampling after a prescribed pushforward word, for a classically
specified polynomial with nonzero resulting image.

### 6.1 Why a new positive metric does not make this a projection circuit

ASSUME two orthogonal projectors `P,Q` satisfy `PQP=QPQ`. PROVE they commute.

6.1.1 Denote their common product by `C`. Multiplying the equality on the
left by `P` gives `PQPQ=C`; multiplying on the right gives `QPQP=C`.

6.1.2 Expand
`(PQ-QP)^dag(PQ-QP)=QPQ-QPQP-PQPQ+PQP=C-C-C+C=0`.
Thus `PQ=QP`. This is independent of dimension or the chosen positive metric.

6.1.3 On the degree-one span of `x_1,x_2,x_3`, the two actual operators are

`pi_1=[[1,0,0],[1,0,0],[0,0,1]]`,

`pi_2=[[1,0,0],[0,1,0],[0,1,0]]`.

They are idempotent, satisfy braid, and do not commute. Thus no positive
Hermitian metric can make both orthogonal projectors while retaining their
algebraic action. One projective measurement per Demazure step is not the desired
geometric pushforward. Replacing it by a nonnormal filter changes the resource
analysis and reintroduces normalization; the claimed automatic repair fails.

6.1.4 This obstruction does not rule out an algorithm that uses several gates,
ancillas, special input promises, or a different observable. No such repair with
an advantageous classical-output theorem was constructed in this lane.

## 7. Bounded verification and MERGE PROPOSAL

An in-memory numerical exploration enumerated all 21 flags for `n=3,q=2`
and all 52 flags for `n=3,q=3`. The quadratic and ordinary braid errors were
exactly zero; unitary and parameter-dependent braid errors were below `3e-15`.
The six-dimensional Bruhat representation checked the large-field estimate at
`q=2,100,1000000`. For `q=1000000,L=20`, leaving the initial cell had probability
about `7.66e-6`, below the bound `0.001600`. The explicit Demazure matrices also
satisfied braid and had nonzero commutator norm. These are exploratory checks,
not registered red-capable checkers or independent adjudication.

Provisional definitions suitable for review are the weighted flag-gallery task
of section 1 and its prescribed finite-field/circuit encoding. Candidate statements
for an independent critic are the constant-affine no-go of 2.2, deterministic
resource construction of 3.3, Bruhat classical attack of 5.1, large-field bound
of 5.2, and orthogonal-projector obstruction of 6.1.

The spectral operator and Yang--Baxter identity are cited established formulas
after the exact parameter matching in section 4. No originality assertion about
them should be merged. No speedup statement is proposed: the best classical
algorithm has not been adjudicated, and the mechanism already fails D22.
