# Intersection and integration observables (arm C)

Lane `briefs/lane-intersection-observables.md`, PRD §4 arm C. r0 2026-09-03; **repaired at r1
2026-09-03** against `verdicts/intersection-observables-r1.md` (FAIL, O1-O8, three FATAL). Scouting
only; nothing ratcheted. Script `checkers/explore/intersection_observables.py` (`timeout 900`,
exit 0). See `## Repair r1 response` at the end for the objection-by-objection disposition.

Conventions C1-C12 binding; objects cited, never redefined: D-polynomial-ring, D-fock-space,
D-fock-basis, D-hamiltonian, D-ground-space, D-inverse-system, D-projectors, D-coherent-state,
D-bergman-projector, D-toeplitz-operator, D-hilbert-function, D-normalised-hilbert-function,
D-saturation-regularity-stable-range, D-macaulay-matrix, D-input-model, D-qsvt,
D-dqc1-style-estimate, D-block-encoding-normalisation, D-condition-number, D-hardness-anchors,
D-spin-mixing-hamiltonian, D-symmetric-sector. **Departure from C5**, as in the whole checker suite:
generators are as written, not unit Bombieri-Weyl; nothing depends on it, every quantity being a
projector overlap, a Hilbert-function count or a ratio (C-002, D-norm-comparison).

**Notation.** `P_I` is the projector onto `ker H_N^{(I)} = (I_N)^perp`, the Bergman projector of
D-bergman-projector -- *not* the projector onto `I_N`, which D-projectors calls `P_{I_N}`. This is
folded into the proposed D-intersection-overlap and into the C-085/C-166/C-167 amendments; it is
**not** a claim row (verdict O7). Metric: `d(p,q) = arccos|<p,q>|` (diameter `pi/2`), so
`vol(CP^n) = pi^n/n!`, `vol(V) = deg(V)pi^k/k!`, `|<e_p,e_q>|^2 = cos^{2N}d(p,q)` for
`e_p = (p.z)^N/sqrt(N!)`.

## Bottom line (r1)

1. **The linear half of arm C is EXACT and needs no analysis at all.** For subspaces `U, W` of
   `C^{n+1}` with principal cosines `sigma_1..sigma_r`, `r = min(dim U, dim W)`,
   `Tr(P_{Sym^N U} P_{Sym^N W}) = h_N(sigma_1^2, ..., sigma_r^2)` with `h_N` the complete
   homogeneous symmetric polynomial. Elementary proof (principal vectors diagonalise the overlap)
   and machine-precision verification on random subspaces (N11). Every linear table in this lane --
   two lines, two planes, Clifford and generic skew pairs, the excess `P^4` families, hyperplanes in
   `P^n` -- is one specialisation. This identity is the opening move of verdict O1 and is this
   lane's most defensible product.
2. **The general clean-intersection asymptotic is CONJECTURAL, with the missing step named.** For
   radical `I, J`, `V, W` smooth, `N` stable, intersection clean (Bott),
   `Tr(P_I P_J) = (N/pi)^l int_Z J(x)^{-1} dvol_Z (1 + O(1/N))`. The r0 Laplace derivation omitted
   the anti-diagonal `T_xZ` normal block (verdict O1); that block is supplied here and tested by a
   new angle-carrying excess family (N7b). What remains unproved is the ambient Bergman-frame
   operator-norm estimate, Geometry 2.4. The row is CONJECTURE, marked **HOLD (do not merge)**.
3. **C-086 and C-168 are REFUTED as written** (verdict O3, FATAL). Under the registered
   D-toeplitz-operator, `T_g = P_0 :g: P_0`, so for `g = |z_2|^2` the ratio `Tr(P_0T_g)/HF(N)` grows
   like `N` and diverges. The lane silently tested a different operator. The normalisation that
   makes the trace consistent with the Fubini-Study average is
   `T~_g^{(N)} = ((N-r)!/N!) P_0 :g(a^dag,a): P_0` for a bidegree-`(r,r)` symbol at `N >= r`; that is
   the surviving statement (C-NEW-IO-TOEPLITZ) and it is confirmed numerically.
4. **The r0 `1/N` Toeplitz coefficient was a finite-range fit.** Section K carries the conic to
   `N = 1200` by an exact 1-D kernel recurrence: the coefficient is about **0.03144**, not 0.03275.
   The r0 intercept was nevertheless right to 1.7e-5 against the exact
   `<|z_2|^2>_V = -1/6 + 2 sqrt(3) pi/27`.
5. **K-IO2 is RETRACTED** (verdict O6, FATAL). It contradicted this lane's own N9: visibility
   persists to `codim(V ^ W) = O(log n)`, not `O(1)`, so the "small degrees" squeeze fails --
   `n^{O(log n)}` is quasipolynomial. The cited Sommese-Verschelde-Wampler and Lairez results also
   do not prove the universal polynomial baseline that was asserted. C-NEW-IO-WITNESS-BASELINE is
   deleted. What survives: `I_N + J_N` is a concatenation of Macaulay rows, and diagonal homotopy is
   a relevant competitor **once witness sets and conditioning promises are supplied**.
6. **The dequantization comparison was wrong** (verdict O5, FATAL) and is redone below at a single,
   stated error model: relative `delta` for Hutch++, additive `eps` for `tau_N`, three projector
   filters per `A`-application, and every quantum cost expressed through `gamma_N = Delta_N/alpha_BE`
   exactly once. C-NEW-IO-TOEPLITZ-COST is REFUTED: it double-counted `alpha_BE`, and the conic
   (`Delta_N = N+1`, `alpha_BE = O(N^2)`) is a counterexample to its degree-only exponent.
7. **C-167 survives as mathematics; its cost row is REFUTED.** The Clifford closed form is exact,
   `Tr = (N+1)cos^{2N}(d_FS)`, and the bias in `-(1/2N)log Tr` is `-log(N+1)/(2N)` -- NEGATIVE, so
   the estimator sits BELOW the target; r0 had the sign backwards. Because the prefactor is known
   exactly it can be divided out, so no `N = Omega(eta^{-1}log(1/eta))` is forced. The exponentially
   small normalised signal is real (`tau_N = 1.657e-37` at `d_0 = 0.3`, `N = 800`); the alleged
   necessity was not.
8. **Score 1/5** (verdict O8), or at most 2/5 if the trivial linear-subspace demonstration takes
   full criterion-5 credit. Criteria 2, 3 and 4 are not met. The outputs are one exact identity, one
   conjectural asymptotic with a named missing step, exact closed forms for six families, and
   negative evidence -- **not** "three theorems" (r0 wording, an L1 violation).

## Numerics

Regenerate with `timeout 900 python3 checkers/explore/intersection_observables.py` (exit 0).
`M_N = dim R_N`, `l = dim(V ^ W)`, `J = prod_i sin^2 theta_i`, `mu_cap = sup_Z J^{-1}`. The script
now carries five in-process mutations that must be caught (verdict O4); its terminal message states
exactly which quantities carry an assertion and which are reported as observations only.

**N1. Two lines in `P^2`, `l = 0`, transversal (section A).** `I = (z_0)`,
`J = (cos(t)z_0 + sin(t)z_1)`; `Tr = sum_{a=0}^{N}cos^{2a}(t) -> 1/sin^2 t = 1/J`, SVD-verified to 8
digits at `N <= 16`. Tangent-space `J` matches `sin^2 t` to 1e-9.

| `t` | `1/J` | `Tr(N=8)` | `Tr(N=16)` | `Tr(N=64)` | `Tr/M_N`(64) | `Tr/(HF_I HF_J)`(64) |
|---|---|---|---|---|---|---|
| `pi/2` | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 4.66e-4 | 2.37e-4 |
| 1.0 | 1.412283 | 1.412261 | 1.412283 | 1.412283 | 6.58e-4 | 3.34e-4 |
| 0.4 | 6.594277 | 5.093355 | 6.191586 | 6.594127 | 3.07e-3 | 1.56e-3 |

**N2. Two planes in `P^3` meeting in a line, `l = 1` (section C).** `Tr = sum_a c^{2a}(N+1-a) =
(N+1)/s^2 - c^2/s^4 + O(c^{2N})`, SVD-verified to 8 digits at `N <= 12`. `Tr/N` at `N = 128` is
1.0078, 1.9441, 10.605 for `t = pi/2, 0.8, 0.3` against `1/J` = 1.0000, 1.9433, 11.4505.

**N3. The crossover -- killer K-IO3 (section C).** Local exponent `d log Tr/d log N`. Truth is 1;
`2` is the `V = W` value. **Asserted** at `mu_cap = 100.3`: slope(256) = 1.5366 (> 1.4) and
slope(1024) = 1.1599 (< 1.3); mutation M-IO4 moves the angle and is caught.

