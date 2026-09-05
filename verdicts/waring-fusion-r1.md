# Independent verdict: Waring component-packet fusion

2026-09-05. Reviewed `scouting/fresh-mechanism-round4.md`, independently
recomputed its rank-two maps, probabilities, and reduced-state error, and
audited its original `r-1`-hyperedge extension algebraically. The later
coded higher-rank construction is outside this verdict. Only this verdict
is written by the reviewer; no shared claim status is changed.

**VERDICT: PASS after verification of repairs W1--W3.** The core
identities and polynomial expected-cost theorem at fixed promises survive.
Rank-two mechanism novelty is REFUTED by the explicit comparison/Bell-fusion
reduction in §4 below, as the constructor's final disposition now recognizes.
No FATAL or MAJOR objection remains. No matched classical separation is proved.
Neither conclusion is a global
refutation of future higher-rank constructions.

## 1. Input, seed, and the discarded edge

1.1 For independent unit `u,v` and `k>=3`, the two component rays of a
rank-two Waring tensor are unique. Its first catalecticant has image
`span{u^(k-1),v^(k-1)}`. A line through those two Veronese points contains
no third Veronese point when `k-1>=2`: writing another vector in `span{u,v}`
would introduce mixed monomials unless one coefficient vanished. This
also explains why the growth/identification statement cannot start at `k=2`.

1.2 Let `s=<u,v>`, `t=|s|^2`, `g=1-t`, with the normalization of `T`
as stated in the memo. Antisymmetrizing one slot from each of two copies
kills the `uu` and `vv` terms. The surviving terms factor exactly as

`c_u c_v sqrt(g(1-t^(k-1))) omega tensor Psi_(k-1)^-`,
`omega=(u tensor v-v tensor u)/sqrt(2g)`.

The edge `omega` is unknown but independent of the remaining packet. It
may be discarded without decoherence of that packet. All complex phases
and the relative minus sign agree with the memo. Squaring its norm gives
`p_0=|c_u c_v|^2 g(1-t^(k-1))`.

1.3 There is a useful invariant interpretation of the seed promise. If
`rho_1` is the one-slot reduced density operator of `T`, it has rank two and

`p_0=(1-Tr(rho_1^2))/2=det_positive(rho_1)<=1/4`.

This follows either from the swap identity or from the two Gram determinants
in the `1 versus k-1` decomposition. Thus the seed is the ordinary
two-copy antisymmetric Schmidt-projection concentration step. A lower
bound on component separation alone does not lower-bound its probability.

1.4 Small separation also does not necessarily make the seed expensive:
normalization can magnify cancelling coefficients. Set
`u=e_0`, `v=cos(theta)e_0+sin(theta)e_1`, and
`T=(u^k-v^k)/sqrt(2(1-cos(theta)^k))`. Then

`p_0 -> (k-1)/k^2` as `theta -> 0`.

The separate known promise `p_0>=p_*` is therefore the appropriate input
condition. This example does not remove overlap dependence from the fusion
bound, and does not prove a general obstruction as `g` shrinks.

## 2. Fusion, trace distance, and the offline recurrence

2.1 In two `m` packets, compare one `A_1` slot with one `B_2` slot. The
oppositely oriented products have equal selected states and vanish. The
two equal orientations acquire opposite wedge signs, leaving

`sqrt(p_m) omega tensor Psi_(2m-1)^-`,
`p_m=g(1-t^(2m-1))/(4(1-t^m)^2)`.

The edge again factors out, including for nonreal `s`. In fact
`g/4<=p_m<=1/4`: the lower bound follows from
`1-t^(2m-1)>=(1-t^m)^2`; for the upper bound, write

`4p_m=(sum_(j=0)^(2m-2)t^j)/(sum_(j=0)^(m-1)t^j)^2`.

Each coefficient in the denominator's expanded polynomial is at least
one. The `m=1` case has probability `1/4` and does not grow, so `k>=3`
is essential for the intended recursion.

2.2 Successfully prepared child packets can be stored independently of
later failures. Rebuilding both children when fusion fails gives exactly

`C_0=2/p_0`, `C_(j+1)=2C_j/p_(m_j)`,
`m_j=1+(k-2)2^j`, `C_j<=(2/p_0)(8/g)^j`.

It is incorrect to replace this recurrence by the success probability of
one fixed complete tree. The displayed expected copy bound is polynomial
in the final packet size at fixed `g,p_0`, with exponent `log_2(8/g)`.
It is not a jointly polynomial guarantee in packet size and `1/g`.
Depth-first storage and geometric packet sizes give `O(m_j log q)` live
qubits. The stated expected gate bound includes the source-register and
source-preparation costs explicitly and is a valid conservative bound.

