<!-- ROLE: single-source definitions register (rk-light law L2). Every symbol and object used in
     seed/page81.tex or seed/analysis-2026-09-01/report.md has exactly one entry here.
     UPDATE POLICY: artifacts cite ids, never redefine. Amend only by orchestrator merge. -->

# Definitions register

Ids are stable: cite them as `D-<slug>`. Line references are to the files as committed:
`seed/analysis-2026-09-01/report.md` (cited "report Lnn") and `seed/page81.tex` (cited "page81 Lnn").
The seed report is a proposer document, not established truth; entries record what it *defines*,
and the Pitfalls lines record where the definition is fragile or where a referee objected.

## Frozen conventions

These are campaign choices. Every entry below is written in them; every artifact must state
explicitly when it departs.

- **C1 (inner product).** The Bargmann-Fock/Fischer inner product is the default (D-fock-space).
  Bombieri-Weyl and sphere norms appear only via D-norm-comparison, never silently.
- **C2 (variables).** $n+1$ variables $z_0,\dots,z_n$; ambient projective space $\mathbb P^n$;
  local qudit dimension $n+1$ (report L20, correcting page81 L9).
- **C3 (conjugation).** $a(f)=\bar f(\partial)$, conjugated coefficients (D-annihilation-of-form).
  Points of $V$ carry coherent states of the *conjugate* vector (D-coherent-state).
- **C4 (ideal piece vs variety).** $I_N$ is the degree-$N$ piece of the ideal; $V(I)$ is the variety.
  page81's $V_{(f_1,\dots,f_d)_N}$ is $I_N$ and is never written $V$ in this campaign.
- **C5 (generator normalisation).** Gap statements are made for **unit Bombieri-Weyl generators**,
  $\|f_j\|_{\mathrm{BW}}=1$, equivalently $\|f_j\|^2_{\mathrm{Fock}}=m_j!$ (D-macaulay-gap).
  Any other presentation must be stated; the seed's numerical survey does *not* use it (see OPEN-1).
- **C6 (identity).** $\mathbb 1$ for the identity operator; $I$ is always an ideal (page81 writes
  $\mathbb I$ for identity and $I$ for the ideal; keep the ideal, change the identity symbol).
- **C7 (block-encoding normalisation).** Written $\alpha_{\mathrm{BE}}$, never $\alpha$;
  $\alpha,\beta$ are reserved for multi-indices (D-block-encoding-normalisation).
- **C8 (degree operator).** $\hat N=\sum_j\hat n_j$; the letter $D$ is reserved for $\deg V$ /
  scheme length (report L15 writes $D$ for the degree operator; do not).
- **C9 (Takagi values).** $\tau_1\ge\dots\ge\tau_{n+1}\ge0$, $\tau_{\min}$; the report's $d_j,d_{\min}$
  collide with $d=$ number of generators (D-takagi-factorisation).
- **C10 (row sparsity).** $s_{\mathrm{row}}$; the bare $s$ is the level index of $z_{i,s}$.
- **C11 (Schatten).** "Schatten-$p$" only as a fixed phrase; the symbol $p$ is a point of
  $\mathbb C^{n+1}$ / a coherent-state label, never a polynomial and never an exponent.
- **C12 (dual polynomials).** Elements of the inverse system are $u,q$; in multigraded contexts
  $q$ is the local dimension, so use $u$ there. $\mathbb F_q$ keeps $q$ (finite fields appear only
  in D-finite-field-analogue, a disjoint context).

---

## A. Ambient spaces, bases, norms

### D-polynomial-ring
$$R=\mathbb C[z_0,\dots,z_n]=\bigoplus_{N\ge0}R_N,$$
the graded ring in $n+1$ variables. $R_N$ is the space of homogeneous polynomials (forms) of
degree $N$, $\dim R_N=\binom{N+n}{n}$; $R_0=\mathbb C$. Multi-index notation
$z^k=z_0^{k_0}\cdots z_n^{k_n}$, $|k|=\sum_jk_j$, $k!=\prod_jk_j!$.
Source: report §1 L9; page81 L13-L19 (as $h_N$), L37.
Pitfalls: $n+1$ variables, not $n$ (C2). page81 writes $h_N$ for $R_N$ and also $h,h_j$ for
multipliers; the campaign writes $R_N$ for the graded piece and reserves $h$ for multipliers.

