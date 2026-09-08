# Independent verdict: R12 syzygy advantage candidates

Reviewer: Sol, 2026-09-07.  This verdict audits the source-only problems under
D25.  It does not demand a coefficient-list advantage from a task whose common
input is physical copies.  Conversely, a coefficient sampler and a copy-source
sampler are different problems and are never placed in one resource comparison.
Claim status remains in `claims/CLAIMS.md`.

## Verdict

**PASS for the syzygy generator-selection theorem; HOLD for the BosonSampling
candidate.**  The rank-two Pluecker route has an unconditional same-output copy
advantage in its declared comparator model.  Its strengthened principal output
finds any minimal pair of original generators with success at least `2/3`: eight
copies suffice, whereas every fixed-cap adaptive separate-copy strategy needs
`Omega(sqrt q)`.  It uses an ordinary two-copy swap test, which is eligible
under D25 and is neither QFT, Grover nor DQI.

The additional volume law is a genuine invariant of the **based generating
tuple**: it is the complementary Pluecker-coordinate law of the constant-
syzygy space.  Neither output is an invariant of the bare ideal, which is fixed
throughout the family.  The BosonSampling algebra and optical law are correct,
but its advantage is complexity-assumption-dependent and its measured label
removes the syzygy cancellation; no useful downstream AG consumer is proved.

## 1. Independent derivation of the rank-two source theorem

Let `C` be a hidden `2 x q` row coisometry, `C C^dag=I_2`, and use the
Fock-orthonormal degree-two vectors

`e_0=z_0^2/sqrt(2)`, `e_1=z_1^2/sqrt(2)`.

Define the based quadratic tuple

`f_a=C_(0a)e_0+C_(1a)e_1`, `1<=a<=q`.                                (1)

Its minimal-degree Macaulay map is `F_2:C^q->R_2`, with the two nonzero
coefficient rows equal to `C`.  Hence

`F_2^dag F_2=C^dag C=:P_U`,                                           (2)

the rank-two projector onto the row space `U` of `C`.  At emitter degree
`N=d=2`, the annihilation emitter is

`V=sum_a |a><f_a|=F_2^dag`.                                          (3)

Since `||V||=1`, inputting the fixed maximally mixed degree-two state
`tau_2=I_(R_2)/3` gives the unnormalised bath state and emission probability

`V tau_2 V^dag=P_U/3`, `p_emit=2/3`.                                 (4)

Conditional on the fixed herald, the supplied source copy is therefore

`rho_C=P_U/2`.                                                        (5)

Equations (1)--(5) realize **every** rank-two flat source: for any two-plane
`U subset C^q`, choose the rows of `C` to be any orthonormal basis of `U`.
Changing that row basis left-multiplies `C` by `U(2)` and leaves both (5) and
the output probabilities below unchanged.  The source model supplies
independent copies of (5), not `C`, its entries, a purification, controlled
preparation, an inverse, or a controllable emitter.  If raw emitter attempts
are later charged, their common `2/3` heralding cost must be charged equally to
both sides; it is outside the fixed-copy problem as currently stated.

The tuple (1) spans the fixed ideal `(z_0^2,z_1^2)`.  Its constant syzygy
space is `K=ker C`, of dimension `q-2`.  A pair `{a,b}` is a minimal generating
subtuple exactly when the `2 x 2` minor `C[:,{a,b}]` is nonzero.  Cauchy--Binet
gives

`sum_(a<b)|det C[:,{a,b}]|^2=det(CC^dag)=1`.                          (6)

The complementary-minor/Hodge-dual identity identifies these magnitudes with
the Pluecker coordinates of `K`.  Thus the exact common classical output is

`Pr_C({a,b})=det(P_U[{a,b},{a,b}])=|det C[:,{a,b}]|^2`.               (7)

This is projection-DPP volume sampling of bases of the two-dimensional
generator quotient.  Presentation dependence is explicit and permitted; no
claim about the fixed bare scheme varying with `C` is valid.

## 2. Twenty-copy quantum algorithm

On two independent copies of `rho_C`, measure
`P_-=(I-SWAP)/2`.  Since `rho_C` has two eigenvalues `1/2`,

`Pr(P_-)=Tr[P_- rho_C tensor rho_C]
        =(1-Tr rho_C^2)/2=1/4`.                                      (8)

