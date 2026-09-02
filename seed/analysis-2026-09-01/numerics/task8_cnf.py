"""Task 8: the boolean + 3-CNF ideal.

Ring C[z_0, z_1..z_n]  (z_0 homogenising).  Generators
    g_i = z_i^2 - z_i z_0                              (i = 1..n)
    c_C = prod_{literals of C} (z_0 - z_i) [pos lit x_i] or z_i [neg lit ~x_i]
K = (g_1..g_n, c_C).  c_C([1:x]) = 0 iff C is satisfied by x, so V(K) = SAT(phi)
(there are no points at infinity: z_0=0 forces every z_i=0 through g_i).

Conventions from bf.py: |k> = z^k/sqrt(k!), a_j = d_j, a^dag(f) = mult by f,
a(f) = sum_a conj(f_a) d^a, H_N = sum_j a^dag(f_j) a(f_j) on the degree-N piece.

Exact Hilbert-function machinery used here
------------------------------------------
{z_i^2 - z_i z_0} is a Groebner basis (pairwise coprime leading terms z_i^2 under
grlex with z_1>..>z_n>z_0), so A_N := R_N/(bool)_N has the basis
{ z_0^{N-|S|} z_S : S subset [n], |S| <= min(N,n) },  and the reduction of any
degree-N monomial z^e is the basis vector labelled by S = supp(e) cap [n].
Hence HF_{R/K}(N) = dim A_N - rank_N, where rank_N is the rank of the images of
z^beta c_C, |beta| = N-3.  That image depends on beta only through
T = supp(beta) cap [n], |T| <= min(N-3, n), which gives an exact rank problem of
size (#clauses * 2^n) x 2^n -- solved over GF(p).  This is cross-checked against
the GF(p) rank of the full Macaulay matrix wherever that is affordable, and
against the numerical kernel count of H_N wherever H_N is diagonalised densely.
"""
import numpy as np, math, itertools, sys, time, warnings
import scipy.sparse as sp
from scipy.sparse.linalg import eigsh, lobpcg, LinearOperator
import bf

DENSE_CAP = 6000
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
    return [{bf.emono(nv, [i, i]): 1, bf.emono(nv, [i, 0]): -1} for i in range(1, n + 1)]


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
    """every 3-clause on three distinct variables (C(n,3)*8 of them)."""
    out = []
    for vs in itertools.combinations(range(1, n + 1), 3):
        for sg in itertools.product((True, False), repeat=3):
            out.append(tuple(sorted(zip(vs, sg))))
    return out


def rand_3cnf(n, m, rng):
    """m random 3-clauses with three DISTINCT variables, random signs, deduplicated
    (m is capped at the number C(n,3)*8 of distinct such clauses)."""
    pool = all_clauses(n)
    m = min(m, len(pool))
    pick = rng.choice(len(pool), size=m, replace=False)
    return [pool[i] for i in sorted(pick)]


def unique_sol_instance(n, rng):
    """Genuine 3-distinct-literal instance with exactly one satisfying assignment:
    fix a random target x*, keep adding random clauses that x* satisfies (so x* stays
    a solution) until the solution count drops to 1."""
    pool = all_clauses(n)
    for _ in range(200):
        x = tuple(int(b) for b in rng.integers(0, 2, size=n))
        ok = [C for C in pool if any((x[i - 1] == 1) == pos for (i, pos) in C)]
        order = rng.permutation(len(ok))
        cl = []
        for j in order:
            cl.append(ok[j])
            ns = len(sat_assignments(n, cl))
            if ns == 1:
                # greedily prune redundant clauses -> a near-minimal instance
                changed = True
                while changed:
                    changed = False
                    for j in range(len(cl)):
                        trial = cl[:j] + cl[j + 1:]
                        if len(sat_assignments(n, trial)) == 1:
                            cl = trial
                            changed = True
                            break
                return cl
    return None


def degenerate_unique(n, target):
    """clauses (l_i v l_i v l_i) with l_i the literal true at the target string."""
    return [tuple([(i + 1, bool(target[i]))] * 3) for i in range(n)]


