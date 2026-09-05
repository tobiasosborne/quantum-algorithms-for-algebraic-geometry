# Support-to-Pluecker conversion by measured tableau steering

Author lane, 2026-09-05. This is a constructive mathematical submission;
the independent audit rejects D22 originality. The finite-register task uses
the ordinary Hermitian tensor inner product, explicitly departing from the
polynomial default in convention C1; the local dimension and direct coefficient-state interpretation depart from
C2/C3 as declared in `definitions/support-plucker.md`.
Root owns qaag-j8n and all canonical registers. No shared definitions or claim
statuses are changed here.

The proposed extraction works. A Jucys--Murphy measurement gives an elementary
implementation whose dependence on ambient dimension is logarithmic. A final
exact antisymmetry certificate repairs finite-precision steering: on every
accepted outcome the output is **exactly** the support Slater state. The
certificate has constant acceptance probability on a correctly steered column;
it does not impose a factorial loss. A separate matched transcript proof in
`scouting/support-plucker-classical-r9.md` establishes a copy separation for
the DPP output. The mechanism still fails D22.

## 1. Canonical task and parameters

Use D-SUPPORT-PLUCKER-INPUT, D-SUPPORT-PLUCKER-OUTPUT,
D-SUPPORT-TABLEAU-OPERATORS and D-SUPPORT-STEERING-BUDGET from
`definitions/support-plucker.md`. That file also fixes the always-output
sampling convention and the classical single-copy comparison model.
The failure parameter is restricted to `0<delta<=1/3`. Rank one is trivial.
Claim status lives only in `claims/CLAIMS.md`, C-361--C-364.

## 2. Submitted resource statement

**ASSUME** D-SUPPORT-PLUCKER-INPUT, r >= 2, ideal copies, and a noiseless
finite universal gate model with exact Hadamard, reversible Boolean gates,
and controlled physical permutations. Arbitrary ancilla rotations are
approximated and charged; physical noise in the copies is not covered.

**PROVE** There is a uniform heralded conversion using at most B N input
copies, failure probability at most delta, and exact conditional output
D-SUPPORT-PLUCKER-OUTPUT. A conservative gate bound is

    O(B K^2 N^3 m^2 [w + log^4(KN)]
         + B [r^3 log^2(r+1) + r^2(w+log(r+1))]).                 (2.1)

The logarithmic fourth power allows ordinary Solovay--Kitaev compilation;
no near-optimal rotation synthesis is assumed. Since K = O(N^2 log N),
this is at most

    O(B N^7 log^4 N [w + log^4 N]).                             (2.2)

The first expression also absorbs the O(B A M w) physical swaps used for
steering. Quantum storage can be bounded by

    O(N w + r^2 log^2(r+1) + log N),                            (2.3)

with O(N log N) classical tableau storage and polynomial classical circuit
generation and feedback computation. The deliberately crude exponents in
(2.1) are an existence bound, not an implementation-performance claim.
There is no inverse output-accuracy parameter: exact certification replaces
an approximation guarantee on accepted states. The result is q-efficient,
with source budget O((r^2/eta) log(1/delta)).

## 3. Probability of obtaining r rows

**3.1 ASSUME** D-SUPPORT-PLUCKER-INPUT and an ideal weak Schur measurement of
N copies. **PROVE** Its shape has exactly r rows with probability at least
one half at the stated N.

**3.2** In a diagonal eigenbasis, Schur--Weyl duality gives

    Pr(lambda) = dim(V_lambda) s_lambda(theta_1,...,theta_r).

The same formula is the RSK shape law of an independent length-N word on
letters 1,...,r with respective probabilities theta_1,...,theta_r. Indeed,
RSK is a weight-preserving bijection to a semistandard insertion tableau
and a standard recording tableau of common shape: summing insertion weights
gives the Schur polynomial and counting recording tableaux gives dim(V_lambda).

**3.3** Use row-weak, column-strict insertion. The number of rows is the
length of a longest **strictly decreasing** subsequence. Thus no shape has
more than r rows, and any occurrence of r,r-1,...,1 as a subsequence forces
exactly r rows. Repeated identical letters are not a decreasing subsequence.

