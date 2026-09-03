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


<!-- Merged verbatim from scouting/real-variety.md "Proposed definitions" (codex lane, 2026-09-02); orchestrator merge, no edits. Status: proposed, not yet cited by an argument shard. -->

MERGE PROPOSAL (`definitions/definitions.md`, new entry):

### D-real-locus-and-real-radical
For a homogeneous ideal \(I\subseteq\mathbb R[z_0,\ldots,z_n]\), its real projective locus is
\[
V_{\mathbb R}(I)=\{[x]\in\mathbb P^n(\mathbb R):f(x)=0\ \forall f\in I\},
\]
and its real radical is
\[
\sqrt[\mathbb R]{I}=I(V_{\mathbb R}(I))
=\{q\in\mathbb R[z]:q(x)=0\ \forall[x]\in V_{\mathbb R}(I)\}.
\]
Equivalently, \(q\in\sqrt[\mathbb R]{I}\) iff there exist \(k\ge1\) and a sum of squares \(\sigma\) with \(q^{2k}+\sigma\in I\). Its complexification is \(J=\sqrt[\mathbb R]{I}\otimes_{\mathbb R}\mathbb C\).
Source: Real Nullstellensatz; Basu–Pollack–Roy, DOI 10.1007/3-540-33099-2.
Pitfalls: \(\sqrt[\mathbb R]{I}\) is not generally the ordinary radical \(\sqrt I\); computing it is a real-algebraic problem. If \(V_{\mathbb R}(I)\) is Zariski dense in \(V(I_{\mathbb C})\), complexification removes no complex component.

MERGE PROPOSAL (`definitions/definitions.md`, new entry):

### D-real-coherent-span
For \(I\subseteq\mathbb R[z_0,\ldots,z_n]\), \(J=\sqrt[\mathbb R]{I}\otimes_{\mathbb R}\mathbb C\), and degree \(N\),
\[
\mathcal G_N^{\mathbb R}:=
\operatorname{span}_{\mathbb C}\{|x\rangle^{\otimes N}:[x]\in V_{\mathbb R}(I),\ \|x\|=1\}
=(J_N)^\perp.
\]
Thus a D-hamiltonian built from generators whose degree-\(N\) ideal piece is \(J_N\) has ground space equal to the complex span of real-point coherent states.
Source: the reproducing identity in D-coherent-state applied to the vanishing ideal of \(V_{\mathbb R}(I)\).
Pitfalls: the set of real coherent states is nonlinear; only its complex span is a ground space. When the real locus is Zariski dense, \(\mathcal G_N^{\mathbb R}\) equals the ordinary radical complex ground space and does not select real labels.

MERGE PROPOSAL (`definitions/definitions.md`, new entry):

### D-real-structure
For a complex Hilbert space with a fixed real orthonormal basis, \(K\) is coefficientwise conjugation, an antiunitary involution. Its fixed set \(\operatorname{Fix}(K)\) is a real Hilbert space but not a complex-linear subspace. A real-coefficient D-hamiltonian commutes with \(K\), so each eigenspace has a real basis, but degenerate eigenspaces contain complex superpositions and there is no complex-linear projector with range \(\operatorname{Fix}(K)\).
Source: elementary antiunitary linear algebra.
Pitfalls: \(K\)-invariance of an operator does not project onto real points. The scalar \(|\langle\psi|K\psi\rangle|^2\) is nonlinear in a one-copy state and is not the expectation of a one-copy observable.

MERGE PROPOSAL (`definitions/definitions.md`, new entry):