# ------------------------------------------------- exact HF via boolean quotient
def subsets_upto(n, smax):
    out = []
    for s in range(smax + 1):
        out.extend(itertools.combinations(range(1, n + 1), s))
    return out


def hf_exact(n, clauses, N):
    """HF_{R/K}(N), exact, by the boolean-quotient reduction described above."""
    if N < 0:
        return 0
    nv = n + 1
    smax = min(N, n)
    subs = subsets_upto(n, smax)
    sidx = {S: i for i, S in enumerate(subs)}
    dimA = len(subs)
    if N < 3:
        return dimA                      # no clause multiples in degree < 3
    tmax = min(N - 3, n)
    rows = []
    for C in clauses:
        c = clause_poly(nv, C)
        terms = [(frozenset(j for j in range(1, nv) if a[j] > 0), ca) for a, ca in c.items()]
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
    R = np.array(rows, dtype=np.int64)
    R = np.unique(R, axis=0)
    rk = bf.rank_mod_p([list(map(int, r)) for r in R])
    return dimA - rk


def hf_macaulay(gens, N, nv):
    """cross-check: dim R_N - rank_GF(p)(full Macaulay matrix)."""
    rows = bf.macaulay_rows(gens, N)
    rows = [[int(round(x.real)) if isinstance(x, complex) else int(round(x)) for x in r]
            for r in rows]
    return bf.dim_h(nv, N) - bf.rank_mod_p(rows)


# ------------------------------------------------------------------ sparse a(f)
_PASCAL = np.zeros((80, 80), dtype=np.int64)
_PASCAL[0, 0] = 1
for _i in range(1, 80):
    _PASCAL[_i, 0] = 1
    _PASCAL[_i, 1:] = _PASCAL[_i - 1, 1:] + _PASCAL[_i - 1, :-1]


def mono_index_vec(K, nv, deg):
    """Vectorised position of each row of K (exponent tuples of degree `deg`) in
    bf.monomials(nv, deg).  bf enumerates the first coordinate descending, so
      idx = sum_{a>k_0} dim_h(nv-1, deg-a) + idx(k_1..; nv-1, deg-k_0),
    and the inner sum telescopes by the hockey-stick identity to C(B+r, r)."""
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


def _check_mono_index_vec():
    for nv in (2, 4, 6):
        for deg in (0, 1, 3, 5):
            M = np.array(bf.monomials(nv, deg), dtype=np.int64)
            got = mono_index_vec(M, nv, deg)
            assert np.array_equal(got, np.arange(len(M))), (nv, deg)
    return True


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
        II.append(rr); JJ.append(idx); VV.append(float(np.real(ca)) * np.sqrt(ff))
    if not II:
        return None
    return sp.csr_matrix((np.concatenate(VV), (np.concatenate(II), np.concatenate(JJ))),
                         shape=(R, C.shape[0]))


def stack_A(gens, N, nv):
    B = [ann_sparse(f, N) for f in gens]
    B = [b for b in B if b is not None and b.shape[0] > 0]
    if not B:
        return sp.csr_matrix((0, bf.dim_h(nv, N)))
    return sp.vstack(B, format='csr')


# ------------------------------------------------------------- coherent states
def coherent_matrix(pts, N, nv):
    """columns = normalised |p_x>^{ox N}, amplitude_k = sqrt(N!/k!) p^k, p=(1,x)/||.||"""
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
    """<p_x|p_y>^N for p = (1,x)/||.||  =  (1+|x&y|)^N / ((1+|x|)(1+|y|))^{N/2}"""
    X = np.array(pts, dtype=np.int64)
    if X.size == 0:
        return np.zeros((0, 0))
    w = 1.0 + X.sum(axis=1)
    inter = 1.0 + X @ X.T
    lw = np.log(w)
    return np.exp(N * (np.log(inter) - 0.5 * (lw[:, None] + lw[None, :])))


