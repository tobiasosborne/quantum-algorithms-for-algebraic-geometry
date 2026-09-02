"""Checker: the pyramid / unused-variable counterexample (cones pin the gap).

CONVENTIONS: definitions/definitions.md is the single source (rk-light L2).
DEPARTURE FROM convention C5: like the seed's own numerics, generators are
used AS WRITTEN (unit coefficients), not normalised to unit Bombieri-Weyl
norm, so every Delta_N below is the gap of that presentation.  See README.

SEED CLAIMS UNDER TEST
  seed/analysis-2026-09-01/report.md
  - Sect. 7, toric bullet:
      "for the toric ideal (x00 x11 - x01 x10) of the pyramid over a square,
       with apex variable y absent from the relation, h = y^(N-2) attains
       Fact 7.1 and Delta_N = 2 for all N (NUMERICALLY exact for N <= 8; the
       same binomial without y has Delta_N = N exactly, and adjoining an
       unused variable to the twisted cubic flattens its gap from 0.85N to
       exactly 2 for N <= 12).  Any lower bound growing with N must therefore
       exclude ideals extended from a subring."
  - Conjecture 8.3(b) (cones versus growth), whose numerical support this is;
    also referee round 1 item 51, which used the pyramid to REFUTE the earlier
    version of 8.3(b).

WHAT IS CHECKED (exit 0 only if all hold)
  (1) pyramid (5 variables, y unused): Delta_N = 2 exactly for N = 2..8;
  (2) same binomial in 4 variables: Delta_N = N exactly for N = 2..12;
  (3) twisted cubic + one dummy variable: Delta_N = 2 exactly for N = 2..12,
      while the plain twisted cubic has Delta_N/N >= 0.85 for N >= 7 (so the
      dummy variable really does flatten a growing gap);
  (4) at every N, the numerical kernel dimension equals the predicted Hilbert
      function, and (where dim R_N <= EXACT_RANK_CAP) also equals
      dim R_N - rank_GF(p)(Macaulay);
  (5) the pyramid minimiser is where the seed says it is: the subspace
      y^(N-2) * (quadratic monomials in x) contains a vector of energy exactly
      2 and that equals the global Delta_N.

BUDGET: pyramid N <= 8 (dim R_8 = 495), 4-variable N <= 12 (455), TC+dummy
N <= 12 (dim R_12 = 1820).
"""
import math

import numpy as np

import bf
import checkharness

EXACT_RANK_CAP = 1400
TC_SLOPE_MIN = 0.85


def hf_quadric(nv, N):
    return bf.dim_h(nv, N) - bf.dim_h(nv, N - 2)


def hf_tc_dummy(N):
    return sum(3 * (N - j) + 1 for j in range(0, N + 1))


def analyse(ck, name, nv, gens, Ns, hf):
    ck.info(f"\n  === {name} ===")
    ck.info(f"  {'N':>3} {'dim':>6} {'HF':>6} {'HF_GFp':>7} {'kerNum':>7} "
            f"{'Delta_N':>12} {'||H_N||':>12} {'zero-sep':>10}")
    out = {}
    for N in Ns:
        D = bf.dim_h(nv, N)
        H = bf.hamiltonian(gens, N, dtype=float).real
        H = (H + H.T) / 2
        ev = np.linalg.eigvalsh(H)
        norm = float(ev[-1])
        kd = hf(N)
        kernum = int((ev < 1e-9 * max(norm, 1e-300)).sum())
        hf_exact = None
        if D <= EXACT_RANK_CAP:
            rows = bf.macaulay_rows(gens, N)
            hf_exact = D - bf.rank_mod_p([[int(round(x.real)) for x in r]
                                          for r in rows])
        gap = float(ev[kd]) if kd < D else float('nan')
        zmax = abs(float(ev[kd - 1])) if kd > 0 else 0.0
        sep = gap / max(zmax, 1e-300)
        ck.info(f"  {N:>3} {D:>6} {kd:>6} {str(hf_exact):>7} {kernum:>7} "
                f"{gap:>12.8g} {norm:>12.8g} {sep:>10.2e}")
        ck.equal(kernum, kd, f"{name}, N={N}: numeric dim ker H_N vs HF(N)")
        if hf_exact is not None:
            ck.equal(hf_exact, kd,
                     f"{name}, N={N}: HF from exact GF(p) Macaulay rank")
        ck.atleast(sep, 1e6, f"{name}, N={N}: zero/non-zero separation")
        out[N] = gap
    return out


