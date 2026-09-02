"""Task 3, part 2: scaling of Delta with the number of variables n at fixed N.
(Split out of task3_gaps.py, with a dimension cap so it finishes.)"""
import numpy as np, bf, ideals
from gaps import gap_row
CAP = 3500

print("boolean ideal in P^n at N = n+1 (kernel = 2^n):")
print(f"{'n':>3} {'N':>3} {'dim':>7} {'ker':>8} {'Delta':>12} {'||H||':>12} {'||H||/Delta':>12}")
bn, bg = [], []
for n in range(2, 8):
    N = n + 1
    nv, g, name, hf = ideals.boolean(n)
    if bf.dim_h(nv, N) > CAP:
        break
    r = gap_row(g, N, hf(N))
    bn.append(n); bg.append(r['gap'])
    print(f"{n:>3} {N:>3} {r['dim']:>7} {r['ker']:>8} {r['gap']:>12.6g} "
          f"{r['norm']:>12.6g} {r['ratio']:>12.4g}", flush=True)
if len(bn) > 2:
    print(f"  exp fit: log Delta = {np.polyfit(bn, np.log(bg),1)[0]:+.4f}*n + c ;"
          f"  power fit: Delta ~ n^({np.polyfit(np.log(bn), np.log(bg),1)[0]:+.3f})")

for k in (1, 2):
    for N in (3, 4):
        print(f"\n{k} random quadric(s) in P^n, N={N}:")
        print(f"  {'n':>3} {'dim':>7} {'ker':>6} {'Delta':>12} {'||H||':>12} {'||H||/Delta':>12}")
        ns, gs = [], []
        for n in range(2, 15):
            nv, g, name, hf = ideals.k_random_quadrics(n, k, seed=100 + n)
            if bf.dim_h(nv, N) > CAP:
                break
            r = gap_row(g, N, hf(N))
            ns.append(n); gs.append(r['gap'])
            print(f"  {n:>3} {r['dim']:>7} {r['ker']:>6} {r['gap']:>12.6g} "
                  f"{r['norm']:>12.6g} {r['ratio']:>12.4g}", flush=True)
        if len(ns) > 2:
            print(f"    exp fit: log Delta = {np.polyfit(ns, np.log(gs),1)[0]:+.4f}*n + c ;"
                  f"  power fit: Delta ~ n^({np.polyfit(np.log(ns), np.log(gs),1)[0]:+.3f})")
