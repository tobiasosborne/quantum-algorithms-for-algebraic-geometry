# Intersection and integration observables (arm C)

Lane `briefs/lane-intersection-observables.md`, PRD §4 arm C, 2026-09-03. Scouting only; nothing
ratcheted; every proposed row is CONJECTURE or REFUTED per L1. Script
`checkers/explore/intersection_observables.py` (`timeout 900`, exit 0).

Conventions C1-C12 binding; objects cited, never redefined: D-polynomial-ring, D-fock-space,
D-fock-basis, D-hamiltonian, D-ground-space, D-inverse-system, D-projectors, D-coherent-state,
D-bergman-projector, D-toeplitz-operator, D-hilbert-function, D-normalised-hilbert-function,
D-saturation-regularity-stable-range, D-macaulay-matrix, D-input-model, D-qsvt,
D-dqc1-style-estimate, D-block-encoding-normalisation, D-condition-number, D-hardness-anchors,
D-spin-mixing-hamiltonian. **Departure from C5**, as in the whole checker suite: generators are as
written, not unit Bombieri-Weyl; nothing depends on it, every quantity being a projector overlap, a
Hilbert-function count or a ratio (C-002, D-norm-comparison).

**Notation fixed here.** `P_I` is the projector onto `ker H_N^{(I)} = (I_N)^perp`, the Bergman
projector of D-bergman-projector -- *not* the projector onto `I_N`, which D-projectors calls
`P_{I_N}`. Conjecture 8.10(a) never says which; under the second reading
`Tr(P_{I_N}P_{J_N}) = M_N - HF_I - HF_J + Tr(P_I P_J) = Theta(M_N)`, with no geometry.
Metric: `d(p,q) = arccos|<p,q>|` (diameter `pi/2`), so `vol(CP^n) = pi^n/n!`,
`vol(V) = deg(V)pi^k/k!`, `|<e_p,e_q>|^2 = cos^{2N}d(p,q)` for `e_p = (p.z)^N/sqrt(N!)`.

## Bottom line

1. **The seed's law is right under a hypothesis the seed does not state.** For radical `I, J`,
   `V, W` smooth, `N` stable, and the intersection **clean** (Bott: `T_xV ^ T_xW = T_xZ`,
   `Z = V ^ W`): `Tr(P_I P_J) = (N/pi)^l int_Z J(x)^{-1} dvol_Z (1 + O(1/N))`, `l = dim Z`,
   `J(x) = prod_i sin^2 theta_i(x)` over the principal angles between the tangent spaces modulo
   `T_xZ`. Clean, not transversal: **excess** intersections are covered, and there the observable
   reports the ACTUAL dimension (N7: two planes in `P^4`, expected 0, actual 1, `Tr = N+1` exactly).
2. **C-085 is REFUTED as written** (it carries no transversality hypothesis). At a contact of order
   `m` between smooth plane curves the exponent is `1 - 1/m`, not `dim(V ^ W) = 0`, and
   `Tr -> infinity`. Measured: conic and its tangent line, exponent 0.42 at `N = 60` rising to 1/2,
   constant 0.8915 against the predicted `Gamma(3/2) = 0.886227`. C-166, which does say
   "transversal", survives and is *strengthened* (clean is weaker), with its constant made explicit.
3. **The observable is arm A's Hilbert function of `I + J` inflated by a metric factor:**
   `Tr(P_I P_J) = HF_{R/(I+J)}(N)/J . (1 + O(1/N))` for constant `J`. Since `I_N + J_N` is the row
   span of the *concatenated* Macaulay matrices, "estimating `dim(V ^ W)` without forming `I + J`"
   saves nothing. Arm C adds no new quantum primitive, no new hardness anchor, one nuisance
   parameter (K-IO1).
4. **The visible regime is the classically easy regime** (K-IO2, decisive): the signal is
   polynomially visible iff `codim(V ^ W) = O(1)`; `N` unary bounds `reg`, which for complete
   intersections bounds `deg V . deg W`; and `deg V . deg W = poly(n)` is exactly when the
   Sommese-Verschelde-Wampler diagonal homotopy returns the exact integer `dim(V ^ W)` in `poly(n)`.
5. **C-167 (Fubini-Study distance): true, dead as an algorithm.** For the equidistant "Clifford" skew
   pair in `P^3` the closed form is exact, `Tr = (N+1)cos^{2N}(d_FS)`, so `-(1/2N)log Tr` carries a
   bias `+log(N+1)/(2N)`. At `d_FS = 0.3, N = 40` the bias (0.0464) exceeds the signal (0.0457); 10%
   relative accuracy needs `N ~ 800`, where `Tr ~ 1e-29`.
6. **C-168 (Toeplitz integration): CONFIRMED as mathematics, killed as a speedup.** With the degree
   normalisation this lane adds, the extrapolated averages match independent quadrature to 1.7e-5 and
   3.5e-6 on the conic. But the bias is `Theta(1/N)`, so `eps` forces `N = Omega(1/eps)` and every
   quantum cost is `poly(N)`, against C-087's `O(1/eps^2)` classical samples with no `N`.
7. **One genuine positive.** `Tr/M_N` is *not* automatically exponentially small: two orthogonal
   hyperplanes in `P^n` at `N = n` give `Tr/M_N -> 1/4`, `Tr/sqrt(HF_I HF_J) -> 1/2`; applications
   caution 1 bites through `codim(V ^ W)`, not through `n`. **Score 2/5** (criteria 1 and 5 only):
   three theorems and four negative algorithmic results, not a speedup (PRD §7 Q4).

## Numerics

Regenerate with `timeout 900 python3 checkers/explore/intersection_observables.py` (exit 0). Every
closed form was checked against an independent SVD computation of `ker H_N` at small `N`; the script
exits 1 on disagreement. `M_N = dim R_N`, `l = dim(V ^ W)`, `J = prod_i sin^2 theta_i`,
`mu_cap = sup_Z J^{-1}`.

**N1. Two lines in `P^2`, `l = 0`, transversal (section A).** `I = (z_0)`,
`J = (cos(t)z_0 + sin(t)z_1)`. Closed form found here, SVD-verified to 8 digits at `N <= 16`:
`Tr = sum_{a=0}^{N} cos^{2a}(t) -> 1/sin^2 t = 1/J`. The `J` computed independently from the tangent
spaces matches `sin^2 t` to 1e-9. So **C-166's unspecified "combination of degrees and angle
factors" is exactly `1/J`**.

| `t` | `1/J` | `Tr(N=8)` | `Tr(N=16)` | `Tr(N=64)` | `Tr/M_N`(64) | `Tr/(HF_I HF_J)`(64) |
|---|---|---|---|---|---|---|
| `pi/2` | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 4.66e-4 | 2.37e-4 |
| 1.0 | 1.412283 | 1.412261 | 1.412283 | 1.412283 | 6.58e-4 | 3.34e-4 |
| 0.4 | 6.594277 | 5.093355 | 6.191586 | 6.594127 | 3.07e-3 | 1.56e-3 |

**N2. Two planes in `P^3` meeting in a line, `l = 1` (section C).** `I = (z_0)`,
`J = (c z_0 + s z_1)`; closed form `Tr = sum_a c^{2a}(N+1-a) = (N+1)/s^2 - c^2/s^4 + O(c^{2N})`
(SVD-verified to 8 digits, `N <= 12`), against the prediction `Tr ~ (N/pi)vol(Z)/J = N/sin^2 t`
with `Z = P^1`, `vol(Z) = pi`. `Tr/N` at `N = 128` is 1.0078, 1.9441, 10.605 for
`t = pi/2, 0.8, 0.3` against `1/J` = 1.0000, 1.9433, 11.4505; loglog slopes 0.984, 0.999, 1.178.

