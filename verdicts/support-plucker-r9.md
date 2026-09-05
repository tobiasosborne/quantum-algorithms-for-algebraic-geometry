# Support-to-Pluecker r9: independent mechanism and baseline audit

Date: 2026-09-05. Scope: `scouting/support-plucker-r9.md`, its originating
brief, and `scouting/support-plucker-classical-r9.md`, before integration
into the claims register. Root owns tracking
`qaag-9v2` and all shared files. This audit uses the finite-dimensional Hilbert
inner product specified by that brief, rather than the default polynomial
Bargmann--Fock inner product. Write a coordinate subset as `J`, preserving C6;
`q` is the explicitly declared local Hilbert dimension. No claim status is
assigned here.

**Verdict:** mathematical PASS for the finite-circuit exact heralded conversion
and the root's quantitative adaptive lower bound. The mechanism fails D22:
its complete processing reduces to known generalized phase estimation,
multiplicity reset and signed-permutation certification. There is also an
exact rank-two universal-purification ancestor. The familiar classical
projection-DPP sampler does require unavailable kernel information; it is
not a copies-only dequantization. Exact universal DPP sampling with finite
separable measurements is impossible for `2 <= r < q`. Separately, the
root's full adaptive-transcript proof establishes an `Omega(sqrt(q))`
constant-error sampling lower bound on the rank-two hidden-block family,
and a matched `Theta(sqrt(q))` classical bound for its decision bit.

## 1. Independent derivation of the conversion

### 1.1 Schur factor and success probability

ASSUME the input promise in the brief: rank `r`, support `U`, and positive
eigenvalues `p_i >= eta/r`. With `Q_lambda` denoting the unitary-group factor
and `S_lambda` the symmetric-group factor,

```
rho^tensor N = direct-sum_lambda A_lambda(rho) tensor 1_(S_lambda).
```

Only shapes with at most `r` rows occur. Conditional on a final shape and a
standard Young path `b`, the state is

```
sigma_lambda tensor |b><b|,
```

with the same `sigma_lambda` for every path. Prefix central projectors act
as the identity on `Q_lambda`; their joint spectral projections specify the
Young--Yamanouchi basis of `S_lambda`.

Use row-insertion RSK with weakly increasing rows and strictly increasing
columns. The number of rows is the longest strictly decreasing subsequence
length. The time `T` to see `r,r-1,...,1` in that order has

```
E[T] = sum_i 1/p_i <= r^2/eta.
```

Since finding this subsequence forces exactly `r` rows, `N=ceil(2r^2/eta)`
gives probability at least `1/2` of a usable shape by Markov's inequality.
This is a sufficient bound, not an optimal-copy theorem. It does not require
observing eigenvalue letters or knowing their eigenbasis: RSK supplies the
distributional proof of the Schur measurement outcome.

### 1.2 Steering is a valid operation on the full factor

ASSUME `b' = s_k b` is a valid adjacent-number swap of standard tableaux and
put `d = content_b(k+1)-content_b(k)`. In a consistent orthogonal convention,

```
R_lambda(s_k)|b> = (1/d)|b> + sqrt(1-1/d^2)|b'>,
|d| >= 2.
```

The two tableaux differ only at prefix `k`. Measuring that prefix shape
therefore gives `b'` with probability `1-1/d^2 >= 3/4`; the other outcome
restores `b`. Each branch Kraus operator, restricted to the starting path,
is a scalar times `1_(Q_lambda) tensor |new path><b|`. This proves preservation
of arbitrary unitary-factor states, including entanglement with an external
reference. It is stronger than a calculation on a highest-weight vector.

A valid path of adjacent swaps exists because standard tableaux are linear
extensions of the Young-diagram partial order. Moving the target next box
leftward through incomparable boxes gives at most `N(N-1)/2` swaps. A target
linear extension may start with the entire first column whenever the shape
has `r` rows. Capping each edge at `L` attempts gives conditional steering
failure at most `N(N-1)4^(-L)/2`, with no fresh source copies used by retries.

### 1.3 Pure output, including mixed post-Schur states

At the target path, the first `r` physical registers carry the sign
representation of `S_r`. Every physical permutation and prefix projector
preserves `U^tensor N`. Their joint range is consequently contained in

