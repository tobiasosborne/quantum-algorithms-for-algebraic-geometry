"""EXPLORATION ONLY -- deliberately excluded from run_all.sh (PRD arm B lane,
brief `briefs/lane-koszul-betti.md`; repaired after verdict
`verdicts/koszul-betti-r1.md`, objections O7, O8, O12).

Supersymmetric Koszul Laplacian for graded Betti numbers.

OBJECTS (D-fock-space conventions C1, C2, C3, C6, C8).  Ideals below have
integer coefficients.  Every `Delta_N` printed is the Macaulay gap of the
presentation AS WRITTEN (unit coefficients on monomials), the same departure
from C5 that `checkers/README.md` records for the whole suite.

  W_N   = ker H_N = (I_N)^perp                        (D-ground-space, C-008)
  P     = (+)_N P_{0,N},  Phat = P (x) 1
  Q     = sum_k a_k (x) c_k^dag  on the FINITE-PARTICLE CORE of F (x) Lambda
  q     = Q Phat = Phat Q Phat   (well defined: W is a_k-invariant, since
          <a_k u, h> = <u, z_k h> = 0 for u in (I_N)^perp, h in I_{N-1})
  q^dag = sum_k Z_k (x) c_k,  Z_k = P_0 a_k^dag P_0  (D-compressed-multiplication)
  L_W   = q q^dag + q^dag q   on block (fermion number i, boson degree N)
  X     = Phat Q (1 - Phat)   -- CONSTRUCTED here, not inferred (O12)

CENTRAL IDENTIFICATION (part A):

      nullity( L_W | block (i,N) )  =  beta_{i, i+N}(R/I),

because (W (x) Lambda, q) is the CONJUGATE-linear dual (O10) of the Koszul
complex K_.(z_0..z_n ; R/I); dimensions are unaffected.  Betti information
lives only at N = j - i <= reg(R/I) (O1: the condition is on N, not on j).

WHAT IS CHECKED (each prints OK/MISMATCH; exit 1 on any MISMATCH, 2 on an
unexpected exception):

  A   nullity(L_W|(i,N)) against TWO independent references: (1) exact Koszul
      ranks over GF(p), p = 10^9+7 -- exact in characteristic p, and the tested
      examples are characteristic-independent (O12); (2) a hard-coded FIXTURE
      Betti table per ideal, asserted from the literature, so that mutating an
      ideal cannot make the script verify a new ideal against itself (O12).
      Also: L_W is PSD to tolerance, and nullity uses |ev| < TOL (O12).
  B   Q Q^dag + Q^dag Q = (N+i)*1 on the full space, hence Phat L Phat =
      (N+i) Phat has NO kernel; and L_W = (N+i)1 - X X^dag with X built
      explicitly from Phat Q (1-Phat), not defined as (N+i)1 - L_W (O12).
  C   Betti gap g_{i,N} = min{ev : ev > TOL}, normalised g/(N+i), against
      Delta_N.  NOTE (O8): adjacent blocks do NOT share full nonzero spectra;
      what is shared is the nonzero singular-value set of each single
      differential q_{i,N}: spec^{>0}(q^dag q)|(i,N) = spec^{>0}(q q^dag)|(i+1,N-1).
      That equality is what is tested here.
  D   Hochster: for a Stanley-Reisner ideal the SQUAREFREE multidegree-sigma
      summand of block (i,N), |sigma| = i+N, is the reduced (N-1)-chain
      Laplacian of Delta|_sigma; the total block also carries non-squarefree
      multidegrees (O4), whose dimension is printed.
  E   COUNTERFAMILY for the gap question (O7).  For the m-cycle Stanley-Reisner
      ideal, m >= 4:  Delta_2 = 1 for every m, while the squarefree-sigma
      summand (sigma = all m vertices) of block (i = m-2, N = 2) is the edge
      Laplacian d_1^dag d_1 of the cycle graph, with smallest nonzero eigenvalue
      exactly 2 - 2 cos(2 pi / m) -> 0.  Checked against the closed form for
      m = 4..12, and against the TOTAL-block gap for m = 4..8 (where the two
      agree, but the total-block statement is observed, not proved).
  F   generator-Koszul supercharge Q_f = sum_j M_{f_j} (x) c_j: its fermion-
      number-zero Laplacian block is EXACTLY the seed H_N, and its higher-block
      nullities differ from beta_{i,j}(R/I) (this makes mutation M4 real).
  G   normalised Betti fraction for complete intersections, with the two
      asymptotic regimes (fixed i / growing i) stated separately (O6), and the
      block dimension printed alongside so the polynomial-dimension regime is
      visible.  Dimensions are recomputed by an independent route (O19).
  H   O17: the AMBIENT normalised fraction is the normalised trace of the
      HARMONIC projector extended by zero, obtained by filtering
      Ltilde = L_W + (N+i)(1 - Phat_N); the zero-eigenvalue fraction of L_W
      extended by zero is a DIFFERENT and larger number, (M_N-h_N)b + beta.
      O18: rebuilding the block without the adjacent-degree projector P_{0,N+1}
      collapses it to the scalar j, so adjacent-degree access is necessary.
      O21: h_N/M_N is 1, not exponentially small, for n generic degree-(n+1)
      forms in P^n at N = n -- also a zero-dimensional square system.

MUTATIONS (run in-process by `mutations()`, each must come out RED):
  M1  drop the compression: use Phat L Phat instead of L_W.
  M2  wrong index convention: compare nullity(i,N) with beta_{i,N}.
  M3  drop the fermionic sign (-1)^{#{l in S : l<k}} in c_k^dag.
  M4  use the generator-Koszul supercharge of part F instead of the variable one.
Registration of these in `checkers/MUTATIONS.md` is a merge action for the
orchestrator: this lane may not edit that file.

Run: timeout 900 python3 explore/koszul_laplacian.py
"""
import math
import os
import sys
import time

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import bf  # noqa: E402
import ideals  # noqa: E402

TOL = 1e-8
P_MOD = bf.P_MOD
FAILS = []
M4_RED = None   # set by generator_koszul_section(); consumed by mutations()


