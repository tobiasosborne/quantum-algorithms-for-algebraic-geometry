"""Checker: the multigraded (quantum-2-SAT) sector and how small Delta gets.

CONVENTIONS: definitions/definitions.md is the single source (rk-light L2).
DEPARTURE FROM convention C5: like the seed's own numerics, generators are
used AS WRITTEN (unit coefficients), not normalised to unit Bombieri-Weyl
norm, so every Delta_N below is the gap of that presentation.  See README.

SEED CLAIMS UNDER TEST
  seed/analysis-2026-09-01/report.md
  - Sect. 3, multigraded (Segre) version:
      "a^dag(f) a(f) restricted to multidegree (1,...,1) = |f><f|_S (x) 1
       EXACTLY, no factorials (checked to machine precision ...);
       ... three singlet projectors leave the 4-dimensional spin-3/2 multiplet."
    Here: the degree-m block of the polynomial-ring H, restricted to the
    squarefree multidegree-(1,..,1) monomials, equals the direct m-qubit
    Hamiltonian sum_j |psi_j><psi_j| (x) 1 to machine precision.
  - Sect. 7 / Conjecture 8.3(d):
      "a chain of nearest-neighbour singlet projectors on m qubits has
       Delta = 9.13 m^-1.97 (m^2 Delta -> pi^2, the ferromagnetic Heisenberg
       gap)", and its kernel is the symmetric subspace, dimension m+1.

WHAT IS CHECKED (exit 0 only if all hold)
  (1) max |H_sector - H_direct| <= SECTOR_TOL for m = 3, 4, 5 (the sizes the
      seed's own script reaches; see README for the scope discrepancy with
      the report's "3 to 12 sites");
  (2) singlet chain, m = 2..MMAX: kernel dimension = m+1 exactly;
  (3) m^2 Delta_m increases with m and lies below pi^2, and is within
      PI2_TOL of pi^2 at m = MMAX  (i.e. m^2 Delta -> pi^2 from below);
  (4) the power fit over m >= 5 gives Delta ~ c m^a with a in EXP_RANGE and
      c in PRE_RANGE (published: 9.13 m^-1.97);
  (5) the random frustration-free chain is frustration free at every m
      (kernel dimension m+1 > 0) and has Delta > 0.

BUDGET: MMAX = 11 (2^11 = 2048 dense complex eigh), reduced from the seed's
m <= 12 to keep this checker inside the 600 s budget; see README.
"""
import itertools
import math

import numpy as np

import bf
import checkharness

MMAX = 11
SECTOR_TOL = 1e-12
PI2 = math.pi ** 2
PI2_TOL = 0.15          # |m^2 Delta - pi^2| at m = MMAX
EXP_RANGE = (-2.05, -1.90)
PRE_RANGE = (8.5, 9.8)

SINGLET = np.array([0, 1, -1, 0], dtype=complex)


def two_local(psi, i, j, m):
    """|psi><psi| on qubits i<j tensor identity elsewhere, as a 2^m matrix."""
    P = np.outer(psi, psi.conj())
    dim = 2**m
    H = np.zeros((dim, dim), dtype=complex)
    others = [k for k in range(m) if k not in (i, j)]
    for bits in itertools.product((0, 1), repeat=len(others)):
        idxs = []
        for s in (0, 1):
            for t in (0, 1):
                b = [0] * m
                b[i] = s
                b[j] = t
                for k, val in zip(others, bits):
                    b[k] = val
                idxs.append(int("".join(map(str, b)), 2))
        H[np.ix_(idxs, idxs)] += P
    return H


def verify_against_bf(m, pairs, psis):
    """Cross-check the direct qubit construction against the polynomial-ring H."""
    nv = 2 * m

    def v(i, s):
        return 2 * i + s

    gens = []
    for (i, j), psi in zip(pairs, psis):
        f = {}
        F = psi.reshape(2, 2)
        for s in (0, 1):
            for t in (0, 1):
                e = bf.emono(nv, [v(i, s), v(j, t)])
                f[e] = f.get(e, 0) + F[s, t]
        gens.append({a: c for a, c in f.items() if abs(c) > 1e-14})
    Hfull = bf.hamiltonian(gens, m)
    idx = bf.mono_index(nv, m)
    sel = [idx[bf.emono(nv, [v(i, b[i]) for i in range(m)])]
           for b in itertools.product((0, 1), repeat=m)]
    Hs = Hfull[np.ix_(sel, sel)]
    Hd = sum(two_local(p, i, j, m) for (i, j), p in zip(pairs, psis))
    return float(np.abs(Hs - Hd).max())


