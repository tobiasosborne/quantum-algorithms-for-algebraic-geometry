# Theta-isogeny transport: twisted sectors, exact weights, and its finite transform

2026-09-05. Bounded independent construction for `qaag-ibb`.
Canonical data and outputs are D-THETA-ISOGENY, D-THETA-SECTOR-TRANSFORM
and D-THETA-CLASSICAL-OUTPUTS in `definitions/theta-isogeny.md`.
Claim status lives only in `claims/CLAIMS.md`, C-353--C-354.
The declared section metric below departs from C1's Fock convention.
Evaluation kets conjugate section coordinates, consistently with C3.
The local level n and dimension g are not the seed's variable parameters.
Root owns all shared definitions, claims, references, tracking and commits.

The construction works exactly, retaining every character sector. Its circuit
is independent of the period matrix even for a non-product abelian variety.
The geometric information remains in the supplied evaluation states and their
nonuniform sector weights. The resulting operation is a finite theta-character
transform; at the lowest level it is an ordinary Bell transform. No original
mechanism or matched speedup is established by this construction.

## 1. Explicit family, twists, and the section metric

1.1. Supply a symmetric g-by-g period matrix Omega with Y=Im(Omega)>0 and
A=C^g/(Z^g+Omega Z^g), with its standard symmetric principal polarization L.
Begin with g=1; every calculation below also applies to non-diagonal Omega.
The marking of the lattice and the standard theta bases are input conventions,
not outputs to be reconstructed from an arbitrary equation of a variety.

1.2. For n>=1, j in {0,...,n-1}^g, and alpha,beta in {0,1/2}^g, put

    theta_(n,j)^(alpha,beta)(z)
      =sum_(ell congruent j mod n)
         exp[pi i*(ell+alpha)^T Omega*(ell+alpha)/n
              +2 pi i*(ell+alpha)^T*(z+beta/n)].              (1)

Under z->z+a, a integral, the extra flat multiplier is exp(2 pi i alpha.a).
Under z->z+Omega a, the usual level-n multiplier gains exp(-2 pi i beta.a).
Thus these are sections of L^n tensor F_(alpha,beta), where F is the specified
flat two-torsion bundle. Distinct twists are not declared the same line bundle.

1.3. On the universal cover choose the Gaussian cubist metric

    h_n(z)=exp[-2 pi n*Im(z)^T Y^(-1) Im(z)]

and normalized Haar measure dx dy, where z=x+Omega y and x,y lie in [0,1]^g.
The flat factor has its unitary metric. This is not a finite-level
Fubini--Study metric. Orthogonality in x eliminates different frequencies.
For a diagonal basis norm, the translates m+y+(j+alpha)/n tile R^g, giving

    ||theta_(n,j)^(alpha,beta)||^2
      =integral_(R^g) exp(-2 pi n*u^T Y u)du
      =det(2nY)^(-1/2).                                     (2)

Consequently phi_(n,j)^(alpha,beta)=det(2nY)^(1/4)*theta_(n,j)^(alpha,beta)
is an orthonormal basis. Denote its section space by H_n^(alpha,beta).

1.4. The isogeny mu(P,Q)=(P+Q,P-Q) has diagonal A[2] as its kernel,
of order 4^g. The symmetric bundle identity is

    mu^*(L^k box L^k)=L^(2k) box L^(2k).

Both metrics agree pointwise on the chosen lifts, because
h_k(P+Q)h_k(P-Q)=h_(2k)(P)h_(2k)(Q). Pullback of
F_(alpha,beta) box F_(alpha,beta) is trivial: the flat multipliers cancel
or square to one on both input lattices. The target sectors are therefore

    direct-sum_(alpha,beta)
      H_k^(alpha,beta) tensor H_k^(alpha,beta).               (3)

There are 4^g sectors of dimension k^(2g), matching the input dimension
(2k)^(2g). Normalized Haar measure makes pullback within each sector an
isometry. Distinct deck characters give orthogonal sectors. The following
formula constructs the full unitary explicitly, rather than inferring a
cheap circuit merely from this abstract direct-sum statement.

