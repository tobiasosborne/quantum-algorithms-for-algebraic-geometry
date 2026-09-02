# Adversarial critic verdict: `scouting/koszul-betti.md`, round 3

- **Target:** `scouting/koszul-betti.md` and `checkers/explore/koszul_laplacian.py`
- **Repair range:** `0f5ef2c..HEAD`
- **Date:** 2026-09-03
- **Critic model:** OpenAI Codex, GPT-5 family

## Commands run

| Command | Exit |
|---|---:|
| `bd prime` | 0 |
| Required file inspections and exact-text searches | 0 |
| `git diff 0f5ef2c HEAD -- scouting/koszul-betti.md checkers/explore/koszul_laplacian.py` | 0 |
| `cd checkers && timeout 900 python3 explore/koszul_laplacian.py` | 0 |
| Independent Python recomputation of O17, O19, and O21 quantities | 0 |

The prescribed checker completed in 15.6 seconds. Parts A–H passed, the 5-cycle row reported `51/150` versus `1/150`, the adjacent-projector mutations reported nullity zero, both dimension computations agreed, and M1–M4 all reported `RED (good)`.

## O17–O22 disposition

| Objection | Proposer disposition | Adjudication |
|---|---|---|
| **O17** | FIXED | **VERIFIED.** The memo consistently distinguishes the harmonic projector extended by zero from the zero extension of \(L_W\). Fresh computation gives \(M_N=15\), \(h_N=10\), \(b=10\), and \(\beta=1\), hence harmonic-projector trace \(1/150\), while zero-extended \(L_W\) has nullity \((15-10)10+1=51\) and fraction \(51/150\). Part H reproduces both values. Step 9.5 prices the extra \(P_{0,N}\) use in \(\widetilde L\). |
| **O18** | FIXED | **VERIFIED.** Step 9.4, §3, K-KB9, and D8 all require adjacent-degree access. Since \(q_{i-1,N+1}=P_{0,N}QP_{0,N+1}\), the incoming term depends on \(P_{0,N+1}\). Generator mode supplies \(H_N,H_{N+1}\) and both required normalized-gap promises; quotient mode supplies \(Z_{k,N},Z_{k,N+1}\). The adjacent-degree maximum is equivalent up to a constant to the requested sum. Part H obtains nullity zero after replacing \(P_{0,N+1}\) by the identity. |
| **O19** | FIXED | **VERIFIED.** Independently, \(h_2=\binom{22}{2}-5=226\) and \(h_3=\binom{23}{3}-5\binom{21}{1}=1666\). Thus \(226\binom{21}{2}=47460\) and \(1666\binom{21}{3}=2215780\). Both corrected values occur in the memo and checker. |
| **O20** | DOWNGRADED | **VERIFIED.** Step 5.6, K-KB6, D5, and the HOLD row restrict the conclusion to a uniformly positive lower bound on the selected squarefree summand with \(\phi(1)>0\). They explicitly disclaim total-block and reverse comparisons and retain all three missing steps. |
| **O21** | DOWNGRADED | **NEW DEFECT.** The named-family quantifier, explicit promise, and counterfamily \(h_n/M_n=1\) are verified. However, three changed summaries incorrectly say that the costs \(M_N/h_N\) and \(\sqrt{M_N/h_N}\) are exponentially small. They are exponentially large when the acceptance weight \(h_N/M_N\) is exponentially small. See O23. |
| **O22** | FIXED | **VERIFIED.** Active definition D8 includes \(\epsilon\), contains no thresholds, supplies both adjacent degrees, and makes regularity optional metadata only for whole-table enumeration. Historical discussion of the removed thresholds is not part of the problem definition. |

## Exact-text audit

| Required text | Result |
|---|---|
| **D5 — D-betti-gap** | **VERIFIED verbatim** |
| **D6 — D-normalised-betti-fraction** | **VERIFIED verbatim** |
| **D8 — D-betti-estimation-problem** | **VERIFIED verbatim and without thresholds** |
| **C-NEW-KB-QMA1 missing step** | **VERIFIED verbatim:** “a polynomial reduction preserving the total-block normalized gap across all non-squarefree summands.” |
| **C-NEW-KB-GAP-INDEPENDENT missing steps** | **VERIFIED verbatim:** “a total-block counterfamily, a specified positive class of forbidden lower bounds, and any reverse-direction result.” |
| **C-NEW-KB-DEQUANT surviving statements** | **VERIFIED verbatim**, both sentences |
| **C-NEW-KB-NO-FREE-LUNCH surviving statement** | **VERIFIED verbatim** |

