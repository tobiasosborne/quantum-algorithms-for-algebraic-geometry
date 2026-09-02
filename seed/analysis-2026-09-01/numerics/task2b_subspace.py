"""Direct subspace check of the claim ker H_N = (I_N)^perp (not just dimensions).

I_N is spanned by the vectors z^beta f_j; in the ORTHONORMAL basis |k>=z^k/sqrt(k!)
the vector z^gamma has coordinates sqrt(gamma!) e_gamma.  We build the coordinate
matrix of a spanning set of I_N and check (i) it is orthogonal to ker H_N and
(ii) rank(I_N) + dim ker = dim h_N.
"""
import numpy as np, math, bf, ideals

def I_N_coords(gens, N):
    nv = bf.poly_nvars(gens[0])
    idx = bf.mono_index(nv, N)
    rows = []
    for f in gens:
        m = bf.poly_deg(f)
        if m > N: continue
        for b in bf.monomials(nv, N-m):
            v = np.zeros(len(idx), dtype=complex)
            for a, c in f.items():
                e = tuple(a[j]+b[j] for j in range(nv))
                v[idx[e]] += c*math.sqrt(bf.fact_prod(e))   # z^e = sqrt(e!)|e>
            rows.append(v)
    return np.array(rows)

for maker, Ns in ((ideals.twisted_cubic, range(2, 8)),
                  (ideals.rnc4, range(2, 7)),
                  (ideals.two_generic_quadrics, range(2, 8)),
                  (ideals.monomial_ideal, range(2, 8)),
                  (lambda: ideals.boolean(4), range(2, 7))):
    nv, g, name, hf = maker()
    print(f"\n{name}")
    for N in Ns:
        H = bf.hamiltonian(g, N); H = (H+H.conj().T)/2
        ev, U = np.linalg.eigh(H)
        kd = int((ev < 1e-9*ev[-1]).sum())
        K = U[:, :kd]                       # orthonormal basis of ker H_N
        M = I_N_coords(g, N)
        overlap = np.abs(M.conj() @ K).max()   # Hermitian <.,.> / max(np.abs(M).max(), 1e-300)
        r = np.linalg.matrix_rank(M, tol=1e-9*np.abs(M).max())
        print(f"  N={N:2d}: dim h={bf.dim_h(nv,N):4d} dim ker={kd:4d} rank I_N={r:4d} "
              f"sum={kd+r:4d}  max|<I_N , ker>|/scale = {overlap:.2e}  "
              f"{'OK' if kd+r == bf.dim_h(nv,N) and overlap < 1e-10 else 'MISMATCH'}")
