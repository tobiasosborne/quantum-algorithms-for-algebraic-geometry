<!-- ROLE: adversarial critic verdict, round 2 (adjudication of the repair), on
     scouting/quantum-primitives.md (rk-light L5). Prior: verdicts/quantum-primitives-r1.md.
     UPDATE POLICY: append-only; a round-3 verdict is a new file. -->

# Verdict: scouting/quantum-primitives.md, round 2 (adjudication of repair r1)

- **Target:** `scouting/quantum-primitives.md` at commit `e9ad40b` (2637 lines; parent `2a5f540` is the r0 memo attacked in round 1; `git diff 2a5f540 e9ad40b` = 612 insertions, 205 deletions). 15 ranked rows, 23 proposed claim rows, 14 proposed definitions, 73 references, plus a `# Repair r1 response` disposition table.
- **Date:** 2026-09-03.
- **Critic model:** Claude Opus 5 (1M), adversarial critic seat, round 2.
- **Prior:** `verdicts/quantum-primitives-r1.md` — FAIL(10 MAJOR, 11 MINOR, 4 NOTE; 66/66 references resolved). Under the later-round protocol I treat r1 as settled and attack **changed text only**.
- **Files read this round:** the diff `2a5f540..e9ad40b`; the repaired memo's changed sections in full; `scouting/koszul-betti.md` (Arm B, landed at `68b5a2f`, i.e. **before** this repair); `scouting/classical-landscape.md` §5 trace-estimation baseline (L540–L548); `scouting/real-variety.md` Route 7; `claims/CLAIMS.md` status legend and REFUTED-row convention (C-155, C-181), C-246, C-092/C-099; `definitions/definitions.md` id table.
- **Network fetches this round:** 10 DOIs through Crossref; 1 DOI through DataCite; 1 `doi.org` resolution; 2 arXiv Atom queries (2005.02607 abstract; 2112.03444 v1 and v2 titles); 1 arXiv PDF (`2005.02607v5`, text-extracted, 2317 lines); 2 WebSearch; 1 WebFetch (pure.psu.edu, EHKS abstract). One WebFetch to `authors.library.caltech.edu` returned HTTP 403 and was routed around.
- **Commands run (all `timeout`-bounded, all exit 0):** `git log`/`git diff`/`git status`; `curl` ×5; `pdftotext -layout` ×1; `grep`/`sed`/`awk` ×~25; `python3` ×5 (Crossref/DataCite batch resolution; **numerical re-derivation of the new §1 counterexample**; row status/`where-tested` audit over all 23 rows; definition-id collision audit; reference-citation sweep). No file other than this verdict was created or modified; nothing committed.

Departures from conventions C1–C12: none.

---

## 1. Disposition of O1–O25

Verdict per objection: **VERIFIED** = the claimed disposition holds under fresh recomputation or fetch; **NOT VERIFIED** = something is still wrong; **NEW DEFECT** is recorded separately in §2.

