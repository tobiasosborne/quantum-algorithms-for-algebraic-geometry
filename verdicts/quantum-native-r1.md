<!-- ROLE: adversarial critic verdict, round 1, on scouting/quantum-native.md (arm D).
     Written under rk-light L5. Nothing in this file changes a status; the orchestrator
     merges from the adjudication tables below. -->

# Verdict — scouting/quantum-native.md, round 1

- **Target:** `scouting/quantum-native.md` at commit `a0a9a6d` (2166 lines, 12 proposed rows
  `C-NEW-QN-*`, 9 proposed definitions `D-QN-*`, 30 references, 17 killers `K-QN1..17`).
- **Date:** 2026-09-03.
- **Critic model:** Opus (Claude), adversarial critic seat, brief `briefs/critic-quantum-native-r1.md`.
- **Proposer:** codex `gpt-5.6-sol` (lane brief `briefs/lane-quantum-native.md`).
- **Writable file:** this file only. No other file was edited; nothing was committed.

## Files read

`CLAUDE.md`; `PRD.md` (§1, §2, §3, §4 arms A–E/R/X, §5, §6 D1–D18, §7 Q1–Q13);
`definitions/definitions.md` (frozen conventions C1–C12; `D-polynomial-ring`, `D-fock-space`,
`D-fock-basis`, `D-sphere-norm`, `D-bombieri-weyl-norm`, `D-norm-comparison`, `D-inverse-system`,
`D-projectors`, `D-multidegree-sector`, `D-quantum-k-sat`, `D-hard-core-generators`,
`D-coherent-state`, `D-coherent-gram-matrix`, `D-entangled-defect`, `D-takagi-factorisation`,
`D-input-model`, `D-hardness-anchors`, `D-reserved-photonic`, `D-multihomogeneous-bezout`,
`D-optical-counting-access`, `D-analogue-degeneracy-readout`, `D-boolean-residual-energy`);
`claims/CLAIMS.md` (header/status legend, §3 C-019–C-039, §4 C-040–C-051, C-008/C-009,
C-024, C-044, C-057, C-099, C-118–C-121, C-125–C-131, C-216–C-220, C-295–C-303, DAG section,
"Critical claims for the north star"); `scouting/quantum-native.md` (whole);
`briefs/lane-quantum-native.md`; `scouting/applications-wide-net.md` (Observations A/B, §2.15,
shortlist); `scouting/classical-landscape.md` (§12 index); `briefs/critic-quantum-native-r1.md`.

## URLs fetched (all 2026-09-03)

arXiv abstract pages: `quant-ph/0602108`, `1302.0290`, `2401.02368`, `1010.2480`, `1010.3060`,
`2412.19623` (+ `arxiv.org/html/2412.19623v2`, 1.36 MB, grepped locally), `2201.01824`,
`2206.11185`, `1105.4449`, `1105.2390`, `1109.0221`, `1210.2812`, `1904.07563`, `2101.03148`,
`1501.01120`, `2608.19071`, `math/0410604`, `math/0601452`, `1801.02662`, `1508.01907`,
`0911.1393`, `2005.14485`, `1011.3245`, `cs/0405021`, `quant-ph/0007058`, `cond-mat/9807258`.
DOI resolution: `doi.org/10.4230/LIPIcs.ITCS.2026.7` → `drops.dagstuhl.de/entities/document/…`
(fetched); Crossref REST (`api.crossref.org/works/…`) for `10.1145/1008731.1008738`,
`10.1145/2512329`, `10.1103/PhysRevLett.92.140403`, `10.1038/35051009`, `10.1007/s003400000484`,
`10.1103/PhysRevA.84.042338`, `10.1103/PhysRevLett.107.040501`, `10.1103/PhysRevA.83.050301`,
`10.1088/1751-8113/45/10/105304`, `10.3842/SIGMA.2014.095`, `10.1142/S0219199722500596`,
`10.1007/s10231-011-0238-6`, `10.1038/s41567-024-02535-8`, `10.1103/PhysRevLett.81.5257`,
`10.1103/PhysRevA.81.062345`.

## Commands run (exit codes)

| # | command | exit |
|---|---|---|
| 1 | `grep -o "arXiv:…" scouting/quantum-native.md \| sort \| uniq -c` (citation census) | 0 |
| 2 | `grep`-loop auditing every `D-*` / `C-###` cited by the memo against the register and the DAG | 0 |
| 3 | `curl api.crossref.org/works/<doi>` × 15 + local `python3` field extraction | 0 |
| 4 | `curl -sL arxiv.org/html/2412.19623v2 -o /tmp/agr.html` then keyword census and context extraction | 0 |
| 5 | `python3 scratchpad/qn_check.py` (memo steps 1.8/1.13/1.14/1.17, C3 conjugation, §5 singlet, §6 four-qubit family, §7 Bézout/permanent, Hoeffding) | **0** |
| 6 | `python3 scratchpad/qn_check2.py` (memo 2.5/2.6/2.7/2.8 product span and entangled defect, diagonal HF profile) | **0** |

Both scripts are red-capable (each assertion exits nonzero on violation) and are written so that
their assertions encode the **corrected** statements; they are not proposed as `checkers/` entries
here, because L4 requires a mutation record, which is the proposer's job (objection O19).
They live at `scratchpad/qn_check.py`, `scratchpad/qn_check2.py`.

## Reference table

Every reference the memo lists or cites, checked for existence, authors, title, year, and whether
the theorem the memo attributes is what the source states.

