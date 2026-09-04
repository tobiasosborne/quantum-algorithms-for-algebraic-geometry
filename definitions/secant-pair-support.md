# Pair-support definitions

2026-09-05. Ordinary finite-dimensional complex tensor Hilbert spaces are used;
this explicitly departs from C1's Fock convention and C2's variable notation.
No historical novelty or spectral guarantee is implicit in these definitions.

## D-PAIR-SECANT-SUPPORT

Let `H=tensor_(i=1)^k H_i`, with `k>=1` and positive finite local dimensions.
For `r>=1`, let `X_r` be the nonzero affine cone of tensors of border rank at
most r, and put `t=r+1`. Define
`S_t(X_r)=span_C{x^tensor t:x in X_r}` and its orthogonal projector `P_sec`.

Let `P` be the global replica symmetrizer onto `Sym^t(H)`. For `1<=a<b<=t`,
let `B_ab=tensor_i (1+Swap_i(a,b))/2`, with identity on the other replicas.
Define `A_t=P B_12 P`, with zero extension off `Sym^t(H)`. Operator support
means the orthogonal complement of its kernel. Any equality of `A_t` with
the uncompressed average of `B_ab` must specify the globally symmetric sector.

## D-PAIR-S4-COMPRESSION

At `t=4` the five local replica types are `4,31,22,211,1111`. After removing
trivial type 4, denote the counts of `31,211,22` by `a,b,c`. A `1111` factor
has no transposition-fixed vectors. In the real sum-zero standard representation
on four coordinates, choose
`u=(1,1,-1,-1)/2`, `v=(0,0,1,-1)/sqrt(2)`, `n=(1,-1,0,0)/sqrt(2)`.
The transposition `(12)` fixes the orthonormal plane `[u v]`.
For a permutation g let `C_g=[u v]^T R_31(g)[u v]`,
`alpha_g=sign(g)<n,R_31(g)n>`, and let `beta_g` be one if g preserves the
perfect matching `12|34`, and `-1/2` otherwise. These alpha values are line
compressions, not block-encoding normalizations.

The compression to `range B_12` is represented by
`M_(a,b,c)=(1/24)sum_g det(C_g)^b beta_g^c C_g^tensor a` once the cofactor
identity is established. In the party-permutation block `(a-j,j)`, set
`ell=a-2j`, `h=j+b`, with `0<=j<=floor(a/2)`.

Use normalized Dicke bases for all symmetric powers. Define
`F=diag(1,-1)`, `D=diag(-1,0)`,
`C=[[0,1/sqrt(2)],[1/sqrt(2),1/2]]`, `S=Sym^ell(C)`.
Let `e` be the Dicke vector of weight zero and `P_h` the projector onto
Dicke indices congruent to h modulo two. The zeroth symmetric power of
every matrix is the scalar one, even for a singular matrix, and a zeroth
determinant power is one. Define the proposed small-block expression
`M_(ell,h,c)=P_h/6 + 1_(h=0)(-1)^ell |e><e|/6`
`             +(2/3)(-1/2)^(h+c) P_h S P_h`.
Equality with the group compression is C-340, not a definitional assumption.
