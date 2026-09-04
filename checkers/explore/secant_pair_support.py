#!/usr/bin/env python3
"""Red-capable checks for the proposed S4 pair-support gap (finite evidence).

Ordinary tensor inner products, departing from C1. Independent permutation
matrices are compared with the analytic small-block formula in
scouting/secant-pair-support.md. Caps: 6 repeated standard factors (64-square
matrices), symmetric power degree 16, one BLAS thread, timeout 60.
"""
import argparse
from functools import lru_cache
from itertools import permutations
from math import comb, sqrt
from pathlib import Path
import sys

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from checkharness import main


def tensor_power(matrix, count):
    result = np.ones((1, 1))
    for _ in range(count):
        result = np.kron(result, matrix)
    return result


def symmetric_power(matrix, degree):
    a, b, c, d = matrix.reshape(-1)
    result = np.zeros((degree + 1, degree + 1))
    for j in range(degree + 1):
        for k in range(degree + 1):
            result[k, j] = sqrt(comb(degree, j) / comb(degree, k)) * sum(
                comb(degree - j, k - ell) * comb(j, ell)
                * a**(degree - j - k + ell) * c**(k - ell)
                * b**(j - ell) * d**ell
                for ell in range(max(0, k - degree + j), min(j, k) + 1)
            )
    return result


def dicke_isometry(degree):
    result = np.zeros((2**degree, degree + 1))
    for word in range(2**degree):
        weight = word.bit_count()
        result[word, weight] = 1 / sqrt(comb(degree, weight))
    return result


def group_compressions():
    plane = np.array([[0.5, 0], [0.5, 0], [-0.5, 1/sqrt(2)], [-0.5, -1/sqrt(2)]])
    normal = np.array([1, -1, 0, 0]) / sqrt(2)
    matching = {frozenset((0, 1)), frozenset((2, 3))}
    result = []
    for perm in permutations(range(4)):
        action = np.eye(4)[:, perm]
        sign = (-1)**sum(perm[i] > perm[j] for i in range(4) for j in range(i + 1, 4))
        standard = plane.T @ action @ plane
        alternating_standard = sign * (normal @ action @ normal)
        image = {frozenset((perm[0], perm[1])), frozenset((perm[2], perm[3]))}
        two_rows = 1.0 if image == matching else -0.5
        result.append((standard, alternating_standard, two_rows))
    return result


@lru_cache(None)
def central_power(degree):
    return symmetric_power(np.array([[0, 1/sqrt(2)], [1/sqrt(2), 0.5]]), degree)


def formula(degree, h, c, mutation=None):
    parity = np.diag([int(j % 2 == h % 2) for j in range(degree + 1)])
    rank_one = np.zeros((degree + 1, degree + 1))
    if h == 0:
        rank_one[0, 0] = (-1)**degree / 6
    if mutation == "drop-kernel-term":
        rank_one *= 0
    sign_base = 0.5 if mutation == "wrong-phase" else -0.5
    return parity / 6 + rank_one + (2/3) * sign_base**(h+c) * parity @ central_power(degree) @ parity


def body(ck, mutation):
    group = group_compressions()
    ck.equal(len(group), 24, "all S4 permutations")
    for matrix, sign_line, _ in group:
        ck.close(np.linalg.det(matrix), sign_line, 2e-12, "cofactor identity for sign-twisted standard line")
    matrix = np.array([[0.2, -0.3], [0.7, 0.4]])
    for degree in range(7):
        dicke = dicke_isometry(degree)
        actual = dicke.T @ tensor_power(matrix, degree) @ dicke
        ck.close(np.linalg.norm(actual - symmetric_power(matrix, degree)), 0, 2e-12, f"normalized symmetric power vs explicit tensor at degree {degree}")
    for a in range(7):
        for b in range(3):
            for c in range(3):
                actual = sum(line**b * match**c * tensor_power(matrix, a) for matrix, line, match in group) / 24
                expected_values = []
                for j in range(a // 2 + 1):
                    multiplicity = comb(a, j) - (comb(a, j-1) if j else 0)
                    block = formula(a - 2*j, j + b, c, mutation)
                    expected_values.extend(np.linalg.eigvalsh(block).tolist() * multiplicity)
                expected_values = np.sort(expected_values)
                actual_values = np.linalg.eigvalsh((actual + actual.T) / 2)
                ck.equal(len(expected_values), 2**a, "party Schur multiplicities exhaust the compressed space")
                ck.close(np.linalg.norm(expected_values - actual_values), 0, 2e-10, f"full permutation spectrum vs analytic blocks a,b,c={a,b,c}")
    blocks = 0
    smallest = 1.0
    for degree in range(17):
        for h in range(5):
            for c in range(5):
                matrix = formula(degree, h, c, mutation)
                values = np.linalg.eigvalsh((matrix + matrix.T) / 2)
                ck.atleast(values.min(), -2e-10, f"positivity at {degree,h,c}")
                ck.atmost(values.max(), 1 + 2e-10, f"contraction at {degree,h,c}")
                positive = values[values > 1e-8]
                if positive.size:
                    ck.atleast(positive.min(), 1/12 - 2e-10, f"nonzero gap at {degree,h,c}")
                    smallest = min(smallest, positive.min())
                blocks += 1
    ck.close(formula(0, 2, 1, mutation)[0, 0], 1/12, 2e-12, "sharp pattern 211,211,22")
    ck.info(f"Verified {blocks} analytic blocks; smallest positive eigenvalue {smallest:.15g}.")
    ck.info("Finite numerical evidence only; the analytic proof decides exact kernels.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mutation", choices=("drop-kernel-term", "wrong-phase"))
    args = parser.parse_args()
    sys.exit(main("secant_pair_support", "Proposed exact S4 compression and uniform 1/12 gap", lambda ck: body(ck, args.mutation)))
