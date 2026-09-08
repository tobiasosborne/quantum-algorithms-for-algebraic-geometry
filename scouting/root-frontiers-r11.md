# R11 root portfolio: geometric information in open quantum dynamics

2026-09-07. These are constructions and adversarial questions, not promoted claims.
The user requested a broad round on cohomology, schemes, complex surfaces, thermal
states and CP maps. This root portfolio complements `geometry-frontiers-r11.md` and
`thermal-cp-frontiers-r11.md`. Finite Hermitian models below explicitly depart from
the Fock metric C1; dimensions are independent of C2. Existing R10 work remains an
interim audit. All input matrices, metrics, preparation interfaces and precision
are part of the proposed problem, rather than free geometric oracles.

## 1. Candidate register

The R identifiers name research candidates, not canonical claim statuses. A claimed
quantum advantage must concern the identical output under the identical access model.

| ID | Geometric question and finite input | Proposed physical operation and output | Cost/attack that must be resolved | Decisive development |
|---|---|---|---|---|
| R01 | Prepare harmonic representatives of a supplied finite coherent-sheaf complex `(C,d)` with Hermitian metrics and efficiently implemented `d` | Couple to baths with jump operators made from `d,d†`; attempt autonomous attraction to cohomology, then measure a supplied bounded geometric observable | Are harmonic sectors reachable at all? A fast simulation of the channel is not a mixing theorem. Preparing a reset state with harmonic weight is charged | Section 2 derives an invariant-sector obstruction and specifies the necessary escape through additional geometric jumps |
| R02 | Detect nonreduced local structure of a finite algebra `A`, given multiplication in a declared orthonormal basis or a physically supplied multiplication instrument | Fuse two algebra states by multiplication, split by its adjoint, and iterate a thermal collision process; read an acceptance or cycle statistic | Multiplication must be divided by its operator norm. Algebraic Frobenius duality need not equal a Hilbert adjoint. A nonlinear two-copy recursion consumes fresh states | Section 3 derives the dual-number instrument, its complete success law, and failure of the dagger-Frobenius identity |
| R03 | Approximate a balanced metric for a polarized complex surface from a finite weighted sample of evaluation vectors `s_i` and positive matrix `H` | Use measurement-induced normalization to implement a Donaldson-type metric update in density matrices | The Born distribution weights the very denominators the update wants to cancel. Averaging normalized trajectories can erase the desired inverse dependence | Section 4 gives the exact cancellation and required importance-reweighting cost; retain genuinely different instruments as candidates |
| R04 | Recover higher Ext/Massey products from a finite contraction of a dg-algebra with multiplication `mu`, differential `d`, and a supplied low-energy input | Retain coherent bath-time labels while summing `mu(d† exp(-t Delta) mu(...),...)` contributions, rather than estimating a nullity | Time integration realizes a Green operator: gap, branch normalization, tree count, quotient ambiguity and classical tensor-DP all count | Derive an instrument for a complete nonzero higher product, including coherent sign cancellations, then compare its full channel with generic resolvent/LCU processing |
| R05 | Obtain characteristic information of a surface bundle from a smooth finite family of full-rank thermal density matrices on a fixed ambient space | Compose purification transport or recovery maps around a parameter loop; measure a loop character or integrated curvature | Ordinary Uhlmann Chern classes vanish for a globally faithful density family; modified thermal curvature is a different observable and need not be quantized | Identify an exact algebraic invariant retained by support/eigenbundle structure without free low-temperature projection; Section 5 fixes the scope |
| R06 | Read nilpotency order or multiplicity of a local scheme from a finite channel representation of its multiplication maps | Encode a nilpotent in a channel's slow/peripheral sector and amplify its polynomial transient before readout | A CPTP channel cannot have a nontrivial Jordan block at a unit-modulus eigenvalue. Interior Jordan blocks are allowed, but signal and physical-time costs remain | Section 6 proves the peripheral obstruction, then asks for a transient-family advantage under identical matrix/circuit access |
| R07 | Compare cohomological data across a Fourier–Mukai correspondence supplied by a finite graded kernel/resolution | Physically glue and trace kernel registers, retaining degree/parity to measure a correspondence pairing | A derived equivalence is not automatically an isometry of the selected Hermitian complexes. A partial trace is CP but usually loses the desired signed amplitude | Construct one finite, metric-explicit surface kernel, complete its instrument and compare the same scalar with direct contraction; no free categorical equivalence |
| R08 | Estimate analytic-torsion-type or determinant-line variation of a finite Hermitian family of sheaf complexes, with a promised output margin | Interfere two reservoirs with different degree weights, subtract matched heat traces at the channel level, integrate only the surviving signal | Small eigenvalues, ultraviolet/finite truncation and the norm of the signed integral must be paid; standard normalized trace estimation is a novelty comparator | Prove an endpoint cancellation that changes the resource scaling of the actual instrument, rather than merely relabeling a log-determinant estimator |

