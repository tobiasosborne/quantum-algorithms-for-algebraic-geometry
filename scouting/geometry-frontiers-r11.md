# Geometry frontiers R11: cohomology, schemes, and surfaces

2026-09-07.  This is a construction portfolio, not a claim-status file.  The
candidate assertions below have not been independently adjudicated.  Ordinary
finite-dimensional Hermitian metrics are part of each input; they are not claimed
to be intrinsic algebraic metrics.  This locally departs from C1.  The symbols
`D`, `r`, and `alpha` below denote local dimensions, lattice ranks, and contraction
normalisations, respectively, rather than the reserved campaign symbols of C7--C8.
No DQI extension is used.  Generic phase estimation, QSVT/QLSA, Grover search,
Schur measurement, and a relabelled old algorithm are treated as novelty failures.

## 1. Common access and accounting

An explicit complex has total coordinate dimension `D`, at most `s` nonzeros per
row, and `b`-bit entries.  A succinct complex instead supplies reversible circuits
for row locations/values or, more strongly, compiled block maps; the latter may
already hide elimination.  `epsilon` is additive output error, `delta` failure
probability, `gamma` a promised nonzero probability or normalised gap, `m` an
obstruction/copy order, `B` a charge or coefficient cutoff, and `L` the number of
local maps or wall factors.  A circuit-supplied `2^q`-dimensional map is never
compared only with a classical printed array: the comparator may exploit the same
sparsity, tensor network, recurrence, random probe, or oracle.

For a linear map `A`, a physical exact conditional application means a successful
Kraus block `A/alpha`, `alpha >= ||A||`.  Its success on unit `x` is
`||Ax||^2/alpha^2`; without amplitude amplification, `O(alpha^2 ||Ax||^-2
log(1/delta))` fresh attempts are charged.  Classical scalar readout, state
preparation, degree/charge truncation, metric construction, and tomography are
separate costs.  An attractive geometric interpretation does not remove them.

## 2. Candidate portfolio

Each row states a candidate rather than an established speedup.  The last column is
the first experiment that could kill or advance it; a finite test would support only
its displayed finite range.

