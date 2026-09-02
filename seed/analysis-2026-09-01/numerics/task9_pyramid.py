"""Task 9: toric 'pyramid' counterexample -- does an unused variable pin Delta_N?

Ring C[x00,x01,x10,x11,y]  (variable indices 0,1,2,3,4), ideal (x00 x11 - x01 x10).
Compare with the same binomial in C[x00,x01,x10,x11] (no y), and with the twisted
cubic in C[z0..z3] with a dummy variable w adjoined.

Conventions as in bf.py:  |k> = z^k/sqrt(k!), a(f) = sum_a conj(f_a) d^a,
H_N = sum_j a^dag(f_j) a(f_j) restricted to degree N.  ker H_N = (I_N)^perp.
"""
import numpy as np, math, sys
import bf

np.set_printoptions(linewidth=200)


def hf_quadric(nv, N):
    return bf.dim_h(nv, N) - bf.dim_h(nv, N - 2)


def hf_tc_dummy(N):
    # R/(I_tc) tensor C[w]; HF_tc(M) = 3M+1
    return sum(3 * (N - j) + 1 for j in range(0, N + 1))


def analyse(name, nv, gens, Ns, hf, dumvar=None, exact_rank_cap=1400):
    """dumvar: index of the 'unused' variable, for eigenvector diagnostics."""
    print(f"\n=== {name} ===")
    print(f"{'N':>3} {'dim':>6} {'HF':>6} {'rkGFp':>7} {'kerNum':>7} {'Delta_N':>12} "
          f"{'||H_N||':>12} {'||H||/D':>9} {'zero-sep':>10}  eigvec diagnostics")
    out = []
    for N in Ns:
        D = bf.dim_h(nv, N)
        H = bf.hamiltonian(gens, N, dtype=float).real
        H = (H + H.T) / 2
        ev, U = np.linalg.eigh(H)
        norm = ev[-1]
        kd = hf(N)
        kernum = int((ev < 1e-9 * max(norm, 1e-300)).sum())
        # exact cross-check: rank of Macaulay matrix over GF(p)
        if D <= exact_rank_cap:
            rows = bf.macaulay_rows(gens, N)
            rk = bf.rank_mod_p([[int(round(x.real)) for x in r] for r in rows])
            hf_exact = D - rk
        else:
            hf_exact = None
        gap = ev[kd] if kd < D else float('nan')
        zmax = abs(ev[kd - 1]) if kd > 0 else 0.0
        # eigenvector diagnostics: distribution over the degree in `dumvar`
        diag = ""
        if dumvar is not None and kd < D:
            mons = bf.monomials(nv, N)
            v = U[:, kd]
            dy = np.array([m[dumvar] for m in mons])
            w = v**2
            wt = np.array([w[dy == d].sum() for d in range(N + 1)])
            top = int(np.argmax(wt))
            diag = (f"lam2 eigvec: max weight on deg_y={top} (w={wt[top]:.4f}); "
                    f"weight on deg_y=N-2: {wt[N-2] if N>=2 else float('nan'):.4f}")
        print(f"{N:>3} {D:>6} {kd:>6} {str(hf_exact):>7} {kernum:>7} {gap:>12.8g} "
              f"{norm:>12.8g} {ratio(norm, gap):>9.4g} {gap/max(zmax,1e-300):>10.2e}  {diag}",
              flush=True)
        out.append((N, D, kd, hf_exact, kernum, gap, norm))
    return out


def ratio(a, b):
    return a / b if b else float('inf')


def fits(tag, Ns, gaps):
    Ns = np.asarray(Ns, float); g = np.asarray(gaps, float)
    m = (g > 0) & np.isfinite(g)
    if m.sum() < 3:
        return
    pw = np.polyfit(np.log(Ns[m]), np.log(g[m]), 1)
    ex = np.polyfit(Ns[m], np.log(g[m]), 1)
    lin = np.polyfit(Ns[m], g[m], 1)
    print(f"  {tag}: power fit Delta ~ {math.exp(pw[1]):.4g} N^({pw[0]:+.4f}) ; "
          f"exp fit log Delta = {ex[0]:+.4f} N + {ex[1]:+.3f} ; "
          f"linear fit Delta = {lin[0]:+.4f} N {lin[1]:+.4f}")