| id | claimed | my check | verdict |
|---|---|---|---|
| O1 | FIXED | Compared §1 against the `2111.00405v2` PDF text I extracted in r1. Theorem 4.5's two formulas √(((d+1)^h−1)/t) and √((C(d+h,h)−1)/t) are reproduced exactly; both alternative hypotheses (equal Hamming weight, or minimum-ℓ₂ solution in the convex hull) are carried; the Chen–Gao specialisation √((3n)^h/t) and the unique-solution reading Ω((3n)^{h/2}) match the paper; Ω(2^{h/2}) for the reduced m2ⁿ×2ⁿ system matches the paper's §1 ("a smaller lower bound Ω(2^{h/2})"); the Grover cost O(√C(n,h)) is now explicitly labelled "not a condition-number bound", and D-boolean-macaulay-solve repeats that pitfall. κ_b(M)=‖M‖‖M⁺b‖/‖b‖ matches the paper's definition. | **VERIFIED** (residue in O34) |
| O2 | FIXED | The `(log q)^{O(g² log g)}` attribution is gone and replaced by Kedlaya's own sentence ("polynomial in log q but exponential in g, as shown by Pila and Adleman–Huang"), plus an explicit line recording that the paper does not state the removed bound. Matches `math/0411623v3` p. 1. | **VERIFIED** |
| O3 | FIXED | Ref 40 and the §7 body now read Dyer–Gritzmann–Hufnagel; Crossref confirms M. Dyer, P. Gritzmann, A. Hufnagel, SIAM J. Comput. 1998. | **VERIFIED** |
| O4 | FIXED | The rubric now states input-model fidelity as part of criterion 1 and output-mismatch/no-end-to-end-theorem exclusions for criteria 2–3; "No primitive scores 4 or 5" is deleted. I extracted all 15 `Score: **x/5**` lines and compared them with the 15 ranked-table rows: 2,4,3,3,1,2,2,2,2,2,1,2,1,0,1 — every one agrees. I then checked that each section's new per-criterion justification sums to its score: all 15 do. Kedlaya 3→4 and path amplification 3→2 are exactly the r1 demands. | **VERIFIED** (residue in O36) |
| O5 | FIXED | New §4 subsection "Is the isolated-singularity ground-state count the Milnor number?" states Tr(−1)^F = ±μ = ±dim Jac(W) for an isolated non-degenerate LG critical locus, lists the four hypotheses, and moves cancellation to an explicit witness: Witten's deformed de Rham complex on S¹ with b₀=b₁=1 and index 0 — arithmetically correct. D-jacobian-ring-susy carries the same display and the pitfall "alternating-index cancellation in a de Rham model does not refute the Landau–Ginzburg equality". The §4 "killers" list is rewritten. | **VERIFIED** (row-status defect in O32; sourcing in O-def table) |
| O6 | DOWNGRADED | The index convention is now β_{k−1}/\|Cl_k(G)\| in §5 Problem P, in the Berry Lemma 1 quotation, in the Schmidhuber factor √(C(s,k)/β_{k−1}), and in D-vr-betti-estimation — four places, one convention. The NSW sentence now says "union of balls, equivalently its Čech nerve", and §5 states in the body that the VR–Čech interleaving "has not been supplied here". Marking the row HOLD rather than claiming a composition is the honest choice and is what r1 demanded. | **VERIFIED** (status-name defect in O30) |
| O7 | FIXED | Half holds: the Schmidhuber–Lloyd escape clause ("an exponential advantage may be recoverable when the input is a specification of simplices") is added to §5, to K-QP5 and to the row, and matches `2209.14286`'s abstract; the NP-hardness wording is corrected to the source's ("approximating Betti numbers up to multiplicative error is NP-hard"); Gyurik–Cade–Dunjko is added as ref 67 with a resolved DOI. But the memo attributes **BQP-hardness** to that paper, which it does not contain — see O28. | **NOT VERIFIED** |
| O8 | FIXED | New §2A. Hallgren: I confirmed the JACM 2007 paper solves Pell, the principal ideal problem in real quadratic fields, and the class group under GRH — all three appear in the memo. EHKS: the STOC 2014 abstract states "a quantum algorithm that is polynomial in the degree of the field and the logarithm of its discriminant", exactly the memo's `[K:Q] + log|Disc K|`. The classical baseline is now a real citation (Cohen–Diaz y Diaz–Olivier, "Subexponential Algorithms for Class Group and Unit Computations", DOI 10.1006/jsco.1996.0143, verified) and the comparison is honestly stated as "polynomial quantum versus best-known heuristic subexponential classical methods, not an unconditional exponential separation theorem" — stronger than my r1 framing. Ref 70's DOI 10.4230/LIPIcs.ICALP.2016.16 404s in Crossref but resolves in DataCite to the correct title and all four authors (Dagstuhl registers with DataCite); `doi.org` returns 200. Ref 71 (RevModPhys.82.1) verified. Criterion 1 is conservatively withheld, and the ranked table, §2A score line and K-QP2A agree. | **VERIFIED** (residue in O34) |
| O9 | RETRACTED | The toric combination is deleted, Route 7 and C-262 are cited with their 2/5 and 4/5 scores, the quantum-walk delta is correctly bounded by K-QP10B, and Q5 is rewritten. But the *replacement* Combination 1 duplicates a different landed lane — see O26. | **NOT VERIFIED** |
| O10 | FIXED | The unreachable superpolynomial-mixing criterion is gone and the new criterion is reachable by amplitude estimation. But it is set against a classical baseline the campaign's own classical memo already rejects — see O27. | **NOT VERIFIED** |
| O11 | FIXED | I parsed all 23 rows: **every** `where-tested` field reads `none`. The three fabricated test descriptions ("rank-two tensors…", "translated thin-polytopes…", "reported device instances") and the two non-checker ones are gone. | **VERIFIED** |
| O12 | FIXED | Ref 25 now lists Part I with 10.2307/1970746 and Part II with 10.2307/1970747; Crossref confirms both (Ann. of Math. 90 (1969), pp. 460 and 496). The §4 body matches. | **VERIFIED** |
| O13 | FIXED | §2 now derives O(g² log q) from 2g+1 coefficients each of O(g log q) bits under the Weil bounds — my own r1 recomputation. | **VERIFIED** |
| O14 | FIXED | `s log₂ s` replaces `s log² s`, matching Berry Lemma 1 eq. (12); `log`→`ln` in two places, also matching; the spurious `poly(s)` is removed and an explicit sentence records its absence; the Dicke variant's `6|E|+2ks` factor matches eq. (13). | **VERIFIED** |
| O15 | FIXED | Row renamed `C-NEW-QP-MHOM-BEZOUT-PERMANENT`; `depends-on` is now D-multihomogeneous-bezout; the new definition carries the permanent expansion and the pitfall "B_A is not the general BKK mixed volume"; every downstream "BKK count/permanent" phrase is retitled (0 stale occurrences). The identity itself I verified numerically in r1 (sympy, n=3,4,5). | **VERIFIED** |
| O16 | RETRACTED | `C-NEW-QP-FINITE-FIELD-SEED` is deleted; §2 keeps only the D-finite-field-analogue citation and the funding consequence. | **VERIFIED** |
| O17 | FIXED | §10B, the row and D-real-variety-gibbs now state Wocjan et al.'s actual hypotheses — an FPRAS combining simulated annealing with MCMC under a non-adaptive cooling schedule, with the two quadratic reductions "linked and not independently claimed" — matching the `0811.0596` abstract I fetched in r1. The invented warm-start-overlap hypothesis is gone. | **VERIFIED** |
| O18 | RETRACTED | `C-NEW-QP-ID-KEDLAYA` deleted; the correction survives in §2 ("belongs in reference and worklog hygiene, not in a mathematical claim row") and as orchestrator action Q15. | **VERIFIED** |
| O19 | FIXED | The assumed "polynomial-time unique-encoding Jacobian arithmetic" is gone from the row and from D-curve-zeta-problem, replaced by "Kedlaya constructs the unique-encoding class-group/Jacobian operations from this input protocol; they are not an additional oracle promise" — matching §§6–7, Lemma 10 and Prop 11 of the paper. | **VERIFIED** |
| O20 | FIXED | The decision rule now states the convention explicitly and cites C-092/C-099; 7 rows carry SKETCH with `(cited theorem)`. | **VERIFIED** (residue in O35) |
| O21 | FIXED | Tang is now cited in §1's dequantization paragraph and Vafa–Warner in §4; ref 66 gains "M. Amy and L. Stinchcombe"; ref 35's author is corrected to Chiang-Heng Chien. But ref 35's **title** was replaced by one that is not this paper's title — see O29. | **NOT VERIFIED** |
| O22 | FIXED | §8 now reads "QMA-hard in a different graph-local input model at fixed particle number", plus "The graph is arbitrary; 'lattice-local' is not assumed." Matches `1311.3297`. | **VERIFIED** |
| O23 | FIXED | §8 records that the verified identifier suffices to lift C-099's mark, and Q13 makes it an orchestrator action. | **VERIFIED** |
| O24 | RESIDUE | Correctly out of lane (`claims/CLAIMS.md` is orchestrator-owned under rule 3); recorded as orchestrator action Q14. Accepting the residue. | **VERIFIED (as residue)** |
| O25 | FIXED | §7 cites Oh–Liu–Alexeev–Fefferman–Jiang with arXiv:2306.03709 and DOI 10.1038/s41567-024-02535-8 (Crossref: Nature Physics 2024) for the classical GBS simulation claim; the Ω(√d + 1/ε) quantum query lower bound appears in §10C, in K-QP10C, in the row and in D-toric-lattice-counting, and drove the honest 2→1 downgrade. | **VERIFIED** |

