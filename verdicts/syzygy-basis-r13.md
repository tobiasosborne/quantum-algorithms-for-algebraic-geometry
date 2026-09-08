# Independent verdict: growing-rank syzygy basis selection R13

Reviewer: Sol, 2026-09-08.  This file audits the source-only growing-rank task
under D25.  It does not infer coefficient access, a purification, emitter
control, or a practical device-construction advantage.  Status belongs in the
canonical claim register only after this review converges.

## Initial independent derivation

Let `s=r-1` and give `R_s=C[z_0,z_1]_s` its Fock-orthonormal monomial basis
`g_0,...,g_(r-1)`.  For a hidden row coisometry `C in C^(r x q)`, define

`f_a=sum_(i=0)^(r-1) C_(ia)g_i`.                                    (1)

The minimal-degree Macaulay map is exactly `F_s=C`.  Its columns span all
`R_s`, so the based tuple generates `(z_0,z_1)^s`; its constant syzygy space is
`ker C`, and an `r`-subset `J` is a minimal generating subtuple exactly when
`det C[:,J]!=0`.  The affine quotient has the monomial basis of total degree
below `s`, hence length

`sum_(k=0)^(s-1)(k+1)=s(s+1)/2=r(r-1)/2`.                            (2)

It is a nonreduced fat point for `r>=3`.

At emitter degree `N=s`, annihilation identifies the emitter with
`V=F_s^dag=C^dag`.  Since `CC^dag=I_r`, `V` is an isometry: the fixed input
`I_(R_s)/r` succeeds with probability one and produces

`rho_C=C^dag C/r`.                                                    (3)

Thus every flat rank-`r` support source occurs, without branch conditioning.

## 1. Independent hidden-partition lower bound

Let `q=rd`.  Choose a hidden uniform ordered balanced partition
`S=(S_1,...,S_r)` of the coordinate labels, each group of size `d`, then choose
independent Haar unit vectors `u_i` supported on `S_i`.  Take the rows of `C`
to be `u_i^dag`.  Almost surely an `r`-subset generates if and only if it is a
transversal of the hidden partition.

Fix any adaptive strategy using at most `T` original copies, with an arbitrary
POVM on each whole copy and unlimited classical memory.  Refine a complete
leaf to product rank-one effects.  Conditional on latent source components,
its probability is a product of squared homogeneous linear forms in the `r`
independent Haar vectors.  If group `i` occurs `L_i` times, Haar/Gaussian norm
comparison gives the factor

`(d/(d+L_i-1))^L_i >= (d/(d+T-1))^L_i`.

Multiplying and summing the latent labels yields, for every fixed partition,

`P_S >= c_T P_*`, `c_T=(d/(d+T-1))^T`,                              (4)

where `P_*` is the transcript law on fresh `I_q/q` states.  This reference is
independent of `S`; revealing `S` as metadata would invalidate the argument.

Any fixed `r`-subset is a transversal of a uniform balanced partition with
probability

`a_(r,d)=r! d^r/(rd)_r`,                                             (5)

where `(rd)_r=rd(rd-1)...(rd-r+1)`.  Absorb the output randomness into the
transcript.  The common component succeeds with probability (5), and the
residual component succeeds at most one.  A uniform success guarantee `2/3`
therefore requires, whenever `a_(r,d)<2/3`,

`1-c_T >= (2/3-a_(r,d))/(1-a_(r,d))`.                               (6)

Using `1-c_T<=T(T-1)/d` gives the exact lower bound

`T(T-1) >= d [2/3-a_(r,d)]/[1-a_(r,d)]`.                            (7)

For `r>=3,d>=2`, `a_(r,d)<=a_(3,2)=2/5`, so the bracketed ratio is at least
`4/9`.  Consequently

`T=Omega(sqrt d)=Omega(sqrt(q/r))`.                                 (8)

The right side of (7) is `Omega(q/r)`; the copy lower bound is its square
root.  This is a fixed-cap theorem, not an expected-stopping lower bound.

## 2. What the QSVT content bank must prove

For `X_k=sum_(i<k)S_(ik)`, the Young content spectrum consists of integers in
`[-(k-1),k-1]`, with gap one.  Let `h=k-1`.  For a candidate content `c`, a
block encoding of

`A_(k,c)=(X_k-cI)/(h+|c|)`                                           (9)

