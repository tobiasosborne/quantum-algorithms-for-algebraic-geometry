# Adversarial verdict: `scouting/intersection-observables.md`, round 2

- Date: 2026-09-03
- Critic model: OpenAI Codex (GPT-5)
- Target delta: `git diff 6776f99 HEAD -- scouting/intersection-observables.md checkers/explore/intersection_observables.py`
- Mandated run: `cd checkers && timeout 900 python3 explore/intersection_observables.py`
- Exit code: **0**
- Runtime environment reported by checker: NumPy 2.4.6
- Scope: repair-r1 changes only; prior passing material was not re-litigated.

## Fresh recomputation

### Geometry 5.3–5.4 and the excess family

At \(x\in Z\), write
\[
T_xV=T_xZ\oplus A_x,\qquad T_xW=T_xZ\oplus B_x.
\]
The quadratic distance normal to the diagonal is
\[
|\delta|^2+\lVert a-b\rVert^2,\qquad
\delta=t-s\in T_xZ.
\]
Consequently,
\[
\int_{\mathbb C^l}e^{-N|\delta|^2}\,d\delta=(\pi/N)^l.
\]
For \(L(a,b)=a-b\), the Hermitian Gram determinant is
\[
\det(L^\dagger L)=\prod_i\sin^2\theta_i=J(x),
\]
including unit factors from padded \(\pi/2\) angles. Hence
\[
\int_{A_x\times B_x}e^{-N\lVert a-b\rVert^2}\,da\,db
=\frac{(\pi/N)^{k_1+k_2-2l}}{J(x)}.
\]
The product is
\[
\frac{(\pi/N)^{k_1+k_2-l}}{J(x)}.
\]
The missing anti-diagonal block is now present and the stated exponent is correct.

For the repaired \(\mathbb P^4\) family, the principal cosines are \((1,1,\cos t)\), so
\[
T_N=h_N(1,1,\cos^2t)
=\sum_{a=0}^N\cos^{2a}t\,(N+1-a).
\]
Independent evaluation gives

| \(t\) | \(\csc^2t\) | \(T_{48}/48\) | \(T_{1024}/1024\) | \(T_{10000}/10000\) |
|---:|---:|---:|---:|---:|
| 0.9 | 1.6297234242 | 1.6422952661 | 1.6303127293 | 1.6297837691 |
| 0.4 | 6.5942770963 | 5.9633549406 | 6.5646912210 | 6.5912475026 |

Thus \(T_N/N\to1.6297,6.5943\), as claimed.

### Tangency and distance

For contact order \(m\ge2\),
\[
d^2=|u-v|^2+|\gamma|^2|u|^{2m}+o(|u-v|^2+|u|^{2m})
\]
gives
\[
\int_{\mathbb C}e^{-N|u-v|^2}\,dv=\frac{\pi}{N},
\]
and
\[
\int_{\mathbb C}e^{-N|\gamma|^2|u|^{2m}}\,du
=\pi\Gamma(1+1/m)(N|\gamma|^2)^{-1/m}.
\]
After the two frame factors, this yields
\[
T_N\sim\Gamma(1+1/m)|\gamma|^{-2/m}N^{1-1/m}.
\]
For \(m=2,\gamma=1\), the constant is
\[
\Gamma(3/2)=0.88622692545,
\]
against the checker’s fitted \(0.891497\). At \(m=1\), the induced volume factor on the graph is \(1+|\gamma|^2\), giving
\[
(1+|\gamma|^2)/|\gamma|^2,
\]
not \(|\gamma|^{-2}\). The restriction \(m\ge2\) is necessary.

For the Clifford pair,
\[
-\frac{\log T_N}{2N}
=\log\sec t-\frac{\log(N+1)}{2N}.
\]
At \(t=0.3,N=800\),
\[
T_N=1.4250104716\times10^{-29},\qquad
T_N/M_N=1.6574745798\times10^{-37},
\]
and the bias is \(-0.00417866309\). The estimator is below the target. The first \(N\) at which the uncorrected bias is at most \(10\%\) of \(\log\sec(0.3)\) is \(N=721\).

### Toeplitz normalization and recurrence

Under the registered D-toeplitz-operator,
\[
T_g=P_0:g(a^\dagger,a):P_0.
\]
For \(g=|z_2|^2\), this is \(P_0n_2P_0\), and its trace divided by \(\mathrm{HF}(N)\) grows like \(N\). C-086 and C-168 are therefore refuted as written.

