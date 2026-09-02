"""Checker: the two closed forms the seed reads off its gap data.

CONVENTIONS: definitions/definitions.md is the single source (rk-light L2).
DEPARTURE FROM convention C5: like the seed's own numerics, generators are
used AS WRITTEN (unit coefficients), not normalised to unit Bombieri-Weyl
norm, so every Delta_N below is the gap of that presentation.  See README.

SEED CLAIMS UNDER TEST
  seed/analysis-2026-09-01/report.md
  - Sect. 7, Fact 7.1 (and Fact 7.2 for the conic):
      "For the conic, a(f)a^dag(f) = a^dag(f)a(f) + n0 + n1 + 4 n2 + 3 gives
       Delta_N >= N+1, and NUMERICALLY Delta_N = N+1 exactly for N <= 30."
  - Sect. 7, first bullet of the "what is known or easy" list:
      "monomial ideals: H_N is diagonal with integer entries
       sum_j prod_i k_i!/(k_i - alpha_i^(j))!, so Delta_N >= 1;
       e.g. ||H_N|| = N(N-1)(N-2) exactly for (z0^2, z0z1, z1^3)."

WHAT IS CHECKED (exit 0 only if all hold)
  (1) conic, N = 2..NMAX_CONIC: dim ker H_N = 2N+1 and Delta_N = N+1 to
      relative 1e-9, with the zero / non-zero split unambiguous;
  (2) monomial ideal (z0^2, z0z1, z1^3) at N in NS_MONO:
      (a) H_N is EXACTLY diagonal (max off-diagonal entry <= 1e-12),
      (b) every diagonal entry equals the closed form
          sum_j prod_i k_i!/(k_i - alpha_i^(j))!  exactly (integers),
      (c) hence every eigenvalue is an integer and Delta_N = 1, ||H_N|| =
          N(N-1)(N-2).

BUDGET: NMAX_CONIC = 30 (dim R_30 = 496), NS_MONO up to N = 16 (dim 153).
"""
import math

import numpy as np

import bf
import checkharness
import ideals

NMAX_CONIC = 30
NS_MONO = (5, 8, 12, 16)
ZERO_SEP = 1e6
DIAG_TOL = 1e-12
INT_TOL = 1e-9

CONIC = {(1, 1, 0): 1, (0, 0, 2): -1}


def diagonal_closed_form(gens, N, nv):
    """sum_j prod_i k_i!/(k_i - alpha_i^(j))!  for each monomial k of degree N."""
    out = []
    for k in bf.monomials(nv, N):
        tot = 0
        for f in gens:
            (alpha,) = tuple(f.keys())          # single monomial per generator
            if any(alpha[i] > k[i] for i in range(nv)):
                continue
            term = 1
            for i in range(nv):
                for t in range(alpha[i]):
                    term *= (k[i] - t)
            tot += term * abs(f[alpha])**2
        out.append(tot)
    return np.array(out, dtype=float)


def body(ck):
    # ---- (1) conic ---------------------------------------------------------
    ck.info("  conic z0z1 - z2^2 in P^2:")
    ck.info(f"    {'N':>3} {'dim':>5} {'ker':>5} {'Delta_N':>11} {'N+1':>5} "
            f"{'||H_N||':>12} {'zero-sep':>10}")
    for N in range(2, NMAX_CONIC + 1):
        ev = bf.spectrum([CONIC], N)
        kd = 2 * N + 1
        knum = int((ev < 1e-9 * float(ev[-1])).sum())
        gap = float(ev[kd])
        sep = gap / max(abs(float(ev[kd - 1])), 1e-300)
        ck.info(f"    {N:>3} {bf.dim_h(3, N):>5} {knum:>5} {gap:>11.6f} "
                f"{N+1:>5} {float(ev[-1]):>12.6f} {sep:>10.2e}")
        ck.equal(knum, kd, f"conic N={N}: numeric dim ker H_N vs 2N+1")
        ck.atleast(sep, ZERO_SEP, f"conic N={N}: zero/non-zero separation")
        ck.rel(gap, N + 1, 1e-9, f"conic N={N}: Delta_N = N+1 exactly (Fact 7.1)")

    # ---- (2) monomial ideal ------------------------------------------------
    nv, g, name, hf = ideals.monomial_ideal()
    ck.info(f"\n  {name}: H_N diagonal with the closed-form integer entries")
    ck.info(f"    {'N':>3} {'dim':>5} {'max off-diag':>13} {'max|H_kk - cf|':>15} "
            f"{'max|lam-round|':>15} {'Delta_N':>9} {'||H_N||':>9}")
    for N in NS_MONO:
        H = bf.hamiltonian(g, N)
        H = (H + H.conj().T) / 2
        d = np.diag(H).real.copy()
        off = H - np.diag(np.diag(H))
        offmax = float(np.abs(off).max())
        cf = diagonal_closed_form(g, N, nv)
        cfdev = float(np.abs(d - cf).max())
        ev = np.sort(np.linalg.eigvalsh(H))
        intdev = float(np.abs(ev - np.round(ev)).max())
        gap = float(ev[hf(N)])
        ck.info(f"    {N:>3} {bf.dim_h(nv, N):>5} {offmax:>13.2e} {cfdev:>15.2e} "
                f"{intdev:>15.2e} {gap:>9.6f} {float(ev[-1]):>9.1f}")
        ck.atmost(offmax, DIAG_TOL, f"monomial ideal N={N}: H_N is diagonal")
        ck.atmost(cfdev, INT_TOL,
                  f"monomial ideal N={N}: diagonal entries vs the closed form "
                  f"sum_j prod_i k_i!/(k_i-alpha_i)!")
        ck.atmost(intdev, INT_TOL,
                  f"monomial ideal N={N}: spectrum is integral")
        ck.rel(gap, 1.0, 1e-9, f"monomial ideal N={N}: Delta_N = 1 (>= 1 claimed)")
        ck.rel(float(ev[-1]), N * (N - 1) * (N - 2), 1e-9,
               f"monomial ideal N={N}: ||H_N|| = N(N-1)(N-2)")


if __name__ == "__main__":
    checkharness.run(
        "task3c_exact",
        "report.md Fact 7.1 (conic Delta_N = N+1 exactly for N <= 30) and "
        "Sect. 7 monomial bullet (H_N diagonal, integer closed-form entries, "
        "Delta_N = 1, ||H_N|| = N(N-1)(N-2))",
        body)
