<!-- ROLE: how we work in this repo. UPDATE POLICY: amend only on a felt failure or a TJO
     directive, with a dated note. TRIGGER: read at session start and after any compaction. -->

# CLAUDE.md — quantum-algorithms-for-algebraic-geometry (campaign, rk-light)

Exploratory research campaign run under the rk-light method (five laws below), NOT under
the full rk toolchain (TJO decision 2026-09-02: rk is too heavy for the exploration phase).

## 0. Read order (gate)

1. This file.
2. `PRD.md` — north star, scope, decision record.
3. `claims/CLAIMS.md` — the claims DAG (the only place a status lives).
4. `HANDOFF.md` — current state and next steps.

## 1. North star (verbatim, TJO 2026-09-02)

A genuinely new quantum algorithm giving a real speedup (space, time, or both) over the
best-in-class classical algorithm for the same problem, where the problem comes from
algebraic geometry (varieties, ideals) or its application areas. BQP-completeness is a
bonus, not a requirement. The north star must admit a cheaper heuristic attack via
linear optics with postselection / MBQC, boson sampling, or a natural condensed-matter
model (e.g. Bose–Hubbard). Applications are part of the exploration: cast the net wide,
from robotics and other classical application areas of varieties and ideals to serious
algebraic geometry.

## 2. Laws (rk-light; non-negotiable)

- **L1 — Claims ratchet.** Every claim is a row in `claims/CLAIMS.md`: id, exact
  statement with quantifiers, status in {PROVED, SKETCH, CONJECTURE, REFUTED},
  depends-on, where-proved, where-tested. Status goes UP only after an adversarial
  critic loop converges (verdict in `verdicts/` with no FATAL/MAJOR). Never by the
  author, never at a writeup. REFUTED rows are kept forever.
- **L2 — Single-source definitions.** Every symbol lives once, in `definitions/`.
  Artifacts cite, never redefine. When a claim weakens, its shard, DAG row, HANDOFF and
  PRD move in lockstep; every critic pass audits lockstep explicitly.
- **L3 — Addressable arguments.** Rigorous arguments in `argument/` are Lamport
  hierarchical: numbered steps, explicit ASSUME/PROVE, every leaf citing a definition
  id, a claim id, or a named checker run.
- **L4 — Red-capable checkers.** Everything under `checkers/` must be able to FAIL:
  nonzero exit on violation, no bare `assert`, a mutation for each checker recorded in
  `checkers/MUTATIONS.md`. "Runs without errors" is never a test.
- **L5 — Honest verdicts.** Downgrade over ambition. A sharp refutation with the
  surviving weaker statement is a product. Critic verdicts without a FIX DEMAND and a
  SURVIVING STATEMENT per objection are redone.

## 3. Rules

1. **Model roster.** Subagents: Opus (Claude) and `codex exec -m gpt-5.6-sol -c
   model_reasoning_effort="xhigh"`. NO Fable subagents (TJO directive 2026-09-02).
   Critic and proposer from different model families where possible.
2. **Codex invocation.** Prompt in a FILE under `briefs/`; `-s read-only
   --skip-git-repo-check -o <out> "$(cat brief)" < /dev/null`; background; `timeout`.
3. **Lanes are disjoint.** Every brief names its writable files. Shared files
   (`definitions/`, `claims/CLAIMS.md`, `PRD.md`, `HANDOFF.md`) are edited only by the
   orchestrator, from MERGE PROPOSAL sections in lane outputs.
4. **Tracking in bd** (prefix `qaag-`), never markdown TODOs.
5. **Seed is read-only.** `seed/` holds the 2026-09-01 analysis and the notebook page as
   received; never edited. Claims are extracted from it into the DAG, not proved by it.
6. **Citations.** A reference enters `refs/` only with a resolved identifier (arXiv id
   or DOI) that was actually fetched; unverified citations are marked `[UNVERIFIED]`.
7. **No emoji, no marketing prose.** Concrete statements, concrete numbers.
8. **Every spawned process is bounded**: `timeout` on anything that loops; no
   detached processes.
9. **Commit discipline.** Atomic commits; message states what changed and which
   verdict or checker backs it; end with the acting model's `Co-Authored-By:` line.
10. **Conventions are binding** (added 2026-09-02, definitions lane merge). Conventions
    C1–C12 of `definitions/definitions.md` are binding; an artifact departing from one
    says so in its first paragraph, and cites definition ids rather than restating
    definitions.
