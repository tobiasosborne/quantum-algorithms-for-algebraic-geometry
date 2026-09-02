# Adversarial critic verdict: `scouting/koszul-betti.md`, round 1

- **Target:** `scouting/koszul-betti.md`
- **Date:** 2026-09-02
- **Critic model:** OpenAI Codex, GPT-5 family
- **Files read:** `CLAUDE.md`; `PRD.md` §2 and arm B; `definitions/definitions.md`; `claims/CLAIMS.md` §2, §5, §6, and “Critical claims for the north star”; `scouting/koszul-betti.md`; `checkers/explore/koszul_laplacian.py`; `checkers/bf.py`; `checkers/ideals.py`; `checkers/README.md`; `checkers/MUTATIONS.md`; `briefs/lane-koszul-betti.md`; `scouting/classical-landscape.md` §10; `scouting/applications-wide-net.md` filters F1–F6 and shortlist 2.
- **Commands run:**

| Command | Exit |
|---|---:|
| `bd prime` | 0 |
| `sed`, `nl`, and `rg` inspections listed above | 0 |
| `cd checkers && timeout 900 python3 explore/koszul_laplacian.py` | 0 |
| Independent exact SymPy computation of quotient duals, Koszul ranks, and harmonic nullities for the twisted cubic and `(z0^2,z1^2)` | 0 |
| Independent exact SymPy computation of the corresponding Fock-Hilbert Laplacian spectra | 0 |
| In-memory mutation M2, replacing `beta_{i,i+N}` by `beta_{i,N}` | 1, expected red |
| In-memory mutation M3, deleting the fermionic signs | 1, expected red |
| In-memory fixture mutation dropping `z1^2` from the second monomial example on both comparison paths | 0, unexpectedly green |
| Dependency-ID audit with `rg` | 0 |

- **Mutated copies under `/tmp`:** NOT RUN because the sandbox was declared read-only. Equivalent in-memory mutations were executed without modifying repository files.
- **Literature access:** Primary arXiv and publisher records were fetched successfully; these were web fetches rather than shell commands.

## O1 — MAJOR: the problem statement uses the wrong regularity index

- **Location:** `scouting/koszul-betti.md` §3.1, lines 263–270; K-KB10, lines 417–420; D-betti-estimation-problem, lines 457–458.
- **Independent computation:** The block labels obey \(j=N+i\), so regularity gives \(N=j-i\leq\operatorname{reg}(R/I)\), not \(j\leq\operatorname{reg}(R/I)\). The memo’s own twisted-cubic example has \(\operatorname{reg}(R/I)=1\) and \(\beta_{2,3}=2\): here \(j=3>1\), while \(j-i=N=1\). Thus `NORM-BETTI` as written excludes a flagship positive block. Likewise, the two-quadric complete intersection has \(\operatorname{reg}(R/I)=2\) and \(\beta_{2,4}=1\), contradicting `j <= reg`. The text also alternates between `reg(I)` and `reg(R/I)`, which generally differ by one for a nonzero proper homogeneous ideal. Supplying regularity is unnecessary for a single requested entry; it is needed only as a bound when enumerating the whole table. The fraction is undefined when \(\mathrm{HF}(N)=0\), and \(g_{i,N}\) is undefined if the block has no nonzero eigenvalue.
- **FIX DEMAND:** Replace every `j <= reg` by `N=j-i <= reg(R/I)`, distinguish `reg(I)` from `reg(R/I)`, require `HF(N)>0` for the normalized fraction, and require a nonzero spectral complement when promising \(g_{i,N}\).
- **SURVIVING STATEMENT:** \(\beta_{i,j}(R/I)=0\) whenever \(j-i>\operatorname{reg}(R/I)\).

## O2 — FATAL: the quantum runtime omits the ground-space weight needed to normalize by `HF`

