#!/usr/bin/env python3
"""Finite exact checks of the R15 Boolean/Picard encoding and period reduction.

Fixed examples with at most four Boolean variables. These checks do not prove
the uniform NP-completeness reduction, Picard identities or Lenstra's theorem.
Mutations affect only the in-process model. Exit 0 pass, 1 violation, 2 error.
"""
import argparse
import itertools
import sys
from fractions import Fraction
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from checkharness import Checker, CheckFailure


def quad(length, terms):
    result = {}
    for coefficient, i, j in terms:
        exponent = [0] * length
        exponent[i] += 1
        exponent[j] += 1
        key = tuple(exponent)
        result[key] = result.get(key, 0) + coefficient
    return {key: value for key, value in result.items() if value}


def encode(a, b, mutation=None):
    v = len(a[0])
    size = v + 2
    equations = [quad(size, [(1, 1, 1), (-1, 1, 0)])]
    for i in range(2, size):
        equations.append(quad(size, [(1, i, i), (-1, i, 0)]))
        if mutation != "dummy-not-unique":
            equations.append(quad(size, [(1, 0, i), (-1, 1, i)]))
    for row, target in zip(a, b):
        terms = [(value, 1, i + 2) for i, value in enumerate(row)]
        terms.append((-target, 1, 0))
        equations.append(quad(size, terms))
    return equations


def evaluate(poly, coordinates):
    value = 0
    for exponent, coefficient in poly.items():
        term = coefficient
        for coordinate, power in zip(coordinates, exponent):
            term *= coordinate ** power
        value += term
    return value


def run(mutation):
    c = Checker("R15 Picard encoding", "D-BOOLEAN-PICARD-SURFACE")
    instances = [([[1, 2, 3]], [3]), ([[1, 2, 3]], [7]),
                 ([[0, 0]], [0]), ([[0, 0]], [1]),
                 ([[1, -1, 2, 0], [0, 1, 0, 1]], [1, 1])]
    for a, b in instances:
        v = len(a[0])
        equations = encode(a, b, mutation)
        expected = sum(all(sum(ai * xi for ai, xi in zip(row, x)) == target
                           for row, target in zip(a, b))
                       for x in itertools.product([0, 1], repeat=v))
        actual = 0
        for tx in itertools.product([0, 1], repeat=v + 1):
            u = (1,) + tx
            good = all(evaluate(g, u) == 0 for g in equations)
            actual += good
            for scalar in [-2, 3]:
                for g in equations:
                    c.equal(evaluate(g, tuple(scalar * z for z in u)),
                            scalar ** 2 * evaluate(g, u), "homogeneous quadratic scaling")
            for y in [(1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 2, 3)]:
                z = [[ui * yj for yj in y] for ui in u]
                for i, k in itertools.combinations(range(v + 2), 2):
                    for j, ell in itertools.combinations(range(3), 2):
                        c.equal(z[i][j] * z[k][ell] - z[i][ell] * z[k][j],
                                0, "Segre minors")
                charts = [0] if mutation == "only-first-chart" else range(3)
                embedded_good = all(evaluate(g, tuple(row[j] for row in z)) == 0
                                    for g in equations for j in charts)
                c.equal(embedded_good, good, "three-chart Segre pullback equivalence")
        c.equal(actual, 1 + expected, "one dummy point plus Boolean solutions")
        c.require(all(sum(exponent) == 2 for g in equations for exponent in g),
                  "all expanded source equations have degree two")

    # Exact finite control of the period-to-rational-inequality reduction.
    # pi=sqrt(2)*(1,k), so its exact zeros are z0+k*z1=0. Nonzero pairings
    # have absolute value at least sqrt(2)>g=1/2. The approximation below
    # lies within the canonical error budget; no floating zero test is used.
    h, gap = 3, Fraction(1, 2)
    for k in [2, 7]:
        approximation = [Fraction(141421, 100000), Fraction(k * 141421, 100000)]
        exact_exists = False
        rational_exists = False
        for z in itertools.product(range(-h, h + 1), repeat=2):
            if z == (0, 0):
                if mutation == "allow-zero":
                    rational_exists = True
                continue
            exact_zero = z[0] + k * z[1] == 0
            pairing = sum(ai * zi for ai, zi in zip(approximation, z))
            rational_zero = abs(pairing) <= gap / 2
            c.equal(rational_zero, exact_zero, "separated rational slab detects exact relation")
            exact_exists |= exact_zero
            rational_exists |= rational_zero
        c.equal(rational_exists, exact_exists, "nonzero relation decision")
    print(f"PASS: {c.count} finite exact checks; no uniform complexity proof inferred")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutate", choices=["dummy-not-unique", "only-first-chart", "allow-zero"])
    args = parser.parse_args()
    try:
        run(args.mutate)
    except CheckFailure as error:
        print(f"FAIL: {error}")
        sys.exit(1)
    except Exception as error:
        print(f"ERROR: {error}")
        sys.exit(2)
