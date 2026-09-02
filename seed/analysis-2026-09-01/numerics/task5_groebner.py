"""Task 5: Groebner degeneration path for the twisted cubic.

Weight w=(0,1,4,9) on (z0,z1,z2,z3).  For each generator f = sum_a f_a z^a set
   f^{(t)} = sum_a f_a t^{M - w.a} z^a ,  M = max_a w.a  (over the support of f),
so f^{(1)} = f and f^{(0)} = in_w(f).   NOTE: the prompt's exponent w.a - max
gives t^{negative} -> divergence as t->0; the sign is flipped here so that the
non-leading terms are the ones that die.  (Same family after t -> 1/t.)
in_w(I) = (z0z2, z0z3, z1z3), a monomial ideal with HF = 3N+1 (checked below).
"""
import numpy as np, math, bf, ideals
from gaps import gap_row

W = (0, 1, 4, 9)
nv = 4

def deform(f, t):
    M = max(sum(w*a for w, a in zip(W, al)) for al in f)
    return {al: c * (t ** (M - sum(w*a for w, a in zip(W, al)))) for al, c in f.items()}

def initial(f):
    M = max(sum(w*a for w, a in zip(W, al)) for al in f)
    return {al: c for al, c in f.items() if sum(w*a for w, a in zip(W, al)) == M}

if __name__ == "__main__":
    _, G, _, hf = ideals.twisted_cubic()
    print("generators:", G)
    IN = [initial(f) for f in G]
    print("in_w(f_j) :", IN)
    print("\nHF of in_w(I) = (z0z2, z0z3, z1z3):")
    for N in range(1, 9):
        r = bf.rank_mod_p([[int(round(x.real)) if isinstance(x, complex) else int(x) for x in row]
                           for row in bf.macaulay_rows(IN, N)])
        print(f"   N={N}: dim h={bf.dim_h(nv,N):4d}  dim I_N={r:4d}  HF={bf.dim_h(nv,N)-r:4d}  3N+1={3*N+1}")

    ts = np.concatenate([np.logspace(0, -6, 25), [1e-8, 1e-10]])
    print("\nPath t in (0,1]:  dim ker H_N(t) (numeric, rel tol 1e-9) and Delta_N(t)")
    for N in range(3, 8):
        pred = 3*N+1
        gs, rs, kds = [], [], []
        for t in ts:
            gens = [deform(f, t) for f in G]
            r = gap_row(gens, N, kd=pred)
            gs.append(r['gap']); rs.append(r['ratio']); kds.append(r['kernum'])
        gs = np.array(gs); rs = np.array(rs)
        # also the t=0 endpoint (pure initial monomial ideal)
        r0 = gap_row(IN, N, kd=pred)
        ok = all(k == pred for k in kds)
        i = int(np.argmin(gs)); j = int(np.argmax(rs))
        print(f"  N={N}: ker const = {pred}? {ok}   (kerdims seen: {sorted(set(kds))})")
        print(f"        Delta(t=1)={gs[0]:.6g}  Delta(t=0,monomial)={r0['gap']:.6g}"
              f"  min_t Delta={gs[i]:.6g} at t={ts[i]:.3g}")
        print(f"        max_t ||H||/Delta = {rs[j]:.6g} at t={ts[j]:.3g}  "
              f"(t=1: {rs[0]:.4g}, t=0: {r0['ratio']:.4g})")
    print("\nfull path detail for N=5,7:")
    for N in (5, 7):
        print(f"  N={N}: " + "  ".join(f"t={t:.2e}:D={gap_row([deform(f,t) for f in G],N,kd=3*N+1)['gap']:.4g}"
                                       for t in np.logspace(0, -4, 9)))
    # scaling of min-gap along path with N
    print("\nmin_t Delta_N(t) and min_t Delta/||H|| vs N:")
    print(f"{'N':>3} {'Delta(1)':>11} {'min_t Delta':>12} {'argmin t':>10} {'min_t Delta/||H||':>18}")
    Ns, mg, mr = [], [], []
    for N in range(2, 10):
        gens_t = [[deform(f, t) for f in G] for t in ts]
        rows = [gap_row(gg, N, kd=3*N+1) for gg in gens_t]
        gs = np.array([r['gap'] for r in rows]); nr = np.array([r['gap']/r['norm'] for r in rows])
        i = int(np.argmin(gs))
        Ns.append(N); mg.append(gs[i]); mr.append(nr.min())
        print(f"{N:>3} {gs[0]:>11.5g} {gs[i]:>12.5g} {ts[i]:>10.3g} {nr.min():>18.6g}")
    A = np.vstack([np.log(Ns), np.ones(len(Ns))]).T
    for lab, y in (("min_t Delta", mg), ("min_t Delta/||H||", mr)):
        c = np.linalg.lstsq(A, np.log(y), rcond=None)[0]
        print(f"  fit {lab} ~ {math.exp(c[1]):.4g} * N^({c[0]:+.3f})")