- **Location:** Step 9.1, lines 131–141; §3.3, lines 288–292; trap audit, lines 337–341; C-NEW-KB-NO-FREE-LUNCH, lines 555–560.
- **Independent computation:** Let \(M_N=\dim R_N\), \(h_N=\mathrm{HF}_{R/I}(N)\), and \(b=\binom{n+1}{i}\). A maximally mixed state on the ambient block yields zero-mode probability
  \[
  \frac{\beta_{i,j}}{M_N b},
  \]
  not the claimed
  \[
  \frac{\beta_{i,j}}{h_N b}.
  \]
  The latter is a conditional probability inside \(W_N\). It requires either preparing \(P_{0,N}/h_N\), which succeeds from the ambient mixed state with weight \(h_N/M_N\), or estimating two ambient-normalized traces and dividing by \(h_N/M_N\). The stated complexity contains neither an \(M_N/h_N\) sampling factor nor a \(\sqrt{M_N/h_N}\) coherent-projection factor, despite C-096 explicitly identifying this cost. Consequently the claimed polynomial quantum algorithm is not established when \(h_N/M_N\) is exponentially small.
- **FIX DEMAND:** Add the promise \(h_N/M_N\geq1/\mathrm{poly}(n)\), assume an explicit efficient preparation oracle for \(P_{0,N}/h_N\), or change the output to the ambient-normalized quantity \(\beta_{i,j}/(M_N\binom{n+1}{i})\) and recalculate all runtimes.
- **SURVIVING STATEMENT:** Conditional on efficient normalized access to \(W_N\), phase filtering of \(L_W\) estimates \(\beta_{i,j}/(h_N\binom{n+1}{i})\).

## O3 — MAJOR: the dequantization conclusion does not follow from the quoted runtime

- **Location:** §3.4(a), lines 294–305; K-KB3, lines 377–382; C-NEW-KB-DEQUANT, lines 516–526.
- **Independent computation:** The cited Apers–Gribling–Sen–Szabó bound is
  \[
  n^{O(\gamma^{-1/2}\log(1/\epsilon))}.
  \]
  At constant \(\gamma\) and constant \(\epsilon\), this is polynomial. At the memo’s required \(\epsilon=1/\mathrm{poly}(n)\), however, it is \(n^{O(\log n)}\), which is quasi-polynomial and still permits a super-polynomial separation from a polynomial quantum algorithm. Therefore “no super-polynomial quantum advantage exists at \(\gamma=\Omega(1)\)” and “the only surviving window is \(\gamma=1/\mathrm{poly}(n)\)” are false as stated.
- **FIX DEMAND:** Restrict the no-super-polynomial-advantage conclusion to constant additive precision, and call the constant-gap, inverse-polynomial-precision regime unresolved by this bound.
- **SURVIVING STATEMENT:** At constant normalized gap and constant additive error, the cited simplicial-complex estimator is polynomial-time classical.

## O4 — MAJOR: the Apers theorem is applied outside its established access model

- **Location:** §3.2, lines 279–286; §3.4(a), lines 294–305; C-NEW-KB-DEQUANT, lines 516–526.
- **Independent computation:** Apers et al. prove their stated bound for combinatorial Laplacians of simplicial complexes, exploiting their row structure and bounded path-integral weights. A generic \(L_W\) contains the generally dense projector \(P_0\). A quantum block encoding obtained through QSVT is not a classical sparse-row oracle. The memo simply assumes “sparse access to \(L_W\)” without constructing it from the generator input. Even for Stanley–Reisner ideals, the total-degree block includes nonsquarefree multidegrees in addition to the squarefree induced-complex summands.
- **FIX DEMAND:** Restrict the cited dequantization theorem to directly accessible simplicial Laplacians or prove a separate path-integral variance and row-oracle theorem for the projected \(L_W\).
- **SURVIVING STATEMENT:** Apers et al. directly apply to the squarefree multidegree summands that are explicitly identified with ordinary simplicial Laplacians.

## O5 — MAJOR: the QMA-hardness reduction does not preserve this memo’s gap promise