**N3. The crossover -- killer K-IO3 (section C).** Local exponent `d log Tr/d log N`, same family.
Truth is 1; the value 2 is what `V = W` gives.

| `t` | `mu_cap` | `N=16` | `N=32` | `N=64` | `N=128` | `N=256` | `N=1024` | `N=4096` |
|---|---|---|---|---|---|---|---|---|
| 0.500 | 4.4 | 1.198 | 1.115 | 1.056 | 1.027 | 1.013 | 1.003 | 1.001 |
| 0.100 | 100.3 | 1.728 | 1.801 | 1.793 | 1.705 | 1.537 | 1.160 | 1.036 |
| 0.020 | 2500.3 | 1.764 | 1.871 | 1.929 | 1.955 | 1.959 | 1.902 | 1.678 |

The exponent is misreported until `N >~ 10 mu_cap`.

**N4. Two skew lines in `P^3`, `V ^ W = {}` (section B).** Clifford pair `L_1 = span(e_0,e_1)`,
`L_2 = span(c e_0 + s e_2, c e_1 + s e_3)`: every point of `L_2` at Fubini-Study distance `t` from
`L_1`. Exact closed form found here, SVD-verified to 10 digits at `N <= 12`:
**`Tr = (N+1)cos^{2N}(t)`**, so the bias in `-(1/2N)log Tr` is exactly `+log(N+1)/(2N)`.

| `d_0 = t` | `log sec d_0` | `-(1/2N)log Tr`, `N=8` | `N=20` | `N=40` | `Tr(40)` | `Tr/M_N(40)` |
|---|---|---|---|---|---|---|
| 0.6 | 0.191965 | 0.054639 | 0.115852 | 0.145546 | 8.77e-6 | 7.11e-10 |
| 0.3 | 0.045692 | -0.091635 | -0.030421 | -0.000728 | 1.060 | 8.59e-5 |

Generic skew pair `L_1 = {z_2=z_3=0}`, `L_2 = {z_0 = 2z_2+z_3, z_1 = z_2-3z_3}`, `d_0 = 0.303546`:
`Tr/cos^{2N}(d_0)` = 2.74, 4.17, 5.35, 7.14, 8.82 at `N = 2,4,6,10,16`, saturating -- exponent 0, as
Laplace predicts for an *isolated* closest pair; the Clifford pair has a one-complex-parameter family
of closest pairs and gains exactly one power of `N`.

**N5. Conic and line in `P^2`, transversal versus TANGENT (section D).** `V = {z_0z_1 - z_2^2}`
(`HF = 2N+1`); `W_t = {z_1 = z_0}` transversal at `[1:1:+-1]` (both angles `pi/2`, `J = 1`,
prediction `sum_i 1/J_i = 2`); `W_g = {z_1 = 0}` TANGENT at `[1:0:0]`, `m = 2`, `gamma = 1`.

| `N` | `Tr` transversal | slope | `Tr` tangent | slope | `Tr_tan/sqrt(N)` |
|---|---|---|---|---|---|
| 16 | 2.034957 | -0.0241 | 4.792859 | 0.3817 | 1.198215 |
| 44 | 2.011779 | -0.0068 | 7.199825 | 0.4144 | 1.085415 |
| 60 | 2.008552 | -0.0047 | 8.205198 | 0.4237 | 1.059286 |

Transversal: exponent `-> 0`, constant `-> 2` as `2 + 0.5/N`. **TANGENT: exponent `-> 1/2`**, with
the three-term fit `Tr/sqrt(N) = 0.8915 + 1.380/sqrt(N) - 0.62/N` against the predicted
`Gamma(1+1/m)|gamma|^{-2/m} = 0.886227` (0.6%). Meanwhile `HF_{R/(I+J)}(N) = 2` for all `N >= 1`
(`I+J = (z_1, z_2^2)`): at a tangency the observable is neither a dimension nor the Hilbert function
of the sum ideal.

**N6. Two smooth conics in `P^2`, four transversal points (section E).** `V = {z_0z_1-z_2^2}`,
`W_lam = {z_0^2+z_1^2+lam z_2^2}`; `lam < -2` gives four real transversal points at
`[w:1:+-sqrt w]`, `w^2 + lam w + 1 = 0`. Both pairs have `HF_{R/(I+J)}(N) = 4` (Bezout).

| `lam` | `cos t` (all four) | `1/J` each | predicted `sum_i 1/J_i` | `Tr(60)` | `Tr/limit` | slope at 60 |
|---|---|---|---|---|---|---|
| -10 | 0.560612 | 1.458333 | 5.833333 | 6.276744 | 1.0760 | -0.098 |
| -3 | 0.872872 | 4.200000 | 16.800000 | 16.799398 | 0.99996 | 0.287 |

The **angle-inflation factor** `sum_i J_i^{-1}/4` is 1.458 and 4.200: the observable is the Bezout
number times the inverse angle factor (Corollary 6a). The well-conditioned pair (`mu_cap = 1.46`) has
reached exponent 0 by `N = 60`, Richardson extrapolation of `a + b/N` giving 5.70 against 5.833
(2.3%); the ill-conditioned pair (`mu_cap = 4.2`) is still climbing at exponent 0.29 while passing
through its predicted constant -- the curved-variety version of N3.

**N7. Excess but clean intersection (section F).** `V = {z_3=z_4=0}`, `W = {z_2=z_4=0}` in `P^4`:
two `P^2`s of **expected** intersection dimension `2+2-4 = 0` whose actual intersection is the line
`{z_2=z_3=z_4=0}`, `l = 1`; clean, not transversal. Measured `Tr = N+1` exactly for `N = 2..12`
(`= HF_{R/(I+J)}(N)`, `J = 1`), local slope 0.71 -> 0.92 toward 1. **The observable reports the
actual dimension** -- the one thing it does that Krull's principal ideal theorem does not.

**N8. Toeplitz averages on the conic (section G).** `T_g^{(N)} = ((N-r)!/N!) P_0 :g: P_0`
(D-normalised-toeplitz-operator). Reference values by 4000-node Gauss-Legendre quadrature on
`[s:t] -> [s^2:t^2:st]` with the induced density `A(u) = (u^2+4u+1)/(u^2+u+1)^2`, `u = |s/t|^2`;
the quadrature reproduces `int_0^inf A du = 2.0000000000` (`= deg V`) and
`2<|z_0|^2> + <|z_2|^2> = 1.0000000000`.

| `N` | `Tr(P_0 n_2)/(N HF)` | err | `Tr(P_0 n_2(n_2-1))/(N(N-1)HF)` | err |
|---|---|---|---|---|
| 22 | 0.2378805749 | 1.48e-3 | 0.0651502954 | 5.28e-4 |
| 60 | 0.2369303424 | 5.31e-4 | 0.0648133103 | 1.91e-4 |
| fit `a+b/N` | **0.23638334 + 0.03275/N** | **-1.65e-5** | **0.06461880 + 0.01166/N** | **-3.51e-6** |
| quadrature | 0.23639986 | | 0.06462232 | |

**C-168 / C-086 confirmed** to 1.7e-5 and 3.5e-6 in the extrapolated constant, with a clean
`Theta(1/N)` correction whose coefficient is what forces `N = Omega(1/eps)` in K-IO6. The `O(1/N)`
coefficient is ordering dependent (D-toeplitz-operator Pitfalls); the leading term is not.

