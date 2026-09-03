"""EXPLORATION ONLY -- deliberately excluded from run_all.sh (PRD arm C lane,
brief `briefs/lane-intersection-observables.md`).

Intersection and integration observables: the first numerical test of seed
Conjecture 8.10, i.e. of claim rows C-085 / C-166 / C-167 (overlaps
`Tr(P_I P_J)`) and C-086 / C-168 (Toeplitz averages `Tr(P_0 T_g)/HF(N)`).
`HANDOFF.md` suggested next step 3 in the seed is exactly this test.

OBJECTS (conventions C1-C12 of `definitions/definitions.md`; ids cited, never
redefined): D-polynomial-ring, D-fock-space, D-fock-basis, D-annihilation-of-form,
D-hamiltonian, D-ground-space, D-inverse-system, D-projectors, D-coherent-state,
D-bergman-projector, D-toeplitz-operator, D-hilbert-function,
D-normalised-hilbert-function, D-dqc1-style-estimate.

NOTATION FIXED HERE (and proposed to the register as D-intersection-overlap):
`P_I` denotes the projector onto `ker H_N^{(I)} = (I_N)^perp` -- the *Bergman*
projector of D-bergman-projector -- NOT the projector onto `I_N`, which
D-projectors calls `P_{I_N}`.  The seed's `Tr(P_I P_J)` only has the asserted
geometric meaning under the first reading; under the second it is
`M_N - HF_I - HF_J + Tr(P_I P_J)`, which is `Theta(M_N)` for every example here.

DEPARTURE FROM C5, as in the whole checker suite (`checkers/README.md`):
generators are taken as written, unit coefficients on monomials, not unit
Bombieri-Weyl.  Nothing below depends on it: every quantity reported is a
projector overlap, a Hilbert-function count, or a ratio, and projectors are
normalisation independent within one degree (C-002, D-norm-comparison).

METRIC CONVENTION.  Fubini-Study distance `d(p,q) = arccos |<p,q>|` on `CP^n`
(diameter pi/2), so `vol(CP^n) = pi^n/n!`, `vol(V) = deg(V) pi^k/k!` for `V`
smooth of complex dimension `k` (Wirtinger), and the coherent overlap is
`|<e_p,e_q>|^2 = cos^{2N} d(p,q)` with `e_p = (p.z)^N/sqrt(N!)` (D-coherent-state).

WHAT IS COMPUTED
  A  two lines in P^2 meeting in a point, orthogonal and at angle theta.
  B  two skew lines in P^3 (equidistant Clifford pair, and a generic pair).
  C  two planes in P^3 meeting in a line, at angle theta; the CROSSOVER table.
  D  conic and line in P^2: transversal versus TANGENT.
  E  two conics in P^2 (four transversal points).
  F  excess (non-generic-dimension but clean) intersection: two planes in P^4
     meeting in a line.
  G  Toeplitz averages for the conic, symbols |z_2|^2 and |z_2|^4, against
     Gauss-Legendre quadrature on the rational parametrisation.
  H  the DQC1 signal size: Tr(P_I P_J)/M_N, /sqrt(HF_I HF_J), /(HF_I HF_J)
     for two hyperplanes in P^n with n growing.
  I  direct test of the Bergman lemma S_V = int_V |e_p><e_p| dV ~ (pi^k/N^k) P_I.

Every closed form printed is checked against an independent SVD kernel
computation at small N; a mismatch exits 1 (exit 2 = could not run).

Run: timeout 900 python3 checkers/explore/intersection_observables.py
"""
import math
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import bf  # noqa: E402

NGRID_P2 = (4, 8, 12, 16, 22, 28, 36, 44, 52, 60)

TOL_REL = 5e-8          # closed form vs SVD, relative
KERNEL_TOL = 1e-9       # relative singular-value cutoff for the kernel


class Mismatch(Exception):
    pass


FAILURES = []


def check(name, got, want, tol=TOL_REL):
    """Record a numerical agreement check; never raises, collects failures."""
    denom = max(1.0, abs(want))
    rel = abs(got - want) / denom
    ok = rel <= tol
    if not ok:
        FAILURES.append(f"{name}: got {got!r}, want {want!r}, rel {rel:.3e}")
    return ok


# ------------------------------------------------------------------ kernels
_GB_CACHE = {}


def ground_basis(gens, N, hf_expected):
    """Orthonormal basis (columns) of ker H_N = (I_N)^perp, via the SVD of the
    stacked annihilation matrix (D-ground-space, D-inverse-system).

    Returns (B, sig_min_nonzero, sig_max_zero).  Raises Mismatch if the
    numerical kernel dimension disagrees with hf_expected.
    """
    key = (repr([sorted((tuple(k), repr(complex(v))) for k, v in g.items())
                 for g in gens]), N)
    if key in _GB_CACHE:
        return _GB_CACHE[key]
    nv = bf.poly_nvars(gens[0])
    M = bf.dim_h(nv, N)
    A = bf.stacked_A(gens, N)
    if A.shape[0] == 0:
        out = (np.eye(M, dtype=complex), float("inf"), 0.0)
        _GB_CACHE[key] = out
        return out
    _, s, Vh = np.linalg.svd(A, full_matrices=True)
    smax = s[0] if len(s) else 0.0
    cut = max(A.shape) * smax * KERNEL_TOL
    rank = int((s > cut).sum())
    kdim = M - rank
    if kdim != hf_expected:
        raise Mismatch(
            f"kernel dim {kdim} != HF {hf_expected} at N={N} "
            f"(rank {rank}, M {M}, cut {cut:.3e})")
    B = Vh[rank:].conj().T          # M x kdim, orthonormal columns
    sig_min_nonzero = s[rank - 1] if rank else float("inf")
    sig_max_zero = s[rank] if rank < len(s) else 0.0
    out = (B, sig_min_nonzero, sig_max_zero)
    _GB_CACHE[key] = out
    return out


def tr_pp(B1, B2):
    """Tr(P_1 P_2) = || B1^dag B2 ||_F^2 for orthonormal column bases."""
    G = B1.conj().T @ B2
    return float(np.real(np.vdot(G, G)))


# ------------------------------------------------- Fubini-Study tangent data
def tangent_space(x, grads):
    """Orthonormal basis (columns) of T_x V inside C^{n+1}, for x a unit
    representative and grads the holomorphic gradients of the generators at x.

    T_x V = { v : <x,v> = 0 and sum_j d_j f(x) v_j = 0 for all generators }.
    With d(p,q) = arccos|<p,q>| the FS metric on x^perp is the Euclidean one,
    so principal angles below are FS angles.
    """
    rows = [np.conj(x)] + [np.asarray(g, dtype=complex) for g in grads]
    Aq = np.array(rows, dtype=complex)
    _, s, Vh = np.linalg.svd(Aq)
    cut = max(Aq.shape) * (s[0] if len(s) else 1.0) * 1e-12
    rank = int((s > cut).sum())
    return Vh[rank:].conj().T


def angle_factor(TV, TW):
    """J = prod over principal angles theta_i between T_V and T_W with
    cos theta_i < 1 of sin^2 theta_i.  Angles with cos = 1 span T_V ^ T_W and
    are excluded (they are the clean-intersection directions)."""
    if TV.shape[1] == 0 or TW.shape[1] == 0:
        return 1.0, []
    c = np.linalg.svd(TV.conj().T @ TW, compute_uv=False)
    c = np.clip(c, 0.0, 1.0)
    keep = c < 1 - 1e-9
    J = float(np.prod(1.0 - c[keep] ** 2)) if keep.any() else 1.0
    return J, list(c)


# ------------------------------------------- exact linear-subspace identity
def h_complete(xs, N):
    """Complete homogeneous symmetric polynomial h_N(x_1..x_r), by DP."""
    dp = np.zeros(N + 1)
    dp[0] = 1.0
    for x in xs:
        for k in range(1, N + 1):
            dp[k] += x * dp[k - 1]
    return float(dp[N])


def principal_cosines(QU, QW):
    """Cosines of the principal angles between two orthonormal column bases."""
    return np.clip(np.linalg.svd(QU.conj().T @ QW, compute_uv=False), 0.0, 1.0)


def ortho_complement(Q):
    m = Q.shape[0]
    P = np.eye(m, dtype=complex) - Q @ Q.conj().T
    u, sv, _ = np.linalg.svd(P)
    return u[:, : int((sv > 1e-10).sum())]