def gapof(H, rtol=1e-10):
    ev = np.linalg.eigvalsh((H + H.conj().T) / 2)
    nrm = ev[-1]
    k = int((ev < rtol * nrm).sum())
    return k, (ev[k] if k < len(ev) else float('nan')), nrm


def body(ck):
    # ---- (1) sector identity ---------------------------------------------
    ck.info("  === sector identity: polynomial-ring H vs direct qubit build ===")
    for m in (3, 4, 5):
        rng = np.random.default_rng(m)
        pairs = [(i, i + 1) for i in range(m - 1)]
        psis = [rng.normal(size=4) + 1j * rng.normal(size=4) for _ in pairs]
        err = verify_against_bf(m, pairs, psis)
        ck.info(f"    m={m}: max|H_sector - H_direct| = {err:.2e}")
        ck.atmost(err, SECTOR_TOL,
                  f"m={m}: multidegree-(1,..,1) sector identity (Sect. 3)")

    # ---- (2)(3)(4) singlet chain -----------------------------------------
    ck.info("\n  === (A) nearest-neighbour singlet projectors on m qubits ===")
    ck.info(f"    {'m':>3} {'dim':>6} {'kerdim':>7} {'m+1':>5} {'Delta':>12} "
            f"{'m^2 Delta':>11}")
    ms, gs, m2g = [], [], []
    for m in range(2, MMAX + 1):
        H = sum(two_local(SINGLET, i, i + 1, m) for i in range(m - 1))
        k, g, nrm = gapof(H)
        ms.append(m)
        gs.append(float(g))
        m2g.append(m * m * float(g))
        ck.info(f"    {m:>3} {2**m:>6} {k:>7} {m+1:>5} {g:>12.6g} "
                f"{m*m*g:>11.5g}")
        ck.equal(k, m + 1,
                 f"singlet chain m={m}: kernel dimension (spin-m/2 multiplet)")
        ck.atleast(float(g), 0.0, f"singlet chain m={m}: Delta > 0")
        ck.atmost(m * m * float(g), PI2 + 1e-9,
                  f"singlet chain m={m}: m^2 Delta below pi^2")
        if len(m2g) > 1:
            ck.atleast(m2g[-1] - m2g[-2], -1e-12,
                       f"singlet chain m={m}: m^2 Delta increasing in m")
    ck.close(m2g[-1], PI2, PI2_TOL,
             f"singlet chain: m^2 Delta at m={MMAX} vs pi^2 = {PI2:.4f}")

    A = np.vstack([np.log(ms[3:]), np.ones(len(ms) - 3)]).T
    c = np.linalg.lstsq(A, np.log(gs[3:]), rcond=None)[0]
    pre, exp_ = math.exp(c[1]), c[0]
    ck.info(f"    fit (m >= {ms[3]}): Delta ~ {pre:.4g} * m^({exp_:+.3f})   "
            f"[published: 9.13 m^-1.97]")
    ck.between(exp_, EXP_RANGE[0], EXP_RANGE[1],
               "singlet chain: fitted Delta exponent (published -1.97)")
    ck.between(pre, PRE_RANGE[0], PRE_RANGE[1],
               "singlet chain: fitted Delta prefactor (published 9.13)")

    # ---- (5) random frustration-free chain -------------------------------
    ck.info("\n  === (B) random frustration-free 2-local chain (one seed / m) ===")
    ck.info(f"    {'m':>3} {'kerdim':>7} {'Delta':>12} {'||H||':>10}")
    for m in range(2, MMAX + 1):
        rng = np.random.default_rng(1000 + m)
        phis = [rng.normal(size=2) + 1j * rng.normal(size=2) for _ in range(m)]
        phis = [p / np.linalg.norm(p) for p in phis]
        H = np.zeros((2**m, 2**m), dtype=complex)
        for i in range(m - 1):
            prod = np.kron(phis[i], phis[i + 1])
            w = rng.normal(size=4) + 1j * rng.normal(size=4)
            psi = w - prod * (np.vdot(prod, w) / np.vdot(prod, prod))
            H += two_local(psi / np.linalg.norm(psi), i, i + 1, m)
        k, g, nrm = gapof(H)
        ck.info(f"    {m:>3} {k:>7} {g:>12.6g} {nrm:>10.4g}")
        ck.equal(k, m + 1,
                 f"random FF chain m={m}: kernel dimension (frustration free)")
        ck.require(float(g) > 0.0, f"random FF chain m={m}: Delta > 0")


if __name__ == "__main__":
    checkharness.run(
        "task3b_hard",
        "report.md Sect. 3 multigraded sector identity (m = 3,4,5, machine "
        "precision) and Sect. 7 / Conj. 8.3(d) singlet-chain gap "
        f"Delta = 9.13 m^-1.97 with m^2 Delta -> pi^2, m <= {MMAX}",
        body)