**Counts: VERIFIED 21 · NOT VERIFIED 4 (O7, O9, O10, O21) · NEW DEFECT 11 (O26–O36 below).**

---

## 2. New objections (changed text only)

### O26 — MAJOR. The replacement Combination 1 duplicates Arm B, which landed before this repair.

**Location:** Combinations §1, "Koszul-Laplacian Betti fractions plus DQC1-style trace estimation".

O9 objected that Combination 1 duplicated `scouting/real-variety.md` Route 7. The repair deleted that and substituted a one-week probe on "a supersymmetric Koszul Laplacian whose graded kernel records a syzygy or Betti nullity" combined with C-061's DQC1-style trace estimator. `scouting/koszul-betti.md` (596 lines, Arm B, committed at `68b5a2f`, one commit **before** this repair) has already done that work in far more depth, and its conclusions contradict the probe's premise:

- it prices the quantum side at `Õ(n (α_BE/Δ_N)(j/g_{i,N}) ε^{-2})` block-encoding uses, "`ε^{-1}` with amplitude estimation on a pure-state version" — i.e. the exact ε-exponent the probe proposes to discover;
- it names the competing classical baseline (Di Napoli–Polizzi–Saad stochastic Chebyshev/Lanczos eigenvalue counting, DOI 10.1002/nla.2048, "polynomial filtering plus Hutchinson traces counts eigenvalues in an interval, i.e. exactly the normalised nullity of L_W");
- it states the result: "**Proven margin over the baseline: none.** … **Arm B cannot beat arm A; it strictly contains it.**";
- it has already run the numerics (`checkers/explore/koszul_laplacian.py`) and proposed 10 rows, 8 definitions and killers K-KB1..10, including K-KB6 and K-KB9 which are precisely the probe's two failure modes.