def check(ok, msg):
    if not ok:
        FAILS.append(msg)
    return "OK" if ok else "MISMATCH"


# ------------------------------------------------------------ GF(p) reference

def rref_mod_p(rows, ncols, p=P_MOD):
    """Reduced row echelon form over GF(p).  Returns (R, pivots)."""
    if not rows:
        return np.zeros((0, ncols), dtype=np.int64), []
    M = np.array([[int(x) % p for x in r] for r in rows], dtype=np.int64)
    nr = M.shape[0]
    r, pivots = 0, []
    for c in range(ncols):
        piv = None
        for i in range(r, nr):
            if M[i, c]:
                piv = i
                break
        if piv is None:
            continue
        M[[r, piv]] = M[[piv, r]]
        M[r] = (M[r] * pow(int(M[r, c]), p - 2, p)) % p
        col = M[:, c].copy()
        col[r] = 0
        nz = np.nonzero(col)[0]
        if len(nz):
            M[nz] = (M[nz] - col[nz][:, None] * M[r][None, :]) % p
        pivots.append(c)
        r += 1
        if r == nr:
            break
    return M[:r], pivots


class Quotient:
    """Standard-monomial model of (R/I)_M, M = 0..Mmax, exact over GF(p)."""

    def __init__(self, nv, gens, Mmax, p=P_MOD):
        self.nv, self.p = nv, p
        self.nonpiv, self.pos, self.red = {}, {}, {}
        for M in range(0, Mmax + 1):
            ncols = bf.dim_h(nv, M)
            R, piv = rref_mod_p(bf.macaulay_rows(gens, M), ncols, p)
            pivset = set(piv)
            nonpiv = [c for c in range(ncols) if c not in pivset]
            pos = {c: t for t, c in enumerate(nonpiv)}
            red = {c: {pos[c]: 1} for c in nonpiv}
            for ri, c in enumerate(piv):
                red[c] = {pos[q]: (-int(R[ri, q])) % p
                          for q in nonpiv if int(R[ri, q]) % p}
            self.nonpiv[M], self.pos[M], self.red[M] = nonpiv, pos, red

    def hf(self, M):
        return 0 if M < 0 else len(self.nonpiv[M])


def subsets(nv, i):
    return [tuple(k for k in range(nv) if mask >> k & 1)
            for mask in range(1 << nv) if bin(mask).count("1") == i]


def koszul_rank(quo, nv, i, N):
    """rank over GF(p) of d : (R/I)_N (x) Lambda^i -> (R/I)_{N+1} (x) Lambda^{i-1}."""
    if i <= 0 or N < 0 or quo.hf(N) == 0:
        return 0
    S_src = subsets(nv, i)
    S_tgt = {s: t for t, s in enumerate(subsets(nv, i - 1))}
    hf1 = quo.hf(N + 1)
    if hf1 == 0 or not S_tgt:
        return 0
    ncols = hf1 * len(S_tgt)
    monos_N, idx_N1 = bf.monomials(nv, N), bf.mono_index(nv, N + 1)
    rows = []
    for c in quo.nonpiv[N]:
        m = monos_N[c]
        for S in S_src:
            v = [0] * ncols
            for r, k in enumerate(S):
                sign = (-1) ** r
                tgt = tuple(m[t] + (1 if t == k else 0) for t in range(nv))
                off = S_tgt[tuple(x for x in S if x != k)] * hf1
                for coord, coeff in quo.red[N + 1][idx_N1[tgt]].items():
                    v[off + coord] = (v[off + coord] + sign * coeff) % quo.p
            rows.append(v)
    return bf.rank_mod_p(rows, quo.p)


def betti(quo, nv, i, N):
    """beta_{i,i+N}(R/I) over GF(p) = dim K_i - rank d_i - rank d_{i+1}."""
    dim = quo.hf(N) * math.comb(nv, i)
    if dim == 0:
        return 0
    return dim - koszul_rank(quo, nv, i, N) - koszul_rank(quo, nv, i + 1, N - 1)


# ------------------------------------------------------------------ Fock side

def kernel_basis(gens, nv, N, kerdim):
    """(dim R_N) x kerdim orthonormal basis of ker H_N in the |k> ONB."""
    MN = bf.dim_h(nv, N)
    if kerdim == 0:
        return np.zeros((MN, 0), dtype=complex)
    A = bf.stacked_A(gens, N)
    if A.shape[0] == 0:
        return np.eye(MN, dtype=complex)
    _, _, Vh = np.linalg.svd(A)
    return Vh[MN - kerdim:].conj().T


def monomial_kernel_basis(quo, nv, N):
    """For a MONOMIAL ideal: the standard monomials are already an ONB of
    ker H_N, so the block carries the multigrading in its basis labels."""
    MN = bf.dim_h(nv, N)
    cols = quo.nonpiv[N]
    B = np.zeros((MN, len(cols)), dtype=complex)
    for t, c in enumerate(cols):
        B[c, t] = 1.0
    return B


def ak_matrices(nv, N):
    if N <= 0:
        return [np.zeros((0, bf.dim_h(nv, N)), dtype=complex) for _ in range(nv)]
    return [bf.annihilation_matrix({bf.emono(nv, [k]): 1}, N) for k in range(nv)]


def cdag_matrices(nv, i, sign=True):
    src = subsets(nv, i)
    tgt = {s: t for t, s in enumerate(subsets(nv, i + 1))}
    out = []
    for k in range(nv):
        C = np.zeros((len(tgt), len(src)))
        for c, S in enumerate(src):
            if k in S:
                continue
            sg = (-1) ** sum(1 for l in S if l < k) if sign else 1
            C[tgt[tuple(sorted(S + (k,)))], c] = sg
        out.append(C)
    return out


def Q_block(Bs, nv, i, N, sign=True):
    """q : W_N (x) Lambda^i -> W_{N-1} (x) Lambda^{i+1}; kron = boson (x) fermion."""
    kd_s = Bs[N].shape[1]
    kd_t = Bs[N - 1].shape[1] if (N - 1) in Bs else 0
    ns, nt = math.comb(nv, i), math.comb(nv, i + 1)
    if N <= 0 or 0 in (kd_s, kd_t, ns, nt):
        return np.zeros((kd_t * nt, kd_s * ns), dtype=complex)
    A, C = ak_matrices(nv, N), cdag_matrices(nv, i, sign)
    out = np.zeros((kd_t * nt, kd_s * ns), dtype=complex)
    for k in range(nv):
        out += np.kron(Bs[N - 1].conj().T @ A[k] @ Bs[N], C[k])
    return out