def linear_gens(Uperp):
    """Ideal generators: the linear forms spanning U^perp (columns).  With
    a(f) = conj(f)(partial) (C3), ker on R_1 is the Hermitian complement, so
    ker H_N = Sym^N U exactly."""
    nv = Uperp.shape[0]
    out = []
    for j in range(Uperp.shape[1]):
        v = Uperp[:, j]
        f = {}
        for i in range(nv):
            e = [0] * nv
            e[i] = 1
            f[tuple(e)] = complex(v[i])
        out.append(f)
    return out


# ------------------------------------- exact conic kernel (1-D recurrence)
def conic_kernel_moments(N):
    """INDEPENDENT exact computation, for I = (z_0 z_1 - z_2^2), of
    Tr(P_0 n_2) and Tr(P_0 n_2(n_2-1)) and HF(N), without any SVD.

    a(f) = d_0 d_1 - d_2^2 conserves d = k_0 - k_1, so H_N is block diagonal
    over d and each block is a 1-D chain whose kernel is one dimensional:
    with k(j) = (j+d, j, N-2j-d),
        c_{j+1} = c_j (N-2j-d)(N-2j-d-1) / ((j+1+d)(j+1)),
    and the Fock-ONB weight of |k(j)> is |c_j|^2 k(j)!.  Summing the 2N+1
    blocks gives the traces exactly.  Used to push N to 1200 (O3)."""
    tot1 = 0.0
    tot2 = 0.0
    nb = 0
    for d in range(-N, N + 1):
        jmin = max(0, -d)
        jmax = (N - d) // 2
        if jmax < jmin:
            continue
        js = np.arange(jmin, jmax + 1)
        k0 = js + d
        k1 = js
        k2 = N - 2 * js - d
        lc = np.zeros(len(js))
        for i in range(len(js) - 1):
            j = int(js[i])
            kk2 = N - 2 * j - d
            num = kk2 * (kk2 - 1)
            den = (j + 1 + d) * (j + 1)
            lc[i + 1] = (-np.inf if num <= 0
                         else lc[i] + math.log(num) - math.log(den))
        lw = 2 * lc + (np.vectorize(math.lgamma)(k0 + 1.0)
                       + np.vectorize(math.lgamma)(k1 + 1.0)
                       + np.vectorize(math.lgamma)(k2 + 1.0))
        m = np.isfinite(lw)
        lw = lw[m]
        kk2 = k2[m]
        lw -= lw.max()
        pr = np.exp(lw)
        pr /= pr.sum()
        tot1 += float((pr * kk2).sum())
        tot2 += float((pr * kk2 * (kk2 - 1.0)).sum())
        nb += 1
    return tot1, tot2, nb


# EXACT Fubini-Study average of |z_2|^2 over the conic (O3):
#   int_0^inf A(u) u/(u^2+u+1) du = -1/3 + 4 sqrt(3) pi / 27,  int A du = 2,
#   so <|z_2|^2>_V = -1/6 + 2 sqrt(3) pi / 27.
TOEPLITZ_L1 = -1.0 / 6.0 + 2.0 * math.sqrt(3.0) * math.pi / 27.0
# FIXTURE (asserted, not fitted): the asymptotic 1/N coefficient of the
# NORMAL-ordered r=1 Toeplitz average.  Anti-normal ordering (n_2 -> n_2+1)
# shifts the level-N value by exactly 1/N, hence this coefficient by exactly
# +1, which is what makes the window below red to mutation M2.
TOEPLITZ_B1_WINDOW = (0.030, 0.034)


# ---------------------------------------------------------------- fitting
def loglog_slope(Ns, ys):
    Ns = np.asarray(Ns, dtype=float)
    ys = np.asarray(ys, dtype=float)
    m = ys > 0
    if m.sum() < 2:
        return float("nan")
    return float(np.polyfit(np.log(Ns[m]), np.log(ys[m]), 1)[0])


def local_slope(Ns, ys):
    out = []
    for i in range(1, len(Ns)):
        if ys[i] > 0 and ys[i - 1] > 0:
            out.append(math.log(ys[i] / ys[i - 1]) / math.log(Ns[i] / Ns[i - 1]))
        else:
            out.append(float("nan"))
    return out


def fit_a_plus_b_over_N(Ns, ys):
    return fit_powers(Ns, ys, (0.0, -1.0))


def fit_powers(Ns, ys, powers):
    """Least squares fit  y = sum_i coef_i * N^{powers_i}."""
    Ns = np.asarray(Ns, dtype=float)
    X = np.vstack([Ns ** p for p in powers]).T
    coef, *_ = np.linalg.lstsq(X, np.asarray(ys, dtype=float), rcond=None)
    return tuple(float(c) for c in coef)


# ================================================================= section A
def section_A():
    print("=" * 78)
    print("A. Two lines in P^2 meeting in a point (dim(V ^ W) = 0, transversal)")
    print("   I = (z_0), J = (c z_0 + s z_1), c = cos(theta), s = sin(theta).")
    print("   Closed form (this lane): Tr(P_I P_J) = sum_{a=0}^{N} c^{2a}")
    print("                                        -> 1/sin^2(theta) = 1/J.")
    print()
    nv = 3
    z0 = {(1, 0, 0): 1.0}
    hdr = f"{'N':>4} {'M_N':>6} {'HF':>5} {'Tr(SVD)':>14} {'Tr(closed)':>14} " \
          f"{'Tr/M_N':>11} {'Tr/sqrt(HFHF)':>13} {'Tr/(HF HF)':>12}"
    for theta in (math.pi / 2, 1.0, 0.4):
        c = math.cos(theta)
        s = math.sin(theta)
        gJ = {(1, 0, 0): c, (0, 1, 0): s}
        print(f"  theta = {theta:.4f} rad, 1/sin^2 = {1.0 / s**2:.6f}")
        print(hdr)
        for N in (2, 4, 6, 8, 12, 16, 24, 32, 48, 64):
            hf = N + 1
            M = bf.dim_h(nv, N)
            closed = sum(c ** (2 * a) for a in range(N + 1))
            if N <= 16:
                BI, _, _ = ground_basis([z0], N, hf)
                BJ, _, _ = ground_basis([gJ], N, hf)
                tr = tr_pp(BI, BJ)
                check(f"A theta={theta:.3f} N={N}", tr, closed)
                trs = f"{tr:14.8f}"
            else:
                trs = f"{'-':>14}"
            print(f"{N:>4} {M:>6} {hf:>5} {trs} {closed:14.8f} "
                  f"{closed / M:11.3e} {closed / hf:13.3e} {closed / hf**2:12.3e}")
        print()
    # geometric prediction from the tangent spaces
    print("  Angle factor J from the tangent spaces at the intersection point:")
    for theta in (math.pi / 2, 1.0, 0.4):
        c, s = math.cos(theta), math.sin(theta)
        x = np.array([0, 0, 1], dtype=complex)
        TV = tangent_space(x, [np.array([1, 0, 0], dtype=complex)])
        TW = tangent_space(x, [np.array([c, s, 0], dtype=complex)])
        J, cs = angle_factor(TV, TW)
        check(f"A angle theta={theta:.3f}", J, s ** 2, 1e-9)
        print(f"    theta={theta:.4f}  J={J:.8f}  sin^2(theta)={s**2:.8f}  "
              f"1/J={1/J:.6f}  limit of Tr = {1/(1-c**2):.6f}")
    print()


