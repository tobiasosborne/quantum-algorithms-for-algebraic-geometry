# Framed Hall correspondences and a quiver-obstruction query

2026-09-05. Field-labelled quantum basis states are orthonormal, departing
from C1. The local field order q departs from C2's seed convention. The
symbol 1 in a module automorphism denotes identity, a local C6 departure.
No moduli-space canonicalization or coherent fibre erasure is an input oracle.

## D-HALL-A2-EXTENSIONS

Let q be a finite-field order. Counting statements apply to every q; the
binary circuit model takes `q=2^s`, `s>=1`, with a supplied irreducible
polynomial defining field arithmetic. For the quiver `1 -> 2`, let
`N_a:F_q^(n_1)->F_q^(n_2)` and
`M_a:F_q^(m_1)->F_q^(m_2)` be explicit matrices with fixed vertex bases.
All four dimensions are nonnegative integers. Write

`C^1=Mat_(n_2 by m_1)(F_q)`,
`C^0=Hom(M_1,N_1) direct-sum Hom(M_2,N_2)`,
`d(f_1,f_2)=N_a f_1-f_2 M_a`,
`E_(X),a=[[N_a,X],[0,M_a]]` for `X in C^1`.

The elementary sampling input chooses X uniformly. Its quantum version is
the uniform superposition of the displayed framed matrices, with the standard
submodule and quotient retained. Quotient-class output means the coset of X
in `C^1/im d`, with any quotient-basis computation charged.
For the zero-arrow subfamily `N_a=M_a=0`, a middle-object isomorphism-class
sample means the integer rank of X, not an explicit list of every orbit.

For a fixed middle representation E, let `F_(MN)^E` count submodules
isomorphic to N with quotient isomorphic to M. Put `a_A=|Aut(A)|` and
`h=|Hom(M,N)|`, including the zero homomorphism. The set
`Ext^1(M,N)_E` comprises extension classes with middle object isomorphic to E.
Flags, endpoint-framed exact sequences and extension classes are distinct
finite sets and carry their own measures.

## D-HALL-FLAG-FORGETTING

Let `f:mathcal X->mathcal Y` be a specified map of finite framed sets,
with `mathcal Y=f(mathcal X)` nonempty. Set
`F_y=|f^(-1)(y)|`, `F_max=max_y F_y`, and
`omega_y=F_y^(-1/2)sum_(f(x)=y)|x>`.
The raw counting map is `T|x>=|f(x)>`. The normalized-coarea map is
`C|x>=F_(f(x))^(-1/2)|f(x)>`. Their operator identities do not include a
cheap unitary completion, fibre-coordinate algorithm or isomorphism oracle.
Retaining the full flag uses the injective map `|x> -> |f(x),x>` instead.

## D-HALL-YONEDA-QUERY

For the bound quiver `1 -> 2 -> 3` with length-two path equal to zero,
let `a,b,c>=1` and supply explicit fixed matrices
`X in Mat_(b by a)(F_(2^s))`, `Y in Mat_(c by b)(F_(2^s))`.
The classical output is membership in the variety of complexes `YX=0`.
Let `r=rank(YX)` and `0<delta<1` be the error tolerance.

The quantum auxiliary basis is `|u,v,w>` with
`u in F_q^a,v in F_q^b,w in F_q^c`. Define

`S_X|u,v,w>=|u,v+Xu,w>`,
`T_Y|u,v,w>=|u,v,w+Yv>`,
`C_(X,Y)=T_Y S_X T_Y^(-1) S_X^(-1)`.

The initial auxiliary state is `q^(-a/2)sum_u |u,0,0>`.
The event measured is `w!=0`. Matrix input, gate compilation and auxiliary
storage are charged. These auxiliary shears are not vertex-preserving
isomorphisms of the input representation. They are ordinary controlled
arithmetic on a probe vector; X,Y are not quantum-superposed programs.
