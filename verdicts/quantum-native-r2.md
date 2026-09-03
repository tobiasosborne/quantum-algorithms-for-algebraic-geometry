<!-- ROLE: adversarial critic adjudication, round 2, on scouting/quantum-native.md (arm D).
     Prior: verdicts/quantum-native-r1.md, FAIL(12 MAJOR, 9 MINOR, 0 FATAL). Under rk-light L5
     later-round protocol: what passed in r1 is not re-litigated; only changed text is attacked.
     Nothing here changes a status; the orchestrator merges from the tables below. -->

# Verdict — scouting/quantum-native.md, round 2 (adjudication)

- **Target:** `scouting/quantum-native.md` at commit `fa71136` (2247 lines; 13 proposed rows,
  8 proposed `D-QN-*` definitions plus one amendment proposal, 31 references).
- **Prior:** `verdicts/quantum-native-r1.md` at `00a66b9`, FAIL(12 MAJOR, 9 MINOR, 0 FATAL).
- **Scope:** `git diff a0a9a6d fa71136 -- scouting/quantum-native.md` (850 insertions, 769
  deletions) plus the memo's `# Repair r1 response` disposition table.
- **Date:** 2026-09-03. **Critic model:** Opus (Claude). **Writable file:** this one only.
  Nothing else edited; nothing committed.

## Commands run (exit codes)

| # | command | exit |
|---|---|---|
| 1 | `git diff -U1 a0a9a6d fa71136 -- scouting/quantum-native.md` (2264 lines) + hunk survey | 0 |
| 2 | citation census diff: `git show a0a9a6d:… \| grep -oE 'arXiv:…\|DOI:…' \| sort -u` vs the same on the new file, `comm -13/-23` | 0 |
| 3 | Crossref REST for the two DOIs newly introduced by the repair, plus the alternative Valiant DOI (`10.1016/0304-3975(79)90044-6`, `10.1137/0208032`, `10.1007/s00029-024-00935-5`) | 0 |
| 4 | WebFetch `arxiv.org/abs/2111.05881`, `arxiv.org/abs/2112.00778`; WebSearch for the Feigin–Makhlin preprint | 0 |
| 5 | `python3` — C-019 conjugation, `Λ` normalisation and `0≤A_F≤1` (new text in `D-QN-COPY-RESIDUAL-OBSERVABLE`) | 0 |
| 6 | `python3` — decomposition-independence of `I_Q` under unitary rebasing of the clause decomposition (new claim in `D-QN-QSAT-IDEAL`), 6 trials | 0 |

## Disposition verification

The memo's own table reads 16 FIXED, 3 DOWNGRADED, 1 RETRACTED (O6), 1 RESIDUE — the
orchestrator's brief records 17 FIXED, which folds O6's RETRACTED into FIXED. Verified below.

