"""Task 3: spectral gaps Delta_N, ||H_N||, ratio; power-law fits; n-scaling."""
import numpy as np, math, bf, ideals
from gaps import table, gap_row, fit_power

print("############ Task 3: gap vs N ############")
out = {}

nv,g,name,hf = ideals.twisted_cubic()
out['tc'] = table("(a) twisted cubic P^3", g, list(range(2, 23)), hf)

nv,g,name,hf = ideals.monomial_ideal()
out['mono'] = table("(b) monomial (z0^2,z0z1,z1^3) P^2", g, list(range(2, 41)), hf)

nv,g,name,hf = ideals.rnc4()
out['rnc'] = table("(c) rational normal curve deg 4, P^4", g, list(range(2, 14)), hf)

nv,g,name,hf = ideals.two_generic_quadrics()
out['2q'] = table("(d) 2 generic quadrics P^3", g, list(range(2, 23)), hf)

for n, Nmax in ((2, 14), (3, 14), (4, 12), (5, 10)):
    nv,g,name,hf = ideals.boolean(n)
    out[f'bool{n}'] = table(f"(e) boolean P^{n}", g, list(range(2, Nmax+1)), hf)

for n, Nmax in ((2, 30), (3, 20), (4, 14)):
    nv,g,name,hf = ideals.one_random_quadric(n)
    out[f'rq{n}'] = table(f"(f) single random quadric P^{n}", g, list(range(2, Nmax+1)), hf)

print("\n############ Task 3b: scaling with n at fixed N ############")
print("\nboolean ideal in P^n at N = n+1  (and N=n):")
print(f"{'n':>3} {'N':>3} {'dim':>7} {'ker=2^n':>8} {'Delta':>12} {'||H||':>12} {'||H||/Delta':>12}")
bn, bg = [], []
for n in range(2, 8):
    N = n+1
    nv,g,name,hf = ideals.boolean(n)
    if bf.dim_h(nv, N) > 9000: break
    r = gap_row(g, N, hf(N))
    bn.append(n); bg.append(r['gap'])
    print(f"{n:>3} {N:>3} {r['dim']:>7} {r['ker']:>8} {r['gap']:>12.6g} {r['norm']:>12.6g} {r['ratio']:>12.4g}")
if len(bn) > 2:
    sl = np.polyfit(bn, np.log(bg), 1)[0]
    slp = np.polyfit(np.log(bn), np.log(bg), 1)[0]
    print(f"  fit: log Delta = {sl:+.4f}*n + c  (exp rate)   |   Delta ~ n^({slp:+.3f}) (power)")

print("\nrandom quadric families in P^n at fixed N (k quadrics, k=1 and k=2):")
for k in (1, 2):
    for N in (3, 4):
        print(f"\n  k={k} random quadrics, N={N}:")
        print(f"  {'n':>3} {'dim':>7} {'ker':>6} {'Delta':>12} {'||H||':>12} {'||H||/Delta':>12}")
        ns, gs = [], []
        for n in range(2, 15):
            nv,g,name,hf = ideals.k_random_quadrics(n, k, seed=100+n)
            if bf.dim_h(nv, N) > 6000: break
            r = gap_row(g, N, hf(N))
            ns.append(n); gs.append(r['gap'])
            print(f"  {n:>3} {r['dim']:>7} {r['ker']:>6} {r['gap']:>12.6g} {r['norm']:>12.6g} {r['ratio']:>12.4g}")
        if len(ns) > 2:
            sl = np.polyfit(ns, np.log(gs), 1)[0]
            slp = np.polyfit(np.log(ns), np.log(gs), 1)[0]
            print(f"    fit: log Delta = {sl:+.4f}*n + c   |   Delta ~ n^({slp:+.3f})")