## 2. Actual pullback matrix and its inverse circuit

2.1. Set sigma=2alpha and delta=2beta, both binary g-vectors. The unitary
J from (3) to H_(2k)^(0,0) tensor H_(2k)^(0,0) has the exact columns

    J |sigma,delta;j,l>
      =2^(-g/2) sum_(epsilon in {0,1}^g)
         exp[pi i*delta.(j+l+sigma+k epsilon)/k]
         |[j+l+sigma+k epsilon]_(2k),
           [j-l+k epsilon]_(2k)>.                           (4)

Here j,l range in {0,...,k-1}^g; all vector remainders are coordinatewise.
The quantum operation on input evaluation states is J^dagger, not J.

2.2. Derivation: in the product of two level-k theta series evaluated at
P+Q and P-Q, write their frequencies as p=km+j+alpha and q=kn+l+alpha.
Use a=p+q and b=p-q. Then

    p^T Omega p+q^T Omega q=(a^T Omega a+b^T Omega b)/2.

The two integer vectors m+n and m-n have a common parity epsilon.
Splitting that parity yields the two level-2k theta indices in (4).
The beta terms give its displayed phase. The orthonormalization ratio
from (2) supplies 2^(-g/2). No factorization assumption on Omega occurred.
In particular, off-diagonal entries of a general period matrix do not
create a new circuit or a residual moduli-dependent mixing matrix.

2.3. Equation (4) factors into three explicit operations. Apply the phase
exp[pi i*delta.(j+l+sigma)/k], apply Hadamards delta->epsilon, then apply
the permutation from (j,l,sigma,epsilon) to the two displayed indices a,b.
Its inverse is obtained coordinatewise from

    sigma=(a+b) mod 2,
    j=((a+b-sigma)/2) mod k,
    l=((a-b-sigma)/2) mod k,
    epsilon=([a-j-l-sigma]_(2k))/k.                         (5)

The last numerator is either 0 or k. Thus the permutation is bijective
even when k is even. This proves unitarity without a norm oracle.
Arithmetic, one Hadamard per coordinate, and controlled rational phases
compile in O(g*poly(log(k+1),log(1/eta))) gates at error eta.
Live data occupy O(g log(k+1)) qubits, plus arithmetic/synthesis workspace.
At k=1 there are no j,l registers and the circuit is Clifford with O(g)
gates. All outputs are retained; the ideal transformation has no failures.

## 3. Evaluation normalization and the reproducing kernel

3.1. Define the unnormalized evaluation ket and its squared norm by

    e_n^xi(z)=sqrt(h_n(z))*sum_j conjugate(phi_(n,j)^xi(z))|j>,
    B_n^xi(z)=||e_n^xi(z)||^2,
    E_n^xi(z)=e_n^xi(z)/sqrt(B_n^xi(z)) when B_n^xi(z)>0.      (6)

Here xi=(alpha,beta), and a missing xi means the untwisted bundle.
The input model supplies copies of E_(2k)(P) and E_(2k)(Q), expressed in
these known basis indices. It supplies neither the classical points nor
a preparation inverse unless separately declared and charged.

3.2. Conjugating the section evaluation identity for J gives

    J^dagger[e_(2k)(P) tensor e_(2k)(Q)]
      =direct-sum_xi [e_k^xi(P+Q) tensor e_k^xi(P-Q)].        (7)

All relative phases follow from (1) and the chosen lifts and fiber frames.
Changing those frames changes the corresponding ket phases consistently.
Measured weights are intrinsic. Taking squared norms gives

    B_(2k)(P)B_(2k)(Q)
      =sum_xi B_k^xi(P+Q)B_k^xi(P-Q).                        (8)

Thus the normalized output has sector probabilities

    w_xi(P,Q)=B_k^xi(P+Q)B_k^xi(P-Q)
                   /[B_(2k)(P)B_(2k)(Q)].                  (9)

Conditional on a positive-weight sector, its state is the product of the
two normalized twisted evaluation kets. Zero-weight sectors are absent;
their normalized conditional kets need not be defined. Selecting one
sector costs its actual probability w_xi, not 4^(-g) by assumption.

