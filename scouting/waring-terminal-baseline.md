# A terminal classical-output separation for Waring component packets

2026-09-05. This memo gives a concrete terminal component-property query and a
proof of a copy separation against arbitrary adaptive global measurements on
one original source copy at a time. It uses the standard tensor Hermitian norm,
departing from C1; each Waring component space has the supplied bipartition
`C^q=C^d tensor C^d`, with `q=d^2` and `d>=20`. Displayed I denotes identity
and D_omega a representation dimension, local departures from C6 and C8.
Canonical problem D-WARING-TERMINAL-QUERY is in `definitions/waring-components.md`;
C-345 in the claims register carries status, and its independent review is
`verdicts/waring-terminal-baseline-r1.md`.

The result is a formal copy-access separation. Its quantum constants are very
large. It neither proves practical advantage nor establishes that determinant
fusion, coded fusion, or any other proposed packet mechanism is historically
original or necessary. The classical output is one bit about the Waring points;
neither component coordinate lists nor output quantum packets are the comparator.

## 1. The terminal problem

Fix Waring rank `r=4` and source order `k=4`. The input supplies fresh copies of

`T=sum_(a=1)^4 c_a u_a^(tensor 4)`, `||T||=1`, `||u_a||=1`,

where the four component vectors are linearly independent. Their coordinates,
coefficients, preparation circuits, and inverse source circuit are not supplied.
Use the identifiable independent-component family of
`scouting/fresh-mechanism-round4.md` and `scouting/waring-coded-fusion.md`.
The supplied promises are

`G=(<u_a,u_b>) >= (1/2) 1`, and `p_0>=1/512`,

where `p_0` is the determinant seed probability in the coded-fusion memo, (12).
These are access promises, not quantities the algorithm gets to evaluate freely.

Let `rho_A(u)=Tr_B |u><u|`, and define

`Gamma(T)=(1/4) sum_(a=1)^4 e_5(rho_A(u_a))`.

Here `e_5` is the fifth elementary symmetric polynomial of the eigenvalues.
If a normalized component is viewed as a `d`-by-`d` coefficient matrix, Cauchy--
Binet identifies `e_5` with the sum of squared absolute values of all its `5x5`
minors. Therefore `Gamma(T)=0` exactly when all four Waring points lie on the
matrix-rank-at-most-four determinantal variety.

**Terminal promise:** either `Gamma(T)=0`, or `Gamma(T)>=gamma`, with the
fixed constant `gamma=10^(-6)`. Return the corresponding YES/NO bit with
probability at least `2/3`. This is a normalized geometric residual promise;
it is not a demand to compute unnormalized minors or reconstruct any component.

No separate query state is provided. The terminal measurement is the explicit
five-copy exterior-rank measurement described in section 2.

**Comparator:** any POVM acting jointly on every register of one original
`T` copy, including all four component slots and both internal sides, followed
by unrestricted classical memory, computation, randomness, and adaptation.
Fresh ancillas are allowed within that measurement. No quantum information
from an original copy is retained into the processing of the next original copy.

**Derived separation:** the packet procedure uses a number of original source
copies bounded independently of `d`, including all failures and restarts.
Every comparator using at most `N` original copies must satisfy

`N >= sqrt(d)/(sqrt(24) k) = q^(1/4)/(4 sqrt(24))`.

The upper bound is uniform over the full stated Waring promise, including
nonorthogonal components, arbitrary allowed weights, and overlapping supports
on the internal bipartite sides. The lower bound uses a particularly structured
orthogonal subfamily. This is a standard restriction for a lower-bound proof;
it is not an assertion that this subfamily requires fusion specifically.

## 2. The actual quantum upper bound, including packet costs

### 2.1 Extracting a sufficiently accurate five-copy component mixture

For a normalized permutation packet `Omega_m^sigma` from the coded-fusion memo,
retain five slots of its first row and discard all other rows and slots. Write
`mu=max_(a!=b)|<u_a,u_b>|`. The Gram promise implies `mu<=1/2` by its two-by-two
principal submatrices.

ASSUME `m>=5` and `(r!-1)mu^(2m)<=1/2`. PROVE that the retained marginal is
within trace distance `2(r!-1)mu^(2m-5)` of `Sigma_5=(1/r)sum_a |u_a^5><u_a^5|`.

