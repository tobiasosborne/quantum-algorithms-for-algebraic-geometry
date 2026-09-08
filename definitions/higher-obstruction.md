# Finite obstruction-transfer input model

2026-09-05. This exploratory model uses ordinary finite-dimensional Hermitian
spaces, explicitly departing from C1. Its dimensions are independent of the
polynomial-variable convention C2. No polynomial/coherent-state conjugation
identification is assumed (C3). These definitions specify a candidate family;
they do not establish an algorithm, geometric realization or novelty claim.

## D-HIGHER-OBSTRUCTION-PENCIL

Let K_in, K_out and L_in, L_out be finite-dimensional Hermitian spaces, with
L_in and L_out of equal dimension m. The endpoint dimensions may differ.
Let A:K_in->K_out, B:L_in->K_out, C:K_in->L_out,
D_0:L_in->L_out and E:L_in->L_out be supplied linear maps, with D_0
invertible. In declared orthonormal bases define the two-term complex over
C[t] by the single map

`F(t) = [[t A, t B], [t C, D_0+t E]]`.

It is a two-term complex because no consecutive nonzero differentials occur;
no unmentioned square-zero constraints on these five blocks are imposed.
At t=0, D_0 is a contractible block. Formal elimination defines

`S(t) = t A - t^2 B (D_0+t E)^(-1) C`
`     = sum_(k>=1) t^k S_k`,

with `S_1=A` and `S_k=(-1)^(k-1) B (D_0^(-1)E)^(k-2) D_0^(-1) C`
for k>=2. The formal identities need no numerical convergence assumption.
Analytic use of a Neumann series requires a separately stated domain.
S_k are coefficients in the supplied splitting. Calling them intrinsic
higher differentials requires an additional quotient/gauge-independence
argument, which is not included in the definition.

## D-HIGHER-OBSTRUCTION-QUERY

For a supplied unit endpoint x in K_in, a positive integer ell, and a
specified rational gamma>0, the candidate bit task promises
`S_1 x=...=S_(ell-1)x=0` and asks to distinguish
`S_ell x=0` from `||S_ell x||>=gamma`.

The input includes explicit descriptions of the splitting, metric and norm
scales. When classical coefficient lists are supplied, their lengths and
bit precisions are charged. Under a succinct-access variant, each sparse
entry/location or block-encoding oracle, its cost, normalization and inverse
access must be separately stated. A circuit preparing x and its inverse,
if used, are charged resources. A classical comparison must have the same
input access and the same output bit, not an entire printed cohomology basis.
No finite-gap, resonant preparation or endpoint reflection is free.

## D-HIGHER-OBSTRUCTION-REALIZATION

A geometric use-case claim must exhibit the pencil as a finite complex of
vector bundles or modules arising from a stated algebraic family, and prove
what the output bit says about that family. A general C[t]-module
presentation is a coherent sheaf on the affine line; stronger claims about
Ext, Massey products, deformation obstructions or a spectral-sequence page
require the additional data and identification theorem. The supplied metric
and splitting remain part of the computational input.

## D-HIGHER-CYCLIC-FIXTURE

For ell>=2 take H=C^ell with orthonormal coordinate basis e_0,...,e_(ell-1),
endpoint P=|e_0><e_0|, internal projector Q=mathbb1-P and unitary
`U e_j=e_((j+1) mod ell)`. Its colligation blocks are A=0,
`B=e_(ell-1)^*`, `C=e_1` and the truncated forward shift E on QH.
Set D_0=mathbb1_(QH). The resulting square pencil is `F(t)=Q+t U`.
For analytic singular-value comparisons restrict real `0<t<=1/2`.

The input basis and forward cycle are supplied, rather than a hidden
conjugating basis. State e_0 is free of a state-loading ambiguity; its
preparation and the reversible modular increment still have ordinary
circuit costs. A classical method can evaluate the same cycle permutation.
A comparison for this fixture is not a simulation theorem for arbitrary
succinctly given unitaries or a universal bound for all obstruction queries.
