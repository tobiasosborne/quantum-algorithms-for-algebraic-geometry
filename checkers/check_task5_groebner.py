"""Checker: the adiabatic Groebner degeneration of the twisted cubic.

CONVENTIONS: definitions/definitions.md is the single source (rk-light L2).
DEPARTURE FROM convention C5: like the seed's own numerics, generators are
used AS WRITTEN (unit coefficients), not normalised to unit Bombieri-Weyl
norm, so every Delta_N below is the gap of that presentation.  See README.

SEED CLAIMS UNDER TEST
  seed/analysis-2026-09-01/report.md
  - Sect. 5, item 5 (adiabatic preparation via Groebner degeneration):
      "NUMERICALLY (twisted cubic, whose 2x2 minors are a Groebner basis for
       w = (0,1,4,9), N <= 9): kernel dimension 3N+1 for all t in [1e-10, 1],
       Delta_N(t) decreasing monotonically from ~0.85N at t=1 to exactly 1 at
       t=0, so min_t Delta_N(t) = 1 independent of N and
       min_t Delta_N(t)/||H_N(t)|| ~ 2.5 N^-1.75."
  - Conjecture 8.4(a): "the twisted cubic, min_t Delta_N(t) = Delta_N(0) = 1
       for N = 3,...,9, with Delta_N(t) monotone in t."
  - Sect. 5.5 / referee round 1 item 27: the family is flat at t = 0 only
       because the generators are a w-Groebner basis; in_w(I) = (z0z2, z0z3,
       z1z3) has Hilbert function 3N+1.

WHAT IS CHECKED (exit 0 only if all hold)
  (1) in_w(f_j) are the three monomials z0z2, z0z3, z1z3, and the monomial
      ideal they generate has HF(N) = 3N+1 for N = 1..8 by exact GF(p) rank
      (this is what makes the degeneration flat);
  (2) for N = 2..NMAX and every t on the seed grid (1 down to 1e-10), the
      NUMERICAL kernel dimension of H_N(t) is exactly 3N+1;
  (3) Delta_N(t) is monotone non-increasing as t decreases along the grid
      (tolerance MONO_TOL);
  (4) Delta_N(0) = 1 exactly and min_t Delta_N(t) = 1 to relative 1e-6, for
      every N (i.e. the minimum gap along the path is N-independent);
  (5) Delta_N(t=1)/N lies in TC_SLOPE_RANGE ("~0.85 N" at the ideal end);
  (6) min_t Delta_N/||H_N|| fits c N^a with a in EXP_RANGE, c in PRE_RANGE
      (published 2.5 N^-1.75).

BUDGET: NMAX = 9 (dim R_9 = 220), the seed's own cap; 27 grid points in t.
"""
import math

import numpy as np

import bf
import checkharness
import ideals
from gaps import gap_row

W = (0, 1, 4, 9)
NV = 4
NMAX = 9
MONO_TOL = 1e-9
TC_SLOPE_RANGE = (0.83, 1.05)
EXP_RANGE = (-1.80, -1.70)
PRE_RANGE = (2.2, 2.9)


def deform(f, t):
    M = max(sum(w * a for w, a in zip(W, al)) for al in f)
    return {al: c * (t ** (M - sum(w * a for w, a in zip(W, al))))
            for al, c in f.items()}


def initial(f):
    M = max(sum(w * a for w, a in zip(W, al)) for al in f)
    return {al: c for al, c in f.items()
            if sum(w * a for w, a in zip(W, al)) == M}


