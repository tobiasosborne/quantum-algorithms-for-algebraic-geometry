# Adversarial verdict: `scouting/intersection-observables.md`

- Date: 2026-09-03
- Critic model: OpenAI Codex (GPT-5)
- Target: `scouting/intersection-observables.md`, round 1 attack
- Files read: `CLAUDE.md`; `PRD.md` §§1–4; requested entries of `definitions/definitions.md`; requested rows and “Critical claims” in `claims/CLAIMS.md`; target memo; `checkers/explore/intersection_observables.py`; `checkers/bf.py`; `briefs/lane-intersection-observables.md`; `scouting/classical-landscape.md` §§5, 8 and lines 540–550; `scouting/applications-wide-net.md` cautions 1–3; relevant `checkers/MUTATIONS.md`/`checkers/README.md` searches.
- Commands run:
  - All `sed`, `nl`, `rg`, `wc`, dependency/status audits: exit 0.
  - `cd checkers && timeout 900 python3 explore/intersection_observables.py`: exit 0, NumPy 2.4.6.
  - Independent SymPy quadrature: exit 0.
  - Independent conic-kernel recurrence through \(N=1200\): exit 0.
  - Independent multiplication-map QR, linear-subspace formulas, and radial Bergman-frame quadrature: exit 0.
  - `timeout 30 bd prime`: exit 0.
  - Mutated copies under `/tmp`: NOT RUN; the sandbox is read-only.
- External checks: Hutch++ arXiv:2010.09649; Sommese–Verschelde–Wampler DOI 10.1137/S0036142903430463; Lairez arXiv:1507.05485.

## O1 — MAJOR — the leading geometry is right, but the advertised Laplace proof omits an entire normal block

**Location:** `scouting/intersection-observables.md:187–233`, especially steps 2.4 and 5.3–5.4; `:447–456`.

For vector subspaces \(U,W\), the exact overlap is
\[
\operatorname{Tr}\!\left(P_{\mathrm{Sym}^NU}P_{\mathrm{Sym}^NW}\right)
=h_N(\sigma_1^2,\ldots,\sigma_r^2),
\]
where \(\sigma_i\) are the one-particle principal cosines.

Thus the three requested cases are exact:

1. Two projective lines in \(\mathbb P^2\), meeting at one point, have principal cosines \(1,c\):
   \[
   T_N=\sum_{a=0}^N c^{2a}
   =\frac{1-c^{2N+2}}{1-c^2}
   \longrightarrow \csc^2t.
   \]
   The exponent is \(0=\dim(V\cap W)\).

2. The Clifford skew-line pair in \(\mathbb P^3\) has principal cosines \(c,c\):
   \[
   T_N=(N+1)c^{2N}.
   \]
   This verifies exponential rate \(\cos^{2N}t\), with a polynomial prefactor.

   For the memo’s generic skew pair, the principal cosines are independently
   \[
   \sigma_1=0.954282512625,\qquad \sigma_2=0.909838680515,
   \]
   and
   \[
   T_N=\frac{\sigma_1^{2N+2}-\sigma_2^{2N+2}}
              {\sigma_1^2-\sigma_2^2}.
   \]
   Hence \(T_N/\sigma_1^{2N}\to10.9917866070\), not the \(8.81988\) value at \(N=16\). The printed numbers are correct, but “saturating” at `:105` is false; at \(N=100\) the ratio is \(10.99107\).

3. Two planes in \(\mathbb P^3\), meeting in a line, have principal cosines \(1,1,c\):
   \[
   T_N=\sum_{a=0}^N c^{2a}(N+1-a)
   =\frac{N+1-(N+2)c^2+c^{2N+4}}{(1-c^2)^2}.
   \]
   Therefore
   \[
   T_N=\frac{N+1}{\sin^2t}-\frac{\cos^2t}{\sin^4t}
       +O(\cos^{2N}t),
   \]
   and the exponent is \(1=\dim(V\cap W)\).

The memo’s final clean-intersection constant is consistent with these exact cases:
\[
c=\pi^{-l}\int_Z\prod_i\sin^{-2}\theta_i\,d\mathrm{vol}_Z.
\]

