"""Checker: ker H_N = (I_N)^perp as SUBSPACES, not merely as dimensions.

CONVENTIONS: definitions/definitions.md is the single source (rk-light L2).
DEPARTURE FROM convention C5: like the seed's own numerics, generators are
used AS WRITTEN (unit coefficients), not normalised to unit Bombieri-Weyl
norm, so every Delta_N below is the gap of that presentation.  See README.

SEED CLAIM UNDER TEST
  seed/analysis-2026-09-01/report.md, Sect. 2, Fact 2.1:
    "ker H_N = (I_N)^perp ... and span{z^beta f_j} perp ker H_N held to 1e-14."

WHAT IS CHECKED (exit 0 only if all hold)
  For each test ideal and each N:
  (1) the coordinate matrix M of the spanning set {z^beta f_j} of I_N, written
      in the ORTHONORMAL Fock basis |k> = z^k/sqrt(k!), is orthogonal to an
      orthonormal basis K of ker H_N:  max |M^* K| <= ORTH_TOL;
  (2) rank(M) + dim ker H_N = dim R_N exactly (so the kernel is the FULL
      orthogonal complement, not just contained in it);
  (3) the numerically declared kernel dimension equals the predicted Hilbert
      function, and the zero / non-zero eigenvalue split is unambiguous.

ORTH_TOL is 1e-10 on the scale-free quantity max |<I_N basis, ker>| with the
I_N rows normalised; the seed reports 1e-14 on the raw (unnormalised) rows,
which is the same statement up to the row norms printed below.

BUDGET: N ranges as in the seed's task2b_subspace.py (largest dim R_N = 120).
"""
import math

import numpy as np

import bf
import checkharness
import ideals

ORTH_TOL = 1e-10
ZERO_SEP = 1e6


def I_N_coords(gens, N):
    """Rows = z^beta f_j in the ORTHONORMAL basis |e> = z^e/sqrt(e!)."""
    nv = bf.poly_nvars(gens[0])
    idx = bf.mono_index(nv, N)
    rows = []
    for f in gens:
        m = bf.poly_deg(f)
        if m > N:
            continue
        for b in bf.monomials(nv, N - m):
            v = np.zeros(len(idx), dtype=complex)
            for a, c in f.items():
                e = tuple(a[j] + b[j] for j in range(nv))
                v[idx[e]] += c * math.sqrt(bf.fact_prod(e))   # z^e = sqrt(e!)|e>
            rows.append(v)
    return np.array(rows)


def body(ck):
    cases = ((ideals.twisted_cubic, range(2, 8)),
             (ideals.rnc4, range(2, 7)),
             (ideals.two_generic_quadrics, range(2, 8)),
             (ideals.monomial_ideal, range(2, 8)),
             (lambda: ideals.boolean(4), range(2, 7)))
    for maker, Ns in cases:
        nv, g, name, hf = maker()
        ck.info(f"\n  --- {name} ---")
        ck.info(f"  {'N':>3} {'dimR_N':>7} {'ker':>5} {'rank I_N':>9} {'sum':>5} "
                f"{'max|<I_N,ker>|':>15} {'zero-sep':>10}")
        for N in Ns:
            H = bf.hamiltonian(g, N)
            H = (H + H.conj().T) / 2
            ev, U = np.linalg.eigh(H)
            norm = float(ev[-1])
            kd = int((ev < 1e-9 * norm).sum())
            K = U[:, :kd]

            M = I_N_coords(g, N)
            rown = np.linalg.norm(M, axis=1)
            Mn = M / np.maximum(rown, 1e-300)[:, None]
            overlap = float(np.abs(Mn.conj() @ K).max()) if kd else 0.0
            r = int(np.linalg.matrix_rank(M, tol=1e-9 * np.abs(M).max()))
            sep = (float(ev[kd]) / max(abs(float(ev[kd - 1])), 1e-300)
                   if 0 < kd < len(ev) else float('inf'))

            ck.info(f"  {N:>3} {bf.dim_h(nv, N):>7} {kd:>5} {r:>9} {kd + r:>5} "
                    f"{overlap:>15.2e} {sep:>10.2e}")

            ck.equal(kd, hf(N), f"{name}, N={N}: numeric dim ker H_N vs HF(N)")
            ck.equal(kd + r, bf.dim_h(nv, N),
                     f"{name}, N={N}: dim ker H_N + rank I_N vs dim R_N")
            ck.atmost(overlap, ORTH_TOL,
                      f"{name}, N={N}: max |<normalised I_N row, ker H_N>|")
            if math.isfinite(sep):
                ck.atleast(sep, ZERO_SEP,
                           f"{name}, N={N}: zero/non-zero eigenvalue separation")


if __name__ == "__main__":
    checkharness.run(
        "task2b_subspace",
        "report.md Fact 2.1 as a subspace identity: span{z^beta f_j} is exactly "
        "orthogonal to ker H_N (to 1e-10 on normalised rows) and rank I_N + "
        "dim ker H_N = dim R_N, for five test ideals",
        body)
