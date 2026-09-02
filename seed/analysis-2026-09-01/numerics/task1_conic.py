"""Task 1: sanity checks on the conic f = z0 z1 - z2^2 in P^2."""
import numpy as np, sympy as sp, math, sys
import bf

nv = 3
f = {(1, 1, 0): 1, (0, 0, 2): -1}

print("=== Task 1a: notes' hand computations (unnormalized monomial basis) ===")
z0, z1, z2 = sp.symbols('z0 z1 z2')
Z = [z0, z1, z2]
def a_of_f(f, expr):
    out = 0
    for a, c in f.items():
        t = expr
        for j in range(nv):
            t = sp.diff(t, Z[j], a[j])
        out += sp.conjugate(sp.nsimplify(c)) * t
    return sp.expand(out)

e1 = a_of_f(f, z0*z1*z2**2)
print("  a(f)(z0 z1 z2^2) =", e1, "   expected z2^2 - 2 z0 z1 :",
      sp.simplify(e1 - (z2**2 - 2*z0*z1)) == 0)
c = sp.symbols('c')
e2 = a_of_f(f, z0*z1 + c*z2**2)
sol = sp.solve(sp.Eq(e2, 0), c)
print("  a(f)(z0 z1 + c z2^2) =", e2, " -> zero iff c =", sol, " expected [1/2]")

# <f|f> in Fischer inner product = sum |f_a|^2 a!
nrm = sum(abs(cc)**2 * bf.fact_prod(a) for a, cc in f.items())
print("  <f|f> =", nrm, " expected 3 :", nrm == 3)

print()
print("=== Task 1b: dim ker H_N vs HF(N) = 2N+1 ===")
print(f"{'N':>3} {'dim h_N':>8} {'rank(A) num':>12} {'dim I_N (mod p)':>16} "
      f"{'dim ker H_N':>12} {'2N+1':>6} {'ok':>4}")
rowsout = []
for N in range(2, 9):
    A = bf.stacked_A([f], N)
    dh = bf.dim_h(nv, N)
    rnum = bf.rank_numeric(A)
    rp = bf.rank_mod_p(bf.macaulay_rows([f], N))
    ker = dh - rnum
    ok = (ker == 2*N+1) and (rnum == rp)
    print(f"{N:>3} {dh:>8} {rnum:>12} {rp:>16} {ker:>12} {2*N+1:>6} {str(ok):>4}")
    rowsout.append((N, dh, rnum, rp, ker, 2*N+1))

# exact sympy rank cross-check for small N
print("\n  sympy exact ranks (cross-check of mod-p routine):")
for N in range(2, 7):
    M = sp.Matrix(bf.macaulay_rows([f], N))
    print(f"   N={N}: sympy rank={M.rank()}  modp={bf.rank_mod_p(bf.macaulay_rows([f],N))}")

print("\n  eigenvalue check: number of ~zero eigenvalues of H_N")
for N in range(2, 9):
    ev = bf.spectrum([f], N)
    nz = int((ev < 1e-8 * max(1.0, ev[-1])).sum())
    print(f"   N={N}: numeric ker dim={nz}, expected {2*N+1}, "
          f"largest 'zero' ev={ev[2*N]:.3e}, smallest nonzero={ev[2*N+1]:.6f}, ||H||={ev[-1]:.4f}")