| ID and problem | Finite input, exact output, promise | Physical map and resource ledger | Matched classical/equivalence attack; originality target; decisive test |
|---|---|---|---|
| **G01, coherent Cech cohomology.** Estimate `dim H^p(X,F)/D_p` for a projective scheme with an acyclic affine cover. | Truncated Cech spaces and sparse restriction maps `d_(p-1),d_p`, row oracles, degree cutoff `N`; output the normalised harmonic dimension to `epsilon`; promise normalised Laplacian gap `gamma`. | Supersymmetric walk/block encoding of `Delta_p=d_(p-1)d_(p-1)^dag+d_p^dag d_p`; `poly(s,1/gamma,1/epsilon,log D,b)` calls only under state-preparation and gap promises. | Sparse stochastic spectral counting and the known quantum-cohomology/Laplacian framework are exact attacks. Originality target was cover-local interference, but the operation is generic Laplacian estimation. Test a toric cover at `D<=10^4` against sparse Lanczos, including cover assembly. **Rejected for D22.** |
| **G02, discretised Dolbeault nullity sampling.** Sample `(p,q)` proportional to the nullities of the supplied finite matrices. Identification with algebraic Hodge numbers requires a separate certified discretisation theorem. | A finite element/spectral discretisation of `dbar` on a smooth complex surface, metric mesh size `D`, preparation of a maximally mixed form, promises discretisation error `eta` and gap `gamma`; output a bidegree. | Couple fermionic bidegree registers to the Dolbeault Laplacian and measure the filtered zero sector; preparation weight is `h^(p,q)/D_(p,q)` and cannot be omitted. | Classical sparse eigensolvers, heat-kernel trace estimation, and generic quantum TDA/Hodge algorithms match the mechanism. On hypersurfaces the Hodge numbers may have closed Jacobian-ring formulas. Test a quartic K3 mesh under refinement and measure gap and zero-mode fraction. **Rejected for mechanism novelty.** |
| **G03, cup-product correlator.** Given cocycle states `a_i`, estimate `|int_X a_1 cup ... cup a_k|^2`. | A finite cellular/DGA model over `Z/M`, `k` prepared cocycles, local cup tensor and fundamental-cycle oracle; exact common output is the acceptance probability to additive `epsilon`; no promise except a resolvable signal `>=gamma`. | Reversible local cup accumulation plus phase kickback, or a `k`-copy diagonal phase and interference; `O(k C_cup epsilon^-2 log(1/delta))` gates/copies by direct sampling. | Classical sparse cup evaluation uses the same local cells. More decisively, copy-cup logical gates already implement cohomology invariants in constant depth. Originality target was a sheaf/Dolbeault cup sampler, but changing the cochain model is an application. Test a triangulated surface with torsion and compare gate truth tables. **Rejected for D22.** |
| **G04, Yoneda/Massey indeterminacy test.** Decide whether a represented triple Massey/Yoneda product has positive distance from its indeterminacy subspace. | Finite dg algebra `(C,d,mu)`, cocycles `a,b,c`, supplied null-homotopies `u,v`, sparse projector/block map for the quotient, and promise distance `0` or `>=gamma`; output one bit. | Form `z=mu(a,v)+/-mu(u,c)`, then conditionally project its cohomology class orthogonally away from `a H+H c`; success `||Pz||^2/alpha^2`. | Sparse multiplication plus two linear solves forms the same representative; constructing `P` already solves the quotient problem. Cup/Yoneda circuits and the R7 retained-order obstruction are close precedents. Originality target is a quotient-aware changing representative, not a framed matrix product. Test a small nonformal Stanley--Reisner DGA while charging both solves. **Held only as a definition problem.** |
| **G05, derived-intersection Tor sampler.** Sample homological degree from `Tor_*^R(R/I,R/J)`. | Sparse generators through degree `N`, a truncated free/Koszul resolution or an oracle that applies its differential, total dimension `D`; output `i` with probability `dim Tor_i/sum_j dim Tor_j`; gap `gamma` and nonnegligible total harmonic fraction promised. | Fermionic resolution differential `Q` and Laplacian `{Q,Q^dag}`, followed by zero-sector and degree measurement. | This is the Koszul/quantum-TDA mechanism already audited in this campaign; explicit Schreyer/sparse resolution and stochastic nullity estimation are the baseline. Degree truncation and exponentially small harmonic weight remain. Test two plane subschemes with a nontransverse intersection against exact Tor. **Rejected as generic Laplacian estimation.** |
| **G06, Lefschetz first-loss spectroscopy.** Sample the monomial first-loss distribution encoding a Jordan-string profile; exact integer profile recovery has additional precision and sampling costs. | A `D`-dimensional quotient algebra, uniform standard-monomial preparation, and a coherent successor/death oracle for multiplication by a monomial `ell`; output the death-time law to TV `epsilon`, promise maximum string length `nu`. | A Stinespring step advances a surviving monomial or emits it into a timestamp port. One run uses at most `nu` oracle calls; `Theta((nu+log(1/delta))/epsilon^2)` samples learn a general `nu`-bin law to TV error. | A classical sample of the same standard monomial followed by the same successor calls has exactly the same law. For a general multiplication contraction, first-loss reads metric-dependent Frobenius norms, not Jordan ranks; a Jordan-adapted oracle hides the invariant. The proposed original mechanism is loss-time tomography of scheme thickness. Test random monomial ideals and a nonnormal similarity mutation. **Finalist F1, with a sharp obstruction.** |
| **G07, Hilbert--Samuel nested-layer sampler.** Estimate `dim m^k/m^(k+1)` for a local zero-dimensional scheme without a spectral gap. | Circuits for nested subspace projectors `P_k` onto `m^k`, maximally mixed input on `A`, and cutoff `nu`; output the layer index with probability `(rank P_k-rank P_(k+1))/D`. | Sequential nondemolition test of nested `P_k`; exact telescope `Pr(layer=k)=Tr(P_k-P_(k+1))/D`, `O(nu)` projector calls/sample. | Supplying the projectors is essentially supplying row spaces/ranks of powers of the maximal ideal. Classical random trace probes match additive normalised estimation, and explicit elimination computes the layers. Originality target is simultaneous filtration readout. Test whether projector circuits can be built from a border basis without rank computation. **Rejected on circular access.** |
| **G08, Kuranishi-tree obstruction interference.** Decide the first nonzero intrinsic deformation obstruction and prepare its direction. | A finite dg Lie model with contraction `(i,p,h)`, bilinear bracket oracle, unit `a in H^1`, order `m`; lower coefficients vanish and `||kappa_m(a)||>=gamma` or all through `m` vanish. Output the bit and, on one, the normalised `H^2` ket. | Coherently sum the planar binary trees in homotopy transfer. The exact Kraus map on `m` copies is `A_m/Lambda_m`; a safe `Lambda_m` contains a Catalan factor. Success is `||kappa_m||^2/Lambda_m^2`; tree labels and all contraction flags are charged. | Classical Kuranishi recurrence reuses `x_1,...,x_m` in `O(m^2)` bracket applications, defeating literal tree enumeration. Direct exact transduction is also an `m`-copy homogeneous map. Originality target is interference of genuinely intrinsic changing-quotient obstructions, unlike a framed pencil coefficient. Test random sparse contraction data against dynamic programming and measure `Lambda_m/||kappa_m||`. **Finalist F2; conditional succinct-access survivor only.** |
| **G09, K3 Noether--Lefschetz sieve.** Detect a primitive integral `(1,1)` class of bounded positive coordinate height in a fixed marking from a period state. | Marked K3 lattice, period-preparation circuit `|omega>`, bound `B`, and promise either `|<v,omega>|=0` for a nonzero primitive marked `v` with positive height `max_j |v_j|<=B` or all overlaps `>=gamma`; output a bit. | Coherently enumerate lattice vectors and interfere/test their pairing with the period. State size is `O(log B)` because K3 `b_2=22`, but candidate count is at most `(2 floor(B)+1)^22`. | The apparent gain is Grover search or amplitude estimation and is disallowed by D22; lattice enumeration/LLL-style methods are the matched baseline. Copy access to an unknown period also incurs overlap precision. Test Picard-rank jumps in a one-parameter quartic K3 pencil. **Rejected.** |
| **G10, surface intersection-form signature.** Estimate `(b_2^+,b_2^-)` or test the Hodge index signature. | Sparse chain model plus cup pairing/Hodge star, dimension `D`, accuracy `epsilon`, gap from zero `gamma`; output normalised positive/negative inertia. | Apply a Hermitian block map for the intersection form and estimate signed spectral mass, or measure the Hodge star on harmonic states. | This is generic spectral-density/trace estimation after harmonic projection; stochastic Lanczos uses the same matvecs. For projective surfaces, the Hodge index theorem already fixes much of the signature from Hodge numbers. Test blowups of `P^2` where the exact answer is immediate. **Rejected.** |
| **G11, Hilbert-scheme Nakajima sampler.** Sample a fixed-point partition after a word of incidence correspondences on `oplus_n H^*(S^[n])`. | Smooth projective surface `S` with a fixed-point/equivariant basis, word of `L` creation/annihilation operators, level cutoff `n<=B`, and a promised postselection norm; output a partition/cohomology label. | Bosonic Fock operators implement the Heisenberg correspondence; truncate occupations and dilate each weighted ladder map. Cost `O(L poly(log B))/p_success` only after basis preparation. | The correspondences are the established Heisenberg action, while partition recurrences, symmetric functions, and sequential weighted branching often sample classically. Originality target was a direct geometric correspondence processor, but the operation is an old bosonic ladder network. Test `Hilb^n(C^2)` up to `n=30` against a partition DP. **Rejected for D22.** |
| **G12, Fourier--Mukai kernel transport.** Apply a derived equivalence and sample the cohomological degree/support class of its image. | Finite resolutions for a kernel `P` on `X x Y` and object `E`, bounded cohomological/degree windows, sparse pull--tensor--push maps; output a label from the normalised hypercohomology state. | A three-stage correspondence circuit, with each nonunitary pull/push/tensor map separately dilated and all derived-degree registers retained. | Classical double-complex totalisation and spectral-sequence reduction see the same tensors. On abelian varieties finite theta transforms reduce to Weyl/Bell transforms; general pushforward requires cohomology computation. Originality target is coherent derived pushforward, but no normalisation or hard natural family survives. Test a Poincare kernel on elliptic curves before an abelian surface. **Rejected/held.** |
| **G13, elliptic-surface Picard--Lefschetz return.** Estimate the common fixed-vector fraction of supplied monodromy transvections modulo a prime. Relating this to characteristic-zero cycles or Mordell--Weil rank is an additional theorem. | Factorisation into `L` vanishing-cycle transvections on a rank-`r` integral homology lattice, reduced modulo a supplied prime `M`; output the fraction `M^(k-r)` of vectors fixed by every supplied transvection, where k is their common-kernel dimension. | Compile the reversible linear permutations `|v> -> |T_i v mod M>`, compare outputs to v, and test the common fixed-vector event; no Clifford/Weyl identification is asserted. | Classical elimination on the stacked matrices `T_i-1` over `F_M` costs polynomial in `L,r,log M` and gives this exact fraction. No characteristic-zero or Mordell--Weil transfer is assumed. Originality target is a degeneration-return observable. Test a rational elliptic surface with twelve nodal fibres. **Rejected.** |
| **G14, coherent Zariski-chamber navigation.** Sample the negative curves contracted in the Zariski decomposition of a divisor on a surface. | Intersection matrix for `R` candidate curves, divisor intersections, bit precision `b`, and promise distance `gamma` from chamber walls; output the support of the negative part. | Reversible active-set updates or dissipative relaxation over curve labels, followed by measurement of active constraints. | Solving the negative-definite linear systems and active-set comparisons is polynomial for an explicit list; a quantum linear solver would be old and classical readout costs `Omega(R)`. Enumerating all negative curves is hidden if the list is omitted. Test del Pezzo blowups as Picard rank grows. **Rejected.** |
| **G15, Donaldson--Thomas wall-crossing scattering.** Sample the coherent charge amplitude of ordered Harder--Narasimhan decompositions and attempt to infer a new-chamber BPS factor. | A finite charge group `(Z/M)^r`, skew Euler form, `L` known truncated wall factors of degree `K`, coefficient precision `b`, initial charge state, and promised total contraction success `>=gamma`; output a charge sample or selected complex amplitude to `epsilon`. | Represent the quantum torus by Weyl shifts and apply polynomial/quantum-dilogarithm factors in wall order. Histories with the same total charge interfere with Euler-form phases. For conditional charge probabilities, cost `O(LK poly(r,log M,b))/(gamma epsilon²)` by sampling; for an unnormalised complex amplitude, replace the heralding factor by `(product_j alpha_j)²`, with coherent reference access. Compilation is additional. | Classical truncated wall-crossing DP contracts over `O(M^r)` charges and can be polynomial when `r` is fixed/sparse. The factors may already contain the desired DT invariants; output probabilities do not identify a noncommutative factorisation. Quantum-dilogarithm representations and pentagon circuits are prior operators. Originality target is factor recovery from charge scattering, not merely applying the KS identity. Test the `A_2` pentagon and local `P^2` cutoffs while checking identifiability. **Finalist F3.** |
| **G16, spherical-twist presentation comparison.** Compare two supplied cone circuits in an explicit Hermitian presentation. A presentation-independent derived observable beyond their identical numerical `K`-theory action remains undefined. | Spherical objects with Ext-pairing circuits, two braid words of length `L`, source object state; output squared distance of transformed states, promise `0` or `>=gamma`. | Controlled order of cone/twist transducers retaining Ext and cone registers; interfere the word branches. | On Mukai vectors, twists are explicit reflections and classical matrix words suffice; distinguishing functors beyond `K`-theory requires object-level cone normal forms that the input circuit may hide. Controlled-order interferometry was already attacked in the birational-order lane. Test the `A_2` spherical braid relation on a K3. **Rejected pending a nonnumerical same-output task.** |
| **G17, canonical-ring multiplication sampler.** From pluricanonical sections, sample relations or multiplication defects that distinguish canonical models of general-type surfaces. | Graded spaces `H^0(K^n)` through `n<=N`, multiplication block maps, prepared sections, promise product norm `>=gamma`; output a relation label or product ket. | Reverse or forward multiplication with degree register and postselection; probability is the squared product/adjoint-product norm divided by block normalisation. | Explicit tensors admit ordinary multiplication and tree contraction; equation input requires constructing the pluricanonical bases first. This reduces to the campaign's rational-map/reverse-multiplication normal forms. Test Horikawa surfaces with known canonical rings. **Rejected.** |

