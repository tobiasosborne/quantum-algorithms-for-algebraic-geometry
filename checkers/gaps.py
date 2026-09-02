"""Shared gap-computation driver.

Kernel dimension is supplied by the (task-2-verified) Hilbert function; the
'zero-sep' column = Delta_N / (largest eigenvalue declared zero) is the internal
consistency check that the split is unambiguous (should be huge).
"""
import numpy as np, math, bf

def kerdim_numeric(ev, norm, rtol=1e-9):
    return int((ev < rtol*max(norm, 1e-300)).sum())

def gap_row(gens, N, kd=None, rtol=1e-9):
    nv = bf.poly_nvars(gens[0])
    d = bf.dim_h(nv, N)
    H = bf.hamiltonian(gens, N)
    H = (H + H.conj().T)/2
    ev = np.linalg.eigvalsh(H)
    norm = ev[-1]
    kdn = kerdim_numeric(ev, norm, rtol)
    if kd is None:
        kd = kdn
    gap = ev[kd] if kd < d else float('nan')
    zmax = abs(ev[kd-1]) if kd > 0 else 0.0
    return dict(N=N, dim=d, ker=kd, kernum=kdn, gap=gap, norm=norm,
                ratio=norm/gap if gap else float('inf'),
                sep=gap/max(zmax, 1e-300))

def fit_power(Ns, ys):
    Ns = np.asarray(Ns, float); ys = np.asarray(ys, float)
    m = (ys > 0) & np.isfinite(ys)
    if m.sum() < 2: return float('nan'), float('nan')
    A = np.vstack([np.log(Ns[m]), np.ones(int(m.sum()))]).T
    c, *_ = np.linalg.lstsq(A, np.log(ys[m]), rcond=None)
    return c[0], math.exp(c[1])

def table(name, gens, Ns, hf=None, fitfrom=None, rtol=1e-9):
    print(f"\n--- {name} ---", flush=True)
    print(f"{'N':>3} {'dim':>6} {'ker':>5} {'kerNum':>7} {'Delta_N':>13} {'||H_N||':>13} "
          f"{'||H||/Delta':>12} {'zero-sep':>10}")
    rows = []
    for N in Ns:
        kd = hf(N) if hf else None
        r = gap_row(gens, N, kd, rtol)
        rows.append(r)
        print(f"{r['N']:>3} {r['dim']:>6} {r['ker']:>5} {r['kernum']:>7} {r['gap']:>13.6g} "
              f"{r['norm']:>13.6g} {r['ratio']:>12.4g} {r['sep']:>10.2e}", flush=True)
    ff = fitfrom if fitfrom is not None else (Ns[len(Ns)//2] if len(Ns) > 3 else Ns[0])
    sel = [r for r in rows if r['N'] >= ff]
    g1, c1 = fit_power([r['N'] for r in sel], [r['gap'] for r in sel])
    g2, c2 = fit_power([r['N'] for r in sel], [r['ratio'] for r in sel])
    print(f"  fit (N>={ff}):  Delta_N ~ {c1:.4g}*N^({g1:+.3f})   ||H||/Delta ~ {c2:.4g}*N^({g2:+.3f})",
          flush=True)
    return rows, g1, g2