### D-fock-space
The Bargmann-Fock (Fischer, Segal-Bargmann) space of the $n+1$ bosonic modes: polynomials with
$$\langle z^k,z^l\rangle_{\mathrm F}=k!\,\delta_{kl},\qquad
\mathcal F=\overline{\bigoplus_{N\ge0}R_N}^{\ \|\cdot\|_{\mathrm F}},$$
the completion of $R$; equivalently $L^2$-holomorphic functions for the Gaussian measure
$\pi^{-(n+1)}e^{-\|z\|^2}dV$ on $\mathbb C^{n+1}$. Conjugate-linear in the first argument.
$R_N$ is the $N$-boson sector.
Source: report §1 L17; standard (Bargmann 1961; Fischer 1918) [UNVERIFIED ids].
Pitfalls: $\mathcal F$ is *not* $L^2(\mathbb{CP}^n)$ and not the Hardy space; see D-l2-cpn and
D-norm-comparison. All three candidate inner products agree degreewise up to a scalar but give
different Hilbert modules across degrees (referee round1 #1).

### D-fock-basis
$$|k\rangle:=\frac{z^k}{\sqrt{k!}},\qquad \langle k|l\rangle=\delta_{kl},\qquad k\in\mathbb Z_{\ge0}^{n+1}.$$
$\{|k\rangle:|k|=N\}$ is an orthonormal basis of $R_N$.
Source: report §1 L17; numerics `bf.py` docstring; page81 L22-L26 uses a different normalisation
(D-sphere-norm).
Pitfalls: page81's computations (L179-L195) are done in the *unnormalised* monomial basis
$|k\rangle\leftrightarrow z^k$, not in either normalised basis; see OPEN-8.

### D-sphere-norm
The normalised-surface-measure inner product of $S^{2n+1}$, i.e. page81's convention:
$$\langle z^k,z^l\rangle_{\mathrm S}=\int_{S^{2n+1}}\overline{z^k}\,z^l\,d\sigma
=\delta_{kl}\,\frac{n!\,k!}{(|k|+n)!},\qquad
|k\rangle_{\mathrm S}=\sqrt{\frac{(N+n)!}{k!\,n!}}\;z^k\ \ (N=|k|).$$
The adjoint of multiplication by $z_j$ is $\partial_j(\hat N+n)^{-1}$ (act with $(\hat N+n)^{-1}$
first, i.e. divide by $N+n$ on $R_N$).
Source: page81 L22-L33; report §1 L15, §9 L256.
Pitfalls: $\bar z^kz^l$ descends to $\mathbb{CP}^n$ only for $|k|=|l|$; the integral is over the
sphere, with different degrees orthogonal by $U(1)$-averaging. The page81 basis is the sphere-ONB,
but the page then computes in monomials (OPEN-8).

### D-bombieri-weyl-norm
The Bombieri-Weyl (Kostlan, Drury-Arveson, apolar) norm:
$$\langle z^k,z^l\rangle_{\mathrm{BW}}=\delta_{kl}\frac{k!}{N!}\ \ (N=|k|),\qquad
\|f\|^2_{\mathrm{BW}}=\sum_\alpha|f_\alpha|^2\frac{\alpha!}{m!}\ \ (\deg f=m).$$
It is $U(n+1)$-invariant: $\|f\circ U\|_{\mathrm{BW}}=\|f\|_{\mathrm{BW}}$ for unitary $U$.
For a quadric $f=z^{\mathsf T}Az$ with $A$ complex symmetric, $\|f\|_{\mathrm{BW}}=\|A\|_{\mathrm F}$.
Source: report §1 L14, §3 L63, §7 L198.
Pitfalls: the natural tensor norm of D-symmetric-tensor-of-a-form, and the norm in which
generators are normalised (C5) - but *not* the norm in which $H_N$ is built (C1).

### D-norm-comparison
On a fixed $R_N$ the three inner products are proportional:
$$\langle\cdot,\cdot\rangle_{\mathrm{BW}}=\frac{1}{N!}\langle\cdot,\cdot\rangle_{\mathrm F},\qquad
\langle\cdot,\cdot\rangle_{\mathrm S}=\frac{n!}{(N+n)!}\langle\cdot,\cdot\rangle_{\mathrm F}
=\binom{N+n}{n}^{-1}\langle\cdot,\cdot\rangle_{\mathrm{BW}}.$$
Hence for $f$ of degree $m$: $\|f\|^2_{\mathrm F}=m!\,\|f\|^2_{\mathrm{BW}}$. Orthogonal
complements, kernels of homogeneous differential operators, orthogonal projectors and ground
spaces *within one degree* coincide in all three. Across degrees they are different Hilbert
modules: the graded sum is $\mathcal F$ (Fock), $H^2_{n+1}$ (BW, D-drury-arveson-space) or
$H^2(S^{2n+1})$ (sphere), and boundedness of the shifts, curvature and essential normality are
statements about the choice.
The adjoint of $M_f:R_{N-m}\to R_N$ (D-multiplication-map) is
$$M_f^{*_{\mathrm F}}=\bar f(\partial),\qquad
M_f^{*_{\mathrm{BW}}}=\tfrac{(N-m)!}{N!}\bar f(\partial),\qquad
M_f^{*_{\mathrm S}}=\tfrac{(N-m+n)!}{(N+n)!}\bar f(\partial),$$
so $H_N$ and therefore $\Delta_N$ carry a convention-dependent degree factor:
$\Delta_N^{\mathrm{BW}}=\binom{N}{m}^{-1}\frac{1}{m!}\Delta_N^{\mathrm F}$ for one generator of degree $m$.
Source: report §1 L11-L17, §9 L256; referee round1 #1.
Pitfalls: "the norms agree" is false; they agree *degreewise up to a scalar*. Absolute gap
statements (D-macaulay-gap, Fact 7.1) are Fock statements; the normalised gap
$\Delta_N/\alpha_{\mathrm{BE}}$ is invariant under the choice because $\alpha_{\mathrm{BE}}$
rescales with $H_N$.

### D-l2-cpn
page81's $L^2(\mathbb{CP}^n)=\bigoplus_{N\ge0}h_N$ is *not* the $L^2$ space of the projective
space. The correct reading is the graded sum of spaces of holomorphic sections,
$$h_N=H^0(\mathbb P^n,\mathcal O(N))=R_N,$$
i.e. the Hardy space of $S^{2n+1}$ (sphere norm), the Drury-Arveson space (BW norm), or symmetric
Fock space (Fock norm), depending on the norm chosen. Genuine $L^2(\mathbb{CP}^n)$ is
non-holomorphic and decomposes into $(p,q)$-harmonic pieces, not into $\bigoplus_N R_N$.
Source: page81 L13; report §1 L23, §9 L255.
Pitfalls: also $\{z:\sum_j|z_j|^2=1\}=S^{2n+1}$, not $\mathbb{CP}^n$ (page81 L5-L7, report §9 L254);
$\mathbb{CP}^n=S^{2n+1}/U(1)$.

### D-symmetric-sector
The unitary identification (Fock norm on the left, tensor norm on the right)
$$R_N\;\cong\;\mathrm{Sym}^N(\mathbb C^{n+1})\;=\;H^0(\mathbb P^n,\mathcal O(N)),\qquad
|k\rangle\mapsto \text{normalised symmetrisation of }|0\rangle^{\otimes k_0}\cdots|n\rangle^{\otimes k_n},$$
the symmetric subspace of $N$ qudits of dimension $n+1$; equivalently the ambient space of the
$N$-th Veronese embedding of $\mathbb P^n$.
Source: report §1 L20, §3 L59.
Pitfalls: local dimension $n+1$, not $n$ (C2). The identification is unitary only for the Fock
norm on $R_N$ with the standard tensor norm on $\mathrm{Sym}^N$.

### D-symmetric-tensor-of-a-form
For $f=\sum_\alpha f_\alpha z^\alpha$ of degree $m$, the corresponding symmetric tensor is
$$|F\rangle=\sum_\alpha f_\alpha\frac{\alpha!}{m!}\!\!\sum_{w:\ \mathrm{content}(w)=\alpha}\!\!|w\rangle
\in\mathrm{Sym}^m(\mathbb C^{n+1}),\qquad
\langle F|F\rangle=\sum_\alpha|f_\alpha|^2\frac{\alpha!}{m!}=\|f\|^2_{\mathrm{BW}},$$
the sum over words $w\in\{0,\dots,n\}^m$ of content $\alpha$ (there are $m!/\alpha!$ of them).
Source: report §3 L62-L63; referee round1 #4, #6.
Pitfalls: $|F\rangle\langle F|$ is a projector only if $\|f\|_{\mathrm{BW}}=1$; otherwise it is
$\|f\|^2_{\mathrm{BW}}$ times a rank-one projector, which matters for every endpoint gap quoted
in terms of it.

### D-drury-arveson-space
$H^2_{n+1}=\bigoplus_NR_N$ completed in the Bombieri-Weyl norm; the $(n+1)$-shift is the
contraction
$$S_j=\frac{a_j^\dagger}{\sqrt{\hat N+1}}\qquad\text{(on }R_N:\ a_j^\dagger/\sqrt{N+1}).$$
A homogeneous ideal closes to a graded submodule $[I]$, and $\bigoplus_N(I_N)^\perp$ is the
quotient module $H^2_{n+1}/[I]$ carrying the compressed shifts.
Source: report §2 L53; referee round1 #2.
Pitfalls: Arveson-Douglas statements are about the *normalised bounded* shifts $S_j$, not about
the unbounded Fock $a_j^\dagger$; and the space is $H^2_{n+1}$ ($n+1$ variables), not $H^2_n$.
The report's "Arveson's $d$-shift" uses $d=n+1$, colliding with $d=$ number of generators (C9).

---

## B. Operators

### D-mode-operators
$$a_j^\dagger=\text{multiplication by }z_j,\qquad a_j=\partial_j,\qquad [a_i,a_j^\dagger]=\delta_{ij},$$
adjoints in the Fock inner product (C1). Number operators $\hat n_j=a_j^\dagger a_j=z_j\partial_j$,
$\hat n_j|k\rangle=k_j|k\rangle$; total number / degree operator $\hat N=\sum_j\hat n_j$,
$\hat N|_{R_N}=N$.
Source: page81 L48; report §1 L17.
Pitfalls: page81's $\ell_j,\ell_j^\dagger$ are the *shifts* (D-shift-operator), not $a_j,a_j^\dagger$;
"$\ell_j\propto a_j$" (page81 L65) is not an operator identity (OPEN-9). Use $\hat N$, not $D$, for
the degree operator (C8).

### D-creation-of-form
For $f=\sum_\alpha f_\alpha z^\alpha$ homogeneous of degree $m$,
$$a^\dagger(f)=f(a^\dagger)=\sum_\alpha f_\alpha (a_0^\dagger)^{\alpha_0}\cdots(a_n^\dagger)^{\alpha_n}
=\text{multiplication by }f,$$
mapping $R_L\to R_{L+m}$. Written $M_f$ when the domain and codomain matter (D-multiplication-map).
Source: page81 L92-L94; report §1 L28.
Pitfalls: page81's $L_f$ is the same operator; the campaign writes $a^\dagger(f)$ or $M_f$, never
$L_f$. It is unbounded on $\mathcal F$; its bounded normalisation is the D-drury-arveson-space shift.

### D-annihilation-of-form
$$a(f):=a^\dagger(f)^\dagger=\bar f(\partial)=\sum_\alpha\overline{f_\alpha}\,\partial^\alpha,$$
mapping $R_L\to R_{L-m}$. Conjugation of the coefficients is forced by taking the Fock adjoint of
$a^\dagger(f)$; without it $H$ is not $\sum_j a^\dagger(f_j)a(f_j)$ and need not be positive.
Source: report §1 L29, §9 L256; page81 L119, L140 (written $f(\partial)$, no conjugation).
Pitfalls: C3. Agrees with page81 only for real coefficients. In the sphere convention the adjoint
of $a^\dagger(f)$ carries an extra positive scalar (D-norm-comparison), harmless within a fixed
degree, fatal for absolute gap statements. In characteristic $p$ ordinary differentiation fails and
must be replaced by divided powers/contraction (D-finite-field-analogue).

### D-multiplication-map
$M_f:R_{N-m}\to R_N$, $h\mapsto fh$, the degree-graded restriction of $a^\dagger(f)$. Polar
decomposition $M_f=U_f|M_f|$ with $U_f$ an isometry of $R_{N-m}$ onto $(f)_N$ (the "unitary version
of $L_f^\dagger$" asked for in page81 L272); $U_f$ is a QSVT singular-value transformation of
$M_f$ at cost set by $\sigma_{\max}(M_f)/\sigma_{\min}(M_f)=O(N^{m/2})$ via Fact 7.1.
Source: report §4 L115; page81 L272.
Pitfalls: $U_f$ is an isometry, not a unitary on $R_N$; the polar isometry exists only because
$M_f$ is injective (no principal syzygies).

### D-macaulay-map
$$\Phi_N:\bigoplus_{j=1}^dR_{N-m_j}\longrightarrow R_N,\qquad (h_1,\dots,h_d)\mapsto\sum_jf_jh_j,$$
in Fock norms, with $\|(h_j)\|^2=\sum_j\|h_j\|^2$. Then $\operatorname{ran}\Phi_N=I_N$,
$\ker\Phi_N=\mathrm{Syz}(I)_N$ and $H_N=\Phi_N\Phi_N^\dagger$.
Source: report §5 L120.
Pitfalls: $\Phi_N$ depends on the *tuple* $(f_1,\dots,f_d)$, not on $I$; so do its singular values
and hence D-macaulay-gap. Not to be confused with the CNF formula $\phi$ of report L167.

### D-macaulay-matrix
The matrix of $\Phi_N$ in the monomial basis: rows indexed by $(j,\beta)$ with
$|\beta|=N-m_j$, entries the coefficients of $z^\beta f_j$. Its rank is $\dim I_N$; the numerics
compute it independently of $H_N$ (exact rank over $\mathbb Q$ or $\mathbb F_p$) as a cross-check.
Source: report §2 L49, §5 L118; numerics `bf.py:macaulay_rows`, `rank_mod_p`.
Pitfalls: the *unnormalised* monomial basis is used for the rank computation; the Fock-normalised
basis is used for the spectrum. Rank is basis independent, singular values are not.

### D-syzygy-module
$\mathrm{Syz}(I)_N=\ker\Phi_N=\{(h_j)\in\bigoplus_jR_{N-m_j}:\sum_jf_jh_j=0\}$, the degree-$N$ part
of the first syzygy module of the tuple $(f_1,\dots,f_d)$ (shifted grading).
Source: report §5 L120, §7 L179.
Pitfalls: a property of the tuple, not of the ideal. Adding a redundant generator adds syzygies and
changes $\Delta_N$.

### D-shift-operator
The unilateral shifts on $\ell^2(\mathbb Z_{\ge0})$ per mode,
$$J_j|k\rangle=|k+e_j\rangle,\qquad J_j^\dagger|k\rangle=|k-e_j\rangle\ (k_j\ge1),\qquad
a_j^\dagger=J_j\sqrt{\hat n_j+1},$$
i.e. $J_j$ is the isometric part of $a_j^\dagger$. page81's $\ell_j^\dagger,\ell_j$ are $J_j,J_j^\dagger$.
Source: page81 L53-L61, L357-L361, L519; report §4 L116.
Pitfalls: a *graded* subspace invariant under all $a_j^\dagger$ is exactly a homogeneous ideal;
invariance under the $J_j$ is a different condition, since $\sqrt{\hat n_j+1}$ does not preserve a
general ideal (referee round2 #5). Without the grading the invariant-subspace lattice is strictly
larger (Beurling $\theta H^2$ already for $n=0$) - "ideals are exactly the closed invariant
subspaces" is false (referee round1 #17). Passing to $\ell^2(\mathbb Z)$ (Laurent polynomials,
page81 L373) makes the shifts unitary but destroys the positive grading and the Fock structure.

### D-compressed-multiplication
On the ground spaces, $Z_j:=P_{0,N+1}\,a_j^\dagger\,P_{0,N}$ is multiplication by $z_j$ transported
through the isomorphism $(R/I)_N\cong(I_N)^\perp$ of D-inverse-system. For $I$ saturated,
$R/I$ a zero-dimensional scheme of length $D$ and $z_0$ a non-zero-divisor, on the stabilised
ground space ($N\ge\mathrm{reg}$)
$$X_j:=\mu_{z_0}^{-1}\mu_{z_j}\ \text{on }(R/I)_N,\ \text{transported to }(I_N)^\perp,
\qquad Z_j=Z_0X_j,$$
and the eigenvalues of $X_j$ are the $j$-th affine coordinates of the points of $V$
(Stickelberger), with Jordan blocks at non-reduced points.
Source: report §5 task 4 L140; referee round1 #24, #25, round2 #18.
Pitfalls: $X_j$ and $Z_j$ act on different spaces until the transport is fixed. Needs
zero-dimensionality, saturation and $z_0$ a non-zero-divisor; for positive-dimensional $V$,
$\mu_{z_0}$ is not invertible. The $X_j$ commute but are not normal, so phase estimation does not
apply; conditioning is pseudospectral, not coordinate separation (referee round1 #26, #63).
Stable $\mathrm{HF}$ is the scheme length $D=\deg(R/I)$, equal to $\#V$ only for reduced points.

---

## C. Ideals, varieties, invariants

### D-homogeneous-ideal
For homogeneous $f_1,\dots,f_d$ with $\deg f_j=m_j$, $I=(f_1,\dots,f_d)\subseteq R$ and
$$I_N=\Big\{\sum_{j=1}^df_jh_j:\ h_j\in R_{N-m_j}\Big\}=\sum_jf_jR_{N-m_j}\subseteq R_N,$$
the degree-$N$ graded piece. $I=\bigoplus_NI_N$.
Source: page81 L37-L44 (written $(f_1,\dots,f_d)_N$ and $V_{(f_1,\dots,f_d)_N}$); report §2 L36.
Pitfalls: C4 - page81's $V_{(\cdot)_N}$ is this vector space, not a variety. $I_N$ is a *span*
(an OR-type condition), which is the source of the parent-Hamiltonian obstruction (D-parent-hamiltonian).

### D-variety
$V(I)=\{[z]\in\mathbb P^n: f(z)=0\ \forall f\in I\}$, the projective variety of $I$;
$V(I_N)=V(I)$ for $N\ge\max_jm_j$. The vanishing ideal of a set $V$ is
$I(V)=\{f: f|_V=0\}$; $I\subseteq I(V)=\sqrt{I^{\mathrm{sat}}}$ for $V=V(I)$.
Source: report §3 L79, L90; page81 L202 (implicit, "ideal membership").
Pitfalls: C4. $I_N=I(V)_N$ in one degree does not make $I$ radical or saturated; radicality and
saturation are statements for all large $N$ (referee round1 #10).

### D-saturation-regularity-stable-range
$I^{\mathrm{sat}}=\{f:\mathfrak m^kf\subseteq I\text{ for some }k\}$ with $\mathfrak m=(z_0,\dots,z_n)$;
$\mathrm{reg}(I)$ is Castelnuovo-Mumford regularity. The **stable range** is $N\ge\mathrm{reg}$,
where $\mathrm{HF}_{R/I}(N)$ equals the Hilbert polynomial, irrelevant ($\mathfrak m$-primary)
torsion has vanished and $I_N=(I^{\mathrm{sat}})_N$.
Source: report §5 L140, §8.5 L238, §8.7 L242; referee round1 #34.
Pitfalls: "$N\ge\mathrm{poly}(n)$" does not by itself place an input in the stable range
(referee round1 #65); regularity must be bounded as part of the input promise.

### D-hilbert-function
$\mathrm{HF}_{R/I}(N)=\dim_{\mathbb C}(R/I)_N=\binom{N+n}{n}-\dim I_N$. For $N\ge\mathrm{reg}$ it
agrees with the Hilbert polynomial $p_{R/I}$, whose degree is $\dim V(I)$ and whose leading
coefficient is $\deg V/(\dim V)!$; for zero-dimensional saturated $I$ it stabilises at the scheme
length $D=\deg(R/I)$.
Source: report §2 L46, L51; §5 L138, L140.
Pitfalls: exact evaluation is $\#\mathrm P$-hard (D-boolean-ideal, D-clause-ideal); only the
normalised additive version is a realistic target (D-normalised-hilbert-function).

### D-normalised-hilbert-function
$$\frac{\mathrm{HF}_{R/I}(N)}{\dim R_N}=\frac{\operatorname{Tr}P_0}{\binom{N+n}{n}},\qquad
\text{for }\operatorname{codim}V=c,\ \deg V=D,\ N\text{ stable}:\quad
\frac{\mathrm{HF}(N)}{\dim R_N}\approx D\,\frac{n!}{(n-c)!}\,N^{-c}.$$
Source: report §5 task 2 L138; §8.7 L242.
Pitfalls: informative only for $c=O(1)$, and only if the additive error is below
$\tfrac12\frac{n!}{(n-c)!}N^{-c}$ after controlling lower-order terms (referee round1 #66).

### D-inverse-system
The Macaulay inverse system (apolar dual) in degree $N$:
$$(I_N)^\perp=\{u\in R_N:\ \bar f(\partial)u=0\ \ \forall f\in I\}
=\bigcap_j\ker a(f_j)|_{R_N},$$
the orthogonal complement of $I_N$ in $R_N$; it is the degree-$N$ part of the inverse system of
$\bar I$ (the ideal with conjugated coefficients). The map $(R/I)_N\to(I_N)^\perp$,
$[u]\mapsto P_0u$, is a linear isomorphism, so the ground space *is* the graded quotient ring as a
vector space, with multiplication realised by D-compressed-multiplication.
Source: report §2 L45, L51; page81 L69-L75 (as $V^\perp_{(f_1,\dots,f_d)_N}$); standard
(Macaulay 1916; Iarrobino-Kanev, Springer LNM 1721, 1999 [UNVERIFIED DOI]).
Pitfalls: it is the inverse system of $\bar I$, not of $I$, because the Fock pairing is Hermitian
(C3). For a principal ideal $R_N=fR_{N-m}\oplus\ker\bar f(\partial)$ is Fischer's decomposition;
calling the general orthogonal splitting "Fischer decomposition" overstates the terminology
(referee round1 #3).

### D-monomial-ideal
$I$ generated by monomials $z^{\alpha^{(j)}}$. Then $H_N$ is diagonal in the Fock basis with entries
$$\langle k|H_N|k\rangle=\sum_j\prod_i\frac{k_i!}{(k_i-\alpha^{(j)}_i)!}\ \ (\text{terms with }k\ge\alpha^{(j)}),$$
integer-valued, so $\Delta_N\ge1$ for monic monomial generators; the ground space is spanned by the
**standard monomials** (those not in $I$).
Source: report §7 L196; §8.3(a) L226.
Pitfalls: monomial ideals do *not* admit fixed-$k$-body parents for $I_N$ (referee round1 #14,
report §9 L259): for $I=(z_0)$ the projector onto $(I_N)^\perp$ is $(\mathbb 1-|0\rangle\langle0|)^{\otimes N}$,
which is $N$-body; $\theta(\hat n_0)$ is diagonal but not fixed-body. With unit-BW normalisation
(C5) a degree-$m$ monomial has $\|z^\alpha\|^2_{\mathrm F}=m!$, so the bound is $\min_jm_j!$, not
$\min_j\alpha^{(j)}!$ (OPEN-2).

### D-toric-ideal
A binomial (toric) ideal $I_A$ for an integer matrix $A$: $H_N$ is block diagonal over the fibres
$\{k:Ak=u\}$ of the $A$-grading, each block a weighted graph Laplacian on the fibre with
one-dimensional kernel spanned by the fibre sum
$$q_u=\sum_{Ak=u}\frac{z^k}{k!},$$
so $\mathrm{HF}(N)=\#\{\text{fibres in degree }N\}$ and $\Delta_N=\min_u\lambda_2(H_u)$, a weighted
Poincare constant of the fibre graphs.
Source: report §7 L197; numerics `task4_toric.py`.
Pitfalls: growth of $\Delta_N$ is not automatic: the pyramid ideal $(x_{00}x_{11}-x_{01}x_{10})$
with an unused apex variable $y$ has $\Delta_N=2$ for all $N$ (D-cone).

### D-boolean-ideal
$$J=(z_i^2-z_iz_0)_{i=1}^n\subseteq\mathbb C[z_0,\dots,z_n],$$
a radical saturated complete intersection of $n$ quadrics with
$\mathrm{HF}_{R/J}(N)=\sum_{i\le\min(N,n)}\binom ni$, equal to $2^n$ for $N\ge n$; $(R/J)_N$ is the
full function algebra on $\{0,1\}^n$ (points $[1:x]$, $x\in\{0,1\}^n$) for $N\ge n$.
Source: report §6 L167; §9 L261; numerics `task8_cnf.py`.
Pitfalls: stabilisation at $N=n$, not $n+1$ (report §9 L261 correcting page-level confusion).
Its gap is numerically $2$ for $n\le6$ only; not a theorem (referee round1 #44).

### D-clause-ideal
$K=J+(\text{homogenised cubic clause forms of a 3-CNF }\phi)$, a clause form vanishing at $[1:x]$
iff the clause is satisfied. Then $\mathrm{HF}_{R/K}(N)=\#\mathrm{SAT}(\phi)$ for $N\ge n+3$, and
$V(K)=\{[1:x]:x\models\phi\}$.
Source: report §6 L167; §8.6 L240.
Pitfalls: the homogeneous $K$ is generally neither radical nor saturated (irrelevant torsion);
only the dehomogenisation is radical (referee round1 #34). Below $N=n+3$ the Hilbert function
overshoots (e.g. $29,57,71,57,29,9,2,1$ for a unique-solution instance with $n=7$).

### D-initial-ideal
For a weight $w\in\mathbb R^{n+1}$, $\mathrm{in}_w(f)$ is the sum of the terms of $f$ maximising
$w\cdot\alpha$, and $\mathrm{in}_w(I)=(\mathrm{in}_w(f):f\in I)$. A $w$-**Grobner basis** of $I$ is
a generating set $g_1,\dots,g_r$ with $(\mathrm{in}_wg_1,\dots,\mathrm{in}_wg_r)=\mathrm{in}_w(I)$.
The **Grobner fan** is the fan of weight cones with a fixed initial ideal; $w$ in an open maximal
cone gives a monomial $\mathrm{in}_w(I)$.
Source: report §5 task 5 L141; §8.4(b) L236; standard (Eisenbud, *Commutative Algebra*, GTM 150,
Thm 15.17).
Pitfalls: for an arbitrary generating set $(\mathrm{in}_wf_j)$ can be strictly smaller than
$\mathrm{in}_w(I)$ (referee round1 #27). Even with a monomial initial *ideal*, an individual
$\mathrm{in}_w(g_j)$ may have several tied terms (referee round1 #29), and then $H_N(0)$ is not
diagonal.

### D-groebner-deformation-path
Fix $w$ and a $w$-Grobner basis $g_1,\dots,g_r$ with $\mathrm{in}_w(g_j)$ a single monomial. Scale
each monomial $z^\alpha$ of $g_j$ by $t^{\max_{\alpha'}w\cdot\alpha'-w\cdot\alpha}$, $t\in[0,1]$,
giving $g_j(t)$ with $g_j(1)=g_j$ and $g_j(0)=\mathrm{in}_w(g_j)$; $I(t)=(g_1(t),\dots,g_r(t))$ is a
flat family with $I(0)=\mathrm{in}_w(I)$, so $\dim I(t)_N$ is constant on $[0,1]$.
At $t=0$, $H_N(0)$ is diagonal with ground states the standard monomials of $\mathrm{in}_w(I)$ and
$$\Delta_N(0)\ \ge\ \min_j|\gamma_j|^2\,\alpha^{(j)}!,\qquad
\gamma_j=\text{leading coefficient of }g_j,\ \ \mathrm{in}_w(g_j)=\gamma_jz^{\alpha^{(j)}}.$$
Source: report §5 task 5 L141; §8.4 L236; referee round1 #27-#31, round2 #13.
Pitfalls: flatness requires the $g_j$ to be a Grobner basis (referee round1 #27). For $t>0$ the
family is a diagonal coordinate change, so constancy is trivial; the content is at $t=0$. The
endpoint bound is an inequality, not an equality: $f=x^2y+xy^2$ with $w_x>w_y$ has
$\Delta_4(0)=4|\gamma|^2\ne2|\gamma|^2$ (referee round2 #13). Rescaling a generator changes
$\Delta_N(t)$ without changing $I$ (C5). Flatness gives no spectral monotonicity in $t$
(referee round1 #56).

### D-adiabatic-groebner-complexity
$$\mathcal G_N(I)=\min_{w}\ \max_{t\in[0,1]}\ \frac{\alpha_{\mathrm{BE}}(t)}{\Delta_N(t)},$$
minimised over weight vectors $w$ in the open maximal cones of the Grobner fan, with $G$ the
corresponding reduced Grobner basis normalised to unit Bombieri-Weyl norm (C5) and
$\alpha_{\mathrm{BE}}(t)$ the block-encoding normalisation along the path.
Source: report §8.4(b) L236.
Pitfalls: still under-specified - the presentation class (redundant generators allowed?), the path
space and the normalisation along the path were the referee's standing objection
(round1 #57, round2 #14). Not an invariant of $I$ without fixing all three.

### D-cone
$V(I)$ is a **cone** when, after a unitary change of variables, the generators omit a variable $w$
(equivalently $I$ is extended from a subring); the vertex is the point dual to $w$. For a
hypersurface $V(f)$ this is equivalent to linear dependence of the partials
$\partial_0f,\dots,\partial_nf$; for a quadric it is $\tau_{\min}=0$ (D-takagi-factorisation).
Source: report §7 L197; §8.3(b) L228.
Pitfalls: for $d=1$ the test vector $h=w^{N-m}$ pins $\Delta_N=\|f\|^2_{\mathrm F}$ exactly. For
$d\ge2$ the corresponding vector is not in general orthogonal to $\mathrm{Syz}_N$, and projecting
the syzygy component out *raises* the Rayleigh quotient, so no upper bound
$\Delta_N\le\min_j\|f_j\|^2$ follows (OPEN-5, referee round2 #10).

### D-kostlan-random-form
A form of degree $m$ with independent complex Gaussian coefficients of variance
$\alpha!/m!$ (equivalently, standard Gaussian in the Bombieri-Weyl orthonormal basis), so that the
law is $U(n+1)$-invariant; normalised to $\|f\|_{\mathrm{BW}}=1$ where stated.
Source: report §8.3(c) L230; referee round1 #52.
Pitfalls: the statement must quantify over $N$ explicitly; the seed's form is
$\Pr[\inf_{N\ge m}\Delta_N\ge c(m)]\to1$ as $n\to\infty$, supported only by $N=3,4$ data.

---

## D. The Hamiltonian and its spectral data

### D-hamiltonian
$$H=\sum_{j=1}^d a^\dagger(f_j)\,a(f_j)\ \ \text{on }\mathcal F,\qquad
H_N:=H|_{R_N}=\Phi_N\Phi_N^\dagger\ \ge 0 .$$
$H$ is degree preserving and block diagonal over $N$; it is number conserving as a bosonic
Hamiltonian.
Source: page81 L130; report §2 L39.
Pitfalls: positivity and the kernel identity require C3 (conjugated coefficients). Each term
$a^\dagger(f_j)a(f_j)$ moves $m_j$ bosons and can change up to $2m_j$ occupation numbers
(referee round1 #8).

### D-ground-space
$$\ker H_N=\bigcap_j\ker a(f_j)|_{R_N}=\bigcap_j(f_jR_{N-m_j})^\perp=(I_N)^\perp,\qquad
\dim\ker H_N=\mathrm{HF}_{R/I}(N),$$
and $\operatorname{ran}H_N=I_N$. (Fact 2.1 of the seed report; the identity
$\ker M^\dagger=(\operatorname{ran}M)^\perp$.)
Source: report §2 L42-L49; page81 L119-L131.
Pitfalls: this is the ground space of the *restricted* $H_N$; statements about the full $H$ must
say which sector. Verified numerically against independent Macaulay ranks for the conic ($2N+1$),
twisted cubic ($3N+1$), rational normal quartic ($4N+1$), a monomial ideal, two generic quadrics in
$\mathbb P^3$ ($4N$) and the boolean ideals.

### D-frustration-free
$H=\sum_j T_j$ with each $T_j\ge0$ is frustration free at energy $0$ when
$\ker H=\bigcap_j\ker T_j\ne0$, i.e. a ground state of the sum minimises every term separately.
$H_N$ is frustration free whenever $\mathrm{HF}_{R/I}(N)>0$.
Source: report §2 L42 (Fact 2.1), §8 L218.
Pitfalls: the kernel of a sum of positive operators is the *intersection* of kernels (AND); this is
exactly why a parent Hamiltonian for the span $I_N$ (OR) cannot be built by summing positive terms
(D-parent-hamiltonian). Deciding frustration-freeness has no rescue from a gap promise
(report §6 L168).

### D-parent-hamiltonian
A positive operator (usually a sum of positive local terms) whose kernel is a prescribed subspace.
Here: the seed asks for $H'\ge0$ with $\ker H'=I_N$ rather than $(I_N)^\perp$, e.g. by summing
shifted projectors $H\mapsto\sum_\alpha J^\alpha H(J^\alpha)^\dagger$.
Source: page81 L250-L253, L503-L529; report §4 L104.
Pitfalls: the obstruction is exact - kernels of sums intersect (AND) while $I_N=\operatorname{span}_\beta\{z^\beta f_j\}$
is a span (OR); $\bigcap_\alpha J^\alpha(\ker H_0)$ is far too small. The available substitute is
the spectral projector $\Theta(H_N)$ by QSVT (D-projectors).

### D-k-body
First-quantised locality on the qudit register: $T$ is $k$-body if, under D-symmetric-sector,
$T=P_{\mathrm{sym}}\big[\sum_{|S|=k}T_S\otimes\mathbb 1\big]P_{\mathrm{sym}}$ with each $T_S$
acting on $k$ of the $N$ tensor factors. $H_N$ itself is $\max_jm_j$-body:
$$H_N\;\cong\;P_{\mathrm{sym}}\Big[\sum_jm_j!\sum_{|S|=m_j}\big(|F_j\rangle\langle F_j|\big)_S\Big]P_{\mathrm{sym}} .$$
Source: report §3 L69, L72; §4 L108 (Fact 4.1); referee round1 #5.
Pitfalls: individual subset terms do not preserve $\mathrm{Sym}^N$; only the permutation-symmetric
sum does. **Fact 4.1**: for $0\ne I_N\ne R_N$ and $N\ge k+\min_jm_j$, any $k$-body $T\ge0$ with
$T(I_N)=0$ is $0$ on $\mathrm{Sym}^N$ - there is no $k$-body parent for $I_N$, monomial ideals
included. Locality on the *qubit* register (occupation numbers in binary) is a different and weaker
notion: there $H_N$ is only sparse and row-computable.

### D-few-mode
Second-quantised locality: $T$ is $|A|$-mode if it is a (possibly unbounded) function of the mode
operators $\{a_i,a_i^\dagger:i\in A\}$ for a bounded mode set $A$ - legitimate as an on-site term
in the Bose-Hubbard sense, but not local in the complexity-theoretic sense. If $I$ is generated by
forms in the modes of $A$ (after a unitary change of variables) then
$$I_N=\bigoplus_r (I\cap R(A))_r\otimes R(A^c)_{N-r},$$
and $\mathbb 1-P_{I\cap R(A)}$ is an $|A|$-mode operator with kernel $I_N$.
Source: report §4 L110 (Fact 4.2); referee round2 #2, #4.
Pitfalls: the converse direction is generator-dependent: $(z_0+z_1,z_0-z_1)=(z_0,z_1)$ is confined
to two modes although the displayed generators are non-monomial. An ideal-invariant
support-hypergraph criterion is still missing (OPEN-6). A product over generators acts on the
*union* of their mode sets, so few-mode locality holds only when that union is bounded.

### D-macaulay-gap
$$\Delta_N:=\lambda^{\ne0}_{\min}(H_N)=\sigma^{\ne0}_{\min}(\Phi_N)^2
=\min\Big\{\frac{\big\|\sum_jf_jh_j\big\|^2}{\sum_j\|h_j\|^2}:\ (h_j)\in\bigoplus_jR_{N-m_j},\
(h_j)\perp\mathrm{Syz}(I)_N\Big\},$$
in Fock norms (C1): a *quantitative syzygy constant* - how close a non-syzygy can come to being one.
Normalisation convention (C5): stated for **unit Bombieri-Weyl generators**,
$\|f_j\|_{\mathrm{BW}}=1$, i.e. $\|f_j\|^2_{\mathrm F}=m_j!$.
Source: report §5 L123, §7 L179; numerics `bf.py:gap_from_spectrum` (smallest nonzero eigenvalue at
the independently known kernel dimension).
Pitfalls: (i) depends on the *generating tuple*, not on $I$: $(f_1,f_1+\epsilon f_2)$ generates the
same ideal for $\epsilon\ne0$ with $\Delta_N=O(\epsilon^2)$ (report L194; referee round1 #42 fixed
the direction of this example). (ii) Rescaling a generator changes $\Delta_N$ but not $I$; only the
normalised gap is meaningful in a promise. (iii) It is convention dependent: the same tuple has
$\Delta^{\mathrm{BW}}_N=\binom Nm^{-1}\frac{1}{m!}\Delta^{\mathrm F}_N$ for $d=1$
(D-norm-comparison). (iv) It is a $U(n+1)$ invariant of the tuple in the Bombieri-Weyl basis.
(v) Known values: **Fact 7.1** $\Delta_N\ge\|f\|^2_{\mathrm F}=m!\|f\|^2_{\mathrm{BW}}$ for $I=(f)$
(Bombieri-Beauzamy-Enflo-Montgomery product inequality; in BW form the constant is
$\binom Nm^{-1/2}$); **Fact 7.2** for quadrics, $4\tau_{\min}^2(N-2)+\|f\|^2_{\mathrm F}\le\Delta_N\le
\tau_{\min}^2N(N-1)+\|f\|^2_{\mathrm F}-2\tau_{\min}^2$; monomial ideals with monic generators
$\Delta_N\ge1$; toric $\Delta_N=\min_u\lambda_2(H_u)$. No several-generator lower bound is known.

### D-normalised-gap
$\Delta_N/\alpha_{\mathrm{BE}}$, the only spectral quantity that can appear in a promise, since an
absolute bound $\Delta_N\ge1/\mathrm{poly}(n)$ is destroyed by rescaling generators.
Source: report §5 L133; referee round1 #21 (fatal), #18.
Pitfalls: the seed's numerical survey tabulates $\|H_N\|/\Delta_N$, not
$\alpha_{\mathrm{BE}}/\Delta_N$; the ratio $\alpha_{\mathrm{BE}}/\|H_N\|$ (sparse-access overhead)
is never bounded in the report (OPEN-3).

### D-block-encoding-normalisation
For a sparse-access block encoding of $H_N$,
$$\alpha_{\mathrm{BE}}=O\big(s_{\mathrm{row}}\max_{x,y}|(H_N)_{xy}|\big)
=\mathrm{poly}(n)\,N^{m}\max_j\|f_j\|^2,$$
with row sparsity $s_{\mathrm{row}}\le\sum_j(\#\text{monomials of }f_j)^2$ and entries
$\sum_j\overline{f_{j,\alpha}}f_{j,\beta}\sqrt{k!\,(k-\alpha+\beta)!}/(k-\alpha)!$, reversibly
computable in $\mathrm{poly}(n,\log N)$ time. Also
$\|H_N\|\le\sum_j\frac{N!}{(N-m_j)!}\|f_j\|^2_{\mathrm{BW}}\le d\,N^{m}\max_j\|f_j\|^2_{\mathrm{BW}}$.
Source: report §5 L124, L127; referee round1 #18.
Pitfalls: C7 (write $\alpha_{\mathrm{BE}}$, not $\alpha$). $\alpha_{\mathrm{BE}}\ge\|H_N\|$ in
general; runtimes must be quoted with $\alpha_{\mathrm{BE}}$, never with $\|H_N\|$.

### D-projectors
$P_0$: orthogonal projector onto $\ker H_N=(I_N)^\perp$ (with $P_{0,N}$ when the degree matters).
$P_{I_N}=\mathbb 1-P_0=\Theta(H_N)$: projector onto $I_N$, the Heaviside step function of $H_N$,
obtainable by QSVT at cost $O(\alpha_{\mathrm{BE}}/\Delta_N\cdot\log\epsilon^{-1})$ block-encoding
uses. $P_{\mathrm{sym}}$: projector onto the symmetric subspace.
Source: report §2 L49, §4 L114, §3 L69.
Pitfalls: $\Theta(H_N)$ is non-local; it is the substitute for the impossible parent Hamiltonian,
not a parent Hamiltonian.

### D-multidegree-sector
With variables $z_{i,s}$, $i=1,\dots,n$ (sites), $s=0,\dots,q-1$ (levels), $R$ is
$\mathbb Z^n$-graded and $H$ preserves each multidegree. The multidegree $(1,\dots,1)$ sector is
$$R_{(1,\dots,1)}\;=\;(\mathbb C^q)^{\otimes n},\qquad
z_{1,s_1}\cdots z_{n,s_n}\leftrightarrow|s_1\cdots s_n\rangle,$$
orthonormal (all Fock norms $1$). For a multilinear form $f$ supported on a site set $S$,
$$a^\dagger(f)a(f)\big|_{(1,\dots,1)}=|f\rangle\langle f|_S\otimes\mathbb 1$$
exactly, with no factorials.
Source: report §3 L92-L98; numerics `task6_2sat.py`.
Pitfalls: this is the Segre/multigraded picture, different from the total-degree symmetric sector;
the factorial-free identity holds only in multidegree $(1,\dots,1)$. Product-state solutions are the
points of $V(I)\subseteq(\mathbb P^{q-1})^n$; entangled solutions are the rest of the inverse system.

### D-quantum-k-sat
The Bravyi promise problem for a frustration-free Hamiltonian $\sum_S\Pi_S$ of $k$-local
projectors: decide "ground energy $0$" vs "ground energy $\ge1/\mathrm{poly}$". Via
D-multidegree-sector, every quantum $k$-SAT instance is the $(1,\dots,1)$ block of an ideal
generated by $k$-multilinear forms (a rank-$r$ local projector split into $r$ rank-one ones, which
preserves the Hamiltonian and its gap), and conversely that block of such an ideal is a QSAT
instance. The corresponding promise problem "$\mathrm{HF}_{R/I}(1,\dots,1)>0$ or
$\lambda_{\min}(H_{(1,\dots,1)})\ge1/\mathrm{poly}(n)$" is in P for $k=2,q=2$, and
$\mathrm{QMA}_1$-complete for $k=3,q=2$; with monomial generators it is classical $k$-SAT.
Source: report §3 L98-L100 (Proposition 3.1); Bravyi arXiv:quant-ph/0602108; Gosset-Nagaj
arXiv:1302.0290; Rudolph-Gharibian-Nagaj arXiv:2401.02368 (bilinear forms over blocks of unequal
sizes, e.g. $(2,5)$, already $\mathrm{QMA}_1$-complete).
Pitfalls: "$k=2$ is in P" holds for **qubits** ($q=2$) only (referee round2 #1). The ordinary
(total-degree) construction is a *bosonic/permutation-symmetric analogue*, not a Bravyi instance:
the domain is $\mathrm{Sym}^N$ and every forbidden tensor is replicated over all $m$-subsets
(referee round1 #9). Without the NO-gap promise, exact non-vanishing of $\mathrm{HF}$ is not
thereby in $\mathrm{QMA}_1$ (referee round1 #12).

### D-hard-core-generators
The generators $z_{i,s}z_{i,s'}$ for all sites $i$ and all $s\le s'$ (squares included), which
force at most one boson per site: every generator preserves the per-site occupation pattern, on the
pattern $(1,\dots,1)$ the hard-core terms vanish, and on every other pattern the diagonal hard-core
part alone is $\ge1$.
Source: report §8.2 L222 (Proposition 8.2: bosonic QSAT with $N=n$ bosons in $2n$ modes and
generators of degree $\le3$ is $\mathrm{QMA}_1$-hard); referee round1 #49, round2 #8.
Pitfalls: omitting the squares $s=s'$ leaves same-mode multiple occupancy and spurious zero modes
(all bosons in one block).

### D-coherent-state
For $p\in\mathbb C^{n+1}$ with $\|p\|=1$, the spin-coherent (product) state
$$|p\rangle^{\otimes N}\ \longleftrightarrow\ \frac{(p\cdot z)^N}{\sqrt{N!}}\in R_N,\qquad
\langle (p\cdot z)^N,u\rangle_{\mathrm F}=N!\,u(\bar p),$$
so that
$$|p\rangle^{\otimes N}\in\ker H_N\iff u(\bar p)=0\ \forall u\in I_N\iff \bar p\in V(I_N),\qquad
\langle p^{\otimes N}|H_N|p^{\otimes N}\rangle=\sum_j\frac{N!}{(N-m_j)!}|f_j(\bar p)|^2 .$$
Moreover $\operatorname{span}\{|p\rangle^{\otimes N}:\bar p\in V\}=(I(V)_N)^\perp$.
Source: report §3 L76-L90; referee round1 #4, #7, #58.
Pitfalls: C3 - a point $x\in V(I)$ corresponds to the physical state $|\bar x\rangle^{\otimes N}$.
The normalised representative is $(p\cdot z)^N/\sqrt{N!}$, not $(p\cdot z)^N$. The ground space is
spanned by coherent states of points of $V$ exactly when $I_N=I(V)_N$; otherwise it contains
$\dim I(V)_N-\dim I_N$ further, necessarily entangled, states (D-entangled-defect).

### D-coherent-gram-matrix
For a finite set $X\subset\mathbb P^n$ of (conjugated) points, $G_{xy}=\langle p_x,p_y\rangle^N$,
the Gram matrix of the coherent states $|p_x\rangle^{\otimes N}$; for the boolean family
$\hat p_x=(1,x)/\sqrt{1+|x|}$, $x\in\{0,1\}^n$, nearest neighbours have overlap
$\approx e^{-N/(2n)}$ and $G$ is $\varepsilon$-close to $\mathbb 1$ in operator norm only for
$N=\Omega(n\log(n/\varepsilon))$.
Source: report §5.7 L154, §8.6(ii) L240; referee round2 #16, #17.
Pitfalls: pairwise near-orthogonality is not operator-norm control. Numerically the smallest Gram
eigenvalue of the full hypercube family is $3.5e^{-0.85n}$ at $N=n+3$ and $0.7e^{-0.35n}$ at $N=2n$.
A root-sampling oracle does not give the projector onto the span of these states (referee round1 #60).

### D-entangled-defect
$\dim I(V)_N-\dim I_N$, the dimension of the part of $\ker H_N$ orthogonal to all coherent states of
points of $V$. For zero-dimensional $I$ in the stable range it equals
$\operatorname{length}(\operatorname{Proj}R/I)-\#V$, and the seed conjectures that it is spanned by
the jets of coherent states along the differential functionals of Macaulay's local dual at each
non-reduced point.
Source: report §8.5 L238; referee round1 #59, round2 #15.
Pitfalls: outside the stable range it also counts irrelevant torsion; in positive dimension it grows
polynomially. Arbitrary non-reduced inverse systems need higher jets, not only first derivatives.

### D-takagi-factorisation
For a quadric $f=z^{\mathsf T}Az$ with $A$ complex symmetric, the Takagi factorisation
$A=U\Sigma U^{\mathsf T}$ ($U$ unitary, $\Sigma=\mathrm{diag}(\tau_1,\dots,\tau_{n+1})$,
$\tau_j\ge0$ the **Takagi values** = singular values of $A$) gives
$$f=\sum_j\tau_j w_j^2,\qquad w_j=u_j^{\mathsf T}z\ \text{orthonormal linear forms},\qquad
[a(f),a^\dagger(f)]=\sum_j\tau_j^2(4\hat n_j+2),$$
with $\|f\|^2_{\mathrm{BW}}=\|A\|_{\mathrm F}^2=\sum_j\tau_j^2$ and
$\|f\|^2_{\mathrm F}=2\sum_j\tau_j^2$. $\tau_{\min}$ is the Bombieri-Weyl distance from $f$ to the
quadrics of deficient rank, i.e. to the cones.
Source: report §7 L186-L192 (Fact 7.2).
Pitfalls: C9 (write $\tau$, not $d$). The change of variables is unitary, so it preserves the
Bombieri-Weyl norm and turns $a(w_j)$ into canonical modes; a non-unitary diagonalisation would not.
A cone has $\tau_{\min}=0$ and hence a bounded gap.

---

## E. Algorithmic objects, geometric readings, complexity conventions

### D-input-model
Generators with $\mathrm{poly}(n)$ monomials and $\mathrm{poly}(n)$-bit coefficients; $N$ given in
**unary** (all tasks are polynomial in $N$, never in $\log N$); the register holds
$k=(k_0,\dots,k_n)$ with $\sum_jk_j=N$ in $O(n\log N)$ qubits.
Source: report §5 L127; referee round1 #19, #20 (fatal), #50.
Pitfalls: a degree $N$ exponential in $n$ is cheap in *qubits* only - $\alpha_{\mathrm{BE}}/\Delta_N$
and all precision targets scale polynomially in $N$, so the running time is exponential there.
"Polynomial in $N$" with $N$ in binary would be exponential in the input length.

### D-qsvt
Quantum singular value transformation applied to a block encoding of $H_N$ with normalisation
$\alpha_{\mathrm{BE}}$: at cost
$$T=\mathrm{poly}(n^m,d)\times\frac{\alpha_{\mathrm{BE}}}{\Delta_N}\times\log\frac1\epsilon$$
block-encoding uses it produces $P_0$, $\Theta(H_N)=P_{I_N}$, the polar isometries $U_f$, and
eigenvalue-resolved access to $H_N$.
Source: report §5 L130-L133.
Pitfalls: the polynomial degree needed for the step function is set by the *normalised* gap; a
promise on $\Delta_N$ alone is worthless (D-normalised-gap).

### D-distance-to-ideal
$$\delta(f)^2:=\frac{\langle f|P_0|f\rangle}{\|f\|^2}=\frac{\operatorname{dist}(f,I_N)^2}{\|f\|^2},$$
the squared normalised distance from $f\in R_N$ to $I_N$; equal to $\|[f]\|^2/\|f\|^2$ for the
quotient norm on $(R/I)_N$ induced from the ambient norm. Equivalent readings: the
Drury-Arveson quotient-module norm; the restriction norm
$\delta(f)^2=\|f|_V\|^2_{\mathrm{RKHS}(V)}/\|f\|^2$ for radical $I$ in the stable range, comparable
to $N^{\dim V-n}\int_V|f|^2_{h^N}/\int_{\mathbb P^n}|f|^2_{h^N}$ by Bergman-kernel asymptotics; the
polynomial-kernel quantity $f_X^\dagger G^{-1}f_X$ for a finite point set (D-coherent-gram-matrix);
and the weight of a guiding state on the ground space of a gapped frustration-free Hamiltonian.
Source: report §5 task 1 L137, §5.7 L144-L155.
Pitfalls: the ratio is convention independent (the three norms are degreewise proportional), but the
*unnormalised* $\operatorname{dist}(f,I_N)$ is not; the seed writes $\operatorname{dist}_{\mathrm{BW}}$
inside a Fock-convention document (OPEN-4) and equates the normalised $\delta(f)$ with the
unnormalised quotient norm $\|[f]\|$ (OPEN-7).

### D-distance-to-ideal-problem
The seed's Conjecture 8.1, verbatim in content: **Input** multi-homogeneous generators of degree
$\le m=O(1)$ in $\mathrm{poly}(n)$ variables with $\mathrm{poly}(n)$-bit coefficients of unit
Bombieri-Weyl norm; a multidegree sector (or total degree $N\le\mathrm{poly}(n)$); a
$\mathrm{poly}(n)$-sparse unit vector $f$ in that sector; thresholds $a<b$ with
$b-a\ge1/\mathrm{poly}(n)$; and the promise $\Delta/\alpha_{\mathrm{BE}}\ge1/\mathrm{poly}(n)$ for
the Hamiltonian **restricted to that sector**. **Decide** $\langle f|P_0|f\rangle\le a$ or $\ge b$.
Conjectured BQP-hard and in BQP; containment is D-qsvt with amplitude estimation, cost
$\tilde O(T/\epsilon)$. Hardness sketch: embed a Feynman-Kitaev history Hamiltonian
(D-history-state) into the $(1,\dots,1)$ sector and use the two endpoint states
$f_\pm=(|0,\mathrm{clock}=0\rangle\pm|y,\mathrm{clock}=T\rangle)/\sqrt2$, whose weights
$|1\pm\overline{\langle y|U|0\rangle}|^2/(2(T+1))$ differ by $2\operatorname{Re}\langle y|U|0\rangle/(T+1)$.
Source: report §8.1 L220; referee round1 #45 (fatal), #46, #47; round2 #7.
Pitfalls: this is hardness for **estimating a distance**, not for exact membership: an oracle
deciding "$f\in I_N$ or $\epsilon$-far" is not what the reduction produces. One endpoint state does
not suffice ($|a|^2$ is also unknown), so both signs are needed. Exact membership is
EXPSPACE-complete only for unbounded degree (Mayr-Meyer); at fixed $N$ it is linear algebra of
dimension $\binom{N+n}{n}$.

### D-history-state
The Feynman-Kitaev Hamiltonian $H_{\mathrm{in}}+H_{\mathrm{prop}}$ of a circuit $U=U_T\cdots U_1$:
frustration free, unique ground state the history state
$\frac{1}{\sqrt{T+1}}\sum_{t=0}^T U_t\cdots U_1|0\rangle|t\rangle$, with gap $\Omega(T^{-2})$ in its
sector.
Source: report §8.1 L220; referee round1 #47.
Pitfalls: the $\Omega(T^{-2})$ gap is a statement about that sector; other multidegree blocks can
carry smaller positive eigenvalues, so it is not a bound on the global $\Delta_N$.

### D-dqc1-style-estimate
Additive estimation of a normalised trace, $\operatorname{Tr}(P_0X)/\dim$, by preparing the
maximally mixed state on the valid weak-composition register plus controlled QSVT with clean
ancillas; cost $\tilde O(T/\epsilon^2)$.
Source: report §5 task 2 L138, §8.10 L248; referee round1 #22.
Pitfalls: "DQC1-style" only - membership in DQC1 proper is not claimed, because the mixed state is
over the composition subspace, not a power-of-two register.

### D-hardness-anchors
The fixed points against which any speedup claim is tested: exact $\mathrm{HF}$ evaluation is
$\#\mathrm P$-hard (D-clause-ideal), so an exact quantum evaluation gives
$\#\mathrm P\subseteq\mathrm{FBQP}$ and a multiplicative approximation gives
$\mathrm{NP}\subseteq\mathrm{BQP}$; $\ker H_N\ne0$ is NP-hard and $\ker H_N=0$ is coNP-hard;
non-emptiness of $V$ over $\mathbb C$ is NP-hard and in AM under GRH (Koiran), emptiness in coAM;
permutation-invariant Hamiltonians at **fixed** local dimension are classically easy in
$\mathrm{poly}(N)$ (Anschuetz-Bauer-Kiani-Lloyd, Quantum 7, 1189 (2023)), so any advantage must come
from growing $n$; HHL on Macaulay systems has an exponential condition number unless the solution
has Hamming weight $O(\log n)$ (Ding-Gheorghiu-Gilyen-Hallgren-Li, Quantum 7, 1069 (2023),
DOI 10.22331/q-2023-07-26-1069, on the system of Chen-Gao); $H_N$ is sparse and high rank, so
low-rank dequantisation does not apply.
Source: report §6 L167-L172; referee round1 #36-#41, #76.
Pitfalls: there is **no** universal overlap lower bound $\sqrt{\dim R_N/\mathrm{HF}(N)}$; that factor
applies only to black-box projection from a state with that overlap (referee round1 #40).
$\#\mathrm P$-hardness of monomial Hilbert series is via edge ideals / independence polynomials
(Dickenstein-Tobis arXiv:1003.3508), not via Bayer-Stillman.

### D-bergman-projector
$P_0$ read geometrically: for radical $I$ in the stable range it is the degree-$N$ Bergman projector
of $V$ written in ambient monomial coordinates (the projector onto the closed span of the coherent
kernel functions at points of $V$). Derived quantities: the **Berezin symbol**
$\langle p^{\otimes N}|P_0|p^{\otimes N}\rangle$, a smooth indicator of $V$ at Fubini-Study
resolution $N^{-1/2}$ with Tian-Zelditch expansion
$N^{\dim V}\pi^{-\dim V}(1+S(p)/2N+\cdots)$; the **overlap** $\operatorname{Tr}(P_IP_J)$, whose
growth exponent is $\dim(V\cap W)$ and which decays like $\cos^{2N}d_{FS}(V,W)$ for disjoint
varieties; and **Toeplitz traces** $\operatorname{Tr}(P_0T_g)/\mathrm{HF}(N)\to
\int_Vg\,d\mathrm{vol}_V/\mathrm{vol}(V)$.
Source: report §5.7 L153, L159-L161, §8.10 L248; standard (Tian-Zelditch-Catlin;
Bordemann-Meinrenken-Schlichenmaier) [UNVERIFIED ids].
Pitfalls: the Berezin symbol is classically easy (differentiate the equations), so it carries no
advantage; only the trace-type quantities are candidates. All three are conjectural in the stated
asymptotic form (Conjecture 8.10) and informative only for low codimension.

### D-toeplitz-operator
For $g(z,\bar z)$ a polynomial, $T_g=P_0\,g(a^\dagger,a)\,P_0$ in normal order: a bosonic
observable whose normalised trace against $P_0$ converges by Berezin-Toeplitz theory to the average
of $g$ over $V$, with $1/N$ corrections given by the Laplacian and scalar curvature.
Source: report §5.7 L161, §8.10(c) L248.
Pitfalls: normal ordering is part of the definition; a different ordering changes the $1/N$ term.

### D-condition-number
The Burgisser-Cucker normalised condition number $\mu_{\mathrm{norm}}(f,p)$ of a polynomial system
at a root, and $\mu_{\max}(V)=\sup_{p\in V}\mu_{\mathrm{norm}}(f,p)$; the quantity controlling
homotopy-continuation cost (Beltran-Pardo, Lairez) for the fair classical competitor - Monte Carlo
on $V$ by slicing with a random linear space of complementary dimension and averaging.
Source: report §5.7 L163, §8.11 L250; standard (Burgisser-Cucker, *Condition*, Grundlehren 349, 2013).
Pitfalls: the seed's Conjecture 8.11 (that $\Delta_N/\alpha_{\mathrm{BE}}\ge1/\mathrm{poly}(n,N,\mu_{\max})$)
is the open link between the quantum and classical cost models; no reduction between the
Ding et al. condition number and $\Delta_N$ is established (referee round1 #64).

### D-spin-mixing-hamiltonian
For the conic $f=z_0z_1-z_2^2$,
$$H=\hat n_0\hat n_1+\hat n_2(\hat n_2-1)-(a_0^\dagger a_1^\dagger a_2^2+\mathrm{h.c.}),$$
the single-mode-approximation spin-mixing Hamiltonian of a spin-1 spinor condensate under
$(z_0,z_1,z_2)\leftrightarrow(a_{+1},a_{-1},a_0)$; its ferromagnetic phase has exactly $2N+1$
degenerate ground states, the Hilbert function of the conic.
Source: report §3 L72; Law-Pu-Bigelow, PRL 81, 5257 (1998), DOI 10.1103/PhysRevLett.81.5257.
Pitfalls: this is a realisation of one quadric ideal, not of the general construction; the number
of modes is fixed at 3, which is exactly the classically easy regime (D-hardness-anchors).

### D-hard-gap-instances
The transfer of known frustration-free pathologies into the multigraded sector: area-weighted
Motzkin chains (Levine-Movassagh, arXiv:1611.03147) are 2-local, frustration free, with gap
$\le 8ns\,t^{-n^2/3}$; the D-multidegree-sector embedding transfers the spectrum, giving ideals with
$\mathrm{poly}(n)$ generators of degree $m=2$ and $\Delta/\alpha_{\mathrm{BE}}\le2^{-\Omega(n)}$ in a
sector specified by polynomially many sites (of dimension $q^n$); for $m>2$ pad each term by a
complete rank-one decomposition of the identity on $m-2$ auxiliary sites.
Source: report §8.3(d) L232; referee round1 #53, round2 #11.
Pitfalls: the sector has exponential *dimension* even though it is specified by polynomially many
sites. Numerically, random frustration-free 2-local chains are only polynomially gapped
($\approx L^{-3.5}$ for $L\le11$), so typical multigraded instances are not the hard ones; and the
singlet chain has $\Delta\approx9.13L^{-1.97}$ ($L^2\Delta\to\pi^2$).

### D-finite-field-analogue
Over $\mathbb F_q$, Macaulay duality survives via the divided-power/contraction action (ordinary
differentiation fails since $\partial x^p=0$), and is realised quantumly as Fourier duality between
the uniform superpositions over $I_N$ and over its contraction dual, on the additive group
$\mathbb F_q^{\dim R_N}$, with the syzygy module as the hidden subgroup of the explicitly known map
$(h_j)\mapsto\sum_jh_jf_j$. That register needs $\dim R_N\log q$ qubits.
Source: report §8.8 L244; page81 L254 ("This should allow finite field"); referee round1 #67-#69.
Pitfalls: the compact amplitude encoding of the complex construction does **not** transport, because
$\mathbb F_q$ has no field embedding into $\mathbb C$, so complex linear algebra preserves neither
$\mathbb F_q$-ranks nor products (the earlier "needs a positive-definite inner product" reason is
wrong). The HSP formulation gives no advantage over finite-field Gaussian elimination. The seed
calls this the one direction of the notes that does not work.

### D-bose-hubbard
A number-conserving bosonic lattice Hamiltonian with on-site terms that are functions of $\hat n_i$
and bounded-range hopping. Used here only as the standard of what counts as a legitimate physical
term in D-few-mode: $\mathbb 1-P_{I\cap R(A)}$ is an unbounded function of the mode operators of a
bounded mode set, acceptable "in a Bose-Hubbard sense" but not local in the complexity-theoretic
sense. Frustration-free Bose-Hubbard ground energy is QMA-hard (Childs-Gosset-Webb,
Theory of Computing 11, 491 (2015), DOI 10.4086/toc.2015.v011a020), which is a different statement
from the QSAT one used in D-hard-core-generators.
Source: report §4 L110; literature scout `literature-2026-09-02.md` L13; referee round2 #8.
Pitfalls: the Hamiltonians here are not Bose-Hubbard (the interactions are $m$-boson,
non-nearest-neighbour, and mode-nonlocal); the analogy is about term admissibility only.

### D-reserved-photonic
**Reserved.** The seed report does not use boson sampling, linear-optical circuits or GBS objects;
they appear only in the literature scout and in the campaign north star. Definitions that will be
needed before any such claim enters the DAG, none of them fixed yet:
passive linear-optical unitary (mode transformation $a^\dagger\mapsto Ua^\dagger$) and what it does
to $I$ (a unitary change of variables, hence a $U(n+1)$ action on generators);
measurement-induced nonlinearity and its success probability (Knill; Scheel-Audenaert);
Fock filters "at most $k$ photons in a mode", realising power-ideal terms $\ell_j^{m}$ after a
passive rotation (Pegg-Phillips-Barnett; Winnel-Hosseinidehaj-Ralph);
postselected-linear-optics / MBQC model and its complexity class; boson sampling and GBS
distributions and the graph polynomials they compute (hafnian/matching polynomial);
stellar rank (Chabaud et al.) and its relation to $\deg f$;
the notion of "cheap heuristic attack" the north star asks for.
Source: `seed/analysis-2026-09-01/literature-2026-09-02.md` L18-L22; CLAUDE.md §1.
Pitfalls: none of these objects has a definition in the seed report; nothing may cite this entry as
if it did.

---

### D-arveson-curvature
STUB (orchestrator, 2026-09-02; requested by claims lane, cited by rows C-170/C-172 area). Arveson curvature of a pure $d$-contraction / of the quotient module $H^2_d/[I]$, per Arveson, "The curvature invariant of a Hilbert module over $\mathbb C[z_1,\dots,z_d]$", J. reine angew. Math. 522 (2000) [UNVERIFIED id]. To be written by the definitions lane before any C-row citing it is critiqued.
Source: claims lane request. Pitfalls: not yet defined; do not cite in an argument shard.

### D-essential-normality
STUB (orchestrator, 2026-09-02; requested by claims lane). Essential normality of the quotient module $H^2_d/[I]$ (commutators $[S_i^*,S_j]$ compact), Arveson–Douglas conjecture. To be written by the definitions lane.
Source: claims lane request. Pitfalls: not yet defined; do not cite in an argument shard.

### OPEN

Issues found while building this register. Nothing here is repaired silently; each is a question for
the claims lane or the orchestrator. "report" = `seed/analysis-2026-09-01/report.md`,
"page81" = `seed/page81.tex`.

**OPEN-1 (normalisation of the gap survey).** report L200 states the numerical survey uses
"unit-coefficient generators as written", while the conjectures that the survey is evidence for fix
"unit Bombieri-Weyl generators" (report L224, Conjecture 8.3 preamble; also L220 and L236). These
differ by a generator-dependent factor: the conic $z_0z_1-z_2^2$ has $\|f\|^2_{\mathrm{BW}}=3/2$, so
its tabulated $\Delta_N=N+1$ becomes $\tfrac23(N+1)$ after normalisation. Every number in the table
at report L202-L212 needs a stated normalisation before it can support or refute 8.3.

**OPEN-2 (monic vs unit-BW inside Conjecture 8.3(a)).** report L226 asserts the conjecture "holds for
monomial ideals with monic generators with $c=\min_j\alpha^{(j)}!$", inside a conjecture whose
preamble (L224) fixes unit Bombieri-Weyl generators. Under that preamble the constant is
$\min_jm_j!$, since a unit-BW degree-$m$ monomial has $\|\cdot\|^2_{\mathrm F}=m!$. Referee round2 #9
asked for exactly this separation; the text names both normalisations without choosing.

**OPEN-3 (which normalisation the promise is on).** report L133 states that all promises are on
$\Delta_N/\alpha_{\mathrm{BE}}$, but the survey (L202-L212) and Conjecture 8.6(i) (L240) report
$\|H_N\|/\Delta_N$. The gap between them is the sparse-access overhead
$\alpha_{\mathrm{BE}}/\|H_N\|=O(s_{\mathrm{row}}\max|H_{xy}|/\|H_N\|)$, which is never bounded in
the report. The numerics therefore do not directly measure the quantity the conjectures promise.

**OPEN-4 (norm subscript on the distance).** report L137 writes
$\langle f|P_0|f\rangle/\|f\|^2=\operatorname{dist}_{\mathrm{BW}}(f,I_N)^2/\|f\|^2$ inside a document
that fixes the Fock convention at L17. Harmless (the ratio is the same in all three norms, since
they are degreewise proportional) but the register must fix one; C1 fixes Fock and the ratio is
labelled convention-free in D-distance-to-ideal.

**OPEN-5 (Conjecture 8.3(b) upper bound for $d\ge2$).** report L228: "then $h_j=w^{N-m_j}$ shows
$\Delta_N\le\min_j\|f_j\|^2$ up to the syzygy correction". $\Delta_N$ is a minimum over vectors
orthogonal to $\mathrm{Syz}(I)_N$; the test vector $w^{N-m_j}e_j$ is not in general orthogonal to
$\mathrm{Syz}(I)_N$, and removing its syzygy component shortens it, so the Rayleigh quotient of the
projected vector is $\ge\|f_j\|^2$, not $\le$. The upper bound is established only for $d=1$ (the
pyramid, which is principal). Also $\|f_j\|^2$ is not said to be Fock or BW. Referee round2 #10
asked for exactly this restriction.

**OPEN-6 (Fact 4.2's converse is not ideal-invariant).** report L110 states "few-mode parents exist
only for ideals confined to few modes", but the converse half is proved from a *generator* support
condition, and the same paragraph notes the condition is not invariant under change of generators
($(z_0+z_1,z_0-z_1)=(z_0,z_1)$). So the Fact as titled is about ideals while its proof is about
presentations. Referee round2 #4 demanded an ideal-invariant support-hypergraph condition; it is
still missing.

**OPEN-7 (normalised vs unnormalised quotient norm).** report L144 defines
$\delta(f)^2=\langle f|P_0|f\rangle/\|f\|^2$; report L146 then says "$\delta(f)=\|[f]\|$ for the
Hilbert norm on $(R/I)_N$". The two differ by the factor $\|f\|$: the correct identity is
$\delta(f)=\|[f]\|/\|f\|$. The same omission propagates to the RKHS reading at L150.

**OPEN-8 (page81 defines one basis and computes in another).** page81 L22-L26 defines
$|k\rangle=\sqrt{(N+n)!/(k!\,n!)}\,z^k$ (the sphere ONB), but the worked examples at L179-L189 and
the state at L195 are correct only under $|k\rangle\leftrightarrow z^k$ (unnormalised monomials):
$a(f_0)|112\rangle=|002\rangle-2|110\rangle$ and $|\psi\rangle=|110\rangle+\tfrac12|002\rangle$ hold
in the monomial basis; in the Fock basis the state is $|110\rangle+\tfrac1{\sqrt2}|002\rangle$.
The same page also writes the general basis without any normalisation at L315.

**OPEN-9 (page81 L65, "$\ell_j\propto a_j$").** False as an operator statement: the ratio is
occupation dependent, $a_j^\dagger=J_j\sqrt{\hat n_j+1}$ (report L116). The page's later
constructions (L427 CG operator, L519 $\sum_\alpha J^\alpha H(J^\alpha)^\dagger$) use $J$, not $a$,
and inherit this.

**OPEN-10 (page81 L207-L219, the symbol $H'$).** L208 defines $H+L_f^\dagger L_f=H'$, so
$H'=H+L_f^\dagger L_f$; L213, L228 and L245 then use $\ker(H+H')$ as if $H'=L_f^\dagger L_f$. The
intended object is $H+L_f^\dagger L_f$, the Hamiltonian of $(I,f)$. The surviving content (report
§9 L258) is $\ker(H+H')\subseteq\ker H$ with the clean test $f\in I_N\iff P_0|f\rangle=0$.

**OPEN-11 (page81 L174-L176, a false vanishing criterion).** "$a(f_0)|k_0\cdots k_n\rangle=0$ if
$\sum_{j\ge2}k_j=1$" is false: with $a(f_0)=\partial_0\partial_1-\partial_2^2$,
$a(f_0)z^k=k_0k_1z^{k-e_0-e_1}-k_2(k_2-1)z^{k-2e_2}$, so $k=(1,1,1)$ gives $z_2\ne0$. The correct
condition is $k_2\in\{0,1\}$ **and** ($k_0=0$ or $k_1=0$). Not listed among the report's corrections
in §9 (L254-L261).

**OPEN-12 (page81 transcription defects).** L184 writes $a(f_1)|11\rangle=|000\rangle$ where $f_0$
and a 3-mode ket are meant; L286 writes "$(1)=\mathbb R$" where the unit ideal equals the ring $R$;
L280 "$\lvert hf\times hf\rvert^2$" and L348 the arrow diagram are malformed; L367 writes $m+1$
tensor factors where the variable count is $n+1$. These are transcription-level, but any argument
citing page81 must cite the corrected object, not the page's glyphs.

**OPEN-13 (report L184, the one-variable value).** "in one variable $\Delta_N=N!/(N-m)!$" is correct
for the monomial $f=z^m$; for a general one-variable $f$ of degree $m$ the value is
$\sum_j|f_j|^2(j+N-m)!/(N-m)!$. As placed (immediately after the monomial examples) the scope is
ambiguous.

**OPEN-14 (Fact 7.1's equality condition).** report L184 gives a sufficient condition for equality
("after a unitary change of variables, the extra degree can be placed in a linear subspace
orthogonal to the variables $f$ depends on") and does not claim necessity. Whether it is necessary
is open, and 8.3(b)/(e) implicitly need the converse. Referee round2 #6 flagged the earlier
"strict otherwise" as false ($f=z_0+z_1$, $h=(z_0-z_1)^{N-1}$).

## Lane report

Included: 66 entries in five parts - the three inner products with exact degreewise scalars; all operators ($a_j$, $a(f)$, $M_f$, $\Phi_N$, shifts, compressed multiplications); ideals, Hilbert function, inverse system, monomial/toric/boolean/clause ideals, Grobner deformation; Hamiltonian, ground space, frustration-freeness, parent Hamiltonians, $k$-body vs few-mode, $\Delta_N$ and its normalisations, coherent states, Takagi; algorithmic/geometric objects (input model, QSVT, the distance-to-ideal problem verbatim, Bergman projector, hardness anchors, condition number, hard-gap instances, finite fields, Bose-Hubbard). Every mandatory entry in the brief is present. `D-reserved-photonic` is a stub: the seed uses no boson-sampling / linear-optics / GBS object, so it lists what must be defined first. 14 OPEN issues, 5 of them substantive (OPEN-1,3,5,6,7); `notation.md` holds the symbol table and 18 page81-vs-report conflicts with the chosen convention.

Could not pin down: (i) the normalisation actually used in the numerical survey (OPEN-1/3), which decides whether the survey is evidence for Conjecture 8.3; (ii) an ideal-invariant form of Fact 4.2 (OPEN-6); (iii) ids for Fang 2003, Fischer 1918, Shapiro 1989, Iarrobino-Kanev, BBEM 1990, Tian-Zelditch-Catlin, Bordemann-Meinrenken-Schlichenmaier, Douglas-Tang-Yu, Chen-Gao - all left [UNVERIFIED].

MERGE PROPOSAL (CLAUDE.md §3, new rule 10): "Conventions C1-C12 of `definitions/definitions.md` are binding; an artifact departing from one says so in its first paragraph, and cites definition ids rather than restating definitions."
MERGE PROPOSAL (PRD.md, scope note): the campaign's spectral promise is on the normalised gap $\Delta_N/\alpha_{\mathrm{BE}}$; absolute $\Delta_N$ statements are presentation artefacts (C5, C7).
MERGE PROPOSAL (HANDOFF.md, conventions block): replace "Sphere/Bombieri norms agree with Fock only degreewise" by the exact scalars of D-norm-comparison, and add "Fact 7.1's uniform gap is a Fock-normalisation statement; in Bombieri-Weyl it reads $\Delta_N\ge\binom Nm^{-1}\|f\|^2_{\mathrm{BW}}$", and "$\Delta_N$ survey numbers in report §7 are unit-coefficient, not unit-BW (OPEN-1)."