The original lane brief for this memo also said Arm B "is being developed by a PARALLEL lane; do not develop it, just note the relation". Funding this probe would buy a week of work that is already on disk.

**FIX DEMAND:** delete the probe, cite `scouting/koszul-betti.md` §3 and its K-KB6/K-KB9 as the settled analysis, and either name a *delta* Arm B did not cover or leave Combinations at two entries.

**SURVIVING STATEMENT:** the observation that C-061's estimator and the Koszul Laplacian compose is correct; it is prior work in this campaign, not a new combination.

---

### O27 — MAJOR. Combination 1's success criterion is set against a classical baseline the campaign has already rejected.

**Location:** Combinations §1, success criterion.

The probe "succeeds only if it identifies a growing family with … total quantum error dependence O(ε^{-1}) versus a **verified classical O(ε^{-2}) sampling dependence**". `scouting/classical-landscape.md` L545 states: "Hutch++ obtains relative trace error with **O(1/ε)** matrix-vector products for PSD inputs [R55]", and L547 draws the conclusion the probe needs: "The possible advantage is therefore in the cost of applying the filter, not simply in 'quantum trace estimation.'" The object being estimated is a normalized trace of a spectral projector — PSD — so Hutch++ applies directly and the classical exponent is already 1, not 2. `scouting/koszul-betti.md` says the same thing independently ("both sides pay the Δ_N promise, one inside a QSVT and one inside a Krylov iteration").

r1 objected that the old criterion was unreachable by its own mechanism. The new one has the opposite defect: it is reachable *because* it races a strawman. A probe that cannot fail is not a probe.

**FIX DEMAND:** if the probe survives O26, replace the criterion with a filter-cost comparison at equal accuracy — quantum QSVT block-encoding uses at normalized gap Δ/α_BE versus classical Chebyshev-filtered Hutch++ matrix–vector products on the same sparse operator, with the ε-exponent held at 1 on both sides — and state the falsifier as a gap- or dimension-exponent margin.

**SURVIVING STATEMENT:** amplitude estimation does improve ε-dependence from ε^{-2} to ε^{-1} over *naive* Hutchinson sampling; that is not an advantage over the campaign's stated classical baseline.

---

### O28 — MAJOR. BQP-hardness is attributed to Gyurik–Cade–Dunjko, which does not prove it. (This corrects my own r1 wording.)

**Location:** §5 "Dequantization and hidden costs"; §5 score justification ("criterion 4 for the DQC1/BQP hardness evidence").

Memo: "Gyurik–Cade–Dunjko supply complementary dequantization resistance: natural generalizations of the LGZ linear-algebraic estimation task are DQC1-hard, **with BQP-hard regimes among the related rank-estimation problems**".

I downloaded `2005.02607v5` and extracted the text. The paper's results are Theorem 1 (llsd is DQC1-hard, and remains so for log-local Hamiltonians), Theorem 2 (llsd restricted to log-local Hamiltonians is DQC1-complete) and Theorem 5 (swes is DQC1-hard). **The string "BQP-hard" does not occur in the paper, and the only occurrence of "BQP-complete" is bibliography entry [25], Wocjan–Zhang.** The first clause of the memo's sentence is right; the second is not in the source.

Two aggravating facts. First, my r1 objection O7 itself wrote "DQC1-hard / BQP-hard in the relevant regimes", so the critic seeded this error; that r1 wording is hereby corrected. Second, `scouting/koszul-betti.md` had already issued the matching correction before this repair: "Gyurik–Cade–Dunjko … prove DQC1-hardness of **low-lying spectral density estimation**, *not* of normalised Betti number estimation, and leave the restriction to clique-complex Laplacians explicitly open; any row citing them for 'normalised BNE is DQC1-hard' is mis-citing." The memo's §5 body correctly says "natural generalizations", so it clears that second trap — but the score line does not.

**FIX DEMAND:** delete "with BQP-hard regimes among the related rank-estimation problems"; change the score justification to "criterion 4 for the DQC1-hardness of the natural generalization (llsd), noting that the restriction to clique-complex Laplacians is open".

**SURVIVING STATEMENT:** low-lying spectral density estimation is DQC1-hard and DQC1-complete for log-local Hamiltonians, which is evidence of dequantization resistance for the *generalization* of the LGZ task, not for Betti-number estimation itself.