But step 5.4 does not derive it. If
\[
T_xV=T_xZ\oplus A,\qquad T_xW=T_xZ\oplus B,
\]
the normal bundle to the diagonal in \(V\times W\) includes the anti-diagonal common-tangent variable
\[
\delta=t-s\in T_xZ.
\]
The memo integrates only \((a,b)\mapsto a-b\), whose complex dimension is \(k_1+k_2-2l\), while claiming the factor for dimension \(k_1+k_2-l\). The missing integral is
\[
\int_{\mathbb C^l}e^{-N|\delta|^2}\,d\delta=(\pi/N)^l.
\]
The transverse map contributes
\[
(\pi/N)^{k_1+k_2-2l}/J(x).
\]
Together they give the stated factor
\[
(\pi/N)^{k_1+k_2-l}/J(x).
\]

Step 2.4 also remains an unproved applicability claim: mean eigenvalue flatness does not prove operator-norm flatness. The numerical N10 table supports it but cannot replace the missing ambient-restriction Bergman theorem.

**Table comparison, checked:** N1 exact values \(1.412261181\), \(1.412282926\), \(6.594126900\); N2 values \(15.659069083\), \(31.202397980\), \(248.847263188\); N3 slopes follow the same exact sum; N4 values and rates match; N5 independent recurrence matches \(2.0349567937/4.7928590091\), \(2.0117792411/7.1998253299\), \(2.0085524517/8.2051977632\); N6 independent multiplication-map QR matches every sampled entry; N7 is exactly \(N+1\); N8–N10 are addressed below. No raw numerical discrepancy was found apart from floating display rounding in N9.

**FIX DEMAND:** Insert the anti-diagonal \(T_xZ\) Gaussian calculation, prove or precisely cite the ambient Bergman-frame operator-norm estimate, and change “theorem-grade” to “conjectural pending step 2.4.”

**SURVIVING STATEMENT:** The exact linear examples and the corrected Morse–Bott calculation support \(T_N\sim(N/\pi)^l\int_ZJ^{-1}d\mathrm{vol}_Z\) for fixed smooth clean intersections.

## O2 — MAJOR — the tangency row is false at \(m=1\), and the distance law lacks the necessary Morse–Bott hypothesis

**Location:** `scouting/intersection-observables.md:239–256`, `:467–505`, K-IO5 at `:361–365`.

For \(m\ge2\), the local model
\[
d^2=|u-v|^2+|\gamma|^2|u|^{2m}+o(|u-v|^2+|u|^{2m})
\]
does give
\[
(N/\pi)^2
\left(\frac{\pi}{N}\right)
\left[\pi\Gamma(1+1/m)(N|\gamma|^2)^{-1/m}\right]
=
\Gamma(1+1/m)|\gamma|^{-2/m}N^{1-1/m}.
\]
The independent conic recurrence confirms the \(m=2\) data.

The proposed row nevertheless quantifies over \(m\ge1\). For \(m=1\), if \(V\) is the graph \(v=\gamma u\) over \(W=\{v=0\}\), the induced volume on \(V\) contributes \(1+|\gamma|^2\). The constant is
\[
J^{-1}=\frac{1+|\gamma|^2}{|\gamma|^2},
\]
not \(|\gamma|^{-2}\). The formula must be restricted to \(m\ge2\).

The disjoint-distance row is also underhypothesized. The closest-pair set \(S\subset V\times W\) need not be a complex submanifold, so \(\dim_{\mathbb C}S\) may be undefined. If \(S\) is a real Morse–Bott minimum manifold of real dimension \(r\), the prefactor is \(N^{r/2}\). Degenerate minima can have different powers or logarithmic factors.

The sign of the Clifford bias is repeatedly misstated. Exactly,
\[
-\frac{\log T_N}{2N}
=\log\sec t-\frac{\log(N+1)}{2N}.
\]
The memo’s own table shows the estimate below the target. Lines 46–47 and K-IO5 call this a positive bias.

The claimed forced \(N\sim800\) is not an information-theoretic lower bound. For the Clifford family the prefactor is known exactly and can be divided out at every \(N\). The 10% uncorrected-bias threshold is \(N=721\), and at \(N=800\)
\[
T_N=1.42501047\times10^{-29},\qquad
T_N/M_N=1.65747458\times10^{-37},
\]
versus the memo’s approximate \(10^{-29}\) and \(10^{-36}\). The exponentially small normalized signal is real, but the alleged necessity from an uncorrected known bias is not.