The distinct normalized operator is
\[
\widetilde T_g^{(N)}
=\frac{(N-r)!}{N!}P_0:g(a^\dagger,a):P_0,\qquad N\ge r.
\]

Independent symbolic integration gives
\[
\int_0^\infty A(u)\,du=2,
\]
\[
\int_0^\infty A(u)\frac{u}{u^2+u+1}\,du
=-\frac13+\frac{4\sqrt3\pi}{27},
\]
and therefore
\[
L=\langle|z_2|^2\rangle_V
=-\frac16+\frac{2\sqrt3\pi}{27}
=0.2363998587187150779\ldots.
\]

An independent recurrence in normalized Fock amplitudes,
\[
\frac{A_{j+1}}{A_j}
=\sqrt{\frac{k_2(k_2-1)}{(j+d+1)(j+1)}},
\]
reproduces:

| \(N\) | normalized trace | \(N(\text{trace}-L)\) |
|---:|---:|---:|
| 22 | 0.237880574939233 | 0.032575756851 |
| 60 | 0.236930342380032 | 0.031829019679 |
| 200 | 0.236557557384253 | 0.031539733108 |
| 800 | 0.236439169045958 | 0.031448261794 |
| 1200 | 0.236426057170887 | 0.031438142606 |
| 2400 | 0.236412953732136 | 0.031428032211 |

Extrapolating the last four values linearly in \(1/N\) gives approximately \(0.0314179\). Thus “about \(0.03144\)” is an acceptable finite-\(N\) summary, while the apparent asymptotic coefficient is closer to \(0.03142\). The old \(0.03275\) value is conclusively a short-range fit.

Pinning the intercept to \(L\) and requiring \(N(v_N-L)\in[0.030,0.034]\) is sufficient to reject \(n_2\mapsto n_2+1\): the mutation shifts the coefficient to approximately \(1.03144\).

### Dequantization

For
\[
A=P_IP_JP_I,\qquad \tau_N=\operatorname{Tr}(A)/M_N,
\]
an application of \(A\) uses three projector filters. In the nontrivial regime \(0<\epsilon<\tau_N\), additive error \(\epsilon\) in \(\tau_N\) corresponds to Hutch++ relative error
\[
\delta=\epsilon/\tau_N.
\]
Thus the classical cost is
\[
\widetilde O\!\left(
M_Ns_{\rm row}\gamma_N^{-1}\frac{\tau_N}{\epsilon}
\right),
\]
whereas registered DQC1-style sampling costs
\[
\widetilde O(\gamma_N^{-1}\epsilon^{-2}).
\]
Their ratio is
\[
M_Ns_{\rm row}\tau_N\epsilon
\]
up to constants and logarithms. The three filters contribute only a constant factor, and \(\gamma_N^{-1}\) is counted once on each side. If \(\epsilon\ge\tau_N\), the zero estimator is already within the requested additive tolerance, so the displayed Hutch++ formula must not be used without this regime qualification.

The TOEPLITZ-COST row is correctly refuted. For the conic,
\[
\Delta_N=N+1,\qquad \alpha_{\rm BE}=O(N^2),\qquad
\gamma_N^{-1}=O(N),
\]
so at \(N=\Theta(\epsilon^{-1})\), coherent amplitude estimation costs
\[
\widetilde O(\gamma_N^{-1}\epsilon^{-1})
=\widetilde O(\epsilon^{-2}),
\]
not \(\epsilon^{-4}\).

### Visibility

At \(N=n\),
\[
R_{n,k}
=\frac{\binom{2n-2k}{n-2k}}{\binom{2n}{n}}
=\prod_{j=0}^{2k-1}\frac{n-j}{2n-j}.
\]
For \(k=o(n)\),
\[
\log R_{n,k}
=-k\log4-\frac{k(2k-1)}{2n}
+O(k^3/n^2).
\]
In particular, for \(k=o(\sqrt n)\), including \(k=O(\log n)\),
\[
R_{n,k}=4^{-k}\bigl(1+O(k^2/n)\bigr).
\]
The exact product also shows \(R_{n,k}\le4^{-k}\). Together with the corresponding lower estimate for \(k=O(\log n)\), inverse-polynomial visibility holds exactly through \(k=O(\log n)\) in the stated \(k=o(n)\) regime. The core correction to K-IO2 is valid.

### Exact linear row

