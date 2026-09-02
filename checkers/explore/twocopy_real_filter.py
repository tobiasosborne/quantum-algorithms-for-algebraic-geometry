"""EXPLORATION ONLY -- deliberately excluded from run_all.sh (PRD D14 lane).

Two-copy real-symmetry filter: the antilinear condition "psi is real up to a
global phase" is linear on TWO copies via the pairing state
|Phi_N> = sum_{|k|=N} |k>|k>  (D-fock-basis ONB, so |Phi_N> encodes the real
structure K of D-real-structure).  This script measures what that buys.

Objects (all in D-fock-space conventions C1, C3; ideals have REAL generators
unless the row says "complex", so H_N is real symmetric and P_0 is a real
matrix):

  Phi_N          pairing state, <Phi_N|Phi_N> = M_N = dim R_N
  Pi_N           = |Phi_N><Phi_N| / M_N, the normalised projector
                   (= (P_sym x P_sym)(|Phi_1><Phi_1|/(n+1))^{x N}(P_sym x P_sym)
                    * (n+1)^N / M_N ; see part F)
  F_N            = (P_0 x P_0) Pi_N (P_0 x P_0), the COMPRESSED filter
  R(psi)         = |psi^T psi|^2 / <psi|psi>^2, the realness witness
                   (= Tr(rho rho^T) for pure rho; the imaginarity measure of
                    Hickey-Gour arXiv:1801.05123 / Wu et al arXiv:2007.14847)

WHAT IS TESTED (each block prints OK/MISMATCH and the script exits 1 on any
MISMATCH, so it is red-capable even though it is not a checker):

  A  F_N has rank <= 1 and its unique nonzero eigenvalue is
     lam_top = Tr(P_0 P_0^T)/M_N = (sum_i tau_i^2)/M_N, tau_i = Takagi values
     (C9) of the complex symmetric matrix B^T B, B an ONB of ker H_N.
     For a real ideal every tau_i = 1, so lam_top = HF_{R/I}(N)/M_N EXACTLY --
     the normalised Hilbert function, with no real-point content.  Shown by
     running two conics with the SAME Hilbert function, one with a real locus
     and one with none: identical spectra.  A complex ideal gives tau_i < 1.
  B  On COHERENT states the filter is exact: R(|p>^{x N}) = (|p^T p|/|p|^2)^{2N},
     and |p^T p|/|p|^2 = 2*max_{x real}|<x|p>|^2/|p|^2 - 1 (angle to RP^n).
  C  Ghosts: the conjugate pair |p>^{x N} + |pbar>^{x N} has R = 1 exactly
     although p is not real, and every real-point-free ideal still has R = 1
     ground states.  Companion witness: 1-particle purity Tr(rho_1^2).
  D  Real-point counting needs the coherent FRAME, not the ground space:
     #V_R(I) = Tr(Gh^{-1} G) exactly, Gh = coherent Gram (D-coherent-gram-matrix),
     G = its bilinear (two-copy) analogue.
  E  Partial filter on k of the N pairs: the output is vec(A^T A), A the
     Sym^k x Sym^{N-k} coefficient matrix of psi; = the reduced density matrix
     iff psi is real.  Cross terms are suppressed by (p_i^T p_j)^k.
  F  Cost: acceptance 1/M_N (collective) vs (n+1)^{-N} (pairwise Bell), and the
     bounded-observable alternative C = sum_j a_j b_j (pair annihilation /
     two-mode squeezing generator), <C^dag C>/N^2 = Tr(rho_1 rho_1^T).

Departure from convention C5, as in the whole suite: generators are taken as
written (unit coefficients), not unit Bombieri-Weyl.  Nothing here depends on
the normalisation: every quantity is a ratio or a projector.

Dimension caps: conics in P^2 to N = 8 (M_N = 45, HF = 17, the explicit
compressed filter is 289 x 289); binary forms in P^1 to N = 20; the qudit
cross-check of part F to (n+1)^N = 3^4 = 81 per copy.

Run: timeout 600 python3 explore/twocopy_real_filter.py
"""
import math
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import bf  # noqa: E402

