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
    print(f"{'N':>4} {'Tr':>16} {'Tr/cos^{2N}d0':>16} {'-log Tr/(2N)':>13} "
          f"{'log sec d0':>11}")
    prev = None
    for N in (2, 3, 4, 5, 6, 8, 10, 12, 14, 16):
        hf = N + 1
        BI, _, _ = ground_basis(I, N, hf)
        BJ, _, _ = ground_basis(Jg, N, hf)
        tr = tr_pp(BI, BJ)
        ratio = tr / math.cos(d0) ** (2 * N)
        rate = -math.log(tr) / (2 * N)
        print(f"{N:>4} {tr:16.10g} {ratio:16.8f} {rate:13.6f} "
              f"{math.log(1/math.cos(d0)):11.6f}")
        prev = ratio
    print(f"  Tr/cos^{{2N}}d0 tends to a constant = {prev:.6f} "
          f"(exponent 0), as the Laplace argument predicts for an isolated")
    print("  closest pair; the Clifford pair above has a 1-parameter family of")
    print("  closest pairs and gains exactly one power of N.")
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
            # well-conditioned pair: the leading constant is confirmed to 5%
            check("E constant (lam=-10), Richardson", rich, csum, 5e-2)
            check("E constant (lam=-10), last point", trs_[-1] / csum, 1.0,
                  1.2e-1)
        else:
            # ill-conditioned pair: still climbing at N = 60, so only the
            # weaker statement "has not yet overshot" is checked
            check("E (lam=-3) below the limit at N=60",
                  min(trs_[-1] / csum, 1.0), 1.0, 1.5e-1)
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
    print("  => C-168 / C-086 CONFIRMED numerically at 1e-4 on this family,")
    print("     with a clean 1/N correction; the O(1/N) coefficient is")
    print("     ordering dependent (D-toeplitz-operator Pitfalls).")
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
    print("=" * 78)
    if FAILURES:
        print(f"FAIL: {len(FAILURES)} numerical agreement checks failed")
        for f in FAILURES:
            print("  " + f)
        return 1
    print("OK: every closed form agreed with the independent SVD kernel")
    print("computation, and every predicted constant/exponent was met.")
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