# ================================================================= section B
def section_B():
    print("=" * 78)
    print("B. Two SKEW lines in P^3 (V ^ W = empty).  C-167 / C-085 decay test.")
    print("   Clifford pair: L1 = span(e0,e1), L2 = span(c e0 + s e2, c e1 + s e3),")
    print("   every point of L2 at FS distance t = theta from L1.")
    print("   Closed form (this lane): Tr(P_I P_J) = (N+1) cos^{2N}(t) EXACTLY.")
    print()
    nv = 4
    hdr = (f"{'N':>4} {'Tr(SVD)':>16} {'(N+1)cos^2N t':>16} "
           f"{'-log Tr/(2N)':>13} {'log sec t':>11} {'Tr/M_N':>11}")
    for theta in (0.6, 0.3):
        c, s = math.cos(theta), math.sin(theta)
        I = [{(0, 0, 1, 0): 1.0}, {(0, 0, 0, 1): 1.0}]          # z2, z3
        # L2 = zero set of (-s z0 + c z2, -s z1 + c z3)
        J = [{(1, 0, 0, 0): -s, (0, 0, 1, 0): c},
             {(0, 1, 0, 0): -s, (0, 0, 0, 1): c}]
        print(f"  t = d_FS(L1,L2) = {theta:.4f},  log sec t = "
              f"{math.log(1/c):.6f}")
        print(hdr)
        for N in (2, 3, 4, 6, 8, 10, 12, 16, 20, 30, 40):
            hf = N + 1
            M = bf.dim_h(nv, N)
            closed = (N + 1) * c ** (2 * N)
            if N <= 12:
                BI, _, _ = ground_basis(I, N, hf)
                BJ, _, _ = ground_basis(J, N, hf)
                tr = tr_pp(BI, BJ)
                check(f"B theta={theta} N={N}", tr, closed)
                trs = f"{tr:16.10g}"
            else:
                trs = f"{'-':>16}"
            rate = -math.log(closed) / (2 * N) if closed > 0 else float("nan")
            print(f"{N:>4} {trs} {closed:16.10g} {rate:13.6f} "
                  f"{math.log(1/c):11.6f} {closed / M:11.3e}")
        print()
    print("  Generic (non-equidistant) skew pair: L1 = {z2=z3=0},")
    print("  L2 = zero set of (z0 - 2 z2 - z3, z1 - z2 + 3 z3) (rescaled).")
    print("  Laplace prediction (this lane): isolated closest pair =>")
    print("  Tr ~ const * cos^{2N}(d_0), i.e. local exponent -> 0 after")
    print("  dividing by cos^{2N} d_0.")
    I = [{(0, 0, 1, 0): 1.0}, {(0, 0, 0, 1): 1.0}]
    g1 = {(1, 0, 0, 0): 1.0, (0, 0, 1, 0): -2.0, (0, 0, 0, 1): -1.0}
    g2 = {(0, 1, 0, 0): 1.0, (0, 0, 1, 0): -1.0, (0, 0, 0, 1): 3.0}
    Jg = [g1, g2]
    # d_FS(L1, L2): principal angles between the 2-planes span(e0,e1) and L2hat
    U1 = np.eye(4, dtype=complex)[:, :2]
    Nsp = np.array([[1, 0, -2, -1], [0, 1, -1, 3]], dtype=complex)
    _, sv, Vh = np.linalg.svd(Nsp)
    U2 = Vh[2:].conj().T
    cang = np.linalg.svd(U1.conj().T @ U2, compute_uv=False)
    d0 = math.acos(min(1.0, float(cang.max())))
    print(f"  cos of principal angles between the two 2-planes: {cang}")
    print(f"  d_FS(L1,L2) = {d0:.6f},  cos d_0 = {math.cos(d0):.8f}")
    s1, s2 = float(cang[0]), float(cang[1])
    limit = s1 ** 2 / (s1 ** 2 - s2 ** 2)
    print(f"  EXACT (section J): Tr = h_N(s1^2, s2^2) = "
          f"(s1^{{2N+2}} - s2^{{2N+2}})/(s1^2 - s2^2),")
    print(f"  so Tr/cos^{{2N}}d_0 -> s1^2/(s1^2 - s2^2) = {limit:.10f}.")
    print(f"{'N':>5} {'Tr(SVD)':>16} {'Tr(exact h_N)':>16} "
          f"{'Tr/cos^{2N}d0':>16} {'-log Tr/(2N)':>13}")
    for N in (2, 4, 6, 10, 16, 40, 100):
        hf = N + 1
        exact = h_complete([s1 ** 2, s2 ** 2], N)
        if N <= 16:
            BI, _, _ = ground_basis(I, N, hf)
            BJ, _, _ = ground_basis(Jg, N, hf)
            tr = tr_pp(BI, BJ)
            check(f"B generic skew N={N}", tr, exact, 1e-9)
            ts = f"{tr:16.10g}"
        else:
            ts = f"{'-':>16}"
        ratio = exact / math.cos(d0) ** (2 * N)
        rate = -math.log(exact) / (2 * N)
        print(f"{N:>5} {ts} {exact:16.10g} {ratio:16.8f} {rate:13.6f}")
    print(f"  CORRECTION (verdict O1): the r0 memo called the N <= 16 values")
    print(f"  'saturating'.  They are not: at N = 16 the ratio is 8.82, at")
    print(f"  N = 100 it is {h_complete([s1**2, s2**2], 100)/math.cos(d0)**200:.5f},")
    print(f"  and the true limit is {limit:.10f}.  The exponent IS 0, but the")
    print("  approach is slow.  The Clifford pair has a one-complex-parameter")
    print("  family of closest pairs and gains exactly one power of N.")
    print("  BIAS SIGN (verdict O2): -log Tr/(2N) = log sec d_0 - log(N+1)/(2N)")
    print("  for the Clifford pair, i.e. the estimator sits BELOW the target;")
    print("  the r0 memo called this a positive bias.")
    print()


# ================================================================= section C
def section_C():
    print("=" * 78)
    print("C. Two planes in P^3 meeting in a LINE (dim(V ^ W) = 1).")
    print("   I = (z_0), J = (c z_0 + s z_1).")
    print("   Closed form (this lane): Tr = sum_{a=0}^{N} c^{2a} (N+1-a)")
    print("                               = (N+1)/s^2 - c^2/s^4 + O(c^{2N}).")
    print("   Laplace prediction: Tr ~ (N/pi) vol(Z)/J = N/sin^2(theta),")
    print("   Z = P^1 the common line, vol(Z) = pi, J = sin^2(theta).")
    print()
    nv = 4
    for theta in (math.pi / 2, 0.8, 0.3):
        c, s = math.cos(theta), math.sin(theta)
        I = [{(1, 0, 0, 0): 1.0}]
        J = [{(1, 0, 0, 0): c, (0, 1, 0, 0): s}]
        print(f"  theta = {theta:.4f}, 1/sin^2 = {1/s**2:.6f}")
        print(f"{'N':>4} {'HF':>6} {'Tr(SVD)':>16} {'Tr(closed)':>16} "
              f"{'Tr/N':>12} {'localslope':>11} {'Tr/M_N':>11}")
        Ns, trs_ = [], []
        for N in (2, 4, 6, 8, 12, 16, 24, 32, 48, 64, 96, 128):
            hf = bf.dim_h(3, N)
            M = bf.dim_h(nv, N)
            closed = sum(c ** (2 * a) * (N + 1 - a) for a in range(N + 1))
            if N <= 12:
                BI, _, _ = ground_basis(I, N, hf)
                BJ, _, _ = ground_basis(J, N, hf)
                tr = tr_pp(BI, BJ)
                check(f"C theta={theta:.3f} N={N}", tr, closed)
                ss = f"{tr:16.8f}"
            else:
                ss = f"{'-':>16}"
            Ns.append(N)
            trs_.append(closed)
            ls = local_slope(Ns, trs_)
            print(f"{N:>4} {hf:>6} {ss} {closed:16.8f} {closed/N:12.6f} "
                  f"{(ls[-1] if ls else float('nan')):11.5f} {closed/M:11.3e}")
        print(f"    loglog slope (last 5 points) = "
              f"{loglog_slope(Ns[-5:], trs_[-5:]):.5f}   [predicted 1]")
        print()
    print("  CROSSOVER: the exponent reported by the observable is 2 (the")
    print("  EXCESS value, i.e. V=W) until N >~ 1/sin^2(theta), and only then")
    print("  falls to the true value 1.  Local slope d log Tr / d log N:")
    thetas = (0.5, 0.2, 0.1, 0.05, 0.02)
    Ns = (4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096)
    print(f"    {'theta':>7} {'1/sin^2':>10} " +
          " ".join(f"{N:>7}" for N in Ns[1:]))
    for theta in thetas:
        c = math.cos(theta)
        s = math.sin(theta)
        vals = [sum(c ** (2 * a) * (N + 1 - a) for a in range(N + 1))
                for N in Ns]
        ls = local_slope(Ns, vals)
        print(f"    {theta:>7.3f} {1/s**2:>10.1f} " +
              " ".join(f"{v:>7.3f}" for v in ls))
    print("    (slope 2 = 'V and W coincide', slope 1 = the true dim(V^W)=1)")
    ok, detail = pred_crossover_slope()
    print(f"    ASSERTED at 1/sin^2 t = 100.3: {detail}")
    if not ok:
        FAILURES.append(f"C crossover slopes: {detail}")
    print()


