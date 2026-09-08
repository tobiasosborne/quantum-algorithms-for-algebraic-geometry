#!/usr/bin/env python3
"""Finite diagnostics for scouting/root-frontiers-r11.md, not proof or advantage.

Declared Euclidean Hermitian metrics depart from C1. Dimensions do not use C2.
Run from any directory with Python/NumPy; fixed seed, matrices of size at most 14.
Each --mutate choice deliberately breaks a modeled mathematical ingredient.
Exit 0: finite properties pass; 1: property violation; 2: could not run.
"""
import argparse
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from checkharness import Checker, CheckFailure


def adj(a):
    return a.conj().T


def outer(v):
    return np.outer(v, v.conj())


def run(mutate):
    c = Checker("R11 CP geometry", "root-frontiers-r11 sections 2--6")
    rng = np.random.default_rng(1107)

    # Change basis by genuinely complex unitaries to expose adjoint errors.
    for trial in range(8):
        z = rng.normal(size=(7, 7)) + 1j * rng.normal(size=(7, 7))
        u, _ = np.linalg.qr(z)
        d0 = np.zeros((7, 7), complex)
        d0[2, 0], d0[3, 1] = 0.4, 0.7
        p0 = np.diag([0, 0, 0, 0, 1, 1, 1]).astype(complex)
        if mutate == "harmonic-projector":
            p0 = np.diag([1, 0, 0, 0, 0, 1, 1]).astype(complex)
        d, p = u @ d0 @ adj(u), u @ p0 @ adj(u)
        c.close(np.linalg.norm(d @ d), 0, 1e-12, "d squares to zero")
        c.close(np.linalg.norm(d @ p), 0, 1e-12, "harmonic projector killed by d")
        delta = d @ adj(d) + adj(d) @ d
        h = d + adj(d) + delta
        generator_p = 1j * (h @ p - p @ h)
        for jump in [d, adj(d), delta + 0.3j * d, np.eye(7) + d]:
            jj = adj(jump) @ jump
            generator_p += adj(jump) @ p @ jump - (jj @ p + p @ jj) / 2
        c.close(np.linalg.norm(generator_p), 0, 1e-11, "harmonic Heisenberg generator zero")

    mu = np.array([[1, 0, 0, 0], [0, 1, 1, 0]], dtype=complex)
    c.close(np.linalg.norm(mu, 2), np.sqrt(2), 1e-12, "dual number multiplication norm")
    k = mu / (1 if mutate == "fusion-normalization" else np.sqrt(2))
    c.atmost(np.linalg.eigvalsh(adj(k) @ k).max(), 1 + 1e-12, "fusion is a contraction")
    for x in list(np.linspace(0, 1, 31)) + [2 / 3]:
        psi = np.array([np.sqrt(x), np.exp(0.37j) * np.sqrt(1 - x)])
        observed = np.linalg.norm(k @ np.kron(psi, psi)) ** 2
        c.close(observed, 2 * x - 1.5 * x * x, 1e-12, "fusion probability polynomial")
        c.atmost(observed, 2 / 3 + 1e-12, "identical-input success ceiling")
    ee = np.array([0, 0, 0, 1], complex)
    left = adj(mu) @ mu @ ee
    right = np.kron(mu, np.eye(2)) @ np.kron(np.eye(2), adj(mu)) @ ee
    c.close(np.linalg.norm(left), 0, 1e-12, "dagger-Frobenius left side zero")
    c.close(np.linalg.norm(right - ee), 0, 1e-12, "dagger-Frobenius right side nonzero")

    for trial in range(8):
        a = rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3))
        h = a @ adj(a) + 0.4 * np.eye(3)
        ev, basis = np.linalg.eigh(h)
        sqrt_h = (basis * np.sqrt(ev)) @ adj(basis)
        vectors = rng.normal(size=(5, 3)) + 1j * rng.normal(size=(5, 3))
        weights = rng.uniform(0.1, 1, 5)
        frame = sum(w * outer(s) for w, s in zip(weights, vectors))
        scale = float(np.linalg.norm(frame, 2))
        ensemble = np.zeros((3, 3), complex)
        denominators = []
        total_acceptance = 0
        for w, s in zip(weights, vectors):
            denominator = float(np.vdot(s, h @ s).real)
            denominators.append(denominator)
            probability = w * denominator / (scale * np.trace(h).real)
            if mutate == "born-weight":
                probability = w / sum(weights)
            v = sqrt_h @ s / np.sqrt(denominator)
            c.close(np.linalg.norm(v), 1, 1e-12, "conditional vector normalized")
            ensemble += probability * outer(v)
        expected = sqrt_h @ frame @ sqrt_h / (scale * np.trace(h).real)
        c.close(np.linalg.norm(ensemble - expected), 0, 1e-11, "Born denominators cancel")
        small = min(denominators)
        for w, denominator in zip(weights, denominators):
            probability = w * denominator / (scale * np.trace(h).real)
            total_acceptance += probability * small / denominator
        c.close(total_acceptance, small * sum(weights) / (scale * np.trace(h).real),
                1e-12, "importance repair acceptance")

    # A valid CPTP channel can contain interior nilpotent transients.
    for size in range(3, 8):
        kraus = []
        for j in range(size):
            k = np.zeros((size, size), complex)
            target = max(j - 1, 0)
            if mutate == "absorbing-boundary":
                target = (j - 1) % size
            k[target, j] = 1
            kraus.append(k)
        c.close(np.linalg.norm(sum(adj(k) @ k for k in kraus) - np.eye(size)),
                0, 1e-12, "absorbing channel is TP")
        rho = np.zeros((size, size), complex)
        rho[-1, -1] = 1
        for step in range(size - 1):
            rho = sum(k @ rho @ adj(k) for k in kraus)
            c.close(np.trace(rho).real, 1, 1e-12, "trajectory preserves trace")
        zero = np.zeros_like(rho)
        zero[0, 0] = 1
        c.close(np.linalg.norm(rho - zero), 0, 1e-12, "finite absorption")
        after = sum(k @ rho @ adj(k) for k in kraus)
        c.close(np.linalg.norm(after - zero), 0, 1e-12, "absorbing fixed state")
    # Construct the supercharge from occupation rules independently of its
    # four-state formula. Higher sectors expose a lost fermionic sign.
    for coupling in [0.0, 0.01, 0.2, 0.5, np.sqrt(3) / 2, 1.0, 2.0]:
        for weight in range(9):
            states = [(nx, nu, nv, nw) for nx in range(weight + 1)
                      for nu in range(weight // 2 + 1)
                      for nv in range(2) for nw in range(2)
                      if nx + 2 * nu + 2 * nv + 3 * nw == weight]
            index = {state: j for j, state in enumerate(states)}
            q = np.zeros((len(states), len(states)), complex)
            for column, (nx, nu, nv, nw) in enumerate(states):
                if not nv and nu:
                    q[index[nx, nu - 1, 1, nw], column] += np.sqrt(nu)
                if not nv and nx >= 2:
                    scale = 1 if mutate == "ce-merge-weight" else np.sqrt(6)
                    q[index[nx - 2, nu, 1, nw], column] += coupling * np.sqrt(nx * (nx - 1)) / scale
                if not nw and nx and nu:
                    sign = 1 if mutate == "ce-fermion-sign" else (-1) ** nv
                    q[index[nx - 1, nu - 1, nv, 1], column] += sign * coupling * np.sqrt(nx * nu)
            c.close(np.linalg.norm(q @ q), 0, 1e-11, "CE supercharge squares to zero")
            if weight != 3:
                continue
            order = [index[s] for s in [(3, 0, 0, 0), (1, 0, 1, 0),
                                        (1, 1, 0, 0), (0, 0, 0, 1)]]
            h = (q + adj(q))[np.ix_(order, order)]
            expected_h = np.array([[0, coupling, 0, 0], [coupling, 0, 1, 0],
                                   [0, 1, 0, coupling], [0, 0, coupling, 0]])
            c.close(np.linalg.norm(h - expected_h), 0, 1e-12, "CE occupation normalization")
            energies, eigbasis = np.linalg.eigh(h)
            omega = np.sqrt(1 + 4 * coupling * coupling)
            for elapsed in [0.0, 0.1, 0.7, np.pi, 9.0]:
                evolved = (eigbasis * np.exp(-1j * elapsed * energies)) @ adj(eigbasis)
                expected = 1j * (np.cos(elapsed / 2) * np.sin(omega * elapsed / 2) / omega
                                 - np.sin(elapsed / 2) * np.cos(omega * elapsed / 2))
                c.close(abs(evolved[3, 0] - expected), 0, 1e-11, "CE full scattering amplitude")
                if coupling == np.sqrt(3) / 2 and elapsed == np.pi:
                    c.close(abs(evolved[3, 0] - 1j), 0, 1e-11, "resonant perfect transfer phase")
    print(f"PASS: {c.count} finite checks; no proof or advantage inferred")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutate", choices=["harmonic-projector", "fusion-normalization",
                                             "born-weight", "absorbing-boundary",
                                             "ce-merge-weight", "ce-fermion-sign"])
    args = parser.parse_args()
    try:
        run(args.mutate)
    except CheckFailure as error:
        print(f"FAIL: {error}")
        sys.exit(1)
    except Exception as error:
        print(f"ERROR: {error}")
        sys.exit(2)