```
(wedge^r H intersect U^tensor r) tensor U^tensor(N-r)
  = span(Omega_U) tensor U^tensor(N-r).
```

Any positive operator supported on this space factors as
`|Omega_U><Omega_U| tensor tau`, including a mixed state and any retained
reference. Tracing out the other systems therefore produces the exact pure
Slater state in the ideal instrument. Measuring all retained coordinates
and sorting gives probability `det(P_U[J,J])`; each ordering has `1/r!`
of this probability. There is no determinant postselection cost at this step.

### 1.4 Circuit scope and precision

The prefix measurement must be the **Lueders** instrument. A group Fourier
implementation may prepare a uniform group register, apply controlled
permutations and its Fourier transform, copy only the irrep label, then
uncompute the entire ancillary operation. On each isotypic subspace the
copied label is deterministic; uncomputation removes the internal Fourier
labels without dephasing the system. Measuring or discarding these labels
first is a different channel and cannot justify the argument above.

There is an independently verified efficient complete implementation in
Section 2 below, so a polynomial dependence on `q` is unnecessary. Without
an exact final certificate, approximate gate synthesis would give only an
approximate output instrument. The author's final Section 7 supplies that
certificate, and its exactness claim survives the following additional audit.

### 1.5 Final author circuit and exactness repair

The Jucys--Murphy operators `X_k=sum_(i<k) SWAP_(i,k)` have integer contents
as their eigenvalues, in `[-(k-1),k-1]`. Phase estimation modulo
`R=2^ceil(log_2(2N))` therefore has no ideal resolution error. Copying its
label and applying the literal inverse gives the required Lueders
instrument. Measuring `X_k` instead of prefix shape is sufficient during
steering because the two reachable paths have different kth contents.

Every controlled exponential is compiled by sign extraction with a
controlled swap, an ancilla phase, and inverse sign extraction. This
identity is valid on both eigenspaces. The first-order product bound
`t^2 (k-1)^2/(2L)` and the sum over the `m` controlled powers are valid.
The submitted `L=ceil(4 pi^2 m N^2/nu)` leaves more than the claimed
`nu/2` product-formula allowance. Ancilla phase synthesis supplies the
remaining error. Replacing both extraction and uncomputation changes
one instrument by at most `4 nu` in diamond norm, hence all `K` adaptive
uses by at most `4Knu=1/64`. This comparison is on the entire flagged
instrument, so no rare-branch normalization is hidden.

Most importantly, only exact controlled permutations touch the physical
data. Arbitrarily imperfect ancilla states, ancilla synthesis, measurement
and discarding preserve `U^tensor N` exactly. Set `h=2^ceil(log_2(r!))`.
Uniform Hadamard labels, a valid-label flag, reversible permutation
unranking and a final Hadamard-basis projection have data Kraus operator

```
C_r = (1/h) sum_(pi in S_r) sign(pi) T(pi)
    = gamma_r P_-^(r),        gamma_r=r!/h>1/2.
```

Conditioning on its flag removes every nonantisymmetric component exactly.
Together with exact support preservation, this forces `Omega_U` even on
an incorrectly steered trajectory. Correct ideal steering occurs with
probability at least `3/8`; the certificate retains at least one quarter
of it. The implemented acceptance is at least
`3/32-1/64=5/64>=1/16`. Thus `B=ceil(16 ln(1/delta))` batches suffice,
each consuming at most `N` copies, with exactly correct accepted output.

The certificate is not a factorial lookup: factoradic arithmetic and
controlled swaps implement the sum on `O(r log r)` label bits. Its constant
acceptance only applies after a correct column; applied to fresh flat
rank-r copies it retains the original `r^(-r)` overlap. The submitted
conservative overall gate bound
`O(B K^2 N^3 m^2 [w+log^4(KN)] + B[r^3 log^2(r+1)+r^2(w+log(r+1))])`
and storage `O(Nw+r^2 log^2(r+1)+log N)` follow from the displayed loops.
The exact-rank and exact-controlled-permutation assumptions are material.

## 2. Historical and substantive reduction audit

### 2.1 An exact previously described rank-two protocol

