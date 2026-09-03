<!-- ROLE: current state + next steps. UPDATE POLICY: rewritten whole at session close,
     <=150 lines. TRIGGER: read at session start (item 4 of the CLAUDE.md read order). -->

# HANDOFF — quantum-algorithms-for-algebraic-geometry

## State (2026-09-03, session 2 close: exploration round 1 complete)

- Method: rk-light (CLAUDE.md laws L1–L5, rules 1–10). Not rk. Tracking: bd, prefix `qaag-`.
- North star: CLAUDE.md §1. Robotics is a first-class arm (PRD D5).
- Seed (2026-09-01 analysis + notebook page 81) is read-only under `seed/`.
- `definitions/definitions.md`: 118 entries (66 seed + 2 stubs + 50 merged from lanes), conventions
  C1–C12 binding, 14 OPEN issues. `definitions/notation.md`: symbol table.
- `claims/CLAIMS.md`: 334 rows (163 SKETCH, 91 CONJECTURE, 80 REFUTED, 0 PROVED). SKETCH legend
  widened 2026-09-03 to admit cited published theorems with resolved ids (C-092/C-099 convention).
  Four proposed rows are HELD in their memos and not merged: C-NEW-KB-QMA1, C-NEW-KB-GAP-INDEPENDENT
  (`scouting/koszul-betti.md`), C-NEW-IO-CLEAN, C-NEW-IO-SUM-IDEAL (`scouting/intersection-observables.md`).
- `verdicts/`: 14 verdict files from four converged critic loops (all PASS at the final round):
  quantum-primitives r1–r3, koszul-betti r1–r5, quantum-native r1–r3, intersection-observables r1–r3.
  Every merged row since C-281 entered at the status a converged verdict adjudicated.
- Scouting memos: classical-landscape, applications-wide-net, robotics-deep-dive, real-variety,
  robotics-space, two-copy-real-filter (session 1); quantum-primitives (codex, 2652 lines),
  koszul-betti (Opus, 974 lines), quantum-native (codex, 2253 lines), intersection-observables
  (Opus, 884 lines) (session 2, all critiqued).
- Checkers: `checkers/` 16 red-capable checkers unchanged; three new EXPLORATION scripts under
  `checkers/explore/` (koszul_laplacian.py, intersection_observables.py, twocopy_real_filter.py),
  not in run_all.sh, each with in-process mutations that the orchestrator re-ran (all exit 0).
  Mutation registrations M1–M4 (Koszul) and M-IO1..M-IO5 (intersection) are NOT yet in
  `checkers/MUTATIONS.md` (bead work).
- PRD.md: decisions D1–D20; arms A–E and R; §7 questions Q3–Q13 open for TJO.

## Findings of exploration round 1 (each backed by a PASS verdict)

- **Quantum-primitives map (D17, C-281..C-303).** Fourteen known primitives scored against PRD §2:
  none above 4/5. Kedlaya's curve-zeta algorithm (4/5, prior art, no hardware hook) and the
  Hallgren / Eisentraeger–Hallgren–Kitaev–Song number-field ideal problems (3/5, prior art; input is
  an ideal of a number field) are the benchmarks. Eleven primitive-problem pairs REFUTED (HHL on
  Macaulay uniformly, hypersurface zeta, SUSY Hodge speedup, generic quantum TDA, path-tracking
  internal speedup, boson-count, analogue degeneracy readout, annealing demonstrations, Groebner
  annealer, qPCA secant, volume/Ehrhart). Two combinations survive as one-week probes.
- **Arm B Koszul/Betti Laplacian (D18, C-304..C-311).** The graded Betti table IS the block
  nullity of a boson–fermion Laplacian on the inverse system (exact; tested on six ideals against
  GF(p) Koszul ranks). But: the naive compression P_0 L P_0 is the scalar N+i (information-free);
  monomial-ideal blocks are simplicial Laplacians (Hochster), so the problem is quantum TDA with its
  whole dequantization ledger; the Betti gap has no lower bound and is independent of Delta_N; the
  Hilbert-function acceptance weight h_N/M_N is exponentially small on the quadratic
  complete-intersection family. No PRD §2 criterion met. Arm B is an instrument and hardness anchor.
- **Arm D quantum-native varieties (D19, C-312..C-324).** QSAT ground space = multidegree-1 piece of
  a Macaulay inverse system (exact); product ground states = points of a multiprojective variety
  with entangled defect e_Q; diagonal Hilbert-function vanishing is a multihomogeneous
  Nullstellensatz hierarchy of product-unsatisfiability certificates whose level 2 is incomplete
  (first certifying level r = 4 on the generic four-qubit family). No criterion 3 met; product
  satisfiability geometry is prior art (Laumann et al. 2010; Aldi–Gharibian–Rudolph 2026). The broad
  negative "no arm D speedup" is NOT proved: copy-access membership/distance tests for entanglement,
  secant, MPS and tensor-network varieties, against a single-copy adaptive comparator, are the one
  open door (C-324 held). C-024 weakened in lockstep: the spinor-BEC interaction is realised, the
  2N+1 degeneracy has never been measured.