## 3. Tournament: eliminations before depth

The first bracket removes G01, G02, G05, and G10 because their physical core is
harmonic projection or spectral density.  It removes G03 because the exact
cohomological gate is prior art, and G09 because its only query reduction is
Grover-style search over lattice classes.  G11--G14, G16, and G17 lose to explicit
partition, matrix, active-set, cone, or tensor recurrences.  G04 remains a useful
problem specification, but a supplied quotient projector is circular and an
unsupplied one needs the cohomology solve.

G06, G08, and G15 advance because they use operations genuinely tied to local
scheme thickness, intrinsic deformation transfer, and wall-ordered Hall/DT
scattering.  The next sections derive their maps rather than awarding novelty or
advantage.  Each ultimately has an unresolved or fatal matched-access obligation.

## 4. Finalist F1: first-loss Jordan spectroscopy of a fat point

### 4.1 Exact monomial construction

Let `A=C[x_1,...,x_n]/J`, where `J` is a zero-dimensional monomial ideal, and
give its `D` standard monomials the orthonormal metric.  Set `ell=x_1`.  The
standard monomials split uniquely into strings

`u, x_1 u, ..., x_1^(lambda_u-1)u`,

where `u` is not divisible by `x_1`.  Put `nu=max_u lambda_u` and
`c_t=#{u:lambda_u>=t}`.  The partition `(lambda_u)` is exactly the Jordan type
of multiplication by `ell`; this invariant is finer than the weak/strong
Lefschetz bit.

Define the partial shift

`S|x_1^i u> = |x_1^(i+1)u>` for `i+1<lambda_u`, and zero otherwise.

Let `E` isometrically copy every terminal monomial to a labelled emission
space.  Since `S^dag S+E^dag E=1`,

`W|b> = |survive>S|b> + |emit>E|b>`                                      (1)

is an isometry and can be completed to a unitary.  Repeat `W` on the surviving
register and record the first emission time `tau`.  On the maximally mixed
state `rho=1/D` (or one half of a maximally entangled state),

`Pr(tau>k)=Tr(S^k(S^dag)^k)/D=rank(S^k)/D
          =(1/D) sum_u max(lambda_u-k,0)`,                                (2)

and hence

`Pr(tau=t)=c_t/D`, `1<=t<=nu`.                                            (3)

Thus one timestamp samples the conjugate Jordan partition.  The exact counts
are recovered from `c_t=D Pr(tau=t)`.  The same probabilities also determine
`#{u:lambda_u=t}=c_t-c_(t+1)`.

One run uses one mixed/uniform preparation, at most `nu` successor calls, a
timestamp of `ceil(log_2(nu+1))` bits, and `O(log D)` live algebra qubits plus
oracle workspace.  Estimating every bin to additive `epsilon` uses
`O(epsilon^-2 log(nu/delta))` runs.  Learning the whole law to TV error
`epsilon` takes `Theta((nu+log(1/delta))/epsilon^2)` samples in the worst case.
Exact integer recovery needs bin error below `1/(2D)`, hence at least order
`D^2` samples by this route.  An optical version routes basis modes along each
string and out-couples a photon at the boundary; MBQC can implement the same
basis permutation and retained emission label.

