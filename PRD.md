<!-- ROLE: WHAT the campaign is for — north star, success criteria, scope, decision record.
     UPDATE POLICY: decision rows are appended, never rewritten; scope and arms sections are
     rewritten at phase boundaries with a dated note. TRIGGER: TJO directive or phase change. -->

# PRD — quantum algorithms for algebraic geometry

## 1. North star

Verbatim in CLAUDE.md §1. Short form: a new quantum algorithm with a real time or space
speedup over the best classical algorithm for a problem about varieties or ideals, with a
cheap heuristic-hardware attack (linear optics + postselection / MBQC, boson sampling, or a
natural condensed-matter model). BQP-completeness is a bonus.

## 2. Success criteria (what "done" means)

A north-star hit is a claim row in `claims/CLAIMS.md` at status PROVED with ALL of:

1. **Problem.** A precisely stated computational problem P with input encoding and size
   parameters, drawn from algebraic geometry or one of its application areas.
2. **Classical baseline.** The best-known classical algorithm for P, cited, with its
   complexity as a function of the same parameters, and a statement of practical state of
   the art (software, solvable sizes). "Best-known" is adjudicated by a critic, not asserted.
3. **Quantum algorithm.** An algorithm with a proven resource bound (time, space, or both)
   that beats the baseline by a stated margin on a stated input family. The input model
   (sparse access, QRAM, explicit circuit) is part of the statement.
4. **Dequantization audit.** A written argument, adjudicated, that the speedup survives
   the known dequantization attacks (Tang; Gilyen–Lloyd–Tang; Chia et al.) and hidden
   costs (state preparation, readout, exponentially small overlaps, closing gaps).
5. **Heuristic attack.** A concrete mapping of P (or a natural sub-family) onto linear
   optics with postselection / MBQC, boson sampling, or a condensed-matter Hamiltonian
   such as Bose–Hubbard or spinor-BEC spin mixing, with an estimate of what an experiment
   could test.

Partial credit that is still a product: a sharp negative result (P admits no speedup of a
given type, with proof), or a new classical algorithm found while hunting.

## 3. Scope

In scope: every problem family listed in `scouting/classical-landscape.md`; every
application area in `scouting/applications-wide-net.md`; robotics as a named arm
(`scouting/robotics-deep-dive.md`). The seed's Fock-space Hamiltonian construction is the
starting primitive, not a commitment: an arm may abandon it.

Out of scope until a phase change: fault-tolerance resource estimates; hardware
engineering; anything requiring the full rk toolchain.

## 4. Arms

(Filled from lane outputs; see §7 for the current state.)

## 5. Phases

- **Phase 0 (now): stand-up.** Definitions, claims DAG, checkers, three scouting memos,
  this PRD. Exit: TJO ratifies arms.
- **Phase 1: probes.** Per ratified arm, one <=1-day numerical or analytic probe per
  candidate, each ending in a claim row and a checker. Exit: critic round on the probe
  claims; ranked candidate list.
- **Phase 2: bite.** One candidate gets a full proposer/critic loop to PROVED or REFUTED.
- **Phase 3: writeup.** Only rows with converged verdicts. Ratchet audit before drafting.

## 6. Decision record

| id | date | decision | by |
|----|------|----------|----|
| D1 | 2026-09-02 | Method is rk-light, not rk. rk stays available for a later hardening phase. | TJO |
| D2 | 2026-09-02 | North star as in CLAUDE.md §1: real speedup (time or space or both) over best-in-class classical; BQP-completeness a bonus; must admit a cheap heuristic hardware attack. | TJO |
| D3 | 2026-09-02 | Subagent roster: Opus and codex gpt-5.6-sol xhigh. No Fable subagents. | TJO |
| D4 | 2026-09-02 | Applications are part of the exploration; net cast wide from robotics to serious algebraic geometry. | TJO |
| D5 | 2026-09-02 | Robotics is a first-class arm with its own scouting lane. | TJO ("i would love a robotics application") |
| D6 | 2026-09-02 | Seed (2026-09-01 analysis, notebook page 81) is read-only under `seed/`; nothing from it enters the DAG above SKETCH without a converged verdict in this campaign. | orchestrator, under L1 |
| D7 | 2026-09-02 | Campaign repo is this directory, git-initialized in place; bd prefix `qaag-`. | orchestrator |

## 7. Current state and open questions for TJO

(Filled after lane harvest.)
