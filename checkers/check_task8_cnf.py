"""Checker: the boolean + 3-CNF ideal K = (z_i^2 - z_i z_0 ; c_C).

CONVENTIONS: definitions/definitions.md D-boolean-ideal, D-clause-ideal,
D-hilbert-function, D-macaulay-gap, D-coherent-state, D-coherent-gram-matrix.
DEPARTURE FROM C5: generators are used as written (unit coefficients), not
normalised to unit Bombieri-Weyl norm; see README, "Conventions".

SEED CLAIMS UNDER TEST
  seed/analysis-2026-09-01/report.md
  - Sect. 6, first bullet:
      "The boolean ideal J = (z_i^2 - z_i z_0) ... has HF(N) = sum_{i<=min(N,n)}
       C(n,i), equal to 2^n from N = n on (NUMERICALLY confirmed for n <= 5)"
      (Sect. 9 correction 8: "reaches 2^n at N = n, not n+1"), and
      "HF_{R/K}(N) = #SAT(phi) for N >= n+3 (NUMERICALLY: 45 random and
       constructed instances with n = 3,...,7, exact Groebner/GF(p) ranks;
       stabilisation happens by N = n+2, and for N below that the Hilbert
       function overshoots".
  - Conjecture 8.6(i): "at N = n+3 over 54 instances with n = 3,...,8 the
      smallest nonzero eigenvalue stays in [0.29, 2.3] while 2^n grows by 32x
      ... and the pure boolean part has Delta = 2 throughout; so the gap is not
      where the hardness is."
  - Conjecture 8.6(ii): "NUMERICALLY the smallest Gram eigenvalue of the full
      hypercube family is 3.5 e^{-0.85 n} at N = n+3 and still 0.7 e^{-0.35 n}
      at N = 2n, while the Gram matrix restricted to the satisfying assignments
      of a random instance is well conditioned, lam_min >= 0.13; at N = n+3 the
      weight <Psi|P_0|Psi> exceeds D/2^n by factors 1-12."

WHAT IS CHECKED (exit 0 only if all hold)
  (0) the vectorised monomial index used by the sparse builder agrees with
      bf.monomials on every (nv, deg) tested, and the sparse deflated LOBPCG
      gap agrees with the dense eigh gap to SOLVER_TOL;
  (1) pure boolean ideal: HF(N) = sum_{i<=min(N,n)} C(n,i) exactly, and
      HF(N) = 2^n for every N >= n (NOT only for N >= n+1);
  (2) for every instance: HF_{R/K}(N) = #SAT(phi) for N in [n+3, n+4], and the
      exact boolean-quotient HF agrees with dim R_N - rank_GF(p)(full Macaulay)
      wherever that is affordable and with the numerical kernel count of H_N
      wherever H_N is diagonalised densely;
  (3) the degenerate unique-solution instances DO overshoot below the stable
      range: HF(N) > #SAT for some N < n+3;
  (4) Delta_{n+3} lies in GAP_RANGE for every instance, the pure boolean ideal
      has Delta = 2 (to BOOL_GAP_TOL) at N = n+1, n+2, n+3, and 1/min_instances
      Delta grows by at most GAP_BLOWUP between n = 3 and n = NMAX while 2^n
      grows by 2^(NMAX-3);
  (5) coherent states of the satisfying assignments are IN the ground space:
      rank of the coherent-state matrix = #SAT, ||A V||/||V|| <= COH_TOL, and
      (dense cases) ||(1-P_0)V||/||V|| <= COH_TOL;
  (6) the Gram matrix over the SAT points of the ratio-2.0 instances has
      lam_min >= SAT_GRAM_MIN = 0.13;
  (7) the FULL hypercube Gram lam_min matches 3.5 e^{-0.85 n} at N = n+3 and
      0.7 e^{-0.35 n} at N = 2n, each within FIT_BAND relative;
  (8) <Psi|P_0|Psi> / (#SAT/2^n) lies in OVERLAP_RANGE = [1, 12] for every
      satisfiable instance, and the Gram-matrix formula for that overlap agrees
      with a direct computation in the full Hilbert space.

BUDGET (REDUCED from the seed, which ran n = 3..8 and N = n+3, n+4 in 7644 s):
n = 3..6 and N = n+3 for the spectral parts, dense eigh up to dim 1400 and the
sparse deflated LOBPCG above it.  Combinatorial parts (exact HF, Gram, overlap)
run for n = 3..6.  See README for the effect on the reproduced numbers.
"""
import itertools
import math
import time
import warnings