- **Location:** §3.4(d), lines 317–326; K-KB3, lines 377–382; C-NEW-KB-QMA1, lines 505–514.
- **Independent computation:** King–Kohler’s gapped result is for weighted clique complexes. C1’s Fock metric gives the unweighted squarefree block, and the memo supplies no encoding of arbitrary vertex-product weights. The 2026 Hayakawa result establishes an unweighted gapped theorem, but for one clique-complex Laplacian. In contrast, \(g_{i,N}\) here is the smallest positive eigenvalue of the entire total-degree block, hence the minimum over the desired squarefree multidegree and all other multidegrees. A promise on the target clique Laplacian does not bound those extra summands. Hochster’s formula preserves nullity, not this global spectral gap. QMA-hardness also rules out a BQP algorithm only conditionally, unless \(\mathrm{QMA}_1\subseteq\mathrm{BQP}\).
- **FIX DEMAND:** State hardness for the selected squarefree multidegree block, citing the unweighted gapped theorem, or prove an inverse-polynomial lower bound for every additional multidegree introduced by the total-degree reduction.
- **SURVIVING STATEMENT:** Exact \(\beta_{i,j}\) evaluation is #P-hard and multiplicative approximation is NP-hard; unweighted gapped clique homology transfers to a squarefree multidegree version of the Betti-Laplacian problem.

## O6 — MAJOR: the favorable-fraction argument occupies the classically small regime

- **Location:** §2(e), lines 241–257; §3.4(b), lines 306–311; trap audit, lines 337–341; C-NEW-KB-FRACTION, lines 535–543.
- **Independent computation:** For the Boolean complete intersection \(c=n\),
  \[
  \mathrm{HF}(i)=\sum_{r=0}^{i}\binom nr,\qquad
  \beta_{i,2i}=\binom ni.
  \]
  At fixed \(i\), both \(\mathrm{HF}(i)\binom{n+1}{i}\) and \(\beta_{i,2i}\) are polynomial in \(n\), so there is no exponential state-space compression. If \(i=\rho n\), the chain dimension and Betti number can both be exponential, but the normalized fraction is exponentially small; at \(i=n\) it is exactly \(1/(2^n(n+1))\). Thus the memo has not exhibited a regime simultaneously having exponential chain dimension and polynomially visible normalized fraction. The blanket \(n^{-2i}\) asymptotic assumes fixed \(i\) and effectively fixed \(c\); for \(c=n\) and fixed \(i\) the fraction scales as \(i!n^{-i}\).
- **FIX DEMAND:** State the asymptotic regimes for \(c\) and \(i\) explicitly and remove the claim that the fraction by itself escapes the compression/overlap obstruction.
- **SURVIVING STATEMENT:** The exact fraction is \(\binom ci/(\mathrm{HF}(i)\binom{n+1}{i})\), and it is inverse-polynomial when \(i\) is fixed.

## O7 — MAJOR: the gap-independence row is unproved, and its definition contradicts the construction

- **Location:** Step 5.4, lines 93–99; Step 9.2, lines 138–141; D-betti-gap, lines 448–450; C-NEW-KB-GAP-INDEPENDENT, lines 528–533.
- **Independent computation:** Since
  \[
  L_W=L_W(I)
  \]
  is built solely from \(P_{I_N^\perp}\), the fixed annihilation operators, and the Fock metric, \(g_{i,N}\) is an invariant of the ideal and the chosen metric. It is not presentation-dependent. Only the cost of manufacturing \(P_0\) through \(H_N\), including \(\Delta_N\) and \(\alpha_{\mathrm{BE}}\), depends on the generating tuple. The two finite numerical examples do not prove that no function relates the gaps. There are promising actual families: cycle ideals have \(\Delta_2=1\) while the displayed top-block gap follows \(2-2\cos(2\pi/m)\to0\), and the fixed monomial example has \(\Delta_N=1\) while some \(g_{i,N}\) grow. Those infinite-family formulas still need proof and a precise meaning of “bounded by a function.”
- **FIX DEMAND:** Define \(g_{i,N}\) as ideal- and metric-dependent, and replace the universal no-function assertion by explicit proved counterfamilies to specified inequalities.
- **SURVIVING STATEMENT:** No comparison between \(g_{i,N}\) and the tuple-dependent \(\Delta_N\) follows from the construction; the reported finite spectra show markedly different behavior.

## O8 — MAJOR: adjacent Koszul blocks do not have identical nonzero spectra

