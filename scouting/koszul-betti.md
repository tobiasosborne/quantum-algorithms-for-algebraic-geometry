<!-- ROLE: arm B proposer lane (brief `briefs/lane-koszul-betti.md`): the supersymmetric
     Koszul Laplacian for graded Betti numbers. Scouting memo, not a claims file.
     Writable files of this lane: this file and checkers/explore/koszul_laplacian.py. -->

# Koszul / supersymmetric Laplacian for graded Betti numbers (arm B, round 1)

Conventions C1–C12 of `definitions/definitions.md` are in force; symbols are cited by `D-`
id and never redefined. One departure, the same one `checkers/README.md` records for the
whole suite: every `Delta_N` printed by the numerics is the Macaulay gap of the generating
tuple **as written** (unit coefficients on monomials), not of a unit Bombieri–Weyl
presentation (C5, OPEN-1). Nothing here depends on that: the Betti nullities are
presentation-independent (Step 12) and the Betti gap is quoted as `g/(N+i)`.

Bottom line. The identification works, exactly, with a clean normalisation and no compression
error — and it is **not** a speedup candidate. Three findings decide that, all new here and
each expanded below: (i) the naive compression `P_0 L P_0` is *identically the scalar* `N+i`
and carries no Betti information at all (Step 4.3, K-KB2), so arm B must use compressed
multiplications and is strictly more expensive than arm A; (ii) Betti information lives only
at `N <= reg(R/I)` (Step 6, K-KB1), so the large-`N` compression motivating the seed programme
is unavailable except where regularity grows with `n`; (iii) via Hochster's formula the problem
**is** quantum TDA (part d, K-KB3), so arm B inherits that ledger whole — #P-hardness,
QMA_1-hardness of the gapped decision version, and the Apers–Gribling–Sen–Szabó dequantization.
What survives is a theorem plus a hardness anchor, as the applications memo predicted for
shortlist entry 2, and one honest positive arm A lacks: the observable is a
presentation-independent invariant of the ideal.

---

## 1. Statement and sketch

Lamport-hierarchical; every leaf cites a `D-` id, a `C-` id, a named checker part, or a
cited theorem.

**ASSUME.** `R = C[z_0..z_n]` (D-polynomial-ring), `I = (f_1,...,f_d)` homogeneous with
`deg f_j = m_j`, `H = sum_j a^†(f_j) a(f_j)` (D-hamiltonian), `H_N = H|_{R_N}`, `P_{0,N}`
the projector onto `ker H_N` (D-projectors), Fock inner product throughout (C1).
**PROVE.** With `Q`, `L_W`, `g_{i,N}` of Steps 3 and 7,
`dim ker(L_W | block (i,N)) = beta_{i,i+N}(R/I) := dim Tor_i^R(R/I,C)_{i+N}`;
`||L_W|| <= N+i`; and `beta_{i,j} = 0` for `j-i > reg(R/I)`.

**Step 1 (the graded inverse system, and its annihilation-invariance).** 1.1
`ker H_N = (I_N)^perp` (C-008, D-ground-space), the degree-`N` part of the Macaulay inverse
system of `conj(I)` (C-012, D-inverse-system); by C-014 the map `[u] |-> P_0 u` is a linear
isomorphism `(R/I)_N -> (I_N)^perp`. Write `W := ⊕_N (I_N)^perp`. 1.2 For `u in (I_N)^perp`
and `h in I_{N-1}`, `<a_k u, h> = <u, a_k^† h> = <u, z_k h> = 0` since `z_k h in I_N`
(D-mode-operators); hence `a_k (I_N)^perp ⊆ (I_{N-1})^perp` for every `k, N` (the standard
closure of an inverse system under differentiation) and equivalently
`(1 - P_{0,N-1}) a_k P_{0,N} = 0`. This is what makes Step 2 need no compression.

**Step 2 (the supercharge).** 2.1 Adjoin `n+1` fermionic modes on `Lambda(C^{n+1})`,
`{c_k,c_l^†} = delta_{kl}`, `F̂ = sum_k c_k^† c_k`, basis `|S>` for `S ⊆ {0..n}` with
`c_k^†|S> = (-1)^{#{l in S : l<k}}|S ∪ {k}>` for `k not in S`, else `0`. 2.2
`Q := sum_k a_k ⊗ c_k^†` on `F ⊗ Lambda` satisfies `Q^2 = 0` **exactly** (the `a_k` commute,
the `c_k^†` anticommute) — no compression, no error term. 2.3 `Q` maps block `(i,N)`
(fermion number, boson degree) to `(i+1,N-1)`, so it preserves the **internal degree**
`j := N+i`: the natural block is `j`, not `N`. 2.4 By Step 1.2, `Q(W ⊗ Lambda) ⊆ W ⊗ Lambda`;
write `P̂ := P_0 ⊗ 1`, `Q_W := Q P̂ = P̂ Q P̂`. 2.5 The adjoint *on* `W ⊗ Lambda` is
`Q_W^† = sum_k Z_k ⊗ c_k` with `Z_k = P_{0,N} a_k^† P_{0,N-1}` the **compressed
multiplication** (D-compressed-multiplication) — not the restriction of `sum_k a_k^† ⊗ c_k`,
since `a_k^†` does not preserve `W`.

**Step 3 (the complex is the dual Koszul complex of `R/I`; Hodge).** 3.1
`K_.(z_0..z_n ; R/I)` has `(K_i)_j = (R/I)_{j-i} ⊗ Lambda^i`, `∂ = sum_k mu_{z_k} ⊗ iota_k`,
`H_i(K_.) = Tor_i^R(R/I,C)`, graded pieces `beta_{i,j}(R/I)` (Eisenbud, *The Geometry of
Syzygies*, GTM 229, DOI 10.1007/b137572). 3.2 Under `W_N ≅ (R/I)_N^*` (pairing
`<u,[h]> := <u,h>`, well defined since `u ⊥ I_N`), Step 1.2 says `a_k` is the transpose of
`mu_{z_k}` and `c_k^†` the transpose of `iota_k`, so `Q = ∂^T` and `(W ⊗ Lambda, Q)` is the
`C`-dual of `K_.(z; R/I)`, block `(i,N)` dual to `(K_i)_j` at `j = N+i`. 3.3 For a complex of
finite-dimensional Hilbert spaces `ker L` is the harmonic space, of the dimension of the
homology; and homology of the dual is the dual of the homology. Hence

