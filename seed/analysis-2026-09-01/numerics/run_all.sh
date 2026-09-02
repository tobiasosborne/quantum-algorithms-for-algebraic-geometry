#!/bin/bash
# Reproduce everything.  Long runs (task3*, task4, task5) take ~10-40 min each.
set -e
cd "$(dirname "$0")"
python3 -u task1_conic.py      | tee task1_out.txt
python3 -u task2_hilbert.py    | tee task2_out.txt
python3 -u task2b_subspace.py  | tee task2b_out.txt
python3 -u task3_gaps.py       | tee task3_out.txt      # gap vs N (long)
python3 -u task3b_hard.py      | tee task3b_out.txt     # 2-SAT chain gaps vs n
python3 -u task3c_exact.py     | tee task3c_out.txt     # closed forms
python3 -u task3d_nscale.py    | tee task3d_out.txt     # gap vs n at fixed N
python3 -u task4_toric.py      | tee task4_out.txt
python3 -u task5_groebner.py   | tee task5_out.txt
python3 -u task6_2sat.py       | tee task6_out.txt
python3 -u task7_coherent.py   | tee task7_out.txt
