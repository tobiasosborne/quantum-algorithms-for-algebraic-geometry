"""Checker: Fact 7.2, the Takagi two-sided gap bound for quadrics (NEW checker).

CONVENTIONS: definitions/definitions.md D-takagi-factorisation, D-macaulay-gap.
Takagi values are written tau_j, tau_min (convention C9).  DEPARTURE FROM C5:
like the whole seed survey, generators are used AS WRITTEN (unit coefficients),
not normalised to unit Bombieri-Weyl norm; see README, "Conventions".

This is the check HANDOFF.md lists as "suggested next small step 1":
"Check Fact 7.2 numerically on the survey's random quadric in P^4: compute
Takagi values, compare slope of Delta_N with 4 tau_min^2."

SEED CLAIM UNDER TEST
  seed/analysis-2026-09-01/report.md, Sect. 7, Fact 7.2:
    "Any quadric can be brought by a UNITARY change of variables (Takagi
     factorisation of its complex symmetric matrix) to f = sum_j tau_j w_j^2 with
     tau_j >= 0 the Takagi values and w_j orthonormal linear forms ... Then
        4 tau_min^2 (N-2) + ||f||^2_Fock  <=  Delta_N
                                        <=  tau_min^2 N(N-1) + ||f||^2_Fock
                                            - 2 tau_min^2,
     the upper bound from h = w_min^(N-2).  For the conic, d = (1/2,1/2,1) and
     the lower bound is N+1, which is the exact value found numerically.  So
     the gap of a quadric grows at least linearly with slope 4 tau_min^2 ...
     a cone (tau_min = 0) has bounded gap.  This explains the 'flat' random
     quadric in P^4 in the survey (a 5x5 Gaussian symmetric matrix typically
     has a small Takagi value, so the growth is slow) and the pinned pyramid."

WHAT IS CHECKED (exit 0 only if all hold)
  For eight quadrics (conic; sum of squares; z0^2; the square binomial with
  and without an unused apex variable; the survey's Kostlan-random quadrics in
  P^2, P^3, P^4), at every N in range:
  (1) NORMALISATION IDENTITY: ||f||^2_Fock = 2 sum_j tau_j^2 with tau_j the
      singular values of the symmetric coefficient matrix (this is what makes
      the Takagi form norm-preserving);
  (2) LOWER BOUND: Delta_N >= 4 tau_min^2 (N-2) + ||f||^2_Fock;
  (3) UPPER BOUND: Delta_N <= tau_min^2 N(N-1) + ||f||^2_Fock - 2 tau_min^2;
  (4) Delta_2 = ||f||^2_Fock exactly (both bounds coincide at N = 2);
  (5) SLOPE: (Delta_Nmax - Delta_2)/(Nmax - 2) >= 4 tau_min^2, i.e. the gap
      really grows at least at the claimed rate;
  (6) CONES: when tau_min = 0 (z0^2, the pyramid) the bounds pinch and
      Delta_N = ||f||^2_Fock exactly for every N -- a bounded gap;
  (7) the "flat quadric in P^4" explanation: tau_min <= P4_TAU_MIN_MAX = 0.05 for
      the survey's P^4 quadric, so 4 tau_min^2 <= 0.01 and the observed total
      growth over the whole N range is below FLAT_GROWTH.

BUDGET: dim R_N <= 1820 (P^4 to N = 12, P^2 to N = 14).
"""
import math

import numpy as np

import bf
import checkharness
import ideals

RTOL = 1e-9
P4_TAU_MIN_MAX = 0.05
FLAT_GROWTH = 0.05      # Delta_Nmax - Delta_2 for the P^4 random quadric


def sym_matrix(f, nv):
    """The symmetric A with f = z^T A z, from the coefficient dict."""
    A = np.zeros((nv, nv), dtype=complex)
    for a, c in f.items():
        idx = [i for i in range(nv) for _ in range(a[i])]
        i, j = idx
        if i == j:
            A[i, i] += c
        else:
            A[i, j] += c / 2
            A[j, i] += c / 2
    return A


def fock_norm2(f):
    return float(sum(abs(c)**2 * bf.fact_prod(a) for a, c in f.items()))


