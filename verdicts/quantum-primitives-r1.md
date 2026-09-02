<!-- ROLE: adversarial critic verdict, round 1, on scouting/quantum-primitives.md (rk-light L5).
     UPDATE POLICY: append-only; a round-2 verdict is a new file. -->

# Verdict: scouting/quantum-primitives.md, round 1

- **Target:** `scouting/quantum-primitives.md` (2230 lines, 10 primitives + 5 sub-primitives, 14 ranked rows, 3 combinations, 23 proposed claim rows, 12 proposed definitions, 66 references).
- **Date:** 2026-09-02.
- **Critic model:** Claude Opus 5 (1M), adversarial critic seat. Proposer was a codex lane (different family), as rule 1 requires.
- **Files read:** `CLAUDE.md`; `PRD.md` (§2, §3, §4, §6, §7); `definitions/definitions.md` (conventions C1–C12; D-input-model, D-hardness-anchors, D-finite-field-analogue, D-toric-ideal, D-residual-spectral-hierarchy, D-ground-space); `claims/CLAIMS.md` (§5, §6, C-009/024/052/055/056/057/058/061/068/078/088/091/092/096/097/099/150/154/166/262/275–280); `scouting/quantum-primitives.md` (whole); `briefs/lane-quantum-primitives.md` (read as context, **not** as evidence); `scouting/classical-landscape.md` (§1–§2, §3 "Best classical algorithms", section index); `scouting/applications-wide-net.md` (F2, Observations A/B, shortlist); `scouting/real-variety.md` (Route 7).
- **Network fetches:** 66 memo references resolved (arXiv Atom API in 2 batches: 52 entries; Crossref `works` API: 39 DOIs), plus 6 candidate omitted references and 2 Griffiths DOIs, plus 4 full-text PDFs downloaded and text-extracted (`2111.00405v2`, `0705.2784v1`, `2111.13224v2`, `1311.3297v1`, `2209.13581v3`, `math/0411623v3`) and 1 publisher landing page (`quantum-journal.org/papers/q-2023-07-26-1069/`), 1 web search (Bernstein–Yang exponents). Total network requests: 15 curl/urllib calls + 1 WebSearch + 1 failed WebFetch (cr.yp.to, HTTP parse error; routed around by search).
- **Commands run (all `timeout`-bounded, all exit 0 unless noted):** `curl` (arXiv Atom API ×3, Crossref ×3 batches, PDF ×6, Quantum landing page ×1); `pdftotext` / `pdftotext -layout` ×7; `grep`/`sed`/`awk` ×~30; `python3` recomputation ×4 (reference parsing; multihomogeneous-Bézout/permanent identity `sympy` check, n=3,4,5, 3 random nonnegative integer matrices each — all equal; Jacobian Hilbert-series check for (n,d) = (2,3),(2,4),(3,3) — all match the closed form and Σ = (d−1)^{n+1}; D-id and C-id existence audit over the repo). One `curl` against `http://export.arxiv.org` returned empty (plain HTTP blocked in sandbox); re-run over HTTPS, exit 0. One `WebFetch` on `cr.yp.to` failed with a Content-Length/Transfer-Encoding parse error.

Departures from conventions: none. This verdict uses C1–C12 and cites D-ids.

---

## 1. Reference table (obligation 1)

Every one of the 66 memo references was resolved against the arXiv Atom API and/or Crossref; **no reference is fabricated**. "Attribution" = does the source actually state what the memo attributes to it.