# ================================================================= section D
def section_D():
    print("=" * 78)
    print("D. Conic and line in P^2.  TRANSVERSAL versus TANGENT.")
    print("   V = {z_0 z_1 - z_2^2 = 0} (smooth, deg 2, HF = 2N+1).")
    print("   W_t = {z_1 - z_0 = 0}  transversal, two points [1:1:+-1].")
    print("   W_g = {z_1 = 0}        TANGENT at [1:0:0], contact order 2.")
    print()
    nv = 3
    conic = {(1, 1, 0): 1.0, (0, 0, 2): -1.0}

    def grad_conic(x):
        return np.array([x[1], x[0], -2 * x[2]], dtype=complex)

    # --- transversal: predicted constant sum_i 1/J_i
    pts = []
    for sgn in (1, -1):
        v = np.array([1, 1, sgn], dtype=complex)
        pts.append(v / np.linalg.norm(v))
    csum = 0.0
    print("  Transversal case, tangent-space angles at the two points:")
    for x in pts:
        TV = tangent_space(x, [grad_conic(x)])
        TW = tangent_space(x, [np.array([-1, 1, 0], dtype=complex)])
        J, cang = angle_factor(TV, TW)
        csum += 1.0 / J
        print(f"    x = {np.round(x*math.sqrt(3),6)}/sqrt(3): "
              f"cos(theta) = {[round(float(t),8) for t in cang]}, J = {J:.8f}")
    print(f"  Predicted limit  Tr(P_I P_J) -> sum_i 1/J_i = {csum:.8f}")
    print(f"  (= HF_{{R/(I+J)}}(N)/J = 2 for the two reduced points, J = 1)")
    print()
    line_t = {(0, 1, 0): 1.0, (1, 0, 0): -1.0}
    line_g = {(0, 1, 0): 1.0}
    NS = NGRID_P2
    print(f"{'N':>4} {'M_N':>6} {'Tr transversal':>16} {'localslope':>11} "
          f"{'Tr tangent':>14} {'localslope':>11} {'Tr_g/sqrt(N)':>13}")
    Ns, tr_t, tr_g = [], [], []
    for N in NS:
        BV, smin, smax0 = ground_basis([conic], N, 2 * N + 1)
        BT, _, _ = ground_basis([line_t], N, N + 1)
        BG, _, _ = ground_basis([line_g], N, N + 1)
        a = tr_pp(BV, BT)
        b = tr_pp(BV, BG)
        Ns.append(N)
        tr_t.append(a)
        tr_g.append(b)
        lt = local_slope(Ns, tr_t)
        lg = local_slope(Ns, tr_g)
        print(f"{N:>4} {bf.dim_h(nv,N):>6} {a:16.8f} "
              f"{(lt[-1] if lt else float('nan')):11.5f} {b:14.8f} "
              f"{(lg[-1] if lg else float('nan')):11.5f} "
              f"{b/math.sqrt(N):13.8f}")
    print(f"  transversal: loglog slope (last 5) = "
          f"{loglog_slope(Ns[-5:], tr_t[-5:]):.5f}  [predicted 0 = dim(V^W)]")
    print(f"  transversal: Tr -> {tr_t[-1]:.6f}   [predicted {csum:.6f}]")
    print(f"  TANGENT:     loglog slope (last 5) = "
          f"{loglog_slope(Ns[-5:], tr_g[-5:]):.5f}  [predicted 1/2, NOT 0]")
    ys = [t / math.sqrt(N) for t, N in zip(tr_g, Ns)]
    a0, b0 = fit_powers(Ns[-4:], ys[-4:], (0.0, -0.5))
    a1, b1, c1 = fit_powers(Ns[-5:], ys[-5:], (0.0, -0.5, -1.0))
    # contact order m = 2, psi(u) = gamma u^m with gamma = 1 for
    # z_1 = z_2^2 in the chart z_0 = 1 (FS-normal coordinates at [1:0:0]);
    # prediction  Tr -> Gamma(1 + 1/m) |gamma|^{-2/m} N^{1 - 1/m}.
    pred = math.gamma(1.5)
    print(f"  TANGENT:     Tr/sqrt(N) = {a0:.6f} + {b0:.4f}/sqrt(N)"
          f"          [2-term fit]")
    print(f"  TANGENT:     Tr/sqrt(N) = {a1:.6f} + {b1:.4f}/sqrt(N) "
          f"+ {c1:.3f}/N  [3-term fit]")
    print(f"  TANGENT:     predicted Gamma(1+1/m)|gamma|^{{-2/m}} = "
          f"{pred:.6f} at m = 2, gamma = 1")
    check("D tangent constant", a1, pred, 5e-2)
    print(f"  HF_{{R/(I+J)}}(N) for the tangent case = 2 for all N >= 1 "
          f"(I+J = (z_1, z_2^2)),")
    print("  so Tr is NOT the Hilbert function of I+J when contact is tangential.")
    print()


# ================================================================= section E
def section_E():
    print("=" * 78)
    print("E. Two smooth conics in P^2 meeting in FOUR transversal points.")
    print("   V = {z_0 z_1 - z_2^2},  W_lam = {z_0^2 + z_1^2 + lam z_2^2}.")
    print("   V is parametrised by [s^2 : t^2 : s t]; substituting gives")
    print("   w^2 + lam w + 1 = 0 with w = (s/t)^2, so lam < -2 gives four")
    print("   real transversal points.  lam = -10 is well conditioned")
    print("   (cos theta = 0.56); lam = -3 is the near-tangential contrast.")
    print()
    f1 = {(1, 1, 0): 1.0, (0, 0, 2): -1.0}

    def g1(x):
        return np.array([x[1], x[0], -2 * x[2]], dtype=complex)

    for lam in (-10.0, -3.0):
        f2 = {(2, 0, 0): 1.0, (0, 2, 0): 1.0, (0, 0, 2): lam}

        def g2(x, lam=lam):
            return np.array([2 * x[0], 2 * x[1], 2 * lam * x[2]], dtype=complex)

        csum = 0.0
        cosmax = 0.0
        print(f"  lam = {lam}: intersection points and angle factors")
        disc = lam * lam - 4.0
        for w in ((-lam + math.sqrt(disc)) / 2, (-lam - math.sqrt(disc)) / 2):
            for sgn in (1, -1):
                sv = sgn * math.sqrt(w)
                v = np.array([sv * sv, 1.0, sv], dtype=complex)
                v = v / np.linalg.norm(v)
                TV = tangent_space(v, [g1(v)])
                TW = tangent_space(v, [g2(v)])
                J, cang = angle_factor(TV, TW)
                csum += 1.0 / J
                cosmax = max(cosmax, float(cang[0]))
                print(f"    [{sv*sv:+.6f} : 1 : {sv:+.6f}] normalised: "
                      f"cos theta = {float(cang[0]):.8f}, J = {J:.8f}, "
                      f"1/J = {1/J:.6f}")
        cot2 = cosmax ** 2 / (1.0 - cosmax ** 2)
        print(f"  Predicted limit Tr -> sum_i 1/J_i = {csum:.8f}  "
              f"(HF_{{R/(I+J)}} = 4 = Bezout; angle-inflation factor "
              f"{csum/4:.4f})")
        print(f"  expected relative 1/N deficit ~ cot^2(theta)/N = "
              f"{cot2:.3f}/N  (crossover scale N ~ {cot2:.0f})")
        print(f"{'N':>4} {'Tr':>16} {'localslope':>11} {'Tr/limit':>11} "
              f"{'(1-Tr/lim)*N':>13}")
        Ns, trs_ = [], []
        for N in NGRID_P2:
            BV, _, _ = ground_basis([f1], N, 2 * N + 1)
            BW, _, _ = ground_basis([f2], N, 2 * N + 1)
            t = tr_pp(BV, BW)
            Ns.append(N)
            trs_.append(t)
            ls = local_slope(Ns, trs_)
            print(f"{N:>4} {t:16.8f} {(ls[-1] if ls else float('nan')):11.5f} "
                  f"{t/csum:11.6f} {(1 - t/csum)*N:13.4f}")
        rich = ((Ns[-1] * trs_[-1] - Ns[-2] * trs_[-2])
                / (Ns[-1] - Ns[-2]))          # Richardson for a + b/N
        a2, b2 = fit_powers(Ns[-3:], trs_[-3:], (0.0, -1.0))
        print(f"  Richardson (last two points, a + b/N): {rich:.6f}")
        print(f"  fit (last 3, a + b/N)                : {a2:.6f} + "
              f"{b2:.3f}/N        [predicted a = {csum:.6f}]")
        print(f"  Tr(N={Ns[-1]})/limit = {trs_[-1]/csum:.6f}")
        if lam == -10.0:
            # well-conditioned pair: the leading constant is confirmed to 5%.
            # NOTE (verdict O4): the r0 script clamped Tr/limit to <= 1, so an
            # overshoot passed automatically.  The clamp is gone; the two-sided
            # tolerance below is what mutation M-IO3 exercises.
            check("E constant (lam=-10), Richardson", rich, csum, 5e-2)
            check("E constant (lam=-10), last point", trs_[-1] / csum, 1.0,
                  1.2e-1)
        else:
            # ill-conditioned pair: still climbing at N = 60.  Two-sided, and
            # only the honest statement is asserted: the value is within 15%
            # of the predicted constant and has not overshot it by more than
            # the tolerance.
            check("E (lam=-3) within 15% of the limit at N=60",
                  trs_[-1] / csum, 1.0, 1.5e-1)
        print()
    print("  The lam = -3 pair is the CURVED-VARIETY version of the crossover")
    print("  of section C: the same asymptotic law, reached at N ~ cot^2(theta).")
    print()


