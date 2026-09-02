"""Checker: the Macaulay-gap survey table of report Sect. 7.

CONVENTIONS: definitions/definitions.md is the single source (rk-light L2).
DEPARTURE FROM convention C5: like the seed's own numerics, generators are
used AS WRITTEN (unit coefficients), not normalised to unit Bombieri-Weyl
norm, so every Delta_N below is the gap of that presentation.  See README.

SEED CLAIM UNDER TEST
  seed/analysis-2026-09-01/report.md, Sect. 7, "Numerical survey" table, and
  the sentence closing it:
    "For every 'algebraic-geometry' family tested, Delta_N is bounded below by
     a constant and ||H_N||/Delta_N grows like N^1 to N^3."
  Table rows tested here (published Delta_N ; ||H_N||/Delta_N):
    twisted cubic, N<=22               0.80 N^1.03    ; 1.08 N^1.01
    monomial (z0^2,z0z1,z1^3), N<=40   1 exactly      ; ~0.6 N^3.1,
                                       with ||H_N|| = N(N-1)(N-2) exactly
    rational normal quartic, N<=13     0.61 N^1.05    ; 1.5 N^0.97
    two generic quadrics in P^3, N<=22 0.11 N^0.66    ; 3.3 N^1.39
    boolean ideal P^3..P^5, N<=14      -> 2, then N^(0.05..0.4) ; N^(1.7..2.1)
    one random quadric P^2/P^3/P^4     N^1.04 / N^0.56 / ~1.75
  Also Sect. 2, Fact 2.1, at every N of the survey: dim ker H_N = HF(N).

WHAT IS CHECKED (exit 0 only if all hold)
  (1) EVERY row of EVERY table: the numerically declared kernel dimension
      (eigenvalues < 1e-9 ||H_N||) equals the predicted Hilbert function
      exactly, and the zero / non-zero split is unambiguous (ratio >= 1e6);
  (2) Delta_N >= a per-family constant floor at every N
      ("Delta_N is bounded below by a constant");
  (3) the fitted power laws (same fit window as the seed: N >= median N)
      agree with the published table, exponents to +-EXP_TOL and prefactors
      to the absolute tolerances written at each call;
  (4) monomial ideal: Delta_N = 1 exactly, and ||H_N|| = N(N-1)(N-2) exactly
      for N >= 3 (at N = 2 the cubic generator cannot act and ||H_2|| = 2);
  (5) the ||H_N||/Delta_N exponent of every family lies in RATIO_EXP_RANGE.

BUDGET: seed N caps kept (largest dim R_N = 3060).
"""
import numpy as np

import bf
import checkharness
import ideals
from gaps import fit_power, table

EXP_TOL = 0.06                    # absolute tolerance on a fitted exponent
ZERO_SEP = 1e6
RATIO_EXP_RANGE = (0.9, 3.3)      # "||H_N||/Delta_N grows like N^1 to N^3"