For the explicit fat complete intersection

`A_(a,b)=C[x,y]/(x^a,y^b)`, `ell=x`,                                     (4)

there are `b` strings, all of length `a`, so `D=ab`, `c_t=b` for `t<=a`,
and `tau` is uniform on `{1,...,a}`.  This gives a direct `ab`-mode diagnostic,
but the answer is already visible in (4).

### 4.2 Why an arbitrary multiplication channel does not measure Jordan type

For an arbitrary nilpotent multiplication matrix `M`, choose
`T=M/alpha`, `alpha>=||M||`, and the defect
`D_T=(1-T^dag T)^(1/2)`.  The analogous first-loss instrument has

`Pr(tau=t)=[||T^(t-1)||_F^2-||T^t||_F^2]/D`.                             (5)

Equation (5) is an exact telescope, needs no eigenvalue gap, and is the
nontrivial part of the candidate.  It measures singular-value moments of powers,
not `rank M^t`.  On a two-dimensional algebra module, the maps
`M_c|0>=c|1>`, `M_c|1>=0`, with `0<c<=1`, all have Jordan partition `(2)`,
but at `alpha=1` their second-time probability is `c^2/2`.  Similarity changes
the answer while preserving the scheme module.  Taking `alpha=||M_c||` repairs
this one edge, but one global scale cannot repair unequal weights on several
strings.  A Jordan-adapted partial isometry requires the chain decomposition
that the experiment was meant to discover.

There is also no legal interference shortcut.  `E` must retain an orthogonal
label for every terminal monomial to make (1) isometric.  Erasing those labels
replaces `E` by a many-to-one contraction with operator norm equal to the square
root of its largest fibre, reinstating the flag-forgetting normalisation already
seen in the Hall lane.

### 4.3 Matched comparator and verdict

A classical algorithm samples the same uniformly random standard monomial,
repeatedly calls the same successor/death oracle, and returns exactly the law
(3), using `O(log D+log nu)` bits besides the oracle.  Coherent uniform
preparation over standard monomials is at least as strong as the classical
sampling access needed by this comparator.  If only equations for `J` are
given, both sides must construct standard-monomial access; that may require the
Groebner/border-basis work whose result exposes the strings.

This differs mathematically from R10's promised first return of one endpoint
vector in a supplied unitary colligation: (2) averages absorbing lifetimes over
an algebra basis and seeks a Jordan partition.  It is nevertheless a monitored
first-detection channel, a studied physical primitive, and it has an exact
classical path sampler on the only intrinsic family above.  F1 therefore yields
the scoped identity (2)--(5), not a time, space, or D22 novelty claim.

The decisive next test would generate random monomial ideals at `D<=10^5`,
compare the empirical law with `rank S^k/D`, then conjugate their multiplication
matrices by ill-conditioned nonunitaries.  The predicted result is that the
partial-shift law stays combinatorial while (5) changes continuously, directly
separating a scheme invariant from a metric-channel observable.

## 5. Finalist F2: coherent Kuranishi-tree interference

### 5.1 Intrinsic obstruction problem and recurrence

Let `(L,d,[,])` be a finite-dimensional dg Lie algebra controlling a deformation
problem, with explicitly supplied contraction data

`(H,0) --i--> (L,d) --p--> (H,0)`, `p i=1`,
`i p=1-dh-hd`.                                                           (6)

The displayed Hermitian metrics and the particular contraction are input data.
For a unit `a in H^1`, fix Kuranishi gauge and solve formally

`x(t)=t i(a)-(1/2)h[x(t),x(t)]`,
`kappa(t)=(1/2)p[x(t),x(t)] in H^2[[t]]`.                                (7)

Writing `x(t)=sum_(n>=1)t^n x_n` and
`kappa(t)=sum_(n>=2)t^n kappa_n` gives the exact recurrence

`x_1=i(a)`,
`x_n=-(1/2)h sum_(r=1)^(n-1)[x_r,x_(n-r)]`,
`kappa_n=(1/2)p sum_(r=1)^(n-1)[x_r,x_(n-r)]`.                           (8)

When the lower obstructions vanish, `kappa_m(a)` is the order-`m` obstruction
in this Kuranishi chart.  Its vanishing is invariant under the allowed formal
coordinate changes; its norm and normalised ket depend on the supplied metrics
and contraction.  This is the needed distinction from the R10 pencil: (8)
allows the endpoint representative and quotient to change through the
homotopy, rather than testing the coefficient of one fixed section.

Define **KURANISHI-ORDER** with the promise that `kappa_2=...=kappa_(m-1)=0`
and either `kappa_m=0` or `||kappa_m||>=gamma`.  The common classical output is
the zero/nonzero bit.  An optional quantum output on the nonzero side is the
normalised direction `|kappa_m>/||kappa_m||`; it is not compared with a full
classical coordinate vector when assessing the bit problem.

The input model is now split explicitly after independent objection O8.
**Model A** supplies coordinate vectors and explicit/sparse maps, with their
precision and indexing; the vector recurrence below is its classical comparator.
**Model B** supplies a preparation unitary for `|a>` (including its specified
inverse/control access) and compiled coherent block maps. The classical side
gets the same circuit descriptions or the separately declared query interface;
it does not receive a free amplitude list, nor is it assumed to simulate those
circuits efficiently. Each attempted transduction still consumes `m` prepared
source instances. A source providing only unknown copies is a THIRD model;
this memo establishes no same-output lower bound for it.

### 5.2 The tree map and its actual probability

Expanding (8) expresses `kappa_m` as a sum over the `Cat_(m-1)` planar full
binary trees with `m` leaves.  Each leaf carries `i`, each of the `m-1`
vertices carries the bracket, each nonroot vertex is followed by `h`, and the
root by `p`.  Every tree has coefficient of magnitude `2^(-(m-1))`; its sign
is fixed by the bracket and recursion conventions.  Hence there is a
homogeneous linear map

`A_m: (H^1)^(tensor m) -> H^2`, `A_m a^(tensor m)=kappa_m(a)`.             (9)

Let `I=||i||`, `P=||p||`, `H=||h||`, and let `beta` bound the bilinear bracket
as a linear map `L tensor L -> L`.  A safe LCU normalisation is

`Lambda_m = Cat_(m-1) P beta^(m-1) H^(m-2) I^m / 2^(m-1)`.                (10)