# ------------------------------------------------------------------ spectra
def spectral(gens, N, nv, sat_pts, kd_exact, want_dense=None, kextra=3):
    """Delta_N, ||H_N||, numerical kernel dim, coherent-state diagnostics."""
    D = bf.dim_h(nv, N)
    A = stack_A(gens, N, nv)
    V = coherent_matrix(sat_pts, N, nv) if len(sat_pts) else np.zeros((D, 0))
    res = dict(N=N, dim=D, kd=kd_exact, nsat=len(sat_pts), nnzA=A.nnz)

    # coherent-state diagnostics (independent of how H is diagonalised)
    if V.shape[1]:
        Uv, s, _ = np.linalg.svd(V, full_matrices=False)
        res['V_rank'] = int((s > 1e-10 * s[0]).sum())
        res['V_smin'] = float(s[-1])
        Q = Uv[:, :res['V_rank']]
        res['AVres'] = float(np.linalg.norm(A @ V) / max(np.linalg.norm(V), 1e-300))
    else:
        res['V_rank'] = 0; res['V_smin'] = float('nan'); res['AVres'] = 0.0
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
        res['zsep'] = res['gap'] / max(abs(ev[kd_exact - 1]), 1e-300) if kd_exact > 0 else float('inf')
        res['mode'] = 'dense'
        if V.shape[1]:
            P = U[:, :kd_exact]
            res['projres'] = float(np.linalg.norm(V - P @ (P.T @ V)) / np.linalg.norm(V))
        else:
            res['projres'] = 0.0
        res['_U'] = U; res['_ev'] = ev
    else:
        AT = A.T.tocsr()
        Hmv = lambda X: AT @ (A @ X)
        Hop = LinearOperator((D, D), matvec=Hmv, matmat=Hmv, dtype=float)
        norm = float(eigsh(Hop, k=1, which='LA', tol=1e-9,
                           return_eigenvectors=False, maxiter=20000)[0])
        res['norm'] = norm
        c = norm                       # deflation: kernel states are pushed to +c
        if Q.shape[1]:
            Mmv = lambda X: AT @ (A @ X) + c * (Q @ (Q.T @ X))
        else:
            Mmv = Hmv
        Mop = LinearOperator((D, D), matvec=Mmv, matmat=Mmv, dtype=float)
        lams, resids = [], []
        seeds = (0, 1) if D <= 60000 else (0,)   # two random starts where affordable
        for seed in seeds:
            rs = np.random.default_rng(seed)
            X = rs.normal(size=(D, 8))
            with warnings.catch_warnings():
                warnings.simplefilter("ignore")
                lam, U = lobpcg(Mop, X, largest=False, tol=1e-9, maxiter=3000)
            o = np.argsort(lam); lam = lam[o]; U = U[:, o]
            rr = np.linalg.norm(Mmv(U) - U * lam[None, :], axis=0)
            lams.append(lam); resids.append(rr)
        j = int(np.argmin([l[0] for l in lams]))
        res['gap'] = float(lams[j][0])
        res['ev_low'] = lams[j][:4]
        res['lobpcg_resid'] = float(resids[j][0])
        res['lobpcg_seed_spread'] = (float(abs(lams[0][0] - lams[1][0]))
                                     if len(lams) > 1 else 0.0)
        res['kernum'] = -1               # certified instead via V_rank + AVres + gap
        res['zsep'] = float('nan')
        res['projres'] = float('nan')
        res['mode'] = 'sparse(deflated)' 
    return res


# ------------------------------------------------------------------ instances
_INST_CACHE = {}