**N9. Size of the DQC1 signal (section H).** Two hyperplanes in `P^n` at angle `t`, `N = n`
(`reg = 1`); `Tr = sum_{a=0}^{N} cos^{2a}(t)binom(N-a+n-2, n-2)` exactly.

| `n = N` | `M_N` | `Tr` (`t = pi/2`) | `Tr/M_N` | `Tr/sqrt(HF_I HF_J)` | `Tr/(HF_I HF_J)` |
|---|---|---|---|---|---|
| 4 | 70 | 15 | 2.143e-1 | 4.286e-1 | 1.22e-2 |
| 8 | 12870 | 3003 | 2.333e-1 | 4.667e-1 | 7.25e-5 |
| 32 | 1.8e18 | 4.5e17 | 2.460e-1 | 4.921e-1 | 5.37e-19 |

At `t = 0.4` the same two ratios read 0.4337 and 0.8674 at `n = 32`. So **`Tr/M_N -> 1/4`,
`Tr/sqrt(HF_I HF_J) -> 1/2`**. With codimension growing (`I = (z_0..z_{k-1})`, `J = (z_k..z_{2k-1})`,
`n = N = 4k`, `codim(V^W) = 2k`) it collapses: `Tr/M_N` = 2.14e-1, 3.85e-2, 1.22e-3, 1.23e-6 and
`Tr/(HF_I HF_J)` = 1.22e-2, 5.49e-5, 7.95e-10, 1.19e-19 at `k = 1,2,4,8`. Visibility is controlled by
`codim(V ^ W)` alone, and the SWAP-test normalisation is far smaller at every size (K-IO8).

