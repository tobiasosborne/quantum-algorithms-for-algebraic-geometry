# Adversarial verdict: `scouting/intersection-observables.md`, round 3

- Date: 2026-09-03
- Target delta: `git diff 7dda56d HEAD -- scouting/intersection-observables.md checkers/explore/intersection_observables.py`
- Mandated run: `cd checkers && timeout 900 python3 explore/intersection_observables.py`
- Exit code: **0**
- Runtime environment reported by checker: NumPy 2.4.6
- Scope: repair-r2 changes only; priors stand.

## Repair-r2 disposition audit

| objection | adjudication | evidence |
|---|---|---|
| O9 | **VERIFIED** | The C-079, C-085, C-086, C-087, C-166, C-167, C-168, and C-169 paste blocks reproduce the r2 texts exactly. C-087 drops C-085/C-086, C-168 drops C-086, and C-169 drops C-168. The memo explicitly orders dependency amendments first, other statement/testing amendments second, and REFUTED status changes last. |
| O10 | **VERIFIED** | D-intersection-overlap, D-bergman-frame-operator, and D-normalised-toeplitz-operator reproduce the three r2 rewordings verbatim, modulo the memo’s declared ASCII rendering of inline mathematics. They contain the radical/stable-range qualification, `P_{0,N}^{(I(V))}`, the explicit error operator `E_N`, unit-representative evaluation, and the C3-compatible conjugated coherent state. |
| O11 | **VERIFIED** | TANGENCY, DISTANCE, TOEPLITZ, SIGNAL, CROSSOVER, and DEQUANT reproduce the r2 texts verbatim under the same rendering convention. Both REFUTED rows reproduce their r2 surviving statements verbatim. C-NEW-IO-SUM-IDEAL is now explicitly HOLD because it assumes the held CLEAN row. |
| O12 | **VERIFIED** | Criterion 5 and C-NEW-IO-SWAP-HARDWARE both specify the parity of the total photon number in the antisymmetric/difference output modes. The observable is explicitly identified as \((-1)^{\sum_j n_{j,-}}\), not total output parity. |
| O13 | **VERIFIED** | The script now prints “These five,” and crossover details report both targets and Boolean comparisons. The mandated run caught M-IO1 through M-IO5; the mutated second crossover result is correctly reported as `target < 1.3: False`. |

## New objections

No O14. The changed text and the two changed script labels introduce no new defect.

## Final per-row decisions

| row | final decision |
|---|---|
| C-NEW-IO-LINEAR-EXACT | **ACCEPT AS CONJECTURE.** |
| C-NEW-IO-CLEAN | **HOLD missing step.** Geometry 2.4 remains unproved. |
| C-NEW-IO-SUM-IDEAL | **HOLD missing step.** It assumes C-NEW-IO-CLEAN. |
| C-NEW-IO-TANGENCY | **ACCEPT AS CONJECTURE.** The repaired statement is the exact r2 text. |
| C-NEW-IO-DISTANCE | **ACCEPT AS CONJECTURE.** The repaired statement is the exact r2 text. |
| C-NEW-IO-DISTANCE-COST | **ACCEPT AS REFUTED.** The surviving statement is the exact r2 text. |
| C-NEW-IO-TOEPLITZ | **ACCEPT AS CONJECTURE.** The repaired statement is the exact r2 text. |
| C-NEW-IO-TOEPLITZ-COST | **ACCEPT AS REFUTED.** The surviving statement is the exact r2 text. |
| C-NEW-IO-SIGNAL | **ACCEPT AS CONJECTURE.** The repaired statement is the exact r2 text. |
| C-NEW-IO-CROSSOVER | **ACCEPT AS CONJECTURE.** The repaired statement is the exact r2 text. |
| C-NEW-IO-DEQUANT | **ACCEPT AS CONJECTURE.** The repaired statement is the exact r2 text. |
| C-NEW-IO-SWAP-HARDWARE | **ACCEPT AS CONJECTURE.** The difference-mode parity repair is correct. |

## Per-definition decisions

| definition | final decision |
|---|---|
| D-intersection-overlap | **ACCEPT.** Exact r2 rewording present. |
| D-clean-intersection | **ACCEPT.** |
| D-intersection-angle-condition-number | **ACCEPT.** |
| D-bergman-frame-operator | **ACCEPT.** Exact r2 rewording present. |
| D-normalised-toeplitz-operator | **ACCEPT.** Exact r2 rewording present. |
| D-contact-order | **ACCEPT.** |

## Final lockstep paste blocks

### C-079

```text
- where-tested: checkers/explore/intersection_observables.py sections A–K; section I tests the frame spectrum numerically but is evidence for, not a proof of, the operator-norm estimate in Geometry 2.4.
```

### C-085