def body(ck):
    _, G, _, hf = ideals.twisted_cubic()
    IN = [initial(f) for f in G]
    ck.info(f"  generators : {G}")
    ck.info(f"  in_w(f_j)  : {IN}")

    # ---- (1) the initial ideal ------------------------------------------
    for f in IN:
        ck.equal(len(f), 1, "each in_w(f_j) is a single monomial (w is generic)")
    got = sorted(tuple(next(iter(f))) for f in IN)
    want = sorted([(1, 0, 1, 0), (1, 0, 0, 1), (0, 1, 0, 1)])
    ck.equal(got, want, "in_w(I) generators are (z0z2, z0z3, z1z3)")

    ck.info("\n  HF of in_w(I) = (z0z2, z0z3, z1z3):")
    for N in range(1, 9):
        r = bf.rank_mod_p([[int(round(x.real)) if isinstance(x, complex) else int(x)
                            for x in row] for row in bf.macaulay_rows(IN, N)])
        hfv = bf.dim_h(NV, N) - r
        ck.info(f"    N={N}: dim R_N={bf.dim_h(NV, N):4d}  dim I_N={r:4d}  "
                f"HF={hfv:4d}  3N+1={3*N+1}")
        ck.equal(hfv, 3 * N + 1, f"in_w(I), N={N}: HF = 3N+1 (flatness at t=0)")

    # ---- (2)(3)(4)(5) the path ------------------------------------------
    ts = np.concatenate([np.logspace(0, -6, 25), [1e-8, 1e-10]])
    ck.info("\n  path t in (0,1]:")
    ck.info(f"    {'N':>3} {'Delta(t=1)':>11} {'Delta(t=0)':>11} "
            f"{'min_t Delta':>12} {'argmin t':>10} {'min_t D/||H||':>14}")
    Ns, mr = [], []
    for N in range(2, NMAX + 1):
        pred = 3 * N + 1
        gs, nr, kds = [], [], []
        prev = None
        for t in ts:
            gens = [deform(f, t) for f in G]
            r = gap_row(gens, N, kd=pred)
            gs.append(r['gap'])
            nr.append(r['gap'] / r['norm'])
            kds.append(r['kernum'])
            ck.equal(r['kernum'], pred,
                     f"N={N}, t={t:.3g}: kernel dimension constant = 3N+1")
            if prev is not None:
                ck.atmost(r['gap'] - prev, MONO_TOL * max(prev, 1.0),
                          f"N={N}, t={t:.3g}: Delta_N(t) monotone non-increasing "
                          f"as t decreases")
            prev = r['gap']
        r0 = gap_row(IN, N, kd=pred)
        gs = np.array(gs)
        i = int(np.argmin(gs))
        ck.info(f"    {N:>3} {gs[0]:>11.5g} {r0['gap']:>11.5g} {gs[i]:>12.5g} "
                f"{ts[i]:>10.3g} {min(nr):>14.6g}")
        ck.rel(r0['gap'], 1.0, 1e-9,
               f"N={N}: Delta_N(0) = 1 exactly at the monomial endpoint")
        ck.rel(float(gs[i]), 1.0, 1e-6,
               f"N={N}: min_t Delta_N(t) = 1, independent of N (Conj. 8.4(a))")
        if N >= 5:
            ck.between(gs[0] / N, TC_SLOPE_RANGE[0], TC_SLOPE_RANGE[1],
                       f"N={N}: Delta_N(t=1)/N (published ~0.85 N)")
        Ns.append(N)
        mr.append(min(nr))

    A = np.vstack([np.log(Ns), np.ones(len(Ns))]).T
    c = np.linalg.lstsq(A, np.log(mr), rcond=None)[0]
    pre, exp_ = math.exp(c[1]), c[0]
    ck.info(f"\n  fit min_t Delta_N/||H_N|| ~ {pre:.4g} * N^({exp_:+.3f})   "
            f"[published 2.5 N^-1.75]")
    ck.between(exp_, EXP_RANGE[0], EXP_RANGE[1],
               "min_t Delta/||H||: fitted exponent (published -1.75)")
    ck.between(pre, PRE_RANGE[0], PRE_RANGE[1],
               "min_t Delta/||H||: fitted prefactor (published 2.5)")


if __name__ == "__main__":
    checkharness.run(
        "task5_groebner",
        "report.md Sect. 5.5 / Conj. 8.4(a): along the w-Groebner degeneration "
        "of the twisted cubic the kernel dimension stays 3N+1, Delta_N(t) is "
        "monotone in t, min_t Delta_N(t) = Delta_N(0) = 1 for N = 3..9, and "
        "min_t Delta/||H|| ~ 2.5 N^-1.75",
        body)