**N10. The Bergman frame lemma, measured (section I).** Spectrum of `(N/pi)S_V` on `ker H_N` for the
conic, `S_V = int_V |e_p><e_p| dvol_V` on a 900x96 Gauss-Legendre grid; Geometry step 2 (the
argument's only unproved leaf) says these are asymptotically flat at 1. Min / max / mean on
`ker H_N`, and max on `I_N`: `N=6`: 0.890019 / 1.032096 / 0.923077 / 7.2e-16; `N=10`: 0.930690 /
1.038218 / 0.952381 / 1.2e-15; `N=14`: 0.949404 / 1.035624 / 0.965517 / 1.0e-15; `N=18`: 0.960160 /
1.032098 / 0.972973 / 9.7e-16. The mean is exactly `2N/(2N+1) = vol(V)N/(pi HF)` (an identity, steps
2.2-2.3); the spread falls as 0.14, 0.11, 0.086, 0.072, i.e. `O(1/N)`; `S_V` annihilates `I_N` to
machine precision, confirming `ran S_V = ker H_N` exactly (C-028).

## Geometry

Lamport-hierarchical sketch (L3); leaves cite a D-id, a C-id, or a named script section.

**ASSUME.** **A1** `I, J` homogeneous radical; `V = V(I)`, `W = V(J)` smooth of dimensions
`k_1, k_2` (D-homogeneous-ideal, D-variety). **A2** `N >= max(reg I, reg J)`
(D-saturation-regularity-stable-range), so `I_N = I(V)_N`, `J_N = I(W)_N`. **A3** the intersection is
**clean**: `Z = V ^ W` smooth of pure dimension `l` and `T_xV ^ T_xW = T_xZ` for every `x in Z`
(transversal is `dim_R(T_xV + T_xW) = 2n`, i.e. `l = k_1+k_2-n`; excess-but-clean is
`l > k_1+k_2-n`; tangency violates A3). **A4** the metric convention above, with
`theta_i(x)` the principal angles between `T_xV (-) T_xZ` and `T_xW (-) T_xZ`,
`J(x) = prod_i sin^2 theta_i(x)`.

**PROVE.** `Tr(P_I P_J) = (N/pi)^l int_Z J(x)^{-1} dvol_Z(x) . (1 + O(1/N))`.

1. `P_I` projects onto `H_V := span{e_p : p in V}`.
   1.1 `ran P_I = ker H_N = (I_N)^perp` [D-ground-space, D-projectors, D-inverse-system].
   1.2 `(I_N)^perp = (I(V)_N)^perp` [A2].
   1.3 `(I(V)_N)^perp = span{e_p : conj(p) in V}` [C-028, C-026, D-coherent-state]; the conjugation
   is C3 and is immaterial for the real-coefficient examples N1-N10.
2. **(Bergman frame lemma.)** `S_V := int_V |e_p><e_p| dvol_V(p) = (pi/N)^{k_1}(P_I + E_N)`,
   `||E_N|| = O(1/N)`.
   2.1 `ran S_V = H_V` exactly for every `N` [step 1; `S_V >= 0` and `<u|S_V|u> = 0` iff `u` is
   orthogonal to every `e_p`, `p in V`]. Measured to 1e-15 in N10.
   2.2 `Tr S_V = int_V ||e_p||^2 dvol_V = vol(V) = deg V . pi^{k_1}/k_1!` [Wirtinger].
   2.3 `rank S_V = HF_{R/I}(N) = deg V . N^{k_1}/k_1! (1+O(1/N))` [A2, D-hilbert-function].
   2.4 So the *mean* eigenvalue of `(N/pi)^{k_1}S_V` on `H_V` is `1 + O(1/N)`. The lemma is the
   stronger statement that the eigenvalues are asymptotically **flat**, i.e. Tian-Zelditch-Catlin
   Bergman asymptotics for `(V, O(N)|_V)` read in the ambient frame [Tian,
   DOI 10.4310/jdg/1214445039; Zelditch, arXiv:math-ph/0002009]. **LEAF STATUS: the one step this
   lane does not prove** -- a citation plus the spectral measurement N10; everything downstream
   inherits its status.
3. `Tr(P_I P_J) = (N/pi)^{k_1+k_2} Tr(S_V S_W)(1+O(1/N))` [step 2 twice; `P_I, P_J` projectors].
4. `Tr(S_V S_W) = int_V int_W |<e_p,e_q>|^2 = int_V int_W cos^{2N}d(p,q)` [D-coherent-state:
   `<e_p,e_q> = <p,q>^N`; A4].
5. **(Laplace.)** `int_V int_W cos^{2N}d = (pi/N)^{k_1+k_2-l} int_Z J^{-1}dvol_Z (1+O(1/N))`.
   5.1 `cos^{2N}d = exp(-Nd^2(1+O(d^2)))`, concentrating at `d = O(N^{-1/2})` where the correction
   is `O(1/N)`.
   5.2 The zero set of `d` on `V x W` is the diagonal `{(x,x): x in Z}`, real dimension `2l`.
   5.3 In normal coordinates at `x in Z`, with `L = T_xV`, `M = T_xW`, the form `|u-v|^2` on `L x M`
   has kernel exactly `{(e,e): e in T_xZ}` -- this **is** A3 -- and is positive definite on a
   complement of real dimension `dim_R(L+M) = 2(k_1+k_2-l)`.
   5.4 The Gaussian integral over that complement is `(pi/N)^{k_1+k_2-l}` over the Jacobian of
   `(u',v') -> u'-v'` from `(L (-) T_xZ) x (M (-) T_xZ)` onto `(L+M) (-) T_xZ`, which is
   `prod sin theta` over the *real* principal angles; a complex angle occurs twice, giving `J(x)`
   [linear algebra; verified to 8 digits against N1, N2 and the curved cases N5, N6].
6. Combining 3-5: `(N/pi)^{k_1+k_2}(pi/N)^{k_1+k_2-l} = (N/pi)^l`. QED modulo 2.4.

**Corollary 6a (Hilbert-function identity).** For `J(x) = J` constant on `Z`,
`int_Z J^{-1}dvol_Z = deg(Z)pi^l/(l!J)`, so `Tr(P_I P_J) = HF_{R/(I+J)}(N)/J . (1+O(1/N))`; under A3
the scheme `V ^ W` is reduced, so `I+J` may replace its radical in the stable range.
**Corollary 6b.** Under A1-A4 the growth exponent is exactly `dim(V ^ W)` -- transversal or excess,
provided clean. **Corollary 6c (disjoint).** If `V ^ W = {}`, with `d_0 = d_FS(V,W) > 0` and `S` the
set of closest pairs, the same argument gives `Tr = C N^{dim_C S}cos^{2N}(d_0)(1+o(1))`, hence
`-(1/2N)log Tr = log sec d_0 - dim_C(S)log N/(2N) + O(1/N)`. Clifford pair: `dim_C S = 1` and the
closed form is exact; generic skew pair: `dim_C S = 0` (N4). This is C-167 with its missing
polynomial prefactor and its bias made explicit.

**What fails without each hypothesis.** Without **A2**, `(I_N)^perp` strictly contains the coherent
span (D-entangled-defect), step 1.3 fails, and the observable also measures irrelevant torsion.
Without **A1** the same, plus multiplicity entering through jets. Without **smoothness**, 5.3 has no
tangent space and the local exponent becomes an invariant of the singularity. Without **A3** the
exponent changes: for smooth curves in `CP^2` meeting at one point with contact order `m` (local
model `d^2 = |u-v|^2 + |gamma|^2|u|^{2m}` in a Fubini-Study normal chart, and
`int_C exp(-N|gamma|^2|u|^{2m})dA = pi Gamma(1+1/m)(N|gamma|^2)^{-1/m}`),
**`Tr(P_I P_J) -> Gamma(1+1/m)|gamma|^{-2/m}N^{1-1/m}`**. Since the intersection multiplicity of two
smooth curves with contact order `m` is `m`, the exponent is `1 - 1/mu`: a non-integer rational fixed
by the multiplicity, not the dimension (N5 measures `m = 2`, `gamma = 1`). **Near-**failure of A3 is
worse than failure: `J -> 0` inflates the constant and the asymptotic regime only begins at
`N ~ mu_cap` (N3, N6).

## Against the north star

**1 -- Problem (met).** Same input throughout (D-input-model: sparse generators of `I, J`, `poly(n)`
monomials and coefficient bits, `N` unary). **P0 (native):** estimate `tau_N = Tr(P_I P_J)/M_N` to
additive `eps`. **P1 (dimension):** with A1-A3, `reg <= N`, `Delta_N/alpha_BE >= 1/poly` for both
ideals and `mu_cap <= poly`, decide `dim(V ^ W) >= l` versus `<= l-1`. **P2 (distance):** with
`V ^ W = {}`, estimate `d_FS(V,W)` to additive `eta`. **P3 (integration):** estimate
`vol(V)^{-1}int_V g dvol_V` to additive `eps`. All four are precisely stated; all are promise
problems; the promise list has five entries, two of which (`mu_cap`, cleanness) this lane had to
invent because the seed does not state them.

**2 -- Classical baseline (failed).** For P1 the baseline is not trace estimation but numerical
algebraic geometry: witness sets and numerical irreducible decomposition [SVW,
DOI 10.1137/S0036142900372549] present `V, W` as witness point sets of sizes `deg V`, `deg W`; the
diagonal homotopy [SVW, DOI 10.1137/S0036142903430463] intersects them in `deg V . deg W` path tracks
and returns the **exact integer** `dim(V ^ W)` with witness points on each component; the trace test
[SVW, DOI 10.1137/S0036142901397101] certifies it; tracking is `poly(n)` per path on average [Lairez,
DOI 10.1007/s10208-016-9319-7; D-condition-number], implemented in HomotopyContinuation.jl
[arXiv:1711.10911]. For P3 the baseline is C-087 (slice with a random linear space -- the points are
Fubini-Study distributed by the kinematic formula -- and average): `O(1/eps^2)` samples of `deg V`
tracks each. For P0 the baseline is Hutch++ [arXiv:2010.09649] on the PSD operator `P_I P_J P_I`
(note `Tr(P_I P_J) = ||P_J P_I||_F^2 >= 0`): `O(1/eps_rel)` matrix-vector products, each two spectral
filters of `O~(M_N s_row alpha_BE/Delta_N)` flops by sparse Krylov; dense rank is not the baseline
(classical memo trap 1). Decisively: `HF_{R/(I+J)}(N)` is a rank of the concatenated Macaulay matrix,
so the exact answer to P1 at level `N` costs one Hilbert-function evaluation, no Groebner basis and
no elimination.

**3 -- Quantum algorithm (partial, no arm-specific margin).** P0 is a D-dqc1-style-estimate:
maximally mixed state on the weak-composition register (`O(n log N)` qubits), two QSVT spectral
projectors (D-qsvt, D-projectors) at `O~(alpha_BE/Delta_N . log(1/eps'))` block-encoding uses each,
Hadamard test; `O(1/eps)` rounds with amplitude estimation. Total
`O~(poly(n, log N)(alpha_I/Delta_I + alpha_J/Delta_J)/eps)`. Reading an *exponent* needs
`tau_{2N}/tau_N` to relative accuracy `1/4`, so `eps = Theta(tau_N)` and `Omega(1/tau_N)` rounds, and
needs `N >~ mu_cap` (N3): honest bound `O~(poly(n, N, mu_cap, alpha_BE/Delta_N)/tau_N)`. Against the
classical `Omega(M_N)` per filter the margin is exactly `M_N` -- exponential when `N = Theta(n)`, but
it is arm A's margin for `HF/M_N` applied to a concatenated generator list, not a new one. Space
`O(n log N)` qubits versus `M_N` words is not by itself a separation (fact SP-0, PRD D15) and must be
stated as a simultaneous (space, time) claim (D-space-time-pareto).

**4 -- Dequantization audit (failed).** Low-rank dequantization (Tang; Gilyen-Lloyd-Tang; Chia et
al.) does not apply: `H_N` is sparse and high rank and `P_I` has rank `HF(N)`, a constant fraction of
`M_N` at low codimension (D-hardness-anchors). The live attack is the classical comparator. (i)
Hutch++ is already `O(1/eps)` matvecs for PSD inputs, so amplitude estimation beats naive Hutchinson,
not the stated best classical baseline (`scouting/quantum-primitives.md`, Combinations preamble).
(ii) What remains is the vector length `M_N`, the generic "quantum works in the exponentially large
space" claim. (iii) The seed's selling point, "without forming `I + J`", is void (criterion 2). (iv)
The answer is an exponent, and extracting it needs `eps = Theta(tau_N)`; `tau_N` obeys the campaign's
codimension law (`applications-wide-net.md` caution 1, `rho^codim`, `rho ~ 0.75` at `N = n`), so the
cost is `rho^{-codim(V^W)}`. (v) One nominal margin survives: for `V, W` complete intersections of
quadrics with `codim(V^W) = c`, the classical witness route needs `deg V . deg W = 2^c` path tracks
while the quantum estimator needs `rho^{-c} ~ 1.33^c` amplitude-estimation rounds -- an exponential
with a smaller base. It is fragile: it ignores `mu_cap` and `alpha_BE/Delta_N`, and the classical
route returns points and a certificate where the quantum route returns a real number from which an
integer must be inferred.

**5 -- Heuristic hardware (met).** With `rho_I = P_I/HF_I`, `rho_J = P_J/HF_J`, a **bosonic SWAP
test** -- mode-wise 50:50 beam splitters between the two `(n+1)`-mode registers, then photon-number
parity in the difference modes, i.e. many-mode Hong-Ou-Mandel interference -- measures
`Tr(rho_I rho_J) = Tr(P_I P_J)/(HF_I HF_J)` with `O(1/eps^2)` shots, no postselection and no
non-Gaussian element. (a) **Linear `V, W`:** `rho_I` is `N` photons maximally mixed over the
symmetric subspace of a `(k+1)`-mode subspace, reachable with a passive interferometer and a
phase-randomised source; the smallest instance is `n = 2`, `N = 1`, two lines in `P^2` at angle `t`,
measuring `(1+cos^2 t)/4` -- an interferometric measurement of the angle between two projective
lines, classically trivial. (b) **The conic:** `ker H_N` for `z_0z_1 - z_2^2` is the `2N+1`-fold
degenerate ferromagnetic ground manifold of the Law-Pu-Bigelow spin-mixing Hamiltonian (C-024,
D-spin-mixing-hamiltonian, DOI 10.1103/PhysRevLett.81.5257); two such condensates in relatively
rotated bases, interfered, measure `Tr(P_I P_J)/(2N+1)^2` for two conics, whose limit N6 predicts
exactly. A genuine analogue measurement of a Bezout-type constant times an angle factor -- and not a
speedup, three modes being fixed `n` and therefore classically polynomial by C-099 [arXiv:2211.16998,
DOI 10.22331/q-2023-11-28-1189].

**Verdict 2/5.** Report the arm as producing three theorems (the clean-intersection asymptotic with
its explicit constant, the tangency exponent `1 - 1/mu`, and `Tr = HF_{R/(I+J)}/J`) plus four
negative algorithmic results, then close it as a speedup route unless PRD §7 Q4 is answered in favour
of dictionary theorems.

## Killers

**K-IO1 (structural; kills novelty).** `Tr(P_I P_J) = HF_{R/(I+J)}(N)/J (1+O(1/N))` under clean
intersection: the observable is arm A's normalised Hilbert function on the concatenated generator
list, times an unknown metric factor, and `I_N + J_N` is free to form. Arm C adds no new quantum
primitive, no new hardness anchor and one nuisance parameter; everything arm A proves or fails to
prove about `HF/M_N` transfers verbatim.

**K-IO2 (decisive for P1).** `tau_N` is polynomially visible iff `codim(V ^ W) = O(1)` (N9). `N`
unary bounds `reg` polynomially; for complete intersections `reg = sum(m_i-1)+1`, `deg = prod m_i`,
so bounded codimension plus bounded regularity forces `deg V . deg W = poly(n)` -- exactly when the
diagonal homotopy returns the exact integer `dim(V ^ W)` in `poly(n)` expected time. Either the
degrees are small and classical numerical algebraic geometry wins outright, or they are exponential
and then `N >= reg` is exponential, which under `N` unary is an exponential-size input for the
quantum algorithm too. Closed from both sides.

**K-IO3 (conditioning; the arm-C form of C-170/C-172).** The exponent is misreported until
`N >~ mu_cap`: at `mu_cap = 100` the local slope is 1.80 at `N = 32`, 1.54 at `N = 256`, 1.16 at
`N = 1024`, truth 1 (N3); curved analogue N6. Every promise making P1 solvable must bound an angle
condition number, and the cost is polynomial in it -- the phenomenon Conjecture 8.11 anticipates for
`Delta_N` versus `mu_norm`, arriving through the observable instead of the gap.

**K-IO4 (kills C-085 as written).** No transversality hypothesis, no dimension reading: at an
order-`m` contact the exponent is `1 - 1/m` and `Tr -> infinity` although `dim(V ^ W) = 0` and
`HF_{R/(I+J)}(N) = m`. Off the clean locus the observable reads a metric contact order, not an
algebraic dimension, and the exponent can be a non-integer rational.

**K-IO5 (kills P2 / C-167 as an algorithm).** `-(1/2N)log Tr` carries a bias `+dim_C(S)log N/(2N)`.
On the exact Clifford form at `d_0 = 0.3` the bias at `N = 40` (0.0464) exceeds the signal (0.0457).
Ten per cent relative accuracy needs `log(N+1)/(2N) < 0.0046`, i.e. `N >~ 800`, where `Tr ~ 1e-29`
and `tau_N ~ 1e-36`. Additive estimation of an exponentially small number is exponential work, with
or without amplitude estimation.

**K-IO6 (kills P3 / C-168 as a speedup).** The Berezin-Toeplitz bias is `Theta(1/N)` with measured
coefficients 0.033 and 0.012 (N8), so `eps` forces `N = Omega(1/eps)`. Under D-input-model (`N`
unary) and D-block-encoding-normalisation (`alpha_BE = poly(n)N^m`) the quantum cost is at least
`alpha_BE/(Delta_N eps) = Omega(eps^{-(m+1)})`, against C-087's `O(eps^{-2})` with no `N` dependence:
the quadratic amplitude-estimation gain is not merely cancelled but reversed for `m >= 2`.

**K-IO7 (regime).** Everything computable here has `n <= 4`, inside the region C-099 says is
classically polynomial [arXiv:2211.16998]. The numerics can validate the geometry; they can never
exhibit an advantage, which must be argued at growing `n` where no such numerics exist.

**K-IO8 (hardware readout).** The SWAP test measures `Tr/(HF_I HF_J)`, not `Tr/M_N` -- smaller by
`M_N/(HF_I HF_J)`, a factor `~n/4` for two hyperplanes and exponential at higher codimension (N9) --
and it needs the maximally mixed state on each ground space, which for anything but linear or toric
`V` is the hard preparation problem. Where preparation is easy the classical problem is trivial;
where the classical problem is interesting, preparation is the bottleneck. K-QP8 in intersection
clothing.

**K-IO9 (genericity).** For generic `I, J` the exponent is the expected dimension `k_1+k_2-n`, free
classically; the observable is informative only on the excess locus, which is measure zero and where
angles are typically small so the required `N` grows (K-IO3). The clean positive is that on the
excess locus the observable is *correct* (N7) -- more than C-166's "transversal" promised.

**K-IO10 (definitional).** The seed never says which projector `P_I` is; under D-projectors' reading
the quantity is `Theta(M_N)` with no geometry, so C-085/C-166/C-167 are not well-posed until
D-intersection-overlap is ratified.

## Proposed definitions

MERGE PROPOSAL (`definitions/definitions.md`); all verified in the lane script.

**D-intersection-overlap.** `T_N(I,J) := Tr(P_{0,N}^{(I)}P_{0,N}^{(J)})`, `P_{0,N}` the projector
onto `ker H_N` (D-projectors), i.e. the Bergman projector of D-bergman-projector; equivalently
`||B_I^dag B_J||_F^2` for orthonormal ground-space bases, and `= Tr(P_I P_J P_I) >= 0`. Three
normalisations, all in use: `tau_N = T_N/M_N` (the D-dqc1-style-estimate quantity),
`T_N/sqrt(HF_I HF_J)`, `T_N/(HF_I HF_J) = Tr(rho_I rho_J)` (what a two-copy SWAP test measures).
Source: seed §5.7 L159, Conjecture 8.10(a); this lane. Pitfalls: it is **not**
`Tr(P_{I_N}P_{J_N}) = M_N - HF_I - HF_J + T_N = Theta(M_N)`; the three normalisations differ by
factors exponential in codimension, so a signal-size statement must say which.

**D-clean-intersection.** Smooth `V, W` in `CP^n` intersect cleanly along `Z = V ^ W` if `Z` is
smooth of pure dimension and `T_xV ^ T_xW = T_xZ` for every `x in Z` (Bott). Transversal implies
clean; clean also covers **excess** intersection (`dim Z > k_1+k_2-n`); tangential contact is exactly
the failure. Source: this lane, Geometry A3. Pitfalls: this, not transversality, is the hypothesis
every intersection-overlap asymptotic needs; C-166's "transversal" is strictly stronger and misses the
excess case, the only case in which the observable answers a question Krull does not.

**D-intersection-angle-condition-number.** For a clean intersection,
`J(x) = prod_i sin^2 theta_i(x)` over the principal angles between `T_xV (-) T_xZ` and
`T_xW (-) T_xZ`, and `mu_cap(V,W) := sup_{x in Z}J(x)^{-1} in [1, infinity]`; `mu_cap = 1` iff the
tangent spaces meet orthogonally modulo `T_xZ`, `= infinity` iff the intersection is not clean.
Source: this lane, Geometry 5.4. Pitfalls: arm C's condition number, the analogue of
D-condition-number for the observable; the asymptotic regime begins only at `N ~ mu_cap`, so
`mu_cap` belongs in every promise and every cost bound.

**D-bergman-frame-operator.** `S_V^{(N)} := int_V |e_p><e_p| dvol_V(p)` on `R_N` for smooth `V` of
dimension `k` with the induced Fubini-Study volume. Exactly `ran S_V = (I(V)_N)^perp` (C-028);
asymptotically `S_V^{(N)} = (pi/N)^k(P_I + O(1/N))` [Tian, DOI 10.4310/jdg/1214445039; Zelditch,
arXiv:math-ph/0002009]. Source: this lane, Geometry step 2. Pitfalls: the trace and rank identities
are elementary and exact; the flatness of the spectrum is the cited, unproved part, and every
asymptotic constant in arm C rests on it.

**D-normalised-toeplitz-operator.** Amendment to D-toeplitz-operator: for `g(z, conj z)` of bidegree
`(r,r)` the level-`N` Toeplitz operator must carry the degree normalisation
`T_g^{(N)} = ((N-r)!/N!)P_0 :g(a^dag,a): P_0`, whose Berezin symbol is exactly `g(p, conj p)` for
every `N`. Without it `Tr(P_0 T_g)/HF(N)` diverges like `N^r` and C-168 is dimensionally false as
stated. Examples: `r=1`, `g = |z_2|^2`, `T_g = n_2/N`; `r=2`, `g = |z_2|^4`,
`T_g = n_2(n_2-1)/(N(N-1))`. Source: this lane, N8. Pitfalls: normal ordering fixes the `O(1/N)`
term, the degree normalisation fixes the leading term; Conjecture 8.10(c) supplies neither.

**D-contact-order.** For smooth curves `V, W` in `CP^2` meeting at `x`, the contact order `m` is the
largest integer with `W` agreeing with `V` to order `m-1` at `x`; in a Fubini-Study normal chart with
`W` the tangent geodesic, `V` is `psi(u) = gamma u^m + O(u^{m+1})`, and `m` equals the intersection
multiplicity at `x`. Source: this lane, Geometry, failure of A3. Pitfalls: `m = 1` is transversality;
`m >= 2` sends `mu_cap` to infinity and the growth exponent to `1 - 1/m`.

## Proposed claim rows

MERGE PROPOSAL (`claims/CLAIMS.md`), all CONJECTURE per L1 except the REFUTED row; `where-proved` is
this memo by step number, `where-tested` is `checkers/explore/intersection_observables.py` by section.

**C-NEW-IO-CLEAN.** For all homogeneous radical `I, J` in `C[z_0..z_n]` with `V = V(I)`, `W = V(J)`
smooth, all `N >= max(reg I, reg J)`, and `V, W` intersecting CLEANLY along `Z` of pure complex
dimension `l` (D-clean-intersection): `Tr(P_I P_J) = (N/pi)^l int_Z J(x)^{-1}dvol_Z(x)(1 + O(1/N))`
in the convention `d = arccos|<p,q>|`, `J(x)` as in D-intersection-angle-condition-number. In
particular the growth exponent is exactly `dim(V ^ W)`, in the excess case as well as the
transversal one. depends-on C-026, C-028, C-079, C-166, D-intersection-overlap,
D-clean-intersection, D-intersection-angle-condition-number, D-bergman-frame-operator,
D-saturation-regularity-stable-range; where-proved Geometry 1-6 (complete except 2.4, a citation);
where-tested N1, N2, N5, N6, N7, N10. Relevance: the arm's only theorem-grade product; supersedes
C-166, whose hypothesis is strictly stronger and whose constant is unspecified.

**C-NEW-IO-SUM-IDEAL.** Under C-NEW-IO-CLEAN with `J(x) = J` constant on `Z`,
`Tr(P_I P_J) = HF_{R/(I+J)}(N)/J . (1+O(1/N))`; and since `I_N + J_N` is the row span of the
concatenation of the two Macaulay matrices (D-macaulay-matrix), computing `HF_{R/(I+J)}(N)` costs no
more than one Hilbert-function evaluation, so the quantum route avoids no elimination. depends-on
C-NEW-IO-CLEAN, D-hilbert-function, D-macaulay-matrix, D-normalised-hilbert-function; where-proved
Corollary 6a; where-tested N1, N2, N5, N6, N7 (exact in every case with `J` constant). Relevance:
**negative, and the sharpest thing in the lane** -- reduces arm C to arm A on a concatenated
generator list. Traps checked: "changing the output", "hiding an elimination".

**C-NEW-IO-TANGENCY.** For smooth curves `V, W` in `CP^2` meeting at a single point with contact
order `m >= 1` (D-contact-order), `psi(u) = gamma u^m + O(u^{m+1})` in a Fubini-Study normal chart,
`Tr(P_I P_J) = Gamma(1+1/m)|gamma|^{-2/m}N^{1-1/m}(1+o(1))`; for `m >= 2` the exponent is a
non-integer rational, `Tr -> infinity`, `dim(V ^ W) = 0`, and `HF_{R/(I+J)}(N) = m` for `N >= m-1`.
depends-on C-NEW-IO-CLEAN, D-contact-order, D-intersection-overlap; where-proved Geometry ("what
fails without A3"); where-tested N5 (`m = 2`, `gamma = 1`: exponent 0.42 -> 1/2, constant 0.8915
versus 0.886227). Relevance: refutes C-085, fixes C-166's hypothesis, shows the observable is a
metric rather than an algebraic invariant off the clean locus.

**C-085 (lockstep: REFUTED).** It asserts "its growth exponent in `N` is `dim(V ^ W)`" with no
hypothesis beyond radicality and smoothness; C-NEW-IO-TANGENCY exhibits smooth radical `I, J` with
`dim(V ^ W) = 0` and growth exponent `1/2`. Surviving weaker statements: C-NEW-IO-CLEAN and
C-NEW-IO-DISTANCE.

**C-166 (lockstep: amended, status unchanged).** Replace "TRANSVERSAL" by "CLEAN
(D-clean-intersection)" -- strictly weaker, hence a strengthening; replace "`c` a positive
combination of the degrees of the components of `V ^ W` and angle factors" by the explicit
`c = pi^{-l} int_Z prod_i sin^{-2}theta_i dvol_Z` of C-NEW-IO-CLEAN; cite D-intersection-overlap for
`P_I`. `where-tested` becomes N1, N2, N5, N6, N7.

**C-NEW-IO-DISTANCE.** For radical `I, J`, `V, W` smooth in the stable range, `V ^ W = {}`,
`d_0 = d_FS(V,W) > 0` and `S` the set of closest pairs:
`Tr(P_I P_J) = C N^{dim_C S}cos^{2N}(d_0)(1+o(1))` with `C > 0`, so
`-(1/2N)log Tr = log sec d_0 - dim_C(S)log N/(2N) + O(1/N)`. For the Clifford pair
`L_1 = span(e_0,e_1)`, `L_2 = span(c e_0 + s e_2, c e_1 + s e_3)` in `P^3` the closed form is EXACT,
`Tr = (N+1)cos^{2N}(t)` with `d_FS(L_1,L_2) = t`. (The Clifford form is an elementary exact
computation verified to 10 digits; the general statement is Laplace.) depends-on C-167,
C-NEW-IO-CLEAN, D-intersection-overlap, D-coherent-state; where-proved Corollary 6c; where-tested N4.
Relevance: supplies the polynomial prefactor C-167 omits, and with it the bias that kills the readout.

**C-NEW-IO-DISTANCE-COST.** Estimating `d_FS(V,W)` to additive `eta` from `Tr(P_I P_J)` needs
relative accuracy `O(eta N tan d_0)` on `Tr`, hence additive `O(eta N tan(d_0)cos^{2N}(d_0)/M_N)` on
`tau_N`; the bias `dim_C(S)log N/(2N)` forces `N = Omega(eta^{-1}log(1/eta))`, so the round
complexity is `exp(Omega(eta^{-1}log(1/eta)))` with amplitude estimation and its square without. At
`d_0 = 0.3` the bias at `N = 40` (0.0464) already exceeds the signal (0.0457), and 10% relative
accuracy needs `N ~ 800`, where `Tr ~ 1e-29`. depends-on C-NEW-IO-DISTANCE, C-167,
D-dqc1-style-estimate; where-proved K-IO5; where-tested N4. Relevance: **refutes C-167 as an
algorithm** while leaving it true as mathematics. Trap checked: "exponentially small geometric
signal".

**C-NEW-IO-TOEPLITZ.** With the degree normalisation of D-normalised-toeplitz-operator, for `V` the
conic `z_0z_1 - z_2^2` in `P^2` and `g in {|z_2|^2, |z_2|^4}`,
`Tr(P_0 T_g^{(N)})/HF(N) = vol(V)^{-1}int_V g dvol_V + b/N + O(1/N^2)`, the integral computed
independently by Gauss-Legendre quadrature on `[s:t] -> [s^2:t^2:st]` with density
`A(u) = (u^2+4u+1)/(u^2+u+1)^2`, `u = |s/t|^2`. Measured `0.23638334 + 0.03275/N` against
`0.23639986`, and `0.06461880 + 0.01166/N` against `0.06462232`. depends-on C-086, C-168,
D-toeplitz-operator, D-normalised-toeplitz-operator, D-bergman-frame-operator; where-proved Geometry
step 2 applied to `Tr(P_0 X)` for `X` of Berezin symbol `g`; where-tested N8. Relevance: the
campaign's first numerical confirmation of C-168/C-086, and the first statement of the normalisation
without which they are false.

**C-NEW-IO-TOEPLITZ-COST.** Because the Berezin-Toeplitz bias is `Theta(1/N)` with nonzero
coefficient, additive accuracy `eps` forces `N = Omega(1/eps)`; under D-input-model (`N` unary) and
D-block-encoding-normalisation (`alpha_BE = poly(n)N^m`) the quantum cost is
`Omega(poly(n)eps^{-(m+1)}/(Delta_N/alpha_BE))`, against `O(eps^{-2})` slice-and-average samples
classically (C-087) with no `N` dependence. Hence no quantum advantage for integration over a variety
at `m >= 2`, and none at `m = 1` once `alpha_BE/Delta_N` is counted. depends-on C-NEW-IO-TOEPLITZ,
C-087, C-168, D-input-model, D-block-encoding-normalisation, D-condition-number; where-proved K-IO6;
where-tested N8. Relevance: **refutes C-168 as a speedup** while confirming it as mathematics. Trap
checked: "hiding a polynomial `N`".

**C-NEW-IO-WITNESS-BASELINE.** For `V, W` with `deg V . deg W = poly(n)` -- which under D-input-model
(`N` unary, hence `reg <= poly(n)`) is implied by `codim(V ^ W) = O(1)` for complete intersections --
the diagonal homotopy of Sommese-Verschelde-Wampler (DOI 10.1137/S0036142903430463) computes
`dim(V ^ W)` exactly, with witness points on every component, in `deg V . deg W` path tracks of
expected `poly(n)` cost each (DOI 10.1137/S0036142900372549; DOI 10.1137/S0036142901397101; Lairez
DOI 10.1007/s10208-016-9319-7; arXiv:1711.10911). Hence P1 admits no quantum speedup on the family
for which the observable's signal is polynomially visible. Status CONJECTURE (a literature-baseline
statement; a critic must confirm the path count and the average-cost claim); depends-on C-087,
C-NEW-IO-SIGNAL, D-input-model, D-condition-number; where-proved K-IO2; where-tested none
(literature). Relevance: **the arm's killer**; PRD §2 criterion 2 fails.