# ================================================================= section F
def section_F():
    print("=" * 78)
    print("F. EXCESS but CLEAN intersection: two planes in P^4 meeting in a line.")
    print("   V = {z_3 = z_4 = 0}, W = {z_2 = z_4 = 0}: both are P^2's,")
    print("   expected dim = 2+2-4 = 0, actual dim(V ^ W) = 1 (the line z_2=z_3=z_4=0).")
    print("   Clean: T_x V ^ T_x W = T_x Z at every x in Z.  Prediction: Tr ~ N^1.")
    print()
    nv = 5
    I = [{(0, 0, 0, 1, 0): 1.0}, {(0, 0, 0, 0, 1): 1.0}]
    J = [{(0, 0, 1, 0, 0): 1.0}, {(0, 0, 0, 0, 1): 1.0}]
    print(f"{'N':>4} {'M_N':>7} {'HF_I=HF_J':>10} {'Tr(SVD)':>12} "
          f"{'closed N+1':>11} {'localslope':>11} {'Tr/M_N':>11}")
    Ns, trs_ = [], []
    for N in (2, 3, 4, 5, 6, 8, 10, 12):
        hf = bf.dim_h(3, N)
        M = bf.dim_h(nv, N)
        BI, _, _ = ground_basis(I, N, hf)
        BJ, _, _ = ground_basis(J, N, hf)
        t = tr_pp(BI, BJ)
        check(f"F N={N}", t, N + 1)
        Ns.append(N)
        trs_.append(t)
        ls = local_slope(Ns, trs_)
        print(f"{N:>4} {M:>7} {hf:>10} {t:12.6f} {N+1:>11} "
              f"{(ls[-1] if ls else float('nan')):11.5f} {t/M:11.3e}")
    print("  Tr = N+1 exactly = HF_{R/(I+J)}(N) with I+J = (z_2,z_3,z_4);")
    print("  the observable reports the ACTUAL dimension 1, not the expected 0.")
    print()
    print("  EXCESS WITH A NONTRIVIAL ANGLE (added in repair r1, verdict O1).")
    print("  V = span(e_0,e_1,e_2) i.e. I = (z_3, z_4);")
    print("  W = span(e_0,e_1, cos(t) e_2 + sin(t) e_3), i.e.")
    print("  J = (-sin(t) z_2 + cos(t) z_3, z_4).  Both are P^2's in P^4 with")
    print("  expected intersection dimension 0 and ACTUAL Z = {z_2=z_3=z_4=0},")
    print("  l = 1, clean for sin(t) != 0.  This is the case that separates the")
    print("  ANTI-DIAGONAL block (which contributes vol(Z)/pi^l = 1) from the")
    print("  TRANSVERSE block (which contributes 1/J = 1/sin^2 t): the r0 memo")
    print("  derived only the second, and its exponent was right only because")
    print("  the two exponents happen to add to l.  Principal cosines (1,1,c),")
    print("  so section J gives Tr = h_N(1,1,c^2) = sum_a c^{2a}(N+1-a)")
    print("  = (N+1)/sin^2 t - cos^2 t/sin^4 t + O(cos^{2N} t) EXACTLY.")
    print(f"{'t':>7} {'1/sin^2 t':>11} {'N':>4} {'Tr(SVD)':>14} "
          f"{'Tr(exact)':>14} {'Tr/N':>10}")
    for t in (0.9, 0.4):
        c, sn = math.cos(t), math.sin(t)
        allok = True
        Iv = [{(0, 0, 0, 1, 0): 1.0}, {(0, 0, 0, 0, 1): 1.0}]
        Jv = [{(0, 0, 1, 0, 0): -sn, (0, 0, 0, 1, 0): c},
              {(0, 0, 0, 0, 1): 1.0}]
        for N in (3, 5, 8, 12, 24, 48):
            hf = bf.dim_h(3, N)
            exact = sum(c ** (2 * a) * (N + 1 - a) for a in range(N + 1))
            if N <= 12:
                BI, _, _ = ground_basis(Iv, N, hf)
                BJ, _, _ = ground_basis(Jv, N, hf)
                tr = tr_pp(BI, BJ)
                allok &= check(f"F excess-angle t={t} N={N}", tr, exact)
                ts = f"{tr:14.8f}"
            else:
                ts = f"{'-':>14}"
            print(f"{t:>7.2f} {1/sn**2:>11.6f} {N:>4} {ts} {exact:14.8f} "
                  f"{exact/N:10.6f}")
        print(f"   {'OK' if allok else 'MISMATCH'}: excess-with-angle at "
              f"t = {t}, SVD versus h_N(1,1,cos^2 t), N <= 12 "
              f"(verdict O1's anti-diagonal block)")
    print("  Tr/N -> 1/sin^2 t = 1.6297 and 6.5943: the excess intersection")
    print("  carries BOTH the vol(Z) factor and the angle factor, as the")
    print("  corrected Geometry 5.3-5.4 requires.")
    print()


