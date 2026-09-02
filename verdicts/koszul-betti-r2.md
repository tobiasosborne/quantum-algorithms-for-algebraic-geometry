# Adversarial critic verdict: `scouting/koszul-betti.md`, round 2

- **Target:** `scouting/koszul-betti.md` and `checkers/explore/koszul_laplacian.py`
- **Repair range:** `bceb14f..98053f5`
- **Date:** 2026-09-03
- **Critic model:** OpenAI Codex, GPT-5 family

## Commands run

| Command | Exit |
|---|---:|
| `bd prime` | 0 |
| `sed`, `nl`, and `rg` inspections of the required files | 0 |
| `git diff bceb14f 98053f5 -- scouting/koszul-betti.md checkers/explore/koszul_laplacian.py` | 0 |
| `cd checkers && timeout 900 python3 explore/koszul_laplacian.py` | 0 |
| Independent Python recomputation of the \(M_N/h_N\) conversion, ambient-extension nullity, \(m\)-cycle incidence spectra, and complete-intersection dimensions | 0 |
| Independent square-system counterfamily computation | 0 |
| `rg -n 'koszul\|M1\|M2\|M3\|M4' checkers/MUTATIONS.md` | 1, expected no match |

The prescribed checker completed in 26.3 seconds. Parts A–G passed, and M1–M4 all reported `RED (good)`.

## O1–O16 disposition

| Objection | Proposer disposition | Adjudication |
|---|---|---|
| **O1** | FIXED | **NOT VERIFIED.** The support index, regularity convention, positive-HF condition, and nonzero-gap condition are corrected. However, the resubmitted problem says P1 is only for table enumeration and then imposes P1 on `GAPPED-BETTI`; see O22. |
| **O2** | FIXED | **NEW DEFECT.** The \(M_N/h_N\) conversion is now arithmetically correct, but the ambient “zero-mode weight” is not the zero-mode weight of \(L_W\) extended by zero, the block cost omits \(P_{0,N+1}\), and the claimed obstruction for every square system is false. See O17, O18, and O21. |
| **O3** | RETRACTED | **VERIFIED.** The memo now correctly gives \(n^{O(\log n)}\) at constant gap and inverse-polynomial error and withdraws the former polynomial-time conclusion. |
| **O4** | FIXED | **VERIFIED.** The Apers result is restricted to directly accessible squarefree simplicial summands; no generic sparse-row oracle for projected \(L_W\) is claimed. |
| **O5** | DOWNGRADED | **VERIFIED.** The total-block QMA\(_1\)-hardness claim is on HOLD, weighted and unweighted results are distinguished, and the BQP consequence is explicitly conditional. |
| **O6** | FIXED | **NEW DEFECT.** The regimes and row statement are corrected, but two block dimensions in the repaired memo are wrong; see O19. |
| **O7** | FIXED + partly supplied | **NOT VERIFIED.** The cycle formula and ideal/metric dependence are correct, but §1, K-KB6, and D-betti-gap still state an unquantified “no lower bound” conclusion that the HOLD row itself admits is not precise. See O20. |
| **O8** | FIXED | **VERIFIED.** The repaired statement is the per-differential singular-value pairing. The checker obtains maximum deviation \(2.13\times10^{-14}\) and prints the adjacent-block counterexample. |
| **O9** | FIXED | **VERIFIED.** The \(\beta_2\) statement is restricted to a minimal free resolution/minimal homogeneous presentation, and the \((x,x)\) counterexample is retained. |
| **O10** | FIXED | **VERIFIED.** Conjugate-linear duality, Hilbert adjoints, and the finite-particle domain are stated correctly. |
| **O11** | RETRACTED | **NOT VERIFIED.** The universal \(P_0\)-per-call claim is correctly retracted and filtering repetitions are separated, but the revised generator-only call cost still omits the adjacent-degree projector and gap; see O18. |
| **O12** | FIXED, one residue | **NOT VERIFIED.** Fixtures, explicit \(X\), absolute nullity threshold, PSD checks, characteristic labels, and in-process M1–M4 are verified. M1–M4 remain absent from `checkers/MUTATIONS.md`, contrary to L4 and the original FIX DEMAND. |
| **O13** | FIXED | **VERIFIED.** The memo is explicitly non-theorem status, provisional definitions and claim IDs are identified, merge ordering is stated, and C-103 replaces C-107. |
| **O14** | FIXED | **VERIFIED.** Every PRD criterion opens with `FAILS`, the ququart wording is corrected, and no speedup is claimed. |
| **O15** | FIXED, retained | **VERIFIED.** The core finite-dimensional identities survive with the O10 qualifications. |
| **O16** | FIXED | **VERIFIED.** The repaired theorem applications respect the cited gaps, weights, and access models; the QMA\(_1\) conclusion is not asserted for the total block. |

