"""Checker: the toric (binomial-ideal) fibre structure of the ground space.

CONVENTIONS: definitions/definitions.md is the single source (rk-light L2).
DEPARTURE FROM convention C5: like the seed's own numerics, generators are
used AS WRITTEN (unit coefficients), not normalised to unit Bombieri-Weyl
norm, so every Delta_N below is the gap of that presentation.  See README.

SEED CLAIM UNDER TEST
  seed/analysis-2026-09-01/report.md, Sect. 7, second bullet:
    "binomial (toric) ideals: H_N is exactly block diagonal over the fibres of
     the A-grading; each block is a weighted graph Laplacian on the fibre whose
     one-dimensional kernel is spanned by the fibre sum q_u = sum_{Ak=u} z^k/k!
     (the exponential generating function of the fibre, NUMERICALLY EXACT), so
     the degeneracy is the number of fibres and Delta_N = min_u lambda_2(H_u).
     ... for the twisted cubic Delta_N/N -> 0.854 and for the rational normal
     quartic Delta_N ~ 0.61 N^1.05"
  (also quoted in Conjecture 8.3(b)).

WHAT IS CHECKED (exit 0 only if all hold)
  For the rational normal quartic in P^4 and the twisted cubic in P^3, at every
  N in the seed's ranges:
  (1) BLOCK DIAGONALITY: max |H_N[a,b]| over pairs with different A-degree
      u = sum_i i k_i is <= OFF_TOL;
  (2) FIBRE SUMS IN THE KERNEL: max |H_N q_u| <= RES_TOL for every fibre u;
  (3) DEGENERACY = NUMBER OF FIBRES: rank{q_u} = #fibres = dim ker H_N, and
      each individual fibre block has EXACTLY a one-dimensional kernel;
  (4) Delta_N = min_u lambda_2(H_u) to relative 1e-9;
  (5) growth: twisted cubic Delta_N/N -> 0.854 +- TC_TOL for N >= 10;
      rational normal quartic Delta_N/N in [0.66, 0.72] at N = 10, consistent
      with the published 0.61 N^1.05.

BUDGET: rnc4 N <= 10 (dim R_10 = 1001), twisted cubic N <= 12 (dim 455), as
in the seed's task4_toric.py.
"""
import math

import numpy as np

import bf
import checkharness
import ideals

OFF_TOL = 1e-12
RES_TOL = 1e-10
TC_LIMIT = 0.854
TC_TOL = 0.005
RNC_RANGE_AT_10 = (0.66, 0.72)


def fiber_label(k, weights):
    return sum(w * kk for w, kk in zip(weights, k))


def run(ck, name, nv, gens, Ns):
    ck.info(f"\n  === {name} ===")
    weights = list(range(nv))
    out = {}
    for N in Ns:
        mons = bf.monomials(nv, N)
        H = bf.hamiltonian(gens, N)
        H = (H + H.conj().T) / 2
        labels = np.array([fiber_label(k, weights) for k in mons])
        us = sorted(set(labels.tolist()))

        # (1) block diagonality over the A-grading
        diff = labels[:, None] != labels[None, :]
        offblock = float(np.abs(H[diff]).max()) if diff.any() else 0.0

        # (2) fibre sums q_u = sum_{Ak=u} z^k/k!  (normalised)
        Q = np.zeros((len(us), len(mons)))
        for j, u in enumerate(us):
            for a, k in enumerate(mons):
                if labels[a] == u:
                    Q[j, a] = 1.0 / math.sqrt(bf.fact_prod(k))
            Q[j] /= np.linalg.norm(Q[j])
        resid = float(np.abs(Q @ H).max())

        ev = np.linalg.eigvalsh(H)
        kd = int((ev < 1e-9 * float(ev[-1])).sum())
        rankQ = int(np.linalg.matrix_rank(Q, tol=1e-10))
        gap = float(ev[kd])

        # (3)+(4) per-fibre second eigenvalue
        fib_ker, fib_lam2 = 0, []
        for u in us:
            sel = np.where(labels == u)[0]
            e = np.linalg.eigvalsh(H[np.ix_(sel, sel)])
            k0 = int((e < 1e-9 * max(float(ev[-1]), 1.0)).sum())
            fib_ker += k0
            fib_lam2.append(float(e[k0]) if k0 < len(e) else float('inf'))
        minfib = min(fib_lam2)

        ck.info(f"   N={N:2d} dim={len(mons):5d} #fibres={len(us):4d} "
                f"kerdim={kd:4d} rank(q_u)={rankQ:4d} |H q_u|max={resid:.2e} "
                f"offblock={offblock:.1e} per-fibre-ker={fib_ker:4d} "
                f"Delta={gap:.6g} min_u lam2={minfib:.6g} Delta/N={gap/N:.4f}")

        ck.atmost(offblock, OFF_TOL,
                  f"{name}, N={N}: H_N block diagonal over the A-grading")
        ck.atmost(resid, RES_TOL,
                  f"{name}, N={N}: fibre sums q_u annihilated by H_N")
        ck.equal(rankQ, len(us), f"{name}, N={N}: the q_u are independent")
        ck.equal(kd, len(us),
                 f"{name}, N={N}: dim ker H_N = number of A-graded fibres")
        ck.equal(fib_ker, len(us),
                 f"{name}, N={N}: every fibre block has a 1-dimensional kernel")
        ck.rel(gap, minfib, 1e-9,
               f"{name}, N={N}: Delta_N = min_u lambda_2(H_u)")
        out[N] = gap
    return out


def body(ck):
    nv, g, name, hf = ideals.rnc4()
    rnc = run(ck, name, nv, g, range(2, 11))
    ck.between(rnc[10] / 10.0, RNC_RANGE_AT_10[0], RNC_RANGE_AT_10[1],
               "rational normal quartic: Delta_10/10 (published 0.61 N^1.05)")

    nv, g, name, hf = ideals.twisted_cubic()
    tc = run(ck, name, nv, g, range(2, 13))
    for N in (10, 11, 12):
        ck.close(tc[N] / N, TC_LIMIT, TC_TOL,
                 f"twisted cubic: Delta_{N}/{N} vs the published limit 0.854")
    ck.close(tc[12] / 12 - tc[10] / 10, 0.0, 0.01,
             "twisted cubic: Delta_N/N is flat between N=10 and N=12")


if __name__ == "__main__":
    checkharness.run(
        "task4_toric",
        "report.md Sect. 7 toric bullet: H_N exactly block diagonal over the "
        "A-graded fibres, kernel spanned by the fibre sums q_u, degeneracy = "
        "number of fibres, Delta_N = min_u lambda_2(H_u), and Delta_N/N -> "
        "0.854 for the twisted cubic",
        body)