R04 is connected to the geometry proposer's Kuranishi construction but asks a different
implementation question: can a real retained reservoir sum the required homotopies
with a better normalization? R07 and R08 remain undeveloped proposals; neither has a
resource theorem. The explicit calculations below are attempts to establish a reliable
starting point, not universal impossibility results for their geometric domains.

## 2. Autonomous harmonic pumping: an exact reachability test

### 2.1 Finite model and invariant sector

1. ASSUME a finite-dimensional graded Hermitian space `C`, a degree-one map `d`
   with `d²=0`, and `Delta=d d†+d† d`. Let `P` be the orthogonal projector onto
   `ker Delta = ker d intersection ker d†`.
2. PROVE `dP=d†P=Pd=Pd†=0`. For example, `range(d)` is orthogonal to
   `ker d†`, and every vector in `range(P)` lies in that kernel.
3. Consequently `P` commutes with every element of the unital star algebra
   generated by `d,d†`. In fact every nonconstant word annihilates `P` on both sides.
4. Consider any Lindblad generator with Hermitian Hamiltonian `H` and jumps `L_a`
   in this algebra. The Heisenberg generator satisfies

       L*(P)= i[H,P] + sum_a(L_a† P L_a - {L_a† L_a,P}/2) = 0.

   Thus `Tr(P rho_t)=Tr(P rho_0)` for all nonnegative times. Thermalization inside
   this algebra cannot increase the population of harmonic representatives.
5. The same conclusion holds for any CPTP map whose Kraus operators are in that
   algebra: commutation and `sum K_a†K_a=1` give `E*(P)=P`.
   This includes arbitrary compositions and mixtures of such channels.

### 2.2 Exact toy complex

Take basis `(h,a,b)` and `d=|b><a|`. Then `P=|h><h|` and
`Delta=|a><a|+|b><b|`. Jumps `d,d†` equilibrate the `a,b` pair but never
move any of its population into `h`. Starting from the maximally mixed state
leaves harmonic weight exactly `1/3`, however long the process runs.

Conditioning on no jump can filter the `a,b` sector, but its unconditional
success tends to the starting harmonic weight. This is a different physical
instrument from trace-preserving autonomous cooling.

### 2.3 Constructive escape that remains worth investigating

An additional local geometric jump `J` with `P J (1-P) != 0` can change the
conclusion. A rank-one reset into a known harmonic vector trivially does so,
but assumes the solution. The useful problem is to obtain such jumps directly
from sheaf restrictions, local exactness witnesses, or geometric correspondences,
prove the dark space remains the intended cohomology, and prove mixing from an
easily supplied state. Dissipative error correction is a substantive prior-mechanism
comparator. The calculation does not rule out those additional jumps.

## 3. A physical fusion test for a nonreduced scheme

### 3.1 Exact dual-number multiplication

Use the algebra `A=C[e]/(e²)` in the explicitly declared orthonormal basis `(1,e)`.
Its multiplication matrix from `A tensor A` to `A` is

    mu = [[1,0,0,0], [0,1,1,0]].