def run(ck, name, nv, f, Ns, cone=False):
    ck.equal(bf.poly_deg(f), 2, f"{name}: f is a quadric")
    A = sym_matrix(f, nv)
    tau = np.linalg.svd(A, compute_uv=False)
    tau_min_v = float(tau.min())
    nrm = fock_norm2(f)
    ck.info(f"\n  --- {name} ---")
    ck.info(f"    Takagi values tau = {np.round(tau, 6)}   tau_min = {tau_min_v:.6f}   "
            f"||f||^2_Fock = {nrm:.6f}   2*sum tau_j^2 = {2*float((tau**2).sum()):.6f}")
    ck.rel(2.0 * float((tau**2).sum()), nrm, 1e-9,
           f"{name}: ||f||^2_Fock = 2 sum_j tau_j^2 (Takagi form is norm "
           f"preserving)")
    ck.info(f"    {'N':>3} {'dim':>6} {'lower':>13} {'Delta_N':>13} "
            f"{'upper':>13}")
    gaps = {}
    for N in Ns:
        ev = bf.spectrum([f], N)
        kd = bf.dim_h(nv, N) - bf.dim_h(nv, N - 2)
        knum = int((ev < 1e-9 * max(float(ev[-1]), 1e-300)).sum())
        gap = float(ev[kd])
        lo = 4 * tau_min_v**2 * (N - 2) + nrm
        hi = tau_min_v**2 * N * (N - 1) + nrm - 2 * tau_min_v**2
        gaps[N] = gap
        ck.info(f"    {N:>3} {bf.dim_h(nv, N):>6} {lo:>13.8g} {gap:>13.8g} "
                f"{hi:>13.8g}")
        ck.equal(knum, kd, f"{name}, N={N}: dim ker H_N = dim R_N - dim R_(N-2)")
        ck.atleast(gap, lo - RTOL * max(lo, 1.0),
                   f"{name}, N={N}: Fact 7.2 LOWER bound "
                   f"4 tau_min^2 (N-2) + ||f||^2")
        ck.atmost(gap, hi + RTOL * max(hi, 1.0),
                  f"{name}, N={N}: Fact 7.2 UPPER bound "
                  f"tau_min^2 N(N-1) + ||f||^2 - 2 tau_min^2")
        if cone:
            ck.rel(gap, nrm, RTOL,
                   f"{name}, N={N}: tau_min = 0 pinches the bounds, "
                   f"Delta_N = ||f||^2_Fock (bounded gap)")
    Nlo, Nhi = min(Ns), max(Ns)
    ck.rel(gaps[Nlo], nrm, RTOL,
           f"{name}: Delta_2 = ||f||^2_Fock (bounds coincide at N=2)")
    slope = (gaps[Nhi] - gaps[Nlo]) / (Nhi - Nlo)
    ck.info(f"    secant slope over N in [{Nlo},{Nhi}] = {slope:.6f} ; "
            f"4 tau_min^2 = {4*tau_min_v**2:.6f}")
    ck.atleast(slope, 4 * tau_min_v**2 - RTOL,
               f"{name}: mean slope of Delta_N is at least 4 tau_min^2")
    return tau, tau_min_v, nrm, gaps


def body(ck):
    run(ck, "conic z0z1 - z2^2 in P^2", 3, {(1, 1, 0): 1, (0, 0, 2): -1},
        range(2, 15))
    run(ck, "z0^2 + z1^2 + z2^2 in P^2", 3,
        {(2, 0, 0): 1, (0, 2, 0): 1, (0, 0, 2): 1}, range(2, 15))
    run(ck, "z0^2 in P^2 (a cone, tau_min = 0)", 3, {(2, 0, 0): 1},
        range(2, 15), cone=True)
    run(ck, "x00x11 - x01x10 in P^3 (no unused variable)", 4,
        {(1, 0, 0, 1): 1.0, (0, 1, 1, 0): -1.0}, range(2, 13))
    run(ck, "pyramid x00x11 - x01x10 with apex y (a cone, tau_min = 0)", 5,
        {(1, 0, 0, 1, 0): 1.0, (0, 1, 1, 0, 0): -1.0}, range(2, 9), cone=True)

    # the survey's own random quadrics (same seeds as ideals.one_random_quadric)
    caps = {2: 15, 3: 13, 4: 13}
    last = None
    for n in (2, 3, 4):
        nv, g, name, hf = ideals.one_random_quadric(n)
        last = run(ck, f"survey's {name}", nv, g[0], range(2, caps[n]))

    # ---- (7) the "flat quadric in P^4" explanation -----------------------
    tau, tau_min_v, nrm, gaps = last
    Nhi = max(gaps)
    ck.info(f"\n  P^4 random quadric: tau_min = {tau_min_v:.6f}, 4 tau_min^2 = "
            f"{4*tau_min_v**2:.6f}, Delta_{Nhi} - Delta_2 = "
            f"{gaps[Nhi] - gaps[2]:.6f}")
    ck.atmost(tau_min_v, P4_TAU_MIN_MAX,
              "survey's P^4 random quadric: tau_min is small (the report's "
              "explanation of the flat row in the Sect. 7 table)")
    ck.atmost(gaps[Nhi] - gaps[2], FLAT_GROWTH,
              f"survey's P^4 random quadric: Delta_N barely grows over "
              f"N = 2..{Nhi}")


if __name__ == "__main__":
    checkharness.run(
        "fact72_takagi",
        "report.md Fact 7.2: for eight quadrics the Takagi values give "
        "4 tau_min^2 (N-2) + ||f||^2 <= Delta_N <= tau_min^2 N(N-1) + ||f||^2 - "
        "2 tau_min^2, with equality throughout for cones (tau_min = 0), and "
        "tau_min explains the flat P^4 row of the Sect. 7 survey",
        body)