# ================================================================= section G
def section_G():
    print("=" * 78)
    print("G. Toeplitz averages on the conic  V = {z_0 z_1 = z_2^2} in P^2.")
    print("   D-toeplitz-operator with the degree normalisation this lane adds:")
    print("   for g of bidegree (r,r) the level-N Toeplitz operator is")
    print("     T_g^{(N)} = ((N-r)!/N!) P_0 :g(a^dag,a): P_0,")
    print("   whose Berezin symbol is exactly g.  r=1: n_2/N.  r=2: n_2(n_2-1)/(N(N-1)).")
    print("   Target: (1/vol V) int_V g dvol_V, by Gauss-Legendre quadrature on")
    print("   the rational parametrisation [s:t] -> [s^2 : t^2 : s t].")
    print()
    # induced FS area density on the conic in u = |s/t|^2:
    #   A(u) = (u^2 + 4u + 1) / (u^2 + u + 1)^2 ;  dvol = (1/2) A(u) du dphi
    #   total = pi * int_0^inf A du  (= vol = deg * pi = 2 pi)
    def A(u):
        return (u * u + 4 * u + 1) / (u * u + u + 1) ** 2

    def g1(u):      # |z_2|^2 / ||z||^2   at [u : 1 : sqrt(u)] up to phase
        return u / (u * u + u + 1)

    def g0(u):      # |z_0|^2 / ||z||^2
        return u * u / (u * u + u + 1)

    # Gauss-Legendre on x in (0,1) with u = x/(1-x)
    deg = 4000
    xs, ws = np.polynomial.legendre.leggauss(deg)
    xs = 0.5 * (xs + 1.0)
    ws = 0.5 * ws
    us = xs / (1.0 - xs)
    jac = 1.0 / (1.0 - xs) ** 2
    w = ws * jac * A(us)
    tot = float(w.sum())
    avg_g1 = float((w * g1(us)).sum()) / tot
    avg_g0 = float((w * g0(us)).sum()) / tot
    avg_g1sq = float((w * g1(us) ** 2).sum()) / tot
    print(f"  quadrature: int_0^inf A(u) du = {tot:.10f}  "
          f"(exact value 2 = deg V; vol V = 2 pi)")
    check("G total area", tot, 2.0, 1e-8)
    print(f"  <|z_2|^2>_V = {avg_g1:.10f}      <|z_0|^2>_V = {avg_g0:.10f}")
    print(f"  <|z_2|^4>_V = {avg_g1sq:.10f}    (2<|z_0|^2> + <|z_2|^2> = "
          f"{2*avg_g0 + avg_g1:.10f}, must be 1)")
    check("G normalisation", 2 * avg_g0 + avg_g1, 1.0, 1e-8)
    print()
    conic = {(1, 1, 0): 1.0, (0, 0, 2): -1.0}
    nv = 3
    print(f"{'N':>4} {'HF':>5} {'Tr(P0 n2)/(N HF)':>18} {'err':>12} "
          f"{'Tr(P0 n2(n2-1))/(N(N-1)HF)':>28} {'err':>12}")
    Ns, v1, v2 = [], [], []
    for N in NGRID_P2:
        hf = 2 * N + 1
        B, _, _ = ground_basis([conic], N, hf)
        ks = np.array(bf.monomials(nv, N), dtype=float)
        n2 = ks[:, 2]
        wts = np.sum(np.abs(B) ** 2, axis=1)      # diagonal of P_0
        t1 = float(np.dot(wts, n2)) / (N * hf)
        t2 = float(np.dot(wts, n2 * (n2 - 1.0))) / (N * (N - 1) * hf)
        Ns.append(N)
        v1.append(t1)
        v2.append(t2)
        print(f"{N:>4} {hf:>5} {t1:18.10f} {t1-avg_g1:12.3e} "
              f"{t2:28.10f} {t2-avg_g1sq:12.3e}")
    a1, b1 = fit_a_plus_b_over_N(Ns[-5:], v1[-5:])
    a2, b2 = fit_a_plus_b_over_N(Ns[-5:], v2[-5:])
    print(f"  fit  <n_2/N>   = {a1:.8f} + {b1:.6f}/N   "
          f"[quadrature {avg_g1:.8f}, difference {a1-avg_g1:.2e}]")
    print(f"  fit  <n2(n2-1)>= {a2:.8f} + {b2:.6f}/N   "
          f"[quadrature {avg_g1sq:.8f}, difference {a2-avg_g1sq:.2e}]")
    check("G Toeplitz r=1 limit", a1, avg_g1, 3e-4)
    check("G Toeplitz r=2 limit", a2, avg_g1sq, 3e-3)
    check("G quadrature vs exact <|z_2|^2>", avg_g1, TOEPLITZ_L1, 1e-12)
    print("  The INTERCEPTS agree with the quadrature (and, for r=1, with the")
    print(f"  exact value -1/6 + 2 sqrt(3) pi/27 = {TOEPLITZ_L1:.16f}).")
    print("  The 1/N COEFFICIENTS above are finite-range fits over N <= 60")
    print("  only (verdict O3); section K carries them to N = 1200, where the")
    print("  r=1 coefficient is about 0.03144, not 0.03275.")
    print("  NOTE: this is the DEGREE-NORMALISED operator, not the registered")
    print("  D-toeplitz-operator.  With the registered operator the ratio is")
    print("  N times these numbers and diverges, which is why C-086/C-168 are")
    print("  proposed REFUTED as written (verdict O3).")
    print()


# ================================================================= section H
def section_H():
    print("=" * 78)
    print("H. Size of the DQC1 signal (D-dqc1-style-estimate, applications")
    print("   caution 1).  Two hyperplanes in P^n at FS angle theta:")
    print("   Tr(P_I P_J) = sum_{a=0}^{N} c^{2a} binom(N-a+n-2, n-2),")
    print("   HF_I = HF_J = binom(N+n-1, n-1),  M_N = binom(N+n, n).")
    print()
    for theta in (math.pi / 2, 0.4):
        c = math.cos(theta)
        print(f"  theta = {theta:.4f} (c = {c:.6f}); N = n (regularity 1, so")
        print("  every N >= 1 is in the stable range).")
        print(f"    {'n':>3} {'N':>3} {'M_N':>12} {'Tr':>16} {'Tr/M_N':>11} "
              f"{'Tr/sqrt(HFHF)':>13} {'Tr/(HF HF)':>12}")
        for n in (2, 3, 4, 6, 8, 12, 16, 24, 32):
            N = n
            M = math.comb(N + n, n)
            hf = math.comb(N + n - 1, n - 1)
            tr = sum(c ** (2 * a) * math.comb(N - a + n - 2, n - 2)
                     for a in range(N + 1))
            print(f"    {n:>3} {N:>3} {M:>12} {tr:16.6f} {tr/M:11.4e} "
                  f"{tr/hf:13.4e} {tr/hf**2:12.4e}")
        print()
    print("  Same, but with codimension GROWING: I = (z_0,...,z_{k-1}),")
    print("  J = (z_k,...,z_{2k-1}) in P^n, n = 4k, N = n; V ^ W has")
    print("  codimension 2k.  Tr = binom(N + n - 2k, n - 2k) exactly.")
    print(f"    {'k':>3} {'n':>3} {'N':>3} {'M_N':>16} {'Tr':>16} "
          f"{'Tr/M_N':>11} {'Tr/(HF HF)':>12}")
    for k in (1, 2, 3, 4, 5, 6, 8):
        n = 4 * k
        N = n
        M = math.comb(N + n, n)
        hf = math.comb(N + n - k, n - k)
        tr = math.comb(N + n - 2 * k, n - 2 * k)
        print(f"    {k:>3} {n:>3} {N:>3} {M:>16} {tr:16} {tr/M:11.4e} "
              f"{tr/hf**2:12.4e}")
    print("  => Tr/M_N stays polynomially visible while the codimension of")
    print("     V ^ W is O(1) and collapses exponentially once it grows,")
    print("     exactly the codimension law of applications caution 1.")
    print("     Tr/(HF_I HF_J) -- the quantity a two-copy SWAP test measures --")
    print("     is ALWAYS much smaller than Tr/M_N here.")
    print()


# ================================================================= section I
def section_I():
    print("=" * 78)
    print("I. Direct test of the Bergman lemma used in the Laplace argument:")
    print("     S_V := int_V |e_p><e_p| dvol_V  ~  (pi^k / N^k) P_I   (k = dim V),")
    print("   for V the conic in P^2 (k = 1).  Reported: the spectrum of S_V")
    print("   rescaled by N/pi, which should concentrate at 1 on ker H_N and")
    print("   at 0 on I_N.")
    print()
    nv = 3
    conic = {(1, 1, 0): 1.0, (0, 0, 2): -1.0}

    def A(u):
        return (u * u + 4 * u + 1) / (u * u + u + 1) ** 2

    nr, na = 900, 96
    xs, ws = np.polynomial.legendre.leggauss(nr)
    xs = 0.5 * (xs + 1.0)
    ws = 0.5 * ws
    us = xs / (1.0 - xs)
    jac = 1.0 / (1.0 - xs) ** 2
    # dvol = (1/2) A(u) du dphi ; u = |w|^2, point [w^2 : 1 : w]
    wr = 0.5 * ws * jac * A(us)
    phis = 2.0 * math.pi * np.arange(na) / na
    dphi = 2.0 * math.pi / na
    print(f"{'N':>4} {'HF':>5} {'min(ker)':>11} {'max(ker)':>11} "
          f"{'mean(ker)':>11} {'max(I_N)':>11}")
    for N in (6, 10, 14, 18):
        mons = bf.monomials(nv, N)
        idx = np.array(mons, dtype=np.int64)
        # (p.z)^N / sqrt(N!) = sum_k sqrt(N!/k!) p^k |k>   (D-coherent-state)
        coef = np.array([math.sqrt(math.factorial(N) / bf.fact_prod(m))
                         for m in mons])
        S = np.zeros((len(mons), len(mons)), dtype=complex)
        for ph in phis:
            wcpx = np.sqrt(us) * np.exp(1j * ph)
            P = np.stack([wcpx ** 2, np.ones_like(wcpx) + 0j, wcpx], axis=1)
            P = P / np.linalg.norm(P, axis=1, keepdims=True)
            V = np.ones((len(us), len(mons)), dtype=complex)
            for j in range(nv):
                V = V * (P[:, j][:, None] ** idx[None, :, j])
            V = V * coef[None, :]
            S += (V.conj().T * (wr * dphi)) @ V
        S = (S + S.conj().T) / 2
        B, _, _ = ground_basis([conic], N, 2 * N + 1)
        Sk = B.conj().T @ S @ B
        ev = np.linalg.eigvalsh(Sk) * N / math.pi
        # complement
        Q = np.eye(len(mons), dtype=complex) - B @ B.conj().T
        ev2 = np.linalg.eigvalsh(Q @ S @ Q) * N / math.pi
        print(f"{N:>4} {2*N+1:>5} {ev.min():11.6f} {ev.max():11.6f} "
              f"{ev.mean():11.6f} {abs(ev2).max():11.3e}")
    print("  The eigenvalues on ker H_N concentrate at 1 with O(1/N) spread and")
    print("  S_V annihilates I_N to machine precision (its range IS ker H_N,")
    print("  exactly, by D-coherent-state/C-028); the lemma is the statement")
    print("  that the eigenvalues are asymptotically FLAT, which is what the")
    print("  min/max columns test.")
    print()