| # | ref as cited by memo | id | resolves | attribution correct | note |
|---|---|---|---|---|---|
| 1 | Bravyi, "Efficient algorithm for a quantum analogue of 2-SAT" | arXiv:quant-ph/0602108 | yes | **yes** | 2006. Abstract: qubit 2-QSAT in P; k≥4 QMA₁-complete. Memo 1.20 / C-034 correct; memo does not misstate the qubit restriction. |
| 2 | Gosset–Nagaj, "Quantum 3-SAT is QMA1-complete" | arXiv:1302.0290 | yes | **yes** | 2013; abstract itself states completeness. Memo 1.21, K-QN2, 8.7 correct. |
| 3 | Rudolph–Gharibian–Nagaj | arXiv:2401.02368 | yes | **yes** | Full title is "…: Direct embeddings and black-box simulation" (memo truncates the subtitle). (2,5)-QSAT QMA₁-complete confirmed. |
| 4 | Ji–Wei–Zeng | arXiv:1010.2480, DOI 10.1103/PhysRevA.84.042338 | yes | **NO — see O1** | Abstract says the degeneracy problem "is as hard as, but no harder than, its classical analog". No `#P` statement anywhere. Memo asserts `#P`-complete in three places. |
| 5 | Chen–Chen–Duan–Ji–Zeng no-go | arXiv:1004.3787, DOI 10.1103/PhysRevA.83.050301 | yes | n/a | Listed; **never cited in the body**. |
| 6 | Brown–Flammia–Schuch | arXiv:1010.3060, DOI 10.1103/PhysRevLett.107.040501 | yes | yes | "difficulty of both problems is exactly captured by a class which we call #BQP"; also #BQP ⊆ #P. Memo's "#BQP-complete" reading acceptable. |
| 7 | Aldi–Gharibian–Rudolph, "An unholy trinity" | arXiv:2412.19623; DOI 10.4230/LIPIcs.ITCS.2026.7 | yes (DOI → Dagstuhl, ITCS 2026, LIPIcs vol. 362, art. 7) | **partly — see O6** | HTML grep: "Bézout" ×104, "multi-homogeneous" ×107, "SDR" ×435, "Laumann" ×4; **"permanent" ×0, "Macaulay" ×0, "inverse system" ×0, "apolar" ×0**. Def. 52 is verbatim the memo's `B_Q`; Obs. 55 = "number of weighted SDRs equals Bézout number"; the permanent appears only as "counts the number of perfect matchings in said graph". |
| 8 | Soleimanifar–Wright, "Testing matrix product states" | arXiv:2201.01824 | yes | **yes** | `O(nr²)` copies "independent of the dimensions of the qudits"; `Ω(n^{1/2})` lower bound for r≥2. |
| 9 | Landsberg–Qi–Ye | arXiv:1105.4449 | yes | yes | "the limit of tensors in a space of tensor network states need not be a tensor network state"; supports K-QN9. |
| 10 | Bernardi–Carusotto | arXiv:1109.0221, DOI 10.1088/1751-8113/45/10/105304 | yes | yes | Full title "…: an application to spin squeezed states" (memo truncates). The memo's correction of the brief's `arXiv:1105.2390` is **right**: 1105.2390 is Chen–Bale–Salem–Mozer, "Frame Dependence of the Electric Field Spectrum of Solar Wind Turbulence" (2011), an unrelated space-physics paper. |
| 11 | Critch–Morton | arXiv:1210.2812, DOI 10.3842/SIGMA.2014.095 | yes | yes | Trace varieties, periodic/open boundary conditions — matches the memo's sentence. |
| 12 | Bernardi–De Lazzari–Gesmundo | arXiv:2101.03148, DOI 10.1142/S0219199722500596 | yes | yes | Comm. Contemp. Math. 25 (2022). |
| 13 | Hoşten–Chakrabarty Paul–Schmidt–Skurt | arXiv:2608.19071 | yes (19 Aug 2026) | yes | "prime ideals of these varieties are generated by minors of matrix flattenings" — supports the tree-flattening sentence and `D-QN-TENSOR-NETWORK-VARIETY`. |
| 14 | Buczyńska–Buczyński–Michałek | arXiv:1501.01120 | yes | **over-cited — O17** | arXiv title is "Hackbusch Conjecture on tensor formats"; it compares tree formats, it does not supply "edge-flattening descriptions". |
| 15 | Ye–Lim, "Tensor network ranks" | arXiv:1801.02662 | yes | n/a | Listed; **never cited in the body**. |
| 16 | Hillar–Lim | arXiv:0911.1393, DOI 10.1145/2512329 | yes (JACM 60(6), 2013) | **partly — O17** | Proves NP-hardness of rank and best **rank-1** approximation of 3-tensors; the memo also cites it for "border-rank optimization … NP-hard", which is not in the source. |
| 17 | Landsberg–Weyman | arXiv:math/0601452 | yes | yes | Ideals of secants of Segre. |
| 18 | Landsberg–Ottaviani | arXiv:1111.4567, DOI 10.1007/s10231-011-0238-6 | yes | yes | Ann. Mat. Pura Appl. 192 (2013). |
| 19 | Yuen | arXiv:2206.11185 | yes | yes | `Ω(rd/ε)` for rank-r mixed states; at r=1 this is the `Ω(q^n/ε)` the memo uses. The memo should say "the r=1 case of". |
| 20 | O'Donnell–Wright | arXiv:1508.01907 | yes | n/a | Listed; **never cited in the body**. |
| 21 | Allman–Rhodes | arXiv:math/0410604 | yes | yes | Phylogenetic ideals, general Markov model. |
| 22 | Bartzos–Emiris–Schicho | arXiv:2005.14485 | yes | yes | Explicitly "leverages a matrix permanent formulation" for m-Bézout bounds. This — **not** ref. 7 — is where the permanent form actually lives. |
| 23 | Aaronson–Arkhipov | arXiv:1011.3245 | yes | yes | Linear optics / permanents of submatrices. |
| 24 | Jerrum–Sinclair–Vigoda | DOI 10.1145/1008731.1008738 | yes (JACM 51, 2004) | yes | FPRAS for nonnegative permanents; K-QN15's argument is sound. |
| 25 | Knill–Laflamme–Milburn | DOI 10.1038/35051009 | yes (Nature 409, 2001) | yes | |
| 26 | Calsamiglia–Lütkenhaus | arXiv:quant-ph/0007058, DOI 10.1007/s003400000484 | yes (Appl. Phys. B 72, 67–71, 2001) | yes | "not possible to discriminate unambiguously four equiprobable Bell states with a probability higher than 50 %". The memo's follow-on "that limitation does not prevent identifying the singlet signature" is true but **uncited**. |
| 27 | Law–Pu–Bigelow | arXiv:cond-mat/9807258, DOI 10.1103/PhysRevLett.81.5257 | yes (PRL 81, 5257, 1998) | yes | |
| 28 | Chang et al. | DOI 10.1103/PhysRevLett.92.140403 | yes (PRL 92, 140403, 2004; Chang, Hamley, Barrett, Sauer, Fortier, Zhang, You, Chapman) | yes | Observes spinor **dynamics**, not a `2N+1` degeneracy — which is exactly the memo's own point, and the basis of O9. |
| 29 | "Changhyoup Oh" et al. | arXiv:2306.03709, DOI 10.1038/s41567-024-02535-8 | yes | **author name wrong** | First author is **Changhun** Oh (Nature Physics 20, 2024). Listed; **never cited in the body**. |
| 30 | Malajovich–Meer | arXiv:cs/0405021 | yes | n/a | Listed; **never cited in the body**. Relevant to §7 (optimal m-Bézout number is NP-hard, not in APX) and unused. |
| — | Czapliński–Michałek–Seynnaeve | arXiv:1904.07563 | yes | yes | **Cited in the body, absent from the reference list.** |

**Summary: 30 listed + 1 body-only = 31 identifiers; 31/31 resolve; 0 fabricated; 1 substantive
misattribution (ref. 4, O1); 1 partial misattribution (ref. 7 on the permanent, O6); 2 over-
attributions (refs. 14 and 16, O17); 1 wrong author name (ref. 29); 2 truncated titles (refs. 3, 10);
5 listed-but-uncited (refs. 5, 15, 20, 29, 30); 1 cited-but-unlisted (1904.07563).** The memo's own
correction of the brief's `arXiv:1105.2390` is confirmed correct.

## Recomputation record

Independent recomputation, not a re-reading of the memo. Numbers below are the critic's.

**(a) The QSAT / inverse-system identification.** Built four QSAT instances directly from random
orthonormal clause vectors — `(n,q,k,ranks)` = `(4,2,2,[1,2,1])`, `(3,3,2,[2,1,3])`,
`(5,2,{3,3,2},[3,2,1])`, `(3,2,2,[2,1])` — assembled `H_Q = Σ_a Π_a ⊗ 1` in the computational basis
and, independently, the multidegree-**1** Macaulay map `Φ_1` of `D-macaulay-map`/`D-multidegree-sector`.
Verified to machine precision in all four: `H_Q = Φ_1 Φ_1^†` (max `|Δ|` ≤ 2.3e-16, memo 1.13);
`ker H_Q = ((I_Q)_1)^⊥` (max overlap ≤ 1.3e-13, memo 1.14);
`dim ker H_Q = q^n − rank Φ_1 = HF_{R/I_Q}(1)` (memo 1.17; e.g. `q=3,n=3`: dim ker `= 9 = 27 − 18`).
Also verified memo 1.8 directly: with the **unconjugated** coefficient association of 1.6,
`a^†(f)a(f)|_{R_1} = |φ⟩⟨φ|_S ⊗ 1` exactly. **The identification of steps 1.1–1.18 is correct.**

**(b) The conjugation / notation counter-check.** For a complex `|φ⟩`, built both `I_Q` and
`conj(I_Q)` and compared `((I_Q)_1)^⊥` with `((\overline{I_Q})_1)^⊥`: the two subspaces are
**different** (their principal angles are not zero). Consequence in O4.

**(c) Two-qubit singlet (memo 5.1–5.8).** `HF(1,1) = 4 − 3 = 1`; the inverse-system line is the Bell
singlet (overlap 1 to 1e-16); `HF(2,2) = 0` (dim `R_{(2,2)} = 9`, Macaulay rank 9 from the 12
products). Enumerated **all 220** `9×9` minors: 18 are nonzero. With the **unnormalised** generator
`x_0y_1+x_1y_0` every nonzero minor has `det = ±1` (both signs occur). With the memo's own §5.2
generator `(x_0y_1+x_1y_0)/√2` the nonzero minors have `|det| ∈ {0.25, 0.353553, 0.5}` and **never 1**.
See O11.

**(d) Four qubits, five generic `(1,1,1,1)` clauses (memo 6.1–6.8).** Diagonal Hilbert profile,
random complex generic coefficients:
`HF(1,1,1,1) = 11` (16 − 5), `HF(2,2,2,2) = 11` (81 − 70), `HF(3,3,3,3) = 1` (256 − 255),
`HF(4,4,4,4) = 0` (625 − 625). So `V = ∅` is confirmed (level-4 Nullstellensatz certificate), the
memo's `HF(2,2,2,2) ≥ 1` is correct, and its refutation of `HF(2,…,2) > 0 ⇒ product solution`
stands. But the memo's bound "at most 5·16 = 80" is 11-fold loose (actual `HF(2,2,2,2) = 11`), and
the **first certifying level for this family is r = 4, not 2 and not 3** (O18).