| `t` | `mu_cap` | `N=16` | `N=32` | `N=64` | `N=128` | `N=256` | `N=1024` | `N=4096` |
|---|---|---|---|---|---|---|---|---|
| 0.500 | 4.4 | 1.198 | 1.115 | 1.056 | 1.027 | 1.013 | 1.003 | 1.001 |
| 0.100 | 100.3 | 1.728 | 1.801 | 1.793 | 1.705 | 1.537 | 1.160 | 1.036 |
| 0.020 | 2500.3 | 1.764 | 1.871 | 1.929 | 1.955 | 1.959 | 1.902 | 1.678 |

**N4. Two skew lines in `P^3`, `V ^ W = {}` (section B).** Clifford pair: exact,
`Tr = (N+1)cos^{2N}(t)`, SVD-verified to 10 digits at `N <= 12`. **Bias sign corrected (O2):**
`-(1/2N)log Tr = log sec t - log(N+1)/(2N)`, so the estimator lies BELOW the target, as the table
shows.

| `d_0 = t` | `log sec d_0` | `-(1/2N)log Tr`, `N=8` | `N=20` | `N=40` | `Tr(40)` | `Tr/M_N(40)` |
|---|---|---|---|---|---|---|
| 0.6 | 0.191965 | 0.054639 | 0.115852 | 0.145546 | 8.77e-6 | 7.11e-10 |
| 0.3 | 0.045692 | -0.091635 | -0.030421 | -0.000728 | 1.060 | 8.59e-5 |

**Generic skew pair corrected (O1).** `sigma = (0.954282512625, 0.909838680515)`, so by N11
`Tr = h_N(sigma_1^2, sigma_2^2) = (sigma_1^{2N+2} - sigma_2^{2N+2})/(sigma_1^2 - sigma_2^2)` exactly.
`Tr/cos^{2N}d_0` = 2.735, 4.169, 5.354, 7.142, **8.820** at `N = 2,4,6,10,16` and **10.99107** at
`N = 100`, converging to `sigma_1^2/(sigma_1^2 - sigma_2^2) = 10.9917866070`. r0 called the `N <= 16`
values "saturating"; they are not. The exponent is nevertheless 0, as Laplace predicts for an
isolated closest pair.

**N5. Conic and line in `P^2`, transversal versus TANGENT (section D).** `V = {z_0z_1 - z_2^2}`;
`W_t = {z_1 = z_0}` transversal at `[1:1:+-1]` (`J = 1`, prediction 2); `W_g = {z_1 = 0}` TANGENT at
`[1:0:0]`, contact order `m = 2`, `gamma = 1`.

| `N` | `Tr` transversal | slope | `Tr` tangent | slope | `Tr_tan/sqrt(N)` |
|---|---|---|---|---|---|
| 16 | 2.034957 | -0.0241 | 4.792859 | 0.3817 | 1.198215 |
| 44 | 2.011779 | -0.0068 | 7.199825 | 0.4144 | 1.085415 |
| 60 | 2.008552 | -0.0047 | 8.205198 | 0.4237 | 1.059286 |

Transversal exponent `-> 0`, constant `-> 2` as `2 + 0.5/N`. **TANGENT exponent `-> 1/2`**, with the
three-term fit `Tr/sqrt(N) = 0.8915 + 1.380/sqrt(N) - 0.62/N` against `Gamma(3/2) = 0.886227` (0.6%,
asserted; mutation M-IO1 swaps the two lines and is caught). `HF_{R/(I+J)}(N) = 2` for all `N >= 1`.
**The `m >= 2` restriction is essential** (verdict O2): at `m = 1` the induced volume on `V`
contributes `1 + |gamma|^2` and the constant is `(1+|gamma|^2)/|gamma|^2`, not `|gamma|^{-2}`.

**N6. Two smooth conics in `P^2`, four transversal points (section E).** `W_lam =
{z_0^2+z_1^2+lam z_2^2}`; both pairs have `HF_{R/(I+J)}(N) = 4` (Bezout).

| `lam` | `cos t` | `1/J` each | predicted `sum_i 1/J_i` | `Tr(60)` | `Tr/limit` | slope at 60 |
|---|---|---|---|---|---|---|
| -10 | 0.560612 | 1.458333 | 5.833333 | 6.276744 | 1.0760 | -0.098 |
| -3 | 0.872872 | 4.200000 | 16.800000 | 16.799398 | 0.99996 | 0.287 |

Richardson on the well-conditioned pair gives 5.70 against 5.833 (2.3%). The r0 check clamped
`Tr/limit` to `<= 1` so overshoots passed automatically (verdict O4); the clamp is gone and the
two-sided tolerance is what mutation M-IO3 exercises.

**N7. Excess but clean intersection (section F).** (a) `V = {z_3=z_4=0}`, `W = {z_2=z_4=0}` in
`P^4`: expected dimension `2+2-4 = 0`, actual `l = 1`, `J = 1`; `Tr = N+1` exactly for `N = 2..12`.
**(b) NEW at r1, the case that tests verdict O1's missing block.** `I = (z_3, z_4)`,
`J = (-sin(t)z_2 + cos(t)z_3, z_4)`: again excess with `l = 1`, but now `J = sin^2 t`. Principal
cosines `(1,1,c)`, so by N11 `Tr = h_N(1,1,c^2) = sum_a c^{2a}(N+1-a)` exactly (SVD-verified,
`N <= 12`), and `Tr/N -> 1/sin^2 t` = 1.6297 at `t = 0.9` and 6.5943 at `t = 0.4`. The `vol(Z)/pi^l`
factor (anti-diagonal block) and the `1/J` factor (transverse block) are both present and separately
identifiable; r0 derived only the second.

**N8. Toeplitz averages on the conic (section G).** `T~_g^{(N)} = ((N-r)!/N!)P_0 :g: P_0`. Reference
values by 4000-node Gauss-Legendre quadrature on `[s:t] -> [s^2:t^2:st]` with density
`A(u) = (u^2+4u+1)/(u^2+u+1)^2`; the quadrature gives `int A du = 2.0000000000` (`= deg V`),
`2<|z_0|^2>+<|z_2|^2> = 1.0000000000`, and reproduces the **exact**
`<|z_2|^2>_V = -1/6 + 2 sqrt(3) pi/27 = 0.2363998587187151` to 1e-12.

| `N` | `Tr(P_0 n_2)/(N HF)` | err | `Tr(P_0 n_2(n_2-1))/(N(N-1)HF)` | err |
|---|---|---|---|---|
| 22 | 0.2378805749 | 1.48e-3 | 0.0651502954 | 5.28e-4 |
| 60 | 0.2369303424 | 5.31e-4 | 0.0648133103 | 1.91e-4 |
| fit over `N<=60` | 0.23638334 + **0.03275**/N | -1.65e-5 | 0.06461880 + 0.01166/N | -3.51e-6 |
| quadrature | 0.23639986 | | 0.06462232 | |

The intercepts are right; the `1/N` coefficients are finite-range fits, superseded by N12.

**N9. Size of the DQC1 signal (section H).** Two hyperplanes in `P^n` at angle `t`, `N = n`.

| `n = N` | `M_N` | `Tr` (`t = pi/2`) | `Tr/M_N` | `Tr/sqrt(HF_I HF_J)` | `Tr/(HF_I HF_J)` |
|---|---|---|---|---|---|
| 4 | 70 | 15 | 2.143e-1 | 4.286e-1 | 1.22e-2 |
| 8 | 12870 | 3003 | 2.333e-1 | 4.667e-1 | 7.25e-5 |
| 32 | 1.8e18 | 4.5e17 | 2.460e-1 | 4.921e-1 | 5.37e-19 |

`Tr/M_N -> 1/4`, `Tr/sqrt(HF_I HF_J) -> 1/2`. With codimension growing (`I = (z_0..z_{k-1})`,
`J = (z_k..z_{2k-1})`, `n = N = 4k`, `codim(V^W) = 2k`), `Tr/M_N` = 0.2143, 0.03846, 0.0012236,
1.2304e-6 at `k = 1,2,4,8`. **Corrected reading (O6):** at `N = n` and `k = o(n)`,
`Tr/M_N = binom(2n-2k, n-2k)/binom(2n,n) = 4^{-k}(1 + O(k^2/n))`, so inverse-polynomial visibility
persists to `k = O(log n)`, i.e. `codim(V ^ W) = O(log n)` -- not `O(1)`, which is what r0's squeeze
assumed.

**N10. The Bergman frame lemma, measured (section I).** Spectrum of `(N/pi)S_V` on `ker H_N` for the
conic. Min / max / mean on `ker H_N` and max on `I_N`: `N=6`: 0.890019 / 1.032096 / 0.923077 /
7.2e-16; `N=10`: 0.930690 / 1.038218 / 0.952381 / 1.2e-15; `N=14`: 0.949404 / 1.035624 / 0.965517 /
1.0e-15; `N=18`: 0.960160 / 1.032098 / 0.972973 / 9.7e-16. The mean is exactly `2N/(2N+1)` (an
identity); the spread falls as 0.14, 0.11, 0.086, 0.072. **This is evidence for, not a proof of,
Geometry 2.4** -- mean flatness does not imply operator-norm flatness (verdict O1).

