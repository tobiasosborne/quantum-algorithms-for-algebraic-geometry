"""Task 3 addendum: how small can Delta get?  Use the (verified-exact) 2-SAT
embedding of task 6: with m blocks z_{i,0},z_{i,1} and bilinear generators on
pairs (i,j), the multidegree-(1,..,1) sector of H_m is exactly sum_j |f_j><f_j| (x) 1
on m qubits.  Delta_N (N=m) over the FULL degree-m space is <= the gap in that
sector, so this gives an upper bound on Delta_N as a function of n = 2m-1.
"""
import numpy as np, itertools, bf

SINGLET = np.array([0, 1, -1, 0], dtype=complex)

def two_local(psi, i, j, m):
    """|psi><psi| on qubits i<j tensor identity elsewhere, as a 2^m matrix."""
    P = np.outer(psi, psi.conj())
    dim = 2**m
    H = np.zeros((dim, dim), dtype=complex)
    others = [k for k in range(m) if k not in (i, j)]
    for bits in itertools.product((0, 1), repeat=len(others)):
        idxs = []
        for s in (0, 1):
            for t in (0, 1):
                b = [0]*m
                b[i] = s; b[j] = t
                for k, val in zip(others, bits):
                    b[k] = val
                idxs.append(int("".join(map(str, b)), 2))
        H[np.ix_(idxs, idxs)] += P
    return H

def verify_against_bf(m, pairs, psis):
    """cross-check the direct qubit construction against the polynomial-ring H."""
    nv = 2*m
    def v(i, s): return 2*i+s
    gens = []
    for (i, j), psi in zip(pairs, psis):
        f = {}
        F = psi.reshape(2, 2)
        for s in (0, 1):
            for t in (0, 1):
                e = bf.emono(nv, [v(i, s), v(j, t)])
                f[e] = f.get(e, 0) + F[s, t]
        gens.append({a: c for a, c in f.items() if abs(c) > 1e-14})
    Hfull = bf.hamiltonian(gens, m)
    idx = bf.mono_index(nv, m)
    sel = [idx[bf.emono(nv, [v(i, b[i]) for i in range(m)])]
           for b in itertools.product((0, 1), repeat=m)]
    Hs = Hfull[np.ix_(sel, sel)]
    Hd = sum(two_local(p, i, j, m) for (i, j), p in zip(pairs, psis))
    return np.abs(Hs - Hd).max()

def gapof(H, rtol=1e-10):
    ev = np.linalg.eigvalsh((H+H.conj().T)/2)
    nrm = ev[-1]
    k = int((ev < rtol*nrm).sum())
    return k, (ev[k] if k < len(ev) else float('nan')), nrm

if __name__ == "__main__":
    print("=== cross-check direct qubit build vs polynomial-ring H (multidegree sector) ===")
    for m in (3, 4, 5):
        rng = np.random.default_rng(m)
        pairs = [(i, i+1) for i in range(m-1)]
        psis = [rng.normal(size=4)+1j*rng.normal(size=4) for _ in pairs]
        print(f"  m={m}: max|H_sector - H_direct| = {verify_against_bf(m, pairs, psis):.2e}")

    print("\n=== (A) singlet chain: nearest-neighbour singlet projectors on m qubits ===")
    print(f"{'m':>3} {'n=2m-1':>7} {'dim':>7} {'kerdim':>7} {'Delta':>12} {'||H||':>9} "
          f"{'m^2*Delta':>10} {'1/Delta':>10}")
    ms, gs = [], []
    for m in range(2, 13):
        H = sum(two_local(SINGLET, i, i+1, m) for i in range(m-1))
        k, g, nrm = gapof(H)
        ms.append(m); gs.append(g)
        print(f"{m:>3} {2*m-1:>7} {2**m:>7} {k:>7} {g:>12.6g} {nrm:>9.4g} {m*m*g:>10.5g} {1/g:>10.4g}")
    A = np.vstack([np.log(ms[3:]), np.ones(len(ms)-3)]).T
    c = np.linalg.lstsq(A, np.log(gs[3:]), rcond=None)[0]
    ce = np.polyfit(ms[3:], np.log(gs[3:]), 1)[0]
    print(f"  fit Delta ~ {np.exp(c[1]):.4g} * m^({c[0]:+.3f})   [exp fit: log Delta = {ce:+.4f} m + c]")
    print(f"  kernel dims are the symmetric subspace dim m+1 (spin m/2): check "
          f"{[gapof(sum(two_local(SINGLET,i,i+1,mm) for i in range(mm-1)))[0] for mm in range(2,9)]}"
          f" vs {[mm+1 for mm in range(2,9)]}")

    print("\n=== (B) random frustration-free chain (product state in the kernel) ===")
    print(f"{'m':>3} {'kerdim':>7} {'Delta':>12} {'||H||':>9} {'1/Delta':>10}")
    ms, gs = [], []
    for m in range(2, 13):
        rng = np.random.default_rng(1000+m)
        phis = [rng.normal(size=2)+1j*rng.normal(size=2) for _ in range(m)]
        phis = [p/np.linalg.norm(p) for p in phis]
        H = np.zeros((2**m, 2**m), dtype=complex)
        for i in range(m-1):
            prod = np.kron(phis[i], phis[i+1])
            # random psi orthogonal to the product state -> frustration free
            w = rng.normal(size=4)+1j*rng.normal(size=4)
            psi = w - prod*(np.vdot(prod, w)/np.vdot(prod, prod))
            H += two_local(psi/np.linalg.norm(psi), i, i+1, m)
        k, g, nrm = gapof(H)
        ms.append(m); gs.append(g)
        print(f"{m:>3} {k:>7} {g:>12.6g} {nrm:>9.4g} {1/g:>10.4g}")
    c = np.linalg.lstsq(np.vstack([np.log(ms[3:]), np.ones(len(ms)-3)]).T,
                        np.log(gs[3:]), rcond=None)[0]
    ce = np.polyfit(ms[3:], np.log(gs[3:]), 1)[0]
    print(f"  fit Delta ~ {np.exp(c[1]):.4g} * m^({c[0]:+.3f})   [exp fit: log Delta = {ce:+.4f} m + c]")

    print("\n=== (C) tunable near-degenerate 2-block generator (coefficient dynamic range) ===")
    print("  f = z_{1,0}z_{2,1} - z_{1,1}z_{2,0} + eps*(z_{1,0}z_{2,0}) on a chain")
    print(f"{'eps':>10} {'m':>3} {'kerdim':>7} {'Delta':>12}")
    for eps in (1.0, 1e-1, 1e-2, 1e-3):
        for m in (6, 8, 10):
            psi = np.array([eps, 1, -1, 0], dtype=complex); psi /= np.linalg.norm(psi)
            H = sum(two_local(psi, i, i+1, m) for i in range(m-1))
            k, g, nrm = gapof(H)
            print(f"{eps:>10.0e} {m:>3} {k:>7} {g:>12.6g}")