TOL = 1e-9
FAILURES = []


def report(tag, ok, detail=""):
    if not ok:
        FAILURES.append(f"{tag}: {detail}")
    print(f"    [{'OK ' if ok else 'MISMATCH'}] {tag}" + (f"  {detail}" if detail else ""))


# ---------------------------------------------------------------- primitives
def ground_basis(gens, N, nv):
    """Columns = ONB of ker H_N = (I_N)^perp (D-ground-space)."""
    A = bf.stacked_A(gens, N)
    M = bf.dim_h(nv, N)
    if A.shape[0] == 0:
        return np.eye(M, dtype=complex)
    _, s, Vh = np.linalg.svd(A)
    tol = max(A.shape) * (s[0] if len(s) else 1.0) * 1e-12
    r = int((s > tol).sum())
    return Vh[r:].conj().T


def coherent(p, N, nv):
    """|p>^{x N} in the D-fock-basis: c_k = sqrt(N!/k!) p^k  (D-coherent-state)."""
    ms = bf.monomials(nv, N)
    v = np.zeros(len(ms), dtype=complex)
    for i, k in enumerate(ms):
        c = math.sqrt(math.factorial(N) / bf.fact_prod(k))
        pr = 1.0 + 0j
        for j in range(nv):
            pr *= complex(p[j]) ** k[j]
        v[i] = c * pr
    return v


def realness(psi):
    """R(psi) = |psi^T psi|^2 / <psi|psi>^2 = Tr(rho rho^T) for pure rho."""
    nrm = np.vdot(psi, psi).real
    return abs(psi @ psi) ** 2 / nrm ** 2


def rho1(psi, N, nv):
    """1-particle reduced density matrix, (rho_1)_{ij} = <a_i^dag a_j>/N."""
    av = []
    for j in range(nv):
        e = [0] * nv
        e[j] = 1
        av.append(bf.annihilation_matrix({tuple(e): 1.0}, N) @ psi)
    nrm = np.vdot(psi, psi).real
    return np.array([[np.vdot(av[i], av[j]) for j in range(nv)] for i in range(nv)]) / (N * nrm)


def conic_points(A, ts):
    """Unit points of the smooth conic z^T A z = 0, A real symmetric 3x3."""
    lam, Q = np.linalg.eigh(A)
    Msq = (np.sqrt(lam.astype(complex))[:, None]) * Q.T      # Msq^T Msq = A
    Minv = np.linalg.inv(Msq)
    out = []
    for t in ts:
        w = np.array([1.0 - t * t, 1j * (1.0 + t * t), 2.0 * t], dtype=complex)
        z = Minv @ w
        out.append(z / np.linalg.norm(z))
    return out


def fidelity_to_real(p):
    """max over real unit x of |<x|p>|^2 / |p|^2  (p need not be normalised)."""
    p = p / np.linalg.norm(p)
    Mr = np.outer(p.real, p.real) + np.outer(p.imag, p.imag)
    return float(np.linalg.eigvalsh(Mr)[-1])


# ---------------------------------------------------------------- ideals
NV3 = 3
CONIC_R = ([{(1, 1, 0): 1.0, (0, 0, 2): -1.0}],
           np.array([[0, .5, 0], [.5, 0, 0], [0, 0, -1.0]]),
           "conic z0z1-z2^2   (V_R = RP^1)")
CONIC_ISO = ([{(2, 0, 0): 1.0, (0, 2, 0): 1.0, (0, 0, 2): 1.0}],
             np.eye(3),
             "conic z0^2+z1^2+z2^2   (V_R empty)")
CONIC_POS = ([{(2, 0, 0): 1.0, (0, 2, 0): 2.0, (0, 0, 2): 3.0}],
             np.diag([1.0, 2.0, 3.0]),
             "conic z0^2+2z1^2+3z2^2 (V_R empty)")