- **Location:** Step 5.3, lines 96–97; §2(c), line 212.
- **Independent computation:** For a differential \(q_i:C^i\to C^{i+1}\),
  \[
  L_i=q_i^\dagger q_i+q_{i-1}q_{i-1}^\dagger.
  \]
  Only the \(q_i^\dagger q_i\) part shares its nonzero spectrum with \(q_iq_i^\dagger\) in the adjacent block. The complete spectrum of \(L_i\) is the multiset union of contributions from \(q_i\) and \(q_{i-1}\); it need not equal that of \(L_{i+1}\). The script itself refutes the sentence: for the twisted cubic at internal degree \(j=3\), block \((0,3)\) has gap \(3\), while adjacent block \((1,2)\) has gap \(4/3\). Supersymmetry pairs the aggregate positive spectra of the even and odd sectors, not every adjacent pair.
- **FIX DEMAND:** Replace Step 5.3 by the singular-value pairing for each individual differential and, if desired, the global even/odd spectral pairing.
- **SURVIVING STATEMENT:** Nonzero singular values of \(q_i\) occur in both \(q_i^\dagger q_i\) and \(q_iq_i^\dagger\).

## O9 — MAJOR: `Syz / m Syz` gives \(\beta_2\) only for a minimal presentation

- **Location:** Step 7.2, lines 111–120; D-graded-betti-number, lines 444–447.
- **Independent counterexample:** Let \(I=(x)\) but supply the redundant tuple \((x,x)\). Its tuple syzygy module contains the constant relation \((1,-1)\), which survives modulo \(\mathfrak m\operatorname{Syz}\). Nevertheless the minimal resolution of \(R/(x)\) is \(0\to R(-1)\to R\), so \(\beta_{2,*}(R/I)=0\). The asserted equality therefore fails under the memo’s arbitrary-generator assumptions.
- **FIX DEMAND:** Say that \(\beta_{2,j}\) is the degree-\(j\) number of first syzygies in a minimal free resolution, or impose a minimal homogeneous generating set before quotienting its syzygy module by \(\mathfrak m\).
- **SURVIVING STATEMENT:** \(\beta_{1,j}(R/I)\) counts minimal generators of \(I\) in degree \(j\), and \(\beta_{2,j}\) counts minimal relations among a minimal presentation.

## O10 — MINOR: the duality is conjugate-linear, and full-Fock operator domains are suppressed

- **Location:** Step 3.2, lines 65–70; Step 4.1–4.2, lines 77–81; C-NEW-KB-FREE, lines 479–485.
- **Independent computation:** Under C1, \(\langle u,h\rangle\) is conjugate-linear in \(u\), so \(u\mapsto([h]\mapsto\langle u,h\rangle)\) is an anti-linear isomorphism \(W_N\to(R/I)_N^*\), not the stated linear identification. The relation is the Hermitian/conjugate dual of the Koszul differential, not literally a complex-linear transpose. Also \(a_k\), \(Q\), and \(L\) are unbounded on completed Fock space; the algebraic identities hold first on the finite-particle core and then for the appropriate closures. Neither issue changes finite-block nullities.
- **FIX DEMAND:** Write “conjugate-linear dual/Hilbert adjoint” and state the full-Fock identities on the finite-particle core with closures understood.
- **SURVIVING STATEMENT:** The restricted cohomology is anti-linearly dual to Koszul homology and therefore has the same dimension.

## O11 — MAJOR: “every evaluation requires \(P_0\)” is false and the cost is mislabeled

- **Location:** §3.3, lines 288–292; K-KB2, lines 371–375; C-NEW-KB-NO-FREE-LUNCH, lines 555–560.
- **Independent counterexample:** For a monomial ideal, the standard-monomial basis and membership predicate give the compressed differentiation and multiplication maps directly. The memo itself uses exactly this fact to call \(L_W\) an honest sparse hopping Hamiltonian. Such an implementation need not invoke a QSVT ground-space projector on each application. More generally, a supplied quotient-multiplication oracle also bypasses \(H_N\). In addition, \(j/g\) is the number of spectral-filtering applications, not the cost “per application” of \(L_W\).
- **FIX DEMAND:** Make the cost statement conditional on the generator-only/Hamiltonian-oracle implementation, separate per-call cost from filtering repetitions, and include the normalization cost from O2.
- **SURVIVING STATEMENT:** If the only available quotient access is obtained by QSVT from \(H_N\), constructing a call to \(L_W\) inherits dependence on \(\alpha_{\mathrm{BE}}/\Delta_N\).