Choose principal-vector bases so that
\[
\langle u_i,w_j\rangle=\sigma_i\delta_{ij}.
\]
Normalized occupation-vector bases of \(\mathrm{Sym}^NU\) and \(\mathrm{Sym}^NW\) then have overlap
\[
\langle u^\alpha,w^\beta\rangle
=\delta_{\alpha\beta}\prod_i\sigma_i^{\alpha_i}
\]
on the paired coordinates; any occupation of an unpaired direction has zero overlap. Therefore
\[
\operatorname{Tr}(P_{\mathrm{Sym}^NU}P_{\mathrm{Sym}^NW})
=\sum_{|\alpha|=N}\prod_i\sigma_i^{2\alpha_i}
=h_N(\sigma_1^2,\ldots,\sigma_r^2).
\]
This proves C-NEW-IO-LINEAR-EXACT for all stated dimensions and for \(N=0\) as well.

### Mutations

All five mutations are genuine counterfactuals and are caught:

| mutation | mutated result | adjudication |
|---|---|---|
| M-IO1 | fitted tangent constant \(0.002496\) instead of \(0.886227\) | caught |
| M-IO2 | coefficient \(1.031479,1.031448,1.031438\) | caught |
| M-IO3 | Richardson \(5.700593\) versus corrupted \(2.916667\), ratio \(2.152027\) | caught |
| M-IO4 | slopes \(1.9174,1.7592\); the second violates \(<1.3\) | caught |
| M-IO5 | relative discrepancy \(7.822\times10^{-6}>10^{-10}\) | caught |

Registration in `checkers/MUTATIONS.md` remains an accurately disclosed external residue.

## Disposition audit

| response-table item | adjudication | evidence |
|---|---|---|
| O1a anti-diagonal block | **VERIFIED** | The \((\pi/N)^l\) block and transverse \(J^{-1}\) block recompute correctly; N7b has the exact required limit. |
| O1b frame operator norm | **VERIFIED (RESIDUE)** | Geometry 2.4 is explicitly unproved; CLEAN is correctly marked CONJECTURE/HOLD. |
| O1c theorem-grade/saturation wording | **VERIFIED** | The theorem claim is removed; the generic skew limit \(10.9917866070\) and \(N=100\) value \(10.99107\) are correct. |
| O2a \(m=1\) defect | **VERIFIED** | The row is restricted to \(m\ge2\), and the missing \(1+|\gamma|^2\) factor is recorded. |
| O2b Morse–Bott hypothesis | **VERIFIED** | Real dimension \(r\), prefactor \(N^{r/2}\), and nondegenerate normal Hessian are present. |
| O2c bias sign | **VERIFIED** | The corrected negative sign agrees with the exact Clifford formula. |
| O2d forced-\(N\) claim | **VERIFIED** | The claim is retracted and the row is retained as REFUTED. |
| O3a C-086/C-168 status | **VERIFIED** | Both are proposed REFUTED under the registered operator; the normalized operator is distinct. |
| O3b long-\(N\) coefficient | **VERIFIED** | The recurrence and values through \(N=1200\) reproduce independently; \(0.03144\) is a valid approximation, with extrapolated limit near \(0.03142\). |
| O4a ordering blindness | **VERIFIED** | The exact intercept plus coefficient window rejects the anti-normal mutation by a shift of \(+1\). |
| O4b N6 clamp | **VERIFIED** | The production check is two-sided; the isolated self-test demonstrates the old clamp’s blindness. |
| O4c mutations/terminal claim | **VERIFIED (RESIDUE)** | Five mutations run and are caught; registration remains outside the lane. The terminal claim is now scoped to asserted quantities. |
| O4d crossover assertions | **VERIFIED** | The unmutated \(1.5366,1.1599\) slopes pass and the moved-angle case fails. |
| O5a common error model | **VERIFIED, WITH ROW REWORDING REQUIRED** | The algebra is correct for \(0<\epsilon<\tau_N\); that regime is absent from the proposed row. |
| O5b filter count | **VERIFIED** | Three filters are counted. |
| O5c DQC1 versus BQP | **VERIFIED** | The \(O(\epsilon^{-1})\) route is correctly separated as coherent BQP amplitude estimation. |
| O5d double-counting | **VERIFIED** | TOEPLITZ-COST is REFUTED and \(\gamma_N\) is counted once. |
| O5e signal regimes | **VERIFIED** | Both polynomially visible and exponentially small examples are quoted. |
| O6a K-IO2 contradiction | **VERIFIED** | K-IO2 is retracted and the \(O(\log n)\) threshold is correct. |
| O6b literature attribution | **VERIFIED** | The universal baseline row is deleted and the surviving literature statement is conditional. |
| O6c one Hilbert value | **VERIFIED** | The line/three-points counterexample is recorded. |
| O6d SUM-IDEAL exactness | **VERIFIED** | The relation is now asymptotic and inherits CLEAN’s hold. |
| O7a dependencies of proposed rows | **VERIFIED** | All named ids resolve; no proposed row depends on either deleted row, and no proposed row directly depends on C-085, C-086, or C-168. |
| O7b C-087 rewire | **NOT VERIFIED** | The residue mentions only C-085, but C-087 also depends on newly REFUTED C-086. C-168 itself depends on C-086, and C-169 depends on C-168. |
| O7c quantifiers | **NOT VERIFIED** | TANGENCY, DISTANCE, and TOEPLITZ omit explicit \(N\to\infty\); CROSSOVER does not quantify its double scaling; DEQUANT omits \(\epsilon<\tau_N\). |
| O7d editorial row | **VERIFIED** | PROJECTOR-AMBIGUITY is deleted and its content moved into the definition/amendments. |
| O8a score | **VERIFIED** | The score is reduced to 1/5, at most 2/5 under the stated convention. |
| O8b theorem language | **VERIFIED** | The L1-violating language is removed. |
| O8c C-168 lockstep status | **VERIFIED, SUBJECT TO O9** | REFUTED is correct, but its dependency rewire remains incomplete. |
| O8d hardware qualifications | **VERIFIED, SUBJECT TO O12** | Non-Gaussian measurement and preparation assumptions are stated; the parity observable itself is now underspecified. |