| # | short ref | identifier | resolves | attribution | note |
|---|---|---|---|---|---|
| 1 | Chen–Gao, Boolean equation solving | arXiv:1712.06239; DOI 10.1007/s11424-020-0028-6 | Y | Y | journal title is singular "Algorithm"; DOI never cited in body |
| 2 | Ding–Gheorghiu–Gilyén–Hallgren–Li | arXiv:2111.00405; DOI 10.22331/q-2023-07-26-1069 | Y | **N** | see O1: memo's κ = Ω(√C(n,h)) is not the paper's bound; matrix sizes, VV/copy counts, h^h/2, n=300 all verified correct |
| 3 | Harrow–Hassidim–Lloyd | DOI 10.1103/PhysRevLett.103.150502 | Y | Y | |
| 4 | Gilyén–Su–Low–Wiebe, QSVT | arXiv:1806.01838; DOI 10.1145/3313276.3316366 | Y | Y | |
| 5 | Bardet–Faugère–Salvy–Spaenlehauer | arXiv:1112.6263 | Y | Y | O(2^{0.792n}) Las Vegas, m=n, under stated algebraic assumptions — exact |
| 6 | Faugère–Horan–Kahrobaei–Kaplan–Kashefi–Perret | arXiv:1712.07211 | Y | Y | O(2^{0.462n}) quantum gates, n=m — exact |
| 7 | Bernstein–Yang | DOI 10.1007/978-3-319-79063-3_23 | Y | Y | t≈0.45743, a≈0.01467 confirmed (AT exponent 0.47210) |
| 8 | Tang, recommendation systems | arXiv:1807.04271; DOI 10.1145/3313276.3316310 | Y | n/a | **listed but never cited in the body** (O21) |
| 9 | Gilyén–Lloyd–Tang | arXiv:1811.04909 | Y | Y | |
| 10 | Chia–Gilyén–Li–Lin–Tang–Wang | arXiv:1910.06151; DOI 10.1145/3357713.3384314 | Y | Y | |
| 11 | Gharibian–Le Gall | arXiv:2111.09079 | Y | Y | published DOI 10.1137/22M1513721 (memo gives none) |
| 12 | Kedlaya, quantum zeta of curves | arXiv:math/0411623; DOI 10.1007/s00037-006-0204-7 | Y | **partial** | Theorem 1, Prop 11 (16g<q^{e/2}), m=max{18,2g}, §10 Question 12 all verified; the "(log q)^{O(g² log g)}" bound is **not in the paper** (O2) |
| 13 | Lauder–Wan | arXiv:math/0612147 | Y | Y | "fixed dimension, small characteristic, deterministic poly time" — exact |
| 14 | Costa–Harvey–Kedlaya | arXiv:1806.00368 | Y | Y | "linear time in p" exact; memo drops "ample", "projectively normal" |
| 15 | Roy–Saxena–Venkatesh | arXiv:2511.02262 | Y | partial | AM protocol confirmed; "AM ∩ coAM" is the memo's inference, abstract says AM certification; P₁(T) bounds exact |
| 16 | van Dam, zeta zeroes | arXiv:quant-ph/0405081 | Y | Y | corroborated by Kedlaya §10 |
| 17 | Wang–Fei–Wu (the wrong-ID paper) | arXiv:quant-ph/0608151; DOI 10.1088/0305-4470/39/36/L01 | Y | Y | correction stands |
| 18 | Childs–Schulman–Vazirani | arXiv:0705.2784; DOI 10.1109/FOCS.2007.18 | Y | Y | Thm 1 (expected exponential classical, 1/poly(d log q) bias), Thm 3 (d odd, poly(log q) queries), Lemma 4 walk time t = 1/√(q^{d−1} log q) with per-point prob. \|H\|⁻¹[1/log q + O(log^{−3/2} q)] — **all exact** |
| 19 | Decker–Draisma–Wocjan | arXiv:0706.1219 | Y | Y | Ω(√q) classical, polylog(q) quantum, all but finitely many q — exact |
| 20 | Decker–Ivanyos–Santha–Wocjan | arXiv:1107.2189; DOI 10.1137/120864416 | Y | partial | abstract confirms quadratic hidden polynomial problems; "constant characteristic"/"arbitrary fields" qualifiers not confirmable from the abstract |
| 21 | Ivanyos–Santha | arXiv:1503.09016 | Y | Y | exact |
| 22 | Witten, SUSY and Morse theory | DOI 10.4310/jdg/1214437492 | Y | Y | JDG 1982 |
| 23 | Lerche–Vafa–Warner | DOI 10.1016/0550-3213(89)90474-4 | Y | Y | |
| 24 | Vafa–Warner | DOI 10.1016/0370-2693(89)90473-5 | Y | n/a | **listed but never cited in the body** (O21) |
| 25 | Griffiths | DOI 10.2307/1970746 | Y | **N** | DOI is Part **I** (p. 460); memo's title says II (Part II = 10.2307/1970747) (O12) |
| 26 | Kedlaya, p-adic cohomology | arXiv:math/0403233 | Y | Y | |
| 27 | Lloyd–Garnerone–Zanardi | arXiv:1408.3106; DOI 10.1038/ncomms10138 | Y | Y | published title drops "big" |
| 28 | Berry–Su–Gyurik–King–Basso | arXiv:2209.13581; DOI 10.1103/PRXQuantum.5.010319 | Y | **partial** | Lemma 1 eq. (12) matches except `n log₂ n` transcribed as `s log² s` (O14); "super-quadratic only for multiplicative error with growing β" and "tens of billions of Toffolis" exact |
| 29 | Apers–Gribling–Sen–Szabó | arXiv:2211.09618 | Y | partial | exponents exact; memo adds a `poly(s)` factor not in the source (O14); published DOI 10.22331/q-2023-12-06-1202 |
| 30 | Schmidhuber–Lloyd | arXiv:2209.14286; DOI 10.1103/PRXQuantum.4.040349 | Y | partial | #P-hard exact; source says "**multiplicative approximation** is NP-hard", memo says "deciding nonzero is NP-hard"; memo **omits the paper's escape clause** (O7) |
| 31 | Niyogi–Smale–Weinberger | DOI 10.1007/s00454-006-1250-7 | Y | partial | it is a submanifold / union-of-balls result, not a Vietoris–Rips persistence result (O6) |
| 32 | Brassard–Høyer–Mosca–Tapp | arXiv:quant-ph/0005055 | Y | Y | DOI 10.1090/conm/305/05215 |
| 33 | Duff–Hill–Jensen–Lee–Leykin | arXiv:1609.08722 | Y | Y | "expected number of paths tracked is linear in the number of solutions" — exact |
| 34 | Lairez | arXiv:1507.05485; DOI 10.1007/s10208-016-9319-7 | Y | Y | |
| 35 | Chien–Fan–Abdelfattah–Tsigaridas–Tomov | arXiv:2112.03444 | Y | Y | "up to 26 times" exact; **memo's initials wrong** (Chiang-Heng Chien, not "C.-F. Chien") (O21) |
| 36 | van Apeldoorn–Gilyén | arXiv:1904.03180 | Y | Y | Õ(√(n+m)/ε³) dense — exact |
| 37 | Aaronson–Arkhipov | arXiv:1011.3245 | Y | Y | |
| 38 | Hamilton et al., GBS | arXiv:1612.01199; DOI 10.1103/PhysRevLett.119.170501 | Y | Y | |
| 39 | Quesada–Arrazola–Killoran | arXiv:1807.01639; DOI 10.1103/PhysRevA.98.062322 | Y | Y | |
| 40 | "Gritzmann and Klee", mixed volumes | DOI 10.1137/S0097539794278384 | Y | **N** | the paper is **Dyer, Gritzmann and Hufnagel**, SIAM J. Comput. 1998 (O3). The #P-hardness content is correct |
| 41 | Jerrum–Sinclair–Vigoda | DOI 10.1145/1008731.1008738 | Y | Y | |
| 42 | Aaronson–Hance | arXiv:1212.0025 | Y | Y | ε‖A‖ⁿ additive in O(n²/ε²) — exact |
| 43 | Dickenstein–Tobis | arXiv:1003.3508; DOI 10.1142/S0218196711006819 | Y | Y | matches C-092's corrected citation |
| 44 | Lloyd, universal simulators | DOI 10.1126/science.273.5278.1073 | Y | Y | |
| 45 | Anschuetz–Bauer–Kiani–Lloyd | arXiv:2211.16998; DOI 10.22331/q-2023-11-28-1189 | Y | Y | **this resolves C-099's `[UNVERIFIED]` mark** (O23) |
| 46 | Law–Pu–Bigelow | arXiv:cond-mat/9807258; DOI 10.1103/PhysRevLett.81.5257 | Y | Y | |
| 47 | Childs–Gosset–Webb | DOI 10.4086/toc.2015.v011a020 | Y | Y | "Frustration-Free Bose–Hubbard Hamiltonian is QMA-hard" is genuinely in the paper (arXiv:1311.3297 §1); "lattice-local" is wrong, it is an arbitrary graph (O22) |
| 48 | Ramos-Calderer et al. | arXiv:2111.13224; DOI 10.1103/PhysRevResearch.4.013096 | Y | Y | 2^{(n+2)/2}−2 / 3·2^{(n−1)/2}−2, eq. (10), 46/179, 67/167, 114/221, 1000-sample run, <80 000 and <300 000 logical — **every number verified** |
| 49 | Dridi–Alghassi | arXiv:1604.05796; DOI 10.1038/srep43048 | Y | Y | "all bi-primes up to just over 200 000" — exact |
| 50 | Alghassi–Dridi–Tayur | arXiv:1902.04215 | Y | Y | Graver, not Gröbner — exact |
| 51 | Chang–Gambhir–Humble–Sota | arXiv:1812.06917 | Y | partial | second-order system on an annealer confirmed; the 10⁻⁸ tolerance is body-level, not verified here |
| 52 | Boulebnane–Montanaro | arXiv:2208.06909; DOI 10.1103/PRXQuantum.5.030348 | Y | Y | "around 14 layers matches WalkSATlm, more layers outperform" — exact |
| 53 | Lloyd–Mohseni–Rebentrost | arXiv:1307.0401 | Y | Y | DOI 10.1038/nphys3029 |
| 54 | Gu–Wang–Lee–Zhang | arXiv:1908.00719 | Y | Y | "exponential speedup" claim is the paper's own |
| 55 | Hillar–Lim | arXiv:0911.1393; DOI 10.1145/2512329 | Y | Y | |
| 56 | Bernardi–Daleo–Hauenstein–Mourrain | arXiv:1512.04312; DOI 10.1016/j.difgeo.2017.07.009 | Y | Y | |
| 57 | Temme–Osborne–Vollbrecht–Poulin–Verstraete | arXiv:0911.3635 | Y | Y | "no universal fast-mixing theorem" — correct |
| 58 | Wocjan–Chiang–Abeyesinghe–Nagaj | arXiv:0811.0596 | Y | **partial** | the theorem is an FPRAS/annealing result with non-adaptive cooling, not a warm-start preparation theorem (O17) |
| 59 | Arunachalam–Havlíček–Nannicini–Temme–Wocjan | arXiv:2009.11270 | Y | Y | |
| 60 | Chakrabarti–Childs–Hung–Li–Wang | arXiv:1908.03903; DOI 10.1145/3588579 | Y | Y | all four exponents exact; memo **omits** the paper's Ω(√d + 1/ε) quantum lower bound (O25) |
| 61 | Barvinok | DOI 10.1287/moor.19.4.769 | Y | Y | |
| 62 | Barvinok–Woods | arXiv:math/0211146; DOI 10.1090/S0894-0347-03-00428-4 | Y | Y | |
| 63 | Shor | DOI 10.1137/S0097539795293172 | Y | Y | |
| 64 | Roetteler | arXiv:0911.4724 | Y | Y | quadratic-form hidden shift — exact |
| 65 | Gavinsky–Roetteler–Roland | arXiv:1103.3017 | Y | Y | "minimum influence" is the paper's own phrase — exact |
| 66 | (no authors given) | DOI 10.22331/q-2025-12-02-1926 | Y | Y | Amy & Stinchcombe, Quantum 2025; **memo gives no authors** (O21) |

