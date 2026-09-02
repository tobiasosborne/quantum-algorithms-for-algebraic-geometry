<!-- ROLE: arm B proposer lane (brief `briefs/lane-koszul-betti.md`): the supersymmetric
     Koszul Laplacian for graded Betti numbers. Scouting memo, not a claims file.
     Writable files of this lane: this file and checkers/explore/koszul_laplacian.py.
     REPAIRED at round r1 against verdicts/koszul-betti-r1.md (FAIL, O2 FATAL, 11 MAJOR).
     Every objection O1-O16 is dispositioned in §8. -->

# Koszul / supersymmetric Laplacian for graded Betti numbers (arm B, round 1, repaired r1)

Conventions C1–C12 of `definitions/definitions.md` are in force; symbols are cited by `D-`
id and never redefined. One departure, the same one `checkers/README.md` records for the
whole suite: every `Delta_N` printed by the numerics is the Macaulay gap of the generating
tuple **as written** (unit coefficients on monomials), not of a unit Bombieri–Weyl
presentation (C5, OPEN-1).

**Status after r1 (honest, and the header of the memo, not a footnote).** *Nothing here is a
theorem of this campaign.* All ten proposed rows are CONJECTURE, HOLD or REFUTED per L1; the
`D-` ids below are **not yet registered headings** in `definitions/definitions.md` and the
`C-NEW-KB-*` ids are **provisional** — a merge must register the definitions first and assign
real C-ids (O13). Measured against PRD §2, **none of criteria 1–5 is met** (§3, O14). What the
lane has is: a finite-dimensional identification, checked to machine precision against two
independent references; two exact structural facts about the compression; a reduction of the
squarefree part of the problem to simplicial Betti numbers; and one proved infinite
counterfamily separating the Betti gap from the Macaulay gap. What the lane does **not** have
is a quantum algorithm with a proven output, because the output as originally stated is a
`W_N`-conditional quantity whose preparation cost was omitted (O2, FATAL; fixed in Step 9 and
propagated).

**The four findings that decide the arm.** (i) *The naive compression is information-free*:
on the full Fock ⊗ Λ space the Koszul Laplacian is identically the free number operator
`N̂ + F̂`, so `P̂ L P̂ = (N+i) P̂` has no kernel (Step 4.3, K-KB2). (ii) *The estimable output is
an ambient trace of the harmonic projector, and the useful one is conditional on `W_N`*: the
ambient fraction `beta_{i,j}/(M_N C(n+1,i))` is the normalised trace of the harmonic projector
on `W_N ⊗ Lambda^i` **extended by zero**, reached by filtering `L~ = L_W + (N+i)(1 - P̂_N)` and
**not** by the zero-eigenvalue fraction of `L_W` extended by zero (O17); converting it to the
conditional fraction `beta_{i,j}/(HF(N) C(n+1,i))` costs `M_N/h_N` samples or
`sqrt(M_N/h_N)` coherent projections (C-096). The acceptance weight `h_N/M_N` is
exponentially small for the quadratic complete-intersection family at `N = n`, and
potentially exponentially small in general; equivalently, the rejection-sampling cost
`M_N/h_N` and coherent-projection cost `sqrt(M_N/h_N)` are exponentially large (O23). The
acceptance weight is **not** exponentially small for every square system (Step 9,
K-KB11). (iii) *Betti information
lives only at `N = j - i <= reg(R/I)`* (Step 6, K-KB1) —
note `N`, not `j`, and `reg(R/I) = reg(I) - 1`. (iv) *Only the squarefree multidegree summands
are simplicial Laplacians*, so the quantum-TDA hardness and dequantization theorems transfer
to a squarefree-multidegree version of the problem and **not** to the total-degree block
(Step 5.5, K-KB3, K-KB12).

---

## 1. Statement and sketch

Lamport-hierarchical; every leaf cites a `D-` id, a `C-` id, a named checker part, or a cited
theorem. All operator identities on the full Fock space are asserted on the **finite-particle
core** `R ⊗ Λ`, with closures understood; `a_k`, `Q` and `L` are unbounded on the completion
(O10). Finite-block nullities, norms and spectra are unaffected.

**ASSUME.** `R = C[z_0..z_n]` (D-polynomial-ring), `I = (f_1,...,f_d)` homogeneous and proper
with `deg f_j = m_j >= 1`, `H = sum_j a^†(f_j) a(f_j)` (D-hamiltonian), `H_N = H|_{R_N}`,
`P_{0,N}` the projector onto `ker H_N` (D-projectors), Fock inner product (C1).
**PROVE.** With `q`, `L_W`, `g_{i,N}` of Steps 2 and 5,
`dim ker(L_W | (i,N)) = beta_{i,i+N}(R/I)`; `||L_W|| <= N+i`; and `beta_{i,j} = 0` for
`j - i > reg(R/I)`.

**Step 1 (the graded inverse system, and its annihilation-invariance).** 1.1
`ker H_N = (I_N)^perp` (C-008, D-ground-space), the degree-`N` part of the Macaulay inverse
system of `conj(I)` (C-012, D-inverse-system); by C-014 the map `[u] |-> P_0 u` is a linear
isomorphism `(R/I)_N -> (I_N)^perp`. Write `W_N := (I_N)^perp`, `W := ⊕_N W_N`,
`P := ⊕_N P_{0,N}`. 1.2 For `u in W_N` and `h in I_{N-1}`,
`<a_k u, h> = <u, a_k^† h> = <u, z_k h> = 0` since `z_k h in I_N` (D-mode-operators); hence
`a_k W_N ⊆ W_{N-1}` for every `k, N`, equivalently `(1 - P_{0,N-1}) a_k P_{0,N} = 0`. No
radicality, saturation, genericity or stable-range hypothesis is used (O15).

**Step 2 (the supercharge).** 2.1 Adjoin `n+1` fermionic modes on `Lambda(C^{n+1})`,
`{c_k,c_l^†} = delta_{kl}`, `F̂ = sum_k c_k^† c_k`, basis `|S>` for `S ⊆ {0..n}` with
`c_k^†|S> = (-1)^{#{l in S : l<k}}|S ∪ {k}>` for `k not in S`, else `0`. 2.2
`Q := sum_k a_k ⊗ c_k^†` on the finite-particle core satisfies
`Q^2 = (1/2) sum_{k,l} a_k a_l {c_k^†, c_l^†} = 0` **exactly** — no compression, no error term.
2.3 `Q` maps block `(i,N)` to `(i+1,N-1)`, preserving the **internal degree** `j := N+i`; the
natural sector is `j`, not `N`. 2.4 By Step 1.2, `Q(W ⊗ Lambda) ⊆ W ⊗ Lambda`; write
`P̂ := P ⊗ 1` and `q := Q P̂ = P̂ Q P̂`. 2.5 The adjoint *within* `W ⊗ Lambda` is
`q^† = sum_k Z_k ⊗ c_k` with `Z_k = P_{0,N} a_k^† P_{0,N-1}` the **compressed multiplication**
(D-compressed-multiplication) — not the restriction of `sum_k a_k^† ⊗ c_k`, since `a_k^†` does
not preserve `W`.

**Step 3 (the complex is the conjugate dual Koszul complex of `R/I`; Hodge).** 3.1
`K_.(z_0..z_n ; R/I)` has `(K_i)_j = (R/I)_{j-i} ⊗ Lambda^i`, `∂ = sum_k mu_{z_k} ⊗ iota_k`,
`H_i(K_.) = Tor_i^R(R/I,C)`, graded pieces `beta_{i,j}(R/I)` (Eisenbud, *The Geometry of
Syzygies*, GTM 229, DOI 10.1007/b137572). 3.2 Under C1 the Fock pairing is conjugate-linear in
its first argument, so `u |-> ([h] |-> <u,h>)` is an **anti-linear** isomorphism
`W_N -> (R/I)_N^*` (O10). Step 1.2 identifies `a_k` with the Hilbert adjoint of `mu_{z_k}` and
`c_k^†` with the adjoint of `iota_k`, so `(W ⊗ Lambda, q)` is the **conjugate-linear dual** of
`K_.(z; R/I)` — not literally a complex-linear transpose. Dimensions are unaffected. 3.3 For a
complex of finite-dimensional Hilbert spaces `ker L` is the harmonic space, of the dimension of
the homology there; homology of the (conjugate) dual is dual to the homology. Hence

> **KB1.** `dim ker(L_W | (i,N)) = beta_{i,i+N}(R/I)` for all `i in 0..n+1`, `N >= 0`.

Part A: exact agreement on every block of six ideals against **two** independent references —
Koszul ranks over GF(p) and hard-coded literature Betti tables (O12).

**Step 4 (the full Laplacian is the free number operator).** 4.1 On the finite-particle core,
with `a_k a_l^† = a_l^† a_k + delta_{kl}` and `c_l c_k^† = delta_{kl} - c_k^† c_l`,
`Q Q^† + Q^† Q = sum_k a_k^† a_k ⊗ 1 + 1 ⊗ sum_k c_k^† c_k = N̂ + F̂`, the scalar `N+i = j` on
block `(i,N)` (part B: `1.8e-15`). 4.2 *Exactness*: `ker L = 0` except at the vacuum.
4.3 ***The naive compression is information-free***: `P̂ L P̂ = (N+i) P̂` exactly (part B:
`4.4e-15`), so its nullity on `range(P̂)` is `0` for `j > 0`. The operator to encode is `L_W`,
built from the `Z_k`. 4.4 *Normalisation*: with `X := P̂ Q (1-P̂)` — **constructed explicitly**
in part B, not defined as `(N+i)1 - L_W` (O12) — expanding
`P̂ Q Q^† P̂ = P̂ Q P̂ Q^† P̂ + X X^†` and using `(1-P̂) Q P̂ = 0` gives `L_W = (N+i)·1 - X X^†`
with `X X^† >= 0`, hence `0 <= L_W <= (N+i)1` and `||L_W|| <= j` (part B: `7.1e-15`; `L_W`
PSD to `-1.0e-15`). 4.5 *The `i=0` row is trivial*: `L_W|(0,N) = P_0 N̂ P_0 = N·1`.