| obj | claimed | verified? | evidence |
|---|---|---|---|
| O1 | FIXED | **VERIFIED, with NEW DEFECT O23** | The `#P`-complete attribution to arXiv:1010.2480 is gone from all three loci; the dictionary, Complexity conclusions and K-QN3 now state Ji–Wei–Zeng's equivalence composed with `#2-SAT` hardness and cite `D-hardness-anchors`. But the Valiant DOI supplied is the wrong paper (O23). |
| O2 | FIXED | **VERIFIED** | The dictionary now carries three separate rows: the promise problem (P for qubit 2-QSAT, `QMA₁`-complete for 3-QSAT and (2,5)), exact no-promise nonvanishing ("Not thereby in `QMA₁`", C-038), and exact `HF(1)`. No row asserts `QMA₁`-completeness of an exact problem. |
| O3 | FIXED | **VERIFIED** | Step 2.10 leaf is now `[C-029; the contrary draft claim is REFUTED as C-216]`; Complexity conclusions read "C-038, with C-034–C-037, remains binding; the contrary draft is REFUTED as C-217" and likewise for C-041/C-043/C-044 vs C-219; K-QN17's leaf carries the same form. No REFUTED row is cited as authority anywhere. |
| O4 | FIXED | **VERIFIED** | `C-NEW-QN-QSAT-INVERSE-SYSTEM` now carries exactly the r1 demanded text; the false `(\overline{I_Q}^{\,\perp})_{\mathbf1}` equality is deleted, and a new step **1.16 CAUTION** records that under the register's notation that expression would mean `((\overline{I_Q})_{\mathbf1})^\perp`, which generally differs — the r1 numerical counter-check, correctly transcribed. |
| O5 | DOWNGRADED | **VERIFIED as a downgrade** | Laumann et al. (DOI 10.1103/PhysRevA.81.062345, Crossref-confirmed in r1) added at 2.10, 7.10 and in the dictionary; 2.10 now states what is left over ("the degree-`1` linear-span identity and the defect"), 7.11 says novelty is unestablished and withholds the "new" claim pending a broader audit and an L4 pass; 4.9/6.8 name the multihomogeneous Nullstellensatz and declare the effective degree bound open. Residual: the hierarchy's only external source is the fabricated O22 citation, and no Nullstellensatz-proof-system literature is cited. Accepting the downgrade. |
| O6 | RETRACTED | **VERIFIED** | `D-QN-PRODUCT-BEZOUT-NUMBER` is gone, replaced by "### D-multihomogeneous-bezout amendment" which explicitly says "No D-QN-PRODUCT-BEZOUT-NUMBER is proposed". 7.5 now reads "The permanent formulation is in arXiv:2005.14485 and D-multihomogeneous-bezout/C-295. It is not attributed to arXiv:2412.19623." 7.10 cites AGR Definition 52, Observation 55 and the perfect-matching remark — matching my r1 HTML grep exactly (AGR word count for "permanent": 0). C-295, C-296, C-297, C-298 are now cited in the dictionary, K-QN15, K-QN16, the readout section and three rows. |
| O7 | DOWNGRADED | **VERIFIED as a downgrade** | §Verdict now opens "Arm D does not currently contain an established north-star speedup. The broad negative in PRD §4 is also not proved and is not discharged by this memo." Steps 8.5/8.6 are relabelled **TAUTOLOGY**, 8.8 is a SCOPED VERDICT explicitly "not an impossibility theorem for Arm D", and 8.10 is a SCOPE BOUNDARY with a five-item non-coverage list (C-129/C-130 bosonic sector; copy-access membership/distance; structured QSAT subfamilies; new collective-measurement separations; new preparation/gap/readout theorems). The row is now CONJECTURE, scoped to relabelling-composition families. This is exactly repair option (a) of r1 O7. Residual: O24 (status-field form). |
| O8 | FIXED | **VERIFIED** | "PRD §2 has no novelty criterion" is now stated twice; novelty is relocated to CLAUDE.md §1 / PRD §1; the criteria audit is split into two columns (relabelling-composition family vs copy-access variety testing) and criterion 3 for the copy-access column reads "Input model is legitimately part of the problem"; the comparator is named as adaptive single-copy measurement plus classical post-processing in the §Verdict, 8.10, `D-QN-PHYSICAL-DATA-ACCESS` and the MPS row; arXiv:2111.05881 and DOI:10.1126/science.abn7293 are cited *without* claiming transfer. Both new references refetched: Chen–Cotler–Huang–Li, "Exponential separations between learning with and without quantum memory" (2021), and Huang et al., "Quantum advantage in learning from experiments", Science 376, 1182 (2022), arXiv:2112.00778 — titles, authors and DOI all correct. |
| O9 | FIXED | **VERIFIED** | New row `C-NEW-QN-C024-WEAKENING` carries verbatim the wording demanded in r1, plus a `lockstep:` field naming C-024, its shard, HANDOFF and the PRD §4 Arm A sentence; the spinor-BEC section now lists only the three supported statements and says C-024's final clause "must therefore be weakened in lockstep". |
| O10 | DOWNGRADED | **VERIFIED as a downgrade** | The readout section and the optical row now condition the `1/4` acceptance on the `(1,1)` occupation pattern and on ideal unit-efficiency implementations of both the maximally mixed probe and `\|\psi^-\rangle\langle\psi^-\|`, introduce `\eta_{\rm sector}` with unconditioned acceptance `\eta_{\rm sector}/4`, and state "119 is not a launched-shot count". `C-297` is added to the row's depends-on. |
| O11 | FIXED | **VERIFIED by recomputation** | 5.2 now fixes the unnormalised ideal and notes the `1/\sqrt2` variant changes neither ideal nor Hilbert function but rescales minors; 5.7 states rank 9, "Exactly 18 of its 220 maximal `9×9` minors are nonzero, and each has `\|\det\|=1` … both determinant signs occur", and records `\|\det\|\in\{0.25, 0.353553…, 0.5\}` for the `\sqrt2` variant. These are exactly my r1 numbers. |
| O12 | FIXED | **VERIFIED, with NEW DEFECT O25** | `\Lambda=\sum_j w_j\|F_j\|^2` is defined, C-019 is cited for `\|F_j\|=\|f_j\|_{\rm BW}`, access case 1 is named, and the copy cost is `m\cdot O(\varepsilon^{-2}\log(1/\delta))`. I confirmed numerically that `\|F\|=\|f\|_{\rm BW}` and that `\|\sum_j w_j\|F_j\rangle\langle F_j\|\|\le\Lambda`, so `0\le A_F\le\mathbb 1` holds. The conjugation in the defining equation is wrong (O25). |
| O13 | FIXED | **VERIFIED except its source (O22)** | "reduced point set" is replaced by "reduced closed subscheme `V_{X_0}(I)`, of any dimension"; `I(\varnothing)=R` is adopted with the one-line proof (`V=\varnothing\Rightarrow B\subseteq\sqrt I\Rightarrow B^k\subseteq I\Rightarrow I:B^\infty=R`); 4.6 uses it explicitly. The Nullstellensatz citation attached to it is fabricated (O22). |
| O14 | FIXED | **VERIFIED** | `D-reserved-photonic` removed; depends-on is now `D-optical-counting-access, D-QN-DUAL-RAIL-SECTOR, D-multidegree-sector, D-coherent-state, C-295, C-296`. |
| O15 | FIXED | **VERIFIED** | Reference list rebuilt (31 entries, all hyperlinked). The four orphans and the "Changhyoup Oh" entry are removed (with a note recording the correct name Changhun Oh); arXiv:1904.07563 added as #26 with full author list; refs 3 and 9 carry their full subtitles. |
| O16 | FIXED | **VERIFIED against my r1 computation** | The readout section now gives `\Theta(g\,2^n)` shots and `\Theta(\sqrt g\,2^{n/2})` amplitude-estimation queries at degeneracy `g`, with `\Theta(4^n)` and `\Theta(2^n)` retained only as worst cases over `g` — the exact correction demanded. |
| O17 | FIXED | **VERIFIED** | Two explicit disclaimers now appear ("Hillar–Lim prove NP-hardness for tensor rank and best rank-one approximation of a 3-tensor"; "No border-rank-optimization hardness claim is attributed to Hillar–Lim"), and the edge-flattening sentence in `D-QN-TENSOR-NETWORK-VARIETY` now cites arXiv:2608.19071, with arXiv:1501.01120 relabelled as format comparison. |
| O18 | FIXED | **VERIFIED by recomputation** | New step 6.5 records `HF(1^4)=11, HF(2^4)=11, HF(3^4)=1, HF(4^4)=0` with ambient dimensions 16, 81, 256, 625; 6.6 states level two is inconclusive; 6.7 gives the first certifying level `r=4`; 6.8 adds the existential completeness direction and says no effective bound is given. Identical to my r1 profile. |
| O19 | RESIDUE | **ACCEPTED as residue** | A read-only lane memo cannot ship a `checkers/` entry with a recorded mutation; both affected rows stay CONJECTURE and say so. See O28 for the one consequence the orchestrator must handle. |
| O20 | FIXED | **VERIFIED** | 7.1 restricts steps 7.1–7.7 to square subsystems and says explicitly they do not apply to the §5 three-form or §6 five-form examples; 7.7 restricts genericity to "tuples having the fixed supports and the orthonormality constraints imposed by the clause decomposition" and records that a rank-`r_a>1` projector cannot be generic in the unconstrained space. |
| O21 | FIXED | **VERIFIED** | depends-on is now `C-008, C-009, C-033, D-macaulay-map, D-multidegree-sector, D-quantum-k-sat, D-inverse-system, D-ground-space, C-030, C-031, C-032`, and the statement closes "This is the multidegree-`1` instance of C-008 and C-009." |

