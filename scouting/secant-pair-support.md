# Pair-product support and a sharp four-copy gap

2026-09-05. Independent construction requested by the root. This file uses
ordinary finite-dimensional tensor Hilbert spaces, departing from C1's Fock
convention. Canonical definitions are now in `definitions/secant-pair-support.md`
(D-PAIR-SECANT-SUPPORT and D-PAIR-S4-COMPRESSION). Claim status lives only in
`claims/CLAIMS.md`, C-339--C-341; numerical probes do not promote claims.
Historical novelty has not been checked.

**Result of the probe:** the pair-product support identity is valid for
`t=r+1`. For `t=4`, every nonzero eigenvalue of its compression to globally
symmetric replicas is at least **1/12**, uniformly in party count and local
dimensions. The constant is attained on the local-type pattern `211,211,22`.
The proof below covers all five local `S_4` types, not just the three families
in the initial dense experiment. This produces a constant-gap realization
of the secant's degree-four span by existing product-test operations; generic
support filtering remains an established mechanism and does not satisfy D22.

## 1. Local definitions and the support identity

Use H, X_r, t, S_t, P, B_ab and A_t from D-PAIR-SECANT-SUPPORT. Normalizing
the nonzero cone vectors does not change S_t. B_ab is the usual multipartite
product-test acceptance projector on a pair, with identity on other replicas.
There is no implementation or gap promise implicit in operator support.

### Proposed pair-support theorem

ASSUME these finite-dimensional complex spaces and `t=r+1`.
PROVE

`S_t(X_r)=range(P B_12)=support(A_t)`

and, on `Sym^t(H)`,

`A_t=(1/binom(t,2)) sum_(a<b) B_ab`.

1.1 Expand the `t`th tensor power of a sum of at most `r=t-1` product
vectors. Every monomial in this expansion repeats at least one of them.
After global symmetrization, it therefore belongs to the span of
`P(x tensor x tensor y_1 tensor ... tensor y_(t-2))`, where `x` and all
`y_j` are product vectors. This proves one containment for actual rank
at most `r`; continuity adds the border closure.

1.2 Conversely, the displayed symmetrized tensor is a coefficient in
`(z_0 x+sum_(j=1)^(t-2) z_j y_j)^tensor t`. Multivariate polarization over
`C` expresses each such coefficient as a finite linear combination of values
of this polynomial. Every value is the `t`th power of a sum of at most `r`
product vectors. Thus every displayed tensor belongs to `S_t(X_r)`.

1.3 Local polarization gives
`span{x tensor x:x product}=tensor_i Sym^2(H_i)`, with replicas regrouped
by party. Product vectors span `H` in each remaining replica. The span of
the tensors in 1.1 is consequently exactly `range(P B_12)`.

1.4 In finite dimensions, `range(T)=range(T T^dag)` for every operator `T`.
Taking `T=P B_12` and using `B_12^2=B_12` gives the support statement.

1.5 Conjugating `B_12` by a simultaneous replica permutation yields its
corresponding `B_ab`. Averaging these conjugates gives the pair average,
which commutes with `P`. Therefore `P B_12 P` equals this average on the
range of `P`. The equality with the uncompressed average is not asserted
on the entire unsymmetrized replica space.

## 2. Reduction of the four-copy spectrum

ASSUME `t=4`. PROVE the nonzero spectrum can be reduced to the explicit
small matrices in 2.8 below, for every local-type pattern.

2.1 Local Schur-Weyl decomposition has types `4,31,22,211,1111`. Their Weyl
factors are spectators, since all operators are replica permutations. The
local transposition-fixed subspaces have dimensions respectively `1,2,1,1,0`.
A `1111` factor makes every `B_ab` zero, so contributes no positive spectrum.
Type `4` factors can be removed without changing the spectrum. Write
`a,b,c` for the remaining counts of `31,211,22`.

2.2 Nonzero eigenvalues of `P B_12 P` equal those of `B_12 P B_12` on
`range B_12`: these are the squared nonzero singular values of `P B_12`.
We can therefore compress each local representation to its fixed space
for the transposition `tau=(12)` before averaging the group.

2.3 Realize `V_31` as the sum-zero subspace of `R^4`. In its `tau`-fixed
plane use the orthonormal columns

