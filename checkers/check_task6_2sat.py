"""Checker: the multigraded (Segre) quantum-2-SAT embedding, 3 blocks.

CONVENTIONS: definitions/definitions.md is the single source (rk-light L2).
DEPARTURE FROM convention C5: like the seed's own numerics, generators are
used AS WRITTEN (unit coefficients), not normalised to unit Bombieri-Weyl
norm, so every Delta_N below is the gap of that presentation.  See README.

SEED CLAIM UNDER TEST
  seed/analysis-2026-09-01/report.md, Sect. 3, "Multigraded (Segre) version",
  and Proposition 3.1:
    "A multilinear form f on a set S of sites gives
        a^dag(f) a(f) |_(1,...,1) = |f><f|_S (x) 1
     EXACTLY, no factorials (checked to machine precision for 3 to 12 sites;
     e.g. three generic bilinear forms on the three pairs of a 3-qubit system
     leave a 2-dimensional inverse system, three singlet projectors leave the
     4-dimensional spin-3/2 multiplet)."
  and "the Hilbert function at the multilinear degree is the linear-algebra
  relaxation of the geometric question".

WHAT IS CHECKED (exit 0 only if all hold)
  With 3 blocks z_{i,0}, z_{i,1} (i = 0,1,2), so nv = 6 and N = 3:
  (1) the multidegree-(1,1,1) block of the polynomial-ring H_3 equals the
      3-qubit reference sum_j |f_j><f_j| (x) 1 to <= SECTOR_TOL, in EVERY
      configuration tested (23 instances);
  (2) dim ker H_sector equals the multigraded Hilbert function
      8 - rank(Macaulay restricted to the sector), in every instance;
  (3) three singlet projectors leave a 4-dimensional kernel (the spin-3/2
      multiplet) with the remaining spectrum {3,3,3,3};
  (4) one singlet leaves a 6-dimensional kernel with spectrum {2,2};
  (5) three generic bilinear forms leave a 2-dimensional inverse system
      (5 seeds); two generic forms leave 4; one generic form leaves 6.

BUDGET: nv = 6, N = 3, dim R_3 = 56.  Sub-second.
"""
import itertools

import numpy as np

import bf
import checkharness

NB = 3
NV = 2 * NB
SECTOR_TOL = 1e-12
EV_TOL = 1e-9

SINGLET = np.array([[0, 1], [-1, 0]], dtype=complex)


def v(i, s):
    return 2 * i + s


def bilinear(i, j, F):
    f = {}
    for s in (0, 1):
        for t in (0, 1):
            e = bf.emono(NV, [v(i, s), v(j, t)])
            f[e] = f.get(e, 0) + F[s, t]
    return {a: c for a, c in f.items() if abs(c) > 0}


def sector_indices():
    idx = bf.mono_index(NV, NB)
    out, lbl = [], []
    for bits in itertools.product((0, 1), repeat=NB):
        e = bf.emono(NV, [v(i, bits[i]) for i in range(NB)])
        out.append(idx[e])
        lbl.append(bits)
    return out, lbl


def two_sat_H(pairs):
    """Reference 3-qubit Hamiltonian sum_j |f_j><f_j| (x) 1."""
    H = np.zeros((8, 8), dtype=complex)
    for (i, j, F) in pairs:
        k = [x for x in range(3) if x not in (i, j)][0]
        for u in (0, 1):
            psi = np.zeros(8, dtype=complex)
            for s in (0, 1):
                for t in (0, 1):
                    bits = [0] * 3
                    bits[i] = s
                    bits[j] = t
                    bits[k] = u
                    psi[bits[0] * 4 + bits[1] * 2 + bits[2]] += F[s, t]
            H += np.outer(psi, psi.conj())
    return H


def sector_H(pairs):
    gens = [bilinear(i, j, F) for (i, j, F) in pairs]
    Hfull = bf.hamiltonian(gens, NB)
    sel, lbl = sector_indices()
    Hs = Hfull[np.ix_(sel, sel)]
    perm = np.argsort([b[0] * 4 + b[1] * 2 + b[2] for b in lbl])
    Hs = Hs[np.ix_(perm, perm)]
    err = float(np.abs(Hs - two_sat_H(pairs)).max())
    ev = np.linalg.eigvalsh((Hs + Hs.conj().T) / 2)
    kd = int((ev < 1e-9 * max(float(ev[-1]), 1.0)).sum())
    rows = bf.macaulay_rows(gens, NB)
    R = np.array(rows, dtype=complex)[:, sel][:, perm]
    R = R[np.abs(R).max(axis=1) > 1e-12]
    rk = int(np.linalg.matrix_rank(R, tol=1e-10)) if len(R) else 0
    return kd, err, 8 - rk, ev


def one(ck, tag, pairs, want_ker, want_nonzero=None):
    kd, err, hfv, ev = sector_H(pairs)
    ck.info(f"    {tag:34s} ker={kd}  HF(1,1,1)={hfv}  "
            f"||H_sector - ref||={err:.2e}  ev={np.round(ev, 8)}")
    ck.atmost(err, SECTOR_TOL,
              f"{tag}: multidegree-(1,1,1) sector identity (Sect. 3)")
    ck.equal(kd, hfv,
             f"{tag}: dim ker H_sector vs multigraded Hilbert function")
    ck.equal(kd, want_ker, f"{tag}: dimension of the inverse system")
    if want_nonzero is not None:
        got = sorted(round(float(x), 6) for x in ev[kd:])
        ck.equal(got, sorted(want_nonzero), f"{tag}: non-zero spectrum")


def body(ck):
    ck.info("  [A] singlets on all three pairs")
    one(ck, "three singlets", [(0, 1, SINGLET), (1, 2, SINGLET), (0, 2, SINGLET)],
        4, [3.0, 3.0, 3.0, 3.0])

    ck.info("\n  [B] singlet on one pair only")
    one(ck, "one singlet", [(0, 1, SINGLET)], 6, [2.0, 2.0])

    ck.info("\n  [C] random bilinear forms on all three pairs (5 seeds)")
    for seed in range(5):
        rng = np.random.default_rng(seed)
        F = [rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2)) for _ in range(3)]
        one(ck, f"3 generic forms, seed {seed}",
            [(0, 1, F[0]), (1, 2, F[1]), (0, 2, F[2])], 2)

    ck.info("\n  [D] random bilinear form on one pair (5 seeds)")
    for seed in range(5):
        rng = np.random.default_rng(seed)
        F = rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2))
        one(ck, f"1 generic form, seed {seed}", [(0, 1, F)], 6)

    ck.info("\n  [E] random forms on two pairs (5 seeds)")
    for seed in range(5):
        rng = np.random.default_rng(seed)
        F = [rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2)) for _ in range(2)]
        one(ck, f"2 generic forms, seed {seed}", [(0, 1, F[0]), (1, 2, F[1])], 4)


if __name__ == "__main__":
    checkharness.run(
        "task6_2sat",
        "report.md Sect. 3 / Prop. 3.1: the multidegree-(1,1,1) block of H_3 IS "
        "sum_j |f_j><f_j| (x) 1 exactly, its kernel dimension is the multigraded "
        "Hilbert function, and the singlet / generic instances leave inverse "
        "systems of dimension 4 / 6 / 2 / 4",
        body)
