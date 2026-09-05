# Independent verdict: terminal Waring-component copy separation

2026-09-05. Reviewed the completed `scouting/waring-terminal-baseline.md`,
`definitions/waring-components.md`, and registered C-345, using the previously
audited coded-packet identities/resource bounds. This is a mathematical audit
of the terminal separation, not an originality audit or north-star promotion.
Only this verdict is written by the reviewer.

**VERDICT: PASS.** No FATAL or MAJOR mathematical objection remains. The
uniform quantum upper bound covers the full stated component promise, and
the lower bound covers arbitrary adaptive global measurements on one whole
original source copy at a time. They have the same one-bit output. The
constant quantum budget is exceptionally large, as disclosed. D22 remains
separate and is not repaired by this separation. C-345's statement is supported
for the campaign's ratchet; this reviewer does not edit its status.

## 1. Well-defined problem and full-family identifiability

1.1 Write the `2|2` catalecticant of
`T=sum_a c_a u_a^tensor 4` as
`sum_a c_a (u_a^2) tensor (u_a^2)`. Independence of the four `u_a` implies
independence of their squares, by dual linear-function contraction. Since
every `c_a` is nonzero, this catalecticant has image
`S=span{u_1^2,...,u_4^2}` and rank four.

1.2 If `v^2 in S`, a linear functional annihilating `span{u_a}` shows that
`v` lies in that span. Write `v=sum_a x_a u_a`. All cross-monomial
coefficients in `v^2` must vanish, so `x_a x_b=0` for `a!=b`. Thus the
only Veronese points of `S` are the four original squares. Any other
four-term decomposition would give the same catalecticant image, and hence
the same four unordered component rays. No unstated genericity promise or
component-finding oracle is needed for this identifiability argument.

1.3 Normalizing the component rays makes `Gamma` independent of their phases
and ordering. If `M_u` is the normalized bipartite coefficient matrix,
`rho_A=M_u M_u^dag`; Cauchy--Binet gives
`e_5(rho_A)=sum_(I,J) |det(M_u[I,J])|^2` over five-element row/column sets.
This nonnegative quantity vanishes exactly at component matrix rank at most
four. The promised residual is a specified geometric scalar, not a coordinate
list, an unnormalized minor, or an additional query state.

## 2. Quantum upper bound, including all failures

2.1 The Gram promise gives `|<u_a,u_b>|<=1/2`, since the two-by-two
principal Gram block has least eigenvalue `1-|<u_a,u_b>|`. The marginal
argument works for either packet parity and does not use disjoint internal
supports or orthogonal components.

For an unnormalized packet, the `r!` diagonal permutation pairs contribute
`r!` to its norm and `r! Sigma_5` to its reduced numerator. A cross pair
differs in at least two rows. If its first-row labels differ, the discarded
overlap has modulus at most `mu^(m-5)mu^m`; otherwise the stronger
`mu^(2m)` bound holds. Each retained rank-one operator has trace norm one.
Together with `Z>=r!/2`, these facts prove the claimed bound

`D(rho_(m,5),Sigma_5)<=2(r!-1)mu^(2m-5)`.

2.2 At `r=k=4`, coded degree sequence `m_j=2+2^j` gives `m_4=18`.
The uniform trace error is at most `46/2^31`, strictly below `gamma/30`.
Antisymmetrizing the five internal A registers has expectation
`e_5(rho_A(u))` on five copies of a component: there is no additional `5!`
in this probability. Hence its expectation on the approximate mixture differs
from `Gamma(T)` by at most the displayed trace error.

2.3 With `B=3,000,000=3/gamma` independent packet trials, the ideal YES
error is at most `1/10`, by a union bound. On a NO input the probability
of no detection is at most `exp(-2.9)<1/6`. The source is fixed but the
fresh input copies and measurements for the distinct trials are independent;
successful packets have the specified output irrespective of their prior
failure histories.

2.4 The coded promise bound gives exactly

`1/f_*=2^12 (4!)^5=32,614,907,904`,
`Cbar_4=2048 (2/f_*)^4`
` =37,077,851,528,602,707,333,906,344,250,393,377,236,014,071,808`.

This is an expected source-copy upper bound per trial, not a claimed
practical running time. Executing at most `B` trials has expected cost at
most `B Cbar_4`, including all discarded seeds and child packets. Aborting
at `6 B Cbar_4` source calls has probability at most `1/6`. Thus the two
total ideal error bounds are `1/10+1/6` and `exp(-2.9)+1/6`, both strictly
below `1/3`. Early termination on detection only lowers the cost.

2.5 The strict margins also accommodate synthesized gates: an overall
compiled-instrument error at most `1/30` still leaves both errors below
`1/3`. Choose local precision against the known finite execution cap and
the known number of controlled register permutations. No component basis
or inverse source circuit is needed. With r, k, m, B and this cap fixed,
the gate dependence outside source generation is polynomial in `log q`.
The source-generation cost/workspace remains separately charged, as in the
definitions. These statements concern ideal promised source copies.