The antisymmetric subspace `wedge^2 U` is one-dimensional.  Conditional on
the antisymmetric result the two data registers are exactly the support Slater
ray, and coordinate measurement has law (7).  An ordinary ancilla swap test
implements `{P_+,P_-}`; it uses one controlled physical swap across the two
`ceil(log_2 q)`-qubit source registers.  No QFT, Grover, DQI, QSVT, tomography,
or coefficient access occurs.

Run ten independent two-copy trials, stop at the first antisymmetric outcome,
and output its sorted coordinate pair.  If all ten fail, output a fixed pair.
The source cap is 20 copies and

`p_fail=(3/4)^10=59049/1048576 < 1/16`.                              (9)

The always-output law is a mixture of the exact law (7) and a fallback law,
so its total-variation distance from (7) is at most (9).  The ideal gate count
is ten controlled swaps, `O(10 log q)` Fredkin gates under a qubit register
encoding, plus ancilla gates and coordinate readout.  Finite gate/source noise
needs a separate trace-distance budget; the exact theorem assumes ideal copies
and noiseless swaps.

A passive-linear-optical realization uses two single-photon `q`-mode copies,
pairwise balanced beam splitters on the copy rails, and number-resolved
coincidence detection.  The coincidence/antisymmetric port is the Hong--Ou--
Mandel swap measurement.  Ten trials require at most twenty source photons;
loss, distinguishability and detector error are not covered by (9).

## 3. Exact transfer of C-362

D-SUPPORT-BLOCK-PAIR consists entirely of rank-two flat sources of the form
(5), so (1)--(5) physically realize both hard ensembles, including their hidden
off-diagonal coherence.  The Haar frames are fixed for the full transcript and
are not redrawn per copy.  The classical comparator may make an arbitrary POVM
on each complete `q`-dimensional source copy and adapt later POVMs using
unlimited classical computation and memory, but keeps no quantum system across
copies.  This is stronger than coordinate measurement and is not a tomography
straw man.

C-362 proves for every fixed cap `T` that the averaged transcript laws obey

`TV(P_0,P_1)<=1-c_T<=T(T-1)/d`, `q=2d`,                              (10)

while event `E` (one selected coordinate in each known block) has target
probabilities `1` and `1/2`.  If an always-output sampler is within TV
`epsilon` of (7) for every promised source, data processing and the triangle
inequality force

`T(T-1)>=d(1/2-2epsilon)`.                                           (11)

At `epsilon=1/16`,

`T(T-1)>=3q/16`,                                                     (12)

an unconditional `Omega(sqrt q)` source-copy lower bound for every adaptive
separate-copy strategy.  Equations (9) and (12) are the same output, promise,
and physical-copy access.  They give a constant-versus-root-`q` separation;
the explicit cap 20 becomes strictly smaller than the lower-bound requirement
for even `q>=2028`.  This is a fixed-total-cap theorem, not an expected-stopping-
time lower bound and not a coefficient-list theorem.

The transfer would fail if the physical source generated only diagonal/block-
separable `P_U`; equation (4) prevents that failure because an arbitrary hidden
coisometry is allowed.  In particular it realizes the coherent `W_1` ensemble,
whose off-diagonal blocks are essential to C-362.

## 4. Issues to check against the forthcoming canonical artifact

1. The source must be defined as fixed copies of the **conditional** bath state
   (5), or raw heralding must be charged symmetrically.  No preparation inverse,
   purification, coefficient list or emitter control may be inferred.
2. `CC^dag=I_2` and the Fock factors `1/sqrt(2)` are essential to (2)--(5).
   Individual `f_a` need not have unit norm and some general coisometries may
   have zero columns; the pair law simply gives dependent pairs zero weight.
3. The output must be attached to the based tuple/minimal generator quotient,
   not called an invariant of `(z_0^2,z_1^2)` alone.
4. The lower bound must retain the fixed hidden frames, all-source uniform
   guarantee, fixed total cap, always-output TV convention, flat rank two and
   arbitrary within-copy POVMs.
5. The twenty-copy theorem assumes ideal support and exact swaps.  A robust
   statement needs source trace-distance and gate-error accumulation across all
   ten trials.

## 5. Audit of the canonical Pluecker artifact