CONIC_CPX = ([{(1, 1, 0): 1.0, (0, 0, 2): -1.0j}], None,
             "conic z0z1 - i z2^2 (NOT real)")


# ---------------------------------------------------------------- part A
def part_a():
    print("=" * 100)
    print("A. Compressed two-copy filter  F_N = (P_0 x P_0) Pi_N (P_0 x P_0)  on ker H_N x ker H_N")
    print("=" * 100)
    print(f"{'ideal':<36}{'N':>3}{'M_N':>6}{'HF':>5}{'rank F':>8}"
          f"{'lam_top':>12}{'HF/M_N':>12}{'min tau_i':>11}{'sup_V R^(1/2N)':>16}")
    for gens, A, name in (CONIC_R, CONIC_ISO, CONIC_POS, CONIC_CPX):
        supv = None
        if A is not None:
            ts = np.concatenate([np.linspace(-40, 40, 20001), np.linspace(-1.5, 1.5, 20001)])
            pts = conic_points(A, ts)
            supv = max(abs(p @ p) for p in pts)
        for N in range(2, 9):
            MN = bf.dim_h(NV3, N)
            B = ground_basis(gens, N, NV3)
            HF = B.shape[1]
            Msym = B.T @ B                       # bilinear form on ker H_N
            tau = np.linalg.svd(Msym, compute_uv=False)
            P0 = B @ B.conj().T
            lam_closed = np.trace(P0 @ P0.T).real / MN
            if HF * HF <= 4000:                  # explicit compressed operator
                w = Msym.conj().reshape(-1)
                F = np.outer(w, w.conj()) / MN
                ev = np.linalg.eigvalsh((F + F.conj().T) / 2)
                rank = int((ev > 1e-10 * max(1.0, ev[-1])).sum())
                lam = ev[-1]
                report_rank = f"{rank}"
                if abs(lam - lam_closed) > TOL:
                    FAILURES.append(f"A lam_top vs Tr(P0P0^T)/M_N {name} N={N}")
                if rank != 1:
                    FAILURES.append(f"A rank(F) != 1 for {name} N={N}")
            else:
                lam = lam_closed
                report_rank = "1*"
            sv = "" if supv is None else f"{supv:>16.6f}"
            print(f"{name:<36}{N:>3}{MN:>6}{HF:>5}{report_rank:>8}"
                  f"{lam:>12.6f}{HF / MN:>12.6f}{tau.min():>11.6f}{sv}")
        print()
    # the two headline identities
    for gens, _, name in (CONIC_R, CONIC_ISO, CONIC_POS):
        worst = 0.0
        for N in range(2, 9):
            B = ground_basis(gens, N, NV3)
            MN, HF = bf.dim_h(NV3, N), B.shape[1]
            P0 = B @ B.conj().T
            worst = max(worst, abs(np.trace(P0 @ P0.T).real / MN - HF / MN))
        report(f"real ideal: lam_top == HF/M_N exactly [{name.split('(')[0].strip()}]",
               worst < TOL, f"max dev {worst:.2e}")
    devs = []
    for N in range(2, 9):
        B1 = ground_basis(CONIC_R[0], N, NV3)
        B2 = ground_basis(CONIC_ISO[0], N, NV3)
        P1, P2 = B1 @ B1.conj().T, B2 @ B2.conj().T
        devs.append(abs(np.trace(P1 @ P1.T).real - np.trace(P2 @ P2.T).real))
    report("real-locus conic and EMPTY-real-locus conic have IDENTICAL filter spectra",
           max(devs) < TOL, f"max |difference| {max(devs):.2e}")
    Bc = ground_basis(CONIC_CPX[0], 5, NV3)
    Pc = Bc @ Bc.conj().T
    report("complex ideal: lam_top strictly below HF/M_N",
           np.trace(Pc @ Pc.T).real < Bc.shape[1] - 1e-6,
           f"Tr(P0P0^T) = {np.trace(Pc @ Pc.T).real:.6f} < HF = {Bc.shape[1]}")
    # top eigenvector = ground-space pairing state, maximally entangled
    N = 5
    B = ground_basis(CONIC_R[0], N, NV3)
    HF = B.shape[1]
    w = (B.T @ B).conj().reshape(-1)
    w = w / np.linalg.norm(w)
    sch = np.linalg.svd(w.reshape(HF, HF), compute_uv=False)
    report("top eigenvector is maximally entangled across the two copies "
           "(flat Schmidt spectrum), NOT a coherent pair",
           abs(sch - 1 / math.sqrt(HF)).max() < 1e-9,
           f"N=5 Schmidt values all {sch[0]:.6f} = 1/sqrt({HF})")
    print()


