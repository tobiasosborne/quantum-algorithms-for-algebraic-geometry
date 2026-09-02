"""Checker: coherent states, points of V, and the conjugation.

CONVENTIONS: definitions/definitions.md is the single source (rk-light L2).
DEPARTURE FROM convention C5: like the seed's own numerics, generators are
used AS WRITTEN (unit coefficients), not normalised to unit Bombieri-Weyl
norm, so every Delta_N below is the gap of that presentation.  See README.

SEED CLAIM UNDER TEST
  seed/analysis-2026-09-01/report.md, Sect. 3, "Consequences", first bullet:
    "|p>^{(x)N} in ker H_N  <=>  conj(p) in V(I)  ...  The energy of a coherent
     state is a weighted sum of squares of the equations,
        <p^{(x)N}| H_N |p^{(x)N}> = sum_j N!/(N-m_j)! |f_j(conj p)|^2,  ||p||=1,
     NUMERICALLY exact to 1e-15, conjugation included (a complex quadric and a
     point with f(p) = 0 != f(conj p): the state of p has energy O(N^2), the
     state of conj p has energy 1e-16)."
  and Sect. 9, correction 3: "Points of V correspond to coherent states of the
  CONJUGATE vectors."

WHAT IS CHECKED (exit 0 only if all hold)
  For the conic, the twisted cubic and a genuinely complex quadric, at several
  points on and off the variety and several N:
  (1) the measured energy E = <psi|H_N|psi>/<psi|psi> of the normalised
      coherent state agrees with sum_j N!/(N-m_j)! |f_j(conj p)|^2 to
      relative REL_TOL;
  (2) when conj(p) is a point of V, E <= ZERO_TOL (the state is in ker H_N);
  (3) when conj(p) is not a point of V, E >= OFF_MIN (it is not);
  (4) CONJUGATION IS ESSENTIAL: for the complex quadric with f(p) = 0 but
      f(conj p) != 0, the alternative prediction sum_j N!/(N-m_j)!|f_j(p)|^2
      differs from the measured energy by at least SPLIT_MIN, in both
      directions (p and conj p).  A checker that passed with the conjugation
      removed from a(f) would not be testing this claim.

BUDGET: N <= 5, nv <= 4; sub-second.
"""
import math

import numpy as np

import bf
import checkharness
import ideals

REL_TOL = 1e-12
ZERO_TOL = 1e-12
OFF_MIN = 1e-3
SPLIT_MIN = 1.0


def coh(p, N):
    nv = len(p)
    mons = bf.monomials(nv, N)
    return np.array([math.factorial(N) * np.prod([p[j]**k[j] for j in range(nv)])
                     / math.sqrt(bf.fact_prod(k)) for k in mons], dtype=complex)


def evalp(f, p):
    return sum(c * np.prod([p[j]**a[j] for j in range(len(p))])
               for a, c in f.items())


def energies(gens, p, N):
    pn = np.array(p, dtype=complex)
    pn = pn / np.linalg.norm(pn)
    H = bf.hamiltonian(gens, N)
    v = coh(pn, N)
    E = float(np.real(v.conj() @ H @ v) / np.real(v.conj() @ v))
    predA = sum(math.factorial(N) / math.factorial(N - bf.poly_deg(f))
                * abs(evalp(f, np.conj(pn)))**2
                for f in gens if bf.poly_deg(f) <= N)
    predB = sum(math.factorial(N) / math.factorial(N - bf.poly_deg(f))
                * abs(evalp(f, pn))**2
                for f in gens if bf.poly_deg(f) <= N)
    return E, float(predA), float(predB), pn


def check_set(ck, name, gens, pts_on, pts_off, Ns, split=False):
    ck.info(f"\n  === {name} ===")
    for tag, pts in (("ON  V(conj)", pts_on), ("OFF V(conj)", pts_off)):
        for p in pts:
            for N in Ns:
                E, predA, predB, pn = energies(gens, p, N)
                ck.info(f"    {tag}  p={np.round(np.array(p, dtype=complex), 4)} "
                        f"N={N}: E={E:.10g}  pred[f(conj p)]={predA:.10g} "
                        f"(err {abs(E - predA):.2e})  pred[f(p)]={predB:.10g}")
                ck.rel(E, predA, REL_TOL,
                       f"{name}, p={np.round(np.array(p, dtype=complex), 4)}, "
                       f"N={N}: coherent-state energy formula (Sect. 3)")
                if tag.startswith("ON"):
                    ck.atmost(abs(E), ZERO_TOL,
                              f"{name}, N={N}: coherent state of a point with "
                              f"conj(p) in V lies in ker H_N")
                else:
                    ck.atleast(E, OFF_MIN,
                               f"{name}, N={N}: coherent state of a point with "
                               f"conj(p) not in V is NOT in ker H_N")
                if split:
                    ck.atleast(abs(E - predB), SPLIT_MIN,
                               f"{name}, N={N}: the UNconjugated prediction "
                               f"sum_j |f_j(p)|^2 must disagree (conjugation is "
                               f"essential, Sect. 9 correction 3)")


def body(ck):
    # ---- conic (real coefficients: f(p) and f(conj p) agree in modulus) ---
    fc = {(1, 1, 0): 1, (0, 0, 2): -1}

    def conic_pt(a, b):
        return (a, b, np.sqrt(complex(a) * complex(b)))

    on = [conic_pt(1, 1), conic_pt(4, 1), conic_pt(2 + 1j, 1 - 3j), conic_pt(1j, 1)]
    off = [(1, 1, 0), (1, 2, 3), (1j, 1, 1)]
    check_set(ck, "conic z0z1 - z2^2 in P^2", [fc], on, off, [2, 3, 5])

    # ---- twisted cubic ---------------------------------------------------
    _, G, _, _ = ideals.twisted_cubic()

    def tcp(s, t):
        return (t**3, s * t**2, s * s * t, s**3)

    on = [tcp(1, 1), tcp(2, 1), tcp(1j, 1), tcp(1 + 1j, 2 - 1j), (0, 0, 0, 1)]
    # NOTE: the seed's task7_coherent.py lists (1,1,1,1) as an OFF point, but
    # (1,1,1,1) = tcp(1,1) IS on the twisted cubic (all three 2x2 minors vanish);
    # replaced here by (1,1,1,2), for which z0z3 - z1z2 = 1.  See README.
    off = [(1, 1, 1, 2), (1, 0, 0, 1), (1, 2, 1, 0)]
    check_set(ck, "twisted cubic in P^3", G, on, off, [2, 3, 4])

    # ---- genuinely complex quadric: only conj(p) matters ------------------
    f = {(2, 0, 0): 1 + 0j, (0, 2, 0): 1j, (0, 0, 2): 2 - 1j, (1, 1, 0): 3j}
    z2 = np.sqrt(-(1 + 1j + 3j) / (2 - 1j))
    p = (1, 1, z2)                       # f(p) = 0, f(conj p) != 0
    pbar = (1, 1, np.conj(z2))           # f(conj pbar) = 0
    check_set(ck, "random complex quadric in P^2", [f],
              [pbar], [p], [2, 3, 4], split=True)


if __name__ == "__main__":
    checkharness.run(
        "task7_coherent",
        "report.md Sect. 3: <p^{(x)N}|H_N|p^{(x)N}> = sum_j N!/(N-m_j)! "
        "|f_j(conj p)|^2 to relative 1e-12, the coherent state is in ker H_N "
        "iff conj(p) in V, and the UNconjugated formula demonstrably fails for "
        "a complex quadric",
        body)
