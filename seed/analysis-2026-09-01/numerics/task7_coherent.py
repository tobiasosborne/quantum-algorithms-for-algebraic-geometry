"""Task 7: product / spin-coherent states.

|p^{(x)N}> := (p.z)^N ; in the orthonormal basis its amplitude on |k> is
   c_k = N! p^k / sqrt(k!)  ~  sqrt(N!/k!) p^k   (matches the prompt).
Prediction derived analytically:
   a(f) (p.z)^N = (N!/(N-m)!) * conj(f)(p) * (p.z)^{N-m},  conj(f)(p)=sum conj(f_a) p^a
                = (N!/(N-m)!) * conj( f(conj(p)) ) * (p.z)^{N-m}
   ||(p.z)^N||^2 = N! ||p||^{2N}
==> E(p,N) = <psi|H_N|psi>/<psi|psi> = sum_j (N!/(N-m_j)!) |f_j(conj p)|^2 / ||p||^{2 m_j}
so the state is in ker H_N  iff  conj(p) in V(I).
"""
import numpy as np, math, bf, ideals

def coh(p, N):
    nv = len(p)
    mons = bf.monomials(nv, N)
    c = np.array([math.factorial(N)*np.prod([p[j]**k[j] for j in range(nv)])/math.sqrt(bf.fact_prod(k))
                  for k in mons], dtype=complex)
    return c

def evalp(f, p):
    return sum(c*np.prod([p[j]**a[j] for j in range(len(p))]) for a, c in f.items())

def check(name, gens, pts_on, pts_off, Ns):
    print(f"\n=== {name} ===")
    for tag, pts in (("ON  V(I)", pts_on), ("OFF V(I)", pts_off)):
        for p in pts:
            p = np.array(p, dtype=complex)
            pn = p/np.linalg.norm(p)
            print(f"  {tag}  p = {np.round(p,4)}   f_j(p)={[complex(np.round(evalp(f,p),12)) for f in gens]}"
                  f"  f_j(conj p)={[complex(np.round(evalp(f,np.conj(p)),12)) for f in gens]}")
            for N in Ns:
                H = bf.hamiltonian(gens, N)
                v = coh(pn, N)
                E = float(np.real(v.conj() @ H @ v)/np.real(v.conj() @ v))
                predA = sum(math.factorial(N)/math.factorial(N-bf.poly_deg(f)) *
                            abs(evalp(f, np.conj(pn)))**2 for f in gens if bf.poly_deg(f) <= N)
                predB = sum(math.factorial(N)/math.factorial(N-bf.poly_deg(f)) *
                            abs(evalp(f, pn))**2 for f in gens if bf.poly_deg(f) <= N)
                print(f"      N={N}: E={E:.10g}   pred[f(conj p)]={predA:.10g} (err {abs(E-predA):.2e})"
                      f"   pred[f(p)]={predB:.10g} (err {abs(E-predB):.2e})")

if __name__ == "__main__":
    fc = {(1,1,0): 1, (0,0,2): -1}     # conic z0z1 - z2^2 (real coeffs)
    on = [(1, 1, 1), (4, 1, 2), (1, 0, 0), (1j, 1j, 1j*1j**0)]
    on = [(1,1,1), (4,1,2), (1,0,0), (2+1j, 1, 0)]
    # fix: need z0 z1 = z2^2. pick z0=a,z1=b,z2=sqrt(ab)
    def conic_pt(a, b):
        return (a, b, np.sqrt(complex(a)*complex(b)))
    on = [conic_pt(1,1), conic_pt(4,1), conic_pt(2+1j, 1-3j), conic_pt(1j, 1)]
    off = [(1,1,0), (1,2,3), (1j,1,1)]
    check("conic z0z1 - z2^2 in P^2", [fc], on, off, [2,3,5])

    _, G, _, _ = ideals.twisted_cubic()
    tcp = lambda s, t: (t**3, s*t**2, s*s*t, s**3)
    on = [tcp(1,1), tcp(2,1), tcp(1j,1), tcp(1+1j, 2-1j), (0,0,0,1)]
    off = [(1,1,1,1), (1,0,0,1), (1,2,1,0)]
    check("twisted cubic in P^3", G, on, off, [2,3,4])

    # complex-coefficient ideal: does it really pick out conj(p)?
    rng = np.random.default_rng(5)
    f = {(2,0,0): 1+0j, (0,2,0): 1j, (0,0,2): 2-1j, (1,1,0): 3j}
    # a point with f(p)=0 but f(conj p) != 0 : solve for z2 given z0=1,z1=1
    z2 = np.sqrt(-(1 + 1j + 3j)/(2-1j))
    p = (1, 1, z2)
    print("\n=== complex-coefficient quadric: which of f(p), f(conj p) matters? ===")
    check("random complex quadric in P^2", [f], [p], [(1,1,np.conj(z2))], [2,3,4])