**Score: 21/21 dispositions verified as claimed** (16 FIXED + 1 RETRACTED + 3 DOWNGRADED + 1
RESIDUE). No claimed disposition is NOT VERIFIED. Nothing that passed in r1 was broken by the
repair: I re-read steps 1.13, 5.3, 5.4, 5.8, 6.2, 7.4–7.6 and the beamsplitter derivation and they
are unchanged or strengthened.

## New citation audit

Five identifiers were introduced by the repair. Each was independently resolved.

| new identifier | resolves to | attribution | verdict |
|---|---|---|---|
| arXiv:2111.05881 | Chen, Cotler, Huang, Li, "Exponential separations between learning with and without quantum memory" (2021) | used for exponential separations against protocols without quantum memory | **correct** |
| arXiv:2112.00778 / DOI:10.1126/science.abn7293 | Huang, Broughton, Cotler, Chen, Li, Mohseni, Neven, Babbush, Kueng, Preskill, McClean, "Quantum advantage in learning from experiments", Science 376, 1182 (2022) | same use | **correct** |
| DOI:10.1103/PhysRevA.81.062345 | Laumann, Läuchli, Moessner, Scardicchio, Sondhi, "Product, generic, and random generic quantum satisfiability", PRA 81, 062345 (2010) | product-satisfiability geometry / geometrization | **correct** |
| DOI:10.1016/0304-3975(79)90044-6 | Valiant, **"The complexity of computing the permanent"**, Theor. Comput. Sci. **8**, 189–201 (1979) | cited three times for **`#2-SAT` hardness** | **WRONG PAPER — O23** |
| DOI:10.1007/s00029-024-00935-5 | Feigin, Makhlin, **"Relative poset polytopes and semitoric degenerations"**, Selecta Math. **30** (2024), arXiv:2112.05894 | cited as **"Theorem 1.8.1"**, the **multiprojective Nullstellensatz** | **FABRICATED ATTRIBUTION — O22** |