**N11. The exact linear identity (section J, new at r1).** For subspaces `U, W` of `C^{n+1}` with
principal cosines `sigma_1..sigma_r`, `r = min(dim U, dim W)`:
`Tr(P_{Sym^N U} P_{Sym^N W}) = h_N(sigma_1^2,...,sigma_r^2)`. Verified on random subspaces in
`C^4, C^5, C^6` at `N = 4..7`, worst relative discrepancy `< 1e-14`; mutation M-IO5 perturbs the
cosines and is caught. Specialisations: `(1,c) -> sum_a c^{2a}` (N1); `(1,1,c) -> sum_a c^{2a}(N+1-a)`
(N2, N7b); `(c,c) -> (N+1)c^{2N}` (N4 Clifford); `(sigma_1,sigma_2)` (N4 generic);
`(1,1,0) -> N+1` (N7a); `(1^{n-1},c) -> sum_a c^{2a}binom(N-a+n-2,n-2)` (N9).

**N12. Toeplitz asymptotics at `N = 1200` (section K, new at r1).** `H_N` for the conic is block
diagonal over `d = k_0 - k_1` and each block has a one-dimensional kernel with an explicit
recurrence, so the traces are computed exactly with no SVD. Values agree with the SVD at `N <= 16`.

| `N` | `Tr(P_0 n_2)/(N HF)` | `N(value - L)`, `L = -1/6 + 2 sqrt(3) pi/27` |
|---|---|---|
| 22 | 0.237880574939233 | 0.0325757569 |
| 60 | 0.236930342380032 | 0.0318290197 |
| 200 | 0.236557557384253 | 0.0315397331 |
| 800 | 0.236439169045958 | 0.0314482618 |
| 1200 | 0.236426057170887 | 0.0314381426 |

The asymptotic coefficient is about **0.03144**, not the r0 short-range 0.03275. **Ordering check
(O4):** the intercept is now pinned to the exact `L` and the coefficient must land in `[0.030,
0.034]`; the anti-normal alternative `n_2 -> n_2 + 1` shifts the level-`N` value by exactly `1/N`
and the coefficient by exactly `+1`, so it is rejected. r0's free-intercept, free-coefficient fit
absorbed that mutation.

## Geometry

Lamport-hierarchical sketch (L3). **Status: the argument is not complete; step 2.4 is an unproved
leaf and is why C-NEW-IO-CLEAN is HOLD.** Steps 5.3-5.4 were repaired at r1 (verdict O1).

**ASSUME.** **A1** `I, J` homogeneous radical; `V = V(I)`, `W = V(J)` smooth of dimensions
`k_1, k_2`. **A2** `N >= max(reg I, reg J)` (D-saturation-regularity-stable-range). **A3** the
intersection is **clean**: `Z = V ^ W` smooth of pure dimension `l` and `T_xV ^ T_xW = T_xZ` for
every `x in Z`. **A4** the metric convention above; `A_x = T_xV (-) T_xZ`, `B_x = T_xW (-) T_xZ`,
`theta_i(x)` their principal angles (padded with `pi/2` when the dimensions differ),
`J(x) = prod_i sin^2 theta_i(x)`.

**PROVE (for fixed `I, J`, as `N -> infinity`).**
`Tr(P_I P_J) = (N/pi)^l int_Z J(x)^{-1} dvol_Z(x) . (1 + O_{I,J}(1/N))`.

1. `P_I` projects onto `H_V := span{e_p : p in V}`. 1.1 `ran P_I = (I_N)^perp` [D-ground-space,
   D-projectors]. 1.2 `= (I(V)_N)^perp` [A2]. 1.3 `= span{e_p : conj(p) in V}` [C-028, C-026,
   D-coherent-state]; conjugation is C3 and immaterial for the real-coefficient examples.
2. **(Bergman frame lemma.)** `S_V := int_V |e_p><e_p| dvol_V(p) = (pi/N)^{k_1}(P_I + E_N)` with
   `||E_N|| = O(1/N)`. 2.1 `ran S_V = H_V` exactly, every `N` [step 1]; measured to 1e-15 (N10).
   2.2 `Tr S_V = vol(V) = deg V . pi^{k_1}/k_1!` [Wirtinger]. 2.3 `rank S_V = HF_{R/I}(N)` [A2].
   2.4 So the **mean** eigenvalue of `(N/pi)^{k_1}S_V` on `H_V` is `1 + O(1/N)`. The lemma needs
   **operator-norm** flatness, which 2.2-2.3 do not give. **UNPROVED LEAF.** It is the
   Tian-Zelditch-Catlin statement for `(V, O(N)|_V)` read in the ambient frame [Tian,
   DOI 10.4310/jdg/1214445039; Zelditch, arXiv:math-ph/0002009], but this lane found no statement in
   ambient coordinates for a subvariety that can be cited verbatim. N10 is evidence, not proof.
3. `Tr(P_I P_J) = (N/pi)^{k_1+k_2} Tr(S_V S_W)(1+O(1/N))` [step 2 twice].
4. `Tr(S_V S_W) = int_V int_W cos^{2N}d(p,q)` [D-coherent-state; A4].
5. **(Laplace, repaired at r1.)** `int_V int_W cos^{2N}d = (pi/N)^{k_1+k_2-l} int_Z J^{-1}dvol_Z
   (1+O(1/N))`.
   5.1 `cos^{2N}d = exp(-Nd^2(1+O(d^2)))`, concentrating at `d = O(N^{-1/2})`.
   5.2 The zero set of `d` on `V x W` is the diagonal `{(x,x) : x in Z}`.
   5.3 **Normal decomposition.** Write `T_xV = T_xZ (+) A_x`, `T_xW = T_xZ (+) B_x`; a point of
   `V x W` near `(x,x)` is `(s + a, t + b)` with `s,t in T_xZ`, `a in A_x`, `b in B_x`. The normal
   directions to the diagonal split into (i) the **anti-diagonal common-tangent** variable
   `delta = t - s in T_xZ`, complex dimension `l`, and (ii) the **transverse** variable
   `a - b in A_x + B_x`, complex dimension `k_1 + k_2 - 2l`. The diagonal variable `s + t` runs
   along `Z` and contributes `vol(Z)`.
   5.4 **The two Gaussian blocks.** (i) `int_{C^l} e^{-N|delta|^2} d(delta) = (pi/N)^l`.
   (ii) The map `(a,b) -> a - b` from `A_x x B_x` onto `A_x + B_x` is a linear isomorphism (this
   **is** A3) with Jacobian `prod_i sin theta_i` over the *real* principal angles, i.e. `J(x)^{1/2}`
   per copy and `J(x)` in the squared measure, giving `(pi/N)^{k_1+k_2-2l}/J(x)`. Their product is
   `(pi/N)^{k_1+k_2-l}/J(x)`, which is the stated factor. **r0 integrated only (ii) while quoting
   the exponent of the product** (verdict O1): had r0 used what it actually derived it would have
   obtained `N^{2l}`, not `N^l`. N7b separates the two blocks experimentally.
6. Combining 3-5: `(N/pi)^{k_1+k_2}(pi/N)^{k_1+k_2-l} = (N/pi)^l`. QED **modulo 2.4**.

**Corollary 6a.** For `J(x) = J_0` constant on `Z`, `Tr(P_I P_J) = J_0^{-1}HF_{R/(I+J)}(N)(1+O(1/N))`
-- asymptotic, **not exact** (verdict O6: N1 at `t=1, N=8` gives 1.41226118, not `1/J = 1.41228293`;
N5 gives 2.03495679, not 2). **Corollary 6b.** Under A1-A4 the growth exponent is `dim(V ^ W)`,
transversal or excess, provided clean. **Corollary 6c (disjoint, Morse-Bott).** If `V ^ W = {}`,
assume the closest-pair set `S subset V x W` is a compact smooth **real Morse-Bott** minimum
manifold of real dimension `r` with nondegenerate normal Hessian (r0 wrote `dim_C S`, which need not
exist -- verdict O2). Then `Tr = C N^{r/2}cos^{2N}(d_0)(1+O(1/N))` and
`-(1/2N)log Tr = log sec d_0 - r log N/(4N) + O(1/N)`. Clifford: `r = 2`, closed form exact; generic
skew: `r = 0` (N4).

