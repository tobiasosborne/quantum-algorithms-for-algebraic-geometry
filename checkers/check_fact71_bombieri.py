"""Checker: Fact 7.1, principal ideals are uniformly gapped (NEW checker).

CONVENTIONS: definitions/definitions.md is the single source (rk-light L2).
DEPARTURE FROM convention C5: like the seed's own numerics, generators are
used AS WRITTEN (unit coefficients), not normalised to unit Bombieri-Weyl
norm, so every Delta_N below is the gap of that presentation.  See README.

SEED CLAIM UNDER TEST
  seed/analysis-2026-09-01/report.md, Sect. 7, Fact 7.1:
    "For I = (f), Delta_N >= ||f||^2_Fock = m! ||f||^2_BW for all N >= m.  The
     bound is attained whenever, after a unitary change of variables, the extra
     degree can be placed in a linear subspace orthogonal to the variables f
     depends on (e.g. f = z0^m, h = z1^(N-m); or f = z0+z1,
     h = (z0-z1)^(N-1)); in one variable Delta_N = N!/(N-m)!."
  This is the Bombieri-Beauzamy-Enflo-Montgomery inequality in Fock
  normalisation, and the d = 1 case of Conjecture 8.3(a).
  Referee round 1, item 43, corrected the earlier "attained for monomials":
  in ONE variable f = z^m has Delta_N = N!/(N-m)! > m! for N > m.

WHAT IS CHECKED (exit 0 only if all hold)
  (1) LOWER BOUND: for every principal ideal in the list (degrees 1,2,3,4,
      monomial / binomial / Kostlan-random / cone), Delta_N >= ||f||^2_Fock
      at every N in range, to relative 1e-9;
  (2) EQUALITY where the seed says it is attained: f = z0^m in >= 2 variables,
      f = z0 + z1 in >= 3 variables, the pyramid binomial (apex variable
      unused) -- Delta_N = ||f||^2_Fock exactly for every N;
  (3) STRICTNESS where the seed says it is strict: in ONE variable
      f = z0^m has Delta_N = N!/(N-m)! exactly, which exceeds m! for N > m;
  (4) at every N the numerical kernel dimension equals the principal-ideal
      Hilbert function dim R_N - dim R_{N-m}.

BUDGET: nv <= 5, dim R_N <= 1820; a few seconds.
"""
import math

import numpy as np

import bf
import checkharness

RTOL = 1e-9


def fock_norm2(f):
    return float(sum(abs(c)**2 * bf.fact_prod(a) for a, c in f.items()))


def gap_and_ker(f, nv, N):
    ev = bf.spectrum([f], N)
    m = bf.poly_deg(f)
    kd = bf.dim_h(nv, N) - bf.dim_h(nv, N - m)
    knum = int((ev < 1e-9 * max(float(ev[-1]), 1e-300)).sum())
    gap = float(ev[kd]) if kd < len(ev) else float('nan')
    return gap, kd, knum


def run(ck, name, nv, f, Ns, equality=False):
    nrm = fock_norm2(f)
    ck.info(f"\n  --- {name} (deg {bf.poly_deg(f)}, nv={nv}, "
            f"||f||^2_Fock = {nrm:.6f}) ---")
    ck.info(f"    {'N':>3} {'dim':>6} {'ker':>6} {'Delta_N':>13} "
            f"{'||f||^2_Fock':>13} {'Delta/||f||^2':>14}")
    for N in Ns:
        gap, kd, knum = gap_and_ker(f, nv, N)
        ck.info(f"    {N:>3} {bf.dim_h(nv, N):>6} {kd:>6} {gap:>13.8g} "
                f"{nrm:>13.6f} {gap / nrm:>14.6f}")
        ck.equal(knum, kd,
                 f"{name}, N={N}: dim ker H_N = dim R_N - dim R_(N-m)")
        ck.atleast(gap, nrm * (1 - RTOL),
                   f"{name}, N={N}: Fact 7.1 lower bound Delta_N >= "
                   f"||f||^2_Fock")
        if equality:
            ck.rel(gap, nrm, RTOL,
                   f"{name}, N={N}: Fact 7.1 equality (extra degree fits in an "
                   f"orthogonal linear subspace)")


def body(ck):
    # ---- (2) equality cases ----------------------------------------------
    for m in (1, 2, 3):
        run(ck, f"f = z0^{m} in P^2", 3, {bf.emono(3, [0] * m): 1.0},
            range(m, 13), equality=True)
    run(ck, "f = z0 + z1 in P^2", 3, {(1, 0, 0): 1.0, (0, 1, 0): 1.0},
        range(1, 13), equality=True)
    run(ck, "pyramid binomial x00x11 - x01x10 with unused apex y", 5,
        {(1, 0, 0, 1, 0): 1.0, (0, 1, 1, 0, 0): -1.0}, range(2, 9),
        equality=True)

    # ---- (1) strict / generic cases --------------------------------------
    run(ck, "conic z0z1 - z2^2 in P^2", 3, {(1, 1, 0): 1, (0, 0, 2): -1},
        range(2, 15))
    run(ck, "binomial x00x11 - x01x10 in P^3 (no unused variable)", 4,
        {(1, 0, 0, 1): 1.0, (0, 1, 1, 0): -1.0}, range(2, 13))
    rng = np.random.default_rng(17)
    run(ck, "Kostlan-random cubic in P^2", 3, bf.random_form(3, 3, rng),
        range(3, 13))
    rng = np.random.default_rng(23)
    run(ck, "Kostlan-random quartic in P^2", 3, bf.random_form(3, 4, rng),
        range(4, 13))
    rng = np.random.default_rng(29)
    run(ck, "Kostlan-random cubic in P^3", 4, bf.random_form(4, 3, rng),
        range(3, 11))

    # ---- (3) one variable: the bound is NOT attained for N > m -----------
    ck.info("\n  --- one variable: f = z0^m in C[z0], Delta_N = N!/(N-m)! ---")
    for m in (1, 2, 3):
        f = {(m,): 1.0}
        nrm = fock_norm2(f)
        for N in range(m, 11):
            H = bf.hamiltonian([f], N)
            lam = float(np.linalg.eigvalsh((H + H.conj().T) / 2)[0])
            want = math.factorial(N) / math.factorial(N - m)
            ck.info(f"    m={m} N={N:2d}: Delta_N = {lam:.6f}, N!/(N-m)! = "
                    f"{want:.6f}, ||f||^2_Fock = m! = {nrm:.1f}")
            ck.rel(lam, want, RTOL,
                   f"one variable, m={m}, N={N}: Delta_N = N!/(N-m)!")
            ck.atleast(lam, nrm * (1 - RTOL),
                       f"one variable, m={m}, N={N}: Fact 7.1 lower bound")
            if N > m:
                ck.atleast(lam / nrm, 1.0 + 1e-9,
                           f"one variable, m={m}, N={N}: the bound is STRICT "
                           f"(referee round 1, item 43)")


if __name__ == "__main__":
    checkharness.run(
        "fact71_bombieri",
        "report.md Fact 7.1: Delta_N >= ||f||^2_Fock for principal ideals over "
        "degrees 1-4 in 1-5 variables; equality exactly in the seed's stated "
        "cases; in one variable Delta_N = N!/(N-m)!, strictly above m! for N>m",
        body)