### D-hermite-trace-form
Let \(I\subseteq\mathbb R[x_1,\ldots,x_n]\) be zero dimensional, \(A=\mathbb R[x]/I\), \(\mathcal B=(b_1,\ldots,b_D)\) a basis, and \(M_h\) multiplication by \(h\) on \(A\). For \(g\in\mathbb R[x]\), the Hermite trace form and its matrix are
\[
\mathfrak h_g(u,v)=\operatorname{Tr}_A(M_{guv}),\qquad
\mathcal H_g(\mathcal B)_{ij}=\operatorname{Tr}_A(M_{g b_i b_j}).
\]
Its signature is
\[
\operatorname{sig}\mathcal H_g
=\#\{x\in V_{\mathbb R}(I):g(x)>0\}
-\#\{x\in V_{\mathbb R}(I):g(x)<0\}.
\]
In particular \(\operatorname{sig}\mathcal H_1=\#V_{\mathbb R}(I)\) as a count of distinct real roots.
Source: multivariate Hermite theorem, arXiv:2110.10313.
Pitfalls: this is an algebraic trace form, not D-toeplitz-operator and not merely \(\operatorname{Tr}M_g\). The matrix is basis-dependent by congruence although its inertia is invariant. Exact signature requires integer resolution and can be ill-conditioned numerically.

MERGE PROPOSAL (`definitions/definitions.md`, new entry):

### D-lasserre-order
For a real homogeneous form \(c\) of degree \(2m\) on the unit sphere and an integer \(r\ge m\), the order-\(r\) sphere SOS bound is
\[
\operatorname{sos}_r(c)=
\max\{\lambda:(\sum_i x_i^2)^{r-m}c-\lambda(\sum_i x_i^2)^r\text{ is SOS}\}.
\]
Its dual moment matrix is indexed by homogeneous monomials of degree \(r\), hence acts on \(\operatorname{Sym}^r(\mathbb R^{n+1})\); moments extend through degree \(2r\). Therefore the corresponding D-symmetric-sector has boson number \(N=r\), not \(2r\). For inequalities and equalities, order \(r\) additionally imposes the usual localizing-matrix PSD and equality constraints.
Source: Lasserre, DOI 10.1137/S1052623400366802; Fang–Fawzi, arXiv:1908.05155.
Pitfalls: a general density operator on the symmetric sector is not a moment matrix; the latter has Hankel/maximal-symmetry constraints. A fixed Hamiltonian ground energy is therefore not automatically the Lasserre value.

MERGE PROPOSAL (`definitions/definitions.md`, new entry):

### D-residual-spectral-hierarchy
For real homogeneous residuals \(f_1,\ldots,f_d\) of common degree \(m\), set \(c(x)=\sum_j f_j(x)^2\) and, for \(N\ge m\),
\[
A_N=\frac{(N-m)!}{N!}H_N.
\]
Then \(\langle x^{\otimes N}|A_N|x^{\otimes N}\rangle=c(x)\) for every real unit \(x\), and
\[
\lambda_{\min}(A_N)\le\operatorname{sos}_N(c)\le\min_{\|x\|=1}c(x).
\]
The first value is a presentation-dependent spectral relaxation obtained from the supplied residual Gram representation.
Source: D-coherent-state and D-symmetric-tensor-of-a-form; comparison with the sphere spectral/SOS hierarchies in arXiv:2310.17827 and DOI 10.1137/24M1717750.
Pitfalls: \(\lambda_{\min}(A_N)\) is not generally the order-\(N\) Lasserre value or the canonical Lovitz–Johnston spectral value. The relevant gap for ground-energy estimation is the gap above \(\lambda_{\min}(A_N)\), not D-macaulay-gap unless the minimum is zero.

MERGE PROPOSAL (`definitions/definitions.md`, new entry):

### D-positive-toric-part
For a projective toric ideal \(I_A\), the positive part is \(V(I_A)\cap\mathbb P^n(\mathbb R_{>0})\) and the nonnegative part is its closure in \(\mathbb P^n(\mathbb R_{\ge0})\). The algebraic moment map identifies the nonnegative part with the defining polytope under the standard toric hypotheses. In D-toric-ideal, consistently signed binomial generators produce stoquastic weighted fibre Laplacians whose kernel vectors have nonnegative occupation-basis amplitudes.
Source: Sottile, arXiv:math/0212044.
Pitfalls: occupation-basis positivity is not positivity of a coherent-state label. The positive torus is normally Zariski dense, so its coherent-state span equals the complex toric inverse system and is not selected by a projector.


<!-- Merged verbatim from scouting/robotics-space.md §4 "Proposed definitions" (Opus lane, 2026-09-02); orchestrator merge. Status: proposed. -->

MERGE PROPOSAL (`definitions/definitions.md`, new entry):

### D-streaming-polynomial-input
A one-pass stream `sigma = (g_1, ..., g_T)` whose items are generators of an ideal
`I = (g_1, ..., g_T) subset R` (D-polynomial-ring), each with `poly(n)` monomials and
`poly(n)`-bit coefficients. An algorithm for `sigma` holds `S(n)` bits, or `S(n)` qubits together
with `S(n)` classical bits, reads each item exactly once in the given order, may not revisit an
item, and produces its output after the last item. The **arrival order** is part of the problem
specification. For a fixed prefix split `sigma = sigma_A sigma_B`, one-pass space is at least the
one-way communication complexity of the induced two-party problem, so every one-way lower bound
transfers. Distinguish from D-input-model, where the whole generator tuple is available for
re-reading and `N` is given in unary.
Source: proposed in `scouting/robotics-space.md` §2.2; streaming conventions follow
Clarkson-Woodruff DOI 10.1145/1536414.1536445 and Kallaugher arXiv:2106.04633.
Pitfalls: the model is vacuous for problems whose input is a small generator tuple and whose
large object (`Phi_N`, `H_N`) is derived; it has content only when the generators themselves are
consumed sensor data. The `Omega(sqrt n)` transfers only under a fixed prefix split; adversarial
interleaving needs the Kapralov-Khanna-Sudan / Kallaugher-Parekh-Voronova machinery.

MERGE PROPOSAL (`definitions/definitions.md`, new entry):

### D-quantum-space-measure
For an algorithm on a register of `q` logical qubits with a classical control of `c` bits, the
quantum space is `q + c`, counting every ancilla including those of the row oracle and of QSVT
phase angles, and the algorithm's description must be uniform in `O(q + c)` classical workspace.
Two encodings of `R_N` are used and must never be conflated: the **occupation encoding**,
`(n+1) ceil(log_2(N+1))` qubits (D-input-model), and the **compact encoding**,
`ceil(log_2 M_N)` qubits. Fact SP-0 is stated in the compact encoding; the occupation encoding is
larger by a factor `~ (n+1) log(N)/ (N log n)` and quoting a classical bound against it
overstates the advantage.
Source: proposed in `scouting/robotics-space.md` §1.3-§2.1; class definitions from
Fefferman-Lin arXiv:1604.01384 and Fefferman-Remscrim arXiv:2006.03530.
Pitfalls: `q` logical qubits is not a comparable resource to `q` classical bits of DRAM at any
current or projected error rate; a space claim quoted in logical qubits against a classical
byte count is a category error unless said so.

MERGE PROPOSAL (`definitions/definitions.md`, new entry):

### D-space-time-pareto
A **space advantage** for a problem `P` is a pair of statements: a quantum algorithm attaining
`(S_Q, T_Q)` and a proof that no classical algorithm attains `(S_C, T_C)` with
`S_C = O(S_Q polylog)` and `T_C = O(T_Q polylog)`. By C-NEW-SP-WATROUS-CEILING a pure space
statement (`T` unbounded) can never exceed a quadratic gap in the read-only-input model, so every
nontrivial claim in this campaign is a statement about the `(S, T)` Pareto frontier and must
quote both coordinates for both sides.
Source: proposed in `scouting/robotics-space.md` §0, §1.0.
Pitfalls: a space advantage bought with exponential time is not a claim (brief, task 2); nor is a
time advantage bought with exponential space. The three classical points that must always be
quoted for a succinctly-specified operator are: time-efficient (`O(M_N)` space), space-efficient
(`O(log^2 M_N)` space, `poly(M_N)` time), and any sparsity-exploiting solver in between.

---


<!-- Merged verbatim from scouting/two-copy-real-filter.md "Proposed definitions" (Opus lane, 2026-09-02); orchestrator merge. Status: proposed. -->

MERGE PROPOSAL (`definitions/definitions.md`); full statements in the Statement section, verified in
`checkers/explore/twocopy_real_filter.py`.

### D-pairing-state
`|Phi_N> = sum_{|k|=N}|k>|k>` in the D-fock-basis ONB; `<Phi_N|Phi_N> = M_N = dim R_N`,
`(A x 1)|Phi_N> = (1 x A^T)|Phi_N>`, `SWAP^{T_2} = |Phi_N><Phi_N|`; second-quantised
`|Phi_N> = (C^dag)^N|vac>/N!`, `C = sum_j a_j b_j`, the `N`-photon-per-copy sector of the multimode
two-mode-squeezed vacuum; `(P_sym x P_sym)|Phi_1>^{x N} = |Phi_N>`. Source: standard; part F.
Pitfalls: fixed by `K`, not by the ideal; norm `M_N` collectively versus `(n+1)^N` pairwise, a cost.

### D-two-copy-real-filter
`Pi_N = |Phi_N><Phi_N|/M_N`, compression `F_N = (P_0 x P_0)Pi_N(P_0 x P_0)`; diagonal
`M_N <psi x psi|Pi_N|psi x psi> = R(psi)`; acceptance `R(psi)/M_N` collective, `R(psi)/(n+1)^N`
pairwise; `k`-pair filter `<Phi_k|(psi x psi) = vec(A^T A)`. Source: this memo; PRD D14.
Pitfalls: rank one, eigenvalue `HF_{R/I}(N)/M_N` for every real ideal -- a Hilbert-function ratio,
not a real-point statistic; a measurement, not a projector.

### D-realness-witness
`R(psi) = |psi^T psi|^2/<psi|psi>^2 = Tr(rho rho^T)`, the imaginarity measure (arXiv:1801.05123, DOI
10.1088/1751-8121/aabe9c; arXiv:2007.14847, PRL 126 090401); `R = 1` iff the ray meets `Fix(K)`; on
coherent states `(|p^T p|/|p|^2)^{2N}` with `|p^T p|/|p|^2 = 2F_R(p) - 1 = cos 2t`. Source: part B.
Pitfalls: quadratic, so not a one-copy observable (C-256 stands); realness of a vector, not of a
coherent label -- conjugate-pair ghosts saturate it.

### D-one-particle-reduced-state
`(rho_1)_{ij} = <a_i^dag a_j>_psi/N` on `C^{n+1}`; `Tr(rho_1^2) = 1` iff `psi` is coherent, and
`Tr(rho_1 rho_1^T) = <C^dag C>/N^2` (`= |p^T p|^2/|p|^4` when coherent); both of norm at most one.
Source: this memo; parts C and F.
Pitfalls: it is the one-particle witness, not `R(psi)`; they agree only on coherent states.

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

### Merged from scouting/quantum-primitives.md (2026-09-03; critic loop PASS at verdicts/quantum-primitives-r3.md, all 14 ACCEPT; orchestrator merge, verbatim)

### D-boolean-macaulay-solve

For a Boolean polynomial system \(\mathcal F\subseteq\mathbb F_2[x_1,\ldots,x_n]\), a Boolean Macaulay solve is a complex linear system \(M_{\mathcal F}y=b\) constructed after adjoining Boolean field equations and, where required, lifting finite-field equations to complex equations.

The original Chen–Gao matrix has approximate dimensions

\[
(m+n)(3n+1)^n\times(3n+1)^n.
\]

The reduced Boolean Macaulay matrix of Ding et al. has dimensions

\[
m2^n\times2^n.
\]

Its right-hand-side-dependent truncated QLS condition number is

\[
\kappa_b(M)
=
\|M\|\frac{\|M^+b\|}{\|b\|}.
\]

Source: arXiv:1712.06239 and arXiv:2111.00405.

Pitfalls: this is not D-macaulay-map in Fock norms, its condition parameter is not D-macaulay-gap, and its output is a linear-system state rather than D-projectors. The Grover cost \(O(\sqrt{\binom nh})\) is not a condition-number bound.

### D-curve-zeta-problem

For a smooth projective geometrically irreducible curve \(C/\mathbb F_q\) of genus \(g\),

\[
Z(C,T)
=
\exp\!\left(
\sum_{r\ge1}
\#C(\mathbb F_{q^r})\frac{T^r}{r}
\right)
=
\frac{P_C(T)}{(1-T)(1-qT)},
\]

where \(P_C\in\mathbb Z[T]\) has degree \(2g\).

The computational problem is to output every coefficient of \(P_C\) from a polynomial-size plane model, explicit normalization/desingularization data, and finite-field arithmetic.

Source: arXiv:math/0411623, DOI 10.1007/s00037-006-0204-7.

Pitfalls: the input includes more than one polynomial equation. Kedlaya constructs the unique-encoding class-group/Jacobian operations from this input protocol; they are not an additional oracle promise.

### D-number-field-ideal-problems

Let \(K\) be a number field of degree \(d_K\), discriminant \(\Delta_K\), and ring of integers \(\mathcal O_K\), supplied with an effective integral basis and arithmetic.

The principal ideal problem takes an ideal \(\mathfrak a\subseteq\mathcal O_K\), represented by an integral lattice basis, and asks whether \(\mathfrak a=(\alpha)\). If so, the output must specify whether it is a literal generator or a compact infrastructure/logarithmic representation, because \(\alpha\) may have exponentially many bits.

The unit-group problem asks for the torsion subgroup and a basis of the logarithmic unit lattice representing \(\mathcal O_K^\times\).

Source: DOI 10.1145/1206035.1206039 and DOI 10.1145/2591796.2591860.

Pitfalls: an ideal of \(\mathcal O_K\) is not D-homogeneous-ideal in a coordinate polynomial ring. Hallgren’s 2007 principal-ideal theorem is for real quadratic fields; the arbitrary-degree cited theorem computes unit groups. Output representation and regulator precision are part of the resource statement.

### D-hidden-polynomial-structure

Fix a finite field \(\mathbb F_q\), variable count \(a\), and degree \(t\).

A hidden polynomial structure consists of an unknown \(h\in\mathbb F_q[x_1,\ldots,x_a]\) and a coherent oracle \(O\) whose level sets coincide with the fibers of \(h\), while distinct fibers receive distinct arbitrary labels.

The task is to identify \(h\) up to scalar or other equivalences invisible to the labeled partition.

Source: arXiv:0705.2784, arXiv:0706.1219, and arXiv:1107.2189.

Pitfalls: this oracle is stronger than coefficient access, value access, membership in one zero set, or classical samples from one fiber.

### D-jacobian-ring-susy

For \(W\in\mathbb C[z_0,\ldots,z_n]\),

\[
J_W=(\partial_0W,\ldots,\partial_nW),
\qquad
\operatorname{Jac}(W)=R/J_W.
\]

A Jacobian-ring SUSY model is a graded supercharge complex whose cohomology is \(\operatorname{Jac}(W)\) under isolated-critical-locus and regularity hypotheses.

The following campaign assertion is [UNVERIFIED]: for a Landau–Ginzburg model with isolated non-degenerate critical locus, all vacua lie in one fermion-number sector and

\[
\operatorname{Tr}(-1)^F
=
\pm\mu
=
\pm\dim\operatorname{Jac}(W).
\]

Source: DOI 10.1016/0550-3213(89)90474-4 and DOI 10.1016/0370-2693(89)90473-5.

Pitfalls: Landau–Ginzburg chiral-ring cohomology, Witten’s de Rham complex, and the finite-degree seed inverse system are related but not identical Hilbert-space models. Alternating-index cancellation in a de Rham model does not refute the Landau–Ginzburg equality above. The cited sources identify the chiral ring with the Jacobian quotient but no specific theorem or equation for the displayed \(\pm\mu\) assertion has been supplied.

### D-vr-betti-estimation

For a graph \(G\) on \(s\) sampled points, let \(\mathrm{Cl}_k(G)\) be its set of \(k\)-vertex cliques, hence its \((k-1)\)-simplices. Let \(\Delta_{k-1}\) be the corresponding combinatorial Laplacian, \(\beta_{k-1}=\dim\ker\Delta_{k-1}\), and \(\Gamma_{k-1}\) its smallest nonzero eigenvalue.

Normalized Vietoris–Rips Betti estimation returns

\[
\frac{\beta_{k-1}}{|\mathrm{Cl}_k(G)|}
\]

to stated additive or relative error, including clique-mixture preparation and spectral filtering in the cost.

Persistent estimation replaces one kernel dimension by the appropriate image rank between two Vietoris–Rips filtration scales.

Source: arXiv:1408.3106 and arXiv:2209.13581.

Pitfalls: Niyogi–Smale–Weinberger reconstruct a positive-reach submanifold through a union of balls and its Čech nerve. A separate VR–Čech interleaving and persistence-interval argument is required before this normalized VR output is identified with a Betti number of the sampled real variety.

### D-coherent-path-oracle

For a homotopy with \(D\) indexed start solutions, a coherent path oracle is a reversible circuit

\[
|i\rangle|0\rangle
\longmapsto
|i\rangle|\widetilde x_i(1)\rangle|\mathrm{work}_i\rangle
\]

that tracks path \(i\) to the target parameter, bounds failure and branch-switching error, evaluates a marked-root predicate, and can be uncomputed.

Its cost \(C_{\mathrm{track}}(\mu,L,b)\) includes conditioning \(\mu\), predictor-corrector length \(L\), arithmetic precision \(b\), and every stored or recomputed checkpoint.

Source: proposed here from arXiv:1609.08722 and amplitude amplification.

Pitfalls: a classical adaptive tracker is not automatically reversible or coherent. Under \(O(\sqrt{D/r})\) oracle invocations, the per-invocation error must be \(o(\sqrt{r/D})\), not merely a bound on an unspecified total error.

### D-multihomogeneous-bezout

For a nonnegative \(n\times n\) degree matrix \(A=(A_{ij})\), define

\[
B_A
=
[t_1\cdots t_n]
\prod_{i=1}^n
\left(\sum_{j=1}^n A_{ij}t_j\right).
\]

This is the multihomogeneous Bézout coefficient for the corresponding square system with one-dimensional variable blocks. Direct coefficient expansion gives

\[
B_A
=
\sum_{\sigma\in S_n}\prod_iA_{i,\sigma(i)}
=
\operatorname{per}(A).
\]

Source: multihomogeneous Bézout theorem and coefficient expansion.

Pitfalls: \(B_A\) is not the general BKK mixed volume. Optical access to an event with probability proportional to \(|B_A|^2\) is a separate object, D-optical-counting-access.

Amendment (2026-09-03, scouting/quantum-native.md, verdicts/quantum-native-r3.md): general-\(q\) coefficient

\[
B_D
=
[t_1^{q-1}\cdots t_n^{q-1}]
\prod_{a=1}^{n(q-1)}
\left(\sum_i d_{ai}t_i\right).
\]

For \(q=2\), \(D\) is square and this coefficient is \(\operatorname{per}(D)\). Definition 52 and Observation 55 of arXiv:2412.19623 supply the PRODSAT Bézout/weighted-SDR formulation; arXiv:2005.14485 supplies the permanent formulation for the one-dimensional-block case.

Pitfalls: this counts product solutions with multiplicity, not QSAT ground-space degeneracy, and it applies directly only to square subsystems.

### D-optical-counting-access

Optical counting access to a matrix \(A\) means an efficiently prepared passive or Gaussian optical experiment whose specified outcome \(S\) has probability

\[
p_S=c(A,S)|\operatorname{per}(A_S)|^2,
\]

or the analogous hafnian or Torontonian expression, with the normalization \(c(A,S)\) known.

Source: arXiv:1011.3245, arXiv:1612.01199, and arXiv:1807.01639.

Pitfalls: sample access does not give signed amplitudes, relative estimation of a rare \(p_S\) costs \(\Omega(1/p_S)\) shots, and embedding a nonunitary matrix can make \(c(A,S)\) exponentially small.

### D-analogue-degeneracy-readout

For a physical realization of D-hamiltonian, an analogue degeneracy readout is a protocol estimating

\[
\dim\ker H_N
\quad\text{or}\quad
\frac{\dim\ker H_N}{\dim R_N}
\]

with specified confidence, temperature, state preparation, energy resolution, and shot count.

Source: proposed here; algebraic identity from D-ground-space.

Pitfalls: spectroscopy of one ground state, measurement of zero energy, and low-temperature occupation do not individually determine the degeneracy. Resolving a normalized fraction to additive error \(\varepsilon\) from independent samples requires \(\Omega(1/\varepsilon^2)\) shots.

### D-boolean-residual-energy

For Boolean polynomials \(p_i\in\mathbb F_2[x_1,\ldots,x_n]\), a Boolean residual-energy Hamiltonian is a diagonal real Hamiltonian obtained by converting each Boolean function to an integer-valued numerical normal form and adding nonnegative penalties so that its zero-energy bit strings are precisely the common zeros.

Source: arXiv:2111.13224, DOI 10.1103/PhysRevResearch.4.013096.

Pitfalls: the ANF-to-integer conversion can have \(2^n-1\) terms; quadratization of a general \(n\)-body term can require \(2^{(n+2)/2}-2\) total qubits for even \(n\) or \(3\cdot2^{(n-1)/2}-2\) for odd \(n\), before minor embedding.

### D-tensor-secant-problem

For \(T\in V_1\otimes\cdots\otimes V_p\), CP rank at most \(r\) means that \(T\) is a sum of at most \(r\) simple tensors.

Border rank at most \(r\) means that \([T]\) lies in the \(r\)-th secant variety of the Segre variety; for symmetric tensors use the Veronese variety and Waring rank.

Source: arXiv:0911.1393 and arXiv:1512.04312.

Pitfalls: matrix flattening rank, Tucker rank, HOSVD rank, CP rank, and border rank are different outputs.

### D-real-variety-gibbs

For real polynomials \(f_1,\ldots,f_d\), compact domain \(K\), and \(\beta>0\),

\[
\pi_\beta(dx)
=
Z_\beta^{-1}
e^{-\beta\sum_jf_j(x)^2}
\mathbf1_K(x)\,dx.
\]

A real-variety Gibbs sampler returns a sample within stated total-variation distance of \(\pi_\beta\).

Source: proposed here; partition-function annealing framework from arXiv:0811.0596.

Pitfalls: finite \(\beta\) samples a tube, not the variety; mixing can be exponentially slow across components, and a bosonic Gibbs state is not automatically this classical coherent-state distribution. The Wocjan et al. theorem assumes an FPRAS built from MCMC along a non-adaptive cooling schedule and does not prove a polynomial gap for polynomial residuals.

### D-toric-lattice-counting

For a rational polytope \(P\subset\mathbb R^d\),

\[
L_P(N)=|NP\cap\mathbb Z^d|
\]

is its Ehrhart counting function.

The exact task returns \(L_P(N)\) or the Ehrhart polynomial; the approximate-volume task returns \(\operatorname{vol}(P)\) multiplicatively.

Source: DOI 10.1287/moor.19.4.769 and arXiv:math/0211146.

Pitfalls: volume estimation, uniform lattice-point sampling, and exact Ehrhart evaluation are inequivalent. The cited quantum volume algorithm has an \(\Omega(\sqrt d+1/\varepsilon)\) membership-query lower bound.

### Merged from scouting/koszul-betti.md (2026-09-03; critic loop verdicts/koszul-betti-r1..r5, PASS at r5, codex critic; all 8 ACCEPT; orchestrator merge, text verbatim from memo §5 with the memo's adjudication annotations removed; D-betti-gap, D-normalised-betti-fraction and D-betti-estimation-problem are the critic's r2 texts D5/D6/D8)

### D-fermionic-modes
`c_k, c_k^†` (`k = 0..n`) on `Lambda(C^{n+1})`
with `{c_k, c_l^†} = delta_{kl}`; basis `|S>`, `S ⊆ {0..n}`;
`c_k^†|S> = (-1)^{#{l in S : l<k}}|S ∪ {k}>` for `k not in S`, else 0; `F̂ = sum_k c_k^† c_k`.
Pitfall: dropping the sign breaks `Q^2 = 0` (mutation M3, run in-process).

### D-koszul-supercharge
On the **finite-particle core** `R ⊗ Λ` of
`F ⊗ Lambda(C^{n+1})`, `Q = sum_k a_k ⊗ c_k^†` (D-mode-operators, D-fermionic-modes);
`Q^2 = 0` exactly; `Q` maps block `(i,N)` to `(i+1,N-1)` and preserves `j = N+i`. With
`P = ⊕_N P_{0,N}` the **degreewise direct-sum** ground-space projector and `P̂ = P ⊗ 1`, the
restriction `q = Q P̂ = P̂ Q P̂` is well defined because `W` is `a_k`-invariant. Under the
conjugate-linear Fock pairing `(W ⊗ Lambda, q)` is the **conjugate dual** of the Koszul
complex of `R/I` on the variables. Pitfall: `Q^†` does not restrict; its restriction is
`sum_k Z_k ⊗ c_k` (D-compressed-multiplication). `a_k, Q, L` are unbounded on the completion.

### D-betti-laplacian
Globally on `W ⊗ Lambda`, `L_W = q q^† + q^† q`, which
preserves each internal-degree sector `j` and each block `(i,N)`, `N + i = j`. On a fixed `j`
sector, `L_W = j P̂ - X X^†` with `X = P̂ Q (1 - P̂)`; hence `0 <= L_W <= j P̂` and
`||L_W|| <= j`. A block may have `L_W|(i,N) = 0` (no positive spectrum); such a block admits
no gap and no gap promise. Pitfall: `L_W != P̂ L P̂`, which is the scalar `j P̂`.

### D-graded-betti-number
`beta_{i,j}(R/I) = dim Tor_i^R(R/I,C)_j`;
`beta_{i,j} = 0` for `i > n+1` and for `j - i > reg(R/I)`, where
`reg(R/I) = max{j-i : beta_{i,j} != 0}` and `reg(I) = reg(R/I) + 1` for a nonzero proper
homogeneous ideal. `beta_{1,j}` counts minimal generators of `I` in degree `j`; `beta_{2,j}`
counts the degree-`j` minimal relations **in a minimal free resolution**, equivalently among
a **minimal homogeneous presentation** — the quotient `Syz/m Syz` of an arbitrary tuple's
syzygy module is *not* `beta_2` (counterexample `(x,x)`). `Syz(I)_N` (D-syzygy-module) is a
tuple invariant, not a Betti number.

### D-betti-gap
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

### D-normalised-betti-fraction
> Let \(M_N=\dim R_N\), \(h_N=\mathrm{HF}_{R/I}(N)\), and
> \(b=\binom{n+1}{i}\). The ambient normalized Betti fraction is
> \(\beta_{i,i+N}/(M_Nb)\). It equals the normalized trace of the harmonic
> projector on \(W_N\otimes\Lambda^i\) extended by zero to
> \(R_N\otimes\Lambda^i\); it is not the zero-eigenvalue fraction of \(L_W\)
> extended by zero. When \(h_N>0\), the conditional fraction is
> \(\beta_{i,i+N}/(h_Nb)\). Estimating the conditional ratio requires normalized
> access to \(W_N\), with ambient acceptance weight \(h_N/M_N\), or an explicit
> preparation oracle.

### D-generator-koszul-supercharge
For positive-degree homogeneous
`f_1,...,f_d`, `Q_f = sum_j M_{f_j} ⊗ c_j` with **fermionic annihilators** `c_j` on
`Lambda(C^d)`, fermion `j` carrying internal weight `deg f_j` (a weighted internal grading).
On the finite-particle core `Q_f^2 = 0`; the fermion-number-zero Laplacian block is
`sum_j M_{f_j} M_{f_j}^† = H` (D-hamiltonian). Only the **zero-mode dimensions** of the higher
blocks compute `H_i(f;R) ≅ Tor_i^{C[y_1..y_d]}(C,R)`, and all positive homology vanishes iff
the positive-degree sequence is regular. Pitfall: these are not `beta_{i,j}(R/I)`.

### D-betti-estimation-problem
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

### Merged from scouting/quantum-native.md (2026-09-03; critic loop verdicts/quantum-native-r1..r3, PASS at r3, Opus critic; 8 ACCEPT with D-QN-MULTIPROJECTIVE-SATURATION reworded per r3 O30; orchestrator merge, verbatim)

### D-QN-QSAT-IDEAL
For a quantum \(k\)-SAT instance \(Q=\{\Pi_a\}\), choose an orthonormal rank-one decomposition

\[
\Pi_a=\sum_\mu|\phi_{a\mu}\rangle\langle\phi_{a\mu}|.
\]

Write each \(|\phi_{a\mu}\rangle\) as a multilinear coefficient tensor on its support and form \(f_{a\mu}\) using those coefficients unconjugated. The **QSAT ideal** is

\[
I_Q=(f_{a\mu})
\]

in the Cox ring of \((\mathbb P^{q-1})^n\).

The ideal does not depend on the chosen orthonormal rank-one decomposition, because
\(\operatorname{span}_{\mu}\{f_{a\mu}\}\) is the image of
\(\operatorname{ran}\Pi_a\) in the multilinear forms on \(S_a\); another orthonormal decomposition changes these generators by a unitary matrix.

Source: D-multidegree-sector, D-quantum-k-sat, C-030–C-032.

Pitfalls: coefficients are taken unconjugated; this is what makes
\(a^\dagger(f)a(f)|_{R_{\mathbf1}}=|\phi\rangle\langle\phi|\). The ideal forgets positive weights and spectral conditioning. Under C3 its ground space is the multidegree-\(\mathbf1\) inverse system of \(\overline{I_Q}\).

### D-QN-MULTIPROJECTIVE-SATURATION
For

\[
R=\mathbb C[z_{i,s}]
\]

with site multigrading, let

\[
B=\bigcap_i(z_{i,0},\ldots,z_{i,q-1}).
\]

The **reduced multiprojective saturation** of \(I\) is

\[
J=\sqrt{I:B^\infty}.
\]

By the multiprojective Nullstellensatz, \(J\) is the multihomogeneous vanishing ideal of the reduced closed subscheme

\[
V_{X_0}(I)\subseteq(\mathbb P^{q-1})^n,
\]

of any dimension. Adopt \(I(\varnothing)=R\). If
\(V_{X_0}(I)=\varnothing\), then \(B\subseteq\sqrt I\), hence
\(B^k\subseteq I\) for some \(k\), so \(I:B^\infty=R\).

Source: Cox–Little–Schenck, `Toric Varieties`, GSM 124, AMS 2011 (ISBN:978-0-8218-4819-7): Proposition 5.2.6 (Toric Weak Nullstellensatz) for the empty case, Proposition 5.2.7 (Toric Ideal-Variety Correspondence), and Proposition 6.A.7 for the B(Σ)-saturation normalisation; multiprojective use in arXiv:2412.19623.

Pitfalls: \(I_{\mathbf1}=J_{\mathbf1}\) is only a degreewise equality and does not imply global radicality or saturation. The closed subscheme need not be finite. (P^{q-1})^n is smooth, hence simplicial, so the hypotheses of 5.2.6/5.2.7 (simplicial) and 6.A.7 (smooth) are met; 5.2.7 normalises the ideal of a subvariety as a radical ideal contained in B(Σ) rather than as the B-saturation, and the two agree in multidegree 1 because B_1 = R_1.

### D-QN-PRODUCT-SPAN
For a QSAT ideal \(I_Q\) and
\(J_Q=\sqrt{I_Q:B^\infty}\), the **product-ground span** is

\[
\mathcal P_Q=(J_Q)_{\mathbf1}^{\perp}.
\]

Equivalently,

\[
\mathcal P_Q
=
\operatorname{span}
\left\{
\bigotimes_i|\overline{x_i}\rangle:
x\in V_{X_0}(I_Q)
\right\},
\]

with \(\mathcal P_Q=\{0\}\) when the variety is empty.

Source: D-coherent-state and C-028.

Pitfalls: \(\mathcal P_Q\) contains entangled superpositions; it is not the set of product states.

### D-QN-MULTIGRADED-ENTANGLED-DEFECT
The **multigraded entangled defect** of \(Q\) is

\[
e_Q
=
\dim(I_Q)_{\mathbf1}^{\perp}
-
\dim(J_Q)_{\mathbf1}^{\perp}
=
\dim(J_Q)_{\mathbf1}-\dim(I_Q)_{\mathbf1}.
\]

Source: specialization of D-entangled-defect.

Pitfalls: it counts linear directions orthogonal to the product-ground span, not entangled rays or an entanglement entropy.

### D-QN-COPY-RESIDUAL-OBSERVABLE
For homogeneous degree-\(m\) equations \(f_j\) on a pure-state amplitude space, let
\(|F_j\rangle\in\operatorname{Sym}^m(\mathcal H)\) satisfy, under C3,

\[
\overline{f_j(\overline\psi)}
=
\langle F_j|\psi^{\otimes m}\rangle.
\]

C-019 gives

\[
\|F_j\|=\|f_j\|_{\mathrm{BW}}.
\]

For \(w_j\ge0\), define

\[
\Lambda=\sum_jw_j\|F_j\|^2,
\qquad
A_F=\Lambda^{-1}\sum_jw_j|F_j\rangle\langle F_j|.
\]

Then \(A_F\) acts on \(\operatorname{Sym}^m(\mathcal H)\), satisfies
\(0\le A_F\le\mathbb1\), and has expectation

\[
\langle\psi|^{\otimes m}A_F|\psi\rangle^{\otimes m}
=
\Lambda^{-1}\sum_jw_j|f_j(\overline\psi)|^2.
\]

Each shot consumes \(m\) copies.

Source: D-coherent-state, C-019, and the normalized form of C-027.

Pitfalls: residual is not distance; implementing the sum can scale with the number of generators; uncontrolled copies do not supply amplitude-estimation reflections.

### D-QN-TENSOR-NETWORK-VARIETY
For a graph \(G\), local dimensions, and bond bounds \(\boldsymbol\chi\), the
**tensor-network variety** is the Zariski closure of the polynomial contraction image.

For trees and open chains, the bounded-rank locus is characterized by edge-flattening rank conditions
(arXiv:2608.19071). arXiv:1501.01120 concerns comparison of tree tensor formats.

Source: arXiv:1105.4449, arXiv:1501.01120, arXiv:2101.03148,
arXiv:2608.19071.

Pitfalls: the exact parametrized image can be nonclosed; “bond dimension exactly
\(\chi\)” is generally a stratum rather than the closed variety.

### D-QN-PHYSICAL-DATA-ACCESS
D-QN-PHYSICAL-DATA-ACCESS **extends**, rather than replaces, the campaign’s classical
D-input-model. A physical data-state problem must specify one of:

1. uncontrolled copies of \(\rho\);
2. a preparation circuit \(U_\rho\);
3. controlled \(U_\rho,U_\rho^\dagger\);
4. classical measurement samples;
5. a classical amplitude description.

For a comparison, both algorithms must receive the same declared input or the statement must explicitly describe different measurement models on the same physical source.

Source: D-input-model; proposed extension for physical/copy access.

Pitfalls: copy bounds, coherent-query bounds, and classical input runtimes cannot be compared without fixing the access model. A classical copy-access baseline means single-copy, possibly adaptive measurements followed by classical post-processing, not possession of a dense amplitude array.

### D-QN-DUAL-RAIL-SECTOR
The **dual-rail \(\mathbf1\) sector** for \(n\) qubits is the two-optical-mode-per-site Fock subspace with exactly one photon in each mode pair.

Source: D-multidegree-sector; linear-optical computation in
DOI:10.1038/35051009.

Pitfalls: general passive interferometers do not preserve per-site occupation; output postselection is not an energetic hard-core constraint.

### Merged from scouting/intersection-observables.md (2026-09-03; critic loop verdicts/intersection-observables-r1..r3, PASS at r3, codex critic; orchestrator merge, verbatim from memo "Proposed definitions": the adjudicated rewordings of the r1/r2 critic in the memo's ASCII convention)

### D-intersection-overlap
"For homogeneous ideals `I, J`
and degree `N`, define
`T_N(I,J) = Tr(P_{0,N}^{(I)} P_{0,N}^{(J)}) = Tr(P_{0,N}^{(I)} P_{0,N}^{(J)} P_{0,N}^{(I)}) >= 0`.
Equivalently, `T_N = ||B_I^dag B_J||_F^2` for orthonormal ground-space bases. When `I, J` are radical
and `N` is in their stable ranges, the two factors are the Bergman projectors of
D-bergman-projector. The normalizations in use are `tau_N = T_N/M_N`, `T_N/sqrt(HF_I HF_J)`, and
`T_N/(HF_I HF_J) = Tr(rho_I rho_J)`. It is not
`Tr(P_{I_N}P_{J_N}) = M_N - HF_I - HF_J + T_N`."
Retained note (r1, folded in from the deleted C-NEW-IO-PROJECTOR-AMBIGUITY row): the seed's
Conjecture 8.10(a) and rows C-085, C-166, C-167 do not say which projector they mean, and only the
`P_{0,N}` reading has the asserted geometric asymptotics, so those rows should be amended to cite
this id. The three normalisations differ by factors exponential in codimension, so a signal-size
statement must say which.

### D-clean-intersection
"Smooth `V, W` in `CP^n` intersect cleanly along a
smooth pure-dimensional `Z = V ^ W` if `T_xZ = T_xV ^ T_xW` for every `x in Z`. Transverse
intersections are clean; clean intersections may have excess dimension."

### D-intersection-angle-condition-number
"For a clean intersection, let
`A_x = T_xV (-) T_xZ` and `B_x = T_xW (-) T_xZ`. Define `J(x) = prod_i sin^2 theta_i(x)`, padding the
principal-angle list with `pi/2` when the dimensions differ, and `mu_cap = sup_Z J^{-1} < infinity`.
No universal crossover scale follows from this definition alone."

### D-bergman-frame-operator
"Define
`S_V^{(N)} = int_V |e_p><e_p| dvol_V(p)`. Exactly,
`ran S_V^{(N)} = (I(V)_N)^perp = ran P_{0,N}^{(I(V))}`. The claimed operator-norm asymptotic is
`S_V^{(N)} = (pi/N)^k(P_{0,N}^{(I(V))} + E_N)`, with `||E_N|| = O(N^{-1})`. This asymptotic is a
separate conjectural/theorem claim requiring a precise source; it is not part of the definition."
(r2, verdict O10: the r1 text wrote `P_{I(V),N}`, which under D-projectors denotes the projector
onto the ideal piece -- the wrong complementary projector.)

### D-normalised-toeplitz-operator
"For `N >= r` and a
bihomogeneous polynomial `g(z, conj z)` of bidegree `(r,r)`, regarded as a projective symbol by
evaluation on unit representatives, define
`T~_g^{(N)} = ((N-r)!/N!) P_{0,N} :g(a^dag,a): P_{0,N}`. If `I` is radical, `N` is stable, and
`x in V(I)`, then the C3-compatible restricted coherent-state symbol is exactly
`<conj(x)^{x N}| T~_g^{(N)} |conj(x)^{x N}> = g(x, conj x)`."
A distinct definition, not an amendment to D-toeplitz-operator (verdict O3). (r2, verdict O10: the
r1 text said "`p in V(I)`", violating binding convention C3, under which a geometric point
`x in V(I)` is carried by the coherent state `|conj(x)>^{x N}`.)

### D-contact-order
"At a common point of smooth plane curves choose holomorphic
coordinates unitary for the Fubini-Study metric at the point and flatten `W` to `v = 0`. If `V` has
`v = gamma u^m + O(u^{m+1})`, `gamma != 0`, then `m` is the contact order and local intersection
multiplicity. `m = 1` is transverse; `m >= 2` is tangent."

## Lane report

Included: 66 entries in five parts - the three inner products with exact degreewise scalars; all operators ($a_j$, $a(f)$, $M_f$, $\Phi_N$, shifts, compressed multiplications); ideals, Hilbert function, inverse system, monomial/toric/boolean/clause ideals, Grobner deformation; Hamiltonian, ground space, frustration-freeness, parent Hamiltonians, $k$-body vs few-mode, $\Delta_N$ and its normalisations, coherent states, Takagi; algorithmic/geometric objects (input model, QSVT, the distance-to-ideal problem verbatim, Bergman projector, hardness anchors, condition number, hard-gap instances, finite fields, Bose-Hubbard). Every mandatory entry in the brief is present. `D-reserved-photonic` is a stub: the seed uses no boson-sampling / linear-optics / GBS object, so it lists what must be defined first. 14 OPEN issues, 5 of them substantive (OPEN-1,3,5,6,7); `notation.md` holds the symbol table and 18 page81-vs-report conflicts with the chosen convention.

Could not pin down: (i) the normalisation actually used in the numerical survey (OPEN-1/3), which decides whether the survey is evidence for Conjecture 8.3; (ii) an ideal-invariant form of Fact 4.2 (OPEN-6); (iii) ids for Fang 2003, Fischer 1918, Shapiro 1989, Iarrobino-Kanev, BBEM 1990, Tian-Zelditch-Catlin, Bordemann-Meinrenken-Schlichenmaier, Douglas-Tang-Yu, Chen-Gao - all left [UNVERIFIED].

MERGE PROPOSAL (CLAUDE.md §3, new rule 10): "Conventions C1-C12 of `definitions/definitions.md` are binding; an artifact departing from one says so in its first paragraph, and cites definition ids rather than restating definitions."
MERGE PROPOSAL (PRD.md, scope note): the campaign's spectral promise is on the normalised gap $\Delta_N/\alpha_{\mathrm{BE}}$; absolute $\Delta_N$ statements are presentation artefacts (C5, C7).
MERGE PROPOSAL (HANDOFF.md, conventions block): replace "Sphere/Bombieri norms agree with Fock only degreewise" by the exact scalars of D-norm-comparison, and add "Fact 7.1's uniform gap is a Fock-normalisation statement; in Bombieri-Weyl it reads $\Delta_N\ge\binom Nm^{-1}\|f\|^2_{\mathrm{BW}}$", and "$\Delta_N$ survey numbers in report §7 are unit-coefficient, not unit-BW (OPEN-1)."