**C-NEW-IO-SIGNAL.** For two hyperplanes in `P^n` at Fubini-Study angle `t`,
`Tr(P_I P_J) = sum_{a=0}^{N}cos^{2a}(t)binom(N-a+n-2, n-2)` exactly; at `t = pi/2`, `N = n`,
`Tr/M_N = n(n-1)/((2n)(2n-1)) -> 1/4` and `Tr/sqrt(HF_I HF_J) = (n-1)/(2n-1) -> 1/2`. With
`I = (z_0..z_{k-1})`, `J = (z_k..z_{2k-1})`, `Tr/M_N` decays like `rho^{codim(V^W)}`
(`applications-wide-net.md` caution 1) and is independent of `n` at fixed codimension; the DQC1 signal
is polynomially visible iff `codim(V ^ W) = O(log n)`. depends-on D-intersection-overlap,
D-normalised-hilbert-function, D-dqc1-style-estimate; where-proved elementary monomial count;
where-tested N9. Relevance: **positive** -- removes the objection that the arm-C observable is
automatically exponentially small; smallness is controlled by `codim(V ^ W)`, not by `n`.

**C-NEW-IO-CROSSOVER.** For two hyperplanes in `P^3` at angle `t`, `Tr = sum_a c^{2a}(N+1-a)`,
`c = cos t`, whose local growth exponent equals `2` (the `V = W` value) for `N << mu_cap = 1/sin^2 t`
and tends to `1 = dim(V ^ W)` only for `N >> mu_cap`; measured at `mu_cap = 100`: 1.80 at `N = 32`,
1.54 at `N = 256`, 1.16 at `N = 1024`. Any promise under which P1 is solvable must bound `mu_cap`,
and the cost is polynomial in it. depends-on C-NEW-IO-CLEAN, D-intersection-angle-condition-number,
C-170, C-172; where-proved exact closed form plus Corollary 6a; where-tested N3, N6. Relevance: the
arm-C form of Conjecture 8.11 -- the observable's cost is governed by a condition number of the
geometry, exactly as the classical competitor's is.