import numpy as np
import scipy.sparse as sp
from scipy.sparse.linalg import LinearOperator, eigsh, lobpcg

import bf
import checkharness

NMAX = 6
DENSE_CAP = 1400
MAC_CAP = 400

SOLVER_TOL = 1e-6
GAP_RANGE = (0.25, 2.5)
BOOL_GAP_TOL = 0.05
GAP_BLOWUP = 4.0
COH_TOL = 1e-8
SAT_GRAM_MIN = 0.13
FIT_BAND = 0.25          # relative band around the published Gram fits
OVERLAP_RANGE = (1.0, 12.0)

P_MOD = bf.P_MOD


# ------------------------------------------------------------------ polynomials
def pmul(f, g):
    h = {}
    for a, ca in f.items():
        for b, cb in g.items():
            e = tuple(x + y for x, y in zip(a, b))
            h[e] = h.get(e, 0) + ca * cb
    return {k: v for k, v in h.items() if v != 0}


def clause_poly(nv, clause):
    """clause = tuple of literals (i, pos); pos=True <-> x_i, pos=False <-> ~x_i."""
    f = {tuple([0] * nv): 1}
    for (i, pos) in clause:
        g = ({bf.emono(nv, [0]): 1, bf.emono(nv, [i]): -1} if pos
             else {bf.emono(nv, [i]): 1})
        f = pmul(f, g)
    return f


def boolean_gens(n):
    nv = n + 1
    return [{bf.emono(nv, [i, i]): 1, bf.emono(nv, [i, 0]): -1}
            for i in range(1, n + 1)]


def cnf_gens(n, clauses):
    return boolean_gens(n) + [clause_poly(n + 1, C) for C in clauses]


# ------------------------------------------------------------------ SAT
def sat_assignments(n, clauses):
    out = []
    for bits in itertools.product((0, 1), repeat=n):
        ok = True
        for C in clauses:
            if not any((bits[i - 1] == 1) == pos for (i, pos) in C):
                ok = False
                break
        if ok:
            out.append(bits)
    return out


def all_clauses(n):
    out = []
    for vs in itertools.combinations(range(1, n + 1), 3):
        for sg in itertools.product((True, False), repeat=3):
            out.append(tuple(sorted(zip(vs, sg))))
    return out


def rand_3cnf(n, m, rng):
    pool = all_clauses(n)
    m = min(m, len(pool))
    pick = rng.choice(len(pool), size=m, replace=False)
    return [pool[i] for i in sorted(pick)]


def unique_sol_instance(n, rng):
    pool = all_clauses(n)
    for _ in range(200):
        x = tuple(int(b) for b in rng.integers(0, 2, size=n))
        ok = [C for C in pool if any((x[i - 1] == 1) == pos for (i, pos) in C)]
        order = rng.permutation(len(ok))
        cl = []
        for j in order:
            cl.append(ok[j])
            if len(sat_assignments(n, cl)) == 1:
                changed = True
                while changed:
                    changed = False
                    for j2 in range(len(cl)):
                        trial = cl[:j2] + cl[j2 + 1:]
                        if len(sat_assignments(n, trial)) == 1:
                            cl = trial
                            changed = True
                            break
                return cl
    return None


def degenerate_unique(n, target):
    return [tuple([(i + 1, bool(target[i]))] * 3) for i in range(n)]


# ------------------------------------------------- exact HF via boolean quotient
def subsets_upto(n, smax):
    out = []
    for s in range(smax + 1):
        out.extend(itertools.combinations(range(1, n + 1), s))
    return out