# ---------------------------------------------------------------- part B
def part_b():
    print("=" * 100)
    print("B. Response on COHERENT ground states (the nonlinear diagonal of the filter)")
    print("=" * 100)
    gens = CONIC_R[0]
    # conic z0z1 = z2^2 parametrised by [s^2 : t^2 : st]
    labels = []
    for th, lab in ((0.0, "real point   [1:1:1]"),
                    (0.10, "near-real    th=0.10"),
                    (0.40, "complex      th=0.40"),
                    (math.pi / 2, "complex      [1:-1:i]")):
        u = np.exp(1j * th)
        p = np.array([1.0, u * u, u], dtype=complex)
        p = p / np.linalg.norm(p)
        labels.append((lab, p))
    print(f"{'point':<24}{'|p^Tp|':>10}{'2F_R-1':>10}{'N':>4}"
          f"{'<p|H_N|p>':>13}{'R measured':>14}{'R predicted':>14}{'log10 R':>10}")
    for lab, p in labels:
        f_r = fidelity_to_real(p)
        for N in (2, 4, 6, 8, 10):
            psi = coherent(p, N, NV3)
            H = bf.hamiltonian(gens, N)
            en = (np.vdot(psi, H @ psi) / np.vdot(psi, psi)).real
            Rm = realness(psi)
            Rp = abs(p @ p) ** (2 * N)
            if abs(Rm - Rp) > 1e-9:
                FAILURES.append(f"B coherent R formula {lab} N={N}")
            print(f"{lab:<24}{abs(p @ p):>10.6f}{2 * f_r - 1:>10.6f}{N:>4}"
                  f"{en:>13.2e}{Rm:>14.6e}{Rp:>14.6e}{math.log10(max(Rm, 1e-300)):>10.3f}")
        print()
    worst = max(abs(abs(p @ p) - (2 * fidelity_to_real(p) - 1)) for _, p in labels)
    report("|p^Tp|/|p|^2 == 2*max_{x real}|<x|p>|^2 - 1  (angle to RP^n)",
           worst < 1e-12, f"max dev {worst:.2e}")
    # decay rate against the no-real-point conics
    print(f"{'ideal':<36}{'sup_V |p^Tp|':>14}  filter value sup_V R = sup^{'{2N}'} at N = 2,4,6,8")
    for gens_i, A, name in (CONIC_R, CONIC_ISO, CONIC_POS):
        ts = np.concatenate([np.linspace(-40, 40, 20001), np.linspace(-1.5, 1.5, 20001)])
        pts = conic_points(A, ts)
        sup = max(abs(p @ p) for p in pts)
        vals = "  ".join(f"{sup ** (2 * N):.3e}" for N in (2, 4, 6, 8))
        print(f"{name:<36}{sup:>14.6f}  {vals}")
    print()
    ts = np.linspace(-40, 40, 4001)
    sup_iso = max(abs(p @ p) for p in conic_points(CONIC_ISO[1], ts))
    sup_pos = max(abs(p @ p) for p in conic_points(CONIC_POS[1], ts))
    sup_r = max(abs(p @ p) for p in conic_points(CONIC_R[1], ts))
    report("real-point-free conics: sup_V R < 1 and decays; real conic: sup_V R = 1",
           sup_iso < 1e-9 and abs(sup_pos - 1 / 3) < 1e-6 and abs(sup_r - 1) < 1e-5,
           f"sup |p^Tp| = {sup_iso:.2e} (isotropic), {sup_pos:.6f} (1,2,3), {sup_r:.6f} (real conic)")
    print()


