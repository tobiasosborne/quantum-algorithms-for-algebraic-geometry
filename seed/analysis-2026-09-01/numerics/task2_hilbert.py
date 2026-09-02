"""Task 2: Hilbert functions dim ker H_N vs independent Macaulay-rank computation."""
import numpy as np, sympy as sp, bf, ideals

def report(nv, gens, name, hf, Ns, integer_coeffs=True, exact_small=True):
    print(f"\n--- {name} ---")
    hdr = f"{'N':>3} {'dim h_N':>8} {'dim I_N (A,num)':>16} {'dim I_N (Mac)':>14} {'dim ker H_N':>12} {'HF pred':>8} {'match':>6}"
    print(hdr)
    allok = True
    for N in Ns:
        dh = bf.dim_h(nv, N)
        A = bf.stacked_A(gens, N)
        rA = bf.rank_numeric(A)
        rows = bf.macaulay_rows(gens, N)
        if integer_coeffs:
            rM = bf.rank_mod_p([[int(round(x.real)) if isinstance(x, complex) else int(x) for x in r] for r in rows])
        else:
            rM = bf.rank_numeric(rows)
        ker = dh - rA
        pred = hf(N)
        ok = (ker == pred) and (rA == rM)
        allok &= ok
        print(f"{N:>3} {dh:>8} {rA:>16} {rM:>14} {ker:>12} {pred:>8} {str(ok):>6}")
    if exact_small and integer_coeffs:
        Nsm = [N for N in Ns][:4]
        ex = []
        for N in Nsm:
            M = sp.Matrix([[sp.Integer(int(round(x.real)) if isinstance(x, complex) else int(x)) for x in r]
                           for r in bf.macaulay_rows(gens, N)])
            ex.append((N, M.rank()))
        print("  sympy exact Macaulay ranks:", ex)
    print("  ALL MATCH:", allok)
    return allok

if __name__ == "__main__":
    res = {}
    nv, g, name, hf = ideals.twisted_cubic();      res[name] = report(nv, g, name, hf, range(1, 10))
    nv, g, name, hf = ideals.monomial_ideal();     res[name] = report(nv, g, name, hf, range(1, 11))
    nv, g, name, hf = ideals.rnc4();               res[name] = report(nv, g, name, hf, range(1, 9))
    nv, g, name, hf = ideals.two_generic_quadrics();res[name] = report(nv, g, name, hf, range(1, 9),
                                                                      integer_coeffs=False, exact_small=False)
    for n in (2, 3, 4, 5):
        nv, g, name, hf = ideals.boolean(n)
        res[name] = report(nv, g, name, hf, range(1, n+5))
    print("\n=== summary ===")
    for k, v in res.items():
        print(f"  {k:35s} {'CONFIRMED' if v else 'FAILED'}")