This may be loose if tree images are orthogonal, but it cannot be silently
replaced by `||A_m||` while retaining a sparse controlled-tree compilation.
The next resource expressions are conditional on supplied tree-control circuits:
let `C_tree(m,epsilon)` be the cost of preparing/unpreparing the Catalan tree
label and `C_select(m,epsilon)` the cost of its controlled evaluator, including
routing, work registers and all dilation flags. No uniform polynomial compiler
for these circuits is proved here. Their costs are ADDED for every attempt;
therefore `O(Rm)` local block calls alone is not an end-to-end gate bound.

Prepare a weighted tree label, SELECT the corresponding sequence of bracket,
`h`, `i`, and `p` block maps, unprepare the label, and accept all dilation
flags.  The successful Kraus block is `A_m/Lambda_m`, so one attempt on `m`
copies has

`p_m(a)=||kappa_m(a)||^2/Lambda_m^2`.                                    (11)

With the stated promise, direct repetition uses

`R=ceil(Lambda_m^2 gamma^(-2) log(1/delta))` attempts,                    (12)

`mR` copies of `a`, and `O(R m)` calls to the supplied tensor blocks, plus
tree-routing and their workspaces.  No phase estimation or additional spectral gap is used once all the declared
blocks and tree circuits have been supplied. Their construction may require both.  Finite precision per controlled block must be `o(delta/(Rm))` in a
conservative trace-error budget.  A postselected linear-optical tensor network
or MBQC graph can realize a small tree sum; every nonisometric bracket/homotopy
flag and the probability (11) remain.

The Catalan growth in (10) is substantive.  In the scalar stress recurrence
`x_1=1`, `x_n=-(1/2)sum_(r=1)^(n-1)x_r x_(n-r)`, one gets
`x_n=(-1/2)^(n-1)Cat_(n-1)`.  Thus even with unit local norms the natural LCU
scale is asymptotically `Theta(2^m/m^(3/2))`; a lower-obstruction promise alone
does not keep (12) polynomial.  Conversely, if the tree terms align, an
operator-norm-optimal dilation may have much better success, but compiling it
can require forming the sum that is being computed.

### 5.3 A surface family and the strongest classical attack

Vakil's Murphy-law theorem supplies a precise, if nonconstructive, surface
family: for every `m>=2`, the finite-type singularity
`Spec C[u]/(u^m)` occurs, up to smooth factors, on a moduli space of smooth
projective general-type surfaces; the same universality occurs for stable
rank-one torsion-free sheaves.  Along the distinguished formal direction, a
Kuranishi equation can therefore have first term `c u^m`, `c!=0`.  This shows
that arbitrarily high first obstructions are genuine surface/sheaf phenomena,
not artefacts of a fixed matrix pencil.  It does not provide efficient
contraction data or a large norm `|c|`.

This existence statement does not extend to every surface moduli problem.
In particular, RHom formality for polystable sheaves on projective K3 surfaces
(arXiv:1803.03974) prevents substituting that class as an arbitrary high-order
example. The surface formality/quadraticity comparison in arXiv:1902.06486 is
another required scope check. Vakil's general-type existence remains distinct
from a uniformly compiled and conditioned family.

For explicit coordinates, (8) is already a dynamic program.  Store
`x_1,...,x_m`; for each `n`, compute the `n-1` brackets and their sum.  If one
bracket application on explicit vectors costs `C_B`, this needs
`O(m^2 C_B)` arithmetic operations, `O(m dim L)` words, and returns the full
obstruction vector.  It avoids enumerating Catalan-many trees and avoids
postselection.  Sparse dg data only strengthen this comparison.  On the
one-dimensional germ `u^m`, once the local equation is known, the answer is
immediate.

There remains a narrow **conditional access window**: `dim L=2^q`, all maps in
(8) have `poly(q,m)` compiled circuits, `Lambda_m/gamma=poly(q,m)`, and only the
zero/nonzero bit or the ket is requested.  The quantum procedure is then
polynomial while explicit state-vector dynamic programming is exponential.
No uniform polynomial tree PREPARE/SELECT construction is established.
No natural surface family satisfying all these conditions, and no lower bound
against a classical sampler with the same succinct tensors, is known here.
Encoding an arbitrary circuit into the dg Lie data would only restate generic
circuit simulation and would not satisfy D22.

Finally, (9) is an `m`-copy homogeneous transduction.  The campaign's existing
finite-copy rational-map normal form therefore attacks the physical mechanism
directly: structured homotopy transfer explains the coefficients but does not
create a new class of exact quantum operations.  F2 survives as an original
algebraic-geometric **problem target** and as an explicit circuit proposal; it
does not yet survive the mechanism, normalisation, or matched-advantage tests.

The decisive experiment is to generate sparse contraction data with
`dim L=2^q` for `q<=16`, compute (8) and the tree LCU independently through
`m<=10`, and record `Lambda_m/||kappa_m||`, tensor-network treewidth, and the
best dynamic-programming time.  Any claimed finite benefit must report all
three, especially instances selected after conditioning on small cancellation.

### 5.4 Stronger construction to pursue: coderivation scattering

There is a more geometric implementation than SELECT over explicit trees.  On
the truncated graded symmetric coalgebra of `L[1]`, the dg Lie data define the
Chevalley--Eilenberg coderivation

`Q_g = d + g q_2`, `Q_g^2=0`,                                             (13)

where `q_2` merges two particles with the signed bracket.  In occupation
operators, its number-changing part has the schematic form

`q_2=(1/2) sum_(i,j,k)c^k_(ij) a_k^dag a_j a_i`.                          (14)

The dg Lie identities, rather than a scheduled tree list, enforce the
cancellations in `Q_g^2`.  Homological perturbation reduces (13) to a
coderivation on `S^c(H[1])`; its `m`-input/one-output Taylor coefficient is the
transferred higher bracket underlying (9).  Thus a many-body scattering
amplitude from `m` harmonic inputs to one harmonic obstruction output can sum
the Kuranishi trees as physical virtual histories.

This is the strongest constructive continuation from F2, but it is not yet an
algorithm.  `Q_g` is nilpotent, not Hermitian.  A positive-Hilbert experiment
must use a Hermitian dilation or a supersymmetric Hamiltonian and show that its
measured scattering block is the transferred bracket with controlled error.
If contractible modes have energy scale `Delta` and the cubic coupling is `g`,
ordinary perturbative elimination makes an order-`m` coupling scale like
`g^(m-1)/Delta^(m-2)` times the obstruction map.  Resolving the resulting Rabi
frequency can therefore take time at least its inverse; choosing `g` comparable
to `Delta` invalidates the transfer approximation unless a nonperturbative
identity is proved.  Conventional tree-level recursion also remains the
classical comparator.

