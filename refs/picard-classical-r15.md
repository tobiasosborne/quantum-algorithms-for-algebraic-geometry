# Primary sources checked for the classical Picard review

Fetched/read 2026-09-08. Identifiers below resolve to primary papers or their
authors' software. Published runtimes are not new experiments in this repository.

| Key | Source | Role |
|---|---|---|
| NS | Poonen, Testa, van Luijk, [Computing Néron–Severi groups and cycle class groups](https://arxiv.org/abs/1210.3720), DOI 10.1112/S0010437X14007878; [author's final PDF](https://math.mit.edu/~poonen/papers/compute_ns.pdf) | Theorem8.38 is unconditional for K3 surfaces over finitely generated fields of characteristic not2; general abstract hypotheses must not obscure that specialization |
| Charles | Charles, [On the Picard number of K3 surfaces over number fields](https://arxiv.org/abs/1111.4117); [author's PDF](https://www.imo.universite-paris-saclay.fr/~francois.charles/Picard.pdf) | Reduction ranks, real-multiplication jumps, two-prime discriminants; Theorem5 has a conditional termination clause |
| Periods | Lairez, Sertöz, [A numerical transcendental method in algebraic geometry](https://arxiv.org/abs/1811.10634), DOI 10.1137/18M122861X | Period continuation, lattice reduction and reliability of numerical Picard recovery |
| Separation | Lairez, Sertöz, [Separation of periods of quartic surfaces](https://arxiv.org/abs/2011.12316), DOI 10.2140/ant.2023.17.1753 | Exact period separation, computable surface-dependent constant, and the distinction between testing one class and finding the whole lattice |
| Crystalline | Costa, Sertöz, [Effective obstruction to lifting Tate classes from positive characteristic](https://arxiv.org/abs/2003.11037) | Certified single-prime upper bounds, Galois decomposition and the large quartic-database experiment |
| Homology | Lairez, Pichon-Pharabod, Vanhove, [Effective homology and periods of complex projective hypersurfaces](https://arxiv.org/abs/2306.05263), DOI 10.1090/mcom/3947 | Modern Picard–Lefschetz period/homology algorithm and published laptop performance |
| ILP | Lenstra, [Integer Programming with a Fixed Number of Variables](https://doi.org/10.1287/moor.8.4.538); [author's PDF](https://pub.math.leidenuniv.nl/~lenstrahw/PUBLICATIONS/1983i/art.pdf) | Fixed-dimensional polynomial integer feasibility used in the new bounded-period reduction |
| MM | Mayr, Meyer, [The complexity of the word problems for commutative semigroups and polynomial ideals](https://doi.org/10.1016/0001-8708(82)90048-2) | Unrestricted ideal-membership space hardness |
| Mayr | Mayr, [Membership in polynomial ideals over Q is exponential space complete](https://doi.org/10.1007/BFb0029002), STACS1989 | Matching EXPSPACE upper bound; distinguish conference year from later online publication date |
| BQP | Watrous, [Quantum Computational Complexity](https://arxiv.org/abs/0804.3401), sectionIII | BQP containment in PP and standard classical simulation consequences; no reliance on its historical discussion of later-settled QIP questions |

Software documentation checked:

- [PeriodSuite](https://github.com/emresertoz/PeriodSuite): SageMath/Magma,
  period continuation and an explicitly uncertified numerical Hodge-lattice output.
- [crystalline_obstruction](https://github.com/edgarcosta/crystalline_obstruction):
  rigorous upper bounds from finite-precision crystalline obstruction calculations.
- [lefschetz-family](https://github.com/ericpipha/lefschetz-family): the authors'
  Picard–Lefschetz period/homology implementation.

Identifier check: arXiv:2401.05131 is a separate paper on elliptic surfaces,
not the hypersurface paper arXiv:2306.05263. They were not treated as one source.

The Boolean encoding also uses Karp,
[Reducibility among Combinatorial Problems](https://link.springer.com/chapter/10.1007/978-1-4684-2001-2_9),
DOI 10.1007/978-1-4684-2001-2_9 (1972), for NP-completeness of Boolean integer
feasibility/knapsack. The publisher record and primary-paper copies were
resolved. The Picard-scheme reduction is the campaign's separate derived control,
not a theorem attributed to Karp.