def L_block(Bs, nv, i, N, sign=True):
    dim = Bs[N].shape[1] * math.comb(nv, i)
    L = np.zeros((dim, dim), dtype=complex)
    if dim == 0:
        return L
    Qout = Q_block(Bs, nv, i, N, sign)
    if Qout.size:
        L += Qout.conj().T @ Qout
    if i >= 1 and (N + 1) in Bs:
        Qin = Q_block(Bs, nv, i - 1, N + 1, sign)
        if Qin.size:
            L += Qin @ Qin.conj().T
    return L


def X_block(Bs, nv, i, N):
    """X = Phat Q (1 - Phat) restricted to I_{N+1} (x) Lambda^{i-1} -> W_N (x) Lambda^i,
    CONSTRUCTED from the ambient Q and the complementary projector (O12)."""
    if i < 1 or (N + 1) not in Bs:
        return np.zeros((Bs[N].shape[1] * math.comb(nv, i), 0), dtype=complex)
    Bi = np.eye(bf.dim_h(nv, N + 1), dtype=complex) - Bs[N + 1] @ Bs[N + 1].conj().T
    amb = {N: np.eye(bf.dim_h(nv, N), dtype=complex),
           N + 1: np.eye(bf.dim_h(nv, N + 1), dtype=complex)}
    Qfull = Q_block(amb, nv, i - 1, N + 1)          # ambient (i-1,N+1) -> (i,N)
    Pl = np.kron(Bs[N].conj().T, np.eye(math.comb(nv, i)))
    Pr = np.kron(Bi, np.eye(math.comb(nv, i - 1)))
    return Pl @ Qfull @ Pr


def spec(L):
    return np.linalg.eigvalsh((L + L.conj().T) / 2)


def nullity_and_gap(L):
    ev = spec(L)
    if ev.size == 0:
        return 0, float("nan"), 0.0
    nul = int((np.abs(ev) < TOL).sum())
    nz = ev[ev > TOL]
    return nul, (float(nz.min()) if nz.size else float("nan")), float(ev.min())


# --------------------------------------------------- literature fixture tables

FIXTURES = {
    "twisted cubic": {(0, 0): 1, (1, 2): 3, (2, 3): 2},
    "2 int quadrics CI": {(0, 0): 1, (1, 2): 2, (2, 4): 1},
    "(z0^2,z0z1,z1^3)": {(0, 0): 1, (1, 2): 2, (1, 3): 1, (2, 3): 1, (2, 4): 1},
    "(z0^2,z0z1,z1^2)": {(0, 0): 1, (1, 2): 3, (2, 3): 2},
    "rat normal quartic": {(0, 0): 1, (1, 2): 6, (2, 3): 8, (3, 4): 3},
    "5-cycle SR": {(0, 0): 1, (1, 2): 5, (2, 3): 5, (3, 5): 1},
}


def int_random_form(nv, deg, rng, lo=-4, hi=5):
    f = {m: int(rng.integers(lo, hi)) for m in bf.monomials(nv, deg)}
    f = {m: c for m, c in f.items() if c}
    return f or {bf.monomials(nv, deg)[0]: 1}


# ------------------------------------------------------------------ main parts

