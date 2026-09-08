# Minimal-syzygy coefficient sampling by passive linear optics

2026-09-07. R12 construction memo under D25. This is a candidate and not a
canonical claim-status file. The algebraic and sampling identities below are
unconditional. The exact classical-hardness consequence is an implication to a
polynomial-hierarchy collapse, not an unconditional time lower bound. The
approximate-sampling consequence additionally uses the standard average-case
permanent and anti-concentration conjectures. No downstream algebraic-geometry
speedup is established merely by giving the distribution a syzygy name.

## 1. Problem, compact input and output

Fix integers `m>=2` and `q>=2m`, and put

`R=C[z_1,...,z_q]`,
`S_1={1,...,m}`, `S_2={m+1,...,2m}`,
`f_1=product_(i in S_1) z_i`, `f_2=product_(i in S_2) z_i`.             (1)

The finite classical input is `(m,q,U_description,epsilon)`, in one of three
explicit models:

1. **Exact circuit input:** a list of `B=poly(q)` two-mode beam splitters and
   phase shifts with entries in a declared exact algebraic gate set, whose
   product is `U in U(q)`.
2. **Finite-mesh input:** a list of `B=poly(q)` exactly unitary two-mode gates,
   each angle/phase specified to `b` bits, whose product is the exactly defined
   mesh unitary `U_tilde`. The target is the distribution for `U_tilde`, not
   for an unrecorded laboratory setting.
3. **AA exact-hardness input:** a `q x m` column-isometry description `A` in
   the polynomial binary-precision convention of Aaronson--Arkhipov, followed
   by their stated Gram--Schmidt correction when the encoded columns are only
   exponentially close to orthonormal. Fix a deterministic polynomial-time
   Gram--Schmidt completion `U_A in U(q)` whose first `m` columns are `A`.
   The exact sampling implication is formulated for this standard mathematical
   matrix model. It does not assert exact synthesis of arbitrary continuous
   angles by a fixed finite digital gate set.

Both quantum and classical algorithms receive the same description and
completion rule. The transformed
based ideal is supplied succinctly, not by expanded coefficient tables:

`phi_U(z_i)=sum_(r=1)^q U_(ri) z_r`,
`I_U=(F_1,F_2)`, `F_j=phi_U(f_j)`.                                    (2)

One output is `(j,nu)`, where `j in {1,2}`, `nu=(nu_1,...,nu_q)` is an
occupation vector with nonnegative entries and `sum_r nu_r=m`. Define
`nu!=product_r nu_r!` and let `U[nu,S]` be the `m x m` matrix whose columns are
indexed by `S` and whose row `r` occurs `nu_r` times. The ideal target law is

`P_U(j,nu)=|Per(U[nu,S_(3-j)])|^2/(2 nu!).`                            (3)

The approximate problem asks for independent samples from a distribution `Q`
with total-variation distance at most `epsilon` from (3). Collisions are part
of the output. There is no collision postselection, spectral-gap promise,
QRAM, expanded ideal, quotient basis, Gibbs state or hidden normalization.

Equation (3) is the squared Fock-coefficient distribution of the normalized
distinguished minimal syzygy defined below. It is basis sensitive: `U` and the
ordered generator frame are part of the input. It is not an intrinsic invariant
of the unbased projective scheme.

## 2. Exact algebraic geometry

### 2.1 Regular sequence and minimal resolution

The monomials `f_1,f_2` are coprime. Since `R` is a domain, `f_1` is a
non-zero-divisor. The associated primes of the squarefree principal ideal
`(f_1)` are `(z_i)` for `i in S_1`; `f_2` belongs to none of them. Hence `f_2`
is a non-zero-divisor modulo `(f_1)`, and `(f_1,f_2)` is a homogeneous regular
sequence of degrees `(m,m)`.

The Koszul resolution is therefore minimal:

`0 -> R(-2m) --d_2--> R(-m)^2 --d_1--> R -> R/I_0 -> 0`,              (4)

with

`d_1(h_1,h_2)=h_1f_1+h_2f_2`,
`d_2(1)=(f_2,-f_1)`.                                                   (5)

For completeness, the kernel assertion in (5) can be proved without invoking
the general theorem. If `h_1f_1=-h_2f_2`, coprimality in the UFD `R` implies
`f_2|h_1` and `f_1|h_2`; hence `(h_1,h_2)=a(f_2,-f_1)`. At total degree `2m`,
`a` is a scalar. Thus the degree-`2m` minimal first-syzygy space is one
dimensional and

