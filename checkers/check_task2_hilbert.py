"""Checker: dim ker H_N = HF_{R/I}(N) for the whole test-ideal family.

CONVENTIONS: definitions/definitions.md is the single source (rk-light L2).
DEPARTURE FROM convention C5: like the seed's own numerics, generators are
used AS WRITTEN (unit coefficients), not normalised to unit Bombieri-Weyl
norm, so every Delta_N below is the gap of that presentation.  See README.

SEED CLAIM UNDER TEST
  seed/analysis-2026-09-01/report.md, Sect. 2, Fact 2.1:
    "ker H_N = (I_N)^perp, dim ker H_N = HF_{R/I}(N).  Numerically:
     dim ker H_N agreed with an independent exact rank of the Macaulay matrix
     for the conic (2N+1), the twisted cubic (3N+1), the rational normal
     quartic (4N+1), a monomial ideal, two generic quadrics in P^3 (4N) and
     the boolean ideals of Section 6."
  The closed forms 3N+1 / 4N+1 / 4N / sum_i C(n,i) are the Hilbert functions
  supplied by ideals.py and are part of the claim.

WHAT IS CHECKED (exit 0 only if all hold, for EVERY ideal and EVERY N run)
  (1) dim R_N - rank_numeric(stacked a(f_j)) == the predicted HF(N);
  (2) that numerical rank equals an INDEPENDENT exact rank of the Macaulay
      matrix (GF(p) for integer generators, SVD for the complex ones);
  (3) for the integer ideals, both agree with an exact sympy rank at the
      four smallest N.
  A single mismatch at a single N exits 1.

BUDGET: N ranges as in the seed's task2_hilbert.py (largest dim R_N = 210);
runs in a few seconds.
"""
import numpy as np
import sympy as sp

import bf
import checkharness
import ideals

EXACT_SMALL = 4     # how many of the smallest N get an exact sympy rank


def report(ck, nv, gens, name, hf, Ns, integer_coeffs=True, exact_small=True):
    ck.info(f"\n  --- {name} ---")
    ck.info(f"  {'N':>3} {'dimR_N':>7} {'rk(A,num)':>10} {'rk(Macaulay)':>13} "
            f"{'ker':>6} {'HF pred':>8}")
    for N in Ns:
        dh = bf.dim_h(nv, N)
        A = bf.stacked_A(gens, N)
        rA = bf.rank_numeric(A)
        rows = bf.macaulay_rows(gens, N)
        if integer_coeffs:
            rM = bf.rank_mod_p([[int(round(x.real)) if isinstance(x, complex) else int(x)
                                 for x in r] for r in rows])
        else:
            rM = bf.rank_numeric(rows)
        ker = dh - rA
        pred = hf(N)
        ck.info(f"  {N:>3} {dh:>7} {rA:>10} {rM:>13} {ker:>6} {pred:>8}")
        ck.equal(ker, pred,
                 f"{name}, N={N}: dim ker H_N vs Hilbert function (Fact 2.1)")
        ck.equal(rA, rM,
                 f"{name}, N={N}: numeric rank(A) vs independent Macaulay rank")
    if exact_small and integer_coeffs:
        for N in list(Ns)[:EXACT_SMALL]:
            M = sp.Matrix([[sp.Integer(int(round(x.real)) if isinstance(x, complex) else int(x))
                            for x in r] for r in bf.macaulay_rows(gens, N)])
            rex = M.rank()
            rA = bf.rank_numeric(bf.stacked_A(gens, N))
            ck.equal(rex, rA, f"{name}, N={N}: exact sympy Macaulay rank vs rank(A)")
        ck.info(f"  sympy exact ranks cross-checked for N in "
                f"{list(Ns)[:EXACT_SMALL]}")


def body(ck):
    nv, g, name, hf = ideals.twisted_cubic()
    report(ck, nv, g, name, hf, range(1, 10))

    nv, g, name, hf = ideals.monomial_ideal()
    report(ck, nv, g, name, hf, range(1, 11))

    nv, g, name, hf = ideals.rnc4()
    report(ck, nv, g, name, hf, range(1, 9))

    nv, g, name, hf = ideals.two_generic_quadrics()
    report(ck, nv, g, name, hf, range(1, 9),
           integer_coeffs=False, exact_small=False)

    for n in (2, 3, 4, 5):
        nv, g, name, hf = ideals.boolean(n)
        report(ck, nv, g, name, hf, range(1, n + 5))


if __name__ == "__main__":
    checkharness.run(
        "task2_hilbert",
        "report.md Fact 2.1: dim ker H_N = HF_{R/I}(N) for the twisted cubic "
        "(3N+1), monomial ideal, rational normal quartic (4N+1), two generic "
        "quadrics in P^3 (4N) and the boolean ideals in P^2..P^5, cross-checked "
        "against an independent exact Macaulay rank",
        body)
