# Independent verdict: residue traces and retained packets

2026-09-05. Reviewed the final 450-line
`scouting/original-residue-round3.md`, including its completed §3.4 packet
extension. This pass independently derives the normalization, metric, energy,
and classical-comparison statements below. Only this verdict is written by
the reviewer. No claim is promoted to PROVED.

**VERDICT: PASS for the qualified mathematical statements and negative
dispositions.** No FATAL or MAJOR mathematical objection remains in the final
memo. No proposed construction establishes a new algorithm under D22.
High-energy digital packet sampling remains HOLD because neither its gate
bound nor a same-output classical hardness result has been supplied. That is
an unresolved regime, not a proved impossibility theorem.

## 1. Normalization and local-duality audit

1.1 For a real map, half-density transport divides by
`sqrt(|det_R DF|)`. For a holomorphic map in complex dimension `n`,
`det_R DF=|det_C DF|^2`, so the corresponding divisor is `|J_C|`.
The phase `|J_C|/J_C` then gives canonical-form transport. All four rows
of the memo's encoding table have the correct functional norm and retain
the required source-state norm. A phase-only merger on a degree-`D` fibre
has norm `sqrt(D)`; it does not remove the fibre-degree normalization.
The measurable inverse-branch labeling remains explicitly charged access.

1.2 For `z^2-t^2`, the residue functional on the quotient is exactly the
coefficient of `z`. Its bilinear pairing in `1,z` is `[[0,1],[1,0]]`,
including at the double root. The evaluation transformation has singular
values `sqrt(2),sqrt(2)t`, whereas the ordinary trace pairing is
`diag(2,2t^2)`. The memo correctly separates these three objects and
does not identify bilinear duality with a positive Hermitian metric.

1.3 The two evaluation kets have squared overlap `1/(1+t^2)`. Helstrom's
bound therefore gives exactly
`T>=log(9/8)/log(1+t^2)` for success at least `2/3` under a uniform prior.
This is a valid collective-copy lower bound for the stated two-state encoding.
It is not a residue-computation lower bound under coefficient access. The
tensor-product example is also correctly limited to its specified readout.

1.4 Root cancellation and Bergman normalization give

`T_d(z^n)=y^m` for `n=dm+d-1`, and zero otherwise;
`(T_d/sqrt(d))e_(dm+d-1)=e_m`.

The partial-isometry norm, arithmetic division circuit, full remainder
instrument, success probability, and sparse-list classical sampler all agree.
Retaining the other remainders preserves total probability; it does not
make those outcomes the requested canonical residue.

