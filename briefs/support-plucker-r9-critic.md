# Independent audit: support-to-Pluecker conversion and its computational value

Read CLAUDE.md, PRD criterion 6/D22--D24 and HANDOFF.md, then
`briefs/support-plucker-r9.md`. Root owns shared files and tracking
(`qaag-9v2`); no additional subagents. Write only
`verdicts/support-plucker-r9.md`. The construction agent writes
`scouting/support-plucker-r9.md`; root is also working on the baseline.

Independently test whether the proposed N=O(r^2/eta) protocol can produce the
pure Slater state of an unknown rank-r support by measuring the symmetric-
group factor, steering its known standard tableau with physical adjacent
swaps plus nondemolition prefix-shape measurements, and retaining a full
column. Exact operator identities and full Hilbert-factor scopes matter.

Two separate substantive audits are required:

- Historical/mechanism audit after deriving the operation. Look for an exact
  efficient reduction to described universal mixed-state purification,
  support extraction, Schur concentration, or measurement-only recoupling.
  Merely naming Schur--Weyl theory, Hamiltonian simulation or a universal
  gate set is not enough. Conversely, an existing full protocol must be
  recognized; a new target encoding or parameter regime does not meet D22.
- Same-output classical baseline. The source is copies of rho, with arbitrary
  adaptive global single-copy POVMs and classical processing allowed. The
  classical output is projection-DPP/Pluecker-coordinate sampling, or a
  precisely specified geometric bit implied by that sampler. An explicit
  support basis or tomography is not the default comparator. Check whether
  a classical sequential measurement protocol already samples the DPP.

Root's candidate r=2 lower-bound pair to investigate (not a claimed theorem):
H=A direct-sum B, each dimension d. In one case U=span(u_A,v_B).
In the other U=span((u1_A+v1_B)/sqrt2,(u2_A+v2_B)/sqrt2).
Frames within A and B are independently hidden Haar frames; rho=P_U/2.
Both block masses are1/2. A projection-DPP pair has one index in each block
with probabilities1 and1/2 respectively. The first single-copy averages
agree. Does a full adaptive single-copy lower bound survive the second
case's off-diagonal coherence? Do not infer it solely from matching averages.
This scalar witness alone also reduces to known two-copy block purity tests;
the full sampler/growing-r conversion and original mechanism need their own
adjudication. Scope every conclusion accordingly.

Every objection needs FIX DEMAND and SURVIVING STATEMENT. Bound experiments
and fail nonzero on actual violations. Do not promote claims or broaden a
successful finite test into a universal theorem. Communicate precise evidence
early, especially an existing algorithm or a cheap classical sampler.
