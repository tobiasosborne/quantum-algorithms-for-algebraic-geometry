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
Hutch++ on the implicit Macaulay matrix, NOT dense rank. Hardware: Bose–Hubbard and spinor-BEC spin mixing for quadric generators (row C-024, weakened
2026-09-03 by C-323 (C-NEW-QN-C024-WEAKENING): the interaction is realised and its spin-changing dynamics
observed, but the `2N+1` degeneracy has not been measured). Dequantization
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
geometric quantity at polynomially resolvable scale. Update 2026-09-03 (`scouting/intersection-observables.md`, critic loop r1–r3): the seed's suggested test has been run. The conditional is MET exactly for linear families (C-325 (C-NEW-IO-LINEAR-EXACT): Tr(P_{Sym^N U} P_{Sym^N W}) = h_N(sigma^2)) and NOT met in general (the clean-intersection law C-NEW-IO-CLEAN is held on the unproved ambient Bergman-frame estimate, Geometry 2.4). C-085, C-086 and C-168 are REFUTED as written (tangency gives exponent 1 - 1/m at dim(V ∩ W) = 0; the registered Toeplitz normalisation diverges), with surviving statements C-166/C-167 (amended) and C-331 (C-NEW-IO-TOEPLITZ). The normalised signal survives to codim(V ∩ W) = O(log n) (C-333 (C-NEW-IO-SIGNAL)); the arm reduces to arm A on a concatenated generator list (held C-NEW-IO-SUM-IDEAL) and scores 1/5 on evidence; not closed by a baseline argument.

**Arm D: quantum-native varieties.**
Candidates: multigraded quantum k-SAT ground spaces and their inverse-system description
(seed Prop 8.2; applications shortlist 1), entanglement and tensor-network varieties,
with phylogenetic varieties as the classical shadow (shortlist 5). The only area where
the input model does not defeat the construction. Hardware: dual-rail linear optics for
the (1,...,1) sector, the existing spinor-BEC conic. Products are new statements about QSAT, plus possibly an analogue demonstration. The arm reports
(2026-09-03, `scouting/quantum-native.md`, critic loop r1–r3): no north-star speedup is
established. What is argued is only that composing an algorithm with the QSAT–inverse-system
relabelling supplies no asymptotic advantage (C-324 (C-NEW-QN-ARM-D-NORTHSTAR), CONJECTURE, held) — a
tautology about a spectrum-preserving relabelling, not an impossibility theorem. The broad
negative "no arm D speedup exists" is NOT proved and remains an open negative; it explicitly
excludes the bosonic Proposition 8.2 sector (C-129/C-130), copy-access membership and distance
testing for entanglement, secant, MPS and tensor-network varieties, and structured QSAT
subfamilies. For copy-access problems the comparator is adaptive single-copy measurement plus
classical post-processing; exponential separations against it exist for other learning tasks
(arXiv:2111.05881; DOI 10.1126/science.abn7293) but no transfer to variety membership is known.

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

**Arm R, space direction (D13).** `scouting/robotics-space.md` (Opus, 1363 lines).
Governing fact SP-0: BQSPACE(s) is contained in DSPACE(s^2) and DTIME(2^O(s)) (Watrous 2003
composed with Borodin–Cook–Pippenger 1983; the log-space case is quoted verbatim by
Fefferman–Remscrim). Consequences: with a re-readable input, a pure quantum space advantage
can never exceed a quadratic gap in the space exponent; "n log N qubits versus M_N words" is
not a space separation; at n=100, r=3 the honest classical space for the residual-hierarchy
minimum eigenvalue is about 300 bits, not 250 GB and not 28 MB. What survives is a
SIMULTANEOUS (space, time) claim: quantum poly(n, log N) space with poly time under a
guiding-state promise, versus classical either M_N words or log^2 space with poly(M_N)
time; no classical algorithm with both is known, and none exists unless BQP = BPP provided
the bosonic guided-local-Hamiltonian problem (C-269 (C-NEW-SP-GLH-BOSONIC)) is BQP-hard.
Two survivors: (i) streaming / communication: an UNCONDITIONAL separation, tiny margin,
realisable with one photon in n modes plus phase shifters and one beamsplitter, close
relative already run (DOI 10.1038/s41467-019-12139-z); (ii) succinct-operator (space, time)
Pareto claim, large nominal margin, conditional, and currently missing a robotics family that
provably needs Lasserre order r >= 3. Killer coverage: K5 right for zero-dimensional root
lists, wrong for certification, inconsistent noisy systems, positive-dimensional witness
sets, streaming; K6 right at polynomial space, silent at the s versus s^2 resolution where
every real space claim lives; K-RV8 walls out at r=4..6 (736 MB to 273 GB at n=100); K-RV9
is a treewidth statement that fails for hub-coupled TLS perception. Eleven rows
C-264..C-274 and three definitions merged verbatim.

