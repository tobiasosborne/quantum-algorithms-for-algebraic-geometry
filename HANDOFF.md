<!-- ROLE: current state + next steps. UPDATE POLICY: rewritten whole at session close,
     <=150 lines. TRIGGER: read at session start (item 4 of the CLAUDE.md read order). -->

# HANDOFF — quantum-algorithms-for-algebraic-geometry

## State (2026-09-02, session 1 close: campaign stood up under rk-light)

- Method: rk-light (CLAUDE.md laws L1–L5, rules 1–10). Not rk. Tracking: bd, prefix `qaag-`.
- North star: CLAUDE.md §1. Robotics is a first-class arm (PRD D5).
- Seed (2026-09-01 analysis + notebook page 81) is read-only under `seed/`.
- `definitions/definitions.md`: 66 entries + 2 stubs (D-arveson-curvature,
  D-essential-normality), conventions C1–C12 binding, 14 OPEN issues (substantive:
  OPEN-1, 3, 5, 6, 7). `definitions/notation.md`: symbol table, 18 page81-vs-report conflicts.
- `claims/CLAIMS.md`: 254 rows (157 SKETCH, 40 CONJECTURE, 57 REFUTED, 0 PROVED), 529
  edges, acyclic. Critical-claims section lists the 8 rows for the first critic cycle.
- Scouting: `scouting/classical-landscape.md` (codex, 2113 lines, 9 ranked candidates,
  21 traps, 63 refs none marked unverified: treat as unverified), `applications-wide-net.md`
  (Opus, 325 lines, shortlist of 8, filters F1–F6, Observations A/B),
  `robotics-deep-dive.md` (Opus, 763 lines, bets R1–R3, killers K1–K10),
  `real-variety.md` (codex, 2146 lines, 10 routes, 15 killers, 0 refs marked unverified:
  treat as unverified), `robotics-space.md` (Opus, 1363 lines, D13 proposer lane; refs
  resolved live except the Watrous/BCP primaries, see its §8), `two-copy-real-filter.md`
  (Opus, 400 lines, all 7 refs resolved).
- Checkers: `checkers/` 16 red-capable checkers (14 ported from seed + Fact 7.1 + Fact 7.2),
  3717 checks, 17 mutations all red; orchestrator re-ran both independently 2026-09-02
  (413 s wall, all PASS; 17/17 RED). Suite uses generators as written, NOT unit
  Bombieri–Weyl (departs from C5, matching the seed); a unit-BW re-run is bead work.
- PRD.md: north star, success criteria, arms A/B/C/D/R/X, phases, decisions D1–D9, ten
  open questions for TJO (§7).

## Findings this session (not yet critiqued; nothing promoted)

- Two-copy real filter (D14): strong form CLOSED. For a real ideal the compressed filter
  spectrum is identical whether or not V has real points (checked numerically to 1e-15);
  a conjugate-pair ghost state passes. Survivors: coherent response (cos 2t)^{2N}, exact
  real-point count via the coherent frame, a one-pair linear-optics certificate. Rows
  C-275..C-280, PRD D16. Exploration script checkers/explore/twocopy_real_filter.py.

- SP-0 (space lane): BQSPACE(s) in DSPACE(s^2) and DTIME(2^O(s)); pure quantum space
  advantage is capped at a quadratic gap. Bet R1's 250 GB sentence refuted; survivors are a
  simultaneous (space,time) claim (conditional on bosonic GLH hardness, C-269) and an
  unconditional streaming/communication separation with a one-photon linear-optics protocol.
  Rows C-264..C-274, PRD D15 (pending TJO).

- Fact 7.2 (quadric gap bound via Takagi) holds on all eight quadrics tested; cones pinch
  to equality Delta_N = ||f||^2_Fock; tau_min = 0.0165 explains the flat P^4 survey row.
  Four minor seed discrepancies recorded in checkers/README.md, none touching a §2–7 theorem.

- Seed's §7 gap survey used unit-coefficient, not unit-Bombieri–Weyl, generators
  (definitions OPEN-1): it is not yet evidence for Conjecture 8.3(a) / C-132.
- Three seed errors missed by both referee rounds: 8.3(b) upper bound inequality backwards
  for d >= 2 (C-135); page81 annihilation identity fails at k=(1,1,1) (C-193 REFUTED);
  distance formula report L146 off by ||f|| (C-078).
- Round-1 finding #77 (FATAL on the whole quantum-algorithmic programme) was never
  retracted: C-250. This is why nothing enters above SKETCH.
- Robotics: kinematics is zero-dimensional (codim = n) and the seed's observables need
  codim O(1); only closure/self-motion varieties (bet R3) escape. Motion planning is
  PSPACE-complete so no quantum space advantage exists there.
- Applications: the construction is complex projective; nearly every classical application
  asks a real question. Best fit is quantum-native varieties (multigraded QSAT).

## Next steps

TJO answered Q1 and Q2 on 2026-09-02 (PRD D10, D11): design-time speedups count, robotics
target is bet R2; real-variety lane opened (`briefs/lane-real-variety.md`, codex scout,
output `scouting/real-variety.md`). Real-variety scout harvested as arm E (D12); its 7 D-entries and 9 claim rows C-255..C-263
are merged verbatim. Still open: PRD §7 Q3–Q11.

1. Robotics bet R1 must be reframed (K-RV8/9): compare against implicit Lanczos on the
   residual hierarchy, not dense Lasserre; the 250 GB space claim is withdrawn from R1.
2. Arm X kill-first checks (each one bead, one checker or one short memo):
   C-099 Schur–Weyl classical easiness at fixed local dimension; C-110 literature scout
   for a multi-generator Bombieri inequality (codex or Opus, not a proof); re-run the gap
   survey with unit-BW generators (OPEN-1).
3. Cheapest numerics, ~20 lines each on `checkers/bf.py`: Fact 7.2 Takagi slope
   (C-108/C-109); cone criterion on a cubic with/without dependent partials (C-136);
   robotics bet R3 degree growth via HomotopyContinuation.jl (one day).
4. First critic round on the 8 critical claims (codex gpt-5.6-sol xhigh as critic, Opus
   as proposer; verdicts in `verdicts/<claim>-r1.md` per CLAUDE.md L5).
5. Reference verification pass over both scouting ledgers (bead filed).

## Conventions / pitfalls

- Fock basis |k> = z^k/sqrt(k!); page81's projective basis differs degreewise by the
  scalars in D-norm-comparison. Spectral promise is on Delta_N / alpha_BE (C5, C7).
- Fact 7.1 uniform gap is a Fock-normalisation statement; in Bombieri–Weyl it reads
  Delta_N >= binom(N,m)^{-1} ||f||_BW^2.
- Delta_N depends on the generating tuple, not the ideal; compare only at unit BW.
- Gröbner path needs a w-Gröbner basis as generators, else not flat at t = 0.
- Subagents: Opus, or codex per CLAUDE.md rule 2. No Fable subagents. Briefs as files
  under `briefs/`; disjoint lanes; shared files merged by the orchestrator only.
- Lane timing this session: Opus lanes 25–38 min each; codex classical memo ~25 min.