**C-NEW-IO-DEQUANT.** `Tr(P_I P_J) = Tr(P_I P_J P_I) >= 0` with `P_I P_J P_I` PSD, so Hutch++
(arXiv:2010.09649) estimates `tau_N` to relative error `eps_rel` with `O(1/eps_rel)` matrix-vector
products, each two spectral-filter applications of `O~(M_N s_row alpha_BE/Delta_N)` flops, while the
quantum D-dqc1-style-estimate with amplitude estimation costs
`O~(poly(n, log N)alpha_BE/Delta_N/eps)`. The only asymptotic margin is the factor `M_N`, which is
the margin arm A already claims for `HF/M_N`; the `eps^{-2} -> eps^{-1}` improvement is not a margin,
Hutch++ being already `O(1/eps)`. depends-on C-NEW-IO-SUM-IDEAL, D-dqc1-style-estimate, D-qsvt,
D-block-encoding-normalisation, D-hardness-anchors; where-proved criterion 4; where-tested none (a
cost statement). Relevance: the dequantization audit for arm C. Traps checked: "dense rank",
"ignoring dequantization", "hidden state preparation" (none: the input is maximally mixed).

**C-NEW-IO-SWAP-HARDWARE.** For `rho_I = P_I/HF_I`, `rho_J = P_J/HF_J` on the `N`-boson sector of
`n+1` modes, the many-mode Hong-Ou-Mandel SWAP test (mode-wise 50:50 beam splitters plus
photon-number parity in the difference modes) measures `Tr(rho_I rho_J) = Tr(P_I P_J)/(HF_I HF_J)`
with `O(1/eps^2)` shots, no postselection and no non-Gaussian element. For linear `V, W` the states
are preparable with passive optics; the smallest instance is `n = 2`, `N = 1`, two lines in `P^2` at
angle `t`, measuring `(1+cos^2 t)/4`. For the conic the state is the `2N+1`-fold ferromagnetic ground
manifold of the spin-mixing Hamiltonian (C-024, DOI 10.1103/PhysRevLett.81.5257), giving an analogue
measurement of a Bezout-type constant times an angle factor. depends-on C-024,
D-spin-mixing-hamiltonian, D-intersection-overlap, D-symmetric-sector; where-proved criterion 5;
where-tested N6 supplies the predicted constant (the interferometer is not simulated). Relevance:
hardware. Trap checked: "mistaking a physical realization for an algorithm" -- a demonstration, not a
speedup (fixed `n`, C-099).