## New objections

### O9 — MAJOR — lockstep remains incomplete after the REFUTED status changes

**Location:** memo lines 629–641; `claims/CLAIMS.md` rows C-087, C-168, C-169 and dependency index.

Fresh grep gives:

- C-087 depends on both C-085 and C-086.
- C-168 depends on C-086.
- C-169 depends on C-168.
- The repair records only the C-087-to-C-085 edge.
- The C-168 lockstep text changes its status but does not remove its dependency on C-086.

Thus the proposed ratchet would leave multiple live rows depending directly on newly REFUTED rows. This is a delta consequence of the repair, not an attack on previously passing text.

**FIX DEMAND:** Apply the C-087 and C-168 dependency amendments printed under Lockstep notes, and also amend C-169 before changing the statuses.

**SURVIVING STATEMENT:** The proposed statuses C-085/C-086/C-168 = REFUTED and C-079/C-087/C-166/C-167 unchanged are substantively correct; the DAG edits are incomplete.

### O10 — MAJOR — two proposed definitions violate registered projector and conjugation conventions

**Location:** proposed definitions, memo lines 418–447.

D-bergman-frame-operator writes
\[
P_{I(V),N}
\]
inside its asymptotic. Under D-projectors, notation of this form denotes the projector onto the ideal piece, whereas the intended operator is the ground/Bergman projector \(P_{0,N}^{(I(V))}\). At best the symbol is undefined; under the registered reading it is the wrong complementary projector.

D-normalised-toeplitz-operator says the exact symbol holds for “\(p\in V(I)\).” Binding convention C3 says a geometric point \(x\in V(I)\) is represented by the coherent state \(|\bar x\rangle^{\otimes N}\), while the memo’s \(e_p=(p\cdot z)^N/\sqrt{N!}\) lies in the ground space when \(\bar p\in V(I)\). The definition must state the conjugation explicitly.

D-intersection-overlap also calls \(P_0\) a Bergman projector without stating the radical/stable-range qualification.

**FIX DEMAND:** Use the exact definition rewordings below.

**SURVIVING STATEMENT:** The intended frame operator, normalized Toeplitz operator, and overlap are mathematically coherent after replacing the projector symbol, adding the radical/stable qualification, and enforcing C3.

### O11 — MAJOR — the repair’s claim rows are still not fully quantified

**Location:** C-NEW-IO-TANGENCY, DISTANCE, TOEPLITZ, SIGNAL, CROSSOVER, DEQUANT and the surviving TOEPLITZ-COST text, memo lines 505–604.

Defects:

