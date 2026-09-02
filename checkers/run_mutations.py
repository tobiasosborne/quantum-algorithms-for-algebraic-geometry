"""Mutation harness: one recorded mutation per checker (rk-light law L4).

For each checker, this copies the whole suite into a fresh temporary directory,
applies ONE exact textual edit there (never to the tracked tree), runs that one
checker under `timeout`, and records the exit code and the last line of output.
A checker with no red mutation does not exist.

Usage:
    timeout 1800 python3 run_mutations.py            # all mutations
    timeout 600  python3 run_mutations.py task1      # substring filter
    timeout 1800 python3 run_mutations.py --md       # emit the MUTATIONS.md table

Every mutation must produce exit code 1 (a printed FAIL reason).  Exit code 0
from a mutated copy means the checker does not actually test the property it
claims to test, and this harness then exits nonzero itself.
"""
import os
import shutil
import subprocess
import sys
import tempfile
import time

HERE = os.path.dirname(os.path.abspath(__file__))
BUDGET = 600

# checker -> (target file, exact old text, exact new text, what the defect is)
MUTATIONS = {
    "check_task1_conic.py": (
        "bf.py",
        "            A[ridx[kk], cj] += np.conj(ca) * math.sqrt(ff)",
        "            A[ridx[kk], cj] += np.conj(ca) * ff",
        "drop the square root in the Fock matrix element of a(f): the falling "
        "factorial enters unsquare-rooted, so |k> = z^k/sqrt(k!) is no longer "
        "the orthonormal basis",
    ),
    "check_task2_hilbert.py": (
        "ideals.py",
        '    return nv, bf.minors2x2(nv, [0, 1, 2], [1, 2, 3]), "twisted cubic P^3", lambda N: 3*N+1',
        '    return nv, bf.minors2x2(nv, [0, 1, 2], [1, 2, 3]), "twisted cubic P^3", lambda N: 3*N+2',
        "change the twisted cubic's Hilbert function by one, 3N+1 -> 3N+2",
    ),
    "check_task2b_subspace.py": (
        "check_task2b_subspace.py",
        "                v[idx[e]] += c * math.sqrt(bf.fact_prod(e))   # z^e = sqrt(e!)|e>",
        "                v[idx[e]] += c                                # z^e = sqrt(e!)|e>",
        "write the spanning set of I_N in the UNNORMALISED monomial basis, i.e. "
        "forget that z^e = sqrt(e!) |e>; orthogonality to ker H_N is then a "
        "statement in the wrong inner product",
    ),
    "check_task3_gaps.py": (
        "bf.py",
        "        f[m] = c / math.sqrt(2 * len(ms))",
        "        f[m] = c",
        "drop the Kostlan normalisation of random forms, so every random-quadric "
        "gap is rescaled and the published prefactors no longer apply",
    ),
    "check_task3b_hard.py": (
        "check_task3b_hard.py",
        "SINGLET = np.array([0, 1, -1, 0], dtype=complex)",
        "SINGLET = np.array([0, 2, -1, 0], dtype=complex)",
        "unbalance the singlet to 2|01> - |10>: still a rank-one 2-local "
        "projector, but no longer the ferromagnetic Heisenberg chain, so "
        "m^2 Delta -> pi^2 must fail.  (A pure sign flip to |01> + |10> is NOT "
        "a valid mutation: it is a local unitary conjugation by Z on alternate "
        "sites and leaves the whole spectrum invariant.)",
    ),
    "check_task3c_exact.py": (
        "check_task3c_exact.py",
        "CONIC = {(1, 1, 0): 1, (0, 0, 2): -1}",
        "CONIC = {(1, 1, 0): 1, (0, 0, 2): -2}",
        "rescale one coefficient of the conic (z0z1 - 2 z2^2): the ideal is the "
        "same variety but the presentation changes, so Delta_N = N+1 must fail",
    ),
    "check_task3d_nscale.py": (
        "ideals.py",
        "    g = [bf.random_form(nv, 2, rng) for _ in range(k)]",
        "    g = [{a: c * (2.0 ** (-n / 4.0)) for a, c in bf.random_form(nv, 2, rng).items()}\n         for _ in range(k)]",
        "scale the random quadrics by 2^(-n/4), so Delta decays exponentially in "
        "the number of variables instead of being flat",
    ),
    "check_task3e_ffstats.py": (
        "check_task3e_ffstats.py",
        "                psi = w - prod * (np.vdot(prod, w) / np.vdot(prod, prod))",
        "                psi = w",
        "stop projecting the forbidden state off the product state, so the "
        "chains are no longer frustration free",
    ),
    "check_task4_toric.py": (
        "check_task4_toric.py",
        "    weights = list(range(nv))",
        "    weights = [i * i for i in range(nv)]",
        "use the wrong A-grading (i^2 instead of i) for the rational normal "
        "curve, so the claimed block decomposition is not the right one",
    ),
    "check_task5_groebner.py": (
        "check_task5_groebner.py",
        "def initial(f):\n    M = max(sum(w * a for w, a in zip(W, al)) for al in f)",
        "def initial(f):\n    M = min(sum(w * a for w, a in zip(W, al)) for al in f)",
        "take the MINIMAL-weight terms as the initial form: the t=0 fibre is then "
        "not in_w(I) and the family is not flat (referee round 1, item 27)",
    ),
    "check_task6_2sat.py": (
        "bf.py",
        "    return A.conj().T @ A",
        "    return A.T @ A",
        "drop the conjugate in H_N = a^dag(f) a(f), so H_N is no longer the "
        "positive operator sum_j |f_j><f_j| on the multilinear sector",
    ),
    "check_task7_coherent.py": (
        "bf.py",
        "            A[ridx[kk], cj] += np.conj(ca) * math.sqrt(ff)",
        "            A[ridx[kk], cj] += ca * math.sqrt(ff)",
        "define a(f) = f(partial) instead of conj(f)(partial) -- exactly the "
        "notes' error corrected in report Sect. 9, item 3 (convention C3)",
    ),
    "check_task8_cnf.py": (
        "check_task8_cnf.py",
        "        g = ({bf.emono(nv, [0]): 1, bf.emono(nv, [i]): -1} if pos\n             else {bf.emono(nv, [i]): 1})",
        "        g = ({bf.emono(nv, [0]): 1, bf.emono(nv, [i]): 1} if pos\n             else {bf.emono(nv, [i]): 1})",
        "flip the sign in the positive-literal factor (z0 + z_i instead of "
        "z0 - z_i), so the clause form no longer vanishes exactly on the "
        "satisfying assignments",
    ),
    "check_task8_cnf.py::hf": (
        "check_task8_cnf.py",
        "    tmax = min(N - 3, n)",
        "    tmax = min(N - 4, n)",
        "use the wrong multiplier-degree bound in the exact boolean-quotient "
        "Hilbert function (the clause forms are cubic, so multipliers run over "
        "degree N-3).  This leaves H_N untouched, so it isolates the HF claim: "
        "the checker must catch it by disagreeing with the independent GF(p) "
        "Macaulay rank and with the numerical kernel count",
    ),
    "check_task9_pyramid.py": (
        "check_task9_pyramid.py",
        "    f5 = {(1, 0, 0, 1, 0): 1.0, (0, 1, 1, 0, 0): -1.0}",
        "    f5 = {(1, 0, 0, 1, 0): 1.0, (0, 1, 1, 0, 0): -1.0, (0, 0, 0, 0, 2): 1.0}",
        "add a y^2 term to the pyramid relation, so the apex variable is no "
        "longer unused and the variety is no longer a cone",
    ),
    "check_fact71_bombieri.py": (
        "bf.py",
        "            A[ridx[kk], cj] += np.conj(ca) * math.sqrt(ff)",
        "            A[ridx[kk], cj] += np.conj(ca) * math.sqrt(ff) * 0.9",
        "rescale a(f) by 0.9, so H_N is scaled by 0.81 and the Bombieri lower "
        "bound Delta_N >= ||f||^2_Fock is violated by 19%",
    ),
    "check_fact72_takagi.py": (
        "check_fact72_takagi.py",
        "            A[i, j] += c / 2\n            A[j, i] += c / 2",
        "            A[i, j] += c\n            A[j, i] += c",
        "forget the factor 1/2 on the off-diagonal entries of the symmetric "
        "matrix of the quadric, so the Takagi values are wrong",
    ),
}


