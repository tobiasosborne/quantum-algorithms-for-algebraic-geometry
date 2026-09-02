"""Checker: the conic f = z0 z1 - z2^2 in P^2.

CONVENTIONS: definitions/definitions.md is the single source (rk-light L2).
DEPARTURE FROM convention C5: like the seed's own numerics, generators are
used AS WRITTEN (unit coefficients), not normalised to unit Bombieri-Weyl
norm, so every Delta_N below is the gap of that presentation.  See README.

SEED CLAIM UNDER TEST
  seed/analysis-2026-09-01/report.md
  - Sect. 2, Fact 2.1  : ker H_N = (I_N)^perp and dim ker H_N = HF_{R/I}(N);
                         for the conic HF(N) = 2N+1.
  - Sect. 2, Fact 2.3  : a(f)(z0 z1 z2^2) = z2^2 - 2 z0 z1 ;
                         a(f)(z0 z1 + c z2^2) = 0 iff c = 1/2 ;
                         a(f) f = 3 = ||f||^2_Fock  (Sect. 9, correction 4:
                         the notes' "1 - 2 =? -1" should read 1 + 2 = 3).
  - Sect. 7, Fact 7.1  : Delta_N >= ||f||^2_Fock = 3, and for the conic
                         Delta_N = N + 1 exactly.

WHAT IS CHECKED (exit 0 only if all hold)
  (1) the three hand computations of Fact 2.3, symbolically (sympy);
  (2) for N = 2..NMAX, three INDEPENDENT computations of dim I_N agree
      (numerical SVD rank of the stacked a(f_j); exact GF(p) rank of the
      Macaulay matrix; exact sympy rank for N <= NMAX_SYMPY) and
      dim ker H_N = dim R_N - dim I_N = 2N+1 exactly;
  (3) the numerical kernel count of H_N (eigenvalues < 1e-8 ||H_N||) equals
      2N+1, with the zero/non-zero split unambiguous by a factor >= 1e6;
  (4) Delta_N = N+1 to relative 1e-9.

BUDGET: NMAX = 8 (dim R_8 = 45); runs in a few seconds.
"""
import math

import numpy as np
import sympy as sp

import bf
import checkharness

NMAX = 8            # dimension cap: dim R_N = C(N+2,2) = 45 at N = 8
NMAX_SYMPY = 6      # exact sympy rank cross-check up to here
ZERO_SEP = 1e6      # required ratio Delta_N / (largest eigenvalue called zero)

NV = 3
F = {(1, 1, 0): 1, (0, 0, 2): -1}


def a_of_f(f, expr, Z):
    out = 0
    for a, c in f.items():
        t = expr
        for j in range(len(a)):
            t = sp.diff(t, Z[j], a[j])
        out += sp.conjugate(sp.nsimplify(c)) * t
    return sp.expand(out)


def body(ck):
    # ---- (1) Fact 2.3, the notes' hand computations ---------------------
    z0, z1, z2 = sp.symbols('z0 z1 z2')
    Z = [z0, z1, z2]

    e1 = a_of_f(F, z0 * z1 * z2**2, Z)
    ck.info(f"  a(f)(z0 z1 z2^2) = {e1}")
    ck.require(sp.simplify(e1 - (z2**2 - 2 * z0 * z1)) == 0,
               f"Fact 2.3: a(f)(z0 z1 z2^2) = {e1}, expected z2^2 - 2 z0 z1")

    c = sp.symbols('c')
    e2 = a_of_f(F, z0 * z1 + c * z2**2, Z)
    sol = sp.solve(sp.Eq(e2, 0), c)
    ck.info(f"  a(f)(z0 z1 + c z2^2) = {e2}  -> zero iff c = {sol}")
    ck.equal(sol, [sp.Rational(1, 2)], "Fact 2.3: c solving a(f)(z0z1 + c z2^2) = 0")

    nrm = sum(abs(cc)**2 * bf.fact_prod(a) for a, cc in F.items())
    ck.info(f"  ||f||^2_Fock = <f|f> = {nrm}")
    ck.equal(nrm, 3, "Sect. 9 correction 4: ||f||^2_Fock for z0z1 - z2^2")

    # ---- (2)+(3)+(4) Fact 2.1 and Fact 7.1 ------------------------------
    ck.info(f"  {'N':>3} {'dimR_N':>7} {'rk(A)':>6} {'rk_GFp':>7} {'rk_sympy':>9} "
            f"{'ker':>5} {'2N+1':>5} {'Delta_N':>10} {'zero-sep':>10}")
    for N in range(2, NMAX + 1):
        A = bf.stacked_A([F], N)
        dh = bf.dim_h(NV, N)
        rows = bf.macaulay_rows([F], N)
        rnum = bf.rank_numeric(A)
        rp = bf.rank_mod_p(rows)
        rs = sp.Matrix(rows).rank() if N <= NMAX_SYMPY else rp
        ker = dh - rnum

        ev = bf.spectrum([F], N)
        norm = float(ev[-1])
        kd = 2 * N + 1
        zmax = float(abs(ev[kd - 1]))
        gap = float(ev[kd])
        sep = gap / max(zmax, 1e-300)
        knum = int((ev < 1e-8 * max(norm, 1.0)).sum())

        ck.info(f"  {N:>3} {dh:>7} {rnum:>6} {rp:>7} {rs:>9} {ker:>5} {2*N+1:>5} "
                f"{gap:>10.6f} {sep:>10.2e}")

        ck.equal(rnum, rp, f"N={N}: numeric rank(A) vs GF(p) Macaulay rank")
        ck.equal(rp, rs, f"N={N}: GF(p) rank vs exact sympy rank")
        ck.equal(ker, 2 * N + 1, f"N={N}: dim ker H_N (Fact 2.1, HF = 2N+1)")
        ck.equal(knum, 2 * N + 1,
                 f"N={N}: numeric kernel count of H_N (Fact 2.1)")
        ck.atleast(sep, ZERO_SEP, f"N={N}: zero/non-zero eigenvalue separation")
        ck.rel(gap, N + 1, 1e-9, f"N={N}: Delta_N (Fact 7.1, conic Delta_N = N+1)")
        ck.atleast(gap, 3.0 - 1e-9,
                   f"N={N}: Delta_N >= ||f||^2_Fock = 3 (Fact 7.1)")


if __name__ == "__main__":
    checkharness.run(
        "task1_conic",
        "report.md Facts 2.1, 2.3, 7.1 for the conic z0z1 - z2^2 in P^2: "
        "dim ker H_N = 2N+1 (three independent ranks) and Delta_N = N+1 exactly, "
        f"N <= {NMAX}",
        body)