**Step 5 (the Betti gap, and what supersymmetry actually pairs).** 5.1 When
`L_W|(i,N) != 0`, set `g_{i,N} := lambda_min^{>0}(L_W|(i,N))`, normalised `g_{i,N}/(N+i)`;
when the block Laplacian vanishes identically the gap is undefined and no promise may be made
(O1). 5.2 By 4.4, `g_{i,N} = j - lambda_max^{<j}(X X^†)`. 5.3 **Correction (O8).** Adjacent
*block Laplacians* do **not** share their nonzero spectra: for the twisted cubic at `j = 3`,
`g(0,3) = 3.0000` while `g(1,2) = 1.3333`. What supersymmetry gives is the singular-value
pairing of each *individual* differential,
`spec^{>0}(q_{(i,N)}^† q_{(i,N)}) = spec^{>0}(q_{(i,N)} q_{(i,N)}^†)`, the second living in
block `(i+1,N-1)`; `L_W|(i,N)` is the sum of two such contributions. Part C tests exactly this
equality (max deviation `2.1e-14`). 5.4 `g_{i,N}` is an invariant of the **ideal and the Fock
metric**, not of the generating tuple (O7); only the *cost of manufacturing* `P_0` through
`H_N` is presentation-dependent. It is not `Delta_N` (D-macaulay-gap), and no analogue of
Fact 7.1 (**C-103**, not C-107 — O13) is known for it. Part E supplies a proved infinite
counterfamily (Step 5.6). 5.5 **The multigrading (O4).** For a monomial ideal the block
`(i,N)` splits over total multidegrees `mu` with `|mu| = i+N`. Only the **squarefree** `mu`
are the reduced simplicial chain Laplacians of Hochster's formula; the rest of the block is
non-squarefree and is covered by no cited TDA theorem. Part D prints both dimensions: for the
7-cycle at `(i=2,N=1)` the block has dimension 147 of which 105 is squarefree. 5.6
**Counterfamily.** For the `m`-cycle Stanley–Reisner ideal (`m >= 4`): `Delta_2 = 1` for every
`m` (monic monomial generators, `H_2` diagonal), while the squarefree summand `sigma = [m]` of
block `(i=m-2, N=2)` is unitarily the edge Laplacian `∂_1^† ∂_1` of the cycle graph — its
1-chain group has no incoming `∂_2` because `C_m` has no 2-faces — with nullity
`1 = b_1(C_m)` and smallest nonzero eigenvalue exactly `2 - 2cos(2 pi/m) = Theta(m^{-2})`.
Part E verifies this closed form for `m = 4..12`. What this proves, stated with the
quantifier the evidence supports (O20): **"The `m`-cycle family rules out any uniform
strictly positive lower bound on the selected squarefree-summand gap depending only on
`Delta_2`: no `phi` with `phi(1) > 0` satisfies `g_sq >= phi(Delta_2)` throughout this family.
No total-block or reverse comparison is established."**

**Step 6 (support: Betti information lives at `N <= reg(R/I)`).** `reg(R/I) =
max{j-i : beta_{i,j} != 0}` (D-saturation-regularity-stable-range) and `beta_{i,j} = 0` for
`i > n+1` (Hilbert syzygy). Since the block label is `N = j-i`:

> **KB2.** `dim ker(L_W|(i,N)) = 0` for every `i` whenever `N > reg(R/I)`.

**The condition is on `N = j - i`, never on `j` (O1).** The twisted cubic has
`reg(R/I) = 1` and `beta_{2,3} = 2`, so `j = 3 > reg(R/I)` while `N = 1 <= reg(R/I)`; a
`j <= reg` condition would exclude a flagship positive block. Note also
`reg(I) = reg(R/I) + 1` for a nonzero proper homogeneous ideal; the memo uses `reg(R/I)`
throughout. Part A checks KB2 as a prediction to `N = 8,7,7,6,5,4` against
`reg(R/I) = 1,2,2,1,1,2`. This does not preclude large `N`: it says the useful `N` is bounded
by a regularity that may itself grow with `n`.

**Step 7 (relation to `Syz(I)_N` and the §5 rows).** 7.1 `Syz(I)_N = ker Phi_N`
(D-syzygy-module, C-052) is the non-minimal degree-`N` piece of the *tuple's* syzygies, of
dimension `sum_j dim R_{N-m_j} - dim I_N`, fixed by the Hilbert function; it is not a Betti
number. 7.2 **Corrected (O9).** `beta_{1,j}(R/I)` counts minimal generators of `I` in degree
`j`, and `beta_{2,j}(R/I)` counts the degree-`j` minimal relations in a **minimal free
resolution**, equivalently the minimal relations among a **minimal homogeneous presentation**.
The formula `beta_{2,j} = dim(Syz / m Syz)_j` is false for a non-minimal tuple: the redundant
tuple `(x, x)` for `I = (x)` has the constant syzygy `(1,-1)`, which survives mod `m Syz`,
although `beta_{2,*}(R/(x)) = 0`. 7.3 *Caution*: the first nonzero row is free. For `I` with
no linear forms, `L_W|(1,1) = 2 - X X^†` with `X f = sum_k (∂_k f) ⊗ e_k` the gradient on
`I_2`, and `sum_k ||∂_k f||^2 = <f, N̂ f> = 2||f||^2`, so `X^†X = 2` on `I_2` and
`beta_{1,2} = dim I_2` — a rank of the input (confirmed in every family: 3, 2, 5, 14). The
first genuinely non-input block is `i = 2`.