def run_ideal(key, name, nv, gens, Nmax, hf_expected=None, monomial=False):
    print("=" * 78)
    print(f"{name}   ({nv} variables, {len(gens)} generators)   N = 0..{Nmax}")
    print("=" * 78)
    t0 = time.time()
    quo = Quotient(nv, gens, Nmax + 2)
    Bs, delta = {}, {}
    for N in range(0, Nmax + 2):
        kd = quo.hf(N)
        if hf_expected is not None and kd != hf_expected(N):
            FAILS.append(f"{name}: GF(p) HF({N})={kd} != closed form {hf_expected(N)}")
        Bs[N] = (monomial_kernel_basis(quo, nv, N) if monomial
                 else kernel_basis(gens, nv, N, kd))
        if kd and N >= 1:
            g = bf.gap_from_spectrum(bf.spectrum(gens, N), kd)
            delta[N] = g if g is not None else float("nan")

    fix = FIXTURES[key]
    print("\n(A) nullity of L_W | (i,N)  vs  GF(p) beta_{i,i+N}  vs  literature fixture")
    print(f"{'i':>2} {'N':>2} {'j':>3} {'dimblk':>7} {'null':>5} {'GF(p)':>6} {'fix':>4} "
          f"{'':>9} {'g_{i,N}':>9} {'g/(N+i)':>8} {'lam_min':>10} {'beta/dim':>10}")
    reg, gaps = -1, {}
    for N in range(0, Nmax + 1):
        for i in range(0, nv + 1):
            dim = quo.hf(N) * math.comb(nv, i)
            if dim == 0:
                continue
            nul, g, lmin = nullity_and_gap(L_block(Bs, nv, i, N))
            b = betti(quo, nv, i, N)
            bf_fix = fix.get((i, i + N), 0)
            if b > 0:
                reg = max(reg, N)
            gaps.setdefault(i, []).append((N, g))
            ok = (nul == b == bf_fix) and lmin > -TOL
            tag = check(ok, f"{name}: (i={i},N={N}) null={nul} GF(p)={b} fix={bf_fix} "
                            f"lam_min={lmin:.2e}")
            if b or bf_fix or N <= 3 or tag == "MISMATCH":
                print(f"{i:>2} {N:>2} {i+N:>3} {dim:>7} {nul:>5} {b:>6} {bf_fix:>4} "
                      f"{tag:>9} {g:>9.4f} "
                      f"{(g/(N+i) if N+i else float('nan')):>8.4f} {lmin:>10.2e} "
                      f"{b/dim:>10.3e}")
    print(f"  reg(R/I) = max(j-i : beta != 0) = {reg}   (so reg(I) = {reg+1});"
          f"  the Betti support condition is N = j-i <= reg(R/I), NOT j <= reg")
    bad = []
    for N in range(reg + 1, Nmax + 1):
        for i in range(0, nv + 1):
            if quo.hf(N) == 0:
                continue
            if nullity_and_gap(L_block(Bs, nv, i, N))[0] != 0:
                bad.append((i, N))
    check(not bad, f"{name}: nonzero nullity beyond reg at {bad}")
    print(f"  prediction 'nullity = 0 for every N > reg(R/I)' to N = {Nmax}: "
          f"{'OK' if not bad else 'MISMATCH ' + str(bad)}")

    print("\n(B) uncompressed Laplacian is the scalar N+i; X constructed explicitly")
    worst, worstX, worstP = 0.0, 0.0, 0.0
    for N in range(0, min(Nmax, 4) + 1):
        amb = {M: np.eye(bf.dim_h(nv, M), dtype=complex)
               for M in (N - 1, N, N + 1) if M >= 0}
        for i in range(0, nv + 1):
            Lf = L_block(amb, nv, i, N)
            if Lf.shape[0]:
                worst = max(worst, float(np.abs(Lf - (N + i) * np.eye(Lf.shape[0])).max()))
            if quo.hf(N) == 0:
                continue
            Lw = L_block(Bs, nv, i, N)
            Xb = X_block(Bs, nv, i, N)
            rhs = (N + i) * np.eye(Lw.shape[0]) - (Xb @ Xb.conj().T if Xb.size
                                                   else 0 * Lw)
            worstX = max(worstX, float(np.abs(Lw - rhs).max()))
            Phat = np.kron(Bs[N] @ Bs[N].conj().T, np.eye(math.comb(nv, i)))
            comp = Phat @ L_block(amb, nv, i, N) @ Phat
            worstP = max(worstP, float(np.abs(comp - (N + i) * Phat).max()))
    check(worst < 1e-9, f"{name}: full L != (N+i)*1, err {worst:.2e}")
    check(worstX < 1e-9, f"{name}: L_W != (N+i)1 - X X^dag, err {worstX:.2e}")
    check(worstP < 1e-9, f"{name}: Phat L Phat != (N+i) Phat, err {worstP:.2e}")
    print(f"  max |Q Q^dag + Q^dag Q - (N+i)1|            = {worst:.2e}  "
          f"{'OK' if worst < 1e-9 else 'MISMATCH'}")
    print(f"  max |L_W - ((N+i)1 - X X^dag)|, X built     = {worstX:.2e}  "
          f"{'OK' if worstX < 1e-9 else 'MISMATCH'}")
    print(f"  max |Phat L Phat - (N+i) Phat|              = {worstP:.2e}  "
          f"{'OK' if worstP < 1e-9 else 'MISMATCH'}  "
          f"=> nullity of P_0 L P_0 on range(Phat) is 0")

    print("\n(C) Betti gap g_{i,N} and Macaulay gap Delta_N versus N")
    print(f"{'N':>2} {'Delta_N':>10} " +
          " ".join(f"{'g(i=%d)' % i:>10}" for i in range(0, min(nv, 4) + 1)))
    for N in range(1, Nmax + 1):
        row = f"{N:>2} {delta.get(N, float('nan')):>10.4f} "
        for i in range(0, min(nv, 4) + 1):
            gg = [x for x in gaps.get(i, []) if x[0] == N]
            row += f"{gg[0][1] if gg else float('nan'):>10.4f} "
        print(row)
    # O8: the correct pairing statement, tested
    worstS = 0.0
    for N in range(1, Nmax + 1):
        for i in range(0, nv):
            Qb = Q_block(Bs, nv, i, N)
            if Qb.size == 0:
                continue
            s1 = np.sort(spec(Qb.conj().T @ Qb))
            s2 = np.sort(spec(Qb @ Qb.conj().T))
            a = s1[s1 > TOL]
            b_ = s2[s2 > TOL]
            if a.size == b_.size and a.size:
                worstS = max(worstS, float(np.abs(a - b_).max()))
            elif a.size != b_.size:
                FAILS.append(f"{name}: singular pairing count mismatch at (i={i},N={N})")
    check(worstS < 1e-8, f"{name}: singular-value pairing of q_(i,N) fails, {worstS:.2e}")
    print(f"  O8 check: spec^>0(q^dag q)|(i,N) = spec^>0(q q^dag)|(i+1,N-1) for every "
          f"single differential, max deviation {worstS:.2e}  "
          f"{'OK' if worstS < 1e-8 else 'MISMATCH'}")
    print("  (adjacent BLOCK Laplacians do NOT share full nonzero spectra: e.g. the "
          "twisted\n   cubic at j=3 has g(0,3)=3.0000 but g(1,2)=1.3333)")
    print(f"  wall {time.time()-t0:.1f}s")
    return quo, Bs, reg


# ------------------------------------------------ (D) Hochster / (E) cycle gaps

def cycle_complex(m):
    faces = [()] + [(v,) for v in range(m)]
    edges = sorted({tuple(sorted((v, (v + 1) % m))) for v in range(m)})
    faces += edges
    gens = [{bf.emono(m, [a, b]): 1} for a in range(m) for b in range(a + 1, m)
            if (a, b) not in set(edges)]
    return faces, gens, edges


def reduced_homology(faces, sigma, p=P_MOD):
    S = set(sigma)
    F = [f for f in faces if set(f) <= S]
    by_dim = {}
    for f in F:
        by_dim.setdefault(len(f) - 1, []).append(f)
    for k in by_dim:
        by_dim[k].sort()
    kmax = max(by_dim) if by_dim else -1
    idx = {k: {f: t for t, f in enumerate(v)} for k, v in by_dim.items()}
    rank = {}
    for k in range(0, kmax + 1):
        src, tgt = by_dim.get(k, []), by_dim.get(k - 1, [])
        if not src or not tgt:
            rank[k] = 0
            continue
        rows = []
        for f in src:
            v = [0] * len(tgt)
            for r in range(len(f)):
                v[idx[k - 1][f[:r] + f[r + 1:]]] = ((-1) ** r) % p
            rows.append(v)
        rank[k] = bf.rank_mod_p(rows, p)
    return {k: len(by_dim.get(k, [])) - rank.get(k, 0) - rank.get(k + 1, 0)
            for k in range(0, kmax + 1)}