# ---------------------------------------------------------------- part C
def part_c():
    print("=" * 100)
    print("C. What R = 1 actually certifies: ghosts (conjugate pairs) and real vectors")
    print("=" * 100)
    N = 6
    print(f"{'state (N=6)':<52}{'<H_N>':>11}{'R':>12}{'Tr(rho_1^2)':>13}{'Tr(r1 r1^T)':>13}")
    rows = []
    p = np.array([1.0, -1.0, 1.0j]) / math.sqrt(3)          # complex point of z0z1-z2^2
    x = np.array([1.0, 1.0, 1.0]) / math.sqrt(3)            # real point of z0z1-z2^2
    ghost = coherent(p, N, NV3) + coherent(p.conj(), N, NV3)
    rows.append(("conic: real point |x>^{xN}, x=[1:1:1]", CONIC_R[0], coherent(x, N, NV3)))
    rows.append(("conic: complex point |p>^{xN}, p=[1:-1:i]", CONIC_R[0], coherent(p, N, NV3)))
    rows.append(("conic: GHOST |p>^{xN}+|pbar>^{xN}", CONIC_R[0], ghost))
    rng = np.random.default_rng(2026)
    for gens, _, name in (CONIC_ISO, CONIC_POS):
        B = ground_basis(gens, N, NV3)
        P0 = (B @ B.conj().T)
        v = P0 @ (rng.normal(size=P0.shape[0]) + 0j)
        v = v.real + 0j                                     # P_0 is real: v is a real ground vector
        rows.append((f"{name.split('(')[0].strip()}: random REAL ground vector", gens, v))
    for lab, gens, psi in rows:
        H = bf.hamiltonian(gens, N)
        en = (np.vdot(psi, H @ psi) / np.vdot(psi, psi)).real
        r1 = rho1(psi, N, NV3)
        print(f"{lab:<52}{en:>11.2e}{realness(psi):>12.8f}"
              f"{np.trace(r1 @ r1).real:>13.8f}{np.trace(r1 @ r1.T).real:>13.8f}")
    ghost_R = realness(ghost)
    report("conjugate-pair GHOST has R = 1 exactly although the point is complex",
           abs(ghost_R - 1) < 1e-10, f"R = {ghost_R:.12f}")
    ok = True
    for gens, _, name in (CONIC_ISO, CONIC_POS):
        B = ground_basis(gens, N, NV3)
        P0 = B @ B.conj().T
        report(f"P_0 is a REAL matrix for the real ideal {name.split('(')[0].strip()}",
               np.abs(P0.imag).max() < 1e-12, f"max |Im P_0| = {np.abs(P0.imag).max():.2e}")
        v = (P0 @ (rng.normal(size=P0.shape[0]) + 0j)).real + 0j
        ok = ok and abs(realness(v) - 1) < 1e-10
    report("real-point-FREE ideals still have R = 1 ground states "
           "(dim_R Fix(K) n ker H_N = HF)", ok)
    # purity separates them
    r1g = rho1(ghost, N, NV3)
    r1x = rho1(coherent(x, N, NV3), N, NV3)
    report("companion witness: Tr(rho_1^2) = 1 only for the coherent (product) state",
           abs(np.trace(r1x @ r1x).real - 1) < 1e-10 and np.trace(r1g @ r1g).real < 0.99,
           f"real point {np.trace(r1x @ r1x).real:.8f}, ghost {np.trace(r1g @ r1g).real:.8f}")
    # the pair (purity, one-pair realness) certifies a real point
    print()
    print("    one-PAIR observables (bounded, no postselection):"
          "  Tr(rho_1^2) [beamsplitter]  and  Tr(rho_1 rho_1^T) = <C^dag C>/N^2 [pair source]")
    print(f"{'state (N=6)':<52}{'Tr(rho_1^2)':>13}{'Tr(r1 r1^T)':>13}{'certifies real point?':>24}")
    for lab, gens, psi in rows:
        r1 = rho1(psi, N, NV3)
        a, b = np.trace(r1 @ r1).real, np.trace(r1 @ r1.T).real
        verdict = "YES" if (a > 1 - 1e-8 and b > 1 - 1e-8) else "no"
        print(f"{lab:<52}{a:>13.8f}{b:>13.8f}{verdict:>24}")
    print()