---

### O29 — MINOR. The repair fixed ref 35's author and broke its title.

**Location:** reference 35.

r0 read "C.-F. Chien et al., GPU homotopy continuation, arXiv:2112.03444". The repair reads "Chiang-Heng Chien et al., **'Parallel GPU Implementation of Homotopy Continuation Methods for Solving Polynomial Systems'**". I queried the arXiv Atom API for both `2112.03444v1` and `2112.03444v2`: the title in both versions is **"GPU-Based Homotopy Continuation for Minimal Problems in Computer Vision"**. The supplied title matches no version of this paper.

**FIX DEMAND:** restore the actual title.

**SURVIVING STATEMENT:** the "up to 26 times" GPU speedup attributed to this arXiv id is correct (verified in r1).

---

### O30 — MINOR. `status: HOLD` is not one of L1's four statuses.

**Location:** row `C-NEW-QP-TDA-REAL-VARIETY`; decision rule paragraph.

CLAUDE.md L1 fixes the status set as {PROVED, SKETCH, CONJECTURE, REFUTED}, and `claims/CLAIMS.md`'s legend lists exactly those four. HOLD is a *critic disposition* in the r1 adjudication table, not a row status; a row carrying `status: HOLD` cannot be merged into the DAG without silently extending the ratchet's vocabulary. The memo's own decision rule now defines HOLD as a status ("HOLD marks a proposed row whose required composition is missing and must not be merged as a mathematical claim"), which is a lane artifact redefining a campaign-level convention.

