"""Closed forms spotted in the data: conic Delta_N = N+1 ; monomial ideal ||H_N||
= N(N-1)(N-2) and Delta_N = 1 (integer spectrum)."""
import numpy as np, bf, ideals
f = {(1,1,0):1, (0,0,2):-1}
print("conic z0z1-z2^2 in P^2:")
print(f"{'N':>3} {'Delta_N':>10} {'N+1':>5} {'||H_N||':>12} {'(N^2+N)/2?':>12}")
for N in range(2, 31):
    ev = bf.spectrum([f], N)
    kd = 2*N+1
    print(f"{N:>3} {ev[kd]:>10.6f} {N+1:>5} {ev[-1]:>12.6f} {(N*N+N)/2:>12.4f}")
print("\nmonomial ideal (z0^2,z0z1,z1^3): integrality of the spectrum")
nv,g,name,hf = ideals.monomial_ideal()
for N in (5, 8, 12, 16):
    ev = bf.spectrum(g, N)
    dev = np.abs(ev - np.round(ev)).max()
    print(f"  N={N}: max|lambda - round(lambda)| = {dev:.2e}, "
          f"distinct rounded eigenvalues (first 8) = {sorted(set(np.round(ev,6)))[:8]}")