def hf_exact(n, clauses, N):
    """HF_{R/K}(N), exact, by the boolean-quotient reduction (see seed task8)."""
    if N < 0:
        return 0
    nv = n + 1
    subs = subsets_upto(n, min(N, n))
    sidx = {S: i for i, S in enumerate(subs)}
    dimA = len(subs)
    if N < 3:
        return dimA
    tmax = min(N - 3, n)
    rows = []
    for C in clauses:
        c = clause_poly(nv, C)
        terms = [(frozenset(j for j in range(1, nv) if a[j] > 0), ca)
                 for a, ca in c.items()]
        for ts in range(tmax + 1):
            for T in itertools.combinations(range(1, n + 1), ts):
                Ts = frozenset(T)
                v = [0] * dimA
                for sup, ca in terms:
                    v[sidx[tuple(sorted(sup | Ts))]] += ca
                if any(v):
                    rows.append(v)
    if not rows:
        return dimA
    R = np.unique(np.array(rows, dtype=np.int64), axis=0)
    return dimA - bf.rank_mod_p([list(map(int, r)) for r in R])


def hf_macaulay(gens, N, nv):
    rows = bf.macaulay_rows(gens, N)
    rows = [[int(round(x.real)) if isinstance(x, complex) else int(round(x))
             for x in r] for r in rows]
    return bf.dim_h(nv, N) - bf.rank_mod_p(rows)


# ------------------------------------------------------------------ sparse a(f)
_PASCAL = np.zeros((80, 80), dtype=np.int64)
_PASCAL[0, 0] = 1
for _i in range(1, 80):
    _PASCAL[_i, 0] = 1
    _PASCAL[_i, 1:] = _PASCAL[_i - 1, 1:] + _PASCAL[_i - 1, :-1]


def mono_index_vec(K, nv, deg):
    K = np.asarray(K, dtype=np.int64)
    idx = np.zeros(K.shape[0], dtype=np.int64)
    rem = np.full(K.shape[0], deg, dtype=np.int64)
    for j in range(nv - 1):
        r = nv - j - 1
        B = rem - K[:, j] - 1
        good = B >= 0
        idx[good] += _PASCAL[B[good] + r, r]
        rem = rem - K[:, j]
    return idx


def check_mono_index_vec():
    """Returns the first failing (nv, deg), or None.  (No bare assert: L4.)"""
    for nv in (2, 4, 6):
        for deg in (0, 1, 3, 5):
            M = np.array(bf.monomials(nv, deg), dtype=np.int64)
            if not np.array_equal(mono_index_vec(M, nv, deg), np.arange(len(M))):
                return (nv, deg)
    return None


def ann_sparse(f, N):
    nv = bf.poly_nvars(f)
    m = bf.poly_deg(f)
    if m > N:
        return None
    C = np.array(bf.monomials(nv, N), dtype=np.int64)
    R = bf.dim_h(nv, N - m)
    II, JJ, VV = [], [], []
    for a, ca in f.items():
        av = np.array(a, dtype=np.int64)
        idx = np.nonzero(np.all(C >= av[None, :], axis=1))[0]
        if idx.size == 0:
            continue
        sub = C[idx]
        ff = np.ones(idx.size, dtype=np.float64)
        for j in range(nv):
            for t in range(a[j]):
                ff *= (sub[:, j] - t)
        rr = mono_index_vec(sub - av[None, :], nv, N - m)
        II.append(rr)
        JJ.append(idx)
        VV.append(float(np.real(ca)) * np.sqrt(ff))
    if not II:
        return None
    return sp.csr_matrix((np.concatenate(VV),
                          (np.concatenate(II), np.concatenate(JJ))),
                         shape=(R, C.shape[0]))


def stack_A(gens, N, nv):
    B = [ann_sparse(f, N) for f in gens]
    B = [b for b in B if b is not None and b.shape[0] > 0]
    if not B:
        return sp.csr_matrix((0, bf.dim_h(nv, N)))
    return sp.vstack(B, format='csr')