## O12 — MINOR: the checker passes, but its advertised mutation coverage and independence are overstated

- **Location:** `checkers/explore/koszul_laplacian.py` lines 41–61, 321–344, 375–381; `scouting/koszul-betti.md` lines 147–161.
- **Independent computation:** The required script exited 0. An independent rational/SymPy construction gave:

| Ideal | Exact nonzero harmonic blocks |
|---|---|
| Twisted cubic | \((0,0):1,\ (1,2):3,\ (2,3):2\) |
| CI \((z_0^2,z_1^2)\subset\mathbb C[z_0,\ldots,z_3]\) | \((0,0):1,\ (1,2):2,\ (2,4):1\) |

  For the twisted cubic, the exact characteristic polynomials include
  \[
  \chi_{(1,1)}(\lambda)=\lambda^3(\lambda-2)^{13},
  \]
  and the \((2,1)\) block has nullity two and smallest positive eigenvalue \(4/3\), matching the printed table. For the monomial CI,
  \[
  \chi_{(1,1)}=\lambda^2(\lambda-2)^{14},\qquad
  \chi_{(2,2)}=\lambda(\lambda-4)^{31}(\lambda-2)^{16}.
  \]
  M2 and M3 both turned the script red with exit 1. Conversely, dropping `z1^2` from the unchecked monomial fixture on both the Fock and GF(p) paths exited 0: the script verified the new ideal against itself because no closed-form fixture table was asserted. M4 is explicitly untested and none of these mutations is recorded in `checkers/MUTATIONS.md`. The printed \(XX^\dagger\) identity is tautological because the code defines `XXd = (N+i)I-Lw` instead of constructing \(X\). Finally, `ev < TOL` counts every negative eigenvalue as a zero mode; it should test `abs(ev) < TOL` and separately test positivity. GF(\(p\)) ranks are exact in that characteristic, not automatically over \(\mathbb C\), although the audited examples are characteristic-independent.
- **FIX DEMAND:** Add independently asserted fixture Betti tables, construct \(X\) directly, test PSD separately, use absolute nullity thresholds, run and register M1–M4 in `MUTATIONS.md`, and label GF(\(p\)) results by characteristic.
- **SURVIVING STATEMENT:** The unmutated script exits 0, M2/M3 are red, and its tested characteristic-independent examples agree with the independent exact computation.

## O13 — MAJOR: lockstep and dependency discipline fail despite correct row statuses

- **Location:** bottom line, lines 14–25; K-KB3/K-KB4, lines 377–388; proposed rows, lines 462–560.
- **Independent audit:** All ten proposed rows are labeled CONJECTURE, as L1 requires. No proposed row relies on an existing REFUTED C-row; checked, holds. However, the prose calls the construction a “theorem,” calls the TDA debate “settled,” and presents QMA-hardness as a completed product while the corresponding rows remain conjectural and the reduction has the gap defect in O5. None of `D-koszul-supercharge`, `D-betti-laplacian`, `D-graded-betti-number`, `D-betti-gap`, `D-normalised-betti-fraction`, or `D-generator-koszul-supercharge` currently exists as a registered heading in `definitions/definitions.md`. Likewise no `C-NEW-KB-*` dependency exists yet in `claims/CLAIMS.md`; merge ordering must assign real IDs first. Existing cited IDs C-008, C-012, C-014, C-052, C-055, C-056, C-058, C-062, C-091, C-092, C-100 and the existing D-ids were found. Lines 98 and 396 misidentify Fact 7.1 as C-107; it is C-103.
- **FIX DEMAND:** Keep all conclusions explicitly conjectural, merge corrected D-entries before C-rows, replace provisional dependencies by assigned IDs, and change the Fact 7.1 citation from C-107 to C-103.
- **SURVIVING STATEMENT:** The proposed row statuses themselves obey the ratchet, and no REFUTED claim is used as an antecedent.

## O14 — MAJOR: none of PRD §2 criteria 1–5 is met

- **Location:** `scouting/koszul-betti.md` §3, lines 261–358.
- **Independent audit:**