def make_instances(n, seed=0):
    """9 instances per n:  3 random at clause/variable ratio 4.2 (near threshold),
    3 random at ratio 2.0 (many solutions), 1 guaranteed-UNSAT at ratio 4.2,
    1 degenerate unique-solution ((l v l v l) clauses), 1 genuine 3-distinct-literal
    unique-solution instance found by brute force."""
    if (n, seed) in _INST_CACHE:
        return _INST_CACHE[(n, seed)]
    rng = np.random.default_rng(1000 * n + seed)
    inst = []
    for r in range(3):
        cl = rand_3cnf(n, int(round(4.2 * n)), rng)
        inst.append((f"r4.2-{r}", cl, "ratio4.2"))
    for r in range(3):
        cl = rand_3cnf(n, int(round(2.0 * n)), rng)
        inst.append((f"r2.0-{r}", cl, "ratio2.0"))
    # guaranteed UNSAT (resample at 4.2, then raise the ratio if needed)
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
    _INST_CACHE[(n, seed)] = inst
    return inst


# ------------------------------------------------------------------ main
def main():
    try:
        sys.stdout.reconfigure(line_buffering=True)
    except Exception:
        pass
    t0 = time.time()
    NS_A = [3, 4, 5, 6, 7]          # full N-sweep (exact rank + dense eigh affordable)
    NS = [3, 4, 5, 6, 7, 8]        # gap scaling
    ALL = {}

    print("=" * 100)
    print("TASK 8: boolean + 3-CNF ideal   K = (z_i^2 - z_i z_0 ; c_C)")
    print("=" * 100)

    # ------------------------------------------------ solver validation
    print("\n########## (0) validation of the sparse deflated LOBPCG solver ##########")
    print("same instance solved by (i) dense eigh of H_N and (ii) LOBPCG on")
    print("H_N + ||H_N|| Q Q^T with Q = orthonormalised coherent states at SAT points.")
    print(f"  {'n':>3} {'instance':10s} {'N':>3} {'dim':>6} {'#SAT':>5} {'kd(exact)':>10} "
          f"{'kerNum(dense)':>14} {'Delta(dense)':>14} {'Delta(sparse)':>14} {'|diff|':>10} "
          f"{'lobpcg res':>11} {'seed spread':>12}")
    assert _check_mono_index_vec()
    for n in (4, 5, 6):
        for tag, clauses, cls in make_instances(n)[:1] + make_instances(n)[3:5] + make_instances(n)[6:]:
            N = n + 3
            nv = n + 1
            S = sat_assignments(n, clauses)
            kd = hf_exact(n, clauses, N)
            rd = spectral(cnf_gens(n, clauses), N, nv, S, kd, want_dense=True)
            rs_ = spectral(cnf_gens(n, clauses), N, nv, S, kd, want_dense=False)
            print(f"  {n:>3} {tag:10s} {N:>3} {rd['dim']:>6} {len(S):>5} {kd:>10} "
                  f"{rd['kernum']:>14} {rd['gap']:>14.9g} {rs_['gap']:>14.9g} "
                  f"{abs(rd['gap']-rs_['gap']):>10.2e} {rs_['lobpcg_resid']:>11.2e} "
                  f"{rs_['lobpcg_seed_spread']:>12.2e}", flush=True)
            rd.pop('_U', None); rd.pop('_ev', None)

    # =================================================== (a) kernel dimension
    print("\n\n########## (a) dim ker H_N(K) vs #SAT ##########")
    print("exact HF from the boolean-quotient rank (GF(p)); 'MacGFp' = dim R_N - rank(full")
    print("Macaulay) over GF(p), computed where dim R_N <= 400; 'kerNum' = # eigenvalues")
    print("< 1e-9 ||H_N|| from a dense eigh (dim <= 6000).  n+3 marked with *.")
    hfrec = {}
    for n in NS:
        ALL[n] = make_instances(n)
    for n in NS_A:
        nv = n + 1
        insts = ALL[n]
        print(f"\n--- n = {n}  (dim R_N = C(N+{n},{n})) ---")
        for tag, clauses, cls in insts:
            S = sat_assignments(n, clauses)
            print(f"  [{tag:10s} {cls:18s}] m={len(clauses):3d} clauses, #SAT={len(S)}")
            hdr = f"    {'N':>3} {'dimR_N':>7} {'HFexact':>8} {'MacGFp':>7} {'kerNum':>7}  note"
            print(hdr)
            for N in range(2, n + 5):
                D = bf.dim_h(nv, N)
                he = hf_exact(n, clauses, N)
                mg = hf_macaulay(cnf_gens(n, clauses), N, nv) if D <= 400 else None
                kn = None
                if D <= DENSE_CAP:
                    A = stack_A(cnf_gens(n, clauses), N, nv)
                    H = (A.T @ A).toarray(); H = (H + H.T) / 2
                    ev = np.linalg.eigvalsh(H)
                    kn = int((ev < 1e-9 * max(ev[-1], 1e-300)).sum())
                note = ""
                if N == n + 3:
                    note += "*  <- N=n+3"
                if he == len(S):
                    note += "  [= #SAT]"
                print(f"    {N:>3} {D:>7} {he:>8} {str(mg):>7} {str(kn):>7}  {note}", flush=True)
                hfrec.setdefault((n, tag), {})[N] = he
        print(f"    (elapsed {time.time()-t0:.0f}s)", flush=True)

    print("\n--- (a) summary: smallest N with HF(N') = #SAT for all N' in [N, n+4] ---")
    print(f"  {'n':>3} {'instance':12s} {'class':18s} {'m':>3} {'#SAT':>5} {'N_stab':>7} "
          f"{'n+3':>5} {'N_stab-n':>9}  HF at N = 2..n+4")
    for n in NS_A:
        for tag, clauses, cls in ALL[n]:
            S = sat_assignments(n, clauses)
            rec = hfrec[(n, tag)]
            Nlist = sorted(rec)
            nst = None
            for i, N in enumerate(Nlist):
                if all(rec[M] == len(S) for M in Nlist[i:]):
                    nst = N
                    break
            print(f"  {n:>3} {tag:12s} {cls:18s} {len(clauses):>3} {len(S):>5} {str(nst):>7} "
                  f"{n+3:>5} {str(nst-n) if nst is not None else '-':>9}  "
                  + " ".join(f"{rec[N]}" for N in Nlist))

    # =================================================== (b) gaps
    print("\n\n########## (b) spectral gap Delta_N and ||H_N|| ##########")
    print("kernel dimension taken from the EXACT HF; Delta_N = smallest nonzero eigenvalue.")
    print("dense: full eigh.  sparse: Delta = lambda_min(H + ||H|| Q Q^T), Q = orthonormal")
    print("basis of the coherent states at SAT points (validity certified by V_rank=#SAT,")
    print("||A V||/||V|| ~ 0 and HFexact = #SAT).")
    GAPS = {}
    for n in NS:
        nv = n + 1
        print(f"\n--- n = {n} ---")
        print(f"  {'instance':12s} {'class':18s} {'m':>3} {'#SAT':>5} {'N':>3} {'dim':>6} "
              f"{'ker':>5} {'kerNum':>7} {'Delta_N':>12} {'||H_N||':>12} {'ratio':>9} "
              f"{'V_rank':>6} {'AVres':>9} {'chk':>9} {'mode':>16}")
        for tag, clauses, cls in ALL[n]:
            S = sat_assignments(n, clauses)
            Ns = [n + 3, n + 4]
            for N in Ns:
                D = bf.dim_h(nv, N)
                if N == n + 4 and n == 7 and tag not in ("r4.2-0", "r2.0-0", "unsat",
                                                          "uniq-3lit"):
                    continue
                if N == n + 4 and n >= 8:
                    continue          # dim R_{12} = 125970 at n=8: out of budget
                kd = hf_exact(n, clauses, N)
                r = spectral(cnf_gens(n, clauses), N, nv, S, kd)
                GAPS.setdefault((cls, N - n), []).append((n, tag, r['gap'], r['norm'], len(S)))
                chk = (r['zsep'] if r['mode'] == 'dense'
                       else max(r['lobpcg_resid'], r['lobpcg_seed_spread']))
                print(f"  {tag:12s} {cls:18s} {len(clauses):>3} {len(S):>5} {N:>3} {D:>6} "
                      f"{kd:>5} {r['kernum']:>7} {r['gap']:>12.6g} {r['norm']:>12.6g} "
                      f"{r['norm']/max(r['gap'],1e-300):>9.4g} {r['V_rank']:>6} "
                      f"{r['AVres']:>9.2e} {chk:>9.2e} {r['mode']:>16}", flush=True)
                r.pop('_U', None); r.pop('_ev', None)
        print(f"    (elapsed {time.time()-t0:.0f}s)", flush=True)

    # boolean-only reference
    print("\n--- pure boolean ideal (no clauses), for comparison ---")
    print(f"  {'n':>3} {'N':>3} {'dim':>7} {'ker=2^n':>8} {'kerNum':>7} {'Delta_N':>12} {'||H_N||':>12}")
    for n in NS:
        nv = n + 1
        for N in (n + 1, n + 2, n + 3):
            D = bf.dim_h(nv, N)
            if D > 40000:
                print(f"  {n:>3} {N:>3} {D:>7}   (skipped: dim too large with a 2^n-fold deflation)")
                continue
            pts = list(itertools.product((0, 1), repeat=n))
            kd = hf_exact(n, [], N)
            r = spectral(boolean_gens(n), N, nv, pts, kd)
            print(f"  {n:>3} {N:>3} {D:>7} {kd:>8} {r['kernum']:>7} {r['gap']:>12.6g} "
                  f"{r['norm']:>12.6g}", flush=True)
            r.pop('_U', None); r.pop('_ev', None)

    # fits
    print("\n--- fits of Delta_N vs n, per class (N = n+3 and n+4) ---")
    print(f"  {'class':20s} {'points (n, Delta)':60s} {'power  Delta~c n^a':28s} {'exp  Delta~c e^{bn}':26s}")
    for (cls, off), rows in sorted(GAPS.items()):
        print(f"  [N = n+{off}]")
        by_n = {}
        for (n, tag, g, nrm, ns) in rows:
            by_n.setdefault(n, []).append(g)
        ns_ = sorted(by_n)
        gs = [float(np.mean(by_n[n])) for n in ns_]
        gmin = [float(np.min(by_n[n])) for n in ns_]
        pts = " ".join(f"{n}:{g:.4g}" for n, g in zip(ns_, gs))
        if len(ns_) >= 3:
            gs = gs  # mean over the instances of this class
            a = np.polyfit(np.log(ns_), np.log(gs), 1)
            b = np.polyfit(ns_, np.log(gs), 1)
            r_pow = np.corrcoef(np.log(ns_), np.log(gs))[0, 1] ** 2
            r_exp = np.corrcoef(ns_, np.log(gs))[0, 1] ** 2
            print(f"  {cls:20s} {pts:60s} c={math.exp(a[1]):.3g} a={a[0]:+.3f} R2={r_pow:.3f}  "
                  f"| c={math.exp(b[1]):.3g} b={b[0]:+.4f} R2={r_exp:.3f}")
            print(f"  {'':20s} min over instances: " + " ".join(f"{n}:{g:.4g}" for n, g in zip(ns_, gmin)))

    print("\n--- OVERALL: worst (smallest) Delta_{n+3} over ALL instances at each n ---")
    allrows = {}
    for (cls, off), rows in GAPS.items():
        if off != 3:
            continue
        for (n, tag, g, nrm, ns) in rows:
            allrows.setdefault(n, []).append((g, tag, cls))
    ns_ = sorted(allrows)
    worst = [min(allrows[n])[0] for n in ns_]
    who = [min(allrows[n])[1] for n in ns_]
    med = [float(np.median([x[0] for x in allrows[n]])) for n in ns_]
    print("  n            : " + " ".join(f"{n:>10d}" for n in ns_))
    print("  min Delta    : " + " ".join(f"{g:>10.5f}" for g in worst))
    print("  attained by  : " + " ".join(f"{t:>10s}" for t in who))
    print("  median Delta : " + " ".join(f"{g:>10.5f}" for g in med))
    print("  1/min Delta  : " + " ".join(f"{1/g:>10.4f}" for g in worst))
    if len(ns_) >= 3:
        a = np.polyfit(np.log(ns_), np.log(worst), 1)
        b = np.polyfit(ns_, np.log(worst), 1)
        rp = np.corrcoef(np.log(ns_), np.log(worst))[0, 1] ** 2
        re = np.corrcoef(ns_, np.log(worst))[0, 1] ** 2
        print(f"  worst-case power fit: Delta_min ~ {math.exp(a[1]):.4g} * n^({a[0]:+.4f})  R2={rp:.4f}"
              f"   -> extrapolated Delta_min(n=50) = {math.exp(a[1])*50**a[0]:.4g}")
        print(f"  worst-case exp   fit: Delta_min ~ {math.exp(b[1]):.4g} * exp({b[0]:+.4f} n)  R2={re:.4f}"
              f"   -> extrapolated Delta_min(n=50) = {math.exp(b[1])*math.exp(b[0]*50):.4g}")
        am = np.polyfit(np.log(ns_), np.log(med), 1)
        bm = np.polyfit(ns_, np.log(med), 1)
        print(f"  median    power fit: Delta_med ~ {math.exp(am[1]):.4g} * n^({am[0]:+.4f})"
              f"   R2={np.corrcoef(np.log(ns_), np.log(med))[0,1]**2:.4f}")
        print(f"  median    exp   fit: Delta_med ~ {math.exp(bm[1]):.4g} * exp({bm[0]:+.4f} n)"
              f"   R2={np.corrcoef(ns_, np.log(med))[0,1]**2:.4f}")

    # =================================================== (c) Gram conditioning
    print("\n\n########## (c) coherent-state ground space / Gram conditioning ##########")
    print("Gram G_xy = (1+|x&y|)^N / ((1+|x|)(1+|y|))^{N/2}  over the SAT points, N = n+3.")
    print(f"  {'n':>3} {'instance':12s} {'#SAT':>5} {'rank(G)':>8} {'lam_min(G)':>12} "
          f"{'lam_max(G)':>12} {'cond':>10} {'||A V||/||V||':>14} {'||(1-P0)V||/||V||':>18}")
    for n in NS:
        for tag, clauses, cls in ALL[n]:
            if cls != "ratio2.0" and tag not in ("r4.2-0", "uniq-3lit"):
                continue
            S = sat_assignments(n, clauses)
            if not S:
                print(f"  {n:>3} {tag:12s} {0:>5}   (UNSAT: ground space is empty)")
                continue
            N = n + 3
            nv = n + 1
            G = gram01(S, N)
            gev = np.linalg.eigvalsh(G)
            rk = int((gev > 1e-12 * gev[-1]).sum())
            V = coherent_matrix(S, N, nv)
            if bf.dim_h(nv, N) <= 200000:
                A = stack_A(cnf_gens(n, clauses), N, nv)
                avres = float(np.linalg.norm(A @ V) / np.linalg.norm(V))
            else:
                avres = float('nan')
            if bf.dim_h(nv, N) <= DENSE_CAP:
                H = (A.T @ A).toarray(); H = (H + H.T) / 2
                ev, U = np.linalg.eigh(H)
                kd = hf_exact(n, clauses, N)
                P = U[:, :kd]
                projres = float(np.linalg.norm(V - P @ (P.T @ V)) / np.linalg.norm(V))
            else:
                projres = float('nan')
            print(f"  {n:>3} {tag:12s} {len(S):>5} {rk:>8} {gev[0]:>12.6g} {gev[-1]:>12.6g} "
                  f"{gev[-1]/max(gev[0],1e-300):>10.3g} {avres:>14.2e} "
                  f"{projres:>18.2e}", flush=True)

    print("\n  Gram lam_min for the FULL boolean set (all 2^n points), N = n+3 and n+1:")
    print(f"  {'n':>3} {'2^n':>6} {'lam_min(N=n+1)':>16} {'lam_min(N=n+3)':>16} {'lam_min(N=2n)':>16}")
    for n in NS:
        pts = list(itertools.product((0, 1), repeat=n))
        vals = []
        for N in (n + 1, n + 3, 2 * n):
            G = gram01(pts, N)
            vals.append(np.linalg.eigvalsh(G)[0])
        print(f"  {n:>3} {2**n:>6} {vals[0]:>16.6g} {vals[1]:>16.6g} {vals[2]:>16.6g}")

    # =================================================== (d) overlap test
    print("\n\n########## (d) overlap of |Psi_bool> with the ground space ##########")
    print("|Psi_bool> ~ sum_{x in {0,1}^n} |p^_x>^{ox N};  <Psi|P_0|Psi> computed from the")
    print("2^n x 2^n Gram matrix:  P_0 = V_S (V_S^T V_S)^{-1} V_S^T, S = SAT points.")
    print(f"  {'n':>3} {'instance':12s} {'class':18s} {'#SAT':>5} {'N':>3} "
          f"{'<Psi|P0|Psi>':>14} {'#SAT/2^n':>11} {'ratio':>9} {'#SAT/dimR_N':>13} "
          f"{'gain vs mixed':>14}")
    for n in NS:
        allpts = list(itertools.product((0, 1), repeat=n))
        for tag, clauses, cls in ALL[n]:
            S = sat_assignments(n, clauses)
            N = n + 3
            D = bf.dim_h(n + 1, N)
            Gall = gram01(allpts, N)
            Z = Gall.sum()
            if S:
                sidx = [allpts.index(x) for x in S]
                Gss = Gall[np.ix_(sidx, sidx)]
                b = Gall[sidx, :].sum(axis=1)
                ov = float(b @ np.linalg.solve(Gss, b) / Z)
            else:
                ov = 0.0
            frac = len(S) / 2 ** n
            mixed = len(S) / D
            print(f"  {n:>3} {tag:12s} {cls:18s} {len(S):>5} {N:>3} {ov:>14.8g} "
                  f"{frac:>11.6g} {ov/frac if frac else float('nan'):>9.4g} {mixed:>13.6g} "
                  f"{ov/mixed if mixed else float('nan'):>14.4g}", flush=True)

    # direct big-space verification of (d) for a couple of small cases
    print("\n  direct verification of (d) in the full Hilbert space (dense cases):")
    for n in (3, 4, 5):
        allpts = list(itertools.product((0, 1), repeat=n))
        for tag, clauses, cls in ALL[n][:1] + ALL[n][3:4]:
            S = sat_assignments(n, clauses)
            N = n + 3
            nv = n + 1
            kd = hf_exact(n, clauses, N)
            A = stack_A(cnf_gens(n, clauses), N, nv)
            H = (A.T @ A).toarray(); H = (H + H.T) / 2
            ev, U = np.linalg.eigh(H)
            Vall = coherent_matrix(allpts, N, nv)
            psi = Vall.sum(axis=1); psi /= np.linalg.norm(psi)
            P = U[:, :kd]
            ov_direct = float(np.linalg.norm(P.T @ psi) ** 2)
            Gall = gram01(allpts, N); Z = Gall.sum()
            if S:
                sidx = [allpts.index(x) for x in S]
                b = Gall[sidx, :].sum(axis=1)
                ov_gram = float(b @ np.linalg.solve(Gall[np.ix_(sidx, sidx)], b) / Z)
            else:
                ov_gram = 0.0
            print(f"    n={n} {tag:10s} #SAT={len(S):3d}: direct={ov_direct:.10g}  "
                  f"gram={ov_gram:.10g}  |diff|={abs(ov_direct-ov_gram):.2e}  "
                  f"#SAT/2^n={len(S)/2**n:.10g}", flush=True)

    print(f"\n\n(total elapsed {time.time()-t0:.0f}s)")


if __name__ == "__main__":
    main()
