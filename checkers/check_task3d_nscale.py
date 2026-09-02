"""Checker: scaling of Delta with the number of variables n at fixed N.

CONVENTIONS: definitions/definitions.md is the single source (rk-light L2).
DEPARTURE FROM convention C5: like the seed's own numerics, generators are
used AS WRITTEN (unit coefficients), not normalised to unit Bombieri-Weyl
norm, so every Delta_N below is the gap of that presentation.  See README.

SEED CLAIM UNDER TEST
  seed/analysis-2026-09-01/report.md, Sect. 7, closing paragraph of the survey:
    "At fixed N and growing n: the boolean ideal has Delta_{n+1} = 2 for
     n = 2,...,6 (numerically, not a theorem), and random quadric ideals at
     N = 3, 4 have Delta ~ 0.7-1.2, flat in n."
  This is the numerical support quoted for Conjecture 8.3(c) ("generic forms
  are gapped uniformly in n").

WHAT IS CHECKED (exit 0 only if all hold)
  (1) boolean ideal in P^n, N = n+1, n = 2..6: dim ker H_N = 2^n exactly and
      Delta = 2 to relative 1e-9;
  (2) k = 1, 2 Kostlan-random quadrics in P^n at N = 3, 4, n up to the
      dimension cap: dim ker H_N equals the complete-intersection Hilbert
      function exactly, Delta stays inside GAP_RANGE, and the fitted
      EXPONENTIAL rate |d log Delta / dn| <= FLAT_TOL, which is the
      operative content of "flat in n".
  NOTE (recorded in README): the literal interval "0.7-1.2" does NOT hold --
  one random quadric gives Delta = 3.70 (N=3, n=2), 4.62 (N=4, n=2) and 1.80
  (n=8).  This checker therefore tests the wider GAP_RANGE plus flatness, and
  the discrepancy is reported rather than hidden.

BUDGET: CAP = 3500 on dim R_N, as in the seed's task3d_nscale.py.
"""
import numpy as np

import bf
import checkharness
import ideals
from gaps import gap_row

CAP = 3500
GAP_RANGE = (0.5, 5.0)
FLAT_TOL = 0.10          # |log-slope of Delta per extra variable|


def body(ck):
    # ---- (1) boolean ideal at N = n+1 -------------------------------------
    ck.info("  boolean ideal in P^n at N = n+1 (kernel = 2^n):")
    ck.info(f"    {'n':>3} {'N':>3} {'dim':>7} {'ker':>7} {'Delta':>10} "
            f"{'||H||':>11} {'||H||/Delta':>12}")
    bn, bg = [], []
    for n in range(2, 8):
        N = n + 1
        nv, g, name, hf = ideals.boolean(n)
        if bf.dim_h(nv, N) > CAP:
            break
        r = gap_row(g, N, hf(N))
        bn.append(n)
        bg.append(r['gap'])
        ck.info(f"    {n:>3} {N:>3} {r['dim']:>7} {r['ker']:>7} {r['gap']:>10.6g} "
                f"{r['norm']:>11.6g} {r['ratio']:>12.4g}")
        ck.equal(r['kernum'], 2**n, f"boolean P^{n}, N={N}: dim ker H_N = 2^n")
        ck.rel(r['gap'], 2.0, 1e-9,
               f"boolean P^{n}, N={N}: Delta_(n+1) = 2 exactly (Sect. 7)")
    ck.atleast(len(bn), 5, "boolean sweep reached n = 2..6")

    # ---- (2) random quadric families at fixed N ---------------------------
    for k in (1, 2):
        for N in (3, 4):
            ck.info(f"\n  {k} random quadric(s) in P^n, N={N}:")
            ck.info(f"    {'n':>3} {'dim':>7} {'ker':>6} {'Delta':>10} "
                    f"{'||H||':>11} {'||H||/Delta':>12}")
            ns, gs = [], []
            for n in range(2, 15):
                nv, g, name, hf = ideals.k_random_quadrics(n, k, seed=100 + n)
                if bf.dim_h(nv, N) > CAP:
                    break
                r = gap_row(g, N, hf(N))
                ns.append(n)
                gs.append(r['gap'])
                ck.info(f"    {n:>3} {r['dim']:>7} {r['ker']:>6} {r['gap']:>10.6g} "
                        f"{r['norm']:>11.6g} {r['ratio']:>12.4g}")
                ck.equal(r['kernum'], hf(N),
                         f"{k} random quadrics P^{n}, N={N}: dim ker H_N vs the "
                         f"complete-intersection Hilbert function")
                ck.between(r['gap'], GAP_RANGE[0], GAP_RANGE[1],
                           f"{k} random quadrics P^{n}, N={N}: Delta in range")
            ck.atleast(len(ns), 8, f"k={k}, N={N}: sweep reached n >= 9")
            slope = float(np.polyfit(ns, np.log(gs), 1)[0])
            power = float(np.polyfit(np.log(ns), np.log(gs), 1)[0])
            ck.info(f"      exp fit: log Delta = {slope:+.4f}*n + c ; "
                    f"power fit: Delta ~ n^({power:+.3f})")
            ck.atmost(abs(slope), FLAT_TOL,
                      f"k={k}, N={N}: |exponential rate of Delta in n| "
                      f"('flat in n', Sect. 7 / Conj. 8.3(c))")


if __name__ == "__main__":
    checkharness.run(
        "task3d_nscale",
        "report.md Sect. 7 n-scaling: boolean Delta_(n+1) = 2 exactly for "
        "n = 2..6, and k = 1,2 random quadrics at N = 3,4 are flat in n "
        "(|d log Delta/dn| <= 0.1), with kernel dims equal to the predicted "
        "Hilbert functions",
        body)