Thus `mu mu†=diag(1,2)` and `||mu||=sqrt(2)`. The successful Kraus map is
`K=mu/sqrt(2)`. Complete it by `F=sqrt(1-K†K)` into a separate failure-output
space. The resulting flagged map is trace-preserving; discarding the failure
flag and pretending `mu` was deterministic is not valid.

For a normalized pure input `psi=a|1>+b|e>`, two independent copies have

    K(psi tensor psi)=(a²|1>+2ab|e>)/sqrt(2),
    p(psi)=(|a|^4+4|a|²|b|²)/2.

Writing `x=|a|²` gives `p=2x-(3/2)x² <= 2/3`, with equality at `x=2/3`.
The normalized output is nonlinear in `psi`; it requires two actual input
copies plus the flagged measurement. A recursive factory must account for
how each new pair is produced, including correlations if recycling is attempted.

### 3.2 Frobenius duality is not the physical adjoint

The algebraic trace `epsilon(1)=0, epsilon(e)=1` gives nondegenerate Frobenius
pairing `epsilon(xy)` with matrix `[[0,1],[1,0]]`. This bilinear form is not
the positive Hermitian inner product defining the quantum register.

There is also a direct failure of the dagger-Frobenius identity. On `e tensor e`,

    mu† mu(e tensor e)=0,
    (mu tensor 1)(1 tensor mu†)(e tensor e)=e tensor e.

No change of positive inner product can make this commutative nonreduced algebra
a finite-dimensional commutative dagger-Frobenius algebra: the classification
identifies those with orthogonal classical basis structures, hence with products
of copies of `C`, which have zero nilradical. This classification is a cited
theorem, not an original campaign result. A noncommutative matrix C*-algebra DOES
contain nilpotent matrices, so this is not a claim that all quantum operator
algebras lose nilpotent information.

