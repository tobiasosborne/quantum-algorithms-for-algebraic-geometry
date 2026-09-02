"""Task 6: multigraded / quantum 2-SAT embedding. z_{i,s}, i=0,1,2 blocks, s in {0,1}."""
import numpy as np, itertools, bf

NB = 3
nv = 2*NB
def v(i, s): return 2*i + s

def bilinear(i, j, F):
    """f = sum_{s,t} F[s,t] z_{i,s} z_{j,t}"""
    f = {}
    for s in (0, 1):
        for t in (0, 1):
            e = bf.emono(nv, [v(i, s), v(j, t)])
            f[e] = f.get(e, 0) + F[s, t]
    return {a: c for a, c in f.items() if abs(c) > 0}

SINGLET = np.array([[0, 1], [-1, 0]], dtype=complex)   # z_{i,0}z_{j,1} - z_{i,1}z_{j,0}

def sector_indices():
    """the 8 squarefree monomials z_{0,s0} z_{1,s1} z_{2,s2} of multidegree (1,1,1)"""
    idx = bf.mono_index(nv, NB)
    out, lbl = [], []
    for bits in itertools.product((0, 1), repeat=NB):
        e = bf.emono(nv, [v(i, bits[i]) for i in range(NB)])
        out.append(idx[e]); lbl.append(bits)
    return out, lbl

def two_sat_H(pairs):
    """reference 3-qubit Hamiltonian sum_j |f_j><f_j| (x) 1"""
    H = np.zeros((8, 8), dtype=complex)
    for (i, j, F) in pairs:
        psi = np.zeros(8, dtype=complex)
        # build |f> on qubits i,j tensor identity on the third
        for s in (0, 1):
            for t in (0, 1):
                for u in (0, 1):
                    bits = [0]*3
                    bits[i] = s; bits[j] = t
                    k = [x for x in range(3) if x not in (i, j)][0]
                    bits[k] = u
                    a = bits[0]*4 + bits[1]*2 + bits[2]
                    # accumulate later; handled below
        # cleaner: loop over spectator value
        k = [x for x in range(3) if x not in (i, j)][0]
        for u in (0, 1):
            psi = np.zeros(8, dtype=complex)
            for s in (0, 1):
                for t in (0, 1):
                    bits = [0]*3
                    bits[i] = s; bits[j] = t; bits[k] = u
                    psi[bits[0]*4 + bits[1]*2 + bits[2]] += F[s, t]
            H += np.outer(psi, psi.conj())
    return H

def sector_H(pairs, verbose=True, tag=""):
    gens = [bilinear(i, j, F) for (i, j, F) in pairs]
    Hfull = bf.hamiltonian(gens, NB)
    sel, lbl = sector_indices()
    Hs = Hfull[np.ix_(sel, sel)]
    # reorder to computational-basis order (bits[0]*4+bits[1]*2+bits[2])
    perm = np.argsort([b[0]*4 + b[1]*2 + b[2] for b in lbl])
    Hs = Hs[np.ix_(perm, perm)]
    Href = two_sat_H(pairs)
    err = np.abs(Hs - Href).max()
    ev = np.linalg.eigvalsh((Hs+Hs.conj().T)/2)
    kd = int((ev < 1e-9*max(ev[-1], 1)).sum())
    # multigraded Hilbert function at (1,1,1) via Macaulay rank in that sector
    rows = bf.macaulay_rows(gens, NB)
    R = np.array(rows, dtype=complex)[:, sel][:, perm]
    R = R[np.abs(R).max(axis=1) > 1e-12]
    rk = np.linalg.matrix_rank(R, tol=1e-10) if len(R) else 0
    if verbose:
        print(f"  {tag}")
        print(f"    ||H_sector - sum_j |f_j><f_j| (x) 1||_max = {err:.3e}")
        print(f"    dim ker H_sector = {kd}   multigraded HF(1,1,1) = 8 - rank(Macaulay|sector) = {8-rk}"
              f"   match={kd == 8-rk}")
        print(f"    eigenvalues: {np.round(ev,10)}")
    return kd, err, 8-rk

if __name__ == "__main__":
    print("=== Task 6: quantum 2-SAT embedding ===")
    print("\n[A] singlets on (1,2),(2,3),(1,3)  [blocks 0-1, 1-2, 0-2]")
    sector_H([(0,1,SINGLET),(1,2,SINGLET),(0,2,SINGLET)], tag="three singlets")
    print("\n[B] singlet on (1,2) only")
    sector_H([(0,1,SINGLET)], tag="one singlet")
    print("\n[C] random bilinear forms on all three pairs (5 seeds)")
    for seed in range(5):
        rng = np.random.default_rng(seed)
        F = [rng.normal(size=(2,2)) + 1j*rng.normal(size=(2,2)) for _ in range(3)]
        kd, err, hfv = sector_H([(0,1,F[0]),(1,2,F[1]),(0,2,F[2])], verbose=False)
        print(f"    seed {seed}: dim ker = {kd}, HF = {hfv}, ||H-H_ref||={err:.2e}")
    print("\n[D] random bilinear form on (1,2) only (5 seeds)")
    for seed in range(5):
        rng = np.random.default_rng(seed)
        F = rng.normal(size=(2,2)) + 1j*rng.normal(size=(2,2))
        kd, err, hfv = sector_H([(0,1,F)], verbose=False)
        print(f"    seed {seed}: dim ker = {kd}, HF = {hfv}, ||H-H_ref||={err:.2e}")
    print("\n[E] random forms on two pairs (1,2),(2,3) (5 seeds)")
    for seed in range(5):
        rng = np.random.default_rng(seed)
        F = [rng.normal(size=(2,2)) + 1j*rng.normal(size=(2,2)) for _ in range(2)]
        kd, err, hfv = sector_H([(0,1,F[0]),(1,2,F[1])], verbose=False)
        print(f"    seed {seed}: dim ker = {kd}, HF = {hfv}, ||H-H_ref||={err:.2e}")
