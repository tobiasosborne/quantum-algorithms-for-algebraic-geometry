<!-- ROLE: symbol table + convention conflicts for the campaign (rk-light law L2).
     Companion to definitions/definitions.md; ids there are authoritative.
     In tables, LaTeX uses \lvert \rvert \lVert \rVert so that no bare pipe breaks a row. -->

# Notation

"First used" points at the earliest occurrence in the seed: `report Lnn` is
`seed/analysis-2026-09-01/report.md`, `page81 Lnn` is `seed/page81.tex`.
Campaign conventions C1-C12 are stated at the top of `definitions/definitions.md`.

## 1. Spaces

| symbol | meaning | defined at | first used |
|---|---|---|---|
| $\mathbb C$, $\mathbb F_q$ | base field; finite field (only in the finite-field entry) | D-polynomial-ring, D-finite-field-analogue | report L9, L244 |
| $\mathbb P^n$, $\mathbb{CP}^n$ | complex projective $n$-space, $n+1$ homogeneous coordinates | D-variety | page81 L6 |
| $S^{2n+1}$ | unit sphere $\{z:\sum_j\lvert z_j\rvert^2=1\}$; page81 calls it $\mathbb{CP}^n$ | D-sphere-norm | page81 L6 |
| $R$ | the graded ring $\mathbb C[z_0,\dots,z_n]$ | D-polynomial-ring | report L9 |
| $R_N$ | degree-$N$ forms, $\dim=\binom{N+n}{n}$; page81's $h_N$, $\mathcal P_N$ | D-polynomial-ring | report L9, page81 L13 |
| $\mathcal F$ | Bargmann-Fock space, completion of $\bigoplus_NR_N$ in $\lVert\cdot\rVert_{\mathrm F}$ | D-fock-space | report L17 |
| $H^2_{n+1}$ | Drury-Arveson space (BW norm on the graded sum) | D-drury-arveson-space | report L53 |
| $H^2(S^{2n+1})$ | Hardy space of the sphere (sphere norm) | D-l2-cpn | report L23 |
| $\mathcal H$, $\mathcal H_R$ | page81's ambient space; = $\mathcal F$, resp. $\ell^2(\mathbb Z_{\ge0})^{\otimes(n+1)}$ | D-fock-space, D-shift-operator | page81 L315, L366 |
| $H^0(\mathbb P^n,\mathcal O(N))$ | global sections of $\mathcal O(N)$; $=R_N$ | D-symmetric-sector | report L20 |
| $\mathrm{Sym}^N(\mathbb C^{n+1})$ | symmetric subspace of $N$ qudits of dimension $n+1$ | D-symmetric-sector | report L20 |
| $R_{(1,\dots,1)}$ | multidegree-$(1,\dots,1)$ sector $=(\mathbb C^q)^{\otimes n}$ | D-multidegree-sector | report L92 |
| $\ell^2(\mathbb Z_{\ge0})$, $\ell^2(\mathbb Z)$ | single-mode space; its Laurent extension | D-shift-operator | page81 L367, L373 |
| $V$, $V(I)$, $W$ | projective variety of $I$ (never the ideal piece; C4) | D-variety | report L46 |
| $I$, $I_N$ | homogeneous ideal and its degree-$N$ piece; page81's $V_{(f_1,\dots,f_d)_N}$ | D-homogeneous-ideal | report L36, page81 L37 |
| $I(V)$ | vanishing ideal of $V$ | D-variety | report L90 |
| $I^{\mathrm{sat}}$, $\mathfrak m$ | saturation; irrelevant ideal $(z_0,\dots,z_n)$ | D-saturation-regularity-stable-range | report L167 |
| $(I_N)^\perp$ | Macaulay inverse system in degree $N$; the ground space | D-inverse-system | report L45, page81 L69 |
| $\mathrm{Syz}(I)_N$ | degree-$N$ syzygies of the tuple | D-syzygy-module | report L120 |
| $\mathrm{in}_w(I)$, $\mathrm{in}_w(f)$ | initial ideal / initial form for weight $w$ | D-initial-ideal | report L141 |

## 2. Ring elements, indices, degrees

