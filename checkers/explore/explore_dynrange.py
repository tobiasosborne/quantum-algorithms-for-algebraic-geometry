"""EXPLORATION ONLY -- deliberately excluded from run_all.sh.

This is part (C) of the seed's numerics/task3b_hard.py:

    f = z_{1,0} z_{2,1} - z_{1,1} z_{2,0} + eps * z_{1,0} z_{2,0}
    on a nearest-neighbour chain of m blocks, eps in {1, 1e-1, 1e-2, 1e-3}.

WHY IT IS NOT A CHECKER
  The seed report makes no quantitative claim that these numbers support.  The
  nearest statement is Sect. 7, "Delta_N depends on the generating tuple, not
  only on I: (f_1, f_1 + eps f_2) generates the same ideal as (f_1, f_2) for
  eps != 0 and has Delta_N = O(eps^2)" -- but that is a statement about a
  two-generator tuple with a near-redundancy, whereas this script perturbs a
  SINGLE generator, and the ideal changes with eps.  The observed behaviour is
  the opposite of a collapse: Delta is SMALLEST at eps = 1 (0.0833 at m = 6)
  and saturates at the eps -> 0 value (0.1340) already by eps = 1e-2, i.e. the
  numbers show a limit, not a small-gap phenomenon.  There is therefore no
  property here whose violation would refute anything in the report, and a
  pass/fail wrapper around it would be theatre (rk-light L4).

  If a future claim is written about coefficient dynamic range in a single
  generator, this script is the starting point and should be promoted to a
  checker with an exit code at that time.

Run: timeout 300 python3 explore/explore_dynrange.py
"""
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from check_task3b_hard import gapof, two_local     # noqa: E402


def main():
    print("f = z_{1,0}z_{2,1} - z_{1,1}z_{2,0} + eps*(z_{1,0}z_{2,0}) on a chain")
    print(f"{'eps':>10} {'m':>3} {'kerdim':>7} {'Delta':>12}")
    for eps in (1.0, 1e-1, 1e-2, 1e-3):
        for m in (6, 8, 10):
            psi = np.array([eps, 1, -1, 0], dtype=complex)
            psi /= np.linalg.norm(psi)
            H = sum(two_local(psi, i, i + 1, m) for i in range(m - 1))
            k, g, nrm = gapof(H)
            print(f"{eps:>10.0e} {m:>3} {k:>7} {g:>12.6g}", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