1. TANGENCY says only “take \(N\) in the stable range” despite using \(o(1)\).
2. DISTANCE introduces \(T_N(I,J)\) without introducing \(I,J\), and omits explicit \(N\to\infty\).
3. TOEPLITZ omits explicit \(N\to\infty\).
4. SIGNAL’s \(4^{-k}(1+O(k^2/n))\) form is informative as a relative asymptotic only for \(k=o(\sqrt n)\), although the exact product supports the broader \(O(\log n)\) threshold.
5. CROSSOVER’s two regimes require a sequence \(t=t_N\) or an explicit two-parameter definition of local slope.
6. DEQUANT’s \(\delta=\epsilon/\tau_N\) requires \(0<\epsilon<\tau_N\); otherwise the relative-error call is unnecessary.
7. The surviving TOEPLITZ-COST text again says the \(1/N\) bias “forces” \(N=\Omega(1/\epsilon)\). That is true only for a raw one-level estimator with an uncancelled nonzero \(1/N\) term. Richardson extrapolation or a known correction can change the requirement.

**FIX DEMAND:** Use the exact row texts in the decision table.

**SURVIVING STATEMENT:** Every affected row has a correct core after its scaling variables and estimator regime are made explicit.

### O12 — MAJOR — “total photon-number parity” is not the SWAP observable as written

**Location:** criterion 5 and C-NEW-IO-SWAP-HARDWARE, memo lines 344–350 and 599–604.

Both inputs occupy the fixed \(N\)-particle sector, so the total photon number over all outputs is always \(2N\), whose parity is identically \(+1\). The SWAP observable is the parity
\[
(-1)^{\sum_j n_{j,-}}
\]
of the total occupation of the antisymmetric/difference output modes after the pairwise beam splitters. The r0 wording identified the difference modes; the repaired row removed that qualification.

**FIX DEMAND:** Replace “total photon-number parity” with “the parity of the total photon number in the antisymmetric/difference output modes.”

**SURVIVING STATEMENT:** With that measurement, the assumed preparations yield \(\operatorname{Tr}(\rho_I\rho_J)\); the \(n=2,N=1\) value is \((1+\cos^2t)/4\).

### O13 — MINOR — the mutation report contains two false labels

**Location:** checker lines 1104 and 1004.

The checker says “These four are the registration text” but lists five mutations. Its crossover detail string always prints `(<1.3)`, so the caught mutation is reported as
`1.7592 (<1.3)`, a false comparison. Neither defect changes the Boolean result.

**FIX DEMAND:** Change “four” to “five” and print the second threshold as `target < 1.3` or report the comparison result explicitly.

**SURVIVING STATEMENT:** All five mutations are real and caught; the checker exits 0 for the unmutated implementation.

## Final per-row decisions