`u=(1,1,-1,-1)/2`, `v=(0,0,1,-1)/sqrt(2)`;

its unit normal is `n=(1,-1,0,0)/sqrt(2)`. Let
`C_g=[u v]^T R_31(g)[u v]`. The representation `211` is the sign twist
of `31`; its `tau`-fixed line is spanned by `n`. The scalar compression is

`alpha_g=sign(g)<n,R_31(g)n>=det(C_g)`.

The last equality is the cofactor identity for an orthogonal three-dimensional
matrix whose determinant is `sign(g)`.

2.4 Type `22` is the standard representation on the three perfect matchings
of four symbols. Its `tau`-fixed line points toward the matching `12|34`.
Its scalar compression `beta_g` is one if `g` preserves that matching and
`-1/2` otherwise. The compressed group average is consequently

`M_(a,b,c)=(1/24)sum_g det(C_g)^b beta_g^c C_g^tensor a`.

2.5 Decompose `(C^2)^tensor a` under permutation of its `a` equal factors.
The `GL(2)` factor with partition `(a-j,j)` is unitarily identified with
`det^j tensor Sym^ell(C^2)`, where `ell=a-2j`, `0<=j<=floor(a/2)`.
The unitary identification uses the ordinary tensor inner product; the
determinant line has unit norm and symmetric tensors use normalized Dicke
basis vectors. Thus no unnormalized polynomial-basis factors are omitted.
The corresponding small matrix is

`M_(ell,h,c)=(1/24)sum_g det(C_g)^h beta_g^c Sym^ell(C_g)`,
`h=j+b`.

This intertwining identity extends to singular `C_g` by polynomial continuity.
The large multiplicity of a party-permutation irrep changes eigenvalue
multiplicity, not the small matrix's eigenvalues.

2.6 There are only seven plane compression matrices. Define

`F=diag(1,-1)`, `D=diag(-1,0)`,
`C=[[0,1/sqrt(2)],[1/sqrt(2),1/2]]`.

The 24 permutations give `I` twice, `F` twice, `D` four times, and
`F^s C F^t` four times for each `s,t in {0,1}`. The first eight have
`beta_g=1`; the remaining sixteen have `beta_g=-1/2`.
Also `det C=-1/2` and `det F=-1`. This finite list can be checked directly
by permuting the four coordinates of `u,v`.

2.7 On `Sym^ell(C^2)`, let `e` be the all-zero Dicke vector and let `P_h`
select Dicke indices congruent to `h mod 2`. Put `S=Sym^ell(C)`.
For `ell=0` the symmetric power is the scalar representation, including on
singular matrices. A zeroth determinant power is one.

2.8 Substituting the list from 2.6 gives the exact formula

`M_(ell,h,c) = P_h/6`
` + 1_(h=0) (-1)^ell |e><e|/6`
` + (2/3)(-1/2)^(h+c) P_h S P_h`.                  (PAIR-4)

For example, the four `F^s C F^t` terms sum to
`(I+(-1)^h Sym^ell F) S (I+(-1)^h Sym^ell F)=4 P_h S P_h`.
This formula covers arbitrary mixtures of local types, independent of all
Weyl dimensions. If `ell=0` and `h` is odd, `P_h=0` and the block is zero.

## 3. Spectral tools and exact exceptional kernels

The following facts complete the uniform bound without an asymptotic or
numerical extrapolation.

3.1 The symmetric matrix `C` has orthonormal eigenvectors

`f=(1,sqrt(2))/sqrt(3)` with eigenvalue one,
`g=(sqrt(2),-1)/sqrt(3)` with eigenvalue `-1/2`.

For `ell>=1`, put `z=f^tensor ell` and let `y` be normalized symmetrization
of `f^tensor(ell-1) tensor g`. Then `S z=z`, `S y=-y/2`, and all other
eigenvalues of `S` lie in `[-1/8,1/4]`. In particular

`S <= I/4 + 3|z><z|/4`,
`S >= -I/8 - 3|y><y|/8`.                         (OUTLIERS)

The first inequality also holds at `ell=0`. Globally `-I/2<=S<=I`.
After compression by any contraction, these rank-one bounds imply at most
one eigenvalue above `1/4`, or respectively below `-1/8`.

