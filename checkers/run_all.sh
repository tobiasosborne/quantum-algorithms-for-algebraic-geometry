#!/bin/bash
# Run every checker under `timeout`, print PASS/FAIL and wall time per checker,
# exit nonzero if any checker fails (rk-light law L4).
#
# Usage:   ./run_all.sh            (all checkers)
#          ./run_all.sh check_task1_conic.py check_fact72_takagi.py
#
# Each checker exits 0 only when every property it tests holds; 1 with a
# printed reason otherwise; 2 if it could not run at all.  Per-script budgets
# below are ~5x the measured wall time on the reference machine.
# Exploration scripts under explore/ are NOT run here: see README.

cd "$(dirname "$0")" || exit 2
export PYTHONPATH="$PWD:$PYTHONPATH"
PY=${PYTHON:-python3}
LOGDIR=${LOGDIR:-logs}
mkdir -p "$LOGDIR"

# checker                       budget(s)
CHECKERS=(
  "check_task1_conic.py         120"
  "check_task2_hilbert.py       300"
  "check_task2b_subspace.py     120"
  "check_task3_gaps.py          600"
  "check_task3b_hard.py         300"
  "check_task3c_exact.py        300"
  "check_task3d_nscale.py       300"
  "check_task3e_ffstats.py      300"
  "check_task4_toric.py         300"
  "check_task5_groebner.py      120"
  "check_task6_2sat.py          120"
  "check_task7_coherent.py      120"
  "check_task8_cnf.py           600"
  "check_task9_pyramid.py       300"
  "check_fact71_bombieri.py     120"
  "check_fact72_takagi.py       120"
)

SELECT=("$@")

fail=0
total=0
run=0
printf '%-28s %8s %9s  %s\n' "CHECKER" "STATUS" "WALL(s)" "LAST LINE"
printf '%s\n' "--------------------------------------------------------------------------------"
t_all=$SECONDS
for entry in "${CHECKERS[@]}"; do
  set -- $entry
  script=$1
  budget=$2
  if [ ${#SELECT[@]} -gt 0 ]; then
    keep=0
    for s in "${SELECT[@]}"; do [ "$s" = "$script" ] && keep=1; done
    [ $keep -eq 1 ] || continue
  fi
  log="$LOGDIR/${script%.py}.log"
  t0=$SECONDS
  timeout "$budget" "$PY" -u "$script" > "$log" 2>&1
  rc=$?
  dt=$((SECONDS - t0))
  run=$((run + 1))
  total=$((total + dt))
  last=$(tail -n 1 "$log")
  case $rc in
    0) status="PASS" ;;
    124) status="TIMEOUT"; last="exceeded the ${budget}s budget" ;;
    *) status="FAIL($rc)" ;;
  esac
  [ $rc -eq 0 ] || fail=$((fail + 1))
  printf '%-28s %8s %9s  %s\n' "$script" "$status" "$dt" "$last"
done
printf '%s\n' "--------------------------------------------------------------------------------"
printf '%d checkers run, %d failed, %d s total wall\n' "$run" "$fail" "$((SECONDS - t_all))"
echo "per-checker output in $LOGDIR/"
[ $fail -eq 0 ] || exit 1
exit 0
