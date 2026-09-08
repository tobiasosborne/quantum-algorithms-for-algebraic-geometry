#!/usr/bin/env python3
"""Finite diagnostics for the R13 growing-rank syzygy basis compiler.

This independently assembles small source, permutation, projected-unitary,
Lueders-bank and certificate matrices.  It does not prove the asymptotic
Haar/Gaussian transcript lower bound, QSVT phase synthesis, or advantage.
Fixed seed; largest matrix dimension is 512.  Mutations alter only this
in-process model.  Exit 0 means all stated finite checks passed; 1 means a
modeled property failed; 2 means the checker could not run.
"""
import argparse
import itertools
import math
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from checkharness import Checker, CheckFailure


def adj(matrix):
    return matrix.conj().T


def outer(vector):
    return np.outer(vector, vector.conj())


def random_isometry(rng, rows, columns):
    matrix = rng.normal(size=(rows, columns)) + 1j * rng.normal(size=(rows, columns))
    frame, _ = np.linalg.qr(matrix)
    return frame


def hadamard_power(size):
    matrix = np.array([[1.0]])
    gate = np.array([[1.0, 1.0], [1.0, -1.0]]) / np.sqrt(2)
    while matrix.shape[0] < size:
        matrix = np.kron(matrix, gate)
    return matrix


def permutation_sign(permutation):
    inversions = sum(permutation[i] > permutation[j]
                     for i in range(len(permutation))
                     for j in range(i + 1, len(permutation)))
    return -1 if inversions % 2 else 1


def tensor_permutation(local_dimension, factors, permutation):
    dimension = local_dimension ** factors
    matrix = np.zeros((dimension, dimension), complex)
    shape = (local_dimension,) * factors
    for column in range(dimension):
        coordinates = np.unravel_index(column, shape)
        output = tuple(coordinates[permutation[j]] for j in range(factors))
        row = np.ravel_multi_index(output, shape)
        matrix[row, column] = 1
    return matrix


def swap_operator(local_dimension, factors, first, second):
    permutation = list(range(factors))
    permutation[first], permutation[second] = permutation[second], permutation[first]
    return tensor_permutation(local_dimension, factors, tuple(permutation))


def spectral_projectors(operator, labels):
    values, vectors = np.linalg.eigh(operator)
    projectors = {}
    for label in labels:
        mask = np.abs(values - label) < 1e-9
        projectors[label] = vectors[:, mask] @ adj(vectors[:, mask])
    return values, projectors


def padded_jm_encoding(x_operator, k, mutation):
    h = k - 1
    bank = 1 << math.ceil(math.log2(h))
    data_dimension = x_operator.shape[0]
    signal_x = np.array([[0, 1], [1, 0]], complex)
    signal_i = np.eye(2)
    select = np.zeros((bank * data_dimension * 2,) * 2, complex)
    for label in range(bank):
        if label < h:
            data_action = swap_operator(2, int(round(math.log2(data_dimension))), label, k - 1)
            block = np.kron(data_action, signal_i)
        else:
            if mutation == "padded-block":
                block = np.kron(np.eye(data_dimension), signal_i)
            else:
                block = np.kron(np.eye(data_dimension), signal_x)
        start = label * data_dimension * 2
        select[start:start + data_dimension * 2, start:start + data_dimension * 2] = block
    prepare = np.kron(hadamard_power(bank), np.eye(data_dimension * 2))
    encoded = adj(prepare) @ select @ prepare
    clean = np.array([(0 * data_dimension + index) * 2 for index in range(data_dimension)])
    return bank, select, encoded, clean


