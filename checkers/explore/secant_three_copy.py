#!/usr/bin/env python3
"""Bounded checks of the proposed cubic secant projector, not a speedup proof.

Uses ordinary tensor inner products (departure from campaign C1), qubit factors,
and definitions/secant-three-copy.md. At most 6 sites, arrays <= 8**6 entries.
Run with timeout 60 and one BLAS thread. Optional mutations must exit 1.
"""
import argparse
import itertools
import pathlib
import sys

import numpy as np

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from checkharness import main


def schur_matrix():
    mat = np.zeros((8, 8))
    mat[0, 0] = mat[3, 7] = 1
    for weight, positions in enumerate(([4, 2, 1], [3, 5, 6])):
        mat[1 + weight, positions] = 1 / np.sqrt(3)
        mat[4 + 2 * weight, positions] = np.array([2, -1, -1]) / np.sqrt(6)
        mat[5 + 2 * weight, positions] = np.array([0, 1, -1]) / np.sqrt(2)
    return mat


def trine_cat(m, mutation=None):
    vectors = np.array([[1, 0], [-0.5, np.sqrt(3) / 2], [-0.5, -np.sqrt(3) / 2]])
    if mutation == "trine-sign":
        vectors[2, 0] = 0.5
    terms = []
    for vector in vectors:
        term = np.ones(1)
        for _ in range(m):
            term = np.kron(term, vector)
        terms.append(term)
    norm_sq = 3 + 6 * (-0.5) ** m
    if mutation == "normalization":
        norm_sq = 3
    return np.sum(terms, axis=0) / np.sqrt(norm_sq), terms


def cubic_acceptance(psi, n, mutation=None, return_random=False):
    state = np.einsum("i,j,k->ijk", psi, psi, psi).reshape([2] * (3 * n))
    axes = [j for i in range(n) for j in (i, n + i, 2 * n + i)]
    state = state.transpose(axes).reshape([8] * n)
    mat = schur_matrix()
    for i in range(n):
        state = np.moveaxis(np.tensordot(mat, state, axes=(1, i)), 0, i)
    acceptance = 0.0
    random_rejection = 0.0
    for pattern in itertools.product((0, 1), repeat=n):
        m = sum(pattern)
        if m == 1:
            continue
        block = state
        dimensions, multiplicity_axes = [], []
        for i, is_standard in enumerate(pattern):
            block = np.take(block, range(4 * is_standard, 4 * is_standard + 4), axis=i)
            if is_standard:
                dimensions.extend((2, 2))
                multiplicity_axes.append(len(dimensions) - 1)
            else:
                dimensions.append(4)
        other_axes = [i for i in range(len(dimensions)) if i not in multiplicity_axes]
        block = block.reshape(dimensions).transpose(other_axes + multiplicity_axes).reshape(-1, 2**m)
        if m == 0:
            sector_acceptance = np.vdot(block, block).real
        else:
            cat, terms = trine_cat(m, mutation)
            if mutation == "dephase-cat":
                sector_acceptance = sum(np.linalg.norm(block @ term) ** 2 for term in terms) / 3
            else:
                sector_acceptance = np.linalg.norm(block @ cat.conj()) ** 2
        acceptance += sector_acceptance
        coefficient = (1 + 2 * (-0.5)**m) / 6
        if mutation == "cut-coefficient":
            coefficient = 1 / 6
        random_rejection += coefficient * (np.vdot(block, block).real - sector_acceptance)
    if return_random:
        return float(acceptance), float(random_rejection)
    return float(acceptance)


def product(rng, n):
    out = np.ones(1, dtype=complex)
    for _ in range(n):
        local = rng.normal(size=2) + 1j * rng.normal(size=2)
        out = np.kron(out, local / np.linalg.norm(local))
    return out


def normalize(state):
    return state / np.linalg.norm(state)