Cirac, Ekert and Macchiavello explicitly choose multiplicity states with
`|j,m,1> = |j,m> tensor singlet^(J-j)`. They measure `S_(j,alpha)`, move the
observed multiplicity label `alpha` to `1`, and obtain a mixed symmetric
factor tensored with pure singlet pairs. Their purifier discards the singlets.
See Eqs. (6)--(10) and the procedure following Eq. (12) in
[Optimal purification of single qubits, quant-ph/9812075](https://arxiv.org/html/quant-ph/9812075),
PRL 82, 4344--4347 (1999), DOI `10.1103/PhysRevLett.82.4344`.

The correspondence to the candidate is operational: measure the irrep and
multiplicity, reset that multiplicity, and expose a determinant factor. On
an unknown embedded two-dimensional support, retaining one singlet gives
the support wedge. Their multiplicity operators are specified by permutation
representations, so the construction is independent of the unknown basis
of that support. Extending the operator on irrelevant ambient sectors can
be done by the Schur circuit below. This is not a claim that their paper
states the present growing-`r` copy bound or embedded-support problem.

Keyl--Werner's later
[The Rate of Optimal Purification Procedures, quant-ph/9910124](https://arxiv.org/html/quant-ph/9910124)
also formulates its source and purified outputs on qubits. It is supporting
context, not evidence that every higher-rank support result was already
explicitly stated there.

### 2.2 Exact channel reduction for growing rank

After deriving the channel above, a targeted primary-source check found
Theorem 1 and Fig. 2 of
[High-dimensional quantum Schur transforms, arXiv:2509.22640v1](https://arxiv.org/html/2509.22640v1).
It specifies a reversible Schur transform with Gelfand--Tsetlin bases on
both representation registers, gate complexity `O-tilde(N^4)` and space
`O-tilde(N^2)`. Only polylogarithmic dependence on the local dimension is
hidden; input storage also includes the required `N log q` qubits. The
paper repairs an error in Krovi's original multiplicity-basis conversion.
Thus citing [Krovi 2019 alone](https://arxiv.org/abs/1804.00055) without
addressing that issue would be inadequate. For the high-dimensional
formulation, one may pad the physical alphabet to dimension `max(q,N)`.

Here is the complete reduction, derived in this audit. Apply the corrected
Schur transform `S`; measure shape `lambda` and tableau `b`; fail if the
shape has fewer than `r` rows; replace the now-classical tableau value by
the computable first-column path `b0(lambda)`; apply `S^dagger`; retain
the first `r` physical systems. Conditional on the initial shape, its
channel is

```
X -> S^dagger [Tr_(S_lambda)(S X S^dagger)
              tensor |b0(lambda)><b0(lambda)|] S.
```

The shape label and unitary factor remain untouched. The map is defined
on the entire `Q_lambda tensor S_lambda` block and commutes with adjoining
an arbitrary reference. For a measured starting tableau, it is exactly
the almost-sure final channel of the repeated steering procedure. The
capped steering implementation merely adds a bounded flag-failure event.
Only two calls to the known structured transform, ordinary computational
basis measurements, an efficient classical tableau computation and a
label overwrite are needed. There is no amplitude amplification and no
small multiplicity postselection probability.

This proves ideal-channel equivalence. Arbitrary approximate full Schur
circuits on the data need not preserve `U^tensor N` exactly, so they alone
do not justify the author's exact finite-circuit guarantee. The following
stronger prior-algorithm reduction does.

### 2.3 A prior GPE reduction that also preserves exact support

Fig. 3 and Eq. (11) of
[Bacon--Chuang--Harrow, quant-ph/0407082v4](https://arxiv.org/pdf/quant-ph/0407082)
explicitly describe generalized phase estimation for a finite-group
representation. Its gates are a Fourier transform on a group ancilla,
controlled representation action, and another ancilla Fourier transform.
The output exposes the original representation index, retaining the
multiplicity index and entangling a second Fourier index with the physical
representation register.

Specialized to tensor permutations, and choosing the Fourier-index
convention of that equation, its exact isometry is

```
W (|0>_anc tensor |lambda,Q,a>_physical)
 = (1/sqrt(d_lambda)) sum_b |lambda,a,b>_anc
                                  tensor |lambda,Q,b>_physical.
```

Here `a,b` range over standard tableau indices and `d_lambda=dim S_lambda`;
`Q` denotes the entire untouched unitary-group factor. This identity is
also obtained directly from finite-group matrix-coefficient orthogonality.
Measure only `lambda,a`. Conditional on an r-row shape, overwrite the
exposed `a` by `b0(lambda)` and apply `W^dagger`. The resulting physical
tableau is `b0` deterministically, because the other index and physical
factor still form the precise maximally entangled sum in the display.
No measurement of that other index is performed. For a general mixed
input, measurement/reset implements the same trace-and-reprepare
channel as Section 2.2.

The `S_N` Fourier transform is already efficient; controlled physical
permutations and classical tableau manipulation cost polynomially in
`N` and `log q`. All its approximate synthesis occurs on ancillas.
Every data gate is an exact controlled permutation, including in
`W^dagger`, so `U^tensor N` remains an exact invariant subspace. Appending
the same exact `gamma_r P_-^(r)` certificate therefore recovers the
author's exact accepted-output guarantee, with only constant acceptance
loss and polynomial overhead. Approximate finite Fourier labels need
not themselves be certified correctly for this conclusion.

This is a complete reduction to the previously described GPE extraction
algorithm, the previously described multiplicity-reset rule, and the
explicit signed group projector. It addresses the finite-precision
loophole in a bare full-Schur-transform reduction.

**FATAL objection N1 — D22 originality.** The claimed operation is
substantively reducible to a described quantum representation-processing
algorithm, and its rank-two measure/reset/factor-extraction ancestor is
explicit. This is stronger than saying the circuit uses Schur theory or
a universal gate set.

**FIX DEMAND:** classify the support conversion and measured steering as
a useful Schur-processing construction, with originality rejected under
D22. A new target encoding, improved elementary implementation or
different rank regime cannot alone repair the strict criterion.

**SURVIVING STATEMENT:** the conversion theorem and its polynomial-rank,
polylogarithmic-dimension implementation remain mathematically valid;
neither the reduction nor the prior purification paper refutes them.

## 3. Matched classical sampling baseline

### 3.1 Why the usual sequential DPP sampler is not copies-only

For a known projection kernel `P`, the sequential sampler selects `i`
with probability `P_ii/r` and updates the kernel to

```
P' = P - P[:,i] P[i,:] / P_ii.
```

Its range is `U intersect e_i^perp`. This is the standard projection-DPP
sampling construction discussed by Hough, Krishnapur, Peres and Virag in
[Determinantal Processes and Independence, math/0503110](https://arxiv.org/abs/math/0503110),
DOI `10.1214/154957806000000078`. It needs the kernel or a support basis.

Applying the known physical coordinate-complement filter
`Q_i=1-|i><i|` to a fresh copy instead gives `Q_i rho Q_i`, whose range
is `Q_i U`. In general `Q_i U` has dimension `r`, while
`U intersect e_i^perp` has dimension `r-1`. These are different operations.
The first-coordinate probability is itself wrong for a nonflat source:
`rho_ii` need not equal `P_ii/r`.

### 3.2 Exact universal single-copy sampling is impossible

The following is an independent finite-dimensional argument, not a
quantitative approximation lower bound.

ASSUME `2 <= r < q`, flat sources `rho_U=P_U/r`, a fixed finite copy cap
`T`, and measurements separable across source copies. Arbitrary adaptive
single-copy POVMs and classical processing form a subclass of these
measurements. For each output subset `J`, let `M_J` be its separable
positive effect on `H^tensor T`.

1. Choose a coordinate unit vector `w` outside `J`. Let `nu` be the
   distribution of supports `U=span(w) direct-sum V`, where `V` is a
   Haar `(r-1)`-plane in `w^perp`.
2. For every such support, `det(P_U[J,J])=0`, because projecting `U`
   onto the `r` coordinates in `J` kills `w` and has rank at most `r-1`.
3. For every nonzero positive single-copy effect `E`,
   `Tr(E P_U)>0` for `nu`-almost every `U`. To see this, take a nonzero
   vector in the support of `E`. If it overlaps `w`, the conclusion is
   immediate; otherwise a positive-dimensional Haar plane `V` overlaps
   it almost surely.
4. Thus every nonzero positive product effect `E_1 tensor ... tensor E_T`
   has strictly positive expectation against `integral rho_U^tensor T dnu`.
5. Every nonzero separable positive effect is a finite positive sum of
   nonzero product effects in finite dimension. Consequently the same
   strict positivity holds for every nonzero `M_J`.
6. Exact DPP correctness demands zero probability of output `J` for every
   support in Step 1, contradicting Step 5 unless `M_J=0`. This applies
   to every `J`, so no normalized exact sampler exists.

The proof also excludes a sampler with a failure flag and positive exact
sampling success, and excludes almost-sure finite stopping: apply the
argument to each event “output `J` at time `t`,” then take the countable
union. The exceptions matter: rank-one coordinate measurement samples
its DPP, and `r=q` has a deterministic output. The ideal collective
conversion is consistent with the obstruction because its output effects
are not separable across copies.

**Resolved objection B1 — exactness and approximation must be separate.**
The zero-probability argument alone supplies no dimension-dependent lower
bound for constant total-variation error. The final author certificate
repairs exactness of finite-gate accepted output, and the root's separate
quantitative proof in Section 3.4 repairs the approximation comparison.

**FIX DEMAND:** retain both repairs and use the same failure convention
on both sides; to obtain an always-output approximate sampler, replace
the quantum failure flag by an arbitrary fixed subset. Its unconditional
TV error is at most the failure probability `delta`.

**SURVIVING STATEMENT:** there is no exact finite separable copies-only
sampler in the nontrivial ranks above; there is also a distinct quantitative
lower bound on the rank-two family below. The known-kernel classical
sampler changes the access model.

### 3.3 Hidden-block witness and a matched classical upper bound

For the two rank-two families in the brief, let `A` denote the known first
block and `R_A=Pi_A rho Pi_A`. Both have `Tr R_A=1/2`. In the first family,
`R_A` has nonzero spectrum `(1/2)`; in the second, `(1/4,1/4)`.
The DPP probability of one index in each block is respectively `1` and
`1/2`. Equivalently the within-A DPP mass is `0` and `1/4`.

A known two-copy antisymmetric test already decides this scalar promise:
project both copies into `A` and measure their swap sign. The negative
event has probability

```
((Tr R_A)^2 - Tr(R_A^2))/2 = 0 or 1/16.
```

Repeating a constant number of times gives a constant-error decision.
Hence a separation proved only for this bit would not establish a new
quantum mechanism or the need for the full support conversion.

A matched classical upper bound for the bit is available without
tomography: measure the block first, keep the A outcomes, and estimate
purity of the resulting rank-one versus rank-two state using randomized
single-copy measurements and collision statistics. The required copies
are `O(sqrt(d))` for constant accuracy; the block filtering changes this
only by a constant expected factor, with a bounded cap obtainable by
a concentration bound. The general single-copy purity-estimation upper
bound is stated in
[On the sample complexity of purity and inner product estimation,
arXiv:2410.12712](https://arxiv.org/abs/2410.12712).

**Resolved objection B2 — first-moment matching is insufficient.** The
second hidden-frame ensemble has off-diagonal A--B coherence. Its
single-copy ensemble average agrees with the first, but adaptive
transcripts depend on higher moments. A lower bound after dephasing
the input is not automatically a lower bound before dephasing: the
allowed measurement may mix the two blocks.

**FIX DEMAND:** retain the full coherent-transcript proof audited in
Section 3.4. Do not replace it by matching averages or the general
worst-case purity lower bound.

**SURVIVING STATEMENT:** the displayed probability gap and constant-copy
collective bit test are exact; an `O(sqrt(d))` single-copy upper bound
holds; the root's additional argument supplies the matching adaptive
single-copy decision lower bound and a sampler lower bound.

### 3.4 Independent review of the quantitative root proof

The proof in `scouting/support-plucker-classical-r9.md` survives the
following audit, including the off-diagonal coherence. For every fixed
copy cap `T`, both averaged full transcript laws dominate the same
maximally-mixed-source law by

```
P_theta >= c_T P_*,        c_T=[d/(d+T-1)]^T.
```

1. For degree `L` holomorphic polynomials in one full `d` by `d` matrix,
   left/right unitary invariance and the Cauchy decomposition make each
   partition sector a scalar covariance block. Its Haar/Gaussian squared
   norm ratio, for Gaussian entry variance `1/d`, is
   `d^L/product_((i,j) in lambda)(d+j-i)`. Every denominator factor is at
   most `d+L-1`. Partitions with more than `d` rows are absent from the
   polynomial representation itself. No hypothesis `L<=d` is required.
2. The product of the linear amplitudes in a fixed transcript is of total
   degree `T` in the two independent frame matrices. For the coherent
   ensemble it need not have one fixed bidegree. Independent central
   phases make distinct bidegrees orthogonal under both Haar and Gaussian
   measures. On a bidegree `(L,T-L)`, the product of the two preceding
   lower ratios is at least `c_T`. This justifies the stated comparison
   without discarding any A--B cross terms.
3. Under circular complex Gaussian measure, multiplication by a linear
   holomorphic form is a Fock creation operator. Its squared norm is the
   form variance times the preceding squared norm plus a nonnegative
   annihilation-operator term. Iterating yields
   `E product_t |f_t|^2 >= product_t E|f_t|^2`. This is the homogeneous
   complex Gaussian product inequality needed here; no stronger and
   potentially false inhomogeneous version is being used.
4. Refining single-copy effects to rank one is legitimate. On a fixed
   complete adaptive leaf, all effect vectors are fixed. For each latent
   mixture-label sequence, the source amplitude is a product of linear
   forms, so Steps 1--3 apply before summing the positive mixture weights.
   The sum factors into the product of degree-one variances, each equal
   to the effect probability under `tau=1/(2d)`. The resulting reference
   law `P_*` is a normalized physical transcript law, although the
   intermediate Gaussian matrices are not normalized quantum states.
5. The common domination implies
   `P_theta=c_T P_*+(1-c_T)Q_theta`, and hence
   `TV(P_0,P_1)<=1-c_T<=T(T-1)/d`. Classical randomness, rank-one
   refinement, continuous outcome measures and coarse-graining preserve
   this argument. The copy cap is fixed; no expected-time stopping
   lower bound is implicitly claimed.

An always-output sampler within TV `epsilon` of the DPP on every promised
support must have cross-block event probabilities differing by at least
`1/2-2epsilon`. Therefore

```
T(T-1) >= d(1/2-2epsilon).
```

At `epsilon<=1/16`, this is at least `3d/8`; since `q=2d`, it gives the
claimed `Omega(sqrt(q))` lower bound. For the decision bit, a test correct
with probability at least `2/3` in both cases requires transcript TV at
least `1/3`, and therefore `T(T-1)>=d/3`. Together with Section 3.3, the
classical bit complexity is `Theta(sqrt(d))` at constant error, versus
constant collective copies. The exact certified quantum sampler can
be made always-output with TV at most `delta` by the fallback convention
in B1, matching the sampler lower bound's interface.

This is a valid same-classical-output copy separation. For the scalar
bit its quantum operation is the known two-copy antisymmetric purity
test; for growing-r conversion Section 2 supplies the prior-algorithm
reduction. Neither conclusion meets D22.

### 3.5 Accepted three-copy hardware diagnostic

For rank two, let `Delta=det(rho restricted to U)` and use one triple of
copies. Measure first-pair antisymmetry. After a failure, swap physical
registers 2 and 3 and repeat the first-pair measurement, allowing at most
`L` such recycle steps after the initial measurement. Every click returns
the exact support Slater state on registers 1 and 2.

Algebraically, the rank-two source has no `(1,1,1)` sector. The fully
symmetric sector has mass `1-2Delta` and never clicks; the standard
`(2,1)` sector has mass `2Delta`, split equally between its two first-pair
symmetry paths. The initial click therefore has mass `Delta`. On every
remaining standard-sector branch, the next swap and measurement transfer
`3/4` of its mass to the antisymmetric path and retain `1/4` in precisely
the original symmetric path. Consequently the capped success probability is

```
Delta + (3Delta/4) sum_(j=0)^(L-1) 4^(-j)
  = Delta (2-4^(-L)),                   L >= 0.
```

For flat rank two and one recycle step, this is `7/16`. The fixed-triple
success ceiling is `2Delta<=1/2`. No additional source copies are consumed
by recycling. At `q=4`, the circuit uses six data qubits and one reusable
swap-test ancilla: at most `2(L+1)` Fredkin gates for the pair tests and
`2L` ordinary qubit SWAP gates, together with ancilla Hadamards, measurement
and classical feedback. This is a concrete known-comparison/purification
implementation under the stated exact-copy/gate model, with no novelty
claim. The derivation uses the already audited two-dimensional Young
block; no new broad test run is needed.

## 4. Bounded independent checks and integration

An in-memory Python/NumPy check, bounded by `timeout 45s`, built full
physical permutation matrices for `q=3,4`, `N=3`. Its 22 checks covered
the `(2,1)` row/column path projectors, the signed Young diagonal
coefficient, the `3/4` transition probability, failure restoration,
mixed-state output factorization for spectra `(1/2,1/2)` and `(0.8,0.2)`,
and the flat-source shape probability `1/2`. Maximum residual:
`1.86e-16`. A separately run mutation replaced `3/4` by `1/2` and exited
nonzero (exit code 1), with residual `0.25` in the two-dimensional block.
No checker file or extra artifact was written.

A second bounded check at `d=5` verified the hidden-frame cross-block
DPP masses `1` and `1/2` and the two-copy event probabilities `0` and
`1/16`; numerical residuals were below `5e-16`. These finite checks
support only the specific operator identities tested. The universal
statements rest on Sections 1--3, not numerical extrapolation.

A third independent bounded check evaluated exact second-order Haar
moment formulas for random global adaptive two-copy projective
measurements at `d=2,3,8`. All 616 leaf minorization inequalities held,
including the coherent A--B covariance term; the smallest numerical
slack was `0.000589`, and transcript normalization error was at most
`7.77e-16`. The measured TVs were `0.023002367`, `0.023665942` and
`0.011436917`, each below its `1-c_2` bound. This is a finite diagnostic
of the transcript calculation, not a substitute for Section 3.4.

The original exactness and adaptive-baseline objections are resolved.
Root may integrate the scoped mathematical claims with a mathematical
PASS, while preserving the FATAL D22 mechanism verdict. No claim can
be promoted to a north-star hit on this audit.

## 5. Independent canonical-integration addendum — 2026-09-05

The dedicated report/editorial agent independently cross-checked the newly
registered C-361--C-364 against the canonical support definitions, the author
construction, and the saved independent audit above. This is an integration
and scope review; it does not substitute a new numerical run for the proofs.

**Integration verdict: scoped PASS, with no FATAL or MAJOR integration
discrepancy.** The existing FATAL N1 remains the mathematical construction's
separate originality verdict, correctly recorded as REFUTED in C-364.

- **C-361:** the finite-circuit exact accepted-output statement preserves the
  exact source-support and physical-permutation assumptions, and excludes
  arbitrary hardware noise. Substituting `K=O(N^2 log N)` and `m=O(log N)`
  into the detailed resource bound gives the registered conservative
  `O(B N^7 log^4 N [w+log^4 N])` gate cap. Independent batches with acceptance
  at least `1/16` justify expected source cost at most `16N`; the capped
  failure/fixed-subset convention gives the stated always-output TV bound.
- **C-362:** the row keeps the full coherent adaptive-transcript law, the
  fixed total copy cap, and the relation `q=2d`. At `epsilon<=1/16`,
  `d(1/2-2epsilon)>=3d/8=3q/16`. One recycle step gives
  `1/4+(3/4)(1/4)=7/16`; five independent triples fail with probability
  `(9/16)^5<1/16`, so 15 is a valid sufficient copy cap. This is not a
  claim of practical runtime optimality or a coefficient-list lower bound.
- **C-363:** the statement retains `2<=r<q`, separability across source
  copies, the failure-flag and finite-terminal-time scope, and the distinction
  between exact nonexistence and the separate quantitative approximate lower
  bound. Its proof provenance is the positivity argument, not finite tests.
- **C-364:** the row records the specific generalized-phase-estimation,
  multiplicity-reset and signed-permutation reduction. It preserves exact
  support under ancillary approximation and does not infer novelty failure
  merely from elementary-gate universality. It does not assert prior
  publication of the exact growing-r DPP theorem.

One MINOR parameter-quantifier correction was identified during this review:
C-362's finite `log(1/epsilon)` repetition formula requires positive error.
The canonical row now explicitly states `0<epsilon<1/4`; this was verified
before the scoped PASS. No claim-status change is requested by this addendum,
and the original-algorithm research goal remains unachieved.