Two of the five new identifiers are defective, in a repair whose whole subject was reference
verification. Both are of the same kind: the reference list prints the *correct* title of the
cited work, and the body then attributes to it a theorem that work does not contain.

---

## Objections (new; changed text only)

### O22 — FATAL — a fabricated theorem attribution is the sole source for the multiprojective Nullstellensatz

**Location.** `D-QN-MULTIPROJECTIVE-SATURATION`, `Source:` line —
"[Feigin–Makhlin, Theorem 1.8.1](https://doi.org/10.1007/s00029-024-00935-5)"; step **4.9
COMPLETENESS**, leaf "[D-QN-MULTIPROJECTIVE-SATURATION; [Feigin–Makhlin, Theorem
1.8.1](https://doi.org/10.1007/s00029-024-00935-5)]"; reference **31**.

**Computation.** Crossref (`api.crossref.org/works/10.1007/s00029-024-00935-5`) returns:
TITLE "Relative poset polytopes and semitoric degenerations"; AUTHORS Evgeny Feigin, Igor Makhlin;
VENUE Selecta Mathematica, vol. 30, 2024. Abstract (verbatim, first sentence): "*The two best
studied toric degenerations of the flag variety are those given by the Gelfand–Tsetlin and FFLV
polytopes.*" Preprint arXiv:2112.05894, same title. The paper is about relative poset polytopes,
regular subdivisions, and semitoric degenerations of flag varieties. It contains no multiprojective
Nullstellensatz, and there is no basis for a "Theorem 1.8.1" of that content. The memo's own
reference 31 prints the correct title, so the body's use contradicts its own bibliography.

**Aggravating.** This is the **only** external source offered for the statement
`\sqrt{I:B^\infty}=I(V_{X_0}(I))`, which is load-bearing for the definition, for step 2.4/2.5, for
step 4.6's `e_Q=\operatorname{HF}(\mathbf1)`, and hence for rows
`C-NEW-QN-PRODUCT-SPAN-DEFECT` and `C-NEW-QN-HILBERT-VANISH-ENTANGLEMENT`. Under the r1 brief's
rule ("fabricated FATAL for the dependent row") this is FATAL for that definition and those rows.

**Mitigating (L5, honestly).** The **mathematics is correct and I verified it in r1**: the
product-span identity and the `e_Q` formula were checked numerically on three point sets and an
explicit `e_Q=1` instance. Moreover the direction the memo actually *uses* at 4.9 is proved
self-containedly in the memo's own two lines (`V=\varnothing\Rightarrow B\subseteq\sqrt I\Rightarrow
B^k\subseteq I`, and every monomial of multidegree `\ge(k,\dots,k)` lies in `B^k`), so that leaf
needs no citation at all. Only the "`J` is the vanishing ideal of `V_{X_0}(I)`" direction needs a
source, and that is textbook multigraded commutative algebra.

**FIX DEMAND.** Delete the Feigin–Makhlin citation from the `Source:` line, from the 4.9 leaf and
from the reference list. Replace it either with (i) a fetched, resolved source for the
multiprojective/multigraded Nullstellensatz — for instance a Cox-ring or multigraded-Nullstellensatz
reference whose statement is quoted — or (ii) a two-line proof in the memo (the affine
Nullstellensatz applied to the affine cone with `V(B)` removed), in which case the entry cites
nothing external. Mark `[UNVERIFIED]` per CLAUDE.md rule 6 if no identifier is actually fetched.
Additionally: re-audit every citation introduced in this repair round before the next submission.

**SURVIVING STATEMENT.** `\sqrt{I:B^\infty}` is the multihomogeneous vanishing ideal of
`V_{X_0}(I)\subseteq(\mathbb P^{q-1})^n`, with the convention `I(\varnothing)=R`; if
`V_{X_0}(I)=\varnothing` then `I:B^\infty=R` and `I_{\mathbf r}=R_{\mathbf r}` for all
`\mathbf r\ge(k,\dots,k)`. Both facts stand; the citation does not.

### O23 — MAJOR — the Valiant DOI is the permanent paper, not the `#2-SAT` counting paper

**Location.** QSAT dictionary, row "Exact `\operatorname{HF}_{R/I_Q}(\mathbf1)`", reference cell;
"Complexity conclusions", bullet 2; killer **K-QN3**; reference **28**.

**Computation.** Crossref: `10.1016/0304-3975(79)90044-6` = L. G. Valiant, "The complexity of
computing the permanent", *Theoretical Computer Science* **8**, 189–201 (1979). That paper proves
`#P`-completeness of the 0/1 permanent; it is not the source for `#P`-completeness of counting
satisfying assignments of 2-CNF. The standard source is `10.1137/0208032` = Leslie G. Valiant, "The
Complexity of Enumeration and Reliability Problems", *SIAM Journal on Computing* **8**(3), 410–421
(1979) (Crossref-confirmed). The memo's own reference 28 prints the *permanent* title while the
three body citations attribute `#2-SAT` hardness to it.

**FIX DEMAND.** Replace `DOI:10.1016/0304-3975(79)90044-6` by `DOI:10.1137/0208032` in all three
body loci and in the reference list, with the title "The Complexity of Enumeration and Reliability
Problems"; name the counting problem precisely (`#2-SAT`, or `#`MONOTONE-2-SAT, whichever the
composition with Ji–Wei–Zeng actually needs) and say which theorem of that paper supplies it. If the
permanent paper is wanted elsewhere, keep it as a separate entry.

