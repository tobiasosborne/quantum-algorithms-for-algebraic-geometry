"""Exit-code harness for the checker suite (rk-light law L4).

Every checker is `python3 check_*.py`:
  exit 0  <=> every stated property held within the stated tolerance
  exit 1  <=> some property failed; the reason is printed as a single
              line beginning with 'FAIL:' and it is the LAST line of output
  exit 2  <=> the checker could not run at all (missing dependency, etc.)

No `assert` is used anywhere in this suite: `python3 -O check_*.py` must
behave exactly like `python3 check_*.py`.  Checks are FAIL-FAST: the first
violation aborts the run, so a mutated copy of a checker reports quickly.
"""
import math
import sys
import time
import traceback


class CheckFailure(Exception):
    """A tested property did not hold."""


class Checker:
    def __init__(self, name, claim):
        self.name = name
        self.claim = claim
        self.count = 0
        self.t0 = time.time()

    # ---- primitive requirements -------------------------------------
    def require(self, cond, reason):
        self.count += 1
        if not bool(cond):
            raise CheckFailure(reason)

    def equal(self, got, want, what):
        self.count += 1
        if got != want:
            raise CheckFailure(f"{what}: got {got!r}, expected {want!r}")

    def close(self, got, want, tol, what):
        """|got - want| <= tol (absolute)."""
        self.count += 1
        if not (math.isfinite(got) and abs(got - want) <= tol):
            raise CheckFailure(
                f"{what}: got {got!r}, expected {want!r} +- {tol:g} "
                f"(|diff| = {abs(got - want):.6g})")

    def rel(self, got, want, rtol, what):
        """|got - want| <= rtol * max(|want|, 1)."""
        self.count += 1
        tol = rtol * max(abs(want), 1.0)
        if not (math.isfinite(got) and abs(got - want) <= tol):
            raise CheckFailure(
                f"{what}: got {got!r}, expected {want!r} (rtol {rtol:g}, "
                f"|diff| = {abs(got - want):.6g} > {tol:.6g})")

    def between(self, got, lo, hi, what):
        self.count += 1
        if not (math.isfinite(got) and lo <= got <= hi):
            raise CheckFailure(f"{what}: got {got!r}, expected in [{lo:g}, {hi:g}]")

    def atleast(self, got, lo, what):
        self.count += 1
        if not (math.isfinite(got) and got >= lo):
            raise CheckFailure(f"{what}: got {got!r}, expected >= {lo!r}")

    def atmost(self, got, hi, what):
        self.count += 1
        if not (math.isfinite(got) and got <= hi):
            raise CheckFailure(f"{what}: got {got!r}, expected <= {hi!r}")

    def info(self, line):
        print(line, flush=True)


def main(name, claim, body):
    """Run `body(checker)`; print a verdict; return the process exit code."""
    ck = Checker(name, claim)
    print(f"CHECKER  {name}")
    print(f"CLAIM    {claim}")
    print("-" * 78, flush=True)
    try:
        body(ck)
    except CheckFailure as exc:
        dt = time.time() - ck.t0
        print("-" * 78)
        print(f"{ck.count} checks attempted, {dt:.1f}s wall")
        print(f"FAIL: {exc}", flush=True)
        return 1
    except Exception:                                    # noqa: BLE001
        traceback.print_exc()
        dt = time.time() - ck.t0
        print("-" * 78)
        print(f"FAIL: unexpected exception after {ck.count} checks ({dt:.1f}s)",
              flush=True)
        return 2
    dt = time.time() - ck.t0
    print("-" * 78)
    print(f"PASS: {ck.count} checks in {dt:.1f}s wall", flush=True)
    return 0


def run(name, claim, body):
    sys.exit(main(name, claim, body))