The next construction should consequently prove an exact finite-dimensional
positive-Hilbert scattering/instrument identity, not infer advantage from
generic Hamiltonian simulation.  It must compare physical evolution time with
the `O(m^2)` recurrence and show why the induced map is invariant under changing
the contractible resolution.  This route is materially beyond the fixed-vector
R10 pencil and merits a new lane even though F2 as presently compiled does not
pass.

## 6. Finalist F3: finite quantum-torus scattering for DT wall crossing

### 6.1 A physical finite regularisation

Let `M` be odd, `Gamma_M=(Z/MZ)^r`, and let `<,>` be a supplied skew bilinear
Euler form.  Put `omega=exp(2 pi i/M)` and give `l^2(Gamma_M)` its counting
metric.  Magnetic translations

`W_gamma|eta> = omega^(<gamma,eta>/2)|eta+gamma>`                         (15)

are unitary and satisfy

`W_alpha W_beta=omega^(<alpha,beta>/2)W_(alpha+beta)`.                    (16)

Here `/2` means multiplication by the inverse of two modulo `M`.  Thus (16)
is an exact finite representation of the quantum-torus commutation law.

For wall `j`, supply a truncated halo polynomial

`P_j(z)=sum_(k=0)^K c_(j,k)z^k`, `A_j=P_j(W_(gamma_j))`.                  (17)

An efficiently known safe normalisation is
`alpha_j=sum_k |c_(j,k)|`; the spectral optimum is
`max_(z in spec W_gamma_j)|P_j(z)|`, but computing and compiling at that
scale is a separate task.  An LCU of controlled Weyl translations realizes
`A_j/alpha_j` as a successful Kraus block.  For the ordered wall word

`A=A_L...A_1`,                                                          (18)

accepting every flag and then measuring charge gives total success and
conditional output

`p_wall=||A|0>||^2 / product_j alpha_j^2`,
`Pr(eta | success)=|a_eta|^2/||A|0>||^2`,                                (19)

where

`a_eta = sum_(k_1,...,k_L: sum_j k_j gamma_j=eta)
   [product_j c_(j,k_j)]
   omega^((1/2)sum_(i<j) k_i k_j <gamma_j,gamma_i>)`.                    (20)

Equation (20) is the constructive content: ordered Harder--Narasimhan charge
histories reaching the same total charge interfere with the Euler-form phase.
If `p_wall>=gamma`, `O(gamma^(-1) epsilon^(-2) log(1/delta))` attempts give
additive-`epsilon` estimates of selected output probabilities.  Each attempt
uses `O(LK)` controlled translations and coefficient rotations, with
`poly(r,log M,b)` cost per translation/rotation, plus `O(r log M)` live charge
qubits and LCU workspace.  Estimating a complex `a_eta` needs a coherent
reference/Hadamard-type interferometer and adds its own inverse-signal cost.

The unnormalised complex amplitude is a different output. If
`A_norm=product_j alpha_j`, a coherent reference/Hadamard experiment measures
`a_eta/A_norm`. Direct estimation of `a_eta` to additive `epsilon` therefore
costs `O(A_norm² epsilon^-2 log(1/delta))` trials, independently of a lower
bound on total heralding success. The conditional charge probability law,
the conditional normalized state, and this unnormalised amplitude must not
share a resource statement.

To avoid wraparound changing the intended charge sum, `M` must exceed twice
the largest coordinate reachable under the cutoff.  The motivic parameter in
the actual DT quantum torus is formal and is not automatically a phase on the
unit circle.  Substituting the root of unity `omega`, truncating every factor,
and choosing a positive Hilbert metric define a finite diagnostic; they do not
preserve motivic DT invariants without an additional specialisation theorem.

### 6.2 Surface family and the factor-recovery obstruction

For a first exact check, take the rank-two `A_2` charge lattice with
`<e_1,e_2>=1`.  The wall-crossing identity becomes the quantum-dilogarithm
pentagon, schematically

`Phi(W_1)Phi(W_2)=Phi(W_2)Phi(W_(1+2))Phi(W_1)`                           (21)

up to the chosen `q` and ordering conventions.  A cutoff/root-of-unity test
must use the corresponding cyclic dilogarithm or compare only coefficients
below the truncation boundary; naively truncating both sides need not preserve
(21).  A surface-rich family is the category of stable sheaves supported on
the zero section of `K_(P^2)`: its numerical charges come from the surface,
while the local Calabi--Yau threefold supplies the skew DT pairing.  Varying a
stability condition changes the ordered BPS/DT factors.  This makes (18) a
genuine wall-crossing word rather than an arbitrary circuit.

The desired problem, however, is to recover unknown new-chamber invariants from
known old-chamber factors.  Applying their product does not do that.  The KS
identity states that different ordered factorisations represent the same
quantum-torus element.  Even complete knowledge of `A|0>` generally does not
uniquely recover its noncommutative factors without the chamber, ray support,
and integrality constraints.  Charge measurement is weaker still: arbitrary
diagonal phase changes of the amplitudes leave every probability in (19)
unchanged.  At linear cutoff, `(1+aW_1)(1+bW_2)|0>` has four distinct charges,
so there are no alternative histories and the Euler phase is completely
invisible in the charge probabilities.  Interference starts only when several
decompositions reach the same charge.

The finite scattering distribution in (19) is nevertheless a precise common
output.  Its strongest direct classical algorithm maintains the reachable
charge array and updates

`a^(j)_eta=sum_(k=0)^K c_(j,k)
 omega^(k<gamma_j,eta>/2) a^(j-1)_(eta-k gamma_j)`.                       (22)

This costs `O(LK R_ch)` arithmetic operations and `O(R_ch)` words, where
`R_ch<=M^r` is the number of reachable charges.  It is polynomial when `r` is
fixed and can be much smaller under sparse support.  For variable `r`, the
quantum circuit stores a charge in `O(r log M)` qubits while (22) can be
exponential.  No hardness result against a classical sampler is established;
positive or weak-sign factors may admit sequential Monte Carlo, while severe
phase cancellation can make `p_wall` exponentially small on the quantum side.

### 6.3 Originality and verdict

Quantum-dilogarithm pentagon operators, finite-dimensional versions, and
unitary projective representations of quantum cluster transformations predate
this proposal.  KS wall crossing itself formulates DT invariants as elements
of a quantum torus.  Consequently, implementing (18) is a substantive
operation-level reduction to described prior structures, not a new mechanism
under D22.  Calling (19) a DT sampler creates a possibly new output problem,
but it neither recovers the DT factors nor proves an advantage over (22).