**SURVIVING STATEMENT.** Computing `\operatorname{HF}_{R/I_Q}(\mathbf1)` exactly is `#P`-hard
already for qubit 2-QSAT, by Ji–Wei–Zeng's equivalence with the classical counting analogue
(arXiv:1010.2480, DOI 10.1103/PhysRevA.84.042338) composed with `#P`-completeness of counting
2-CNF solutions (Valiant 1979, SIAM J. Comput.); see `D-hardness-anchors`. The decision problem
remains in P.

### O24 — MINOR — the HOLD marker sits inside the `status:` field, and the statement repeats the status

**Location.** `C-NEW-QN-ARM-D-NORTHSTAR`: `status: CONJECTURE; HOLD — do not merge as discharging
the PRD §4 Arm D sentence`; the statement itself opens `statement: CONJECTURE: For every algorithm
family …`.

**Computation.** L1 admits exactly four status values, `{PROVED, SKETCH, CONJECTURE, REFUTED}`. A
`status:` cell reading `CONJECTURE; HOLD — …` is not one of them and would break any grep-based
ratchet audit of `claims/CLAIMS.md`; and a status word inside the `statement:` field duplicates the
status in the one place L1 says a status must not live.

**FIX DEMAND.** Split into
`- status: CONJECTURE` and a separate field
`- hold: do not merge as discharging the PRD §4 Arm D sentence; the broad Arm D negative remains an
open negative`, and delete the leading `CONJECTURE:` from the statement text.

**SURVIVING STATEMENT.** The row's content is correct and is the r1-demanded scoping; only its
field layout is illegal.

### O25 — MINOR — the copy-residual defining equation is off by a conjugation, against C3

**Location.** `D-QN-COPY-RESIDUAL-OBSERVABLE`, "let `|F_j\rangle\in\operatorname{Sym}^m(\mathcal H)`
satisfy, under C3, `f_j(\overline\psi)=\langle F_j|\psi^{\otimes m}\rangle`"; the same equation in
`C-NEW-QN-COPY-RESIDUAL`; the corresponding line in "What the seed can estimate from copies".

**Computation.** With `|F\rangle` the C-019 tensor of a degree-`m` form
(`|F\rangle=\sum_\alpha f_\alpha(\alpha!/m!)\sum_{{\rm content}(w)=\alpha}|w\rangle`), a direct
computation gives `\langle F|\psi^{\otimes m}\rangle=\sum_\alpha\overline{f_\alpha}\psi^\alpha
=\overline{f(\overline\psi)}`. Numerically (`q=2, n=3, m=2`, random complex form and state):
`\langle F|\psi^{\otimes 2}\rangle = 0.1092567019+0.6211036221i`, `f(\overline\psi) =
0.1092567019-0.6211036221i`, so the identity holds against `\overline{f(\overline\psi)}` and fails
against `f(\overline\psi)`. The same run confirms `\|F\|=\|f\|_{\rm BW}` to `1e-15` and
`\|\sum_j w_j|F_j\rangle\langle F_j|\|\le\Lambda` (so `0\le A_F\le\mathbb1` is correct).

**FIX DEMAND.** Write either `\overline{f_j(\overline\psi)}=\langle F_j|\psi^{\otimes m}\rangle`
with `|F_j\rangle` the C-019 tensor, or keep the displayed equation and say that `|F_j\rangle` is the
*conjugate* of the C-019 tensor (its BW norm is unchanged, so `\|F_j\|=\|f_j\|_{\rm BW}` survives
either way). Same edit in the row and in the prose.

**SURVIVING STATEMENT.** `\langle\psi|^{\otimes m}A_F|\psi\rangle^{\otimes m}
=\Lambda^{-1}\sum_j w_j|f_j(\overline\psi)|^2` is correct under either convention, because only the
modulus enters; `\Lambda=\sum_j w_j\|F_j\|^2` does give `0\le A_F\le\mathbb 1`.

### O26 — MINOR — conventions are cited in `depends-on`, colliding with the claim-id namespace