def shifted_encoding(encoded, clean, threshold, mutation):
    total_dimension = encoded.shape[0]
    magnitude = abs(threshold)
    first = math.sqrt(1 / (1 + magnitude))
    second = math.sqrt(magnitude / (1 + magnitude))
    prepare = np.array([[first, -second], [second, first]], complex)
    sign = 1 if threshold > 0 else -1
    scalar = sign if mutation == "shift-sign" else -sign
    select = np.zeros((2 * total_dimension,) * 2, complex)
    select[:total_dimension, :total_dimension] = encoded
    select[total_dimension:, total_dimension:] = scalar * np.eye(total_dimension)
    full_prepare = np.kron(prepare, np.eye(total_dimension))
    shifted = adj(full_prepare) @ select @ full_prepare
    shifted_clean = clean.copy()
    return select, shifted, shifted_clean


def antisymmetrizer(local_dimension, rank, mutation=None):
    total = np.zeros((local_dimension ** rank,) * 2, complex)
    permutations = list(itertools.permutations(range(rank)))
    for permutation in permutations:
        total += permutation_sign(permutation) * tensor_permutation(
            local_dimension, rank, permutation)
    denominator = math.sqrt(math.factorial(rank)) if mutation == "antisymmetry-normalization" \
        else math.factorial(rank)
    return total / denominator, permutations


def balanced_partitions(total, groups, group_size):
    labels = tuple(range(total))

    def recurse(remaining, number):
        if number == 1:
            yield (tuple(remaining),)
            return
        for chosen in itertools.combinations(remaining, group_size):
            chosen_set = set(chosen)
            rest = tuple(value for value in remaining if value not in chosen_set)
            for tail in recurse(rest, number - 1):
                yield (tuple(chosen),) + tail

    return recurse(labels, groups)


