# Single-copy baseline for second-Segre-secant testing

2026-09-05. This memo derives a same-promise, same-output copy lower bound. It is
independent of whether the proposed collective projector has a soundness theorem
or a fast circuit. Tensor states use the ordinary tensor-product Hermitian metric,
a stated departure from frozen convention C1. The auxiliary polynomial calculation
in section 3 uses the campaign's Fock norm, including coefficient conjugation.
Definitions are local pending orchestrator merge; no claims-DAG status is assigned.

## 1. Statement and measurement model

Use `D-S3-SECANT` in `definitions/secant-three-copy.md`, with equal local
dimensions: `H=(C^q)^(tensor k)`, `k>=4`, and `q>=8`. This memo abbreviates its
normalized second-secant locus `X_2` as `S_2`. Distance means its stipulated
pure-state trace distance, `sqrt(1-|<u,v>|^2)`, minimized over the locus.

The task receives identical copies of one unknown pure state `u`, promised either
`u in S_2` or `d_tr(u,S_2)>=1/2`, and returns its YES/NO membership decision.
Completeness and soundness are respectively at least `2/3` and at most `1/3`.

The comparator may perform an arbitrary POVM on an entire copy, with unrestricted
ancillas during that measurement, classical computation, randomness, and adaptation
to all previous outcomes. Every quantum system carrying information about a copy
is discarded before processing the next copy. Thus POVMs may entangle all `k`
parties within a copy. There is no restriction to local measurements across parties,
efficiently implementable POVMs, or computational-basis measurements.

**Derived lower bound.** Every such protocol using at most `T` copies satisfies

`T(T-1) >= 14 / [27 (k/q + q^(-k))] >= 14q/[27(k+1)]`.

Consequently `T=Omega(sqrt(q/k))`, and `T=Omega(sqrt q)` for each fixed `k>=4`.
This is a copy-access lower bound against protocols without quantum memory.
It is not a classical running-time lower bound for explicitly given tensors or
polynomial equations, nor a lower bound against collective quantum measurements.

## 2. Source verification and the transfer being made