1.5 In the Fock sampler, the orthonormal input columns imply
`sum_alpha alpha! |[z^alpha]g_U|^2=1`, and
`[z^alpha]g_U=per(U_alpha)/alpha!`. Its law is precisely BosonSampling.
The cited exact classical cost and `O(m)` additional space are supported by
[Clifford--Clifford](https://arxiv.org/abs/1706.01260v2); the later average-case
improvement at proportional mode count is explicitly scoped in
[their follow-up](https://arxiv.org/abs/2005.04214v2). No exhaustive current
best-algorithm claim is needed: the exact operation equivalence already
prevents a D22 promotion.

## 2. Packet metrics and the meaning of the output

2.1 For `g(z)=sum_r z^r h_r(z^d)`, angular orthogonality and radial change
of variables give

`||g||_B^2=sum_r (1/d) integral_D |h_r(y)|^2 |y|^(2(r+1)/d-2) dA(y)`.

Thus `h_r/sqrt(d)` belongs to the weighted space with
`alpha_r=(r+1)/d`, whose unit basis is
`sqrt((m+alpha_r)/pi)y^m`. The digital map sends its coefficients to the
corresponding remainder branch with no further normalization. Only the
branch `r=d-1` is ordinary Bergman space.

2.2 The memo's explicit diagnostic is correct:
`||phi_a'||_(alpha=1/2)^2=2pi-(4pi/3)a^2+O(a^4)` for real small `a`.
An ordinary canonical disk pullback is therefore not unitary on that fixed
weighted branch. Its compensating modulus would be
`|phi_a(z)/z|^(alpha-1)`, with genuine divisor/branch issues if interpreted
holomorphically. Labeling every branch as the same unweighted space does
not implement that geometric transport.

2.3 The displayed basis identification `J_alpha` rescales monomials by
`sqrt((m+1)/(m+alpha))`. Accordingly, a digital ordinary-Bergman operation
on those labels realizes `J_alpha^(-1)C_a J_alpha`, not the original
weighted-space canonical pullback. The final memo now states this change
of task explicitly. No direct-image metric-transport circuit is supplied.

2.4 Integer division is inexpensive on a binary exponent register. Native
two-mode squeezing acts on the encoding `|n> -> |n+1,n>` and realizes the
discrete-series `SU(1,1)` generators. These are different resource models:
native squeezing does not supply a proved `poly(log M)` digital transform,
and binary division does not supply physical coherent photon-number halving.
The final memo correctly leaves a common cheap implementation unproved.

## 3. A precise classical trajectory regime

3.1 If previous remainder labels are only retained, measured later, or used
as diagonal controls, measuring them immediately preserves the final joint
law. A classical simulation stores one conditional coefficient vector and
one sampled label history. It never has to store all `2^L` branches.
This reduction does not apply to a subsequently constructed coherent mixing
of old labels; that would require its own operation and cost analysis.

3.2 Put `E=Tr((N+1)rho)`. In ordinary Bergman space,
`K_0=N+1`, `K_+|n>=sqrt((n+1)(n+2))|n+1>`.
The Cauchy--Schwarz bound on adjacent coefficients gives
`|<K_x>|<=<K_0>`. Therefore a squeeze of magnitude `r` obeys
`E_after<=exp(2r)E_before`. Division by two then gives

`E_next <= (exp(2r) E_before+1)/2`.

These are average energies over the retained labels, not bounds on every
rare conditioned branch. For `r<=r_*<(log 2)/2` they stay bounded by
`E_0+O(1)`. The regime actually extends to the critical value
`r_*=(log 2)/2`, equivalently `|a|=1/3`, where
`E_j<=E_0+j/2`. Intermediate pre-division energies satisfy the same
polynomial bound up to a constant factor.

3.3 A cutoff `M` loses probability at most `E_max/(M+1)` at each stage.
A square-root disturbance estimate and a hybrid over the `L` operations
bound the total output error by `O(L sqrt(E_max/(M+1)))`. Thus

`M=O(E_max L^2/epsilon^2)`

suffices. One rigorous trajectory implementation retains the computed
subnormalized vector after truncation and includes an overflow outcome
for its missing squared norm. On overflow it returns any fixed output.
This defines a trace-preserving approximation; silently normalizing away
each path's discarded tail would require a different error argument.

3.4 No matrix-entry oracle is needed at this cutoff. For the memo's
`phi_a(z)=(z-a)/(1-conj(a)z)`, the exact entry is

`(C_a)_(m,n)=(1-|a|^2)sqrt((n+1)/(m+1))`
` *sum_(j=0)^min(m,n) binom(n,j)(-a)^(n-j)`
`                  binom(n+m-j+1,m-j)conj(a)^(m-j)`.

It is a finite binomial sum. Sufficient guard precision for its cancellations
costs polynomially in `M`, the supplied parameter precision, and the
requested output accuracy. Thus explicit coefficient input and the energy
regime above give a polynomial-time same-output classical sampler. This
does not prove a polynomial bound in the binary length of a huge initial
degree, nor prove impossibility of a future fast digital squeeze transform.

3.5 There is a separate copy-access boundary. A complete packet run consumes
only one original coefficient-state copy; its other registers are known
ancillas. Any final classical label/scalar law is therefore one POVM on that
copy. The campaign's comparator permits arbitrary global single-copy POVMs,
so it permits this same law. This rules out a copy-complexity separation
for that run. It does not settle classical circuit-input running time,
which is why the trajectory and energy comparison above is still needed.

## 4. Canonical traces on kernel states: an exact further attack

The following is an independent addition to the final memo's audit. Define
the normalized Bergman reproducing-kernel state, for `|a|<1`, by

`k_a(z)=(1-|a|^2)/(sqrt(pi)(1-conj(a)z)^2)`;
its coefficient at `e_n` is `(1-|a|^2)sqrt(n+1)conj(a)^n`.

4.1 Applying the residue partial isometry coefficientwise gives exactly

`(T_d/sqrt(d))k_a`
` = [sqrt(d)conj(a)^(d-1)(1-|a|^2)/(1-|a|^(2d))] k_(a^d)`.

The conditional state is again a kernel state. With `s=|a|^2`, its
success probability is

`p_d(a)=d s^(d-1)/(1+s+...+s^(d-1))^2 <= 1/d`.

The inequality follows from arithmetic--geometric means; at `a=0` the
residue probability is zero. Disk automorphisms map normalized kernel
states into this family up to a known phase. In particular, a vacuum
reference followed by automorphisms and canonical residue branches never
leaves this one-parameter family.

4.2 A prescribed chain of degrees `d_1,...,d_L` therefore has canonical
success probability at most `1/prod_j d_j`. Conditional coefficient
sampling remains the negative-binomial law
`Pr(n)=(1-|a|^2)^2(n+1)|a|^(2n)`, with `a` obtained by the composed
point transformations. Its norm, success scalars, and output law can be
tracked classically. Arithmetic precision and parameters approaching the
boundary must still be charged. This is a genuine explicit classical
family, not a comparison against dense coefficient expansion.

4.3 More generally, treat `g(z)dz` as a meromorphic differential on the
Riemann sphere. A degree-`D` polynomial gives one pole, at infinity, of
order `D+2`. Automorphisms move poles without increasing their orders.
A finite-map canonical trace sends poles to their images and creates no
poles over regular source differentials. At ramification index `e`, a
pole of order `s` maps to order at most `ceil(s/e)`, by the same Laurent
coefficient selection as in §1. Thus powers and automorphisms preserve a
one-pole rational representation with order at most `D+2`.

For the degree-two trace, the identity
`T_2 g(y)=[g(sqrt(y))-g(-sqrt(y))]/(2sqrt(y))` eliminates the formal
square root algebraically. Polynomial numerator/denominator operations
update this bounded-order representation without expanding the composed
map's degree. This suggests a further classical attack polynomial in the
initial degree in arithmetic operations. A general efficient bit-complexity
and normalized-sampling theorem for ill-conditioned coefficients is not
proved here. It is not a `poly(log D)` result, and it does not apply to
the artificial even packet after its different `J_alpha` rescaling.

## 5. Minor fixes and disposition

**R1 — MINOR. Location:** §3.4's cutoff/trajectory paragraph.
**FIX DEMAND:** Specify the overflow or equivalent subnormalized-trajectory
rule in §3.3 of this verdict, and state that `E_max` includes intermediate
squeeze outputs. **SURVIVING STATEMENT:** The averaged energy and hybrid
argument prove the claimed polynomial-cutoff classical simulation; no
per-branch energy bound is needed.

**R2 — MINOR. Location:** §3.4's copy/encoding comparison and §5 merge proposal.
**FIX DEMAND:** Add the one-original-copy POVM boundary in §3.5 above, and
retain the distinction from a classical running-time comparison.
**SURVIVING STATEMENT:** The proposed scalar/label packet task cannot give
a copy separation against the stated arbitrary-single-copy comparator;
other input models still need their own cost theorem.

**R3 — MINOR. Location:** canonical composition research direction in §3.4.
**FIX DEMAND:** Record kernel-state closure and its `1/prod d_j` success
bound before treating vacuum/reference-state compositions as a hard family.
Keep the broader rational-function observation at its stated arithmetic
scope. **SURVIVING STATEMENT:** This canonical family is explicitly
trackable; it does not settle arbitrary high-degree digital packet inputs.

Accept the encoding table, two-root pairing and scoped copy lower bound,
monomial residue partial isometry, weighted-branch identities, and energy/
trajectory comparison for retention with their stated hypotheses. Accept
the proposed bosonic residue sampler only with its exact BosonSampling
equivalence. Retain the new kernel-closure derivation as a mathematical
candidate for archival and checking. Hold geometric metric transport,
large-energy digital squeezing, coherent label recombination, and any
same-output hardness result until actual constructions/theorems exist.
Do not assert exact equivalence with a published wavelet/baker-map algorithm
from resemblance alone. No global impossibility or historical novelty was
established here.

Independent bounded computation used one BLAS thread and a 60-second timeout:
73 checks passed for complex kernel closure, the `1/d` bound, explicit
Möbius matrices, norm/energy estimates, halving, and the weighted-branch
norm expansion. These are unregistered finite checks; no hardware operation
or high-energy gate compilation was verified. The two primary BosonSampling
sources were opened only to verify the cited comparisons.

**VERDICT: PASS for the qualified memo; no D22-compliant algorithm established.**
