# Higher-obstruction r10: cyclic fat points and access diagnostics

2026-09-05, root derivation. Use the ordinary finite-dimensional Hermitian
conventions of `definitions/higher-obstruction.md`, departing from C1/C2
as stated there. This is an independent comparison note for the constructor
and critic, not a canonical claim-status assignment. The monitored procedure
is separately being checked against quantum first-return prior work.

## 1. An exact geometric family

**1.1 ASSUME** D-HIGHER-CYCLIC-FIXTURE. **PROVE** the polynomial cokernel of
F(t) is isomorphic to C[t]/(t^ell).

**1.2** The internal block G=mathbb1+t E is unimodular over C[t], since E is
nilpotent of index ell-1 and det(G)=1. Its inverse is the finite geometric
series sum_(j=0)^(ell-2) (-t E)^j. The endpoint Schur complement from
D-HIGHER-OBSTRUCTION-PENCIL is therefore

`S(t)=(-1)^(ell-1) t^ell`.

Indeed B E^j C vanishes unless j=ell-2, when it equals1.

**1.3** Block Gaussian elimination by polynomial unimodular row/column
matrices takes F to diag(S,G), and G is polynomially invertible. Multiplying
the scalar block by its unit sign yields the asserted cokernel. As a
coherent sheaf, it is the length-ell nonreduced point at the origin of the
affine line. Unlike a general matrix coefficient query, this scalar order
has an intrinsic local-module interpretation. No claim about a general
Massey product or unobstructed deformation functor follows.

## 2. Its small singular value is not a universal information barrier

**2.1 ASSUME** additionally 0<t<=1/2. Set N=U^dagger Q. This is the truncated
backward shift: N e_0=0 and N e_j=e_(j-1) for j>=1. Thus N^ell=0 and

`U^dagger F(t)=N+t mathbb1`.

Multiplication by U^dagger preserves singular values.

**2.2** Its inverse is sum_(j=0)^(ell-1) (-N)^j/t^(j+1). The triangle
inequality and ||N^j||<=1 give

`||F(t)^(-1)|| <= (1-t^ell)/((1-t)t^ell)`.

Hence sigma_min(F(t))>=(1-t)t^ell/(1-t^ell).

**2.3** The vector v=sum_(j=0)^(ell-1) (-t)^j e_j obeys
`(N+t mathbb1)v=(-1)^(ell-1)t^ell e_(ell-1)` and
`||v||^2=(1-t^(2ell))/(1-t^2)`. Therefore

`(1-t)t^ell/(1-t^ell) <= sigma_min(F(t))`
`   <= t^ell sqrt((1-t^2)/(1-t^(2ell))) <= t^ell`.

In particular this singular value is Theta(t^ell), uniformly for t<=1/2,
while ||F(t)||<=1+t. The smallest eigenvalue of F^dagger F is consequently
Theta(t^(2ell)); the nonzero gap of its Hermitian off-diagonal dilation is
Theta(t^ell). Any invocation of a gap-resolution routine must charge the
resolution it actually uses. These facts are NOT a lower bound on all
algorithms for the module task.

## 3. Direct monitored readout and a matched classical method

**3.1** Prepare e_0. Apply U, test P versus Q after each step, and stop at
the first P event. The first ell-1 measurements return Q with certainty;
the ell-th returns P with certainty. This samples the first-return time
ell without t-dependent attenuation. Its first-return amplitude is exactly
the coefficient of S(t), up to the sign in section1.

**3.2** A classical procedure starts with label0, applies the supplied same
cycle permutation, and records the first return to0. It produces the
identical deterministic answer in ell forward steps and O(log ell) bits.
Both step descriptions can use reversible modular increment at polynomial
cost in log ell. If the cycle length is explicitly supplied, it is already
known classically; the trajectory experiment is then only a hardware
illustration, not a hard input family or a query lower bound.

**3.3** Thus small spectral gaps do not by themselves establish difficulty
of this geometric output. The direct monitored operation escapes that
particular spectral readout, and the displayed classical method escapes it
too. This is not a dequantization of general unitary colligations: arbitrary
succinct circuits can have complicated interference and endpoint statistics.

## 4. The constant-section query is not unrestricted lifting

**4.1 ASSUME** D-HIGHER-OBSTRUCTION-PENCIL with K_in=K_out=C^2,
L_in=L_out=C, A=[[0,1],[0,0]], B=[[-1],[0]], C=[[1,0]],
D_0=1 and E=0, and x=e_1 in the two-dimensional endpoint basis.
Then S_1 x=0 but S_2 x=e_1 is nonzero.

**4.2** Nevertheless the endpoint series x(t)=e_1-t e_2 and internal
series y(t)=-t satisfy F(t)(x(t),y(t))=0 identically. The putative second
obstruction is removable by changing the endpoint section at first order.
It lies in the image of S_1. An intrinsic lifting obstruction therefore
needs the appropriate earlier-page quotient/gauge data; the raw coefficient
norm in a supplied splitting is a different computational question.

## 5. Bounded diagnostics and scope

The identities above are derived algebraically. Small exact symbolic and
floating-point checks can diagnose signs and normalization, but do not
replace the uniform proof. No originality, general classical simulation,
or universal spectral lower bound is asserted. The author and independent
critic evaluate the actual candidate instrument and its rescaled variants
in their separate r10 documents.
