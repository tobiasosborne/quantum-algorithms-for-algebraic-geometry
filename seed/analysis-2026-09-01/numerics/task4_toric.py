"""Task 4: toric case -- kernel = fiber sums; block structure; per-fiber gaps."""
import numpy as np, math, bf, ideals

def fiber_label(k, weights):
    return sum(w*kk for w, kk in zip(weights, k))

def run(nv, gens, name, d, Ns):
    """Rational normal curve of degree d in P^d: z_i <-> s^i t^{d-i}; A-degree of
    z^k is (sum i k_i, dN - sum i k_i), so the fiber label is u = sum_i i*k_i."""
    print(f"\n=== {name} ===")
    weights = list(range(nv))
    for N in Ns:
        mons = bf.monomials(nv, N)
        idx = bf.mono_index(nv, N)
        H = bf.hamiltonian(gens, N); H = (H+H.conj().T)/2
        labels = np.array([fiber_label(k, weights) for k in mons])
        us = sorted(set(labels.tolist()))
        # 1. block structure w.r.t. fiber label
        offblock = 0.0
        for a in range(len(mons)):
            for b in range(len(mons)):
                if labels[a] != labels[b]:
                    offblock = max(offblock, abs(H[a, b]))
        # 2. fiber sums
        Q = np.zeros((len(us), len(mons)))
        for j, u in enumerate(us):
            for a, k in enumerate(mons):
                if labels[a] == u:
                    Q[j, a] = 1.0/math.sqrt(bf.fact_prod(k))
            Q[j] /= np.linalg.norm(Q[j])
        resid = np.abs(Q @ H).max()
        ev = np.linalg.eigvalsh(H)
        kd = int((ev < 1e-9*ev[-1]).sum())
        # do the q_u span the whole kernel?
        rankQ = np.linalg.matrix_rank(Q, tol=1e-10)
        gap = ev[kd]
        # per-fiber second eigenvalue
        fg = []
        for u in us:
            sel = np.where(labels == u)[0]
            Hb = H[np.ix_(sel, sel)]
            e = np.linalg.eigvalsh(Hb)
            k0 = int((e < 1e-9*max(ev[-1], 1)).sum())
            fg.append((u, len(sel), k0, e[k0] if k0 < len(e) else np.inf))
        minfib = min(x[3] for x in fg)
        nzk = sum(x[2] for x in fg)
        print(f" N={N:2d} dim={len(mons):5d} #fibers={len(us):4d} kerdim={kd:4d} "
              f"rank(q_u)={rankQ:4d} |H q_u|max={resid:.2e} offblock={offblock:.1e} "
              f"per-fiber-ker-total={nzk:4d} Delta={gap:.6g} min_u lam2(H_u)={minfib:.6g} "
              f"N^2*Delta={N*N*gap:.4g}  Delta/N={gap/N:.4g}")

if __name__ == "__main__":
    nv, g, name, hf = ideals.rnc4()
    run(nv, g, name, 4, range(2, 11))
    nv, g, name, hf = ideals.twisted_cubic()
    run(nv, g, name, 3, range(2, 13))
