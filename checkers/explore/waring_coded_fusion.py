#!/usr/bin/env python3
"""Finite, red-capable checks for coded determinant packet fusion.

Ordinary tensor norms, departing from C1. Caps r<=5, explicit seed r=3,k=4
(3**12 amplitudes), and at most (5!)**2 labeling pairs. Run under timeout 60
with one BLAS thread. No originality, classical advantage or global optimality
is established by these checks. Reference: scouting/waring-coded-fusion.md.
"""
import argparse
from itertools import permutations
from math import factorial
from pathlib import Path
import sys

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from checkharness import main


def parity(word):
    return (-1)**sum(word[i] > word[j] for i in range(len(word)) for j in range(i + 1, len(word)))


def tensor(vectors):
    result = np.ones(1, dtype=complex)
    for vector in vectors:
        result = np.kron(result, vector)
    return result


def antisymmetrize(state, axes):
    result = np.zeros_like(state)
    for perm in permutations(range(len(axes))):
        order = list(range(state.ndim))
        for j, axis in enumerate(axes):
            order[axis] = axes[perm[j]]
        result += parity(perm) * state.transpose(order)
    return result / factorial(len(axes))


def packet_gram(gram, degree, labels):
    indices = np.array(labels)
    overlaps = gram[indices[:, None, :], indices[None, :, :]]
    return np.prod(overlaps**degree, axis=2)


def permanent(matrix, labels):
    return sum(np.prod(matrix[np.arange(len(matrix)), perm]) for perm in labels)


def packet_norm_formula(gram, degree, sign, labels):
    powered = gram**degree
    immanant = np.linalg.det(powered) if sign else permanent(powered, labels)
    return float((factorial(len(gram)) * immanant).real)


def body(ck, mutation):
    rng = np.random.default_rng(20260905)
    for rank in range(2, 6):
        labels = list(permutations(range(rank)))
        signs = np.array([parity(word) for word in labels])
        bits = (rank - 1).bit_length()
        used_bits = bits - 1 if mutation == "drop-guard" and rank >= 4 else bits
        survivors = []
        for left in labels:
            for right in labels:
                phase = 1
                for bit in range(used_bits):
                    edge = tuple(left[i] if i >> bit & 1 else right[i] for i in range(rank))
                    if len(set(edge)) != rank:
                        break
                    phase *= parity(edge)
                else:
                    if mutation == "drop-phase" and rank >= 4:
                        phase = 1
                    survivors.append((left, right, phase))
        ck.equal(len(survivors), factorial(rank), f"exact number of synchronized labelings r={rank}")
        for left, right, phase in survivors:
            ck.equal(left, right, f"survival forces the same component labeling r={rank}")
            ck.equal(phase, parity(left)**bits, f"determinant phase r={rank}")
        for row in range(rank):
            left_used = sum(row >> bit & 1 for bit in range(bits))
            right_used = bits - left_used
            ck.equal(left_used + right_used, bits, "uniform per-row consumption")
        # Independent necessity witness: removing any final bit leaves a repeated signature.
        signatures = [row % (2**(bits - 1)) for row in range(rank)]
        ck.require(len(set(signatures)) < rank, "fewer binary guards leave an indistinguishable pair")

        frame = np.eye(rank, dtype=complex) + 0.15 * (rng.normal(size=(rank, rank)) + 1j*rng.normal(size=(rank, rank)))
        frame /= np.linalg.norm(frame, axis=0)
        gram = frame.conj().T @ frame
        wedge = antisymmetrize(tensor(frame[:, i] for i in range(rank)).reshape([rank] * rank), list(range(rank)))
        actual_edge = np.vdot(wedge, wedge).real
        assumed_edge = np.linalg.det(gram).real / (1 if mutation == "drop-factorial" else factorial(rank))
        ck.close(actual_edge, assumed_edge, 2e-12, f"literal exterior projector norm r={rank}")
        m, n = bits + 1, bits + 2
        output_degree = m + n - bits
        for sign_a in (0, 1):
            for sign_b in (0, 1):
                sign_out = (sign_a + sign_b + bits) % 2
                norm_a = packet_norm_formula(gram, m, sign_a, labels)
                norm_b = packet_norm_formula(gram, n, sign_b, labels)
                norm_out = packet_norm_formula(gram, output_degree, sign_out, labels)
                for degree, sign, expected in ((m, sign_a, norm_a), (n, sign_b, norm_b), (output_degree, sign_out, norm_out)):
                    coefficients = signs**sign
                    actual = (coefficients @ packet_gram(gram, degree, labels) @ coefficients).real
                    ck.close(actual, expected, 2e-9, f"direct labeling Gram norm r={rank},degree={degree},sign={sign}")
                output_coefficients = np.array([parity(left)**sign_a * parity(right)**sign_b * phase for left, right, phase in survivors])
                direct_output_norm = (output_coefficients @ packet_gram(gram, output_degree, labels) @ output_coefficients).real
                actual_probability = actual_edge**bits * direct_output_norm / (norm_a * norm_b)
                predicted_probability = assumed_edge**bits * norm_out / (norm_a * norm_b)
                ck.close(actual_probability, predicted_probability, 1e-12, f"full coherent successful-label sum r={rank},signs={sign_a,sign_b}")
                ck.between(actual_probability, 0, 1, "physical fusion probability")
        orthogonal_probability = (1/factorial(rank))**bits / factorial(rank)
        ck.close(orthogonal_probability, factorial(rank)**(-bits-1), 1e-14, "orthogonal cost formula")
        ck.info(f"r={rank}, guards={bits}, orthogonal fusion probability={orthogonal_probability:.12g}")

    rank, degree = 3, 4
    frame = np.eye(rank, dtype=complex) + 0.12 * (rng.normal(size=(rank, rank)) + 1j*rng.normal(size=(rank, rank)))
    frame /= np.linalg.norm(frame, axis=0)
    gram = frame.conj().T @ frame
    coefficients = np.array([1, 0.7+0.2j, -0.5+0.4j])
    source = sum(coefficients[i] * tensor([frame[:, i]] * degree) for i in range(rank))
    coefficients /= np.linalg.norm(source)
    source /= np.linalg.norm(source)
    copies = tensor([source] * rank).reshape([rank] * (rank * degree))
    projected = antisymmetrize(copies, [degree*i for i in range(rank)])
    observed_seed = np.vdot(projected, projected).real
    predicted_seed = np.prod(abs(coefficients)**2) * np.linalg.det(gram) * np.linalg.det(gram**(degree - 1))
    ck.close(observed_seed, predicted_seed.real, 2e-12, "literal three-copy quantum seed vs determinant formula")
    rho_one = source.reshape(rank, -1) @ source.reshape(rank, -1).conj().T
    ck.close(observed_seed, np.linalg.det(rho_one).real, 2e-12, "seed equals product of marginal eigenvalues")
    ck.atmost(observed_seed, rank**(-rank), "universal seed-probability upper bound")
    ck.equal(2 * 4**5 * factorial(4)**3, 28311552, "rank-four expected copies through first merge")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mutation", choices=("drop-guard", "drop-phase", "drop-factorial"))
    args = parser.parse_args()
    sys.exit(main("waring_coded_fusion", "Proposed coded synchronization, phases and normalization; no speedup claim", lambda ck: body(ck, args.mutation)))
