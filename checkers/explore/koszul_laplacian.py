"""EXPLORATION ONLY -- deliberately excluded from run_all.sh (PRD arm B lane,
brief `briefs/lane-koszul-betti.md`).

Supersymmetric Koszul Laplacian for graded Betti numbers.

OBJECTS (all in D-fock-space conventions C1, C2, C3, C6, C8; ideals below have
integer or Gaussian-random generators, and every Delta_N printed is the gap of
the presentation AS WRITTEN, i.e. the same departure from convention C5 that
`checkers/README.md` records for the whole suite).

  W_N   = ker H_N = (I_N)^perp                        (D-ground-space, C-008)
  a_k   = d/dz_k                                      (D-mode-operators)
  Q     = sum_k a_k (x) c_k^dag  on  F (x) Lambda(C^{n+1})   (free supercharge)
  Q_W   = Q restricted to W (x) Lambda -- legitimate because W is a_k-invariant:
          <a_k u, h> = <u, z_k h> = 0 for u in (I_N)^perp, h in I_{N-1}
  Q_W^dag = sum_k Z_k (x) c_k,  Z_k = P_0 a_k^dag P_0  (D-compressed-multiplication)
  L_W   = Q_W Q_W^dag + Q_W^dag Q_W   on block (fermion number i, boson degree N)

CLAIMED IDENTIFICATION (this lane's central statement, tested in part A):

      nullity( L_W | block (i,N) )  =  beta_{i, i+N}(R/I),

the graded Betti number dim Tor_i^R(R/I, C)_{i+N}, because (W (x) Lambda, Q_W)
is the C-dual of the Koszul complex K_.(z_0..z_n ; R/I) and Hodge theory turns
dual homology into a nullity.  Betti information therefore lives at
N = j - i <= reg(R/I) ONLY, and every block with N > reg is empty of it.

ALSO TESTED (parts B, C):
  B  the UNCOMPRESSED Laplacian is a scalar: on R_N (x) Lambda^i,
     Q Q^dag + Q^dag Q = (N + i) * 1  exactly, hence
        (P_0 (x) 1) L (P_0 (x) 1) = (N+i) (P_0 (x) 1),
     which has NO kernel for N+i > 0.  So a block encoding of P_0 L P_0 carries
     zero Betti information; the compressed Q_W^dag = sum_k Z_k (x) c_k is
     mandatory.  Equivalently  L_W = (N+i) 1 - X X^dag  with
     X = (P_0 (x) 1) Q (1 - P_0 (x) 1), so ||L_W|| <= N + i.
  C  the Betti gap g_{i,N} = smallest nonzero eigenvalue of L_W on block (i,N),
     the normalised gap g_{i,N}/(N+i), and the Betti fraction
     beta_{i,i+N} / dim(block), against N, against the Macaulay gap Delta_N,
     and against n for complete intersections of c quadrics in P^n.

INDEPENDENT REFERENCE VALUE.  beta_{i,i+N} is recomputed from scratch over
GF(p), p = 10^9+7, by exact ranks of the Koszul differentials of R/I in a
standard-monomial basis (reduced row echelon of the Macaulay matrix,
D-macaulay-matrix).  Nothing on that side touches H_N, the Fock basis or any
floating-point number.

RED-CAPABLE (rk-light L4): every block prints OK/MISMATCH; the script exits 1
on any mismatch and 2 on an unexpected exception.  Mutations that make it red
are listed at the bottom of this docstring.

  M1  drop the compression: use  P_0 L P_0  instead of L_W  -> every nullity
      becomes 0, all nonzero Betti blocks MISMATCH.
  M2  wrong index convention: compare nullity(i,N) with beta_{i,N} instead of
      beta_{i,i+N}  -> MISMATCH on the twisted cubic at (1,1) and (2,1).
  M3  drop the fermionic sign (-1)^{#{l in S : l<k}} in c_k^dag  -> Q^2 != 0
      and the part-B scalar identity fails.
  M4  use a^dag(f_j) (x) gamma_j (Koszul on the d GENERATORS) instead of the
      n+1 variables -> the nullities become the Koszul homology H_i(f;R) =
      Tor_i^S(C,R), S = C[y_1..y_d] with y_j -> f_j, a DIFFERENT invariant
      (it vanishes for i > 0 exactly when f is a regular sequence, whereas
      beta_{i,j}(R/I) does not).  Untested here; see memo Step 10.

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


# ------------------------------------------------------------------ GF(p) side

def rref_mod_p(rows, ncols, p=P_MOD):
    """Reduced row echelon form over GF(p).  Returns (R, pivots)."""
    if not rows:
        return np.zeros((0, ncols), dtype=np.int64), []
    M = np.array([[int(x) % p for x in r] for r in rows], dtype=np.int64)
    nr = M.shape[0]
    r = 0
    pivots = []
    for c in range(ncols):
        piv = None
        for i in range(r, nr):
            if M[i, c]:
                piv = i
                break
        if piv is None:
            continue
        M[[r, piv]] = M[[piv, r]]
        inv = pow(int(M[r, c]), p - 2, p)
        M[r] = (M[r] * inv) % p
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
    """Standard-monomial model of (R/I)_M for M = 0..Mmax, exact over GF(p)."""

    def __init__(self, nv, gens, Mmax, p=P_MOD):
        self.nv, self.p = nv, p
        self.nonpiv = {}   # M -> list of monomial indices (basis of (R/I)_M)
        self.pos = {}      # M -> {monomial index: coordinate}
        self.red = {}      # M -> {monomial index: dict coordinate -> coeff}
        for M in range(0, Mmax + 1):
            ncols = bf.dim_h(nv, M)
            R, piv = rref_mod_p(bf.macaulay_rows(gens, M), ncols, p)
            pivset = set(piv)
            nonpiv = [c for c in range(ncols) if c not in pivset]
            pos = {c: t for t, c in enumerate(nonpiv)}
            red = {}
            for c in nonpiv:
                red[c] = {pos[c]: 1}
            for ri, c in enumerate(piv):
                d = {}
                for q in nonpiv:
                    v = int(R[ri, q]) % p
                    if v:
                        d[pos[q]] = (-v) % p
                red[c] = d
            self.nonpiv[M], self.pos[M], self.red[M] = nonpiv, pos, red

    def hf(self, M):
        if M < 0:
            return 0
        return len(self.nonpiv[M])


def subsets(nv, i):
    out = []
    for mask in range(1 << nv):
        if bin(mask).count("1") == i:
            out.append(tuple(k for k in range(nv) if mask >> k & 1))
    return out


def koszul_rank(quo, nv, i, N):
    """rank over GF(p) of  d : (R/I)_N (x) Lambda^i -> (R/I)_{N+1} (x) Lambda^{i-1},
    the degree-(N+i) piece of the Koszul differential of R/I on z_0..z_n."""
    if i <= 0 or N < 0 or quo.hf(N) == 0:
        return 0
    S_src = subsets(nv, i)
    S_tgt = {s: t for t, s in enumerate(subsets(nv, i - 1))}
    hf1 = quo.hf(N + 1)
    if hf1 == 0 or not S_tgt:
        return 0
    ncols = hf1 * len(S_tgt)
    monos_N = bf.monomials(nv, N)
    idx_N1 = bf.mono_index(nv, N + 1)
    rows = []
    for c in quo.nonpiv[N]:
        m = monos_N[c]
        for S in S_src:
            v = [0] * ncols
            for r, k in enumerate(S):
                sign = (-1) ** r
                tgtmon = tuple(m[t] + (1 if t == k else 0) for t in range(nv))
                red = quo.red[N + 1][idx_N1[tgtmon]]
                Sk = tuple(x for x in S if x != k)
                off = S_tgt[Sk] * hf1
                for coord, coeff in red.items():
                    v[off + coord] = (v[off + coord] + sign * coeff) % quo.p
            rows.append(v)
    return bf.rank_mod_p(rows, quo.p)


def betti(quo, nv, i, N):
    """beta_{i, i+N}(R/I) = dim K_i^{(i+N)} - rank d_i - rank d_{i+1}."""
    dim = quo.hf(N) * math.comb(nv, i)
    if dim == 0:
        return 0
    return dim - koszul_rank(quo, nv, i, N) - koszul_rank(quo, nv, i + 1, N - 1)


# ------------------------------------------------------------------ Fock side

def kernel_basis(gens, nv, N, kerdim):
    """(dim R_N) x kerdim matrix of an orthonormal basis of ker H_N (|k> ONB)."""
    MN = bf.dim_h(nv, N)
    if kerdim == 0:
        return np.zeros((MN, 0), dtype=complex)
    A = bf.stacked_A(gens, N)
    if A.shape[0] == 0:
        return np.eye(MN, dtype=complex)
    _, s, Vh = np.linalg.svd(A)
    return Vh[MN - kerdim:].conj().T


def ak_matrices(nv, N):
    """[a_k : R_N -> R_{N-1}] in the |k> ONB, one matrix per variable."""
    if N <= 0:
        return [np.zeros((0, bf.dim_h(nv, N)), dtype=complex) for _ in range(nv)]
    return [bf.annihilation_matrix({bf.emono(nv, [k]): 1}, N) for k in range(nv)]


def cdag_matrices(nv, i):
    """[c_k^dag : Lambda^i -> Lambda^{i+1}] with the fermionic sign."""
    src = subsets(nv, i)
    tgt = {s: t for t, s in enumerate(subsets(nv, i + 1))}
    out = []
    for k in range(nv):
        C = np.zeros((len(tgt), len(src)))
        for c, S in enumerate(src):
            if k in S:
                continue
            sign = (-1) ** sum(1 for l in S if l < k)
            T = tuple(sorted(S + (k,)))
            C[tgt[T], c] = sign
        out.append(C)
    return out


def Q_block(Bs, nv, i, N):
    """Matrix of Q_W : W_N (x) Lambda^i -> W_{N-1} (x) Lambda^{i+1}.
    Kron order is (boson) (x) (fermion)."""
    kd_s, kd_t = Bs[N].shape[1], Bs[N - 1].shape[1] if N - 1 in Bs else 0
    ns, nt = math.comb(nv, i), math.comb(nv, i + 1)
    if kd_s == 0 or kd_t == 0 or ns == 0 or nt == 0 or N <= 0:
        return np.zeros((kd_t * nt, kd_s * ns), dtype=complex)
    A = ak_matrices(nv, N)
    C = cdag_matrices(nv, i)
    out = np.zeros((kd_t * nt, kd_s * ns), dtype=complex)
    for k in range(nv):
        Ak = Bs[N - 1].conj().T @ A[k] @ Bs[N]
        out += np.kron(Ak, C[k])
    return out


def L_block(Bs, nv, i, N):
    """L_W on block (i, N)."""
    dim = Bs[N].shape[1] * math.comb(nv, i)
    L = np.zeros((dim, dim), dtype=complex)
    if dim == 0:
        return L
    Qout = Q_block(Bs, nv, i, N)          # (i,N) -> (i+1,N-1)
    if Qout.size:
        L += Qout.conj().T @ Qout
    if i >= 1 and (N + 1) in Bs:
        Qin = Q_block(Bs, nv, i - 1, N + 1)  # (i-1,N+1) -> (i,N)
        if Qin.size:
            L += Qin @ Qin.conj().T
    return L


def full_L_block(nv, i, N):
    """Uncompressed Q Q^dag + Q^dag Q on R_N (x) Lambda^i (part B)."""
    Bs = {M: np.eye(bf.dim_h(nv, M), dtype=complex) for M in (N - 1, N, N + 1) if M >= 0}
    return L_block(Bs, nv, i, N)


# ------------------------------------------------------------------ reporting

def int_random_form(nv, deg, rng, lo=-4, hi=5):
    """A random form with small INTEGER coefficients (the GF(p) reference side
    needs integers; complex Kostlan forms of D-kostlan-random-form do not work
    there)."""
    f = {}
    for m in bf.monomials(nv, deg):
        c = int(rng.integers(lo, hi))
        if c:
            f[m] = c
    if not f:
        f[bf.monomials(nv, deg)[0]] = 1
    return f


FAILS = []


def check(ok, msg):
    if not ok:
        FAILS.append(msg)
    return "OK" if ok else "MISMATCH"


def run_ideal(name, nv, gens, Nmax, hf_expected=None):
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
        Bs[N] = kernel_basis(gens, nv, N, kd)
        if kd > 0 and N >= 1:
            ev = bf.spectrum(gens, N)
            g = bf.gap_from_spectrum(ev, kd)
            delta[N] = g if g is not None else float("nan")

    print("\n(A) nullity of L_W per block (i,N)  vs  exact beta_{i,i+N} over GF(p)")
    print(f"{'i':>2} {'N':>2} {'j=i+N':>5} {'dimblk':>7} {'nullity':>7} "
          f"{'beta':>6} {'':>4} {'g_{i,N}':>10} {'g/(N+i)':>9} {'beta/dim':>10}")
    reg = -1
    gaps = {}
    for N in range(0, Nmax + 1):
        for i in range(0, nv + 1):
            dim = quo.hf(N) * math.comb(nv, i)
            if dim == 0:
                continue
            L = L_block(Bs, nv, i, N)
            ev = np.linalg.eigvalsh((L + L.conj().T) / 2)
            nul = int((ev < TOL).sum())
            nz = ev[ev >= TOL]
            g = float(nz.min()) if len(nz) else float("nan")
            b = betti(quo, nv, i, N)
            if b > 0:
                reg = max(reg, N)
            gaps.setdefault(i, []).append((N, g, nul, b, dim))
            tag = check(nul == b, f"{name}: block (i={i},N={N}) nullity {nul} != beta {b}")
            if b > 0 or N <= 4 or tag == "MISMATCH":
                print(f"{i:>2} {N:>2} {i+N:>5} {dim:>7} {nul:>7} {b:>6} {tag:>4} "
                      f"{g:>10.4f} {g/(N+i) if N+i else float('nan'):>9.4f} "
                      f"{b/dim:>10.3e}")
    print(f"  regularity read off the table: reg(R/I) = max(j-i : beta != 0) = {reg}")
    for N in range(reg + 1, Nmax + 1):
        for i in range(0, nv + 1):
            if quo.hf(N) == 0:
                continue
            L = L_block(Bs, nv, i, N)
            ev = np.linalg.eigvalsh((L + L.conj().T) / 2)
            if int((ev < TOL).sum()) != 0:
                FAILS.append(f"{name}: nonzero nullity at (i={i},N={N}) beyond reg={reg}")
    print(f"  prediction 'nullity = 0 for every N > reg' checked to N = {Nmax}: "
          f"{'OK' if not any('beyond reg' in f for f in FAILS) else 'MISMATCH'}")

    print("\n(B) uncompressed Laplacian is the scalar N+i "
          "(so P_0 L P_0 = (N+i) P_0 has no kernel)")
    okB = True
    for N in range(0, min(Nmax, 4) + 1):
        for i in range(0, nv + 1):
            Lf = full_L_block(nv, i, N)
            if Lf.shape[0] == 0:
                continue
            err = np.abs(Lf - (N + i) * np.eye(Lf.shape[0])).max()
            if err > 1e-9:
                okB = False
                FAILS.append(f"{name}: full L at (i={i},N={N}) is not (N+i)*1, err {err:.2e}")
    print(f"  max deviation over all (i,N) with N <= {min(Nmax,4)}: "
          f"{'< 1e-9  OK' if okB else 'FAILED'}")
    if quo.hf(2) > 0:
        i, N = 1, 2
        P0 = Bs[N] @ Bs[N].conj().T
        Lf = full_L_block(nv, i, N)
        Phat = np.kron(P0, np.eye(math.comb(nv, i)))
        comp = Phat @ Lf @ Phat
        Lw = L_block(Bs, nv, i, N)
        # eigenvalues of P0 L P0 on range(P0 (x) 1) are all N+i
        ev = np.linalg.eigvalsh((comp + comp.conj().T) / 2)
        ev = ev[ev > 1e-9]
        print(f"  compressed-in-the-wrong-way P_0 L P_0 at (i=1,N=2): "
              f"{len(ev)} nonzero eigenvalues, all equal to "
              f"{ev.min():.6f}..{ev.max():.6f} (should be {N+i}); "
              f"its nullity ON range(P_0 (x) 1) is 0, while beta_{{1,3}} = "
              f"{betti(quo, nv, 1, 2)}")
        # X X^dag identity
        XXd = (N + i) * np.eye(Lw.shape[0]) - Lw
        print(f"  ||L_W - ((N+i) - X X^dag)|| at (i=1,N=2) = "
              f"{np.abs(Lw - ((N+i)*np.eye(Lw.shape[0]) - XXd)).max():.2e} (identically 0 "
              f"by construction); smallest eigenvalue of (N+i)-L_W = "
              f"{np.linalg.eigvalsh((XXd+XXd.conj().T)/2).min():.4f} "
              f"(>= 0 required, X X^dag PSD)")

    print("\n(C) Betti gap g_{i,N} and Macaulay gap Delta_N versus N")
    print(f"{'N':>2} {'Delta_N':>10} " + " ".join(f"{'g(i=%d)'%i:>10}" for i in range(0, min(nv, 4) + 1)))
    for N in range(1, Nmax + 1):
        row = f"{N:>2} {delta.get(N, float('nan')):>10.4f} "
        for i in range(0, min(nv, 4) + 1):
            g = [x for x in gaps.get(i, []) if x[0] == N]
            row += f"{g[0][1] if g else float('nan'):>10.4f} "
        print(row)
    print(f"  wall {time.time()-t0:.1f}s")
    return quo, reg


def ci_fraction_table():
    """Complete intersection of c quadrics in P^n: Koszul resolution, so
    beta_{i,2i} = C(c,i) and the block is (i, N=i).  Normalised Betti fraction
    beta / (HF(i) * C(n+1,i))."""
    print("=" * 78)
    print("(C') normalised Betti fraction for a complete intersection of c "
          "quadrics in P^n")
    print("     block (i, N=i), beta_{i,2i} = C(c,i), dim = HF(i)*C(n+1,i)")
    print("=" * 78)

    def hf(nv, c, N):
        return sum((-1) ** t * math.comb(c, t) * bf.dim_h(nv, N - 2 * t)
                   for t in range(0, c + 1))
    print(f"{'n':>4} {'c':>3} " + " ".join(f"{'i=%d'%i:>11}" for i in range(1, 6)))
    for n, c in [(3, 2), (5, 3), (10, 3), (10, 5), (20, 5), (20, 10),
                 (40, 5), (40, 10), (40, 20)]:
        nv = n + 1
        row = f"{n:>4} {c:>3} "
        for i in range(1, 6):
            if i > c:
                row += f"{'-':>11} "
                continue
            dim = hf(nv, c, i) * math.comb(nv, i)
            row += f"{math.comb(c, i)/dim:>11.3e} "
        print(row)
    print("  the fraction falls off like C(c,i)/(C(n+1,i) HF(i)) ~ (i!)^2 / "
          "(n^i * n^i) for fixed i: exponential in i, polynomial in 1/n^{2i}.")


def cycle_complex(m):
    """Simplicial complex of the m-cycle: vertices 0..m-1, edges (i,i+1 mod m).
    Returns (faces, Stanley-Reisner generators) in m variables."""
    faces = [()] + [(v,) for v in range(m)]
    edges = set()
    for v in range(m):
        edges.add(tuple(sorted((v, (v + 1) % m))))
    faces += sorted(edges)
    gens = []
    for a in range(m):
        for b in range(a + 1, m):
            if (a, b) not in edges:
                gens.append(bf.emono(m, [a, b]))
    return faces, [{g: 1} for g in gens]


def reduced_homology(faces, sigma, p=P_MOD):
    """dim H~_k(Delta|_sigma; GF(p)) for all k, induced subcomplex on sigma."""
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
                g = f[:r] + f[r + 1:]
                v[idx[k - 1][g]] = ((-1) ** r) % p
            rows.append(v)
        rank[k] = bf.rank_mod_p(rows, p)
    out = {}
    for k in range(0, kmax + 1):
        out[k] = len(by_dim.get(k, [])) - rank.get(k, 0) - rank.get(k + 1, 0)
    return out


def hochster_betti(faces, m, i, j):
    """Hochster's formula: beta_{i,j}(R/I_Delta) =
    sum_{|sigma| = j} dim H~_{j-i-1}(Delta|_sigma)."""
    tot = 0
    for sigma in subsets(m, j):
        k = j - i - 1
        h = reduced_homology(faces, sigma)
        tot += h.get(k, 0)
    return tot


def stanley_reisner_section():
    print("=" * 78)
    print("(D) Stanley-Reisner bridge to quantum TDA: the Betti Laplacian of a")
    print("    monomial ideal, block by block, against HOCHSTER's formula")
    print("    beta_{i,j} = sum_{|sigma|=j} dim H~_{j-i-1}(Delta|_sigma).")
    print("    So the multigraded blocks of L_W ARE simplicial Laplacians of")
    print("    induced subcomplexes -- exactly the operator of quantum TDA.")
    print("=" * 78)
    for m in (4, 5, 6, 7):
        faces, gens = cycle_complex(m)
        Nmax = 3
        quo = Quotient(m, gens, Nmax + 2)
        Bs = {N: kernel_basis(gens, m, N, quo.hf(N)) for N in range(0, Nmax + 2)}
        print(f"\n  {m}-cycle, I_Delta = {len(gens)} quadrics in P^{m-1}, "
              f"HF(N) = {[quo.hf(N) for N in range(0, 4)]}")
        print(f"  {'i':>2} {'N':>2} {'j':>2} {'dimblk':>7} {'nullity':>7} "
              f"{'GF(p) beta':>10} {'Hochster':>9} {'':>9} {'g_{i,N}':>9} "
              f"{'g/(N+i)':>8} {'beta/dim':>10}")
        for N in range(1, Nmax + 1):
            for i in range(1, m + 1):
                dim = quo.hf(N) * math.comb(m, i)
                if dim == 0:
                    continue
                b = betti(quo, m, i, N)
                if b == 0:
                    continue
                L = L_block(Bs, m, i, N)
                ev = np.linalg.eigvalsh((L + L.conj().T) / 2)
                nul = int((ev < TOL).sum())
                nz = ev[ev >= TOL]
                g = float(nz.min()) if len(nz) else float("nan")
                hb = hochster_betti(faces, m, i, i + N)
                tag = check(nul == b and b == hb,
                            f"{m}-cycle: (i={i},N={N}) nullity {nul}, beta {b}, "
                            f"Hochster {hb}")
                print(f"  {i:>2} {N:>2} {i+N:>2} {dim:>7} {nul:>7} {b:>10} "
                      f"{hb:>9} {tag:>9} {g:>9.4f} {g/(N+i):>8.4f} "
                      f"{b/dim:>10.3e}")


def main():
    print("Koszul / supersymmetric Laplacian for graded Betti numbers")
    print("exploration script, arm B; conventions C1-C3, C6, C8; "
          f"tolerance {TOL:g}; GF(p) p = {P_MOD}\n")

    nv, g, name, hf = ideals.twisted_cubic()
    run_ideal(name + "  [expect beta_{1,2}=3, beta_{2,3}=2]", nv, g, 8, hf)

    # complete intersection of two quadrics in P^3, INTEGER coefficients so the
    # GF(p) reference side is exact (ideals.k_random_quadrics is complex).
    nv = 4
    rng = np.random.default_rng(11)
    g = [int_random_form(nv, 2, rng), int_random_form(nv, 2, rng)]
    hf = lambda N: sum((-1) ** t * math.comb(2, t) * bf.dim_h(nv, N - 2 * t)
                       for t in range(0, 3))
    run_ideal("2 random integer quadrics P^3  [complete intersection: "
              "beta_{1,2}=2, beta_{2,4}=1]", nv, g, 7, hf)

    nv, g, name, hf = ideals.monomial_ideal()
    run_ideal(name + "  [expect beta_{1,2}=2, beta_{1,3}=1, beta_{2,3}=1, "
              "beta_{2,4}=1]", nv, g, 7, hf)

    nv = 3
    g = [{(2, 0, 0): 1}, {(1, 1, 0): 1}, {(0, 2, 0): 1}]
    run_ideal("monomial (z0^2,z0z1,z1^2) P^2  [expect beta_{1,2}=3, beta_{2,3}=2]",
              nv, g, 6, None)

    nv, g, name, hf = ideals.rnc4()
    run_ideal(name + "  [Eagon-Northcott: beta_{1,2}=6, beta_{2,3}=8, beta_{3,4}=3]",
              nv, g, 5, hf)

    stanley_reisner_section()
    print()
    ci_fraction_table()

    print("\n" + "=" * 78)
    if FAILS:
        print(f"FAIL: {len(FAILS)} mismatch(es)")
        for f in FAILS[:40]:
            print("  " + f)
        return 1
    print("PASS: every block nullity equals the independently computed "
          "GF(p) graded Betti number; the uncompressed Laplacian is the scalar N+i.")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as exc:  # noqa: BLE001
        print(f"ERROR: {type(exc).__name__}: {exc}")
        sys.exit(2)