**FIX DEMAND:** either withhold the row from the merge entirely (recording the missing step in the memo's Questions), or enter it as CONJECTURE with `missing step:` retained and the statement restricted to the conditional it can support. Do not introduce a fifth status.

**SURVIVING STATEMENT:** the row's content — that the VR–Čech interleaving is the missing step — is correct and is the right thing to record.

---

### O31 — MINOR. Two REFUTED rows invert the DAG's REFUTED convention and add a non-standard field.

**Location:** rows `C-NEW-QP-MACAULAY-CONDITION-EQUALITY`, `C-NEW-QP-ANALOGUE-DEGENERACY`.

In `claims/CLAIMS.md` a REFUTED row puts the **false** proposition in `statement` and names the residue in `surviving statement` (C-155, C-181 are the pattern). Both rows now put the **true** statement in `statement`, keep `status: REFUTED`, and introduce a new field `refuted proposition:`. The other nine REFUTED rows keep the "The claim that X … is false" form, so the memo is inconsistent with itself as well as with the DAG. The memo also writes `surviving weaker statement:` where the DAG writes `surviving statement:`.

**FIX DEMAND:** for both rows, move the false proposition into `statement` and the true content into `surviving statement`; drop the `refuted proposition:` field; use the DAG's field name throughout.

**SURVIVING STATEMENT:** both rows' mathematical content is correct and, for the first, is now backed by a verified witness (see O33).

---

### O32 — MINOR. `C-NEW-QP-WITTEN-INDEX-COUNT` at SKETCH violates the memo's own decision rule.

**Location:** row `C-NEW-QP-WITTEN-INDEX-COUNT`; D-jacobian-ring-susy.

The decision rule now says "Imported published theorems are proposed at status SKETCH with `where-proved: … (cited theorem)`. **New compositions remain CONJECTURE.**" This row is a composition of two different statements — an existence claim about de Rham SUSY models, plus the positive LG identity Tr(−1)^F = ±μ — and its `where-proved` names Witten (DOI 10.4310/jdg/1214437492) and Lerche–Vafa–Warner (DOI 10.1016/0550-3213(89)90474-4) as "(cited results)". Neither source states the ±μ identity: Witten proves Morse inequalities, and Lerche–Vafa–Warner identify the chiral ring with the Jacobian quotient. The ±μ sentence entered this campaign as an assertion in my r1 verdict, not as a quoted theorem, and it is not entitled to SKETCH on that basis.

**FIX DEMAND:** set the status to CONJECTURE, or supply a specific source and theorem/equation number for "all LG vacua of an isolated non-degenerate critical locus lie in one fermion-number sector, so Tr(−1)^F = ±μ" and keep SKETCH only for that clause.

**SURVIVING STATEMENT:** the S¹ cancellation witness (b₀=b₁=1, index 0) is elementary and correct, and the separation of de Rham cancellation from the LG case is the right structural point.

---

### O33 — MINOR. The new §1 witness has a trivial kernel, contradicting the row that cites it.

**Location:** §1 "Combination with the seed"; row `C-NEW-QP-MACAULAY-CONDITION-EQUALITY`.

I re-derived the new counterexample numerically. With f₁ = z₀, f₂ = (z₀+z₁)/√2 and N = 1: both generators have unit Bombieri–Weyl norm (1.000, 1.000); H₁ has eigenvalues 0.29289322 and 1.70710678, i.e. exactly 1 ∓ 1/√2; α_BE/Δ₁ = 5.828427 = (1+√2)²; and κ_b(Φ₁) = 1.000000 on the largest left singular vector and 2.414214 = 1+√2 on the smallest. **Every number in the memo checks out.**

The defect is elsewhere: the row describes α_BE/Δ_N as "a spectral gap ratio of a PSD operator **with nontrivial kernel**", but in this instance Φ₁ is surjective onto R₁, so ker H₁ = 0 and HF(1) = 0 — the witness does not exhibit the feature the row uses to distinguish the two quantities.

**FIX DEMAND:** use three variables — f₁ = z₀, f₂ = (z₀+z₁)/√2 in ℂ[z₀,z₁,z₂], N = 1. Then H₁ on the 3-dimensional R₁ has eigenvalues 1±1/√2 and 0, ker H₁ = span{z₂} is 1-dimensional, Δ₁ = 1−1/√2 is the smallest **nonzero** eigenvalue, and α_BE/Δ₁ = (1+√2)² is unchanged while κ_b is unchanged. One extra variable repairs the witness at no cost.

**SURVIVING STATEMENT:** the two quantities differ; the arithmetic is right.

---

### O34 — NOTE. Two `where-proved` fields point at a theorem number I could not confirm, or at less than the row asserts.

`C-NEW-QP-UNIT-GROUP` cites "DOI 10.1145/2591796.2591860 **Theorem 1.2**". I confirmed the running-time claim from the STOC 2014 abstract ("polynomial in the degree of the field and the logarithm of its discriminant") but could not reach the paper body to confirm the numbering (the Caltech repository returned HTTP 403). `C-NEW-QP-MACAULAY-HHL-UNIFORM` cites "Theorem 4.5" alone, although its Ω(2^{h/2}) clause is stated in §1 of that paper and follows from Theorem 4.5 only after specialising the max degree.

**FIX DEMAND:** drop "Theorem 1.2" unless the body has been read; extend the other to "Theorem 4.5 and §1".

---

### O35 — NOTE. The SKETCH convention still needs an orchestrator action that the memo did not list.

r1's O20 fix demand had two halves: use SKETCH for cited published theorems, **and** record the convention once in `claims/CLAIMS.md`'s legend. The memo did the first. The legend still reads "`SKETCH` — a proof or derivation exists **in the seed**", which none of the 7 new SKETCH rows satisfies. The memo added orchestrator actions Q13–Q15 but not this one.

**FIX DEMAND:** add a Q16: widen the CLAIMS.md SKETCH legend to "a proof or derivation exists in the seed **or in a cited published source with a resolved identifier**, with no converged critic verdict in this campaign".

---

### O36 — NOTE. One score justification is silent on criterion 4.

§4's justification reads "earns criterion 1 … has no end-to-end quantum resource theorem, no survival proof for gap and readout, and no established cheap protocol that returns the invariant" — covering criteria 2, 3 and 5 but not 4, even though the section says "Low-rank dequantization is not the main issue", which would earn it. The score of 1 is defensible either way, but the audit trail should be complete for all 15 sections since O4 made the rubric explicit.

---

**New-objection counts: 3 MAJOR (O26, O27, O28) · 5 MINOR (O29, O30, O31, O32, O33) · 3 NOTE (O34, O35, O36). 0 FATAL.**

---

## 3. Lockstep check

- **Ranked table vs sections.** 15 ranked rows; 15 `Score:` lines; scores agree one-for-one (2, 4, 3, 3, 1, 2, 2, 2, 2, 2, 1, 2, 1, 0, 1). Rank order is monotone in score. Every killer id in the table matches the killer stated in its section, including the two new ones (K-QP2A) and the two rewritten ones (K-QP5, K-QP10C).
- **Rubric vs scores.** Each section's per-criterion justification sums to its score (15/15). One incomplete audit trail (O36).
- **Sections vs rows.** Checked in both directions. §2A's conservative "not coordinate-ideal problems" framing is reproduced in D-number-field-ideal-problems' pitfalls and is *not* overclaimed by C-NEW-QP-PRINCIPAL-IDEAL or C-NEW-QP-UNIT-GROUP. §5's "vertex-and-edge input model" restriction is carried into K-QP5, C-NEW-QP-TDA-GENERIC-EXPONENTIAL and its surviving statement. §10C's Ω(√d+1/ε) appears in the section, the killer, the row and the definition. **One miss:** §5's score justification claims "DQC1/BQP hardness evidence" while no row asserts BQP-hardness and the source proves none — the section claims more than any row (O28).
- **Rows vs definitions.** All 23 rows' `depends-on` ids resolve: 14 to definitions proposed in this memo, the rest to existing D-ids and to C-052, C-055, C-057, C-061, C-091, C-097, C-099, C-246, C-009 — I confirmed C-246 and D-homogeneous-ideal exist and that none of the 14 proposed definition ids collides with an existing entry. No row depends on a REFUTED C-row.
- **Statuses.** 23 rows: SKETCH 7, REFUTED 11, CONJECTURE 4, HOLD 1 — matching the memo's own tally. All 23 `where-tested` fields read `none`. HOLD is not a legal status (O30).
- **Combinations vs DAG.** Combination 1 is not disjoint (O26); Combinations 2 and 3 are unchanged from r0 apart from the BKK→Bézout renaming and were not objected to in r1.

---

## 4. Proposed claim rows: decisions

| id | decision | note |
|---|---|---|
| C-NEW-QP-MACAULAY-HHL-UNIFORM | **ACCEPT AS SKETCH** | Bound, hypotheses and specialisations verified against `2111.00405v2`. Extend `where-proved` to "Theorem 4.5 and §1" (O34). |
| C-NEW-QP-MACAULAY-CONDITION-EQUALITY | **ACCEPT WITH REWORDING** | Restore the DAG convention (O31) and repair the witness (O33). Exact text: *statement:* "For every homogeneous tuple (f_j) and every N, the Chen–Gao truncated QLS condition number κ_b(M) equals the seed ratio α_BE/Δ_N." *status:* REFUTED. *surviving statement:* "C-097 — the two obstructions are analogous and no reduction is known between them." *where-proved:* "explicit instance: f₁=z₀, f₂=(z₀+z₁)/√2 in ℂ[z₀,z₁,z₂], N=1, unit Bombieri–Weyl generators; H₁ has spectrum {0, 1−1/√2, 1+1/√2}, so α_BE/Δ₁=(1+√2)²≈5.8284, while κ_b(Φ₁)=1 on the largest left singular vector and 1+√2≈2.4142 on the smallest." Delete the `refuted proposition:` field. |
| C-NEW-QP-ZETA-CURVE | **ACCEPT AS SKETCH** | Hypotheses now match Kedlaya's input protocol; Theorem 1 verified. |
| C-NEW-QP-ZETA-HYPERSURFACE | **ACCEPT AS REFUTED** | §10 / Question 12 verified in r1; surviving statement added. |
| C-NEW-QP-PRINCIPAL-IDEAL | **ACCEPT AS SKETCH** | Matches Hallgren, JACM 54(1) 2007; the compact-output qualification is correctly part of the statement. |
| C-NEW-QP-UNIT-GROUP | **ACCEPT WITH REWORDING** | Substance verified. Change `where-proved` to "DOI 10.1145/2591796.2591860 (cited theorem)" — drop "Theorem 1.2" until the body is read (O34). |
| C-NEW-QP-HIDDEN-POLYNOMIAL | **ACCEPT AS SKETCH** | Matches Decker–Draisma–Wocjan's abstract verbatim (verified r1). |
| C-NEW-QP-HIDDEN-EXPLICIT-TRANSFER | **ACCEPT AS CONJECTURE** | Reworded to the "no reduction is known" form as demanded; `where-proved: none` is correct. |
| C-NEW-QP-SUSY-HODGE-SPEEDUP | **ACCEPT AS REFUTED** | Hilbert series verified numerically in r1; applications-memo attribution and the e^{−0.249n}–e^{−0.299n} fits now exact. |
| C-NEW-QP-WITTEN-INDEX-COUNT | **ACCEPT WITH REWORDING** | Change `status:` to CONJECTURE, or split off the ±μ clause with a specific source and theorem number (O32). Statement text otherwise correct. |
| C-NEW-QP-TDA-REAL-VARIETY | **HOLD** | Missing step correctly named (VR–Čech interleaving plus a persistence-interval theorem). Must not be merged with `status: HOLD`; withhold from the DAG or enter as CONJECTURE per O30. |
| C-NEW-QP-TDA-GENERIC-EXPONENTIAL | **ACCEPT AS REFUTED** | Now carries the source's own NP-hardness wording, the input-model restriction, the corrected index and the simplices exception. |
| C-NEW-QP-PATH-AA | **ACCEPT AS CONJECTURE** | Per-invocation error o(√(r/D)) as demanded; `where-proved: none (conditional composition)` correct. |
| C-NEW-QP-PATH-INTERNAL-SPEEDUP | **ACCEPT AS REFUTED** | Surviving statement added. |
| C-NEW-QP-MHOM-BEZOUT-PERMANENT | **ACCEPT AS CONJECTURE** | Renamed, definition supplied, `depends-on` corrected; identity verified numerically (r1, n=3,4,5). |
| C-NEW-QP-BOSON-COUNT | **ACCEPT AS REFUTED** | Renamed object; surviving statement added. |
| C-NEW-QP-ANALOGUE-DEGENERACY | **ACCEPT WITH REWORDING** | Content is the substantive version r1 demanded. Restore the REFUTED convention (O31): *statement:* "Ground-state energy measurements alone determine HF_{R/I}(N)." *surviving statement:* the current text, ending "(D-analogue-degeneracy-readout)". |
| C-NEW-QP-FIXED-MODE-HARDWARE | **ACCEPT AS CONJECTURE** | Unary-N quantifier and `where-proved: restatement of C-057 and C-099` are both as demanded. |
| C-NEW-QP-ANNEALING-DEMONSTRATION | **ACCEPT AS REFUTED** | All device numbers verified in r1; `where-tested` now `none`. |
| C-NEW-QP-GROEBNER-ANNEALER | **ACCEPT AS REFUTED** | "just over 200 000" verified in r1. |
| C-NEW-QP-QPCA-SECANT | **ACCEPT AS REFUTED** | Fabricated `where-tested` removed. |
| C-NEW-QP-GIBBS-QUADRATIC | **ACCEPT AS SKETCH** | Hypotheses now Wocjan et al.'s own. |
| C-NEW-QP-VOLUME-EHRHART | **ACCEPT AS REFUTED** | Lower bound added; fabricated `where-tested` removed. |

**Row decision counts: ACCEPT AS SKETCH 5 · ACCEPT AS REFUTED 9 · ACCEPT AS CONJECTURE 4 · ACCEPT WITH REWORDING 4 · HOLD 1 · REJECT 0. Total 23.**

## 5. Proposed definitions: decisions

| id | decision | note |
|---|---|---|
| D-boolean-macaulay-solve | **ACCEPT** | Both matrix sizes and the κ_b formula verified against the source; the "Grover cost is not a condition-number bound" pitfall is the right permanent guard. |
| D-curve-zeta-problem | **ACCEPT** | Pitfall now states the group law is constructed, not assumed. |
| D-number-field-ideal-problems | **ACCEPT** | Correctly separates Hallgren's real-quadratic principal-ideal theorem from the arbitrary-degree unit-group theorem, and flags the compact-output issue; cites D-homogeneous-ideal, which exists. |
| D-hidden-polynomial-structure | **ACCEPT** | Unchanged, accepted in r1. |
| D-jacobian-ring-susy | **REWORD** | The ±μ display needs a source that states it, or an explicit mark that it is the campaign's own assertion pending a citation (O32). Everything else is right, including the new cancellation pitfall. |
| D-vr-betti-estimation | **ACCEPT** | Index convention fixed; Čech-vs-VR pitfall added. |
| D-coherent-path-oracle | **ACCEPT** | Per-invocation error pitfall added. |
| D-multihomogeneous-bezout | **ACCEPT** | Expansion is correct (verified numerically); the "not the general BKK mixed volume" pitfall is the point of the definition. |
| D-optical-counting-access | **ACCEPT** | Unchanged. |
| D-analogue-degeneracy-readout | **ACCEPT** | Ω(1/ε²) shot bound added. |
| D-boolean-residual-energy | **ACCEPT** | 2ⁿ−1, 2^{(n+2)/2}−2 and 3·2^{(n−1)/2}−2 all verified against `2111.13224` in r1. |
| D-tensor-secant-problem | **ACCEPT** | Unchanged. |
| D-real-variety-gibbs | **ACCEPT** | Wocjan hypotheses now stated in the pitfall. |
| D-toric-lattice-counting | **ACCEPT** | Lower bound added to the pitfall. |

**Definition decision counts: ACCEPT 13 · REWORD 1 · REJECT 0. Total 14.**

---

## 6. Trajectory

r1: 0 FATAL, 10 MAJOR, 11 MINOR, 4 NOTE (25). r2: 0 FATAL, 3 MAJOR, 5 MINOR, 3 NOTE (11), of which the three MAJORs carry the unresolved substance of r1's O7, O9 and O10 — one mis-citation and one duplicated-and-unfalsifiable probe. Every quantitative repair I could recompute or refetch checked out, including the two hardest: the Ding et al. condition-number formulas and the new §1 counterexample. The memo is one narrow revision from PASS: delete Combination 1 and delete six words from §5.

VERDICT: FAIL(O26, O27, O28)