**What fails without each hypothesis.** Without **A2**, `(I_N)^perp` strictly contains the coherent
span (D-entangled-defect) and 1.3 fails. Without **A1**, multiplicity enters through jets. Without
**smoothness**, 5.3 has no tangent space. Without **A3** the exponent changes: for smooth plane
curves meeting at one point with contact order **`m >= 2`** (local model
`d^2 = |u-v|^2 + |gamma|^2|u|^{2m}` in a unitary Fubini-Study normal chart, and
`int_C exp(-N|gamma|^2|u|^{2m})dA = pi Gamma(1+1/m)(N|gamma|^2)^{-1/m}`),
`Tr(P_I P_J) -> Gamma(1+1/m)|gamma|^{-2/m}N^{1-1/m}`. **The formula is false at `m = 1`**: the
induced volume on `V` contributes `1+|gamma|^2` and the constant is `(1+|gamma|^2)/|gamma|^2`
(verdict O2). Since the intersection multiplicity of two smooth curves with contact order `m` is
`m`, the exponent for `m >= 2` is `1 - 1/m`, a non-integer rational fixed by the multiplicity, not
the dimension. Near-failure of A3 is worse than failure: `J -> 0` inflates the constant and the
asymptotic regime only begins at `N ~ mu_cap` (N3, N6).

## Against the north star

**1 -- Problem: PARTIALLY MET.** Input as in D-input-model (`N` unary). **P0 (native):** estimate
`tau_N = Tr(P_I P_J)/M_N` to additive `eps` -- precise. **P1 (dimension):** decide
`dim(V ^ W) >= l` vs `<= l-1`. Not yet sufficient: recovering an integer exponent from
`tau_N` needs uniform lower-order control across the family, not just a per-instance `O(1/N)`, and
one fixed-degree Hilbert-function value does not determine dimension (in `P^2` at the stable
`N = 2`, a line and three noncollinear reduced points both have `HF = 3` but dimensions 1 and 0 --
verdict O6). **P2 (distance):** needs a closest-pair nondegeneracy (Morse-Bott) promise. **P3
(integration):** needs encoding, degree, norm and projective bihomogeneity promises for `g`.
Only P0 is fully specified.

**2 -- Classical baseline: NOT MET.** r0's K-IO2 squeeze is retracted (O6). What can honestly be
said: (i) `I_N + J_N` is the row span of the concatenated degree-`N` Macaulay matrices
(D-macaulay-matrix), so no elimination is avoided by the quantum route; (ii) numerical irreducible
decomposition [SVW, DOI 10.1137/S0036142900372549], the diagonal homotopy [SVW,
DOI 10.1137/S0036142903430463] and the trace test [SVW, DOI 10.1137/S0036142901397101] are the
relevant competitors **once witness sets for `V` and `W` are already supplied and the tracking is
well conditioned**; the cited papers do not establish a universal `deg V . deg W` path bound, exact
certification, or polynomial cost from sparse generators, and Lairez [DOI 10.1007/s10208-016-9319-7,
arXiv:1507.05485] proves average-case polynomial time for one approximate root in a specific model,
not per-path polynomial cost for every diagonal homotopy here. (iii) For P0 the comparator is
Hutch++ [arXiv:2010.09649]; see criterion 4. No adjudicated best classical algorithm for P1 is
established by this lane.

**3 -- Quantum algorithm: NOT MET.** Write `gamma_N = Delta_N/alpha_BE` (D-normalised-gap,
D-block-encoding-normalisation). A spectral filter `P_I` costs `O~(gamma_N^{-1} log(1/eps'))`
block-encoding uses (D-qsvt). The registered D-dqc1-style-estimate is
`O(eps^{-2})` repetitions on the maximally mixed valid-sector state, so estimating `tau_N` to
additive `eps` costs `O~(gamma_N^{-1} eps^{-2})` queries, times `poly(n, log N)` per query.
`O(eps^{-1})` requires a coherent purification/preparation and BQP-style amplitude estimation, which
is **not** the registered DQC1 procedure (verdict O5). Space `O(n log N)` qubits versus `M_N` words
is not by itself a separation (fact SP-0, PRD D15). There is no proved family with a complete
resource bound beating the best baseline, so this criterion is not met.

**4 -- Dequantization audit: NOT MET (redone at r1).** Low-rank dequantization does not apply
(`H_N` sparse and high rank, `rank P_I = HF(N)`; D-hardness-anchors). Single error model, as the
critic demands: `A = P_I P_J P_I >= 0`, `tau_N = Tr(A)/M_N`. **Classical:** Hutch++ gives relative
error `delta` in `O(1/delta)` applications of `A`; each application needs **three** projector
filters, each `O~(M_N s_row gamma_N^{-1})` flops by sparse Krylov. For additive `eps` in `tau_N`,
`delta = eps/tau_N`, i.e. `O(tau_N/eps)` applications, so
`O~(M_N s_row gamma_N^{-1} tau_N/eps)` flops. **Quantum (registered DQC1):**
`O~(gamma_N^{-1} eps^{-2})` queries. Ratio classical/quantum `= M_N s_row tau_N eps`. So the only
margin is the vector length `M_N` (times `s_row tau_N eps`), and it **shrinks as `eps` shrinks**,
because Hutch++ is `1/eps` where registered DQC1 sampling is `1/eps^2`; with BQP amplitude
estimation the ratio becomes `M_N s_row tau_N`, a clean vector-length margin. The margin is arm A's
for `HF/M_N` applied to a concatenated generator list, not a new one. A quantum advantage requires
simultaneously: efficient coherent valid-sector preparation, efficient sparse oracles,
inverse-polynomial `gamma_N`, inverse-polynomial required additive precision and signal, and no
structure-aware classical shortcut. No such family is proved here. The r0 statement that `tau_N` is
"always" or "never" exponentially small was wrong in both directions: N9 gives 0.214, 0.233, 0.246
at `n = 4, 8, 32` for orthogonal hyperplanes, while `tau_N = 7.110e-10` at `t = 0.6, N = 40` and
`1.657e-37` at `t = 0.3, N = 800` in the distance experiment, and `1.23e-6` at `codim = 16`.

**5 -- Heuristic hardware: PARTIAL.** With `rho_I = P_I/HF_I`, `rho_J = P_J/HF_J`, mode-wise beam
splitters followed by **total photon-number parity** estimate `Tr(rho_I rho_J)` with `O(eps^{-2})`
shots. Two honest qualifications (verdict O8): photon counting/parity is a **non-Gaussian
measurement**, and ground-space mixture preparation is an **explicit assumption**. For linear
subspaces the mixture is produced by a **passive-optics Haar twirl** (r0's "phase-randomised source"
is insufficient); at `n = 2, N = 1` the result is `(1+cos^2 t)/4`, an interferometric reading of the
angle between two projective lines and classically trivial. For the conic the state is the
`2N+1`-fold ferromagnetic ground manifold of the Law-Pu-Bigelow spin-mixing Hamiltonian (C-024,
DOI 10.1103/PhysRevLett.81.5257), giving an analogue reading of a Bezout constant times an angle
factor -- a demonstration, not a speedup, three modes being fixed `n` and classically polynomial by
C-099 [arXiv:2211.16998, DOI 10.22331/q-2023-11-28-1189].

**Verdict: 1/5** (criterion 1 partial, 5 partial; 2, 3, 4 not met), or **at most 2/5** if the
trivial linear-subspace demonstration takes full criterion-5 credit. Arm C has useful exact formulas
and a plausible clean-intersection dictionary, but no adjudicated quantum speedup and no completed
north-star hit.

## Killers

**K-IO1 (structural).** Under clean intersection with constant angle,
`Tr(P_I P_J) = J_0^{-1}HF_{R/(I+J)}(N)(1+O(1/N))` (asymptotic, not exact), and `I_N + J_N` is a
concatenation of Macaulay rows. Arm C therefore adds no new quantum primitive and one nuisance
parameter. What r0 additionally claimed -- that this yields a polynomial classical algorithm for the
dimension -- is retracted with K-IO2.

**K-IO2 -- RETRACTED at r1 (verdict O6, FATAL).** It asserted polynomial visibility iff
`codim = O(1)`, contradicting this lane's own N9, where visibility persists to `codim = O(log n)`;
with `c = O(log n)` equations the degree product can be `n^{O(log n)}`, quasipolynomial, so the
squeeze does not close. Its literature attribution was also too strong. Surviving statement: the
concatenation fact, and that diagonal homotopy is a relevant competitor under explicit
input-representation, conditioning, certification and average-case promises.

**K-IO3 (conditioning; the arm-C form of C-170/C-172).** The finite-`N` exponent estimator is
misreported until `N sin^2 t -> infinity`: at `mu_cap = 100` the local slope is 1.80 at `N = 32`,
1.54 at `N = 256`, 1.16 at `N = 1024`, truth 1 (N3, asserted); curved analogue N6. Every promise
making P1 solvable must bound an angle condition number.

**K-IO4 (kills C-085 as written).** At an order-`m >= 2` contact the exponent is `1 - 1/m` and
`Tr -> infinity` although `dim(V ^ W) = 0` and `HF_{R/(I+J)}(N) = m`. Off the clean locus the
observable reads a metric contact order, not an algebraic dimension.

