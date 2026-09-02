"""Bargmann-Fock / Fischer machinery for ideals -> Hamiltonians.

Conventions:
  ring C[z_0..z_n], n_vars = n+1.
  |k> = z^k / sqrt(k!),  <z^a, z^b> = a! delta_ab   (Fischer inner product)
  a_j = d/dz_j,  a_j^dag = mult by z_j.
  a^dag(f) = mult by f ;  a(f) = conj(f)(partial) = sum_a conj(f_a) d^a
  H_N = sum_j a^dag(f_j) a(f_j) | h_N     (PSD, degree preserving)
  claim: ker H_N = (I_N)^perp,  dim ker = HF_{R/I}(N)
"""
import itertools, math
from functools import lru_cache
import numpy as np


# ---------- monomial bookkeeping ----------
@lru_cache(maxsize=None)
def monomials(n_vars, deg):
    """All exponent tuples of length n_vars summing to deg (graded-lex-ish order)."""
    if deg < 0:
        return ()
    if n_vars == 1:
        return ((deg,),)
    out = []
    for a in range(deg, -1, -1):
        for rest in monomials(n_vars - 1, deg - a):
            out.append((a,) + rest)
    return tuple(out)


@lru_cache(maxsize=None)
def mono_index(n_vars, deg):
    return {m: i for i, m in enumerate(monomials(n_vars, deg))}


def dim_h(n_vars, deg):
    if deg < 0:
        return 0
    return math.comb(deg + n_vars - 1, n_vars - 1)


def fact_prod(k):
    r = 1
    for x in k:
        r *= math.factorial(x)
    return r


# ---------- polynomials as dicts {exponent tuple: complex coeff} ----------
def poly_deg(f):
    return sum(next(iter(f)))


def poly_nvars(f):
    return len(next(iter(f)))


# ---------- a(f): h_N -> h_{N-m}, orthonormal bases ----------
def annihilation_matrix(f, N, dtype=complex):
    """Matrix A of a(f) = sum_a conj(f_a) d^a  from h_N to h_{N-m} in |k> bases."""
    nv = poly_nvars(f)
    m = poly_deg(f)
    rows = monomials(nv, N - m)
    cols = monomials(nv, N)
    ridx = mono_index(nv, N - m)
    A = np.zeros((len(rows), len(cols)), dtype=dtype)
    for cj, k in enumerate(cols):
        for a, ca in f.items():
            ok = True
            ff = 1
            for j in range(nv):
                if a[j] > k[j]:
                    ok = False
                    break
                # falling factorial k_j (k_j-1) ... (k_j-a_j+1)
                for t in range(a[j]):
                    ff *= (k[j] - t)
            if not ok:
                continue
            kk = tuple(k[j] - a[j] for j in range(nv))
            A[ridx[kk], cj] += np.conj(ca) * math.sqrt(ff)
    return A


def stacked_A(gens, N, dtype=complex):
    """Vertically stacked annihilation matrices; ker = ker H_N, rank = dim I_N."""
    blocks = [annihilation_matrix(f, N, dtype) for f in gens if poly_deg(f) <= N]
    blocks = [B for B in blocks if B.shape[0] > 0]
    nv = poly_nvars(gens[0])
    if not blocks:
        return np.zeros((0, dim_h(nv, N)), dtype=dtype)
    return np.vstack(blocks)


def hamiltonian(gens, N, dtype=complex):
    A = stacked_A(gens, N, dtype)
    return A.conj().T @ A


# ---------- Macaulay matrix (independent, unnormalized monomial basis) ----------
def macaulay_rows(gens, N):
    """Rows = coefficient vectors of z^beta * f_j, |beta| = N - deg f_j,
    in the *unnormalized* monomial basis of degree N.  rank = dim I_N."""
    nv = poly_nvars(gens[0])
    cols = mono_index(nv, N)
    rows = []
    for f in gens:
        m = poly_deg(f)
        if m > N:
            continue
        for b in monomials(nv, N - m):
            v = [0] * len(cols)
            for a, ca in f.items():
                e = tuple(a[j] + b[j] for j in range(nv))
                v[cols[e]] += ca
            rows.append(v)
    return rows


P_MOD = 1000000007


def rank_mod_p(rows, p=P_MOD):
    """Exact rank over GF(p) of an integer matrix (lower bound on rank over Q;
    equal for a random large p).  Gaussian elimination in int64."""
    if not rows:
        return 0
    M = np.array([[int(x) % p for x in r] for r in rows], dtype=np.int64)
    nr, nc = M.shape
    r = 0
    for c in range(nc):
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
        col = M[r + 1:, c].copy()
        nz = np.nonzero(col)[0]
        if len(nz):
            M[r + 1 + nz] = (M[r + 1 + nz] - col[nz][:, None] * M[r][None, :]) % p
        r += 1
        if r == nr:
            break
    return r


def rank_numeric(rows_or_mat, tol=None):
    M = np.array(rows_or_mat, dtype=complex)
    if M.size == 0:
        return 0
    s = np.linalg.svd(M, compute_uv=False)
    if tol is None:
        tol = max(M.shape) * s[0] * 1e-12
    return int((s > tol).sum())


# ---------- spectra ----------
def spectrum(gens, N, dtype=complex):
    H = hamiltonian(gens, N, dtype)
    H = (H + H.conj().T) / 2
    return np.linalg.eigvalsh(H)


def gap_from_spectrum(ev, kerdim):
    """Delta = smallest nonzero eigenvalue given the *exactly known* kernel dim."""
    ev = np.sort(ev)
    if kerdim >= len(ev):
        return None
    return ev[kerdim]


# ---------- convenience polynomial builders ----------
def mono(nv, **kw):
    e = [0] * nv
    for k, v in kw.items():
        e[int(k[1:])] = v
    return tuple(e)


def P(nv, terms):
    """terms: list of (coeff, dict var_index->power)"""
    f = {}
    for c, d in terms:
        e = [0] * nv
        for j, pw in d.items():
            e[j] = pw
        f[tuple(e)] = f.get(tuple(e), 0) + c
    return {k: v for k, v in f.items() if v != 0}


def emono(nv, idxs):
    """exponent tuple obtained by multiplying variables in the list idxs."""
    e = [0] * nv
    for j in idxs:
        e[j] += 1
    return tuple(e)


def minors2x2(nv, top, bot):
    """2x2 minors of [[top],[bot]] where top/bot are lists of variable indices."""
    out = []
    L = len(top)
    for i in range(L):
        for j in range(i + 1, L):
            g = {}
            e1 = emono(nv, [top[i], bot[j]])
            e2 = emono(nv, [top[j], bot[i]])
            g[e1] = g.get(e1, 0) + 1
            g[e2] = g.get(e2, 0) - 1
            g = {a: c for a, c in g.items() if c != 0}
            if g:
                out.append(g)
    return out


def random_form(nv, deg, rng, real=False):
    ms = monomials(nv, deg)
    f = {}
    for m in ms:
        c = rng.normal() + 1j * rng.normal() if not real else rng.normal()
        f[m] = c / math.sqrt(2 * len(ms))
    return f