def multidegree_split(quo, nv, i, N):
    """Labels (monomial exponent, fermion subset) of the block basis, in the
    monomial_kernel_basis ordering, with their total multidegree."""
    monos = bf.monomials(nv, N)
    lab = []
    for c in quo.nonpiv[N]:
        a = monos[c]
        for S in subsets(nv, i):
            mu = tuple(a[t] + (1 if t in S else 0) for t in range(nv))
            lab.append(mu)
    return lab


def hochster_section():
    print("=" * 78)
    print("(D) Stanley-Reisner: the SQUAREFREE multidegree summands are simplicial")
    print("    Laplacians (Hochster); the total block also carries non-squarefree")
    print("    multidegrees, which the quantum-TDA theorems do NOT cover (O4).")
    print("=" * 78)
    for m in (4, 5, 6, 7):
        faces, gens, _ = cycle_complex(m)
        Nmax = 3
        quo = Quotient(m, gens, Nmax + 2)
        Bs = {N: monomial_kernel_basis(quo, m, N) for N in range(0, Nmax + 2)}
        print(f"\n  {m}-cycle, I_Delta = {len(gens)} quadrics in P^{m-1}, "
              f"HF(N) = {[quo.hf(N) for N in range(0, 4)]}")
        print(f"  {'i':>2} {'N':>2} {'j':>2} {'dimblk':>7} {'sqfree':>7} {'null':>5} "
              f"{'GF(p)':>6} {'Hoch':>5} {'':>9} {'g_{i,N}':>9} {'beta/dim':>10}")
        for N in range(1, Nmax + 1):
            for i in range(1, m + 1):
                dim = quo.hf(N) * math.comb(m, i)
                if dim == 0:
                    continue
                b = betti(quo, m, i, N)
                if b == 0:
                    continue
                nul, g, _ = nullity_and_gap(L_block(Bs, m, i, N))
                hb = sum(reduced_homology(faces, s).get(N - 1, 0)
                         for s in subsets(m, i + N))
                nsq = sum(1 for mu in multidegree_split(quo, m, i, N)
                          if max(mu) <= 1)
                tag = check(nul == b == hb,
                            f"{m}-cycle: (i={i},N={N}) null={nul} beta={b} Hoch={hb}")
                print(f"  {i:>2} {N:>2} {i+N:>2} {dim:>7} {nsq:>7} {nul:>5} {b:>6} "
                      f"{hb:>5} {tag:>9} {g:>9.4f} {b/dim:>10.3e}")


def counterfamily_section():
    print("=" * 78)
    print("(E) COUNTERFAMILY (O7): m-cycle Stanley-Reisner ideals, m = 4..12.")
    print("    PROVED: the squarefree-sigma summand (sigma = all m vertices) of block")
    print("    (i = m-2, N = 2) is the edge Laplacian d_1^dag d_1 of the cycle graph,")
    print("    nullity 1 = b_1(C_m), smallest nonzero eigenvalue 2 - 2 cos(2 pi/m).")
    print("    Delta_2 = 1 for every m.  Hence no lower bound g >= phi(Delta_N) can hold.")
    print("=" * 78)
    print(f"  {'m':>3} {'Delta_2':>8} {'g_sqfree':>10} {'2-2cos(2pi/m)':>14} {'':>9} "
          f"{'g_total':>9} {'agree?':>7} {'g_sq/(N+i)':>11}")
    for m in range(4, 13):
        faces, gens, edges = cycle_complex(m)
        quo = Quotient(m, gens, 4)
        d2 = bf.gap_from_spectrum(bf.spectrum(gens, 2), quo.hf(2))
        i, N = m - 2, 2
        # squarefree sigma = all vertices: basis is the edge set, Laplacian = d1^dag d1
        B = np.zeros((len(edges), m))
        for e, (a, b_) in enumerate(edges):
            B[e, a], B[e, b_] = 1.0, -1.0
        Lsq = B @ B.T                       # d_1 d_1^dag on 1-chains
        evs = np.sort(np.linalg.eigvalsh(Lsq))
        nulsq = int((np.abs(evs) < TOL).sum())
        gsq = float(evs[evs > TOL].min())
        closed = 2 - 2 * math.cos(2 * math.pi / m)
        okc = abs(gsq - closed) < 1e-9 and nulsq == 1 and abs(d2 - 1.0) < 1e-9
        check(okc, f"{m}-cycle: sqfree gap {gsq} vs {closed}, nullity {nulsq}, "
                   f"Delta_2 {d2}")
        gtot = float("nan")
        agree = "n/a"
        if m <= 8:
            Bs = {NN: monomial_kernel_basis(quo, m, NN) for NN in range(0, 4)}
            _, gtot, _ = nullity_and_gap(L_block(Bs, m, i, N))
            agree = "yes" if abs(gtot - closed) < 1e-8 else "NO"
        print(f"  {m:>3} {d2:>8.4f} {gsq:>10.6f} {closed:>14.6f} "
              f"{'OK' if okc else 'MISMATCH':>9} {gtot:>9.6f} {agree:>7} "
              f"{gsq/(N+i):>11.6f}")
    print("  Delta_2 = 1 for all m (monic monomial generators, H_2 diagonal) while the")
    print("  squarefree Betti gap is Theta(m^-2): PROVED for the squarefree summand;")
    print("  the total-block equality is OBSERVED for m <= 8, not proved.")