> **KB1.** `dim ker(L_W | (i,N)) = beta_{i,i+N}(R/I)` for all `i in 0..n+1`, `N >= 0`.

Part A: exact agreement on every block of five ideals, against `beta` recomputed over GF(p)
from exact ranks of Koszul differentials of `R/I` in a standard-monomial basis.

**Step 4 (the full Laplacian is the free number operator).** 4.1 With
`a_k a_l^† = a_l^† a_k + delta_{kl}` and `c_l c_k^† = delta_{kl} - c_k^† c_l`, on all of
`F ⊗ Lambda`: `Q Q^† + Q^† Q = sum_k a_k^† a_k ⊗ 1 + 1 ⊗ sum_k c_k^† c_k = N̂ + F̂`, the
scalar `N+i = j` on block `(i,N)` (part B: max deviation `< 1e-9`, all five families).
4.2 *Exactness*: `ker L = 0` except at the vacuum — nothing to compute before restriction.
4.3 ***The naive compression is information-free***: since `L` is a scalar,
`P̂ L P̂ = (N+i) P̂` exactly, nullity `0` on `range(P̂)` for `j > 0`. The operator to
block-encode is **not** `P_0 L P_0` but `L_W`, built from the `Z_k`. Part B prints the
nonzero eigenvalues of `P̂ L P̂`, all exactly `3`, in a block where `beta_{1,3} = 1` for the
monomial ideal. 4.4 *Normalisation*: with `X := P̂ Q (1-P̂)`, expanding
`P̂ Q Q^† P̂ = P̂ Q P̂ Q^† P̂ + X X^†` and using `(1-P̂) Q P̂ = 0` gives
`L_W = (N+i)·1 - X X^†`, `X X^† >= 0`, hence `0 <= L_W <= (N+i)1` and `||L_W|| <= j`: no
`alpha_BE` blow-up of the D-block-encoding-normalisation kind for `L_W` itself. 4.5 *The
`i=0` row is trivial*: `L_W|(0,N) = P_0 N̂ P_0 = N·1`; part C's `g(i=0)` column is exactly
`N` in every family.

**Step 5 (the Betti gap).** 5.1 `g_{i,N} := lambda_min^{≠0}(L_W|(i,N))`, normalised
`g_{i,N}/(N+i)` — only the normalised quantity may enter a promise (D-normalised-gap). 5.2
By 4.4, `g_{i,N} = j - lambda_max^{<j}(X X^†)`: a spectral gap at the *top* of `X X^†`. 5.3
Supersymmetry makes the nonzero spectra of `(i,N)` and `(i+1,N-1)` coincide, so the invariant
object is the Laplacian of the whole internal-degree-`j` complex (part C). 5.4 `g` is a
**new parameter**, not `Delta_N` (D-macaulay-gap), and no analogue of Fact 7.1 (C-107) is
known for it.

**Step 6 (support: Betti information lives at `N <= reg`).** `reg(R/I) =
max{j-i : beta_{i,j} != 0}` (D-saturation-regularity-stable-range) and `beta_{i,j} = 0` for
`i > n+1` (Hilbert syzygy); since the block label is `N = j-i`:

> **KB2.** `dim ker(L_W|(i,N)) = 0` for every `i` whenever `N > reg(R/I)`.

Part A checks this as a prediction out to `N = 8,7,7,6,5` against `reg = 1,2,2,1,1`. This
inverts the seed's geometry: arm A wants the *stable* range `N >= reg` (C-011); arm B has all
its content at `N <= reg`.

**Step 7 (relation to `Syz(I)_N` and the §5 rows).** 7.1 `Syz(I)_N = ker Phi_N`
(D-syzygy-module, C-052) is the non-minimal degree-`N` piece of the *tuple's* syzygies, of
dimension `sum_j dim R_{N-m_j} - dim I_N`, fixed by the Hilbert function; it is not a Betti
number. 7.2 `beta_{1,j}(R/I)` counts minimal generators of `I` in degree `j` and
`beta_{2,j} = dim(Syz / m Syz)_j` counts minimal first syzygies: arm B performs exactly the
minimalisation `Phi_N` does not. 7.3 *Caution*: the first nonzero row is free. For `I` with no
linear forms, `L_W|(1,1) = 2 - X X^†` with `X f = sum_k (∂_k f) ⊗ e_k` the gradient on `I_2`,
and `sum_k ||∂_k f||^2 = <f, N̂ f> = 2||f||^2`, so `X^†X = 2` on `I_2` and
`beta_{1,2} = dim I_2` — a rank, readable from the input (confirmed in every family:
3, 2, 5, 14). The first genuinely non-input block is `i = 2`.