## New objections

### O17 — MAJOR: the ambient trace uses the wrong zero eigenspace

- **Location:** §1 Step 9.1, lines 172–176; D-normalised-betti-fraction, lines 561–566; D-betti-estimation-problem, lines 587–590.
- **Computation:** \(L_W\) is defined on \(W_N\otimes\Lambda^i\). Extending it by zero to \(R_N\otimes\Lambda^i\) makes the entire orthogonal complement a zero eigenspace. For the 5-cycle block \((i,N)=(3,2)\),
  \[
  M_N=15,\quad h_N=10,\quad b=\binom53=10,\quad\beta_{3,5}=1.
  \]
  The desired ambient ratio is \(1/150\), whereas the zero-mode weight of zero-extended \(L_W\) is
  \[
  \frac{(15-10)10+1}{150}=\frac{51}{150}=0.34.
  \]
  Thus an unspecified “DQC1-style trace estimate” does not return the stated ratio.
- **FIX DEMAND:** Define the ambient observable as the harmonic projector on \(W_N\otimes\Lambda^i\) extended by zero, or filter
  \[
  \widetilde L_{i,N}=L_W+j(1-\widehat P_N),\qquad j=N+i>0,
  \]
  whose zero eigenspace is exactly the harmonic subspace. Price the additional projector use.
- **SURVIVING STATEMENT:** The normalized trace of the harmonic projector extended by zero is \(\beta_{i,j}/(M_N\binom{n+1}{i})\).

### O18 — MAJOR: generator-only access to \(H_N\) does not construct the block

- **Location:** §1 Steps 9.4–9.5, lines 187–198; K-KB9, lines 496–501; D-betti-estimation-problem, lines 578–586.
- **Computation:** On block \((i,N)\),
  \[
  L_{i,N}=q_{i,N}^{\dagger}q_{i,N}
          +q_{i-1,N+1}q_{i-1,N+1}^{\dagger}.
  \]
  The first term uses \(P_{0,N}\), while the incoming term contains
  \[
  QP_{0,N+1}Q^\dagger.
  \]
  Therefore access only to \(H_N\), with a promise only on \(\Delta_N/\alpha_N\), is insufficient. A small \(\Delta_{N+1}\) can make the claimed polynomial implementation fail despite P4. Direct quotient access likewise needs the adjacent maps \(Z_{k,N}\) and \(Z_{k,N+1}\).
- **FIX DEMAND:** In generator mode supply \(H_N,H_{N+1}\) and promise inverse-polynomial \(\Delta_r/\alpha_r\) for every nontrivial required projector \(r\in\{N,N+1\}\). Replace
  \(O(n\alpha_{\mathrm{BE}}/\Delta_N)\) by an adjacent-degree sum or maximum. In quotient mode supply both adjacent compressed-multiplication maps.
- **SURVIVING STATEMENT:** Given direct adjacent compressed maps, or generator access with good gaps at every required adjacent degree, the filtering cost has the advertised \(j/g_{i,N}\) dependence.

### O19 — MINOR: the repaired complete-intersection dimension table is numerically false

- **Location:** §2(g), lines 326–334.
- **Computation:** For \(n=20,c=5\),
  \[
  \dim(i=2)=47460,\qquad \dim(i=3)=2215780,
  \]
  not \(23730\) and \(886445\). The fractions printed beside them equal \(10/47460\) and \(10/2215780\), so the fractions and the checker output are correct but the memo table is stale.
- **FIX DEMAND:** Replace the two dimensions by `47460` and `2215780`.
- **SURVIVING STATEMENT:** The exact fraction and the fixed-\((c,i)\) asymptotic in C-NEW-KB-FRACTION are correct.

### O20 — MAJOR: the cycle family does not prove the stated unqualified no-function claim

- **Location:** §1 Step 5.6, lines 143–148; K-KB6, lines 480–486; D-betti-gap, lines 555–560; C-NEW-KB-GAP-INDEPENDENT, lines 679–697.
- **Computation:** The incidence-matrix spectra independently give
  \[
  \Delta_2=1,\qquad g_{\rm sq}=2-2\cos(2\pi/m)\to0.
  \]
  This rules out a uniform bound \(g_{\rm sq}\ge\phi(\Delta_2)\) only when \(\phi(1)>0\). It does not rule out \(\phi(1)=0\), does not concern the defined total-block \(g_{i,N}\) beyond the finite observations \(m\le8\), and proves no reverse inequality. The HOLD row explicitly acknowledges these missing qualifications, while §1, K-KB6, and the definition do not.