The available `definitions/syzygy-plucker-r12.md` and
`scouting/syzygy-plucker-r12.md` satisfy items 1--4 above.  They fix the
conditional-copy source, explicitly deny coefficient/purification/emitter
access, state row coisometry and Fock normalisation, attach the output to the
based tuple, preserve every C-362 promise, and include both delivered-copy and
raw-emitter-call ledgers.

The raw-call bound is also correct.  For 50 independent emitter attempts with
success `2/3`, the mean is `100/3` and the shortfall to 20 is `40/3`, so
Hoeffding gives

`Pr[number delivered <20] <= exp[-2(40/3)^2/50]=exp(-64/9)`.           (13)

Hence
`(3/4)^10+exp(-64/9)<1/16`.  The first shorthand in (13) should not be copied;
the mean/shortfall derivation is the unambiguous statement.

The robust hybrid bound `20 epsilon_s+10 epsilon_t` is valid for independent
noisy product deliveries with per-copy trace distance `epsilon_s` and per-trial
instrument diamond distance `epsilon_t`.  If the twenty delivered systems can
be correlated, the premise must instead bound their joint trace distance from
`rho_C^tensor20`; marginal bounds alone do not imply the hybrid estimate.

### Pluecker objections

#### P1 — MINOR: state the independence premise in the noise extension

The ideal source definition supplies independent copies, but the optional
noise paragraph says only that “each source copy differs” by a trace distance.
That does not exclude adversarial correlations across deliveries.

**FIX DEMAND.**  Say that the noisy deliveries are a product of individually
`epsilon_s`-close states, or replace the term `20epsilon_s` by one bound on the
joint twenty-register trace distance.

**SURVIVING STATEMENT.**  The ideal twenty-copy theorem and the product-noise
hybrid bound are correct.

#### P2 — MINOR: qualify total-resource advantage when device construction dominates

The theorem proves source-copy and online-processing advantages.  An arbitrary
one-time `B_source(q)` is common, but if paid for a single sample it can dominate
both algorithms; the copy lower bound alone does not compare total wall-clock
time including source construction.

**FIX DEMAND.**  State the winning resource as delivered copies/online source
uses and `O(log q)` post-source processing.  Claim a total-time advantage only
after amortising or bounding `B_source` and `C_source` in the same model.

**SURVIVING STATEMENT.**  The constant-versus-`Omega(sqrt q)` copy separation
is unconditional and independent of common per-copy delivery cost.

#### P3 — MINOR: keep utility at the exact level proved

Volume sampling is useful for selecting independent columns, but this source
returns only labels and supplies no later coefficient or generator oracle.
The regression citation does not prove a downstream ideal computation in this
model.

**FIX DEMAND.**  Retain “volume-weighted minimal generator selection” as the
useful AG output and presentation invariant.  Describe regression/design only
as motivation, as the memo currently does; do not infer preconditioning,
membership or full-syzygy recovery.

**SURVIVING STATEMENT.**  Positive-probability outputs are minimal generating
pairs and their law is the squared complementary Pluecker-coordinate law of
the constant-syzygy space.

### PRD assessment for the Pluecker route

1. **Problem: met.**  The finite source, based quadratic tuple, syzygy space,
   output law, error and size parameter `q` are exact.  Presentation dependence
   is explicit and allowed.
2. **Classical baseline: met in the declared source model.**  C-362 lower-bounds
   every adaptive arbitrary-POVM separate-copy strategy, not only a named
   classical heuristic.  Coefficient-list and cross-copy quantum-memory access
   are correctly declared different models.
3. **Quantum advantage: met for delivered-copy/online complexity.**  At TV
   `1/16`, 20 copies and `O(log q)` processing beat the unconditional
   `T(T-1)>=3q/16` lower bound, strictly for even `q>=2028` and asymptotically
   by constant versus `Omega(sqrt q)` copies.  No total device-construction or
   practical runtime advantage is included.
4. **Dequantisation audit: met for the same scope.**  The lower bound permits
   arbitrary measurements on each full original copy, adaptation and unlimited
   classical processing.  It is not a tomography comparison.  It deliberately
   does not cover quantum memory joining copies.
5. **Heuristic hardware: met as a diagnostic.**  Pairwise Hong--Ou--Mandel
   interference implements the antisymmetry measurement with two photons per
   trial; mode-resolved coincidence gives the pair.  The `q=4` experiment tests
   the law, while loss/distinguishability/detector bias remain measured costs.