| row | decision |
|---|---|
| C-NEW-IO-LINEAR-EXACT | **ACCEPT AS CONJECTURE.** The identity is proved above and the quantifiers are complete. |
| C-NEW-IO-CLEAN | **HOLD missing step.** Geometry 2.4 remains unproved. |
| C-NEW-IO-SUM-IDEAL | **HOLD missing step.** Its wording is correct, but it explicitly assumes the held CLEAN row. |
| C-NEW-IO-TANGENCY | **ACCEPT WITH REWORDING exact text:** “For fixed homogeneous radical ideals \(I=I(V)\) and \(J=I(W)\) of smooth plane curves \(V,W\subset\mathbb{CP}^2\) meeting only at \(x\), let \(N\to\infty\) through the stable range. If their contact order is \(m\ge2\) and in unitary Fubini–Study normal coordinates their normal separation is \(\gamma u^m+O(u^{m+1})\), then \(T_N(I,J)=\Gamma(1+1/m)|\gamma|^{-2/m}N^{1-1/m}(1+o(1))\).” |
| C-NEW-IO-DISTANCE | **ACCEPT WITH REWORDING exact text:** “Let \(I=I(V)\) and \(J=I(W)\) be fixed homogeneous radical ideals of disjoint smooth projective varieties. Let \(N\to\infty\) through the stable range. Assume the closest-pair set \(S\subset V\times W\) is a compact smooth real Morse–Bott minimum manifold of real dimension \(r\), with nondegenerate normal Hessian. Then \(T_N(I,J)=C N^{r/2}\cos^{2N}(d_0)(1+O_{I,J}(N^{-1}))\), \(C>0\), and \(-\log T_N/(2N)=\log\sec d_0-r\log N/(4N)+O_{I,J}(N^{-1})\).” |
| C-NEW-IO-DISTANCE-COST | **ACCEPT AS REFUTED with surviving statement:** “For a fixed disjoint pair satisfying C-NEW-IO-DISTANCE with \(d_0>0\), \(\tau_N=T_N/M_N\) is exponentially small in \(N\). Relative resolution by an additive-error estimator requires \(\epsilon=O(\tau_N)=O(CN^{r/2}\cos^{2N}(d_0)/M_N)\). No lower bound on \(N\) follows when a known prefactor is divided out.” |
| C-NEW-IO-TOEPLITZ | **ACCEPT WITH REWORDING exact text:** “For the conic \(z_0z_1=z_2^2\), let \(g=|z_2|^2\) with \(r=1\), or \(g=|z_2|^4\) with \(r=2\), and define \(\widetilde T_g^{(N)}=((N-r)!/N!)P_0:g(a^\dagger,a):P_0\) for \(N\ge r\). As \(N\to\infty\), the computed traces are consistent with \(\operatorname{Tr}(\widetilde T_g^{(N)})/\mathrm{HF}(N)=\mathrm{vol}(V)^{-1}\int_Vg\,d\mathrm{vol}+b_g/N+O(N^{-2})\). For \(g=|z_2|^2\), the exact limit is \(-1/6+2\sqrt3\pi/27\), and the data give \(b_g\approx0.03142\).” |
| C-NEW-IO-TOEPLITZ-COST | **ACCEPT AS REFUTED with surviving statement:** “For raw one-level use of C-NEW-IO-TOEPLITZ with a nonzero uncancelled \(b_g/N\) term, controlling that bias to \(O(\epsilon)\) requires \(N=\Omega(\epsilon^{-1})\). Coherent amplitude estimation then costs \(\widetilde O(\gamma_N^{-1}\epsilon^{-1})\), with \(\gamma_N\) counted once. This proves neither a quantum advantage nor a disadvantage; a known correction or extrapolation can change the required \(N\).” |
| C-NEW-IO-SIGNAL | **ACCEPT WITH REWORDING exact text:** “For \(n\ge2\), \(N\ge0\), and \(0\le t\le\pi/2\), two hyperplanes at angle \(t\) satisfy \(T_N=\sum_{a=0}^N\cos^{2a}t\binom{N-a+n-2}{n-2}\). At \(t=\pi/2,N=n\), \(T_N/M_N=n(n-1)/(2n(2n-1))\) and \(T_N/\mathrm{HF}=(n-1)/(2n-1)\). For integer \(k\ge0\), \(2k\le n\), coordinate ideals on disjoint blocks of size \(k\) satisfy \(T_N/M_N=\binom{N+n-2k}{n-2k}/\binom{N+n}{n}\). When \(N=n\) and \(k=o(n)\), \(\log(T_N/M_N)=-k\log4-k(2k-1)/(2n)+O(k^3/n^2)\); in particular, for \(k=o(\sqrt n)\), \(T_N/M_N=4^{-k}(1+O(k^2/n))\). The exact product formula implies inverse-polynomial visibility exactly when \(k=O(\log n)\) within the regime \(k=o(n)\).” |
| C-NEW-IO-CROSSOVER | **ACCEPT WITH REWORDING exact text:** “For \(0<t\le\pi/2\), let \(T_N(t)=\sum_{a=0}^N\cos^{2a}t\,(N+1-a)\). For sequences \(N\to\infty\), \(t=t_N\), define the dyadic local slope \(s_N=\log(T_{2N}(t_N)/T_N(t_N))/\log2\). If \(N\sin^2t_N\to0\), then \(s_N\to2\); if \(N\sin^2t_N\to\infty\), then \(s_N\to1\). Thus this finite-\(N\) estimator resolves the intersection exponent only when \(N\sin^2t\) is large.” |
| C-NEW-IO-DEQUANT | **ACCEPT WITH REWORDING exact text:** “For \(A=P_IP_JP_I\succeq0\), \(\tau_N=\operatorname{Tr}(A)/M_N\), and \(0<\epsilon<\tau_N\), Hutch++ gives additive error \(\epsilon\) in \(\tau_N\) by taking relative tolerance \(\delta=\epsilon/\tau_N\), using \(O(\tau_N/\epsilon)\) applications of \(A\). Each application uses three approximate projector filters. Direct DQC1-style sampling costs \(O(\epsilon^{-2})\) controlled-filter uses; \(O(\epsilon^{-1})\) requires coherent purification and BQP amplitude estimation. If \(\epsilon\ge\tau_N\), the zero estimate already meets the additive tolerance. A quantum advantage requires efficient oracles, inverse-polynomial normalized gaps and signal, and a per-filter advantage over length-\(M_N\) Krylov vectors; none is proved here.” |
| C-NEW-IO-SWAP-HARDWARE | **ACCEPT WITH REWORDING exact text:** “Given preparations of \(\rho_I=P_I/\mathrm{HF}_I\) and \(\rho_J=P_J/\mathrm{HF}_J\), apply mode-wise 50:50 beam splitters and measure the parity of the total photon number in the antisymmetric/difference output modes. Its expectation is \(\operatorname{Tr}(\rho_I\rho_J)\), estimable with \(O(\epsilon^{-2})\) shots. Photon counting/parity is a non-Gaussian measurement, and ground-space mixture preparation is an explicit assumption. For linear subspaces the mixture can be produced by a passive-optics Haar twirl; at \(n=2,N=1\) the result is \((1+\cos^2t)/4\).” |

