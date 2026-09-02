"""The test ideals."""
import math, numpy as np, bf

def twisted_cubic():
    nv = 4
    return nv, bf.minors2x2(nv, [0, 1, 2], [1, 2, 3]), "twisted cubic P^3", lambda N: 3*N+1

def monomial_ideal():
    nv = 3
    g = [{(2,0,0):1}, {(1,1,0):1}, {(0,3,0):1}]
    def hf(N):
        # standard monomials: a<=1, not(a>=1 and b>=1), b<=2
        c = 0
        for a in range(0, N+1):
            for b in range(0, N+1-a):
                cc = N-a-b
                if a <= 1 and not (a >= 1 and b >= 1) and b <= 2:
                    c += 1
        return c
    return nv, g, "monomial (z0^2,z0z1,z1^3) P^2", hf

def rnc4():
    nv = 5
    return nv, bf.minors2x2(nv, [0,1,2,3], [1,2,3,4]), "rat normal curve deg4 P^4", lambda N: 4*N+1

def two_generic_quadrics(seed=7):
    nv = 4
    rng = np.random.default_rng(seed)
    g = [bf.random_form(nv, 2, rng), bf.random_form(nv, 2, rng)]
    def hf(N):
        # complete intersection of two quadrics in P^3: (1+t)^2/(1-t)^2
        s = 0
        for j, c in [(0,1),(1,2),(2,1)]:
            if N-j >= 0:
                s += c*(N-j+1)
        return s
    return nv, g, "2 generic quadrics P^3", hf

def boolean(n):
    nv = n+1
    g = []
    for i in range(1, n+1):
        e1 = bf.emono(nv, [i, i]); e2 = bf.emono(nv, [i, 0])
        g.append({e1: 1, e2: -1})
    hf = lambda N: sum(math.comb(n, i) for i in range(0, min(N, n)+1))
    return nv, g, f"boolean P^{n}", hf

def one_random_quadric(n, seed=3):
    nv = n+1
    rng = np.random.default_rng(seed)
    g = [bf.random_form(nv, 2, rng)]
    hf = lambda N: bf.dim_h(nv, N) - bf.dim_h(nv, N-2)
    return nv, g, f"1 random quadric P^{n}", hf

def k_random_quadrics(n, k, seed=11):
    nv = n+1
    rng = np.random.default_rng(seed)
    g = [bf.random_form(nv, 2, rng) for _ in range(k)]
    def hf(N):  # CI Hilbert series (1-t^2)^k/(1-t)^{n+1}, valid while k<=n
        s = 0
        for j in range(0, k+1):
            if N-2*j >= 0:
                s += (-1)**j * math.comb(k, j) * bf.dim_h(nv, N-2*j)
        return max(s, 0)
    return nv, g, f"{k} random quadrics P^{n}", hf
