<!-- ROLE: adversarial critic adjudication, round 3 (final), on scouting/quantum-native.md (arm D).
     Priors: verdicts/quantum-native-r1.md FAIL(12 MAJOR, 9 MINOR), quantum-native-r2.md
     FAIL(1 FATAL, 1 MAJOR, 5 MINOR). Later-round protocol: priors stand, only changed text is
     attacked. On PASS the orchestrator merges verbatim from the tables below. -->

# Verdict — scouting/quantum-native.md, round 3 (adjudication)

- **Target:** `scouting/quantum-native.md` at `90d5c5c` (2254 lines; 13 rows, 8 `D-QN-*`
  definitions + 1 register amendment, 31 references).
- **Priors:** r1 FAIL(12 MAJOR, 9 MINOR, 0 FATAL) → r2 FAIL(1 FATAL, 1 MAJOR, 5 MINOR).
- **Scope:** `git diff fa71136 90d5c5c -- scouting/quantum-native.md` (47 insertions, 41
  deletions, 13 hunks) plus the memo's `# Repair r2 response` / `## r2` table.
- **Date:** 2026-09-03. **Critic model:** Opus (Claude). **Writable file:** this one only.
  Nothing else edited; nothing committed.

## Commands run (exit codes)

| # | command | exit |
|---|---|---|
| 1 | `git diff -U2 fa71136 90d5c5c -- scouting/quantum-native.md` | 0 |
| 2 | `curl` the Cox–Little–Schenck *Toric Varieties* PDF (863 pp, 5.1 MB) + `pdftotext -layout`, then `grep -n "Proposition 5\.2\.[4-9]"` and read §5.2 and the Chapter 6 appendix verbatim | 0 |
| 3 | OpenLibrary API on ISBN 9780821848197 | 0 |
| 4 | `curl` + `pdftotext` on three secondary sources (arXiv:0810.2042, 1211.2376, 1701.06639) to pin the Valiant `#MONOTONE-2-SAT` locus; WebSearch ×3; WebFetch `epubs.siam.org/doi/abs/10.1137/0208032` (**HTTP 403**, paywalled) | 0 / 403 |
| 5 | `python3` — recheck the corrected copy-residual convention at `(q,n,m) = (2,3,2), (3,2,3), (2,2,4)`: `conj(f_j(\barψ)) = ⟨F_j|ψ^{⊗m}⟩`, `‖F_j‖ = ‖f_j‖_BW`, the expectation identity, and `0 ≤ A_F ≤ 1` | 0 |
| 6 | `grep` census of `where-tested`, `depends-on`, and every `⟨F_j\|` locus in the memo | 0 |

## Disposition verification (O22–O28)