2.3 Tracing everything except `h<=m` registers on side `A` gives exactly

`rho_(m,h)=[U_h+V_h-s^h t^(m-h)|u^h><v^h|`
`                   -conj(s)^h t^(m-h)|v^h><u^h|]/[2(1-t^m)]`.

After making the component overlap real by a phase convention, the normalized
sum/difference vectors diagonalize its difference from the target mixture.
The two nonzero eigenvalues of that difference are opposite, with magnitude

`D(rho_(m,h),Sigma_h)=(1-t^h)t^(m-h/2)/[2(1-t^m)]`.

In particular, the full side is half the orthogonal projector onto
`span{u^m,v^m}`, and its distance from the uniform component mixture is
`|s|^m/2`. Discarding surplus slots cannot increase this distance. Thus the
output claim is a valid unlabelled quantum mixture, not a classical root list
or a preparation of the original component weights.

2.4 The explicit nonorthogonal family in §4 is normalized correctly and
has `g=3/4`, `p_0=5/36`. At `m=2`, fusion has probability `21/100`.
The next packet costs `960/7` original copies in expectation offline,
versus `6912/7` when restarting a fresh four-source tree after any failure.
This confirms the claimed operational distinction, without certifying novelty.

## 3. Parameters and the same-output comparison

3.1 The algorithm need not know `u,v,c_u,c_v` or their actual overlap.
It does need the declared numerical lower bounds `g_*,p_*`. An executable
choice is the first attainable `m_j` at least `h` and at least

`(2/g_*) max{0,log(1/(2epsilon))}`.

Since `t<=1-g_*<=exp(-g_*)`, this guarantees the required trace-distance
error. A known expected-copy upper bound is
`B_j=(2/p_*)(8/g_*)^j`. Aborting after `3B_j` copies gives failure at most
`1/3` by Markov's inequality. Both decisions use supplied promises, not
unknown decomposition data. Repeating independently capped attempts gives
an optional logarithmic overhead for a smaller abort probability.

3.2 The quantum-output task is mathematically well defined. It does not
automatically have a classical-output baseline, however. A classical list
of roots, full tomography, and the mixed packet `Sigma_h` are different
outputs. For a scalar downstream task, one must compare the same observable
against arbitrary adaptive global single-copy POVMs. The memo now requires
this and correctly leaves that lower bound unproved.

3.3 A measure-and-prepare comparison needs special care. With orthogonal
components and equal weights, tracing slots from one original `T` already
gives `Sigma_h` whenever `h<k`. For unequal weights it gives the weighted
mixture. At `h=k` no slot is traced, and the coherent `T` remains, so the
memo's original `h<=k` wording is false at its endpoint. A separation against
measure-and-prepare on the balanced `h<k` subfamily could certify the benefit
of retaining quantum data, without establishing any benefit of fusion.

## 4. Substantive known-fusion reduction

4.1 Let `E:C^2 -> C^q` have columns `u,v`. Then

`P_-^(q)(E tensor E)=(E tensor E)P_-^(2)`.

On the logical singlet this is the exterior map `wedge^2 E`, whose norm
is `sqrt(det(E^dag E))=sqrt(g)`. If `E=QL` is its polar factorization,
the square two-dimensional part obeys
`<singlet|(L tensor L)=det(L)<singlet|`.

4.2 The initial state is `E^tensor k` applied to the logical GHZ vector
with coefficients `c_u,c_v`. A physical packet is the same local embedding
of a redundantly encoded logical Bell singlet, normalized by
`sqrt(1-t^m)`. Commuting these embeddings through each comparison edge
identifies every successful tree branch with the corresponding redundant-
GHZ/Bell-fusion branch. Each edge contributes its exterior factor; incoming
and outgoing norms give exactly the probabilities in §§1--2. No extra
state-dependent operation appears in the graph or its offline schedule.

