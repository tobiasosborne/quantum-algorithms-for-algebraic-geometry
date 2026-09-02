# The two-copy real-symmetry filter

Lane: two-copy real filter, PRD D14 (TJO question 2026-09-02, "About real QM: do we simulate it via
two copies to ensure real symmetry?"). Date: 2026-09-02. Status: scouting only; nothing ratcheted;
every proposed row is CONJECTURE per L1.

Conventions C1-C12 are binding; objects are D-fock-space, D-fock-basis, D-hamiltonian,
D-ground-space, D-coherent-state, D-coherent-gram-matrix, D-projectors, D-real-structure,
D-real-locus-and-real-radical, D-real-coherent-span, D-takagi-factorisation, D-hermite-trace-form.
**Departure from C5**, as in the whole checker suite: generators are taken as written, not unit
Bombieri-Weyl; nothing here depends on that, every reported quantity being a ratio, a projector or a
Hilbert-function count (D-norm-comparison). `D` is only a quotient dimension (C8), `p` only a
coherent-state label (C11), `tau_i` only a Takagi / principal-angle value (C9).

## Bottom line

The two-copy trick is exact, and it does not do what the working answer hoped.

1. Realness **is** linear on two copies: `SWAP^{T_2} = |Phi_N><Phi_N|` exactly and the pairing
   measurement accepts `psi x psi` with probability `R(psi)/M_N` for
   `R(psi) = |psi^T psi|^2/<psi|psi>^2`; C-256 is circumvented as an arithmetic matter.
2. But the compression onto `ker H_N x ker H_N` has **rank one**, with eigenvalue `HF_{R/I}(N)/M_N`
   -- the normalised Hilbert function, no real-point content: `z0z1-z2^2` (real locus a whole `RP^1`)
   and `z0^2+z1^2+z2^2` (real locus EMPTY) have *identical* filter spectra at every `N` tested
   (3.6e-15), and the top eigenvector is the maximally entangled ground-space pairing state.
3. The reason is structural and is the sharpest thing this lane found: **`(ker H_N, K)` carries no
   invariant beyond `dim`**, since any two conjugations on equidimensional spaces are unitarily
   conjugate. Real-point information lives in the *algebra* action (the coherent frame = the
   compressed multiplications), never in the real structure.
4. On the nonlinear diagonal the filter is exactly `(|p^T p|/|p|^2)^{2N} = (cos 2t)^{2N}` for `t` the
   Fubini-Study angle to `RP^n`, so its resolution is `Theta(N^{-1/2})`, not an exponentially sharp
   point separator; and even there `R = 1` certifies "real up to a global phase", **not** "real
   point": the ghost `|p>^{x N} + |pbar>^{x N}` has `R = 1` exactly and both real-point-free conics
   carry `R = 1` ground states (K-TC1).
5. Cost: acceptance `1/M_N` collective, `(n+1)^{-N}` pairwise -- the linear-optics-native version is
   the *worse* one, by `(n+1)^N/M_N` = 5840 at `n=2, N=12` -- times at most `2^{-N}` for ancilla-free
   Bell analysis; and the projection consumes both copies, so it is a measurement, not a filter.
6. What survives and is new: (a) `<C^dag C>/N^2 = Tr(rho_1 rho_1^T)`, `C = sum_j a_j b_j` the
   pair-annihilation (two-mode-squeezing / spin-mixing) operator, is a **bounded** two-copy
   observable: `O(1/eps^2)`, no postselection; (b) with the purity `Tr(rho_1^2)` it is a
   **polynomial-cost verifier** that a supplied ground state is a real point of `V(I)`; (c) the exact
   `#V_R(I) = Tr(Gh^{-1} G)`, naming the extra structure a real count needs and its cost.

## Statement

**D-pairing-state.** `|Phi_N> = sum_{|k|=N}|k>|k>` in `R_N x R_N` for the D-fock-basis ONB, with
`<Phi_N|Phi_N> = M_N := dim R_N`, `(A x 1)|Phi_N> = (1 x A^T)|Phi_N>` and
`SWAP^{T_2} = |Phi_N><Phi_N|`; `Pi_N := SWAP^{T_2}/M_N` is the projector onto the normalised pairing
state and depends only on `K` (D-real-structure). Second quantisation makes it native: with `a_j,
b_j` the modes of the two copies, `exp(sum_j a_j^dag b_j^dag)|vac> = sum_N |Phi_N>`, so
`|Phi_N> = (C^dag)^N|vac>/N!` with **`C := sum_j a_j b_j`** -- the `N`-photon-per-copy sector of the
multimode two-mode-squeezed vacuum.

**D-two-copy-real-filter.** `F_N := (P_0 x P_0) Pi_N (P_0 x P_0)` on `ker H_N x ker H_N`. The
**pairwise** (linear-optics) form `Pi_Bell^{x N}`, `Pi_Bell = |Phi_1><Phi_1|/(n+1)`, agrees up to
normalisation: the symmetrisation isometry `Sym^N(C^{n+1}) -> (C^{n+1})^{x N}` has real entries, so
it intertwines the two bilinear forms and `(P_sym x P_sym)|Phi_1>^{x N} = |Phi_N>` exactly. The only
difference is `M_N` versus `(n+1)^N` -- the entire cost gap.

**D-realness-witness.** `R(psi) = |psi^T psi|^2/<psi|psi>^2 = Tr(rho rho^T)` for pure `rho`, the
imaginarity measure (Hickey-Gour arXiv:1801.05123; Wu et al arXiv:2007.14847); `R = 1` iff the ray
meets `Fix(K)`, and `M_N <psi x psi|Pi_N|psi x psi> = R(psi)`. For a real ideal and `psi in ker H_N`
acceptance is `R(psi)/M_N` collective, `R(psi)/(n+1)^N` pairwise, `R(|p>^{x N})` is exactly
`(|p^T p|/|p|^2)^{2N}`, and with `F_R(p) = max_{x real, |x|=1}|<x|p>|^2/|p|^2` the fidelity to the
nearest real point, `|p^T p|/|p|^2 = 2F_R(p) - 1 = cos 2t` for `t` the Fubini-Study angle to `RP^n`,
so `R = (cos 2t)^{2N} ~ e^{-4Nt^2}`. The *response* is what the working answer said; the *spectrum*
is not.

## Spectrum of the compressed filter

**Proposition TC1 (rank and eigenvalue).** With `B` an ONB matrix of `ker H_N`, `HF = HF_{R/I}(N)`:
`F_N` has rank at most one, range spanned by `(P_0 x P_0)|Phi_N>`, unique nonzero eigenvalue
`lam_top = Tr(P_0 P_0^T)/M_N = ||B^T B||_F^2/M_N = (sum_i tau_i^2)/M_N`, the `tau_i` being the
singular values of the complex symmetric `B^T B` (C9) = the cosines of the principal angles between
`ker H_N` and its complex conjugate. For real `I` that space has a real ONB, `B^T B` is unitary, every
`tau_i = 1` and `lam_top = HF/M_N` **exactly**, with eigenvector `Omega_N = sum_i |e_i>|e_i>/sqrt(HF)`
-- maximally entangled (flat Schmidt spectrum, verified at `N=5`: all `0.301511 = 1/sqrt(11)`).

**Is the top eigenspace spanned by `|x>^{x N} x |x>^{x N}`, `x in V_R(I)`?** No, twice over: the range
is one dimensional whatever `V_R(I)` is; and since real vectors spanning a complex `W` give
`span_C{v x v} = Sym^2(W)` by polarisation, `Omega_N` is in the span of real-point pairs **iff**
`HF_{R/J}(N) = HF_{R/I}(N)` for `J = realradical(I) x_R C` (C-255), i.e. exactly when the real radical
has been reached in degree `N` -- Route 3's circularity restated. **Separation of real from complex
points as `N` grows?** None: `HF(N)/M_N` decays like `N^{dim V - n}` for dimensional reasons and is
identical for two ideals with the same Hilbert function and opposite real behaviour.

**Proposition TC2 (the no-go behind TC1).** If `K, K'` are conjugations on complex Hilbert spaces
`W, W'` with `dim W = dim W' < oo`, a unitary `U` with `UK = K'U` exists: map a real ONB of `Fix(K)`,
itself a complex ONB of `W`, to one of `Fix(K')`. Hence **every unitary invariant of `(ker H_N, K)`
is a function of `HF_{R/I}(N)` alone**, and no construction built from `P_0` and `|Phi_N>` -- all
`F_N` is -- decides whether `V_R(I)` is empty, let alone counts it. The one thing the filter sees is
realness of the *ideal*: `lam_top/(HF/M_N) = (sum_i tau_i^2)/HF <= 1` with equality iff
`I_N = conj(I_N)`; at `N=5` for `z0z1 - i z2^2`, `Tr(P_0P_0^T) = 4.713` against `HF = 11` -- a
subspace property, not a point property.

**Cross terms.** For `psi = sum_i c_i |p_i>^{x N}`, `psi^T psi = sum_{ij} c_i c_j (p_i^T p_j)^N`
while `<psi|psi> = sum_{ij} conj(c_i) c_j <p_i|p_j>^N`, and `|p_i^T p_j| <= |p_i||p_j|` with equality
iff `p_j ~ conj(p_i)`, partners that always exist since `V(I)` is conjugation-stable. So the `K`-fixed
part of `ker H_N` is spanned by `{|x>^{x N} : x real}` and the ghosts `|p>^{x N} + |pbar>^{x N}`, has
real dimension `HF(N)`, and a ghost has `R = 1` **exactly**; coherent ensembles give
`Tr(rho rho^T) -> 1/D` independently of `#V_R`. **K-TC1 (ghost killer).**

**What circumventing C-256 costs.** Four prices. (1) The witness is quadratic, hence a measurement,
not a projector: the projection consumes both copies and returns one bit, so it cannot *prepare* a
real component. (2) The linear operator knows nothing (TC1/TC2); the gain sits entirely on the
nonlinear diagonal already covered by the resource theory of imaginarity. (3) The accept set is
wrong: `Fix(K) n ker H_N` has real dimension `HF(N)` while `V_R(I)` may be empty, and the correct
target `(J_N)^perp` (C-255) is itself `K`-stable, so the filter cannot tell it from `ker H_N`.
(4) Postselection, `1/M_N` or `(n+1)^{-N}`, times at most `1/2` per pair for ancilla-free
linear-optical Bell analysis (Calsamiglia-Lutkenhaus arXiv:quant-ph/0007058, DOI
10.1007/s003400000484). For the record, the standard "real symmetry" simulation is *not* two copies
but one extra qubit encoding `i` (McKague-Mosca-Gisin arXiv:0810.1923, PRL 102 020505), and the two
theories stay operationally distinguishable in networks (Renou et al arXiv:2101.10873, DOI
10.1038/s41586-021-04160-4).

**The partial filter (the only version that outputs a state).** Contract `k` of the `N` pairs: split
`psi` by the real isometry `T_k : R_N -> R_k x R_{N-k}`,
`|m> -> sum_{a+b=m} sqrt(prod_j binom(m_j,a_j)/binom(N,k))|a>|b>` (sending `|p>^{x N}` to
`|p>^{x k} x |p>^{x(N-k)}`), with `A` the coefficient matrix. Then
`<Phi_k|(psi x psi) = vec(A^T A)` and `Tr(A^T A) = psi^T psi`: the output is the **unconjugated**
Gram matrix, equal to the reduced density matrix `A^dag A` iff `psi` is real, with amplitudes
`c_i c_j (p_i^T p_j)^k`, so the copies become correlated and only conjugate pairs survive large `k`;
acceptance `||A^T A||_F^2/M_k`. It still cannot separate a real point from a conjugate pair.

## Numerics

`checkers/explore/twocopy_real_filter.py` (exploration, excluded from `run_all.sh`; 1.2 s wall under
`timeout 600`; exits 1 on any identity violation, confirmed by two mutations:
`psi @ psi -> vdot(psi,psi)` in the witness turns part B red, and `(a@b) -> vdot(a,b)` in the
bilinear Gram turns part D red, returning `4 = D` for all three quartics instead of `#V_R`). Caps:
conics in `P^2` to `N=8` (`M_N=45`, compressed filter `289 x 289`), binary quartics in `P^1` to
`N=20`, qudit cross-check to `3^4 = 81` per copy. Rows below are a subset of the printed tables
(full run `N = 2..8` / `N = 3,5,8,12,20`); `[OK ]` lines are condensed, numbers verbatim.

```
A. F_N = (P_0 x P_0) Pi_N (P_0 x P_0) on ker H_N x ker H_N
ideal                                 N   M_N   HF  rank F     lam_top      HF/M_N  min tau_i  sup_V R^(1/2N)
conic z0z1-z2^2   (V_R = RP^1)        8    45   17       1    0.377778    0.377778   1.000000        1.000000
conic z0^2+z1^2+z2^2   (V_R empty)    8    45   17       1    0.377778    0.377778   1.000000        0.000000
conic z0^2+2z1^2+3z2^2 (V_R empty)    8    45   17       1    0.377778    0.377778   1.000000        0.333333
conic z0z1 - i z2^2 (NOT real)        8    45   17       1    0.108043    0.377778   0.000000
    [OK ] real ideal: lam_top == HF/M_N exactly   (max dev 2.22e-16 over the three real conics)
    [OK ] real-locus conic and EMPTY-real-locus conic have IDENTICAL filter spectra  max |difference| 3.55e-15
    [OK ] complex ideal: lam_top strictly below HF/M_N  Tr(P0P0^T) = 4.713187 < HF = 11

B. Coherent ground states of the conic z0z1 - z2^2 (the nonlinear diagonal)
point                       |p^Tp|    2F_R-1   N    <p|H_N|p>    R measured   R predicted   log10 R
real point   [1:1:1]      1.000000  1.000000  10     1.06e-16  1.000000e+00  1.000000e+00     0.000
complex      th=0.40      0.797804  0.797804  10     3.40e-16  1.091263e-02  1.091263e-02    -1.962
complex      [1:-1:i]     0.333333  0.333333  10     1.06e-16  2.867972e-10  2.867972e-10    -9.542
ideal                                 sup_V |p^Tp|  sup_V R = sup^{2N} at N = 2,4,6,8
conic z0z1-z2^2   (V_R = RP^1)            1.000000  1.000e+00  1.000e+00  1.000e+00  1.000e+00
conic z0^2+2z1^2+3z2^2 (V_R empty)        0.333333  1.235e-02  1.524e-04  1.882e-06  2.323e-08

C. What R = 1 certifies (N = 6)
state                                                     <H_N>           R  Tr(rho_1^2)  Tr(r1 r1^T)
conic: real point |x>^{xN}, x=[1:1:1]                  4.18e-17  1.00000000   1.00000000   1.00000000
conic: complex point |p>^{xN}, p=[1:-1:i]              4.18e-17  0.00000188   1.00000000   0.11111111
conic: GHOST |p>^{xN}+|pbar>^{xN}                      1.77e-17  1.00000000   0.55677988   0.55677988
z0^2+z1^2+z2^2: random REAL ground vector             -9.74e-17  1.00000000   0.38666920   0.38666920
    [OK ] conjugate-pair GHOST has R = 1 exactly although the point is complex  R = 1.000000000000
    [OK ] real-point-FREE ideals still have R = 1 ground states (dim_R Fix(K) n ker H_N = HF)

D. #V_R = Tr(Gh^{-1} G): counting needs the coherent FRAME
binary quartic in P^1       #V_R   N  M_N  HF  lam_top = HF/M_N   Tr(Gh^-1 G)   cond(Gh)
(z0^2-z1^2)(z0^2-4z1^2)        4  20   21   4          0.190476    4.00000000      2.071
(z0^2-z1^2)(z0^2+z1^2)         2  20   21   4          0.190476    2.00000000      1.004
(z0^2+z1^2)(z0^2+4z1^2)        0  20   21   4          0.190476    0.00000000      2.071
    [OK ] Tr(Gh^{-1} G) == #V_R exactly for all three quartics, N = 3,5,8,12,20

E. Partial filter, k of N pairs (N=6, psi = 0.5|x> + 0.6|p> + 0.7|pbar> on the conic)
  k=5: dim out 3, ||A^T A||_F^2 = 0.50105852, Tr(A^T A) = psi^T psi = 1.08938272, accept 1/M_5
    [OK ] output amplitudes == c_i c_j (p_i^T p_j)^k;  psi real => A^T A == rho_{N-k} (max dev 0.00e+00)

F. Cost
  N  M_N = dim R_N   (n+1)^N   accept collective 1/M_N  accept pairwise (n+1)^-N     ratio
  2              6         9                 1.667e-01                 1.111e-01       1.5
 12             91    531441                 1.099e-02                 1.882e-06    5840.0
    real point [1:1:1]      <C^dag C>/N^2 = 1.00000000   Tr(rho_1 rho_1^T) = 1.00000000
    ghost |p>+|pbar>        <C^dag C>/N^2 = 0.55677988   Tr(rho_1 rho_1^T) = 0.55677988
    [OK ] (P_sym x P_sym)|Phi_1^{xN}> = |Phi_N> verified at N = 2,3,4  (|diff| <= 1.99e-15)
```

## Algorithmic content and cost

**Real-point density: no.** By TC2 the filter cannot see it, and K-TC1 says why: every coherent
ensemble on a real ideal has `Tr(rho rho^T) -> 1/D`, the conjugation involution on `V(I)` always having
`D` points whether or not fixed. Not bad precision on `#V_R/D` (K-RV4): no estimate at all.

**Counting, and the price.** The count returns as soon as the **coherent frame** is available: for a
real zero-dimensional radical `I` in the stable range with `V = {x_1..x_D}` and
conjugation-compatible unit representatives (first nonzero coordinate real positive), put
`Gh_{ab} = <x_a|x_b>^N` (D-coherent-gram-matrix) and `G_{ab} = (x_a^T x_b)^N`. Since
`K|x_a>^{x N} = |x_{sigma(a)}>^{x N}`, `G = P_sigma Gh` with `P_sigma` the permutation matrix of conjugation,
so `#V_R(I) = Tr(Gh^{-1}G)` **exactly** at every `N` in the stable range (part D: integers 4, 2, 0;
the mutation `G -> Gh` returns `4 = D` -- the Hermitian Gram counts all points, the bilinear one the
real ones). Three notes: this is the trace of the matrix of the antiunitary `K` in the coherent
frame, hence frame dependent, consistent with TC2; that frame is the joint eigenbasis of the
commuting compressed multiplications (D-compressed-multiplication), so the structure needed is the
**algebra action**; and the cost is `Gh^{-1}`, smallest eigenvalue `3.5 e^{-0.85n}` on the boolean
family, so K-RV6 reappears verbatim.

**Interaction with the Hermite route (C-257/C-258).** The same sesquilinear-to-bilinear passage seen
twice: Hermite's `h_g(u,v) = Tr_A(M_{guv}) = sum_{x in V} g(x)u(x)v(x)` is a *bilinear* form on the
quotient algebra whose signature counts real points, and `|Phi_N>` implements "bilinear instead of
sesquilinear" physically. So the two-copy analogue of Hermite is not `<Phi_N|(psi x psi)>` but the
family `<Phi_{N-m}|((a(g) x 1)(psi x psi))>` over contractions by `g`, whose matrix in the coherent
frame is `diag(g(x_a)) P_sigma Gh`, giving the real-point-weighted sums `sum_{x in V_R} g(x)` whose
sign pattern is the Hermite signature. Two copies therefore do **not** remove K-RV5, but they realise
the bilinear pairing physically once quotient-algebra access exists.

**Cheap estimation.** Estimating `R(psi)` by postselection costs `M_N` shots (`sqrt(M_N)` with
amplitude estimation), and `||SWAP^{T_2}|| = M_N`, so the full-`N` witness has no bounded-norm
estimator (K-TC4). Two escapes. (1) *Conjugated preparation*: if `psi = U|0>` with `U` known then
`conj(U)|0> = K psi` is compiled gate by gate and a SWAP test gives `R(psi)` at `O(1/eps^2)` (Ekert
et al PRL 88 217901, arXiv:quant-ph/0203016). `scouting/real-variety.md` Route 2 dismisses this
because for a circuit-prepared state "the amplitudes are classically specified"; that reason is wrong
-- knowing a circuit does not give its amplitudes. The right objection is that a state prepared by a
real circuit is real by construction, so the test informs only on a state of unknown provenance.
(2) *One-pair bounded observables*: `<C^dag C>/N^2 = Tr(rho_1 rho_1^T)` (part F) and the purity
`Tr(rho_1^2)` from the beamsplitter generator `sum_j a_j^dag b_j`, both of norm at most one and cost
`O(1/eps^2)` with no postselection; the alternative is randomized-measurement estimation of
partial-transpose moments (Elben et al arXiv:2007.06305, PRL 125 200501).

**Proposed protocol (this lane's constructive output): a polynomial-cost real-point verifier.** Given
two copies of `psi` promised to lie in `ker H_N`, measure `Tr(rho_1^2)` and `Tr(rho_1 rho_1^T)`; both
`= 1` iff `psi = |p>^{x N}` with `[p] in V_R(I)`, since purity one on the symmetric sector forces a
product state and the second witness is then `|p^T p|^2`. Cost: `O(1/eps^2)` copies, two Gaussian
mode operations, no postselection, no `M_N` dependence; part C separates real point `(1.000, 1.000)`,
complex point `(1.000, 0.111)`, ghost `(0.557, 0.557)`, real ground vector `(0.387, 0.387)`. What it
is **not**: a way to find or prepare a real point. It is a verifier for a supplied state -- PRD Q4 /
Q10(b) and K-RV10 -- and stronger than K-RV10 assumes, being a device-level check needing no SOS
certificate.

**Is the linear-optics realisation the north star's cheap heuristic attack?** No for the filter, yes
for the verifier. The pairwise Bell projection is native (an array of `n+1` beamsplitters plus photon
counting, equivalently reverse two-mode squeezing plus vacuum detection), but succeeds with
probability `(n+1)^{-N}` times at most `2^{-N}` and returns a bit, not a state: K-RV15 in full. The
verifier uses only `C = sum_j a_j b_j` and its beamsplitter partner -- the pair-creation structure of
the spinor-BEC spin-mixing Hamiltonian (D-spin-mixing-hamiltonian, C-024) and of a parametric
down-conversion source: a cheap heuristic attack, on the verification problem.

## Killers introduced by this lane

- **K-TC1 (ghosts).** `R = 1` certifies a `K`-fixed ray; that set is a real form of `ker H_N` of
  real dimension `HF(N)`, contains a ghost for every conjugate pair, and is nonzero when `V_R = {}`.
- **K-TC2 (dimension is the only invariant).** `(ker H_N, K) ~ (C^{HF}, conjugation)` unitarily; any
  real-point statistic must use the algebra action.
- **K-TC3 (no state emerges).** The full-`N` projection consumes both copies; only the `k`-pair
  filter outputs a state, and it correlates the copies rather than filtering one.
- **K-TC4 (unbounded witness).** `||SWAP^{T_2}|| = M_N`, so the full witness costs `M_N` shots unless
  one drops to one-pair observables or a conjugated preparation circuit.
- **K-TC5 (pairwise costs more).** `(n+1)^N/M_N` = 5840 at `n=2, N=12`.

These five are proposed as one further claim row, **C-NEW-TC-COST** (CONJECTURE; depends-on
D-two-copy-real-filter, D-pairing-state, D-input-model; where-proved this section; where-tested part
F): for every `N, n` the collective pairing measurement accepts `psi x psi` with probability
`R(psi)/M_N` and the pairwise Bell measurement with `R(psi)/(n+1)^N`; ancilla-free linear-optical
Bell analysis contributes at most `1/2` per pair; `||SWAP^{T_2}|| = M_N`, so the full witness admits
no bounded-observable estimator; the projection consumes both copies for one bit. Traps: hidden
postselection; K-RV15; a measurement read as a filter.

## Proposed definitions

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

## Proposed claim rows

MERGE PROPOSAL (`claims/CLAIMS.md`), all CONJECTURE per L1; where-tested is
`checkers/explore/twocopy_real_filter.py`, where-proved is this memo.

### C-NEW-TC-RANK-ONE
- statement: For every homogeneous ideal `I` and every `N`, the compression
  `F_N = (P_0 x P_0)(|Phi_N><Phi_N|/M_N)(P_0 x P_0)` onto `ker H_N x ker H_N` has rank at most one,
  range spanned by `(P_0 x P_0)|Phi_N>`, and unique nonzero eigenvalue
  `Tr(P_0 P_0^T)/M_N = (sum_i tau_i^2)/M_N`, the `tau_i` being the cosines of the principal angles
  between `ker H_N` and its complex conjugate; for real generators every `tau_i = 1`, the eigenvalue
  is `HF_{R/I}(N)/M_N`, the eigenvector the ground-space pairing state.
- depends-on: D-pairing-state, D-two-copy-real-filter, D-projectors, D-ground-space,
  D-takagi-factorisation; where-proved: Proposition TC1; where-tested: part A, `N = 2..8`, four
  ideals in `P^2`. Relevance/traps: settles what the construction is as a linear operator; guards
  against reading a nonlinear witness as an operator spectrum, and against changing the output.

### C-NEW-TC-NO-REAL-INFORMATION
- statement: For every pair of conjugations on complex Hilbert spaces of equal finite dimension there
  is a unitary intertwiner; hence every unitary invariant of `(ker H_N, K)` is a function of
  `HF_{R/I}(N)`, and no construction built from `P_0` and `|Phi_N>` alone decides whether `V_R(I)` is
  empty. In particular `z0z1 - z2^2` (real locus `RP^1`) and `z0^2+z1^2+z2^2` (real locus empty) have
  identical `F_N` spectra at every `N`.
- depends-on: D-real-structure, D-two-copy-real-filter, C-NEW-TC-RANK-ONE, C-256; where-proved:
  Proposition TC2; where-tested: part A, difference 3.55e-15 at `N = 2..8`. Relevance/traps: closes
  the strong form of the proposal (real-point information needs the algebra action, not the real
  structure); guards against mistaking a real form for a subspace, and K-RV2.

### C-NEW-TC-COHERENT-RESPONSE
- statement: For every unit `p in C^{n+1}` and every `N`, `R(|p>^{x N}) = |p^T p|^{2N}` and
  `|p^T p| = 2 max_{x real, |x|=1}|<x|p>|^2 - 1 = cos 2t` with `t` the Fubini-Study distance from
  `[p]` to `RP^n`; a complex point at angle `t` is therefore suppressed as
  `exp(-4Nt^2(1+O(t^2)))`, so the filter's angular resolution about `RP^n` is `Theta(N^{-1/2})`.
- depends-on: D-coherent-state, D-realness-witness; where-proved: Statement; where-tested: part B,
  four points, `N = 2..10`, agreement to 1e-9. Relevance/traps: the exact filter rate and its
  resolution limit; guards against confusing exponential filter strength with exponential separation
  of nearby points.

### C-NEW-TC-GHOST
- statement: For every real ideal `I`, every `N` and every `p in V(I)`, the vector
  `|p>^{x N} + |conj(p)>^{x N}` lies in `ker H_N` and has `R = 1` exactly, and the `K`-fixed subset
  of `ker H_N` is a real subspace of real dimension `HF_{R/I}(N)`, nonzero even when `V_R(I) = {}`;
  so `R(psi) = 1` certifies that the ray is real, not that `psi` is a real point's coherent state.
- depends-on: D-realness-witness, D-coherent-state, D-real-structure, C-255; where-proved: K-TC1;
  where-tested: part C (`R = 1.000000000000` for the ghost; `R = 1` real ground vectors for both
  real-point-free conics). Relevance/traps: refutes "postselecting prepares real points"; real
  vector versus real label; K-RV1, K-RV2.

### C-NEW-TC-FRAME-COUNT
- statement: For every real zero-dimensional radical ideal `I` in the stable range, every `N` at
  which the coherent states of `V(I)` form a basis of `ker H_N`, and conjugation-compatible unit
  representatives `x_1..x_D` of `V(I)`, the Hermitian and bilinear coherent Gram matrices
  `Gh_{ab} = <x_a|x_b>^N` and `G_{ab} = (x_a^T x_b)^N` satisfy `G = P_sigma Gh` with `P_sigma` the
  permutation matrix of complex conjugation on `V(I)`; hence `Tr(Gh^{-1}G) = #V_R(I)` and
  `Tr(Gh^{-1}Gh) = D`.
- depends-on: D-coherent-gram-matrix, D-pairing-state, D-coherent-state,
  D-real-locus-and-real-radical; where-proved: Algorithmic content; where-tested: part D, three
  binary quartics with 4, 2, 0 real roots, `N = 3,5,8,12,20`, exact integers; mutation `G -> Gh`
  returns `4 = D`. Relevance/traps: names the extra structure a real count needs (the coherent frame
  = the compressed multiplications) and its cost `Gh^{-1}`; frame dependence of the trace of an
  antiunitary; phase conventions on projective representatives; K-RV6.

### C-NEW-TC-ONE-PAIR-CERTIFICATE
- statement: For every real ideal `I`, every `N >= max_j m_j`, and every `psi in ker H_N`, the two
  one-particle two-copy observables `Tr(rho_1^2)` and `Tr(rho_1 rho_1^T) = <C^dag C>/N^2` with
  `C = sum_j a_j b_j` both equal `1` if and only if `psi = |p>^{x N}` for some `p` with
  `[p] in V_R(I)`; both have operator norm at most one and are estimable to additive `eps` with
  `O(1/eps^2)` copies and no postselection.
- depends-on: D-one-particle-reduced-state, D-realness-witness, D-coherent-state, D-ground-space;
  where-proved: Algorithmic content; where-tested: parts C and F (real point `(1,1)`, complex point
  `(1, 0.111)`, ghost `(0.557, 0.557)`, real ground vector `(0.387, 0.387)`). Relevance/traps: a
  polynomial-cost verifier with a spinor-BEC / parametric-source realisation, a certification
  product not a speedup; verification versus preparation; robustness (`1-eps` version open); K-RV10.

## Questions for TJO

1. **Does the verifier count as a product?** C-NEW-TC-ONE-PAIR-CERTIFICATE is a polynomial-cost,
   two-copy, linear-optics-native check that a supplied ground state is a real point of `V(I)`; it
   verifies, it does not find. PRD Q4 and Q10(b) ask this in general and this lane supplies a
   concrete instance. Recommendation: yes as an instrument and as arm E's honest hardware
   demonstration; no as a north-star hit.
2. **Amend Route 2 of `scouting/real-variety.md` in lockstep (L2)?** Its 1/5 verdict is right about
   the filter, but its stated reason (for a circuit-prepared state "the amplitudes are classically
   specified") is wrong. With the one-pair certificate and `#V_R = Tr(Gh^{-1}G)`, Route 2 is 2/5 for
   certification and 1/5 for search. Amend there, or leave the correction here only?
3. **Fund the robustness question?** The certificate is exact as stated. The useful version: if
   `Tr(rho_1^2) >= 1-eps`, `Tr(rho_1 rho_1^T) >= 1-eps` and `<psi|H_N|psi> <= delta`, how close is
   `[p]` to `V_R(I)` in Fubini-Study distance, with what dependence on `N`, `Delta_N` and the
   D-condition-number? One analytic day; it is the difference between a demo and a theorem.
   Recommendation: yes, paired with PRD Q10(d).
4. **Is `#V_R = Tr(Gh^{-1}G)` worth its own lane?** It is exact and elementary and names the
   classical object the quantum side must produce. Two algorithmic forms: a QSVT construction of
   `Gh^{-1/2} G Gh^{-1/2}` from Macaulay access, or a DQC1-style normalised trace estimate
   (D-dqc1-style-estimate); both inherit K-RV6. Recommendation: fold into the C-257/C-258 Hermite
   lane, the same passage, not a new lane.
5. **Accept C-NEW-TC-NO-REAL-INFORMATION as closing "real symmetry via two copies"?** It closes the
   strong form (a spectral selector), leaving the weak forms open: the ideal-realness test
   `(sum_i tau_i^2)/HF`, the one-pair certificate, the `k`-pair filter as a preparation primitive.
   Recommendation: enter the seven rows, mark the strong form closed in PRD arm E, keep the
   certificate open.
6. **Reference budget (PRD Q9).** Seven references, all resolved this session, none `[UNVERIFIED]`:
   arXiv:1801.05123 / DOI 10.1088/1751-8121/aabe9c; arXiv:2007.14847 / PRL 126 090401;
   arXiv:0810.1923 / PRL 102 020505; arXiv:2101.10873 / DOI 10.1038/s41586-021-04160-4;
   arXiv:quant-ph/0007058 / DOI 10.1007/s003400000484; arXiv:quant-ph/0203016 / PRL 88 217901;
   arXiv:2007.06305 / PRL 125 200501. A few minutes each: recommend the half-day pass on the
   classical memo's 63.