def run(mutation):
    check = Checker("R13 syzygy basis", "scouting/syzygy-basis-r13.md")
    rng = np.random.default_rng(1313)

    # Success-one Fock emitter and determinant basis law.
    for rank, bath_dimension in [(3, 5), (3, 7), (4, 6), (5, 8)]:
        frame = random_isometry(rng, bath_dimension, rank)
        coefficients = adj(frame)
        emitter = frame / np.sqrt(rank) if mutation == "source-scale" else frame
        incident = np.eye(rank) / rank
        emitted = emitter @ incident @ adj(emitter)
        projector = frame @ adj(frame)
        check.close(np.linalg.norm(coefficients @ adj(coefficients) - np.eye(rank)),
                    0, 1e-11, "row coisometry")
        check.close(np.linalg.norm(adj(emitter) @ emitter - np.eye(rank)),
                    0, 1e-11, "success-one emitter isometry")
        check.close(np.linalg.norm(emitted - projector / rank),
                    0, 1e-11, "flat emitted source")
        check.close(np.trace(emitted).real, 1, 1e-11, "emitter success probability")
        minor_mass = 0.0
        for subset in itertools.combinations(range(bath_dimension), rank):
            probability = abs(np.linalg.det(coefficients[:, subset])) ** 2
            minor_mass += probability
            principal = np.linalg.det(projector[np.ix_(subset, subset)]).real
            check.close(principal, probability, 1e-10, "generating minor law")
        check.close(minor_mass, 1, 1e-10, "Cauchy-Binet basis normalization")

    # Jucys--Murphy matrices and their exact integer spectrum.
    local_dimension = 2
    factors = 4
    data_dimension = local_dimension ** factors
    x_operators = {}
    for k in range(2, factors + 1):
        operator = sum((swap_operator(local_dimension, factors, i, k - 1)
                        for i in range(k - 1)), np.zeros((data_dimension, data_dimension), complex))
        x_operators[k] = operator
        values = np.linalg.eigvalsh(operator)
        check.close(np.max(np.abs(values - np.rint(values))), 0, 1e-10,
                    "integer Jucys--Murphy spectrum")
        check.atmost(np.max(np.abs(values)), k - 1 + 1e-10,
                     "Jucys--Murphy spectral range")
        distinct = np.unique(np.rint(values).astype(int))
        if len(distinct) > 1:
            check.atleast(np.min(np.diff(distinct)), 1, "integer content gap")
    for first in range(2, factors + 1):
        for second in range(first + 1, factors + 1):
            commutator = x_operators[first] @ x_operators[second] \
                - x_operators[second] @ x_operators[first]
            check.close(np.linalg.norm(commutator), 0, 1e-10,
                        "commuting Jucys--Murphy family")

    # Hermitian padded projected-unitary encoding.
    k = 4
    x_operator = x_operators[k]
    alpha, select, encoded, clean = padded_jm_encoding(x_operator, k, mutation)
    check.close(np.linalg.norm(select - adj(select)), 0, 1e-11,
                "padded SELECT Hermitian")
    check.close(np.linalg.norm(select @ select - np.eye(select.shape[0])), 0, 1e-11,
                "padded SELECT involution")
    check.close(np.linalg.norm(encoded - adj(encoded)), 0, 1e-11,
                "JM encoding Hermitian")
    check.close(np.linalg.norm(encoded @ encoded - np.eye(encoded.shape[0])), 0, 1e-11,
                "JM encoding involution")
    projected = encoded[np.ix_(clean, clean)]
    check.close(np.linalg.norm(projected - x_operator / alpha), 0, 1e-11,
                "exact padded JM projected block")

    # Hermitian shifted LCU and the exact two-threshold signed reflection.
    content = 0
    thresholds = [(content - 0.5) / alpha, (content + 0.5) / alpha]
    for threshold in thresholds:
        shifted_select, shifted, shifted_clean = shifted_encoding(
            encoded, clean, threshold, mutation)
        check.close(np.linalg.norm(shifted_select - adj(shifted_select)), 0, 1e-11,
                    "shift SELECT Hermitian")
        check.close(np.linalg.norm(shifted_select @ shifted_select
                                   - np.eye(shifted_select.shape[0])), 0, 1e-11,
                    "shift SELECT involution")
        check.close(np.linalg.norm(shifted - adj(shifted)), 0, 1e-11,
                    "shift encoding Hermitian")
        block = shifted[np.ix_(shifted_clean, shifted_clean)]
        target = (x_operator / alpha - threshold * np.eye(data_dimension)) \
            / (1 + abs(threshold))
        check.close(np.linalg.norm(block - target), 0, 1e-11,
                    "exact shifted projected block")
        spectrum = np.linalg.eigvalsh(target)
        check.atleast(np.min(np.abs(spectrum)), 1 / (5 * alpha) - 1e-10,
                      "shifted integer half-gap")

    labels = list(range(-(k - 1), k))
    values, projectors = spectral_projectors(x_operator, labels)
    check.close(np.linalg.norm(sum(projectors.values()) - np.eye(data_dimension)),
                0, 1e-10, "content projectors resolve identity")
    sign_matrices = []
    eig_values, eig_vectors = np.linalg.eigh(x_operator / alpha)
    for threshold in thresholds:
        diagonal = np.where(eig_values - threshold > 0, 1.0, -1.0)
        sign_matrices.append((eig_vectors * diagonal) @ adj(eig_vectors))
    reflection = -sign_matrices[0] @ sign_matrices[1]
    check.close(np.linalg.norm(reflection - (2 * projectors[content] - np.eye(data_dimension))),
                0, 1e-10, "two signed thresholds isolate one content")

    # One random-window failure is Lueders, including an entangled reference.
    reference_dimension = 2
    total_dimension = data_dimension * reference_dimension
    random_matrix = rng.normal(size=(total_dimension, total_dimension)) \
        + 1j * rng.normal(size=(total_dimension, total_dimension))
    density = random_matrix @ adj(random_matrix)
    density /= np.trace(density)
    chosen = next(label for label in labels
                  if 1 < round(np.trace(projectors[label]).real) < data_dimension - 1)
    chosen_projector = np.kron(projectors[chosen], np.eye(reference_dimension))
    complement = np.eye(total_dimension) - chosen_projector
    expected_failure = complement @ density @ complement
    if mutation == "luders-failure":
        modeled_failure = sum(
            np.kron(projectors[label], np.eye(reference_dimension))
            @ density
            @ np.kron(projectors[label], np.eye(reference_dimension))
            for label in labels if label != chosen)
    else:
        modeled_failure = expected_failure
    check.close(np.linalg.norm(modeled_failure - expected_failure), 0, 1e-11,
                "binary failure retains complement coherence")

    # Exact padded-bank retry channel on the same reference-entangled input.
    real_windows = len(labels)
    padded_windows = 1 << math.ceil(math.log2(real_windows))
    extended = {label: np.kron(projector, np.eye(reference_dimension))
                for label, projector in projectors.items()}

    def failure_channel(state):
        result = (padded_windows - real_windows) * state / padded_windows
        for projector in extended.values():
            other = np.eye(total_dimension) - projector
            result += other @ state @ other / padded_windows
        return result

    one_bank_trace = sum(np.trace(projector @ density @ projector).real
                         for projector in extended.values()) / padded_windows
    one_bank_trace += np.trace(failure_channel(density)).real
    check.close(one_bank_trace, 1, 1e-11, "one padded bank trial trace preserving")
    retries = 5
    for label, projector in extended.items():
        current = density.copy()
        accepted = np.zeros_like(density)
        for _ in range(retries):
            accepted += projector @ current @ projector / padded_windows
            current = failure_channel(current)
        factor = 1 - (1 - 1 / padded_windows) ** retries
        target = factor * projector @ density @ projector
        check.close(np.linalg.norm(accepted - target), 0, 1e-10,
                    "capped bank is scalar Lueders instrument")
    terminal = density.copy()
    for _ in range(retries):
        terminal = failure_channel(terminal)
    check.close(np.trace(terminal).real, (1 - 1 / padded_windows) ** retries,
                1e-11, "state-independent bank exhaustion")

    # Exact antisymmetry and padded certificate, including every failed outcome.
    for rank in [2, 3, 4]:
        true_antisymmetry, permutations = antisymmetrizer(rank, rank)
        modeled_antisymmetry, _ = antisymmetrizer(rank, rank, mutation)
        dimension = rank ** rank
        check.close(np.linalg.norm(modeled_antisymmetry - adj(modeled_antisymmetry)),
                    0, 1e-10, "antisymmetrizer Hermitian")
        check.close(np.linalg.norm(modeled_antisymmetry @ modeled_antisymmetry
                                   - modeled_antisymmetry),
                    0, 1e-10, "antisymmetrizer projector normalization")
        seed_coordinates = tuple(range(rank))
        seed_index = np.ravel_multi_index(seed_coordinates, (rank,) * rank)
        seed = np.zeros(dimension, complex)
        seed[seed_index] = 1
        column = true_antisymmetry @ seed
        column /= np.linalg.norm(column)
        source = np.eye(dimension) / (rank ** rank)
        overlap = np.trace(modeled_antisymmetry @ source).real
        check.close(overlap, 1 / (rank ** rank), 1e-11,
                    "direct antisymmetry overlap has no factorial")

        valid = math.factorial(rank)
        padded = 1 << math.ceil(math.log2(valid))
        branches = []
        for label in range(padded):
            if label < valid:
                permutation = permutations[label]
                branch = tensor_permutation(rank, rank, permutation)
                if mutation != "certificate-sign":
                    branch = permutation_sign(permutation) * branch
            else:
                if mutation == "certificate-invalid":
                    branch = swap_operator(rank, rank, 0, 1)
                else:
                    branch = np.eye(dimension)
                check.close(np.linalg.norm(branch - np.eye(dimension)), 0, 1e-11,
                            "invalid certificate branch is identity")
            branches.append(branch)

        certificate = sum(branches[:valid]) / padded
        gamma = valid / padded
        check.close(np.linalg.norm(certificate - gamma * true_antisymmetry),
                    0, 1e-10, "signed padded certificate Kraus map")
        check.close(np.linalg.norm(certificate @ column - gamma * column),
                    0, 1e-10, "certificate action on correct column")
        check.close(np.trace(certificate @ source @ adj(certificate)).real,
                    gamma * gamma / (rank ** rank), 1e-11,
                    "direct padded-certificate success")

        outcome_probability = 0.0
        for validity in [0, 1]:
            label_range = range(valid) if validity else range(valid, padded)
            for output in range(padded):
                kraus = np.zeros((dimension, dimension), complex)
                for label in label_range:
                    phase = -1 if (label & output).bit_count() % 2 else 1
                    kraus += phase * branches[label] / padded
                state = kraus @ column
                probability = float(np.vdot(state, state).real)
                outcome_probability += probability
                accepted = validity == 1 and output == 0
                if probability > 1e-14 and not accepted:
                    normalized = state / math.sqrt(probability)
                    phase = np.vdot(column, normalized)
                    aligned = normalized * (phase.conjugate() / abs(phase))
                    check.close(np.linalg.norm(aligned - column), 0, 1e-10,
                                "every certificate failure preserves correct column")
        check.close(outcome_probability, 1, 1e-10,
                    "certificate outcome probabilities normalize")

    # Hidden transversal constants by explicit balanced-partition enumeration.
    for rank, group_size in [(3, 2), (3, 3), (4, 2)]:
        total = rank * group_size
        fixed = set(range(rank))
        partition_count = 0
        transversal_count = 0
        for partition in balanced_partitions(total, rank, group_size):
            partition_count += 1
            transversal_count += all(len(fixed.intersection(group)) == 1
                                     for group in partition)
        observed = transversal_count / partition_count
        expected = math.factorial(rank) * group_size ** rank \
            / math.prod(total - index for index in range(rank))
        check.close(observed, expected, 1e-12, "balanced transversal probability")
        check.atmost(observed, 2 / 5 + 1e-12, "uniform transversal ceiling")
        ratio = (2 / 3 - observed) / (1 - observed)
        check.atleast(ratio, 4 / 9 - 1e-12, "uniform lower-bound factor")

    # Revised finite probability, batch and strict-separation constants.
    certificate_retries = math.ceil(math.log(16) / math.log(4 / 3))
    check.equal(certificate_retries, 10, "same-column certificate retry cap")
    check.atmost((3 / 4) ** certificate_retries, 1 / 16,
                 "same-column certificate failure")
    ideal_good = (1 / 2) * (7 / 8) * (15 / 16)
    implemented = ideal_good - 1 / 256 - 1 / 256
    check.close(ideal_good, 105 / 256, 1e-12, "ideal strengthened batch success")
    check.close(implemented, 103 / 256, 1e-12, "implemented batch success")
    check.atleast(implemented, 3 / 8, "batch success above three eighths")
    batches = math.ceil(math.log(3) / math.log(8 / 5))
    check.equal(batches, 3, "three batches at delta one third")
    for rank in [3, 4, 6]:
        quantum_copies = batches * 2 * rank * rank
        check.equal(quantum_copies, 6 * rank * rank, "revised source copy cap")
        group_size = math.floor((9 / 4) * quantum_copies * (quantum_copies - 1)) + 1
        check.require(quantum_copies * (quantum_copies - 1) < 4 * group_size / 9,
                      "strict growing-rank copy separation")

    print(f"PASS: {check.count} finite checks; no asymptotic proof inferred")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutate", choices=[
        "source-scale",
        "padded-block",
        "shift-sign",
        "luders-failure",
        "antisymmetry-normalization",
        "certificate-sign",
        "certificate-invalid",
    ])
    arguments = parser.parse_args()
    try:
        run(arguments.mutate)
    except CheckFailure as error:
        print(f"FAIL: {error}")
        sys.exit(1)
    except Exception as error:
        print(f"ERROR: {error}")
        sys.exit(2)
