# Waring packet fusion with separating subsets

Independent derivation of the orchestrator's coded synchronization proposal,
2026-09-05, under `qaag-eji`. This memo uses the ordinary tensor Hilbert norm,
explicitly departing from the cross-degree Fock default C1; local dimension is
`q=n+1` as in C2. Displayed I denotes an identity, a local departure from C6.
Canonical source and packet definitions are in `definitions/waring-components.md`.
Claim status is recorded only in `claims/CLAIMS.md`, C-342--C-346; the independent
review is `verdicts/waring-coded-fusion-r1.md`. No historical originality is claimed.

The proposed circuit and normalization check out. Binary separating subsets
reduce the number of alternating hyperedges from `r-1` to `ceil(log_2 r)` and
the minimum useful source order from `r+1` to `ceil(log_2 r)+2`. The prescribed
seed still has probability at most `r^(-r)`; this is not an algorithm polynomial
in growing rank. No classical advantage or D22 originality is established here.

## 1. Input, output, and packet normalization

Let `r>=2`, `q>=r`, and let `u_1,...,u_r` be independent unit vectors in `C^q`.
The source supplies copies of the normalized pure symmetric tensor

\[
 T=\sum_{a=1}^r c_a u_a^{\otimes k},\qquad c_a\ne0.             \tag{1}
\]

The components, coefficients, Gram matrix, and inverse source circuit are not
supplied. For this independent-component family at `k>=3`, the Waring points are
identifiable; outputting packets is still different from describing those points.
One source call means one fresh `T` copy. An optional preparation cost `G_T` is
charged separately if a physical source implementation is part of the input.

Put `G_ab=<u_a,u_b>` and `G_m=G^(circ m)`, the entrywise `m`th power. For sign
parity `sigma` in `{0,1}`, define unnormalized and normalized permutation packets

\[
 w_m^\sigma=\sum_{\pi\in S_r}\operatorname{sgn}(\pi)^\sigma
           \bigotimes_{i=1}^r u_{\pi(i)}^{\otimes m},\qquad
 \Omega_m^\sigma=w_m^\sigma/\sqrt{N_\sigma(m)},                 \tag{2}
\]
\[
 N_1(m)=r!\det G_m,\qquad N_0(m)=r!\operatorname{per}G_m.       \tag{3}
\]

To prove (3), expand the squared norm over `pi,tau`. Relabel the product by `pi`
and sum over `tau pi^(-1)`; the remaining outer sum contributes `r!`.
Independence makes all denominators positive. The exact output task is to grow
these packets on the attainable degrees specified below. No measurement or
classical coordinate description of a component is included in this task.

## 2. The coded circuit and its phases

Let `b=ceil(log_2 r)`. Give row `i` the `b`-bit expansion of `i-1`, and let
`S_j` contain rows whose bit `j` equals one. Take input packets
`Omega_m^(sigma_A)` and `Omega_n^(sigma_B)`, with `m,n>b`.

For each bit `j`, select one unused slot from packet-A row `i` if `i in S_j`,
and from packet-B row `i` otherwise. Apply the orthogonal alternating projector

\[
 P_{\wedge^r}=\frac1{r!}\sum_{\tau\in S_r}
                          \operatorname{sgn}(\tau)U_\tau       \tag{4}
\]

to these `r` registers, and postselect acceptance. Order its input registers by
the original row order `1,...,r`. Different hyperedges use distinct physical
slots, so their projectors commute. Each row loses exactly `b` slots across the
two packets, giving output row degree

\[
                         \ell=m+n-b.                         \tag{5}
\]

Fix two input labelings `pi_A,pi_B`. A hyperedge is nonzero precisely when

\[
 \pi_A(S_j)\cap\pi_B(S_j^c)=\varnothing
 \quad\Longleftrightarrow\quad \pi_A(S_j)=\pi_B(S_j).           \tag{6}
\]

Thus `tau=pi_B^(-1) pi_A` preserves every `S_j`. Distinct binary signatures
force `tau` to fix each row. The surviving pairs are exactly `pi_A=pi_B=pi`.

Let `omega` be the normalized wedge of `u_1,...,u_r`. On a surviving pair, the
row-ordered register labels of *every* hyperedge are
`u_(pi(1)),...,u_(pi(r))`. Its output therefore is

\[
 \operatorname{sgn}(\pi)\sqrt{\det G/r!}\,\omega.              \tag{7}
\]

Multiplying (7) over the `b` independent edges and the two input signs gives