# ------------------------------------------------------------- coherent states
def coherent_matrix(pts, N, nv):
    mons = bf.monomials(nv, N)
    M = np.array(mons, dtype=np.int64)
    fN = math.factorial(N)
    sm = np.array([math.sqrt(fN / bf.fact_prod(k)) for k in mons])
    V = np.zeros((len(mons), len(pts)))
    for c, x in enumerate(pts):
        p = np.array([1.0] + list(x), dtype=float)
        p /= np.linalg.norm(p)
        with np.errstate(divide='ignore', invalid='ignore'):
            pk = np.prod(np.power(p[None, :], M), axis=1)
        v = sm * pk
        V[:, c] = v / np.linalg.norm(v)
    return V


def gram01(pts, N):
    """<p_x|p_y>^N for p = (1,x)/||.|| = (1+|x&y|)^N/((1+|x|)(1+|y|))^{N/2}."""
    X = np.array(pts, dtype=np.int64)
    if X.size == 0:
        return np.zeros((0, 0))
    w = 1.0 + X.sum(axis=1)
    inter = 1.0 + X @ X.T
    lw = np.log(w)
    return np.exp(N * (np.log(inter) - 0.5 * (lw[:, None] + lw[None, :])))


# ------------------------------------------------------------------ spectra
def spectral(gens, N, nv, sat_pts, kd_exact, want_dense=None):
    D = bf.dim_h(nv, N)
    A = stack_A(gens, N, nv)
    V = coherent_matrix(sat_pts, N, nv) if len(sat_pts) else np.zeros((D, 0))
    res = dict(N=N, dim=D, kd=kd_exact, nsat=len(sat_pts))

    if V.shape[1]:
        Uv, s, _ = np.linalg.svd(V, full_matrices=False)
        res['V_rank'] = int((s > 1e-10 * s[0]).sum())
        Q = Uv[:, :res['V_rank']]
        res['AVres'] = float(np.linalg.norm(A @ V) / max(np.linalg.norm(V), 1e-300))
    else:
        res['V_rank'] = 0
        res['AVres'] = 0.0
        Q = np.zeros((D, 0))

    dense = (D <= DENSE_CAP) if want_dense is None else want_dense
    if dense:
        H = (A.T @ A).toarray()
        H = (H + H.T) / 2
        ev, U = np.linalg.eigh(H)
        norm = float(ev[-1])
        res['norm'] = norm
        res['kernum'] = int((ev < 1e-9 * max(norm, 1e-300)).sum())
        res['gap'] = float(ev[kd_exact]) if kd_exact < D else float('nan')
        res['mode'] = 'dense'
        if V.shape[1]:
            P = U[:, :kd_exact]
            res['projres'] = float(np.linalg.norm(V - P @ (P.T @ V))
                                   / np.linalg.norm(V))
        else:
            res['projres'] = 0.0
    else:
        AT = A.T.tocsr()

        def Hmv(X):
            return AT @ (A @ X)

        Hop = LinearOperator((D, D), matvec=Hmv, matmat=Hmv, dtype=float)
        norm = float(eigsh(Hop, k=1, which='LA', tol=1e-9,
                           return_eigenvectors=False, maxiter=20000)[0])
        res['norm'] = norm
        c = norm

        if Q.shape[1]:
            def Mmv(X):
                return AT @ (A @ X) + c * (Q @ (Q.T @ X))
        else:
            Mmv = Hmv
        Mop = LinearOperator((D, D), matvec=Mmv, matmat=Mmv, dtype=float)
        lams, resids = [], []
        for seed in (0, 1):
            rs = np.random.default_rng(seed)
            X = rs.normal(size=(D, 8))
            with warnings.catch_warnings():
                warnings.simplefilter("ignore")
                lam, U = lobpcg(Mop, X, largest=False, tol=1e-9, maxiter=3000)
            o = np.argsort(lam)
            lam = lam[o]
            U = U[:, o]
            lams.append(lam)
            resids.append(np.linalg.norm(Mmv(U) - U * lam[None, :], axis=0))
        j = int(np.argmin([l[0] for l in lams]))
        res['gap'] = float(lams[j][0])
        res['lobpcg_resid'] = float(resids[j][0])
        res['lobpcg_seed_spread'] = float(abs(lams[0][0] - lams[1][0]))
        res['kernum'] = -1
        res['projres'] = float('nan')
        res['mode'] = 'sparse'
    return res