**Location.** `C-NEW-QN-SINGLET-HILBERT-WITNESS`, `depends-on: … D-macaulay-matrix, C1`;
`C-NEW-QN-RESIDUAL-EQUALS-DISTANCE`, `depends-on: … D-condition-number, C3`.

**Computation.** `C1` and `C3` are frozen conventions of `definitions/definitions.md`, while the DAG
namespace is `C-###` (`grep '^### C-' claims/CLAIMS.md`). A `depends-on` cell containing `C1` or
`C3` cannot be resolved by the ratchet audit and reads as a malformed claim id. Both rows already
cite the convention correctly *inside* the statement text.

**FIX DEMAND.** Remove `C1` and `C3` from both `depends-on` lists; keep the in-statement references,
written as "convention C1 of `definitions/definitions.md`".

**SURVIVING STATEMENT.** Unaffected.

### O27 — MINOR — two citation loci inside arXiv:2412.19623 are imprecise

**Location.** Step 7.3, `[arXiv:2412.19623, Definition 52]` attached to the Chow ring
`\mathbb Z[h_1,\dots,h_n]/(h_1^q,\dots,h_n^q)`; step 6.4, the same locus attached to
"four meet in `4!=24` points".

**Computation.** From the paper's HTML (fetched in r1): Definition 52 defines the Bézout number;
the Chow-ring/intersection setup is the surrounding §5.1 material (their Eq. (16),
`[V_1]\cdots[V_r]=NH_1^{d_1-1}\cdots H_n^{d_n-1}`). The 6.4 count is elementary multiprojective
intersection theory needing no external source (I recomputed the degree 24 in r1, via the diagonal
Hilbert profile 23, 24, 24, 24 at `r=2,3,4,5`). After a whole round spent on citation loci, these
should be exact.

**FIX DEMAND.** Cite §5.1 / Eq. (16) of arXiv:2412.19623 for the Chow ring, Definition 52 only for
the Bézout coefficient, and drop the citation from 6.4 or replace it with `D-multihomogeneous-bezout`
alone.

**SURVIVING STATEMENT.** Both mathematical statements are correct.

### O28 — MINOR — `where-tested` now points at a verdict, whose scripts are not in the repo

**Location.** Seven rows now read `where-tested: … recomputed in \`verdicts/quantum-native-r1.md\``.

**Computation.** That verdict records the numbers, but the two red-capable scripts that produced
them ran in this critic's session scratchpad and are not committed. Under L4 "runs without errors"
is never a test, and a `where-tested` pointer that no one can re-execute is weaker than the field
implies. This is the practical consequence of the O19 residue, and it is the orchestrator's to
resolve, not the read-only lane's.

**FIX DEMAND.** On merge, either (a) commit the two checkers under `checkers/` with recorded red
mutations in `checkers/MUTATIONS.md` and repoint `where-tested` at them, or (b) reword the field as
`where-tested: numbers recorded in verdicts/quantum-native-r1.md; no executable checker`.

**SURVIVING STATEMENT.** Every number cited from the r1 verdict was independently recomputed and is
correct.

---

## Per-row decision table (all 13 rows)

On PASS the orchestrator merges verbatim from this table. The two rows marked *conditional* carry no
text change of their own; they are blocked only by O22 in a definition they depend on.