6. **D25 mechanism: met.**  The protocol is an ordinary swap/antisymmetry test,
   eligible under D25 and not QFT, Grover or DQI in disguise.

After P1's wording repair, this is a **formal north-star hit in the stated
quantum-data model**: a useful based-syzygy volume-sampling problem with an
unconditional copy/online-resource advantage and a concrete optical attack.
Its narrow scope must accompany the claim: it is not an explicit-coefficient
speedup, an intrinsic invariant of a varying bare scheme, a whole-syzygy
algorithm, or a demonstrated practical total-time advantage.

The current memo repairs P1 by requiring independent product noise or a joint
eight-register trace-distance bound.  It already states P2's device-cost scope
and P3's limited utility.  The Pluecker artifact therefore has no remaining
FATAL or MAJOR mathematical objection.

## 6. Independent audit of the BosonSampling construction

### 6.1 Algebra, normalisation, and optical law

For disjoint `m`-sets `S_1,S_2`, the squarefree monomials
`f_j=product_(i in S_j)z_i` are coprime.  The displayed Koszul resolution is
minimal, and its degree-`2m` syzygy is generated by `(f_2,-f_1)`.  A unitary
linear substitution preserves the regular sequence and sends this generator
to `(F_2,-F_1)`.  Since a squarefree monomial has Fock norm one and the
symmetric-power action is unitary, the normalized module state is

`(|1>Gamma_m(U)|S_2>-|2>Gamma_m(U)|S_1>)/sqrt(2)`.                    (14)

For an occupation vector `nu`, expanding the product of linear forms counts
each repeated-row assignment `nu!` times in the permanent, so

`[z^nu]phi_U(f_S)=Per(U[nu,S])/nu!`,
`<nu|Gamma_m(U)|S>=Per(U[nu,S])/sqrt(nu!)`.                           (15)

Thus the joint law

`P_U(j,nu)=|Per(U[nu,S_(3-j)])|^2/(2nu!)`                            (16)

is correct and includes collisions.  Because the module label is measured,
classical fair-coin selection followed by `m` single photons in the opposite
port set samples (16) exactly.  There is no branch postselection, cat-state
preparation, or hidden coefficient-state normalisation.

The `m=2,q=4` diagnostic also checks: two independent balanced beam splitters
send each relevant coincidence input to two bunched outputs with conditional
probability `1/2`; including the fair label gives the four listed joint events
probability `1/4` each.

### 6.2 Exact and approximate hardness transfers

An exact sampler for (16), repeated until `j=2`, gives ordinary
BosonSampling on `S_1` in two expected calls.  The converse uses a fair coin.
This is an unconditional reduction.  The conclusion that an efficient exact
classical sampler collapses the polynomial hierarchy is the published
Aaronson--Arkhipov implication, contingent as usual on noncollapse when read as
an absence-of-algorithm statement.

The approximate conditioning constant is correct.  If `TV(P,Q)<=epsilon`,
write `q_j=Q(j,*)`, `d_j=sum_nu|P(j,nu)-Q(j,nu)|`.  Adding and subtracting
`2Q(j,nu)` gives

`TV(P(.|j),Q(.|j))<=d_j+|q_j-1/2|<=3epsilon`,                        (17)

and `q_j>=1/2-epsilon`.  The approximate PH consequence still assumes the
average-case Gaussian-permanent and anti-concentration conjectures.  A rounded
finite mesh also needs an explicit induced input distribution; the norm bound
`TV<=mB delta_gate` alone does not prove that this discrete ensemble inherits
the Haar hardness theorem.  The proposer states this limitation honestly.

The general exact classical upper `O(m2^m+poly(q,m,B))` per sample is the
appropriate clean comparator after charging construction of matrix entries
from the same gate list.  The cited `approximately m1.69^m` example at `q=m`
does not itself lie in this candidate's `q>=2m` family, although the later
algorithm remains relevant motivation for proportional-mode regimes.

### 6.3 BosonSampling objections

#### B1 — MAJOR: exact hard gate-family containment remains an obligation

An unspecified “exact algebraic gate set” may generate only an easily
simulated subgroup.  The exact reduction needs the interferometers used in the
Aaronson--Arkhipov construction with polynomial description and compilation
length.

**FIX DEMAND.**  Give an explicit algebraic two-mode gate encoding and prove
that the standard hard unitary dilation compiles into it with polynomial bit
length, or formulate the exact theorem directly for a standard finite matrix
input model and propagate its precision convention.