Beckey, Coffman, Shlosberg, Schatzki, and Leditzky,
[Product testing with single-copy measurements, arXiv:2510.07820v1](https://arxiv.org/html/2510.07820v1),
defines globally acting single-copy POVMs in Definition 7. Its Proposition 3.6 and
Theorem 4.5 establish the adaptive product-Haar indistinguishability method and an
`Omega(sqrt(q/k))` product-testing bound. Section 4.2 compares product Haar with
global Haar, using maximally mixed as an intermediate transcript distribution.

The property here is larger than product states, so its NO promise does not follow
merely from that theorem. Section 4 supplies the necessary new transfer step:
global Haar is far from border rank two, quantitatively, using one flattening.
Section 3 independently proves the transcript inequality, including the multipartite
inequality stated without proof as Lemma 3.5 in the paper.

Two typographical problems in the fetched v1 are not inherited: Definition 4's
display reverses the inequality for being far from a property; some surrounding
discussion writes an upper bound tending to zero for success probability when the
intended quantity is bias. This memo uses the explicit acceptance-probability gap
and total variation throughout. Neither typo is needed for the source's intended
lower-bound argument.

## 3. A self-contained adaptive transcript bound

Define three input ensembles. In `E_prod`, sample independent Haar unit vectors
`u_1,...,u_k in C^q` once and supply copies of `u_1 tensor ... tensor u_k`.
In `E_Haar`, sample one Haar unit vector in `H` and supply its copies.
For comparison only, `E_mix` supplies the maximally mixed density operator
`1/q^k` at every round. The maximally mixed input is not a promised problem input.
Write their complete transcript distributions as `nu_prod,nu_Haar,nu_mix`.

ASSUME the measurement model of section 1. PROVE

`TV(nu_prod,nu_mix) <= k T(T-1)/(2q)`,

`TV(nu_Haar,nu_mix) <= T(T-1)/(2q^k)`.

### 3.1 Reducing arbitrary adaptive measurements to leaf vectors

3.1.1 Any POVM effect can be spectrally refined into rank-one effects. Keeping the
refinement label and then ignoring it simulates the original protocol. A lower
bound for the more informative refined transcript therefore covers arbitrary POVMs.
Condition on any external random seed; averaging later preserves the bound.

3.1.2 Along a fixed refined transcript `ell`, the effect at round `t` is
`c_t |v_t><v_t|`, with `c_t>=0` and `||v_t||=1`. Both depend on the earlier
labels, but are fixed once the complete transcript is fixed. The vectors `v_t`
are arbitrary vectors of `H`; no tensor-product assumption is made about them.

3.1.3 Write `h=q^k`. At any nonzero-weight transcript the likelihood ratio is

`nu_E(ell)/nu_mix(ell) = h^T E_{u~E} product_{t=1}^T |<v_t,u>|^2`.

Indeed, both numerator and denominator contain `product_t c_t`, while each
maximally mixed expectation contributes `1/h`. This cancellation is leafwise,
so unrestricted classical adaptation does not invalidate it.

### 3.2 The homogeneous Fock product inequality

3.2.1 In finitely many complex variables `z`, define
`||f||_F^2=sum_alpha alpha! |f_alpha|^2`. Multiplication `M_f` has adjoint
`M_f^dag=bar(f)(partial)` on the polynomial domain. For every polynomial `f`,
normal ordering gives the exact identity

`M_f^dag M_f = sum_alpha (1/alpha!) M_(partial^alpha f) M_(partial^alpha f)^dag`.

3.2.2 To check its coefficients, the monomial identity is

`partial^beta z^gamma = sum_{alpha<=beta,gamma}`
`[beta! gamma! / (alpha! (beta-alpha)! (gamma-alpha)!)]`
`z^(gamma-alpha) partial^(beta-alpha)`.

This is the multiindex Leibniz rule. Multiply by `bar(f_beta) f_gamma` and sum
over `beta,gamma`. Grouping by `alpha` gives precisely the identity in 3.2.1.
All sums are finite on the polynomial domain.

3.2.3 Suppose now that `f` is homogeneous of total degree `m`. For `|alpha|=m`,
`partial^alpha f=alpha! f_alpha` is a scalar. These summands in 3.2.1 sum to
`||f||_F^2` times the identity. All remaining summands have the form `B B^dag`
with nonnegative coefficient. Therefore, for every polynomial `g`,

`||fg||_F^2 = <g,M_f^dag M_f g> >= ||f||_F^2 ||g||_F^2`.

Homogeneity is essential to this proof and to that displayed bound. For example,
`f=1+z`, `g=1-z` have squared norms `2,2,3` for `f,g,fg`, respectively, and
violate the inhomogeneous version. Iterating the homogeneous bound gives

`||product_t f_t||_F^2 >= product_t ||f_t||_F^2`

when each `f_t` is homogeneous, with degrees allowed to differ.

### 3.3 Gaussian factorization of the product-Haar likelihood

3.3.1 Introduce independent variable blocks `z_j=(z_{j,1},...,z_{j,q})` for
`j=1,...,k`. Associate to the arbitrary normalized leaf vector `v_t` the form

`f_t(z)=sum_{i_1,...,i_k} bar((v_t)_{i_1,...,i_k}) product_j z_{j,i_j}`.

It has degree one in every block, total degree `k`, and Fock norm one. Each
monomial has only zero or unit exponents, so its factorial weight is one.

3.3.2 Let each `g_j` be an independent standard complex Gaussian vector, with
coordinate density `exp(-|z|^2)/pi`. The Gaussian moment formula gives

`E_g |product_t f_t(g)|^2 = ||product_t f_t||_F^2 >= 1`.

The equality follows directly from `E z^alpha bar(z)^beta=alpha!` if
`alpha=beta`, and zero otherwise. The inequality is 3.2.3.

3.3.3 Write `g_j=R_j u_j`. Directions `u_j` are independent Haar vectors;
the squared radius has the gamma distribution with shape `q`, independent of
direction. Hence `E R_j^(2T)=q(q+1)...(q+T-1)`, denoted `q^(overline T)`.
Multihomogeneity gives

`E_g |product_t f_t(g)|^2`
`= [q^(overline T)]^k E_{E_prod} product_t |<v_t,u>|^2`.

3.3.4 Substituting in 3.1.3 proves, for every transcript,

`nu_prod(ell)/nu_mix(ell) >= [q^T/q^(overline T)]^k`
`= product_{j=0}^{T-1} (1+j/q)^(-k)`.

Since `log(1+x)<=x` and `exp(-x)>=1-x` for nonnegative `x`, this is at least
`1-k T(T-1)/(2q)`. Equivalently, the local-permutation contraction appearing
in the source's Lemma 3.5 is the Fock squared norm in 3.3.2 and is at least one.
Individual permutation terms need not be nonnegative; their sum is what is bounded.

3.3.5 The identical argument with one Gaussian block of dimension `h=q^k`, and
linear forms `f_t(z)=<v_t,z>`, gives

`nu_Haar(ell)/nu_mix(ell) >= product_{j=0}^{T-1}(1+j/h)^(-1)`
`>=1-T(T-1)/(2q^k)`.

### 3.4 Turning likelihood bounds into total variation

3.4.1 If probability distributions obey `nu>=a mu` pointwise, with `0<=a<=1`,
write `nu=a mu+(1-a)xi` for another distribution `xi`. It follows that
`TV(nu,mu)<=(1-a)`. Apply this to the exact positive products in 3.3.4--3.3.5
and then the displayed linear bounds. Bounds exceeding one remain harmless.

3.4.2 The triangle inequality now gives the explicit ensemble bound

`TV(nu_prod,nu_Haar) <= [T(T-1)/2] (k/q + q^(-k))`.

This also holds after arbitrary classical postprocessing. For finite-dimensional
POVMs with continuous outcome spaces, the same pointwise likelihood argument
uses densities and integrals instead of finite sums. Variable stopping with a
worst-case cap `T` is covered by padding with uninformative measurements.

## 4. Global Haar satisfies the actual NO promise

Choose the balanced bipartition with `a=floor(k/2)` sites on the first side;
write `m=q^a`, `n=q^(k-a)`. For a unit vector `u`, let `rho_A` have decreasing
eigenvalues `lambda_1,lambda_2,...`.

ASSUME `u` is global Haar. PROVE

`Pr[d_tr(u,S_2)<1/2] <= beta_{q,k}`,

`beta_{q,k} := min(1, (32/9)(m+n)/(mn+1)) <= 64/(9q^2) <= 1/9`.

4.1 Every tensor of border rank at most two has flattening matrix rank at most
two across this cut. Each actual rank-two tensor does, and the set of matrices
of rank at most two is closed, since its `3x3` minors vanish. Thus the assertion
survives passage to border rank; no converse about flattenings is needed here.

4.2 Any Schmidt-rank-two vector has support in a two-dimensional subspace of
the first factor. Cauchy--Schwarz and the variational principle for eigenvalues
give squared overlap with `u` at most `lambda_1+lambda_2`. Therefore
`d_tr(u,S_2)<1/2` implies `lambda_1+lambda_2>3/4`, and consequently

`Tr(rho_A^2)>=lambda_1^2+lambda_2^2>=(lambda_1+lambda_2)^2/2>9/32`.

4.3 The second Haar moment in dimension `mn` is
`E (|u><u|)^(tensor 2)=(1+F_AB)/[mn(mn+1)]`.
Multiplying by the swap `F_A` and taking the trace gives

`E Tr(rho_A^2)=(m n^2 + m^2 n)/[mn(mn+1)]=(m+n)/(mn+1)`.

4.4 Markov's inequality yields the asserted `beta_{q,k}`. Since `k>=4`, both
`m,n>=q^2`, and `(m+n)/(mn+1)<=1/m+1/n<=2/q^2`. Since `q>=8`, the final
bound is at most `1/9`. This deliberately elementary bound suffices; Gaussian
singular-value concentration could improve the exceptional probability but is
unnecessary for the claimed asymptotic lower bound.

## 5. Closing the lower bound

5.1 Every sample of `E_prod` lies in `S_2`, so a valid tester has averaged YES
acceptance at least `2/3`. At least `1-beta_{q,k}` of global Haar states satisfy
the NO promise. Its averaged acceptance on `E_Haar` is therefore at most

`(1-beta_{q,k})/3 + beta_{q,k} = 1/3 + 2 beta_{q,k}/3`.

5.2 The difference in acceptance probabilities is bounded by transcript total
variation. Combining 3.4.2 and 5.1 gives

`1/3 - 2 beta_{q,k}/3 <= [T(T-1)/2](k/q+q^(-k))`.

5.3 For `q>=8,k>=4`, the left side is at least `7/27`. Rearranging gives the
bound in section 1. The comparison involves two ensembles of pure states and
one membership bit; it does not replace the output with tomography or compare
against a mixed-state promise.

5.4 The argument applies more generally to any property containing all product
states and contained in Schmidt-rank-at-most-two states across the chosen cut.
This explains both the strength and the limited originality of this lower bound.
It does not depend on the proposed trine-cat projector.

## 6. Precise novelty boundary and prior tester overlap

Lovitz and Lowe,
[Nearly tight bounds for testing tree tensor network states, arXiv:2410.21417v2](https://arxiv.org/html/2410.21417v2),
Lemma 2.1 already identifies the projector onto the span of accepted pure tensor
powers as the strongly optimal test with perfect completeness. Section 6.1 treats
irreducible projective varieties and removes the benefit of adaptation between
fixed-size batches for perfect-completeness testing. Sections 6.2--6.3 analyze
`r+1`-copy rank, Schmidt-rank, and tree-network tests. For `r=2`, this includes
three-copy tests. Those ingredients cannot be claimed as new here.

Their section 2.3.2 concerns bipartite local-unitary invariance, where the relevant
symmetric-power decomposition is multiplicity-free. It does not give the proposed
multipartite trine-cat multiplicity projector or its circuit. The framework's
existence alone is not a proof of equivalence of those concrete mechanisms.

The earlier [Soleimanifar--Wright MPS tester, arXiv:2201.01824](https://arxiv.org/html/2201.01824)
tests rank bounds on the nested cuts of one chain by compatible Schur measurements.
This is a distinct property: two Bell pairs on sites `12` and `34` form an MPS of
bond dimension two in order `1,2,3,4`, yet have Schmidt rank four across `13|24`.
They are at least `1/sqrt(2)` away from `S_2` by the same overlap bound as 4.2.

There is nevertheless an exact limitation to the speedup claim. If a robustness
argument supplies a dimension-independent lower bound on some cut's three-copy
rank-test rejection for every state far from `S_2`, independent known rank tests
over all cuts also give a dimension-independent copy upper bound at fixed `k`.
Thus the `q`-asymptotic separation proved here does not by itself distinguish the
proposed joint mechanism from a composition of existing rank testers. Potential
new substance must be stated in the explicit joint projector, its cost as `k`
varies, or a quantified performance improvement over those separate tests.

### 6.1 Stronger subsequent audit: an exact reduction to random-cut rank tests

The independent critic subsequently communicated the following identity. It is
also verified directly below, using `D-S3-LOCAL-REPRESENTATION` and its normalized
trine vector `w_m`. This kills the proposed new mechanism's asymptotic distinction
from standard rank testing; it does not invalidate the copy lower bound above.

Choose a subset `A` of the `k` sites by independent fair bits, including the
empty and full subsets. On three copies apply the ordinary antisymmetric rank
test to the grouped subsystem `A`. Its rejection effect is

`Q_A=(1/6) sum_{pi in S_3} sign(pi) U_A(pi)`.

The averaged rejection effect is

`Qbar=(1/6) sum_{pi in S_3} sign(pi) tensor_i [(1+U_i(pi))/2]`.

Restrict to globally symmetric three-copy inputs and a fixed tuple of local
Schur types, with `m` standard representations. Then, on every nonzero sector,

`Qbar=c_m(1-|w_m><w_m|)` if no local alternating type occurs,

`Qbar=c_m 1` if any local alternating type occurs,

where `c_m=[1+2(-1/2)^m]/6`. The spectator Schur-functor spaces carry identities.

6.1.1 The identity permutation contributes `1/6`. For either three-cycle `r`,
the standard representation satisfies `1+U(r)=-U(r)^2`, and the one-dimensional
types have value one on `r`. Global replica symmetry therefore makes the two
three-cycle terms contribute `2(-1/2)^m/6` times the identity.

6.1.2 A local alternating type makes every transposition term zero, since
`(1+(-1))/2=0`. If there are no alternating types, each transposition contributes
the rank-one tensor power of its fixed trine direction. On the invariant subspace,
all three such directions project onto their average. Their compressed sum is
`[3+6(-1/2)^m]/3` times `|w_m><w_m|`, so their signed contribution is
`-c_m |w_m><w_m|`. For `m=0` the same statement holds with the scalar convention.
For `m=1`, there is no global invariant sector, so its zero coefficient causes
no division problem.

6.1.3 For allowed rejection sectors, `1/8<=c_m<=1/2`: `m=0` gives `1/2`,
`m=2` gives `1/4`, `m=3` gives `1/8`, and subsequent values lie between these.
Consequently, if `P_3` is the proposed exact secant projector,

`(1/8)(1-P_3) <= Qbar <= (1/2)(1-P_3)`

on `Sym^3(H)`. Thus the random-cut standard rank tester attains its rejection
probability within a universal constant factor, even as `k` varies.

6.1.4 Local Schur-type measurements commute with `Q_A`. Recording the types and
weighting a rejection outcome by `1/c_m` gives an unbiased estimator of the exact
secant residual, bounded by eight. This also matches additive residual estimation
up to constant sample factors, rather than just the membership promise test.

The ideal projector is not literally the unweighted mixture `Qbar`. That operator
inequality is stronger than necessary to refute a speedup claim based solely on
their different matrix entries: the standard mixture and simple postprocessing
already reproduce the proposed computational behavior to constant factors. No
separate tomography or general circuit-simulation comparison is involved.

## 7. MERGE PROPOSAL

- Define the single-copy adaptive comparator exactly as in section 1, including
  unrestricted global POVMs within a copy and no quantum memory between copies.
- Candidate lower-bound statement: the explicit `T(T-1)` bound of section 1,
  under its `q>=8,k>=4`, trace-distance, and completeness/soundness hypotheses.
- Proof dependencies: sections 3--5 give a self-contained derivation; cite the
  product-testing paper as the source of the ensemble method, not as a theorem
  whose property-testing promise transfers automatically.
- Keep classical explicit-input advantage, optimality against single-copy
  algorithms, collective soundness, and historical originality outside this claim.
- The result has a proof suitable for independent criticism. No numerical check
  is needed for the asymptotic claim, and no shared files or registered checkers
  were modified by this lane.