- **Arm C intersection observables (D20, C-325..C-334).** Tr(P_I P_J) is exact and elementary for
  linear subspaces: h_N of the squared principal-angle cosines (C-325). The growth law is
  dim(V ∩ W) under CLEAN intersection with constant ∏ sin^{-2} theta (held on the ambient
  Bergman-frame estimate, Geometry 2.4); tangency of contact order m gives exponent 1 − 1/m, so the
  seed's C-085 is REFUTED; the registered Toeplitz normalisation diverges, so C-086/C-168 are
  REFUTED with a distinct normalised operator as the surviving statement. The normalised signal is
  visible to codim(V ∩ W) = O(log n), not exponentially small; but the observable equals
  HF_{R/(I+J)}/J_0 (arm C is arm A on the sum ideal) and the Hutch++ comparator needs O(1/eps)
  matvecs, so score 1/5. Hardware hook: beam splitters plus difference-mode photon parity.
- Objection trajectories: primitives 25→11→3 (MAJOR 10→3→0); Koszul 12→4→1→residue→0; quantum-native
  21→7→2 (MAJOR 12→2→0); intersection 8→5→0 (FATAL 3→0). Every loop converged.
- Orchestrator brief defects found by lanes (recorded in worklogs, briefs left as written): Kedlaya
  id (correct: math/0411623); arXiv:1105.2390 is not a tensor-network paper.

## Next steps

1. TJO rulings that now gate work: Q4 (does an exponential copy saving count; decides whether the
   arm D open door is worth a lane), Q13 (should novelty be an explicit PRD §2 criterion),
   ratification of D15 (SP-0), D17–D20.
2. Candidate round-2 exploration lanes, in the orchestrator's order: (a) copy-access variety
   membership with a provable separation against single-copy adaptive measurement (arm D's open
   door; the only place a critic left a speedup possible); (b) a Bombieri-type lower bound on the
   Betti gap g_{i,N} (arm B lives or dies on K-KB6); (c) Geometry 2.4, the ambient Bergman-frame
   operator-norm estimate, which would promote C-NEW-IO-CLEAN and C-NEW-IO-SUM-IDEAL; (d) the two
   surviving primitive combinations (`scouting/quantum-primitives.md` Combinations).
3. Bead work unchanged from session 1: SP-0 audit of qubit-vs-word rows (qaag-1m0), robotics R1
   reframing (qaag-rkf) and R2 claim row (qaag-rk6), reference-ledger verification of the two codex
   scouting memos (qaag-6k1, qaag-cbn), Watrous/BCP primaries (qaag-5uu). New: register M1–M4 and
   M-IO1..M-IO5 in `checkers/MUTATIONS.md`; the C-110 and C-099 kill-first checks; re-run the gap
   survey at unit BW (OPEN-1).
4. First critic round on the eight critical claims of arm A (unchanged; C-099's reference is now
   resolved, C-085/C-086/C-168 are already settled by arm C).

## Conventions / pitfalls

- Fock basis |k> = z^k/sqrt(k!); spectral promise is on Delta_N / alpha_BE (C5, C7).
- Delta_N depends on the generating tuple, not the ideal; compare only at unit BW.
- Two Toeplitz operators now exist: D-toeplitz-operator (seed; normalised trace diverges) and
  D-normalised-toeplitz-operator ((N-r)!/N! P_0 :g: P_0); cite the right one.
- Two Koszul complexes exist: the variable complex on the inverse system (Betti numbers) and the
  generator complex whose i = 0 block is the seed H_N (C-310); do not conflate.
- Loop protocol that worked: proposer (Opus or codex) → cross-family critic r1 (attack, with
  recompute + reference fetch) → proposer repair with verbatim critic rewordings → critic
  adjudication rounds scoped by git diff → orchestrator merges verbatim from the final verdict's
  tables, at the adjudicated status; held rows stay in the memo. Orchestrator re-runs every
  exploration script before committing. Two subagents concurrent maximum (TJO).
- Codex runs are launched with `timeout` in the background; one r3 run was killed mid-run with no
  verdict written and had to be relaunched: check for the output file, not just the exit line.
- Lane timing this session: Opus proposer lanes 45–55 min; Opus repairs 4–30 min; codex proposer
  memos 25–35 min; codex critics 15–25 min; codex repairs 20–30 min.
