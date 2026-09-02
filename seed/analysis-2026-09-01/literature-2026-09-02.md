# Literature scouting, 2026-09-02 (three Opus agents; verify citations before use)

## Verdict
No publication encodes a homogeneous ideal as ker Σ_j f_j(a†) f̄_j(a) on Fock space, identifies the zero-mode degeneracy with the Hilbert function, or uses the Fischer/Bombieri inner product in quantum information. No quantum algorithm exists for Hilbert functions/series/polynomials, syzygies, graded Betti numbers, or ideal membership over C; no DQC1 result for any of these. No Gröbner formulation of quantum SAT.

## Closest prior art
- Law–Pu–Bigelow, PRL 81, 5257 (1998): spin-1 spinor BEC spin-mixing Hamiltonian a₊†a₋†a₀² + h.c. + n₊n₋ + n₀(n₀−1) is the conic ideal (z0z1−z2²); ferromagnetic case has 2N+1 degenerate ground states (= Hilbert function of the conic). Already realised experimentally.
- Aralov et al., arXiv:2507.19397 (photon catalysis): multimode core states as homogeneous polynomials, Waring rank/catalecticants for state preparation. Apolarity in Fock space, but no ideal/kernel.
- Chabaud–Joseph–Mehraban–Motamedi, arXiv:2410.04274 (Bosonic quantum computational complexity): complexity of bosonic Hamiltonians keyed to stellar rank; NP-complete at constant stellar rank, QMA at poly rank, undecidable at unbounded rank (via Nullstellensatz over Z). No ideals/frustration-freeness.
- Chabaud–Markham–Grosshans PRL 124, 063605 (2020); Chabaud–Mehraban Quantum 6, 831 (2022): stellar (Bargmann) representation; multimode zeros treated via factorization, not ideals.
- Sanz–Braak–Solano–Egusquiza, J. Phys. A 50, 195303 (2017): catalecticants + Veronese secants for symmetric-state entanglement classes (the apolarity pairing, used for rank).
- Aldi–Gharibian–Rudolph, arXiv:2412.19623: TFNP class MHS from Bézout's theorem; QSAT-with-SDR is MHS-complete. Laumann et al. PRA 81, 062345 (2010): product-state QSAT via dimension counting.
- Childs–Gosset–Webb, ToC 11, 491 (2015): frustration-free Bose–Hubbard is QMA1-hard. Anschuetz–Bauer–Kiani–Lloyd, Quantum 7, 1189 (2023): permutation-invariant Hamiltonians at FIXED local dimension are classically easy (poly in N) — so speedups need growing mode number n.
- FQH zero-mode / pseudopotential literature (Lee–Papić–Thomale PRX 5, 041003 (2015)): kernels of PSD bosonic Hamiltonians as polynomial spaces defined by vanishing conditions (not graded ideals).
- Chen–Gao, J. Syst. Sci. Complex. 35, 373 (2022) + Ding–Gheorghiu–Gilyén–Hallgren–Li, Quantum 7, 1069 (2023): HHL on Macaulay matrices and its condition-number obstruction.
- Kedlaya, Comput. Complexity 15, 1 (2006): quantum zeta functions of curves (HSP); Kikuchi & Kikuchi (2021, arXiv:2401.00019): informal quantum Gröbner proposals; Dridi–Alghassi–Tayur annealing/Gröbner line.

## Photonic / bosonic implementation
- Measurement-induced nonlinearity toolbox: Scheel–Nemoto–Munro–Knight PRA 68, 032310 (2003). Costs: Knill PRA 68, 064303 (2003) (NS gate ≤ 1/4); Scheel–Audenaert NJP 7, 149 (2005) (generalised NS ~ 1/N²); Eisert PRL 95, 040502 (2005).
- Fock filters "≤ k photons in a mode": Pegg–Phillips–Barnett PRL 81, 1604 (1998); Sanaka–Resch–Zeilinger PRL 96, 083601 (2006); Winnel–Hosseinidehaj–Ralph PRA 102, 063715 (2020) (success prob exponential in truncation order). These realise power-ideal terms (ℓ_j^m) after a passive rotation.
- Symmetric-subspace / multivariate trace overlaps with linear optics: Novo et al. arXiv:2601.14204; Navas-Merlo–García Escartín arXiv:2607.11393.
- GBS ↔ graph polynomials: Brádler et al. PRA 98, 032310 (2018) (hafnians/perfect matchings), Brádler et al. Spec. Matrices 9 (2021) (GBS polynomial ~ matching polynomial). Nothing on independence polynomials = Hilbert series of edge ideals.

## Classical complexity map (scout 3)
- HF at one degree: rank of Macaulay matrix, poly in binom(N+n,n); #P-hard already for degree-2 squarefree monomial ideals (Dickenstein–Tobis 2012 + Stanley–Reisner). Hilbert series #P-hard to evaluate. Hilbert polynomial PSPACE-hard in general; smooth equidimensional case reduces to counting (Bürgisser–Lotz FoCM 7, 2007). dim V: NP-hard, single exponential (Chistov, Giusti–Heintz), AM under GRH (Koiran). Degree of a zero-dim set: FP_C^{#P_C}-complete (Bürgisser–Cucker).
- Membership: EXPSPACE-complete (Mayr–Meyer, Mayr); single exponential for unmixed/0-dim/CI (Dickenstein–Fitchas–Giusti–Sessa 1991).
- Toric: Barvinok P in fixed dim, #P-hard in general; Gröbner/Graver strongly NP-hard, FPT in treedepth (Cifuentes–Onn 2019). Determinantal, CI, Borel-type: closed forms, P.
- Generic forms: Fröberg (proved d ≤ n+2, n ≤ 3, degree ≤ 2d−1 for large n per arXiv:2605.03872); power ideals Fröberg–Iarrobino; Emsalem–Iarrobino duality (ℓ_1^m..ℓ_d^m)^⊥_N = (fat points of multiplicity N−m+1)_N; Alexander–Hirschowitz.
- Conditioning: BBEM 1990 (product inequality), Pinasco Trans. AMS 364 (2012) (several factors); NO several-generator lower bound for Σ f_j h_j and no uniform-in-N σ_min result known. Cucker–Ergür–Tonelli-Cueto Forum Math. Sigma 10 (2022): Weyl norm badly scaled vs sup norm. Note: the BBEM factor binom(N,m)^{-1/2} is polynomial in N for bounded m (= Fact 7.1 in Fock normalisation).