def body(ck):
    # ---- (1) pyramid ------------------------------------------------------
    f5 = {(1, 0, 0, 1, 0): 1.0, (0, 1, 1, 0, 0): -1.0}
    pyr = analyse(ck, "PYRAMID C[x00,x01,x10,x11,y]/(x00 x11 - x01 x10)",
                  5, [f5], range(2, 9), lambda N: hf_quadric(5, N))
    for N, g in pyr.items():
        ck.rel(g, 2.0, 1e-9,
               f"pyramid N={N}: Delta_N = 2 exactly (unused variable pins the gap)")

    # ---- (2) same binomial without the apex variable ----------------------
    f4 = {(1, 0, 0, 1): 1.0, (0, 1, 1, 0): -1.0}
    noy = analyse(ck, "NO-y C[x00,x01,x10,x11]/(x00 x11 - x01 x10)",
                  4, [f4], range(2, 13), lambda N: hf_quadric(4, N))
    for N, g in noy.items():
        ck.rel(g, float(N), 1e-9,
               f"no-y N={N}: Delta_N = N exactly (not a cone)")

    # ---- (3) twisted cubic with and without a dummy variable --------------
    gtc5 = [{k: float(v) for k, v in g.items()}
            for g in bf.minors2x2(5, [0, 1, 2], [1, 2, 3])]
    tcd = analyse(ck, "TC+DUMMY C[z0,z1,z2,z3,w]/I_twisted_cubic",
                  5, gtc5, range(2, 13), hf_tc_dummy)
    for N, g in tcd.items():
        ck.rel(g, 2.0, 1e-9,
               f"twisted cubic + dummy, N={N}: Delta_N = 2 exactly")

    gtc4 = [{k: float(v) for k, v in g.items()}
            for g in bf.minors2x2(4, [0, 1, 2], [1, 2, 3])]
    tcp = analyse(ck, "TC plain C[z0..z3]/I_twisted_cubic (reference)",
                  4, gtc4, range(2, 13), lambda N: 3 * N + 1)
    for N in range(7, 13):
        ck.atleast(tcp[N] / N, TC_SLOPE_MIN,
                   f"plain twisted cubic N={N}: Delta_N/N >= 0.85 (the gap the "
                   f"dummy variable destroys)")
    ck.atleast(tcp[12] / tcd[12], 5.0,
               "twisted cubic: Delta_12(plain)/Delta_12(with dummy) >= 5")

    # ---- (5) where the pyramid minimiser sits -----------------------------
    ck.info("\n  --- pyramid: minimum attained inside y^(N-2) * (quadratic in x)? ---")
    for N in range(2, 9):
        idx = bf.mono_index(5, N)
        H = bf.hamiltonian([f5], N, dtype=float).real
        H = (H + H.T) / 2
        sel = [idx[m2 + (N - 2,)] for m2 in bf.monomials(4, 2)]
        e = np.linalg.eigvalsh(H[np.ix_(sel, sel)])
        k0 = int((e < 1e-9 * max(float(e[-1]), 1.0)).sum())
        loc = float(e[k0]) if k0 < len(e) else float('nan')
        ck.info(f"    N={N:2d}: dim(subspace)={len(sel)}, smallest positive "
                f"energy there = {loc:.8g}, global Delta_N = {pyr[N]:.8g}")
        ck.rel(loc, 2.0, 1e-9,
               f"pyramid N={N}: y^(N-2)*(x-quadrics) contains a vector of "
               f"energy 2 (Fact 7.1 attained)")
        ck.rel(loc, pyr[N], 1e-9,
               f"pyramid N={N}: that vector attains the global Delta_N")


if __name__ == "__main__":
    checkharness.run(
        "task9_pyramid",
        "report.md Sect. 7 / Conj. 8.3(b): the pyramid and the twisted cubic "
        "with a dummy variable have Delta_N = 2 exactly (cones pin the gap) "
        "while the same ideals without the unused variable have Delta_N = N "
        "and Delta_N ~ 0.85N",
        body)
