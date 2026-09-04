"""Explore exact quotient-growth identities and two obstructions (round 2).

Conventions: C1--C12, D-ground-space, D-compressed-multiplication.
Only kernels are used; generator rescaling does not affect the experiments.
No speedup or historical novelty is tested. Dense spaces have dimension <= 70.
The population-chain calculation uses <= 289 states, not an exponential Fock basis.

Run with timeout 60 python3 -B checkers/explore/quotient_growth.py.
--mutate fock, --mutate temperature, --mutate recycling must each exit 1.
"""
import argparse
import math
from pathlib import Path
import sys

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import bf


class Failure(Exception):
    pass


COUNT = 0


def check(ok, message):
    global COUNT
    COUNT += 1
    if not bool(ok):
        raise Failure(message)


def close(got, want, message, tol=2e-10):
    error = np.linalg.norm(np.asarray(got) - np.asarray(want))
    check(np.isfinite(error) and error <= tol, f"{message}: error={error:.3g}")


def kernel(gens, nv, degree):
    mat = bf.stacked_A(gens, degree)
    if mat.shape[0] == 0:
        return np.eye(bf.dim_h(nv, degree), dtype=complex)
    _, singular, vh = np.linalg.svd(mat, full_matrices=True)
    rank = int(np.count_nonzero(singular > 1e-10 * max(1.0, singular[0])))
    return vh.conj().T[:, rank:]


def lower(nv, degree, mode, mutation=None):
    alpha = tuple(int(j == mode) for j in range(nv))
    mat = bf.annihilation_matrix({alpha: 1}, degree)
    if mutation == "fock":
        mat = mat * mat  # Defect: falling factorial, not its square root.
    return mat


def growth(mutation):
    families = [
        ("double point", 2, [{(2, 0): 1}]),
        ("conic", 3, [{(1, 1, 0): 1, (0, 0, 2): -1}]),
        ("complex quadric", 3, [{(2, 0, 0): 1j, (1, 1, 0): 2, (0, 0, 2): 1-1j}]),
        ("twisted cubic", 4, bf.minors2x2(4, [0, 1, 2], [1, 2, 3])),
    ]
    for name, nv, gens in families:
        for degree in range(4):
            w = kernel(gens, nv, degree)
            v = kernel(gens, nv, degree + 1)
            pn, pp = w @ w.conj().T, v @ v.conj().T
            image = np.zeros_like(pp)
            source_effect = np.zeros_like(pn)
            for mode in range(nv):
                a = lower(nv, degree + 1, mode, mutation)
                close((np.eye(len(pn)) - pn) @ a @ pp, 0,
                      f"{name}/{degree}: differentiation preserves inverse system")
                z = pp @ a.conj().T @ pn
                image += z @ z.conj().T
                source_effect += pn @ a @ a.conj().T @ pn
            close(source_effect, (degree + nv) * pn,
                  f"{name}/{degree}: addition-channel normalization")
            close(image, (degree + 1) * pp, f"{name}/{degree}: uniform-growth identity")
            q = float(np.trace(image).real / ((degree + nv) * w.shape[1]))
            expected = (degree + 1) * v.shape[1] / ((degree + nv) * w.shape[1])
            close(q, expected, f"{name}/{degree}: acceptance probability")
            close(image / np.trace(image), pp / v.shape[1],
                  f"{name}/{degree}: conditional output is uniform")
        print(f"growth identities: {name}: PASS")
    for nv in (2, 4, 8, 16, 32):
        product = math.prod((nv-k)/(nv+k) for k in range(nv))
        expected = 1 / math.comb(2*nv - 1, nv)
        close(product / expected, 1, f"squarefree CI/{nv}: telescoping cost")
        print(f"squarefree CI: variables={nv:2d}, final success={product:.8g}")