3.2 If `ell` is odd, `P_0 S e=0`: indeed `C e_0=e_1/sqrt(2)`, so its
`ell`th power has odd Dicke index. Thus whenever `h=0` and `ell` is odd,
the vector `e` is an exact kernel vector of (PAIR-4), decoupled from its
orthogonal complement. On that complement the middle term vanishes.

3.3 A useful congruence rule is the following. If `N>=0` and `D_0>=I` is
invertible, every nonzero eigenvalue of `D_0 N D_0` is bounded below by the
smallest nonzero eigenvalue of `N`. Its nonzero spectrum is that of
`N^(1/2) D_0^2 N^(1/2)>=N`. This justifies the normalization used below;
one must not identify congruence with unitary equivalence.

3.4 Write `s=(-1)^ell`, `d_0=3^(-ell/2)`, and `d_1=sqrt(2ell)3^(-ell/2)`.
The identity `C F f=-e_0/sqrt(3)` yields

`P_1 S P_1 z = P_1 z/2`,
`P_0 S P_0 z = (P_0 z+s d_0 e)/2`.              (POS-KERNEL)

For `ell>=1`, the analogous one-excitation computation gives

`P_0 S P_0 y = -(P_0 y+s d_1 e)/4`.             (NEG-KERNEL)

To verify its scalar, `C F g=e_0/sqrt(6)+(sqrt(3)/2)e_1`. In
`S Sym^ell(F)y`, the even-parity part is therefore `-s d_1 e/2`;
averaging it with `S y=-y/2` gives (NEG-KERNEL).

## 4. Sharp uniform gap theorem

ASSUME any finite tensor product, `t=4`, and a nonzero eigenvalue of `A_4`.
PROVE it lies in `[1/12,1]`.

4.1 The upper bound follows because `P B_12 P` is a compression of a
projector. For the lower bound it suffices to check (PAIR-4). Remove the
zero parity sector, and when applicable the decoupled odd-`ell` vector `e`.

4.2 Suppose `h+c>=2`. If this sum is even, its final coefficient is positive
and `S>=-I/2` gives a lower bound
`1/6-(1/3)2^(-(h+c))>=1/12`.
If it is odd, it is at least three and `S<=I` gives
`1/6-(2/3)2^(-(h+c))>=1/12`.
For even `ell` the additional rank-one term, if present, is positive;
for odd `ell` it was removed in 3.2. This proves the assertion in these cases.

4.3 Suppose `h=1,c=0`. The nonzero parity block is
`(I-2 P_1 S P_1)/6`. At `ell=0` it is absent. At every `ell>=1`,
`P_1 z` is nonzero and (POS-KERNEL) supplies an eigenvalue `1/2` of the
compression. By (OUTLIERS), every other eigenvalue is at most `1/4`.
Hence the matrix has one zero eigenvalue and all others at least `1/12`.

4.4 Suppose `h=0,c=1` and `ell` is even. On the even parity space set
`D_0=(I+|e><e|)^(1/2)` and `T=D_0^(-1) P_0 S P_0 D_0^(-1)`.
Six times the matrix is `D_0(I-2T)D_0`.
By (POS-KERNEL), `D_0 P_0 z` is a nonzero eigenvector of `T` with eigenvalue
`1/2`. The contractive rank-one bound (OUTLIERS) puts every other eigenvalue
at most `1/4`. The inner matrix's nonzero gap is at least `1/2`; 3.3 gives
the desired `1/12`. This includes the all-zero matrix at `ell=0`.

4.5 For `h=0,c=1` and odd `ell`, remove `e`. At `ell=1` nothing remains.
For `ell>=3`, `P_0 z-d_0 e` is nonzero, and (POS-KERNEL) gives the same
eigenvalue `1/2` for the remaining compression. Its other eigenvalues are
at most `1/4`, proving the same gap.

4.6 Only `h=c=0` remains. For even `ell>=2` use the same `D_0,T` as in 4.4.
Six times the matrix is now `D_0(I+4T)D_0`.
By (NEG-KERNEL), `D_0 P_0 y` is a nonzero eigenvector with eigenvalue
`-1/4`. The lower rank-one bound (OUTLIERS) places every other eigenvalue
at least `-1/8`. Therefore `I+4T` has one zero and all other eigenvalues
at least `1/2`; congruence again gives the gap `1/12`.