def generator_koszul_section():
    print("=" * 78)
    print("(F) generator-Koszul supercharge Q_f = sum_j M_{f_j} (x) c_j (makes M4 real)")
    print("=" * 78)
    nv, gens, name, _ = ideals.twisted_cubic()
    d = len(gens)
    ms = [bf.poly_deg(f) for f in gens]
    Mf = {}
    for N in range(0, 7):
        Mf[N] = [bf.annihilation_matrix(f, N).conj().T for f in gens]  # R_{N-m}->R_N

    def Kdim(t, i):
        tot = 0
        for S in subsets(d, i):
            r = t - sum(ms[j] for j in S)
            tot += bf.dim_h(nv, r) if r >= 0 else 0
        return tot

    def dmat(t, i):
        """d : K_i^{(t)} -> K_{i-1}^{(t)},  d = sum_j M_{f_j} (x) c_j."""
        src, tgtl = subsets(d, i), subsets(d, i - 1)
        tgt = {s: k for k, s in enumerate(tgtl)}
        soff, toff, o = {}, {}, 0
        for S in src:
            r = t - sum(ms[j] for j in S)
            soff[S] = (o, bf.dim_h(nv, r) if r >= 0 else 0, r)
            o += soff[S][1]
        o = 0
        for S in tgtl:
            r = t - sum(ms[j] for j in S)
            toff[S] = (o, bf.dim_h(nv, r) if r >= 0 else 0, r)
            o += toff[S][1]
        D = np.zeros((o, soff[src[-1]][0] + soff[src[-1]][1] if src else 0),
                     dtype=complex)
        for S in src:
            so, sd, sr = soff[S]
            if sd == 0:
                continue
            for r_, j in enumerate(S):
                T = tuple(x for x in S if x != j)
                to, td, tr = toff[T]
                if td == 0 or tr < 0 or sr < 0:
                    continue
                D[to:to + td, so:so + sd] += ((-1) ** r_) * Mf[tr][j][:, :sd]
        return D

    print(f"  {name}: d = {d} generators of degree {ms}")
    ok0 = True
    for N in range(2, 6):
        D1 = dmat(N, 1)
        L0 = D1 @ D1.conj().T
        H = bf.hamiltonian(gens, N)
        e = float(np.abs(L0 - H).max())
        ok0 = ok0 and e < 1e-9
        print(f"    N={N}: |L^gen_(i=0) - H_N| = {e:.2e}  "
              f"{'OK' if e < 1e-9 else 'MISMATCH'}")
    check(ok0, "generator-Koszul: i=0 block is not H_N")
    quo = Quotient(nv, gens, 8)
    print(f"  {'t':>3} {'i':>2} {'dimK':>6} {'nullity H_i(f;R)':>17} "
          f"{'beta_{i,t}(R/I)':>16} {'differ?':>8}")
    differ = False
    for t in range(2, 7):
        for i in (1, 2):
            k = Kdim(t, i)
            if k == 0:
                continue
            Di, Di1 = dmat(t, i), dmat(t, i + 1)
            nul = k - bf.rank_numeric(Di) - (bf.rank_numeric(Di1) if Di1.size else 0)
            bb = betti(quo, nv, i, t - i)
            if nul != bb:
                differ = True
            print(f"  {t:>3} {i:>2} {k:>6} {nul:>17} {bb:>16} "
                  f"{'YES' if nul != bb else 'no':>8}")
    global M4_RED
    M4_RED = differ
    check(differ, "generator-Koszul nullities coincide with beta everywhere "
                  "(M4 would not be red)")
    print(f"  the two Koszul complexes give different invariants: "
          f"{'confirmed (M4 is a real mutation)' if differ else 'NOT confirmed'}")



def ambient_extension_section():
    """(H) O17/O18: the ambient observable, and adjacent-degree necessity."""
    print("=" * 78)
    print("(H) O17: the AMBIENT normalised fraction is the normalised trace of the")
    print("    HARMONIC projector extended by zero -- NOT the zero-eigenvalue fraction")
    print("    of L_W extended by zero.  Filtering  Ltilde = L_W + j(1 - Phat_N)")
    print("    on R_N (x) Lambda^i has zero eigenspace exactly the harmonic subspace.")
    print("    O18: dropping the ADJACENT-degree projector P_{0,N+1} destroys the block.")
    print("=" * 78)
    cases = []
    _, g5, _ = cycle_complex(5)
    cases.append(("5-cycle SR P^4", 5, g5, [(3, 2), (2, 1), (1, 1)], True))
    nv, g, _, _ = ideals.twisted_cubic()
    cases.append(("twisted cubic P^3", nv, g, [(1, 1), (2, 1)], False))
    print(f"  {'ideal':<18} {'i':>2} {'N':>2} {'M_N':>5} {'h_N':>4} {'b':>4} {'beta':>5} "
          f"{'null(0-ext)':>11} {'null(Ltilde)':>12} {'':>9} {'amb frac':>10} "
          f"{'null(no P_N+1)':>14} {'':>9}")
    for name, nvv, gens, blocks, mono in cases:
        quo = Quotient(nvv, gens, max(N for _, N in blocks) + 2)
        Bs = {N: (monomial_kernel_basis(quo, nvv, N) if mono
                  else kernel_basis(gens, nvv, N, quo.hf(N)))
              for N in range(0, max(N for _, N in blocks) + 2)}
        for i, N in blocks:
            b = math.comb(nvv, i)
            MN, hN, j = bf.dim_h(nvv, N), quo.hf(N), N + i
            beta = betti(quo, nvv, i, N)
            E = np.kron(Bs[N], np.eye(b))                 # W_N (x) L^i -> R_N (x) L^i
            Lw = L_block(Bs, nvv, i, N)
            Lzero = E @ Lw @ E.conj().T                   # extended by zero
            n0 = int((np.abs(spec(Lzero)) < TOL).sum())
            Ltil = Lzero + j * (np.eye(MN * b) - E @ E.conj().T)
            n1 = int((np.abs(spec(Ltil)) < TOL).sum())
            ok = (n1 == beta) and (n0 == (MN - hN) * b + beta)
            check(ok, f"{name}: (i={i},N={N}) null(0-ext)={n0} exp "
                      f"{(MN-hN)*b+beta}, null(Ltilde)={n1} exp {beta}")
            # O18: same block with the adjacent projector P_{0,N+1} removed
            mixed = dict(Bs)
            mixed[N + 1] = np.eye(bf.dim_h(nvv, N + 1), dtype=complex)
            Qin = Q_block(mixed, nvv, i - 1, N + 1) if i >= 1 else None
            Qout = Q_block(Bs, nvv, i, N)
            Lbad = Qout.conj().T @ Qout
            if Qin is not None and Qin.size:
                Lbad = Lbad + Qin @ Qin.conj().T
            nbad = int((np.abs(spec(Lbad)) < TOL).sum())
            ok2 = nbad != beta
            check(ok2, f"{name}: (i={i},N={N}) dropping P_0,N+1 still gives beta")
            print(f"  {name:<18} {i:>2} {N:>2} {MN:>5} {hN:>4} {b:>4} {beta:>5} "
                  f"{n0:>11} {n1:>12} {'OK' if ok else 'MISMATCH':>9} "
                  f"{beta/(MN*b):>10.6f} {nbad:>14} "
                  f"{'OK (differs)' if ok2 else 'MISMATCH':>9}")
    print("  the 'null(0-ext)' column is (M_N - h_N)*b + beta, NOT beta: the whole")
    print("  orthogonal complement of W_N is a spurious zero eigenspace (O17).")
    print("  the last column is the nullity when P_{0,N+1} is dropped from the incoming")
    print("  term: it collapses to 0 because Phat L Phat = j Phat, so adjacent-degree")
    print("  access is NECESSARY, not an optimisation (O18).")

    print()
    print("  (O21) the conversion weight h_N/M_N is NOT exponentially small for every")
    print("  square system.  Left: c = n quadrics in P^n at N = n (the family in which")
    print("  the applications memo's 0.75^codim law was measured).  Right: n generic")
    print("  forms of degree n+1 in P^n -- also a zero-dimensional square complete")
    print("  intersection -- where at N = n every generator has degree > N, so I_N = 0.")
    print(f"  {'n':>3} {'quadrics h_n/M_n':>17} {'deg-(n+1) h_n/M_n':>19} {'':>9}")
    okq = True
    for n in (2, 3, 4, 8):
        nv = n + 1
        Mn = bf.dim_h(nv, n)
        hq = sum((-1) ** t * math.comb(n, t) * bf.dim_h(nv, n - 2 * t)
                 for t in range(0, n + 1))
        rng = np.random.default_rng(5 + n)
        gh = [int_random_form(nv, n + 1, rng) for _ in range(n)]
        quo = Quotient(nv, gh, n)
        rat = quo.hf(n) / Mn
        ok = abs(rat - 1.0) < 1e-12
        okq = okq and ok
        print(f"  {n:>3} {hq/Mn:>17.6f} {rat:>19.6f} "
              f"{'OK' if ok else 'MISMATCH':>9}")
    check(okq, "high-degree square system does not have h_N/M_N = 1 at N = n")
    print("  so the overlap obstruction is a statement about the measured family, not")
    print("  about square systems in general.")