Summary: **66/66 resolve; 0 fabricated; 3 attributions wrong (refs 2, 25, 40); 6 partial (12, 15, 20, 28, 29, 30, 58 → 7); 2 uncited (8, 24); 2 with wrong or missing author data (35, 66).** `[UNVERIFIED]` marks left by the memo: none — and the memo's one bibliographic correction (ref 17 vs ref 12) is itself correct.

---

## 2. Objections

### O1 — MAJOR. The Ding et al. condition-number bound is misstated (and the decisive bound is missing).

**Location:** §1 "Quantum resource bound as literally stated in the source"; row `C-NEW-QP-MACAULAY-HHL-UNIFORM`; ranked table row 4.

**Memo:** "For a unique Boolean solution of Hamming weight h, Ding et al. prove a condition-number lower bound of order κ = Ω(√(C(n,h))) for the relevant truncated QLS condition number."

**Source (arXiv:2111.00405v2, Theorem 4.5, verified from the PDF):** under the hypothesis that all t solutions have the same Hamming weight h, or that the minimum-ℓ₂ solution lies in the convex hull of the solution vectors,

- using max degree: κ_b(M) ≥ √(((d+1)^h − 1)/t);
- using total degree: κ_b(M) ≥ √((C(d+h,h) − 1)/t);
- "in particular in the setup in [CG21], using max degree d = 3n, we have κ_b(M) ≥ √((3n)^h/t)".

The paper's introduction states this as "the lower bound changes from (3n)^{h/2} to 2^{h/2} on our refined algorithm". The quantity √(C(n,h)) that the memo attributes to the condition number is, in the same paper, the cost of **Grover search over fixed-Hamming-weight assignments** ("we can also use Grover search to find such an assignment with O(√(C(n,h))) evaluations"). The memo has swapped the quantum competitor's cost for the obstruction it competes with.

The memo also never states Ω(2^{h/2}), which is the bound that actually governs the regime the memo calls open ("useful when the Hamming weight is logarithmic"): at h = Θ(log n), (3n)^{h/2} is quasipolynomial while 2^{h/2} is polynomial — that contrast is the entire content of the paper's §4.3, and the memo's §1 loses it.

**FIX DEMAND:** replace √(C(n,h)) by √(((d+1)^h − 1)/t) (max degree) / √((C(d+h,h) − 1)/t) (total degree), state the Chen–Gao specialisation (3n)^{h/2}, state the improved-algorithm bound Ω(2^{h/2}), and carry Theorem 4.5's two alternative hypotheses.

**SURVIVING STATEMENT:** Ding et al. prove an exponential-in-h lower bound on the truncated QLS condition number of the Chen–Gao Macaulay system, so that Grover-type fixed-weight search matches or beats the HHL route whenever d + h ≥ n, and definitely at d = 3n; K-QP1 and the 2/5 score survive unchanged.

---

### O2 — MAJOR. A classical resource bound is attributed to Kedlaya's paper, which does not contain it.

**Location:** §2 "Best classical baseline"; ranked table row 1.

**Memo:** "Kedlaya records a bound of the form (log q)^{O(g² log g)} for the general classical approach then known."