\[
 \sigma_{out}=\sigma_A+\sigma_B+b\pmod2,                       \tag{8}
\]
\[
 K(\Omega_m^{\sigma_A}\otimes\Omega_n^{\sigma_B})
 =\left(\frac{\det G}{r!}\right)^{b/2}
   \sqrt{\frac{N_{\sigma_{out}}(\ell)}
               {N_{\sigma_A}(m)N_{\sigma_B}(n)}}
   \omega^{\otimes b}\otimes\Omega_\ell^{\sigma_{out}},        \tag{9}
\]
\[
 p_{m,n}=\left(\frac{\det G}{r!}\right)^b
          \frac{N_{\sigma_{out}}(m+n-b)}
               {N_{\sigma_A}(m)N_{\sigma_B}(n)}.              \tag{10}
\]

There is no additional sign with row-ordered edges. If hardware instead lists
the A rows first and then the B rows, edge `S` adds the known constant sign
`(-1)^(number of pairs i in S,j in S^c with i>j)`. Their product is a global
phase independent of the hidden components and can be ignored.

## 3. Sharp hyperedge count within the stated model

Consider any `t` tests of the same form: one row-complementary `r`-register
alternation per subset, and postselect all of them. Each row has its membership
signature in `{0,1}^t`. If two rows have the same signature, their transposition
preserves every tested subset, so a nonmatching pair of labelings survives (6).
Exact synchronization consequently requires `r<=2^t`, hence

\[
                         t\ge\lceil\log_2r\rceil.            \tag{11}
\]

Binary subsets attain this bound. This optimality is only for these complementary
row-selection all-distinct tests. It is not a lower bound for arbitrary quantum
instruments, refined measurements, additional state preparation, or approximate
synchronization. In particular, it is not a quantum/classical separation.

## 4. Rank-four and rank-five examples

With rows numbered from one, the separating subsets are:

| Rank | `b` | Subsets | Minimum `k` | Seed degree | Next degree | Next sign |
|---|---:|---|---:|---:|---:|---|
| 4 | 2 | `{2,4}`, `{3,4}` | 4 | 3 | 4 | symmetric |
| 5 | 3 | `{2,4}`, `{3,4}`, `{5}` | 5 | 4 | 5 | alternating |

For rank four the row-ordered hyperedges are
`(B1,A2,B3,A4)` and `(B1,B2,A3,A4)`, using fresh slots at repeated rows.
Of the `24^2=576` input permutation pairs, exactly 24 survive.
For rank five, add the edge `(B1,B2,B3,B4,A5)` to the analogous first two
five-row edges. Exactly 120 of `120^2=14400` pairs survive.

Deleting the last hyperedge leaves 96 survivors at rank four and 240 at rank
five, including nonmatching pairs. This provides a concrete falsification of a
code with too few tests. The phase is `sgn(pi)^2=1` at rank four and
`sgn(pi)^3=sgn(pi)` at rank five for two alternating inputs.

## 5. Seed, restart accounting, and all rank dependence

Apply one `r`-register alternation to one slot from each of `r` source copies.
Only distinct component labels survive, producing `Omega_(k-1)^1` with

\[
 p_0=\left|\prod_a c_a\right|^2\det G\det G_{k-1}.             \tag{12}
\]

The expected seed cost is `C_0=r/p_0`. Let `rho_1` be the one-slot reduced state
of normalized `T`, which has rank `r`. Factoring it through the column matrix
`[u_1 ... u_r]` gives the crucial identity

\[
 p_0=\det{}_+(\rho_1)
    =\prod_{a=1}^r\lambda_a(\rho_1)\le r^{-r},\qquad
                         C_0\ge r^{r+1}.                     \tag{13}
\]

Here `det_+` means the product of the nonzero eigenvalues; their sum is one.
This avoids incorrect conclusions from the coefficients alone: near-canceling
normalized coefficients can grow, so a small Gram determinant by itself does
not prove a small `p_0`. Equation (13) does prove a rank-dependent ceiling for
this *specific seed*, not for every possible seed-preparation algorithm.

Doubling equal-size packets gives

\[
 m_j=b+(k-1-b)2^j,\qquad C_{j+1}=2C_j/p_{m_j,m_j}.             \tag{14}
\]

Growth requires `k>=b+2`. The seed has sign one; after the first doubling,
the sign is `b mod 2` and remains so. Unequal-size fusion (5) permits other
degrees: a tree with `L` seeds yields degree `b+(k-1-b)L` and sign
`L+(L-1)b mod 2`. Discarding surplus slots is not an exact pure-packet degree
reduction, so attainable degrees must be stated rather than silently rounded.

For a uniform promise theorem, assume known `p_0>=p_*` and `G>=eta I`,
with `eta>0`. The Schur product theorem gives `G_m>=eta I` for every `m>=1`.
The Gram matrix of the `r!` permutation product vectors is a principal submatrix
of `G_m^(tensor r)`, so