2.1.1 In the squared packet norm, there are `r!` diagonal permutation pairs.
Distinct permutations differ in at least two rows, so every cross term has
absolute value at most `mu^(2m)`. Thus the squared norm `Z` satisfies

`|Z-r!|<=r!(r!-1)mu^(2m)`, and `Z>=r!/2`.

2.1.2 In the reduced density numerator, diagonal terms sum to `r! Sigma_5`.
For a cross pair whose first-row labels differ, one other row also differs,
giving a partial-trace coefficient at most `mu^m mu^(m-5)`. If first-row labels
agree, at least two other rows differ, giving the stronger `mu^(2m)` bound.
The rank-one retained operator in either case has trace norm one.

2.1.3 The triangle inequality and the normalization discrepancy therefore give

`(1/2)||rho_(m,5)-Sigma_5||_1`
`<= (1/(2Z)) r!(r!-1)[mu^(2m)+mu^(2m-5)]`
`<=2(r!-1)mu^(2m-5)`.

For `r=4`, binary coding has `b=2` and attainable row degrees `m_j=2+2^j`.
Choose `j=4`, so `m=18`. The trace error is bounded by

`46/2^31 < 2.143*10^(-8) < gamma/30`.

### 2.2 The terminal measurement and one-bit rule

On the five retained components, apply the alternating projector to the five
`A` registers and ignore the `B` registers. Its rejection probability on
`u_a^(tensor 5)` is exactly `e_5(rho_A(u_a))`. It is implemented by the signed
average of the 120 register permutations, or the equivalent fixed-size Schur
measurement, with `O(log d)` elementary gate dependence on dimension.

On the approximate mixture, its rejection probability differs from `Gamma(T)`
by at most `gamma/30`. Make `B=ceil(3/gamma)=3,000,000` independent trials and
return NO if any trial rejects.

For a YES input, the probability of any rejection is at most `B gamma/30=1/10`.
For a NO input, the probability of no rejection is at most
`exp[-B(29 gamma/30)]<=exp(-2.9)<1/6`.

### 2.3 No rank or restart cost is hidden

The general coded-fusion bound, memo (15)--(16), gives

`f_*=(1/2)^12/(4!)^5=1/32,614,907,904`,

`Cbar_4=(4/(1/512))(2/f_*)^4`
`       =37,077,851,528,602,707,333,906,344,250,393,377,236,014,071,808`.

This is an expected original-source-copy upper bound **per packet trial**.
It is approximately `3.71*10^46`, not an experimentally reasonable constant.
Cap the entire `B`-trial execution at `6 B Cbar_4` source calls. Markov's
inequality makes the abort probability at most `1/6` for every promised input.
Combining this with the preceding decision errors gives success at least `2/3`.
All constants are independent of `d`; no conclusion about practical sizes follows.

The coherent register cost is `O(rm log q+r log r)` as in the construction memo.
Every source preparation cost `G_T`, if specified, is multiplied by the number
of actual source calls. Outside source generation, the dimension dependence of
the elementary gates is polynomial in `log q`; synthesis precision can be chosen
against the known finite execution cap. No unknown basis change is supplied free.
Allocate at most 1/30 total compiled-channel error over the entire capped
experiment. The displayed decision-plus-abort bounds have enough margin to
retain success at least 2/3 after this additional error.

On the orthogonal hard ensemble below the output mixture is exact already at
`m=6`, and the exact two-fusion packet cost is

`4^5 [2(4!)^3]^2 = 782,757,789,696`

source copies in expectation. The seed alone costs `4^5=1024`. Even this much
better special-family value is very large, and it does not replace the uniform
upper bound needed for the full terminal problem.

## 3. Two explicit component spectra with matching accessible moments

Define the YES spectrum, padded to length five, by

`lambda=(1/10,2/10,3/10,4/10,0)`.

Define the NO spectrum `nu` as the five roots of

`P(z)=z(z-1/10)(z-2/10)(z-3/10)(z-4/10)-10^(-6)`.

3.1 Direct rational endpoint evaluation gives opposite signs on each of

`(0,1/100)`, `(9/100,11/100)`, `(19/100,21/100)`,
`(29/100,31/100)`, `(39/100,41/100)`.