**SURVIVING STATEMENT.**  Conditional on that containment, exact syzygy
sampling and ordinary exact BosonSampling are equivalent up to the fair label
and two expected calls.

#### B2 — MAJOR: the finite approximate input ensemble is not yet a theorem

Rounding a Haar unitary through a mesh changes the input distribution.  Small
operator error controls output TV for each paired unitary, but does not by
itself establish average-case hardness for the rounded mesh distribution.

**FIX DEMAND.**  Specify the sampling/rounding map from Haar unitaries to
finite gate strings, its bit complexity and probability law, then state the
permanent and anti-concentration conjectures for precisely that ensemble or
prove a reduction back to the standard one.

**SURVIVING STATEMENT.**  Equations (14)--(17) and the `mB delta_gate` output
robustness are valid; approximate classical hardness remains conditional on
the named conjectures and this finite-ensemble transfer.

#### B3 — FATAL to a north-star claim: the syzygy is not used computationally

Measuring the direct-sum label destroys every cross term and discards the
relative minus sign.  The sampler is exactly a coin followed by coefficient
sampling from one completely factored generator.  BosonSampling hardness is
already present in either Chow-form component, and no downstream resolution,
membership, deformation, conditioning, or other AG computation is accelerated.

**FIX DEMAND.**  Either prove a concrete algebraic consumer whose same-output
best classical method benefits from samples (16), or define a coherent output
whose computational content depends on cancellation between the two syzygy
components and audit its preparation/readout.

**SURVIVING STATEMENT.**  The distribution is legitimately the Fock
coefficient-energy law of a distinguished minimal syzygy and gives a
reviewable conditional BosonSampling advantage.  It is not yet a useful
syzygy algorithm under the campaign's problem criterion.

#### B4 — MAJOR for end-to-end asymptotics: fixed loss removes polynomial runtime

With independent uniform total transmission `eta_tot`, conditioning on all
`m` detections costs `eta_tot^(-m)`.  Any fixed `eta_tot<1` is exponential.
The ideal optical circuit remains polynomial, but a scalable physical theorem
needs `eta_tot^m>=1/poly(m)` or a specified fault-tolerant/multiplexed source and
detector model.

**FIX DEMAND.**  Attach every runtime/advantage statement either to the ideal
lossless model or to the explicit near-unit-transmission promise
`-m log eta_tot=O(log m)`.  Compare the resulting exponent with the classical
upper rather than calling loss a free restart.

**SURVIVING STATEMENT.**  Uniform loss preserves (16) after all-photon
conditioning and multiplies raw attempts by exactly `eta_tot^(-m)`; mode-
dependent loss defines a different distribution unless separately corrected.

#### B5 — MINOR: keep the classical circuit-read cost and regime attached

The classical sampler needs matrix entries derived from the `B`-gate input,
and the faster cited `q=m` example is outside `q>=2m`.

**FIX DEMAND.**  Write the general upper as including `poly(B,q,m)` and use the
`m2^m` term as the collision-sparse comparison.  Cite proportional-mode
improvements without claiming the displayed `q=m` constant for this family.

**SURVIVING STATEMENT.**  The best clean general exact upper remains
exponential in `m` and polynomial in the mode/circuit description.

### 6.4 PRD assessment for BosonSampling

- The exact AG problem, passive-optical sampler and classical upper are precise.
- The quantum-vs-classical advantage is conditional: exact efficient classical
  sampling has the PH-collapse consequence; approximate hardness additionally
  assumes average-case permanent hardness, anti-concentration and a repaired
  finite input distribution.
- State preparation, collisions, branch conditioning, bit precision and loss
  are honestly accounted for.
- Passive BosonSampling is eligible under D25 and directly supplies the hardware
  route.
- Usefulness is not established because the relation cancellation is unused and
  no downstream AG consumer is proved.

The candidate therefore remains **HOLD as a conditional demonstration**, below
the unconditional Pluecker copy separation.

## 7. Bounded checks and primary-source resolution

An independent `timeout 30` in-memory calculation checked random complex row
coisometries at `q=4,8,16`, Cauchy--Binet, projection-DPP minors, swap success,
both C-362 cross-block probabilities, the exact 50-call binomial tail, and the
`m=2,q=4` BosonSampling permanent law.  All checks passed.  The exact binomial
tail is `3.11745e-5`, below the Hoeffding bound used in (13).