def apply_mutation(root, target, old, new):
    path = os.path.join(root, target)
    with open(path) as fh:
        src = fh.read()
    if src.count(old) != 1:
        return f"pattern occurs {src.count(old)} times in {target} (need exactly 1)"
    with open(path, "w") as fh:
        fh.write(src.replace(old, new))
    return None


def run_one(checker, spec):
    target, old, new, note = spec
    tmp = tempfile.mkdtemp(prefix="mut-")
    try:
        dst = os.path.join(tmp, "checkers")
        shutil.copytree(HERE, dst,
                        ignore=shutil.ignore_patterns("__pycache__", "logs",
                                                      "*.log"))
        err = apply_mutation(dst, target, old, new)
        if err:
            return dict(checker=checker, target=target, note=note, rc=None,
                        last=f"MUTATION NOT APPLIED: {err}", wall=0.0)
        t0 = time.time()
        p = subprocess.run(["timeout", str(BUDGET), sys.executable, "-u", checker],
                           cwd=dst, capture_output=True, text=True)
        wall = time.time() - t0
        out = (p.stdout + p.stderr).rstrip().splitlines()
        last = out[-1] if out else "(no output)"
        return dict(checker=checker, target=target, note=note, rc=p.returncode,
                    last=last, wall=wall)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def main(argv):
    md = "--md" in argv
    filt = [a for a in argv if not a.startswith("-")]
    rows, bad = [], 0
    for key, spec in MUTATIONS.items():
        checker = key.split("::")[0]
        if filt and not any(f in key for f in filt):
            continue
        r = run_one(checker, spec)
        r["key"] = key
        rows.append(r)
        ok = (r["rc"] == 1)
        if not ok:
            bad += 1
        if not md:
            print(f"{key:33s} rc={r['rc']}  {'RED' if ok else 'NOT RED'}  "
                  f"{r['wall']:6.1f}s  {r['last']}", flush=True)
    if md:
        for r in rows:
            print(f"\n### `{r['key']}`\n")
            print(f"- **Mutation** (in `{r['target']}`): {r['note']}.")
            print(f"- **Exit code**: `{r['rc']}`")
            print(f"- **Last line**: `{r['last']}`")
    print(f"\n{len(rows)} mutations run, {bad} did NOT turn the checker red")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