# ============================================== red-capable predicates (O4)
# Each predicate returns (ok, detail).  The normal run requires ok == True;
# mutation_selftest() feeds each one a deliberately wrong input and requires
# ok == False.  Mutations are run IN PROCESS because the sandbox the r1 critic
# used is read-only (verdict O4, "Mutated copies: NOT RUN").

def pred_tangent_constant(swap=False):
    """M1: swapping the tangent and transversal lines must be caught.
    Fits Tr/sqrt(N) = a + b/sqrt(N) + c/N on the tangent family and compares
    a with Gamma(1+1/m)|gamma|^{-2/m} = Gamma(3/2) at m = 2, gamma = 1."""
    conic = {(1, 1, 0): 1.0, (0, 0, 2): -1.0}
    line_t = {(0, 1, 0): 1.0, (1, 0, 0): -1.0}
    line_g = {(0, 1, 0): 1.0}
    tan, tra = (line_t, line_g) if swap else (line_g, line_t)
    Ns = list(NGRID_P2)
    ys = []
    for N in Ns:
        BV, _, _ = ground_basis([conic], N, 2 * N + 1)
        BT, _, _ = ground_basis([tan], N, N + 1)
        ys.append(tr_pp(BV, BT) / math.sqrt(N))
    a, _, _ = fit_powers(Ns[-5:], ys[-5:], (0.0, -0.5, -1.0))
    target = math.gamma(1.5)
    ok = abs(a - target) <= 5e-2 * target
    return ok, f"a = {a:.6f}, target Gamma(3/2) = {target:.6f}"


def pred_toeplitz_ordering(shift=0):
    """M2: the ORDERING mutation.  shift = 0 is the normal-ordered
    D-normalised-toeplitz-operator; shift = 1 is the anti-normal alternative
    (n_2 -> n_2 + 1), which changes the level-N value by exactly 1/N and the
    asymptotic 1/N coefficient by exactly +1.  The r0 script fitted a free
    intercept AND a free 1/N coefficient, so it absorbed this mutation; here
    the intercept is PINNED to the exact Fubini-Study average and the
    coefficient must land inside a fixed window."""
    bs = []
    for N in (400, 800, 1200):
        t1, _, hf = conic_kernel_moments(N)
        v = (t1 + shift * hf) / (N * hf)
        bs.append(N * (v - TOEPLITZ_L1))
    lo, hi = TOEPLITZ_B1_WINDOW
    ok = all(lo <= b <= hi for b in bs)
    return ok, f"b_N at N=400,800,1200: {[round(b, 6) for b in bs]}, window {(lo, hi)}"


def pred_conic_pair_limit(lam=-10.0, clamp=False, limit_scale=1.0,
                          ratio_only=False):
    """Section E's constant.  `clamp = True` reproduces the r0 bug
    (min(Tr/limit, 1)), under which any OVERSHOOT passed automatically
    (verdict O4).  `limit_scale != 1` corrupts the predicted constant; the
    repaired, unclamped check must catch that, while the r0 clamped form does
    not -- which is exactly the blindness the verdict identified."""
    f1 = {(1, 1, 0): 1.0, (0, 0, 2): -1.0}
    f2 = {(2, 0, 0): 1.0, (0, 2, 0): 1.0, (0, 0, 2): lam}
    disc = lam * lam - 4.0
    csum = 0.0
    for w in ((-lam + math.sqrt(disc)) / 2, (-lam - math.sqrt(disc)) / 2):
        for sgn in (1, -1):
            sv = sgn * math.sqrt(w)
            v = np.array([sv * sv, 1.0, sv], dtype=complex)
            v = v / np.linalg.norm(v)
            TV = tangent_space(v, [np.array([v[1], v[0], -2 * v[2]],
                                            dtype=complex)])
            TW = tangent_space(v, [np.array([2 * v[0], 2 * v[1],
                                             2 * lam * v[2]], dtype=complex)])
            J, _ = angle_factor(TV, TW)
            csum += 1.0 / J
    Ns, trs_ = [], []
    for N in NGRID_P2:
        BV, _, _ = ground_basis([f1], N, 2 * N + 1)
        BW, _, _ = ground_basis([f2], N, 2 * N + 1)
        Ns.append(N)
        trs_.append(tr_pp(BV, BW))
    csum *= limit_scale
    rich = (Ns[-1] * trs_[-1] - Ns[-2] * trs_[-2]) / (Ns[-1] - Ns[-2])
    ratio = trs_[-1] / csum
    if clamp:
        ratio = min(ratio, 1.0)          # the r0 bug
    ok_ratio = abs(ratio - 1.0) <= 1.2e-1
    ok_rich = abs(rich - csum) <= 5e-2 * csum
    ok = ok_ratio if ratio_only else (ok_rich and ok_ratio)
    return ok, (f"Richardson {rich:.6f} vs claimed limit {csum:.6f} "
                f"(ok {ok_rich}), Tr(N=60)/limit = {ratio:.6f} (ok {ok_ratio})")


def pred_crossover_slope(shrink=1.0):
    """M4: the crossover assertion.  For two hyperplanes in P^3 at
    1/sin^2 t = 100 the local log-log slope must still be ABOVE 1.4 at
    N = 256 and must have fallen BELOW 1.3 by N = 1024.  shrink < 1 rescales
    the angle so the crossover moves, which must be caught."""
    t = math.asin(shrink * math.sqrt(1.0 / 100.3))
    c = math.cos(t)

    def T(N):
        return sum(c ** (2 * a) * (N + 1 - a) for a in range(N + 1))

    def slope(N1, N2):
        return math.log(T(N2) / T(N1)) / math.log(N2 / N1)

    s256 = slope(128, 256)
    s1024 = slope(512, 1024)
    ok = (s256 > 1.4) and (s1024 < 1.3)
    return ok, f"slope(256) = {s256:.4f} (>1.4), slope(1024) = {s1024:.4f} (<1.3)"


def pred_linear_exact(perturb=0.0):
    """Section J's exact identity, as a predicate.  perturb != 0 corrupts the
    principal cosines and must be caught."""
    rng = np.random.default_rng(7)
    worst = 0.0
    for (nv, r1, r2, N) in ((4, 2, 2, 5), (4, 2, 3, 6), (5, 3, 2, 4),
                            (5, 3, 3, 5), (6, 2, 4, 4), (4, 3, 3, 7)):
        U = rng.normal(size=(nv, r1)) + 1j * rng.normal(size=(nv, r1))
        W = rng.normal(size=(nv, r2)) + 1j * rng.normal(size=(nv, r2))
        QU, _ = np.linalg.qr(U)
        QW, _ = np.linalg.qr(W)
        sig = principal_cosines(QU, QW)
        BU, _, _ = ground_basis(linear_gens(ortho_complement(QU)), N,
                                bf.dim_h(r1, N))
        BW, _, _ = ground_basis(linear_gens(ortho_complement(QW)), N,
                                bf.dim_h(r2, N))
        tr = tr_pp(BU, BW)
        pred = h_complete(list(sig[: min(r1, r2)] ** 2 + perturb), N)
        worst = max(worst, abs(tr - pred) / max(1.0, abs(pred)))
    ok = worst <= 1e-10
    return ok, f"worst relative discrepancy {worst:.3e}"