```text
- status: REFUTED
- counterexample: The smooth conic z_0z_1=z_2^2 and its tangent line z_1=0 have dim(V ∩ W)=0 but T_N ~ Gamma(3/2) N^{1/2}.
- surviving statement: For fixed homogeneous radical ideals whose smooth varieties intersect cleanly, the conjectural formula C-NEW-IO-CLEAN gives growth exponent dim(V ∩ W), conditional on the ambient Bergman-frame operator-norm estimate. Fixed disjoint varieties require the separate distance statement C-NEW-IO-DISTANCE.
- where-tested: checkers/explore/intersection_observables.py sections A–F and J.
```

### C-086

```text
- status: REFUTED
- counterexample: Under D-toeplitz-operator, g=|z_2|^2 gives T_g=P_0 n_2 P_0 and Tr(P_0T_g)/HF(N) ~ N <|z_2|^2>_V, so the stated normalized trace diverges.
- surviving statement: Under the distinct D-normalised-toeplitz-operator, the conjectural replacement is Tr(T~_g^{(N)})/HF(N)=vol(V)^{-1}∫_V g dvol_V+O(N^{-1}) for fixed smooth radical V, bihomogeneous projective g, and N→∞ through the stable range.
- depends-on: C-079, D-toeplitz-operator
- where-tested: checkers/explore/intersection_observables.py sections G and K.
```

### C-087

```text
- statement: Relevant classical competitors are random slicing and averaging when a witness set for V is supplied, diagonal homotopy for intersections when witness sets for both varieties are supplied, and randomized trace estimation using sparse Krylov projector filters. Their costs depend on input representation, tracking condition, certification requirements, and the requested additive precision. No universal polynomial cost from sparse generators is claimed.
- status: SKETCH
- depends-on: C-055, C-170, D-condition-number, D-kostlan-random-form, D-intersection-overlap, D-normalised-toeplitz-operator
```

### C-166

```text
- statement: For fixed homogeneous radical ideals I,J with smooth V,W intersecting transversely along a nonempty smooth pure-dimensional Z of complex dimension l, as N→∞ through the stable range,
  T_N(I,J)=(N/pi)^l ∫_Z prod_i sin^{-2}(theta_i(x)) dvol_Z(x) (1+O_{I,J}(N^{-1})),
  where T_N is D-intersection-overlap and the angles are those of D-intersection-angle-condition-number.
- status: CONJECTURE
- depends-on: C-026, C-028, C-079, D-intersection-overlap, D-intersection-angle-condition-number, D-bergman-frame-operator, D-saturation-regularity-stable-range
- where-tested: checkers/explore/intersection_observables.py sections A, C, D, and E (N1, N2, N5, N6).
```

### C-167

```text
- statement: For fixed homogeneous radical ideals I,J with smooth disjoint V,W, as N→∞ through the stable range,
  T_N(I,J) ≤ HF_I(N) HF_J(N) cos^{2N}(d_FS(V,W))
  and -log T_N(I,J)/(2N) → log sec(d_FS(V,W)).
  Under the real Morse–Bott hypothesis of C-NEW-IO-DISTANCE the polynomial prefactor is N^{r/2}; consequently its logarithmic correction has sign -r log N/(4N).
- status: CONJECTURE
- depends-on: C-026, C-028, C-079, D-intersection-overlap, D-coherent-state, D-bergman-frame-operator, D-saturation-regularity-stable-range
- where-tested: checkers/explore/intersection_observables.py sections B and J (N4, N11).
```

### C-168

```text
- status: REFUTED
- counterexample: Under D-toeplitz-operator, for the smooth conic and g=|z_2|^2, Tr(P_0T_g)/HF(N)=Tr(P_0n_2)/(HF(N)) grows linearly in N.
- surviving statement: Under the distinct D-normalised-toeplitz-operator, the conjectural replacement is Tr(T~_g^{(N)})/HF(N)=vol(V)^{-1}∫_V g dvol_V+O(N^{-1}) for fixed smooth radical V, bihomogeneous projective g, and N→∞ through the stable range. For the conic and g=|z_2|^2, the exact limit is -1/6+2 sqrt(3) pi/27 and the observed 1/N coefficient is approximately 0.03142.
- depends-on: C-079, D-toeplitz-operator
- where-tested: checkers/explore/intersection_observables.py sections G and K.
```

### C-169

```text
- statement: The normalized overlap quantities in C-166 and C-167, and degree-normalized Toeplitz traces defined by D-normalised-toeplitz-operator, are DQC1-style estimable to additive epsilon subject to the access, preparation, and normalized-gap assumptions of D-dqc1-style-estimate.
- status: CONJECTURE
- depends-on: C-061, C-166, C-167, D-intersection-overlap, D-normalised-toeplitz-operator, D-dqc1-style-estimate
```

Apply the `depends-on` amendments to C-087, C-168 and C-169 first, then the `where-tested` and statement amendments to C-079, C-166 and C-167, and only then flip C-085, C-086 and C-168 to REFUTED.

LOCKSTEP: READY

VERDICT: PASS