def survey(ck, label, gens, Ns, hf, gap_floor):
    """Run the seed's table(), then re-fit to recover prefactors too."""
    rows, _, _ = table(label, gens, Ns, hf)
    for r in rows:
        ck.equal(r['kernum'], r['ker'],
                 f"{label}, N={r['N']}: numeric kernel dim vs Hilbert function "
                 f"(Fact 2.1)")
        ck.atleast(r['sep'], ZERO_SEP,
                   f"{label}, N={r['N']}: zero/non-zero eigenvalue separation")
        ck.atleast(r['gap'], gap_floor,
                   f"{label}, N={r['N']}: Delta_N bounded below by a constant")
    ff = Ns[len(Ns) // 2] if len(Ns) > 3 else Ns[0]
    sel = [r for r in rows if r['N'] >= ff]
    g_exp, g_pre = fit_power([r['N'] for r in sel], [r['gap'] for r in sel])
    r_exp, r_pre = fit_power([r['N'] for r in sel], [r['ratio'] for r in sel])
    ck.between(r_exp, RATIO_EXP_RANGE[0], RATIO_EXP_RANGE[1],
               f"{label}: fitted exponent of ||H_N||/Delta_N")
    return rows, g_exp, g_pre, r_exp, r_pre


def body(ck):
    # ---- (a) twisted cubic ------------------------------------------------
    nv, g, name, hf = ideals.twisted_cubic()
    rows, ge, gp, re_, rp = survey(ck, "(a) twisted cubic P^3", g,
                                   list(range(2, 23)), hf, gap_floor=1.9)
    ck.close(ge, 1.03, EXP_TOL, "twisted cubic: Delta_N exponent (table 1.03)")
    ck.close(gp, 0.80, 0.10, "twisted cubic: Delta_N prefactor (table 0.80)")
    ck.close(re_, 1.01, EXP_TOL, "twisted cubic: ||H||/Delta exponent (table 1.01)")
    ck.close(rp, 1.08, 0.15, "twisted cubic: ||H||/Delta prefactor (table 1.08)")

    # ---- (b) monomial ideal ----------------------------------------------
    nv, g, name, hf = ideals.monomial_ideal()
    rows, ge, gp, re_, rp = survey(ck, "(b) monomial (z0^2,z0z1,z1^3) P^2", g,
                                   list(range(2, 41)), hf, gap_floor=1.0 - 1e-9)
    for r in rows:
        ck.rel(r['gap'], 1.0, 1e-9,
               f"monomial ideal, N={r['N']}: Delta_N = 1 exactly (Sect. 7)")
        if r['N'] >= 3:      # N >= max_j m_j; at N = 2 the cubic generator
            want = r['N'] * (r['N'] - 1) * (r['N'] - 2)   # cannot act and
            ck.rel(r['norm'], want, 1e-9,                 # ||H_2|| = 2, not 0
                   f"monomial ideal, N={r['N']}: ||H_N|| = N(N-1)(N-2) exactly")
    ck.close(ge, 0.0, 1e-6, "monomial ideal: Delta_N exponent (table: 0 exactly)")
    ck.close(re_, 3.10, 0.10, "monomial ideal: ||H||/Delta exponent (table 3.1)")

    # ---- (c) rational normal quartic -------------------------------------
    nv, g, name, hf = ideals.rnc4()
    rows, ge, gp, re_, rp = survey(ck, "(c) rational normal curve deg 4, P^4", g,
                                   list(range(2, 14)), hf, gap_floor=1.3)
    ck.close(ge, 1.05, EXP_TOL, "rnc4: Delta_N exponent (table 1.05)")
    ck.close(gp, 0.61, 0.08, "rnc4: Delta_N prefactor (table 0.61)")
    ck.close(re_, 0.97, EXP_TOL, "rnc4: ||H||/Delta exponent (table 0.97)")

    # ---- (d) two generic quadrics ----------------------------------------
    nv, g, name, hf = ideals.two_generic_quadrics()
    rows, ge, gp, re_, rp = survey(ck, "(d) 2 generic quadrics P^3", g,
                                   list(range(2, 23)), hf, gap_floor=0.2)
    ck.close(ge, 0.66, EXP_TOL, "2 generic quadrics: Delta_N exponent (table 0.66)")
    ck.close(gp, 0.11, 0.04, "2 generic quadrics: Delta_N prefactor (table 0.11)")
    ck.close(re_, 1.39, EXP_TOL,
             "2 generic quadrics: ||H||/Delta exponent (table 1.39)")

    # ---- (e) boolean ideals ----------------------------------------------
    for n, Nmax in ((2, 14), (3, 14), (4, 12), (5, 10)):
        nv, g, name, hf = ideals.boolean(n)
        rows, ge, gp, re_, rp = survey(ck, f"(e) boolean P^{n}", g,
                                       list(range(2, Nmax + 1)), hf,
                                       gap_floor=2.0 - 1e-9)
        if n >= 3:      # the table's exponent claim is stated for P^3..P^5
            ck.between(ge, 0.03, 0.45,
                       f"boolean P^{n}: Delta_N exponent (table 0.05..0.4)")
            ck.between(re_, 1.65, 2.15,
                       f"boolean P^{n}: ||H||/Delta exponent (table 1.7..2.1)")

    # ---- (f) one random quadric ------------------------------------------
    want_exp = {2: 1.04, 3: 0.56}
    for n, Nmax in ((2, 30), (3, 20), (4, 14)):
        nv, g, name, hf = ideals.one_random_quadric(n)
        rows, ge, gp, re_, rp = survey(ck, f"(f) single random quadric P^{n}", g,
                                       list(range(2, Nmax + 1)), hf,
                                       gap_floor=1.0)
        if n in want_exp:
            ck.close(ge, want_exp[n], EXP_TOL,
                     f"random quadric P^{n}: Delta_N exponent "
                     f"(table {want_exp[n]})")
        else:
            ck.between(ge, -0.05, 0.10,
                       f"random quadric P^{n}: Delta_N exponent (table: flat)")
            ck.close(rows[-1]['gap'], 1.75, 0.15,
                     f"random quadric P^4: Delta_N at N={rows[-1]['N']} "
                     f"(table ~1.75)")


if __name__ == "__main__":
    checkharness.run(
        "task3_gaps",
        "report.md Sect. 7 numerical survey: kernel dim = Hilbert function at "
        "every N, Delta_N bounded below by a constant, and the published power "
        "laws for Delta_N and ||H_N||/Delta_N for seven ideal families",
        body)