| symbol | meaning | defined at | first used |
|---|---|---|---|
| $z_j$, $z^k$, $z^\alpha$ | variables and monomials, $k!=\prod_jk_j!$ | D-polynomial-ring | report L9 |
| $z_{i,s}$ | multigraded variables: site $i=1..n$, level $s=0..q-1$ | D-multidegree-sector | report L92 |
| $n$ | $n+1$ = number of variables; $\dim\mathbb P^n$ | D-polynomial-ring | page81 L6 |
| $N$ | total degree = boson number = sector label | D-polynomial-ring | page81 L17 |
| $d$ | number of generators (never the variable count; C9) | D-homogeneous-ideal | report L36 |
| $m_j$, $m$ | $\deg f_j$; a generic generator degree | D-homogeneous-ideal | report L36 |
| $k$, $l$, $\alpha$, $\beta$ | multi-indices in $\mathbb Z_{\ge0}^{n+1}$ (C7) | D-fock-basis | page81 L22 |
| $\alpha^{(j)}$ | exponent of the initial monomial of $g_j$ | D-groebner-deformation-path | report L226 |
| $f_j$, $f$, $g_j$ | generators / a form; $g_j$ a Grobner basis element | D-homogeneous-ideal, D-initial-ideal | page81 L37 |
| $f_\alpha$ | coefficient of $z^\alpha$ in $f$ | D-creation-of-form | report L25 |
| $h_j$, $h$ | multipliers in $\sum_jf_jh_j$ | D-homogeneous-ideal | page81 L40 |
| $u$, $q$ | elements of the inverse system / dual polynomials (C12) | D-inverse-system | page81 L71 |
| $\ell$ | a linear form (Fact 4.1 proof) | D-k-body | report L108 |
| $w$, $w_j$ | a weight vector; orthonormal linear forms after Takagi | D-initial-ideal, D-takagi-factorisation | report L141, L186 |
| $A$ | complex symmetric matrix of a quadric; also the $A$-grading matrix of a toric ideal; also a mode set | D-takagi-factorisation, D-toric-ideal, D-few-mode | report L186, L197, L110 |
| $c$ | codimension of $V$ | D-normalised-hilbert-function | report L138 |
| $D$ | $\deg V$ / scheme length / number of solutions (C8) | D-hilbert-function | report L138 |
| $\gamma_j$ | leading coefficient of $\mathrm{in}_w(g_j)$ (report writes $c_j$) | D-groebner-deformation-path | report L236 |
| $t$ | deformation parameter of the Grobner path (also the Motzkin weight in report L232) | D-groebner-deformation-path | report L141 |
| $q$ | local dimension in the multigraded setting (C12) | D-multidegree-sector | report L92 |
| $\mathrm{reg}(I)$ | Castelnuovo-Mumford regularity; stable range $N\ge\mathrm{reg}$ | D-saturation-regularity-stable-range | report L51 |
| $\mathrm{HF}_{R/I}(N)$ | Hilbert function $=\dim\ker H_N$ | D-hilbert-function | report L46 |
| $p_{R/I}$ | Hilbert polynomial | D-hilbert-function | report L51 |
| $\phi$ | a 3-CNF formula (typographically close to $\Phi_N$; never in the same display) | D-clause-ideal | report L167 |
| $J$, $K$ | boolean ideal; boolean-plus-clause ideal | D-boolean-ideal, D-clause-ideal | report L167 |
| standard monomials | basis of $(\mathrm{in}_w I)^\perp$; monomials not in a monomial ideal | D-monomial-ideal | report L141 |
| Kostlan-random form | $U(n+1)$-invariant Gaussian form, unit $\lVert\cdot\rVert_{\mathrm{BW}}$ | D-kostlan-random-form | report L230 |

## 3. Operators