2.6 On the hard orthogonal family, `m=6` already gives the exact five-copy
mixture, and the two-fusion expected count is `782,757,789,696`. This
smaller special-family constant cannot replace the uniform general-input
bound. Both constants are dimension independent; neither suggests practical
advantage at ordinary experimental sizes.

## 3. Exact hard spectra and source promises

3.1 Exact rational substitution gives alternating endpoint signs on each
of the five stated disjoint intervals for
`z(z-.1)(z-.2)(z-.3)(z-.4)-10^(-6)`. They are positive intervals and
the polynomial has degree five, so its roots are five distinct positive
reals. The `z^4` coefficient makes their sum one.

3.2 Only the constant term differs from the YES polynomial. Thus the first
four elementary symmetric functions, and by Newton's identities the first
four power sums, agree exactly. The fifth elementary symmetric function is
zero for the padded rank-four spectrum and exactly `gamma` for the NO one.
The least NO root `v` obeys
`gamma=v prod_(j=1)^4(j/10-v)<(24/10^4)v`, hence `v>1/2400`.
The resulting component distance from Schmidt rank at most four exceeds
`1/sqrt(2400)>1/50`. This part is not based on floating-point root evidence.

3.3 The 20 displayed core basis directions exist for every `d>=20`.
The four cores have mutually orthogonal supports on both sides. Shared
independent Haar `U,V` preserve their orthogonality and their Schmidt spectra.
Consequently every hard input has `G=I`, normalized source coefficients
`1/2`, and `p_0=4^(-4)>=1/512`. Both hard ensembles lie in the full
problem's stated conditioning promises. Their respective `Gamma` values
are exactly zero and `gamma` for every hidden basis, not just on average.

## 4. The Haar/Gaussian comparison is a positive norm statement

4.1 Under the one-source local Haar twirl, the commutant is spanned by
`P_pi^A tensor P_sigma^B`, with `pi,sigma in S_k`. Cross-component
contractions vanish because each core lies in a different support block on
each side. Diagonal contractions equal products of spectral power sums
whose degrees are the cycle lengths of `pi^(-1)sigma`, hence at most `k=4`.
The matched moments therefore give exactly the same average density
operator `M` for both ensembles. Equality against this spanning commutant
suffices even without assuming its spanning elements are orthogonal.

4.2 For matrix entries of variance `1/d`, Gaussian covariance on
`Sym^L(C^d tensor C^d)` is `(L!/d^L)I`. In its Cauchy block
`S_lambda(C^d) tensor S_lambda(C^d)`, left/right Haar invariance makes
the Haar covariance scalar. The `vec(I)^tensor L` component has norm
squared `D_lambda f_lambda`: it is the trace of the row-side Schur-Weyl
projector applied to a maximally entangled vector. Dividing by block
dimension `D_lambda^2` gives eigenvalue `f_lambda/D_lambda`.

