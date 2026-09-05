# Theta-isogeny input, metric and readout

2026-09-05. This section-space model departs from C1's Fock convention.
Conjugated evaluation kets follow C3. Symbols here are local to the theta
construction; neither the level nor the genus denotes a seed parameter.
The divisor symbol D_xi locally departs from the reserved D convention C8.

## D-THETA-ISOGENY

Let `g,k>=1` and let `Omega` be a symmetric complex `g` by `g`
matrix with `Y=Im(Omega)>0`. The marked principally polarized abelian variety is
`A=C^g/(Z^g+Omega Z^g)` with its standard symmetric theta line bundle `L`.
Coordinates, marking and theta structure are supplied conventions.
For level `n>=1`, index `j in {0,...,n-1}^g` and
`xi=(alpha,beta) in {0,1/2}^g times {0,1/2}^g`, define

`theta_(n,j)^xi(z)=sum_(ell congruent j mod n)`
` exp[pi i (ell+alpha)^T Omega (ell+alpha)/n`
`       +2 pi i (ell+alpha)^T(z+beta/n)]`.

The space `H_n^xi` consists of sections of `L^n tensor F_xi`, where the
unitary flat bundle has multipliers `exp(2 pi i alpha.a)` on integral
translations and `exp(-2 pi i beta.a)` on `Omega a` translations.
Use the Gaussian cubist metric
`h_n(z)=exp[-2 pi n Im(z)^T Y^(-1) Im(z)]` and normalized Haar measure
`dx dy`, `z=x+Omega y`, on a fundamental domain. Set
`phi_(n,j)^xi=det(2nY)^(1/4) theta_(n,j)^xi`.

On specified lifts and fibre frames let
`e_n^xi(z)=sqrt(h_n(z))sum_j conjugate(phi_(n,j)^xi(z))|j>`,
`B_n^xi(z)=||e_n^xi(z)||^2` and
`E_n^xi(z)=e_n^xi(z)/sqrt(B_n^xi(z))` when the denominator is positive.
Omitted `xi` means `(0,0)`. The isogeny is
`mu(P,Q)=(P+Q,P-Q)`. The quantum source supplies fresh independent pairs
`E_(2k)(P) tensor E_(2k)(Q)` in the known coefficient bases, with charged
source preparation or copy cost. It supplies no points, inverse preparation
or amplitude queries by implication.

## D-THETA-SECTOR-TRANSFORM

Let `sigma=2alpha,delta=2beta in {0,1}^g`, and let
`j,l in {0,...,k-1}^g`. The map `J` from
`direct-sum_xi H_k^xi tensor H_k^xi` to
`H_(2k) tensor H_(2k)` has columns

`J|sigma,delta;j,l>=2^(-g/2)sum_(epsilon in {0,1}^g)`
` exp[pi i delta.(j+l+sigma+k epsilon)/k]`
` |[j+l+sigma+k epsilon]_(2k),[j-l+k epsilon]_(2k)>`.

The implemented operation is `J^dagger`; its sector is `(sigma,delta)`
and its decoded computational labels are `(j,l)`. Put
`w_xi=B_k^xi(P+Q)B_k^xi(P-Q)/(B_(2k)(P)B_(2k)(Q))`.
Only positive-weight branches have normalized conditional states.
No identification of a flat-twisted output with an ordinary same-point
evaluation state is implicit.

For each level-`2k` coordinate let `X|a>=|a+1 mod 2k>` and
`Z|a>=exp(2 pi i a/(2k))|a>`. On the source pair let
`G_r=Z_r^k tensor Z_r^k` and `H_r=X_r^k tensor X_r^k`.
The sector projector `Pi_(sigma,delta)` is their simultaneous eigenspace
with eigenvalues `(-1)^sigma_r` and `(-1)^delta_r`.

## D-THETA-CLASSICAL-OUTPUTS

The fixed-sector bit distinguishes `w_xi=0` from `w_xi>=gamma>0`.
For `k=1`, if `D_xi` is the divisor of the unique section of `L tensor F_xi`,
this is containment in the pullback under `mu` of
`(D_xi times A) union (A times D_xi)`, versus the stated positive margin.
An allowed separate-source protocol measures each source individually with
known observables and then classically processes the outcomes; it need not
recover a point or its coefficient list.
At every odd k the sector-probability ceiling is 2^(-g); a nonempty positive
promise family must choose gamma at or below that ceiling. At even k, the
complete sector string is reproducible by separate-source Weyl measurements
and XOR of their local eigenbits; this statement concerns the classical output.

A different, explicitly stronger classical-access model supplies sampling
from computational probabilities and queries to both normalized coefficient
vectors of length `N=(2k)^g`. Its output is one sample of the complete
decoded computational law `(sigma,delta;j,l)` or its sector marginal.
Exact arithmetic gives an exact sampler. Approximate vector access or entry
queries must charge precision; this access is not inferred from source copies.
An arbitrary further quantum circuit or the coherent output state is not
part of this classical sampling output.