**C-NEW-IO-PROJECTOR-AMBIGUITY.** Conjecture 8.10(a) and rows C-085, C-166, C-167 write
`Tr(P_I P_J)` without saying whether `P_I` projects onto `I_N` or `(I_N)^perp`; under the first
reading it is `M_N - HF_I - HF_J + Tr(P_I P_J) = Theta(M_N)` in every example of this lane, with no
asymptotics of the asserted form. Only the second reading (D-intersection-overlap) is the
Bergman-projector overlap. Status CONJECTURE (well-posedness); depends-on D-projectors,
D-bergman-projector, D-intersection-overlap; where-proved Notation paragraph; where-tested N1-N7.

## Lockstep notes

- **C-085**: CONJECTURE -> REFUTED; surviving statements C-NEW-IO-CLEAN and C-NEW-IO-DISTANCE;
  `where-tested` becomes this lane's script.
- **C-166**: status unchanged, hypothesis transversal -> clean, constant explicit, `where-tested`
  filled in. PRD §4 arm C's conditional ("valuable only once a theorem ties the normalised observable
  to a geometric quantity at polynomially resolvable scale") is now MET on the mathematics side and
  FAILED on the algorithmic side, by K-IO2.
- **C-167**: status unchanged for its mathematical content; acquires the dependent refutation
  C-NEW-IO-DISTANCE-COST; its `north-star relevance` should move from "speedup" to "instrument, with
  an exponential readout cost".
