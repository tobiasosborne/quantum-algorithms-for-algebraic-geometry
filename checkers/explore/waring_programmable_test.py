#!/usr/bin/env python3
"""Bounded literal quantum checks of the direct Waring component tester.

Ordinary tensor norms, departing from C1. Caps: r=q<=3, k=3, at most 3**12
amplitudes. Tests use a degree-two point projector to verify the general
construction; the terminal degree-five guarantee is analytic. Run with one
BLAS thread and timeout 60. No originality claim is tested.
"""
import argparse
from fractions import Fraction
from itertools import permutations
from math import factorial
from pathlib import Path
import sys

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from checkharness import main
from waring_coded_fusion import antisymmetrize, tensor


def experiment(frame, weights, mutation):
    q, rank = frame.shape
    order = 3
    gram = frame.conj().T @ frame
    source = sum(weights[a] * tensor([frame[:, a]] * order) for a in range(rank))
    source_norm = np.linalg.norm(source)
    source /= source_norm
    coefficients = weights / source_norm
    whole = tensor([source] * (rank + 1)).reshape([q] * (order * (rank + 1)))
    seed_axes = [order*a for a in range(rank)]
    after_seed = whole if mutation == "skip-seed" else antisymmetrize(whole, seed_axes)
    guard_axes = [order*a + 1 for a in range(1, rank)] + [order*rank]
    if mutation == "drop-program-row":
        guard_axes = guard_axes[1:]
    after_guard = antisymmetrize(after_seed, guard_axes)
    point_vector = np.zeros((q, q), dtype=complex)
    point_vector[0, 1] = point_vector[1, 0] = 1 / np.sqrt(2)
    # Take one target slot from the selected old row and one from the new copy.
    target_axes = [1, order*rank + 1]
    contracted = np.tensordot(point_vector.conj(), after_guard, axes=([0, 1], target_axes))
    observed = np.vdot(contracted, contracted).real
    point_amplitudes = np.array([np.vdot(point_vector.reshape(-1), tensor([frame[:, a]] * 2)) for a in range(rank)])
    point_residual = float(np.mean(abs(point_amplitudes)**2))

    labels = np.array(list(permutations(range(rank))))
    selected = labels[:, 0]
    program = gram[labels[:, None, 1:], labels[None, :, 1:]]
    program_gram = np.prod(program**(order - 2), axis=2)
    target_gram = point_amplitudes[selected].conj()[:, None] * point_amplitudes[selected][None, :]
    target_gram *= gram[selected[:, None], selected[None, :]]**(2*order - 4)
    amplitude_coefficients = coefficients[selected]
    norm_after_point = (amplitude_coefficients.conj() @ (program_gram * target_gram) @ amplitude_coefficients).real
    det_gram = np.linalg.det(gram).real
    normalization = factorial(rank) if mutation != "drop-factorial" else 1
    predicted = np.prod(abs(coefficients)**2) * (det_gram/normalization)**2 * norm_after_point
    seed_probability = np.prod(abs(coefficients)**2) * det_gram * np.linalg.det(gram**(order - 1)).real
    return observed, predicted, point_residual, gram, program_gram, coefficients, seed_probability


def body(ck, mutation):
    rng = np.random.default_rng(20260905)
    for rank in (2, 3):
        for trial in range(4):
            frame = np.eye(rank, dtype=complex)
            weights = np.ones(rank, dtype=complex)
            if trial:
                frame += 0.12 * (rng.normal(size=(rank, rank)) + 1j*rng.normal(size=(rank, rank)))
                frame /= np.linalg.norm(frame, axis=0)
                weights += 0.2 * (rng.normal(size=rank) + 1j*rng.normal(size=rank))
            observed, predicted, residual, gram, program, coefficients, pseed = experiment(frame, weights, mutation)
            ck.close(observed, predicted, 2e-12, f"literal two-guard source circuit vs label Gram formula r={rank},trial={trial}")
            ck.between(observed, -1e-14, 1+1e-14, "physical joint event probability")
            if trial == 0:
                ck.close(residual, 0, 1e-15, "coordinate components satisfy point equation")
                ck.close(observed, 0, 1e-14, "perfect completeness, including coherent source cross terms")
            else:
                ck.atleast(observed, 1e-9, "generic violated component gives observable joint event")
            eta = np.linalg.eigvalsh(gram).min()
            ck.atleast(eta, 0.1, "conditioned frame fixture")
            ck.atleast(np.linalg.eigvalsh(program).min(), eta**(rank-1)-2e-12, "injective program Gram lower bound")
            ck.atmost(np.sum(abs(coefficients)**2), 1/eta+2e-12, "source coefficient norm bound")
            ck.atleast(min(abs(coefficients)**2), pseed*(eta*(rank-1))**(rank-1)-2e-12, "smallest weight from seed/Gram promises")
            lower = pseed**2 * eta**(3*rank-2) * (rank-1)**(rank-1) / factorial(rank) * residual
            ck.atleast(observed, lower-2e-12, "general normalized geometric residual lower bound")
            ck.info(f"r={rank}, trial={trial}: joint event={observed:.10g}, residual={residual:.10g}")
    coefficient = Fraction(1, 512)**2 * Fraction(1, 2)**10 * Fraction(27, 24)
    ck.equal(coefficient, Fraction(9, 2**31), "rank-four exact lower coefficient")
    ck.equal(Fraction(1, 4**5 * factorial(4)), Fraction(1, 24576), "orthogonal equal-weight exact coefficient")
    # Exact moment equality and root brackets for the terminal problem's fixed spectra.
    def polynomial(x):
        value = x
        for j in range(1, 5):
            value *= x-Fraction(j, 10)
        return value-Fraction(1, 10**6)
    for lo, hi in ((0, 1), (9, 11), (19, 21), (29, 31), (39, 41)):
        ck.require(polynomial(Fraction(lo, 100))*polynomial(Fraction(hi, 100)) < 0, f"positive NO-spectrum root interval {lo}/100,{hi}/100")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mutation", choices=("skip-seed", "drop-program-row", "drop-factorial"))
    args = parser.parse_args()
    sys.exit(main("waring_programmable_test", "Direct component-property event and lower bound, not novelty", lambda ck: body(ck, args.mutation)))