| obj | claimed | verified? | evidence |
|---|---|---|---|
| **O22** (FATAL) | FIXED | **VERIFIED**, with new MINOR O30 | `grep` confirms the string `s00029-024-00935-5` and `Feigin` occur nowhere in the memo: removed from the step-2.4 leaf, the step-4.9 leaf, the `D-QN-MULTIPROJECTIVE-SATURATION` `Source:` line and reference 31. The replacement is real and correctly identified. I downloaded the book and read the propositions verbatim. **Proposition 5.2.6 (The Toric Weak Nullstellensatz)**: "*Let X_Σ be a simplicial toric variety with total coordinate ring S and irrelevant ideal B(Σ) ⊆ S. If I ⊆ S is a homogeneous ideal, then V(I) = ∅ in X_Σ ⟺ B(Σ)^ℓ ⊆ I for some ℓ ≥ 0.*" That is **exactly** the load-bearing empty-case statement of the definition (and stronger than the memo's own two-step derivation). **Proposition 5.2.7 (The Toric Ideal-Variety Correspondence)**: "*Let X_Σ be a simplicial toric variety. Then there is a bijective correspondence {closed subvarieties of X_Σ} ↔ {radical homogeneous ideals I ⊆ B(Σ) ⊆ S}.*" — a genuine ideal–variety correspondence, but normalised differently from `√(I:B^∞)`; see O30. ISBN verified via OpenLibrary: 978-0-8218-4819-7 = Cox, Little, Schenck, *Toric varieties*, AMS, 2011, xxiv+841 pp., LCCN 2010053054. **The fabricated citation is gone and the replacement is a real, correctly-numbered, correctly-attributed pair of propositions.** |
| **O23** (MAJOR) | FIXED | **VERIFIED at the paper level**, with new MINOR O29 | Reference 28 now reads "Leslie G. Valiant, 'The Complexity of Enumeration and Reliability Problems,' DOI:10.1137/0208032", matching Crossref exactly (SIAM J. Comput. **8**, 410–421, 1979); the permanent-paper DOI `10.1016/0304-3975(79)90044-6` occurs nowhere in the memo. The result is confirmed by three independent sources I fetched: arXiv:0810.2042 ("*The following result is from Valiant's seminal paper on #P [6]. #Monotone 2-SAT is #P-complete*"), arXiv:1211.2376 (two independent uses of "#Monotone-2SAT is #P-hard [Valiant]"), and the Wikipedia ♯SAT article. **The wrong-paper defect is fixed.** The added internal locus "Theorem 1, problem 7" is a separate, new issue (O29). |
| **O24** (MINOR) | FIXED | **VERIFIED** | `C-NEW-QN-ARM-D-NORTHSTAR` now carries `- status: CONJECTURE` on its own line and `- hold: do not merge as discharging the PRD §4 Arm D sentence; the broad Arm D negative remains an open negative` as a separate field; the leading `CONJECTURE:` is deleted from the statement. This is exactly the r2 demanded layout and is L1-legal. |
| **O25** (MINOR) | FIXED | **VERIFIED by fresh recomputation** | All three loci now read `\overline{f_j(\overline\psi)} = \langle F_j|\psi^{\otimes m}\rangle` (memo lines 908–912, 1732–1736, 1925); `grep` finds no fourth locus. Recomputed at `(q,n,m) = (2,3,2), (3,2,3), (2,2,4)`: the conjugated form holds to `1e-15` and the unconjugated form fails, in all three; `‖F‖ = ‖f‖_BW` holds (so the C-019 citation is now exactly right); the expectation identity `⟨ψ|^{⊗m}A_F|ψ⟩^{⊗m} = Λ^{-1}Σ_j w_j|f_j(\barψ)|²` holds; and `‖Σ_j w_j|F_j⟩⟨F_j|‖ ≤ Λ`, so `0 ≤ A_F ≤ 1`. |
| **O26** (MINOR) | FIXED | **VERIFIED** | `C-NEW-QN-SINGLET-HILBERT-WITNESS` depends-on is now `C-NEW-QN-QSAT-INVERSE-SYSTEM, C-NEW-QN-HILBERT-VANISH-ENTANGLEMENT, D-macaulay-matrix`; `C-NEW-QN-RESIDUAL-EQUALS-DISTANCE` is `D-QN-COPY-RESIDUAL-OBSERVABLE, D-condition-number`. No `depends-on` field in any of the 13 rows contains a bare convention label. C1 remains cited in the singlet row's statement text ("basis-dependent under C1") and C3 in the prose the residual row's `where-proved` points at. |
| **O27** (MINOR) | FIXED | **VERIFIED** | Step 6.4 now cites `[D-multihomogeneous-bezout]` alone; step 7.3 cites `[arXiv:2412.19623, §5.1, Eq. (16)]`, which is where the intersection-theoretic setup and the equation `[V_1]⋯[V_r] = N H_1^{d_1-1}⋯H_n^{d_n-1}` actually live (extracted from the paper's HTML in r1). Definition 52 is now cited only at 7.4/7.10, for the Bézout coefficient itself. |
| **O28** (MINOR) | FIXED | **VERIFIED** | `grep -c "^- where-tested: none"` = **13**, and no row has any other `where-tested` value. Every pointer to the critic's non-repository scratch computations is gone. This is the conservative branch of the r2 fix (see Lockstep note (e): the provenance should be preserved elsewhere, not in `where-tested`). |

**Score: 7/7 dispositions verified as claimed.** Nothing that passed in r1 or r2 was broken: the diff
is 13 surgical hunks and I re-read every one. Two new MINOR defects, both citation-precision, are
raised below; neither affects the truth of any statement, and both fixes are carried as exact text
in the tables so the merge is clean.

## New objections

### O29 — MINOR — the Valiant internal locus "Theorem 1, problem 7" is unverifiable and unfetched

**Location.** QSAT dictionary, row "Exact `HF_{R/I_Q}(\mathbf1)`", reference cell ("Valiant,
Theorem 1, problem 7"); "Complexity conclusions" bullet 2 ("Valiant 1979, Theorem 1, problem 7,
DOI:10.1137/0208032"); killer **K-QN3** (same). Memo-only text; no DAG row carries it.

**Computation.** `epubs.siam.org/doi/abs/10.1137/0208032` returns **HTTP 403**; the paper is
paywalled and predates arXiv, so neither this critic nor a read-only proposer can have fetched it.
Three secondary sources I did fetch confirm the *result* and the *paper* but none pins Valiant's
internal numbering: arXiv:0810.2042 states "#Monotone 2-SAT is #P-complete" as **its own**
Theorem 1, citing Valiant only as "[6]"; a further search surfaced a source numbering the same
result "Theorem 4.2". A precise sub-locus that cannot be checked, asserted twice in a row after two
rounds of citation defects, is exactly what CLAUDE.md rule 6 exists to stop.

**FIX DEMAND.** Delete "Theorem 1, problem 7" from all three loci, keeping
"Valiant 1979, DOI:10.1137/0208032" (paper-level, Crossref-verified, and the standard citation for
this result). If the sub-locus is wanted, mark it `[UNVERIFIED]` until someone reads the paper.

**SURVIVING STATEMENT.** Computing `HF_{R/I_Q}(\mathbf1)` exactly is `#P`-hard already for qubit
2-QSAT: `#MONOTONE-2-SAT` is `#P`-complete (Valiant 1979, DOI 10.1137/0208032) and its instances sit
inside qubit 2-QSAT directly — a monotone clause `x_i ∨ x_j` is the rank-one 2-local projector
`|00⟩⟨00|`, whose diagonal ground space has dimension equal to the number of satisfying assignments
— so the Ji–Wei–Zeng equivalence (arXiv:1010.2480) is needed only for the converse "no harder than"
direction, not for the hardness. The decision problem remains in P (Bravyi).

### O30 — MINOR — Proposition 5.2.7 is the wrong normalisation, and the hypothesis is not recorded

**Location.** `D-QN-MULTIPROJECTIVE-SATURATION`, sentence "By the multiprojective Nullstellensatz,
`J` is the multihomogeneous vanishing ideal of the reduced closed subscheme `V_{X_0}(I)`" and its
`Source:` line "Cox–Little–Schenck, `Toric Varieties`, Propositions 5.2.6–5.2.7".

**Computation.** Read verbatim from the book. 5.2.6 supports the empty-case sentence exactly. But
5.2.7's normal form for the ideal of a subvariety is a **radical homogeneous ideal contained in
`B(Σ)`**, not the `B`-saturation `√(I:B^∞)` the definition uses; these differ (for `Y = ∅` the
5.2.7 representative is `√B(Σ)`, whereas the definition adopts `R`). The statement that licenses
`√(I:B^∞)` as the canonical representative is elsewhere in the same book: **Proposition 6.A.7**
(Appendix to Chapter 6, "Subschemes and Homogeneous Ideals"): "*Homogeneous ideals `I, J ⊆ S` in the
total coordinate ring of a **smooth** toric variety `X_Σ` give the same ideal sheaf of `O_{X_Σ}` if
and only if `I : B(Σ)^∞ = J : B(Σ)^∞`.*" Separately, **both** 5.2.6 and 5.2.7 require `X_Σ`
**simplicial** — and CLS give an explicit counterexample where 5.2.7 fails without it — while 6.A.7
requires **smooth**. `(P^{q-1})^n` is smooth, hence simplicial, so all three hypotheses hold, but the
entry never says so.

**Why this is MINOR and not a correctness problem.** In the only multidegree the memo uses, the two
normalisations coincide: every monomial of multidegree `\mathbf1` contains a variable from each
block, so `R_{\mathbf1} ⊆ B` and `B_{\mathbf1} = R_{\mathbf1}`; hence
`(I(W) ∩ B)_{\mathbf1} = I(W)_{\mathbf1}`, and in the empty case `(√B)_{\mathbf1} = R_{\mathbf1} =
(R)_{\mathbf1}`. Independently, the substantive identity `√(I:B^∞) = I(V_{X_0}(I))` is true:
`V_a(I:B^∞) = \overline{V_a(I) \setminus V_a(B)}`, and a multihomogeneous form vanishes on
`\overline{π^{-1}(W)\setminus Z(Σ)}` iff it vanishes at every point of `W`. Every use in the memo
(steps 2.4, 2.5, 4.6, 4.9, and `D-QN-PRODUCT-SPAN`) is therefore correct as written, and I verified
step 2.5 and the `e_Q` formula numerically in r1.

**FIX DEMAND.** Replace the `Source:` line by:
`Source: Cox–Little–Schenck, `Toric Varieties`, GSM 124, AMS 2011 (ISBN:978-0-8218-4819-7):
Proposition 5.2.6 (Toric Weak Nullstellensatz) for the empty case, Proposition 5.2.7 (Toric
Ideal-Variety Correspondence), and Proposition 6.A.7 for the B(Σ)-saturation normalisation;
multiprojective use in arXiv:2412.19623.`
and add to `Pitfalls:` the sentence:
`(P^{q-1})^n is smooth, hence simplicial, so the hypotheses of 5.2.6/5.2.7 (simplicial) and 6.A.7
(smooth) are met; 5.2.7 normalises the ideal of a subvariety as a radical ideal contained in B(Σ)
rather than as the B-saturation, and the two agree in multidegree 1 because B_1 = R_1.`

**SURVIVING STATEMENT.** `√(I:B^∞)` is the multihomogeneous vanishing ideal of `V_{X_0}(I)` in
`(P^{q-1})^n`, with `I(∅) = R`; `V_{X_0}(I) = ∅ ⟺ B^ℓ ⊆ I` (CLS 5.2.6) `⟹ I:B^∞ = R`.

## Objection counts (round 3)

**FATAL 0 · MAJOR 0 · MINOR 2 (O29, O30).**
Trajectory: 12 MAJOR + 9 MINOR → 1 FATAL + 1 MAJOR + 5 MINOR → **0 FATAL, 0 MAJOR, 2 MINOR**. The
loop has converged: both residual objections are citation-precision items on correctly-identified
real sources, neither changes any statement's truth, and both fixes are given as exact text below.

---

## FINAL per-row decision table (all 13 rows)

Merge verbatim from the memo's `## Proposed claim rows` section, with the changes stated here.
Statuses are L1-legal throughout (`CONJECTURE` / `REFUTED`); row 13 carries a separate `hold:` field.

| # | id | decision | status | note |
|---|---|---|---|---|
| 1 | `C-NEW-QN-QSAT-INVERSE-SYSTEM` | **ACCEPT AS CONJECTURE** | CONJECTURE | Merge verbatim. Identity verified in r1 on four instances (`q=2,3`; `k=2,3`; clause ranks 1–3): `H_Q = Φ_1Φ_1^†` to `2.3e-16`, `ker H_Q = ((I_Q)_1)^⊥`, `dim ker = HF(1)`. depends-on complete (C-008, C-009, C-033, D-macaulay-map). |
| 2 | `C-NEW-QN-PRODUCT-SPAN-DEFECT` | **ACCEPT AS CONJECTURE** | CONJECTURE | Merge verbatim; the r2 condition is discharged (O22 fixed). Verified in r1 on three random point sets and on the explicit instance `I = (x_0y_0, x_0y_1+x_1y_0)` with `e_Q = 1`. |
| 3 | `C-NEW-QN-HILBERT-VANISH-ENTANGLEMENT` | **ACCEPT AS CONJECTURE** | CONJECTURE | Merge verbatim; r2 condition discharged. Quantifier widened to every multihomogeneous ideal in the Cox ring, `\mathbf r ≠ \mathbf 1` excluded, `I(∅)=R` stated, existential completeness separated from the (open) effective degree bound. |
| 4 | `C-NEW-QN-SINGLET-HILBERT-WITNESS` | **ACCEPT AS CONJECTURE** | CONJECTURE | Merge verbatim (O26 fixed). All numbers recomputed in r1: `HF(1,1)=1` with the singlet as inverse system, `HF(2,2)=0`, `V = ∅`, rank 9, 18 of 220 `9×9` minors nonzero each with `\|det\|=1`, both signs. |
| 5 | `C-NEW-QN-HF2-COMPLETE` | **ACCEPT AS REFUTED** | REFUTED | Surviving statement, merge verbatim: "*Vanishing at `(2,…,2)` is sufficient for the absence of product ground states, but nonvanishing is inconclusive. For five generic four-local rank-one clause vectors on four qubits, `HF(1^4)=11`, `HF(2^4)=11`, `HF(3^4)=1`, and `HF(4^4)=0`; the product variety is empty and the first certifying diagonal level is `r=4`.*" Independently recomputed in r1. |
| 6 | `C-NEW-QN-BEZOUT-NOVELTY` | **ACCEPT AS REFUTED** | REFUTED | Surviving statement, merge verbatim: Definition 52 and Observation 55 of arXiv:2412.19623 / DOI:10.4230/LIPIcs.ITCS.2026.7, plus its perfect-matching remark, already contain the QSAT/PRODSAT count; the permanent formulation is in arXiv:2005.14485 and `D-multihomogeneous-bezout`/C-295, not in arXiv:2412.19623; the earlier product-satisfiability geometry is Laumann et al., DOI:10.1103/PhysRevA.81.062345. Every locus checked against the paper's full text in r1 ("permanent": 0 occurrences). |
| 7 | `C-NEW-QN-COPY-RESIDUAL` | **ACCEPT AS CONJECTURE** | CONJECTURE | Merge verbatim (O25 fixed). All four assertions rechecked in r3 at three parameter settings: the conjugated defining identity, `‖F_j‖=‖f_j‖_BW` (C-019), `0≤A_F≤1` with `Λ=Σ_j w_j‖F_j‖²`, and the expectation identity. Copy cost correctly carries the factor `m` and names access case 1. |
| 8 | `C-NEW-QN-RESIDUAL-EQUALS-DISTANCE` | **ACCEPT AS REFUTED** | REFUTED | Surviving statement, merge verbatim: "*The residual vanishes exactly on `X` when the equations define `X` set-theoretically. Replacing `f_j` by `λf_j` multiplies the left side by `\|λ\|²` and leaves the right side fixed, so no identity can hold for all generating tuples. Quantitative distance bounds require fixed normalization and a condition, reach, or Łojasiewicz constant.*" |
| 9 | `C-NEW-QN-MPS-TOMOGRAPHY-SPEEDUP` | **ACCEPT AS REFUTED** | REFUTED | Surviving statement, merge verbatim. It rests the refutation on the CLAUDE.md §1 / PRD §1 novelty requirement (published prior art) and on the different-output comparator; records that PRD §2 has no novelty criterion and that its criterion 3 makes the input model part of the problem; identifies `Ω(q^n/ε)` as the `r=1` case of Yuen's `Ω(rd/ε)`; and defers the single-copy comparator to Question 6, citing arXiv:2111.05881 and DOI:10.1126/science.abn7293 **without** claiming transfer. All three references fetched and correct. |
| 10 | `C-NEW-QN-COHERENT-OVERLAP-PERMANENT` | **ACCEPT AS REFUTED** | REFUTED | Surviving statement, merge verbatim: Segre product-state overlaps factor as `∏_i⟨x_i\|y_i⟩`; nontrivial permanents arise only from global interferometer transitions that can leave the multidegree sector; C-296 already records the permanent-weighted-sample point; and the QSAT Bézout incidence matrices are nonnegative, so the JSV FPRAS (DOI:10.1145/1008731.1008738) applies and no optical sampling advantage is available for that count. |
| 11 | `C-NEW-QN-OPTICAL-SINGLET-DEMO` | **ACCEPT AS CONJECTURE** | CONJECTURE | Merge verbatim. Preparation recomputed in r1: success probability exactly `1/2`, output `−\|ψ^-⟩`; Hoeffding `log(2/0.05)/(2(1/8)²) = 118.04 → 119`. The `1/4` acceptance is correctly conditioned on the `(1,1)` occupation pattern and on ideal unit-efficiency probe and projector, with unconditioned acceptance `η_sector/4` and the missing ingredients named. depends-on includes C-297. |
| 12 | `C-NEW-QN-C024-WEAKENING` | **ACCEPT AS CONJECTURE** | CONJECTURE | Merge verbatim **including its `lockstep:` field**, and apply Lockstep notes (a)–(b) in the same commit. Source comparison verified in r1: DOI 10.1103/PhysRevLett.92.140403 is "Observation of Spinor **Dynamics** in Optically Trapped ⁸⁷Rb Bose-Einstein Condensates" (Chang, Hamley, Barrett, Sauer, Fortier, Zhang, You, Chapman, PRL 92, 140403, 2004) — no `2N+1` degeneracy measurement. |
| 13 | `C-NEW-QN-ARM-D-NORTHSTAR` | **ACCEPT AS CONJECTURE (hold marker preserved)** | CONJECTURE + `hold:` field | Merge verbatim, keeping `- hold: do not merge as discharging the PRD §4 Arm D sentence; the broad Arm D negative remains an open negative` as its own field (O24 fixed; the status cell is now L1-legal). The row's scope — algorithm families whose only arm-D operation is composition with the relabelling — and its five-item non-coverage list are the r1/r2 demanded scoping. Apply Lockstep note (c) in the same commit. |

**Counts (13):** ACCEPT AS CONJECTURE **8** (rows 1, 2, 3, 4, 7, 11, 12, 13 — row 13 carrying a
`hold:` field) · ACCEPT AS REFUTED **5** (rows 5, 6, 8, 9, 10) · ACCEPT WITH REWORDING **0** ·
HOLD-as-status **0** · REJECT **0** · ACCEPT AS SKETCH **0** (no proposed row is an imported
published theorem, so the C-092/C-099 widened-SKETCH convention does not apply).

## Per-definition decision table

| id | decision | note |
|---|---|---|
| `D-QN-QSAT-IDEAL` | **ACCEPT** | Merge verbatim. The decomposition-independence claim was verified numerically in r2 (6 trials, random unitary rebasing of a rank-2 clause: the two `(I_Q)_1` column spans agree to `1e-9`). The unconjugated-coefficient convention is stated and is what makes `a^†(f)a(f)\|_{R_1} = \|φ⟩⟨φ\|`. |
| `D-QN-MULTIPROJECTIVE-SATURATION` | **REWORD** (exact text below) | Everything except the `Source:` line merges verbatim. Replace the `Source:` line by: "*Source: Cox–Little–Schenck, `Toric Varieties`, GSM 124, AMS 2011 (ISBN:978-0-8218-4819-7): Proposition 5.2.6 (Toric Weak Nullstellensatz) for the empty case, Proposition 5.2.7 (Toric Ideal-Variety Correspondence), and Proposition 6.A.7 for the B(Σ)-saturation normalisation; multiprojective use in arXiv:2412.19623.*" and append to `Pitfalls:`: "*(P^{q-1})^n is smooth, hence simplicial, so the hypotheses of 5.2.6/5.2.7 (simplicial) and 6.A.7 (smooth) are met; 5.2.7 normalises the ideal of a subvariety as a radical ideal contained in B(Σ) rather than as the B-saturation, and the two agree in multidegree 1 because B_1 = R_1.*" (O30) |
| `D-QN-PRODUCT-SPAN` | **ACCEPT** | Merge verbatim; carries both the `(J_Q)_1^⊥` form and the coherent-state form, with `P_Q = {0}` when the variety is empty. Verified in r1. |
| `D-QN-MULTIGRADED-ENTANGLED-DEFECT` | **ACCEPT** | Merge verbatim. Specialisation of `D-entangled-defect`; both displayed expressions agree; verified on an explicit `e_Q = 1` instance. |
| `D-QN-COPY-RESIDUAL-OBSERVABLE` | **ACCEPT** | Merge verbatim (O25 fixed and rechecked in r3). `Λ`, the `0 ≤ A_F ≤ 1` bound, the C-019 norm identity, "acts on `Sym^m(H)`" and "each shot consumes `m` copies" are all correct. |
| `D-QN-TENSOR-NETWORK-VARIETY` | **ACCEPT** | Merge verbatim. Edge-flattening support attributed to arXiv:2608.19071, with arXiv:1501.01120 relabelled as tree-format comparison; the non-closedness pitfall is Landsberg–Qi–Ye's theorem. |
| `D-QN-PHYSICAL-DATA-ACCESS` | **ACCEPT** | Merge verbatim. States that it **extends** the register's `D-input-model`, and fixes the classical copy-access baseline as single-copy, possibly adaptive measurement with classical post-processing. |
| `D-QN-DUAL-RAIL-SECTOR` | **ACCEPT** | Merge verbatim; the postselection-is-not-an-energetic-constraint pitfall is the one the optical row needs. |
| `D-multihomogeneous-bezout amendment` | **ACCEPT** (as an amendment to the existing register entry, **not** a new id) | Amend `definitions/definitions.md:1237` with the general-`q` coefficient `B_D = [t_1^{q-1}⋯t_n^{q-1}]∏_{a=1}^{n(q-1)}(Σ_i d_{ai}t_i)`, the note that at `q=2` this is `per(D)`, and the split attribution (arXiv:2412.19623 Def. 52 / Obs. 55 for the PRODSAT Bézout–weighted-SDR formulation; arXiv:2005.14485 for the permanent formulation). `B_D = per(D)` at `q=2` was recomputed on 40 random 0/1 incidence matrices in r1, as was `B(D) ≤ k^n`. |

**Counts (9):** ACCEPT **8** · REWORD **1** (`D-QN-MULTIPROJECTIVE-SATURATION`) · REJECT **0**.
`D-QN-PRODUCT-BEZOUT-NUMBER` was withdrawn by the proposer in r2 and is not adjudicated.

## Lockstep notes — orchestrator-side edits that must accompany the merge

**(a) `claims/CLAIMS.md`, row C-024 (currently SKETCH).** Replace the final sentence of the
statement. Exact new statement:

> The operator of C-023 is the spin-mixing Hamiltonian of a spin-1 spinor Bose–Einstein condensate
> in the single-mode approximation (Law–Pu–Bigelow 1998, arXiv:cond-mat/9807258,
> DOI 10.1103/PhysRevLett.81.5257) under `(z_0, z_1, z_2) ↔ (a_{+1}, a_{-1}, a_0)`; its
> ferromagnetic phase has exactly `2N+1` degenerate ground states, which is `HF_{R/(f)}(N)` for the
> conic. The INTERACTION has been physically realised and its spin-changing dynamics observed
> (Chang et al. 2004, DOI 10.1103/PhysRevLett.92.140403); a direct experimental measurement of the
> `2N+1` ground-space dimension has NOT been identified, so the former clause "this quadric ideal's
> ground space has already been realised experimentally" is WITHDRAWN.

Also: status stays `SKETCH`; `depends-on` += `C-297`; append to `referee:` — "weakened 2026-09-03
by C-NEW-QN-C024-WEAKENING (verdicts/quantum-native-r1.md O9; r3 lockstep)"; and in
`north-star relevance` replace "the campaign's only existing physical realisation of a
projective-variety ground space" by "the campaign's only existing physical realisation of the
INTERACTION whose ground space is a projective-variety ground space; the degeneracy readout is not
demonstrated".

**(b) `PRD.md` line 66 (§4, Arm A).** Replace
"Hardware: Bose–Hubbard and spinor-BEC spin mixing for quadric generators (row C-024, unrefereed)."
by:

> Hardware: Bose–Hubbard and spinor-BEC spin mixing for quadric generators (row C-024, weakened
> 2026-09-03 by C-NEW-QN-C024-WEAKENING: the interaction is realised and its spin-changing dynamics
> observed, but the `2N+1` degeneracy has not been measured).

**(c) `PRD.md` lines 88–89 (§4, Arm D).** Replace "Products are new statements about QSAT, plus
possibly an analogue demonstration; a speedup in the north-star sense is not on offer here and the
arm should say so." by:

> Products are new statements about QSAT, plus possibly an analogue demonstration. The arm reports
> (2026-09-03, `scouting/quantum-native.md`, critic loop r1–r3): no north-star speedup is
> established. What is argued is only that composing an algorithm with the QSAT–inverse-system
> relabelling supplies no asymptotic advantage (C-NEW-QN-ARM-D-NORTHSTAR, CONJECTURE, held) — a
> tautology about a spectrum-preserving relabelling, not an impossibility theorem. The broad
> negative "no arm D speedup exists" is NOT proved and remains an open negative; it explicitly
> excludes the bosonic Proposition 8.2 sector (C-129/C-130), copy-access membership and distance
> testing for entanglement, secant, MPS and tensor-network varieties, and structured QSAT
> subfamilies. For copy-access problems the comparator is adaptive single-copy measurement plus
> classical post-processing; exponential separations against it exist for other learning tasks
> (arXiv:2111.05881; DOI 10.1126/science.abn7293) but no transfer to variety membership is known.

**(d) HANDOFF.** The row's `lockstep:` field names HANDOFF, but `grep -n "C-024\|spinor" HANDOFF.md`
returns nothing — the item is currently vacuous. Either add a line recording the C-024 weakening or
strike HANDOFF from the field on merge; do not leave the field naming an artifact it does not touch.

**(e) `where-tested` provenance.** All 13 rows merge with `where-tested: none`, which is the honest
value (O19 residue: a read-only lane cannot ship an L4 checker). Recommend adding, per row, a
`critic:` line — e.g. "recomputed independently in verdicts/quantum-native-r1.md §Recomputation
record (r3 §Disposition verification for the copy-residual convention)" — so the provenance of the
numbers is not lost while `where-tested` stays honest. Rows 1 and 4 remain the two cheapest L4
targets if a checker seat is ever funded.

**(f) Decision record.** Add a `D19` row to `PRD.md` §6 recording: arm D converged (r1
FAIL(12 MAJOR, 9 MINOR) → r2 FAIL(1 FATAL, 1 MAJOR, 5 MINOR) → r3 PASS); 13 rows merged (8
CONJECTURE, 5 REFUTED, 1 of the CONJECTURE rows held); 8 definitions plus one
`D-multihomogeneous-bezout` amendment; verdict of the arm — the QSAT ground space **is** the
multidegree-`1` piece of a Macaulay inverse system (exact, verified numerically), product ground
states **are** the points of a multiprojective variety with an entangled defect `e_Q`, and
diagonal Hilbert-function vanishing is a multihomogeneous Nullstellensatz hierarchy of
product-unsatisfiability certificates whose level 2 is incomplete (first certifying level `r = 4`
on the generic four-qubit family) — but no PRD §2 criterion 3 is met, the product-satisfiability
geometry is prior art (Laumann et al. 2010; Aldi–Gharibian–Rudolph 2026), and arm D is an
instrument and a dictionary, not a speedup candidate. The two open items TJO must rule on are
Question 4 (does an exponential copy saving count) and Question 13 (should novelty become an
explicit PRD §2 criterion).

**(g) Memo-only fix, not a merge blocker.** O29's deletion of "Theorem 1, problem 7" touches the
dictionary reference cell, the Complexity-conclusions bullet and K-QN3 — memo text that no DAG row
carries. Apply it to `scouting/quantum-native.md` at merge time; nothing in the tables above depends
on it.

## LOCKSTEP

**Dictionary table** — moved with the rest: the Valiant cell and the `#MONOTONE-2-SAT` wording
track K-QN3 and Complexity conclusions exactly (all three now identical, modulo O29).
**North-star section** — unchanged in this round and consistent with row 13's scope and `hold:`
field. **Killers** — K-QN3 updated in step with the dictionary; K-QN15/16/17 unchanged and still
citing the live rows C-296, C-298, C-041/C-043/C-044. **Rows** — 13, statuses L1-legal, all
`where-tested: none`, no `depends-on` containing a convention label, no REFUTED row cited as
authority. **Definitions** — 8 + 1 amendment; `D-QN-MULTIPROJECTIVE-SATURATION` is the only one
needing an edit before merge. **Verdict: lockstep is intact across all five artifacts**, with the
three orchestrator-side edits (a), (b), (c) required in the merge commit.

VERDICT: PASS