`beta_(2,2m)(R/I_0)=1`.                                                (6)

The linear substitution `phi_U` is a graded algebra automorphism. Applying it
entrywise to (4) preserves exactness and minimality, so the transformed ideal
`I_U` has the distinguished generator

`s_U=(F_2,-F_1)=(phi_U(f_2),-phi_U(f_1))`                              (7)

of its degree-`2m` first syzygy. The projective scheme
`V(I_U) subset P^(q-1)` is a codimension-two complete intersection of two
unions of hyperplanes. The construction is genuine scheme/syzygy data, though
the factorization is deliberately supplied compactly.

### 2.2 Fock normalization

Give `R_m` the standard Fock inner product: the normalized occupation ket is

`|nu>=z^nu/sqrt(nu!)`.                                                 (8)

Every squarefree monomial in (1) has norm one. The symmetric-power action
`Gamma_m(U)` is unitary on `R_m`, so `||F_1||=||F_2||=1`. In the orthogonal
module summands `R_m e_1 direct-sum R_m e_2`, (7) has norm `sqrt(2)`, and its
normalized coefficient state is

`|s_U>=(|1> Gamma_m(U)|S_2>-|2> Gamma_m(U)|S_1>)/sqrt(2)`.             (9)

Expanding the product of linear forms gives the raw monomial coefficient

`[z^nu] phi_U(f_S)=Per(U[nu,S])/nu!`.                                 (10)

Multiplying by `sqrt(nu!)` to pass from raw monomials to the normalized basis
(8) gives

`<nu|Gamma_m(U)|S>=Per(U[nu,S])/sqrt(nu!).`                            (11)

Equations (9)--(11) prove the probability law (3). They also show why the
collision factorial is required.

## 3. Quantum and optical sampler

### 3.1 No module cat state is required

The output measures the module label, so its two summands never interfere. A
fair sampler may therefore use classical randomness:

1. Draw `j` uniformly from `{1,2}`.
2. Inject one indistinguishable photon in every mode in `S_(3-j)` and vacuum in
   the other modes.
3. Apply the supplied passive `q`-mode interferometer `U`.
4. Number-resolve every output mode, obtaining `nu`, and return `(j,nu)`.

Conditioned on `j`, steps 2--4 are standard BosonSampling; (11) proves (3).
There is no rejection or success normalization. One sample uses exactly `m`
source photons, one classical random bit, `B` supplied two-mode optical gates,
and `q` photon-number-resolving measurements. A universal mesh has
`B=Theta(q^2)` elements and optical depth `O(q)` in a rectangular layout.

A coherent preparation of (9) is possible using a label qubit and controlled
input routing, but it is unnecessary for this classical output and is not
included for free. It becomes necessary only for an observable that mixes the
two generator labels.

For `R_samp` accepted samples, the ideal source count is `m R_samp`, gate uses
are `B R_samp`, and detector records are `q R_samp`. Sampling error is the TV
guarantee of the device or algorithm; there is no additional Monte Carlo error
unless a downstream statistic is estimated from the samples.

### 3.2 Fault-tolerant/digital reading

A digital implementation may encode occupations in
`O(m log(q+m))` qubits and compile each two-mode bosonic rotation on the
fixed-`m` sector. Its cost is polynomial in `B,m,log q,b,log(1/epsilon_gate)`.
This memo does not claim that such a compilation is preferable to the native
photonic circuit. The heuristic-hardware criterion is met much more directly by
passive optics.

## 4. Exact transfer to BosonSampling

### 4.1 Exact samplers

Suppose a probabilistic classical algorithm samples (3) exactly in expected
time `T(m,q,|U_description|)`. In the AA matrix model choose the deterministic
completion `U_A`; its columns in `S_1` are precisely the supplied isometry
`A`. To sample ordinary BosonSampling with input ports `S_1`, call
it until `j=2` and return `nu`. The label has probability exactly `1/2`, so the
expected number of calls is two and the conditional distribution is

`P_U(nu|j=2)=|Per(U[nu,S_1])|^2/nu!`.                                 (12)