Targeted primary source, fetched after the construction: Jamie Vicary,
[Categorical formulation of quantum algebras, arXiv:0805.0432](https://arxiv.org/abs/0805.0432).
The explicit matrix and counterexample above are independent finite calculations.

### 3.3 What could still work

Use the real instrument `(K,F)` and retain its entire environment, rather than
imposing the false Frobenius identity. A useful new algorithm would need a growing
family in which that retained environment permits a provable advantage for a
specified scalar or sampling task. Merely distinguishing `e²=0` from `e²=1` in
an explicit two-dimensional coefficient table is classically constant cost.

## 4. Born normalization does not automatically compute a balanced metric

### 4.1 A finite proposed surface-metric update

For nonzero vectors `s_i in C^q`, positive weights `w_i` and a positive-definite
Hermitian matrix `H`, define the finite matrix

    T(H)=sum_i w_i s_i s_i†/(s_i† H s_i).

This is a finite model inspired by balanced-metric quadrature; the convention
for `H` versus its inverse must be fixed before comparing an actual Donaldson
iteration. No assertion that every such table comes from a surface is made.
For a polarized surface, evaluation vectors of sections provide the intended
source, and their construction, quadrature error and section-space dimension count.

### 4.2 Cancellation in the proposed measurement implementation

Let `C=sum_i w_i s_i s_i†`, choose `c>=||C||`, and use Kraus operators

    M_i=sqrt(w_i/c) |i><s_i|,
    M_fail=sqrt(1-C/c).

On `rho=H/Tr(H)`, the probability of outcome `i` is
`p_i=w_i(s_i†H s_i)/(c Tr(H))`. Define the normalized vector
`v_i=H^(1/2)s_i/sqrt(s_i†H s_i)`. Even granting a circuit to prepare `v_i`
from the label, the unconditional contribution of the sampled outcomes is

    sum_i p_i |v_i><v_i| = H^(1/2) C H^(1/2)/(c Tr(H)).

The inverse denominators have canceled. This is not
`H^(1/2)T(H)H^(1/2)`, whose summands would have weights `w_i`.
To obtain label probabilities proportional to `w_i` using this measurement,
accept outcome `i` with probability `a/(s_i†H s_i)`, where
`0<a<=min_i s_i†H s_i`. The total acceptance is
`a sum_i w_i/(c Tr(H))`. The small evaluation norm is therefore a real
resource cost of this displayed rejection-sampling construction.

This identity excludes that implementation, not all quantum methods for balanced
metrics. Known quantum matrix-scaling algorithms are a baseline, not automatically
a reduction of every operator-valued or surface-specific update.

Targeted primaries: S. K. Donaldson,
[Some numerical results in complex differential geometry, math/0512625](https://arxiv.org/abs/math/0512625),
which includes a K3 surface example; and
[Quantum algorithms for matrix scaling and matrix balancing, arXiv:2011.12823](https://arxiv.org/abs/2011.12823).
Neither citation establishes an algorithm for the full proposed geometric task.

## 5. Full-rank thermal transport and the geometric invariant

For a globally defined positive-definite density matrix `rho(x)` on a fixed
finite-dimensional ambient space, `sqrt(rho(x))` is a globally defined smooth
purification amplitude. It is a global section of the amplitude bundle. Thus
ordinary characteristic classes of that Uhlmann bundle vanish. Nontrivial loop
holonomy is still possible: triviality of the bundle is not flatness of a connection.

The scope matters. A selected spectral subbundle can be nontrivial, and a family
defined on a preexisting nontrivial bundle does not supply a fixed global ambient
frame by assumption. A temperature-weighted curvature functional is also possible,
but needs its own precisely stated output and is not automatically an integer
surface invariant. Support selection, purification and transport costs remain.

Targeted primary comparison:
[Thermal Uhlmann Chern number from the Uhlmann connection, arXiv:1805.04753](https://arxiv.org/abs/1805.04753).
The proposed R05 algorithm must identify a surviving algebraic output before a
complexity comparison can be meaningful.

## 6. Nilpotent amplification at a channel's spectral edge

A finite-dimensional CPTP map `E` is power bounded. On Hermitian matrices its
trace norm is contractive. Decomposing an arbitrary matrix into Hermitian real
and imaginary parts gives a dimension-independent finite bound on `||E^n||_(1->1)`
(the constant 2 suffices), uniformly in `n`.

Suppose an eigenvalue `lambda` with `|lambda|=1` had a Jordan chain of length
at least two. In a suitable pair, `E v=lambda v` and `E w=lambda w+v`, hence
`E^n w=lambda^n w+n lambda^(n-1)v`. Its norm grows at least linearly minus a
constant, contradicting power boundedness. Longer chains are excluded as well.

Interior eigenvalues can have Jordan blocks. This argument places no universal
bound on useful transient behavior there and says nothing about the difficulty
of simulating arbitrary succinct channels. A candidate using an interior block
must give its exact CPTP completion, noise tolerance, initial state, measurement
margin, physical time and matched classical access.

## 7. Tournament obligations and merge proposal

The strongest constructive follow-ups here are the additional geometric jumps
of R01, retained-environment fusion in R02, and a complete coherent-time
implementation of R04. R03's displayed Born-normalization implementation fails;
R05's ordinary full-rank Chern target fails; R06's peripheral-Jordan target fails.
Their broader geometric questions remain available for materially different operations.

Proposed exact statements for independent audit, before canonical integration:

1. Harmonic population is conserved by the specified star-algebra-generated
   channels and Lindblad generators, with the hypotheses of Section 2.
2. The dual-number multiplication instrument has `||mu||=sqrt(2)` and identical
   pure-input success at most `2/3`; the displayed dagger-Frobenius identity fails.
3. The displayed metric-sampling instrument yields the cancellation in Section 4,
   with the stated acceptance probability for its particular reweighting repair.
4. A finite CPTP map has no nontrivial Jordan blocks at unit-modulus eigenvalues.

These are scoped mathematical controls. Even if their audits converge they do not
establish an original algorithm or exclude advantages from different constructions.