has zero singular space equal to the content eigenspace and every other
singular value at least `1/(h+|c|)`.  An even QSVT polynomial can therefore
approximate its kernel projector in degree
`O((h+|c|)log(1/epsilon_step))=O(k log(1/epsilon_step))`.  The shift and
normalisation in (9) avoid the parity error that arises from asking one QSVT
sequence to implement an arbitrary off-centre window directly.

For the **ideal** bank, pad the `J=2k-1` content labels to
`H=2^ceil(log_2 J)`, assign the dummy labels projector zero, choose a uniform
label, and perform `{P_c,I-P_c}`.  The success probability is exactly `1/H`
for every input because `sum_cP_c=I`.  On failure and forgotten label, the
normalised channel preserves every spectral diagonal block and multiplies
off-diagonal blocks by `(H-2)/(H-1)`.  Repeating until success therefore returns
the exact content label distribution and exact conditional Lüders state;
`A_bank` attempts fail with probability `(1-1/H)^A_bank`.

For an **approximate** QSVT bank, state-independent success and exact Lüders
failure do not hold automatically.  The construction must supply one coherent
success/failure/label instrument whose diamond distance from the ideal attempt
is at most `epsilon_step`.  An adaptive hybrid over every bank retry and every
content invocation then bounds the complete transcript, not merely outcome
probabilities.  Failed labels must be measured/discarded or reset with their
dephasing charged.  A final exact antisymmetry certificate can restore exact
support-Slater output because every data operation in (9) is a controlled
permutation and hence preserves `U^tensor N` exactly; it does not repair an
unbounded failure probability.

## 3. Direct antisymmetry fallback

On `r` copies of (3), direct antisymmetrisation succeeds with

`Tr[P_-^(r)rho_C^tensor r]=dim(wedge^rU)/r^r=1/r^r`.                 (10)

The tempting `r!/r^r` is only the probability that latent mixture labels are
all distinct; conditional antisymmetrisation of a fixed ordering succeeds with
probability `1/r!`, giving (10).  The exact padded signed-permutation
certificate has Kraus map `gamma_rP_-`, `1/2<gamma_r<=1`, and success
`gamma_r^2/r^r`.  Repetition to constant success costs
`O(r^(r+1))` copies.  This is a valid non-QFT fallback and can remain polylog in
`q` for very slowly growing `r`, but it is not a polynomial-in-`r` solution.

## 4. Audit of the submitted QSVT construction

The submitted source geometry, lower bound, exact padded-bank channel, caps,
support certificate and separation ledger agree with Sections 1--3.  In
particular:

- `N=2r^2` flat copies give an `r`-row shape with probability at least `1/2`;
- capped ideal steering reaches the column-first tableau with conditional
  probability at least `7/8`;
- the exact padded antisymmetry certificate can be retried on the same correct
  column, reducing its conditional failure below `1/16` without new copies;
- bank exhaustion and approximate-instrument error each subtract at most
  `1/256`, leaving batch acceptance at least `103/256>3/8`;
- `B_batch=ceil(log(1/delta)/log(8/5))` gives copy cap
  `Q_quant=B_batch N`; at `delta=1/3`, this is `6r^2`;
- comparison with (7) is strict when
  `d>(9/4)Q_quant(Q_quant-1)`, hence on a family with `q/r^5` tending to
  infinity, with leading sufficient threshold about `81r^5` at
  `delta=1/3`.

The exact bank formula is especially important.  For `J_k=2k-1` real windows
padded to `H_k`, one random ideal test succeeds with probability `1/H_k`
independent of the input.  Summing every possible sequence of failed labels
before a first success gives

`M_c^(L)(rho)=[1-(1-1/H_k)^L]Pi_c rho Pi_c`.                         (11)

Thus the capped successful bank is a scalar multiple of the full Lüders
instrument, even though intermediate failures dephase cross-window blocks.
No label erasure is treated as unitary: every failure label/ancilla is measured,
discarded or reset and counted.

### 4.1 Same-column certificate retry

The strengthened certificate analysis is exact.  On a correctly steered
column the first `r` registers are a vector `psi in wedge^r U`.  Every valid
branch of the padded certificate acts as

`sign(pi)T(pi)psi=psi`,                                              (12)

