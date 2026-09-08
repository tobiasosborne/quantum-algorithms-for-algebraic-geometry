# Growing-rank useful syzygy basis extraction, R13

Sol xhigh. Own ONLY `scouting/syzygy-basis-r13.md`; no bd, shared edits,
agents or commits. Current D25 permits QSVT and nonexcluded quantum walks /
adiabatic methods. User deadline is 2026-09-08 01:00 UTC, wind-down 00:45 UTC.
Initial artifact in about 15 minutes, followed by an independent audit.

R12 now has an independently accepted useful source-only hit: any original
generating pair, 8 copies vs Omega(sqrt q), using plain swap interference.
Read definitions/syzygy-plucker-r12.md, scouting/syzygy-plucker-r12.md and
verdicts/syzygy-advantage-r12.md. Develop a nontrivial growing-rank extension.

Root proposal: in R=C[z0,z1], let g_0,...,g_(r-1) be the Fock-orthonormal
degree-(r-1) monomials. Hidden C is an r-by-q row coisometry. The based
generators f_a=sum_i C_ia g_i generate (z0,z1)^(r-1). For r>=3 this is a
nonreduced fat point, length r(r-1)/2. At N=d=r-1 the fixed maximally mixed
Fock emitter is an isometry and delivers rho=C†C/r with success ONE. Ask for
any r ORIGINAL labels whose forms generate the same ideal, success>=2/3.
No C list, preparation inverse, controllable emitter or public hidden partition.

Lower bound candidate: q=rd, hidden uniform balanced partition into r groups
of size d, independent Haar line on each group, source average of those lines.
For each fixed partition, extend C362's homogeneous Gaussian/Haar argument to
r groups to get common transcript mass c_T=(d/(d+T-1))^T independent of the
partition. Any reference r-subset is a transversal with probability
a_(r,d)=r! d^r/(q)_r. Thus success<=c_T a+(1-c_T). Derive exact quantitative
lower and its parameter range; do not confuse T²=Omega(q/r) with T=Omega(q/r).

Quantum upper: existing C361 support-to-Slater theorem is polynomial in r and
log q, but its content measurement uses inverse Fourier transforms. Replace
that subroutine EXPLICITLY by QSVT, which the user accepts. For X_k=sum_(i<k)S_ik,
the known content eigenvalues are integers in [-(k-1),k-1], gap1. A padded uniform
label bank of polynomial window filters near each integer can implement the
Lueders measurement without QFT. Root's ideal bank observation: choosing a
label j uniformly among J eigenwindows and testing P_j succeeds with probability
1/J independent of state; on failure the maps (1-P_j) dephase between windows
but preserve each target eigenspace. Repeating up to O(J log(1/delta)) gives
the desired Lueders instrument except a state-independent failure probability.
Derive the exact channel, then bound the approximated QSVT implementation,
parity/LCU normalization, bank PREPARE/SELECT and total degree/gates. Local
block encodings use controlled permutations, so exact source-support preservation
must survive ancilla approximation and the final exact antisymmetry certificate.
Do not assume an operator-norm-optimal projector dilation for free.

Fallback: direct r-copy antisymmetrization of rho^(tensor r) succeeds with
1/r^r (NOT r!/r^r); an exactly padded signed-permutation certificate adds
gamma_r². This yields a non-Fourier upper for slowly growing r satisfying
r log r=O(log log q), even if the polynomial-r QSVT compiler is not established.
Record that honest fallback instead of silently fixing its rank cost.

Provide complete geometry, source, useful output, exact lower, quantum compiler,
finite errors, gate/copy/hardware ledger, references and MERGE PROPOSAL. The
goal is a rigorously stronger version of useful generator reduction, not merely
an arbitrary sampling distribution. Keep source-only vs coefficient-list and
online vs device-construction costs explicit.