- **FIX DEMAND:** Replace the categorical sentence everywhere by: “The \(m\)-cycle family rules out any uniform strictly positive lower bound on the selected squarefree-summand gap depending only on \(\Delta_2\): no \(\phi\) with \(\phi(1)>0\) satisfies \(g_{\rm sq}\ge\phi(\Delta_2)\) throughout this family. No total-block or reverse comparison is established.”
- **SURVIVING STATEMENT:** Constant Macaulay gap does not ensure a uniformly positive squarefree-summand Betti gap.

### O21 — MAJOR: the overlap obstruction is overgeneralized to every square system

- **Location:** status summary; §1 Step 9.3, lines 182–186; §3 criterion 3; K-KB11, lines 507–511.
- **Computation:** The cited \(0.75^{\mathrm{codim}}\) calculation is for complete intersections of quadrics at \(N=n\). Take instead \(n\) generic degree-\(n+1\) forms in \(\mathbf P^n\). This is a zero-dimensional square complete intersection, but at \(N=n\) all generators have degree greater than \(N\), so
  \[
  I_N=0,\qquad h_N=M_N,\qquad h_N/M_N=1.
  \]
  Explicitly this gives ratios \(1\) for \(n=2,3,4,8\), not exponential decay.
- **FIX DEMAND:** Replace “exponentially small for every square system” by a named-family statement, such as “exponentially small for the quadratic complete-intersection family at \(N=n\), and potentially exponentially small in general.” Preserve the explicit \(h_N/M_N\) promise.
- **SURVIVING STATEMENT:** The conversion factor can be exponential, so no unconditional conditional-output algorithm follows without a Hilbert-weight promise or preparation oracle.

### O22 — MINOR: the resubmitted problem has unused and contradictory inputs

- **Location:** D-betti-estimation-problem, lines 578–590.
- **Computation:** Thresholds \(a<b\) are supplied but neither output uses them; additive error \(\epsilon\) is used but is not listed as input. P1 is declared applicable only to whole-table enumeration, yet `GAPPED-BETTI` is stated under P1–P4.
- **FIX DEMAND:** Remove \(a,b\) or define a threshold problem, add \(\epsilon\) to estimation input, and remove P1 from the single-block decision promises.
- **SURVIVING STATEMENT:** Regularity is optional metadata for enumerating the whole Betti table and is unnecessary for a requested block.

## Proposed rows decision

| Proposed row | Decision |
|---|---|
| **C-NEW-KB-HODGE** | **ACCEPT AS CONJECTURE.** The repaired text matches the round-1 rewording. |
| **C-NEW-KB-FREE** | **ACCEPT AS CONJECTURE.** The finite-particle qualification and explicit \(X\) identity are present. |
| **C-NEW-KB-SUPPORT** | **ACCEPT AS CONJECTURE.** The index is correctly \(N=j-i\). |
| **C-NEW-KB-HOCHSTER** | **ACCEPT AS CONJECTURE.** It is expressly limited to squarefree multidegree summands. |
| **C-NEW-KB-QMA1** | **HOLD.** Missing step: a polynomial reduction preserving the total-block normalized gap across all non-squarefree summands. |
| **C-NEW-KB-DEQUANT** | **ACCEPT AS REFUTED.** Surviving statements: “At constant normalized gap and constant additive error, the cited simplicial-complex estimator is polynomial-time classical” and “Apers et al. directly apply to the squarefree multidegree summands explicitly identified with ordinary simplicial Laplacians.” |
| **C-NEW-KB-GAP-INDEPENDENT** | **HOLD.** Missing steps: a total-block counterfamily, a specified positive class of forbidden lower bounds, and any reverse-direction result. |
| **C-NEW-KB-FRACTION** | **ACCEPT AS CONJECTURE.** The row itself is correct; O19 concerns only the accompanying numerical table. |
| **C-NEW-KB-SEED-IS-A-BLOCK** | **ACCEPT AS CONJECTURE.** Part F verifies \(L^{\rm gen}_{i=0}=H_N\) exactly for \(N=2,\ldots,5\), and the higher nullities differ. |
| **C-NEW-KB-NO-FREE-LUNCH** | **ACCEPT AS REFUTED.** Surviving statement: “If the only available quotient access is obtained by QSVT from \(H_N\), constructing a call to \(L_W\) inherits dependence on \(\alpha_{\mathrm{BE}}/\Delta_N\), with the required adjacent-degree gaps included.” |