**Step 8 (the other supercharge: the seed's `H` is a Koszul block).** With `d` fermionic modes
and `Q_f := sum_j a^†(f_j) ⊗ gamma_j`, `Q_f^2 = 0` and the `i=0` block of
`Q_f Q_f^† + Q_f^† Q_f` is `sum_j a^†(f_j) a(f_j) = H`: the seed Hamiltonian is the bottom
block of a supersymmetric Koszul Laplacian on the *generators*, and this one needs no
projector — a genuine `max_j m_j`-body boson–fermion Hamiltonian (D-k-body, D-few-mode). Its
higher blocks compute `H_i(f;R) = Tor_i^S(C,R)`, `S = C[y_1..y_d]`, `y_j |-> f_j`, which
vanish for `i>0` exactly when `f` is a regular sequence; these are **not** `beta_{i,j}(R/I)`.
Untested here (mutation M4).

**Step 9 (what a quantum algorithm block-encodes; and one honest positive).** 9.1 Sparse
access to `H_N` gives `P_0` by QSVT at `O((alpha_BE/Delta_N) log(1/eps))` block-encoding uses
(C-056, D-qsvt); `Q_W` costs `n+1` row-computable `a_k` (C-054) times one `P_0`, and `Q_W^†`
costs `n+1` `a_k^†` sandwiched by two `P_0`s, so one use of `L_W` is
`O(n · alpha_BE/Delta_N)` uses of the `H_N` block encoding with `||L_W|| <= j`. A DQC1-style
estimate (D-dqc1-style-estimate) of `Tr(Pi_{ker L_W})/dim` then costs
`Õ(n (alpha_BE/Delta_N)(j/g_{i,N}) eps^{-2})` and returns the **normalised Betti fraction**
`beta_{i,j}/(HF(j-i) C(n+1,i))`, never `beta`. 9.2 `beta_{i,j}(R/I)` is an invariant of `I`,
so `dim ker L_W` does not move when the generating tuple changes — the
presentation-independence `Delta_N` lacks (D-macaulay-gap pitfall (i), C-106). Arm B's
*output* is better posed than arm A's; only the cost parameters are presentation-dependent.

---

## 2. Numerics

Regenerate with (7.2 s wall on this machine, exit 0):

```bash
cd /home/tobias/Projects/quantum-algorithms-for-algebraic-geometry/checkers
timeout 900 python3 explore/koszul_laplacian.py
```

`checkers/explore/koszul_laplacian.py` is an **exploration** script, excluded from
`run_all.sh`, but red-capable (L4): every block prints OK/MISMATCH, exit 1 on any mismatch,
exit 2 on an unexpected exception, and four red mutations are listed in its docstring
(M1 drop the compression, M2 index slip `beta_{i,N}` for `beta_{i,i+N}`, M3 drop the
fermionic sign, M4 Koszul on the generators). The reference `beta` is recomputed over
GF(p), `p = 10^9+7`, by exact ranks of Koszul differentials of `R/I` in a standard-monomial
basis from the reduced row echelon form of the Macaulay matrix (D-macaulay-matrix) —
nothing on that side touches `H_N`, the Fock basis, or a floating-point number.

**(a) nullity per block vs the independent Betti table — every block OK.** Betti-carrying
blocks and neighbours; `reg` is read off the table and the vanishing prediction of KB2 is
then checked to the stated `N`.

```
                        i  N  j  dimblk nullity beta      g_{i,N}  g/(N+i)  beta/dim
twisted cubic P^3       0  0  0       1       1    1  OK      nan      nan  1.000e+00
  reg=1, checked N<=8   1  1  2      16       3    3  OK   2.0000   1.0000  1.875e-01
                        2  1  3      24       2    2  OK   1.3333   0.4444  8.333e-02
                        3  1  4      16       0    0  OK   1.0677   0.2669  0.000e+00
2 int quadrics P^3      1  1  2      16       2    2  OK   2.0000   1.0000  1.250e-01
  reg=2, checked N<=7   2  2  4      48       1    1  OK   1.6093   0.4023  2.083e-02
(z0^2,z0z1,z1^3) P^2    1  1  2       9       2    2  OK   2.0000   1.0000  2.222e-01
  reg=2, checked N<=7   2  1  3       9       1    1  OK   1.0000   0.3333  1.111e-01
  (two-row table)       1  2  3      12       1    1  OK   1.0000   0.3333  8.333e-02
                        2  2  4      12       1    1  OK   1.0000   0.2500  8.333e-02
rat normal quartic P^4  1  1  2      25       6    6  OK   2.0000   1.0000  2.400e-01
  reg=1, checked N<=5   2  1  3      50       8    8  OK   1.3333   0.4444  1.600e-01
  (Eagon-Northcott)     3  1  4      50       3    3  OK   1.0538   0.2634  6.000e-02
```

Also `(z0^2, z0z1, z1^2)` in `P^2` (`3, 2`): all blocks OK, `reg = 1`, checked to `N = 6`.
Five ideals, every block of every family, no mismatch, and every "nullity `= 0` beyond
`reg`" prediction confirmed.

**(b) the uncompressed Laplacian, and the normalisation.**

```
max deviation of Q Q^dag + Q^dag Q from (N+i)*1 over all blocks N <= 4:  < 1e-9  OK
P_0 L P_0 at (i=1,N=2): all nonzero eigenvalues equal 3.000000, nullity on
  range(P_0 (x) 1) is 0, while beta_{1,3} = 1 for the monomial ideal.
smallest eigenvalue of (N+i) - L_W = -0.0000   (X X^dag is PSD, as required)
```

**(c) Betti gap vs Macaulay gap.** Twisted cubic (left) and monomial `(z0^2,z0z1,z1^3)`
(right); and the `n`-dependence on Stanley–Reisner ideals of the `m`-cycle at the top block
`(i=m-2, N=2)`, where `beta = 1` is the `H_1` of the cycle:

```
 N   Delta_N   g(i=0)  g(i=1)  g(i=2) |  Delta_N  g(i=0) g(i=1) g(i=2)      m:    4      5      6      7
 2    2.0000   2.0000  1.3333  1.0677 |   1.0000  2.0000 1.0000 1.0000      g: 2.000  1.382  1.000  0.753
 4    3.5505   4.0000  3.6000  3.3663 |   1.0000  4.0000 2.0000 2.0000   g/(N+i)0.500  0.276  0.167  0.108
 8    6.8377   8.0000  7.7778  7.6672 |   1.0000  8.0000 5.0000 5.0000
```

Readings: (i) `g(i=0,N) = N` exactly (Step 4.5); (ii) `g` grows roughly linearly in `N`,
normalised `g/(N+i)` settling in `[0.15, 1.0]` here, while `Delta_N` moves independently —
`Delta_N = 1` for all `N` for the monomial ideal, and `Delta_N in [31,56]` against
`g in [0.45,7.2]` for the two random integer quadrics (Step 5.4); (iii) the SUSY pairing of
7.3 is visible on every diagonal (`g(1,1) = g(0,2)`, `g(2,1) = g(1,2)`); (iv) the `m`-cycle
normalised gap decays between `m^{-2}` and `m^{-3}` — inverse-polynomial on this family,
with no proof and no general lower bound.

**(d) Hochster: the blocks are simplicial Laplacians of induced subcomplexes.** For a
Stanley–Reisner ideal, `beta_{i,j} = sum_{|sigma|=j} dim H~_{j-i-1}(Delta|_sigma)`
(Hochster 1977, *Ring Theory II*, Proc. 2nd Oklahoma Conf. 1975, 171–223, Dekker LNPAM 26 —
no DOI exists for that article; the standard modern statement is Miller–Sturmfels,
*Combinatorial Commutative Algebra*, GTM 227, Cor. 5.12, DOI 10.1007/b138602). The script
recomputes the right-hand side from scratch (simplicial boundary ranks over GF(p)):

```
  i  N  j  dimblk nullity GF(p) beta  Hochster        g_{i,N}  g/(N+i)  beta/dim
5-cycle, I_Delta = 5 quadrics in P^4, HF(N) = [1, 5, 10, 15]
  1  1  2      25       5          5         5   OK    2.0000   1.0000  2.000e-01
  2  1  3      50       5          5         5   OK    1.0000   0.3333  1.000e-01
  3  2  5     100       1          1         1   OK    1.3820   0.2764  1.000e-02
7-cycle, I_Delta = 14 quadrics in P^6, HF(N) = [1, 7, 14, 21]
  1  1  2      49      14         14        14   OK    2.0000   1.0000  2.857e-01
  2  1  3     147      35         35        35   OK    1.0000   0.3333  2.381e-01
  3  1  4     245      35         35        35   OK    0.5858   0.1464  1.429e-01
  4  1  5     245      14         14        14   OK    0.3820   0.0764  5.714e-02
  5  2  7     294       1          1         1   OK    0.7530   0.1076  3.401e-03
```

(4-cycle and 6-cycle likewise, all OK.) This is the bridge used in §3.4: restricted to
monomial ideals the arm-B observable **is** the normalised Betti number of a simplicial
complex.

**(e) normalised Betti fraction.** Complete intersection of `c` quadrics in `P^n`,
`beta_{i,2i} = C(c,i)`, block `(i, N=i)`, fraction `= C(c,i)/(HF(i) C(n+1,i))`:

```
   n   c         i=1         i=2         i=3         i=4         i=5
   3   2   1.250e-01   2.083e-02           -           -           -
  10   5   4.132e-02   2.981e-03   2.624e-04   2.225e-05   1.286e-06
  20   5   1.134e-02   2.107e-04   4.513e-06   8.812e-08   1.105e-09
  40  10   5.949e-03   6.449e-05   9.435e-07   1.630e-08   3.056e-10
  40  20   1.190e-02   2.755e-04   9.282e-06   4.030e-07   2.105e-08
```

The fraction is `~ C(c,i)(i!)^2 n^{-2i}`: **inverse-polynomial in `n` at fixed homological
degree `i`**, exponentially small only as `i` grows. Contrast the normalised Hilbert
function, `rho^{codim}` with `rho ~ 0.75` (applications memo F2, caution 1), exponentially
small for every square system. Arm B's observable survives F2 where arm A's does not — at
the price of an `n^{-2i}` precision target, i.e. `n^{4i}` samples at fixed `i`.

---

## 3. Against the north star (PRD §2, criteria 1–5)

**1. Problem.** `NORM-BETTI(i)`: input, homogeneous `f_1..f_d` in `n+1` variables with
`poly(n)` monomials and `poly(n)`-bit coefficients, `i` and `j` in unary with `j <= reg`
(D-input-model); promises `Delta_N/alpha_BE >= 1/poly(n)` at `N = j-i` and
`g_{i,N}/(N+i) >= 1/poly(n)`; output, an additive-`eps` estimate of
`beta_{i,j}(R/I)/(HF(j-i) C(n+1,i))`. Decision version `GAPPED-BETTI(i)`: decide
`beta_{i,j} = 0` versus `>= 1` under the same promises. The input model is the seed's,
unchanged; `reg` must be supplied (K-KB10). The output is a presentation-independent
invariant (Step 9.2) — better posed than any `Delta_N`-style target in arm A.

**2. Classical baseline.** Not Macaulay2 — that is the classical memo's trap "comparing
against the wrong classical algorithm". Structural baselines: minimal free resolutions by
Schreyer frames and Hilbert-function pruning (La Scala–Stillman, *J. Symbolic Comput.*
26(4) 409–431 (1998), DOI 10.1006/jsco.1998.0221; practical `n = 10..40`, `10^3..10^6`
syzygies) and finite-dimensional syzygies by fast linear algebra (Neiger–Schost,
*J. Complexity* 60, 101502 (2020), DOI 10.1016/j.jco.2020.101502, arXiv:1912.01848 — two
authors, not "et al.", correcting classical memo [R31]; `O(m D^{omega-1} + n D^omega log D)`).
The baseline that actually competes is **stochastic Chebyshev/Lanczos eigenvalue counting**
on the same sparse Koszul matrices: Di Napoli–Polizzi–Saad, *Numer. Linear Algebra Appl.*
23(4) 674–692 (2016), DOI 10.1002/nla.2048, arXiv:1308.4275 — polynomial filtering plus
Hutchinson traces counts eigenvalues in an interval, i.e. exactly the normalised nullity of
`L_W`, and it needs the same `P_0`, obtainable classically by a Chebyshev filter on the same
sparse `H_N`. So both sides pay the `Delta_N` promise, one inside a QSVT and one inside a
Krylov iteration on length-`C(N+n,n)` vectors; the residual comparison is `n log N` qubits
versus `M_N` words, which PRD D15 / fact SP-0 (C-264) refuses as a space separation.

**3. Quantum algorithm.** Step 9.1: `Õ(n (alpha_BE/Delta_N)(j/g_{i,N}) eps^{-2})` uses of the
sparse `H_N` block encoding (`eps^{-1}` with amplitude estimation on a pure-state version);
`O(n log N)` bosonic qubits plus `n+1` fermionic. Proven margin over the baseline: none. The
only structural advantage is `||L_W|| <= j` (Step 4.4) — the Koszul layer is cheap, all cost
is in `P_0`, i.e. in arm A's promises. **Arm B cannot beat arm A; it strictly contains it.**

**4. Dequantization audit.** This decides the arm.
(a) Via Hochster (part d) the monomial case is exactly normalised Betti number estimation for
a simplicial complex, and Apers–Gribling–Sen–Szabó, *Quantum* 7, 1202 (2023),
DOI 10.22331/q-2023-12-06-1202, arXiv:2211.09618, estimate the `k`-th **normalised** Betti
number to additive `eps` classically by path-integral Monte Carlo in
`n^{O(gamma^{-1/2} log(1/eps))}`, `gamma` the combinatorial-Laplacian gap (improving to
`(n/lambda_max)^{O(...)}` on clique complexes, matching the quantum runtime when
`gamma = Omega(1)` and `k = Omega(n)`). Our `gamma` is `g/(N+i)`. Plainly: **at a constant
normalised Betti gap the estimator is dequantized to quasi-polynomial time; the only surviving
window is `g/(N+i) = 1/poly(n)` with `eps = 1/poly(n)`, where the classical bound degrades to
`n^{O(poly(n))}` and the quantum stays polynomial** — exactly the window in which no lower
bound on `g` is known (K-KB6).
(b) Berry et al., *PRX Quantum* 5, 010319 (2024), DOI 10.1103/PRXQuantum.5.010319,
arXiv:2209.13581: exponentially large chain dimension **and** exponentially large Betti number
are necessary, neither sufficient; super-quadratic advantage only for multiplicative error with
growing Betti number. Our chain dimension `HF(N) C(n+1,i)` and `beta` can both be exponential
(families with `reg = Theta(n)`, e.g. D-boolean-ideal), and part (e) gives a `1/poly` fraction
at fixed `i` — the necessary conditions are reachable, but multiplicative error is blocked by (c).
(c) Schmidhuber–Lloyd, *PRX Quantum* 4, 040349 (2023), DOI 10.1103/PRXQuantum.4.040349,
arXiv:2209.14286: exact Betti numbers #P-hard, multiplicative approximation NP-hard, in the
regime where quantum TDA performs best. Through Hochster this transfers verbatim to
`beta_{i,j}` of Stanley–Reisner ideals, agreeing with classical memo §10 and
D-hardness-anchors. Only the normalised additive problem survives, as C-093 says for `HF`.
(d) The best product of this lane: King–Kohler, *Gapped Clique Homology on weighted graphs is
QMA_1-hard and contained in QMA*, arXiv:2311.17234, FOCS 2024, 493–504,
DOI 10.1109/FOCS61266.2024.00039 (also SIAM J. Comput. FOCS24 section,
DOI 10.1137/24M1710243); Crichigno–Kohler, *Clique Homology is QMA_1-hard*, arXiv:2209.11793,
*Nature Communications* 15, 9846 (2024), DOI 10.1038/s41467-024-54118-z; Hayakawa,
arXiv:2608.02726 (2026, arXiv only), unweighted gapped clique homology is QMA_1-complete.
Their instances are clique complexes, i.e. Stanley–Reisner complexes of edge ideals, so
`GAPPED-BETTI` **inherits QMA_1-hardness** — a stronger hardness anchor for an
algebraic-geometry problem than the seed's only candidate (C-124, conjectural), and
simultaneously a negative for the speedup.
(e) Novelty caution. Cade–Crichigno, arXiv:2107.00011, *Quantum* 8, 1325 (2024),
DOI 10.22331/q-2024-04-30-1325, already formalise "N=2 SUSY local Hamiltonian, ground energy
zero iff a cohomology group is nontrivial" and prove QMA-completeness; Crichigno,
arXiv:2011.01239 (arXiv only), shows the Witten index is #P-complete. The
SUSY-computes-homology mechanism is **not new**; the algebro-geometric instance is.
*Correction to carry*: Gyurik–Cade–Dunjko, *Quantum* 6, 855 (2022),
DOI 10.22331/q-2022-11-10-855, arXiv:2005.02607, prove DQC1-hardness of **low-lying spectral
density estimation**, *not* of normalised Betti number estimation, and leave the restriction to
clique-complex Laplacians explicitly open; any row citing them for "normalised BNE is
DQC1-hard" is mis-citing.
(f) Trap audit (classical memo): dense rank — avoided; changing the output — a normalised
fraction, said so; hidden state preparation — the maximally mixed block state needs `P_0`,
priced; exponentially small overlap — **not triggered**, part (e) gives `1/poly` at fixed `i`,
the first time in the campaign; hiding exponential `N` — inapplicable (KB2); ignoring gap
closing — triggered (K-KB6); ignoring classical preconditioning — triggered (K-KB9).

**5. Heuristic attack.** Weak, and that is itself a finding: by Step 4.1 the *whole* Koszul
Laplacian is the free Hamiltonian `N̂ + F̂`, a Bose–Fermi Hubbard model with no interaction, and
all content sits in `P_0`, a QSVT projector rather than an interaction term. There is no natural
condensed-matter Hamiltonian whose ground degeneracy is a Betti table, in contrast to C-024 (the
conic as the Law–Pu–Bigelow spin-mixing Hamiltonian). Two survivors. (i) *Monomial ideals*:
`H_N` is diagonal (C-111), `P_0` is a computational-basis projector, and `L_W` is an honest
sparse number-conserving hopping Hamiltonian on the standard monomials tensored with a
Jordan–Wigner fermion register on `n+1` sites. Smallest demonstration: the Stanley–Reisner ideal
of the 4-cycle, `I = (z_0z_2, z_1z_3)`, block `(i=1,N=1)` — **one boson in 4 modes (dual rail)
plus one fermion in 4 modes**, a 16-level two-particle problem whose zero-energy degeneracy is
`beta_{1,2} = 2`; the 7-cycle at `(i=3,N=1)` is 245-dimensional with degeneracy 35 and
normalised gap 0.146, still tabletop. A demonstration, not a computation (K-KB7).
(ii) *The other supercharge* (Step 8): `Q_f = sum_j a^†(f_j) ⊗ gamma_j`, a genuine
`max_j m_j`-body boson–fermion interaction with no projector whose `i=0` block is the seed
Hamiltonian (for quadrics, spin-mixing plus a fermion). It is the only natively physical object
this lane found, and it computes Koszul homology of the sequence, not the Betti table.

---

## 4. Killers

**K-KB1 (support collapse; F3).** `beta_{i,j} = 0` for `j-i > reg(R/I)` (Step 6, part a), so
`N <= reg` and the seed's exponential-compression argument applies only where regularity grows
with `n`; the twisted cubic, the rational normal curves and every determinantal example in the
seed's survey have `reg(R/I) <= 2`. Surviving: arm B needs `reg = Theta(n)`, and
D-boolean-ideal / D-clause-ideal are the campaign's only such families — exactly the #P-hard
ones. Severity high.

**K-KB2 (the naive compression is information-free).** `P_0 L P_0 = (N+i) P_0` exactly
(Step 4.3, part b): "block-encode the projected Koszul Laplacian" returns a scalar. The
algorithm must use `Q_W^† = sum_k Z_k ⊗ c_k`, so each application of `L_W` costs a full QSVT
projector at `alpha_BE/Delta_N`. Surviving: arm B ⊇ arm A in cost, never the cheaper arm.
Severity decisive for cost accounting.

**K-KB3 (the problem is quantum TDA).** Hochster plus part d: the multigraded blocks of `L_W`
for a Stanley–Reisner ideal are simplicial Laplacians of induced subcomplexes. Hence exact
evaluation #P-hard and multiplicative approximation NP-hard (arXiv:2209.14286), gapped decision
QMA_1-hard (arXiv:2311.17234, arXiv:2209.11793), normalised additive dequantized in
`n^{O(gamma^{-1/2} log(1/eps))}` (arXiv:2211.09618). Surviving: arm B is a new *instance* of a
settled debate, not a new debate. Severity decisive for the speedup, valuable as an anchor.

**K-KB4 (novelty of the mechanism).** SUSY Laplacian ↔ homology is standard (Witten) and
Cade–Crichigno arXiv:2107.00011 prove the Hamiltonian-complexity version; only the
algebro-geometric instance is new. Action: a C-110-style scout on whether "graded Betti numbers
= nullity of a Laplacian built from compressed multiplications on the Macaulay inverse system"
already exists (operator theory, C-015/C-017, or physics). Severity medium.

**K-KB5 (the cheap blocks are input data).** `beta_{1,j}` counts minimal generators and
`beta_{1,2} = dim I_2` is a rank (Step 7.3, every family). The first genuinely non-input block
is `i = 2`, where the normalised fraction is already `~ n^{-4}` (part e): precision target
`eps = n^{-4}`, sample count `n^8`. Severity medium.

**K-KB6 (the Betti gap has no lower bound).** `g_{i,N}` is a new parameter, numerically
unrelated to `Delta_N` in either direction (part c); no analogue of Fact 7.1 (C-107) or 7.2
(C-108/C-109) is known; on the `m`-cycle family the normalised gap decays between `m^{-2}` and
`m^{-3}`. Runtime is `1/g` and §3.4(a)'s dequantization window is exactly `1/poly`, so the arm
lives or dies here. Surviving: arm B's first analytic task is a Bombieri-type lower bound for
`g`, not for `Delta`. Severity high.

**K-KB7 (no hardware hook for `L_W`).** The full Koszul Laplacian is the *free* Hamiltonian
`N̂ + F̂` (Step 4.1); the content is entirely in a projector, which is not an interaction.
Surviving: the monomial-ideal demonstration of §3.5(i) and the generator-Koszul Hamiltonian of
Step 8. Severity high against PRD criterion 5.

**K-KB8 (output).** Only the normalised fraction is estimable; recovering `beta` needs
`eps < 1/(2 dim)`, which #P-hardness forbids anyway. The table has `O(n · reg)` blocks so the
*normalised* table is cheap once one entry is — but that is not a Betti table. Severity medium;
same kind as C-091/C-093.

**K-KB9 (classical preconditioning symmetry).** Any filter making `P_0` cheap quantumly makes it
cheap classically on the same sparse `H_N`; the residual comparison, `n log N` qubits versus
`M_N` words, is refused as a space separation by PRD D15 / SP-0 (C-264). The arm should make no
space claim. Severity high for any space claim.

**K-KB10 (regularity is part of the promise).** `reg(I)` is worst-case doubly exponential
(Mayr–Meyer; Bayer–Mumford) and the algorithm needs `j <= reg` to know where to look — the same
defect as C-011's stable range; it must be stated in the input model, not assumed. Severity
medium.

Ranking by how much each must be answered before arm B is worth a prover seat:
**K-KB6 > K-KB3 > K-KB2 > K-KB1 > K-KB7 > K-KB4 > K-KB9 > K-KB5 > K-KB10 > K-KB8.**

---

## 5. Proposed definitions

Register format; ids proposed, orchestrator merges.

- **D-fermionic-modes.** `c_k, c_k^†` (`k = 0..n`) on `Lambda(C^{n+1})` with
  `{c_k, c_l^†} = delta_{kl}`; basis `|S>`, `S ⊆ {0..n}`;
  `c_k^†|S> = (-1)^{#{l in S : l<k}}|S ∪ {k}>` for `k not in S`, else 0; fermion number
  `F̂ = sum_k c_k^† c_k`. Pitfall: the sign is not decorative — dropping it breaks `Q^2 = 0`
  (mutation M3).
- **D-koszul-supercharge.** `Q = sum_k a_k ⊗ c_k^†` on `F ⊗ Lambda(C^{n+1})`
  (D-mode-operators, D-fermionic-modes); `Q^2 = 0` exactly; carries block `(i,N)` to
  `(i+1,N-1)` and preserves `j = N+i`. Restriction `Q_W = Q(P_0 ⊗ 1)` is well defined
  because `(I_N)^perp` is `a_k`-invariant (D-inverse-system). Pitfall: `Q^†` does **not**
  restrict; its restriction is `sum_k Z_k ⊗ c_k`, D-compressed-multiplication.
- **D-betti-laplacian.** `L_W = Q_W Q_W^† + Q_W^† Q_W` on `(I_N)^perp ⊗ Lambda^i`; equals
  `(N+i)1 - X X^†` with `X = (P_0⊗1) Q (1 - P_0⊗1)`; `0 <= L_W <= (N+i)1`. Pitfall:
  `L_W != (P_0⊗1) L (P_0⊗1)`, which is the scalar `(N+i)`.
- **D-graded-betti-number.** `beta_{i,j}(R/I) = dim Tor_i^R(R/I, C)_j`; `beta_{i,j} = 0`
  for `i > n+1` or `j - i > reg(R/I)`; `beta_{1,j}` = minimal generators of `I` in degree
  `j`; `beta_{2,j}` = minimal first syzygies (relation to D-syzygy-module: `Syz(I)_N` is the
  non-minimal degree-`N` piece of the tuple's syzygies, not a Betti number).
- **D-betti-gap.** `g_{i,N} = lambda_min^{≠0}(L_W|(i,N))`, normalised `g_{i,N}/(N+i)`;
  `= (N+i) - lambda_max^{<N+i}(X X^†)`. Pitfall: not `Delta_N` (D-macaulay-gap) and not
  bounded by it in either direction; presentation-dependent although the nullity is not.
- **D-normalised-betti-fraction.** `beta_{i,j} / (HF_{R/I}(j-i) · C(n+1, i))`, the DQC1-style
  observable (D-dqc1-style-estimate). Pitfall: `~ C(c,i)(i!)^2 n^{-2i}` for a complete
  intersection of `c` quadrics — inverse-polynomial at fixed `i`, exponentially small in `i`.
- **D-generator-koszul-supercharge.** `Q_f = sum_j a^†(f_j) ⊗ gamma_j` on
  `F ⊗ Lambda(C^d)`; its `i=0` Laplacian block is D-hamiltonian; higher blocks compute
  `H_i(f;R) = Tor_i^{C[y_1..y_d]}(C, R)`. Pitfall: these are *not* `beta_{i,j}(R/I)`.
- **D-betti-estimation-problem.** `NORM-BETTI(i)` and `GAPPED-BETTI(i)` as stated in §3.1,
  with the two promises (`Delta_N/alpha_BE` and `g_{i,N}/(N+i)`) and `reg` in the input.

---

## 6. Proposed claim rows

Ids `C-NEW-KB-*`, all **CONJECTURE** per L1 (a §1 Lamport sketch and an independent GF(p)
recomputation exist for KB-HODGE, KB-FREE and KB-SUPPORT; the orchestrator decides whether
that warrants SKETCH at merge). `where-tested` is
`checkers/explore/koszul_laplacian.py` throughout.

**C-NEW-KB-HODGE.** For every homogeneous ideal `I ⊆ C[z_0..z_n]`, every `i in 0..n+1` and
every `N >= 0`, the Laplacian `L_W = Q_W Q_W^† + Q_W^† Q_W` of the supercharge
`Q_W = (sum_k a_k ⊗ c_k^†)(P_0 ⊗ 1)` on `(I_N)^perp ⊗ Lambda^i` satisfies
`dim ker L_W|(i,N) = beta_{i, i+N}(R/I)`. — depends-on: D-koszul-supercharge,
D-betti-laplacian, D-graded-betti-number, D-inverse-system, D-compressed-multiplication,
C-008, C-012, C-014; where-proved: §1 Steps 1-3; where-tested: part A, five ideals, every
block, exact agreement against GF(p) Koszul ranks. Relevance/traps: the whole arm; guards
against the index slip `beta_{i,N}` (mutation M2) and against forgetting that the ground
space is the *dual* of `R/I`.

**C-NEW-KB-FREE.** For every `n`, `Q Q^† + Q^† Q = N̂ + F̂` identically on
`F ⊗ Lambda(C^{n+1})`; consequently `(P_0 ⊗ 1) L (P_0 ⊗ 1) = (N+i)(P_0 ⊗ 1)` has zero
nullity for `N+i > 0`, and `L_W = (N+i)1 - X X^†` with `X = (P_0⊗1)Q(1-P_0⊗1)`, so
`||L_W|| <= N+i`. — depends-on: D-koszul-supercharge, D-betti-laplacian, D-projectors,
D-block-encoding-normalisation; where-proved: §1 Step 4; where-tested: part B, max
deviation `< 1e-9`, and the printed spectrum of `P_0 L P_0`. Relevance/traps: fixes what a
quantum algorithm must block-encode (K-KB2); guards against pricing arm B below arm A.

**C-NEW-KB-SUPPORT.** For every homogeneous `I` and every `i`, `beta_{i,j}(R/I) = 0` for
`j - i > reg(R/I)`; hence the Betti Laplacian has trivial kernel in every block with
`N > reg`, and the arm has no large-`N` regime. — depends-on: C-NEW-KB-HODGE,
D-saturation-regularity-stable-range; where-proved: §1 Step 6 (Castelnuovo–Mumford);
where-tested: part A, prediction checked to `N = 8, 7, 7, 6, 5` against `reg = 1,2,2,1,1`.
Relevance/traps: K-KB1, F3; guards against hiding exponential `N`.

**C-NEW-KB-HOCHSTER.** For every simplicial complex `Delta` on `{0..n}` with
Stanley–Reisner ideal `I_Delta`, the multigraded blocks of `L_W` are the reduced simplicial
Laplacians of the induced subcomplexes `Delta|_sigma`, and
`dim ker L_W|(i,N) = sum_{|sigma| = i+N} dim H~_{N-1}(Delta|_sigma)`. Consequently
`NORM-BETTI` and `GAPPED-BETTI` for monomial ideals are, respectively, normalised Betti
number estimation and gapped clique/independence homology. — depends-on: C-NEW-KB-HODGE,
D-monomial-ideal, D-graded-betti-number; where-proved: Hochster 1977 / Miller–Sturmfels
GTM 227 Cor. 5.12 (DOI 10.1007/b138602) composed with Step 3.3; where-tested: part D,
`m`-cycles `m = 4..7`, nullity = GF(p) `beta` = Hochster sum on every Betti-carrying block.
Relevance/traps: the reduction that imports the entire quantum-TDA ledger (K-KB3).

**C-NEW-KB-QMA1.** `GAPPED-BETTI` is QMA_1-hard, by C-NEW-KB-HOCHSTER composed with the
QMA_1-hardness of gapped clique homology (King–Kohler arXiv:2311.17234,
DOI 10.1109/FOCS61266.2024.00039; Crichigno–Kohler arXiv:2209.11793,
DOI 10.1038/s41467-024-54118-z), and exact evaluation of `beta_{i,j}` is #P-hard with
multiplicative approximation NP-hard (Schmidhuber–Lloyd arXiv:2209.14286,
DOI 10.1103/PRXQuantum.4.040349). — depends-on: C-NEW-KB-HOCHSTER, D-hardness-anchors,
C-091, C-092; where-proved: cited literature plus the reduction; where-tested: none (the
reduction's degree bookkeeping is not checked numerically). Relevance/traps: the strongest
hardness anchor in the campaign for an algebraic-geometry problem, and simultaneously a
refutation of any efficient-algorithm claim for the decision version.

**C-NEW-KB-DEQUANT.** Under sparse access to `L_W` and a promise
`g_{i,N}/(N+i) >= gamma`, the normalised Betti fraction is estimable classically to additive
`eps` in `n^{O(gamma^{-1/2} log(1/eps))}` (Apers–Gribling–Sen–Szabó arXiv:2211.09618,
DOI 10.22331/q-2023-12-06-1202); hence no super-polynomial quantum advantage exists at
`gamma = Omega(1)`, and the only surviving window is `gamma = 1/poly(n)` together with
`eps = 1/poly(n)` and a chain dimension and Betti number both exponential (necessary
conditions of Berry et al. arXiv:2209.13581, DOI 10.1103/PRXQuantum.5.010319). —
depends-on: C-NEW-KB-HOCHSTER, D-betti-gap, D-normalised-betti-fraction, C-100;
where-proved: cited literature; where-tested: none. Relevance/traps: the dequantization
audit of PRD criterion 4; guards against comparing with Macaulay2 instead of with a
Chebyshev filter.

**C-NEW-KB-GAP-INDEPENDENT.** The Betti gap `g_{i,N}` is not bounded above or below by any
function of the Macaulay gap `Delta_N`: for `I = (z_0^2, z_0z_1, z_1^3)`, `Delta_N = 1` for
all `N >= 2` while `g_{2,N}` grows linearly; for two random integer quadrics in `P^3`,
`Delta_N in [31, 56]` while `g_{i,N} in [0.45, 7.2]` over `N <= 7`. — depends-on:
D-betti-gap, D-macaulay-gap, C-052; where-proved: none (numerical); where-tested: part C.
Relevance/traps: K-KB6; guards against inheriting arm A's gap promises for free.

**C-NEW-KB-FRACTION.** For a complete intersection of `c` quadrics in `P^n` the normalised
Betti fraction at block `(i, N=i)` is exactly `C(c,i)/(HF(i) C(n+1,i)) ~ C(c,i)(i!)^2
n^{-2i}`: inverse-polynomial in `n` at fixed homological degree `i`, exponentially small in
`i`. In particular arm B's observable is **not** killed by the applications memo's
codimension law (caution 1), unlike the normalised Hilbert function. — depends-on:
D-normalised-betti-fraction, C-062; where-proved: Koszul resolution plus the closed-form
Hilbert series; where-tested: part C', `n in {3,5,10,20,40}`, `c in {2,3,5,10,20}`.
Relevance/traps: the one favourable normalisation finding in the arm; guards against
exponentially small overlaps.

**C-NEW-KB-SEED-IS-A-BLOCK.** For the supercharge `Q_f = sum_j a^†(f_j) ⊗ gamma_j` on
`F ⊗ Lambda(C^d)`, `Q_f^2 = 0` and the fermion-number-zero block of
`Q_f Q_f^† + Q_f^† Q_f` is exactly the seed Hamiltonian `H = sum_j a^†(f_j)a(f_j)`; its
higher blocks compute `H_i(f;R) = Tor_i^{C[y_1..y_d]}(C,R)`, which vanish for `i > 0`
exactly when `(f_1..f_d)` is a regular sequence and are **not** `beta_{i,j}(R/I)`. —
depends-on: D-generator-koszul-supercharge, D-hamiltonian, D-k-body, C-008; where-proved:
§1 Step 8; where-tested: none (mutation M4 is the proposed test). Relevance/traps: the
only projector-free boson–fermion Hamiltonian this lane found, hence the only hardware hook
(K-KB7); guards against conflating the two Koszul complexes.

**C-NEW-KB-NO-FREE-LUNCH.** Every evaluation of `L_W` requires the ground-space projector
`P_0`, so arm B's cost is at least arm A's: `Õ(n · (alpha_BE/Delta_N) · ((N+i)/g_{i,N}))`
uses of the sparse `H_N` block encoding per application, and arm B inherits every promise
of C-055, C-056 and C-058 plus a new one on `g`. — depends-on: C-NEW-KB-FREE, C-055,
C-056, C-058, D-qsvt; where-proved: §1 Step 9.1; where-tested: none. Relevance/traps: K-KB2,
K-KB9; guards against a space claim (PRD D15, C-264).

---

## 7. Questions for TJO

1. **Is a hardness anchor a product?** The sharpest thing this lane found is
   C-NEW-KB-QMA1: an algebraic-geometry problem (gapped graded-Betti decision for
   Stanley–Reisner ideals) that is QMA_1-hard by an explicit reduction to published clique
   homology results. That is *stronger* than the seed's only hardness candidate (C-124,
   conjectural), and it is a negative result for speedups. PRD §7 Q4 asks the same question
   for invariants; here it is asked for hardness.
2. **Do we fund the Bombieri-type lower bound on the Betti gap?** K-KB6 is the single
   analytic question that decides the arm: is `g_{i,N}/(N+i) >= 1/poly(n, N)` for a named
   class (monomial? complete intersections? unit-BW generators)? One analytic week. Without
   it, §3.4(a) dequantizes everything at constant gap.
3. **Arm B versus arm A ordering.** C-NEW-KB-NO-FREE-LUNCH says arm B strictly contains arm
   A in cost. Recommendation: arm B is not funded as a *speedup* lane at all; it is folded
   into arm A as (i) the presentation-independent-observable argument (Step 9.2) and (ii) the
   hardness anchor. Confirm or overrule.
4. **The other supercharge (Step 8).** `Q_f = sum_j a^†(f_j) ⊗ gamma_j` is a genuine
   `m`-body boson–fermion Hamiltonian whose `i=0` block is the seed's `H` and whose higher
   blocks measure failure of the complete-intersection property. It has the hardware hook
   the Betti Laplacian lacks. Fund a one-day probe (extend the same script), or leave it?
5. **Literature scout (K-KB4).** Cade–Crichigno already own "SUSY ground energy zero iff
   nontrivial cohomology". Before anything else, does the specific identification
   "graded Betti numbers = nullity of a Laplacian built from compressed multiplications on
   the Macaulay inverse system" exist? Same shape as C-110; recommend running them together.
6. **Reference corrections to merge** (found while resolving ids, all fetched):
   classical memo [R31] is **Neiger & Schost**, two authors, arXiv:1912.01848; the LGZ
   arXiv title says "big data", the Nature Communications title does not; and
   Gyurik–Cade–Dunjko prove DQC1-hardness of **LLSD**, not of normalised Betti number
   estimation — the classical memo §10's "parallels quantum TDA [R33]" is fine but any row
   that cites GCD for Betti hardness must be reworded.
7. **Does `reg` in the input promise (K-KB10) count as cheating?** Every arm-B problem
   statement needs `j <= reg(R/I)` supplied, and `reg` is worst-case doubly exponential.
   The same defect afflicts C-011's stable range, so a campaign-wide ruling would help.