def recycling(mutation):
    gens, nv, degree = [{(2, 0): 1}], 2, 1
    w, v = kernel(gens, nv, degree), kernel(gens, nv, degree + 1)
    pn, pp = w @ w.conj().T, v @ v.conj().T
    effect = np.zeros_like(pn)
    for mode in range(nv):
        a = lower(nv, degree + 1, mode)
        effect += pn @ a @ pp @ a.conj().T @ pn / (degree + nv)
    if mutation == "recycling":
        effect = np.trace(effect) / w.shape[1] * pn  # Defect: assume scalar backaction.
    close(effect, np.diag([1/3, 1]), "double point: acceptance effect")
    source = pn / w.shape[1]
    failure = source - effect / w.shape[1]
    close(np.trace(failure), 1/3, "double point: failure probability")
    close(failure / np.trace(failure), np.diag([1, 0]), "double point: biased Lueders source posterior")
    print("recycling obstruction: effect=diag(1/3,1), Lueders failure posterior=|x><x|: PASS")


def thermal(mutation):
    nv, cap, temperature = 2, 4, 0.5
    gens = [{(2, 0): 1}]
    blocks = [kernel(gens, nv, k) for k in range(cap + 1)]
    sizes = [w.shape[1] for w in blocks]
    offsets = np.cumsum([0] + sizes)
    weights = np.concatenate([np.full(size, temperature**k) for k, size in enumerate(sizes)])
    rho = np.diag(weights / weights.sum()).astype(complex)
    residual = np.zeros_like(rho)
    for mode in range(nv):
        creation = np.zeros_like(rho)
        for k in range(cap):
            a = lower(nv, k + 1, mode)
            z = blocks[k+1].conj().T @ a.conj().T @ blocks[k]
            creation[offsets[k+1]:offsets[k+2], offsets[k]:offsets[k+1]] = z
        up = temperature if mutation == "temperature" else math.sqrt(temperature)
        for jump in (up * creation, creation.conj().T):
            square = jump.conj().T @ jump
            residual += jump @ rho @ jump.conj().T - (square @ rho + rho @ square) / 2
    close(residual, 0, "Hilbert-series stationary-state identity")
    print("Hilbert-series reservoir: truncated exact stationarity: PASS")


def branch_chain(a, b, cap, temperature):
    size = 2*cap + 1
    rates = np.zeros((size, size))  # Row generator: distributions evolve as p Q.
    weights = np.ones(size)
    for offset, modes in ((0, a), (cap, b)):
        rates[0, offset+1] = temperature*modes
        for k in range(1, cap+1):
            index = offset+k
            previous = 0 if k == 1 else index-1
            rates[index, previous] = k
            if k < cap:
                rates[index, index+1] = temperature*(k+modes)
            weights[index] = math.comb(k+modes-1, k)*temperature**k
    rates[np.diag_indices(size)] = -rates.sum(axis=1)
    return rates, weights / weights.sum()


def bottleneck():
    for a in (4, 8, 12, 16):
        b, cap, temperature = 2*a, 8*a, 0.5
        generator, pi = branch_chain(a, b, cap, temperature)
        close(pi @ generator, 0, f"two components/{a}: stationarity")
        close(pi[:, None]*generator, pi[None, :]*generator.T,
              f"two components/{a}: detailed balance")
        indicator = np.zeros(len(pi))
        indicator[1:cap+1] = 1
        mass = float(pi @ indicator)
        centered = indicator - mass
        variance = float(pi @ (centered**2))
        energy = -float((pi*centered) @ generator @ centered)
        rayleigh = energy / variance
        left_partition = sum(math.comb(k+a-1, k)*temperature**k for k in range(1, cap+1))
        bound = temperature*a / (left_partition*(1-mass))
        close(rayleigh / bound, 1, f"two components/{a}: variational gap upper bound")
        check(0 < mass < 0.5, f"two components/{a}: smaller branch has mass < 1/2")
        print(f"two components: dims={a},{b}, cap={cap}, small mass={mass:.7g}, gap <= {bound:.7g}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutate", choices=("fock", "temperature", "recycling"))
    args = parser.parse_args()
    try:
        growth(args.mutate)
        recycling(args.mutate)
        thermal(args.mutate)
        bottleneck()
    except Failure as exc:
        print(f"FAIL: {exc}")
        return 1
    print(f"PASS: {COUNT} checks; identities and obstructions only, no speedup claim")
    return 0


if __name__ == "__main__":
    sys.exit(main())