**(e) Multiprojective Bézout (memo 7.4–7.6).** For 40 random `n×n` 0/1 incidence matrices,
`n ∈ [2,5]`: `[t_1⋯t_n]∏_a(Σ_i d_{ai}t_i) = per(D)` in every case (memo 7.5), and `B(D) ≤ k^n` with
`k` the max row weight (memo 7.6). Separately, four generic `(1,1,1,1)` forms on `(P^1)^4`:
`HF` = 23, 24, 24, 24 at `r = 2,3,4,5` — the multiprojective degree is **24 = 4!**, confirming 6.4.

**(f) Product span and entangled defect (memo 2.5–2.8).** For random finite point sets in
`(P^{q-1})^n` (`(n,q,|X|)` = `(3,2,4)`, `(2,3,5)`, `(4,2,6)`): `span{⊗_i|\bar x_i⟩} = ((I(X))_1)^⊥`
exactly (dimensions add to `q^n`, cross-overlaps ≤ 1e-9). Explicit nonzero defect:
`I = (x_0y_0,\; x_0y_1+x_1y_0)` on `P^1×P^1` has `dim(I)_1 = 2`, `dim ker H = 2`,
`V = {([0{:}1],[0{:}1])}` (case analysis: `x_0=0 ⇒ x_1≠0 ⇒ x_1y_0=0 ⇒ y_0=0`; `y_0=0 ⇒ x_0y_1=0 ⇒
x_0=0`), `dim(J)_1 = 3`, so `e_Q = 1`, product span `= span{|11⟩}`, and the surviving ground
direction is the singlet. **Memo 2.5–2.8 are correct.**

**(g) Shot counts.** `log(2/0.05)/(2·(1/8)^2) = 118.0441`, so 119 shots — memo correct. For `n`
qubits at degeneracy `g = O(1)`, the Bernoulli variance is `p(1−p)` with `p = g/2^n`, so the
sampling cost is `Θ(g·2^n)`, not `Θ(4^n)`, and amplitude estimation needs `Θ(√p/ε) = Θ(2^{n/2})`
queries, not `Θ(2^n)`. The memo's `Θ` values are correct only in the worst case over `g` (O16).

---

## Objections

### O1 — MAJOR — `#P`-completeness of 2-QSAT degeneracy is misattributed

**Location.** QSAT dictionary row "Exact `HF(1)`", classical column: "`#P`-complete even for qubit
2-QSAT (arXiv:1010.2480)"; "Complexity conclusions" bullet 2; killer K-QN3.

**Fetched statement.** arXiv:1010.2480 / DOI 10.1103/PhysRevA.84.042338 (Ji–Wei–Zeng, PRA 84,
042338): "*This characterization allows us to show that the problem of determining the ground state
degeneracy is as hard as, but no harder than, its classical analog.*" There is no occurrence of
`#P` in the abstract and no complexity-class completeness statement. The paper proves an
**equivalence to a classical counting problem**, not a `#P`-completeness.

**Aggravating.** The campaign register already carries the correct anchor: `D-hardness-anchors`
records that exact `HF` evaluation is `#P`-hard *via edge ideals / independence polynomials
(Dickenstein–Tobis arXiv:1003.3508)*, together with the explicit pitfall that the `#P`-hardness is
**not** via the route people usually assume. The memo cites neither `D-hardness-anchors` nor
Valiant.

**FIX DEMAND.** Replace the three occurrences by: "computing `HF_{R/I_Q}(1)` exactly is `#P`-hard
already for qubit 2-QSAT, by Ji–Wei–Zeng's reduction to and from the classical analogue
(arXiv:1010.2480, DOI 10.1103/PhysRevA.84.042338) composed with `#P`-completeness of `#2-SAT`
(Valiant 1979, DOI 10.1016/0304-3975(79)90044-6)", and cite `D-hardness-anchors`. If Valiant is
not fetched, mark `[UNVERIFIED]` per rule 6. Do not write "`#P`-complete" without a containment
argument.

**SURVIVING STATEMENT.** Exact ground-space degeneracy of qubit 2-QSAT is equivalent (both
directions) to its classical counting analogue [Ji–Wei–Zeng]; the decision problem is in P
[Bravyi], so decision and counting separate here.

### O2 — MAJOR — the dictionary asserts `QMA₁`-completeness for the *exact* problem, which C-038/C-217 forbid

**Location.** QSAT dictionary, row "`HF_{R/I_Q}(1) > 0` | **Exact frustration freeness** | In P for
qubit 2-QSAT; `QMA₁`-hard for qubit 3-QSAT | **`QMA₁`-complete**, not known in BQP".

**Computation.** The row's object is labelled *exact* and its complexity columns are the *promise*
complexities. C-038 (SKETCH, seed Prop 3.1e) states verbatim: "Without the NO-gap promise, exact
vanishing of the Hilbert function at multidegree `(1,...,1)` is NOT thereby placed in `QMA_1`", and
C-217 is the REFUTED draft with surviving statement C-038 + C-034–C-037. The memo's own
"Complexity conclusions" says "C-217 remains binding", and its own step 1.19 correctly states the
*promise* form. The table therefore contradicts the memo's body and the DAG.

**FIX DEMAND.** Split the row into two: (i) "promise problem [`HF(1) > 0`] vs
[`λ_min ≥ 1/poly(n)`]" carrying the P / `QMA₁`-complete entries and citing C-034–C-037; (ii)
"exact `HF(1) > 0`, no promise" carrying "in P for qubit 2-QSAT (Bravyi); not thereby in `QMA₁`
(C-038)". Add C-038 to the dictionary's reference column.

**SURVIVING STATEMENT.** Steps 1.19–1.23 are correct as written; only the table row is wrong.

### O3 — MAJOR — three REFUTED rows are cited as binding authority

**Location.** Step 2.10 leaf "[C-029, **C-216**]"; "Complexity conclusions": "**C-217** remains
binding"; "**C-219** remains binding".

**Computation.** `grep` of `claims/CLAIMS.md`: C-216, C-217, C-219 all have `status: REFUTED` and
sit in the "Refuted draft claims" section. Their surviving statements are, respectively, C-029;
C-038 together with C-034–C-037; and C-041/C-043/C-178 with C-044 the only survivor. Under L1 a
REFUTED row is kept as a record of a killed draft, not as an authority. Citing one in a Lamport
leaf (L3: "every leaf citing a definition id, a claim id, or a named checker run") without marking
it REFUTED makes the argument unauditable and inverts the sense of C-216 in particular, whose
statement is the *false* claim that degreewise equality means saturated-and-radical.