There are five disjoint positive-root intervals and the polynomial has degree
five, so all roots are positive and real. Their sum is one by the coefficient
of `z^4`. Thus both displayed vectors are valid Schmidt probability spectra.

3.2 Only the constant coefficient was changed. Their elementary symmetric
polynomials, hence their power sums, agree through degree four:

`sum_j lambda_j^s=sum_j nu_j^s` for `s=1,2,3,4`.

Their fifth elementary symmetric polynomials are respectively zero and
`10^(-6)=gamma`.

3.3 If `v` is the smallest NO root, then `0<v<1/100` and

`10^(-6)=v product_(j=1)^4(j/10-v) < (24/10^4)v`.

Thus `v>1/2400`. Every NO component has pure-state trace distance greater than
`1/sqrt(2400)>1/50` from the rank-at-most-four determinantal variety. The
residual gap is therefore not caused merely by a vanishing distance promise.

## 4. Hard Waring sources, with no accessible component labels

For `d>=20`, choose orthonormal vectors `e_(a,j)` on each local side, where
`a=1,...,4` and `j=1,...,5`. For a spectrum `theta in {lambda,nu}`, define

`w_a(theta)=sum_(j=1)^5 sqrt(theta_j) e_(a,j) tensor e_(a,j)`.

Sample independent Haar unitary matrices `U,V in U(d)` once and keep them fixed
for the entire source. Set

`u_a(theta;U,V)=(U tensor V)w_a(theta)`,

`T_theta(U,V)=(1/2)sum_(a=1)^4 u_a(theta;U,V)^(tensor k)`, `k=4`.

The unknown shared local basis changes are not revealed as classical circuits
or extra quantum reference states. The four components are orthonormal, so
`||T_theta||=1`, `G=1`, and the seed probability is `4^(-4)>=1/512`.
Every source in the YES ensemble has `Gamma=0`; every source in the NO ensemble
has `Gamma=gamma`.

### 4.1 Identical averages for one whole original source copy

ASSUME the two spectra in section 3. PROVE

`E_(U,V) |T_lambda(U,V)><T_lambda(U,V)|`
`=E_(U,V) |T_nu(U,V)><T_nu(U,V)| =: M`.

4.1.1 The local twirl on the `A^k` and `B^k` registers is the orthogonal
projection onto the commutant spanned by `P_pi^A tensor P_sigma^B`, for
`pi,sigma in S_k`. This follows from Schur--Weyl duality.

4.1.2 For component labels `a!=b`, the matrix coefficient
`<w_b^k|P_pi^A tensor P_sigma^B|w_a^k>` is zero. Their supports are orthogonal
on each side, and permuting the slots does not change those supports. Thus
all intercomponent coherence terms vanish under this one-source twirl.

4.1.3 A diagonal component contraction is

`<w_a(theta)^k|P_pi^A tensor P_sigma^B|w_a(theta)^k>`
`=product_(cycles c of pi^(-1)sigma) sum_j theta_j^(|c|)`.

It depends only on power sums of degrees at most `k`. These agree by 3.2.
Equality of all contractions against the spanning commutant proves the claim.

This one-source equality alone would not prove a many-source adaptive lower
bound. The same unknown `U,V` are reused, so transcript correlations must be
controlled. Sections 5--6 supply that missing argument.

## 5. Haar/Gaussian polynomial norm comparison

Let `Z` be a `d`-by-`d` complex matrix with independent centered Gaussian entries
of variance `1/d`, and let `U` be Haar unitary. For a holomorphic homogeneous
polynomial `F` of degree `L` in matrix entries, write

`H_L(F)=E_U |F(U)|^2`, `G_L(F)=E_Z |F(Z)|^2`.