def all_cut_rejection(psi, n):
    results = []
    for mask in range(1, 2**n - 1):
        left = [i for i in range(n) if mask >> i & 1]
        right = [i for i in range(n) if not (mask >> i & 1)]
        matrix = psi.reshape([2] * n).transpose(left + right).reshape(2**len(left), -1)
        values = np.linalg.svd(matrix, compute_uv=False) ** 2
        # Independent determinantal expression e_3 of the Schmidt probabilities.
        results.append(sum(np.prod(values[list(indices)]) for indices in itertools.combinations(range(len(values)), 3)))
    return results


def local_unitary(rng, psi, n):
    state = psi.reshape([2] * n)
    for i in range(n):
        matrix = rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2))
        unitary, _ = np.linalg.qr(matrix)
        state = np.moveaxis(np.tensordot(unitary, state, axes=(1, i)), 0, i)
    return state.reshape(-1)


def body(ck, mutation):
    rng = np.random.default_rng(20260905)
    mat = schur_matrix()
    ck.close(np.linalg.norm(mat @ mat.T - np.eye(8)), 0, 1e-12, "local Schur orthogonality")
    for m in range(2, 11):
        cat, _ = trine_cat(m, mutation)
        ck.close(np.vdot(cat, cat).real, 1, 2e-12, f"cat normalization m={m}")
        # The cat has Schmidt rank at most three, so constant-memory synthesis exists.
        split = m // 2
        singular = np.linalg.svd(cat.reshape(2**split, -1), compute_uv=False)
        ck.atmost(np.linalg.norm(singular[3:]), 1e-12, f"cat bond dimension m={m}")
    for n in range(2, 7):
        for trial in range(3):
            psi = normalize(product(rng, n) + (0.7 + 0.3j) * product(rng, n))
            ck.close(cubic_acceptance(psi, n, mutation), 1, 2e-11, f"complex nonorthogonal rank-two n={n}, trial={trial}")
        tangent = np.zeros(2**n)
        tangent[[2**i for i in range(n)]] = 1 / np.sqrt(n)
        ck.close(cubic_acceptance(tangent, n, mutation), 1, 2e-11, f"W tangent border-rank-two n={n}")
    for n in (3, 4, 5):
        values = []
        for trial in range(4):
            psi = normalize(rng.normal(size=2**n) + 1j * rng.normal(size=2**n))
            accept, predicted_random = cubic_acceptance(psi, n, mutation, return_random=True)
            ck.between(accept, -1e-12, 1 + 1e-12, f"probability n={n}")
            if n == 3:
                ck.close(accept, 1, 2e-11, "secant fills three-qubit ambient space")
            else:
                ck.atmost(accept, 0.999, f"generic nonmember rejected n={n}")
            rotated = local_unitary(rng, psi, n)
            ck.close(cubic_acceptance(rotated, n, mutation), accept, 2e-11, f"local-unitary invariance n={n}")
            cuts = all_cut_rejection(psi, n)
            actual_random = sum(cuts) / 2**n  # Empty/full cuts have zero rejection.
            ck.close(predicted_random, actual_random, 2e-11, f"independent all-cut average vs Schur coefficient n={n}")
            ck.atleast(actual_random, (1 - accept) / 8 - 2e-11, f"known random-cut test matches within factor eight n={n}")
            ck.atmost(max(cuts), 1 - accept + 2e-11, f"optimal cubic rejection dominates every cut n={n}")
            values.append(1 - accept)
        ck.info(f"n={n}: generic cubic rejection = {values}")
    bells = np.zeros(16)
    bells[[0, 3, 12, 15]] = 0.5
    rejection = 1 - cubic_acceptance(bells, 4, mutation)
    ck.atleast(rejection, 0.01, "two Bell pairs are outside the secant")
    ck.info(f"Two Bell pairs: cubic rejection {rejection:.12g}; max cut exterior rejection {max(all_cut_rejection(bells, 4)):.12g}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mutation", choices=("trine-sign", "normalization", "dephase-cat", "cut-coefficient"))
    args = parser.parse_args()
    sys.exit(main("secant_three_copy", "C-335 candidate exact cubic projector; no robustness/separation inference", lambda ck: body(ck, args.mutation)))
