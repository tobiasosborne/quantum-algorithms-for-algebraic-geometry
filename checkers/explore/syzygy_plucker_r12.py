#!/usr/bin/env python3
"""Finite checks of the R12 syzygy pair sampler, not its asymptotic lower bound.

Fock input basis is (z0²/sqrt2,z0z1,z1²/sqrt2); bath coordinates are Euclidean.
Fixed seed; q=2,4,6,8 and at most 64-dimensional two-copy matrices.
Mutations alter only the in-process model. Exit 0 pass, 1 violation, 2 error.
"""
import argparse
import itertools
import math
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from checkharness import Checker, CheckFailure


def adj(a):
    return a.conj().T


def outer(v):
    return np.outer(v, v.conj())


def unitary(rng, q):
    z = rng.normal(size=(q, q)) + 1j * rng.normal(size=(q, q))
    u, _ = np.linalg.qr(z)
    return u


def pair_law(c):
    return {pair: float(abs(np.linalg.det(c[:, pair])) ** 2)
            for pair in itertools.combinations(range(c.shape[1]), 2)}


def run(mutate):
    test = Checker("R12 syzygy Pluecker", "definitions/syzygy-plucker-r12.md")
    rng = np.random.default_rng(1207)
    for q in [2, 4, 6, 8]:
        for trial in range(4):
            full_u = unitary(rng, q)
            w, z = full_u[:, :2], full_u[:, 2:]
            c = adj(w)
            p = w @ adj(w)
            rho = p / 2
            f = np.zeros((3, q), complex)
            f[0], f[2] = c[0], c[1]
            v = f.T if mutate == "emitter-conjugation" else adj(f)
            emitted = v @ (np.eye(3) / 3) @ adj(v)
            test.close(np.linalg.norm(c @ adj(c) - np.eye(2)), 0, 1e-12, "row coisometry")
            test.close(np.linalg.norm(emitted - p / 3), 0, 1e-12, "C3-oriented bath Gram")
            test.close(np.trace(emitted).real, 2 / 3, 1e-12, "emitter success")
            test.close(np.linalg.norm(c @ z), 0, 1e-12, "constant syzygies")
            law = pair_law(c)
            test.close(sum(law.values()), 1, 1e-12, "Cauchy-Binet normalization")
            for pair, probability in law.items():
                complement = [j for j in range(q) if j not in pair]
                complementary = abs(np.linalg.det(z[complement, :])) ** 2 if complement else 1
                test.close(complementary, probability, 1e-12, "complementary syzygy Pluecker minor")
                test.close(np.linalg.det(p[np.ix_(pair, pair)]).real, probability,
                           1e-12, "projection DPP minor")

            swap = np.zeros((q * q, q * q))
            for i in range(q):
                for j in range(q):
                    swap[j * q + i, i * q + j] = 1
            p_minus = (np.eye(q * q) - swap) / (1 if mutate == "antisymmetry-scale" else 2)
            if mutate == "rank-promise" and q > 2:
                rho = full_u[:, :3] @ adj(full_u[:, :3]) / 3
            accepted = p_minus @ np.kron(rho, rho) @ p_minus
            omega = (np.kron(w[:, 0], w[:, 1]) - np.kron(w[:, 1], w[:, 0])) / np.sqrt(2)
            test.close(np.trace(accepted).real, 1 / 4, 1e-12, "swap success on flat rank two")
            test.close(np.linalg.norm(accepted - outer(omega) / 4), 0, 1e-12, "exact accepted exterior ray")
            for (i, j), probability in law.items():
                observed = accepted[i * q + j, i * q + j].real
                if mutate != "sorted-pair-factor":
                    observed += accepted[j * q + i, j * q + i].real
                test.close(4 * observed, probability, 1e-12, "sorted pair distribution")

            # Independent beamsplitter coincidence calculation, mixture over
            # the two orthonormal internal source vectors. No swap matrix used.
            coincidences = np.zeros((q, q))
            for r in range(2):
                for s in range(2):
                    sign = 1 if mutate == "hom-sign" else -1
                    amplitudes = (np.outer(w[:, r], w[:, s])
                                  + sign * np.outer(w[:, s], w[:, r])) / 2
                    coincidences += np.abs(amplitudes) ** 2 / 4
            test.close(coincidences.sum(), 1 / 4, 1e-12, "two-photon coincidence rate")
            for (i, j), probability in law.items():
                test.close(4 * (coincidences[i, j] + coincidences[j, i]), probability,
                           1e-12, "HOM generator-pair law")

    for d in [2, 3, 4, 6]:
        ua, ub = unitary(rng, d), unitary(rng, d)
        w0 = np.zeros((2 * d, 2), complex)
        w0[:d, 0], w0[d:, 1] = ua[:, 0], ub[:, 0]
        w1 = np.vstack([ua[:, :2], ub[:, :2]]) / np.sqrt(2)
        for w, expected in [(w0, 1), (w1, 1 / 2)]:
            law = pair_law(adj(w))
            cross = sum(value for (i, j), value in law.items() if i < d <= j)
            test.close(cross, expected, 1e-12, "hard-family cross-block event")

    # In the common reference transcript component, the output cannot depend
    # on the hidden partition. Check its exact combinatorial success rate.
    for d in [3, 4, 5]:
        q = 2 * d
        partitions = list(itertools.combinations(range(q), d))
        for pair in itertools.combinations(range(q), 2):
            crossings = 0
            for subset in partitions:
                hidden = set(subset)
                output = pair
                if mutate == "public-partition":
                    output = (min(hidden), min(set(range(q)) - hidden))
                crossings += ((output[0] in hidden) != (output[1] in hidden))
            test.close(crossings / len(partitions), d / (2 * d - 1), 1e-12,
                       "hidden-partition independent-reference success")

    test.close(1 - (3 / 4) ** 4, 175 / 256, 1e-12, "eight-copy generating-pair success")
    test.atleast(175 / 256, 2 / 3, "generating-pair success exceeds two thirds")
    test.close(175 / 256 - 2 / 3, 13 / 768, 1e-12, "generating-pair error margin")
    test.atmost((3 / 4) ** 4 + math.exp(-16 / 3), 1 / 3, "twenty-four raw-call failure bound")
    test.require(8 * 7 < 170 * 168 / (3 * 169), "strict eight-copy separation at q=340")
    failure = (3 / 4) ** 10
    test.atmost(failure, 1 / 16, "twenty-copy fixed-cap TV guarantee")
    test.atmost(failure + math.exp(-64 / 9), 1 / 16, "fifty raw-emitter-call TV guarantee")
    test.require(20 * 19 < 3 * 2028 / 16, "strict separation at q=2028")
    print(f"PASS: {test.count} finite checks; asymptotic lower bound remains C-362")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutate", choices=["emitter-conjugation", "antisymmetry-scale",
                                             "rank-promise", "sorted-pair-factor", "hom-sign",
                                             "public-partition"])
    args = parser.parse_args()
    try:
        run(args.mutate)
    except CheckFailure as error:
        print(f"FAIL: {error}")
        sys.exit(1)
    except Exception as error:
        print(f"ERROR: {error}")
        sys.exit(2)
