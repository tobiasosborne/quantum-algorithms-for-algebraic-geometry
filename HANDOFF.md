<!-- ROLE: current state + fast restart. Rewritten at session close; <=150 lines. -->

# HANDOFF — 2026-09-04, exploration round 2 paused

## Start here

The user requested a quick handoff so the next session can restart immediately.
Round 2 is INCOMPLETE. Four construction memos exist; none establishes a qualifying
new quantum algorithm. No round-2 claim or definition has been merged.

1. Run `bd prime`; read CLAUDE.md and PRD criteria 1–6 / decisions D22–D23.
2. Launch an **Astra critic** with `briefs/critic-original-round2.md`, writing
   `verdicts/original-round2-r1.md`. All four input memos are present.
3. In parallel, if useful, launch an **Astra proposer** with
   `briefs/round2-astra-construction.md`, writing `scouting/original-astra-round2.md`.
   This is a further constructive attempt, not another critique of the same ideas.
4. Use Sol for repairs. Maximum TWO concurrent subagents. Critic loops must converge
   before merging adjudicated rows. Do not call unverified identities new algorithms.

Both Astra tasks were launched but failed with the account usage-limit message before
producing their requested files. Neither target file exists. They need a fresh launch;
do not assume a review or an additional construction has happened.

## Binding user steering

- **New means new to the field:** an unsolved problem-level result AND an original
  quantum algorithmic mechanism, not a new encoding, application, parameter regime,
  or substantive equivalent of a described quantum algorithm.
- No Grover, QFT, DQI, or other established algorithms repackaged as proposals.
  DQI AND proposed extensions are explicitly excluded. No more web-led scouting.
- Algebraic geometry broadly is the domain. Existing discoveries are optional;
  the search is not restricted to Fock/Macaulay constructions or quantum-state varieties.
- **Only Astra and Sol subagents** (D23 supersedes the old Opus/cross-family roster).
  Prefer independent Astra criticism of Sol proposals. Never launch Opus.
- Originality is not certified merely because we derived something independently.
  The user wants actual new mechanisms, not a literature survey or a menu of objects.
- The north star still requires a matched classical advantage and a concrete cheap
  heuristic/hardware route. Do not substitute tomography for a single-copy comparator.

## What this session produced

| File | Result and limitation |
|---|---|
| `scouting/original-growth-round2.md` | Root: exact uniform graded-quotient growth and Hilbert-series reservoir identities. Free retry fails by measurement backaction; a radical quadratic two-component family gives an exponentially small reservoir gap. No recovery/mixing theorem or new algorithm. |
| `scouting/original-algebra-round2.md` | Sol: adjoint multiplication gives exact coherent factorisation samples. Natural equation-level access may already require solving the quotient. Nonreduced trace pairing degenerates. Exterior Newton and finite-difference jets fail resource/equivalence tests. |
| `scouting/original-geometry-round2.md` | Sol: exact finite-copy rational-map normal form, minimal copy-degree and optimal-success bounds; occupation-based tangent-cone instrument; regressive Grassmann meet. No speedup survives the access, single-copy, normalization and known-operation audits. |
| `scouting/original-broad-round2.md` | Sol: positive correspondence fusion has the same output law as two-history collision sampling; signed fusion is LCU; birational order interference is controlled composition/quantum-switch territory. No survivor. |

Each memo has a provisional MERGE PROPOSAL. Held speedup/existence hypotheses must stay
held; an exact operation identity does not establish its missing access or hardness lemma.
No literature results from the aborted initial search were promoted to candidates or claims.

Supporting files:
- `briefs/round2-original-algebra.md`, `briefs/round2-original-geometry.md`: completed Sol lanes.
- `briefs/critic-original-round2.md`: ready for Astra; allows local read-only shell and
  bounded recomputation. Its earlier shell prohibition was removed.
- `briefs/round2-astra-construction.md`: ready; explicitly excludes recycling the first batch.
- `checkers/explore/quotient_growth.py`: bounded exploration, excluded from run_all.sh.
  Baseline PASS (137 checks); all three mutations exit 1, recorded in MUTATIONS.md.
  Checks take under one second with one BLAS thread. Last code change only clarified
  the printed “Lüders failure posterior” label; it did not change the calculation.

## Specific points for the critic / repairs

- Growth: the Lüders counterexample does not forbid every possible recovery map.
  The reservoir counterexample proves a worst-start gap bound, not a universal
  vacuum-start mixing lower bound. Projected jump implementation is not free.
- Algebra: separate the unzipping identity from the held useful-speedup conjecture.
  Trace pairing is not automatically a positive Hermitian metric. Root-correlated
  registers do not provide classical root coordinates.
- Geometry: C3 conjugation; no physical antiunitary Hodge star. The copy lower bound
  is the reduced algebraic degree of the map/iterate, not necessarily its unreduced
  composition degree. Extra accepted branches can cover one another's zeros.
  Jet scalar multiplicity has an identical single-copy comparator.
- Broad memo: check the effective history-to-endpoint Kraus normalization
  (likely 1/sqrt(P), with a second 1/sqrt(P) from the prepared uniform input).
  Classical collision sampling needs equally available uniform history sampling.
  The rational birational example need not supply a finite-dimensional invariant
  section space. Keep gate-list controlled order distinct from unknown-channel access.

## Tracking and repository state

- `qaag-47l`: round-2 epic, IN_PROGRESS.
- `qaag-6ac`: algebra proposer work completed; includes the broader follow-up memo.
- `qaag-s06`: geometry proposer work completed.
- `qaag-tzn`: synthesis/adversarial audit, IN_PROGRESS; this is the immediate work.
- Governing updates: PRD criterion 6 and D22 (novelty), D23 and CLAUDE.md (Astra/Sol).
- Baseline claims remain C-001..C-334: 163 SKETCH, 91 CONJECTURE, 80 REFUTED, 0 PROVED.
  Definitions unchanged. Round-1 final verdicts and all seed files remain intact.
- A prior Opus CLI attempt failed with API DNS resolution; its escalation was cancelled.
  It produced NO review. Only Astra/Sol are authorised now.
- No Git remote is configured. Do not invent one or create a hosted repository.
  Session files are committed locally; remote push requires a supplied destination.
- Earlier campaign history and the round-1 shortlist are preserved in Git and PRD.
  Do not restart familiarisation, rerun the full old numerical suite, or resume the
  superseded literature-led approach.

## Commands that matter

```bash
bd prime
bd show qaag-47l
bd show qaag-tzn
git status --short --branch
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 timeout 60 python3 -B checkers/explore/quotient_growth.py
```