| symbol | meaning | defined at | first used |
|---|---|---|---|
| $a_j^\dagger$, $a_j$ | $z_j\cdot$ and $\partial_j$, $[a_i,a_j^\dagger]=\delta_{ij}$ | D-mode-operators | page81 L48 |
| $\hat n_j$, $\hat N$ | number operators; degree operator (C8) | D-mode-operators | report L53, L72 |
| $a^\dagger(f)$, $M_f$, $L_f$ | multiplication by $f$ ($L_f$ is page81's name) | D-creation-of-form | page81 L92 |
| $a(f)$ | $\bar f(\partial)$, conjugated coefficients (C3) | D-annihilation-of-form | report L29 |
| $U_f$ | polar isometry of $M_f$, onto $(f)_N$ | D-multiplication-map | report L115 |
| $\Phi_N$ | Macaulay map $\bigoplus_jR_{N-m_j}\to R_N$ | D-macaulay-map | report L120 |
| $J_j$, $J^\alpha$, $\ell_j^\dagger$ | unilateral shifts, $a_j^\dagger=J_j\sqrt{\hat n_j+1}$ | D-shift-operator | page81 L53 |
| $S_j$ | Arveson shift $a_j^\dagger/\sqrt{\hat N+1}$ | D-drury-arveson-space | report L53 |
| $H$, $H_N$ | $\sum_ja^\dagger(f_j)a(f_j)$ and its degree-$N$ block | D-hamiltonian | page81 L130 |
| $H_u$ | toric fibre block of $H_N$ (a weighted graph Laplacian) | D-toric-ideal | report L197 |
| $H'$ | page81's Hamiltonian after adjoining $f$ (ambiguous there; OPEN-10) | D-parent-hamiltonian | page81 L208 |
| $P_0$, $P_{0,N}$ | projector onto $\ker H_N=(I_N)^\perp$ | D-projectors | report L51 |
| $P_{I_N}$, $\Theta(H_N)$ | projector onto $I_N$ (Heaviside of $H_N$) | D-projectors | report L49 |
| $P_{\mathrm{sym}}$ | projector onto the symmetric subspace | D-symmetric-sector | report L69 |
| $Z_j$ | compressed multiplication $P_{0,N+1}a_j^\dagger P_{0,N}$ | D-compressed-multiplication | report L51 |
| $X_j$, $\mu_{z_j}$ | $\mu_{z_0}^{-1}\mu_{z_j}$ on the stabilised quotient; multiplication on $R/I$ | D-compressed-multiplication | report L140 |
| $T_g$ | Toeplitz operator $P_0\,g(a^\dagger,a)\,P_0$, normal ordered | D-toeplitz-operator | report L161 |
| $T$ | a candidate positive local term (Facts 4.1/4.2); also the QSVT cost; also circuit length | D-k-body, D-qsvt, D-history-state | report L108, L130, L220 |
| $\mathrm{Mac}_N$ | Macaulay matrix of $\Phi_N$ in the monomial basis, $\mathrm{rank}=\dim I_N$ | D-macaulay-matrix | report L49 |
| $\mathrm{CG}$ | page81's $\sum_jJ^j\otimes\lvert j\rangle\langle j\rvert$ | D-shift-operator | page81 L427 |
| $\mathbb 1$ | identity operator (C6; page81 writes $\mathbb I$) | - | page81 L266 |

## 4. States

| symbol | meaning | defined at | first used |
|---|---|---|---|
| $\ker H_N$ | ground space $=(I_N)^\perp$, $\dim=\mathrm{HF}_{R/I}(N)$ | D-ground-space | page81 L125 |
| $\lvert k\rangle$ | Fock ONB $z^k/\sqrt{k!}$ (C1) | D-fock-basis | report L17 |
| $\lvert k\rangle_{\mathrm S}$ | page81's sphere ONB $\sqrt{(N+n)!/(k!n!)}\,z^k$ | D-sphere-norm | page81 L22 |
| $\lvert f\rangle$, $\lvert h\rangle$, $\lvert q\rangle$ | the polynomial $f$ viewed as a vector | D-fock-space | page81 L87 |
| $\lvert F\rangle$ | symmetric tensor of a form, $\lVert F\rVert=\lVert f\rVert_{\mathrm{BW}}$ | D-symmetric-tensor-of-a-form | report L62 |
| $\lvert p\rangle^{\otimes N}$ | spin-coherent state $(p\cdot z)^N/\sqrt{N!}$ | D-coherent-state | report L76 |
| $\hat p_x$ | boolean coherent label $(1,x)/\sqrt{1+\lvert x\rvert}$ | D-coherent-gram-matrix | report L240 |
| $\Psi$ | $\propto\sum_x\lvert\hat p_x\rangle^{\otimes N}$, the root-sampling initial state | D-coherent-gram-matrix | report L240 |
| $G$ | coherent-state Gram matrix | D-coherent-gram-matrix | report L154 |
| $q_u$ | toric fibre sum $\sum_{Ak=u}z^k/k!$ | D-toric-ideal | report L197 |
| $f_\pm$ | endpoint test states of the hardness sketch | D-distance-to-ideal-problem | report L220 |
| $\lvert\Sigma_N\rangle$ | uniform monomial superposition (page81's $R=\sum_\alpha\lvert\alpha\rangle$) | D-shift-operator | page81 L406 |

## 5. Spectral and metric quantities

| symbol | meaning | defined at | first used |
|---|---|---|---|
| $\lVert\cdot\rVert_{\mathrm F}$, $\lVert\cdot\rVert_{\mathrm{BW}}$, $\lVert\cdot\rVert_{\mathrm S}$ | Fock, Bombieri-Weyl, sphere norms; $\lVert f\rVert^2_{\mathrm F}=m!\lVert f\rVert^2_{\mathrm{BW}}$ | D-fock-space, D-bombieri-weyl-norm, D-sphere-norm, D-norm-comparison | report L11 |
| $\Delta_N$ | Macaulay gap, smallest nonzero eigenvalue of $H_N$ | D-macaulay-gap | report L123 |
| $\Delta_N(t)$ | gap along the Grobner path | D-groebner-deformation-path | report L141 |
| $\alpha_{\mathrm{BE}}$ | block-encoding normalisation (report writes $\alpha$; C7) | D-block-encoding-normalisation | report L127 |
| $\Delta_N/\alpha_{\mathrm{BE}}$ | normalised gap - the only promise-worthy quantity | D-normalised-gap | report L133 |
| $s_{\mathrm{row}}$ | row sparsity of $H_N$ (report writes $s$; C10) | D-block-encoding-normalisation | report L127 |
| $\sigma_{\min}$, $\sigma_{\max}$, $\lambda_2$ | singular values; second eigenvalue of a fibre Laplacian | D-macaulay-gap, D-toric-ideal | report L123, L197 |
| $\tau_j$, $\tau_{\min}$ | Takagi values (report writes $d_j,d_{\min}$; C9) | D-takagi-factorisation | report L186 |
| $\delta(f)$ | normalised distance to the ideal | D-distance-to-ideal | report L144 |
| $d_{FS}$ | Fubini-Study distance between varieties | D-bergman-projector | report L160 |
| $\mu_{\mathrm{norm}}$, $\mu_{\max}$ | Burgisser-Cucker condition numbers | D-condition-number | report L250 |
| $S(p)$ | scalar curvature in the Tian-Zelditch expansion | D-bergman-projector | report L159 |
| $\epsilon$, $\varepsilon$ | algorithmic precision; Gram-matrix closeness | D-qsvt, D-coherent-gram-matrix | report L130, L240 |
| $\kappa$ | the constant $c$ of Conjecture 8.3(a), $\inf_N\Delta_N\ge\kappa$ | D-macaulay-gap | report L226 |
| $\mathcal G_N(I)$ | adiabatic Grobner complexity | D-adiabatic-groebner-complexity | report L236 |

## 6. Complexity and algorithmic vocabulary

| symbol / term | meaning | defined at | first used |
|---|---|---|---|
| QSVT | quantum singular value transformation on a block encoding | D-qsvt | report L114 |
| block encoding | sparse-access encoding with normalisation $\alpha_{\mathrm{BE}}$ | D-block-encoding-normalisation | report L127 |
| promise gap | "$\ker\ne0$" vs "$\lambda_{\min}\ge1/\mathrm{poly}$" | D-quantum-k-sat | report L100 |
| $\mathrm{QMA}_1$ | one-sided-error QMA; QSAT/bosonic QSAT hardness class | D-quantum-k-sat, D-hard-core-generators | report L100 |
| BQP / FBQP | decision vs function class for the estimation problem | D-distance-to-ideal-problem, D-hardness-anchors | report L220, L167 |
| DQC1-style | trace estimation from a maximally mixed register (not DQC1 proper) | D-dqc1-style-estimate | report L138 |
| $\#\mathrm P$, NP, coNP, AM/coAM | hardness anchors for HF, kernel non-triviality, Nullstellensatz | D-hardness-anchors | report L167 |
| guided local Hamiltonian | ground-space overlap reading of $\delta(f)^2$ | D-distance-to-ideal | report L155 |
| Grover scaling | $\sqrt{2^n/D}$ upper bound of the projection root sampler | D-coherent-gram-matrix | report L240 |
| frustration free | $\ker\sum_jT_j=\bigcap_j\ker T_j\ne0$ | D-frustration-free | report L42 |
| $k$-body / few-mode | first- vs second-quantised locality | D-k-body, D-few-mode | report L106 |
| input model | poly-size generators, $N$ in unary, $O(n\log N)$ qubits | D-input-model | report L127 |
| Bose-Hubbard sense | on-site function of mode operators; the admissibility standard for few-mode terms | D-bose-hubbard | report L110 |
| Motzkin / hard-gap instances | 2-local frustration-free chains with $2^{-\Omega(n)}$ gap, embedded multigraded | D-hard-gap-instances | report L232 |
| spin-mixing realisation | the conic Hamiltonian as a spin-1 spinor BEC (Law-Pu-Bigelow) | D-spin-mixing-hamiltonian | report L72 |

---

## Conflicts

Every place where `page81.tex` and `report.md` use different conventions for the same object, or
where one symbol carries two meanings. "Chosen" is binding for the campaign (see C1-C12).

| # | object | page81 | seed report | chosen convention |
|---|---|---|---|---|
| 1 | degree-$N$ piece of the ideal | $V_{(f_1,\dots,f_d)_N}$ (a vector space) | $I_N$; $V$ means the variety | $I_N$ for the space, $V(I)$ for the variety; never $V_I$ (C4) |
| 2 | orthonormal basis of $R_N$ | sphere ONB $\sqrt{(N+n)!/(k!n!)}z^k$ (L22), but computations in bare monomials $z^k$ (L179-195) | Fock ONB $z^k/\sqrt{k!}$ | Fock (C1); monomial-basis statements written as $z^k$, never as $\lvert k\rangle$ (OPEN-8) |
| 3 | ambient Hilbert space | "$L^2(\mathbb{CP}^n)$" | Hardy/Drury-Arveson/symmetric Fock, per norm | $\mathcal F$ with the Fock norm; $L^2(\mathbb{CP}^n)$ is a different, non-holomorphic space (D-l2-cpn) |
| 4 | the unit sphere | called $\mathbb{CP}^n$ (L6) | $S^{2n+1}$, with $\mathbb{CP}^n=S^{2n+1}/U(1)$ | $S^{2n+1}$ for the sphere |
| 5 | qudit dimension | $n$ (L9) | $n+1$ | $n+1$ (C2) |
| 6 | annihilation by a form | $f(\partial)$, unconjugated (L119, L140) | $\bar f(\partial)$ | conjugated (C3); page81 agrees only for real coefficients |
| 7 | multiplication by $f$ | $L_f$ (L269, L419) | $a^\dagger(f)$, $M_f$ | $a^\dagger(f)$ on $\mathcal F$, $M_f$ when the grading matters |
| 8 | shift operators | $\ell_j^\dagger,\ell_j$, with "$\ell_j\propto a_j$" (L65) | $J_j$, with $a_j^\dagger=J_j\sqrt{\hat n_j+1}$ | $J_j$; the proportionality claim is withdrawn (OPEN-9) |
| 9 | graded piece | $h_N$ (L13), also $\mathcal P_d$ (L348) | $R_N$ | $R_N$; $h$, $h_j$ are multipliers only |
| 10 | identity operator | $\mathbb I$ (L266), while $I$ is the ideal (L238) | $\mathbb 1$ | $\mathbb 1$ for the identity, $I$ for the ideal (C6) |
| 11 | the ring / a uniform state | $R$ is both the ring (L385) and $\sum_\alpha\lvert\alpha\rangle$ (L406) | $R$ is the ring | $R$ = ring; the superposition is $\lvert\Sigma_N\rangle$ |
| 12 | block-encoding normalisation | - | $\alpha$, colliding with the multi-index $\alpha$ (L25 vs L127) | $\alpha_{\mathrm{BE}}$; $\alpha,\beta$ stay multi-indices (C7) |
| 13 | degree operator | - | $D$ (L15), colliding with $D=\deg V$ (L138) and $D=\#$solutions (L240) | $\hat N$ for the operator; $D$ for degree/length (C8) |
| 14 | Takagi values | - | $d_j$, $d_{\min}$ (L186), colliding with $d$ = number of generators (L36) and Arveson's $d$-shift (L53) | $\tau_j$, $\tau_{\min}$; $d$ = number of generators; "the $(n+1)$-shift" (C9) |
| 15 | row sparsity vs level index | - | $s$ is both (L127 vs L92); $s$ is also the Motzkin parameter (L232) | $s_{\mathrm{row}}$ for sparsity; $s$ = level index (C10) |
| 16 | chain length | - | $m$ (L214), colliding with $m$ = generator degree (L36) | $L$ for chain length; $m$ = degree |
| 17 | the letter $p$ | $p(z)$, $q(z)$ are polynomials (L35, L71) | $p$ is a point / coherent-state label (L76); also the Schatten exponent (L53) and the characteristic (L244) | $p$ = point; polynomials are $f,g,h,u$; "Schatten-$p$" only as a phrase (C11, C12) |
| 18 | the letter $q$ | $q(z)$, a dual polynomial (L71) | $q$ = local dimension (L92); $\mathbb F_q$ (L244) | $q$ = local dimension in multigraded contexts, $u$ for dual polynomials, $\mathbb F_q$ kept (C12) |

Two further mismatches are recorded as OPEN issues rather than conventions, because choosing a
convention does not settle them: the generator normalisation used in the report's gap survey
(OPEN-1, OPEN-2) and the choice between $\Delta_N/\alpha_{\mathrm{BE}}$ and $\lVert H_N\rVert/\Delta_N$
as the reported figure of merit (OPEN-3).