Two-copy real-symmetry probe (D14, `scouting/two-copy-real-filter.md`): the STRONG form
is closed. For a real ideal the compressed pairing-state filter on ker H_N x ker H_N has rank
one and top eigenvalue HF/M_N regardless of whether V has any real points; a conjugate pair
|p>^N + |pbar>^N passes with R = 1 although p is complex (C-276, C-278). The filter sees
"real vector in the ground space", not "real point". What survives: the coherent-state
response R = (cos 2t)^{2N} with t the Fubini–Study angle to RP^n (C-277); an exact real-point
COUNT #V_R = Tr(G_hat^{-1} G) from the coherent frame (C-279), inheriting Hermite
conditioning K-RV6; and a one-pair linear-optics-native CERTIFICATE that a supplied product
ground state is a real point (C-280): it verifies, it does not find. Second quantisation:
|Phi_N> is the N-photon sector of the multimode two-mode-squeezed vacuum, so the pairwise Bell
projection is native, at acceptance (n+1)^{-N} pairwise versus 1/M_N collective.

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
| D13 | 2026-09-02 | Robotics explores BOTH space and time. The space killers (K5, K6, K-RV8, K-RV9) are judged vague and weak; a proposer lane develops space claims rigorously (`briefs/lane-robotics-space.md`). | TJO ("not convinced we have exhausted space claims") |
| D14 | 2026-09-02 | Probe TJO's two-copy real-symmetry idea: the antilinear realness condition becomes linear on two copies via the pairing state; lane `briefs/lane-two-copy-real.md`. | TJO question, orchestrator |
| D15 | 2026-09-02 | Fact SP-0 (quadratic ceiling on pure space advantage in the read-only-input model) is a campaign-wide constraint: every row comparing a qubit count to a classical word count must be audited against it; robotics bet R1's space sentence is refuted on these grounds, more strongly than by K-RV8. | orchestrator, from space lane; pending TJO ratification |
| D16 | 2026-09-02 | Two-copy real-symmetry filter: strong form (spectral selector of real points) closed by C-276/C-278; certificate and count forms stay open as instruments. Rows C-275..C-280 merged. | orchestrator, from lane; pending TJO |
| D17 | 2026-09-03 | Exploration round 1 (TJO directive: rapid ground, then verifiers, loop; two concurrent subagents). Quantum-primitives map (`scouting/quantum-primitives.md`, codex proposer, Opus critic, PASS at r3 with objections 25 -> 11 -> 3) merged as C-281..C-303 and 14 definitions. Verdict of the map: no known quantum primitive scores above 4/5 against §2; Kedlaya's curve-zeta algorithm (4/5, prior art, no hardware hook) and Hallgren / Eisentraeger-Hallgren-Kitaev-Song number-field ideal problems (3/5, prior art; input is an ideal of a number field, not a projective variety) are the benchmarks any campaign claim must beat; eleven primitive-problem pairs enter REFUTED (C-282, C-284, C-289, C-292, C-294, C-296, C-297, C-299, C-300, C-301, C-303). The SKETCH legend of CLAIMS.md is widened to admit cited published theorems with resolved ids (C-092/C-099 convention). Arm B (Koszul/Betti Laplacian, `scouting/koszul-betti.md`) is in its critic loop; arms C and D lanes launched. | orchestrator; pending TJO ratification of the benchmark reading |
| D18 | 2026-09-03 | Arm B (Koszul/SUSY Betti Laplacian, `scouting/koszul-betti.md`, Opus proposer, codex critic) converged: verdicts r1 FAIL(1 FATAL, 11 MAJOR) -> r2 FAIL(4) -> r3 FAIL(1) -> r4 (verbatim residue) -> r5 PASS. Merged C-304..C-311 (6 CONJECTURE, 2 REFUTED) and 8 definitions; C-NEW-KB-QMA1 and C-NEW-KB-GAP-INDEPENDENT held in the memo. Verdict of the arm: the Betti table IS the ground-state degeneracy of a boson-fermion Laplacian on the inverse system (exact, tested on six ideals), but no PRD §2 criterion is met: the problem reduces to quantum TDA via Hochster (K-KB3), the naive compression is information-free (K-KB2), the Betti gap has no lower bound (K-KB6), and the Hilbert-function acceptance weight h_N/M_N is exponentially small on the quadratic complete-intersection family (K-KB11). Arm B is an instrument and a hardness anchor, not a speedup candidate; no prover seat. | orchestrator, from the loop; pending TJO |
| D19 | 2026-09-03 | Arm D (quantum-native varieties, `scouting/quantum-native.md`, codex proposer, Opus critic) converged: r1 FAIL(12 MAJOR, 9 MINOR) -> r2 FAIL(1 FATAL, 1 MAJOR, 5 MINOR) -> r3 PASS. Merged C-312..C-324 (8 CONJECTURE, 5 REFUTED; C-324 held) and 8 definitions plus a D-multihomogeneous-bezout amendment. Verdict of the arm: the QSAT ground space IS the multidegree-1 piece of a Macaulay inverse system (exact, verified numerically), product ground states ARE the points of a multiprojective variety with an entangled defect e_Q, and diagonal Hilbert-function vanishing is a multihomogeneous Nullstellensatz hierarchy of product-unsatisfiability certificates whose level 2 is incomplete (first certifying level r = 4 on the generic four-qubit family); but no PRD §2 criterion 3 is met, the product-satisfiability geometry is prior art (Laumann et al. 2010; Aldi-Gharibian-Rudolph 2026), and arm D is an instrument and a dictionary, not a speedup candidate. The broad negative is NOT proved (see §4 arm D). C-024 weakened in lockstep. Open for TJO: Q4 (does an exponential copy saving count) and Q13 (should novelty become an explicit §2 criterion). | orchestrator, from the loop; pending TJO |
| D20 | 2026-09-03 | Arm C (intersection and integration observables, `scouting/intersection-observables.md`, Opus proposer, codex critic) converged: r1 FAIL(3 FATAL, 5 MAJOR) -> r2 FAIL(4 MAJOR, 1 MINOR) -> r3 PASS. Merged C-325..C-334 (8 CONJECTURE, 2 REFUTED) and 6 definitions; C-NEW-IO-CLEAN and C-NEW-IO-SUM-IDEAL held. Seed rows amended in lockstep per the critic's paste blocks: C-085, C-086, C-168 REFUTED with surviving statements; C-166, C-167 restated (clean/transverse hypotheses, Morse-Bott prefactor); C-079, C-087, C-169 dependencies and tests updated. Verdict of the arm: the intersection overlap is exact and elementary for linear subspaces, metric rather than algebraic off the clean locus, visible at additive precision only to codim O(log n), and reduces to arm A on the sum ideal; the SWAP-test hardware hook (difference-mode photon parity) is real but assumes ground-space mixture preparation. Score 1/5. | orchestrator, from the loop; pending TJO |

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
3. **Robotics: space or time?** ANSWERED 2026-09-02 (D13): both. Space direction gets its
   own proposer lane; the existing killers are not accepted as final.
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
11. **Space-direction follow-ups** (`scouting/robotics-space.md` §7, condensed): (a) does a
    simultaneous (space, time) claim count as a space claim under D2, given SP-0 closes pure
    space claims at a quadratic gap; (b) is a promise problem an acceptable robotics
    deliverable, since every available space separation is one; (c) does communication
    bandwidth count as space (the only unconditional separation is a communication one);
    (d) is a BQ_USPACE-completeness theorem a product, given it also proves the problem
    classically space-cheap; (e) budget: streaming lane for one week to run experiment E3,
    then the succinct-operator route only if (f) is answered; (f) does anyone in TJO's
    network know a robotics family that provably needs Lasserre order r >= 3, otherwise R1
    closes as unmotivated; (g) ratify SP-0 as campaign-wide (D15) and audit qubit-vs-word
    rows; (h) the robotics memo's contact-mode counts are off by three orders of magnitude
    and Stephenson II is ten degree-8 equations in ten unknowns, not 26: merge corrections?
12. **Two-copy follow-ups** (`scouting/two-copy-real-filter.md` Questions, condensed): (a)
    does the one-pair real-point certificate count as a product (recommended: instrument and
    arm E hardware demo, not a north-star hit); (b) amend real-variety Route 2 in lockstep
    (its 1/5 is right, its reason is wrong); (c) fund one analytic day on the robust version
    of the certificate (eps-close product, real, low-energy state implies Fubini–Study
    distance to V_R bounded in N, Delta_N, condition number); (d) fold the real-point count
    into the Hermite lane rather than a new lane.
13. **Multigraded mechanism dictionary** (robotics memo Q5): a 2-local frustration-free
    qutrit chain whose zero-energy product states are a mechanism's configurations. Not a
    speedup; possibly the right physics paper. Pursue as its own item?