- **C-168 / C-086**: status unchanged; gain `where-tested` (N8), the amendment
  D-normalised-toeplitz-operator, and C-NEW-IO-TOEPLITZ-COST as the refutation of the speedup reading.
- **C-079** gains `where-tested`: the Bergman-projector reading is exercised throughout, the frame
  lemma measured in N10.
- **PRD §4 arm C** and **HANDOFF**: record that the seed's own "suggested next step 3" has been run.
  **Critical claims item 7 (C-166/C-168)**: the requested numerics now exist; what remains for a
  critic is Geometry 2.4 and the baseline claim C-NEW-IO-WITNESS-BASELINE.

## Questions for TJO

1. **Is a dictionary theorem a product here?** (PRD §7 Q4.) The honest output is three theorems --
   the clean-intersection asymptotic with its explicit angle constant, the tangency exponent
   `1 - 1/mu`, and `Tr = HF_{R/(I+J)}/J` -- plus four negative algorithmic results. None is a
   speedup. Do they enter as deliverables, or does arm C close?
2. **Does K-IO2 close arm C outright?** The squeeze (visible signal <=> low codimension <=> small
   degrees <=> diagonal homotopy is polynomial) is the strongest baseline argument the campaign has
   produced. If accepted, arm C's PRD §4 ranking should fall below arm B.
3. **The one surviving margin** is `1.33^c` (quantum, amplitude estimation, codimension law) against
   `2^c` (classical, `deg V . deg W` path tracks) for complete intersections of quadrics. Is an
   exponential-with-a-smaller-base claim worth a week of adversarial work, given that it ignores
   `mu_cap` and `alpha_BE/Delta_N`?
4. **Ratify the notation** (D-intersection-overlap) and the Toeplitz degree normalisation
   (D-normalised-toeplitz-operator) before further arm-C work: three seed rows are not well-posed
   without them.
5. **Fund Geometry step 2.4?** The Bergman frame lemma is the only unproved leaf and all of arm C and
   half of seed §5.7 rest on it. Standard Tian-Zelditch-Catlin material, but this lane found no
   statement of it *in ambient coordinates for a subvariety* that can be cited verbatim. One analytic
   day, or accept as cited?
6. **The analogue experiment.** Two spinor condensates in relatively rotated bases, interfered,
   measure the four-point intersection constant of two conics (N6). Does that count under Q4, and is
   it worth writing up separately from the algorithm question?

## Citation index

Resolved during this lane against the arXiv API, doi.org or api.crossref.org, and read:
arXiv:2010.09649 (Hutch++, Meyer-Musco-Musco-Woodruff: `(1+-eps)` for PSD `A` with `O(1/eps)`
matrix-vector products); DOI 10.1137/S0036142900372549 (Sommese-Verschelde-Wampler, numerical
irreducible decomposition, SIAM J. Numer. Anal. 38, 2001); DOI 10.1137/S0036142901397101 (same
authors, trace test / symmetric functions, 40, 2002); DOI 10.1137/S0036142903430463 (same authors,
homotopies for intersecting solution components, 42, 2004); DOI 10.1007/s10208-016-9319-7 (Lairez,
average-polynomial-time path tracking, FoCM 17, 2016); arXiv:1711.10911 (Breiding-Timme,
HomotopyContinuation.jl); DOI 10.4310/jdg/1214445039 (Tian, JDG 32, 1990) and arXiv:math-ph/0002009
(Zelditch, "Szego kernels and a theorem of Tian"); arXiv:hep-th/9309134
(Bordemann-Meinrenken-Schlichenmaier, Berezin-Toeplitz quantisation); arXiv:2211.16998 =
DOI 10.22331/q-2023-11-28-1189 (Anschuetz-Bauer-Kiani-Lloyd, C-099). DOI 10.1103/PhysRevLett.81.5257
(Law-Pu-Bigelow, C-024) is quoted from D-spin-mixing-hamiltonian, not refetched here.

Not fetched, background only: Bott's clean-intersection condition [UNVERIFIED]; Catlin's and
Zelditch's off-diagonal Bergman expansions for submanifolds [UNVERIFIED]; the many-mode
Hong-Ou-Mandel SWAP test [UNVERIFIED].