**K-IO5 (weakened at r1, verdict O2).** For disjoint `V, W` the normalised signal is genuinely
exponentially small: `tau_N = 7.110e-10` at `d_0 = 0.6, N = 40`, and `1.657e-37` at `d_0 = 0.3,
N = 800`. But the r0 *necessity* argument was wrong twice: the bias is `-log(N+1)/(2N)`, negative,
and where the prefactor is known exactly (Clifford) it can simply be divided out at every `N`, so no
`N = Omega(eta^{-1}log(1/eta))` is forced. The 10% uncorrected-bias threshold is `N = 721`.

**K-IO6 (weakened at r1, verdict O5).** The Berezin-Toeplitz bias is `Theta(1/N)` with asymptotic
coefficient `~0.0314` (N12), so additive accuracy `eps` forces `N = Omega(1/eps)` and the
amplitude-estimation `1/eps` gain is consumed. It does **not** follow that the quantum cost is
`eps^{-(m+1)}`: that expression double-counted `alpha_BE`. With `gamma_N` counted once, the query
cost at `N = Theta(1/eps)` is `O~(gamma_N^{-1}eps^{-1})`, and for the conic
(`Delta_N = N+1`, `alpha_BE = O(N^2)`, `gamma_N^{-1} = O(N)`) that is `O(eps^{-2})` -- **parity**
with classical Monte Carlo's `O(eps^{-2})` samples (C-087), not a `eps^{-4}` disadvantage. No
advantage is demonstrated; no disadvantage is proved.

**K-IO7 (regime).** Everything computable here has `n <= 6`, inside the region C-099 says is
classically polynomial. The numerics validate geometry; they cannot exhibit an advantage.

**K-IO8 (hardware readout).** The SWAP test measures `Tr/(HF_I HF_J)`, smaller than `Tr/M_N` by
`M_N/(HF_I HF_J)` -- a factor `~n/4` for two hyperplanes, exponential at higher codimension (N9);
parity is non-Gaussian; and ground-space mixture preparation is assumed. Where preparation is easy
(linear `V`) the classical problem is trivial. K-QP8 in intersection clothing.

**K-IO9 (genericity).** For generic `I, J` the exponent is the expected dimension `k_1+k_2-n`, free
classically. The observable is informative only on the excess locus, where by K-IO3 angles are
typically small. The clean positive is that on the excess locus the observable is *correct*, with
both normal blocks present (N7a, N7b).

## Proposed definitions

MERGE PROPOSAL (`definitions/definitions.md`). Texts below are the r1 critic's adjudicated
rewordings, verbatim, with the verdict's inline LaTeX rendered in this memo's ASCII convention.

**D-intersection-overlap (ACCEPT).** `T_N(I,J) := Tr(P_{0,N}^{(I)}P_{0,N}^{(J)})`, `P_{0,N}` the
projector onto `ker H_N` (D-projectors), i.e. the Bergman projector of D-bergman-projector;
equivalently `||B_I^dag B_J||_F^2` for orthonormal ground-space bases, and `= Tr(P_I P_J P_I) >= 0`.
Three normalisations, all in use: `tau_N = T_N/M_N` (the D-dqc1-style-estimate quantity),
`T_N/sqrt(HF_I HF_J)`, `T_N/(HF_I HF_J) = Tr(rho_I rho_J)` (what a two-copy SWAP test measures).
Pitfalls: it is **not** `Tr(P_{I_N}P_{J_N}) = M_N - HF_I - HF_J + T_N = Theta(M_N)`; the seed's
Conjecture 8.10(a) and rows C-085, C-166, C-167 do not say which projector they mean, and only this
reading has the asserted geometric asymptotics -- those rows should be amended to cite this id
(folded in here from the rejected C-NEW-IO-PROJECTOR-AMBIGUITY row). The three normalisations differ
by factors exponential in codimension, so a signal-size statement must say which.

**D-clean-intersection (REWORD, verbatim).** "Smooth `V, W` in `CP^n` intersect cleanly along a
smooth pure-dimensional `Z = V ^ W` if `T_xZ = T_xV ^ T_xW` for every `x in Z`. Transverse
intersections are clean; clean intersections may have excess dimension."

**D-intersection-angle-condition-number (REWORD, verbatim).** "For a clean intersection, let
`A_x = T_xV (-) T_xZ` and `B_x = T_xW (-) T_xZ`. Define `J(x) = prod_i sin^2 theta_i(x)`, padding the
principal-angle list with `pi/2` when the dimensions differ, and `mu_cap = sup_Z J^{-1} < infinity`.
No universal crossover scale follows from this definition alone."

**D-bergman-frame-operator (REWORD, verbatim).** "Define
`S_V^{(N)} = int_V |e_p><e_p| dvol_V(p)`. Exactly, `ran S_V^{(N)} = (I(V)_N)^perp`. The claimed
operator-norm asymptotic `S_V^{(N)} = (pi/N)^k(P_{I(V),N} + O(N^{-1}))` is a separate
conjectural/theorem claim requiring a precise source; it is not part of the definition."

**D-normalised-toeplitz-operator (REWORD, verbatim).** "For `N >= r` and a projective bihomogeneous
symbol `g(z, conj z)` of bidegree `(r,r)`, define
`T~_g^{(N)} = ((N-r)!/N!) P_{0,N} :g(a^dag,a): P_{0,N}`. If `I` is radical, `N` is stable and
`p in V(I)`, its restricted coherent-state symbol is exactly `g(p, conj p)`." (Not an amendment to
D-toeplitz-operator: a distinct definition, per verdict O3.)

**D-contact-order (REWORD, verbatim).** "At a common point of smooth plane curves choose holomorphic
coordinates unitary for the Fubini-Study metric at the point and flatten `W` to `v = 0`. If `V` has
`v = gamma u^m + O(u^{m+1})`, `gamma != 0`, then `m` is the contact order and local intersection
multiplicity. `m = 1` is transverse; `m >= 2` is tangent."

## Proposed claim rows

MERGE PROPOSAL (`claims/CLAIMS.md`). Statements marked *verbatim* are the r1 critic's adjudicated
rewordings, copied unchanged. `where-tested` is
`checkers/explore/intersection_observables.py` by section letter.