and every invalid padded branch applies identity.  Before the final ancilla
readout, the data therefore factor as the unchanged `psi` from the entire
label/validity/readout state.  Every failed ancilla outcome leaves `psi`
exactly, so a fresh or reset ancilla repeats the same trial with acceptance
`gamma_r^2>1/4`.  This reset statement is not asserted on a wrongly steered
support state; such a branch remains safe because any later accepted Kraus map
is still `gamma_rP_-` and hence produces the exact exterior ray.

With

`A_cert=ceil(log(16)/log(4/3))=10`,                                 (13)

the correct-column certificate failure is at most `(3/4)^10<1/16`.
Using move failure `1/8`, the ideal good-path success is

`(1/2)(7/8)(15/16)=105/256`.                                       (14)

Subtracting bank exhaustion and complete-instrument hybrid errors of `1/256`
each yields `103/256>3/8`.  Thus per-batch failure is below `5/8`, and
`ceil(log(1/delta)/log(8/5))` batches fail with probability at most `delta`.
For `delta=1/3` the ceiling is three and the copy cap is `3(2r^2)=6r^2`.
Certificate retries consume `A_cert C_cert` gates and coherence time inside a
batch, but no fresh source state; the revised total gate ledger includes this
factor.

### Objections

#### Q1 — RESOLVED MAJOR: the signed QSVT step needs a Hermitian projected-unitary encoding

The proposer describes an exact LCU block encoding of `X_k/alpha_k` and then
uses odd sign polynomials on shifted Hermitian blocks.  A generic block encoding
only supports singular-value transformation; it does not preserve the signs of
Hermitian eigenvalues required by the two-threshold reflection.  The current
text specifies the action of SELECT only on a zero signal state and does not
prove that the full block-encoding unitary, including the affine shift, is
Hermitian/qubitized.

**FIX DEMAND.**  Define SELECT on its entire ancilla space so that valid labels
apply `S_(i,k) tensor I_signal` and padded labels apply
`I_data tensor X_signal`; then `PREPARE^dag SELECT PREPARE` is a Hermitian
projected-unitary encoding.  Build the scalar-shift block from a Hermitian
two-by-two reflection and combine it through a Hermitian LCU, or cite an
equivalent eigenvalue-transformation theorem with all signal projectors.
Propagate the clean-ancilla isometry error through the two sign filters and the
controlled reflection.

**SURVIVING STATEMENT.**  Once that signed-eigenvalue interface is supplied,
the integer half-window gap, odd-polynomial parity, degree
`O(alpha_k log(1/xi))`, leakage budget, and diamond-instrument hybrid are valid.
The direct fallback is independent of Q1.

**REPAIR DISPOSITION.**  The revised Sections 4--5 define the full padded
SELECT as a Hermitian involution, conjugate it by Hadamard PREPARE, and identify
the joint-zero projected block.  The affine shift uses a second Hermitian
involutory SELECT between `U_(X,k)` and `-sgn(t)I`, with the required weighted
selector preparation.  It is therefore a Hermitian projected-unitary encoding
of `(A_k-tI)/(1+|t|)`, so Hermitian eigenvalue transformation, rather than
unsigned singular-value transformation, applies.  Scalar sign error
`zeta<=xi^2/64` bounds clean error and signal leakage; separate retained work
registers make the two-sign reflection `xi`-close, and the controlled binary
instrument is within `2xi` in diamond norm.  This fully satisfies Q1.

#### Q2 — RESOLVED MINOR: keep ideal bank exactness separate from approximate retries

State-independent `1/H_k` success and equation (11) hold for the ideal
projectors.  Approximate QSVT tests can have input-dependent false-positive and
failure probabilities; their correctness comes from the full-instrument
diamond hybrid, not from reusing the exact geometric law.

**FIX DEMAND.**  Continue to state every exhaustion calculation for the ideal
bank, then subtract the complete adaptive hybrid error as in equation (46).
Do not describe an individual approximate failure as an exact tableau reset.

**SURVIVING STATEMENT.**  The submitted global accounting already follows this
separation and yields the valid `1/16` batch lower bound after Q1.

#### Q3 — RESOLVED MINOR: noisy success needs positive margin

Choosing algorithmic failure exactly `delta=1/3` leaves no room for source or
gate noise in a `2/3` success theorem.  Marginal closeness of correlated copies
also does not tensorize.