| Criterion | Adjudication |
|---|---|
| 1. Problem | Fails as written because `j <= reg` is wrong, zero denominators and undefined gaps are unhandled, and the access model for \(L_W\) is not specified. |
| 2. Classical baseline | Names relevant methods, but does not establish which is best under the same oracle model or give a full complexity comparison in \(n,N,i,\epsilon,\Delta,g,\mathrm{HF}/M_N\). The practical `n=10..40` and syzygy counts are not tied to a sourced benchmark for this task. |
| 3. Quantum algorithm | Fails because the \(W_N\)-state preparation/normalization cost is absent; no proven advantage margin exists. |
| 4. Dequantization audit | Fails because O3 and O4 invalidate its main conclusion. |
| 5. Heuristic attack | At most a small monomial demonstration. One photon in four modes is a four-mode path/ququart encoding, not a dual-rail encoding; the generic problem still needs a nonphysical projector. |

  The sharpest single killer is O2: without normalized access to \(W_N\), the claimed output is not the trace that the proposed circuit estimates, and the missing factor can be exponential.
- **FIX DEMAND:** Recast the memo as a conditional dictionary theorem plus hardness probe, with no north-star algorithm claim until the \(W_N\) preparation and common-oracle baseline are supplied.
- **SURVIVING STATEMENT:** The construction offers a mathematically meaningful Betti-Laplacian representation and a possible small monomial-ideal demonstration, not a demonstrated speedup.

## O15 — NOTE: core finite-dimensional mathematics checked, holds

- **Location:** Steps 1–4 and 6, lines 41–109.
- **Independent computation:** If \(u\in I_N^\perp\) and \(h\in I_{N-1}\), then
  \[
  \langle a_ku,h\rangle=\langle u,z_kh\rangle=0,
  \]
  so \(a_kI_N^\perp\subseteq I_{N-1}^\perp\), with no radicality, saturation, genericity, or stable-range assumption. Further,
  \[
  Q^2=\tfrac12\sum_{k,l}a_ka_l\{c_k^\dagger,c_l^\dagger\}=0.
  \]
  With \((K_i)_j=(R/I)_{j-i}\otimes\Lambda^i\), block \(W_N\otimes\Lambda^i\) has \(j=N+i\) and is the conjugate dual of that Koszul chain group, giving
  \[
  \dim\ker L_W|_{(i,N)}=\beta_{i,N+i}(R/I).
  \]
  On the finite-particle core,
  \[
  QQ^\dagger+Q^\dagger Q=\hat N+\hat F,
  \]
  so the full complex is exact except for the vacuum. With \(P=\bigoplus_NP_{0,N}\) and \(X=PQ(1-P)\),
  \[
  L_W=jP-XX^\dagger,\qquad 0\le L_W\le jP.
  \]
  Hence \(\|L_W\|\le N+i\). The twisted-cubic and complete-intersection computations above confirm the exact index convention. Radical, saturated, and generic hypotheses are unnecessary for these statements.
- **FIX DEMAND:** Retain these claims after applying the conjugate-dual and operator-domain corrections in O10.
- **SURVIVING STATEMENT:** The Hodge/nullity identity, full-Fock number-operator identity, support bound, and norm bound all hold in the corrected formulation.

## O16 — NOTE: bibliographic identifiers hold; theorem applications do not all hold