**C-NEW-IO-LINEAR-EXACT** (new at r1, from verdict O1's opening identity).
- statement: For all `n >= 1`, all linear subspaces `U, W` of `C^{n+1}` with `dim U, dim W >= 1`,
  all `N >= 0`, and `r = min(dim U, dim W)` with `sigma_1 >= ... >= sigma_r >= 0` the cosines of the
  principal angles between `U` and `W`:
  `Tr(P_{Sym^N U} P_{Sym^N W}) = h_N(sigma_1^2, ..., sigma_r^2)`, `h_N` the complete homogeneous
  symmetric polynomial of degree `N`. Under D-intersection-overlap with `I = I(P(U))`,
  `J = I(P(W))` (linear ideals, `reg = 1`, so every `N >= 1` is stable),
  `T_N(I,J) = h_N(sigma^2)`.
- status: CONJECTURE (L1: an elementary proof is given here -- in principal-vector bases
  `<u_i, w_j> = sigma_i delta_ij`, so symmetrised monomial bases have overlap
  `prod_i sigma_i^{alpha_i}` diagonally in `alpha`, `|alpha| = N` -- but nothing enters PROVED
  without a verdict).
- depends-on: D-intersection-overlap, D-ground-space, D-symmetric-sector, C-026, C-028.
- where-proved: this memo, N11. where-tested: N11 (random subspaces in `C^4, C^5, C^6`, `N = 4..7`,
  worst relative discrepancy `< 1e-14`, mutation M-IO5); specialisations N1, N2, N4, N7, N9.
- north-star relevance: the lane's most defensible product; it makes every linear family exact and
  independent of Geometry 2.4.

**C-NEW-IO-CLEAN** -- status CONJECTURE, marked **HOLD (do not merge)** per the quantum-primitives
convention; the adjudication is "HOLD missing step".
- statement: For fixed homogeneous radical `I, J` in `C[z_0..z_n]` with `V = V(I)`, `W = V(J)`
  smooth and intersecting cleanly (D-clean-intersection) along `Z` of pure complex dimension `l`, as
  `N -> infinity` through the stable range,
  `T_N(I,J) = (N/pi)^l int_Z J(x)^{-1} dvol_Z(x) . (1 + O_{I,J}(N^{-1}))` in the convention
  `d = arccos|<p,q>|`, `J(x)` as in D-intersection-angle-condition-number.
- MISSING STEP (why HOLD): Geometry 2.4, the ambient Bergman-frame operator-norm estimate
  `S_V^{(N)} = (pi/N)^k(P_I + O(N^{-1}))`. Mean-eigenvalue flatness (2.2-2.3) does not imply it, and
  no ambient-coordinate statement for a subvariety was found that can be cited verbatim. The
  anti-diagonal normal block, the other half of verdict O1, IS supplied (Geometry 5.3-5.4) and
  tested (N7b).
- depends-on: C-026, C-028, C-079, D-intersection-overlap, D-clean-intersection,
  D-intersection-angle-condition-number, D-bergman-frame-operator,
  D-saturation-regularity-stable-range.
- where-proved: Geometry 1-6 modulo 2.4. where-tested: N1, N2, N5, N6, N7a, N7b, N10.

**C-NEW-IO-SUM-IDEAL** -- CONJECTURE; statement *verbatim*:
"Assume C-NEW-IO-CLEAN. If `J(x) = J_0 > 0` on `Z`, then, as `N -> infinity`,
`T_N(I,J) = J_0^{-1} HF_{R/(I+J)}(N)(1 + O_{I,J}(N^{-1}))`. Moreover `I_N + J_N` is the row span of
the concatenated degree-`N` Macaulay matrices. This identity alone does not give the dimension from
one Hilbert-function value or establish a polynomial classical algorithm."
- depends-on: C-NEW-IO-CLEAN (inherits its HOLD), D-hilbert-function, D-macaulay-matrix,
  D-normalised-hilbert-function. where-proved: Corollary 6a. where-tested: N1, N2, N5, N6, N7.
- north-star relevance: negative -- reduces arm C to arm A on a concatenated generator list. Traps
  checked: "changing the output", "hiding an elimination".

**C-NEW-IO-TANGENCY** -- CONJECTURE; statement *verbatim*:
"Let `I = I(V)` and `J = I(W)` be homogeneous radical ideals of smooth plane curves meeting only at
`x`, and take `N` in the stable range. If their contact order is `m >= 2` and in unitary
Fubini-Study normal coordinates their normal separation is `gamma u^m + O(u^{m+1})`, then
`T_N(I,J) = Gamma(1 + 1/m)|gamma|^{-2/m}N^{1-1/m}(1 + o(1))`."
- depends-on: C-026, C-028, C-079, D-contact-order, D-intersection-overlap,
  D-bergman-frame-operator, D-saturation-regularity-stable-range. NOT on C-NEW-IO-CLEAN: tangency is
  expressly outside its hypotheses (verdict O7). Its derivation nevertheless shares the Geometry 2.4
  leaf, so it is conjectural for the same reason.
- where-proved: Geometry, "what fails without A3". where-tested: N5 (`m = 2`, `gamma = 1`: exponent
  0.42 -> 1/2, constant 0.8915 versus 0.886227; mutation M-IO1).
- north-star relevance: refutes C-085; shows the observable is metric, not algebraic, off the clean
  locus.

**C-NEW-IO-DISTANCE** -- CONJECTURE; statement *verbatim*:
"Let `V, W` be disjoint smooth projective varieties in the stable range. Assume the closest-pair set
`S subset V x W` is a compact smooth real Morse-Bott minimum manifold of real dimension `r`, with
nondegenerate normal Hessian. Then `T_N(I,J) = C N^{r/2}cos^{2N}(d_0)(1 + O(N^{-1}))`, `C > 0`, and
`-log T_N/(2N) = log sec d_0 - r log N/(4N) + O(N^{-1})`."
- Exactly solvable instances: the Clifford pair (`r = 2`, `T_N = (N+1)cos^{2N}t` for every `N`) and
  the generic skew pair (`r = 0`, `T_N = h_N(sigma_1^2, sigma_2^2)` by C-NEW-IO-LINEAR-EXACT).
- depends-on: C-167, C-NEW-IO-LINEAR-EXACT, D-intersection-overlap, D-coherent-state,
  D-bergman-frame-operator. where-proved: Corollary 6c. where-tested: N4.

**C-NEW-IO-DISTANCE-COST** -- **REFUTED** (adjudication "REFUTE with counterexample").
- refuted statement (r0): additive estimation of `d_FS` forces
  `N = Omega(eta^{-1}log(1/eta))` and hence `exp(Omega(eta^{-1}log(1/eta)))` rounds.
- counterexample (critic, verbatim): "For the Clifford pair the exact known factor `N+1` can be
  divided out, so its logarithmic bias does not force `N = Omega(eta^{-1}log(1/eta))`. The required
  additive precision also omits the factor `C N^{r/2}`."
- surviving statement: the normalised signal for disjoint varieties is exponentially small in `N` --
  `tau_N = 7.110e-10` at `d_0 = 0.6, N = 40` and `1.657e-37` at `d_0 = 0.3, N = 800` -- so an
  additive-precision estimator of `tau_N` at fixed `eps` cannot see it at those `N`; the
  10% uncorrected-bias threshold is `N = 721`. No necessity claim is made.
- depends-on: C-NEW-IO-DISTANCE, C-167, D-dqc1-style-estimate. where-tested: N4.

**C-NEW-IO-TOEPLITZ** -- CONJECTURE; statement *verbatim*:
"For the conic `z_0z_1 = z_2^2`, `N >= r`, and `g in {|z_2|^2, |z_2|^4}`, define
`T~_g^{(N)} = ((N-r)!/N!)P_0 :g(a^dag,a): P_0`. Then the computed traces are consistent with
`Tr(T~_g^{(N)})/HF(N) = vol(V)^{-1} int_V g dvol + b_g/N + O(N^{-2})`. For `g = |z_2|^2`, the exact
limit is `-1/6 + 2 sqrt(3) pi/27`."
- r1 addition: at `N = 1200` (N12) the `r = 1` coefficient `b_g` is about **0.03144**; the r0 value
  0.03275 was a fit over `N <= 60` only.
- depends-on: C-079, C-026, D-normalised-toeplitz-operator, D-bergman-frame-operator,
  D-hilbert-function. NOT on C-168/C-086, which become REFUTED (verdict O7).
- where-proved: Geometry step 2 applied to `Tr(P_0 X)` for `X` of restricted symbol `g`.
  where-tested: N8, N12 (mutation M-IO2).
- north-star relevance: the surviving statement for C-086/C-168.

**C-NEW-IO-TOEPLITZ-COST** -- **REFUTED** (adjudication "REFUTE with counterexample").
- refuted statement (r0): the quantum cost is
  `Omega(poly(n) eps^{-(m+1)}/(Delta_N/alpha_BE))`.
- counterexample (critic, verbatim): "It double-counts `alpha_BE` after already dividing by
  `Delta/alpha_BE`. The conic has `Delta_N = N+1`, contradicting the claimed degree-only exponent."
  Explicitly: `gamma_N^{-1} = O(N)` for the conic, so at `N = Theta(1/eps)` the query cost is
  `O~(gamma_N^{-1}eps^{-1}) = O(eps^{-2})`, parity with classical Monte Carlo, not `eps^{-4}`.
- surviving statement: the `Theta(1/N)` Berezin-Toeplitz bias forces `N = Omega(1/eps)`, which
  consumes the amplitude-estimation `1/eps` gain; no quantum advantage for integration over a
  variety is demonstrated, and none is refuted.
- depends-on: C-NEW-IO-TOEPLITZ, C-087, D-input-model, D-block-encoding-normalisation,
  D-normalised-gap, D-condition-number. where-tested: N8, N12.

**C-NEW-IO-SIGNAL** -- CONJECTURE; statement *verbatim*:
"For `n >= 2`, `N >= 0`, and two hyperplanes at angle `t`,
`T_N = sum_{a=0}^N cos^{2a}t binom(N-a+n-2, n-2)`. At `t = pi/2, N = n`,
`T_N/M_N = n(n-1)/(2n(2n-1))` and `T_N/HF = (n-1)/(2n-1)`. For coordinate ideals on disjoint blocks
of size `k`, `2k <= n`, `T_N/M_N = binom(N+n-2k, n-2k)/binom(N+n, n)`; when `N = n` and `k = o(n)`,
this is `4^{-k}(1 + O(k^2/n))`, hence inverse-polynomial exactly when `k = O(log n)`."
- depends-on: C-NEW-IO-LINEAR-EXACT, D-intersection-overlap, D-normalised-hilbert-function,
  D-dqc1-style-estimate. where-proved: elementary monomial count, and a specialisation of
  C-NEW-IO-LINEAR-EXACT with `sigma = (1^{n-1}, cos t)`. where-tested: N9.
- north-star relevance: positive, and it is what retracts K-IO2: visibility survives to
  `codim(V ^ W) = O(log n)`.

**C-NEW-IO-CROSSOVER** -- CONJECTURE; statement *verbatim*:
"For `0 < t <= pi/2`, two hyperplanes in `P^3` have `T_N = sum_{a=0}^N cos^{2a}t (N+1-a)`. In the
double-scaling regimes `1 << N << csc^2 t` and `N >> csc^2 t`, its local log-log slope tends
respectively to `2` and `1`. Thus this particular finite-`N` exponent estimator requires
`N sin^2 t -> infinity`."
- depends-on: C-NEW-IO-LINEAR-EXACT, D-intersection-angle-condition-number, C-170, C-172. NOT on
  C-NEW-IO-CLEAN (verdict O7: no dependency on a HOLD row; the closed form is exact and linear).
- where-proved: exact closed form. where-tested: N3 (asserted slopes; mutation M-IO4), N6.

**C-NEW-IO-DEQUANT** -- CONJECTURE; statement *verbatim*:
"For `A = P_I P_J P_I >= 0`, Hutch++ gives relative error `delta` using `O(delta^{-1})` applications
of `A`, each requiring three approximate projector filters. For additive error `eps` in
`tau_N = Tr(A)/M_N`, take `delta = eps/tau_N`. Direct DQC1-style sampling costs `O(eps^{-2})`
controlled-filter uses; `O(eps^{-1})` requires a coherent purification and BQP amplitude estimation.
A quantum advantage requires efficient oracles, inverse-polynomial normalized gaps and signal, and a
per-filter advantage over length-`M_N` Krylov vectors; none is proved here."
- depends-on: D-intersection-overlap, D-dqc1-style-estimate, D-qsvt,
  D-block-encoding-normalisation, D-normalised-gap, D-hardness-anchors. where-proved: criterion 4.
  where-tested: none (a cost statement).

**C-NEW-IO-SWAP-HARDWARE** -- CONJECTURE; statement *verbatim*:
"Given preparations of `rho_I = P_I/HF_I` and `rho_J = P_J/HF_J`, mode-wise beam splitters followed
by total photon-number parity estimate `Tr(rho_I rho_J)` with `O(eps^{-2})` shots. Photon
counting/parity is a non-Gaussian measurement, and ground-space mixture preparation is an explicit
assumption. For linear subspaces the mixture can be produced by a passive-optics Haar twirl; at
`n = 2, N = 1` the result is `(1 + cos^2 t)/4`."
- depends-on: C-024, D-spin-mixing-hamiltonian, D-intersection-overlap, D-symmetric-sector,
  C-NEW-IO-LINEAR-EXACT. where-proved: criterion 5. where-tested: N6 supplies the predicted constant
  for the two-conic version; the interferometer is not simulated.

**Deleted at r1** (adjudication REJECT): **C-NEW-IO-WITNESS-BASELINE** (the cited results do not
establish polynomial per-path cost, exact certification, or cheap witness-set construction for every
quantified input) and **C-NEW-IO-PROJECTOR-AMBIGUITY** (a notation correction, not a conjecture;
folded into D-intersection-overlap and the C-085/C-166/C-167 amendments below).

## Lockstep notes

- **C-085 -> REFUTED.** Counterexample: the smooth conic and its tangent line have
  `dim(V ^ W) = 0` but `T_N ~ Gamma(3/2)N^{1/2}`. Surviving statement: for fixed homogeneous radical
  ideals whose smooth varieties intersect cleanly, **and after the Bergman-frame leaf is proved**,
  the exponent is `dim(V ^ W)` (C-NEW-IO-CLEAN); disjoint varieties require a separate Morse-Bott
  distance statement (C-NEW-IO-DISTANCE).
- **C-166 stays CONJECTURE.** Its transversal hypothesis survives every exact computation and must
  **not** be silently replaced by the stronger clean-intersection claim; C-NEW-IO-CLEAN is a
  separate row. Amend the constant to `c = pi^{-l} int_Z prod_i sin^{-2}theta_i dvol_Z`; add N1, N2,
  N5, N6 as `where-tested`; define `P_I = P_{0,N}^{(I)}` via D-intersection-overlap; and **remove
  its dependency on the newly REFUTED C-085**.
- **C-167 stays CONJECTURE** for its mathematical content, with the polynomial prefactor supplied by
  C-NEW-IO-DISTANCE under a Morse-Bott hypothesis and the bias sign corrected. Its dependent cost
  claim is REFUTED (C-NEW-IO-DISTANCE-COST). `where-tested`: N4.
- **C-168 -> REFUTED, and C-086 -> REFUTED** (this is the r0 memo's largest error: r0 wrote "status
  unchanged" and "CONFIRMED"). Under the registered D-toeplitz-operator, `g = |z_2|^2` gives
  `T_g = P_0 n_2 P_0` and `Tr(P_0T_g)/HF(N) ~ N <|z_2|^2>_V`, which diverges, so both rows are
  dimensionally false as written. Surviving statement for both: with the degree-normalised operator
  `T~_g^{(N)}` of D-normalised-toeplitz-operator, for fixed smooth radical `V`, stable
  `N -> infinity` and bihomogeneous projective `g`,
  `Tr(T~_g^{(N)})/HF(N) = vol(V)^{-1} int_V g dvol_V + O(N^{-1})` (C-NEW-IO-TOEPLITZ). The `1/N`
  coefficient reported at r0 (0.03275) was a fit over `N <= 60`; the asymptotic value is `~0.03144`
  (N12).
- **C-079** gains `where-tested`: the Bergman-projector reading is exercised throughout; N10
  measures the frame spectrum and is evidence for, not proof of, Geometry 2.4.
- **C-087 depends on C-085** and must be rewired by the orchestrator when C-085 becomes REFUTED
  (verdict O7). This lane does not edit `claims/CLAIMS.md`.
- **PRD §4 arm C**: the seed's "suggested next step 3" has been run. The arm's conditional is now
  MET for the *linear* families (exactly, C-NEW-IO-LINEAR-EXACT) and NOT met in general (Geometry
  2.4). r0's claim that K-IO2 closes the arm is retracted; the arm is scored 1/5 on evidence, not
  closed by a baseline argument.
- **checkers/MUTATIONS.md** needs five new entries, M-IO1..M-IO5; that file is outside this lane's
  writable set, so the registration text is printed by the script's `mutation_selftest()`.

## Questions for TJO

1. **Fund Geometry step 2.4?** It is the single unproved leaf under C-NEW-IO-CLEAN, C-NEW-IO-SUM-IDEAL
   and C-NEW-IO-TANGENCY, and under half of seed §5.7. The linear half of the arm (N11) is exact and
   needs none of it. One analytic day on the ambient-coordinate Bergman-frame estimate, or leave the
   arm at "exact for linear, conjectural for curved"?
2. **Is C-NEW-IO-LINEAR-EXACT a product?** (PRD §7 Q4.) It is exact, elementary, and it subsumes six
   of this lane's families -- but it is a statement about symmetric powers of subspaces, not a
   speedup.
3. **Ratify the two definition changes** (D-intersection-overlap for the projector notation;
   D-normalised-toeplitz-operator as a *distinct* definition) before further arm-C work: C-085,
   C-166, C-167 are not well-posed without the first, and C-086/C-168 are false without the second.
4. **Arm C's ranking.** r0 recommended demoting arm C below arm B on the strength of K-IO2, which is
   now retracted. The honest position is 1/5 on evidence with no baseline argument closing it. Demote
   on the score, or leave the ranking to the next critic cycle?
5. **The analogue experiment** (two spinor condensates, N6) still stands, with the r1 corrections
   that parity is non-Gaussian and that the linear case needs a Haar twirl. Worth writing up
   separately?

## Citation index

Resolved against the arXiv API, doi.org or api.crossref.org and read: arXiv:2010.09649 (Hutch++,
Meyer-Musco-Musco-Woodruff, `(1+-eps)` for PSD `A` in `O(1/eps)` matrix-vector products);
DOI 10.1137/S0036142900372549, DOI 10.1137/S0036142901397101, DOI 10.1137/S0036142903430463
(Sommese-Verschelde-Wampler: numerical irreducible decomposition, trace test, diagonal homotopy --
cited at r1 only for what they actually prove, per verdict O6);
DOI 10.1007/s10208-016-9319-7 = arXiv:1507.05485 (Lairez, average-case polynomial time for ONE
approximate root, not per-path cost); arXiv:1711.10911 (Breiding-Timme, HomotopyContinuation.jl);
DOI 10.4310/jdg/1214445039 (Tian) and arXiv:math-ph/0002009 (Zelditch);
arXiv:hep-th/9309134 (Bordemann-Meinrenken-Schlichenmaier); arXiv:2211.16998 =
DOI 10.22331/q-2023-11-28-1189 (Anschuetz-Bauer-Kiani-Lloyd, C-099).
DOI 10.1103/PhysRevLett.81.5257 (Law-Pu-Bigelow, C-024) is quoted from D-spin-mixing-hamiltonian.

Not fetched, background only: Bott's clean-intersection condition [UNVERIFIED]; Catlin's and
Zelditch's off-diagonal Bergman expansions for submanifolds [UNVERIFIED]; the many-mode
Hong-Ou-Mandel SWAP test [UNVERIFIED].

## Repair r1 response

Verdict `verdicts/intersection-observables-r1.md`, FAIL(O1-O8). Every objection is dispositioned;
none is silently ignored. Files touched: this memo and
`checkers/explore/intersection_observables.py` only.

| objection | severity | disposition | exact location | note |
|---|---|---|---|---|
| O1a anti-diagonal normal block omitted | MAJOR | FIXED | Geometry 5.3-5.4; N7b | The `T_xZ` Gaussian `(pi/N)^l` is now derived alongside the transverse `(pi/N)^{k1+k2-2l}/J`; a new angle-carrying excess family in `P^4` (`Tr/N -> 1/sin^2 t` = 1.6297, 6.5943) separates the two blocks experimentally. |
| O1b Bergman-frame operator-norm estimate unproved | MAJOR | RESIDUE | Geometry 2.4; C-NEW-IO-CLEAN | Named as the single missing step; mean flatness explicitly distinguished from operator-norm flatness; CLEAN is CONJECTURE marked HOLD (do not merge). |
| O1c "theorem-grade"; "saturating" generic skew pair | MAJOR | FIXED | Bottom line 2, 8; N4 | "Three theorems" removed (L1). The generic skew ratio is not saturating: exact limit `sigma_1^2/(sigma_1^2-sigma_2^2) = 10.9917866070`, 10.99107 at `N = 100`. |
| O2a tangency false at `m = 1` | MAJOR | FIXED | Geometry "what fails"; C-NEW-IO-TANGENCY | Restricted to `m >= 2` verbatim; the `m = 1` constant `(1+|gamma|^2)/|gamma|^2` is recorded. |
| O2b distance law needs Morse-Bott | MAJOR | FIXED | Corollary 6c; C-NEW-IO-DISTANCE | `dim_C S` replaced by real Morse-Bott dimension `r`, prefactor `N^{r/2}`, verbatim. |
| O2c bias sign misstated | MAJOR | FIXED | Bottom line 7; N4; K-IO5 | The bias is `-log(N+1)/(2N)`: the estimator sits BELOW `log sec d_0`. |
| O2d `N = Omega(eta^{-1}log(1/eta))` not forced | MAJOR | RETRACTED | C-NEW-IO-DISTANCE-COST | Row REFUTED with the critic's counterexample; surviving statement keeps only the exponentially small signal (`tau_N = 1.657e-37` at `d_0=0.3, N=800`). |
| O3a C-086/C-168 refuted, not confirmed | **FATAL** | FIXED | Bottom line 3; lockstep; N8 | Both rows proposed REFUTED. Stated exactly which normalisation restores consistency: `T~_g^{(N)} = ((N-r)!/N!)P_0 :g: P_0`, `N >= r`, bihomogeneous `g`, symbol exact on `p in V`. |
| O3b `1/N` coefficient is a finite-range fit | **FATAL** | FIXED | N12; section K | New exact 1-D kernel recurrence, no SVD, to `N = 1200`: coefficient `~0.03144`, not 0.03275. Values reproduce the critic's table digit for digit. |
| O4a checker not red for the ordering claim | MAJOR | FIXED | section K; `pred_toeplitz_ordering` | Intercept pinned to the exact `-1/6+2 sqrt(3) pi/27`; coefficient must land in `[0.030,0.034]`. Anti-normal `n_2 -> n_2+1` shifts it by exactly `+1` and is rejected. |
| O4b N6 clamp `min(Tr/limit,1)` | MAJOR | FIXED | section E; M-IO3 footnote | Clamp removed, two-sided tolerance; the self-test shows the clamped form accepts a halved constant while the repaired form rejects it. |
| O4c no mutations; overstated terminal claim | MAJOR | FIXED / RESIDUE | `mutation_selftest`; `main` | Five mutations M-IO1..M-IO5 run in process (the critic's sandbox was read-only) and must all be caught; terminal message now lists exactly which quantities are asserted. RESIDUE: `checkers/MUTATIONS.md` is outside this lane's writable files, so the registration text is printed by the script. |
| O4d slopes/crossover unasserted | MAJOR | FIXED | section C | Asserted at `mu_cap = 100.3`: slope(256) > 1.4, slope(1024) < 1.3; M-IO4 moves the angle and is caught. |
| O5a mixed relative/additive error models | **FATAL** | FIXED | criterion 4; C-NEW-IO-DEQUANT | Single model: Hutch++ relative `delta = eps/tau_N`, DQC1 additive `eps`; ratio classical/quantum `= M_N s_row tau_N eps`. |
| O5b two filters, not three | **FATAL** | FIXED | criterion 4; C-NEW-IO-DEQUANT | Three projector filters per application of `A = P_I P_J P_I`. |
| O5c DQC1 `eps^{-2}` vs BQP `eps^{-1}` | **FATAL** | FIXED | criterion 3, 4 | Amplitude estimation is flagged as requiring coherent purification, i.e. not the registered D-dqc1-style-estimate. |
| O5d `alpha_BE` double-counted; conic counterexample | **FATAL** | REFUTED | C-NEW-IO-TOEPLITZ-COST; K-IO6 | Row REFUTED. With `gamma_N` counted once and `gamma_N^{-1} = O(N)` for the conic, the cost at `N = Theta(1/eps)` is `O(eps^{-2})` -- parity with classical Monte Carlo, not `eps^{-4}`. |
| O5e signal "always"/"never" exponentially small | **FATAL** | FIXED | criterion 4; K-IO5 | Both regimes now quoted with numbers from N9 and N4. |
| O6a K-IO2 contradicts N9 | **FATAL** | RETRACTED | K-IO2; bottom line 5; N9 | Visibility to `codim = O(log n)` adopted (`4^{-k}(1+O(k^2/n))`); the squeeze does not close, `n^{O(log n)}` being quasipolynomial. |
| O6b literature over-attributed | **FATAL** | RETRACTED | criterion 2; deleted row | C-NEW-IO-WITNESS-BASELINE deleted; SVW and Lairez cited only for what they prove. |
| O6c one HF value does not give dimension | **FATAL** | FIXED | criterion 1 | The line-versus-three-points counterexample at `N = 2` in `P^2` is recorded. |
| O6d SUM-IDEAL "exact in every case" | **FATAL** | DOWNGRADED | Corollary 6a; C-NEW-IO-SUM-IDEAL | Asymptotic, not exact; the two numerical counterexamples are quoted. |
| O7a rows depend on newly REFUTED rows | MAJOR | FIXED | rows; lockstep | TANGENCY no longer depends on CLEAN; TOEPLITZ no longer on C-168; CROSSOVER on LINEAR-EXACT rather than the HOLD row; C-166's dependency on C-085 removed in lockstep. |
| O7b C-087 depends on C-085 | MAJOR | RESIDUE | lockstep | Flagged for the orchestrator: `claims/CLAIMS.md` is outside this lane's writable files. |
| O7c quantifier defects in eight rows | MAJOR | FIXED | rows | Every row carries the critic's verbatim quantifiers (`N -> infinity` for fixed `I,J`; `N >= r`; `n >= 2`, `2k <= n`; `0 < t <= pi/2`; Morse-Bott; radical + stable range). |
| O7d PROJECTOR-AMBIGUITY is not a conjecture | MAJOR | FIXED | deleted row; D-intersection-overlap | Deleted; folded into the definition and the C-085/C-166/C-167 amendments. |
| O8a score overstated | MAJOR | DOWNGRADED | criterion verdict | 2/5 -> **1/5** (at most 2/5 if the trivial linear demo takes full criterion-5 credit); criteria 2, 3, 4 marked NOT MET. |
| O8b "three theorems" violates L1 | MAJOR | FIXED | bottom line 8; lockstep | Replaced by "one exact identity, one conjectural asymptotic with a named missing step, exact closed forms, negative evidence". |
| O8c C-168 lockstep substantively wrong | MAJOR | FIXED | lockstep | Rewritten as REFUTED with the surviving statement; this was r0's largest single error. |
| O8d criterion 5 overstated | MAJOR | FIXED | criterion 5; C-NEW-IO-SWAP-HARDWARE | Parity is non-Gaussian; preparation is an explicit assumption; "phase-randomised source" replaced by a passive-optics Haar twirl, verbatim. |

**Rows after repair: 12 (CONJECTURE 9, REFUTED 2, HOLD 1, deleted 2).** The HOLD row is
C-NEW-IO-CLEAN (status CONJECTURE, marked "do not merge" per the quantum-primitives convention;
HOLD is not an L1 status); C-NEW-IO-SUM-IDEAL assumes it and inherits the hold. The two REFUTED rows
are C-NEW-IO-DISTANCE-COST and C-NEW-IO-TOEPLITZ-COST, each naming the critic's counterexample and a
surviving statement. The two deleted rows are C-NEW-IO-WITNESS-BASELINE and
C-NEW-IO-PROJECTOR-AMBIGUITY. One row is new at r1: C-NEW-IO-LINEAR-EXACT. Separately, the lockstep
section proposes REFUTED for the existing rows C-085, C-086 and C-168, and amendments to C-166,
C-167, C-079 and (for the orchestrator) C-087.

**Residues, all outside this lane's writable files:** registration of M-IO1..M-IO5 in
`checkers/MUTATIONS.md`; the C-087 dependency rewire in `claims/CLAIMS.md`; and the one
mathematical residue, Geometry 2.4.
