# Lane: applications scout (wide net)

Work fully autonomously; do not ask questions. Repo root: /home/tobias/Projects/quantum-algorithms-for-algebraic-geometry. Read first, in order: CLAUDE.md (laws, north star), seed/analysis-2026-09-01/report.md (the seed analysis; treat as an untrusted proposer document, NOT as established truth), seed/analysis-2026-09-01/referee/round1.md and round2.md (prior critic verdicts), HANDOFF.md, seed/page81.tex (the original notebook page). No emoji, no marketing prose. Mark any citation you cannot resolve to an arXiv id or DOI you are confident of as [UNVERIFIED]. Do not touch seed/ or any file outside your lane.

## Your lane (writable file, nothing else)
- scouting/applications-wide-net.md

## Task
Cast the net wide. The north star (CLAUDE.md §1) says applications are part of the exploration: from classical application areas of varieties and ideals to serious algebraic geometry. Produce a survey memo of application areas where a problem about polynomial ideals / varieties is (a) computationally the bottleneck in practice, (b) has a well-defined best classical method, and (c) where the seed's Fock-space / Macaulay-matrix / coherent-state structure might give a quantum foothold. EXCLUDE robotics (a separate lane covers it in depth) but list adjacent areas (computer vision minimal problems, kinematics of mechanisms in other fields).

Areas to cover at minimum: computer vision (minimal problems, Groebner-basis solvers, Kukelova/Larsson automatic generators); algebraic statistics (ML degree, phylogenetic invariants, graphical models); chemistry and materials (conformation spaces, distance geometry, molecular kinematics, reaction network steady states / CRNT); systems biology (multistationarity); power systems (power-flow equations, number of solutions); coding theory and cryptography (Reed-Solomon/AG codes decoding, multivariate crypto, HFE/UOV, algebraic attacks on ciphers via Groebner bases, Boolean ideals); control theory (polynomial systems, stability); economics (Nash equilibria as polynomial systems); tensor decomposition and machine learning (secant varieties, identifiability, neural network expressivity varieties); combinatorial optimization via Boolean ideals (Nullstellensatz certificates, Lovasz-Schrijver, the seed's quantum k-SAT connection); geometric modelling / CAD (implicitization, intersection); signal processing (Prony, super-resolution, Hankel varieties); quantum information itself (entanglement classes, stabilizer varieties, Segre/Veronese, spinor BEC as in seed §7); serious algebraic geometry (moduli, enumerative geometry, Hodge, syzygies, Castelnuovo-Mumford regularity, Hilbert schemes) — where would a physicist's Hamiltonian view be genuinely new?

For each area: the concrete polynomial problem; sizes that matter in practice; the classical tool actually used; whether the problem has a natural 'gap' or 'ground-state' structure; the honest quantum angle; the heuristic-hardware angle (linear optics/MBQC, boson sampling, Bose-Hubbard/spinor BEC); and a score 1-5 on 'plausibility of a real speedup' with one line of justification.

End with "## Ranked shortlist" (<=8 areas) and "## Questions for TJO" (decisions only a human should make).

Length target 300-600 lines. Cite by arXiv id or DOI where you are confident; else [UNVERIFIED].
