# Streamed Grassmann states: a matched small-memory classical query algorithm

2026-09-05. Bounded construction and baseline audit for `qaag-mw9`.
This memo uses ordinary real Euclidean spaces inside complex quantum Hilbert
spaces, departing from C1's Fock convention. The quantum state is a normalized
exterior tensor; no seed Hamiltonian or metric is implicit. No claim status is
assigned here, and no new quantum mechanism or separation is asserted.
Canonical input and sketch definitions are D-R5-GRASSMANN-QUERY in
`definitions/mechanism-r5.md`; the registry row is C-352.

## 1. Candidate and the actual access requirement

An input stream supplies mutually orthonormal vectors
`u_1,...,u_k in R^q`. After the stream, a classical unit vector `v` arrives.
The output is the bit distinguishing `v in U` from `v perpendicular to U`,
where `U=span{u_i}`; an additive estimate of `beta=v^T P_U v` is a relaxation.
Vectors are explicitly readable while current. Any coherent preparation and
inverse, compilation, numerical precision and temporary input storage must be
charged to the quantum algorithm. An arbitrary unknown vector copy does not
supply its preparation inverse.

The normalized Slater state `u_1 wedge ... wedge u_k` stores this Grassmannian
point in at most `k ceil(log_2 q)` first-quantized data qubits. Rotate a known
incoming vector to a fixed mode. Orthogonality promises that mode is empty;
occupying it and rotating back adds the vector deterministically. This is an
isometry on the promised empty-mode subspace, extended on its complement.
For the late query, rotate `v` to a fixed mode and measure its occupation.
The occupation probability is `beta`; under the two-sided incidence promise,
the measurement is deterministic and preserves the Slater state.

These are familiar fermionic mode operations. A first-quantized implementation
must also implement insertion/removal of a known mode in the antisymmetric
encoding; simply appending a distinguishable register is not that operation.
Granting efficient insertion only strengthens the candidate being audited.
The general simulation result is classical polynomial time in the number of
modes; it alone does not settle small-memory streaming complexity. See
[DiVincenzo--Terhal, Fermionic Linear Optics Revisited](https://arxiv.org/abs/quant-ph/0403031).

## 2. A small-memory comparator for the same output

The tempting comparator stores all `kq` basis entries. It is unnecessary for a
single late query. Independently choose sign vectors `g,h in {+1,-1}^q`, with
four-wise independence within each vector and independence between the two.
Maintain just

`A = sum_i (g^T u_i)(h^T u_i) = g^T P_U h`.

At the query, form `B=(g^T v)(h^T v)` and output the estimator `Z=A B`.
Independence and the second moments give `E Z=beta`.

For four-wise independent signs and real vectors `a,b`, expansion gives

`E[(a^T g)^2 (b^T g)^2]`
` = ||a||^2 ||b||^2 + 2(a^T b)^2 - 2 sum_j a_j^2 b_j^2`
` <= ||a||^2 ||b||^2 + 2(a^T b)^2`.

Condition first on `g` and use this inequality for `h`. Then

`E Z^2 <= E_g[(v^T g)^2 (g^T P_U g + 2(v^T P_U g)^2)]`.

The first term is at most `k+2 beta` by expanding `P_U=sum_i u_i u_i^T`.
The second is at most `2 beta+4 beta^2`, because `||P_U v||^2=beta`.
Consequently

`Var Z <= E Z^2 <= k+4 beta+4 beta^2 <= k+8 <= 9k` for `k>=1`.

A median of independent means therefore estimates `beta` to additive error
`epsilon`, with failure probability at most `delta`, using

`m=O(k epsilon^(-2) log(1/delta))`

accumulators. Four-wise independent signs need `O(log q)` seed bits per
vector, so no length-`q` random vector need be retained. Each arriving coordinate
contributes to two dot products for each accumulator. Time is `O(mq)` arithmetic
operations per input vector and per query, plus sign-generation overhead;
memory is `O(m)` numeric accumulators and `O(m log q)` seed bits. This is a
bilinear moment sketch in the tradition of
[Alon--Matias--Szegedy](https://web.math.princeton.edu/~nalon/PDFS/amsz4.pdf);
the displayed adaptation and variance calculation are supplied here, rather
than attributed verbatim to that paper.

## 3. Precision and scope of the conclusion

The formula above is an exact-arithmetic statement. For dyadic input coordinates
with a common `b`-bit fractional precision, each stored product sum has common
denominator `2^(2b)` and magnitude at most `kq`; its bit size is
`O(b+log(kq))`. A promise on exact orthonormality and query incidence can instead
refer to nearby ideal vectors, provided their supplied approximation makes
the accumulated projector and query errors smaller than the testing margin.
Arbitrary exact real numbers are not unit-cost finite-bit input.

Including sign seeds, temporary dot products, final estimator products and
group sums, a conservative full working budget is
`O(m*(b+log(kq)+log m))` bits. For fixed `epsilon,delta` and `k<=q`,
this is `O(k*(b+log q))`; at `b=O(log q)` it matches the quantum data-register
scale `O(k log q)`. Larger precision needs its own rounding argument or
charged quantum input and compilation storage, rather than an asserted
precision-independent equality of memory budgets.

For constant error and failure probability, the classical algorithm uses
`O(k)` numeric words, rather than `kq`. In the explicit-coordinate input model,
the quantum proposal has not established an asymptotic memory separation once
word size and coherent compilation storage are counted. There is also no
derived time separation: ordinary unstructured mode rotations across the
occupied particles already involve comparable coordinate-reading work.
This is not a lower bound against every quantum implementation.

The argument covers one query independent of the private sketch randomness.
A fixed list of `L` such queries costs only an additional `log L` in memory by
a union bound. It does **not** prove robustness to arbitrarily many adaptively
chosen queries based on previous sketch outputs. Nor does it settle streaming
nonlinear schemes, arbitrary noisy subspace insertion, or a supplied succinct
rotation-circuit input model. Such extensions require their own baseline and
cannot inherit a separation from comparison against a stored full basis.