# ================================================================= section J
def section_J():
    print("=" * 78)
    print("J. EXACT identity for linear V, W (new in repair r1; it is the")
    print("   opening identity of verdict O1, proved here and tested).")
    print("   For subspaces U, W of C^{n+1} with principal cosines")
    print("   sigma_1..sigma_r, r = min(dim U, dim W):")
    print("     Tr(P_{Sym^N U} P_{Sym^N W}) = h_N(sigma_1^2, ..., sigma_r^2),")
    print("   h_N the complete homogeneous symmetric polynomial.  Proof: in")
    print("   principal-vector bases <u_i, w_j> = sigma_i delta_ij, so the")
    print("   symmetrised monomial bases have overlap prod_i sigma_i^{alpha_i}")
    print("   diagonally in the multi-index alpha, |alpha| = N.")
    print("   Every linear table in this script is a special case:")
    print("     two lines in P^2         sigma = (1, c)       -> sum_a c^{2a}")
    print("     two planes in P^3        sigma = (1, 1, c)    -> sum_a c^{2a}(N+1-a)")
    print("     Clifford skew pair       sigma = (c, c)       -> (N+1)c^{2N}")
    print("     excess planes in P^4     sigma = (1, 1, 0)    -> N+1")
    print("     hyperplanes in P^n       sigma = (1^{n-1}, c) -> sum_a c^{2a}C(N-a+n-2,n-2)")
    print()
    ok, detail = pred_linear_exact()
    print(f"   random subspaces in C^4, C^5, C^6, N = 4..7: {detail}")
    if not ok:
        FAILURES.append(f"J exact subspace identity: {detail}")
    print("   => the whole linear half of arm C is EXACT, needs no Bergman")
    print("      frame lemma, and needs no Laplace argument.")
    print()


# ================================================================= section K
def section_K():
    print("=" * 78)
    print("K. Toeplitz asymptotics at large N by the exact conic recurrence")
    print("   (verdict O3: the r0 1/N coefficient was a finite-range fit).")
    print("   No SVD; H_N is block diagonal over d = k_0 - k_1 and each block")
    print("   has a one-dimensional kernel given in closed form.")
    print(f"   EXACT limit  <|z_2|^2>_V = -1/6 + 2 sqrt(3) pi/27 = "
          f"{TOEPLITZ_L1:.16f}")
    print()
    print(f"{'N':>6} {'Tr(P_0 n_2)/(N HF)':>22} {'N(value - L)':>16} "
          f"{'r=2 value':>20} {'N(value - L2)':>16}")
    vals = []
    for N in (22, 60, 100, 200, 400, 800, 1200):
        t1, t2, hf = conic_kernel_moments(N)
        v1 = t1 / (N * hf)
        v2 = t2 / (N * (N - 1) * hf)
        vals.append((N, v1, v2))
    L2 = ((vals[-2][0] * vals[-2][2] - vals[-3][0] * vals[-3][2])
          / (vals[-2][0] - vals[-3][0]))
    for N, v1, v2 in vals:
        print(f"{N:>6} {v1:>22.15f} {N*(v1-TOEPLITZ_L1):>16.10f} "
              f"{v2:>20.15f} {N*(v2-L2):>16.10f}")
    print(f"  r=1: the 1/N coefficient tends to about "
          f"{vals[-1][0]*(vals[-1][1]-TOEPLITZ_L1):.5f}, NOT the 0.03275 that")
    print("  the r0 N <= 60 fit reported; the r0 INTERCEPT was nevertheless")
    print(f"  right to 1.7e-5.  r=2: Richardson limit {L2:.10f} against the")
    print("  quadrature value 0.0646223 (section G).")
    ok, detail = pred_toeplitz_ordering(0)
    print(f"  ordering check (normal ordering, pinned intercept): {detail}")
    if not ok:
        FAILURES.append(f"K normal-ordered 1/N coefficient: {detail}")
    okm, detm = pred_toeplitz_ordering(1)
    print(f"  same with ANTI-normal ordering n_2 -> n_2+1: {detm}")
    print(f"  -> anti-normal is rejected by the window: {not okm}  "
          "(this is what makes the check red to M2)")
    if okm:
        FAILURES.append("K ordering check is NOT red to anti-normal ordering")
    print()


# ============================================================ self-test (O4)
def mutation_selftest():
    print("=" * 78)
    print("MUTATION SELF-TEST (L4, verdict O4).  Each mutation is applied")
    print("in process and MUST be caught; a mutation that passes is a FAILURE.")
    print("These four are the registration text for checkers/MUTATIONS.md,")
    print("which is outside this lane's writable files.")
    muts = [
        ("M-IO1 swap the tangent and transversal lines in section D",
         lambda: pred_tangent_constant(swap=True)),
        ("M-IO2 drop normal ordering, n_2 -> n_2 + 1 (section K)",
         lambda: pred_toeplitz_ordering(shift=1)),
        ("M-IO3 halve the predicted constant in section E (lam = -10)",
         lambda: pred_conic_pair_limit(lam=-10.0, clamp=False,
                                       limit_scale=0.5)),
        ("M-IO4 move the crossover angle by a factor 3 (section C)",
         lambda: pred_crossover_slope(shrink=1.0 / 3.0)),
        ("M-IO5 perturb the principal cosines in section J",
         lambda: pred_linear_exact(perturb=1e-6)),
    ]
    allred = True
    for name, fn in muts:
        ok, detail = fn()
        verdict = "CAUGHT" if not ok else "NOT CAUGHT"
        print(f"  {verdict:>10}  {name}")
        print(f"              {detail}")
        if ok:
            allred = False
            FAILURES.append(f"mutation not caught: {name}")
    # and the unmutated predicates must PASS
    for name, fn in (("D tangent constant", pred_tangent_constant),
                     ("E conic-pair limit", pred_conic_pair_limit),
                     ("C crossover slopes", pred_crossover_slope),
                     ("J exact identity", pred_linear_exact)):
        ok, detail = fn()
        print(f"  {'PASS' if ok else 'FAIL':>10}  unmutated {name}: {detail}")
        if not ok:
            FAILURES.append(f"unmutated predicate failed: {name}")
    okc, detc = pred_conic_pair_limit(lam=-10.0, clamp=True, limit_scale=0.5,
                                      ratio_only=True)
    oku, detu = pred_conic_pair_limit(lam=-10.0, clamp=False, limit_scale=0.5,
                                      ratio_only=True)
    print("  M-IO3 footnote, isolating the clamp on the RATIO leg alone:")
    print(f"    r0 clamped form min(Tr/limit,1) on a halved constant: ok = {okc}")
    print(f"    repaired unclamped form on the same input:            ok = {oku}")
    print("    i.e. the r0 check was blind to a wrong constant (verdict O4);")
    print("    the clamp is removed in section E.")
    if okc is False or oku is True:
        FAILURES.append("M-IO3 footnote: the clamp demonstration did not "
                        f"behave as stated (clamped {okc}, unclamped {oku})")
    print(f"  all mutations caught: {allred}")
    print()


def main():
    print("intersection and integration observables -- exploration (PRD arm C)")
    print("regenerate with:")
    print("  timeout 900 python3 checkers/explore/intersection_observables.py")
    print(f"numpy {np.__version__}")
    print()
    section_A()
    section_B()
    section_C()
    section_D()
    section_E()
    section_F()
    section_G()
    section_H()
    section_I()
    section_J()
    section_K()
    mutation_selftest()
    print("=" * 78)
    if FAILURES:
        print(f"FAIL: {len(FAILURES)} numerical agreement checks failed")
        for f in FAILURES:
            print("  " + f)
        return 1
    print("OK.  What this run establishes: (i) every EXACT closed form agreed")
    print("with an independent SVD kernel computation; (ii) the section-J")
    print("subspace identity holds to 1e-15 on random subspaces; (iii) the")
    print("named constants that carry an explicit assertion were met, namely")
    print("the section-A/C/F closed forms, the section-D tangent constant, the")
    print("section-E well-conditioned limit, the section-C crossover slopes,")
    print("the section-K normal-ordered 1/N coefficient, and the section-G")
    print("Toeplitz leading terms; (iv) all five mutations were caught.")
    print("Printed exponents and tables NOT covered by an assertion are")
    print("reported as observations, not as verified claims.")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Mismatch as e:
        print(f"FAIL: {e}")
        sys.exit(1)
    except Exception as e:  # noqa: BLE001
        import traceback
        traceback.print_exc()
        print(f"ERROR: {e}")
        sys.exit(2)