## Per-definition decisions

| definition | decision |
|---|---|
| D-intersection-overlap | **ACCEPT WITH REWORDING exact text:** “For homogeneous ideals \(I,J\) and degree \(N\), define \(T_N(I,J)=\operatorname{Tr}(P_{0,N}^{(I)}P_{0,N}^{(J)})=\operatorname{Tr}(P_{0,N}^{(I)}P_{0,N}^{(J)}P_{0,N}^{(I)})\ge0\). Equivalently, \(T_N=\lVert B_I^\dagger B_J\rVert_F^2\) for orthonormal ground-space bases. When \(I,J\) are radical and \(N\) is in their stable ranges, the two factors are the Bergman projectors of D-bergman-projector. The normalizations in use are \(\tau_N=T_N/M_N\), \(T_N/\sqrt{\mathrm{HF}_I\mathrm{HF}_J}\), and \(T_N/(\mathrm{HF}_I\mathrm{HF}_J)=\operatorname{Tr}(\rho_I\rho_J)\). It is not \(\operatorname{Tr}(P_{I_N}P_{J_N})=M_N-\mathrm{HF}_I-\mathrm{HF}_J+T_N\).” |
| D-clean-intersection | **ACCEPT.** |
| D-intersection-angle-condition-number | **ACCEPT.** |
| D-bergman-frame-operator | **ACCEPT WITH REWORDING exact text:** “Define \(S_V^{(N)}=\int_V|e_p\rangle\langle e_p|\,d\mathrm{vol}_V(p)\). Exactly, \(\operatorname{ran}S_V^{(N)}=(I(V)_N)^\perp=\operatorname{ran}P_{0,N}^{(I(V))}\). The claimed operator-norm asymptotic is \(S_V^{(N)}=(\pi/N)^k(P_{0,N}^{(I(V))}+E_N)\), with \(\lVert E_N\rVert=O(N^{-1})\). This asymptotic is a separate conjectural/theorem claim requiring a precise source; it is not part of the definition.” |
| D-normalised-toeplitz-operator | **ACCEPT WITH REWORDING exact text:** “For \(N\ge r\) and a bihomogeneous polynomial \(g(z,\bar z)\) of bidegree \((r,r)\), regarded as a projective symbol by evaluation on unit representatives, define \(\widetilde T_g^{(N)}=((N-r)!/N!)P_{0,N}:g(a^\dagger,a):P_{0,N}\). If \(I\) is radical, \(N\) is stable, and \(x\in V(I)\), then the C3-compatible restricted coherent-state symbol is exactly \(\langle\bar x^{\otimes N}|\widetilde T_g^{(N)}|\bar x^{\otimes N}\rangle=g(x,\bar x)\).” |
| D-contact-order | **ACCEPT.** |

## Lockstep notes

### C-079

Status: **SKETCH**.

Paste:

```text
- where-tested: checkers/explore/intersection_observables.py sections A–K; section I tests the frame spectrum numerically but is evidence for, not a proof of, the operator-norm estimate in Geometry 2.4.
```

### C-085

Status: **REFUTED**.

Paste:

```text
- status: REFUTED
- counterexample: The smooth conic z_0z_1=z_2^2 and its tangent line z_1=0 have dim(V ∩ W)=0 but T_N ~ Gamma(3/2) N^{1/2}.
- surviving statement: For fixed homogeneous radical ideals whose smooth varieties intersect cleanly, the conjectural formula C-NEW-IO-CLEAN gives growth exponent dim(V ∩ W), conditional on the ambient Bergman-frame operator-norm estimate. Fixed disjoint varieties require the separate distance statement C-NEW-IO-DISTANCE.
- where-tested: checkers/explore/intersection_observables.py sections A–F and J.
```

### C-086

Status: **REFUTED**.

Paste:

```text
- status: REFUTED
- counterexample: Under D-toeplitz-operator, g=|z_2|^2 gives T_g=P_0 n_2 P_0 and Tr(P_0T_g)/HF(N) ~ N <|z_2|^2>_V, so the stated normalized trace diverges.
- surviving statement: Under the distinct D-normalised-toeplitz-operator, the conjectural replacement is Tr(T~_g^{(N)})/HF(N)=vol(V)^{-1}∫_V g dvol_V+O(N^{-1}) for fixed smooth radical V, bihomogeneous projective g, and N→∞ through the stable range.
- depends-on: C-079, D-toeplitz-operator
- where-tested: checkers/explore/intersection_observables.py sections G and K.
```

### C-087

Status: **SKETCH**.

Paste:

```text
- statement: Relevant classical competitors are random slicing and averaging when a witness set for V is supplied, diagonal homotopy for intersections when witness sets for both varieties are supplied, and randomized trace estimation using sparse Krylov projector filters. Their costs depend on input representation, tracking condition, certification requirements, and the requested additive precision. No universal polynomial cost from sparse generators is claimed.
- status: SKETCH
- depends-on: C-055, C-170, D-condition-number, D-kostlan-random-form, D-intersection-overlap, D-normalised-toeplitz-operator
```

### C-166

Status: **CONJECTURE**.

Paste:

```text
- statement: For fixed homogeneous radical ideals I,J with smooth V,W intersecting transversely along a nonempty smooth pure-dimensional Z of complex dimension l, as N→∞ through the stable range,
  T_N(I,J)=(N/pi)^l ∫_Z prod_i sin^{-2}(theta_i(x)) dvol_Z(x) (1+O_{I,J}(N^{-1})),
  where T_N is D-intersection-overlap and the angles are those of D-intersection-angle-condition-number.
- status: CONJECTURE
- depends-on: C-026, C-028, C-079, D-intersection-overlap, D-intersection-angle-condition-number, D-bergman-frame-operator, D-saturation-regularity-stable-range
- where-tested: checkers/explore/intersection_observables.py sections A, C, D, and E (N1, N2, N5, N6).
```

### C-167

Status: **CONJECTURE**.

Paste:

```text
- statement: For fixed homogeneous radical ideals I,J with smooth disjoint V,W, as N→∞ through the stable range,
  T_N(I,J) ≤ HF_I(N) HF_J(N) cos^{2N}(d_FS(V,W))
  and -log T_N(I,J)/(2N) → log sec(d_FS(V,W)).
  Under the real Morse–Bott hypothesis of C-NEW-IO-DISTANCE the polynomial prefactor is N^{r/2}; consequently its logarithmic correction has sign -r log N/(4N).
- status: CONJECTURE
- depends-on: C-026, C-028, C-079, D-intersection-overlap, D-coherent-state, D-bergman-frame-operator, D-saturation-regularity-stable-range
- where-tested: checkers/explore/intersection_observables.py sections B and J (N4, N11).
```

### C-168

Status: **REFUTED**.

Paste:

```text
- status: REFUTED
- counterexample: Under D-toeplitz-operator, for the smooth conic and g=|z_2|^2, Tr(P_0T_g)/HF(N)=Tr(P_0n_2)/(HF(N)) grows linearly in N.
- surviving statement: Under the distinct D-normalised-toeplitz-operator, the conjectural replacement is Tr(T~_g^{(N)})/HF(N)=vol(V)^{-1}∫_V g dvol_V+O(N^{-1}) for fixed smooth radical V, bihomogeneous projective g, and N→∞ through the stable range. For the conic and g=|z_2|^2, the exact limit is -1/6+2 sqrt(3) pi/27 and the observed 1/N coefficient is approximately 0.03142.
- depends-on: C-079, D-toeplitz-operator
- where-tested: checkers/explore/intersection_observables.py sections G and K.
```

### Additional required DAG consequence: C-169

C-169 cannot continue to depend on C-168 after C-168 becomes REFUTED. Paste:

```text
- statement: The normalized overlap quantities in C-166 and C-167, and degree-normalized Toeplitz traces defined by D-normalised-toeplitz-operator, are DQC1-style estimable to additive epsilon subject to the access, preparation, and normalized-gap assumptions of D-dqc1-style-estimate.
- status: CONJECTURE
- depends-on: C-061, C-166, C-167, D-intersection-overlap, D-normalised-toeplitz-operator, D-dqc1-style-estimate
```

LOCKSTEP: NOT READY — the mathematical status changes are correct, but C-087, C-168, and C-169 require the dependency amendments above before merge.

VERDICT: FAIL(O9, O10, O11, O12, O13)