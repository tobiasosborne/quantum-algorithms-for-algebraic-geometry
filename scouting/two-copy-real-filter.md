# The two-copy real-symmetry filter

Lane: two-copy real filter, PRD D14 (TJO question 2026-09-02, "About real QM: do we simulate it via
two copies to ensure real symmetry?"). Date: 2026-09-02. Status: scouting only; nothing ratcheted;
every proposed row is CONJECTURE per L1.

Conventions C1-C12 are binding; objects are D-fock-space, D-fock-basis, D-hamiltonian,
D-ground-space, D-coherent-state, D-coherent-gram-matrix, D-projectors, D-real-structure,
D-real-locus-and-real-radical, D-real-coherent-span, D-takagi-factorisation, D-hermite-trace-form.
**Departure from C5**, as in the whole checker suite: the numerics take generators as written, not
unit Bombieri-Weyl. Nothing here depends on that: every reported quantity is a ratio, a projector or
a Hilbert-function count, invariant under rescaling generators (D-norm-comparison). `D` is used only
for a zero-dimensional quotient dimension (C8), `p` only for a coherent-state label (C11), `tau_i`
only for Takagi / principal-angle values (C9).

## Bottom line

The two-copy trick is exact, and it does not do what the working answer hoped.

1. Realness **is** linear on two copies: `SWAP^{T_2} = |Phi_N><Phi_N|` exactly, and the acceptance
   probability of the pairing measurement on `psi x psi` is `R(psi)/M_N` with
   `R(psi) = |psi^T psi|^2/<psi|psi>^2`. C-256 (no one-copy projector onto `Fix(K)`) is circumvented
   as an arithmetic matter.
2. But the compression of that operator onto `ker H_N x ker H_N` has **rank one**, with eigenvalue
   `HF_{R/I}(N)/M_N` -- the normalised Hilbert function, no real-point content. Numerically the real
   conic `z0z1-z2^2` (real locus a whole `RP^1`) and `z0^2+z1^2+z2^2` (real locus EMPTY) have
   *identical* filter spectra at every `N` tested (difference 3.6e-15). The top eigenvector is the
   maximally entangled ground-space pairing state, not a real coherent pair.
3. The reason is structural, and is the sharpest thing this lane found: **`(ker H_N, K)` carries no
   invariant beyond `dim`** -- any two conjugations on equidimensional spaces are unitarily
   conjugate. Real-point information lives in the *algebra* action (the coherent frame, i.e. the
   compressed multiplications), never in the real structure.
4. On the nonlinear diagonal the filter is exactly `(|p^T p|/|p|^2)^{2N}`, with
   `|p^T p|/|p|^2 = 2F_R(p) - 1 = cos 2t` for `t` the Fubini-Study angle to `RP^n`. Its angular
   resolution is `Theta(N^{-1/2})` (`R ~ e^{-4Nt^2}`), not an exponentially sharp point separator.
5. Even there, `R = 1` certifies "real up to a global phase", **not** "real point": the ghost
   `|p>^{x N} + |pbar>^{x N}` has `R = 1` exactly, and both real-point-free conics still carry `R = 1`
   ground states (K-TC1).
6. Cost: acceptance `1/M_N` collective, `(n+1)^{-N}` pairwise (the linear-optics-native version is
   the *worse* one, by `(n+1)^N/M_N` = 5840 at `n=2, N=12`), times at most `2^{-N}` for ancilla-free
   Bell analysis; and the full projection consumes both copies, so it is a measurement, not a filter.
7. What survives and is new: (a) `<C^dag C>/N^2 = Tr(rho_1 rho_1^T)` with `C = sum_j a_j b_j` the
   pair-annihilation (two-mode-squeezing / spin-mixing) operator is a **bounded** two-copy observable,
   `O(1/eps^2)`, no postselection; (b) with the two-copy purity `Tr(rho_1^2)` it is a
   **polynomial-cost verifier** that a supplied ground state is a real point of `V(I)`; (c) the exact
   identity `#V_R(I) = Tr(Gh^{-1} G)` for the Hermitian and bilinear coherent Gram matrices, which
   names precisely the extra structure a real count needs and why it is the expensive one.

## Statement

**D-pairing-state.** `|Phi_N> = sum_{|k|=N}|k>|k>` in `R_N x R_N` for the D-fock-basis ONB, with
`<Phi_N|Phi_N> = M_N := dim R_N`, `(A x 1)|Phi_N> = (1 x A^T)|Phi_N>` and
`SWAP^{T_2} = |Phi_N><Phi_N|`; the normalised `SWAP^{T_2}/M_N =: Pi_N` is the projector onto the
normalised pairing state. `|Phi_N>` depends only on the real structure `K` (D-real-structure).
Second quantisation makes it native: with `a_j`, `b_j` the modes of the two copies,
`exp(sum_j a_j^dag b_j^dag)|vac> = sum_N |Phi_N>`, so `|Phi_N> = (C^dag)^N|vac>/N!` with
**`C := sum_j a_j b_j`**; `|Phi_N>` is the `N`-photon-per-copy sector of the multimode
two-mode-squeezed vacuum.

**D-two-copy-real-filter.** `F_N := (P_0 x P_0) Pi_N (P_0 x P_0)` on `ker H_N x ker H_N`. The
**pairwise** (linear-optics) form `Pi_Bell^{x N}`, `Pi_Bell = |Phi_1><Phi_1|/(n+1)`, agrees with it
up to normalisation: the symmetrisation isometry `Sym^N(C^{n+1}) -> (C^{n+1})^{x N}` has real matrix
entries, hence intertwines the two bilinear forms, so `(P_sym x P_sym)|Phi_1>^{x N} = |Phi_N>` and
`(P_sym x P_sym)(|Phi_1><Phi_1|)^{x N}(P_sym x P_sym) = |Phi_N><Phi_N|` exactly. The only difference
is `M_N` versus `(n+1)^N`, which is the entire cost gap.

**D-realness-witness.** `R(psi) = |psi^T psi|^2/<psi|psi>^2 = Tr(rho rho^T)` for pure `rho`: the
imaginarity measure (Hickey-Gour arXiv:1801.05123 / DOI 10.1088/1751-8121/aabe9c; Wu et al
arXiv:2007.14847 / PRL 126 090401). `R = 1` iff the ray meets `Fix(K)`; and
`M_N <psi x psi|Pi_N|psi x psi> = R(psi)`.

For a real ideal and `psi in ker H_N`: acceptance is `R(psi)/M_N` collective and `R(psi)/(n+1)^N`
pairwise; `R(|p>^{x N}) = (|p^T p|/|p|^2)^{2N}` exactly; and with
`F_R(p) = max_{x real, |x|=1}|<x|p>|^2/|p|^2` the fidelity to the nearest real point,
`|p^T p|/|p|^2 = 2F_R(p) - 1 = cos 2t`, `t` the Fubini-Study angle from `[p]` to `RP^n`, so
`R = (cos 2t)^{2N} ~ e^{-4Nt^2}`. The *response* is what the working answer said; the *spectrum* is
not.

## Spectrum of the compressed filter

**Proposition TC1 (rank and eigenvalue).** With `B` any matrix of an ONB of `ker H_N` and
`HF = HF_{R/I}(N)`: `F_N` has rank at most one, range spanned by `(P_0 x P_0)|Phi_N>`, and unique
nonzero eigenvalue
`lam_top = Tr(P_0 P_0^T)/M_N = ||B^T B||_F^2/M_N = (sum_i tau_i^2)/M_N`, where the `tau_i` are the
singular values of the complex symmetric `B^T B` (C9), i.e. the cosines of the principal angles
between `ker H_N` and its complex conjugate. If `I` is real, `ker H_N` has a real ONB, `B^T B` is
unitary, every `tau_i = 1`, and `lam_top = HF/M_N` **exactly**, with eigenvector
`Omega_N = sum_i |e_i>|e_i>/sqrt(HF)` for a real ONB `{e_i}` -- maximally entangled across the copies
(flat Schmidt spectrum `1/sqrt(HF)`, verified at `N=5`).

*Range*: one dimensional, the ground-space pairing state. **Is the top eigenspace spanned by
`|x>^{x N} x |x>^{x N}`, `x in V_R(I)`?** No, twice over. (i) It is one dimensional whatever `V_R(I)`
is. (ii) Real vectors `v` spanning a complex `W` give `span_C{v x v} = Sym^2(W)` by polarisation, so
`Omega_N` lies in the span of real-point pairs **iff** `HF_{R/J}(N) = HF_{R/I}(N)` for
`J = realradical(I) x_R C` (C-255) -- i.e. exactly when the real radical has already been reached in
degree `N`. That is the circularity of Route 3 of `scouting/real-variety.md`, restated.

**How does the spectrum separate real from complex points as `N` grows?** It does not. `HF(N)/M_N` is
a Hilbert-function ratio decaying like `N^{dim V - n}` for dimensional reasons, identical for two
ideals with the same Hilbert function and opposite real behaviour.

**Proposition TC2 (the no-go behind TC1).** If `K, K'` are conjugations on complex Hilbert spaces
`W, W'` with `dim W = dim W' < oo`, a unitary `U` with `UK = K'U` exists (map a real ONB of `Fix(K)`,
which is a complex ONB of `W`, to one of `Fix(K')`). Hence **every unitary invariant of
`(ker H_N, K)` is a function of `HF_{R/I}(N)` alone**, and no construction built from `P_0` and
`|Phi_N>` -- which is all `F_N` is -- can decide whether `V_R(I)` is empty, let alone count it.

**The one thing the filter does see** is realness of the *ideal*: in general
`lam_top/(HF/M_N) = (sum_i tau_i^2)/HF <= 1` with equality iff `I_N = conj(I_N)`. For `z0z1 - i z2^2`
at `N=5`, `Tr(P_0 P_0^T) = 4.713` against `HF = 11`. A subspace property, not a point property.

**Cross terms.** For `psi = sum_i c_i |p_i>^{x N}`,
`psi^T psi = sum_{ij} c_i c_j (p_i^T p_j)^N` while `<psi|psi> = sum_{ij} conj(c_i)c_j <p_i|p_j>^N`;
`|p_i^T p_j| <= |p_i||p_j|` with equality iff `p_j ~ conj(p_i)`. So at large `N` the only surviving
cross terms pair each point with its **complex conjugate**, and for a real ideal `V(I)` is
conjugation-stable so those partners always exist. Hence the `K`-fixed part of `ker H_N` is spanned
by `{|x>^{x N} : x real}` together with the ghosts `|p>^{x N} + |pbar>^{x N}`, its real dimension is
`HF(N)`, and a ghost has `R = 1` **exactly**, not asymptotically. Coherent ensembles give
`Tr(rho rho^T) -> 1/D` independently of `#V_R`, since every point has exactly one conjugate partner
whether or not it is real. **K-TC1 (ghost killer).**

**What circumventing C-256 costs.** The two-copy construction yields a complex-linear operator whose
*diagonal* is (up to scale) the indicator of `Fix(K)` up to phase. Four prices. (1) It is quadratic,
so it is a measurement, not a projector: projecting `psi x psi` on `|Phi_N>` consumes both copies and
returns one bit, so it cannot *prepare* a real component. (2) The linear operator on two copies knows
nothing (TC1/TC2); all the gain sits on the nonlinear diagonal already covered by the resource theory
of imaginarity. (3) The accept set is wrong: `Fix(K) n ker H_N` has real dimension `HF(N)` while
`V_R(I)` may be empty; the correct target `(J_N)^perp` (C-255) is itself `K`-stable, so the filter
cannot distinguish it from `ker H_N`. (4) Postselection, `1/M_N` or `(n+1)^{-N}`, times at most
`1/2` per pair for ancilla-free linear-optical Bell analysis (Calsamiglia-Lutkenhaus
arXiv:quant-ph/0007058, DOI 10.1007/s003400000484). For the record, the standard "real symmetry"
simulation is *not* two copies but one extra qubit encoding `i` (McKague-Mosca-Gisin arXiv:0810.1923,
PRL 102 020505); complex and real quantum theory remain operationally distinguishable in networks
(Renou et al arXiv:2101.10873, DOI 10.1038/s41586-021-04160-4).

**The partial filter (the only version that outputs a state).** Contract `k` of the `N` pairs. Split
`psi` by the real isometry `T_k : R_N -> R_k x R_{N-k}`,
`|m> -> sum_{a+b=m} sqrt(prod_j binom(m_j,a_j)/binom(N,k))|a>|b>` (which sends `|p>^{x N}` to
`|p>^{x k} x |p>^{x(N-k)}`), and let `A` be the coefficient matrix. Then
`<Phi_k|(psi x psi) = vec(A^T A)` and `Tr(A^T A) = psi^T psi`: the output is the **unconjugated**
Gram matrix, equal to the reduced density matrix `A^dag A` iff `psi` is real. In coherent terms the
output amplitudes are `c_i c_j (p_i^T p_j)^k`, so the two copies become correlated and only
conjugate pairs (real points included, `j = i`) survive large `k`. Acceptance `||A^T A||_F^2/M_k`.
It still cannot separate a real point from a conjugate pair.

## Numerics

`checkers/explore/twocopy_real_filter.py` (exploration, excluded from `run_all.sh`; 1.2 s wall under
`timeout 600`; exits 1 on any identity violation -- confirmed by two mutations:
`psi @ psi -> vdot(psi,psi)` in the witness turns part B red, and `(a@b) -> vdot(a,b)` in the
bilinear Gram turns part D red, where it then returns `4 = D` for all three quartics instead of
`#V_R`). Caps: conics in `P^2` to `N=8` (`M_N=45`, explicit compressed filter `289 x 289`); binary
quartics in `P^1` to `N=20`; qudit cross-check to `3^4 = 81` per copy. Rows below are a subset of the
printed tables; `[OK]` lines are verbatim.

```
A. F_N = (P_0 x P_0) Pi_N (P_0 x P_0) on ker H_N x ker H_N
ideal                                 N   M_N   HF  rank F     lam_top      HF/M_N  min tau_i  sup_V R^(1/2N)
conic z0z1-z2^2   (V_R = RP^1)        2     6    5       1    0.833333    0.833333   1.000000        1.000000
conic z0z1-z2^2   (V_R = RP^1)        5    21   11       1    0.523810    0.523810   1.000000        1.000000
conic z0z1-z2^2   (V_R = RP^1)        8    45   17       1    0.377778    0.377778   1.000000        1.000000
conic z0^2+z1^2+z2^2   (V_R empty)    2     6    5       1    0.833333    0.833333   1.000000        0.000000
conic z0^2+z1^2+z2^2   (V_R empty)    5    21   11       1    0.523810    0.523810   1.000000        0.000000
conic z0^2+z1^2+z2^2   (V_R empty)    8    45   17       1    0.377778    0.377778   1.000000        0.000000
conic z0^2+2z1^2+3z2^2 (V_R empty)    8    45   17       1    0.377778    0.377778   1.000000        0.333333
conic z0z1 - i z2^2 (NOT real)        5    21   11       1    0.224437    0.523810   0.215686
conic z0z1 - i z2^2 (NOT real)        8    45   17       1    0.108043    0.377778   0.000000
    [OK ] real ideal: lam_top == HF/M_N exactly   (max dev 2.22e-16 over the three real conics)
    [OK ] real-locus conic and EMPTY-real-locus conic have IDENTICAL filter spectra  max |difference| 3.55e-15
    [OK ] complex ideal: lam_top strictly below HF/M_N  Tr(P0P0^T) = 4.713187 < HF = 11
    [OK ] top eigenvector maximally entangled, NOT a coherent pair: N=5 Schmidt values all 0.301511 = 1/sqrt(11)

B. Coherent ground states of the conic z0z1 - z2^2 (the nonlinear diagonal)
point                       |p^Tp|    2F_R-1   N    <p|H_N|p>    R measured   R predicted   log10 R
real point   [1:1:1]      1.000000  1.000000  10     1.06e-16  1.000000e+00  1.000000e+00     0.000
near-real    th=0.10      0.986711  0.986711  10     1.49e-16  7.652439e-01  7.652439e-01    -0.116
complex      th=0.40      0.797804  0.797804  10     3.40e-16  1.091263e-02  1.091263e-02    -1.962
complex      [1:-1:i]     0.333333  0.333333  10     1.06e-16  2.867972e-10  2.867972e-10    -9.542
    [OK ] |p^Tp|/|p|^2 == 2*max_{x real}|<x|p>|^2 - 1  (angle to RP^n)  max dev 4.44e-16
ideal                                 sup_V |p^Tp|  sup_V R = sup^{2N} at N = 2,4,6,8
conic z0z1-z2^2   (V_R = RP^1)            1.000000  1.000e+00  1.000e+00  1.000e+00  1.000e+00
conic z0^2+z1^2+z2^2   (V_R empty)        0.000000  1.231e-62  1.514e-124 1.864e-186 2.294e-248
conic z0^2+2z1^2+3z2^2 (V_R empty)        0.333333  1.235e-02  1.524e-04  1.882e-06  2.323e-08

C. What R = 1 certifies (N = 6)
state                                                     <H_N>           R  Tr(rho_1^2)  Tr(r1 r1^T)
conic: real point |x>^{xN}, x=[1:1:1]                  4.18e-17  1.00000000   1.00000000   1.00000000
conic: complex point |p>^{xN}, p=[1:-1:i]              4.18e-17  0.00000188   1.00000000   0.11111111
conic: GHOST |p>^{xN}+|pbar>^{xN}                      1.77e-17  1.00000000   0.55677988   0.55677988
z0^2+z1^2+z2^2: random REAL ground vector             -9.74e-17  1.00000000   0.38666920   0.38666920
z0^2+2z1^2+3z2^2: random REAL ground vector           -6.69e-16  1.00000000   0.38796315   0.38796315
    [OK ] conjugate-pair GHOST has R = 1 exactly although the point is complex  R = 1.000000000000
    [OK ] real-point-FREE ideals still have R = 1 ground states (dim_R Fix(K) n ker H_N = HF)
    [OK ] certificate (Tr(rho_1^2), Tr(rho_1 rho_1^T)) = (1,1) only on the real-point row

D. #V_R = Tr(Gh^{-1} G): counting needs the coherent FRAME
binary quartic in P^1       #V_R   N  M_N  HF  lam_top = HF/M_N   Tr(Gh^-1 G)   cond(Gh)
(z0^2-z1^2)(z0^2-4z1^2)        4   3    4   4          1.000000    4.00000000     31.875
(z0^2-z1^2)(z0^2-4z1^2)        4  20   21   4          0.190476    4.00000000      2.071
(z0^2-z1^2)(z0^2+z1^2)         2   3    4   4          1.000000    2.00000000      3.000
(z0^2-z1^2)(z0^2+z1^2)         2  20   21   4          0.190476    2.00000000      1.004
(z0^2+z1^2)(z0^2+4z1^2)        0   3    4   4          1.000000    0.00000000     31.875
(z0^2+z1^2)(z0^2+4z1^2)        0  20   21   4          0.190476    0.00000000      2.071
    [OK ] Tr(Gh^{-1} G) == #V_R exactly for all three quartics, N = 3,5,8,12,20
    [OK ] all three have the SAME compressed-filter spectrum lam_top = 4/(N+1)

E. Partial filter, k of N pairs (N=6, psi = 0.5|x> + 0.6|p> + 0.7|pbar> on the conic)
  k  dim out   ||A^T A||_F^2   Tr(A^T A) = psi^T psi   accept 1/M_k  max cross-term err
  1       21      0.50350548              1.08938272       0.333333            5.55e-17
  3       10      0.41708903              1.08938272       0.100000            4.17e-17
  5        3      0.50105852              1.08938272       0.047619            1.11e-16
    [OK ] output amplitudes == c_i c_j (p_i^T p_j)^k;  psi real => A^T A == rho_{N-k} (dev 0.0e+00)

F. Cost
  N  M_N = dim R_N   (n+1)^N   accept collective 1/M_N  accept pairwise (n+1)^-N     ratio
  2              6         9                 1.667e-01                 1.111e-01       1.5
  6             28       729                 3.571e-02                 1.372e-03      26.0
 12             91    531441                 1.099e-02                 1.882e-06    5840.0
    real point [1:1:1]      <C^dag C>/N^2 = 1.00000000   Tr(rho_1 rho_1^T) = 1.00000000
    complex point [1:-1:i]  <C^dag C>/N^2 = 0.11111111   Tr(rho_1 rho_1^T) = 0.11111111
    ghost |p>+|pbar>        <C^dag C>/N^2 = 0.55677988   Tr(rho_1 rho_1^T) = 0.55677988
    [OK ] (P_sym x P_sym)|Phi_1^{xN}> = |Phi_N> verified at N = 2,3,4  (|diff| <= 1.99e-15)
```

## Algorithmic content and cost

**Real-point density: no.** By TC2 the filter cannot see it, and K-TC1 says why concretely: every
coherent ensemble on a real ideal has `Tr(rho rho^T) -> 1/D`, because the conjugation involution on
`V(I)` always has `D` points whether or not they are fixed. This is not bad precision on `#V_R/D`
(K-RV4); it is not estimating `#V_R/D` at all.

**Counting, and the price.** The count returns as soon as the **coherent frame** is available. For a
real zero-dimensional radical `I` in the stable range with `V = {x_1..x_D}` and
conjugation-compatible unit representatives (first nonzero coordinate real positive, so real points
are real vectors and conjugate points are conjugate vectors), put `Gh_{ab} = <x_a|x_b>^N`
(D-coherent-gram-matrix) and `G_{ab} = (x_a^T x_b)^N`. Since
`K|x_a>^{x N} = |x_{sigma(a)}>^{x N}`, `G = P_sigma Gh` with `P_sigma` the permutation matrix of
conjugation, so `#V_R(I) = Tr(Gh^{-1}G)` **exactly** at every `N` in the stable range (part D: exact
integers 4, 2, 0; the mutation `G -> Gh` returns `4 = D` in all three cases -- the Hermitian Gram
counts all points, the bilinear one counts the real ones). Three notes. (i) This is the trace of the
matrix of the antiunitary `K` in the coherent frame, hence frame dependent, consistent with TC2. (ii)
The coherent frame is intrinsically the joint eigenbasis of the commuting compressed multiplications
(D-compressed-multiplication), the classical eigenvalue method: the extra structure needed is the
**algebra action**. (iii) The cost is `Gh^{-1}`, i.e. D-coherent-gram-matrix, whose smallest
eigenvalue is `3.5 e^{-0.85n}` on the boolean family; K-RV6 reappears verbatim.

**Interaction with the Hermite route (C-257/C-258).** Same passage from the sesquilinear to the
bilinear pairing, seen twice. Hermite's
`h_g(u,v) = Tr_A(M_{guv}) = sum_{x in V} g(x)u(x)v(x)` is a *bilinear* form on the quotient algebra
whose signature counts real points; `|Phi_N>` is the physical implementation of "bilinear instead of
sesquilinear". The correct two-copy analogue of Hermite is therefore not `<Phi_N|(psi x psi)>` but
the family `<Phi_{N-m}|((a(g) x 1)(psi x psi))>` over contractions by `g`, whose matrix in the
coherent frame is `diag(g(x_a)) P_sigma Gh`, giving the real-point-weighted sums
`sum_{x in V_R} g(x)` whose sign pattern is the Hermite signature. Consequences: two copies do
**not** remove K-RV5 (a Hermite block encoding still presupposes quotient-algebra access); but they
supply a physical realisation of the bilinear pairing once that access exists.

**Cheap estimation.** Estimating `R(psi)` by postselection costs `M_N` shots (`sqrt(M_N)` with
amplitude estimation), and `SWAP^{T_2}` has norm `M_N`, so the full-`N` witness has no bounded-norm
estimator (K-TC4). Two escapes. (1) *Conjugated preparation*: if `psi = U|0>` with `U` known, then
`conj(U)|0> = K psi` is compiled gate by gate and a SWAP test gives `R(psi)` at `O(1/eps^2)` (Ekert
et al PRL 88 217901, arXiv:quant-ph/0203016). `scouting/real-variety.md` Route 2 dismisses this as
trivial because "the amplitudes are classically specified"; that reason is wrong -- knowing a circuit
does not give its amplitudes. The right objection is that a state prepared by a real circuit is real
by construction, so the test informs only about a state of unknown provenance. (2) *One-pair bounded
observables*: `<C^dag C>/N^2 = Tr(rho_1 rho_1^T)` with `C = sum_j a_j b_j` (verified exactly in part
F) and the purity `Tr(rho_1^2)` from the beamsplitter generator `sum_j a_j^dag b_j`; both have norm
at most one and cost `O(1/eps^2)` with no postselection. Randomized-measurement / classical-shadow
estimation of partial-transpose moments (Elben et al arXiv:2007.06305, PRL 125 200501) is the
alternative, with its own dimension-dependent sample cost.

**Proposed protocol (this lane's constructive output): a polynomial-cost real-point verifier.**
Given two copies of `psi` promised to lie in `ker H_N`, measure `Tr(rho_1^2)` and
`Tr(rho_1 rho_1^T)`. Both `= 1` iff `psi = |p>^{x N}` with `[p] in V_R(I)`: purity one on the
symmetric sector forces a product state, and then the second witness is `|p^T p|^2`. Cost
`O(1/eps^2)` copies, two Gaussian mode operations, no postselection, no `M_N` dependence. Part C
gives the separation: real point `(1.000, 1.000)`, complex point `(1.000, 0.111)`, ghost
`(0.557, 0.557)`, random real ground vector `(0.387, 0.387)`. What it is **not**: a way to find or
prepare a real point. It is a verifier for a supplied state -- the certification question of PRD Q4 /
Q10(b) and of K-RV10 -- and it is stronger than K-RV10 assumes, being a device-level check needing no
SOS certificate.

**Is the linear-optics realisation the north star's cheap heuristic attack?** No for the filter, yes
for the verifier. The pairwise Bell projection is native (an array of `n+1` beamsplitters plus photon
counting; equivalently reverse two-mode squeezing plus vacuum detection, since `|Phi_N>` is the
`N`-photon sector of the multimode TMSV), but its success probability is `(n+1)^{-N}` times at most
`2^{-N}`, and it returns a bit rather than a state: K-RV15 applies in full. The verifier uses only
`C = sum_j a_j b_j` and its beamsplitter partner -- exactly the pair-creation structure of the
spinor-BEC spin-mixing Hamiltonian (D-spin-mixing-hamiltonian, row C-024) and of a parametric
down-conversion source. That is a cheap heuristic attack, on the verification problem.

## Killers introduced by this lane

- **K-TC1 (ghosts).** `R = 1` certifies a `K`-fixed ray; the `K`-fixed part of `ker H_N` is a real
  form of real dimension `HF(N)`, contains `|p>^{x N} + |pbar>^{x N}` for every conjugate pair, and
  is nonzero even when `V_R(I) = {}`.
- **K-TC2 (dimension is the only invariant).** `(ker H_N, K)` is unitarily equivalent to
  `(C^{HF}, conjugation)`; any real-point statistic must use the algebra action.
- **K-TC3 (no state emerges).** The full-`N` projection consumes both copies; only the partial
  `k`-pair filter outputs a state, and it correlates the copies rather than filtering one.
- **K-TC4 (unbounded witness).** `||SWAP^{T_2}|| = M_N`, so the full witness costs `M_N` shots unless
  one drops to one-pair observables or a conjugated preparation circuit.
- **K-TC5 (pairwise costs more than collective).** `(n+1)^N/M_N` = 5840 at `n=2, N=12`; the
  linear-optics-native version is the expensive one.

## Proposed definitions

MERGE PROPOSAL (`definitions/definitions.md`, new entries). Statements as in the Statement section.

### D-pairing-state
`|Phi_N> = sum_{|k|=N}|k>|k>` in the D-fock-basis ONB, `<Phi_N|Phi_N> = M_N = dim R_N`,
`(A x 1)|Phi_N> = (1 x A^T)|Phi_N>`, `SWAP^{T_2} = |Phi_N><Phi_N|`. Second-quantised:
`|Phi_N> = (C^dag)^N|vac>/N!` with `C = sum_j a_j b_j` the pair-annihilation operator, so `|Phi_N>`
is the `N`-photon-per-copy sector of the multimode two-mode-squeezed vacuum; and
`(P_sym x P_sym)|Phi_1>^{x N} = |Phi_N>` because the symmetrisation isometry has real entries.
Source: standard; verified in `checkers/explore/twocopy_real_filter.py` part F.
Pitfalls: `|Phi_N>` is determined by the real structure `K` (D-real-structure), not by the ideal; its
norm is `M_N` collectively versus `(n+1)^N` pairwise, and that ratio is a cost, not a convention.

### D-two-copy-real-filter
`Pi_N = |Phi_N><Phi_N|/M_N` and its compression `F_N = (P_0 x P_0)Pi_N(P_0 x P_0)` onto
`ker H_N x ker H_N`; diagonal value `M_N <psi x psi|Pi_N|psi x psi> = R(psi)`; acceptance
`R(psi)/M_N` collective, `R(psi)/(n+1)^N` pairwise; `k`-pair partial filter
`<Phi_k|(psi x psi) = vec(A^T A)`, `A` the `Sym^k x Sym^{N-k}` coefficient matrix of `psi`.
Source: this memo, Statement; PRD D14.
Pitfalls: `F_N` has rank one and eigenvalue `Tr(P_0P_0^T)/M_N`, equal to `HF_{R/I}(N)/M_N` for every
real ideal -- a Hilbert-function ratio, not a real-point statistic. It is a measurement, not a
projector: the full-`N` projection consumes both copies.

### D-realness-witness
`R(psi) = |psi^T psi|^2/<psi|psi>^2 = Tr(rho rho^T)` for pure `rho`, the imaginarity measure
(arXiv:1801.05123, DOI 10.1088/1751-8121/aabe9c; arXiv:2007.14847, PRL 126 090401). `R = 1` iff the
ray meets `Fix(K)`. For coherent states `R(|p>^{x N}) = (|p^T p|/|p|^2)^{2N}` and
`|p^T p|/|p|^2 = 2F_R(p) - 1 = cos 2t`, `t` the Fubini-Study angle to `RP^n`.
Source: this memo; numerics part B.
Pitfalls: quadratic in the state, so not a one-copy observable (C-256 stands); `R = 1` is realness of
a vector, not of a coherent label -- conjugate-pair ghosts saturate it.

### D-one-particle-reduced-state
For `psi in R_N`, `(rho_1)_{ij} = <a_i^dag a_j>_psi/N` on `C^{n+1}`. `Tr(rho_1^2) = 1` iff `psi` is
coherent; `Tr(rho_1 rho_1^T) = <C^dag C>/N^2`, equal to `|p^T p|^2/|p|^4` for coherent `psi`. Both
are two-copy observables of norm at most one.
Source: this memo, Algorithmic content; numerics parts C and F.
Pitfalls: `Tr(rho_1 rho_1^T)` is the one-particle realness witness, not `R(psi)`; they agree only on
coherent states. The pair `(1,1)` is the real-point certificate.

## Proposed claim rows

MERGE PROPOSAL (`claims/CLAIMS.md`), all CONJECTURE per L1; where-tested is
`checkers/explore/twocopy_real_filter.py`.

### C-NEW-TC-RANK-ONE
- statement: For every homogeneous ideal `I` and every `N`, the compression
  `F_N = (P_0 x P_0)(|Phi_N><Phi_N|/M_N)(P_0 x P_0)` onto `ker H_N x ker H_N` has rank at most one,
  range spanned by `(P_0 x P_0)|Phi_N>`, and unique nonzero eigenvalue
  `Tr(P_0 P_0^T)/M_N = (sum_i tau_i^2)/M_N`, the `tau_i` being the cosines of the principal angles
  between `ker H_N` and its complex conjugate; if `I` has real generators then every `tau_i = 1`, the
  eigenvalue is exactly `HF_{R/I}(N)/M_N`, and the eigenvector is the maximally entangled
  ground-space pairing state.
- status: CONJECTURE
- depends-on: D-pairing-state, D-two-copy-real-filter, D-projectors, D-ground-space, D-takagi-factorisation
- where-proved: `scouting/two-copy-real-filter.md`, Proposition TC1
- where-tested: part A, `N = 2..8`, four ideals in `P^2`
- north-star relevance: settles what the two-copy construction is as a linear operator.
- traps audited: reading a nonlinear witness as an operator spectrum; changing the output.

### C-NEW-TC-NO-REAL-INFORMATION
- statement: For every pair of conjugations on complex Hilbert spaces of equal finite dimension there
  is a unitary intertwiner; hence every unitary invariant of `(ker H_N, K)` is a function of
  `HF_{R/I}(N)`, and no construction built from `P_0` and `|Phi_N>` alone decides whether `V_R(I)` is
  empty. In particular `z0z1 - z2^2` (real locus `RP^1`) and `z0^2+z1^2+z2^2` (real locus empty) have
  identical `F_N` spectra at every `N`.
- status: CONJECTURE
- depends-on: D-real-structure, D-two-copy-real-filter, C-NEW-TC-RANK-ONE, C-256
- where-proved: `scouting/two-copy-real-filter.md`, Proposition TC2
- where-tested: part A, difference 3.55e-15 at `N = 2..8`
- north-star relevance: closes the strong form of the two-copy proposal; real-point information needs
  the algebra action, not the real structure.
- traps audited: mistaking a real form for a distinguished subspace; Zariski density (K-RV2).

### C-NEW-TC-COHERENT-RESPONSE
- statement: For every unit `p in C^{n+1}` and every `N`, `R(|p>^{x N}) = |p^T p|^{2N}` and
  `|p^T p| = 2 max_{x real, |x|=1}|<x|p>|^2 - 1 = cos 2t` with `t` the Fubini-Study distance from
  `[p]` to `RP^n`; hence a complex point at angle `t` is suppressed as
  `exp(-2N ln(1/cos 2t)) = exp(-4Nt^2(1+O(t^2)))`, and the filter's angular resolution about `RP^n`
  is `Theta(N^{-1/2})`.
- status: CONJECTURE
- depends-on: D-coherent-state, D-realness-witness
- where-proved: `scouting/two-copy-real-filter.md`, Statement
- where-tested: part B, four points, `N = 2..10`, agreement to 1e-9
- north-star relevance: the exact filter rate and its resolution limit.
- traps audited: confusing exponential filter strength with exponential separation of nearby points.

### C-NEW-TC-GHOST
- statement: For every real ideal `I`, every `N`, and every `p in V(I)`, the vector
  `|p>^{x N} + |conj(p)>^{x N}` lies in `ker H_N` and has `R = 1` exactly; the `K`-fixed subset of
  `ker H_N` is a real subspace of real dimension `HF_{R/I}(N)` and is nonzero even when
  `V_R(I) = {}`. Hence `R(psi) = 1` certifies that the ray of `psi` is real, not that `psi` is the
  coherent state of a real point.
- status: CONJECTURE
- depends-on: D-realness-witness, D-coherent-state, D-real-structure, C-255
- where-proved: `scouting/two-copy-real-filter.md`, K-TC1
- where-tested: part C (`R = 1.000000000000` for the ghost; `R = 1` real ground vectors for both
  real-point-free conics)
- north-star relevance: refutes "postselecting on the filter prepares real points".
- traps audited: real vector versus real label; K-RV1, K-RV2.

### C-NEW-TC-FRAME-COUNT
- statement: For every real zero-dimensional radical ideal `I` in the stable range, every `N` at
  which the coherent states of `V(I)` form a basis of `ker H_N`, and conjugation-compatible unit
  representatives `x_1..x_D` of `V(I)`, the Hermitian and bilinear coherent Gram matrices
  `Gh_{ab} = <x_a|x_b>^N` and `G_{ab} = (x_a^T x_b)^N` satisfy `G = P_sigma Gh` with `P_sigma` the
  permutation matrix of complex conjugation on `V(I)`; hence `Tr(Gh^{-1}G) = #V_R(I)` and
  `Tr(Gh^{-1}Gh) = D`.
- status: CONJECTURE
- depends-on: D-coherent-gram-matrix, D-pairing-state, D-coherent-state, D-real-locus-and-real-radical
- where-proved: `scouting/two-copy-real-filter.md`, Algorithmic content
- where-tested: part D, three binary quartics with 4, 2, 0 real roots, `N = 3,5,8,12,20`, exact
  integers; mutation `G -> Gh` returns `4 = D` in all three
- north-star relevance: names the exact extra structure a real count needs (the coherent frame, i.e.
  the compressed multiplications) and its cost `Gh^{-1}`.
- traps audited: frame dependence of the trace of an antiunitary; phase conventions on projective
  representatives; K-RV6 (Gram conditioning).

### C-NEW-TC-ONE-PAIR-CERTIFICATE
- statement: For every real ideal `I`, every `N >= max_j m_j`, and every `psi in ker H_N`, the two
  one-particle two-copy observables `Tr(rho_1^2)` and `Tr(rho_1 rho_1^T) = <C^dag C>/N^2` with
  `C = sum_j a_j b_j` both equal `1` if and only if `psi = |p>^{x N}` for some `p` with
  `[p] in V_R(I)`; both have operator norm at most one and are estimable to additive `eps` with
  `O(1/eps^2)` copies and no postselection.
- status: CONJECTURE
- depends-on: D-one-particle-reduced-state, D-realness-witness, D-coherent-state, D-ground-space
- where-proved: `scouting/two-copy-real-filter.md`, Algorithmic content
- where-tested: parts C and F (real point `(1,1)`, complex point `(1, 0.111)`, ghost
  `(0.557, 0.557)`, random real ground vector `(0.387, 0.387)`)
- north-star relevance: a polynomial-cost verifier that a supplied ground state is a real point, with
  a spinor-BEC / parametric-source realisation; a certification product, not a speedup.
- traps audited: verification versus preparation; robustness (the `1-eps` version is open); K-RV10.

### C-NEW-TC-COST
- statement: For every `N` and `n` the collective pairing measurement accepts `psi x psi` with
  probability `R(psi)/M_N` and the pairwise Bell measurement with probability `R(psi)/(n+1)^N`, a
  ratio `(n+1)^N/M_N`; ancilla-free linear-optical Bell analysis contributes at most `1/2` per pair;
  `SWAP^{T_2}` has operator norm `M_N`, so the full realness witness admits no bounded-observable
  estimator; and the full-`N` projection consumes both copies and outputs one bit.
- status: CONJECTURE
- depends-on: D-two-copy-real-filter, D-pairing-state, D-input-model
- where-proved: `scouting/two-copy-real-filter.md`, K-TC3/K-TC4/K-TC5
- where-tested: part F (ratio 5840 at `n = 2, N = 12`)
- north-star relevance: prices the postselected route out and leaves the one-pair observables.
- traps audited: hidden postselection; hardware universality (K-RV15); measurement read as a filter.

## Questions for TJO

1. **Does the verifier count as a product?** C-NEW-TC-ONE-PAIR-CERTIFICATE is a polynomial-cost,
   two-copy, linear-optics-native check that a supplied ground state is a real point of `V(I)`. It
   verifies; it does not find. PRD Q4 and Q10(b) ask this in general and this lane now supplies a
   concrete instance to rule on. Recommendation: yes as an instrument and as the honest hardware
   demonstration for arm E; no as a north-star hit.
2. **Amend Route 2 of `scouting/real-variety.md` in lockstep (L2)?** It scores 1/5 and dismisses the
   two-copy observable as "only classifies a supplied state". That is right about the filter, but its
   stated reason (for a circuit-prepared state "the amplitudes are classically specified") is wrong.
   With the one-pair certificate and `#V_R = Tr(Gh^{-1}G)`, Route 2 is 2/5 for certification and
   stays 1/5 for search. Amend there, or leave the correction here only?
3. **Fund the robustness question?** The certificate is exact as stated. The useful version: if
   `Tr(rho_1^2) >= 1-eps`, `Tr(rho_1 rho_1^T) >= 1-eps` and `<psi|H_N|psi> <= delta`, how close is
   `[p]` to `V_R(I)` in Fubini-Study distance, with what dependence on `N`, `Delta_N` and the
   D-condition-number? One analytic day; it is the difference between a demo and a theorem.
   Recommendation: yes, paired with PRD Q10(d).
4. **Is `#V_R = Tr(Gh^{-1}G)` worth its own lane?** It is exact and elementary, and it names the
   classical object the quantum side would have to produce. Two possible algorithmic forms: QSVT
   construction of `Gh^{-1/2} G Gh^{-1/2}` from Macaulay access, or a DQC1-style normalised trace
   estimate (D-dqc1-style-estimate). Both inherit K-RV6. Recommendation: fold into the C-257/C-258
   Hermite lane -- it is the same bilinear-versus-sesquilinear passage -- rather than open a new one.
5. **Accept C-NEW-TC-NO-REAL-INFORMATION as closing "real symmetry via two copies"?** It closes the
   strong form (a spectral selector). It leaves the weak forms open: the ideal-realness test
   `(sum_i tau_i^2)/HF`, the one-pair certificate, and the partial `k`-pair filter as a preparation
   primitive for conjugate-paired components. Recommendation: enter the seven rows, mark the strong
   form closed in the PRD arm E description, keep the certificate open.
6. **Reference budget (PRD Q9).** Seven references used, all seven resolved this session, none
   `[UNVERIFIED]`: arXiv:1801.05123 / DOI 10.1088/1751-8121/aabe9c; arXiv:2007.14847 / PRL 126
   090401; arXiv:0810.1923 / PRL 102 020505; arXiv:2101.10873 / DOI 10.1038/s41586-021-04160-4;
   arXiv:quant-ph/0007058 / DOI 10.1007/s003400000484; arXiv:quant-ph/0203016 / PRL 88 217901;
   arXiv:2007.06305 / PRL 125 200501. Cost was a few minutes each, so the half-day resolution pass on
   the classical memo's 63 looks cheap: recommend yes.