def ci_fraction_table():
    print("=" * 78)
    print("(G) normalised Betti fraction, complete intersection of c quadrics in P^n,")
    print("    block (i, N=i): beta_{i,2i} = C(c,i), dim = HF(i)*C(n+1,i).  The two")
    print("    regimes are printed separately (O6): fixed i (dimension POLYNOMIAL in n,")
    print("    so no compression) and i = rho*n (dimension exponential, fraction tiny).")
    print("    Dimensions are recomputed by an INDEPENDENT route (O19): the Hilbert")
    print("    series (1-t^2)^c/(1-t)^{n+1} by explicit polynomial multiplication, and")
    print("    C(n+1,i) by a Pascal recurrence.")
    print("=" * 78)

    def hf(nv, c, N):
        return sum((-1) ** t * math.comb(c, t) * bf.dim_h(nv, N - 2 * t)
                   for t in range(0, c + 1))

    def hf_series(nv, c, N):
        """Independent: coefficients of (1-t^2)^c * (1-t)^{-nv} up to t^N."""
        num = [0] * (N + 1)
        for t in range(0, min(c, N // 2) + 1):
            num[2 * t] = (-1) ** t * math.comb(c, t)
        den = [math.comb(k + nv - 1, nv - 1) for k in range(0, N + 1)]
        return sum(num[k] * den[N - k] for k in range(0, N + 1))

    def pascal(nn, kk):
        row = [1]
        for _ in range(nn):
            row = [1] + [row[t] + row[t + 1] for t in range(len(row) - 1)] + [1]
        return row[kk]

    okdim = True
    print("  fixed i, c (block dimension is POLYNOMIAL in n, so there is no compression):")
    print(f"  {'n':>4} {'c':>3} " + " ".join(f"{'i=%d frac' % i:>12}" for i in range(1, 4))
          + "   " + " ".join(f"{'i=%d dim' % i:>11}" for i in range(1, 4)) + "  check")
    for n, c in [(10, 3), (20, 5), (40, 5), (40, 10)]:
        nv = n + 1
        fr, dm, good = "", "", True
        for i in range(1, 4):
            h1, h2 = hf(nv, c, i), hf_series(nv, c, i)
            d1, d2 = h1 * math.comb(nv, i), h2 * pascal(nv, i)
            good = good and (h1 == h2) and (d1 == d2)
            fr += f"{math.comb(c, i)/d1:>12.3e} "
            dm += f"{d1:>11d} "
        okdim = okdim and good
        print(f"  {n:>4} {c:>3} {fr}  {dm}  {'OK' if good else 'MISMATCH'}")
    print("  growing i (Boolean-type CI, c = n), i = n:  fraction = 1/(2^n (n+1)),")
    print(f"  {'n':>4} {'dim block':>14} {'beta_{n,2n}':>12} {'fraction':>12}  check")
    for n in (8, 12, 16, 20):
        nv = n + 1
        d1 = hf(nv, n, n) * math.comb(nv, n)
        d2 = hf_series(nv, n, n) * pascal(nv, n)
        good = (d1 == d2) and (d1 == 2 ** n * (n + 1))
        okdim = okdim and good
        print(f"  {n:>4} {d1:>14d} {1:>12d} {1/d1:>12.3e}  "
              f"{'OK' if good else 'MISMATCH'}")
    check(okdim, "complete-intersection block dimensions disagree between the two routes")
    print("  So there is NO exhibited regime with exponential block dimension AND an")
    print("  inverse-polynomial fraction: at fixed i the dimension is polynomial.")


# ------------------------------------------------------------------- mutations

def mutations():
    print("=" * 78)
    print("MUTATIONS (each must come out RED).  Not yet registered in "
          "checkers/MUTATIONS.md:")
    print("that file is outside this lane's writable set; registration is a merge action.")
    print("=" * 78)
    nv, gens, _, _ = ideals.twisted_cubic()
    quo = Quotient(nv, gens, 4)
    Bs = {N: kernel_basis(gens, nv, N, quo.hf(N)) for N in range(0, 4)}
    red = {}

    # M1: no compression -- Phat L Phat instead of L_W
    bad = 0
    for N in (1, 2):
        for i in range(0, nv + 1):
            if quo.hf(N) == 0:
                continue
            amb = {M: np.eye(bf.dim_h(nv, M), dtype=complex)
                   for M in (N - 1, N, N + 1) if M >= 0}
            Phat = np.kron(Bs[N] @ Bs[N].conj().T, np.eye(math.comb(nv, i)))
            comp = Phat @ L_block(amb, nv, i, N) @ Phat
            ev = spec(comp)
            nul = int((np.abs(ev) < TOL).sum()) - (Phat.shape[0]
                                                   - int(round(np.trace(Phat).real)))
            if nul != betti(quo, nv, i, N):
                bad += 1
    red["M1 (drop the compression)"] = bad > 0

    # M2: wrong index convention
    bad = 0
    for N in (1, 2):
        for i in range(0, nv + 1):
            if quo.hf(N) == 0:
                continue
            nul = nullity_and_gap(L_block(Bs, nv, i, N))[0]
            wrong = betti(quo, nv, i, N - i) if N - i >= 0 else 0
            if nul != wrong:
                bad += 1
    red["M2 (beta_{i,N} for beta_{i,i+N})"] = bad > 0

    # M3: drop the fermionic sign
    bad = 0
    for N in (1, 2):
        for i in range(0, nv + 1):
            if quo.hf(N) == 0:
                continue
            if nullity_and_gap(L_block(Bs, nv, i, N, sign=False))[0] != betti(quo, nv, i, N):
                bad += 1
    # and Q^2 != 0 without the sign
    amb = {M: np.eye(bf.dim_h(nv, M), dtype=complex) for M in (0, 1, 2, 3)}
    q2 = Q_block(amb, nv, 1, 2, sign=False) @ Q_block(amb, nv, 0, 3, sign=False)
    red["M3 (drop the fermionic sign)"] = bad > 0 or np.abs(q2).max() > 1e-12

    # M4: generator-Koszul instead of variable-Koszul (established in part F)
    # M4: generator-Koszul instead of variable-Koszul; the flag is SET BY part F,
    # which actually ran both tables and compared them (no hard-coded value).
    if M4_RED is None:
        FAILS.append("M4 was never evaluated: part F did not run")
    red["M4 (Koszul on the generators)"] = bool(M4_RED)

    for k, v in red.items():
        print(f"  {k:<40} {'RED (good)' if v else 'GREEN (BAD)'}")
        check(v, f"mutation {k} did not go red")


def main():
    print("Koszul / supersymmetric Laplacian for graded Betti numbers")
    print("arm B exploration script, repaired after verdicts/koszul-betti-r1.md")
    print(f"conventions C1-C3, C6, C8; tolerance {TOL:g}; reference ranks exact over")
    print(f"GF(p) with p = {P_MOD} (characteristic p; the tested examples are")
    print("characteristic-independent), cross-checked against literature fixtures.\n")

    nv, g, _, hf = ideals.twisted_cubic()
    run_ideal("twisted cubic", "twisted cubic P^3", nv, g, 8, hf)

    nv = 4
    rng = np.random.default_rng(11)
    g = [int_random_form(nv, 2, rng), int_random_form(nv, 2, rng)]
    run_ideal("2 int quadrics CI", "2 random integer quadrics P^3 (complete intersection)",
              nv, g, 7,
              lambda N: sum((-1) ** t * math.comb(2, t) * bf.dim_h(4, N - 2 * t)
                            for t in range(0, 3)))

    nv, g, _, hf = ideals.monomial_ideal()
    run_ideal("(z0^2,z0z1,z1^3)", "monomial (z0^2,z0z1,z1^3) P^2", nv, g, 7, hf,
              monomial=True)

    run_ideal("(z0^2,z0z1,z1^2)", "monomial (z0^2,z0z1,z1^2) P^2", 3,
              [{(2, 0, 0): 1}, {(1, 1, 0): 1}, {(0, 2, 0): 1}], 6, None, monomial=True)

    nv, g, _, hf = ideals.rnc4()
    run_ideal("rat normal quartic", "rational normal quartic P^4", nv, g, 5, hf)

    _, g5, _ = cycle_complex(5)
    run_ideal("5-cycle SR", "5-cycle Stanley-Reisner P^4", 5, g5, 4, None, monomial=True)

    print()
    hochster_section()
    print()
    counterfamily_section()
    print()
    generator_koszul_section()
    print()
    ambient_extension_section()
    print()
    ci_fraction_table()
    print()
    mutations()

    print("\n" + "=" * 78)
    if FAILS:
        print(f"FAIL: {len(FAILS)} mismatch(es)")
        for f in FAILS[:40]:
            print("  " + f)
        return 1
    print("PASS: block nullities agree with GF(p) Koszul ranks AND literature fixtures;")
    print("      L_W is PSD; the uncompressed Laplacian is the scalar N+i; X is")
    print("      constructed and reproduces L_W; the singular-value pairing holds per")
    print("      differential; the cycle counterfamily matches 2-2cos(2pi/m); the")
    print("      generator-Koszul i=0 block is H_N; the ambient harmonic filter")
    print("      Ltilde = L_W + j(1-Phat_N) has nullity beta while zero-extended L_W")
    print("      does not; dropping P_{0,N+1} collapses the block; the two independent")
    print("      routes to the CI block dimensions agree; all four mutations are red.")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as exc:  # noqa: BLE001
        print(f"ERROR: {type(exc).__name__}: {exc}")
        sys.exit(2)