**Step 8 (the other supercharge: the seed's `H` is a Koszul block).** With `d` fermionic
annihilators `c_j` (fermion `j` carrying internal weight `m_j`) and
`Q_f := sum_j M_{f_j} ⊗ c_j`, `Q_f^2 = 0` and the fermion-number-zero block of
`Q_f Q_f^† + Q_f^† Q_f` is `sum_j M_{f_j} M_{f_j}^† = sum_j a^†(f_j) a(f_j) = H_N`. **Now
tested** (part F, `|L^{gen}_{i=0} - H_N| = 0` exactly for `N = 2..5` on the twisted cubic).
Its higher-block zero modes are `H_i(f;R) ≅ Tor_i^{C[y_1..y_d]}(C,R)`, which vanish for `i>0`
exactly when the positive-degree sequence is regular; these are **not** `beta_{i,j}(R/I)` —
part F prints both tables and they differ at `t = 2..6` (e.g. `t=2, i=1`: `H_1(f;R) = 0`
versus `beta_{1,2} = 3`). This is what makes mutation M4 a real red mutation.

**Step 9 (what a quantum algorithm actually costs — the O2 repair).** Let `M_N = dim R_N`,
`h_N = HF_{R/I}(N)`, `b = C(n+1,i)`.
9.1 *Two different outputs, and the right operator for each (O17).* The **ambient-normalised**
fraction is `beta_{i,j}/(M_N b)`. It is the normalised trace of the **harmonic projector on
`W_N ⊗ Lambda^i` extended by zero** to `R_N ⊗ Lambda^i` — it is **not** the zero-eigenvalue
fraction of `L_W` extended by zero, because that extension makes the whole orthogonal
complement of `W_N ⊗ Lambda^i` a spurious zero eigenspace of dimension `(M_N - h_N) b`. The
operator to filter is therefore
`L~_{i,N} = L_W + j (1 - P̂_N)`, `j = N + i > 0`,
whose zero eigenspace is exactly the harmonic subspace; the extra `(1 - P̂_N)` term is one more
use of the ground-space projector and must be priced. Part h reproduces the critic's instance
exactly: the 5-cycle at `(i,N) = (3,2)` has `M_N = 15`, `h_N = 10`, `b = 10`, `beta_{3,5} = 1`,
ambient ratio `1/150 = 0.006667`, whereas zero-extended `L_W` has nullity
`(15-10)·10 + 1 = 51`, i.e. `51/150 = 0.34`. The **`W_N`-conditional** fraction
`beta_{i,j}/(h_N b)` — the quantity the r0 memo claimed — is a conditional probability inside
`W_N` and is estimated only with normalised access to `W_N`.
9.2 *The missing factor.* Converting requires preparing `P_{0,N}/h_N`, which succeeds from the
ambient mixed state with weight `h_N/M_N`; so either `Theta(M_N/h_N)` rejection samples, or
`sqrt(M_N/h_N)` coherent projections (exactly the black-box-projection cost of **C-096**), or
an assumed efficient preparation oracle for `P_{0,N}/h_N`. Any conditional-output claim
therefore needs the extra promise `h_N/M_N >= 1/poly(n)`.
9.3 *How expensive that promise is — with the quantifier the evidence supports (O21).*
`h_N/M_N` is the normalised Hilbert function (D-normalised-hilbert-function). The applications
memo's codimension law, `≈ rho^{codim}` with `rho ≈ 0.75`, was **measured for complete
intersections of quadrics at `N = n`** (caution 1, F2), and in that family the factor is
exponentially small. It is **not** a statement about square systems in general: for `n` generic
forms of degree `n+1` in `P^n` — also a zero-dimensional square complete intersection — every
generator has degree `> N` at `N = n`, so `I_N = 0`, `h_N = M_N` and `h_N/M_N = 1`. Part h
prints both columns side by side (`0.667, 0.400, 0.229, 0.020` for the quadric family at
`n = 2,3,4,8` against `1.000` throughout for the degree-`(n+1)` family). The honest statement
is: **the acceptance weight can be exponentially small, making conditional normalization
exponentially expensive; no unconditional conditional-output algorithm follows without a
Hilbert-weight promise or preparation oracle.** That retraction —
r0 had declared the overlap trap untriggered — is the FATAL fix.
9.4 *Per-call cost, adjacent degrees, and filtering repetitions (O11, O18).* On block `(i,N)`,
`L_W = q_{i,N}^† q_{i,N} + q_{i-1,N+1} q_{i-1,N+1}^†`; the first term uses `P_{0,N}`, but the
incoming term contains `Q P_{0,N+1} Q^†`. **Access to `H_N` alone, with a promise only on
`Delta_N/alpha_N`, does not construct the block**: a small `Delta_{N+1}` defeats the
implementation even under that promise. Part h shows the failure is not gradual — rebuilding
the incoming term without `P_{0,N+1}` gives `q^†q + (jP̂ - q^†q) = j·1`, nullity `0` instead of
`beta`, in every block tested. So *generator mode* must supply `H_N` **and** `H_{N+1}` with
their normalisations and promise `Delta_r/alpha_r >= 1/poly(n)` for every nontrivial required
projector `r in {N, N+1}`; *quotient mode* must supply **both** adjacent compressed maps
`Z_{k,N} : W_{N-1} -> W_N` and `Z_{k,N+1} : W_N -> W_{N+1}`. It remains true (O11) that
quotient mode needs no per-call QSVT at all — for a monomial ideal the standard-monomial
membership predicate gives the `Z_k` directly. Separately, kernel-projector filtering needs
`O((j/g_{i,N}) log(1/eps))` **repetitions** of a call; `j/g` is a repetition count, not a
per-call factor.
9.5 *The honest totals.* Ambient-normalised output at additive `eps`, filtering `L~`:
`Õ( C_call · (j/g_{i,N}) · eps^{-2} )`, with `C_call = O(n)` under quotient access to both
adjacent degrees, and `C_call = O(n · max_{r in {N,N+1}} alpha_r/Delta_r)` under generator
access to `H_N` and `H_{N+1}`; the `(1 - P̂_N)` term of `L~` adds one more projector use.
Conditional output: multiply by `M_N/h_N` (sampling) or `sqrt(M_N/h_N)` (coherent), or assume
the preparation oracle.
9.6 *One honest positive.* `beta_{i,j}(R/I)` is an invariant of `I`, so `dim ker L_W` does not
move when the generating tuple changes — the presentation-independence `Delta_N` lacks
(D-macaulay-gap pitfall (i), C-106). Arm B's *output* is better posed than arm A's.

---

## 2. Numerics

Regenerate with (15.0 s wall on this machine, exit 0):

```bash
cd /home/tobias/Projects/quantum-algorithms-for-algebraic-geometry/checkers
timeout 900 python3 explore/koszul_laplacian.py
```

`checkers/explore/koszul_laplacian.py` is an **exploration** script, excluded from
`run_all.sh`, and red-capable (L4): every block prints OK/MISMATCH, exit 1 on any mismatch,
exit 2 on an unexpected exception. Repairs made at r1 (all demanded by O12): (1) a **literature
fixture Betti table per ideal** is asserted and compared alongside the GF(p) value, so mutating
a fixture ideal can no longer make the script verify a new ideal against itself; (2) `X` is
**constructed** as `P̂ Q (1-P̂)` and used to test `L_W = (N+i)1 - X X^†`, instead of being
defined as the difference; (3) nullity uses `|ev| < TOL` and positivity (`lambda_min > -TOL`)
is tested separately; (4) all four mutations M1–M4 are **run in-process** and must come out
red, with M4 driven by the part-F comparison rather than asserted; (5) GF(p) results are
labelled by characteristic (`p = 10^9+7`; the tested examples are characteristic-independent,
as the critic's independent SymPy computation over `Q` confirmed). Added at r2: (6) part **h**, which computes the ambient
harmonic-projector trace via `L~ = L_W + j(1 - P̂_N)`, exhibits the wrong zero-extended
quantity beside it, shows that dropping `P_{0,N+1}` collapses the block, and prints the
`h_N/M_N` counterfamily of O21 — each with its own OK/MISMATCH line; and (7) an **independent
recomputation** of the complete-intersection block dimensions in part g (Hilbert series by
explicit polynomial multiplication, binomials by a Pascal recurrence) with an OK/MISMATCH
line, after O19 found the r1 memo table stale. **Residue (unchanged):** registering M1–M4 in
`checkers/MUTATIONS.md` is a merge action — that file is outside this lane's writable set.

**(a) nullity per block against two independent references.** Twisted cubic, Betti-carrying
blocks and neighbours (`null` = quantum-side nullity, `GF(p)` = Koszul-rank reference,
`fix` = literature fixture, `lam_min` = smallest eigenvalue, tested `> -TOL`):

```
 i  N   j  dimblk  null  GF(p)  fix             g_{i,N}  g/(N+i)    lam_min   beta/dim
 0  0   0       1     1      1    1        OK       nan      nan   0.00e+00  1.000e+00
 1  1   2      16     3      3    3        OK    2.0000   1.0000  -9.44e-16  1.875e-01
 2  1   3      24     2      2    2        OK    1.3333   0.4444  -1.03e-19  8.333e-02
 3  1   4      16     0      0    0        OK    1.0677   0.2669   1.07e+00  0.000e+00
 1  2   3      28     0      0    0        OK    1.3333   0.4444   1.33e+00  0.000e+00
  reg(R/I) = 1 (so reg(I) = 2); support condition is N = j-i <= reg(R/I), NOT j <= reg
  prediction 'nullity = 0 for every N > reg(R/I)' to N = 8: OK
```

Six ideals in all — twisted cubic, a complete intersection of two random integer quadrics in
`P^3` (`beta_{1,2}=2, beta_{2,4}=1`, `reg(R/I)=2`), the monomial ideal `(z0^2,z0z1,z1^3)` in
`P^2` (a genuine two-row table `beta_{1,2}=2, beta_{1,3}=1, beta_{2,3}=1, beta_{2,4}=1`),
`(z0^2,z0z1,z1^2)` in `P^2` (`3, 2`), the rational normal quartic in `P^4` (Eagon–Northcott
`6, 8, 3`) and the 5-cycle Stanley–Reisner ideal (`5, 5, 1`) — every block of every family, no
mismatch, all three columns agreeing, `L_W` PSD throughout.

**(b) the uncompressed Laplacian, `X` constructed, and the dead compression.**

```
max |Q Q^dag + Q^dag Q - (N+i)1|            = 1.78e-15  OK
max |L_W - ((N+i)1 - X X^dag)|, X built     = 7.11e-15  OK
max |Phat L Phat - (N+i) Phat|              = 4.44e-15  OK  => nullity of P_0 L P_0 is 0
```

**(c) Betti gap versus Macaulay gap, and the corrected pairing.** Twisted cubic:

```
 N    Delta_N     g(i=0)     g(i=1)     g(i=2)     g(i=3)
 2     2.0000     2.0000     1.3333     1.0677     2.2279
 4     3.5505     4.0000     3.6000     3.3663     4.4733
 8     6.8377     8.0000     7.7778     7.6672     8.7064
  O8 check: spec^>0(q^dag q)|(i,N) = spec^>0(q q^dag)|(i+1,N-1) for every single
  differential, max deviation 2.13e-14  OK
  adjacent BLOCK Laplacians do NOT share full nonzero spectra: at j=3,
  g(0,3)=3.0000 but g(1,2)=1.3333
```

`g(i=0,N) = N` exactly (Step 4.5). For the monomial ideal `Delta_N = 1` for all `N` while
`g` grows; for the two random integer quadrics `Delta_N in [31,56]` against `g in [0.45,7.2]`.

**(d) Hochster, with the squarefree/non-squarefree split made explicit (O4).**
`beta_{i,j} = sum_{|sigma|=j} dim H~_{j-i-1}(Delta|_sigma)` (Hochster 1977, *Ring Theory II*,
Proc. 2nd Oklahoma Conf. 1975, 171–223, Dekker LNPAM 26 — no DOI exists for that article; the
standard modern statement is Miller–Sturmfels, *Combinatorial Commutative Algebra*, GTM 227,
Cor. 5.12, DOI 10.1007/b138602). The `sqfree` column is the dimension of the squarefree part
of the block, i.e. the part that is a simplicial Laplacian:

```
  7-cycle, I_Delta = 14 quadrics in P^6, HF(N) = [1, 7, 14, 21]
   i  N  j  dimblk  sqfree  null  GF(p)  Hoch             g_{i,N}   beta/dim
   1  1  2      49      42    14     14    14        OK    2.0000  2.857e-01
   2  1  3     147     105    35     35    35        OK    1.0000  2.381e-01
   3  1  4     245     140    35     35    35        OK    0.5858  1.429e-01
   4  1  5     245     105    14     14    14        OK    0.3820  5.714e-02
   5  2  7     294       7     1      1     1        OK    0.7530  3.401e-03
```

(4-, 5- and 6-cycles likewise, all OK.) **The total block is strictly larger than its
squarefree part**, so a theorem about simplicial Laplacians does not by itself say anything
about the total-block spectrum.

**(e) the counterfamily (O7), new at r1.** `m`-cycle Stanley–Reisner ideals:

```
    m  Delta_2   g_sqfree  2-2cos(2pi/m)             g_total  agree?  g_sq/(N+i)
    4   1.0000   2.000000       2.000000        OK  2.000000     yes    0.500000
    6   1.0000   1.000000       1.000000        OK  1.000000     yes    0.166667
    8   1.0000   0.585786       0.585786        OK  0.585786     yes    0.073223
   10   1.0000   0.381966       0.381966        OK       nan     n/a    0.038197
   12   1.0000   0.267949       0.267949        OK       nan     n/a    0.022329
```

`Delta_2 = 1` for every `m` while the squarefree Betti gap is `Theta(m^{-2})` — **proved** for
the squarefree summand (Step 5.6), and the total-block gap coincides for `m <= 8` but that
coincidence is **observed, not proved**.

**(f) the generator-Koszul supercharge (Step 8), new at r1.**

```
  twisted cubic: d = 3 generators of degree [2,2,2]
    N=2..5: |L^gen_(i=0) - H_N| = 0.00e+00  OK          <- the seed H is this block
    t  i   dimK  nullity H_i(f;R)  beta_{i,t}(R/I)  differ?
    2  1      3                 0                3      YES
    3  1     12                 2                0      YES
    4  1     30                 5                0      YES
    6  1    105                11                0      YES
```

**(g) normalised Betti fraction, with the two regimes separated (O6).** Complete intersection
of `c` quadrics in `P^n`, block `(i, N=i)`, `beta_{i,2i} = C(c,i)`:

```
fixed i, c (block dimension is POLYNOMIAL in n, so there is no compression):
     n   c     i=1 frac     i=2 frac     i=3 frac       i=1 dim     i=2 dim     i=3 dim  check
    10   3    2.479e-02    8.658e-04    2.395e-05           121        3465       41745   OK
    20   5    1.134e-02    2.107e-04    4.513e-06           441       47460     2215780   OK
    40   5    2.974e-03    1.425e-05    7.730e-08          1681      701920   129369760   OK
    40  10    5.949e-03    6.449e-05    9.435e-07          1681      697820   127184460   OK
growing i (Boolean-type CI, c = n, i = n): fraction = 1/(2^n (n+1))
     n      dim block  beta_{n,2n}     fraction  check
     8           2304            1    4.340e-04  OK
    20       22020096            1    4.541e-08  OK
```

(The `check` column is the independent recomputation demanded by O19. The r1 memo printed
`23730` and `886445` for `n = 20, c = 5`; the correct dimensions are `47460` and `2215780`,
and the fractions printed beside them were always right.)

The exact fraction is `C(c,i)/(HF(i) C(n+1,i))`. **For fixed `c` and `i` and `n -> infinity`
it is asymptotic to `C(c,i)(i!)^2 n^{-2i}`** — inverse-polynomial, but the block dimension is
then also polynomial, so nothing is compressed. For `c = n` and fixed `i` the fraction is
`~ i! n^{-i}`, again with polynomial dimension. When `i = rho n` both the dimension and the
Betti number can be exponential, but the fraction is exponentially small (`1/(2^n(n+1))` at
`i = n`). **No regime with exponential block dimension and an inverse-polynomially visible
fraction has been exhibited.** The r0 claim that arm B "survives F2 where arm A does not" is
retracted (O6, and see Step 9.3 for the `h_N/M_N` half of the same problem).

**(h) the ambient observable, adjacent-degree necessity, and the `h_N/M_N` counterfamily
(new at r2).**

```
  ideal               i  N   M_N  h_N    b  beta null(0-ext) null(Ltilde)      amb frac null(no P_N+1)
  5-cycle SR P^4      3  2    15   10   10     1          51            1  OK  0.006667      0 OK (differs)
  5-cycle SR P^4      2  1     5    5   10     5           5            5  OK  0.100000      0 OK (differs)
  twisted cubic P^3   1  1     4    4    4     3           3            3  OK  0.187500      0 OK (differs)
  twisted cubic P^3   2  1     4    4    6     2           2            2  OK  0.083333      0 OK (differs)

  (O21)  n  quadrics h_n/M_n   deg-(n+1) h_n/M_n
         2          0.666667            1.000000  OK
         3          0.400000            1.000000  OK
         4          0.228571            1.000000  OK
         8          0.019891            1.000000  OK
```

Three readings. (1) `null(0-ext) = (M_N - h_N) b + beta` while `null(Ltilde) = beta`: the
zero-extended `L_W` has a spurious zero eigenspace, and only the harmonic-projector filter
`L~ = L_W + j(1 - P̂_N)` returns the ambient fraction (O17). The 5-cycle row is the critic's
own instance — `51/150 = 0.34` against the correct `1/150 = 0.006667`. (2) Rebuilding the
incoming term without `P_{0,N+1}` gives nullity `0` in every block, because `P̂ L P̂ = j P̂`
forces `q^†q + (jP̂ - q^†q) = j·1`: adjacent-degree access is **necessary**, not an
optimisation (O18). (3) For `n` generic degree-`(n+1)` forms in `P^n` — a zero-dimensional
square complete intersection — `h_N/M_N = 1` at `N = n`, so the overlap obstruction is a
statement about the *measured* quadric family, not about square systems in general (O21).

---

## 3. Against the north star (PRD §2, criteria 1–5): none met

Adjudication rewritten to match the critic's audit (O14). Each criterion states what fails and
what survives.

**1. Problem — FAILS as stated in r0, and the r1 restatement still carried defects.** r0 had a
false support condition (`j <= reg`), undefined denominators and gaps, and no access model
(O1); r1 added unused thresholds `a < b`, omitted `eps` from the input, and imposed the
optional regularity promise on the single-block decision problem (O22). The problem now used is
**D-betti-estimation-problem = the critic's D8, copied verbatim** (§5): `eps` is an input, the
thresholds are gone, regularity is optional metadata for enumerating the whole table, and both
access modes supply **adjacent degrees** (`H_N` and `H_{N+1}`, or `Z_{k,N}` and `Z_{k,N+1}`) as
O18 requires. *Survives*: a well-posed problem whose output is a presentation-independent
invariant of `I`, once the spectral, access and (for conditional output) Hilbert-weight
promises are supplied.

**2. Classical baseline — FAILS: no common-oracle comparison is established.** The relevant
methods are named but this memo does **not** determine which is best under the same access
model, nor give a complexity comparison in all of `n, N, i, eps, Delta_N, g, h_N/M_N`, and the
`n = 10..40` / `10^3..10^6` syzygy sizes are folklore practice numbers, **not tied to a sourced
benchmark for this task**. Named methods: minimal free resolutions by Schreyer frames and
Hilbert-function pruning (La Scala–Stillman, *J. Symbolic Comput.* 26(4) 409–431 (1998),
DOI 10.1006/jsco.1998.0221); finite-dimensional syzygies by fast linear algebra
(**Neiger–Schost** — two authors, correcting classical memo [R31] — *J. Complexity* 60, 101502
(2020), DOI 10.1016/j.jco.2020.101502, arXiv:1912.01848; `O(m D^{omega-1} + n D^omega log D)`);
and the one that would actually compete, stochastic Chebyshev/Lanczos eigenvalue counting on
the same sparse Koszul matrices (Di Napoli–Polizzi–Saad, *Numer. Linear Algebra Appl.* 23(4)
674–692 (2016), DOI 10.1002/nla.2048, arXiv:1308.4275). *Survives*: the observation that the
classical filter needs the same projectors at **both** adjacent degrees and the same gap
promises, so a fair comparison must give both sides the same quotient access at `N` and `N+1`;
and PRD D15 / SP-0 (C-264) refuses `n log N` qubits versus `M_N` words as a space separation.

**3. Quantum algorithm — FAILS (the r1 FATAL objection, and two further defects found at r2).**
(a) The `W_N`-normalisation cost was omitted; with it (Step 9.2) the conditional output carries
`M_N/h_N` or `sqrt(M_N/h_N)`. The acceptance weight `h_N/M_N` is exponentially small for the
quadratic complete-intersection family at `N = n`, and potentially exponentially small in
general; equivalently, the rejection-sampling cost `M_N/h_N` and coherent-projection cost
`sqrt(M_N/h_N)` are exponentially large. The acceptance weight is not exponentially small
for every square system, since `n` generic degree-`(n+1)` forms in `P^n` give `h_N/M_N = 1` at
`N = n` (Step 9.3, part h, O21, O23). (b) The ambient output must be obtained by
filtering `L~ = L_W + j(1 - P̂_N)`, not from zero-extended `L_W` (Step 9.1, O17). (c) The block
cannot be built from `H_N` alone: the incoming term contains `Q P_{0,N+1} Q^†`, so both
adjacent degrees and both gap promises are required (Step 9.4, part h, O18). No advantage
margin over any baseline is proven. *Survives*: the normalised trace of the harmonic projector
extended by zero is `beta_{i,j}/(M_N C(n+1,i))`, and given direct adjacent compressed maps, or
generator access with good gaps at every required adjacent degree, the filtering cost has the
advertised `j/g_{i,N}` dependence; and `||L_W|| <= j`, so the Koszul layer itself needs no
`alpha_BE`-type normalisation.

**4. Dequantization audit — FAILS: the r0 conclusion does not follow.** Two independent
errors, both conceded.
(a) *Arithmetic (O3).* Apers–Gribling–Sen–Szabó, *Quantum* 7, 1202 (2023),
DOI 10.22331/q-2023-12-06-1202, arXiv:2211.09618, estimate the `k`-th normalised Betti number
of a simplicial complex to additive `eps` in `n^{O(gamma^{-1/2} log(1/eps))}`, `gamma` the
combinatorial-Laplacian gap. At `gamma = Omega(1)` **and constant `eps`** this is polynomial.
At `gamma = Omega(1)` and `eps = 1/poly(n)` it is `n^{O(log n)}` — quasi-polynomial, which
**still permits a super-polynomial separation** from a polynomial quantum algorithm. The r0
sentences "no super-polynomial quantum advantage exists at `gamma = Omega(1)`" and "the only
surviving window is `gamma = 1/poly(n)`" are **withdrawn**.
(b) *Access model (O4).* The theorem is proved for combinatorial Laplacians of simplicial
complexes, using their row structure and bounded path-integral weights. A generic `L_W`
contains the generally dense `P_0`; a QSVT block encoding is not a classical sparse-row oracle;
and this memo never constructs sparse row access to `L_W` from the generators. Even for
Stanley–Reisner ideals the total-degree block contains non-squarefree multidegrees beyond the
induced-complex summands (part d). *Survives*: the theorem applies directly to the squarefree
multidegree summands that are literally simplicial Laplacians, and there it says that at
constant normalised gap and constant additive error the classical estimator is polynomial time.
(c) *Hardness that does hold.* Schmidhuber–Lloyd, *PRX Quantum* 4, 040349 (2023),
DOI 10.1103/PRXQuantum.4.040349, arXiv:2209.14286: exact Betti numbers #P-hard, multiplicative
approximation NP-hard. Through Hochster this transfers to `beta_{i,j}` of Stanley–Reisner
ideals unconditionally, agreeing with classical memo §10, C-091/C-092 and D-hardness-anchors.
(d) *Hardness that does not transfer as claimed (O5).* King–Kohler, arXiv:2311.17234, FOCS
2024, 493–504, DOI 10.1109/FOCS61266.2024.00039 (also SIAM J. Comput. FOCS24 section,
DOI 10.1137/24M1710243), prove the gapped result for **weighted** clique complexes; C1's Fock
metric produces the **unweighted** squarefree block and this memo supplies no encoding of
arbitrary vertex-product weights. Hayakawa, arXiv:2608.02726 (2026, arXiv only), supplies an
unweighted gapped theorem, but for **one** clique-complex Laplacian, whereas `g_{i,N}` is a
minimum over the target squarefree multidegree **and every other multidegree in the block**;
Hochster preserves nullity, not that global gap. Also QMA_1-hardness excludes a BQP algorithm
only under `QMA_1 ⊄ BQP`. *Survives*: unweighted gapped clique homology transfers to a
**squarefree-multidegree** version of the Betti-Laplacian problem; the total-block gapped
version is unresolved (row C-NEW-KB-QMA1 is HOLD).
(e) *Novelty caution.* Cade–Crichigno, arXiv:2107.00011, *Quantum* 8, 1325 (2024),
DOI 10.22331/q-2024-04-30-1325, already formalise "N=2 SUSY local Hamiltonian, ground energy
zero iff a cohomology group is nontrivial", prove QMA-completeness, **and prove DQC1-hardness
of normalised Betti estimation on general cochain complexes** (O16). Crichigno,
arXiv:2011.01239 (arXiv only): the Witten index is #P-complete. The mechanism is not new; only
the algebro-geometric instance is. *Correction retained*: Gyurik–Cade–Dunjko, *Quantum* 6, 855
(2022), DOI 10.22331/q-2022-11-10-855, arXiv:2005.02607, prove DQC1-hardness of **low-lying
spectral density estimation**, not of normalised Betti estimation for clique complexes.
(f) *Trap audit, corrected.* Dense rank — avoided. Changing the output — a normalised
fraction, and r0 named the **wrong** normalisation; fixed. Hidden state preparation — **now
priced** (Step 9.2), previously missing. **Exponentially small overlap — TRIGGERED**, retracting
the r0 claim that it was not: `h_N/M_N ≈ rho^{codim}` (Step 9.3). Hiding exponential `N` —
inapplicable (KB2). Ignoring gap closing — triggered (K-KB6, now with a proved counterfamily).
Ignoring classical preconditioning — triggered (K-KB9).

**5. Heuristic attack — FAILS: at most a small monomial demonstration.** The full Koszul
Laplacian is the *free* Hamiltonian `N̂ + F̂` (Step 4.1); all content sits in `P_0`, which is
not an interaction, so the generic problem still needs a nonphysical projector. *Survives*, and
with a wording correction (O14): for a **monomial** ideal `H_N` is diagonal (C-111), `P_0` is a
computational-basis projector, and `L_W` is a sparse number-conserving hopping Hamiltonian on
the standard monomials tensored with a Jordan–Wigner fermion register on `n+1` sites. The
smallest demonstration is the Stanley–Reisner ideal of the 4-cycle, `I = (z_0z_2, z_1z_3)`,
block `(i=1,N=1)`: one boson in four modes — a **four-mode path (ququart) encoding, not a
dual-rail encoding** — plus one fermion in four modes, a 16-level two-particle problem with
zero-energy degeneracy `beta_{1,2} = 2`. The 7-cycle at `(i=3,N=1)` is 245-dimensional with
degeneracy 35 and normalised gap 0.146. Second survivor: the generator-Koszul supercharge of
Step 8, a genuine `max_j m_j`-body boson–fermion interaction with no projector whose `i=0`
block is exactly `H_N` (part f) — the only natively physical object this lane found, and it
computes Koszul homology of the sequence, not the Betti table.

**Lockstep line.** No PRD §2 criterion 1–5 is met. Two rows are on HOLD —
**C-NEW-KB-QMA1** (missing: a polynomial reduction preserving the total-block normalised gap
across all non-squarefree summands) and **C-NEW-KB-GAP-INDEPENDENT** (missing: a total-block
counterfamily, a specified positive class of forbidden lower bounds, and any reverse-direction
result) — two are REFUTED (C-NEW-KB-DEQUANT, C-NEW-KB-NO-FREE-LUNCH) and six are CONJECTURE.
§3, the killers K-KB1..K-KB12, the rows of §6 and the definitions of §5 state the same
qualifiers: the overlap obstruction is family-named (O21), the gap statement is quantified over
`phi(1) > 0` on the squarefree summand only (O20), the ambient observable is the harmonic
projector (O17), and every access mode is adjacent-degree (O18).

---

## 4. Killers

**K-KB1 (support collapse; F3).** `beta_{i,j} = 0` for `j-i > reg(R/I)` (Step 6, part a), so
the useful block label satisfies `N <= reg(R/I)`; the twisted cubic, the rational normal curves
and every determinantal example in the seed's survey have `reg(R/I) <= 2`. It does **not**
preclude large `N` when regularity grows: D-boolean-ideal / D-clause-ideal have
`reg(R/I) = Theta(n)` — and are exactly the #P-hard families. Severity high.

**K-KB2 (the naive compression is information-free).** `P̂ L P̂ = (N+i) P̂` exactly (Step 4.3,
part b): "block-encode the projected Koszul Laplacian" returns a scalar. `L_W` must be built
from `q^† = sum_k Z_k ⊗ c_k`. Severity decisive for how the operator is presented; see K-KB9
for what it costs, which is **not** unconditionally a QSVT per call (O11).

**K-KB3 (the squarefree part is quantum TDA; the rest is not).** Hochster plus part d: the
**squarefree multidegree summands** of `L_W` for a Stanley–Reisner ideal are simplicial
Laplacians of induced subcomplexes, so #P-hardness of exact evaluation and NP-hardness of
multiplicative approximation transfer unconditionally (arXiv:2209.14286), and the
Apers et al. estimator applies there. The **non-squarefree** part of the total block is covered
by no cited theorem (part d: 42 of 49, 105 of 147, 7 of 294 dimensions squarefree). Severity
decisive for the speedup, and the source of the HOLD on C-NEW-KB-QMA1.

**K-KB4 (novelty of the mechanism).** Cade–Crichigno arXiv:2107.00011 own the SUSY/cohomology
Hamiltonian framework *and* DQC1-hardness of normalised Betti estimation on general cochain
complexes; only the algebro-geometric instance is new here. Action: a C-110-style scout on
whether "graded Betti numbers = nullity of a Laplacian built from compressed multiplications on
the Macaulay inverse system" already exists (operator theory, C-015/C-017, or physics).
Severity medium.

**K-KB5 (the cheap blocks are input data).** `beta_{1,j}` counts minimal generators and
`beta_{1,2} = dim I_2` is a rank (Step 7.3, every family). The first genuinely non-input block
is `i = 2`, where the fraction is `~ n^{-4}` at fixed `c` (part g). Severity medium.

**K-KB6 (a constant Macaulay gap does not ensure a uniformly positive squarefree Betti gap).**
Stated with the quantifier the evidence supports (O20): *"The `m`-cycle family rules out any
uniform strictly positive lower bound on the selected squarefree-summand gap depending only on
`Delta_2`: no `phi` with `phi(1) > 0` satisfies `g_sq >= phi(Delta_2)` throughout this family.
No total-block or reverse comparison is established."* The proof is Step 5.6 (`Delta_2 = 1`
for every `m`; `g_sq = 2-2cos(2 pi/m)`), checked in part e for `m = 4..12`. It does **not** rule
out `phi(1) = 0`, does not concern the total-block `g_{i,N}` beyond the finite observations
`m <= 8`, and proves no reverse inequality. `g_{i,N}` is an invariant of the ideal and the Fock
metric, **not** presentation-dependent (O7); its *realisation cost* through `H_N` is what
depends on the tuple. No lower bound on `g` is known for any interesting class. Severity high:
the runtime carries `j/g`.

**K-KB7 (no hardware hook for `L_W`).** The full Koszul Laplacian is the *free* Hamiltonian
(Step 4.1). Survivors: the monomial-ideal ququart demonstration of §3.5 and the generator-Koszul
Hamiltonian of Step 8, now verified to have the seed `H_N` as its `i=0` block. Severity high
against PRD criterion 5.

**K-KB8 (output).** Only a normalised fraction is estimable; recovering `beta` needs
`eps < 1/(2 dim)`, which #P-hardness forbids anyway. Severity medium; same kind as C-091/C-093.

**K-KB9 (the access model decides the cost, it must span two degrees, and preconditioning is
symmetric).** The block is `L_W = q_{i,N}^† q_{i,N} + q_{i-1,N+1} q_{i-1,N+1}^†`, and the
incoming term contains `Q P_{0,N+1} Q^†`, so **access to `H_N` alone with a promise only on
`Delta_N/alpha_N` does not construct it** (O18): a small `Delta_{N+1}` defeats the
implementation, and part h shows that removing `P_{0,N+1}` outright collapses the block to
`j·1`. Generator mode therefore needs `H_N` *and* `H_{N+1}` with
`Delta_r/alpha_r >= 1/poly(n)` for every nontrivial required `r in {N,N+1}`, and the cost is an
adjacent-degree maximum `O(n · max_r alpha_r/Delta_r)`; quotient mode needs both `Z_{k,N}` and
`Z_{k,N+1}` and then no per-call QSVT at all (O11). Whichever access is granted must be granted
to the classical baseline too, and the residual `n log N` qubits versus `M_N` words is refused
as a space separation by PRD D15 / SP-0 (C-264). The arm should make no space claim.
Severity high.

**K-KB10 (regularity, downgraded).** `reg(I)` is worst-case doubly exponential (Mayr–Meyer;
Bayer–Mumford), but it is needed only to **enumerate** the Betti table, not to answer one
requested `(i,j)`; and `reg(R/I) = reg(I) - 1`. Severity downgraded from medium to minor (O1).

**K-KB11 (the conditional normalisation is the overlap wall — for a named family).** The
`W_N`-conditional fraction costs `M_N/h_N` samples or `sqrt(M_N/h_N)` coherent projections
(Step 9.2, C-096). The acceptance weight `h_N/M_N` is exponentially small for the
quadratic complete-intersection family at `N = n`, and potentially exponentially small in
general; equivalently, the rejection-sampling cost `M_N/h_N` and coherent-projection cost
`sqrt(M_N/h_N)` are exponentially large. The quadratic complete-intersection family is the
one in which the applications memo's `0.75^codim` law was measured (caution 1); explicitly,
`h_n = 2^n` and `M_n = C(2n,n)`, so `h_n/M_n ~ sqrt(pi n)/2^n` and
`M_n/h_n ~ 2^n/sqrt(pi n)` — at `n = 8` the checker's `h_n/M_n = 0.019891` is a cost of
`50.27`, not a small number. The acceptance weight is **not** exponentially small for every
square system, since `n` generic degree-`(n+1)` forms in `P^n` give `h_N/M_N = 1` at `N = n`
(part h, O21). The surviving statement is: *the acceptance weight can be exponentially small,
making conditional normalization exponentially expensive; no unconditional conditional-output
algorithm follows without a Hilbert-weight promise or preparation oracle.* Separately (O17), even the **ambient**
output
must be taken from the harmonic filter `L~ = L_W + j(1 - P̂_N)`, not from zero-extended `L_W`,
which has `(M_N - h_N)b` spurious zero modes. This is the r1 FATAL objection O2, corrected at
r2, turned into a killer; it supersedes the r0 claim that arm B escaped the overlap trap.
Severity decisive.

**K-KB12 (NEW at r1: the total-block gap is not a clique-complex gap).** `g_{i,N}` is a minimum
over every multidegree in the block, while every cited gapped-clique-homology theorem controls
one simplicial Laplacian (O5). Until the non-squarefree summands are bounded below, neither the
hardness transfer nor the dequantization transfer is licensed at the total-block level.
Severity decisive for C-NEW-KB-QMA1 and C-NEW-KB-DEQUANT.

Ranking before arm B is worth a prover seat:
**K-KB11 > K-KB6 > K-KB12 > K-KB3 > K-KB9 > K-KB1 > K-KB7 > K-KB4 > K-KB5 > K-KB2 > K-KB8 > K-KB10.**

---

## 5. Proposed definitions

Ids proposed; **none is yet a registered heading in `definitions/definitions.md`**, and a merge
must register these before any `C-NEW-KB-*` row that cites them (O13). Rewordings follow the
critic's "Proposed definitions adjudication".

- **D-fermionic-modes** (ACCEPTED unchanged). `c_k, c_k^†` (`k = 0..n`) on `Lambda(C^{n+1})`
  with `{c_k, c_l^†} = delta_{kl}`; basis `|S>`, `S ⊆ {0..n}`;
  `c_k^†|S> = (-1)^{#{l in S : l<k}}|S ∪ {k}>` for `k not in S`, else 0; `F̂ = sum_k c_k^† c_k`.
  Pitfall: dropping the sign breaks `Q^2 = 0` (mutation M3, run in-process).
- **D-koszul-supercharge** (REWORDED per O10/O12). On the **finite-particle core** `R ⊗ Λ` of
  `F ⊗ Lambda(C^{n+1})`, `Q = sum_k a_k ⊗ c_k^†` (D-mode-operators, D-fermionic-modes);
  `Q^2 = 0` exactly; `Q` maps block `(i,N)` to `(i+1,N-1)` and preserves `j = N+i`. With
  `P = ⊕_N P_{0,N}` the **degreewise direct-sum** ground-space projector and `P̂ = P ⊗ 1`, the
  restriction `q = Q P̂ = P̂ Q P̂` is well defined because `W` is `a_k`-invariant. Under the
  conjugate-linear Fock pairing `(W ⊗ Lambda, q)` is the **conjugate dual** of the Koszul
  complex of `R/I` on the variables. Pitfall: `Q^†` does not restrict; its restriction is
  `sum_k Z_k ⊗ c_k` (D-compressed-multiplication). `a_k, Q, L` are unbounded on the completion.
- **D-betti-laplacian** (REWORDED). Globally on `W ⊗ Lambda`, `L_W = q q^† + q^† q`, which
  preserves each internal-degree sector `j` and each block `(i,N)`, `N + i = j`. On a fixed `j`
  sector, `L_W = j P̂ - X X^†` with `X = P̂ Q (1 - P̂)`; hence `0 <= L_W <= j P̂` and
  `||L_W|| <= j`. A block may have `L_W|(i,N) = 0` (no positive spectrum); such a block admits
  no gap and no gap promise. Pitfall: `L_W != P̂ L P̂`, which is the scalar `j P̂`.
- **D-graded-betti-number** (REWORDED per O1/O9). `beta_{i,j}(R/I) = dim Tor_i^R(R/I,C)_j`;
  `beta_{i,j} = 0` for `i > n+1` and for `j - i > reg(R/I)`, where
  `reg(R/I) = max{j-i : beta_{i,j} != 0}` and `reg(I) = reg(R/I) + 1` for a nonzero proper
  homogeneous ideal. `beta_{1,j}` counts minimal generators of `I` in degree `j`; `beta_{2,j}`
  counts the degree-`j` minimal relations **in a minimal free resolution**, equivalently among
  a **minimal homogeneous presentation** — the quotient `Syz/m Syz` of an arbitrary tuple's
  syzygy module is *not* `beta_2` (counterexample `(x,x)`). `Syz(I)_N` (D-syzygy-module) is a
  tuple invariant, not a Betti number.
- **D-betti-gap** — **REWORDED at r2; the critic's D5, copied verbatim:**
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
- **D-normalised-betti-fraction** — **REWORDED at r2; the critic's D6, copied verbatim:**
  > Let \(M_N=\dim R_N\), \(h_N=\mathrm{HF}_{R/I}(N)\), and
  > \(b=\binom{n+1}{i}\). The ambient normalized Betti fraction is
  > \(\beta_{i,i+N}/(M_Nb)\). It equals the normalized trace of the harmonic
  > projector on \(W_N\otimes\Lambda^i\) extended by zero to
  > \(R_N\otimes\Lambda^i\); it is not the zero-eigenvalue fraction of \(L_W\)
  > extended by zero. When \(h_N>0\), the conditional fraction is
  > \(\beta_{i,i+N}/(h_Nb)\). Estimating the conditional ratio requires normalized
  > access to \(W_N\), with ambient acceptance weight \(h_N/M_N\), or an explicit
  > preparation oracle.
- **D-generator-koszul-supercharge** (REWORDED). For positive-degree homogeneous
  `f_1,...,f_d`, `Q_f = sum_j M_{f_j} ⊗ c_j` with **fermionic annihilators** `c_j` on
  `Lambda(C^d)`, fermion `j` carrying internal weight `deg f_j` (a weighted internal grading).
  On the finite-particle core `Q_f^2 = 0`; the fermion-number-zero Laplacian block is
  `sum_j M_{f_j} M_{f_j}^† = H` (D-hamiltonian). Only the **zero-mode dimensions** of the higher
  blocks compute `H_i(f;R) ≅ Tor_i^{C[y_1..y_d]}(C,R)`, and all positive homology vanishes iff
  the positive-degree sequence is regular. Pitfall: these are not `beta_{i,j}(R/I)`.
- **D-betti-estimation-problem** — REJECTED at r1 and resubmitted; the r1 resubmission still
  carried unused thresholds, a missing `eps` input and a contradictory regularity promise (O22),
  and omitted adjacent-degree access (O18). **REWORDED at r2; the critic's D8, copied
  verbatim:**
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

---

## 6. Proposed claim rows

Ten rows, unchanged in status by the r2 adjudication. Six carry the critic's r1 reworded
statement **verbatim** (quoted, notation as written in `verdicts/koszul-betti-r1.md`) and were
ACCEPTED AS CONJECTURE at r2; two are HOLD with the r2 missing steps named; two were ACCEPTED
AS REFUTED at r2 and carry the r2 surviving statements verbatim. All non-REFUTED rows are **CONJECTURE** per
L1. `where-tested` is `checkers/explore/koszul_laplacian.py`. Dependencies on `D-` ids are
provisional until those entries are registered (O13).

**C-NEW-KB-HODGE — CONJECTURE.** Statement, verbatim from the verdict:
> "For every homogeneous ideal \(I\subseteq R\), let \(W_N=I_N^\perp\), \(W=\bigoplus_NW_N\),
> \(P=\bigoplus_NP_{0,N}\), and \(q=QP=PQP\) on the finite-degree subspace. For
> \(0\le i\le n+1\), \(N\ge0\), and \(j=N+i\),
> \(\dim\ker(qq^\dagger+q^\dagger q)|_{W_N\otimes\Lambda^i}=\beta_{i,j}(R/I)\). Under the Fock
> pairing this harmonic space is conjugate-linearly dual to \(H_i(K(z;R/I))_j\)."

depends-on: D-koszul-supercharge, D-betti-laplacian, D-graded-betti-number, D-inverse-system,
D-compressed-multiplication, C-008, C-012, C-014. where-proved: §1 Steps 1–3. where-tested:
part A, six ideals, every block, against GF(p) Koszul ranks and literature fixtures.
Relevance/traps: the whole arm; guards against the index slip (M2) and the linear-duality slip.

**C-NEW-KB-FREE — CONJECTURE.** Statement, verbatim:
> "On the finite-particle core, \(QQ^\dagger+Q^\dagger Q=\hat N+\hat F\). For every homogeneous
> \(I\), every \(i,N\), and \(j=N+i\), \(PLP=jP\), while \(L_W=jP-PQ(1-P)Q^\dagger P\); hence
> \(0\le L_W\le jP\) and \(\|L_W\|\le j\)."

depends-on: D-koszul-supercharge, D-betti-laplacian, D-projectors,
D-block-encoding-normalisation. where-proved: §1 Step 4. where-tested: part B, with `X`
constructed (`7.1e-15`), `P̂LP̂ - jP̂` at `4.4e-15`. Relevance/traps: fixes what must be
encoded (K-KB2); does **not** by itself price the algorithm (see K-KB9).

**C-NEW-KB-SUPPORT — CONJECTURE.** Statement, verbatim:
> "For every homogeneous proper ideal \(I\), \(\beta_{i,j}(R/I)=0\) when
> \(j-i>\operatorname{reg}(R/I)\); equivalently the block \((i,N)\) has zero harmonic nullity
> for \(N>\operatorname{reg}(R/I)\). This does not preclude large \(N\) when regularity itself
> grows."

depends-on: C-NEW-KB-HODGE, D-saturation-regularity-stable-range. where-proved: §1 Step 6.
where-tested: part A, prediction checked to `N = 8,7,7,6,5,4` against `reg(R/I) = 1,2,2,1,1,2`.
Relevance/traps: K-KB1, F3; guards against the `j <= reg` slip (O1).

**C-NEW-KB-HOCHSTER — CONJECTURE.** Statement, verbatim:
> "For a Stanley–Reisner ideal, the squarefree multidegree-\(\sigma\) summand of \(L_W\) in
> block \(i,N\), \(|\sigma|=i+N\), is unitarily the reduced \((N-1)\)-chain Laplacian of
> \(\Delta|_\sigma\). Consequently \(\beta_{i,i+N}=\sum_{|\sigma|=i+N}\dim\widetilde
> H_{N-1}(\Delta|_\sigma;\mathbb C)\). No total-block gap or dequantization conclusion is
> included."

depends-on: C-NEW-KB-HODGE, D-monomial-ideal, D-graded-betti-number. where-proved: Hochster
1977 / Miller–Sturmfels GTM 227 Cor. 5.12 (DOI 10.1007/b138602) composed with §1 Step 3.3.
where-tested: part D, `m`-cycles `m = 4..7`, with the squarefree dimension printed against the
total block dimension. Relevance/traps: K-KB3, K-KB12.

**C-NEW-KB-QMA1 — HOLD** (r2 decision unchanged). *Missing step, in the critic's r2 words*: "a
polynomial reduction preserving the total-block normalized gap across all non-squarefree
summands." The King–Kohler gapped theorem is for weighted clique complexes
while C1's Fock metric gives the unweighted block; the Hayakawa unweighted gapped theorem
controls one clique Laplacian, whereas `g_{i,N}` is a minimum over every multidegree summand,
and Hochster preserves nullity, not that gap. What is claimable now, and what the row is
narrowed to pending that step:
> "Exact \(\beta_{i,j}\) evaluation is #P-hard and multiplicative approximation is NP-hard;
> unweighted gapped clique homology transfers to a squarefree multidegree version of the
> Betti-Laplacian problem."

depends-on: C-NEW-KB-HOCHSTER, D-hardness-anchors, C-091, C-092. where-proved: cited literature
(arXiv:2209.14286; arXiv:2608.02726; arXiv:2311.17234, DOI 10.1109/FOCS61266.2024.00039;
arXiv:2209.11793, DOI 10.1038/s41467-024-54118-z). where-tested: none — the reduction's degree
and multidegree bookkeeping is not checked numerically. Relevance/traps: QMA_1-hardness
excludes a BQP algorithm only under `QMA_1 ⊄ BQP`.

**C-NEW-KB-DEQUANT — REFUTED at r1.** The r0 statement claimed that at `gamma = Omega(1)` no
super-polynomial advantage exists and that the only surviving window is `gamma = 1/poly(n)`.
Refuted on two counts: the quoted bound at `gamma = Omega(1)`, `eps = 1/poly(n)` is
`n^{O(log n)}`, quasi-polynomial rather than polynomial, so a super-polynomial separation
remains permitted; and the theorem does not automatically apply to a generic projected `L_W`,
whose sparse row access from the generators was never constructed. ACCEPTED AS REFUTED at r2;
surviving statements, verbatim from `verdicts/koszul-betti-r2.md`:
> "At constant normalized gap and constant additive error, the cited simplicial-complex
> estimator is polynomial-time classical."
and
> "Apers et al. directly apply to the squarefree multidegree summands explicitly identified with
> ordinary simplicial Laplacians."

depends-on: C-NEW-KB-HOCHSTER, D-betti-gap, D-normalised-betti-fraction, C-100. where-proved:
cited literature (arXiv:2211.09618, DOI 10.22331/q-2023-12-06-1202; arXiv:2209.13581,
DOI 10.1103/PRXQuantum.5.010319). where-tested: none. Kept forever per L1.

**C-NEW-KB-GAP-INDEPENDENT — HOLD** (r2 decision unchanged), with the missing step partly
supplied at r1. *Missing steps, in the critic's r2 words*: "a total-block counterfamily, a
specified positive class of forbidden lower bounds, and any reverse-direction result." The r0
statement ("no function relates `g_{i,N}` and `Delta_N`") is not established by two finite
tables, and its premise that `g` is presentation-dependent was wrong: `g_{i,N}` is an invariant
of the ideal and the Fock metric. What r1 supplies is a **proved infinite counterfamily to one
direction**:
for the `m`-cycle Stanley–Reisner ideal, `m >= 4`, `Delta_2 = 1` for every `m`, while the
squarefree-`sigma` summand (`sigma` = all `m` vertices) of block `(i = m-2, N = 2)` is unitarily
the edge Laplacian `∂_1^† ∂_1` of `C_m`, with nullity 1 and smallest nonzero eigenvalue exactly
`2 - 2cos(2 pi/m)`. With the quantifier the evidence supports (O20), that rules out any uniform
strictly positive lower bound on the selected squarefree-summand gap depending only on
`Delta_2` — no `phi` with `phi(1) > 0` satisfies `g_sq >= phi(Delta_2)` throughout this family —
and nothing more. *Still missing, hence HOLD*: (i) a **total-block** counterfamily (numerically
the two gaps coincide for `m <= 8`, unproved in general); (ii) a specified positive class of
forbidden lower bounds (in particular `phi(1) = 0` is not excluded); (iii) any
reverse-direction result. Surviving statement, verbatim from the verdict:
> "No comparison between \(g_{i,N}\) and the tuple-dependent \(\Delta_N\) follows from the
> construction; the reported finite spectra show markedly different behavior."

depends-on: D-betti-gap, D-macaulay-gap, C-052, C-103. where-proved: §1 Step 5.6 for the
squarefree summand. where-tested: part E, `m = 4..12` against the closed form, `m <= 8` for the
total block. Relevance/traps: K-KB6.

**C-NEW-KB-FRACTION — CONJECTURE.** Statement, verbatim:
> "For a complete intersection of \(1\le c\le n+1\) quadrics and \(0\le i\le c\), the block
> \((i,i)\) has \(\beta_{i,2i}=\binom ci\) and fraction \(\binom ci/(\mathrm{HF}(i)\binom{n+1}
> {i})\). For fixed \(c,i\) and \(n\to\infty\), this is asymptotic to \(\binom ci(i!)^2n^{-2i}\).
> This scaling alone implies no quantum advantage because the corresponding block dimension is
> polynomial for fixed \(i\)."

depends-on: D-normalised-betti-fraction, C-062. where-proved: Koszul resolution plus the
closed-form Hilbert series. where-tested: part g, with block dimensions printed, plus the
`i = n` Boolean row (`fraction = 1/(2^n(n+1))`). Relevance/traps: retracts the r0 "survives F2"
claim (O6); see K-KB11 for the `h_N/M_N` half.

**C-NEW-KB-SEED-IS-A-BLOCK — CONJECTURE.** Statement, verbatim:
> "For positive-degree homogeneous \(f_1,\ldots,f_d\), define \(Q_f=\sum_jM_{f_j}\otimes c_j\)
> with fermionic annihilators \(c_j\), assigning fermion \(j\) weight \(\deg f_j\). Then
> \(Q_f^2=0\); its fermion-number-zero Laplacian block is \(\sum_jM_{f_j}M_{f_j}^\dagger=H\).
> Its zero modes in higher blocks are \(H_i(f;R)\cong\operatorname{Tor}^{\mathbb C[y_1,\ldots,
> y_d]}_i(\mathbb C,R)\), and all positive homology vanishes iff the positive-degree sequence is
> regular."

depends-on: D-generator-koszul-supercharge, D-hamiltonian, D-k-body, C-008. where-proved: §1
Step 8. where-tested: part f — `|L^{gen}_{i=0} - H_N| = 0` for `N = 2..5` on the twisted cubic,
and the two nullity tables differ. Relevance/traps: the only projector-free boson–fermion
Hamiltonian this lane found (K-KB7).

**C-NEW-KB-NO-FREE-LUNCH — REFUTED at r1.** The r0 statement ("every evaluation of `L_W`
requires `P_0`, so arm B's cost is at least arm A's, at
`Õ(n (alpha_BE/Delta_N)((N+i)/g_{i,N}))` per application") is refuted on three counts: direct
standard-monomial access (monomial ideals) or a supplied quotient-multiplication oracle avoids
any per-call `P_0`; `j/g` is a count of spectral-filtering repetitions, not a per-application
factor; and the quoted cost omits the `M_N/HF(N)` normalisation of O2. ACCEPTED AS REFUTED at
r2; surviving statement, verbatim from `verdicts/koszul-betti-r2.md`:
> "If the only available quotient access is obtained by QSVT from \(H_N\), constructing a call
> to \(L_W\) inherits dependence on \(\alpha_{\mathrm{BE}}/\Delta_N\), with the required
> adjacent-degree gaps included."
The corrected cost accounting is Step 9.4–9.5, and the surviving cost obstruction is now carried
by **K-KB11** (the `M_N/HF(N)` weight), not by a universal `P_0` claim.

depends-on: C-NEW-KB-FREE, C-055, C-056, C-058, C-096, D-qsvt. where-proved: §1 Step 9.
where-tested: none. Kept forever per L1.

---

## 7. Questions for TJO

1. **Is a conditional hardness anchor a product?** After r1 the sharpest claimable item is
   narrower than r0 said: #P-hardness of exact `beta_{i,j}` and NP-hardness of multiplicative
   approximation transfer unconditionally through Hochster, but the QMA_1 transfer holds only
   for a *squarefree-multidegree* version of the problem (C-NEW-KB-QMA1, HOLD). Does a
   restricted hardness statement of that shape count as a deliverable? Same question as PRD §7
   Q4, now sharpened.
2. **Fund the two cheap missing steps, or close the arm?** (a) Bound the non-squarefree
   multidegree summands of a total block from below — this single lemma would convert both
   HOLD rows, since it would also give the total-block counterfamily and the forbidden-bound
   class that C-NEW-KB-GAP-INDEPENDENT still lacks. (b) A lower bound on `g_{i,N}/(N+i)` for a
   named class. Estimated one analytic week each; without (a) neither the hardness transfer nor
   the dequantization transfer is licensed at the total-block level.
3. **Arm B versus arm A ordering, revised.** r0 said "arm B strictly contains arm A in cost";
   that was refuted (O11). The correct statement is access-model-dependent: with a
   quotient-multiplication oracle **at both adjacent degrees** arm B is *cheaper* per call than
   arm A, and with generator access it needs `H_N` and `H_{N+1}` and good gaps at both (O18).
   Does the campaign want to grant a two-degree quotient oracle as an input model anywhere? That
   decision, not the mathematics, decides where arm B sits.
4. **The other supercharge (Step 8), now tested.** `Q_f = sum_j M_{f_j} ⊗ c_j` is a genuine
   `m`-body boson–fermion Hamiltonian whose `i=0` block is *exactly* the seed's `H_N` (verified
   to machine zero) and whose higher blocks measure failure of the complete-intersection
   property. It has the hardware hook the Betti Laplacian lacks. One-day probe, or leave?
5. **Literature scout (K-KB4).** Cade–Crichigno own the SUSY/cohomology framework *and*
   DQC1-hardness of normalised Betti estimation on general cochain complexes. Before anything
   else: does "graded Betti numbers = nullity of a Laplacian built from compressed
   multiplications on the Macaulay inverse system" already exist? Run with C-110.
6. **Reference and citation corrections to merge** (all fetched, all confirmed by the critic's
   independent audit): classical memo [R31] is **Neiger & Schost**, two authors, arXiv:1912.01848;
   Gyurik–Cade–Dunjko prove DQC1-hardness of **LLSD**, not of normalised Betti estimation;
   Hochster 1977 has **no DOI** (cite Miller–Sturmfels GTM 227, DOI 10.1007/b138602); and this
   memo's r0 citation of **Fact 7.1 as C-107 was wrong — it is C-103**.
7. **Merge ordering (O13).** None of the seven `D-` ids exists yet in
   `definitions/definitions.md`, and the `C-NEW-KB-*` ids are provisional. Register the
   definitions first, then assign real C-ids, then merge the rows.
8. **`MUTATIONS.md` residue.** M1–M4 now run in-process and are red, but this lane may not edit
   `checkers/MUTATIONS.md`. Who registers them?

---

## 8. Repair r1 response

Verdict `verdicts/koszul-betti-r1.md`: FAIL(O1, O2, O3, O4, O5, O6, O7, O8, O9, O11, O13, O14),
O2 FATAL, eleven MAJOR, two MINOR, two NOTE. Every objection is dispositioned.

| objection | severity | disposition | location of the edit | note |
|---|---|---|---|---|
| O1 | MAJOR | FIXED | §1 Step 6; §3.1; D-graded-betti-number, D-betti-estimation-problem (P1); K-KB10; part-A print | Support condition is now `N = j-i <= reg(R/I)`; `reg(I) = reg(R/I)+1` stated; `HF(N)>0` and a non-vanishing block required; regularity needed only to enumerate the table, so K-KB10 downgraded. |
| O2 | **FATAL** | FIXED | §1 Step 9 (new, 6 sub-steps); §3.3, §3.4(f); K-KB11 (new); D-normalised-betti-fraction; D-betti-estimation-problem (P5); C-NEW-KB-NO-FREE-LUNCH | Ambient versus `W_N`-conditional fraction separated; conversion priced at `M_N/h_N` samples or `sqrt(M_N/h_N)` coherent projections (C-096) or an assumed preparation oracle; promise `h_N/M_N >= 1/poly(n)` added; the r0 "overlap trap not triggered" line retracted. |
| O3 | MAJOR | RETRACTED | §3.4(a); C-NEW-KB-DEQUANT (now REFUTED); K-KB3 | `n^{O(gamma^{-1/2} log(1/eps))}` is polynomial only at constant `eps`; at `eps = 1/poly(n)` it is `n^{O(log n)}`, so a super-polynomial separation stays permitted. Both r0 sentences withdrawn. |
| O4 | MAJOR | FIXED | §1 Step 5.5; §2 part d (`sqfree` column, new); §3.4(b); C-NEW-KB-HOCHSTER, C-NEW-KB-DEQUANT; K-KB12 (new) | Only the squarefree multidegree summands are simplicial Laplacians; the access-model hypothesis of Apers et al. is stated and the sparse-row oracle for a generic `L_W` is acknowledged as unconstructed. |
| O5 | MAJOR | DOWNGRADED | §3.4(d); C-NEW-KB-QMA1 (HOLD); K-KB12 | Gap preservation is no longer claimed; hardness is stated for the squarefree-multidegree version, weighted-vs-unweighted distinguished, and `QMA_1 ⊄ BQP` conditionality noted. |
| O6 | MAJOR | FIXED | §2 part g (block dimensions printed, `i=n` row added); C-NEW-KB-FRACTION (critic's wording verbatim); K-KB5 | Regimes for `c` and `i` stated separately; the "arm B survives F2" claim retracted; polynomial block dimension at fixed `i` recorded in the row. |
| O7 | MAJOR | FIXED + partly supplied | §1 Steps 5.4, 5.6; §2 part e (new); D-betti-gap; C-NEW-KB-GAP-INDEPENDENT (HOLD); K-KB6 | "Presentation-dependent" withdrawn (`g` is ideal- and metric-dependent). A **proved** infinite counterfamily added: `m`-cycle, `Delta_2 = 1` versus squarefree gap `2-2cos(2 pi/m)`, verified `m = 4..12`. |
| O8 | MAJOR | FIXED | §1 Step 5.3; §2 part c (new O8 check, max deviation 2.1e-14) | Replaced by the per-differential singular-value pairing; the false adjacent-block claim removed and the critic's counterexample (`g(0,3)=3` vs `g(1,2)=4/3`) printed. |
| O9 | MAJOR | FIXED | §1 Step 7.2; D-graded-betti-number | `beta_2` restricted to a minimal free resolution / minimal presentation; the `(x,x)` counterexample recorded. |
| O10 | MINOR | FIXED | §1 preamble; Step 3.2; D-koszul-supercharge; C-NEW-KB-HODGE (verbatim) | Conjugate-linear duality and Hilbert adjoints; all full-Fock identities asserted on the finite-particle core with closures understood. |
| O11 | MAJOR | RETRACTED | §1 Step 9.4; §3.3; K-KB2 and K-KB9 (split); C-NEW-KB-NO-FREE-LUNCH (REFUTED) | "Every evaluation requires `P_0`" is false under quotient access; per-call cost separated from `O((j/g)log(1/eps))` filtering repetitions; the normalisation cost of O2 added. |
| O12 | MINOR | FIXED (one RESIDUE) | `checkers/explore/koszul_laplacian.py` docstring, `FIXTURES`, `X_block`, `nullity_and_gap`, `mutations()`; §2 preamble | Literature fixture tables added (so a fixture mutation is now caught); `X` constructed, not inferred; `abs(ev)<TOL` plus separate PSD test; M1–M4 run in-process, M4 driven by part f; GF(p) labelled by characteristic. **RESIDUE**: registering M1–M4 in `checkers/MUTATIONS.md` is outside this lane's writable set. |
| O13 | MAJOR | FIXED | Status header; §5 preamble; §6 preamble; §7 Q7; Fact 7.1 citation in Step 5.4 and K-KB6 | "Theorem", "settled" and "product" language removed; all rows explicitly conjectural; unregistered `D-` ids and provisional `C-NEW` ids flagged with a merge order; **C-107 corrected to C-103**. |
| O14 | MAJOR | FIXED | §3 rewritten: every criterion now opens "FAILS" with the surviving statement | None of PRD §2 criteria 1–5 is met; the ququart-vs-dual-rail wording corrected in §3.5; the memo is recast as a conditional dictionary identification plus a hardness probe. |
| O15 | NOTE | FIXED (retained) | §1 Steps 1–4, 6, with the O10 corrections applied | Core finite-dimensional mathematics retained as the critic confirms it, with conjugate-dual and operator-domain wording. |
| O16 | NOTE | FIXED | §3.4(a)–(e); §7 Q6 | Identifiers preserved; theorem applications rewritten to the exact access models, weights and gaps; Cade–Crichigno's DQC1-hardness for general cochain complexes added to the novelty caution. |

Dispositions over all 16 objections: FIXED 13 (O1, O2, O4, O6, O7, O8, O9, O10, O12, O13,
O14, O15, O16), RETRACTED 2 (O3, O11), DOWNGRADED 1 (O5); one RESIDUE inside O12 (registering
M1-M4 in `checkers/MUTATIONS.md`, outside this lane's writable set).

Rows after repair: 10 (CONJECTURE 6, REFUTED 2, HOLD 2, deleted 0).
Definitions after repair: 8 (accepted unchanged 1, reworded 6, rejected-and-resubmitted 1,
deleted 0).

---

## 9. Repair r2 response

Verdict `verdicts/koszul-betti-r2.md`: FAIL(O17, O18, O20, O21), four MAJOR plus O19 and O22
MINOR. Of the sixteen r1 objections the critic marks eleven VERIFIED and five NOT VERIFIED
(O1 via O22, O2 via O17/O18/O21, O6 via O19, O7 via O20, O11 via O18, plus the standing O12
`MUTATIONS.md` residue). All ten rows keep their r1 status; every definition is ACCEPT except
three, replaced below by the critic's D5, D6 and D8 **copied verbatim**.

| objection | severity | disposition | location of the edit | note |
|---|---|---|---|---|
| O17 | MAJOR | FIXED | §1 Step 9.1 (rewritten); status header bullet (ii); §2 part h (new); §3 criterion 3(b); K-KB11; D-normalised-betti-fraction (= D6 verbatim); D-betti-estimation-problem (= D8 verbatim) | The ambient fraction is the normalised trace of the **harmonic** projector extended by zero, reached by filtering `L~ = L_W + (N+i)(1 - P̂_N)`; zero-extended `L_W` has `(M_N-h_N)b` spurious zero modes. Part h reproduces the critic's 5-cycle instance exactly: `null(0-ext) = 51`, `null(Ltilde) = 1`, `1/150 = 0.006667` against `51/150 = 0.34`. The extra projector use is priced in Step 9.5. |
| O18 | MAJOR | FIXED | §1 Steps 9.4–9.5 (rewritten); §2 part h (last column); §3 criteria 1, 2, 3(c); K-KB9 (rewritten); D-betti-estimation-problem (= D8 verbatim); C-NEW-KB-NO-FREE-LUNCH surviving statement; §7 Q3 | The incoming term contains `Q P_{0,N+1} Q^†`, so generator mode must supply `H_N` **and** `H_{N+1}` with `Delta_r/alpha_r >= 1/poly(n)` for every nontrivial required `r in {N,N+1}`, and quotient mode both `Z_{k,N}` and `Z_{k,N+1}`. `O(n alpha_BE/Delta_N)` replaced by the adjacent-degree maximum. Part h shows the failure is total, not gradual: dropping `P_{0,N+1}` gives `q^†q + (jP̂ - q^†q) = j·1`, nullity `0` instead of `beta`, in every block tested. |
| O19 | MINOR | FIXED | `checkers/explore/koszul_laplacian.py` `ci_fraction_table()` (independent Hilbert-series and Pascal recomputation, `check` column); §2 part g table | The r1 memo printed `23730` and `886445` for `n = 20, c = 5`; the correct dimensions are `47460` and `2215780`. The table is now pasted from the script, which recomputes every dimension by a second route and prints OK/MISMATCH. |
| O20 | MAJOR | DOWNGRADED | §1 Step 5.6 (critic's sentence quoted); K-KB6 (rewritten); D-betti-gap (= D5 verbatim); C-NEW-KB-GAP-INDEPENDENT (missing steps in the critic's r2 words) | The categorical "no lower bound `g >= phi(Delta_N)` exists" is replaced everywhere by: the `m`-cycle family rules out any uniform strictly positive lower bound on the **selected squarefree-summand** gap depending only on `Delta_2`, i.e. no `phi` with `phi(1) > 0`; `phi(1) = 0` is not excluded, no total-block comparison and no reverse inequality is established. |
| O21 | MAJOR | DOWNGRADED | Status header bullet (ii); §1 Step 9.3 (rewritten); §2 part h (second table, new); §3 criterion 3(a); K-KB11 (rewritten) | "Exponentially small for every square system" is replaced by "exponentially small for the quadratic complete-intersection family at `N = n`, and potentially exponentially small in general". The script now prints the critic's counterfamily: `n` generic degree-`(n+1)` forms in `P^n` give `h_n/M_n = 1` at `N = n` for `n = 2,3,4,8`, against `0.667, 0.400, 0.229, 0.020` for the quadric family. The explicit `h_N/M_N` promise is preserved. |
| O22 | MINOR | FIXED | D-betti-estimation-problem (replaced by D8 verbatim); §3 criterion 1 | The unused thresholds `a < b` are gone, `eps` is an input, and the optional regularity bound no longer appears among the promises of the single-block decision problem — it is metadata used only when enumerating the whole table. |

Standing residue, unchanged and outside this lane's writable files: M1–M4 run in-process and are
red but are still absent from `checkers/MUTATIONS.md` (r1 O12; the r2 verdict records this as
NOT VERIFIED). Registering them is a merge action; §7 Q8 asks who does it.

Dispositions over the six r2 objections: FIXED 4 (O17, O18, O19, O22), DOWNGRADED 2 (O20, O21),
RETRACTED 0; one standing RESIDUE carried from r1 O12.

Rows after repair: 10 (CONJECTURE 6, REFUTED 2, HOLD 2, deleted 0) — unchanged from r1, as the
r2 rows decision requires.
Definitions after repair: 8 (ACCEPT 5 — D-fermionic-modes, D-koszul-supercharge,
D-betti-laplacian, D-graded-betti-number, D-generator-koszul-supercharge; REWORDED verbatim at
r2 3 — D-betti-gap = D5, D-normalised-betti-fraction = D6, D-betti-estimation-problem = D8;
deleted 0).

---

## 10. Repair r3 response

Verdict `verdicts/koszul-betti-r3.md`: FAIL(O23), one MAJOR. Of the six r2 objections the critic
marks five VERIFIED (O17, O18, O19, O20, O22) and one NEW DEFECT inside O21, raised as O23. The
exact-text audit passed on all seven required strings (D5, D6, D8, both HOLD missing-step
sentences, both DEQUANT surviving statements, the NO-FREE-LUNCH surviving statement), and every
row and definition is accepted. **No row and no definition is edited at r3.**

| objection | severity | disposition | location of the edit | note |
|---|---|---|---|---|
| O23 | MAJOR | FIXED | status summary bullet (ii); §3 criterion 3(a); K-KB11; plus §1 Step 9.3's closing sentence, aligned to the r3 surviving statement | Three passages named the costs `M_N/h_N` and `sqrt(M_N/h_N)` and then called "that factor" exponentially small. The direction is reversed: for `n` quadrics in `P^n` at `N = n`, `h_n = 2^n` and `M_n = C(2n,n)`, so `h_n/M_n ~ sqrt(pi n)/2^n` is exponentially small while `M_n/h_n ~ 2^n/sqrt(pi n)` and its square root are exponentially **large** — at `n = 8` the checker's `h_n/M_n = 0.019891` is a cost of `50.27`. Each passage now carries the FIX DEMAND sentence verbatim: "The acceptance weight `h_N/M_N` is exponentially small for the quadratic complete-intersection family at `N = n`, and potentially exponentially small in general; equivalently, the rejection-sampling cost `M_N/h_N` and coherent-projection cost `sqrt(M_N/h_N)` are exponentially large." Step 9.3 already had the direction right (the critic confirms); its closing sentence is nevertheless brought into lockstep with the r3 surviving statement, "the acceptance weight can be exponentially small, making conditional normalization exponentially expensive; no unconditional conditional-output algorithm follows without a Hilbert-weight promise or preparation oracle." |

Whole-memo sweep for the same error: the remaining occurrences of "exponentially small" are
§1 Step 9.3 (the acceptance weight `h_N/M_N`, direction correct), §2 part g (the normalised
Betti *fraction* `1/(2^n(n+1))`, not a cost), and the §9 r2-response row for O21, whose quoted
phrases are the historical record of the r2 edit and refer to the acceptance weight; that audit
trail is left intact, and O23 corrects the three summaries it produced. No other sentence in the
memo calls a cost exponentially small.

Dispositions over the single r3 objection: FIXED 1 (O23), RETRACTED 0, DOWNGRADED 0; the
standing r1 O12 residue (M1–M4 red in-process but not registered in `checkers/MUTATIONS.md`,
outside this lane's writable files) is unchanged.

Rows after repair: 10 (CONJECTURE 6, REFUTED 2, HOLD 2, deleted 0) — unchanged, and no row text
was edited at r3.
Definitions after repair: 8 (ACCEPT 5, REWORDED verbatim at r2 3, deleted 0) — unchanged, and no
definition text was edited at r3.