## New objections

### O23 — MAJOR: the overlap cost is stated with the exponential direction reversed

- **Location:** status summary, lines 35–38; §3 criterion 3(a), lines 448–452; K-KB11, lines 607–613.
- **Computation:** These passages first identify the rejection and coherent costs as
  \[
  \frac{M_N}{h_N},\qquad \sqrt{\frac{M_N}{h_N}},
  \]
  and then call “that factor” exponentially small for the quadratic complete-intersection family. For \(n\) quadrics in \(\mathbf P^n\) at \(N=n\),
  \[
  h_n=2^n,\qquad M_n=\binom{2n}{n},
  \]
  so
  \[
  \frac{h_n}{M_n}\sim\frac{\sqrt{\pi n}}{2^n}
  \]
  is exponentially small, whereas
  \[
  \frac{M_n}{h_n}\sim\frac{2^n}{\sqrt{\pi n}}
  \]
  and its square root are exponentially large. At \(n=8\), the checker’s \(h_n/M_n=0.019891\) corresponds to \(M_n/h_n=50.2734\), not a small cost. Step 9.3 itself gets the direction right, so the three summaries are not in lockstep with it.
- **FIX DEMAND:** In every affected passage, distinguish the overlap from its cost. Use: “The acceptance weight \(h_N/M_N\) is exponentially small for the quadratic complete-intersection family at \(N=n\), and potentially exponentially small in general; equivalently, the rejection-sampling cost \(M_N/h_N\) and coherent-projection cost \(\sqrt{M_N/h_N}\) are exponentially large.”
- **SURVIVING STATEMENT:** The acceptance weight can be exponentially small, making conditional normalization exponentially expensive; no unconditional conditional-output algorithm follows without a Hilbert-weight promise or preparation oracle.

## Final proposed-row decisions

| Proposed row | Decision |
|---|---|
| **C-NEW-KB-HODGE** | **ACCEPT AS CONJECTURE** |
| **C-NEW-KB-FREE** | **ACCEPT AS CONJECTURE** |
| **C-NEW-KB-SUPPORT** | **ACCEPT AS CONJECTURE** |
| **C-NEW-KB-HOCHSTER** | **ACCEPT AS CONJECTURE** |
| **C-NEW-KB-QMA1** | **HOLD.** Missing step: “a polynomial reduction preserving the total-block normalized gap across all non-squarefree summands.” |
| **C-NEW-KB-DEQUANT** | **ACCEPT AS REFUTED.** Surviving statements: “At constant normalized gap and constant additive error, the cited simplicial-complex estimator is polynomial-time classical.” “Apers et al. directly apply to the squarefree multidegree summands explicitly identified with ordinary simplicial Laplacians.” |
| **C-NEW-KB-GAP-INDEPENDENT** | **HOLD.** Missing steps: “a total-block counterfamily, a specified positive class of forbidden lower bounds, and any reverse-direction result.” |
| **C-NEW-KB-FRACTION** | **ACCEPT AS CONJECTURE** |
| **C-NEW-KB-SEED-IS-A-BLOCK** | **ACCEPT AS CONJECTURE** |
| **C-NEW-KB-NO-FREE-LUNCH** | **ACCEPT AS REFUTED.** Surviving statement: “If the only available quotient access is obtained by QSVT from \(H_N\), constructing a call to \(L_W\) inherits dependence on \(\alpha_{\mathrm{BE}}/\Delta_N\), with the required adjacent-degree gaps included.” |

## Final definition decisions

| Definition | Decision |
|---|---|
| **D-fermionic-modes** | **ACCEPT** |
| **D-koszul-supercharge** | **ACCEPT** |
| **D-betti-laplacian** | **ACCEPT** |
| **D-graded-betti-number** | **ACCEPT** |
| **D-betti-gap** | **ACCEPT** |
| **D-normalised-betti-fraction** | **ACCEPT** |
| **D-generator-koszul-supercharge** | **ACCEPT** |
| **D-betti-estimation-problem** | **ACCEPT** |

**LOCKSTEP:** NO — Step 9.2–9.3 and D-normalised-betti-fraction correctly distinguish the exponentially small acceptance weight \(h_N/M_N\) from the exponentially large costs \(M_N/h_N\) and \(\sqrt{M_N/h_N}\), but the status summary, §3 criterion 3(a), and K-KB11 call those costs exponentially small. All O17, O18, O20, and O22 qualifiers and both HOLD/REFUTED row dispositions are otherwise synchronized.

VERDICT: FAIL(O23)