# ------------------------------------------------------------------ instances
def make_instances(n, seed=0):
    """The seed's 9 instances per n (same rng stream, so same instances)."""
    rng = np.random.default_rng(1000 * n + seed)
    inst = []
    for r in range(3):
        inst.append((f"r4.2-{r}", rand_3cnf(n, int(round(4.2 * n)), rng), "ratio4.2"))
    for r in range(3):
        inst.append((f"r2.0-{r}", rand_3cnf(n, int(round(2.0 * n)), rng), "ratio2.0"))
    cl = None
    for ratio in (4.2, 5.0, 6.0, 8.0, 12.0):
        for _ in range(400):
            c = rand_3cnf(n, int(round(ratio * n)), rng)
            if not sat_assignments(n, c):
                cl = c
                break
        if cl is not None:
            break
    inst.append(("unsat", cl, "UNSAT"))
    tgt = tuple(int(b) for b in rng.integers(0, 2, size=n))
    inst.append(("uniq-deg", degenerate_unique(n, tgt), "unique-degenerate"))
    cl = unique_sol_instance(n, rng)
    if cl is not None:
        inst.append(("uniq-3lit", cl, "unique-3distinct"))
    return inst


# ------------------------------------------------------------------ the checks
def body(ck):
    t0 = time.time()
    bad = check_mono_index_vec()
    ck.require(bad is None,
               f"vectorised monomial index disagrees with bf.monomials at "
               f"(nv, deg) = {bad}")

    ALL = {n: make_instances(n) for n in range(3, NMAX + 1)}

    # ---- (0) dense vs sparse solver agreement ----------------------------
    ck.info("  (0) dense eigh vs sparse deflated LOBPCG, same instances")
    ck.info(f"    {'n':>3} {'instance':10s} {'N':>3} {'dim':>6} {'#SAT':>5} "
            f"{'Delta(dense)':>13} {'Delta(sparse)':>14} {'|diff|':>10}")
    for n in (4, 5):
        for tag, clauses, cls in make_instances(n)[:1] + make_instances(n)[3:5]:
            N, nv = n + 3, n + 1
            S = sat_assignments(n, clauses)
            kd = hf_exact(n, clauses, N)
            rd = spectral(cnf_gens(n, clauses), N, nv, S, kd, want_dense=True)
            rs_ = spectral(cnf_gens(n, clauses), N, nv, S, kd, want_dense=False)
            ck.info(f"    {n:>3} {tag:10s} {N:>3} {rd['dim']:>6} {len(S):>5} "
                    f"{rd['gap']:>13.9g} {rs_['gap']:>14.9g} "
                    f"{abs(rd['gap']-rs_['gap']):>10.2e}")
            ck.atmost(abs(rd['gap'] - rs_['gap']), SOLVER_TOL,
                      f"n={n} {tag}: dense and sparse solvers must agree on "
                      f"Delta_(n+3)")

    # ---- (1) pure boolean Hilbert function -------------------------------
    ck.info("\n  (1) pure boolean ideal J = (z_i^2 - z_i z_0)")
    ck.info(f"    {'n':>3} {'N':>3} {'HF_exact':>9} {'closed form':>12} "
            f"{'2^n':>6}")
    for n in range(3, NMAX + 1):
        for N in range(1, n + 4):
            he = hf_exact(n, [], N)
            cf = sum(math.comb(n, i) for i in range(0, min(N, n) + 1))
            ck.info(f"    {n:>3} {N:>3} {he:>9} {cf:>12} {2**n:>6}")
            ck.equal(he, cf, f"boolean n={n}, N={N}: HF = sum_i<=min(N,n) C(n,i)")
            if N >= n:
                ck.equal(he, 2**n,
                         f"boolean n={n}, N={N}: HF = 2^n already at N = n "
                         f"(Sect. 9 correction 8)")

    # ---- (2)(3) HF of the clause ideal -----------------------------------
    ck.info("\n  (2) HF_{R/K}(N) vs #SAT")
    ck.info(f"    {'n':>3} {'instance':10s} {'#SAT':>5} {'HF at N=2..n+4':<40} "
            f"{'MacGFp ok':>10} {'kerNum ok':>10}")
    for n in range(3, NMAX + 1):
        nv = n + 1
        for tag, clauses, cls in ALL[n]:
            S = sat_assignments(n, clauses)
            hfs, macok, kerok = {}, True, True
            for N in range(2, n + 5):
                D = bf.dim_h(nv, N)
                he = hf_exact(n, clauses, N)
                hfs[N] = he
                if D <= MAC_CAP:
                    mg = hf_macaulay(cnf_gens(n, clauses), N, nv)
                    ck.equal(mg, he,
                             f"n={n} {tag}, N={N}: exact boolean-quotient HF vs "
                             f"dim R_N - rank_GF(p)(full Macaulay)")
                if D <= DENSE_CAP:
                    A = stack_A(cnf_gens(n, clauses), N, nv)
                    H = (A.T @ A).toarray()
                    H = (H + H.T) / 2
                    ev = np.linalg.eigvalsh(H)
                    kn = int((ev < 1e-9 * max(float(ev[-1]), 1e-300)).sum())
                    ck.equal(kn, he,
                             f"n={n} {tag}, N={N}: numerical kernel count of "
                             f"H_N vs exact HF")
            ck.info(f"    {n:>3} {tag:10s} {len(S):>5} "
                    f"{' '.join(str(hfs[N]) for N in sorted(hfs)):<40} "
                    f"{str(macok):>10} {str(kerok):>10}")
            for N in (n + 3, n + 4):
                ck.equal(hfs[N], len(S),
                         f"n={n} {tag}, N={N}: HF_{{R/K}}(N) = #SAT(phi) "
                         f"(Sect. 6)")
            if tag == "uniq-deg":
                ck.require(any(hfs[N] > len(S) for N in range(2, n + 3)),
                           f"n={n} uniq-deg: the Hilbert function must OVERSHOOT "
                           f"below the stable range (Sect. 6)")
        ck.info(f"      (elapsed {time.time()-t0:.0f}s)")

    # ---- (4) gaps ---------------------------------------------------------
    ck.info("\n  (4) Delta_(n+3) over all instances")
    ck.info(f"    {'n':>3} {'instance':10s} {'#SAT':>5} {'dim':>6} {'ker':>5} "
            f"{'Delta':>11} {'||H||':>11} {'ratio':>9} {'V_rank':>6} "
            f"{'AVres':>9} {'mode':>7}")
    minmax = {}
    for n in range(3, NMAX + 1):
        nv, N = n + 1, n + 3
        gaps = []
        for tag, clauses, cls in ALL[n]:
            S = sat_assignments(n, clauses)
            kd = hf_exact(n, clauses, N)
            r = spectral(cnf_gens(n, clauses), N, nv, S, kd)
            gaps.append(r['gap'])
            ck.info(f"    {n:>3} {tag:10s} {len(S):>5} {r['dim']:>6} {kd:>5} "
                    f"{r['gap']:>11.6g} {r['norm']:>11.6g} "
                    f"{r['norm']/max(r['gap'], 1e-300):>9.4g} {r['V_rank']:>6} "
                    f"{r['AVres']:>9.2e} {r['mode']:>7}")
            ck.between(r['gap'], GAP_RANGE[0], GAP_RANGE[1],
                       f"n={n} {tag}: Delta_(n+3) in the published band "
                       f"(Conj. 8.6(i))")
            # (5) coherent states of the SAT points sit in the ground space
            ck.equal(r['V_rank'], len(S),
                     f"n={n} {tag}: rank of the coherent-state matrix = #SAT")
            ck.atmost(r['AVres'], COH_TOL,
                      f"n={n} {tag}: ||A V||/||V|| (SAT coherent states are "
                      f"annihilated by every generator)")
            if r['mode'] == 'dense':
                ck.atmost(r['projres'], COH_TOL,
                          f"n={n} {tag}: ||(1-P_0)V||/||V|| (SAT coherent "
                          f"states lie in ker H_N)")
                ck.equal(r['kernum'], kd,
                         f"n={n} {tag}: numerical kernel dim vs exact HF")
        minmax[n] = (min(gaps), max(gaps), float(np.median(gaps)))
        ck.info(f"      n={n}: min Delta = {minmax[n][0]:.5f}, median = "
                f"{minmax[n][2]:.5f}, max = {minmax[n][1]:.5f}  "
                f"(elapsed {time.time()-t0:.0f}s)")

    blow = (1.0 / minmax[NMAX][0]) / (1.0 / minmax[3][0])
    ck.info(f"    1/min Delta grows by {blow:.3f}x from n=3 to n={NMAX}, "
            f"while 2^n grows by {2**(NMAX-3)}x")
    ck.atmost(blow, GAP_BLOWUP,
              f"1/min Delta must not blow up with n (Conj. 8.6(i): 'the gap is "
              f"not where the hardness is')")

    # ---- (4b) pure boolean gap -------------------------------------------
    ck.info("\n  (4b) pure boolean ideal gap")
    ck.info(f"    {'n':>3} {'N':>3} {'dim':>7} {'ker=2^n':>8} {'Delta':>11} "
            f"{'||H||':>11}")
    for n in range(3, NMAX + 1):
        nv = n + 1
        pts = list(itertools.product((0, 1), repeat=n))
        for N in (n + 1, n + 2, n + 3):
            kd = hf_exact(n, [], N)
            r = spectral(boolean_gens(n), N, nv, pts, kd)
            ck.info(f"    {n:>3} {N:>3} {r['dim']:>7} {kd:>8} {r['gap']:>11.6g} "
                    f"{r['norm']:>11.6g}")
            ck.equal(kd, 2**n, f"boolean n={n}, N={N}: kernel dim = 2^n")
            ck.close(r['gap'], 2.0, BOOL_GAP_TOL,
                     f"boolean n={n}, N={N}: Delta = 2 throughout "
                     f"(Conj. 8.6(i))")

    # ---- (6)(7) Gram conditioning ----------------------------------------
    ck.info("\n  (6) Gram matrix over the SAT points (ratio-2.0 instances)")
    ck.info(f"    {'n':>3} {'instance':10s} {'#SAT':>5} {'rank(G)':>8} "
            f"{'lam_min':>10} {'lam_max':>10} {'cond':>8}")
    for n in range(3, NMAX + 1):
        for tag, clauses, cls in ALL[n]:
            if cls != "ratio2.0":
                continue
            S = sat_assignments(n, clauses)
            if not S:
                continue
            G = gram01(S, n + 3)
            gev = np.linalg.eigvalsh(G)
            rk = int((gev > 1e-12 * gev[-1]).sum())
            ck.info(f"    {n:>3} {tag:10s} {len(S):>5} {rk:>8} {gev[0]:>10.6g} "
                    f"{gev[-1]:>10.6g} {gev[-1]/max(gev[0], 1e-300):>8.3g}")
            ck.equal(rk, len(S), f"n={n} {tag}: Gram over SAT points is full rank")
            ck.atleast(float(gev[0]), SAT_GRAM_MIN,
                       f"n={n} {tag}: lam_min of the SAT Gram matrix "
                       f"(Conj. 8.6(ii): well conditioned, >= 0.13)")

    ck.info("\n  (7) Gram lam_min over the FULL hypercube {0,1}^n")
    ck.info(f"    {'n':>3} {'2^n':>6} {'lam_min(n+3)':>13} {'3.5e^-0.85n':>13} "
            f"{'ratio':>7} {'lam_min(2n)':>12} {'0.7e^-0.35n':>13} {'ratio':>7}")
    for n in range(3, NMAX + 1):
        pts = list(itertools.product((0, 1), repeat=n))
        l1 = float(np.linalg.eigvalsh(gram01(pts, n + 3))[0])
        l2 = float(np.linalg.eigvalsh(gram01(pts, 2 * n))[0])
        f1 = 3.5 * math.exp(-0.85 * n)
        f2 = 0.7 * math.exp(-0.35 * n)
        ck.info(f"    {n:>3} {2**n:>6} {l1:>13.6g} {f1:>13.6g} {l1/f1:>7.3f} "
                f"{l2:>12.6g} {f2:>13.6g} {l2/f2:>7.3f}")
        ck.close(l1 / f1, 1.0, FIT_BAND,
                 f"n={n}: full-hypercube Gram lam_min at N=n+3 vs the published "
                 f"3.5 e^(-0.85 n)")
        ck.close(l2 / f2, 1.0, FIT_BAND,
                 f"n={n}: full-hypercube Gram lam_min at N=2n vs the published "
                 f"0.7 e^(-0.35 n)")

    # ---- (8) overlap of Psi_bool with the ground space --------------------
    ck.info("\n  (8) <Psi|P_0|Psi> vs #SAT/2^n")
    ck.info(f"    {'n':>3} {'instance':10s} {'#SAT':>5} {'<Psi|P0|Psi>':>14} "
            f"{'#SAT/2^n':>10} {'ratio':>8} {'direct':>14} {'|diff|':>9}")
    for n in range(3, NMAX + 1):
        allpts = list(itertools.product((0, 1), repeat=n))
        N, nv = n + 3, n + 1
        Gall = gram01(allpts, N)
        Z = float(Gall.sum())
        for tag, clauses, cls in ALL[n]:
            S = sat_assignments(n, clauses)
            if not S:
                continue
            sidx = [allpts.index(x) for x in S]
            b = Gall[sidx, :].sum(axis=1)
            ov = float(b @ np.linalg.solve(Gall[np.ix_(sidx, sidx)], b) / Z)
            frac = len(S) / 2**n
            direct, diff = float('nan'), float('nan')
            if bf.dim_h(nv, N) <= DENSE_CAP:
                kd = hf_exact(n, clauses, N)
                A = stack_A(cnf_gens(n, clauses), N, nv)
                H = (A.T @ A).toarray()
                H = (H + H.T) / 2
                ev, U = np.linalg.eigh(H)
                Vall = coherent_matrix(allpts, N, nv)
                psi = Vall.sum(axis=1)
                psi /= np.linalg.norm(psi)
                direct = float(np.linalg.norm(U[:, :kd].T @ psi) ** 2)
                diff = abs(direct - ov)
            ck.info(f"    {n:>3} {tag:10s} {len(S):>5} {ov:>14.8g} "
                    f"{frac:>10.6g} {ov/frac:>8.4g} {direct:>14.8g} "
                    f"{diff:>9.2e}")
            ck.between(ov / frac, OVERLAP_RANGE[0], OVERLAP_RANGE[1],
                       f"n={n} {tag}: <Psi|P_0|Psi> / (#SAT/2^n) in the "
                       f"published range 1-12 (Conj. 8.6(ii))")
            if math.isfinite(diff):
                ck.atmost(diff, 1e-8,
                          f"n={n} {tag}: Gram formula for <Psi|P_0|Psi> vs the "
                          f"direct computation in the full Hilbert space")
    ck.info(f"\n  (total elapsed {time.time()-t0:.0f}s)")


if __name__ == "__main__":
    checkharness.run(
        "task8_cnf",
        "report.md Sect. 6 and Conj. 8.6 for the boolean + 3-CNF ideal: "
        f"HF = #SAT for N >= n+3, Delta_(n+3) in [0.25, 2.5], pure boolean gap "
        f"= 2, SAT coherent states in the kernel, Gram fits 3.5e^-0.85n and "
        f"0.7e^-0.35n, overlap gain 1-12; n = 3..{NMAX}",
        body)