**FIX DEMAND:** Restrict tangency to \(m\ge2\); replace \(\dim_{\mathbb C}S\) by \(r/2\) under an explicit real Morse–Bott hypothesis; correct the bias sign and remove the unconditional \(N=\Omega(\eta^{-1}\log(1/\eta))\) claim.

**SURVIVING STATEMENT:** The conic tangent has exponent \(1/2\); the Clifford and generic skew-line families obey their exact closed forms; under a nondegenerate Morse–Bott closest-pair hypothesis the distance rate is \(\log\sec d_0\).

## O3 — FATAL — C-168 is refuted as written, not “confirmed,” and the reported \(1/N\) coefficient is a finite-range fit

**Location:** `scouting/intersection-observables.md:146–161`, `:428–434`, `:507–526`, lockstep `:600–601`; D-toeplitz-operator and C-086/C-168.

The registered definition is
\[
T_g=P_0:g(a^\dagger,a):P_0
\]
with no degree normalization. For \(g=|z_2|^2\), this is \(P_0n_2P_0\), so
\[
\frac{\operatorname{Tr}(P_0T_g)}{\mathrm{HF}(N)}
\sim N\langle |z_2|^2\rangle_V.
\]
It diverges. Therefore C-086 and C-168 are dimensionally false under the definitions on which they depend.

The lane silently tests a different operator,
\[
\widetilde T_g^{(N)}
=\frac{(N-r)!}{N!}P_0:g(a^\dagger,a):P_0.
\]
That produces a valid surviving statement, not confirmation of the original row.

Independent exact integration gives
\[
\int_0^\infty A(u)\,du=2,
\]
\[
\int_0^\infty A(u)\frac{u}{u^2+u+1}\,du
=-\frac13+\frac{4\sqrt3\pi}{27},
\]
and hence
\[
\langle |z_2|^2\rangle_V
=-\frac16+\frac{2\sqrt3\pi}{27}
=0.2363998587187150779.
\]
Independent kernel recurrences give:

| \(N\) | normalized trace | \(N(\text{trace}-L)\) |
|---:|---:|---:|
| 22 | 0.237880574939233 | 0.0325757569 |
| 60 | 0.236930342380032 | 0.0318290197 |
| 200 | 0.236557557384253 | 0.0315397331 |
| 800 | 0.236439169045958 | 0.0314482618 |
| 1200 | 0.236426057170886 | 0.0314381426 |

Thus a \(1/N\) correction is supported, but the asymptotic coefficient is approximately \(0.03142\), not the memo’s short-range \(0.032751\). Its extrapolated intercept happens to be close.

The proposed definition also needs \(N\ge r\), a bihomogeneous projective symbol, and the qualifier that the exact coherent symbol holds on \(p\in V\). It is not exact for arbitrary ambient coherent states after the \(P_0\) compressions.

**FIX DEMAND:** Mark C-086 and C-168 REFUTED under D-toeplitz-operator, introduce the normalized operator as a distinct definition, and rerun the asymptotic fit to larger \(N\).

**SURVIVING STATEMENT:** For \(N\ge r\), normalized compression by \((N-r)!/N!\) has the desired projective symbol and the conic data converge to the exact Fubini–Study average with an apparent \(1/N\) correction.

## O4 — MAJOR — the checker is not red-capable for the ordering claim and overstates what it checks

**Location:** `checkers/explore/intersection_observables.py:372–441`, `:559–626`, `:737–760`; target `:60–63`; L4.

The mandated run exited 0, and all raw tables agree with independent computations. That does not justify the terminal claim that “every predicted constant/exponent was met”:

- Most printed exponents and crossover statements have no failing assertion.
- N6’s ill-conditioned case is checked only through
  `min(Tr/limit,1)`, so every overshoot passes automatically.
- The Toeplitz checker fits a free intercept and free \(1/N\) coefficient; it does not test the claimed ordering-dependent correction.
- No mutation for this checker is recorded in `checkers/MUTATIONS.md`.

Mutation analysis:

1. Swap `line_t` and `line_g` at lines 402–403: predicted exit 1. The “tangent” fit would approach zero after division by \(\sqrt N\), and the check at line 441 would reject it.

2. Drop normal ordering: replace \(n_2\) by \(n_2+1\), and analogously \(n_2(n_2-1)\) by an anti-normal expression. Predicted exit 0. For \(r=1\), the result shifts by exactly \(1/N\); the fitted intercept is unchanged and the free coefficient absorbs the mutation. This directly contradicts the claim that the checker verifies the ordering convention.