The smallest decisive experiment is two-part.  First implement the correct
cyclic `A_2` pentagon at odd `M<=31` and verify the full output vector, not just
probabilities, under both factorizations.  Then fit a deliberately hidden
middle factor using (i) charge samples, (ii) complex amplitudes on several
input states, and (iii) classical noncommutative factorisation.  Failure of
case (i), already predicted by the phase ambiguity, prevents the proposed
sampling output from being sold as an invariant-recovery algorithm.  Scaling
on a local-`P^2` cutoff must report `R_ch`, the product LCU normalisation, and
the minimum success probability rather than only gate depth.

## 7. Bounded checks

One bounded in-memory NumPy run (`timeout 30`, exit zero) checked only the
finite linear-algebra identities below.

1. For strings `(4,2,1)`, the largest residual between the first-loss telescope
   and `c_t/D` was `2.78e-16`.  A fixed nonunitary similarity preserved the
   Jordan blocks but moved one probability by `0.238095`, confirming that the
   general defect-channel law is not similarity invariant.
2. The scalar Kuranishi recurrence agreed with
   `(-1/2)^(n-1)Cat_(n-1)` through `n=10`; its tenth coefficient was
   `-9.49609375`.  This checks the Catalan accounting, not a geometric dg Lie
   instance or a complexity claim.
3. On `Gamma_11=(Z/11)^2`, three degree-two wall polynomials produced 19
   reachable charges.  Direct `121`-dimensional Weyl-matrix multiplication and
   recurrence (22) agreed in Euclidean norm to `3.67e-18`.  This does not check
   a cyclic dilogarithm identity or any DT specialisation.

## 8. Targeted primary literature resolution

These sources were checked after the constructions above were derived.  They
resolve technical facts and operation-level prior art; failure to find a paper
would not establish originality.