| # | id | decision | status to merge | note |
|---|---|---|---|---|
| 1 | `C-NEW-QN-QSAT-INVERSE-SYSTEM` | **ACCEPT AS CONJECTURE** | CONJECTURE | Text is the r1-demanded wording verbatim; depends-on complete (O21); verified numerically on four instances in r1. Merge as written. |
| 2 | `C-NEW-QN-PRODUCT-SPAN-DEFECT` | **ACCEPT AS CONJECTURE**, conditional on O22 | CONJECTURE | Row text needs no change; it depends on `D-QN-MULTIPROJECTIVE-SATURATION`, which must lose the fabricated source first. |
| 3 | `C-NEW-QN-HILBERT-VANISH-ENTANGLEMENT` | **ACCEPT AS CONJECTURE**, conditional on O22 | CONJECTURE | Same. The widened quantifier ("every multihomogeneous ideal in the Cox ring"), the `\mathbf r\ne\mathbf1` exclusion, the `I(\varnothing)=R` convention and the existential-completeness clause are all as demanded. |
| 4 | `C-NEW-QN-SINGLET-HILBERT-WITNESS` | **ACCEPT WITH REWORDING** | CONJECTURE | Exact change: `depends-on: C-NEW-QN-QSAT-INVERSE-SYSTEM, C-NEW-QN-HILBERT-VANISH-ENTANGLEMENT, D-macaulay-matrix` (delete `C1`; the statement already says "basis-dependent under C1"). Statement otherwise merges verbatim — all four numbers recomputed. |
| 5 | `C-NEW-QN-HF2-COMPLETE` | **ACCEPT AS REFUTED** | REFUTED | Surviving statement to merge verbatim: "Vanishing at `(2,\dots,2)` is sufficient for the absence of product ground states, but nonvanishing is inconclusive. For five generic four-local rank-one clause vectors on four qubits, `HF(1^4)=11`, `HF(2^4)=11`, `HF(3^4)=1`, and `HF(4^4)=0`; the product variety is empty and the first certifying diagonal level is `r=4`." Independently recomputed. |
| 6 | `C-NEW-QN-BEZOUT-NOVELTY` | **ACCEPT AS REFUTED** | REFUTED | Surviving statement merges verbatim; every attribution in it was checked against the paper's full HTML (Definition 52, Observation 55, the perfect-matching remark; "permanent" absent) and against Crossref for Laumann et al. and arXiv:2005.14485. |
| 7 | `C-NEW-QN-COPY-RESIDUAL` | **ACCEPT WITH REWORDING** | CONJECTURE | Exact change: replace `f_j(\bar\psi)=⟨F_j\|\psi^{⊗m}⟩` by `\overline{f_j(\bar\psi)}=⟨F_j\|\psi^{⊗m}⟩` (O25). Everything else — `Λ=Σ_j w_j\|F_j\|²`, `0≤A_F≤1`, `\|F_j\|=\|f_j\|_{BW}` by C-019, access case 1, `m·O(ε^{-2}\log(1/δ))` copies — merges verbatim and was verified numerically. |
| 8 | `C-NEW-QN-RESIDUAL-EQUALS-DISTANCE` | **ACCEPT WITH REWORDING** | REFUTED | Exact change: `depends-on: D-QN-COPY-RESIDUAL-OBSERVABLE, D-condition-number` (delete `C3`; O26). Surviving statement merges verbatim. |
| 9 | `C-NEW-QN-MPS-TOMOGRAPHY-SPEEDUP` | **ACCEPT AS REFUTED** | REFUTED | Surviving statement merges verbatim; it now rests the refutation on CLAUDE.md §1 / PRD §1 novelty and the different-output comparator, records that PRD §2 has no novelty criterion and that criterion 3 admits the input model, and defers the single-copy comparator to Question 6 with both separations cited but no transfer claimed. All three references refetched. |
| 10 | `C-NEW-QN-COHERENT-OVERLAP-PERMANENT` | **ACCEPT AS REFUTED** | REFUTED | Surviving statement merges verbatim; it cites and distinguishes C-296 and foregrounds the JSV-FPRAS point (DOI 10.1145/1008731.1008738, Crossref-confirmed in r1). |
| 11 | `C-NEW-QN-OPTICAL-SINGLET-DEMO` | **ACCEPT AS CONJECTURE** | CONJECTURE | The `1/2` preparation and the 119-shot Hoeffding count were recomputed in r1; the acceptance is now correctly conditioned with `\eta_{\rm sector}/4` unconditioned and the missing ingredients named; `C-297` is in depends-on. Merge as written. |
| 12 | `C-NEW-QN-C024-WEAKENING` | **ACCEPT AS CONJECTURE** | CONJECTURE | Merge as written, **including its `lockstep:` field**. On merge the orchestrator must move C-024's final clause, its shard, HANDOFF and the PRD §4 Arm A sentence in the same commit; C-024 itself stays SKETCH with the clause corrected. |
| 13 | `C-NEW-QN-ARM-D-NORTHSTAR` | **HOLD** (merge only with the O24 field split) | CONJECTURE + `hold:` field | Content is exactly the r1-demanded scoping and is correct. Field layout is illegal (O24): merge as `status: CONJECTURE` plus `hold: do not merge as discharging the PRD §4 Arm D sentence; the broad Arm D negative remains an open negative`, with the leading `CONJECTURE:` deleted from the statement. |

Counts (13 rows): **ACCEPT AS CONJECTURE 5** (rows 1, 2, 3, 11, 12; rows 2 and 3 conditional on
O22) · **ACCEPT AS REFUTED 4** (rows 5, 6, 9, 10) · **ACCEPT WITH REWORDING 3** (rows 4, 7, 8) ·
**HOLD 1** (row 13, `C-NEW-QN-ARM-D-NORTHSTAR`) · **REJECT 0** · **ACCEPT AS SKETCH 0** (no
proposed row is an imported published theorem).

## Per-definition decision table