**FIX DEMAND.** Rewrite as: 2.10 leaf → `[C-029]` (optionally "; the contrary draft claim is
REFUTED as C-216"); "C-217 remains binding" → "C-038 (with C-034–C-037) remains binding; the
contrary draft is REFUTED as C-217"; "C-219 remains binding" → "C-041/C-043 remain binding, with
C-044 the only few-mode survivor; the contrary draft is REFUTED as C-219". Apply the same rule to
every future leaf.

**SURVIVING STATEMENT.** The three sentences the memo intends are all true when stated against the
surviving rows.

### O4 — MAJOR — the flagship row's second equality is false under the register's `⊥`

**Location.** `C-NEW-QN-QSAT-INVERSE-SYSTEM` statement:
`ker H_Q = ((I_Q)_{\mathbf 1})^⊥ = (\overline{I_Q}^{\,⊥})_{\mathbf 1}`; also memo step 1.16
"`ker H_Q = (I_Q^⊥)_{\mathbf 1}`".

**Computation.** `D-inverse-system` fixes `(I_N)^⊥` to mean **the orthogonal complement of `I_N` in
`R_N`**, and then *observes* that this equals the degree-`N` part of the inverse system of `\bar I`.
Read in that register notation, `(\overline{I_Q}^{\,⊥})_{\mathbf 1}` is `((\overline{I_Q})_{\mathbf
1})^⊥`. Recomputation (b): for a random complex rank-one clause on 2 of 3 qubits, the subspaces
`((I_Q)_1)^⊥` and `((\overline{I_Q})_1)^⊥` are distinct. So the displayed chain of equalities is
**false as written**; only the memo's informal reading ("the apolar dual, without conjugation, of
the conjugated ideal") is true. `I_Q^⊥` in 1.16 is never defined at all, and L2 forbids an artifact
introducing a second meaning for a register symbol.

**FIX DEMAND.** State the row without inventing notation:
"`ker H_Q = ((I_Q)_{\mathbf 1})^{⊥}` (orthogonal complement in `R_{\mathbf 1}`, `D-inverse-system`),
equivalently `ker H_Q = \{u ∈ R_{\mathbf 1} : \bar f(∂)u = 0\ ∀ f ∈ I_Q\}`, i.e. the
multidegree-`\mathbf 1` piece of the Macaulay inverse system of `\overline{I_Q}` (convention C3)."
Delete `(\overline{I_Q}^{\,⊥})_{\mathbf 1}` and `(I_Q^⊥)_{\mathbf 1}`.

**SURVIVING STATEMENT.** With that wording the row is exactly true; verified numerically on four
instances (recomputation (a)).

### O5 — MAJOR — the novelty audit omits the primary source and the standard hierarchy

**Location.** Step 7.10–7.11 ("NOVELTY VERDICT", "SURVIVING NEW CANDIDATE"); §6.8; the memo's
whole claim that steps 2 and 4–6 may be new.

**Fetched statement.** (i) The memo's own principal reference, arXiv:2412.19623, opens: "*the
computational problem known as Quantum SAT (QSAT) with a System of Distinct Representatives (SDR),
**first studied by [Laumann, Läuchli, Moessner, Scardicchio, and Sondhi 2010]***", and cites that
paper four times. Crossref: Laumann, Läuchli, Moessner, Scardicchio, Sondhi, "Product, generic, and
random generic quantum satisfiability", *Phys. Rev. A* **81**, 062345 (2010),
DOI 10.1103/PhysRevA.81.062345 — a *geometrization theorem* for the dimension of the
product-satisfying manifold, i.e. exactly the object of the memo's step 2. The memo never cites it.
(ii) The step-4/6 device "`HF_{R/I}(\mathbf r) = 0` certifies `V = ∅`" is the multihomogeneous
Nullstellensatz refutation hierarchy (degree-`r` Nullstellensatz certificate); the memo presents it
as a candidate new product with no citation of that literature and no degree bound.

**FIX DEMAND.** (a) Add Laumann et al. (DOI 10.1103/PhysRevA.81.062345) and state precisely what
their geometrization theorem gives and what step 2 adds beyond it. (b) Name the step-4 criterion as
the multihomogeneous Nullstellensatz certificate, cite the Nullstellensatz proof system, state the
completeness direction (`V = ∅ ⇒ ∃ r` with `HF(\mathbf r) = 0`, with a degree bound), and say what
is new. (c) Replace "Novelty remains to be checked adversarially" — a single-source comparison is
not a novelty audit.

**SURVIVING STATEMENT.** The mathematics of steps 2 and 4–6 is correct (verified, recomputation (d),
(f)); its **novelty is unestablished**, and the product-solution-variety framing is prior art.

### O6 — MAJOR — duplication of already-merged rows and definitions; the required cross-lane read did not happen

**Location.** `D-QN-PRODUCT-BEZOUT-NUMBER`; `C-NEW-QN-COHERENT-OVERLAP-PERMANENT`; the "What a
degeneracy measurement would demonstrate" section; `C-NEW-QN-BEZOUT-NOVELTY`'s surviving statement.

**Computation.** `grep` of the memo for `C-28*`, `C-29*`, `C-30*` and for "quantum-primitives"
returns **nothing**, although the lane brief says "If `scouting/quantum-primitives.md` … exist, read
their boson-sampling and QSAT sections", and that file has existed since commit `2a5f540`
(2026-09-02 23:51). Consequences:
- `D-QN-PRODUCT-BEZOUT-NUMBER` is the `q > 2` case of the register's existing
  `D-multihomogeneous-bezout` (definitions.md:1237, `B_A = [t_1⋯t_n]∏_i(Σ_j A_{ij}t_j) = per(A)`),
  and is **verbatim Definition 52 of arXiv:2412.19623** (fetched). A new id for it violates L2.
- `C-NEW-QN-COHERENT-OVERLAP-PERMANENT` overlaps merged **C-296** (REFUTED,
  `C-NEW-QP-BOSON-COUNT`), whose surviving statement is already "the device supplies
  permanent-weighted samples; such samples are useful only when the requested output is the
  distribution or when the relevant event probability is not too small".
- The degeneracy-readout paragraphs re-derive merged **C-297** (REFUTED, analogue degeneracy
  readout) and **C-298** (fixed-mode hardware) without citing either.
- `C-NEW-QN-BEZOUT-NOVELTY`'s surviving statement attributes "the permanent-form … count" to
  arXiv:2412.19623 / the ITCS DOI. HTML grep of that paper: **"permanent" occurs 0 times**. What it
  contains is Def. 52 (the Bézout coefficient), Obs. 55 ("*the number of weighted SDRs in a PRODSAT
  instance is equal to the Bézout number*"), and the remark that "*computing `d_Béz` itself counts
  the number of perfect matchings in said graph*". The permanent *form* is in ref. 22
  (arXiv:2005.14485) and in the campaign's own `D-multihomogeneous-bezout` / C-295.

**FIX DEMAND.** Withdraw `D-QN-PRODUCT-BEZOUT-NUMBER` as a new id and propose instead an amendment
to `D-multihomogeneous-bezout` (general `q`, plus the AGR Def. 52 citation). Reword
`C-NEW-QN-COHERENT-OVERLAP-PERMANENT` to cite C-296 and state only what it adds (the JSV-FPRAS
point, which is genuinely new relative to C-296). Cite C-297/C-298 in the hardware section. In
`C-NEW-QN-BEZOUT-NOVELTY`, name the exact loci: AGR Def. 52 + Obs. 55 + the perfect-matching
remark, and arXiv:2005.14485 for the permanent formulation.

**SURVIVING STATEMENT.** The REFUTED status of `C-NEW-QN-BEZOUT-NOVELTY` is *correct and, if
anything, understated*: the memo's proposed Bézout definition is verbatim prior art.

### O7 — MAJOR — the arm-D negative verdict is asserted, not proved

**Location.** "Against the north star", steps 8.1–8.10; "Criteria audit" ("Failure of criterion 3 is
decisive"); the memo's answer to the PRD §4 arm-D sentence.

**Computation.** What 8.1–8.10 establishes is: the coefficient map `Π_a ↦ f_{a\mu}` is polynomial-
time, invertible, and spectrum-preserving on `R_{\mathbf 1}`, hence composing an algorithm with it
changes no asymptotic cost (8.5, 8.6), and this cannot be repaired by rewording (8.10). That is a
**tautology about a relabelling**, and it refutes only the strawman "the dictionary alone is a
speedup" — a claim nobody in the DAG makes. The PRD §4 sentence under test — "*a speedup in the
north-star sense is not on offer here*" — quantifies over **all** arm-D algorithms. 8.10's list of
"genuinely additional ingredients" required for repair is a description of what a positive result
would need, not a proof that none exists. Likewise the criteria-audit cell for criterion 3 reads
"the inverse-system map is an exact re-encoding; no solver or preparation theorem follows", which
is an absence-of-known-algorithm statement.

**FIX DEMAND.** Either (a) keep `C-NEW-QN-ARM-D-NORTHSTAR` but restrict its scope explicitly — the
row refutes the *encoding-as-algorithm* reading only — and add a separate row, at CONJECTURE, for
"arm D admits no PRD §2 speedup", flagged as an open negative with the specific families it has
*not* covered (bosonic Prop 8.2 sector C-129/C-130; the copy-access family of O8; restricted QSAT
sub-families with structure); or (b) supply an actual impossibility argument.

**SURVIVING STATEMENT.** A poly-time invertible spectrum-preserving identification supplies no
asymptotic advantage by itself; no arm-D speedup is currently known; the PRD §4 arm-D sentence
remains an unproved negative.

### O8 — MAJOR — the north-star audit misreads PRD §2 and leaves the strongest candidate exception unexamined

**Location.** "The actual MPS-testing result" (last five bullets); "Against the north star", Verdict
bullets; criteria-audit rows 2 and 3; `C-NEW-QN-MPS-TOMOGRAPHY-SPEEDUP`.

**Computation.** Two defects.
1. *Mis-citation of the criteria.* The memo rejects the tester "Under **PRD §2's** same-problem and
   **novelty** requirements". PRD §2 has five criteria and **none of them is a novelty criterion** —
   novelty lives in CLAUDE.md §1 / PRD §1 ("a genuinely new quantum algorithm"). Worse, §2
   criterion 3 says verbatim "*The input model (sparse access, QRAM, explicit circuit) is part of
   the statement*", which makes a copy-access problem admissible provided a copy-access classical
   baseline is named. The memo's blanket "a classical algorithm cannot receive an unknown quantum
   state without a measurement interface" is therefore not a criterion-2 failure; it is a demand to
   define the baseline.
2. *The unexamined exception.* The natural same-input comparator is **single-copy (unentangled),
   possibly adaptive, measurements with classical post-processing**, and in exactly that model there
   are proven **exponential** separations: Chen–Cotler–Huang–Li, "Exponential separations between
   learning with and without quantum memory", arXiv:2111.05881 (FOCS 2021); Huang et al., "Quantum
   advantage in learning from experiments", *Science* **376**, 1182 (2022),
   DOI 10.1126/science.abn7293. A separation of that kind for *membership in a tensor-network or
   secant variety* would be precisely a quantum-native-variety advantage and squarely inside arm D.
   The memo raises the comparator only as TJO question 6 and never audits it.

**FIX DEMAND.** (a) Correct every "PRD §2 novelty requirement" to "CLAUDE.md §1 / PRD §1"; (b) quote
§2 criterion 3's input-model clause and re-derive the criterion-2/3 verdicts for the copy-access
family; (c) add a subsection auditing the quantum-memory separations above against arm D, and either
exhibit a variety-membership problem with such a separation (the exception) or state precisely why
the known separations do not transfer.

**SURVIVING STATEMENT.** The Soleimanifar–Wright tester is prior art and therefore fails the
novelty requirement of CLAUDE.md §1 whatever the criteria reading; that alone sustains the row's
REFUTED status. The claim that *no* copy-access separation is available in arm D is unaudited.

### O9 — MAJOR — a weakening of live row C-024 is identified but not moved in lockstep

**Location.** "Spinor-BEC conic", final three bullets and the sentence "Thus C-024 is strongest as
an existing physical realization of the interaction, not yet as an experimental degeneracy readout";
TJO question 9.

**Computation.** C-024 (status SKETCH, referee: "not addressed in either round") states verbatim:
"*Hence this quadric ideal's ground space has already been realised experimentally.*" PRD §4 arm A
carries it forward: "Hardware: Bose–Hubbard and spinor-BEC spin mixing for quadric generators (row
C-024, unrefereed)". Crossref confirms the memo's reading: DOI 10.1103/PhysRevLett.92.140403 is
"Observation of Spinor **Dynamics** in Optically Trapped ⁸⁷Rb Bose-Einstein Condensates" — no
`2N+1` degeneracy readout. The memo is right, and C-297 (REFUTED) independently forbids inferring
degeneracy from spectroscopy. L2 requires the weakening to move in lockstep: shard, DAG row,
HANDOFF, PRD. The memo instead files it as a question.

**FIX DEMAND.** Add a proposed row, e.g. `C-NEW-QN-C024-WEAKENING`, status CONJECTURE:
"C-024's clause 'this quadric ideal's ground space has already been realised experimentally' is not
supported by DOI 10.1103/PhysRevLett.92.140403, which reports spin-mixing dynamics, not a
measurement of the `2N+1` ground-space dimension; the supported statement is that the Hamiltonian of
C-023 has been physically realised (arXiv:cond-mat/9807258, DOI 10.1103/PhysRevLett.81.5257) and
its spin-changing dynamics observed", `depends-on: C-023, C-024, C-297,
D-analogue-degeneracy-readout`, and name the PRD §4 arm-A sentence that must move with it.

**SURVIVING STATEMENT.** As above; the interaction is realised, the degeneracy is not measured.

### O10 — MAJOR — the flagship hardware row asserts an acceptance and a shot count without a protocol

**Location.** `C-NEW-QN-OPTICAL-SINGLET-DEMO`; "Smallest nontrivial instance"; "What a degeneracy
measurement would demonstrate".

**Computation.** The state-preparation half is correct — I recomputed it:
`a_0^†b_1^†|0⟩ ↦ ½(a_0^†+b_0^†)(a_1^†−b_1^†)|0⟩`, postselecting one photon in each rail pair keeps
`½(−a_0^†b_1^† + b_0^†a_1^†)|0⟩`, norm² = ½, giving `−|ψ^-⟩` with success probability exactly ½.
The **measurement** half is not established:
(i) the row asserts acceptance `p_0 = Tr(P_0 · 1/4) = 1/4` but never says how the maximally mixed
state *on the dual-rail `(1,1)` sector* is prepared;
(ii) the physical two-photon space of four modes is 10-dimensional, so `1/4` is an acceptance
*conditioned on the occupation-pattern postselection*, whose own probability is not stated —
precisely the compounding the memo's own K-QN14 ("Postselection multiplies") and the
`D-QN-DUAL-RAIL-SECTOR` pitfall ("output postselection is not an energetic hard-core constraint")
warn about;
(iii) no implementation of the projector `|ψ^-⟩⟨ψ^-|` with a stated efficiency is given; the memo
only remarks that the Calsamiglia–Lütkenhaus 50 % bound "does not prevent identifying the singlet
signature", uncited;
(iv) "119 ideal shots" therefore counts *post-selected, unit-efficiency* shots, with no loss model —
the memo's own list of six requirements for an analogue test (end of the spinor-BEC section) is not
applied to its own proposal.

**FIX DEMAND.** Reword the row to: "…conditioned on the occupation pattern `(1,1)` in each rail
pair and assuming an ideal, unit-efficiency implementation of the projector
`|ψ^-⟩⟨ψ^-|` and of the maximally mixed probe on the four-dimensional dual-rail sector, the
acceptance is `1/4` and `119` post-selected shots suffice…", and add the unconditioned acceptance
(the product of the sector-postselection probability with `1/4`) or mark it as the missing
ingredient. Add `C-297` to depends-on.

**SURVIVING STATEMENT.** Two photons, two balanced beamsplitters and one-photon-per-rail-pair
postselection prepare `|ψ^-⟩` with probability exactly `1/2` (recomputed); the degeneracy-readout
half of the row is not yet a protocol.

### O11 — MAJOR — the singlet example's only quantitative content is inconsistent with the memo's own ideal

**Location.** §5.2 (ideal with `1/√2`), §5.7 ("a `9×9` Macaulay minor of determinant `−1`"),
`C-NEW-QN-SINGLET-HILBERT-WITNESS` (ideal **without** `1/√2`), and its `where-tested` line
("proposed exact checker should verify the `9×9` determinant `−1`").

**Computation.** All 220 `9×9` minors of the `9×12` Macaulay matrix at bidegree `(2,2)` were
enumerated; 18 are nonzero. For the **unnormalised** generator `x_0y_1+x_1y_0`: every nonzero minor
has `det = ±1`, and **both** signs occur — so "determinant `−1`" is an ordering artefact, not an
invariant. For the memo's own §5.2 generator `(x_0y_1+x_1y_0)/√2`: `|det| ∈ {0.25, 0.353553, 0.5}`,
**never 1**. §5.2 and §5.7 are therefore about different ideals, and the row uses the third variant.

**FIX DEMAND.** Use one ideal throughout (recommended: the unnormalised
`I = (x_0y_0,\; x_1y_1,\; x_0y_1+x_1y_0)`, noting that the `1/√2` only rescales a generator and
changes neither the ideal nor any Hilbert function), and replace "determinant `−1`" by the
ordering-independent statement "the `9×12` Macaulay matrix at bidegree `(2,2)` has rank `9`; 18 of
its 220 `9×9` minors are nonzero and each has `|det| = 1` in the monomial basis". Note in the row
that determinants at bidegree `(2,2)` are basis-dependent under C1 (Fock norms there are `k! ≠ 1`).

**SURVIVING STATEMENT.** `HF(1,1) = 1` with the singlet as inverse system, `HF(2,2) = 0`, and
`V_{P^1×P^1}(I) = ∅` — all three recomputed and correct.

### O12 — MINOR — `C-NEW-QN-COPY-RESIDUAL` states an unquantified resource bound

**Location.** `C-NEW-QN-COPY-RESIDUAL`; `D-QN-COPY-RESIDUAL-OBSERVABLE`.

**Computation.** The identity is true **by construction** of `|F_j⟩` (the memo defines `|F_j⟩` by
`f_j(\barψ) = ⟨F_j|ψ^{⊗m}⟩`), so the row's first half carries no content beyond `C-027` in
normalised form. The second half says `O(ε^{-2}\log(1/δ))` "independent measurements … once `A_F` is
implementable": each measurement consumes `m` copies, so the copy cost is `m·O(ε^{-2}\log(1/δ))`;
`Λ` is never bounded, although `0 ≤ A_F ≤ 1` requires `Λ ≥ \|Σ_j w_j |F_j⟩⟨F_j|\|`, which the memo's
own text says "can grow with the number and norms of the equations"; and "once `A_F` is
implementable" is an unquantified hypothesis, contrary to PRD §2 criterion 3.

**FIX DEMAND.** State the copy cost with the factor `m`; define `Λ` and give the bound that makes
`0 ≤ A_F ≤ 1`; relate `\|F_j\|` to `\|f_j\|_{BW}` via C-019; name the access model by
`D-QN-PHYSICAL-DATA-ACCESS` case number.

**SURVIVING STATEMENT.** With `|F_j⟩` normalised as in C-019 and `Λ = Σ_j w_j\|F_j\|²`, the identity
holds and the estimator costs `m·O(ε^{-2}\log(1/δ))` copies, given a measurement of `A_F`.

### O13 — MAJOR — `D-QN-MULTIPROJECTIVE-SATURATION` mis-describes its own object

**Location.** `D-QN-MULTIPROJECTIVE-SATURATION`; step 2.4; step 4.6.

**Computation.** (i) The entry says `J = \sqrt{I:B^∞}` "is the vanishing ideal of **the reduced point
set** `V(I) ⊆ (P^{q-1})^n`". `V(I)` need not be finite — the memo's own dictionary has a row
"`\dim V_{X_0}(I_Q)` | Number of continuous parameters in product ground states", and its 2.9
caution speaks of "a positive-dimensional linear space". Calling it a point set is wrong.
(ii) The convention for `V = ∅` is never stated, yet it is load-bearing: step 4.6's conclusion
`e_Q = HF(\mathbf 1)` requires `J_Q = R` (equivalently `(J_Q)_{\mathbf 1} = R_{\mathbf 1}`) when
`V = ∅`, which holds because `V_{X_0}(I) = ∅ ⟺ B ⊆ \sqrt I ⟺ B^k ⊆ I ⟺ I:B^∞ = R`. Nothing in the
memo says so.
(iii) The multiprojective Nullstellensatz step `\sqrt{I:B^∞} = I(V_{X_0}(I))` is asserted without
citation.

**FIX DEMAND.** Replace "the reduced point set `V(I)`" by "the reduced closed subscheme
`V_{X_0}(I) ⊆ (P^{q-1})^n`, of any dimension"; add the explicit convention `I(∅) = R`, with the
one-line proof that `V_{X_0}(I) = ∅ ⇒ I:B^∞ = R`; cite the multiprojective Nullstellensatz.

**SURVIVING STATEMENT.** `\sqrt{I:B^∞}` is the multihomogeneous vanishing ideal of `V_{X_0}(I)`,
with `I(∅) = R`; step 2.5's product-span identity and step 4.6's `e_Q = HF(\mathbf 1)` are then both
correct (recomputation (f)).

### O14 — MINOR — `D-reserved-photonic` is used exactly as its own pitfall forbids

**Location.** `C-NEW-QN-COHERENT-OVERLAP-PERMANENT`, `depends-on: D-reserved-photonic, …`.

**Computation.** `D-reserved-photonic` is a **Reserved** stub whose pitfall reads: "none of these
objects has a definition in the seed report; **nothing may cite this entry as if it did**". A
`depends-on` edge is exactly such a citation, and the row's content (linear-optical mode
transformations, boson-sampling amplitudes) is drawn from the reserved list.

**FIX DEMAND.** Remove `D-reserved-photonic` from `depends-on`; depend on
`D-optical-counting-access` (which is a real entry, already used) and `D-QN-DUAL-RAIL-SECTOR`, or
propose the missing photonic definitions as register entries.

**SURVIVING STATEMENT.** The row's mathematics is unaffected.

### O15 — MINOR — bibliography hygiene

**Location.** "References" 1–30 and body citations.

**Computation.** Five listed references are never cited in the body (`arXiv:1004.3787`,
`arXiv:1801.02662`, `arXiv:1508.01907`, `arXiv:2306.03709`, `arXiv:cs/0405021`); one body citation
is absent from the list (`arXiv:1904.07563`); ref. 29's first author is **Changhun** Oh, not
"Changhyoup Oh" (Crossref, Nature Physics 20, 2024); refs. 3 and 10 truncate their subtitles.

**FIX DEMAND.** Delete or cite the five orphans (`cs/0405021` is genuinely relevant to §7: computing
the *optimal* m-Bézout number is NP-hard and not in APX, which sharpens 7.9); add 1904.07563 to the
list; fix the author name and the two titles.

**SURVIVING STATEMENT.** No fabricated reference was found; all 31 identifiers resolve.

### O16 — MINOR — the two exponential readout costs hold only in the worst case over the degeneracy

**Location.** "What a degeneracy measurement would demonstrate": "Independent sampling then needs
`Θ(4^n)` shots"; "Ideal coherent amplitude estimation still needs `Θ(2^n)` projector queries."

**Computation.** With `p_0 = g/2^n` and target additive error `ε = 2^{-(n+1)}`, the Bernoulli
variance is `p_0(1−p_0)`, so the shot count is `Θ(g·2^n)`, and amplitude estimation needs
`Θ(\sqrt{p_0}/ε) = Θ(\sqrt g · 2^{n/2})` queries. At `n = 20`, `g = 1`: `4.2e6` shots versus the
memo's Hoeffding worst case `8.1e12`. The memo's `Θ`'s are attained only at `g = Θ(2^n)`.

**FIX DEMAND.** Write "`Θ(4^n)` in the worst case over `g`, and `Θ(g·2^n)` at degeneracy `g`" and
"`Θ(2^n)` in the worst case, `Θ(\sqrt g·2^{n/2})` at degeneracy `g`".

**SURVIVING STATEMENT.** Exact integer degeneracy readout is exponentially expensive in `n` in every
regime; the conclusion is unchanged, the constants are not.

### O17 — MINOR — two over-attributions in the tensor sections

**Location.** "General CP or border-rank optimization remains nonconvex and NP-hard
(arXiv:0911.1393)"; "Tree tensor-network loci similarly admit edge-flattening descriptions
(arXiv:1501.01120; arXiv:2608.19071)".

**Computation.** Hillar–Lim's abstract lists "determining the rank or best **rank-1** approximation
of a 3-tensor"; border-rank hardness is not among their results. arXiv:1501.01120 is the Hackbusch
tensor-format conjecture (comparing perfect-binary-tree and train-track formats); the
edge-flattening description is in arXiv:2608.19071 alone.

**FIX DEMAND.** Restrict the Hillar–Lim citation to rank and best rank-1 approximation; mark
border-rank optimisation `[UNVERIFIED]` or cite a source that proves it. Move arXiv:1501.01120 to
the format-comparison sentence.

**SURVIVING STATEMENT.** Tensor rank and best rank-1 approximation of 3-tensors are NP-hard
[Hillar–Lim]; tree tensor-network varieties have prime ideals generated by flattening minors
[arXiv:2608.19071].

### O18 — MINOR — the four-qubit counterexample is under-computed and the hierarchy's completeness is missing

**Location.** Steps 6.5–6.8; `C-NEW-QN-HF2-COMPLETE`'s `where-proved`.

**Computation.** For random generic complex clause vectors the diagonal profile is
`HF(1^4) = 11`, `HF(2^4) = 11`, `HF(3^4) = 1`, `HF(4^4) = 0`. The memo's bound "at most `5·16 = 80`"
gives only `HF(2^4) ≥ 1` and is 11-fold loose; the **first certifying level is `r = 4`**, which is
the number that actually makes the point that "level two is only sufficient, not complete". §6.8
calls this "a hierarchy" without stating the completeness direction (`V = ∅ ⇒ ∃ r` with
`HF(\mathbf r) = 0`), which needs the multihomogeneous Nullstellensatz and a degree bound.

**FIX DEMAND.** Record the four computed values, state that the counterexample requires generic
clause vectors, and add the completeness statement with a citation and a degree bound (or mark it
open).

**SURVIVING STATEMENT.** The refutation is correct and now quantified.

### O19 — MINOR — no L4 checker for the two exactly checkable rows

**Location.** Every proposed row's `where-tested: none`;
`C-NEW-QN-QSAT-INVERSE-SYSTEM`: "the two-qubit determinant calculation is not an L4 checker";
`C-NEW-QN-SINGLET-HILBERT-WITNESS`: "proposed exact checker should verify…".

**Computation.** Both rows are finite exact-arithmetic statements. This critic wrote and ran two
red-capable scripts covering steps 1.8/1.13/1.14/1.17, 2.5–2.8, 5.3/5.4/5.7/5.8, 6.2/6.4/6.7,
7.5/7.6 and the Hoeffding count (exit 0 after encoding the corrected statements). L4 requires a
checker with a recorded mutation in `checkers/MUTATIONS.md`; the memo proposes none.

**FIX DEMAND.** Ship `checkers/` entries for `C-NEW-QN-QSAT-INVERSE-SYSTEM` (random QSAT instance →
`H_Q = Φ_1Φ_1^†`, `ker H_Q = ((I_Q)_1)^⊥`, `dim ker = HF(1)`) and `C-NEW-QN-SINGLET-HILBERT-WITNESS`
(exact rank/minor computation), each with a recorded red mutation, before either row is merged
above CONJECTURE.

**SURVIVING STATEMENT.** Both rows are true as recomputed here; they are not yet checker-backed.

### O20 — MINOR — the genericity hypothesis of 7.7 is unattainable for rank > 1 clauses

**Location.** Step 7.7 ("For generic clause coefficients and positive `B(D)`, the count is exactly
`B(D)` with multiplicity"); step 7.1.

**Computation.** After rank-one splitting, the `r_a` forms coming from one projector `Π_a` share the
same site support `S_a` **and are mutually orthonormal** (memo 1.5). That is a positive-codimension
condition on the coefficient tuple, so a QSAT instance with any clause of rank `> 1` is never
generic in the full coefficient space. The square-system hypothesis `m = n(q-1)` is also violated by
every instance whose split clause count `Σ_a r_a ≠ n(q-1)` — including the memo's own §5 example
(three forms, `m = 2`) and §6 example (five forms, `m = 4`).

**FIX DEMAND.** State the genericity as "generic within the family of tuples with the given supports
and the orthonormality constraints imposed by the clause decomposition", and say explicitly that
7.1–7.7 apply only to square subsystems.

**SURVIVING STATEMENT.** For a square subsystem of forms generic subject to their supports,
`B(D)` is the count; for the memo's own examples the Bézout section does not apply.

### O21 — MINOR — missing depends-on edges and an undefined symbol in the flagship row

**Location.** `C-NEW-QN-QSAT-INVERSE-SYSTEM` `depends-on`; its statement's use of `Φ_{\mathbf 1}`.

**Computation.** The row is the multidegree-`\mathbf 1` specialisation of C-008 (`ker H_N = (I_N)^⊥`,
"the single load-bearing identity of the campaign") and C-009 (`dim ker H_N = HF(N)`), and it uses
C-033 (product solutions = points of the multiprojective variety) implicitly. None of C-008, C-009,
C-033 appears in `depends-on`; nor does `D-macaulay-map`, although `Φ_{\mathbf 1}` is used in the
row statement and defined only in memo step 1.10. All other cited ids were audited by `grep` and
exist (22 `C-###` ids, 20 register `D-` ids: all resolve).

**FIX DEMAND.** Add `C-008, C-009, C-033, D-macaulay-map` to `depends-on`, and state in the row that
it is the multidegree-`\mathbf 1` instance of C-008/C-009 rather than an independent result.

**SURVIVING STATEMENT.** The row's content is correct; its position in the DAG is misstated.

---

## Proposed rows adjudication

| id | verdict | note |
|---|---|---|
| `C-NEW-QN-QSAT-INVERSE-SYSTEM` | **ACCEPT WITH REWORDING** (CONJECTURE) | O4, O21, O19. Exact text: "For every finite `n`-qudit quantum `k`-SAT instance `Q = {Π_a}` and every orthonormal rank-one decomposition `Π_a = Σ_μ|φ_{aμ}⟩⟨φ_{aμ}|`, let `I_Q` be the associated D-QN-QSAT-IDEAL and `Φ_{\mathbf 1}` the multidegree-`\mathbf 1` Macaulay map (D-macaulay-map, D-multidegree-sector). Under the unitary identification `R_{\mathbf 1} ≅ (\mathbb C^q)^{⊗n}`: `H_Q = Φ_{\mathbf 1}Φ_{\mathbf 1}^†`; `ker H_Q = ((I_Q)_{\mathbf 1})^{⊥} = \{u ∈ R_{\mathbf 1} : \bar f(∂)u = 0\ ∀f ∈ I_Q\}`, i.e. the multidegree-`\mathbf 1` piece of the Macaulay inverse system of `\overline{I_Q}` (C3, D-inverse-system); and `\dim\ker H_Q = HF_{R/I_Q}(\mathbf 1)`. This is the multidegree-`\mathbf 1` instance of C-008 and C-009." depends-on += `C-008, C-009, C-033, D-macaulay-map`. Verified numerically on four instances. |
| `C-NEW-QN-PRODUCT-SPAN-DEFECT` | **ACCEPT WITH REWORDING** (CONJECTURE) | O13. Add: `J_Q := \sqrt{I_Q : B^∞}` with `B` the irrelevant ideal (D-QN-MULTIPROJECTIVE-SATURATION), `J_Q = R` when `V_{X_0}(I_Q) = ∅`; "the span of all fully product ground states" means `span\{⊗_i|\bar x_i⟩ : x ∈ V_{X_0}(I_Q)\}`, `= {0}` when `V = ∅`. Verified numerically (three point sets, plus an explicit `e_Q = 1` instance). |
| `C-NEW-QN-HILBERT-VANISH-ENTANGLEMENT` | **ACCEPT WITH REWORDING** (CONJECTURE) | O5, O13. Widen to "for every multihomogeneous ideal `I` in the Cox ring of `(P^{q-1})^n`" (the proof uses no QSAT structure); require `\mathbf r ≥ \mathbf 1`, `\mathbf r ≠ \mathbf 1`; state the `I(∅) = R` convention that `e_Q = HF(\mathbf 1)` needs; add a sentence naming the criterion as a multihomogeneous Nullstellensatz certificate and flagging the completeness direction as open. |
| `C-NEW-QN-SINGLET-HILBERT-WITNESS` | **ACCEPT WITH REWORDING** (CONJECTURE) | O11, O19. Use one ideal (`I = (x_0y_0, x_1y_1, x_0y_1+x_1y_0)`, and correct §5.2 to match); replace "determinant `−1`" by "the `9×12` bidegree-`(2,2)` Macaulay matrix has rank `9`; 18 of its 220 `9×9` minors are nonzero, each with `|det| = 1` in the monomial basis"; note C1 basis-dependence at bidegree `(2,2)`. |
| `C-NEW-QN-HF2-COMPLETE` | **ACCEPT AS REFUTED, WITH REWORDING** | O18. Add "for generic clause vectors" to the `where-proved`, and record the recomputed profile `HF(1^4)=11`, `HF(2^4)=11`, `HF(3^4)=1`, `HF(4^4)=0` (first certifying level `r = 4`). |
| `C-NEW-QN-BEZOUT-NOVELTY` | **ACCEPT AS REFUTED, WITH REWORDING** | O6. Surviving statement must name the exact loci: Definition 52 (Bézout number) and Observation 55 ("the number of weighted SDRs in a PRODSAT instance is equal to the Bézout number") of arXiv:2412.19623 / DOI 10.4230/LIPIcs.ITCS.2026.7, together with its remark that computing `d_{Béz}` counts perfect matchings; the *permanent formulation* is in arXiv:2005.14485 and in the campaign's own `D-multihomogeneous-bezout` / C-295, **not** in arXiv:2412.19623 (word count 0). Add Laumann et al. DOI 10.1103/PhysRevA.81.062345. |
| `C-NEW-QN-COPY-RESIDUAL` | **ACCEPT WITH REWORDING** (CONJECTURE) | O12. State `Λ = Σ_j w_j\|F_j\|²` (or the bound making `0 ≤ A_F ≤ 1`), relate `\|F_j\|` to `\|f_j\|_{BW}` via C-019, give the copy cost as `m·O(ε^{-2}\log(1/δ))`, and name the access model by `D-QN-PHYSICAL-DATA-ACCESS` case. Note it is the normalised form of C-027. |
| `C-NEW-QN-RESIDUAL-EQUALS-DISTANCE` | **ACCEPT AS REFUTED, WITH REWORDING** | Statement must respect C3 (`f_j(\barψ)`, not `f_j(ψ)`), define `dist` (Fubini–Study on `P(\mathcal H)`), and name the counterexample explicitly: replacing `f_j` by `λf_j` multiplies the left side by `|λ|²` and leaves the right side fixed, so no identity can hold for all generating tuples. |
| `C-NEW-QN-MPS-TOMOGRAPHY-SPEEDUP` | **ACCEPT AS REFUTED, WITH REWORDING** | O8. Rest the refutation on CLAUDE.md §1 / PRD §1 novelty (published prior art) and on the different-output comparator; delete the "PRD §2 novelty requirement" and the blanket criterion-2 argument; state that `Ω(q^n/ε)` is the `r = 1` case of Yuen's `Ω(rd/ε)`; add a sentence that the same-input classical comparator (single-copy adaptive measurement + classical post-processing) is *not* audited here and is deferred to the memo's Q6, naming arXiv:2111.05881 and DOI 10.1126/science.abn7293. |
| `C-NEW-QN-COHERENT-OVERLAP-PERMANENT` | **ACCEPT WITH REWORDING** (REFUTED) | O6, O14. Split the compound statement; cite and distinguish merged **C-296**; drop `D-reserved-photonic` from depends-on; keep and foreground the genuinely new part relative to C-296, namely that the QSAT Bézout incidence matrices are nonnegative and hence admit the JSV FPRAS (DOI 10.1145/1008731.1008738), so no optical sampling advantage is available for that count. |
| `C-NEW-QN-OPTICAL-SINGLET-DEMO` | **ACCEPT WITH REWORDING** (CONJECTURE) | O10. Preparation half recomputed and correct (success probability exactly `1/2`, output `−|ψ^-⟩`); readout half must be conditioned as in O10 and must add `C-297` to depends-on. |
| `C-NEW-QN-ARM-D-NORTHSTAR` | **HOLD** | O7. The row as stated refutes only the encoding-as-algorithm strawman, and 8.10 proves only that a poly-time invertible spectrum-preserving relabelling changes no asymptotics. It must not be merged as if it discharged the PRD §4 arm-D sentence. Merge only after (a) the scope restriction is written into the statement **and** (b) a separate row, at CONJECTURE, carries "arm D admits no PRD §2 speedup", listing the families not covered (bosonic Prop 8.2 sector C-129/C-130; copy-access separations of O8; structured QSAT sub-families). |

Counts (12 rows): **ACCEPT WITH REWORDING, status CONJECTURE — 6**
(`QSAT-INVERSE-SYSTEM`, `PRODUCT-SPAN-DEFECT`, `HILBERT-VANISH-ENTANGLEMENT`,
`SINGLET-HILBERT-WITNESS`, `COPY-RESIDUAL`, `OPTICAL-SINGLET-DEMO`);
**ACCEPT AS REFUTED, WITH REWORDING — 5** (`HF2-COMPLETE`, `BEZOUT-NOVELTY`,
`RESIDUAL-EQUALS-DISTANCE`, `MPS-TOMOGRAPHY-SPEEDUP`, `COHERENT-OVERLAP-PERMANENT`);
**HOLD — 1** (`ARM-D-NORTHSTAR`); **REJECT — 0**; **ACCEPT AS SKETCH — 0** (no proposed row is a
cited published theorem).

## Proposed definitions adjudication

| id | verdict | note |
|---|---|---|
| `D-QN-QSAT-IDEAL` | **ACCEPT WITH ADDITION** | Add the (true, checkable) fact that `I_Q` does not depend on the chosen orthonormal rank-one decomposition, because `span_μ\{f_{aμ}\}` is the image of `Π_a` in the multilinear forms on `S_a`; and state that the coefficients are taken **unconjugated** (memo 1.6), which is what makes 1.8 give `|φ⟩⟨φ|` (recomputed). |
| `D-QN-MULTIPROJECTIVE-SATURATION` | **ACCEPT WITH REWORDING** | O13: "reduced point set" → "reduced closed subscheme `V_{X_0}(I)`, of any dimension"; add the `I(∅) = R` convention and the one-line proof that `V_{X_0}(I) = ∅ ⇒ I:B^∞ = R`; cite the multiprojective Nullstellensatz. |
| `D-QN-PRODUCT-SPAN` | **ACCEPT** | Correct; the pitfall ("contains entangled superpositions") is right. Verified numerically. |
| `D-QN-MULTIGRADED-ENTANGLED-DEFECT` | **ACCEPT** | A clean specialisation of `D-entangled-defect`; the two displayed expressions agree. Verified numerically. |
| `D-QN-COPY-RESIDUAL-OBSERVABLE` | **ACCEPT WITH REWORDING** | O12: specify `Λ`, the conjugation convention (C3), that `A_F` acts on `Sym^m` and that each shot consumes `m` copies; cite C-019 for `\|F_j\| = \|f_j\|_{BW}`. |
| `D-QN-TENSOR-NETWORK-VARIETY` | **ACCEPT** | Citations verified (arXiv:1105.4449, 1501.01120, 2101.03148, 2608.19071); the non-closedness pitfall is exactly Landsberg–Qi–Ye's result. Move the edge-flattening claim's citation to arXiv:2608.19071 (O17). |
| `D-QN-PHYSICAL-DATA-ACCESS` | **ACCEPT WITH REWORDING** | Must cite the register's existing `D-input-model` and say that it *extends* it to physical/copy access rather than replacing it (L2); `D-input-model` fixes the campaign's classical input model and is never mentioned by the memo. |
| `D-QN-DUAL-RAIL-SECTOR` | **ACCEPT** | Correct; the pitfall about postselection versus energetic enforcement is the right one and should be echoed in `C-NEW-QN-OPTICAL-SINGLET-DEMO` (O10). |
| `D-QN-PRODUCT-BEZOUT-NUMBER` | **REJECT** | O6. It is the general-`q` case of the register's `D-multihomogeneous-bezout` and is verbatim Definition 52 of arXiv:2412.19623. Propose an amendment to `D-multihomogeneous-bezout` (general `q`, AGR citation, and the Bartzos–Emiris–Schicho permanent formulation) instead of a new id. |

Counts: **ACCEPT 4**; **ACCEPT WITH REWORDING/ADDITION 4**; **REJECT 1**.

## Lockstep and north-star audit summary

- **Quantifiers.** All twelve rows carry explicit universal quantifiers. Two are compound and should
  be split (`COHERENT-OVERLAP-PERMANENT`, `RESIDUAL-EQUALS-DISTANCE`); one is over-narrow
  (`HILBERT-VANISH-ENTANGLEMENT` needs no QSAT structure); one has a false displayed equality (O4).
- **depends-on.** Every `C-###` and register `D-` id cited by the memo exists (audited by `grep`;
  22 claim ids, 20 definition ids, all resolve). Missing edges in O21. No row depends on a REFUTED
  row, but three REFUTED rows are cited as authority in prose (O3).
- **Statuses.** All twelve are CONJECTURE or REFUTED, as the brief requires; none claims SKETCH, and
  none would qualify (no proposed row is an imported published theorem).
- **REFUTED-row consistency.** C-297 (analogue degeneracy readout) is **not** violated: the memo's
  protocol requires an implemented, calibrated zero-energy projector and explicitly says "Preparing
  one singlet demonstrates only that one ground state exists. It does not measure the ground-space
  dimension." The residual defect is that C-297 and C-298 are never cited (O6) and that the
  acceptance/shot figures are unconditioned (O10).
- **Lockstep.** One live SKETCH row (C-024) is weakened in substance without a proposed row or a PRD
  amendment (O9). No other artifact is left behind.
- **North star.** The memo does answer the brief's question — it says an exponential physical-query
  saving is *not* a north-star hit — but on a misreading of PRD §2 (O8): §2 has no novelty criterion,
  and criterion 3 makes the input model part of the statement, so copy-access problems are
  admissible once a copy-access classical baseline is named. The negative verdict on arm D is proved
  only for the identity re-encoding (a tautology) and is otherwise asserted (O7).

## Objection counts

**FATAL 0 · MAJOR 12 (O1–O11, O13) · MINOR 9 (O12, O14–O21).**

VERDICT: FAIL(12 MAJOR, 9 MINOR, 0 FATAL)