- **Location:** §3.4, lines 294–336; K-KB3/K-KB4, lines 377–388; C-NEW-KB-QMA1 and C-NEW-KB-DEQUANT.
- **Independent literature audit:**

  - Lloyd–Garnerone–Zanardi, [arXiv:1408.3106](https://arxiv.org/abs/1408.3106), is correctly identified; the arXiv title includes “big data,” and it estimates Betti numbers and combinatorial-Laplacian spectral data.
  - Apers–Gribling–Sen–Szabó, [arXiv:2211.09618](https://arxiv.org/abs/2211.09618), gives the quoted \(n^{O(\gamma^{-1/2}\log(1/\epsilon))}\) normalized-Betti estimator for simplicial complexes. O3–O4 describe the invalid extrapolations.
  - Berry et al., [arXiv:2209.13581](https://arxiv.org/abs/2209.13581), do state that super-quadratic advantage requires multiplicative error with growing Betti number, and that exponentially large chain dimension and Betti number are necessary but insufficient for super-polynomial advantage.
  - Schmidhuber–Lloyd, [arXiv:2209.14286](https://arxiv.org/abs/2209.14286), prove exact Betti computation #P-hard and multiplicative approximation NP-hard, including clique-dense regimes.
  - Crichigno–Kohler, [arXiv:2209.11793](https://arxiv.org/abs/2209.11793), prove unweighted clique homology QMA\(_1\)-hard, but this source alone does not establish the memo’s total-block gapped problem.
  - King–Kohler, [arXiv:2311.17234](https://arxiv.org/abs/2311.17234), prove the gapped result for weighted graphs. Hayakawa, [arXiv:2608.02726](https://arxiv.org/abs/2608.02726), supplies the newer unweighted gapped result in the stated restricted gate-set class. O5 remains because the total-degree \(g_{i,N}\) promise is stronger.
  - Gyurik–Cade–Dunjko, [arXiv:2005.02607](https://arxiv.org/abs/2005.02607), concern DQC1-hardness of low-lying spectral density, not normalized Betti estimation for clique complexes. The memo’s correction is accurate.
  - Cade–Crichigno, [arXiv:2107.00011](https://arxiv.org/abs/2107.00011), already establish the SUSY/cohomology Hamiltonian framework and DQC1-hardness for normalized Betti estimation on general cochain complexes, confirming the novelty caution.

- **FIX DEMAND:** Preserve the identifiers but rewrite the dequantization and QMA-transfer claims to match the exact access models, gaps, weights, and complexity assumptions of the cited theorems.
- **SURVIVING STATEMENT:** The cited identifiers and the memo’s Gyurik–Cade–Dunjko correction are accurate.

## Proposed rows adjudication

| Proposed row | Adjudication |
|---|---|
| **C-NEW-KB-HODGE** | **ACCEPT WITH REWORDING:** “For every homogeneous ideal \(I\subseteq R\), let \(W_N=I_N^\perp\), \(W=\bigoplus_NW_N\), \(P=\bigoplus_NP_{0,N}\), and \(q=QP=PQP\) on the finite-degree subspace. For \(0\le i\le n+1\), \(N\ge0\), and \(j=N+i\), \(\dim\ker(qq^\dagger+q^\dagger q)|_{W_N\otimes\Lambda^i}=\beta_{i,j}(R/I)\). Under the Fock pairing this harmonic space is conjugate-linearly dual to \(H_i(K(z;R/I))_j\).” |
| **C-NEW-KB-FREE** | **ACCEPT WITH REWORDING:** “On the finite-particle core, \(QQ^\dagger+Q^\dagger Q=\hat N+\hat F\). For every homogeneous \(I\), every \(i,N\), and \(j=N+i\), \(PLP=jP\), while \(L_W=jP-PQ(1-P)Q^\dagger P\); hence \(0\le L_W\le jP\) and \(\|L_W\|\le j\).” |
| **C-NEW-KB-SUPPORT** | **ACCEPT WITH REWORDING:** “For every homogeneous proper ideal \(I\), \(\beta_{i,j}(R/I)=0\) when \(j-i>\operatorname{reg}(R/I)\); equivalently the block \((i,N)\) has zero harmonic nullity for \(N>\operatorname{reg}(R/I)\). This does not preclude large \(N\) when regularity itself grows.” |
| **C-NEW-KB-HOCHSTER** | **ACCEPT WITH REWORDING:** “For a Stanley–Reisner ideal, the squarefree multidegree-\(\sigma\) summand of \(L_W\) in block \(i,N\), \(|\sigma|=i+N\), is unitarily the reduced \((N-1)\)-chain Laplacian of \(\Delta|_\sigma\). Consequently \(\beta_{i,i+N}=\sum_{|\sigma|=i+N}\dim\widetilde H_{N-1}(\Delta|_\sigma;\mathbb C)\). No total-block gap or dequantization conclusion is included.” |
| **C-NEW-KB-QMA1** | **HOLD:** A polynomial reduction preserving the memo’s total-block normalized gap is missing. Weighted King–Kohler does not directly match C1, and the unweighted result controls the selected clique Laplacian, not every extra multidegree. |
| **C-NEW-KB-DEQUANT** | **REFUTE:** At \(\gamma=\Omega(1)\), \(\epsilon=1/\mathrm{poly}(n)\), the quoted bound is \(n^{O(\log n)}\), not polynomial, and the theorem does not automatically apply to generic projected \(L_W\). |
| **C-NEW-KB-GAP-INDEPENDENT** | **HOLD:** The finite tables do not prove the no-function assertion. Prove explicit infinite counterfamilies and specify the class of forbidden comparisons. |
| **C-NEW-KB-FRACTION** | **ACCEPT WITH REWORDING:** “For a complete intersection of \(1\le c\le n+1\) quadrics and \(0\le i\le c\), the block \((i,i)\) has \(\beta_{i,2i}=\binom ci\) and fraction \(\binom ci/(\mathrm{HF}(i)\binom{n+1}{i})\). For fixed \(c,i\) and \(n\to\infty\), this is asymptotic to \(\binom ci(i!)^2n^{-2i}\). This scaling alone implies no quantum advantage because the corresponding block dimension is polynomial for fixed \(i\).” |
| **C-NEW-KB-SEED-IS-A-BLOCK** | **ACCEPT WITH REWORDING:** “For positive-degree homogeneous \(f_1,\ldots,f_d\), define \(Q_f=\sum_jM_{f_j}\otimes c_j\) with fermionic annihilators \(c_j\), assigning fermion \(j\) weight \(\deg f_j\). Then \(Q_f^2=0\); its fermion-number-zero Laplacian block is \(\sum_jM_{f_j}M_{f_j}^\dagger=H\). Its zero modes in higher blocks are \(H_i(f;R)\cong\operatorname{Tor}^{\mathbb C[y_1,\ldots,y_d]}_i(\mathbb C,R)\), and all positive homology vanishes iff the positive-degree sequence is regular.” |
| **C-NEW-KB-NO-FREE-LUNCH** | **REFUTE:** Direct standard-monomial or quotient-multiplication access avoids repeated \(P_0\), the stated “per application” cost includes a separate \(j/g\) filtering factor, and the desired normalization omits \(M_N/\mathrm{HF}(N)\). The surviving statement is conditional on generator-only access through \(H_N\). |

## Proposed definitions adjudication

| Definition | Adjudication | Reason |
|---|---|---|
| **D-fermionic-modes** | **ACCEPT** | Correct CAR and sign convention. |
| **D-koszul-supercharge** | **REWORD** | Define the degreewise direct-sum projector, finite-particle domain, and conjugate-dual interpretation. |
| **D-betti-laplacian** | **REWORD** | Define \(L_W\) globally before restricting blocks; state \(P\) and \(X\) on a fixed internal-degree sector and handle blocks with no positive spectrum. |
| **D-graded-betti-number** | **REWORD** | Distinguish \(\operatorname{reg}(R/I)\) from \(\operatorname{reg}(I)\); make the \(\beta_2\)/syzygy statement conditional on a minimal homogeneous presentation. |
| **D-betti-gap** | **REWORD** | Delete “presentation-dependent.” The intrinsic gap is ideal- and metric-dependent; only its realization cost through \(H_N\) is presentation-dependent. |
| **D-normalised-betti-fraction** | **REWORD** | It is a numerical ratio, not automatically a DQC1-style observable. Add \(HF(N)>0\) and the required normalized-\(W_N\) state/access assumption. |
| **D-generator-koszul-supercharge** | **REWORD** | Replace ambiguous `gamma_j` by fermionic annihilators \(c_j\), state positive degrees, weighted grading, domains, and that only zero-mode dimensions compute Koszul homology. |
| **D-betti-estimation-problem** | **REJECT** | It inherits the false `j <= reg` condition, undefined zero denominators/gaps, missing \(W_N\)-preparation promise, and an unconstructed sparse-access model for \(L_W\). |

VERDICT: FAIL(O1, O2, O3, O4, O5, O6, O7, O8, O9, O11, O13, O14)