**3.4** Starting at the beginning of an infinite word, wait for r, then
r-1, and so on. The waiting increments have geometric means 1/theta_a;
the memoryless independent word justifies using the same distribution after
each stopping time. If T is their sum, then

    E T = sum_a 1/theta_a <= r^2/eta.

Markov gives Pr(T > N) <= E T/N <= 1/2. Therefore
Pr(number of rows = r) >= Pr(T <= N) >= 1/2. Integer rounding in N only
improves the bound. This argument does not require the eigenvalues to be
ordered by magnitude: their letter order is arbitrary.

## 4. Explicit q-efficient nondemolition instruments

**4.1 ASSUME** D-SUPPORT-TABLEAU-OPERATORS. **PROVE** The tableau can be
measured while preserving the whole Q_lambda(H) factor, with the resources
charged in section 2.

**4.2 Governing representation identities.** The self-adjoint X_k commute
and satisfy

    X_k E_b = c_b(k) E_b,           -(k-1) <= c_b(k) <= k-1.      (4.1)

The content sequence determines b. Given a partial diagram, its addable
boxes have distinct contents, so each next content locates the new box.
In particular, the joint spectral projector for a full content sequence is
E_b, not a rank-one projector on the physical space. These standard
representation identities, including the branching multiplicity one and
Young's orthogonal form used below, are established in sections 3--7 of
[Vershik--Okounkov, arXiv:math/0503040](https://arxiv.org/pdf/math/0503040).

**4.3 Exact ideal content extraction.** Let R = 2^m >= 2N. Perform m-bit
phase estimation for exp(2 pi i X_k/R). The eigenphases are exactly the
integers c_b(k) modulo R, divided by R. Hence there is no phase-resolution
tail in the ideal circuit. Writing Pi_{k,c} for the content projector, the
unitary W_k acts on its initially zero ancillas as

    W_k (|0> tensor psi) = sum_c |c mod R> tensor Pi_{k,c} psi.  (4.2)

The signed interval in (4.1) uniquely decodes the residue. Phase estimation
here is explicitly compiled below; exp(i t X_k) is not an input oracle.

**4.4 The instrument is Lueders.** Apply W_k, copy its content label to a
fresh output register by CNOTs, apply W_k inverse, and measure only the
copied label. On any psi this gives

    psi -> sum_c |c> tensor Pi_{k,c} psi,
    outcome c: sigma -> Pi_{k,c} sigma Pi_{k,c}.                 (4.3)

All original work ancillas return to zero in the ideal circuit. Therefore
no unresolved Fourier matrix index is traced out. Measuring k = 2,...,N
in this way gives a known tableau and preserves Q_lambda(H).

**4.5 Literal weak shape projectors, if desired.** Coherently run content
extraction for all indices up to a prefix, compute that prefix's shape
reversibly, copy only the shape, and uncompute the shape arithmetic and all
content extraction. Because all X_k commute, the resulting Kraus operators
are exactly the prefix isotypic projectors. Thus a nondemolition weak Schur
measurement can also be compiled this way. The algorithm below instead
measures successive contents directly because a full tableau is wanted.
Its cost is lower than reconstructing every prefix projector separately.

**4.6 Elementary controlled swap exponentials.** For a transposition S,
use an ancilla a initialized to zero and let

    F = H_a controlled_a(S) H_a.

On an S-eigenvector with eigenvalue +1 or -1, F writes that sign as the
bit 0 or 1. Consequently

    F exp(i t Z_a) F (|0> tensor psi)
                       = |0> tensor exp(i t S) psi.             (4.4)

For a controlled exponential, control only the middle phase on the phase
estimation control bit. Each exponential uses two controlled physical
transpositions and ancilla gates. A physical transposition of two w-qubit
registers is w Fredkin gates. No operation on a computational coordinate
table of size q occurs.

**4.7 Product formula.** The controlled times in W_k are
t_j = 2 pi 2^j/R, 0 <= j < m, hence 0 < t_j <= pi. For h = k-1 and
integer L, replace exp(i t X_k) by

    [ product_{i=1}^{k-1} exp(i t S_ik/L) ]^L.                  (4.5)

The first-order unitary product-formula estimate, obtained by integrating
the two-factor commutator identity and telescoping, is

    ||exp(i t X_k) - (4.5)||
       <= (t^2/(2L)) sum_{i<j} ||[S_ik,S_jk]||
       <= t^2 h^2/(2L).                                      (4.6)

Here each transposition has norm one, so every commutator has norm at most
two. The same bound holds for controlled versions. With the value L in
D-SUPPORT-STEERING-BUDGET, the accumulated product-formula error across the
m controlled powers is less than nu/2. There are O(m L N) elementary
swap exponentials per W_k. The inverse Fourier transform on m ancillas
uses O(m^2) Hadamards and controlled phases; its usual binary circuit is
independent of q.

**4.8 Finite gate precision.** Approximate every ancilla phase appearing
in this circuit to operator error at most nu/(4 G_0), where
G_0 = O(m L N + m^2) is a concrete upper bound on the number of phase
gates. Standard single-qubit Solovay--Kitaev synthesis and the elementary
controlled-phase decomposition cost O(log^4(G_0/nu)) gates per phase.
All physical data gates remain exact controlled permutations. A hybrid
bound gives a coherent W_k approximation of operator error at most nu.
This statement includes all its work registers, and its implemented inverse
is the literal adjoint of the implemented circuit.

**4.9 Error of the retained-register instrument.** Replacing W_k and its
inverse in (4.3) by these circuits changes the coherent instrument by at
most 2 nu in operator norm, and its channel by at most 4 nu in diamond
norm. Therefore any adaptive circuit using at most K such instruments
has full classical-quantum output trace distance at most

    4 K nu = 1/64                                             (4.7)

from its ideal version. The constant is conservative. Padding terminated
branches by identities makes the ordinary adaptive hybrid argument apply.
This comparison includes failures and all transcripts, not only a
postselected normalized state. Multiplying O(m L N) by 2K, substituting
L = O(m N^2 K), and charging synthesis proves the first term of (2.1).

**4.10 Exact support preservation despite approximation.** Every gate
touching data is a controlled permutation. It commutes with P_U^tensor N
even when controlled by arbitrarily imperfect ancilla states. Ancilla gates,
measurements, and discards therefore preserve U^tensor N exactly. This
structural fact, rather than an approximate support promise, is used for
the exact final certificate in section 7.

## 5. Steering a known tableau to a column-first tableau

**5.1 ASSUME** An ideal content-measurement transcript b of shape lambda
with exactly r rows. **PROVE** At most M adjacent moves suffice, each with
success probability at least 3/4 per attempt and an exact reset on failure.

**5.2 Target construction and path.** Let b0 list boxes column by column,
each column from top to bottom. It is a linear extension, and its first r
boxes form the first column. To transform the current linear extension to
this target, fix target positions from left to right: locate the required
box later in the current order and bubble it left to its target position.
Every box crossed is incomparable with it. Otherwise their two orders
could not occur in the current and target linear extensions. Thus every
crossing is a valid adjacent-number swap of standard tableaux. The total
is the inversion distance between the two lists, at most N(N-1)/2 = M.
The path can be generated with O(N log N) classical storage.

**5.3 One physical move.** Suppose b' = s_k b is standard, with s_k the
transposition of labels k and k+1. Set d = c_b(k+1)-c_b(k). Incomparable
boxes are northeast/southwest of each other; their contents differ in
absolute value by at least two. Young's orthogonal form gives, up to an
irrelevant choice of basis phases,

    T(s_k)|b> = (1/d)|b> + sqrt(1-1/d^2)|b'>.                 (5.1)

Only these two tableau coordinates occur. This identity acts as the
identity on Q_lambda(H). Their kth contents are distinct, so measuring X_k
distinguishes them. On b' the move succeeds with probability 1-1/d^2 >= 3/4;
on b it fails with probability 1/d^2 <= 1/4.

**5.4 Mixed states and repeated failures.** Conditional on the complete
initial tableau, any physical state has the form

    tau tensor |b><b|                                        (5.2)

inside its Schur summand, with tau possibly mixed. In fact rho^tensor N
already has the form direct_sum_lambda rho_lambda tensor identity_{V_lambda}.
The two outcome Kraus operators in the two-dimensional tableau span are
scalar multiples of the identity on tau. After a failed move the normalized
state is precisely (5.2), so it can be retried on the same N source copies.
The success branch is tau tensor |b'><b'|. This is not fresh-copy
postselection and is not restricted to a pure highest-weight vector.

**5.5 Capping.** A prescribed move fails all A attempts with probability
at most 4^{-A}. Union bounding over at most M moves gives at most
M 4^{-A} <= 1/4 for steering failure conditional on any input tableau.
If an approximate transcript is not a valid tableau, or a later content
outcome is neither of the two expected values, the implemented protocol
declares batch failure. This is an ordinary deterministic feedback rule;
the ideal comparison is covered by (4.7).

## 6. Why column extraction gives exactly the support Slater state

**6.1 ASSUME** The physical state is supported on U^tensor N and its
tableau is b0. **PROVE** The first r registers factor as the pure state
Omega_U for every mixed state in this branch.

**6.2** The restriction of the path to S_r has diagram (1^r), its sign
representation. Thus every permutation pi of the first r systems acts
there as sign(pi); equivalently P_-^{(r)} is the identity on this branch.
All its vectors belong both to U^tensor N and to
(wedge^r H) tensor H^tensor(N-r). These projectors commute, and their
intersection is

    (wedge^r U) tensor U^tensor(N-r).

Because dim U = r, the first factor has dimension one. Any positive
operator supported on that tensor product has the form

    |Omega_U><Omega_U| tensor sigma_rest.                     (6.1)

This proves exact factorization without assuming purity of the whole
Schur branch. Discarding the remaining registers returns the requested
Slater ray. Its possible determinant phase depends on the arbitrary
basis of U and has no observable effect.

## 7. An exact certificate with constant normalization

**7.1 ASSUME** An arbitrary, possibly badly steered, batch state still
supported on U^tensor N. **PROVE** An elementary finite circuit accepts
only the exact state (6.1), and has acceptance at least 1/4 on a perfect
column. This removes finite-precision error from the accepted output.

**7.2** Set a = ceil(log_2(r!)) and h = 2^a. Prepare an a-bit label x in
|+>^tensor a. Reversibly compute the flag x < r!. On valid labels, compute
a bijective factoradic unranking x -> pi_x in S_r and implement
sign(pi_x) T(pi_x) on the first r systems. Uncompute the unranking work,
leaving x and the validity flag. Accept only if the validity flag is one
and measuring x in the Hadamard basis gives all zeroes. The data Kraus
operator is exactly

    C_r = (1/h) sum_{x=0}^{r!-1} sign(pi_x) T(pi_x)
        = (r!/h) P_-^{(r)} = gamma_r P_-^{(r)},                (7.1)

where 1/2 < gamma_r <= 1. The acceptance probability on a data state
sigma is gamma_r^2 Tr(P_-^{(r)} sigma). The lower bound is strictly above
1/4 on an ideal column, and one may safely use the weak bound 1/4.

**7.3 Exact compilation.** The factoradic digits d_j in {0,...,j-1},
2 <= j <= r, are obtained by successive integer divisions. The sequence
of swaps (j,d_j+1) bijects these tuples with S_r. For each stage, loop over
possible digit values, compute the equality flag, condition the physical
swap on it, and uncompute that flag. A nontrivial swap contributes a
phase -1. Therefore the entire permutation and sign use exact reversible
Boolean gates, phase signs, and controlled swaps. The label contains only
O(r log(r+1)) bits; no table with r! entries is stored. Elementary
reversible schoolbook arithmetic gives the conservative time bound
O(r^3 log^2(r+1)) and work bound O(r^2 log^2(r+1)). The permutation part
uses O(r^2(w+log(r+1))) gates. Hadamards and the two final measurements are
exact. No arbitrary rotation is needed in this certificate.

**7.4** By (4.10), every implemented batch reaching this certificate is
still supported on U^tensor N. On acceptance, (7.1) places it in the
intersection from section 6, which has the one-dimensional first factor
wedge^r U. Therefore every accepted state is exactly Omega_U, even if
the approximate phase-estimation labels were wrong. The certificate can
reject and consume a batch, but cannot certify a wrong state under the
exact rank/input-support promise.

**7.5 Why no factorial success penalty appears.** The coherent group
average is already normalized as a projector. Its padded implementation
has amplitude gamma_r > 1/2, not 1/sqrt(r!) or 1/r!. Applied directly to
r independent flat-support copies, it still accepts with the small input
overlap Tr(P_- rho^tensor r) = r^{-r}; the certificate does not solve that
seed problem alone. Steering first raises this overlap to one in each
ideal successful branch, which is why its last use costs a constant.

## 8. Overall success, copies, and classical readout

**8.1 One batch.** Acquire N fresh copies. Obtain the tableau by content
measurements and reject unless it has r rows. Follow the path in section 5,
with A attempts per move. If steering finishes, apply the exact certificate.
In the ideal comparison circuit, the probability of reaching a correct
column is at least (1/2)(3/4) = 3/8. Including the certificate, acceptance
is at least 3/32. By (4.7), the implemented circuit's acceptance is at
least 3/32 - 1/64 = 5/64, hence at least 1/16.

**8.2 Independent repetitions.** Run at most B batches and return the
first accepted output. Fresh independent source copies and reset ancillas
give failure probability at most

    (1-1/16)^B <= exp(-B/16) <= delta.

The number of source copies is bounded by B N on every branch. Regardless
of which batch accepts, its quantum output is exactly Omega_U, so taking
the first success does not bias that output. Expected source consumption
without a cap is at most 16 N. No copies of intermediate postselected
states are requested.

**8.3 Classical output identity.** Let V be the q by r isometry with
columns u_1,...,u_r, only for this proof. For any ordered tuple of distinct
coordinates (j_1,...,j_r), the Omega_U amplitude is the corresponding
minor of V divided by sqrt(r!), with the order-dependent sign. Sorting
combines exactly r! equiprobable orderings. Therefore

    Pr(J) = |det V[J,:]|^2 = det(P_U[J,J]).                    (8.1)

Tuples with repeated coordinates have zero amplitude. Cauchy--Binet gives
sum_{|J|=r} det(P_U[J,J]) = det(V^* V) = 1. This is the normalized rank-r
projection DPP, with no omitted factorial. Readout uses r w measured bits
and polynomial-time classical sorting; V is not computed by the algorithm.
If all B batches fail, output any fixed size-r subset J_0 to obtain an
always-output sampler. Its unconditional TV error is at most delta,
matching the interface of the independent classical lower bound.

## 9. Bounded author diagnostics

These are auxiliary executable numerical/combinatorial diagnostics, not a
replacement for the preceding proof or an independent referee verdict.
They were run by bounded inline Python 3 commands; no checker files or
shared files were created. Every diagnostic exits nonzero on a violated
threshold or identity.

**9.1 Rank two, q = 3, N = 3.** A seeded random complex isometry V with
two columns defines rho = VV^*/2. On the 27-dimensional tensor space set

    P_21 = [2 identity - S_12 S_23 - S_23 S_12]/3,
    E_b0 = P_21 (identity-S_12)/2,
    E_b  = P_21 (identity+S_12)/2.

The six checked statements were: shape (2,1) mass 1/2; initial b0 mass
1/4; mass 3/16 transferred from b to b0 by S_23 and measurement; failed
branch exactly one quarter of its pre-attempt state; normalized partial
trace exactly the Slater projector; and [X_2,X_3] = 0. Maximum numerical
residual was 1.23e-16 against a 1e-10 failure threshold. One capped attempt
therefore yields an ideal column with total mass 1/4+3/16 = 7/16; unlimited
feedback reaches the full shape-(2,1) mass 1/2. Direct two-copy
antisymmetrization instead has mass 1/4 on this input. This comparison
checks the mechanism and is not a sufficient classical baseline.

**9.2 All small tableaux.** Exhaustive growth generated all 1115 standard
tableaux of sizes one through eight. Column-order bubble steering performed
5235 swaps. Every intermediate tableau was standard, every moved pair had
absolute content difference at least two, every path had at most N(N-1)/2
moves, and every endpoint began with its first column.

**9.3 Certificate indexing.** Exhaustive factoradic tuples for r = 2,...,7
gave exactly r! distinct permutations, the computed phase agreed with
inversion parity in every case, and the padding normalization satisfied
1/2 < r!/2^ceil(log_2(r!)) <= 1.

**9.4 Rank three, q = 4 certificate.** A second seeded random complex
isometry gave an explicit 64-dimensional check of C_r^* C_r = gamma_r^2
P_-^{(r)}, the flat-copy acceptance gamma_r^2/r^r = 1/48, the exact
normalized Slater projector on that accepted branch, and acceptance
gamma_r^2 = 9/16 on an already correct column. Maximum residual was
1.08e-15 against the same 1e-10 failure threshold.

## 10. Targeted source check and limits of this submission

The construction above was derived before targeted source checks. The
representation-theory source linked in section 4 was fetched as its full
arXiv PDF. Its content-spectrum and adjacent-transposition results are
standard ingredients, not an originality claim.

[Bacon--Chuang--Harrow, arXiv:quant-ph/0407082](https://arxiv.org/pdf/quant-ph/0407082)
was also fetched as a full PDF, including Fig. 3 and Eq. (11). Its generalized
phase estimation exposes the original symmetric-group basis coordinate in
an ancilla while preserving the unitary-group factor. As the independent
critic observed, reading and resetting that exposed coordinate to b0,
then reversing the circuit, implements the same tableau-factor reset.
Only controlled permutations touch the data, so adding section 7's exact
certificate preserves the exact accepted-output guarantee even with
ancilla Fourier approximation. The paper explicitly gives logarithmic
local-dimension dependence for this representation-processing circuit.
Thus the full proposed conversion substantively reduces to a described
quantum operation. The explicit elementary compilation here remains a valid
resource proof, but the mechanism fails D22; see the
[independent audit](../verdicts/support-plucker-r9.md).

The primary record of
[Brahmachari--Hulse--Pfister--Marvian, arXiv:2508.05046](https://arxiv.org/abs/2508.05046)
was fetched: its title and abstract describe qubit purification and unitary
Schur sampling through random SWAP tests. This is a targeted overlap lead
for the independent novelty audit. The exact-channel reduction above is
already sufficient to reject D22 without asserting that this separate
qubit paper states the growing-r support problem. No new citation was added
to the canonical refs directory.

The theorem is restricted to an exactly rank-r input and collective access
to its quantum copies. It does not compare against a classical algorithm
given an explicit basis, coefficient list, or sample-and-query matrix access.
The independent transcript proof and
`verdicts/support-plucker-r9.md` address arbitrary adaptive single-copy
POVMs for the same always-output DPP task, retaining all block coherence.
They give an Omega(sqrt(q)) copy lower bound on a rank-two family at fixed
TV accuracy; this does not transfer to the different access models just
listed. The independent verdict section 3.5 gives a small hardware diagnostic.

## 11. MERGE PROPOSAL for root and independent critic

The submitted mathematical statements are: the r-row probability bound in
section 3; the explicitly compiled, nondemolition tableau instrument in
section 4; recyclable feedback steering and mixed-state column factorization
in sections 5--6; and exact heralded support-to-Pluecker/DPP conversion with
the complete resource cap in sections 7--8. Canonical definition IDs are
linked in section 1. None is promoted to a canonical claim status by
this lane. A referee should check the instrument-level hybrid bound, exact
support preservation under gate synthesis, and the padded certificate's
Kraus normalization before approving integration. The independent critic
has reported that these checks pass. Originality is rejected under D22 by
the separate mechanism audit; the same-input classical baseline and
north-star qualification remain separate obligations.