4.7 For `h=c=0` and odd `ell`, first remove `e`. For `ell>=5`, the vector
`P_0 y-d_1 e` is nonzero: its Dicke-index-two coefficient is proportional
to `ell-3`. By (NEG-KERNEL) it is an eigenvector with eigenvalue `-1/4`
of the remaining compression. The lower rank-one bound gives the same
gap for all other eigenvalues. The exceptional degrees are direct:
`ell=0` gives the scalar one; `ell=1` gives only zero; at `ell=3` the
even-parity matrix in (PAIR-4) is `diag(0,1/2)`.

4.8 All possible parameters have now been covered. Sharpness already occurs
at `a=0,b=2,c=1`, hence `ell=0,h=2,c=1`. Formula (PAIR-4) gives
`1/6+(2/3)(-1/2)^3=1/12`. This is the local-type pattern `211,211,22`,
whose nonzero compressed eigenvalue transfers to the globally invariant
sector by 2.2. It exists, for example, with local dimensions `3,3,2`.

Equivalently, if `P_sec` projects onto `S_4(X_3)`, then on the full replica
space, with the stipulated zero extensions,

`P_sec/12 <= A_4 <= P_sec`.

## 5. Algorithmic consequence and originality boundary

5.1 The six pair-product projectors have explicit normalization-one block
encodings: use the ordinary local controlled-swap/product-test ancillas.
Their uniform coherent average costs `O(sum_i log dim H_i+k)` elementary
operations per call. The global `S_4` projector also has a constant-group
block encoding. On an identical four-copy input it can be omitted from the
average, because that average preserves the globally invariant sector.

5.2 The gap theorem permits an approximation of the support projector with
`O(log(1/epsilon))` calls using an established bounded-polynomial singular-
value filter. No inverse preparation of the unknown input is needed: the
four copies are data registers for the known controlled permutations.
Rotation synthesis, ancillas, and approximation error still have their
ordinary costs. This is a mathematical implementation consequence, not a
claim of exact finite-gate perfect completeness or efficient output-state
preparation at arbitrary overlap.

5.3 Thus this direction does not furnish an original D22 mechanism. The
uniform gap makes generic support filtering particularly effective, so it
strengthens the known-algorithm comparison rather than evading it. A new
recovery or coherent-label operation would need a distinct resource theorem
which this existing product-test/filter construction does not already give.
No such operation is claimed in this memo. For `t>4`, the support identity
survives, but no analogous gap theorem has been proved here.

## 6. Finite verification and merge proposal

Independent bounded runs used one BLAS thread and a 60-second timeout.
The compressed symmetric-power recurrence reproduced the initial dense
values. Scanning all-`31` and one-`211` families through 80 parties found the
smallest positive value `0.10010555292677338`, respectively at 7 and 6
parties; both families approach `1/8` in that experiment. This limited
pattern scan did not find the sharp mixed-type value, which the proof does.

A separate run checked 2,989 blocks with `ell<=60`, `h,c<=6`, including direct
24-term group-average comparisons through `ell=12`. Every positive eigenvalue
passed the `1/12` bound, with equality at `(ell,h,c)=(0,2,1)`. Nonzero minima
were separated numerically by a `1e-9` threshold; the proof, not that threshold,
decides the kernels. These runs were unregistered scratch computations and
are not substitutes for a red-capable archived checker and critic pass.

The exact claims are registered as C-339--C-341 in `claims/CLAIMS.md`; their
status lives there. The independent review is `verdicts/secant-pair-support-r1.md`.
The reviewed content comprises:

- Pair support for `t=r+1`, with finite-dimensional complex spaces and the
  symmetric-sector qualification in §1.
- The complete `S_4` compressed-block formula (PAIR-4), including its metric
  normalization, singular symmetric-power convention, and all local types.
- The sharp uniform nonzero gap `1/12` at four copies, §§3--4.
- The resulting implementation by known product-test block encodings and
  generic support filtering, with charged precision and no D22 promotion.

The new-mechanism claim remains unsupported. Historical novelty of the
spanning/gap results requires a separate targeted check before any such label.