The supplied Pluecker checker was rerun after the ANY-pair extension under
`timeout 60` and reported `PASS: 1032 finite checks`.  It covers complex C3 orientation, complementary
minors, the exact antisymmetric ray, an independently assembled HOM amplitude,
hard-family events and finite caps.  It does not prove the asymptotic C-362
transcript bound or the PRD assessment.  Its six mutations
(`emitter-conjugation`, `antisymmetry-scale`, `rank-promise`,
`sorted-pair-factor`, `hom-sign`, `public-partition`) were each run under bounded subprocesses and
each exited one, so all current red paths are active.

Targeted primary sources:

- Garcia-Escartin--Chamorro-Posada,
  [arXiv:1303.6814](https://arxiv.org/abs/1303.6814), proves the equivalence of
  Hong--Ou--Mandel interference and the destructive swap test, supporting the
  stated two-photon hardware map.
- Aaronson--Arkhipov,
  [arXiv:1011.3245](https://arxiv.org/abs/1011.3245), supplies the exact PH
  consequence and the conjectural approximate-hardness framework used in B1--B2.
- Clifford--Clifford,
  [arXiv:1706.01260](https://arxiv.org/abs/1706.01260), gives the general
  `O(m2^m+poly(q,m))` exact sampler; their
  [arXiv:2005.04214](https://arxiv.org/abs/2005.04214) follow-up gives faster
  average algorithms in particular proportional-mode regimes.
- Arkhipov, [arXiv:1412.2516](https://arxiv.org/abs/1412.2516), supports linear
  output robustness under interferometer error.  Aaronson--Brod,
  [arXiv:1510.05245](https://arxiv.org/abs/1510.05245), treats specified lossy
  BosonSampling regimes without removing the raw attempt cost.
- Derezinski--Warmuth,
  [arXiv:1705.06908](https://arxiv.org/abs/1705.06908), supports volume sampling
  as a useful column/experimental-design primitive.  It does not prove a
  downstream ideal-computation speedup for this source model.

## 8. Joint tournament verdict

1. **Syzygy Pluecker pair sampling: PASS.**  It gives an unconditional
   constant-versus-`Omega(sqrt q)` delivered-copy/online separation for the
   exact same volume law, with a 20-copy cap, a fully adaptive separate-copy
   lower bound, and an elementary two-photon hardware route.  Under D25 it is a
   formal north-star hit in its narrow quantum-data/presentation model.
2. **Minimal-syzygy BosonSampling: HOLD.**  Its identities and conditional
   BosonSampling reductions survive, but exact gate-family containment and the
   finite approximate ensemble remain obligations, fixed loss can destroy the
   runtime, and the output does not use syzygy cancellation or have a proved AG
   consumer.

The Pluecker winner should be registered with its full scope in every claim:
unknown fixed conditional bath copies; row-coisometric based tuples; rank two;
TV `1/16`; 20-copy cap; arbitrary adaptive within-copy classical measurements
but no cross-copy quantum memory; strict finite separation at even `q>=2028`;
and copy/online-resource advantage rather than coefficient-list or total-device
runtime advantage.  Work should continue toward explicit-input and higher-rank
syzygy/supersymmetric problems; this formal win does not exhaust the research
goal.

## 9. Stronger useful output: find any minimal generating pair

The volume-law theorem implies a stronger decision/search result whose output
does not prescribe a DPP distribution.

**Problem.**  Under D-SYZYGY-PAIR-TUPLE and D-SYZYGY-PAIR-SOURCE, always output
a distinct pair `J={a,b}`.  Success means `det C[:,J]!=0`, equivalently that
`(f_a,f_b)` is a minimal generating pair of `(z_0^2,z_1^2)`.  Require success
at least `2/3` for every hidden row coisometry `C`.  The comparator receives no
partition, coefficient, purification or emitter metadata and has a fixed total
copy cap.

### 9.1 Eight-copy quantum upper bound

Run four independent two-copy antisymmetry tests.  Every accepted coordinate
pair has probability proportional to `|det C[:,J]|^2`, so it is generating
with certainty.  On four failures output any fixed distinct pair.  Therefore

`Pr[generating output]>=1-(3/4)^4=175/256>2/3`,                       (18)

using at most eight delivered copies and four controlled swaps.  This theorem
does not require approximating the DPP law; the fallback may be adversarially
bad.  The same HOM apparatus implements it with at most eight photons.

### 9.2 Adaptive separate-copy lower bound

Let `q=2d`, `d>=3`, and choose a uniformly hidden balanced set
`S subset [2d]`, `|S|=d`.  Conditional on `S`, draw independent Haar unit
vectors `u_S` and `v_(S^c)` on the two coordinate supports and take

`U_S=span(u_S,v_(S^c))`, `C_S=(u_S^dag;v_(S^c)^dag)`.                (19)

This is a row coisometry and is physically realized by the same emitter.  With
probability one over the Haar vectors, a pair generates exactly when it crosses
the hidden cut `S|S^c`.

For each fixed `S`, the Haar/Gaussian argument of C-362 gives the full adaptive
transcript minorization

`P_S >= c_T P_*`, `c_T=(d/(d+T-1))^T`.                               (20)

The reference `P_*` is the same for every `S`: it is the transcript law of the
protocol on fresh copies of `I_(2d)/(2d)`, since all the fixed-`S` Gaussian
first moments have that covariance.  This common-reference independence is the
key point; it would fail as a lower-bound argument if `S` were supplied as
classical metadata to the protocol.

Absorb the algorithm's output randomness into its transcript.  On the common
component, the output pair is independent of uniform `S`.  Every fixed distinct
pair crosses a uniform balanced set with probability

`a_0=d/(2d-1)`.                                                       (21)

The residual component succeeds at most one, so average success is at most

`c_T a_0+(1-c_T)=a_0+(1-c_T)(1-a_0)`.                                (22)

Uniform pointwise success at least `2/3` implies the same average success.
Solving (22) and using `1-c_T<=T(T-1)/d` gives

`1-c_T >= (d-2)/[3(d-1)]`,
`T(T-1) >= d(d-2)/[3(d-1)]`.                                        (23)

Thus `T=Omega(sqrt d)=Omega(sqrt q)`.  The right side of the second inequality
is `Omega(q)`; the copy lower bound itself is square-root, not linear.  Since
`8*7=56`, the quantum cap is strictly smaller for every `d>=170`, equivalently
every even `q>=340`.

### 9.3 Scope and verdict of the stronger theorem

This strengthens the usefulness case: the output actually selects a minimal
generating subtuple, rather than merely matching a prescribed volume law.  It
also needs fewer quantum copies and separates at a smaller explicit dimension.
The lower bound remains unconditional and permits every adaptive global POVM on
one complete source copy plus unlimited classical processing.

The exact scope is essential.  The hidden balanced partition is part of the
proof distribution and is not revealed to the algorithm.  If coefficients or
the source-device construction expose which labels lie in `S`, a classical
algorithm outputs a crossing pair without copies.  The theorem is for a fixed
copy cap and does not lower-bound expected-time unbounded stopping.  It proves
copy/online advantage for unknown source presentations, not coefficient-list or
single-shot total-device runtime advantage.

**Verdict for ANY-PAIR.**  The derivation passes and supersedes the DPP sampler
as the strongest R12 result.  After canonical definitions state the hidden-
metadata and fixed-cap conditions, it meets all six current PRD gates as a
formal quantum-data north-star hit: useful AG search output, unconditional
adaptive separate-copy lower bound, eight-copy algorithm, dequantisation scope,
two-photon/HOM hardware, and an eligible non-QFT/non-Grover/non-DQI mechanism.

## MERGE APPROVAL

The root may canonically register the following statements.  This approval is
for their exact scopes and does not broaden them to coefficient input, arbitrary
ideals, correlated marginal noise, unbounded expected stopping, or total device
construction time.

**C-R12-SYZYGY-SOURCE-REALIZATION — approve PROVED after canonical ID
assignment.**  For every hidden `2 x q` row coisometry `C`, the tuple (1)
generates `(z_0^2,z_1^2)`, has constant syzygy space `ker C`, and the fixed
degree-two Fock emitter on `I_3/3` succeeds with probability `2/3` and outputs
`rho_C=C^dag C/2`.  Every rank-two flat source is realized.

**C-R12-SYZYGY-VOLUME-SAMPLING — approve PROVED after canonical ID assignment.**
Ten two-copy swap trials use at most 20 delivered copies and always output a
pair within TV `(3/4)^10<1/16` of
`|det C[:,J]|^2`.  Every adaptive separate-copy sampler with fixed cap `T` and
uniform TV error `1/16` obeys `T(T-1)>=3q/16`; thus the cap separation is
strict for even `q>=2028`.  The theorem is conditional only on ideal source and
gate promises, not a complexity conjecture.

**C-R12-SYZYGY-GENERATOR-SELECTION — approve PROVED after canonical ID
assignment.**  Four two-copy swap trials use at most eight delivered copies and
output an original generating pair with probability at least `175/256>2/3`
for every row coisometry.  Every adaptive separate-copy strategy with fixed cap
`T` and success at least `2/3` for every source obeys, for `q=2d`, `d>=3`,

`T(T-1)>=d(d-2)/[3(d-1)]`.

The proof distribution's balanced partition is hidden, its Haar frames and
partition are fixed for the run, and the common minorizing transcript law is
independent of that partition.  Consequently `T=Omega(sqrt q)`, with strict
eight-copy separation for even `q>=340`.

**R12 north-star disposition.**  The generator-selection statement meets the
six current PRD criteria only in the named quantum-data model.  Call the winning
resource a delivered-copy/online-processing advantage and the output a minimal
subtuple of the original based presentation.  Retain the fixed bare ideal,
source-device cost and unavailable coefficient list prominently.

**BosonSampling merge disposition.**  The algebraic resolution, Fock permanent
law, ideal optical sampler and exact/approximate conditioning reductions may
enter as SKETCH after B1--B2 are retained as assumptions.  Keep utility on HOLD.
No north-star success statement should depend on this conditional candidate.

## 10. Addendum: classical upper and controllable-emitter boundary

The later Sections 5B and 6A of the R12 proposer survive independent audit.

### 10.1 Separate-copy `O(q log q)` upper

After padding to `D<2q`, random Clifford-basis measurement with outcome `phi`
and shadow matrix `X=(D+1)|phi><phi|-I` obeys

`E X=rho`, `E X^2=(D-1)rho+DI`.                                     (24)

For flat rank two, this gives variance norm at most `3D/2` and sample norm at
most `D+1`.  The stated matrix-Bernstein bound follows.  At operator error
`a=1/32`, the top-two estimated support has largest sine principal angle at
most

`a/(1/2-a)=1/15`.                                                    (25)

The exterior-ray trace distance is at most `sqrt(2)/15`, so exact classical
projection-DPP sampling from the estimated frame returns a true generating
pair with probability at least

`(11/12)(1-sqrt(2)/15)>2/3`.                                        (26)

Thus `O(q log q)` copies and polynomial-in-`q` processing are a valid
separate-copy upper.  It is not asserted optimal; the unconditional lower
remains `Omega(sqrt q)`.

### 10.2 Two-query controllable-emitter upper

If a classical controller may choose pure incident states in
`span(g_0,g_1)` and query `C^dag`, the fixed-source theorem no longer applies.
Choose uniformly among the three Pauli bases, randomize the order `(x,x_perp)`,
make two emitter queries, and measure their labels.  The six qubit stabilizer
states form the required projective two-design, and

`E_x |c_i^dag x|^2 |c_j^dag x_perp|^2
   =[2w_iw_j-|c_i^dag c_j|^2]/6`.                                   (27)

For a projective parallel class of columns with total squared weight `m`, the
dependent ordered-pair mass is `m^2/6`.  Positivity and `CC^dag=I_2` imply
`m<=1`, while the class weights sum to two.  Hence total dependent mass is at
most `1/3`, and the two-query controller finds a generating pair with success
at least `2/3` for every `C`.

This is a decisive access boundary, not a refutation.  The eight-copy theorem
continues to hold for inaccessible fixed iid bath copies.  If incident-state
control is physically available at comparable cost, (27) is the correct
classical-control comparator and removes the copy advantage.

An independent bounded calculation verified (27) for random complex
coisometries at `q=3,8,20` and checked (25)--(26).  No finite test establishes
optimality of the `O(q log q)` upper.

**Addendum disposition: approve both scoped statements for PROVED registration.**
Every north-star statement must retain the absence of incident-state control as
an essential input promise and describe the known classical range as
`Omega(sqrt q)` to `O(q log q)`, without claiming optimality.