4.3 Hook-content dimension therefore gives the exact ratio
`d^L/prod_(i,j in lambda)(d+j-i)`. Every occurring partition has at most
`d` rows, so all its content factors are positive, including when `L>d`.
They are always at most `d+L-1`. The lower quadratic-form bound
`[d/(d+L-1)]^L` is valid at every degree. The upper bound with
`d-L+1` is used only at `L=k<=d`. This avoids the invalid unrestricted
entrywise-sign comparison that a Weingarten expansion could suggest.
The representation/integration framework is consistent with
[Collins--Sniady, §§2.1--2.2](https://arxiv.org/html/math-ph/0402073).

4.4 Independence of the two matrix variables tensors their covariance
operators. Squaring the bounds is valid even when the polynomial does not
factor between those variables: they are positive operator inequalities.
Polynomials depending on selected columns are simply a subspace restriction.
Their Gaussian extension keeps the fixed source coefficients; it must not
be renormalized to a unit vector at each Gaussian matrix value.

4.5 The Gaussian multiplication step is also valid. In the auxiliary
standard Fock norm, normal ordering gives

`M_f^dag M_f=sum_alpha M_(partial^alpha f)
                         M_(partial^alpha f)^dag/alpha!`.

For homogeneous f, its full-degree derivatives sum to `||f||_F^2 I`;
all other terms are positive. Hence `||fg||_F^2>=||f||_F^2||g||_F^2`.
Iterating and scaling Gaussian coordinates by `1/sqrt(d)` gives the
stated product inequality. It applies here because every amplitude is
holomorphic with degree k in each matrix variable. No real-Gaussian
product conjecture or normalization of random source states is being used.

## 5. Arbitrary adaptive global single-copy measurements are covered

5.1 Refine each POVM to rank-one effects and retain the refinement outcome.
This can only give the comparator more information. Condition on external
randomness. Along a fixed full transcript, each effect vector `v_j` and
weight `c_j` is then fixed, however complicated its dependence on previous
outcomes. The vector is arbitrary on the entire original `d^8`-dimensional
source space; it need not factor over slots or over the A/B sides.

5.2 The amplitude `<v_j,T_theta(U,V)>` is holomorphic of degree k in U
and degree k in V. Because no quantum memory crosses original copies,
the fixed-basis transcript probability factors before averaging over the
shared hidden bases. The reference distribution is the same adaptive policy
run on a fresh copy of M at each step. It is normalized and common to both
hypotheses; it is not asserted to be the actual fixed-source ensemble.

5.3 Cancelling the effect weights gives the exact likelihood ratio in
section 6.1. A zero-probability reference leaf also has zero actual
probability, since its relevant Haar norm vanishes. Apply the degree-kN
lower covariance bound, the Gaussian product inequality, and the degree-k
upper covariance bounds to obtain, for each hypothesis and each leaf,

`nu_theta >= R nu_M`,
`R=[(d-k+1)/(d+kN-1)]^(2kN)`.

Adaptation has not been replaced by nonadaptivity: its entire effect is
already present in the arbitrary leaf-specific polynomial factors.

5.4 Both leaf distributions are normalized. Pointwise domination implies
`TV(nu_theta,nu_M)<=1-R`; the triangle inequality gives

`TV(nu_lambda,nu_nu)<=2(1-R)`
` <=4kN(kN+k-2)/(d+kN-1)<=8k^2 N^2/d`.

The numerator covariance bound remains valid if `kN>d`. Continuous POVMs
are handled using their positive matrix densities with respect to trace
measure, followed by a measurable rank-one refinement; the same inequalities
then integrate. External randomness and classical postprocessing cannot
increase this total-variation bound. A strategy stopping before its maximum
N can be padded, so variable stopping does not evade the bounded-copy result.

5.5 Uniform terminal success at least `2/3` forces an output probability
gap at least `1/3` between the two ensembles. Therefore

`N>=sqrt(d)/(sqrt(24)k)=q^(1/4)/(4sqrt(24))`.

The count is of whole original T copies, exactly as in the upper bound.
For worst-case bounded expected cost, Markov truncation loses a constant
factor in the bias and gives the stated asymptotic version, rather than
silently preserving this particular numerical constant.

## 6. Whole-source shortcuts and limits of the conclusion

The lower-bound hard family can be distinguished by conventional collective
whole-source rank/moment tests. Such tests are outside the stipulated
single-original-copy comparator, so this does not invalidate the lower bound.
It does show that this hard family alone cannot prove fusion necessary.

Nor does the simplest whole-source rank threshold solve the general promise.
For example, in a shared five-dimensional internal support let
`u_a=5^(-1/2)sum_(j=0)^4 omega^(aj)|j,j>`, `a=0,1,2,3`, with
`omega=exp(2pi i/5)`. These four components are orthonormal, so the balanced
fourth-order source has `G=I,p_0=1/256`. Each component has
`e_5=1/3125>=gamma`, but the whole source's A^4|B^4 Schmidt rank is only
625. It passes the necessary YES rank bound `4*4^4=1024`. Padding embeds
this valid NO instance in every `d>=20`. This confirms the full-task
distinction without establishing necessity or optimality of coded fusion.

## 7. Clarifications and final disposition

**T1 — MINOR. Location:** §2.3's finite-gate implementation sentence.
**FIX DEMAND:** Make the total compiled-channel error budget explicit, for
example at most `1/30` over the already capped execution.
**SURVIVING STATEMENT:** The disclosed strict probability margins support
success at least `2/3` with the same dimension-independent source cap and
polynomial-logarithmic external-source gate dependence.

**T2 — MINOR. Location:** §§5--6, evaluation at Gaussian matrices.
**FIX DEMAND:** Say explicitly that `T_theta(Z,W)` denotes its homogeneous
polynomial extension with fixed coefficients and is not normalized there.
**SURVIVING STATEMENT:** The positive covariance and Fock inequalities apply
exactly to those holomorphic amplitudes; Gaussian normalization would break
this argument and is neither needed nor permitted by the proof.

The terminal definitions, C-345's quantifiers, the full quantum upper bound,
and the adaptive lower bound are consistent. Accept C-345 as mathematically
supported for the claims ratchet, relying on the previously audited coded
identities at their qualified scope. No statement about practical advantage,
classical coefficient-list input, best quantum algorithm, fusion necessity,
or strict mechanism originality is promoted.

Independent bounded computation used one BLAS thread and a 60-second timeout:
413 checks passed for exact root brackets, resource integers, packet error,
content-factor bounds, and the transcript constant. It also independently
formed Haar covariances through Weingarten Gram pseudoinverses and verified
the spectra at `(d,L)=(2,2),(2,3),(2,4),(3,3)`, including `L>d`, against
`f_lambda/D_lambda` with multiplicity `D_lambda^2`. These are unregistered
finite checks; the analytic arguments above, not numerical extrapolation,
establish the uniform bounds. Only the cited primary integration source was
opened for this proof audit.

**VERDICT: PASS — the formal same-output copy separation is established
at the stated promises; D22 qualification remains excluded/separate.**