if __name__ == "__main__":
    print("=== Task 9: toric pyramid / unused-variable counterexample ===")
    print("H_N = a^dag(f) a(f)|_{deg N}, f = x00 x11 - x01 x10")

    # ---- (1) pyramid: 5 variables, y unused by the generator ----
    nv = 5
    f5 = {(1, 0, 0, 1, 0): 1.0, (0, 1, 1, 0, 0): -1.0}
    r1 = analyse("PYRAMID  C[x00,x01,x10,x11,y] / (x00 x11 - x01 x10)", nv, [f5],
                 range(2, 9), lambda N: hf_quadric(5, N), dumvar=4)
    fits("pyramid", [r[0] for r in r1], [r[5] for r in r1])

    # ---- (2) same binomial, no extra variable ----
    nv = 4
    f4 = {(1, 0, 0, 1): 1.0, (0, 1, 1, 0): -1.0}
    r2 = analyse("NO-y     C[x00,x01,x10,x11] / (x00 x11 - x01 x10)", nv, [f4],
                 range(2, 13), lambda N: hf_quadric(4, N))
    fits("no-y", [r[0] for r in r2], [r[5] for r in r2])

    # ---- (3) twisted cubic with a dummy variable w adjoined ----
    nv = 5
    gtc = bf.minors2x2(5, [0, 1, 2], [1, 2, 3])   # only uses z0..z3
    gtc = [{k: float(v) for k, v in g.items()} for g in gtc]
    r3 = analyse("TC+DUMMY C[z0,z1,z2,z3,w] / I_twisted_cubic", nv, gtc,
                 range(2, 13), hf_tc_dummy, dumvar=4)
    fits("tc+dummy", [r[0] for r in r3], [r[5] for r in r3])

    # ---- (4) plain twisted cubic (reference, from task 4) ----
    gtc4 = [{k: float(v) for k, v in g.items()} for g in bf.minors2x2(4, [0, 1, 2], [1, 2, 3])]
    r4 = analyse("TC plain C[z0..z3] / I_twisted_cubic (reference)", 4, gtc4,
                 range(2, 13), lambda N: 3 * N + 1)
    fits("tc plain", [r[0] for r in r4], [r[5] for r in r4])

    # ---- summary table ----
    print("\n--- summary: Delta_N ---")
    print(f"{'N':>3} {'pyramid(5v)':>13} {'no-y(4v)':>12} {'TC+dummy(5v)':>14} {'TC plain(4v)':>14}")
    d1 = {r[0]: r[5] for r in r1}; d2 = {r[0]: r[5] for r in r2}
    d3 = {r[0]: r[5] for r in r3}; d4 = {r[0]: r[5] for r in r4}
    for N in range(2, 13):
        row = [d.get(N) for d in (d1, d2, d3, d4)]
        print(f"{N:>3} " + " ".join(f"{('%.8g'%v) if v is not None else '-':>13}" for v in row))

    # ---- where is the minimiser for the pyramid? explicit check on y^{N-2}*quadric ----
    print("\n--- pyramid: is the minimum attained inside y^{N-2} * (degree-2 in x)? ---")
    nvp = 5
    for N in range(2, 9):
        mons = bf.monomials(nvp, N)
        idx = bf.mono_index(nvp, N)
        H = bf.hamiltonian([f5], N, dtype=float).real
        H = (H + H.T) / 2
        # subspace spanned by y^{N-2} * (monomials of degree 2 in x00..x11)
        sel = [idx[m2 + (N - 2,)] for m2 in bf.monomials(4, 2)]
        Hs = H[np.ix_(sel, sel)]
        e = np.linalg.eigvalsh(Hs)
        kd = int((e < 1e-9 * max(e[-1], 1)).sum())
        ev = np.linalg.eigvalsh(H)
        kdfull = hf_quadric(5, N)
        print(f"  N={N:2d}: dim(y^(N-2)*x-quadrics)={len(sel)}, its spectrum={np.round(e,10)}, "
              f"lam_min>0 there = {e[kd] if kd < len(e) else float('nan'):.8g}, "
              f"global Delta_N = {ev[kdfull]:.8g}")