| id | decision | note |
|---|---|---|
| `D-QN-QSAT-IDEAL` | **ACCEPT** | The added decomposition-independence claim is correct: I verified numerically (6 trials, `n=4, q=2`, rank-2 clause, random unitary rebasing) that the two rank-one decompositions of the same projector generate the same `(I_Q)_{\mathbf1}` (projectors onto the two column spans agree to `1e-9`). The unconjugated-coefficient pitfall is stated. |
| `D-QN-MULTIPROJECTIVE-SATURATION` | **ACCEPT WITH REWORDING** | **O22 is here.** Merge only after the `Source:` line drops "[Feigin–Makhlin, Theorem 1.8.1](https://doi.org/10.1007/s00029-024-00935-5)" and either supplies a fetched multigraded-Nullstellensatz source or gives the two-line proof. Everything else (reduced closed subscheme of any dimension, `I(\varnothing)=R`, the `B^k\subseteq I` argument, the degreewise-equality pitfall) merges verbatim. |
| `D-QN-PRODUCT-SPAN` | **ACCEPT** | Now carries the explicit coherent-state form and `\mathcal P_Q=\{0\}` when the variety is empty. Verified in r1 on three point sets. |
| `D-QN-MULTIGRADED-ENTANGLED-DEFECT` | **ACCEPT** | Unchanged and correct; verified in r1 on an explicit `e_Q=1` instance. |
| `D-QN-COPY-RESIDUAL-OBSERVABLE` | **ACCEPT WITH REWORDING** | Exact change per O25: `\overline{f_j(\overline\psi)}=\langle F_j|\psi^{\otimes m}\rangle`. `\Lambda`, the `0\le A_F\le\mathbb1` bound, the C-019 norm identity and "each shot consumes `m` copies" are all verified and merge verbatim. |
| `D-QN-TENSOR-NETWORK-VARIETY` | **ACCEPT** | Edge-flattening support now correctly attributed to arXiv:2608.19071, with arXiv:1501.01120 relabelled. |
| `D-QN-PHYSICAL-DATA-ACCESS` | **ACCEPT** | Now states that it **extends** `D-input-model` and defines the classical copy-access baseline as single-copy, possibly adaptive measurement with classical post-processing. |
| `D-QN-DUAL-RAIL-SECTOR` | **ACCEPT** | Unchanged; correct. |
| `D-multihomogeneous-bezout amendment` | **ACCEPT** (as an amendment to the existing register entry, not a new id) | Correctly declares "No D-QN-PRODUCT-BEZOUT-NUMBER is proposed" and splits the attribution (AGR Def. 52 / Obs. 55 for the PRODSAT Bézout/weighted-SDR formulation; arXiv:2005.14485 for the permanent formulation). `B_D=\operatorname{per}(D)` at `q=2` was recomputed on 40 random incidence matrices in r1. |

Counts (9 entries): **ACCEPT 7** · **ACCEPT WITH REWORDING 2** (`D-QN-MULTIPROJECTIVE-SATURATION`,
`D-QN-COPY-RESIDUAL-OBSERVABLE`) · **REJECT 0**. `D-QN-PRODUCT-BEZOUT-NUMBER` is withdrawn by the
proposer and is not adjudicated.

## LOCKSTEP

**Dictionary table** — moved: the single `HF(1)>0` row is split into promise / exact-nonvanishing /
exact-count rows citing C-034–C-037, C-038 and `D-hardness-anchors`; `V_{X_0}(I_Q)` now cites
Laumann et al.; the Bézout row cites `D-multihomogeneous-bezout` + C-295 + JSV; `J_Q` reads "reduced
closed product-solution subscheme, of any dimension"; the `HF(\mathbf r)=0` row is relabelled a
multihomogeneous Nullstellensatz certificate. **North-star section** — moved: verdict, criteria
audit (two-column), 8.1–8.10 scope boundary, and the PRD Q13 bullets all restricted in the same
sense as the row. **Killers** — moved: K-QN3 (no `#P`-complete claim), K-QN15 (cites C-296),
K-QN16 (cites C-298), K-QN17 (cites the surviving C-041/C-043/C-044). **Rows** — moved: 12 → 13,
with `C-NEW-QN-C024-WEAKENING` added and its own `lockstep:` field naming C-024, its shard, HANDOFF
and PRD §4 Arm A. **Definitions** — moved: `D-QN-PRODUCT-BEZOUT-NUMBER` withdrawn and replaced by an
amendment proposal; `D-QN-PHYSICAL-DATA-ACCESS` subordinated to `D-input-model`. **Verdict:
lockstep is intact across all five artifacts.** Two orchestrator-side items remain on merge: the
C-024 clause and PRD §4 Arm A must move in the same commit as row 12, and PRD §4 arm D's sentence
"a speedup in the north-star sense is not on offer here" must be annotated as an open negative,
since row 13 explicitly does not discharge it.

## Objection counts (round 2)

**FATAL 1 (O22) · MAJOR 1 (O23) · MINOR 5 (O24–O28).**
Trajectory: r1 FAIL(12 MAJOR, 9 MINOR, 0 FATAL) → r2 FAIL(1 FATAL, 1 MAJOR, 5 MINOR). All 21 r1
objections are correctly dispositioned; both new substantive defects are citation defects
introduced by the repair itself, and both have a one-line fix that changes no mathematics.

VERDICT: FAIL(1 FATAL, 1 MAJOR, 5 MINOR)
