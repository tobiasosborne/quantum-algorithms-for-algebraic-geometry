<!-- ROLE: adversarial critic verdict, round 3 (adjudication of repair r2), on
     scouting/quantum-primitives.md (rk-light L5). Priors: verdicts/quantum-primitives-r1.md,
     verdicts/quantum-primitives-r2.md. UPDATE POLICY: append-only. -->

# Verdict: scouting/quantum-primitives.md, round 3 (adjudication of repair r2)

- **Target:** `scouting/quantum-primitives.md` at commit `6fc3f34` (2652 lines). Scope of this round: `git diff e9ad40b 6fc3f34 -- scouting/quantum-primitives.md` = **80 insertions, 65 deletions**. 15 ranked rows, 23 proposed claim rows, 14 proposed definitions, 73 references, plus a `# Repair r2 response` section with `## r1` and `## r2` disposition tables.
- **Date:** 2026-09-03.
- **Critic model:** Claude Opus 5 (1M), adversarial critic seat, round 3.
- **Priors:** `verdicts/quantum-primitives-r1.md` — FAIL(10 MAJOR, 11 MINOR, 4 NOTE); `verdicts/quantum-primitives-r2.md` — FAIL(O26, O27, O28), with 21 VERIFIED, 4 NOT VERIFIED, 11 NEW DEFECT. Both priors stand. I attack **changed text only**; O1–O6, O8, O11–O20, O22–O25 were settled in r2 and are not re-litigated.
- **Files read this round:** the diff `e9ad40b..6fc3f34` in full; the changed sections of the memo in place; `scouting/classical-landscape.md` L545–L547; `scouting/koszul-betti.md` §3 (re-checked for the cited K-KB6/K-KB9 and the stochastic-Chebyshev comparator); `claims/CLAIMS.md` REFUTED-row convention (C-155, C-181) and the status legend; the r2 extract of `2005.02607v5` retained in scratch.
- **Network/recomputation this round:** no new fetches were required — the only new external claim is an acronym expansion, checked against the `2005.02607v5` text already extracted in r2 (2317 lines). One `python3` numerical re-derivation of the new three-variable witness; four `grep`/`awk` audits (BQP occurrences, field-name leftovers, status counts, `where-tested`); one lockstep extraction of all 15 section scores against the ranked table.
- **Commands run (all `timeout`-bounded, all exit 0):** `git log`/`git diff`/`git status`; `sed`/`grep`/`awk` ×~14; `python3` ×3 (witness recomputation; row status / `surviving statement` / `where-tested` audit over all 23 rows; SKETCH sourcing audit). No file other than this verdict was created or modified; nothing committed. (`verdicts/koszul-betti-r2.log` is another lane's untracked artifact; I did not touch it.)

Departures from conventions C1–C12: none.

---

## 1. Disposition of the r2 items

Fifteen items were open after r2: the four marked NOT VERIFIED (O7, O9, O10, O21) and the eleven new defects (O26–O36).

| id | claimed | my check | verdict |
|---|---|---|---|
| O7 | FIXED | `grep -n "BQP-hard\|BQP-complete"` over the whole memo returns exactly two hits: line 183, the Gharibian–Le Gall "inverse-polynomial precision can remain BQP-complete" statement (correct, verified r1), and line 2637, the disposition table describing the removal. The unsupported attribution is gone. The Schmidhuber–Lloyd simplices-specification exception survives in §5, in K-QP5 and in `C-NEW-QP-TDA-GENERIC-EXPONENTIAL`; the ranked table's row 5 now reads "DQC1-hard natural generalization and simplices-input exception". | **VERIFIED** |
| O9 | RETRACTED | Former Combination 1 is deleted; the Combinations section opens with a preamble that names `scouting/koszul-betti.md` §3 as the settled analysis and cites K-KB6 and K-KB9 by id. I re-read koszul-betti.md §3: it does price the composition, does compare against stochastic Chebyshev/Lanczos eigenvalue counting, and K-KB6/K-KB9 are its gap-closing and classical-preconditioning killers. The citation is accurate. Only two combinations remain (§1 kinematic synthesis, §2 GBS/Bézout), renumbered consistently, with no dangling cross-reference: §5's former pointer "listed under Combinations §1" now reads "settled prior work in `scouting/koszul-betti.md` §3". | **VERIFIED** |
| O10 | RETRACTED | Same deletion. The preamble records the correct comparator rather than burying it: "The campaign's classical comparator for normalized traces of PSD filters is Hutch++, with O(1/ε) matrix–vector products. Amplitude estimation's O(1/ε) dependence therefore beats naive Hutchinson sampling, not the stated best classical baseline. Any possible advantage must be in the cost of applying the filter at equal accuracy." I checked this against `scouting/classical-landscape.md` L545 ("Hutch++ obtains relative trace error with O(1/ε) matrix-vector products for PSD inputs [R55]") and L547 ("The possible advantage is therefore in the cost of applying the filter, not simply in 'quantum trace estimation.'") — the paraphrase is faithful to both lines. The closing sentence "No honest, arm-disjoint replacement with a falsifiable one-week probe was identified, so none is proposed" is the right answer to a failed probe design under L5. | **VERIFIED** |
| O21 | FIXED | Reference 35 now reads "GPU-Based Homotopy Continuation for Minimal Problems in Computer Vision", character-for-character the arXiv title of 2112.03444 (both v1 and v2, checked in r2). Author remains the corrected Chiang-Heng Chien. | **VERIFIED** |
| O26 | RETRACTED | See O9. The duplicated probe is gone and the duplication is recorded rather than concealed. | **VERIFIED** |
| O27 | RETRACTED | See O10. | **VERIFIED** |
| O28 | FIXED | §5 now reads: "Gyurik–Cade–Dunjko prove that low-lying spectral density estimation is DQC1-hard, remains DQC1-hard for log-local Hamiltonians, and is DQC1-complete when restricted to log-local Hamiltonians; they also prove sparse-weighted eigenvalue [sampling] DQC1-hard (Theorems 1, 2, and 5)", followed by "These are natural generalizations of the LGZ linear-algebraic estimation task. They are evidence of dequantization resistance for the generalization, not for Betti-number estimation itself; the restriction to clique-complex Laplacians remains open." Checked against the paper text: Theorem 1 (llsd DQC1-hard, and for log-local inputs), Theorem 2 (DQC1-complete for log-local inputs), Theorem 5 (swes DQC1-hard) — all three attributions correct, and the delimitation matches both the paper and the independent correction already recorded in `scouting/koszul-betti.md`. The §5 score justification and K-QP5 are updated in lockstep. One residual acronym error, O37 below. | **VERIFIED** |
| O29 | FIXED | See O21. | **VERIFIED** |
| O30 | DOWNGRADED | `grep -n "^- status: HOLD"` returns nothing; the row is CONJECTURE. The decision rule now states the convention explicitly and correctly: "A row whose required composition is missing remains CONJECTURE and is marked `HOLD (do not merge)` in its statement; **HOLD is not an L1 status**." The `missing step:` field is retained. This is the second of the two options r2 offered. One presentational residue, O38 below. | **VERIFIED** |
| O31 | FIXED | I audited all 23 rows programmatically. All 11 REFUTED rows now carry a `surviving statement:` field; the field name `surviving weaker statement:` and the ad-hoc `refuted proposition:` field appear in **no** row. Both target rows now put the false proposition in `statement`, matching the DAG pattern of C-155 and C-181: `C-NEW-QP-MACAULAY-CONDITION-EQUALITY` reads "For every homogeneous tuple (f_j) and every N, the Chen–Gao truncated QLS condition number κ_b(M) equals the seed ratio α_BE/Δ_N" with `surviving statement: C-097 — the two obstructions are analogous and no reduction is known between them`; `C-NEW-QP-ANALOGUE-DEGENERACY` reads "Ground-state energy measurements alone determine HF_{R/I}(N)" with the resource list moved to `surviving statement:`. Both are verbatim the text r2 supplied. | **VERIFIED** |
| O32 | DOWNGRADED | `C-NEW-QP-WITTEN-INDEX-COUNT` is now CONJECTURE with `where-proved: none (composition); DOI 10.4310/jdg/1214437492 supports the de Rham component, DOI 10.1016/0550-3213(89)90474-4 supports the chiral-ring component, and the explicit cancellation witness is S¹, with b₀=b₁=1`. D-jacobian-ring-susy prefixes the display with "The following campaign assertion is [UNVERIFIED]:" and its pitfalls now say "The cited sources identify the chiral ring with the Jacobian quotient but no specific theorem or equation for the displayed ±μ assertion has been supplied." This is exactly the second option r2 offered, and it is the honest one: the ±μ claim entered this campaign through my r1 verdict, not through a quoted theorem, and it is now labelled as such. | **VERIFIED** |
| O33 | FIXED | **Recomputed independently.** With f₁ = z₀, f₂ = (z₀+z₁)/√2 in ℂ[z₀,z₁,z₂] and N = 1: Bombieri–Weyl norms 1.0 and 1.0; H₁ spectrum `[0.0, 0.29289322, 1.70710678]` = {0, 1−1/√2, 1+1/√2}; rank 2, so dim ker H₁ = 1 with kernel eigenvector `[0,0,1]`, i.e. exactly span{z₂}, and HF_{R/I}(1) = 1 as the memo states (I = (z₀,z₁), so R₁/I₁ is one-dimensional); nonzero singular-value squares 1.70710678 and 0.29289322; α_BE = 1+1/√2, Δ₁ = 1−1/√2, ratio 5.828427124746191 = (1+√2)² = 5.82842712474619; κ_b(Φ₁) = 1.000000 on the largest left singular vector in the image and 2.414214 = 1+√2 on the smallest. **Every number in the memo is exact**, and the added qualification "in its image" is the one the non-surjective map requires. The row's `where-proved` carries the same instance verbatim. | **VERIFIED** |
| O34 | FIXED | `C-NEW-QP-UNIT-GROUP` now reads `where-proved: DOI 10.1145/2591796.2591860 (cited theorem)` — the unconfirmable "Theorem 1.2" is gone. `C-NEW-QP-MACAULAY-HHL-UNIFORM` now reads `arXiv:2111.00405 Theorem 4.5 and §1 (cited theorem)`, which is where the Ω(2^{h/2}) clause actually lives. | **VERIFIED** |
| O35 | RESIDUE | Question 16 added: "DAG convention action for the orchestrator: widen the `claims/CLAIMS.md` SKETCH legend to 'a proof or derivation exists in the seed or in a cited published source with a resolved identifier, with no converged critic verdict in this campaign.'" That is verbatim the wording r2 demanded, and `claims/CLAIMS.md` is orchestrator-owned under rule 3, so a residue recorded as an action is the correct disposition. **The merge is blocked on this action**: the 6 SKETCH rows below cannot enter the DAG until the legend is widened. | **VERIFIED (as residue)** |
| O36 | FIXED | §4's justification now audits all five criteria: "It does not earn criterion 4: although low-rank dequantization is not the main issue, no end-to-end quantum advantage has been established whose resistance to dequantization could be credited." The 1/5 score is unchanged, and the reasoning is sound — criterion 4 is about an advantage surviving dequantization, and there is no advantage to survive. | **VERIFIED** |

**Counts: VERIFIED 15 · NOT VERIFIED 0 · NEW DEFECT 3 (O37–O39).**

---

## 2. New objections (changed text only)

### O37 — MINOR. The SWES acronym is expanded wrongly in the replacement sentence.

**Location:** §5 "Dequantization and hidden costs" (line 955).

The memo writes "they also prove **sparse-weighted eigenvalue summation** DQC1-hard (Theorems 1, 2, and 5)". In `2005.02607v5` the object is introduced as "**Sparse weighted eigenvalue sampling (SWES)**", and the paper's point about it is a sampling statement: "Besides being able to efficiently sample from an approximation of swes on a quantum computer, we show that swes requires superpolynomial time on a classical computer". "Summation" is not a synonym here — the distinction between sampling from a distribution and computing a sum is the axis on which this memo's own K-QP7 turns, so the slip is worth removing rather than tolerating.

**FIX DEMAND:** replace "summation" with "sampling".

**SURVIVING STATEMENT:** Theorem 5 does prove swes DQC1-hard, and the attribution of Theorems 1, 2 and 5 is otherwise correct.

---

### O38 — NOTE. The merge directive sits inside the `statement` field.

**Location:** row `C-NEW-QP-TDA-REAL-VARIETY`.

`statement:` now begins "HOLD (do not merge): missing step = VR–Čech interleaving. For every compact smooth positive-reach real variety …". The row already carries a dedicated `missing step:` field with the same content, and under L1 `statement` is the exact mathematical statement with quantifiers, not a procedural instruction. The remainder of the statement is a well-formed conditional and needs no change. Since the orchestrator merges verbatim from §4 below, I supply the cleaned text there and this costs nothing.

**FIX DEMAND:** drop the leading directive from `statement`; keep `missing step:` and `where-proved: none (composition proposed)`.

**SURVIVING STATEMENT:** the row's content — that identifying the VR clique-complex quantity with a persistent Betti number of V_ℝ needs an interleaving and persistence-interval step not supplied — is correct and belongs in the DAG as a CONJECTURE recording the gap.

---

### O39 — NOTE. The decision rule still uses the retired field name.

**Location:** decision rule, line 28.

"REFUTED rows name the surviving weaker statement" — but O31's fix standardised every row on the DAG field name `surviving statement:`. One word of drift between the rule and the rows it governs.

**FIX DEMAND:** "REFUTED rows name the surviving statement."

---

**New-objection counts: 0 FATAL · 0 MAJOR · 1 MINOR (O37) · 2 NOTE (O38, O39).**

---

## 3. Lockstep check

- **Ranked table vs sections.** I extracted all 15 `Score:` lines (§1=2, §2=4, §2A=3, §3=3, §4=1, §5=2, §6=2, §7=2, §8=2, §9=2, §10A=1, §10B=2, §10C=1, §10D=0, §10E=1) and all 15 ranked-table scores (4, 3, 3, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 0). Every primitive's two scores agree; the ranking is monotone; every killer id in the table matches its section. The two rows touched this round (row 5's problem column and killer) match the rewritten §5 text and K-QP5.
- **Rubric vs scores.** All 15 per-criterion justifications sum to their scores, and §4 is no longer silent on criterion 4 (O36).
- **Sections vs rows.** §5's DQC1 delimitation ("for the generalization, not for Betti-number estimation itself") is carried into K-QP5, into the ranked table and into no row that overclaims — the only DQC1-citing row, `C-NEW-QP-TDA-GENERIC-EXPONENTIAL`, does not mention DQC1 at all. The r2 lockstep miss (a section claiming BQP-hardness that no row asserted) is closed. §1's counterexample text and `C-NEW-QP-MACAULAY-CONDITION-EQUALITY`'s `where-proved` now carry the identical instance. The Combinations preamble's Hutch++ statement matches `classical-landscape.md` L545/L547.
- **Statuses and metadata.** 23 rows: SKETCH 6, CONJECTURE 6, REFUTED 11 — matching the memo's own tally. All 23 `where-tested` fields read `none`. All 11 REFUTED rows carry `surviving statement:`. All 6 SKETCH rows cite a published theorem with a resolved identifier, each verified in r1 or r2: arXiv:2111.00405 Thm 4.5 and §1; arXiv:math/0411623 Thm 1; DOI 10.1145/1206035.1206039; DOI 10.1145/2591796.2591860; arXiv:0706.1219; arXiv:0811.0596. No status outside {SKETCH, CONJECTURE, REFUTED}. No row depends on a REFUTED C-row; all cited D-ids and C-ids resolve (14 proposed here, the rest existing, including C-246 and C-097).
- **Combinations vs DAG.** Two combinations remain; neither duplicates a landed lane. Combination 1 (Arm R bet R2 kinematic synthesis) is a probe specification for an arm the PRD already names, with severe pre-stated thresholds; Combination 2 (GBS proposal sampling for multihomogeneous start systems) is untouched since r0 and was not objected to.
- **References.** 73 entries, unchanged in count; the single edit (ref 35's title) is verified against arXiv.

---

## 4. Proposed claim rows: final decisions

The orchestrator merges verbatim from this table. **Merge precondition:** Question 16 (widening the `claims/CLAIMS.md` SKETCH legend, r2 O35) must be executed before the six SKETCH rows are entered; the current legend restricts SKETCH to derivations *in the seed*.

| id | decision | note / exact text |
|---|---|---|
| C-NEW-QP-MACAULAY-HHL-UNIFORM | **ACCEPT AS SKETCH** | Bound, hypotheses, Chen–Gao specialisation and the reduced-system Ω(2^{h/2}) all verified against arXiv:2111.00405 (r1, r2). `where-proved: arXiv:2111.00405 Theorem 4.5 and §1 (cited theorem)`. Keep `note: sharpens C-097`. |
| C-NEW-QP-MACAULAY-CONDITION-EQUALITY | **ACCEPT AS REFUTED** | Statement is the false equality; `surviving statement: C-097 — the two obstructions are analogous and no reduction is known between them.` The witness in `where-proved` is recomputed exact this round (O33). |
| C-NEW-QP-ZETA-CURVE | **ACCEPT AS SKETCH** | Kedlaya Theorem 1; hypotheses are the paper's own input protocol. |
| C-NEW-QP-ZETA-HYPERSURFACE | **ACCEPT AS REFUTED** | `surviving statement:` present; `where-proved: arXiv:math/0411623 §10` verified in r1. |
| C-NEW-QP-PRINCIPAL-IDEAL | **ACCEPT AS SKETCH** | Hallgren, J. ACM 54(1) 2007; the compact-output qualification is part of the statement. |
| C-NEW-QP-UNIT-GROUP | **ACCEPT AS SKETCH** | Eisenträger–Hallgren–Kitaev–Song; "polynomial in the field degree and the logarithm of the absolute discriminant" matches the source abstract; unverifiable theorem number removed. |
| C-NEW-QP-HIDDEN-POLYNOMIAL | **ACCEPT AS SKETCH** | Matches Decker–Draisma–Wocjan verbatim. |
| C-NEW-QP-HIDDEN-EXPLICIT-TRANSFER | **ACCEPT AS CONJECTURE** | "No reduction is known" form; `where-proved: none`. |
| C-NEW-QP-SUSY-HODGE-SPEEDUP | **ACCEPT AS REFUTED** | Hilbert series verified numerically (r1); applications-memo F2 credited; `surviving statement:` present. |
| C-NEW-QP-WITTEN-INDEX-COUNT | **ACCEPT AS CONJECTURE** | Composition, correctly at CONJECTURE with `where-proved: none (composition)` and per-component source attribution; the ±μ clause is flagged [UNVERIFIED] in D-jacobian-ring-susy. |
| C-NEW-QP-TDA-REAL-VARIETY | **ACCEPT WITH REWORDING** | Strip the merge directive from the statement (O38). Exact `statement:` text to merge: *"For every compact smooth positive-reach real variety V_ℝ ⊂ ℝ^a, a sufficiently dense independent sample satisfies the Čech/union-of-balls reconstruction theorem, while the cited quantum resource bound estimates β_{k−1}/|Cl_k| for a Vietoris–Rips clique complex; identifying the latter with a persistent Betti number of V_ℝ requires a VR–Čech interleaving and persistence-interval step not supplied here."* Keep `status: CONJECTURE`, `missing step: VR–Čech interleaving plus a persistence-interval theorem connecting the two scales`, `where-proved: none (composition proposed)`, `where-tested: none`. |
| C-NEW-QP-TDA-GENERIC-EXPONENTIAL | **ACCEPT AS REFUTED** | Source's own NP-hardness wording, input-model restriction, corrected index and simplices exception all present. |
| C-NEW-QP-PATH-AA | **ACCEPT AS CONJECTURE** | Per-invocation error o(√(r/D)); `where-proved: none (conditional composition …)`. |
| C-NEW-QP-PATH-INTERNAL-SPEEDUP | **ACCEPT AS REFUTED** | `surviving statement:` present. |
| C-NEW-QP-MHOM-BEZOUT-PERMANENT | **ACCEPT AS CONJECTURE** | Identity verified numerically in r1 (n = 3, 4, 5); `depends-on: D-multihomogeneous-bezout`. |
| C-NEW-QP-BOSON-COUNT | **ACCEPT AS REFUTED** | `surviving statement:` present. |
| C-NEW-QP-ANALOGUE-DEGENERACY | **ACCEPT AS REFUTED** | Statement is the false proposition; the resource list is now the `surviving statement:`. |
| C-NEW-QP-FIXED-MODE-HARDWARE | **ACCEPT AS CONJECTURE** | Unary-N quantifier; `where-proved: restatement of C-057 and C-099`. |
| C-NEW-QP-ANNEALING-DEMONSTRATION | **ACCEPT AS REFUTED** | Every device number verified against arXiv:2111.13224 in r1. |
| C-NEW-QP-GROEBNER-ANNEALER | **ACCEPT AS REFUTED** | "just over 200 000" verified in r1. |
| C-NEW-QP-QPCA-SECANT | **ACCEPT AS REFUTED** | Output-type argument; `surviving statement:` present. |
| C-NEW-QP-GIBBS-QUADRATIC | **ACCEPT AS SKETCH** | Wocjan et al.'s own FPRAS/MCMC/non-adaptive-cooling hypotheses. |
| C-NEW-QP-VOLUME-EHRHART | **ACCEPT AS REFUTED** | Includes the source's Ω(√d + 1/ε) lower bound; `surviving statement:` present. |

**Row decision counts: ACCEPT AS SKETCH 6 · ACCEPT AS CONJECTURE 5 · ACCEPT AS REFUTED 11 · ACCEPT WITH REWORDING 1 · HOLD 0 · REJECT 0. Total 23.** Two rows proposed in r0 (`C-NEW-QP-ID-KEDLAYA`, `C-NEW-QP-FINITE-FIELD-SEED`) were withdrawn in repair r1 on r1's REJECT decisions and do not enter the DAG.

## 5. Proposed definitions: final decisions

| id | decision | note |
|---|---|---|
| D-boolean-macaulay-solve | **ACCEPT** | Both matrix dimensions and κ_b(M)=‖M‖‖M⁺b‖/‖b‖ verified against arXiv:2111.00405; the "Grover cost is not a condition-number bound" pitfall is the permanent guard against the r0 error. |
| D-curve-zeta-problem | **ACCEPT** | Pitfall records that the class-group/Jacobian operations are constructed from the input protocol, not assumed. |
| D-number-field-ideal-problems | **ACCEPT** | Separates Hallgren's real-quadratic theorem from the arbitrary-degree unit-group theorem; flags the compact-output issue; the "not D-homogeneous-ideal" pitfall keeps §2A's conservative scoping honest. |
| D-hidden-polynomial-structure | **ACCEPT** | Unchanged since r1. |
| D-jacobian-ring-susy | **ACCEPT** | r2's REWORD is satisfied: the ±μ display is prefixed "The following campaign assertion is [UNVERIFIED]" and the pitfalls record that no specific theorem or equation has been supplied for it. |
| D-vr-betti-estimation | **ACCEPT** | β_{k−1}/|Cl_k| convention; Čech-vs-VR pitfall. |
| D-coherent-path-oracle | **ACCEPT** | Per-invocation error pitfall. |
| D-multihomogeneous-bezout | **ACCEPT** | Expansion verified numerically; "not the general BKK mixed volume" pitfall. |
| D-optical-counting-access | **ACCEPT** | Unchanged. |
| D-analogue-degeneracy-readout | **ACCEPT** | Ω(1/ε²) shot bound. |
| D-boolean-residual-energy | **ACCEPT** | 2ⁿ−1 and both quadratization qubit counts verified against arXiv:2111.13224. |
| D-tensor-secant-problem | **ACCEPT** | Unchanged. |
| D-real-variety-gibbs | **ACCEPT** | Wocjan hypotheses in the pitfall. |
| D-toric-lattice-counting | **ACCEPT** | Ω(√d + 1/ε) lower bound in the pitfall. |

**Definition decision counts: ACCEPT 14 · REWORD 0 · REJECT 0. Total 14.**

---

## 6. Trajectory and residual actions

Objection trajectory: r1 — 0 FATAL, 10 MAJOR, 11 MINOR, 4 NOTE (25); r2 — 0 FATAL, 3 MAJOR, 5 MINOR, 3 NOTE (11); r3 — 0 FATAL, 0 MAJOR, 1 MINOR, 2 NOTE (3). Fixed point reached: no FATAL and no MAJOR objection stands.

Every quantitative statement I could recompute or refetch across the three rounds now checks out, including the two that decided rounds 1 and 2 — the Ding et al. condition-number formulas and the Gyurik–Cade–Dunjko hardness delimitation — and the witness introduced in this round, which I re-derived exactly. The lane also produced two by-products worth more than its own rows: the resolution of C-099's `[UNVERIFIED]` mark, and a corrected §2A that prevents any unqualified "Kedlaya is the strongest existing quantum algorithm involving ideals" claim.

The three residual items are cosmetic and are dispatched by the tables above: O37 (one word, "sampling" for "summation"), O38 (resolved by the exact text supplied for `C-NEW-QP-TDA-REAL-VARIETY`), O39 (one word in the decision rule). None blocks the merge.

Blocking on the orchestrator, not on the lane: Question 16 (widen the CLAIMS.md SKETCH legend) must be executed before the six SKETCH rows enter the DAG, and Questions 13–15 (lift C-099's `[UNVERIFIED]` mark; restore `status:` fields on C-275–C-280; record the Kedlaya identifier correction in `refs/`, the worklog and the original lane brief) remain open.

VERDICT: PASS
