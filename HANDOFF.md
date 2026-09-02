# Handoff — complex projective varieties as ground spaces (2026-09-02)

## State
- Source: `page81.tex` (transcribed notebook page, preliminary quantum-algorithm ideas).
- Deliverable: `analysis-2026-09-01/report.md` + `report.html` (render with `fmd-report report.md -o report.html`; last render 847 equations, 0 fallbacks).
- Support: `analysis-2026-09-01/numerics/` (bf.py core; task1–9 scripts + `*_out.txt`; `run_all.sh`), `referee/round1.md`, `round2.md` (codex gpt-5.6-sol xhigh critiques), `literature-2026-09-02.md` (three Opus lit scouts, citations unverified unless marked).

## Established (theorem-level, in report Sections 2–4, 7)
- H = Σ_j f_j(a†) f̄_j(a) on Fock space; ker H_N = (I_N)^⊥ = Macaulay inverse system; dim = Hilbert function. Frustration-free. Coherent states |p>^{⊗N} in kernel ⟺ p̄ ∈ V. Multidegree-(1,…,1) sector = quantum k-SAT exactly.
- No k-body parent Hamiltonian for I_N (Fact 4.1); few-mode parents only for ideals confined to few modes (Fact 4.2).
- Principal ideals uniformly gapped (Bombieri inequality, Fact 7.1); quadric gap ≥ 4 d_min²(N−2)+‖f‖² via Takagi (Fact 7.2), exact for the conic (Δ_N = N+1).
- Bosonic QSAT (symmetric sector) is QMA1-hard via hard-core terms (Prop 8.2).
- Conic Hamiltonian = Law–Pu–Bigelow spinor-BEC spin mixing; 2N+1 ground states already realised experimentally.

## Open / conjectures (report Section 8)
8.1 gapped distance-to-ideal BQP-hard; 8.3(a) inf_N Δ_N > 0 for fixed tuple; 8.3(b) cone criterion for gap growth; 8.3(c) generic forms gapped uniformly in n; 8.4 adiabatic Gröbner deformation; 8.6 root sampling Grover-limited; 8.7 low-codim degree/dim from normalised HF; 8.10 geometric overlaps / Toeplitz integration; 8.11 Macaulay gap vs Bürgisser–Cucker condition number.

## Suggested next small steps
1. Check Fact 7.2 numerically on the survey's random quadric in P^4: compute Takagi values, compare slope of Δ_N with 4 d_min². (bf.py has everything; ~20 lines.)
2. Test the cone criterion (8.3(b)) for a non-quadric hypersurface: cubic with/without linearly dependent partials, Δ_N vs N.
3. Test 8.10(a): Tr(P_I P_J) scaling for two curves meeting in a point vs disjoint, N ≤ 12.
4. If writing up: Sections 2, 3, 7 and Props 3.1/8.2 are the solid core; keep 8.x labelled as conjectures.

## Conventions / pitfalls
- Fock basis |k> = z^k/√k!, a(f) = conj-coefficient differential operator. Sphere/Bombieri norms agree with Fock only degreewise.
- Gröbner path (5.5) needs a w-Gröbner basis as generators, else not flat at t=0.
- Δ_N depends on the generating tuple (not just I); use unit Bombieri–Weyl generators when comparing.
- Tooling: no Fable subagents; Opus subagents or `codex exec -m gpt-5.6-sol -c model_reasoning_effort="xhigh" -s read-only --skip-git-repo-check -o out.md "<prompt>" < /dev/null` (stdin must be closed).
