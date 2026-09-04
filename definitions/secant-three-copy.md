# Definitions for the three-copy secant construction

2026-09-05. This file uses ordinary finite-dimensional tensor Hilbert spaces,
explicitly departing from C1's Fock convention and C2's projective-variable
notation. Here `k` counts tensor factors, `q_i` are local dimensions, and no
annihilation operators or coherent-point conjugation convention is used.
These definitions do not assert a theorem or historical novelty.

## D-S3-SECANT

Let `H = H_1 tensor ... tensor H_k`, `H_i = C^{q_i}`, with specified computational
bases and their standard Hermitian inner products. All `q_i >= 2`. Let `X_2`
be the intersection of the unit sphere with the affine Zariski closure of
`{a_1 tensor ... tensor a_k + b_1 tensor ... tensor b_k}`. Its projectivization
is the second secant variety of the Segre variety. It includes tangent limits;
it is not the locus of tensors of actual rank exactly two.

For unit `psi`, let
`distance_2(psi) = min_{phi in X_2} sqrt(1-|<phi,psi>|^2)`.
The input consists of independent copies of one unknown pure `psi`, the tensor
register decomposition, local dimensions, and positive rational accuracy and
failure parameters. It does not supply a preparation circuit or its inverse.

The classical comparator may perform arbitrary adaptive global POVMs on one
whole copy at a time, with unlimited classical computation and classical memory,
but may not retain quantum memory between copies.

## D-S3-CUBIC-SPAN

Let `S_3(X_2) = span_C {phi^{tensor 3}: phi in X_2}` and let `P_3` be its
orthogonal projector, extended by zero off `Sym^3(H)`. Define the cubic residual
`r_3(psi) = 1 - <psi^{tensor 3}, P_3 psi^{tensor 3}>`.
This is a probability, not the geometric distance itself. The dual annihilator
of this span is the degree-three vanishing ideal, with coefficient conjugation
handled by the ordinary Hermitian identification.

## D-S3-LOCAL-REPRESENTATION

The group `S_3` acts by permuting three replicas of `H_i`. Its local decomposition
is `H_i^{tensor 3} = direct_sum_lambda U_{lambda,i} tensor V_lambda` for
`lambda in {(3),(2,1),(1,1,1)}`. The symmetric and alternating representation
spaces have dimension one; the standard representation `V_(2,1)` has dimension
two. The `U` spaces carry the corresponding Schur functors of `H_i`.

Use the real standard representation on the sum-zero plane in `C^3` with
orthonormal basis `(2,-1,-1)/sqrt(6), (0,1,-1)/sqrt(2)`. Projection of the three
coordinate vectors onto this plane gives, after normalization, the trine vectors
`v_0=(1,0)`, `v_1=(-1/2,sqrt(3)/2)`, `v_2=(-1/2,-sqrt(3)/2)`.
For `m>=2`, define
`w_m = sum_{j=0}^2 v_j^{tensor m} / sqrt(3+6(-1/2)^m)`.
For `m=0` use the scalar unit vector; for `m=1` the sum is zero and there is no
accepted multiplicity line.

## D-S3-ROBUSTNESS-CONSTANT

For fixed `k` and rational `0<t<1`, let
`g_k(t)=min {r_3(phi): phi in (C^2)^{tensor k}, ||phi||=1, distance_2(phi)>=t}`.
If the constraint set is empty, set `g_k(t)=1`. Positivity and computability are
claims requiring proof. A certified positive rational lower bound may replace
`g_k(t)` in algorithms. Computing this bound is preprocessing, charged as a
function of `k,t`; it is not claimed polynomial in either.

For rational `0<epsilon<1`, define
`eta_k(epsilon)=min{epsilon^4/(96 k^2), g_k(epsilon/2)^2/(4096 k^2)}`.
This convention does not hide a promised spectral gap: the proposed theorem
must establish its strict positivity and a finite procedure for lower-bounding it.