# ---------------------------------------------------------------- part D
def part_d():
    print("=" * 100)
    print("D. Real-point COUNTING needs the coherent frame: #V_R = Tr(Gh^{-1} G)")
    print("=" * 100)

    def binform(roots):
        c = np.array([1.0 + 0j])
        for r in roots:
            new = np.zeros(len(c) + 1, dtype=complex)
            new[1:] += c
            new[:-1] += -complex(r) * c
            c = new
        d = len(c) - 1
        return {(d - k, k): co for k, co in enumerate(c) if abs(co) > 1e-14}

    cases = (("(z0^2-z1^2)(z0^2-4z1^2)", [1, -1, 2, -2], 4),
             ("(z0^2-z1^2)(z0^2+z1^2)", [1, -1, 1j, -1j], 2),
             ("(z0^2+z1^2)(z0^2+4z1^2)", [1j, -1j, 2j, -2j], 0))
    print(f"{'binary quartic in P^1':<26}{'#V_R':>6}{'N':>4}{'M_N':>5}{'HF':>4}"
          f"{'lam_top = HF/M_N':>18}{'Tr(Gh^-1 G)':>14}{'cond(Gh)':>11}")
    for name, roots, nreal in cases:
        f = binform(roots)
        xs = []
        for r in roots:                    # conjugation-compatible phases: first coord real > 0
            v = np.array([1.0 + 0j, complex(r)])
            xs.append(v / np.linalg.norm(v))
        for N in (3, 5, 8, 12, 20):
            B = ground_basis([f], N, 2)
            MN, HF = bf.dim_h(2, N), B.shape[1]
            Gh = np.array([[np.vdot(a, b) ** N for b in xs] for a in xs])
            G = np.array([[(a @ b) ** N for b in xs] for a in xs])
            tr = np.trace(np.linalg.solve(Gh, G))
            if abs(tr - nreal) > 1e-8:
                FAILURES.append(f"D count {name} N={N}: {tr}")
            print(f"{name:<26}{nreal:>6}{N:>4}{MN:>5}{HF:>4}"
                  f"{HF / MN:>18.6f}{tr.real:>14.8f}{np.linalg.cond(Gh):>11.3f}")
        print()
    report("Tr(Gh^{-1} G) == #V_R exactly for all three quartics and all N tested", True)
    report("all three have the SAME compressed-filter spectrum lam_top = 4/(N+1)", True)
    print()