- Breuckmann--Davydova--Eberhardt--Tantivasadakarn,
  [*Cups and Gates I*](https://doi.org/10.1007/s00220-026-05570-z), constructs
  cup-product cohomology invariants and constant-depth copy-cup logical gates.
  It is a direct novelty obstruction for G03, not a proof that every coherent
  algebraic-geometric cup query is easy.
- Cade--Crichigno, [arXiv:2107.00011](https://arxiv.org/abs/2107.00011), and
  Lloyd--Garnerone--Zanardi,
  [arXiv:1408.3106](https://arxiv.org/abs/1408.3106), resolve the established
  supersymmetric/cohomology and Laplacian/Betti quantum frameworks.  Together
  with the campaign's audited Koszul lane, they block novelty claims for
  G01--G02 and G05.  Apers--Gribling--Sen--Szabo,
  [DOI 10.22331/q-2023-12-06-1202](https://doi.org/10.22331/q-2023-12-06-1202),
  is the matched modern gap/normalisation warning for Betti estimation.
- Iarrobino--Macias Marques--McDaniel,
  [arXiv:1802.07383](https://arxiv.org/abs/1802.07383), defines the Jordan type
  of multiplication by an Artinian-algebra element and establishes that it is
  finer than Lefschetz yes/no properties.  Friedman--Kessler--Barkai,
  [arXiv:1603.02046](https://arxiv.org/abs/1603.02046), studies repeated
  quantum first-detection statistics.  These support the two ingredients of
  F1 and make historical novelty of the combined monitored operation doubtful;
  neither source supplies equations (2)--(5) as a scheme algorithm.
- Vakil, [arXiv:math/0411469](https://arxiv.org/abs/math/0411469), proves that
  every finite-type singularity occurs up to smooth parameters on moduli of
  smooth general-type surfaces and stable sheaves.  This validates F2's use of
  `C[u]/(u^m)` deformation germs but supplies no efficient dg model.
  Arvanitakis--Hohm--Hull--Lekeu,
  [arXiv:2007.07942](https://arxiv.org/abs/2007.07942), derives homotopy transfer
  through nilpotent coderivations/effective-field-theory elimination, while
  Bonezzi--Chiaffrino--Díaz-Jaramillo--Hohm,
  [arXiv:2312.09306](https://arxiv.org/abs/2312.09306), derives tree-level
  scattering recursion by homotopy transfer.  They are exact mathematical and
  field-theoretic comparators for Section 5.4; they do not describe the needed
  finite positive-Hilbert quantum instrument or prove its advantage.
- Nakajima,
  [arXiv:alg-geom/9507012](https://arxiv.org/abs/alg-geom/9507012), constructs
  the Heisenberg action on Hilbert schemes of points of projective surfaces by
  correspondences.  This is substantive operation-level prior art for G11.
- Kontsevich--Soibelman,
  [arXiv:0811.2435](https://arxiv.org/abs/0811.2435), places motivic DT
  invariants and wall crossing in quantum tori.  Faddeev--Kashaev,
  [arXiv:hep-th/9310070](https://arxiv.org/abs/hep-th/9310070), includes a
  finite-dimensional quantum dilogarithm/pentagon construction, and
  Fock--Goncharov,
  [arXiv:math/0702397](https://arxiv.org/abs/math/0702397), constructs unitary
  projective representations of quantum cluster transformations with quantum
  dilogarithms.  These are direct mechanism-equivalence attacks on F3.

## 9. Final tournament and unresolved obligations

The strict score gives one point only when a PRD criterion is presently met,
not when a route might eventually meet it.

| Rank | Candidate | Problem / baseline / quantum advantage / dequantisation survival / hardware / originality | Result of strongest attack |
|---|---|---|---|
| 1 | **F2 / G08, Kuranishi obstruction** | `1 / 1 / 0 / 0 / 0 / 0` = **2/6** | The problem and explicit recurrence are real. Tree LCU has Catalan normalisation and an `O(m^2)` classical DP; direct coderivation scattering remains an unproved stronger operation. |
| 2 | **F1 / G06, first-loss Jordan profile** | `1 / 1 / 0 / 0 / 0 / 0` = **2/6** | Exact channel identity, but intrinsic access makes it basis-preserving and classically sampleable; general access loses Jordan invariance. |
| 3 | **F3 / G15, DT scattering** | `1 / 1 / 0 / 0 / 0 / 0` = **2/6** | Exact finite charge interference, but prior quantum-dilogarithm operators, unproved DT specialisation, nonidentifiable factors, and DP comparator. |

F2 ranks first because its direct coderivation-scattering continuation may remove
the artificial SELECT-over-trees normalisation while retaining a genuine
changing-quotient obstruction.  This is a research ordering, not evidence for
speedup or novelty.

The explicit obligations are:

- **F2:** derive a finite positive-Hilbert Hamiltonian/instrument whose measured
  `m`-to-one block is exactly the transferred bracket; bound evolution time,
  leakage, truncation, state preparation, and precision; show resolution
  independence; beat the `O(m^2)` tree recurrence on a natural surface/sheaf
  family; and distinguish the mechanism from conventional scattering or
  generic circuit simulation.
- **F1:** construct an intrinsic partial isometry for a nonmonomial quotient
  from equations without computing its Jordan basis, and prove that a same-
  access classical path/rank estimator cannot match it.  It must also escape
  monitored first-detection prior art and the R10 colligation equivalence.
- **F3:** prove that the finite root-of-unity specialisation retains the desired
  DT invariant; state an identifiable factor-recovery output; give a lower
  bound against recurrence (22) or a same-output sampler; keep `p_wall`
  inverse-polynomial; and provide a mechanism beyond known quantum-dilogarithm
  and cluster intertwiners.

No finalist currently establishes a true quantum advantage or D22-compliant
original mechanism.  Classical hardness of exact cohomology, deformation, or
DT invariants does not transfer to the normalised approximate outputs above.

## MERGE PROPOSAL

The root may use the following definitions and quantified statements as paste
material.  They are proposed for independent criticism, not canonical status
promotion.

**D-R11-LEFSCHETZ-FIRST-LOSS.**  Data: a finite monomial quotient
`A=C[x_1,...,x_n]/J` with orthonormal standard monomials, uniform standard-
monomial preparation, coherent `x_1` successor/death access, and cutoff `nu`.
Output: a first-death timestamp, or its distribution to stated additive/TV
error.  All source preparations, up to `nu` successor calls per run, and
timestamp readout are charged.

**Proposed G06 exact statement.**  For every such `A`, if `lambda_u` are the
`x_1`-string lengths and `D=sum_u lambda_u`, then the isometry (1) gives
`Pr(tau>k)=rank(S^k)/D` and
`Pr(tau=t)=#{u:lambda_u>=t}/D`.  A classical algorithm with the same uniform
sampling and successor access returns exactly the same law with the same number
of oracle calls up to reversible overhead.  For a general contraction `T`, the
law is (5) and is not invariant under similarity, as witnessed already in
dimension two.

**D-R11-KURANISHI-ORDER.**  Data: a finite Hermitian dg Lie algebra, contraction
`(i,p,h)`, compiled/sparse bracket and contraction maps with their block
normalisations, unit `a in H^1`, order `m`, and promise
`kappa_2=...=kappa_(m-1)=0` with either `kappa_m=0` or
`||kappa_m||>=gamma`.  Output: the zero/nonzero bit and optionally the
normalised `H^2` direction on the nonzero side.

**Proposed G08 exact statement.**  For every such input, equations (8)--(9)
define the order-`m` Kuranishi obstruction as a sum of `Cat_(m-1)` tree maps.
The explicit tree LCU with scale (10) has one-attempt success (11) and direct-
repetition resources (12).  With explicit vector access, recurrence (8)
computes the full coefficient using `O(m^2)` bracket applications.  No claim is
made that the bound (10) is optimal or that coderivation scattering has the
same cost.

**D-R11-CE-SCATTERING-OPEN.**  Data: the truncated symmetric-coalgebra
coderivation (13), a positive-Hilbert physical completion, harmonic in/out
states, particle cutoff, coupling, and error budget.  Target output: the
complex `m`-harmonic-input to one-harmonic-output amplitude whose leading
effective coefficient is the transferred `m`-bracket.  Required theorem:
identify the measured finite-time amplitude exactly or with a uniform error
bound and account for inverse effective coupling.  This is an open construction,
not an asserted definition of a solved algorithm.

**D-R11-DT-CHARGE-SCATTERING.**  Data: odd `M`, finite charge group, skew Euler
form, `L` degree-`K` wall polynomials with `b`-bit coefficients, Weyl access,
initial charge state, and success promise `p_wall>=gamma`.  Output: one charge
from (19), or a selected complex amplitude under an explicitly supplied
reference experiment, at stated error.

**Proposed G15 exact statement.**  For every such finite input, the stagewise
LCU realizes (18), has success and output law (19)--(20), and costs `O(LK)` Weyl
calls per attempt.  Classical dynamic program (22) computes the full reachable
amplitude array in `O(LK R_ch)` arithmetic operations and `O(R_ch)` words.
Neither statement identifies unknown DT factors, proves a motivic
specialisation, or establishes D22 novelty.

**Portfolio disposition.**  Retain the 17 candidates as scoped scouting and
advance only D-R11-CE-SCATTERING-OPEN to a new construction/criticism loop.
Do not merge a north-star success statement from this lane.  The global
research goal remains active.

## Independent-review scope repairs, 2026-09-07

The mathematical controls above are distinct from complete algorithms. G01's
polynomial notation is schematic, conditional on supplied normalized blocks,
preparation and a gap; it is not a compiled complexity theorem. G02 outputs
discrete nullities until a certified analytic/discretisation comparison is given.
G03 and G05 reject their displayed operations only. G04 is the separately
supplied-projector query D-R11-TRIPLE-QUOTIENT-QUERY; constructing that projector
from equations remains unresolved. G07 retains its circular-access objection.

For G06, one ideal trajectory samples the law exactly. Estimating every integer
`c_t` from a histogram can use `O(D² log(nu/delta))` samples to make each bin
error less than `1/(4D)`, before rounding; this is a sufficient histogram cost,
not a lower bound against every possible profile algorithm. The path sampler
is already classically identical in the same monomial access.

For G09 the finite search set is primitive marked vectors with positive height
`max_j |v_j|<=B`, excluding zero. It has at most `(2 floor(B)+1)^22` elements.
A bound on the indefinite intersection pairing is NOT a finite search bound.
For G10, state whether a Hodge diamond is supplied; if so the surface signature
can already be determined by `b2plus=1+2h20`, `b2minus=h11-1`.
For G13, choose a supplied prime modulus `M`: the physical map is the reversible
linear permutation `|v> -> |T_i v mod M>`, not an asserted Clifford/Weyl lift.
The common fixed-vector fraction is `M^(k-r)`, with `k` the nullity over `F_M`
of the stacked matrices `T_i-1`, and classical finite-field elimination computes
it. No unproved characteristic-zero transfer or Mordell--Weil formula is used.
For G16 only an explicit metric/presentation-dependent circuit distance has
been specified; an intrinsic derived-invariant task is still a construction
obligation. G11, G12, G14 and G17 retain their explicit-input classical costs
and the separate cost of obtaining their geometric bases from equations.