4.3 This is not an appeal to universal circuit compilation. The relevant
published structure is explicit: redundant encodings, destructive Bell
contractions on attached states, and offline expected-resource accounting
are described by
[Browne--Rudolph](https://arxiv.org/html/quant-ph/0405157v2), in the Type-II
fusion discussion. A fixed Pauli changes the chosen Bell bra in the known
orthogonal reference encoding. The antisymmetric comparison measurement
itself is the basis-independent primitive of
[Barnett--Chefles--Jex](https://arxiv.org/abs/quant-ph/0202087).

The nonorthogonal case uses the same comparison edges, with the exterior
identity above replacing the orthogonal basis formulas. This argument
does not pretend that the unknown `E` or its inverse can be implemented for
free, nor assert that the original photonic paper analyzes every present
input promise. It identifies the successful operations and their resource
recurrence, while the new Waring interpretation changes their application
and encoding. Those changes are expressly insufficient under D22.

4.4 Accordingly, the rank-two original-mechanism claim is REFUTED. The
parameterized nonorthogonal conversion identity remains a valid mathematical
product; its possible historical originality as an identity was not globally
certified. A missing classical separation cannot rescue a mechanism already
excluded by this specific reduction.

## 5. Scope of the original higher-rank extension

5.1 For the `r-1` hyperedges actually described in §6, the seed formula is
correct. An ordered alternating projection has squared norm `det G/r!`,
and the unnormalized alternating packet has norm
`Z_m^1=r! det G_m`. Their factors cancel to give
`p_0=|prod_a c_a|^2 det G det G_m`.

5.2 Hyperedge `j` survives only if the second packet's row `j` carries the
first packet's row-`j` component. The `r-1` guards force complete permutation
agreement. Rows `1,...,r-1` lose `r-2` slots in the first packet and one in
the second; row `r` loses `r-1` in the first and none in the second. Thus
each final row has `2m-r+1` slots, with growth requiring `m>r-1`.

5.3 Ordering the edge vectors contributes a fixed overall sign and one
`sign(pi)` per hyperedge. The resulting parity is therefore
`sigma_1+sigma_2+r-1 mod 2`. The probability in equation (10), including
every `r!`, is correct. For orthonormal components it equals `(r!)^(-r)`.
This does not by itself prove a useful uniform lower bound for general
Gram matrices or a same-output speedup.

5.4 There is a separate unavoidable cost for this particular seed:
its probability is `det_positive(rho_1)<=r^(-r)` by arithmetic--geometric
means on the rank-`r` one-slot spectrum. Hence that seed consumes at least
`r^(r+1)` original copies in expectation. This is not a lower bound on every
rank-`r` component algorithm. The rank-two Bell-fusion identification also
does not certify a prior-art equivalence for all determinant hypergraphs.
The separately proposed coded guards require their own review.

## 6. Repair record and decisions

**W1 — MAJOR, RESOLVED. Location:** end of §3, packet-size selection and Markov cap.
The displayed operational choices used the unknown `t` and actual expected
cost, despite the source providing only copies and promise bounds.
**FIX DEMAND:** Use the known `g_*,p_*` choices in §3.1 of this verdict.
**SURVIVING STATEMENT:** The claimed approximation and polynomial expected
cost follow under those explicit input promises; no component oracle is needed.
**VERIFIED REPAIR:** The final memo now chooses the packet size from `g_*`
and caps source copies using `3(2/p_*)(8/g_*)^j`.

**W2 — MINOR, RESOLVED. Location:** §2, sentence following the seed probability.
**FIX DEMAND:** Replace the assertion that nearly colliding components make
the seed expensive by the separate `p_0` promise and the cancellation
qualification in §§1.3--1.4. **SURVIVING STATEMENT:** Small weight can suppress
the seed, while overlap controls the stated fusion bound; collision alone
does not force a small seed probability for normalized cancelling tensors.
**VERIFIED REPAIR:** The final memo states the separate promises and explicitly
records the nonzero `(k-1)/k^2` collision limit.

**W3 — MINOR, RESOLVED. Location:** §4, classical attack 3.
**FIX DEMAND:** Replace `h<=k` by `h<k` for the one-copy partial-trace
shortcut. **SURVIVING STATEMENT:** The shortcut is exact when at least one
slot is discarded, with the weights and orthogonality qualifications above.
**VERIFIED REPAIR:** The final memo now uses `h<k`. Supplied source-circuit
workspace is also explicitly charged in its resource paragraph.

Accept the seed, fusion, exact reduced-state distance, and offline recurrence
for mathematical retention under the repaired promises. Accept the rank-two novelty claim only
as REFUTED, with §4's explicit surviving conversion statement. HOLD any
classical-separation claim. Retain equations (9)--(10) only at their original
scope; HOLD higher-rank novelty/resource extensions for separate review.
No theorem about all higher ranks or all quantum-output comparisons follows.

Independent bounded computation used one BLAS thread and a 60-second timeout:
42 checks passed for complex seed/fusion vectors, wedge factorization, both
probability bounds, exact marginal trace distances, the Schmidt determinant
identity, and the colliding-cancellation example. No registered checker or
noisy optical experiment was independently run. The cited primary papers were
opened for the concrete mechanism comparison, not a broad novelty search.

**VERDICT: PASS for the repaired mathematics; rank-two D22 novelty REFUTED.**