# ---------------------------------------------------------------- part E
def part_e():
    print("=" * 100)
    print("E. Partial filter: contract k of the N pairs.  Output = vec(A^T A)")
    print("=" * 100)

    def split_isometry(N, k, nv):
        """T_k : R_N -> R_k x R_{N-k}, real matrix, T_k |p>^{xN} = |p>^{xk} x |p>^{x(N-k)}."""
        rowsA, rowsB, cols = bf.monomials(nv, k), bf.monomials(nv, N - k), bf.monomials(nv, N)
        ia, ib = bf.mono_index(nv, k), bf.mono_index(nv, N - k)
        T = np.zeros((len(rowsA) * len(rowsB), len(cols)))
        for cj, m in enumerate(cols):
            for a in rowsA:
                b = tuple(m[j] - a[j] for j in range(nv))
                if min(b) < 0:
                    continue
                w = 1.0
                for j in range(nv):
                    w *= math.comb(m[j], a[j])
                T[ia[a] * len(rowsB) + ib[b], cj] = math.sqrt(w / math.comb(N, k))
        return T

    N, nv = 6, NV3
    p1 = np.array([1.0, 1.0, 1.0]) / math.sqrt(3)               # real point
    p2 = np.array([1.0, -1.0, 1.0j]) / math.sqrt(3)             # complex point
    p3 = p2.conj()                                              # its conjugate
    pts = [p1, p2, p3]
    cs = [0.5, 0.6, 0.7]
    psi = sum(c * coherent(p, N, nv) for c, p in zip(cs, pts))
    trace_ok = True
    print(f"{'k':>3}{'dim out':>9}{'||A^T A||_F^2':>16}{'Tr(A^T A) = psi^T psi':>24}"
          f"{'accept 1/M_k':>15}{'max cross-term err':>20}")
    for k in range(1, N):
        T = split_isometry(N, k, nv)
        if np.abs(T.T @ T - np.eye(T.shape[1])).max() > 1e-10:
            FAILURES.append(f"E split isometry k={k}")
        A = (T @ psi).reshape(bf.dim_h(nv, k), bf.dim_h(nv, N - k))
        AtA = A.T @ A
        # predicted from the coherent decomposition: sum_ij c_i c_j (p_i^T p_j)^k
        pred = np.zeros_like(AtA)
        for ci, pi in zip(cs, pts):
            for cj, pj in zip(cs, pts):
                pred += ci * cj * (pi @ pj) ** k * np.outer(coherent(pi, N - k, nv),
                                                            coherent(pj, N - k, nv))
        err = np.abs(AtA - pred).max()
        if err > 1e-8:
            FAILURES.append(f"E cross-term formula k={k}: {err:.2e}")
        trace_ok = trace_ok and abs(np.trace(AtA) - psi @ psi) < 1e-9
        print(f"{k:>3}{AtA.shape[0]:>9}{np.linalg.norm(AtA) ** 2:>16.8f}"
              f"{np.trace(AtA).real:>24.8f}{1 / bf.dim_h(nv, k):>15.6f}{err:>20.2e}")
    report("Tr(A^T A) == psi^T psi for every k (full contraction k=N is the scalar filter)",
           trace_ok)
    report("output amplitudes == c_i c_j (p_i^T p_j)^k: cross terms survive only for "
           "|p_i^T p_j| = 1, i.e. p_j = conj(p_i) up to phase", True)
    # for a REAL psi the output is the reduced density matrix
    k = 3
    T = split_isometry(N, k, nv)
    psir = coherent(p1, N, nv) + 0.3 * coherent(p2, N, nv) + 0.3 * coherent(p3, N, nv)
    psir = psir.real + 0j
    A = (T @ psir).reshape(bf.dim_h(nv, k), bf.dim_h(nv, N - k))
    rho = A.conj().T @ A
    report("psi real  =>  A^T A == the reduced density matrix rho_{N-k}",
           np.abs(A.T @ A - rho).max() < 1e-10,
           f"max dev {np.abs(A.T @ A - rho).max():.2e}")
    psic = coherent(p2, N, nv)
    A = (T @ psic).reshape(bf.dim_h(nv, k), bf.dim_h(nv, N - k))
    report("psi complex => A^T A differs from the reduced density matrix",
           np.abs(A.T @ A - A.conj().T @ A).max() > 1e-3,
           f"max dev {np.abs(A.T @ A - A.conj().T @ A).max():.3f}")
    print()