## Proposed definitions decision

| Definition | Decision |
|---|---|
| **D-fermionic-modes** | **ACCEPT** |
| **D-koszul-supercharge** | **ACCEPT** |
| **D-betti-laplacian** | **ACCEPT** |
| **D-graded-betti-number** | **ACCEPT** |
| **D-betti-gap** | **REWORD — use D5 below** |
| **D-normalised-betti-fraction** | **REWORD — use D6 below** |
| **D-generator-koszul-supercharge** | **ACCEPT** |
| **D-betti-estimation-problem** | **REWORD — use D8 below** |

### Exact definition rewordings

**D5 — D-betti-gap**

> For a block for which \(L_W|_{(i,N)}\) has at least one positive eigenvalue, let
> \(g_{i,N}=\lambda_{\min}^{>0}(L_W|_{(i,N)})\), with normalized gap
> \(g_{i,N}/(N+i)\). On a fixed \(j=N+i\) sector,
> \(g_{i,N}=j-\lambda_{\max}^{<j}(XX^\dagger)\). The gap is an invariant of the
> ideal and the Fock metric; only its realization through \(H_N\) is
> presentation-dependent. The \(m\)-cycle family rules out a uniformly positive
> lower bound depending only on \(\Delta_2\) for the selected squarefree summand
> when \(\phi(1)>0\); it establishes neither a total-block comparison nor a
> reverse inequality. The gap is undefined when the block has no positive
> spectrum.

**D6 — D-normalised-betti-fraction**

> Let \(M_N=\dim R_N\), \(h_N=\mathrm{HF}_{R/I}(N)\), and
> \(b=\binom{n+1}{i}\). The ambient normalized Betti fraction is
> \(\beta_{i,i+N}/(M_Nb)\). It equals the normalized trace of the harmonic
> projector on \(W_N\otimes\Lambda^i\) extended by zero to
> \(R_N\otimes\Lambda^i\); it is not the zero-eigenvalue fraction of \(L_W\)
> extended by zero. When \(h_N>0\), the conditional fraction is
> \(\beta_{i,i+N}/(h_Nb)\). Estimating the conditional ratio requires normalized
> access to \(W_N\), with ambient acceptance weight \(h_N/M_N\), or an explicit
> preparation oracle.

**D8 — D-betti-estimation-problem**

> Input consists of homogeneous \(f_1,\ldots,f_d\) in \(n+1\) variables with
> polynomially many monomials and polynomial-bit coefficients; \(i,N\) in unary;
> an additive error \(\epsilon>0\); and one access mode. Generator mode supplies
> block-encoding or sparse-row access to \(H_N\) and \(H_{N+1}\), including their
> normalization bounds. Quotient mode supplies the adjacent quotient spaces and
> compressed maps \(Z_{k,N}:W_{N-1}\to W_N\) and
> \(Z_{k,N+1}:W_N\to W_{N+1}\). Promise that \(L_W|_{(i,N)}\) has positive
> spectrum and \(g_{i,N}/(N+i)\ge1/\mathrm{poly}(n)\). In generator mode, promise
> \(\Delta_r/\alpha_r\ge1/\mathrm{poly}(n)\) for every nontrivial required
> projector \(r\in\{N,N+1\}\). For conditional output, also promise \(h_N>0\)
> and \(h_N/M_N\ge1/\mathrm{poly}(n)\), or supply an efficient normalized
> \(W_N\)-state preparation oracle. `NORM-BETTI-AMB` estimates
> \(\beta_{i,i+N}/(M_N\binom{n+1}{i})\) by filtering
> \(\widetilde L_{i,N}=L_W+(N+i)(1-\widehat P_N)\).
> `NORM-BETTI-COND` estimates
> \(\beta_{i,i+N}/(h_N\binom{n+1}{i})\). `GAPPED-BETTI` decides
> \(\beta_{i,i+N}=0\) versus \(\beta_{i,i+N}\ge1\) under the spectral and access
> promises. A supplied bound on \(\operatorname{reg}(R/I)\) is optional and is
> used only when enumerating the whole table.

**LOCKSTEP:** NO — §3 and K-KB11 repeat the false every-square-system claim; K-KB6 and D-betti-gap assert an unqualified comparison that C-NEW-KB-GAP-INDEPENDENT correctly leaves on HOLD; and Step 9/D-betti-estimation omit adjacent-degree access. K-KB12, which is also present, does agree with the QMA\(_1\) HOLD.

VERDICT: FAIL(O17, O18, O20, O21)