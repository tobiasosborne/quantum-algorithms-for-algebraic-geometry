# Lane: definitions register

Work fully autonomously; do not ask questions. Repo root: /home/tobias/Projects/quantum-algorithms-for-algebraic-geometry. Read first, in order: CLAUDE.md (laws, north star), seed/analysis-2026-09-01/report.md (the seed analysis; treat as an untrusted proposer document, NOT as established truth), seed/analysis-2026-09-01/referee/round1.md and round2.md (prior critic verdicts), HANDOFF.md, seed/page81.tex (the original notebook page). No emoji, no marketing prose. Mark any citation you cannot resolve to an arXiv id or DOI you are confident of as [UNVERIFIED]. Do not touch seed/ or any file outside your lane.

## Your lane (writable files, nothing else)
- definitions/definitions.md
- definitions/notation.md

## Task
Build the single-source definitions register for the campaign (rk-light law L2). Every symbol and every object used anywhere in the seed report and in the notebook page gets exactly one entry.

Format for definitions.md: one entry per definition, heading "### D-<kebab-slug>", then the exact mathematical definition (LaTeX, $...$ and $$...$$), then a line "Source: seed report §x / page81 / standard (cite)" and a line "Pitfalls:" listing known traps. Mandatory entries at minimum: the Fock/Bargmann space and basis |k> = z^k/sqrt(k!); the projective-space L^2 basis on page81 and its relation to Fock (they differ: state exactly how, degreewise); creation/annihilation operators a(f) as conjugate-coefficient differential operators; the Hamiltonian H = sum_j f_j(a^dagger) conj(f_j)(a); the degree-N sector H_N; Macaulay inverse system and (I_N)^perp; Hilbert function; Bombieri-Weyl / sphere norms and their relation to Fock norm (degreewise agreement only); the Macaulay gap Delta_N and its dependence on the generating tuple (not just the ideal) — state the normalization convention (unit Bombieri-Weyl generators); coherent states |p>^{tensor N}; frustration-free; parent Hamiltonian; k-body / few-mode; multidegree sectors and quantum k-SAT; the w-Groebner deformation path; Takagi factorization of a quadric; the distance-to-ideal problem as stated in seed §8.1; boson sampling / linear-optics / Bose-Hubbard objects only if the seed uses them (otherwise leave a stub section "reserved" listing what will be needed).

notation.md: a table of every symbol (symbol | meaning | defined at D-id | first used). Also a "Conflicts" section listing every place where the notebook page and the seed report use different conventions for the same object, with the campaign's chosen convention.

Where the seed report is internally inconsistent or you find a definition that does not make sense, do not silently repair: add a "### OPEN" section at the end of definitions.md listing each issue with file and line.

## Output
The two files. End definitions.md with a section "## Lane report" (<=15 lines): what you included, what you could not pin down, and any MERGE PROPOSAL text for CLAUDE.md or PRD.md.