Thus a polynomial-time exact syzygy sampler for all allowed circuits gives a
polynomial-time exact BosonSampling algorithm. Conversely, a BosonSampling
oracle plus a fair coin samples (3), so the two sampling tasks are equivalent
up to a factor-two expected overhead.

This direct AA matrix formulation closes the gate-family containment issue for
the mathematical exact-sampling reduction. If the exact circuit model is used
instead, its allowed algebraic gate-description family must still contain the
hard interferometers with polynomial description length; a small exactly
synthesizable subgroup need not do so. The exact complexity theorem does not
turn this continuous optical model into a fault-tolerant exact digital circuit.

[Aaronson--Arkhipov, arXiv:1011.3245](https://arxiv.org/abs/1011.3245)
prove that an efficient exact classical BosonSampling algorithm would imply
`P^#P=BPP^NP` and collapse the polynomial hierarchy to its third level. The
unconditional result here is the reduction (12) and that complexity
implication. “Classical exponential lower bound” requires the usual assumption
that the polynomial hierarchy does not collapse.

### 4.2 Approximate joint samplers and branch conditioning

Let `P` be (3), let `TV(P,Q)<=epsilon<1/4`, and put
`q_j=sum_nu Q(j,nu)`. Event monotonicity gives
`q_j>=1/2-epsilon`. Let `P_j,Q_j` denote the distributions conditioned on
label `j`. If
`d_j=sum_nu|P(j,nu)-Q(j,nu)|`, then

`TV(P_j,Q_j)`
` <= d_j+|q_j-1/2| <= 3epsilon`.                                      (13)

The first inequality follows by adding and subtracting `2Q(j,nu)`; the second
uses `d_j<=2epsilon` and the marginal TV bound. Rejection until a chosen label
has expected cost at most `(1/2-epsilon)^(-1)`. Therefore an efficient
`epsilon`-approximate joint syzygy sampler gives an efficient
`3epsilon`-approximate ordinary BosonSampler for either fixed branch.

For Haar-random interferometers in the usual many-mode collision-sparse regime,
Aaronson--Arkhipov's approximate hardness conclusion additionally assumes the
Permanent-of-Gaussians average-case hardness conjecture and the Permanent
Anti-Concentration Conjecture. Under those conjectures, an efficient classical
small-TV sampler would again collapse the polynomial hierarchy. Those are
explicit assumptions. No unconditional approximate-sampling lower bound is
claimed.

The Haar statement is an input-distribution statement, not a worst-case theorem
for every `U`. Structured networks, shallow meshes, block-diagonal networks and
large-loss regimes may be classically easy.

### 4.3 Finite mesh and bit precision

The laboratory and classical input must be finite. Suppose a `B`-gate optical
mesh approximates a target Haar unitary `U` by `U_tilde`, and each two-mode gate
has operator error at most `delta_gate`. Telescoping the gate products gives

`||U-U_tilde|| <= B delta_gate`.                                      (14)

Restricting tensor powers to the symmetric sector and telescoping again gives

`||Gamma_m(U)-Gamma_m(U_tilde)|| <= m ||U-U_tilde||`.                 (15)

Hence every occupation measurement has output TV distance at most

`m B delta_gate`                                                      (16)

from the ideal target. This agrees with the sharper network-error analysis in
[Arkhipov, arXiv:1412.2516](https://arxiv.org/abs/1412.2516), which bounds
BosonSampling variation distance linearly in photon number and unitary
operator error. Choosing

`delta_gate<=epsilon_mesh/(mB)`

requires only `b=O(log(mB/epsilon_mesh))` bits per smoothly parameterized gate.
Rounding angles, rather than matrix entries independently, keeps every recorded
gate exactly unitary.

For an approximate-hardness statement on finite inputs, one must specify the
distribution of rounded Haar meshes and add `epsilon_mesh` to the sampler's TV
error before applying (13). Robustness (16) makes such a reduction plausible,
but this memo does not silently identify a discrete mesh ensemble with exact
Haar measure.

## 5. Best classical algorithms and what is actually known

For arbitrary dense interferometers, [Clifford--Clifford,
arXiv:1706.01260](https://arxiv.org/abs/1706.01260) give an exact classical
BosonSampling algorithm using

`O(m 2^m+poly(|U_description|,q,m,b))` time and `O(q)` additional space
per sample,                                                                  (17)

where the polynomial term includes constructing the required matrix entries
from the same gate list. Their later algorithm
[arXiv:2005.04214](https://arxiv.org/abs/2005.04214) improves average exact
time in particular proportional-mode regimes. Those constants are not claimed
for this candidate's collision-sparse large-`q` hardness regime; (17) is the
clean general upper bound used here. Reading or compiling an explicit dense
interferometer already costs `Theta(q^2)` and is charged on both sides.

There is no proved general exponential classical time lower bound for sampling
(3). The evidence is:

| statement | status |
|---|---|
| algebraic resolution, normalized syzygy and permanent law | unconditional proof in sections 2--3 |
| exact syzygy sampler implies exact BosonSampler | unconditional reduction, section 4.1 |
| efficient exact classical sampler implies PH collapse | published complexity implication |
| absence of polynomial exact classical sampler | conditional on noncollapse of PH |
| approximate hardness for Haar networks | conditional on average-case permanent hardness, anti-concentration, and the stated finite-precision transfer |
| `O(m2^m+poly(q,m))` exact classical sampler | published upper bound |
| polynomial quantum/passive-optical ideal sampling | unconditional circuit identity, conditional experimentally on scalable sources/components/detectors |

Approximate classical simulation has additional algorithms in special regimes:
high photon loss, partial distinguishability, low-depth or low-treewidth optical
circuits, or output statistics coarser than the full sample. A hardware claim
must therefore report these parameters rather than cite only (17).

## 6. Noise, loss and total resources

### 6.1 Coherent implementation error

Let the actual normalized `m`-photon input be `rho_in` at trace distance at
most `epsilon_src` from the desired indistinguishable Fock state. Let the
implemented unitary have operator error `delta_U`, and let detector
postprocessing differ from ideal PNR measurement by at most `epsilon_det` in
TV for every input. Contractivity and (15) give the conservative conditional
bound

`TV(P_ideal,P_impl)<=epsilon_src+m delta_U+epsilon_det+epsilon_label`. (18)

Here `epsilon_label` charges a biased/correlated module-label coin. This bound
does not model every distinguishability parameter; it says exactly which
trace-distance promise is sufficient.

### 6.2 Photon loss is not a free restart

If each prepared photon is present and survives to a detector independently
with uniform probability `eta_tot`, the probability of an accepted `m`-photon
record is `eta_tot^m`. Uniform loss conditioned on detecting all `m` photons
leaves (3) unchanged, but `R_samp` accepted samples require expected raw trials

`R_samp eta_tot^(-m)`.                                                 (19)

Thus constant `eta_tot<1` makes the source/runtime exponential. Polynomial
end-to-end sampling needs `eta_tot^m>=1/poly(m)`, equivalently
`-m log eta_tot=O(log m)`; near one this requires
`1-eta_tot=O(log(m)/m)`. Alternatively, near-deterministic multiplexed sources
and detectors must be a stated hardware assumption.

Mode-dependent loss is more serious. Conditioned on no loss, the effective
single-particle matrix need not be proportional to a unitary. Its normalized
many-boson output is then not the coefficient law of the coordinate
automorphism (2). One may define and calibrate a different nonunitary sampling
problem, or prove it is close to `sqrt(eta)U`; postselection cannot simply call
the result `s_U`.

Known lossy hardness results, for example [Aaronson--Brod,
arXiv:1510.05245](https://arxiv.org/abs/1510.05245), treat specified numbers of
lost photons and precisions. They do not erase the source-attempt factor (19).

### 6.3 End-to-end ledger

For one ideal accepted sample:

| resource | cost/assumption |
|---|---|
| classical input | mesh model: `B` two-mode gates, `b` bits each, plus `m,q`, size `O(Bb+m log q)`; AA model: its standard finite column-isometry description and fixed completion rule |
| source | `m` indistinguishable photons in one of two fixed port sets |
| quantum evolution | `B`, at most `Theta(q^2)`, passive two-mode elements; depth `O(q)` for a universal rectangular mesh |
| quantum memory | `q` optical modes with total occupation `m`, plus one classical label bit |
| measurement | `q` PNR outcomes, serialized as `O(m log q)` bits |
| ideal failures | none; collisions retained |
| physical repetitions | multiply by `eta_tot^(-m)` under the uniform-loss/postselected model |
| accuracy | add the terms in (18); mesh bits satisfy section 4.3 |
| classical exact comparison | (17), plus reading the same `B`-gate circuit |

[Clements et al., arXiv:1603.08788](https://arxiv.org/abs/1603.08788) provide
the rectangular universal-interferometer mesh underlying the `Theta(q^2)`
component and `O(q)` depth figures. The asymptotic optical propagation count
does not include source multiplexing or detector recovery time; (19) supplies
the missing success ledger.

## 7. Utility audit: valid AG task versus useful AG primitive

### 7.1 What the samples literally mean

The law (3) explores the Bombieri--Fock coefficient energy of the unique
minimal relation (7), in a specified variable basis and ordered generator
frame. It can directly provide:

- random monomials weighted by their contribution to the norm of a stored
  syzygy component;
- Monte Carlo estimates of bounded diagonal statistics of its exponent vector;
- empirical coefficient-delocalization and collision diagnostics under a
  change of coordinates;
- samples for a downstream method that explicitly accepts Fock-weighted
  monomial samples rather than a coefficient list.

These are legitimate outputs about a minimal free resolution. None is presently
shown to accelerate Gröbner bases, Schreyer resolution, regularity, membership,
deformation, or numerical conditioning. Low-order occupation moments can often
be computed directly from `U`; a generic diagonal statistic may have a direct
classical estimator even when full-distribution sampling is hard.

### 7.2 The component-collapse objection

The relative minus sign in (7) certifies cancellation
`F_2F_1-F_1F_2=0`, but measuring the direct-sum label removes all interference
between the two components. Operationally, (3) is exactly a fair coin followed
by coefficient sampling from one of the two factored generators. The hardness
does not use syzygy cancellation. A single component is already a point of the
Chow variety of completely decomposable degree-`m` forms, and its coefficient
sampling is ordinary BosonSampling.

This does not invalidate the exact AG definition or hardness transfer. It does
mean that calling the task “syzygy sampling” is not yet a usefulness result.
The based minimal relation supplies provenance and a clean AG family, while the
computational content remains sampling a factored form after a coordinate
change.

### 7.3 Possible next use, stated only as a test

A plausible consumer is a matrix-free numerical resolution method that uses
coefficient-energy samples as importance proposals for selecting monomial rows
or columns. The next experiment should compare:

1. uniform monomial proposals;
2. proposals from (3);
3. classically computable approximations from one- and two-mode marginals;
4. exact Clifford--Clifford samples at small `m`;

on a downstream residual or sketch-variance metric fixed before sampling. A
measured variance reduction would be finite evidence, not an asymptotic
speedup. Haar-random BosonSampling distributions are highly delocalized, so a
large heavy-coordinate benefit should not be assumed.

A coherent label measurement could sample coefficients of `F_2+/-F_1` and
would retain the relative phase, but those are still known linear combinations
of the supplied factors. It needs coherent label/input routing and a new output
definition; it is not part of (3).

### 7.4 A frame-free leverage marginal: partial repair, not a utility theorem

There is a stricter variant that removes the ordered-generator label from the
output. Let the `m` marker modes be `S_2`, let the hard block contain `S_1` and
all remaining modes, and restrict

`U=V_hard direct-sum I_(S_2)`.                                       (20)

Here `V_hard` is an arbitrary BosonSampling interferometer on the `q-m` hard
modes. Then `F_1=Gamma_m(V_hard)|S_1>` has support only on hard-mode
occupations, while `F_2=|S_2>` is the fixed marker monomial. They remain
orthonormal. Since the ideal has no elements below degree `m`,

`(I_U)_m=span(F_1,F_2)=:W`,
`P_W=|F_1><F_1|+|F_2><F_2|`.                                        (21)

Trace out the module label in (9) and measure only `nu`. The law is

`L_U(nu)=<nu|P_W|nu>/2`.                                              (22)

This is the monomial leverage-score distribution of the intrinsic degree-`m`
ideal subspace in the fixed coordinate/Fock metric. It is unchanged by a
unitary change of the two-generator frame. Because the marker and hard supports
are disjoint, rejecting the unique marker occupation in (22) has probability
`1/2` and leaves ordinary BosonSampling for `V_hard`; the exact and approximate
conditioning reductions of section 4 apply unchanged.

Equation (22) is more intrinsic than the labelled law: it depends on the
embedded ideal degree piece rather than an ordered orthonormal generating
tuple. Leverage-score sampling is a legitimate row-selection primitive in
randomized linear algebra. In this compact factored input, however, a sampled
row does not come with its coefficient value; computing that value is itself a
permanent problem. No theorem here turns (22) into a faster subspace embedding,
Macaulay solve or minimal resolution. Moreover the syzygy cancellation is still
unused. This is a partial response to the component-collapse objection, not a
north-star repair.

### 7.5 Current north-star score

| PRD criterion under D25 | assessment |
|---|---|
| precise AG problem | met: based minimal-syzygy coefficient distribution (3) |
| classical baseline | met for exact full-distribution sampling; regime-specific approximate baselines remain |
| quantum speedup | conditional: polynomial ideal optics versus PH consequence/standard exponential exact upper bound; no unconditional lower bound |
| dequantisation/hidden costs | explicit for branch conditioning, precision, collisions, sources and loss; approximate conjectures remain |
| heuristic hardware | met directly by passive linear optics, subject to (19) |
| eligible mechanism D25 | met: BosonSampling is not QFT, Grover or DQI |
| useful intrinsic AG output | **not established**: basis sensitive, factored, and no downstream improvement proved |

The construction is therefore a reviewable conditional sampling advantage and
a strong hardware demonstration, but not yet a completed north-star algorithm.
Usefulness is the decisive unresolved gate.

## 8. Small hardware diagnostic

Take `m=2,q=4`,

`f_1=z_1z_2`, `f_2=z_3z_4`,

and let `U` be a balanced beam splitter on modes `(1,2)` and independently on
`(3,4)`, with

`z_1 -> (z_1+z_2)/sqrt(2)`, `z_2 -> (z_1-z_2)/sqrt(2)`,

and the analogous map on `(3,4)`. Then

`F_1=(z_1^2-z_2^2)/2`, `F_2=(z_3^2-z_4^2)/2`,
`s_U=(F_2,-F_1)`.                                                      (23)

In normalized Fock coordinates, each square term in (23) has amplitude
`+/-1/sqrt(2)`. The four joint outputs

`(j=1,nu=0020)`, `(j=1,nu=0002)`,
`(j=2,nu=2000)`, `(j=2,nu=0200)`

therefore each have probability `1/4`; all coincidence outputs have
probability zero. Here strings such as `0020` denote occupation vectors.

This four-mode/two-photon experiment checks the label factor `1/2`, the
collision factorial in (3), Fock normalization, and Hong--Ou--Mandel
interference. A distinguishable-photon mutation restores coincidences and can
make the diagnostic red. It does not verify asymptotic hardness, approximate
Haar anti-concentration, scalable loss, minimality of an unknown resolution,
or downstream usefulness; the algebra in (23) is classically immediate.

## 9. Targeted primary-source resolution

The construction and reductions were derived before these checks.

1. [Aaronson--Arkhipov,
   arXiv:1011.3245](https://arxiv.org/abs/1011.3245) defines BosonSampling,
   proves the exact classical-sampling collapse consequence, and states the
   conjectures used for approximate hardness.
2. [Clifford--Clifford,
   arXiv:1706.01260](https://arxiv.org/abs/1706.01260) supplies the general
   `O(m2^m+poly(q,m))` exact sampler; their
   [faster follow-up, arXiv:2005.04214](https://arxiv.org/abs/2005.04214)
   improves particular mode regimes.
3. [Arkhipov,
   arXiv:1412.2516](https://arxiv.org/abs/1412.2516) proves linear robustness
   of the output distribution to small operator-norm network error, consistent
   with (14)--(16).
4. [Aaronson--Brod,
   arXiv:1510.05245](https://arxiv.org/abs/1510.05245) studies specified lost-
   photon BosonSampling. It is a hardness comparison, not permission to omit
   the exponentially small no-loss probability.
5. [Clements et al.,
   arXiv:1603.08788](https://arxiv.org/abs/1603.08788) gives a universal
   rectangular mesh of beam splitters and phase shifters and its loss-robust
   layout.

No source was located that makes minimal-syzygy coefficient samples a proved
accelerator for a downstream algebraic-geometry computation. Absence of such a
source is not an impossibility theorem, and no utility claim is promoted.

## MERGE PROPOSAL

**D-R12-SYZYGY-BOSONSAMPLE.** Input: integers `m>=2,q>=2m`, the fixed disjoint
port sets and monomials (1), an exact algebraic circuit, a finite unitary
two-mode-gate mesh, or the standard finite AA column-isometry input with fixed
polynomial-time unitary completion, and TV tolerance `epsilon`. It defines the succinct based ideal
`I_U` in (2), its distinguished degree-`2m` first syzygy (7), and output
`(j,nu)` with target law (3). The input does not contain expanded coefficient
tables. Collisions are retained. Source, mesh, detector, precision and loss
costs are charged.

**C-R12-SYZYGY-ALGEBRA (proposed SKETCH).** For every
D-R12-SYZYGY-BOSONSAMPLE input, `(F_1,F_2)` is a regular sequence, (4)--(5) is
its minimal resolution, `beta_(2,2m)=1`, and the normalized distinguished
syzygy state is (9). Its Fock coefficients obey (10)--(11).

**C-R12-SYZYGY-OPTICS (proposed SKETCH).** A fair classical label choice,
`m` single photons, the supplied passive circuit and PNR detection sample (3)
exactly in the ideal model using `B` optical elements per output and no
postselection. With the trace/operator error model of section 6, the conditional
TV error obeys (18), while uniform total transmission `eta_tot` multiplies raw
trial cost by `eta_tot^(-m)`.

**C-R12-SYZYGY-BS-REDUCTION (proposed SKETCH).** An exact classical sampler for
(3) yields an exact ordinary BosonSampler with two expected calls by conditioning
on either label. If a joint sampler is within TV `epsilon<1/4`, the chosen-label
conditional sampler is within `3epsilon` and uses at most
`(1/2-epsilon)^(-1)` expected calls. Consequently the published exact PH
collapse implication transfers when the allowed algebraic circuit family
contains the standard hard interferometers with polynomial descriptions, or
directly in the AA matrix/completion model. The approximate PH implication
transfers only under the explicitly stated permanent, anti-concentration and
finite-mesh assumptions.

**C-R12-SYZYGY-UTILITY (proposed HOLD, not a positive claim).** The output is a
basis-sensitive Fock coefficient distribution of a minimal relation, but the
measured module label reduces it to a coin followed by generator/Chow-form
coefficient sampling. No downstream AG speedup or intrinsic invariant is known.
The next required result is either a demonstrated consumer of these samples or
a syzygy-coherent output whose advantage depends on relation cancellation.

## 10. Response to the independent R12 verdict

The independent verdict accepted the regular-sequence proof, Fock/permanent
normalization, ideal optical sampler, `3epsilon` conditioning lemma, mesh-error
bound, loss ledger and small diagnostic. Its objections are dispositioned as
follows.

1. **B1, exact hard gate family: repaired.** Section 1 now includes the standard
   finite AA column-isometry model and a fixed polynomial-time unitary
   completion. Section 4.1 states exact hardness directly in that model and
   keeps arbitrary continuous optical transformations separate from exact
   digital synthesis. An alternative algebraic circuit family must still prove
   containment of the hard networks.
2. **B2, rounded-Haar approximate ensemble: HOLD.** Equations (14)--(16) prove
   paired-unitary output robustness. They do not prove average-case hardness of
   a chosen discrete mesh ensemble. The approximate claim remains conditional
   on a precisely stated finite-ensemble transfer in addition to the permanent
   and anti-concentration conjectures.
3. **B3, unused syzygy cancellation: HOLD and made central.** Section 7.2 states
   the component-collapse exactly. Section 7.4 gives a generator-frame-free
   ideal-degree leverage marginal, but it still does not use cancellation or
   prove a downstream improvement. No north-star promotion is proposed.
4. **B4, fixed loss: accepted without weakening.** Every scalable physical
   claim is conditional on the ideal model or
   `-m log(eta_tot)=O(log m)`; equation (19) charges all raw attempts. Fixed
   efficiency below one destroys polynomial end-to-end runtime.
5. **B5, classical input processing and mode regime: repaired.** Equation (17)
   includes polynomial dependence on the full unitary description. The faster
   follow-up is cited only for proportional-mode regimes; no `q=m` constant is
   applied to this `q>=2m` collision-sparse family.

The repaired verdict remains **HOLD**. The construction is an exact algebraic
identity, an ideal optical algorithm and a conditional complexity separation.
It is not a useful syzygy algorithm until B3 is resolved, and its scalable
approximate claim also retains B2 and B4's explicit hypotheses.