**FIX DEMAND.**  Use, for example, `delta_alg=1/4` and require product-source
plus gate error at most `1/12`, or supply a joint batch trace-distance bound.
State total device construction separately from delivered-copy/online cost.

**SURVIVING STATEMENT.**  The ideal theorem at `delta=1/3` and the submitted
product/joint-noise hybrid at positive margin are correct.

The strengthening uses `delta_alg=1/4`; it still needs only three batches, and
the resulting `3/4` ideal success leaves the stated `1/12` noise margin.

#### Q4 — RESOLVED MINOR: state the winning rank regime, not merely polynomial gates

The quantum source cap grows as `r^2`; the classical lower shrinks with `r` as
`sqrt(q/r)`.  Polynomial dependence on `r` alone does not prove a separation
for every growing rank.

**FIX DEMAND.**  Attach the QSVT claim to equation (57), for example
`q/r^5 -> infinity` at fixed error.  Attach the direct fallback to its stronger
condition involving `r^(r+1)` or the sufficient regime
`r log r=O(log log q)`.

**SURVIVING STATEMENT.**  Both displayed regimes give unconditional growing-
rank copy separations in the source-only model.

## 5. Bounded verification and sources

An independent `timeout 30` calculation checked random complex coisometries at
`(r,q)=(3,8),(4,10),(5,12)`, source normalization, Cauchy--Binet, the exact
transversal constant for `3<=r<=11`, `2<=d<=11`, every integer threshold
reflection through `k=29`, padded-bank diagonal weights, and explicit finite
copy-separation thresholds.  All checks passed.  These finite tests do not
prove the adaptive Haar/Gaussian comparison or QSVT compilation.

The relevant primary sources remain:

- Vershik--Okounkov,
  [arXiv:math/0503040](https://arxiv.org/abs/math/0503040), for the integer
  Jucys--Murphy content spectrum, branching basis and tableau moves;
- Gilyen--Su--Low--Wiebe,
  [arXiv:1806.01838](https://arxiv.org/abs/1806.01838), for bounded sign
  polynomials and QSVT, used through the repaired Hermitian eigenvalue interface;
- Garcia-Escartin--Chamorro-Posada,
  [arXiv:1303.6814](https://arxiv.org/abs/1303.6814), for the destructive
  swap/Hong--Ou--Mandel equivalence underlying the small source diagnostics.

The old Bacon--Chuang--Harrow generalized phase-estimation/Schur route is a
resource comparator, not part of this circuit; its group Fourier transform is
excluded from the R13 implementation by D25.

## 6. Verdict and promotion status

**PASS.**  The repaired QSVT upper, source, lower bound, bank identity,
certificate and direct fallback all survive independent derivation.  No
FATAL, MAJOR or MINOR objection remains.

The following may be registered **PROVED** after canonical definitions are
integrated:

1. **Source and geometry:** equations (1)--(3), ideal
   `(z_0,z_1)^(r-1)`, length `r(r-1)/2`, constant syzygies `ker C`, and the
   determinant criterion for a minimal original generating set.
2. **Adaptive separate-copy lower bound:** equations (4)--(8), including the
   exact transversal probability and `T(T-1)>=4q/(9r)` for `r>=3,d>=2`.
3. **Direct fallback:** exact overlap `1/r^r`, padded-certificate probability
   `gamma_r^2/r^r`, capped `O(r^(r+1)log(1/delta))` copies, and separation in
   the stated slow-rank regime.
4. **QSVT upper:** the Hermitian projected-unitary JM encoding, signed
   half-integer window reflection, exact padded-bank Lüders law, capped
   exhaustion and complete-instrument hybrid, exact support certificate,
   `O(r^2log(1/delta))` copy cap, same-column certificate retry, polynomial
   `r,log q,log(1/delta)` online gate cost, and strict separation under the
   displayed `q/r^5` regime.  At `delta=1/3`, three batches use `6r^2` copies
   and the sufficient finite threshold has leading term `81r^5`.

R13 strengthens the accepted R12 theorem to growing rank and meets all six
current PRD gates in its explicitly named source-only regime.  It establishes
delivered-copy and online
coherent-processing advantage, not coefficient-list, arbitrary-rank, practical
hardware, or unamortized device-construction advantage.