**Source (arXiv:math/0411623v3, p. 1, verified from the PDF):** "For g fixed, the approach introduced by Schoof (compute P(t) modulo many small primes) gives an algorithm which is polynomial in log(q) but **exponential in g**, as shown by Pila and Adleman–Huang." No exponent of the form (log q)^{O(g² log g)} appears anywhere in the paper. (The bound is real and is normally attributed to Adleman–Huang; it is not Kedlaya's.)

**FIX DEMAND:** replace with Kedlaya's own wording ("polynomial in log q, exponential in g; Schoof–Pila–Adleman–Huang"), or cite Adleman–Huang directly with a resolved identifier for the (log q)^{O(g² log g)} figure.

**SURVIVING STATEMENT:** No single classical algorithm polynomial in both g and log q is known; Kedlaya's quantum algorithm is therefore a genuine superpolynomial advantage in the joint parameters, which is what K-QP2 and the rank-1 placement rest on.

---

### O3 — MINOR. Reference 40 has the wrong authors.

**Location:** §7 "Best classical baseline"; reference list entry 40.

DOI 10.1137/S0097539794278384 is **Dyer, Gritzmann and Hufnagel**, "On the complexity of computing mixed volumes", SIAM J. Comput. 27 (1998) 356–400 (Crossref, verified). The memo prints "P. Gritzmann and V. Klee". The #P-hardness content attributed to it is correct.

**FIX DEMAND:** correct the author list to Dyer–Gritzmann–Hufnagel before this entry reaches `refs/`.

**SURVIVING STATEMENT:** exact mixed-volume computation is #P-hard, including on families derived from permanent instances.

---

### O4 — MAJOR. The decision rule does not generate the scores it reports (lockstep failure).

**Location:** "Decision rule"; §2, §3, §6 "Score and killer"; ranked table.

The rule awards one point per PRD §2 criterion, and criteria 1–5 are: precise problem; quantum bound beating classical; survives hidden costs; survives dequantization; cheap hardware hook. Apply it to the memo's own §2 text: Kedlaya has (1) a precise problem with input encoding, (2) a proved superpolynomial advantage, (3) an exact output of polynomial size with the hidden costs enumerated and none fatal, (4) "Tang-style low-rank dequantization is not relevant", and fails only (5). That is **4/5 by the memo's own rubric**, not 3. The same arithmetic gives hidden nonlinear structures 4/5. The memo instead asserts "No primitive scores 4 or 5 in this round" and enforces it through K-QP2's clause "it is established prior art" and K-QP3's oracle clause — neither of which is one of the five criteria.

Conversely, primitive 6 is scored 3/5 while the memo itself writes "This formula is a direct composition of amplitude amplification with a path oracle; it is not an existing end-to-end homotopy theorem. No verified source was found giving a quantum continuation algorithm with a proved improvement in C_track." With no theorem, criterion 2 is unmet and criterion 3 is explicitly unmet, so the rubric yields at most 2.

**FIX DEMAND:** either add novelty-to-this-campaign and input-model-fidelity as explicit, numbered rubric criteria and rescore all 14 rows against the amended rubric, or keep the five criteria and report 4 for Kedlaya, 3–4 for hidden nonlinear structures, and 2 for amplitude amplification over paths, moving the novelty and oracle observations into the killer column where they already sit.

**SURVIVING STATEMENT:** the ordinal ranking of primitives 1–3 above primitives 4–11 is defensible; only the cardinal scores and the "no primitive scores 4 or 5" headline are unsupported.

---

### O5 — MAJOR. The SUSY answer to the brief's obligation 2(d) is incomplete, and the Witten-index row is wrong in the case that matters.

**Location:** §4 "Dequantization and hidden costs"; row `C-NEW-QP-WITTEN-INDEX-COUNT`.

The brief asks specifically whether the ground-state count of {Q, Q†} for an isolated singularity is the Milnor number and under what conditions. The memo answers with a correct algebraic caveat (chiral-ring cohomology ≠ Witten Laplacian ≠ finite-degree seed model) but then kills the route with "A Witten index is an alternating signed count. It can vanish through cancellation even when there are many ground states. It does not recover individual Betti or Hodge numbers."

That is exactly false in the Landau–Ginzburg case the section is about. For a superpotential W with isolated non-degenerate critical points, all vacua of the LG model sit in a single fermion-number sector, so Tr(−1)^F = ±μ = ±dim Jac(W): the index **does** determine the Milnor number there. The general Morse/de Rham statement (cancellation between sectors) is the one the memo has in hand, and it does not apply to the LG model.

Row `C-NEW-QP-WITTEN-INDEX-COUNT` inherits this: "The claim that the Witten index determines every individual Betti number, Hodge number, or Milnor number is false, because it is an alternating supertrace and distinct graded degeneracy vectors can have the same index." The scope of the negation is ambiguous (L1 requires exact quantifiers), the "distinct graded degeneracy vectors" assertion is existential with no witness supplied (L3 requires a leaf citing a definition, a claim id, or a checker run), and under the reading "for every model" the row is refuted by the isolated-singularity LG case.

**FIX DEMAND:** restate as "There exist SUSY Hamiltonians (e.g. the Witten deformed de Rham complex on a compact manifold with b₀ = b₁ = 1) whose Witten index does not determine the individual Betti numbers", supply the explicit witness, and add the complementary positive sentence: for an isolated non-degenerate critical locus the LG index equals ±μ, so the SUSY route to Milnor numbers is killed by readout, gap and the closed-form smooth baseline, **not** by index cancellation.

**SURVIVING STATEMENT:** K-QP4 survives on its first clause alone. I independently recomputed the closed form: for Fermat W and (n,d) = (2,3), (2,4), (3,3) the Hilbert function of R/J_W is exactly the coefficient sequence of (1−t^{d−1})^{n+1}/(1−t)^{n+1}, with total (d−1)^{n+1} = 8, 27, 16. For smooth hypersurfaces the Hodge numbers are graded pieces of that closed form and there is no computational content; the content is in singular hypersurfaces, where no quantum resource theorem exists.

---

### O6 — MAJOR. The TDA-on-real-varieties row's `where-proved` does not compose.

**Location:** row `C-NEW-QP-TDA-REAL-VARIETY`; §5 "Problem P".

The row is CONJECTURE with "where-proved: composition of DOI 10.1007/s00454-006-1250-7 with arXiv:2209.13581". Niyogi–Smale–Weinberger recovers the homology of a positive-reach **submanifold** from a **union of balls / Čech** complex at one radius, with high probability. Berry et al. and LGZ compute Betti numbers of a **Vietoris–Rips clique** complex of the sample graph. The two are not the same complex; the bridge is a VR–Čech interleaving argument (Chazal–Oudot type) plus a persistence-interval statement, and the memo supplies neither. Additionally a `where-proved` that asserts a completed composition contradicts the row's own CONJECTURE status.

Secondary indexing defect: the memo's Problem P outputs β_k/|Cl_{k+1}|, the Berry formula it quotes is for β_{k−1} and |Cl_k|, and the Schmidhuber factor it quotes is √(C(s,k+1)/β_k). Three conventions in one section.

**FIX DEMAND:** insert the VR–Čech interleaving step with a resolved identifier, or restrict the row to the Čech/union-of-balls filtration and say so; set `where-proved: none (composition proposed)`; fix the k-index to one convention.

**SURVIVING STATEMENT:** given a sufficiently dense sample and a reach lower bound, the Berry et al. resource bound applies to the clique complex of that sample; whether the resulting number is a Betti number of V_ℝ needs the interleaving step.

---

### O7 — MAJOR. Two published TDA results that change the score are omitted.

**Location:** §5; ranked table row 5; row `C-NEW-QP-TDA-GENERIC-EXPONENTIAL`.

(a) The memo cites Schmidhuber–Lloyd for the negative half of their abstract but silently drops the positive half: "we argue that an exponential quantum advantage can be recovered if the input data is given as a **specification of simplices** rather than as a list of vertices and edges" (arXiv:2209.14286, verified). That is precisely an input-model change of the kind PRD §2(3) makes part of the statement, and it is the one regime in which quantum TDA is not Grover-limited.

(b) Gyurik, Cade and Dunjko, "Towards quantum advantage via topological data analysis", Quantum 6, 855 (2022), **DOI 10.22331/q-2022-11-10-855**, arXiv:2005.02607 — verified — gives the complementary hardness anchor (normalized Betti-number estimation is DQC1-hard / BQP-hard in the relevant regimes). The campaign already runs a DQC1-style estimator in C-061, so this bears directly on Arm A as well as on primitive 5.

**FIX DEMAND:** add both, state the simplices-input regime as a named exception in K-QP5, and re-examine the 2/5 score in light of (b).

**SURVIVING STATEMENT:** in the vertex-and-edge input model, on asymptotically almost all inputs, LGZ gives at most a quadratic advantage; K-QP5 holds in that model only.

---

### O8 — MAJOR. Hallgren's principal-ideal and unit-group algorithms are omitted, although the lane brief named them and the north star names ideals.

**Location:** §2; §10; ranked table (absent).

The memo's §2 covers "class groups" only through Kedlaya's use of them as a subroutine, and never cites Hallgren. Verified identifiers:

- S. Hallgren, "Polynomial-time quantum algorithms for Pell's equation and the principal ideal problem", **DOI 10.1145/1206035.1206039** (J. ACM 54(1), 2007; STOC version DOI 10.1145/509998.510001);
- K. Eisenträger, S. Hallgren, A. Kitaev, F. Song, "A quantum algorithm for computing the unit group of an arbitrary degree number field", **DOI 10.1145/2591796.2591860** (STOC 2014).

These are exponential quantum speedups whose *input is an ideal* (the principal ideal problem asks whether a given ideal of a number ring is principal, and to produce a generator) with no known classical subexponential algorithm. Under CLAUDE.md §1 ("the problem comes from algebraic geometry (varieties, ideals)") this is at least as close a benchmark as Kedlaya's, and the memo's headline sentence "The strongest existing quantum speedup is Kedlaya's curve-zeta algorithm" is not established without it. Two further omissions, smaller: Childs–van Dam–Hung–Shparlinski, "Optimal quantum algorithm for polynomial interpolation", arXiv:1509.09271 (d/2+1/2 quantum queries versus d+1 classical for recovering a degree-d polynomial over GF(q)) — directly in primitive 3's neighbourhood; and the Childs–van Dam survey arXiv:0812.0380 as the standard map of this territory.

**FIX DEMAND:** add a primitive section (or a subsection of §2) on Hallgren-type unit-group/principal-ideal algorithms with its own score and killer; add the interpolation and survey references; withdraw or defend the "strongest existing" superlative.

**SURVIVING STATEMENT:** among the primitives the memo *did* survey, Kedlaya's is the strongest existing algebraic-geometric quantum speedup.

---

### O9 — MAJOR. Combination 1 is not disjoint from Arm E, and its novelty claim is false.

**Location:** "Combinations" §1; "Questions for TJO" Q5.

Q5 asks whether to open the toric-fibre quantum-walk probe "given that it is the only untried combination with both a canonical ideal-derived graph and a Bose–Hubbard hook". `scouting/real-variety.md` Route 7 ("toric and binomial ideals with positive real points") already does exactly this analysis — it invokes D-toric-ideal, decomposes H_N into fibre graph Laplacians, observes that "for a binomial z^u − z^v ... each fibre block is stoquastic", and closes with "**2/5 for speedup; 4/5 for hardware.** Positivity is physically natural but algorithmically collapses toward stoquastic Markov-chain structure." Row C-262 (C-NEW-RV-TORIC-POSITIVITY) is already in the DAG. PRD §4 Arm E lists this as one of its five ranked routes.

**FIX DEMAND:** cite Route 7 and C-262, state the delta (quantum-walk mixing on the fibre chain, which Route 7 did not analyse), and rewrite Q5 to ask whether the delta justifies a probe on top of an already-scored 2/5 route.

**SURVIVING STATEMENT:** the quantum-walk-on-fibre-graph angle is new relative to Route 7; the toric fibre Hamiltonian, its Bose–Hubbard hook and its stoquastic collapse are not.

---

### O10 — MAJOR. Combination 1's success criterion cannot be met by its own mechanism.

**Location:** "Combinations" §1, success criterion.

The probe "succeeds only if it identifies an observable estimable in poly(n) quantum time while the best classical chain requires superpolynomial mixing." The only quantum ingredient the combination supplies is quantum-walk speedup of a reversible chain, which the memo itself scores in K-QP10B as "quadratically improve mixing-gap dependence". A quadratic improvement maps classical time 1/δ to quantum 1/√δ; if the classical chain requires superpolynomial time, δ is superpolynomially small and 1/√δ is still superpolynomial. The stated success condition is therefore unreachable by construction, and the probe is guaranteed to return the memo's "likely negative outcome" regardless of what the numerics show. A one-week probe whose success condition is provably unsatisfiable is not a well-defined probe.

**FIX DEMAND:** replace the success condition with one the mechanism can meet — e.g. "identify a family of A_n with fibre-chain gap δ_n = n^{−Θ(1)} classically but with a *ground-energy* route through QSVT under a normalized-gap promise that beats implicit Lanczos on the same fibre block by a stated exponent" — or state the falsifier as a polynomial-exponent, not a superpolynomial, separation.

**SURVIVING STATEMENT:** the measurable quantities the probe lists (exact seed block, normalized gap, Metropolis gap, conductance, observable variance on fibres of size ≤ 10⁶) are well defined and would be informative; only the pass/fail rule is broken.

---

### O11 — MAJOR. Six proposed rows carry a `where-tested` field that names no checker (L4).

**Location:** rows `C-NEW-QP-ID-KEDLAYA`, `C-NEW-QP-MACAULAY-CONDITION-EQUALITY`, `C-NEW-QP-SUSY-HODGE-SPEEDUP`, `C-NEW-QP-ANNEALING-DEMONSTRATION`, `C-NEW-QP-QPCA-SECANT`, `C-NEW-QP-VOLUME-EHRHART`.

Their `where-tested` values are "arXiv title and author records", "dimension and kernel comparison", "Fermat-family computations in `scouting/applications-wide-net.md`", "reported device instances", "rank-two tensors with identical flattening ranks but different CP ranks", "translated thin-polytopes examples". None of these is a run of a checker under `checkers/` with a nonzero exit on violation and a recorded mutation in `checkers/MUTATIONS.md`. Two of them ("rank-two tensors...", "translated thin-polytopes...") describe tests that were not performed at all. Under L4, "runs without errors" is never a test, and under L1 `where-tested` is a field the ratchet is read off. `C-NEW-QP-BKK-PERMANENT` is the only row that gets this right ("proposed n ≤ 8 symbolic checker").

**FIX DEMAND:** set `where-tested: none` on all six, and move the intended tests into named proposed checkers (a bibliographic-resolution checker is not one; that belongs in `refs/`).

**SURVIVING STATEMENT:** the underlying facts are unaffected; only the ratchet metadata is wrong. I did in fact verify the `SUSY-HODGE-SPEEDUP` Hilbert series and the `BKK-PERMANENT` identity numerically (see O5 and O15), so those two can be re-tested cheaply.

---

### O12 — MINOR. Griffiths reference: title and DOI disagree.

**Location:** §4 "Best classical baseline"; reference 25.

DOI 10.2307/1970746 = "On the Periods of Certain Rational Integrals: **I**", Ann. of Math. 90 (1969) 460; Part II is DOI 10.2307/1970747, p. 496 (both verified via Crossref). The memo's entry reads "II" with the Part I DOI. `scouting/applications-wide-net.md` uses the same DOI without a part number, so the mismatch originates here.

**FIX DEMAND:** cite both parts, or make title and DOI agree.

**SURVIVING STATEMENT:** the primitive-Hodge / graded-Jacobian-ring identification is Griffiths', Ann. of Math. 90 (1969).

---

### O13 — MINOR. The zeta output size is understated by a factor g.

**Location:** §2 "Quantum resource bound as literally stated in the source".

Memo: "The output has only O(g log q) bits". P_C(T) has 2g+1 integer coefficients a_j with |a_j| ≤ C(2g,j) q^{j/2}, so each needs O(g + g log q) = O(g log q) bits and the whole polynomial needs **O(g² log q)** bits.

**FIX DEMAND:** O(g² log q).

**SURVIVING STATEMENT:** the output is of size polynomial in g and log q, so the exponential-output objection does not apply.

---

### O14 — MINOR. Two transcription defects in the TDA resource bounds.

**Location:** §5 "Quantum resource bound"; §5 "Best classical baseline".

(a) Berry et al. Lemma 1, eq. (12) (verified from the PDF) reads `(6|E| + n log₂ n)` — n times the base-2 logarithm of n. The memo writes `(6|E| + s\log^2 s)`, i.e. log squared. Every other factor of eq. (12) — ln(1/δ₂)/r₂, √(|Cl_k|/β_{k−1}), (π/2)√(C(n,k)/|Cl_k|), (n/λ_min) ln(4|Cl_k|/(r₃β_{k−1})), (6|E| + 5n), and the eq. (13) Dicke variant with n^k/k! and (6|E| + 2kn) — matches exactly.

(b) Apers et al. state the clique-complex bound as (n/λ_max)^{O(γ^{−1/2} log(1/ε))} with λ_max ≥ k. The memo appends a `poly(s)` factor that is not in the source.

**FIX DEMAND:** `s log₂ s`; delete the spurious `poly(s)`.

**SURVIVING STATEMENT:** the structure of both bounds, and the "matches quantum asymptotics when γ ∈ Ω(1) and k ∈ Ω(s)" conclusion, are correct as stated.

---

### O15 — MINOR. `C-NEW-QP-BKK-PERMANENT` is misnamed and cites the wrong definition.

**Location:** row `C-NEW-QP-BKK-PERMANENT`; §7 "Problem P".

The statement is about the **multihomogeneous Bézout** coefficient, not the BKK/mixed-volume count — the memo's own §7 draws that distinction two sentences earlier ("The general sparse analogue is the BKK mixed volume"). Its sole `depends-on` is D-optical-counting-access, which defines optical outcome probabilities and none of the symbols A, t_j, per(A) appearing in the statement; the memo proposes no definition for the multihomogeneous Bézout number.

I verified the identity independently (sympy, n = 3, 4, 5, three random nonnegative integer matrices each): the coefficient of t₁···t_n in ∏_i(Σ_j A_ij t_j) equals per(A) in all 9 cases.

**FIX DEMAND:** rename to `C-NEW-QP-MHOM-BEZOUT-PERMANENT`; add a proposed definition D-multihomogeneous-bezout and make it the `depends-on`; drop D-optical-counting-access from this row (it belongs to `C-NEW-QP-BOSON-COUNT`).

**SURVIVING STATEMENT:** the identity itself, verified.

---

### O16 — MINOR. `C-NEW-QP-FINITE-FIELD-SEED` restates a definition.

**Location:** row `C-NEW-QP-FINITE-FIELD-SEED`.

D-finite-field-analogue already reads: "That register needs dim R_N log q qubits", and its Pitfalls already say the compact complex amplitude encoding does not transport. The row asserts the same thing with an Ω(·), and its inference ("therefore does not inherit the seed's O(n log N)-qubit compression") is a non sequitur as stated: it rules out one encoding, not all of them. Under L2 an artifact cites definitions and does not restate them.

**FIX DEMAND:** drop the row and cite D-finite-field-analogue, or replace it with the non-trivial statement (no succinct encoding of F_q^{dim R_N} supporting F_q-linear Macaulay operations in poly(n) qubits) and mark it CONJECTURE with no proof claimed.

**SURVIVING STATEMENT:** D-finite-field-analogue, unchanged; the memo's PRD §7 Q7 recommendation ("fund finite-field work only if it identifies a compact geometric group or cohomological object analogous to a Jacobian") is a good, new, and correctly derived conclusion and should be kept.

---

### O17 — MINOR. `C-NEW-QP-GIBBS-QUADRATIC` cites a theorem with different hypotheses.

**Location:** row `C-NEW-QP-GIBBS-QUADRATIC`; §10B.

arXiv:0811.0596 (verified abstract) proves a quadratic speed-up of an **FPRAS for partition functions** combining simulated annealing with MCMC under **non-adaptive cooling schedules**, with the two quadratic reductions (spectral gap and accuracy) "intimately related and cannot be achieved separately". The row's hypotheses are instead "efficiently implementable coherent transition oracle, and warm-start overlap bounded below by 1/poly(n)", which is the Szegedy-walk / warm-start state-preparation statement, not Wocjan et al.'s.

**FIX DEMAND:** either restate the row as Wocjan et al.'s annealing theorem (with the cooling schedule), or keep the warm-start form and cite the Szegedy/Magniez–Nayak–Roland–Santha line with a resolved identifier.

**SURVIVING STATEMENT:** quantum walks give at most a quadratic improvement in the mixing-gap and accuracy dependence; K-QP10B holds.

---

### O18 — MINOR. `C-NEW-QP-ID-KEDLAYA` is not a claim about the mathematics.

**Location:** row `C-NEW-QP-ID-KEDLAYA`.

The row's content is a bibliographic correction, its status is REFUTED, and the statement it refutes ("Kedlaya's algorithm is arXiv:quant-ph/0608151") appears nowhere in the campaign's artifacts — it appears only in `briefs/lane-quantum-primitives.md`, and a brief is not evidence and is not in the DAG. Putting citation hygiene in the claims ratchet dilutes it.

**FIX DEMAND:** record the correction in `refs/` and in `docs/worklog/2026-09-02.md`, and correct the brief; do not create a claim row. (The correction itself is right and valuable: I confirmed quant-ph/0608151 = Wang–Fei–Wu, "Separability and Entanglement of Identical Bosonic Systems", J. Phys. A 39 (2006), DOI 10.1088/0305-4470/39/36/L01.)

**SURVIVING STATEMENT:** the correct identifiers for Kedlaya's algorithm are arXiv:math/0411623 and DOI 10.1007/s00037-006-0204-7.

---

### O19 — MINOR. `C-NEW-QP-ZETA-CURVE` assumes what Kedlaya constructs.

**Location:** row `C-NEW-QP-ZETA-CURVE`.

The row's hypotheses include "polynomial-time unique-encoding Jacobian arithmetic". Kedlaya does not assume this; §6 ("Computing in class groups") and §7 ("Finding generators of class groups") build the unique-encoding black-box presentation from the plane model plus explicit desingularization data, with Lemma 10 supplying provably random generators and Proposition 11 (for e with 16g < q^{e/2}) computing #Cl(C_e) in time polynomial in g, log q, e. Assuming the black box as an input promise makes the row strictly weaker than Theorem 1 and reads as circular.

**FIX DEMAND:** drop the Jacobian-arithmetic hypothesis; keep the plane-model and desingularization-data hypotheses, which are Kedlaya's actual input protocol.

**SURVIVING STATEMENT:** Kedlaya's Theorem 1 — a bounded-error quantum algorithm computing P_C(T) in time polynomial in g and log q — with the paper's own input protocol.

---

### O20 — MINOR. Imported published theorems enter as CONJECTURE, against the DAG's existing convention.

**Location:** rows `C-NEW-QP-ZETA-CURVE`, `C-NEW-QP-HIDDEN-POLYNOMIAL`, `C-NEW-QP-GIBBS-QUADRATIC`.

The DAG's convention for a cited published theorem is SKETCH with "where-proved: ... (cited theorem)" — see C-092 (Dickenstein–Tobis) and C-099 (Anschuetz et al.), both SKETCH. The memo's imported theorems are CONJECTURE. The memo complied with its brief here, so this is a merge instruction, not a lane fault; but the DAG must not end up with two conventions for the same object.

**FIX DEMAND:** on merge, put imported published theorems at SKETCH with "(cited theorem)" and record the convention once in `claims/CLAIMS.md`'s legend; or downgrade C-092/C-099 to CONJECTURE. Pick one.

**SURVIVING STATEMENT:** neither status is above SKETCH, so L1's ratchet is not violated either way.

---

### O21 — MINOR. Four reference-list hygiene defects.

Reference 35 gives "C.-F. Chien et al."; the author is Chiang-Heng Chien. Reference 66 has a bare title and no authors; it is M. Amy and L. Stinchcombe, Quantum 9, 1926 (2025). References 8 (Tang, arXiv:1807.04271) and 24 (Vafa–Warner, DOI 10.1016/0370-2693(89)90473-5) appear in the list but are cited nowhere in the body — and Tang is one of the three dequantization anchors PRD §2(4) names by name, so its absence from §1's dequantization paragraph is a small substantive gap as well.

**FIX DEMAND:** fix 35 and 66; either cite 8 and 24 in the body or delete them; add Tang to the §1 dequantization discussion.

**SURVIVING STATEMENT:** all four references exist and resolve.

---

### O22 — NOTE. Checked, holds: frustration-free Bose–Hubbard.

§8 says "Frustration-free Bose–Hubbard ground energy is QMA-hard in a different, lattice-local input model". I downloaded arXiv:1311.3297v1 and confirmed the paper explicitly defines a special case "called Frustration-Free Bose Hubbard Hamiltonian" and proves it QMA-hard, then reduces it to an XY-model eigenvalue problem. The memo is right. One correction: the model is defined on an **arbitrary graph**, not a lattice; "lattice-local" should read "graph-local, at fixed particle number".

---

### O23 — NOTE. C-099's `[UNVERIFIED]` mark can be lifted.

C-099 carries "Citation not resolved to an arXiv id or DOI here [UNVERIFIED]". The memo's §8 resolves it to Anschuetz–Bauer–Kiani–Lloyd, arXiv:2211.16998, DOI 10.22331/q-2023-11-28-1189, and I verified both, plus the abstract wording: "classical algorithms that calculate ground states and time-evolved expectation values for permutation-invariant Hamiltonians specified in the symmetrized Pauli basis with runtimes polynomial in the system size". The memo's paraphrase ("specified in the appropriate symmetrized basis") is faithful. This is a real by-product of the lane and should be merged into C-099 and D-hardness-anchors regardless of what happens to the memo's own rows. It bears on PRD §4 Arm X and D9.

---

### O24 — NOTE. C-275…C-280 have no `status:` field.

The memo cites C-276 and C-278 (correctly — §5's "D-real-structure and C-276/C-278 exclude the proposed two-copy filter as a real-point selector" matches those rows' statements). But those six rows in `claims/CLAIMS.md` carry no `- status:` line at all; they were merged with the status folded into a run-on `depends-on / where-proved / where-tested` line. The obligation-3 check "no reliance on REFUTED rows" therefore cannot be run mechanically against them. Orchestrator hygiene, outside this lane.

---

### O25 — NOTE. Two uncited or omitted quantitative points.

(a) §7's "classical approximate GBS samplers in high-loss or positive-phase-space regimes" carries no identifier, against rule 6. Suggested: Oh–Liu–Alexeev–Fefferman–Jiang, "Classical algorithm for simulating experimental Gaussian boson sampling", arXiv:2306.03709 (verified).

(b) §10C omits the volume paper's own quantum **lower** bound Ω(√d + 1/ε) membership queries, which "rules out the possibility of exponential quantum speedup in d". That is a free strengthening of K-QP10C and it is the reason I downgrade primitive 10C below the memo's score.

---

**Objection count: 25 total — 0 FATAL; 10 MAJOR (O1, O2, O4, O5, O6, O7, O8, O9, O10, O11); 11 MINOR (O3, O12, O13, O14, O15, O16, O17, O18, O19, O20, O21); 4 NOTE (O22, O23, O24, O25).**

---

## 3. Proposed rows adjudication

| id | disposition | reason / exact rewording |
|---|---|---|
| C-NEW-QP-ID-KEDLAYA | **REJECT** | Bibliographic, not mathematical; refutes a statement that exists only in the lane brief, which is not a campaign artifact (O18). Record in `refs/` and the worklog instead. The correction itself is verified and should be kept there. |
| C-NEW-QP-MACAULAY-HHL-UNIFORM | **ACCEPT WITH REWORDING** | Bound is wrong (O1). Reword: "For every Boolean system F with n variables whose solutions all have minimum Hamming weight h, and for the degree-d Macaulay linear system of Chen–Gao with t solutions, if all t solutions have equal Hamming weight or the minimum-ℓ₂ solution lies in the convex hull of the t solution vectors, then the truncated QLS condition number satisfies κ_b(M) ≥ √(((d+1)^h − 1)/t) at max degree and κ_b(M) ≥ √((C(d+h,h) − 1)/t) at total degree; in particular κ_b(M) ≥ √((3n)^h/t) at Chen–Gao's d = 3n, and Ω(2^{h/2}) for the reduced Boolean Macaulay system. Hence the original construction is no faster than fixed-weight Grover search, which costs O(√C(n,h)) evaluations, whenever d + h ≥ n." Add: "sharpens C-097." |
| C-NEW-QP-MACAULAY-CONDITION-EQUALITY | **ACCEPT WITH REWORDING** | Duplicates C-097's fixed wording and referee round1 #64 / C-246. Reword to "no reduction is known **and** the two quantities are not equal in general: for the seed's Φ_N the governing quantity α_BE/Δ_N is a spectral gap ratio of a PSD operator with nontrivial kernel, whereas κ_b(M) is a right-hand-side-dependent truncated condition number of a non-square inhomogeneous system with a different domain, so no instance-wise identity holds"; and cite one explicit instance. `depends-on` must add C-246. |
| C-NEW-QP-ZETA-CURVE | **ACCEPT WITH REWORDING** | Drop the assumed "polynomial-time unique-encoding Jacobian arithmetic" hypothesis (O19); it is constructed in §§6–7. Keep the plane-model-of-degree-poly(g) and explicit-desingularization-data hypotheses. On merge, status SKETCH per O20. |
| C-NEW-QP-ZETA-HYPERSURFACE | **ACCEPT AS REFUTED** | Supported: Kedlaya §10, Question 12 and the following paragraph ("there is no 'geometric' realization of the higher étale cohomology groups analogous to the realization of the first étale cohomology group in the Tate module of the Jacobian"), verified from the PDF. `where-proved: arXiv:math/0411623 §10` is correct. |
| C-NEW-QP-FINITE-FIELD-SEED | **REJECT** | Restates D-finite-field-analogue (O16). If retained, must be the non-trivial version, which is unproved. |
| C-NEW-QP-HIDDEN-POLYNOMIAL | **ACCEPT AS CONJECTURE** | Statement matches Decker–Draisma–Wocjan verbatim (fixed variables and degree, all but finitely many field sizes, polylog(q) quantum time and constant success, Ω(√q) classical queries). On merge, status SKETCH per O20. |
| C-NEW-QP-HIDDEN-EXPLICIT-TRANSFER | **ACCEPT WITH REWORDING** | "is false, because constructing the required oracle is not furnished by sparse coefficient access" asserts a non-existence that is not proved. Reword on the C-097 pattern: "**No reduction is known** from sparse coefficient access over F_q to the obfuscated coherent fiber oracle of D-hidden-polynomial-structure, and the natural constructions require enumerating or solving the fibers; hence no efficient algorithm for explicitly presented sparse systems over F_q follows from the hidden-polynomial results." Status CONJECTURE, not REFUTED. |
| C-NEW-QP-SUSY-HODGE-SPEEDUP | **ACCEPT AS REFUTED** | Content verified independently (Hilbert series and totals for (n,d) = (2,3), (2,4), (3,3)). Two fixes: credit `scouting/applications-wide-net.md` F2 as the origin of both the closed form and the exp(−0.249n)…exp(−0.299n) fits (the memo's "e^{−0.25n} to e^{−0.30n}" is faithful); set `where-tested: none` pending a checker (O11). |
| C-NEW-QP-WITTEN-INDEX-COUNT | **ACCEPT WITH REWORDING** | O5. Reword: "There exist supersymmetric models — e.g. Witten's deformed de Rham complex on a compact manifold with b₀ = b₁ — in which the Witten index Tr(−1)^F does not determine the individual Betti numbers, since it is an alternating supertrace. This does **not** apply to the Landau–Ginzburg model with isolated non-degenerate critical locus, where all vacua lie in one fermion-number sector and Tr(−1)^F = ±μ = ±dim Jac(W)." Supply the witness in `where-proved`. |
| C-NEW-QP-TDA-REAL-VARIETY | **HOLD** | Missing step: VR–Čech interleaving between Niyogi–Smale–Weinberger and the clique-complex algorithms (O6). Also fix the k-index convention and set `where-proved: none (composition proposed)`. |
| C-NEW-QP-TDA-GENERIC-EXPONENTIAL | **ACCEPT AS REFUTED** | Supported by arXiv:2209.14286. Two wording fixes: use the source's own hardness statement ("approximating Betti numbers up to multiplicative error is NP-hard") rather than "deciding nonzero is NP-hard", and add the source's exception clause ("in the vertex-and-edge input model; an exponential advantage may be recoverable when the input is a specification of simplices") — O7. |
| C-NEW-QP-PATH-AA | **ACCEPT WITH REWORDING** | The error budget "total error O(1/√(D/r))" is ambiguous between per-call and cumulative. Reword to "if the coherent path oracle and predicate can be computed and uncomputed with **per-invocation** error o(√(r/D))". Otherwise correct as a conditional composition. |
| C-NEW-QP-PATH-INTERNAL-SPEEDUP | **ACCEPT AS REFUTED** | Correct as a query-composition statement, if uncontroversial. Keep. |
| C-NEW-QP-BKK-PERMANENT | **ACCEPT WITH REWORDING** | Rename `C-NEW-QP-MHOM-BEZOUT-PERMANENT`; the object is the multihomogeneous Bézout coefficient, not the BKK mixed volume; replace `depends-on: D-optical-counting-access` with a new D-multihomogeneous-bezout (O15). Identity itself verified numerically for n = 3, 4, 5. |
| C-NEW-QP-BOSON-COUNT | **ACCEPT AS REFUTED** | Bernoulli sample-complexity argument is correct; "the unitary embedding can make p exponentially small" is an existential and is fine as written. |
| C-NEW-QP-ANALOGUE-DEGENERACY | **ACCEPT WITH REWORDING** | As written it refutes a claim no one makes ("one ground-state energy measurement determines HF"). Reword to the substantive version: "No protocol consisting of ground-state energy measurements alone determines dim ker H_N; a degeneracy readout additionally requires temperature below the spectral gap, calibrated partition function or entropy, control of excited-state contamination, and Ω(1/ε²) shots to resolve HF/M_N to additive ε (D-analogue-degeneracy-readout)." |
| C-NEW-QP-FIXED-MODE-HARDWARE | **ACCEPT WITH REWORDING** | Add the input-model quantifier explicitly: "…with N given in unary (D-input-model), C(N+n,n) = poly(N) is polynomial in the input length, so…". Mark as a restatement of C-057 + C-099 rather than a new fact; `depends-on` already cites both. |
| C-NEW-QP-ANNEALING-DEMONSTRATION | **ACCEPT AS REFUTED** | Every device number in the memo's §9 was checked against arXiv:2111.13224 and is exact. Set `where-tested: none` (O11). |
| C-NEW-QP-GROEBNER-ANNEALER | **ACCEPT AS REFUTED** | Verified: the paper's own abstract says the Gröbner-basis step is the classical half of a hybrid algorithm, and the demonstrated range is "all bi-primes up to just over 200 000". |
| C-NEW-QP-QPCA-SECANT | **ACCEPT AS REFUTED** | Output-type argument is sound. Set `where-tested: none` and move the rank-two witness into a proposed checker (O11). |
| C-NEW-QP-GIBBS-QUADRATIC | **ACCEPT WITH REWORDING** | Cite the theorem whose hypotheses the row actually uses (O17), or restate Wocjan et al.'s annealing/FPRAS theorem with its cooling schedule. |
| C-NEW-QP-VOLUME-EHRHART | **ACCEPT AS REFUTED** | Correct. Strengthen by adding the source's own Ω(√d + 1/ε) quantum query lower bound (O25b). Set `where-tested: none` (O11). |

**Counts: ACCEPT AS CONJECTURE 1; ACCEPT AS REFUTED 8; ACCEPT WITH REWORDING 11; REJECT 2 (C-NEW-QP-ID-KEDLAYA, C-NEW-QP-FINITE-FIELD-SEED); HOLD 1 (C-NEW-QP-TDA-REAL-VARIETY). Total 23.** No row is accepted above CONJECTURE/REFUTED; no row depends on a REFUTED C-row; every D-id and C-id cited by the memo exists in the repo (the 12 "missing" D-ids are exactly the 12 the memo proposes) except that C-275…C-280 carry no status field (O24).

---

## 4. Proposed definitions adjudication

| id | disposition | reason |
|---|---|---|
| D-boolean-macaulay-solve | **ACCEPT** | Correctly distinguishes tQLScn from D-macaulay-gap and the linear-system state from D-projectors. Add the two matrix sizes (m2ⁿ × 2ⁿ reduced; (m+n)(3n+1)ⁿ × (3n+1)ⁿ original), both verified. |
| D-curve-zeta-problem | **ACCEPT** | Input protocol matches Kedlaya §6 exactly. |
| D-hidden-polynomial-structure | **ACCEPT** | Pitfalls line ("stronger than coefficient access, value access, membership, or classical samples") is the load-bearing content and is right. |
| D-jacobian-ring-susy | **REWORD** | Add the LG isolated-singularity fact (index = ±μ, all vacua in one fermion-number sector) so it does not silently license the over-broad C-NEW-QP-WITTEN-INDEX-COUNT (O5). Otherwise sound; the three-way non-identification in Pitfalls is exactly right. |
| D-vr-betti-estimation | **REWORD** | Fix the k-index (β_{k−1} and Cl_k, per Berry Lemma 1) and state whether the filtration is Vietoris–Rips or Čech, since the reconstruction theorem is Čech (O6). |
| D-coherent-path-oracle | **ACCEPT** | The Pitfalls line ("a classical adaptive tracker is not automatically reversible or coherent") is precisely the campaign's cross-cutting trap and is worth having as a definition. |
| D-optical-counting-access | **ACCEPT** | Sound; note it is the correct `depends-on` for C-NEW-QP-BOSON-COUNT and not for the Bézout identity (O15). |
| D-analogue-degeneracy-readout | **ACCEPT** | Sound; this is where the substantive content of C-NEW-QP-ANALOGUE-DEGENERACY belongs. |
| D-boolean-residual-energy | **ACCEPT** | ANF-to-NNF 2ⁿ−1 term count and the quadratization qubit counts verified against arXiv:2111.13224 eqs. (8), (10). |
| D-tensor-secant-problem | **ACCEPT** | The five-way rank distinction in Pitfalls is correct and is what makes K-QP10A bite. |
| D-real-variety-gibbs | **ACCEPT** | Sound; "finite β samples a tube, not the variety" is the right pitfall. |
| D-toric-lattice-counting | **ACCEPT** | Sound. |
| (missing) D-multihomogeneous-bezout | **ADD** | Required by the reworded C-NEW-QP-MHOM-BEZOUT-PERMANENT (O15); no existing definition covers the m-Bézout coefficient. |

---

## 5. Revised ranked table

Scores are mine where they differ from the memo's; the memo's five-criterion rubric is applied as written (see O4).

| rank | primitive | memo | revised | one-line reason |
|---:|---|---:|---:|---|
| 1 | Kedlaya class-group order finding | 3 | **4** | Meets criteria 1–4 by the memo's own §2 text; only the hardware hook is absent. Prior art is a scope fact belonging in the killer, not a rubric deduction. |
| 2 | **Hallgren principal-ideal / unit group (NEW)** | — | **3** | Omitted entirely (O8). Exponential speedup whose input *is an ideal*; prior art; no hardware hook; DOIs 10.1145/1206035.1206039, 10.1145/2591796.2591860. Must be scored before "the strongest existing quantum speedup" is asserted. |
| 3 | hidden nonlinear structures | 3 | **3** | Unchanged, but the deduction must be attributed to input-model fidelity (criterion 1 partial: obfuscated fiber oracle, not an explicit ideal), not to an unstated novelty criterion. |
| 4 | QLSA/QSVT on Macaulay matrices | 2 | **2** | Unchanged; the corrected Ding bound (O1) makes the killer sharper, not weaker. |
| 5 | quantum TDA | 2 | **2** | Unchanged in the vertex-and-edge model, but flag two upside results the memo dropped (O7): the simplices-input regime, and Gyurik–Cade–Dunjko's DQC1/BQP-hardness, which also bears on C-061. |
| 6 | GBS / boson sampling | 2 | **2** | Unchanged; the JSV FPRAS for nonnegative permanents is the right and sharp killer, and degree matrices are nonnegative. Best hardware hook in the memo. |
| 7 | analogue algebraic Hamiltonians | 2 | **2** | Unchanged; K-QP8 is correct and D-analogue-degeneracy-readout is the right instrument. |
| 8 | annealing / QAOA / VQE | 2 | **2** | Unchanged; every device number verified. |
| 9 | amplitude amplification over paths | 3 | **2** | Downgraded (O4): the memo states there is no end-to-end theorem and that C_track is untouched, so criteria 2 and 3 are unmet. Its 15× nominal Watt II margin (6^11 ≈ 3.63e8, √(3.63e8/10) ≈ 6000 versus 92 736 paths — arithmetic verified) is inside the constant factors it must beat. |
| 10 | quantum Gibbs / walks on real varieties | 2 | **2** | Unchanged. |
| 11 | quantum volume estimation | 2 | **1** | Downgraded: the cited paper itself proves Ω(√d + 1/ε) quantum membership queries, ruling out exponential speedup, and the output is a continuous volume, not an Ehrhart or Hilbert quantity — a dictionary/negative entry (O25b). |
| 12 | Shor-type polynomial periods | 2 | **1** | Downgraded: the memo's own K-QP10E says no algebraic-geometry input supplies the coset promise, so what remains is a negative result plus a classical-simulation result (DOI 10.22331/q-2025-12-02-1926). |
| 13 | SUSY / Landau–Ginzburg | 1 | **1** | Unchanged, but the killer must be repaired (O5): the LG Witten index *does* equal ±μ for isolated singularities; the real killers are the closed-form smooth baseline, exponentially small normalized signal, and absence of any resource theorem for singular inputs. |
| 14 | quantum PCA / HOSVD | 1 | **1** | Unchanged. |
| 15 | Jacobian discrete log | 0 | **0** | Unchanged; correctly out of scope. |

Top five for the next funding decision: **(1) Kedlaya — benchmark only, cannot be a campaign novelty; (2) Hallgren unit-group/principal-ideal — must be scored before any "strongest existing" claim; (3) hidden nonlinear structures — real separation, wrong input model; (4) QLSA/QSVT on Macaulay — the closest prior art the campaign must evade, with the corrected Ω((3n)^{h/2}) / Ω(2^{h/2}) bounds; (5) quantum TDA — 2/5 as surveyed, but the simplices-input regime and the DQC1 hardness anchor are the two unexamined upsides.** GBS remains the hardware pick at 2/5.

---

VERDICT: FAIL(O1, O2, O4, O5, O6, O7, O8, O9, O10, O11)
