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

Spectral promise convention (definitions lane, 2026-09-02): the campaign's spectral
promise is on the normalised gap $\Delta_N/\alpha_{\mathrm{BE}}$ (definitions C5, C7);
absolute $\Delta_N$ statements are presentation artefacts. The seed's §7 survey numbers
are unit-coefficient, not unit-Bombieri–Weyl (definitions OPEN-1), so they are not yet
evidence for the seed's Conjecture 8.3.

Out of scope until a phase change: fault-tolerance resource estimates; hardware
engineering; anything requiring the full rk toolchain.

## 4. Arms

Proposed 2026-09-02 from the four scouting memos; not yet ratified by TJO. Each arm names
its candidate problems, the classical baseline it must beat (from
`scouting/classical-landscape.md`, "the classical memo"), the claim rows it rests on, and
its heuristic-hardware hook.

**Arm A: spectral core (the seed's own programme).**
Candidates: additive estimation of the distance to a degree piece of an ideal (classical
memo rank 1; rows C-124, C-078); normalised Hilbert function in low codimension (rank 2);
the Macaulay gap itself: uniform Bombieri inequality C-132, cone criterion C-136, gap
versus Bürgisser–Cucker condition number C-170/C-172. Baseline: sparse Krylov / LSQR /
Hutch++ on the implicit Macaulay matrix, NOT dense rank. Hardware: Bose–Hubbard and
spinor-BEC spin mixing for quadric generators (row C-024, unrefereed). Dequantization
risk medium to high. This arm is where the first critic cycle (D9) lands.

**Arm B: syzygies and Betti numbers as a supersymmetric Koszul Laplacian.**
Candidates: normalised Betti fractions and syzygy nullities (classical memo rank 4;
applications memo shortlist 2). Untouched by the seed. Baseline: block Wiedemann,
Schreyer frames, stochastic trace filtering. Exact Betti numbers are excluded by
#P-hardness. Likely product is a theorem, not a speedup.

**Arm C: intersection and integration observables.**
Candidates: Tr(P_I P_J)/M_N and Toeplitz integration (classical memo rank 5;
applications shortlist 4; rows C-166/C-168). The most plausible genuinely new PROBLEM in
the seed. Baseline: randomized trace products, witness-set intersection. Dequantization
risk high; the arm is valuable only once a theorem ties the normalised observable to a
geometric quantity at polynomially resolvable scale.

**Arm D: quantum-native varieties.**
Candidates: multigraded quantum k-SAT ground spaces and their inverse-system description
(seed Prop 8.2; applications shortlist 1), entanglement and tensor-network varieties,
with phylogenetic varieties as the classical shadow (shortlist 5). The only area where
the input model does not defeat the construction. Hardware: dual-rail linear optics for
the (1,...,1) sector, the existing spinor-BEC conic. Products are new statements about
QSAT, plus possibly an analogue demonstration; a speedup in the north-star sense is not
on offer here and the arm should say so.

**Arm R: robotics (TJO priority, D5).**
`scouting/robotics-deep-dive.md` finds three bets and ten killers. Bets: R1, certified
lower bounds for perception polynomial optimisation via the bosonic moment hierarchy (a
SPACE claim: dense Lasserre level 3 at n=100 is ~250 GB, versus ~300 qubits); R2,
amplitude amplification over the design set of a six-bar synthesis system (a TIME claim,
quadratic, design-time only); R3, degree and dimension of closure / self-motion varieties
of many-joint mechanisms, the only robotics family in codimension O(1), decidable by a
one-day HomotopyContinuation.jl experiment. Killers K1–K10 are sharp: kinematics is
zero-dimensional so the seed's normalised observables carry a signal of 1e-4 or worse;
robotics wants real solutions and exact small integers; the classical best is homotopy
continuation, which is small-space and parallel; motion planning is PSPACE-complete so
no quantum space advantage exists. The arm stays open only if TJO answers §7 Q1–Q2.

**Arm E: real varieties (D11).**
`scouting/real-variety.md` (codex, 2146 lines, 10 routes, 15 killers). Bottom line: there is
no complex-linear projector onto the real part of a ground space (K is antiunitary), and a
real Gaussian measure does not repair it; the exact algebraic replacement is the inverse
system of the complexified real radical, which is circular to compute. Ranked routes: a
sparse residual spectral hierarchy on the real sphere (3/5; compare with implicit Lanczos,
not dense SDP); normalised Hermite signature with a succinct oracle (2/5); real-radical
inverse system from a truncated moment state (2/5); positive toric fibre Hamiltonians (2/5
speedup, 4/5 hardware, but stoquastic); totally real Boolean varieties (2/5, Grover-limited).
Nine claim rows C-255..C-263 and seven D-entries merged verbatim. Two corrections to arm R:
the seed ground energy is NOT the Lasserre/DPS value without maximal-symmetry and localizing
constraints (C-261 (C-NEW-RV-R1-NONEQUIVALENCE)), and the "250 GB versus 300 qubits" space
statement in bet R1 compares against dense SDP when the seed matrix admits O(B_3)-space
Lanczos (K-RV8/9); R1 must be reframed as a spectral-hierarchy comparison.

**Arm X: kill-first checks (run before anything else is funded).**
C-099: permutation-invariant Hamiltonians at fixed local dimension are classically easy
(Schur–Weyl), which would remove the whole fixed-n, growing-N regime. C-110: whether a
multi-generator Bombieri inequality already exists (a literature scout, not a proof).
C-250: the unretracted FATAL round-1 verdict on the quantum-algorithmic programme.
Definitions OPEN-1: the seed's gap survey used unit-coefficient rather than
unit-Bombieri–Weyl generators, so the numerical evidence for C-132 has to be redone
before it counts.

Cross-cutting traps (classical memo, 21 named): comparing against dense rank instead of
sparse iterative methods; changing the output (state versus explicit roots); hidden state
preparation; exponentially small overlaps; hiding exponential N; treating boson sampling
as a universal algebraic accelerator; ignoring dequantization. Every claim row that
asserts a speedup must name which traps it has been checked against.

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
| D8 | 2026-09-02 | Claims baseline. The seed enters as a proposer document under an unretracted FATAL referee verdict (round-1 #77, row C-250). Its 254 claims are in `claims/CLAIMS.md` (157 SKETCH, 40 CONJECTURE, 57 REFUTED, 0 PROVED); status moves only via `verdicts/`. | claims lane merge |
| D9 | 2026-09-02 | First critic cycle scope: the eight "Critical claims for the north star" rows in CLAIMS.md: C-124, C-132, C-170/172, C-144/146, C-136, C-150/154, C-166/168, C-099. Sequencing: settle C-110 (novelty of the Fock/Macaulay identification) and C-099 (fixed local dimension is classically easy) first. | claims lane merge, pending TJO |
| D10 | 2026-09-02 | Design-time (offline) speedups count toward the north star. Robotics arm R stays open; bet R2 (kinematic synthesis) is its target, bet R3's one-day experiment still runs. | TJO |
| D11 | 2026-09-02 | Open a real-variety lane: a formulation whose ground space or observable sees real (or positive) points, or the moment/SOS side. | TJO |
| D12 | 2026-09-02 | Real-variety lane harvested as arm E; robotics bet R1 loses its dense-SDP space comparison and is reframed against implicit Lanczos on the residual hierarchy (memo Q5, Q9). | orchestrator, from lane merge |

## 7. Current state and open questions for TJO

State at 2026-09-02 (stand-up session): repo scaffolded; `definitions/` 66 entries + 2
stubs, 14 OPEN issues; `claims/CLAIMS.md` 254 rows, 529 edges, 0 PROVED; four scouting
memos (classical 2113 lines, applications 325, robotics 763, checkers pending). Three
seed errors found that neither referee round caught: the Conjecture 8.3(b) upper bound
has its inequality backwards for d >= 2 (C-135 downgraded); page81's annihilation
identity fails at k=(1,1,1) (C-193 REFUTED); the distance formula at report L146 is off
by ||f|| (C-078 corrected).

Questions only TJO can answer, in order of how much they change the next step:

1. **Real versus complex.** ANSWERED 2026-09-02 (D11): lane opened, brief `briefs/lane-real-variety.md`. Original question: every classical application area asks a real or positive
   question; the construction is complex projective. Open a lane on a real/positive
   analogue (moment/SOS side, or a Hamiltonian whose ground space sees real points), or
   accept that applications are restricted to complex questions and quantum-native
   inputs? Largest scoping decision on the table.
2. **Robotics: is a design-time (offline) speedup acceptable?** ANSWERED 2026-09-02 (D10): yes; bet R2 is the target. Original question: the only robotics problem
   at asymptotic size is kinematic synthesis (CPU-days, offline). If the application
   must run on a robot, the honest answer is that the arm closes after bet R3's one-day
   experiment. If design-time counts, bet R2 is the target.
3. **Robotics: space or time?** Bet R1 is space-only, R2 time-only; the lane budget
   supports one.
4. **What counts as a product?** The north star says speedup. Three of the top four
   application shortlist entries are new invariants or dictionary theorems (SUSY Betti
   Laplacian, metric regularity, analytic intersection theory), not speedups. Do these
   count as deliverables, only as instruments, or not at all? Same question for an
   analogue demonstration (a two-generator spinor-BEC extension whose degeneracy is a
   Hilbert function) and for a quantum-only certificate that no classical checker can
   verify.
5. **Ratify D9 sequencing:** run the kill-first checks (C-099, C-110, OPEN-1 re-survey)
   before any prover seat is funded on arm A. Recommended: yes.
6. **Second deep lane.** Recommendation from the applications scout: quantum-native
   varieties (arm D), because it is the only place the input model does not defeat the
   construction. Alternative if a classical application is wanted at all costs:
   algebraic statistics.
7. **Finite fields.** Seed Conjecture 8.8 closes that direction; it is also the only
   direction where 1e7 to 1e10 column Macaulay matrices are actually built
   (cryptanalysis). Treat 8.8 as settled, or fund one bounded attempt at a
   divided-power / q-deformed Fock model?
8. **Ratchet the scouting by-products?** Observations A and B (applications memo §1) and
   the two lane numerics constraining Conjecture 8.7: enter as CONJECTURE/SKETCH/REFUTED
   rows now, or leave in scouting until a checker reproduces them?
9. **Reference verification budget.** The classical memo cites 63 references with zero
   marked unverified, from an offline model; the robotics memo has 28 unverified marks.
   Half a day of DOI resolution before any number is quoted outside the repo?
10. **Real-variety follow-ups** (memo `scouting/real-variety.md`, Questions 1–10, condensed):
    (a) ratchet the R1 correction now: enter C-259, C-260, C-261 together before any R1
    experiment (recommended yes); (b) is a quantum-only scalar lower bound acceptable as
    certification (same as Q4 above); (c) is normalised real-root density an acceptable
    problem, given it never answers existence or rare-real-root questions; (d) fund one
    analytic day on whether a Hermite trace form can be block-encoded from Macaulay access
    without a D-element quotient basis, closing the route if circular; (e) close general
    ETR / CAD as a Fock-space arm (recommended yes).
11. **Multigraded mechanism dictionary** (robotics memo Q5): a 2-local frustration-free
    qutrit chain whose zero-energy product states are a mechanism's configurations. Not a
    speedup; possibly the right physics paper. Pursue as its own item?