3.3. For completeness, let K_n^xi(z,z')=<e_n^xi(z)|e_n^xi(z')> and let
Gamma be the corresponding kernel divided by sqrt(B(z)B(z')). From (7),

    Gamma_(2k)(P,P') Gamma_(2k)(Q,Q')
      =sum_xi sqrt(w_xi(P,Q)w_xi(P',Q'))
         Gamma_k^xi(P+Q,P'+Q') Gamma_k^xi(P-Q,P'-Q').         (10)

This is the normalized reproducing-kernel identity on the chosen frames;
terms with zero weight are interpreted through the unnormalized identity.
No translation-invariance assumption on finite-level Bergman density is used.

3.4. Nonuniformity already occurs on E_i at k=1 and P=Q=0. A direct
theta-series calculation gives sector weights approximately
(0.5,0.25,0.25,0), ordered by (sigma,delta)=(00,01,10,11).
The final sector is zero because its odd theta section vanishes at zero.
More generally a degree-one theta section has zeros, so its squared norm
cannot be a positive constant over the abelian variety.

## 4. Flat twists do not provide free point corrections

4.1. Expanding (1) gives an exact translation formula. Put
d_xi=(Omega alpha+beta)/k. Then

    theta_(k,j)^xi(z)
      =exp[pi i*alpha^T Omega alpha/k
               +2 pi i*alpha.(z+beta/k)] theta_(k,j)(z+d_xi).

The Gaussian metrics cancel the modulus of the prefactor, so

    B_k^xi(z)=B_k(z+d_xi).                                  (11)

Identifying matching j basis labels thus interprets the twisted output as
an ordinary level-k evaluation state at the translated point z+d_xi,
up to a phase. It does not turn it into the ordinary state at z.

4.2. Generally d_xi is 2k-torsion but not k-torsion. Translation by it
does not preserve L^k and is outside the level-k theta group. If the
complete linear series is globally basepoint-free, a linear unitary
implementing the same-point correction for every z would imply
t_(d_xi)^*L^k isomorphic to L^k by pulling back O(1), which fails here.
An isometry between differently twisted section spaces is consistent
with this obstruction: it changes the interpreted geometric point.
This argument is not asserted on just the complement of the base locus;
in particular it does not apply to the one-dimensional level-one space.
The present algorithm simply keeps the sector and its twist honest.

## 5. Exact reduction to commuting finite Weyl measurements

5.1. In each level-2k coordinate define X|a>=|a+1> and
Z|a>=exp(2 pi i a/(2k))|a>. On the two input registers put

    G_r=Z_r^k tensor Z_r^k,     H_r=X_r^k tensor X_r^k.

These 2g Hermitian involutions commute: the two single-register signs
from interchanging Z^k and X^k cancel. Formula (4) has G_r eigenvalue
(-1)^sigma_r and H_r eigenvalue (-1)^delta_r. Thus sector readout is
exactly the established simultaneous measurement of these known Weyl
operators, with projector

    Pi_(sigma,delta)=4^(-g) sum_(s,t in {0,1}^g)
        (-1)^(s.sigma+t.delta) G^s H^t.                     (12)

The remaining j,l output is the explicit reversible basis decoding and
phase convention in (4)--(5). At k=1, (12) is the ordinary g-pair Bell
measurement. This is a substantive character-measurement reduction,
not an originality objection based merely on a universal gate set.

5.2. A concrete same classical output is available at k=1. Let D_xi be
the divisor of the unique section of L tensor F_xi. Decide whether

    (P,Q) belongs to mu^*[(D_xi times A) union (A times D_xi)],

promising either w_xi=0 or w_xi>=gamma>0. This is exactly a divisor
incidence bit about P+Q and P-Q. The union also respects the sign ambiguity
of level-two Kummer point coordinates. The event xi has probability w_xi;
O(gamma^(-1) log(1/delta)) fresh input pairs suffice for one-sided error delta.
This geometric interpretation does not change the Bell measurement mechanism.
Moreover, at k=1 each sector is a rank-one maximally entangled projector
on two spaces of dimension d=2^g. Its expectation on a product input is
at most 1/d, by Cauchy--Schwarz applied to the Bell amplitude. Hence
w_xi<=2^(-g). A nonempty positive promise at growing genus requires
gamma<=2^(-g); the displayed direct event is not a constant-probability
algorithm in that regime and can require at least 2^g source pairs.

5.3. A matched comparator even avoids joint measurements across sources.
Choose independent uniform s,t in {0,1}^g. The known observable

    W_(s,t)=i^(k*s.t) Z^(ks) X^(kt)

is a Hermitian involution on a single source. Measure it separately on
the P and Q copies, getting signs x,y. Output the classical number

    (-1)^(s.sigma+t.delta+k*s.t)*x*y.

Its expectation is w_xi by (12); it is bounded by one in modulus.
O(gamma^(-2) log(1/delta)) input pairs estimate the bit's promised margin,
with O(g log(k+1)) quantum input-register size per measurement and O(g)
classical seed bits. This is a protocol with only single-source measurements,
not a classical coefficient-list theorem. It gives no dimension-dependent
copy separation at constant gamma. No optimal gamma lower bound is claimed.
This estimates a fixed sector at additive precision; it neither samples the
whole sector law nor matches the rare-event relative-error dependence.

5.3a. There is a stronger exact parity split. If k is even, Z^k and X^k
commute on each individual source. Jointly measure these known local
observables on each source and XOR their eigenbit strings. The result has
exactly the sector law (12), using one input pair and no joint-source
measurement. This finer measurement may disturb the retained quantum output;
the assertion concerns the complete classical sector string.

If k is odd, the reversible Chinese-remainder index map
a -> (a mod 2,a mod k) sends Z^k to Z on a logical qubit and X^k to X
on that qubit, with identity on the k-dimensional spectator. Apply it to
all coordinates of both sources. Sector readout is exactly a g-pair Bell
measurement on their logical qubits, with spectators ignored. Consequently
the ceiling w_xi<=2^(-g) holds for every odd k: for logical input density
matrices rho,sigma it is 2^(-g) Tr(rho^T V sigma V^dagger) for a known
Pauli V, at most 2^(-g). No claim of efficient copies-only classical Bell
sampling at odd k follows. These are exact operator reductions, including
when each logical subsystem is mixed through entanglement with its spectator.

5.4. A stronger classical sampler is available under a DIFFERENT input
model: sample-and-query access to both normalized coefficient vectors,
each with N=(2k)^g entries.
Sample computational indices a,b independently from their squared amplitudes.
Their common-shift orbit consists of (a+k epsilon,b+k epsilon), epsilon binary.
Every point in this orbit has the same sigma,j,l in (5); only epsilon changes.
For the following exact amplitude formula, enumerate the orbit from the
canonical base ([j+l+sigma]_(2k),[j-l]_(2k)), rather than from the sampled pair.
Query its 2^g product amplitudes c_epsilon and compute their normalized Walsh
transform c_hat_delta. Equation (4) gives the decoded output amplitude

    exp[-pi i*delta.(j+l+sigma)/k]*c_hat_delta.

The phase has no effect on its computational-basis probability. Initial
sampling selects this orbit with probability S=sum_epsilon |c_epsilon|^2.
Sampling delta with probability |c_hat_delta|^2/S therefore produces the
entire decoded output law, including its sector marginal, exactly.
This costs O(g*2^g) arithmetic, O(2^g) coefficient queries and numeric memory,
plus label arithmetic and the stated sampling/query precision costs.
It does not transfer to copies-only input or reproduce the quantum output state.
For a finite-precision dense implementation, consistently approximate each
normalized source vector to O(eta) in Euclidean norm and sample those same
approximations; the resulting output distribution differs by O(eta).
Uniform entry accuracy O(eta/sqrt(N)) is a sufficient conservative choice.

5.5. For dense coefficient lists, after O(N) reading/sampling
preprocessing, the same algorithm costs
O(g*2^g) arithmetic per output. Generic quantum state preparation also
has to charge the coefficient data; at k>=2, g*2^g<=N. At k=1 the Walsh
cost is O(N log N). These bounds prevent treating the cheap circuit after
dense preparation as an automatic exponential time advantage. They do
not assert an optimal classical bound or a copy-only simulation theorem.

## 6. What resources still depend on the period matrix

6.1. Write C_src(eta) for preparation or supplied-copy cost of each
evaluation state in the specified theta basis. A trial costs
2C_src(eta)+O(g*poly(log(k+1),log(1/eta))). For the preceding decision
multiply by O(gamma^(-1)log(1/delta)); sufficient total per-trial error
is O(delta*gamma/log(1/delta)). Source preparation is never replaced by
reading a period matrix. No inverse, amplitude amplification, or free
recovery of consumed source pairs appears in this algorithm.

6.2. If Omega,P,Q are classical inputs instead, their precision, a bound
on lambda_min(Y), and evaluation-state accuracy must be supplied. Direct
theta summation involves a g-dimensional Gaussian lattice sum and a
level-(2k) list of (2k)^g amplitudes. The matrix J does not perform that
work. Normalizing an approximate raw vector also requires error small
relative to its norm sqrt(B); small density is not a free promise.
An abstract polarization without a marked theta basis adds a basis
construction problem, which is likewise absent from the cheap circuit.

6.3. With explicit point and period data, (9) is directly computable by
classical theta evaluation. For a product of fixed elliptic curves all
theta vectors and sector weights factor by coordinate; ordinary scalar
theta sums give the same probabilities. No best-classical claim or
asymptotic advantage is asserted for general coupled Gaussian sums.
Non-product moduli can make the source states complicated while J
continues to factor over index coordinates. A sector-dependent geometric
readout beyond (12) has its own compilation and normalization cost.

6.4. At k=1 an MBQC realization uses ordinary Bell-basis circuitry on
g pairs of input qubits. Cluster preparation, input injection and detector
errors are charged in a physical trial. A full deterministic Bell transform
is not assumed to arise from an unassisted passive-optical analyzer.
This gives a hardware diagnostic of (9), not a new heuristic mechanism.

## 7. Targeted prior art, validation, and disposition

7.1. After deriving (1)--(12), primary PDFs were fetched. Lubicz--Robert,
[arXiv:1001.2016](https://arxiv.org/abs/1001.2016), section 4.2 equation (9),
already express pullback under the sum/difference isogeny as sums of
level-doubled theta tensors; their section 3 treats compatible theta structures.
Gelca--Uribe, [arXiv:1006.3252](https://arxiv.org/abs/1006.3252), equation (2.1),
give the same Gaussian inner-product normalization; equations (2.4)--(2.5)
give the finite Heisenberg action and the Fourier/metaplectic viewpoint.
Our explicit sector projectors identify the applicable known transform.
We do not assert that a noninvertible isogeny itself is literally a single
symplectic matrix modulo 2k; the character register resolves its kernel.

7.2. A 40-second inline numerical probe with one BLAS thread checked
elliptic k=1,2,3 and a coupled genus-two period matrix at k=1,2.
Sixty-four unitarity, translation-density, evaluation, and probability
identities passed. Fifteen wrong normalization, wrong-adjoint, or uniform
sector variants were rejected. A second 30-second probe passed 1,164
checks of Hermitian Weyl signs, sector probabilities and the separate-source
estimator on arbitrary source vectors. The theta series were truncated for the
probe; the analytic proof uses convergent full series and Gaussian integrals.
This is supporting computation, not a registered proof checker.

7.3. The bounded construction is resolved: exact twisted-sector transport
exists, but its mechanism reduces to finite arithmetic and character
measurement, and at k=1 to Bell measurement. General Siegel period matrices
do not escape that reduction. A genuinely different family would need an
explicit correspondence whose normalized section map is not removed by
this known theta/Heisenberg basis decomposition, together with charged
input preparation, a geometric output margin and a matched classical audit.
No such additional lemma or original mechanism is supplied here.