\[
 r!\eta^r\le N_\sigma(m)\le(r!)^2,
 \quad p_{m,n}\ge f_*:=\frac{\eta^{r(b+1)}}{(r!)^{b+3}}.       \tag{15}
\]

The upper bound on `N` uses the triangle inequality for `r!` unit vectors.
Thus a fully specified expected-cost bound is

\[
 C_j\le\frac r{p_*}(2/f_*)^j.                                \tag{16}
\]

Cap execution at three times this *known upper bound* to ensure success at
least `2/3`; exact unknown Gram entries or permanent values are not needed to
run the algorithm. For odd `b` all packets stay alternating, allowing the
stronger `f_*=eta^(r(b+1))/(r!)^(b+1)` from `det G_m<=1`.

Each alternation can be implemented by a uniform permutation ancilla, controlled
register permutations, and the sign character. Preparing permutations by mixed-
radix choices and insertion gives a circuit polynomial in `r` and `log q`;
write its cost as `C_alt(r,q)`. The normalized projector is exactly (4), so no
normalized-wedge oracle or missing extra success factor is assumed. Finite gate
precision can be chosen against the known execution cap, charging its logarithm.

Depth-first recursion uses `O(r m_j log q+r log r)` qubits. If `A_j` is the
expected number of alternation attempts, then
`A_0=1/p_0`, `A_(j+1)=(2A_j+b)/p_(m_j,m_j)`, and
`A_j<=(b+1)C_j/r`. Total expected gate work is consequently bounded by
`O(C_j G_T + (b+1)C_j C_alt(r,q)/r + C_j k log q)`.
If a source-preparation circuit is supplied, its workspace is added to the live
qubit bound; the displayed bound describes externally supplied source copies.
Exact packet formulas and the three-times-cap guarantee use ideal operations.
For a finite universal gate set, reserve a margin, for example using a six-times
ideal cap and a separately budgeted total compilation error below 1/12; choose
per-gate precision against that known finite gate count. This retains bounded
success and controlled output error, without claiming exact finite-gate packets.

## 6. Exact orthogonal-family costs and scope of the improvement

For independent orthonormal components and `c_a=1/sqrt(r)`, all normalization
values in (3) equal `r!`, regardless of degree or sign. Therefore

\[
 p_0=r^{-r},\quad p_{m,n}=(r!)^{-(b+1)},\quad
 C_j=r^{r+1}[2(r!)^{b+1}]^j.                                 \tag{17}
\]

| Rank | Seed copies `C_0` | Inverse fusion success | Next packet copies `C_1` |
|---|---:|---:|---:|
| 4 | 1,024 | 13,824 | 28,311,552 |
| 5 | 15,625 | 207,360,000 | 6,480,000,000,000 |

The degree-growth exponent in (17) is `1+(b+1)log_2(r!)`, which grows as
`Theta(r(log r)^2)`. The older `r-1` hyperedge construction has orthogonal fusion
probability `(r!)^(-r)` and exponent `Theta(r^2 log r)`. Coding therefore gives
a substantial improvement *between these two quantum constructions*, including
`r log r` consumed slots instead of `r(r-1)`, while retaining severe rank costs.
It supplies neither a classical lower bound nor a free input-loading advantage.

## 7. Independent checks and remaining questions

A bounded inline NumPy calculation with one BLAS thread enumerated all
permutation pairs at ranks four and five. It checked survivor identities and
phases, both too-few-hyperedge mutations, and probabilities for all four input
sign pairs with random complex Gram matrices. The norm of each packet was
computed both by the permutation-vector Gram matrix and by determinant/permanent
formulas. Result: 212 checks passed, worst absolute residual `7.11e-14`.
This is exploratory evidence, not a registered red-capable checker artifact.

The root subsequently archived `checkers/explore/waring_coded_fusion.py`: 418
checks pass in 0.2 seconds under a 60-second bound with one BLAS thread. It
compares actual alternating projections (including an explicit rank-three seed),
permutation-pair enumeration, direct Gram sums, and closed normalization formulas.
All three recorded mutations exit 1. These checks do not establish originality
or a classical advantage.

The exact construction, phase, normalization, and model-specific hyperedge
optimality are ready for adversarial mathematical review. Its novelty relative
to existing multipartite fusion and separating-family protocols is separately
unverified. The rank-two case is already excluded by the Bell-fusion reduction
in `scouting/fresh-mechanism-round4.md`; that does not refute every higher rank.
The remaining algorithmic lemma is a same-input/same-output classical lower
bound or adjudicated best-known classical cost for a useful geometric task
obtained from these packets, with the costs (12)--(17) retained. Neither a new
source encoding nor the logarithmic hyperedge count alone settles D22.