The primary anchor is Collins--Śniady,
[Integration with respect to the Haar measure on unitary, orthogonal and symplectic group, arXiv:math-ph/0402073](https://arxiv.org/html/math-ph/0402073),
Proposition 2.3 and Corollary 2.4. The following covariance derivation states
explicitly the dimension factors used here rather than relying on an entrywise
asymptotic approximation with uncontrolled signs.

### 5.1 Exact covariance ratios

5.1.1 On `Sym^L(C^d tensor C^d)`, the Gaussian covariance of `vec(Z)^L` is
`(L!/d^L)` times the identity, by the complex Gaussian moment formula.

5.1.2 The Cauchy decomposition of this symmetric tensor space has one block
`S_omega(C^d) tensor S_omega(C^d)` for each partition `omega` of `L` with
at most `d` rows. Let `D_omega` be the dimension of its Schur representation
and `f_omega` the dimension of its symmetric-group representation.

5.1.3 Left and right Haar invariance make the Haar covariance scalar on each
block. The squared norm of the corresponding projection of `vec(1)^L` is
`D_omega f_omega`: it equals the trace of the row-side Schur--Weyl projector
on `(C^d)^L`. The block dimension is `D_omega^2`, so its covariance eigenvalue
is `f_omega/D_omega`.

5.1.4 The hook-content dimension identity gives

`D_omega=(f_omega/L!) C_omega(d)`,
`C_omega(d)=product_((i,j) in omega)(d+j-i)`.

The exact Haar/Gaussian covariance ratio on that block is consequently
`d^L/C_omega(d)`. This argument also covers polynomials depending only on a
specified subset of matrix columns, as occurs in section 4.

5.1.5 Every content factor is positive and at most `d+L-1`. Hence, for all `L`,

`H_L(F)>=[d/(d+L-1)]^L G_L(F)`.

When `L<=d`, every factor is also at least `d-L+1`, giving

`H_L(F)<=[d/(d-L+1)]^L G_L(F)`.

For two independent matrix variables with degree `L` in each, square these
constants. This is a positive quadratic-form comparison, valid uniformly in
the polynomial; it is not termwise positivity of a Weingarten expansion.

### 5.2 Gaussian multiplication inequality

For homogeneous holomorphic polynomials `F_1,...,F_N` in the entries of two
independent Gaussian matrices, one has

`E product_j |F_j(Z,W)|^2 >= product_j E |F_j(Z,W)|^2`.

To see this directly, use Fock multiplication `M_f` and the normal-order identity

`M_f^dag M_f=sum_alpha (1/alpha!) M_(partial^alpha f) M_(partial^alpha f)^dag`.

For homogeneous `f`, the full-degree derivatives contribute `||f||_F^2` times
the identity; all other summands are positive. Therefore
`||fg||_F^2>=||f||_F^2||g||_F^2`, and iterate. Scaling all Gaussian entries to
variance `1/d` preserves the inequality because homogeneous degrees add.
Here every polynomial has total degree `2k`, so the homogeneity condition holds.

## 6. The uniform adaptive transcript bound

Fix any comparator with `N` original-source measurements. Refine each POVM
spectrally to rank-one effects, retaining refinement labels, and condition on
its external classical randomness. A fixed complete leaf has effects
`c_j |v_j><v_j|`, with unit vectors `v_j` on the entire original source space.
They may depend arbitrarily on earlier outcomes, but are fixed along that leaf.

For either ensemble define

`F_j(U,V)=<v_j,T_theta(U,V)>`.

When U,V are replaced by Gaussian matrices, this expression keeps exactly the
same fixed polynomial coefficients. It is not renormalized into a quantum state;
the Gaussian expression is used only for polynomial norm inequalities.

It is holomorphic of degree `k` in `U` and degree `k` in `V`. Denote by
`nu_theta` the actual leaf distribution with shared hidden bases, and by
`nu_M` the leaf distribution if each new source were independently sampled
from the average state `M` of 4.1. The latter is a comparison distribution,
not an additional promise on the problem's input source.

6.1 The adaptive leaf likelihood ratio is

`nu_theta(ell)/nu_M(ell)`
`= E_(U,V) |product_j F_j(U,V)|^2 / product_j E_(U,V)|F_j(U,V)|^2`.

The effect weights `c_j` cancel. Zero-probability comparison leaves can be
discarded. Adaptation causes no difficulty because this is a leafwise identity.

6.2 Apply 5.1's lower comparison to the numerator at degree `kN` in each
matrix, then 5.2, then 5.1's upper comparison to every denominator at degree `k`.
Since `d>=k`, this gives the explicit bound

`nu_theta(ell)/nu_M(ell) >= R_(d,k,N)`,

`R_(d,k,N)=[(d-k+1)/(d+kN-1)]^(2kN)`.

The numerator lower comparison is valid even if `kN>d`; no unnoticed restriction
on total transcript length is being imposed.

6.3 If distributions obey `nu>=R mu` pointwise, write
`nu=R mu+(1-R)xi` to obtain `TV(nu,mu)<=1-R`. Thus

`TV(nu_lambda,nu_nu)<=2(1-R_(d,k,N))`
`<=4kN(kN+k-2)/(d+kN-1)`
`<=8k^2 N^2/d` for `N>=1`.

The middle inequality is the elementary bound `1-(1-x)^s<=sx`. The same
proof uses densities and integrals for continuous POVM outcomes. Averaging
over external random seeds and classical postprocessing cannot increase the bound.

6.4 A valid terminal tester accepts the YES ensemble with probability at least
`2/3` and accepts the NO ensemble with probability at most `1/3`. Their output
probability gap is therefore at least `1/3`, and transcript total variation is
at least that large. Rearranging 6.3 yields

`N>=sqrt(d)/(sqrt(24)k)`.

This proves the lower bound in section 1 for every adaptive global single-copy
strategy. With worst-case bounded expected copy cost, Markov truncation loses
only a constant in the bias and gives the same asymptotic lower bound.

## 7. What the separation settles, and what it does not

7.1 The terminal output is one property-testing bit and the measurement uses
only the supplied internal bipartition. There is no tomography lower bound,
unprovided query state, or comparison between a quantum packet and a coordinate
list. The lower-bound hard family has optimal Waring Gram conditioning and
balanced weights, so those resource promises do not hide the separation.

7.2 Tracing one original source copy in the orthogonal balanced case does
indeed provide `Sigma_h` for `h<k`. Here the terminal determinant has degree
`k+1=5`; exact matching of the first `k` moments demonstrates why those
lower-order marginals cannot distinguish the two hard ensembles in constantly
many original single-copy measurements. Merely pointing to that trace-out
shortcut does not refute this terminal lower bound.

7.3 The lower bound establishes a need for quantum processing across original
source copies. It does not establish a need for coherent determinant packets
in particular. On the special all-same-spectrum hard ensemble, a conventional
Schmidt-rank test on several whole `T` copies also distinguishes the ensembles.
That observation does not provide a tester for the full terminal promise with
arbitrary overlapping component supports and weights, but it prevents a claim
that the hard family itself demonstrates fusion's necessity.

7.4 Ordinary symmetrization of already available balanced component mixtures,
other distillation procedures, or a direct invariant measurement on multiple
whole sources may match or improve the packet upper bound. They are competing
quantum algorithms, not permitted single-original-copy comparators. The present
proof neither rules them out nor makes a historical novelty assertion about the
terminal problem, the lower-bound method, or coded synchronization.

7.5 Rank-two Bell fusion remains a known mechanism. A proof that the rank-four
coded construction is not a substantive equivalent of an existing algorithm is
still separate under D22. The very large stated constants also preclude a claim
of practical advantage from this asymptotic theorem alone. This memo contributes
the previously missing same-input, same-classical-output baseline theorem.

## 8. Verification and MERGE PROPOSAL

An in-memory calculation evaluated the root-interval signs using exact rational
arithmetic. It also checked the NO roots numerically:

`(0.00042034, 0.09835549, 0.20250196, 0.29830911, 0.40041310)`.

The first four moment differences were below `3e-16`, the fifth elementary
symmetric polynomial was `10^(-6)`, and the rank-four trace distance was about
`0.0205021`. The packet constants and marginal error above were recomputed
directly. These are exploratory checks; they do not substitute for criticism
of the uniform covariance and adaptive-transcript argument.

Provisional definitions for review are the terminal `Gamma` promise problem
and the two unknown-basis Waring source ensembles. Candidate claims are the
uniform packet terminal upper bound of section 2, the explicit moment-matched
hard instances, the Haar/Gaussian covariance comparison of section 5, and the
adaptive terminal lower bound of section 6. No claim of optimal classical
complexity, fusion necessity, historical originality, or completed north-star
algorithm is proposed. All proof promotions require an independent verdict.