Mutated copies: NOT RUN because `/tmp` is not writable in the read-only sandbox.

**FIX DEMAND:** Add registered mutations, assert the ordering-specific finite-\(N\) coefficient or exact values, assert representative slopes/crossover values, and remove the unconditional terminal claim.

**SURVIVING STATEMENT:** The script correctly validates its exact linear closed forms, selected conic overlaps, leading Toeplitz limit, and frame-spectrum tables.

## O5 — FATAL — the dequantization comparison mixes relative and additive errors, miscounts filters, and double-counts the gap normalization

**Location:** `scouting/intersection-observables.md:285–311`, `:518–526`, `:558–567`.

The normalized overlap is a legitimate additive-precision trace quantity:
\[
\tau_N=\frac1{M_N}\operatorname{Tr}(P_IP_J)
=\frac1{M_N}\operatorname{Tr}(P_IP_JP_I).
\]
A controlled-block-encoding trace experiment on a maximally mixed valid-sector state estimates it.

However:

- D-dqc1-style-estimate specifies \(O(\epsilon^{-2})\) repetitions. \(O(\epsilon^{-1})\) amplitude estimation requires a coherent purification/preparation and extra clean registers; it is BQP-style, not the registered DQC1-style procedure.
- Hutch++ guarantees a relative \((1\pm\delta)\) trace estimate for PSD matrices in \(O(1/\delta)\) matvecs, as the memo says. [The primary paper states exactly this](https://arxiv.org/abs/2010.09649). For additive error \(\epsilon\) in \(\tau_N\), the corresponding relative tolerance is \(\delta=\epsilon/\tau_N\), giving \(O(\tau_N/\epsilon)\) matvecs when \(\epsilon<\tau_N\). The memo compares this relative \(\delta\) with an unspecified quantum additive \(\epsilon\).
- Applying \(A=P_IP_JP_I\) to a general vector requires three projector filters, not two.
- With \(\gamma_N=\Delta_N/\alpha_{\mathrm{BE}}\), the query cost after choosing \(N=\Theta(1/\epsilon)\) is
  \[
  \widetilde O(\gamma_N^{-1}\epsilon^{-1}).
  \]
  C-NEW-IO-TOEPLITZ-COST writes an additional \(\epsilon^{-m}\) while still dividing by \(\gamma_N\), double-counting \(\alpha_{\mathrm{BE}}\).
- The conic itself is a counterexample to K-IO6’s degree-only conclusion: C-024 records \(\Delta_N=N+1\), while \(\alpha_{\mathrm{BE}}=O(N^2)\), so \(\gamma_N^{-1}=O(N)\). With \(N=\Theta(1/\epsilon)\), the query cost is \(O(\epsilon^{-2})\), not the displayed \(\epsilon^{-4}\) obtained from the proposed row at \(m=2\).

The quantum route has a possible margin only if all of the following hold simultaneously: efficient coherent valid-sector preparation, efficient sparse oracles, inverse-polynomial normalized gaps, inverse-polynomial required additive precision, and no structure-aware classical shortcut. Its per-filter advantage is then polylogarithmic access versus classical vectors of length \(M_N\). No such family is proved here.

The normalized signal is not always exponentially small: N9’s orthogonal hyperplanes give \(0.214286,0.233333,0.246032\) for \(n=4,8,32\). It is exponentially small in the distance experiment and in growing codimension: at \(t=0.6,N=40\), \(\tau_N=7.11018\times10^{-10}\); at \(t=0.3,N=800\), \(1.65747\times10^{-37}\); for coordinate codimension \(2k\), N9 gives \(0.2143,0.03846,0.0012236,1.2304\times10^{-6}\) at \(k=1,2,4,8\).

**FIX DEMAND:** Compare both algorithms at the same additive or relative precision, count three classical filters, distinguish DQC1 sampling from purified amplitude estimation, and express all quantum costs only through \(\gamma_N^{-1}\).

**SURVIVING STATEMENT:** Hutch++ removes any generic quantum advantage in the number of trace-estimator iterations; a conditional margin can remain in the cost of one length-\(M_N\) classical filter application.

## O6 — FATAL — K-IO2 contradicts N9 and its cited literature does not prove the claimed polynomial classical baseline

**Location:** bottom line `:41–44`; north-star criterion 2 at `:269–283`; K-IO2 `:342–348`; C-NEW-IO-WITNESS-BASELINE `:528–537`; C-NEW-IO-SIGNAL `:539–547`.

The memo says both:

- polynomial visibility iff codimension is \(O(1)\), and
- polynomial visibility iff codimension is \(O(\log n)\).

The second is correct for the coordinate family. At \(N=n\),
\[
\frac{T_N}{M_N}
=\frac{\binom{2n-2k}{n-2k}}{\binom{2n}{n}}
=4^{-k}\bigl(1+O(k^2/n)\bigr)
\]
when \(k=o(n)\). Since \(\operatorname{codim}(V\cap W)=2k\), inverse-polynomial visibility persists through \(k=O(\log n)\), not merely \(O(1)\).

That destroys the stated squeeze. With \(c=O(\log n)\) equations and regularity bounded polynomially, the product of degrees can be \(n^{O(\log n)}\), which is quasipolynomial, not polynomial.

The literature attribution is also too strong. The Sommese–Verschelde–Wampler paper shows how to compute intersections when \(A\) and \(B\) are already represented by witness sets; its abstract does not establish the memo’s universal `deg V deg W` path bound, exact-integer certification, or polynomial cost from sparse generators. [Primary source](https://epubs.siam.org/doi/10.1137/S0036142903430463).

Lairez proves average-polynomial time for computing an approximate root of a polynomial system in a specific average-case model. It does not prove polynomial expected cost for each path of every diagonal homotopy appearing here. [Primary source](https://arxiv.org/abs/1507.05485).

Nor does one fixed-degree Hilbert-function value determine dimension. In \(\mathbb P^2\), at the stable level \(N=2\), a line and three noncollinear reduced points both have Hilbert-function value \(3\), but dimensions \(1\) and \(0\). Multiple degrees or additional degree/regularity bounds are required.

Finally, C-NEW-IO-SUM-IDEAL says its identity is “exact in every case.” It is only asymptotic: N1 at \(t=1,N=8\) gives \(1.41226118\), not \(1/J=1.41228293\); N5 gives \(2.03495679\), not \(2\).

**FIX DEMAND:** Retract K-IO2 and C-NEW-IO-WITNESS-BASELINE as universal claims, use \(O(\log n)\) visibility, and state the witness-set baseline only under explicit input-representation, conditioning, certification, and average-case promises.

**SURVIVING STATEMENT:** \(I_N+J_N\) is obtained by concatenating Macaulay rows, and diagonal homotopy is a relevant classical competitor once suitable witness sets and conditioning promises are supplied.

## O7 — MAJOR — quantifiers and the dependency DAG are not merge-safe

**Location:** proposed rows `:442–587`; lockstep `:589–606`.

Dependency grep found every currently named C-id and D-id. Proposed D-ids are defined locally in the memo. No proposed row directly cites a row currently marked REFUTED. Status vocabulary also passes: the blanket declaration assigns CONJECTURE, while C-085 is proposed REFUTED.

The merge ceases to pass immediately after the memo’s own status changes:

- C-166 currently depends on C-085. If C-085 becomes REFUTED, C-166 must be rewired.
- C-087 also depends on C-085.
- C-NEW-IO-TOEPLITZ and C-NEW-IO-TOEPLITZ-COST depend on C-168, which must become REFUTED under O3.
- C-NEW-IO-TANGENCY depends on C-NEW-IO-CLEAN even though tangency is expressly outside its hypotheses.

Quantifier defects include:

- C-NEW-IO-CLEAN says “all \(N\ge\mathrm{reg}\)” for an asymptotic statement; it must say \(N\to\infty\) for fixed \(I,J\), or give uniform family bounds.
- C-NEW-IO-TANGENCY omits homogeneous radical ideals and the stable range.
- C-NEW-IO-DISTANCE omits smoothness/Morse–Bott/nondegeneracy of the closest-pair locus.
- C-NEW-IO-TOEPLITZ omits \(N\ge r\).
- C-NEW-IO-SIGNAL omits \(n\ge2\), \(2k\le n\), and the scaling regime behind “iff.”
- C-NEW-IO-CROSSOVER omits \(0<t\le\pi/2\) and \(1\ll N\).
- C-NEW-IO-DEQUANT lacks a common precision parameter and gap/access promises.
- C-NEW-IO-PROJECTOR-AMBIGUITY is an editorial correction, not a mathematical conjecture.

**FIX DEMAND:** Rewrite every row with explicit asymptotic and input-family quantifiers, remove all dependencies on newly REFUTED rows, and give every merged row its own explicit status field.

**SURVIVING STATEMENT:** The dependency names themselves resolve, and the exact linear-algebra identities can be merged after the rewiring and quantifier repairs below.

## O8 — MAJOR — the north-star score and lockstep claims overstate the result

**Location:** `scouting/intersection-observables.md:258–332`, `:589–606`, `:610–626`.

PRD §2 audit:

1. **Problem:** P0 is precise. P1 lacks sufficient uniform lower-order/asymptotic promises to recover dimension; P2 lacks a closest-pair nondegeneracy promise; P3 omits encoding, degree, norm, and projective homogeneity promises for \(g\). Partially met.
2. **Classical baseline:** Not met. K-IO2 is internally inconsistent, the witness-set input cost is omitted, and the Lairez result is misapplied.
3. **Quantum algorithm:** Not met. There is no proved family with a complete resource bound beating the best baseline.
4. **Dequantization audit:** Not met. Precision conventions are mixed and the Toeplitz cost is algebraically wrong.
5. **Heuristic attack:** Partial. The linear-subspace SWAP experiment is concrete, but photon-number parity is a non-Gaussian measurement and preparation of \(P_I/\mathrm{HF}_I\) is assumed. A Haar passive-optics twirl can prepare the linear case; “phase-randomised source” alone is insufficient.

The defensible score is 1/5, or at most 2/5 if the trivial linear-subspace demonstration receives full criterion-5 credit.

Calling the outputs “three theorems” at lines 329 and 610 violates L1: all new rows remain CONJECTURE, and the clean formula expressly has an unproved leaf.

The lockstep note for C-168 is substantively wrong; it says status unchanged even though the tested operator is not the registered operator. The lockstep note for C-166 also fails to remove its dependency on the newly REFUTED C-085.

**FIX DEMAND:** Report the arm as conjectural geometry plus exact linear examples and negative evidence, score the PRD criteria no higher than 2/5, and apply the status/dependency changes stated below.

**SURVIVING STATEMENT:** Arm C has useful exact formulas and a plausible clean-intersection dictionary, but no adjudicated quantum speedup and no completed north-star hit.

## Proposed rows adjudication

| Proposed row | Adjudication |
|---|---|
| C-NEW-IO-CLEAN | **HOLD missing step.** The anti-diagonal normal calculation is absent and Geometry 2.4 has no verified theorem establishing the required ambient frame estimate. |
| C-NEW-IO-SUM-IDEAL | **ACCEPT WITH REWORDING exact text:** “Assume C-NEW-IO-CLEAN. If \(J(x)\equiv J_0>0\) on \(Z\), then, as \(N\to\infty\), \(T_N(I,J)=J_0^{-1}\mathrm{HF}_{R/(I+J)}(N)(1+O_{I,J}(N^{-1}))\). Moreover \(I_N+J_N\) is the row span of the concatenated degree-\(N\) Macaulay matrices. This identity alone does not give the dimension from one Hilbert-function value or establish a polynomial classical algorithm.” |
| C-NEW-IO-TANGENCY | **ACCEPT WITH REWORDING exact text:** “Let \(I=I(V)\) and \(J=I(W)\) be homogeneous radical ideals of smooth plane curves meeting only at \(x\), and take \(N\) in the stable range. If their contact order is \(m\ge2\) and in unitary Fubini–Study normal coordinates their normal separation is \(\gamma u^m+O(u^{m+1})\), then \(T_N(I,J)=\Gamma(1+1/m)|\gamma|^{-2/m}N^{1-1/m}(1+o(1))\).” |
| C-NEW-IO-DISTANCE | **ACCEPT WITH REWORDING exact text:** “Let \(V,W\) be disjoint smooth projective varieties in the stable range. Assume the closest-pair set \(S\subset V\times W\) is a compact smooth real Morse–Bott minimum manifold of real dimension \(r\), with nondegenerate normal Hessian. Then \(T_N(I,J)=C N^{r/2}\cos^{2N}(d_0)(1+O(N^{-1}))\), \(C>0\), and \(-\log T_N/(2N)=\log\sec d_0-r\log N/(4N)+O(N^{-1})\).” |
| C-NEW-IO-DISTANCE-COST | **REFUTE with counterexample.** For the Clifford pair the exact known factor \(N+1\) can be divided out, so its logarithmic bias does not force \(N=\Omega(\eta^{-1}\log(1/\eta))\). The required additive precision also omits the factor \(CN^{r/2}\). |
| C-NEW-IO-TOEPLITZ | **ACCEPT WITH REWORDING exact text:** “For the conic \(z_0z_1=z_2^2\), \(N\ge r\), and \(g\in\{|z_2|^2,|z_2|^4\}\), define \(\widetilde T_g^{(N)}=((N-r)!/N!)P_0:g(a^\dagger,a):P_0\). Then the computed traces are consistent with \(\mathrm{Tr}(\widetilde T_g^{(N)})/\mathrm{HF}(N)=\mathrm{vol}(V)^{-1}\int_Vg\,d\mathrm{vol}+b_g/N+O(N^{-2})\). For \(g=|z_2|^2\), the exact limit is \(-1/6+2\sqrt3\pi/27\).” |
| C-NEW-IO-TOEPLITZ-COST | **REFUTE with counterexample.** It double-counts \(\alpha_{\mathrm{BE}}\) after already dividing by \(\Delta/\alpha_{\mathrm{BE}}\). The conic has \(\Delta_N=N+1\), contradicting the claimed degree-only exponent. |
| C-NEW-IO-WITNESS-BASELINE | **REJECT.** The cited results do not establish polynomial per-path cost, exact certification, or cheap construction of witness sets for every quantified input. |
| C-NEW-IO-SIGNAL | **ACCEPT WITH REWORDING exact text:** “For \(n\ge2\), \(N\ge0\), and two hyperplanes at angle \(t\), \(T_N=\sum_{a=0}^N\cos^{2a}t\binom{N-a+n-2}{n-2}\). At \(t=\pi/2,N=n\), \(T_N/M_N=n(n-1)/(2n(2n-1))\) and \(T_N/\mathrm{HF}=(n-1)/(2n-1)\). For coordinate ideals on disjoint blocks of size \(k\), \(2k\le n\), \(T_N/M_N=\binom{N+n-2k}{n-2k}/\binom{N+n}{n}\); when \(N=n\) and \(k=o(n)\), this is \(4^{-k}(1+O(k^2/n))\), hence inverse-polynomial exactly when \(k=O(\log n)\).” |
| C-NEW-IO-CROSSOVER | **ACCEPT WITH REWORDING exact text:** “For \(0<t\le\pi/2\), two hyperplanes in \(\mathbb P^3\) have \(T_N=\sum_{a=0}^N\cos^{2a}t(N+1-a)\). In the double-scaling regimes \(1\ll N\ll\csc^2t\) and \(N\gg\csc^2t\), its local log–log slope tends respectively to \(2\) and \(1\). Thus this particular finite-\(N\) exponent estimator requires \(N\sin^2t\to\infty\).” |
| C-NEW-IO-DEQUANT | **ACCEPT WITH REWORDING exact text:** “For \(A=P_IP_JP_I\succeq0\), Hutch++ gives relative error \(\delta\) using \(O(\delta^{-1})\) applications of \(A\), each requiring three approximate projector filters. For additive error \(\epsilon\) in \(\tau_N=\mathrm{Tr}(A)/M_N\), take \(\delta=\epsilon/\tau_N\). Direct DQC1-style sampling costs \(O(\epsilon^{-2})\) controlled-filter uses; \(O(\epsilon^{-1})\) requires a coherent purification and BQP amplitude estimation. A quantum advantage requires efficient oracles, inverse-polynomial normalized gaps and signal, and a per-filter advantage over length-\(M_N\) Krylov vectors; none is proved here.” |
| C-NEW-IO-SWAP-HARDWARE | **ACCEPT WITH REWORDING exact text:** “Given preparations of \(\rho_I=P_I/\mathrm{HF}_I\) and \(\rho_J=P_J/\mathrm{HF}_J\), mode-wise beam splitters followed by total photon-number parity estimate \(\mathrm{Tr}(\rho_I\rho_J)\) with \(O(\epsilon^{-2})\) shots. Photon counting/parity is a non-Gaussian measurement, and ground-space mixture preparation is an explicit assumption. For linear subspaces the mixture can be produced by a passive-optics Haar twirl; at \(n=2,N=1\) the result is \((1+\cos^2t)/4\).” |
| C-NEW-IO-PROJECTOR-AMBIGUITY | **REJECT.** This is a notation correction, not a CONJECTURE. Incorporate it into D-intersection-overlap and amend C-085/C-166/C-167 directly. |

## Proposed definitions adjudication

| Proposed definition | Adjudication |
|---|---|
| D-intersection-overlap | **ACCEPT.** |
| D-clean-intersection | **REWORD exact text:** “Smooth \(V,W\subset\mathbb{CP}^n\) intersect cleanly along a smooth pure-dimensional \(Z=V\cap W\) if \(T_xZ=T_xV\cap T_xW\) for every \(x\in Z\). Transverse intersections are clean; clean intersections may have excess dimension.” |
| D-intersection-angle-condition-number | **REWORD exact text:** “For a clean intersection, let \(A_x=T_xV\ominus T_xZ\) and \(B_x=T_xW\ominus T_xZ\). Define \(J(x)=\prod_i\sin^2\theta_i(x)\), padding the principal-angle list with \(\pi/2\) when the dimensions differ, and \(\mu_\cap=\sup_ZJ^{-1}<\infty\). No universal crossover scale follows from this definition alone.” |
| D-bergman-frame-operator | **REWORD exact text:** “Define \(S_V^{(N)}=\int_V|e_p\rangle\langle e_p|\,d\mathrm{vol}_V(p)\). Exactly, \(\operatorname{ran}S_V^{(N)}=(I(V)_N)^\perp\). The claimed operator-norm asymptotic \(S_V^{(N)}=(\pi/N)^k(P_{I(V),N}+O(N^{-1}))\) is a separate conjectural/theorem claim requiring a precise source; it is not part of the definition.” |
| D-normalised-toeplitz-operator | **REWORD exact text:** “For \(N\ge r\) and a projective bihomogeneous symbol \(g(z,\bar z)\) of bidegree \((r,r)\), define \(\widetilde T_g^{(N)}=((N-r)!/N!)P_{0,N}:g(a^\dagger,a):P_{0,N}\). If \(I\) is radical, \(N\) is stable and \(p\in V(I)\), its restricted coherent-state symbol is exactly \(g(p,\bar p)\).” |
| D-contact-order | **REWORD exact text:** “At a common point of smooth plane curves choose holomorphic coordinates unitary for the Fubini–Study metric at the point and flatten \(W\) to \(v=0\). If \(V\) has \(v=\gamma u^m+O(u^{m+1})\), \(\gamma\ne0\), then \(m\) is the contact order and local intersection multiplicity. \(m=1\) is transverse; \(m\ge2\) is tangent.” |

## Lockstep notes

- **C-085:** status must become **REFUTED**. Counterexample: the smooth conic and its tangent line have \(\dim(V\cap W)=0\) but \(T_N\sim\Gamma(3/2)N^{1/2}\). Surviving statement: for fixed homogeneous radical ideals whose smooth varieties intersect cleanly, and after the Bergman-frame leaf is proved, the exponent is \(\dim(V\cap W)\); disjoint varieties require a separate Morse–Bott distance statement.

- **C-166:** status remains **CONJECTURE**. Its transversal hypothesis survives every exact computation. Do not silently replace it by the stronger new clean-intersection theorem claim; add a separate C-NEW-IO-CLEAN row. Amend the constant to
  \[
  c=\pi^{-l}\int_Z\prod_i\sin^{-2}\theta_i\,d\mathrm{vol}_Z,
  \]
  add N1/N2/N5/N6 as tests, define \(P_I=P_{0,N}^{(I)}\), and remove dependency on REFUTED C-085.

- **C-168:** status must become **REFUTED**, not unchanged. Under the registered D-toeplitz-operator, \(g=|z_2|^2\) gives a trace growing linearly in \(N\). Surviving statement: with the new degree-normalized operator \(\widetilde T_g^{(N)}\), for fixed smooth radical \(V\), stable \(N\to\infty\), and bihomogeneous projective \(g\),
  \[
  \frac{\operatorname{Tr}\widetilde T_g^{(N)}}{\mathrm{HF}(N)}
  =\frac1{\mathrm{vol}(V)}\int_Vg\,d\mathrm{vol}+O(N^{-1}).
  \]
  C-086 requires the same status change and surviving replacement.

VERDICT: FAIL(O1, O2, O3, O4, O5, O6, O7, O8)