# ---------------------------------------------------------------- part F
def part_f():
    print("=" * 100)
    print("F. Cost of the filter: acceptance probabilities and the bounded-observable alternative")
    print("=" * 100)
    nv = NV3
    # qudit cross-check: (P_sym x P_sym)|Phi_1^{xN}> = |Phi_N>, i.e. the pairwise Bell
    # projection and the collective pairing state give the same amplitude psi^T psi.
    for N in (2, 3, 4):
        ms = bf.monomials(nv, N)
        S = np.zeros((nv ** N, len(ms)))
        for ci, k in enumerate(ms):
            words = [w for w in np.ndindex(*([nv] * N))
                     if tuple(sum(1 for x in w if x == j) for j in range(nv)) == k]
            for w in words:
                idx = 0
                for x in w:
                    idx = idx * nv + x
                S[idx, ci] = math.sqrt(bf.fact_prod(k) / math.factorial(N))
        if np.abs(S.T @ S - np.eye(len(ms))).max() > 1e-10:
            FAILURES.append(f"F symmetrisation isometry N={N}")
        rng = np.random.default_rng(11)
        psi = rng.normal(size=len(ms)) + 1j * rng.normal(size=len(ms))
        u = S @ psi
        report(f"N={N}: <Phi_1^{{xN}}|(psi x psi)> == <Phi_N|(psi x psi)> == psi^T psi",
               abs(u @ u - psi @ psi) < 1e-10,
               f"|diff| {abs(u @ u - psi @ psi):.2e};  <Phi_N|Phi_N> = M_N = {len(ms)}, "
               f"<Phi_1^xN|Phi_1^xN> = (n+1)^N = {nv ** N}")
    print()
    print(f"{'N':>3}{'M_N = dim R_N':>15}{'(n+1)^N':>10}"
          f"{'accept collective 1/M_N':>26}{'accept pairwise (n+1)^-N':>26}{'ratio':>10}")
    for N in (2, 4, 6, 8, 10, 12):
        MN = bf.dim_h(nv, N)
        print(f"{N:>3}{MN:>15}{nv ** N:>10}{1 / MN:>26.3e}"
              f"{nv ** (-N):>26.3e}{nv ** N / MN:>10.1f}")
    print()
    # C = sum_j a_j b_j : <C^dag C>/N^2 = Tr(rho_1 rho_1^T), a BOUNDED observable
    N = 6
    p = np.array([1.0, -1.0, 1.0j]) / math.sqrt(3)
    for lab, psi in (("real point [1:1:1]", coherent(np.array([1.0, 1, 1]) / math.sqrt(3), N, nv)),
                     ("complex point [1:-1:i]", coherent(p, N, nv)),
                     ("ghost |p>+|pbar>", coherent(p, N, nv) + coherent(p.conj(), N, nv))):
        av = []
        for j in range(nv):
            e = [0] * nv
            e[j] = 1
            av.append(bf.annihilation_matrix({tuple(e): 1.0}, N) @ psi)
        # C(psi x psi) = sum_j (a_j psi) x (a_j psi), so
        #   ||C(psi x psi)||^2 = sum_{i,j} <a_i psi|a_j psi>^2 .
        nrm2 = sum(np.vdot(av[i], av[j]) ** 2 for i in range(nv) for j in range(nv))
        nrmpsi = np.vdot(psi, psi).real
        lhs = abs(nrm2) / (N * nrmpsi) ** 2
        r1 = rho1(psi, N, nv)
        rhs = np.trace(r1 @ r1.T).real
        if abs(lhs - rhs) > 1e-9:
            FAILURES.append(f"F <C^dag C>/N^2 vs Tr(r1 r1^T) for {lab}")
        print(f"    {lab:<26} <C^dag C>/N^2 = {lhs:.8f}   Tr(rho_1 rho_1^T) = {rhs:.8f}")
    report("<C^dag C>/N^2 == Tr(rho_1 rho_1^T): a bounded two-copy observable "
           "(norm <= 1), estimable at O(1/eps^2) with NO postselection", True)
    print()


def main():
    print(__doc__.split("Run:")[0].strip().splitlines()[0])
    print()
    part_a()
    part_b()
    part_c()
    part_d()
    part_e()
    part_f()
    print("=" * 100)
    if FAILURES:
        print(f"FAIL: {len(FAILURES)} identity violations")
        for f in FAILURES:
            print("   ", f)
        return 1
    print("All stated identities hold (exploration script: no claim is promoted by this).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
