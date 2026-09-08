# Growing-rank syzygy generator-basis extraction without a QFT

2026-09-08. R13 construction memo under D25. This is a proposed growing-rank
extension of the independently accepted rank-two source-only theorem. It uses
QSVT spectral reflections of Jucys--Murphy operators; QSVT is eligible under
D25. No QFT, Grover search or DQI occurs. Canonical status belongs only in the
shared claim register. Independent review has converged: C-377--C-381 are
PROVED under the canonical definitions in `definitions/syzygy-basis-r13.md`.
The original proposal/merge wording below is retained as derivation history.

The principal output is useful but narrow: select `r` original labelled forms
which minimally generate a fixed fat-point ideal. The access is independent
copies of an unknown flat support state. It is not a coefficient-list algorithm,
and the one-time source-device construction may dominate wall-clock time.

## 1. Geometry, source and exact output

### 1.1 A redundant presentation of a fat point

Fix `r>=3`, `q>=r`, and write `e=r-1`. In
`R=C[z_0,z_1]`, let

`g_i=z_0^(e-i) z_1^i/sqrt((e-i)! i!)`, `0<=i<=e`.                    (1)

These are the `r` Fock-orthonormal monomials of degree `e`. Let `C` be an
unknown `r x q` row coisometry,

`C C^dag=I_r`,                                                       (2)

and define the based tuple

`f_a=sum_(i=0)^(r-1) C_(ia) g_i`, `1<=a<=q`.                         (3)

The forms span `R_e`, so their homogeneous ideal is

`I_C=(z_0,z_1)^e`.                                                   (4)

The affine quotient has basis the monomials of degree below `e`, and hence

`length R/I_C=sum_(j=0)^(e-1)(j+1)=r(r-1)/2`.                        (5)

For `r>=3` this is a nonreduced fat point at the origin. Its projectivization
is empty and is not advertised as a nonempty projective variety.

The constant syzygy space of the based presentation is

`K=ker C subset C^q`, `dim K=q-r`;                                   (6)

its orthogonal complement is `U=range(C^dag)` with projector
`P_U=C^dag C`. A size-`r` label set `J` selects a minimal generating subtuple
exactly when

`det C[:,J] != 0`.                                                   (7)

Indeed, (7) says the selected forms are a basis of `R_e`; any such basis
generates (4), and fewer than `r=dim R_e` degree-`e` forms cannot do so.
Equivalently the complementary Plücker coordinate of `K` is nonzero. This is
a based-presentation reduction problem, not an invariant of the already fixed
bare ideal.

### 1.2 The emitter has success one

At Macaulay and emitter degree `N=e`, the coefficient matrix
`F_e:C^q->R_e` is `C` in the bases (1). Since annihilation by a degree-`e`
form maps `R_e` to constants, the bath-emission map is

`V=sum_a |a><f_a|=C^dag:C^r->C^q`.                                  (8)

Equation (2) gives `V^dag V=I_r`: no contraction scaling or failure Kraus
operator is needed. On the fixed maximally mixed Fock input `I_r/r`,

`V(I_r/r)V^dag=P_U/r=:rho_C`, `Tr rho_C=1`.                          (9)

Thus one raw emitter call delivers one source copy. The device implementing
the unknown isometry `C^dag` has construction cost `B_source(q,r)` and each
delivery costs `C_source(q,r)`; neither is free. The theorem's data interface
supplies only independent copies of (9). It supplies no coefficient list,
purification, preparation inverse, controlled emitter, support basis or
hidden-partition metadata.

### 1.3 Useful common output and comparator

Always output a sorted set `J subset [q]`, `|J|=r`. Success means (7). Require
success at least `2/3` for every row coisometry `C`.

The classical comparator receives the same copies of (9), may perform an
arbitrary POVM on each whole `q`-dimensional source register, choose later
POVMs adaptively using unlimited classical computation and memory, and has a
fixed total source-copy cap `T`. It retains no quantum memory between original
copies. Every consumed/discarded copy counts. Coefficient access or a coherent
multi-copy memory is a different model.

The labels identify original available constraints. A successful output is a
minimal set of those constraints defining the same ideal, so the task directly
performs redundant-generator reduction. It does not output the `q-r`
dimensional syzygy basis or the coefficients of the retained forms.

## 2. An exact growing-rank separate-copy lower bound

### 2.1 Hidden balanced partitions

Let `q=rd`, with `d>=2`. Choose a uniformly random labelled balanced partition

`[q]=S_1 disjoint-union ... disjoint-union S_r`, `|S_j|=d`.           (10)

Conditional on this partition, choose independent Haar unit vectors `u_j`
supported on `S_j`, fixed for the whole transcript, and take the rows of `C`
to be `u_j^dag`. Their disjoint supports make (2) automatic. With probability
one, every coordinate of each `u_j` is nonzero. A label set `J` satisfies (7)
exactly when it is a transversal of (10).

The partition and vectors are not public. If (10) were supplied, a classical
algorithm would return one element of each block with no source copies.

### 2.2 Common transcript mass

Fix any adaptive separate-copy strategy and a complete rank-one-refined leaf
of its `T`-copy transcript. After conditioning on earlier outcomes, the leaf
fixes all measurement vectors; adaptivity causes no extra dependence on the
hidden source.

For one Haar vector in `C^d`, the squared norm of a homogeneous holomorphic
polynomial of degree `L` under Haar measure is at least

`[d/(d+L-1)]^L`                                                       (11)

times its norm under a circular Gaussian vector of coordinate variance `1/d`.
Decompose the leaf polynomial by its degrees `L_1,...,L_r` in the independent
groups. Since `sum_j L_j=T`, multiplying (11) and using `L_j<=T` gives the
uniform lower factor

`c_T=[d/(d+T-1)]^T`.                                                  (12)

The Gaussian Fock product inequality then lower-bounds the product moment by
the product of the one-copy moments. Each source has Gaussian first moment

`(1/r)sum_j I_(S_j)/d=I_q/q`,                                        (13)

independent of the partition. Therefore, leaf by leaf and hence as measures,

`P_S >= c_T P_*`,                                                     (14)

where `P_*` is the transcript law of the same strategy on independent copies
of `I_q/q`. The reference is common to every balanced partition. Equivalently,

`P_S=c_T P_*+(1-c_T)Q_S`                                             (15)

for a probability law `Q_S`. Finally Bernoulli's inequality gives

`1-c_T<=T(T-1)/d`.                                                    (16)

This is the `r`-group extension of the already audited rank-two
Haar/Gaussian transcript argument. It is a full adaptive-transcript bound, not
a comparison only of one-copy averages.

### 2.3 Transversal probability and copy lower bound

A fixed set of `r` distinct labels is a transversal of a uniformly random
balanced labelled partition with probability

`a_(r,d)=r! d^r/(rd)_r`,
`(rd)_r=(rd)(rd-1)...(rd-r+1)`.                                      (17)

One proof counts all balanced partitions and those assigning the fixed labels
bijectively to the `r` blocks. On the common component (15), the algorithm's
output is independent of the hidden partition, so it succeeds with probability
exactly (17). The residual component succeeds with probability at most one.
Uniform success at least `2/3` therefore implies

`2/3<=c_T a_(r,d)+(1-c_T)`,
`1-c_T>=[2/3-a_(r,d)]/[1-a_(r,d)]`.                                  (18)

Combining (16)--(18) proves

`T(T-1)>=d [2/3-a_(r,d)]/[1-a_(r,d)]`.                               (19)

The right side is order `d=q/r`, so the copy lower bound is
`Omega(sqrt(q/r))`, not `Omega(q/r)`.

For a simple uniform constant, `a_(r,d)` decreases with `d`. At `d=2`,

`a_(r,2)=2^r/binom(2r,r)`.                                           (20)

The ratio of consecutive terms is `(r+1)/(2r+1)<1`, so for `r>=3,d>=2`,

`a_(r,d)<=a_(3,2)=2/5`.

Consequently (19) yields the convenient bound

`T(T-1)>=4d/9=4q/(9r)`.                                              (21)

All inequalities concern a fixed total cap and worst-case uniform success.
They do not lower-bound expected copies of an unbounded stopping strategy.

## 3. Support-to-Slater strategy

The quantum algorithm first converts copies of `rho_C=P_U/r` into the support
Slater ray

`Omega_U=(r!)^(-1/2) sum_(pi in S_r) sign(pi)
                 u_(pi(1)) tensor ... tensor u_(pi(r))`,              (22)

for any orthonormal basis of `U`. Coordinate measurement of (22), followed by
sorting, has probability

`Pr(J)=det(P_U[J,J])=|det C[:,J]|^2`.                                (23)

Every outcome of positive probability satisfies (7). Thus a heralded Slater
converter, followed by coordinate measurement, solves the useful selection
problem whenever it accepts; no prescribed DPP approximation is required.

The measured-tableau steering proof from the prior support-conversion theorem
uses only these facts:

1. With `N=ceil(2r^2)` flat-rank copies, weak Schur measurement has a shape
   with exactly `r` rows with probability at least `1/2`. This follows by the
   RSK word law and waiting for the subsequence `r,r-1,...,1`.
2. A complete Young-tableau content sequence can be steered by at most
   `M=N(N-1)/2` valid adjacent swaps to the column-first tableau. Young's
   orthogonal form gives success at least `3/4` per attempted adjacent move;
   on ideal failure the same tableau state is restored and can be retried.
3. Once the first `r` boxes form a column, the first `r` data registers factor
   exactly as (22). A final exact antisymmetry certificate removes every
   finite-precision false accept.

The next sections replace the earlier inverse-Fourier content measurement by
an explicit QSVT Lüders instrument and account for its retries and errors.

## 4. Exact block encoding of a Jucys--Murphy operator

On `N` source registers let

`X_k=sum_(i=1)^(k-1) S_(i,k)`, `2<=k<=N`,                             (24)

where `S_(i,k)` swaps the complete `w=ceil(log_2 q)`-qubit data registers.
Its content eigenvalues are integers in `[-(k-1),k-1]`, and the commuting
family `X_2,...,X_N` labels the Young branching basis.

Set

`alpha_k=2^ceil(log_2(k-1))`, `k-1<=alpha_k<2(k-1)`.                  (25)

Prepare a uniform `alpha_k`-label register by Hadamards. For labels
`i<k-1`, SELECT applies `S_(i+1,k) tensor I_signal`. For padded labels it
applies `I_data tensor X_signal`. In full,

`SELECT_k=sum_(i<k-1)|i><i| tensor S_(i+1,k) tensor I`
`       +sum_(i>=k-1)|i><i| tensor I tensor X`.                       (26)

Every summand is a Hermitian involution on an orthogonal label block, so
`SELECT_k=SELECT_k^dag` and `SELECT_k^2=I`. Let `PREP_k` be Hadamards on the
power-of-two label bank and define

`U_(X,k)=(PREP_k^dag tensor I) SELECT_k (PREP_k tensor I)`.           (27)

This is again a Hermitian involution. With signal projector onto the joint
zero label and zero padding-signal ancillas, its projected block is exactly

`A_k=X_k/alpha_k`.                                                    (28)

One query costs

`C_X(k)=O(k[w+log k])`                                                (29)

elementary gates under a direct multiplexed implementation: equality logic
plus at most `k-1` controlled register swaps. Every gate touching the source
data is a controlled permutation.

The power-of-two padding is real normalization; the spectral separation in
(28) is `1/alpha_k=Theta(1/k)`, rather than one. More importantly,
`(U_(X,k),Pi_0)` is a Hermitian projected-unitary encoding. The later
polynomial transformation therefore acts on the signed eigenvalues of `A_k`.
A generic rectangular block encoding would transform singular values and would
not implement the required content thresholds.

## 5. QSVT reflection for one integer content window

### 5.1 Two threshold signs

For an integer `c in [-(k-1),k-1]`, put

`t_-=(c-1/2)/alpha_k`, `t_+=(c+1/2)/alpha_k`.                         (30)

On the spectrum of `A_k`, define

`R_(k,c)=-sgn(A_k-t_- I) sgn(A_k-t_+ I)`.                            (31)

Every eigenvalue is an integer divided by `alpha_k`; hence (31) is `+1`
exactly on content `c` and `-1` on all other content spaces. Thus

`R_(k,c)=2 Pi_(k,c)-I`,                                              (32)

where `Pi_(k,c)` is the exact content projector. Thresholds beyond the
spectral edge can be replaced by the appropriate constant sign.

To implement a nonconstant threshold, use a second explicitly Hermitian LCU.
For a threshold `t`, prepare a selector qubit by a rotation `P_t` satisfying

`P_t|0>=sqrt(1/(1+|t|))|0>+sqrt(|t|/(1+|t|))|1>`,

and set

`SELECT_t=|0><0| tensor U_(X,k)+|1><1| tensor[-sgn(t)I]`,
`U_(Y,t)=(P_t^dag tensor I)SELECT_t(P_t tensor I)`.                   (33)

For `t=0` omit the identity branch. Both SELECT terms are Hermitian
involutions, so `U_(Y,t)` is a Hermitian involution. Its all-zero projected
block is

`Y_t=(A_k-tI)/(1+|t|)`.                                              (34)

This LCU has normalization `1+|t|<=5/2` and one selector rotation. Its spectrum
is separated from zero by at least `1/(5alpha_k)`. The coefficient rotation,
QSVT phase rotations and their synthesis accuracy are charged.

Because (33)--(34) are Hermitian projected-unitary encodings, qubitization and
Hermitian eigenvalue transformation implement an odd polynomial of the signed
eigenvalues of `Y_t`; they do not replace `Y_t` by `|Y_t|`. An odd
sign-approximating polynomial of degree

`D_(k,xi)=O(alpha_k log(1/xi))`                                      (35)

on each shifted block gives the two signs. Here is the clean-space error
explicitly. If `p` is bounded by one and
`|p(lambda)-sgn(lambda)|<=zeta` on the spectrum, the clean projected component
has operator error at most `zeta`, while the orthogonal signal leakage on a
unit vector is at most

`sqrt(1-(1-zeta)^2)<=sqrt(2zeta)`.                                   (36)

Take `zeta<=xi^2/64`, use separate clean work registers for the two signs, and
retain every leakage register. The sequential signs and minus phase then give
a QSVT isometry within `xi` of the clean ideal action (31). The logarithm of
`1/zeta` is still `O(log(1/xi))`, so (35) is unchanged. No
operator-norm-optimal projector dilation or free ancilla reset is assumed.

The parity condition is explicit: the sign polynomials act on the shifted
Hermitian blocks (34) and are odd. The two parities needed by the affine LCU
are carried by its selector ancilla; no arbitrary non-parity polynomial is
silently passed to QSVT.

### 5.2 Approximate binary Lüders test

Given a controlled implementation of the approximate reflection, prepare a
test qubit in `|+>`, control the reflection, apply a Hadamard and measure. In
the ideal case its Kraus maps are

`K_yes=(I+R_(k,c))/2=Pi_(k,c)`,
`K_no =(I-R_(k,c))/2=I-Pi_(k,c)`.                                   (37)

An operator/Stinespring error `xi` in the controlled clean-space reflection changes this
two-outcome instrument by at most `2xi` in diamond norm. All work ancillas and
leakage flags are included in this bound; they cannot be discarded and called
an ideal Lüders measurement.

One test uses two sign filters, hence

`C_win(k,xi)=O(D_(k,xi)[C_X(k)+log^4(D_(k,xi)/xi)])`                 (38)

elementary gates with conservative Solovay--Kitaev synthesis. This is

`O(k^2(w+log k) log(1/xi)+k log^5(1/xi))`.                           (39)

Classical polynomial-time QSVT phase generation at the stated precision is
part of the compiler; a list of optimal phase angles is not an oracle.

## 6. The padded window-bank Lüders instrument

### 6.1 Exact bank channel

There are `J_k=2k-1` possible integer labels. Set

`H_k=2^ceil(log_2 J_k)`, `J_k<=H_k<2J_k<4k`.                         (40)

One bank trial chooses `c` uniformly from the `H_k` labels. Valid labels use
(37); padded labels use `Pi_(k,c)=0`, so their exact reflection is `-I` and
they always return `no`. The choice can be made by exact Hadamards followed by
measurement and classical feed-forward. A fully coherent bank would require a
PREPARE of the same `log H_k` Hadamards and a SELECT over the `c`-dependent
QSVT phases; a naive SELECT costs `O(H_k C_win)` and is neither needed nor
claimed.

For a valid label, the CP maps of one random trial are

`S_c(rho)=Pi_c rho Pi_c/H_k`,
`F_c(rho)=(I-Pi_c)rho(I-Pi_c)/H_k`.                                 (41)

The sum over all yes/no labelled outcomes is trace preserving. Repeat on the
same data state after `no`, with fresh/reset bank ancillas, and stop at the
first `yes`. Since the projectors are mutually orthogonal and sum to identity,
after `L` trials the unnormalised map for output `c` is

`M_c^(L)(rho)=[1-(1-1/H_k)^L] Pi_c rho Pi_c`,                        (42)

while the total terminal-failure probability is

`f_k(L)=(1-1/H_k)^L`,                                                (43)

independent of `rho`. Thus, conditional on not exhausting the bank, (42) is
exactly the desired Lüders instrument, with correct Born probabilities and no
outcome bias. The intermediate no-results dephase or remove content blocks,
but (38) proves that they do not change the final successful instrument.

Every trial consumes time, ancilla preparation and reset. It does not consume
a fresh copy of the `N`-register evolving data state.

### 6.2 Caps and accumulated approximation

For steering define

`N=ceil(2r^2)`, `M=N(N-1)/2`,
`A_move=ceil(log_4(8M))`,
`K=(N-1)+A_move M`.                                                   (44)

Here `K` bounds all requested content measurements: the initial tableau uses
`N-1`, and every capped adjacent-move attempt uses one. For every such request
take

`L_k=ceil(H_k log(256K))`.                                           (45)

Equations (43)--(45) and a union bound make the probability of any bank
exhaustion at most `1/256`. The total number of binary window tests is bounded by

`W<=4 K N [log(256K)+1]`.                                            (46)

Compile every window-test instrument to diamond error at most `1/(256W)` by
taking `xi<=1/(512W)` in section 5 and allocating its internal gate-synthesis
errors within that same budget. An adaptive hybrid argument then makes the
entire implemented content-measurement transcript at most `1/256` in trace
distance from its exact finite-bank version.

### 6.3 Exact source-support preservation

Every operation touching data in (24)--(39) is a controlled permutation of
the `N` source registers or identity. Such permutations commute with
`P_U^tensor N`. Ancilla rotations, imperfect QSVT phases, measurements and
resets therefore never move the data outside `U^tensor N`. The implemented
content results can be wrong with the bounded probability above, but the exact
support promise survives on every branch. This structural statement is what
makes the final exact certificate valid; approximate QSVT alone would not
certify an exact output.

## 7. Steering, exact certificate and success

Conditional on an ideal initial tableau of an `r`-row shape, bubble boxes to
the column-first tableau using at most `M` valid adjacent swaps. Each move
succeeds with probability at least `3/4`, and its exact failed branch resets the
same tableau. With `A_move` trials per move, total ideal steering failure is at
most `1/8`.

The exact certificate uses

`h_r=2^ceil(log_2(r!))`, `gamma_r=r!/h_r`, `1/2<gamma_r<=1`,          (47)

and a uniform padded binary permutation label to implement the successful
Kraus map

`C_r=gamma_r P_-^(r)`,
`P_-^(r)=(1/r!)sum_(pi in S_r)sign(pi)T(pi)`.                         (48)

Factoradic unranking and exact controlled swaps compile (44) in

`C_cert=O(r^3 log^2(r+1)+r^2[w+log(r+1)])`                           (49)

gates with polynomial ancilla space; no `r!` table is stored. On a correct
column, certificate acceptance is `gamma_r^2>1/4`. On any branch still in
`U^tensor N`, acceptance puts the first `r` registers exactly in
`wedge^r U`, which is one dimensional. Thus every accepted output is exactly
(22), including after imperfect QSVT steering.

The exact certificate can be retried on the same correctly steered column.
For every `psi in wedge^r U`, a valid permutation branch obeys

`sign(pi)T(pi)psi=psi`,

and every padded invalid branch applies identity. The data therefore factor as
`psi` from all label, validity and Hadamard-readout registers throughout the
certificate. Every failure outcome leaves `psi` exactly unchanged. With fresh
or reset ancillas, successive certificate trials have the same success
`gamma_r^2>1/4`. Take

`A_cert=ceil(log(16)/log(4/3))`;                                     (49a)

then a correct column fails every certificate attempt with probability at most
`(3/4)^A_cert<=1/16`. These retries consume gates and time but no new source
copies. On a wrongly steered support state, no reset statement is assumed; any
accepted branch is still exact by (48).

With exact unbounded content instruments, one batch reaches a correct column
and passes a capped certificate with probability at least
`(1/2)(7/8)(15/16)=105/256`. Bank exhaustion subtracts at most `1/256`, and
the approximate-instrument hybrid subtracts at most another `1/256`.
Therefore each implemented batch accepts with probability at least

`103/256>3/8`.                                                        (50)

Run

`B_batch=ceil(log(1/delta)/log(8/5))`                               (51)

fresh batches and output the first accepted coordinate set. On total failure
output any fixed size-`r` set. Since per-batch failure is below `5/8`,
equations (50)--(51) give success at least
`1-delta`; for the useful task take `delta<=1/3`. The source-copy cap is

`Q_quant=B_batch N=O(r^2 log(1/delta))`.                              (52)

No copies of a postselected intermediate state are requested. Each new batch
uses fresh source copies; every bank or move retry inside a batch reuses its
one persistent evolving state.

## 8. Full QSVT gate, memory and separation ledger

Using (38), (44)--(46), a conservative gate bound per batch is

`C_QSVT=O(K N^3 (w+log N) log(256K) log^5(512W))`.                   (53)

Since `K=O(N^2 log N)` and `N=O(r^2)`, this is

`r^O(1) polylog(q/delta)`,                                           (54)

with the displayed crude exponent at most `O(r^10 polylog(r)[log q+log r])`.
Equation (53) deliberately overcharges QSVT phase synthesis and direct SELECT
routing. Add `A_move M` physical steering swaps, `A_cert` uses of certificate
(49), source
delivery and coordinate readout. Multiplying by `B_batch`, total online cost is

`B_batch[C_QSVT+A_cert C_cert+O(A_move M w)+N C_source(q,r)]`,        (55)

plus the common one-time `B_source(q,r)` if it is not amortised.

Quantum storage is

`O(Nw+r^2 log^2(r+1)+log W)=O(r^2 log q+r^2 log^2 r)`                (56)

qubits, plus `O(N log N)` classical tableau/feedback bits. The output itself
uses `r log q` classical bits.

For `r>=3,d>=2`, compare the quantum copy cap (52) with (21). A sufficient
strict separation condition is

`d>(9/4) Q_quant(Q_quant-1)`, equivalently
`q>(9r/4) Q_quant(Q_quant-1)`.                                       (57)

At fixed `delta`, (57) is `q=Omega(r^5)` with a sufficiently large constant;
taking `q/r^5 -> infinity` gives

`Q_quant=O(r^2)` versus `T_classical=Omega(sqrt(q/r))`.               (58)

This is an unconditional delivered-copy/online-memory separation in the stated
source model. It is not a coefficient-list time lower bound, and (55) may be
larger than a classical per-copy measurement circuit. The winning resource is
source copies and cross-copy coherent processing.

For the explicit choice `delta=1/3`, one may take `B_batch=3`,
`N=2r^2`, and `Q_quant=6r^2`. Then (57), rather than an asymptotic slogan,
states the finite range in which the cap is strictly smaller; explicitly it
suffices that

`q>(9r/4)(6r^2)(6r^2-1)`,                                            (58a)

whose leading term is `81r^5`.

The finite separation is formal rather than near term. At `r=3`, the quantum
cap is `54` copies and the sufficient condition is `d>=6440`, hence
`q>=19320` labelled generators. This is far beyond the `q=6` mechanism
diagnostic in section 11.

## 9. Exact direct-antisymmetry fallback

The QSVT compiler is not needed for a weaker growing-rank theorem. Apply the
exact certificate (48) directly to `r` independent flat copies. Since

`rho_C^tensor r=P_U^tensor r/r^r`

and `wedge^r U` has rank one,

`Tr(P_-^(r) rho_C^tensor r)=1/r^r`.                                  (59)

This is **not** `r!/r^r`. One way to see the missing factorial is that drawing
`r` distinct basis eigenvectors has probability `r!/r^r`, while projecting a
fixed ordered distinct product onto its normalized antisymmetric ray succeeds
with probability `1/r!`; the product is (59).

The padded certificate succeeds per attempt with probability

`p_direct=gamma_r^2/r^r>1/(4r^r)`.                                  (60)

Taking

`R_direct=ceil(4r^r log(1/delta))`                                  (61)

attempts and a fixed fallback gives success at least `1-delta`, using at most

`Q_direct=r R_direct=O(r^(r+1)log(1/delta))`                          (62)

source copies and `R_direct C_cert` gates. This exact fallback uses only
Hadamards, reversible arithmetic, signs and controlled swaps. It invokes no
QFT, QSVT, Grover or approximate rotations.

Combining (21) with (62) yields another strict copy separation whenever
`d>(9/4)Q_direct(Q_direct-1)`. In particular, if

`r log r=O(log log q)`                                                (63)

at fixed error, `Q_direct` is polylogarithmic in `q` while the classical lower
is `Omega(sqrt(q/r))`; the direct method wins asymptotically. Condition (63) is
a sufficient slow-growth regime, not the maximal possible one.

## 10. Finite noise and physical access

The exact theorems assume independent ideal copies of (9), exact controlled
data permutations and exact final certificate. Let the actual `Q_quant`
deliveries instead be an independent product of states individually within
trace distance `epsilon_s` of `rho_C`, and let the complete online instrument,
beyond the already budgeted QSVT error, have diamond error `epsilon_g`.
A hybrid bound reduces the correct-output probability by at most

`Q_quant epsilon_s+epsilon_g`.                                       (64)

For correlated deliveries, replace the first term by a joint trace-distance
bound; marginal promises do not imply (64). A noisy theorem with target `2/3`
must leave an explicit margin above `2/3`, rather than set `delta=1/3` exactly.
For example choose algorithmic failure `delta_alg=1/4` and require the right
side of (64) at most `1/12`.

The source is deterministic only after the physical isometry (8) exists.
Photon loss, failed state delivery and reset time belong in `C_source`; if a
delivery succeeds with probability `eta_del`, raw attempts multiply by
`eta_del^(-1)` for both algorithms. Mode-dependent distortion changes `P_U`
and is covered only through the trace-distance premise.

Every content-bank trial uses fresh/reset ancillas, but not a fresh source
batch. The elapsed coherence time includes all `W` tests and `A_move M`
steering attempts. Equation (55), rather than circuit depth for one QSVT
polynomial, is the relevant lifetime requirement.

## 11. Hardware diagnostic and what it establishes

For `r=3`, use the normalized quadrics

`g_0=z_0^2/sqrt(2)`, `g_1=z_0z_1`, `g_2=z_1^2/sqrt(2)`,              (65)

and any calibrated `3 x q` row coisometry, for example `q=6`. The emitter
(8) takes the maximally mixed qutrit over (65) to `P_U/3` with probability one.

The smallest exact output test applies the padded permutation certificate to
three delivered copies. Here `h_3=8`, `gamma_3=3/4`, so its heralding
probability is

`gamma_3^2/3^3=1/48`.                                                (66)

On acceptance, mode-resolved coordinate measurement must produce triples with
probabilities `det(P_U[J,J])`. This checks source normalization, the missing
factorial in (59), signed-permutation compilation and the generator-basis law.
It is classically easy at `q=6` and does not check the QSVT steering advantage.

A separate three-register diagnostic tests the `k=3` content bank for
`X_3=S_13+S_23`: its integer windows, repeated-bank outcome frequencies and
state-independent exhaustion probability can be compared with direct matrix
projectors. A small MBQC circuit can implement the controlled swaps, QSVT
ancilla rotations and feed-forward. Scaling the full steering method uses
`N=18` source registers already at `r=3`, so this is a mechanism experiment,
not a near-term advantage claim.

A bounded in-memory numerical check covered random complex row coisometries for
`3<=r<=6`, the success-one emitter, the exact transversal factor and uniform
`a_(r,d)<=2/5` bound for `3<=r<=5,2<=d<=4`, the finite window-bank maps on a
random five-dimensional density matrix, and direct `r=3,q=4`
antisymmetrization. All 49 checked identities passed at tolerance `1e-10`,
including terminal bank trace `(1-1/H)^L` and overlap `1/r^r`. This verifies
finite algebra only, not the Haar transcript inequality, QSVT compiler or
asymptotic advantage.

The hardware route is MBQC/controlled-permutation processing of a natural
emitter source. Linear-optical path encoding can implement the source and small
permutation tests, but no deterministic large controlled-swap photonic device
is assumed.

## 12. Primary-source checks after derivation

The algebra, lower bound and bank channel above were derived before these
targeted comparisons.

1. Vershik--Okounkov,
   [arXiv:math/0503040](https://arxiv.org/abs/math/0503040), gives the
   Jucys--Murphy content spectrum, Young branching basis and adjacent
   transposition structure used in tableau steering.
2. Gilyén--Su--Low--Wiebe,
   [arXiv:1806.01838](https://arxiv.org/abs/1806.01838), gives QSVT and the
   bounded sign-polynomial machinery supporting (31)--(39). The shifted LCU,
   padding, window retries and support-preserving certificate remain costs of
   this construction.
3. Bacon--Chuang--Harrow,
   [arXiv:quant-ph/0407082](https://arxiv.org/abs/quant-ph/0407082), gives an
   efficient Schur transform/generalized phase-estimation route. It is a
   comparator for the old Fourier implementation; it is not used in the R13
   circuit, because D25 excludes QFT-based mechanisms.
4. Garcia-Escartin--Chamorro-Posada,
   [arXiv:1303.6814](https://arxiv.org/abs/1303.6814), identifies
   Hong--Ou--Mandel interference with a destructive swap test. It directly
   supports the rank-two hardware result; the growing-rank signed certificate
   needs the controlled-permutation/MBQC circuit described here.

No source was found that supplies this repeated QSVT window-bank replacement or
the `r`-block adaptive separate-copy lower bound. Absence of a source is not a
novelty proof. Under D25, historical priority would not itself disqualify the
mechanism; the same-output advantage and resources are the relevant tests.

## 13. Tournament assessment

| criterion | assessment |
|---|---|
| precise AG problem | met: minimal original-generator selection for the based presentation (3) of the fat point (4) |
| classical baseline | met in the declared source model: (19), with the explicit uniform bound (21), permits all adaptive within-copy POVMs |
| quantum advantage | met for delivered-copy complexity when (57) holds; QSVT upper is polynomial in `r,log q`, and direct fallback covers (63) |
| dequantisation/hidden costs | source-only access, no metadata, fixed cap, persistent retries, padding, QSVT degree, loss and device construction are explicit |
| heuristic hardware | MBQC controlled-permutation/QSVT route and `r=3` emitter/certificate diagnostic are concrete; no large photonic controlled swap is assumed |
| D25 mechanism | met: QSVT and swap/representation processing are eligible; no QFT, Grover or DQI |

Subject to independent audit of the QSVT reflection and the `r`-group
minorization, this is a formal growing-rank north-star extension in a
quantum-data model. It proves the stated copy advantage. The whole q/r^5 regime is not by itself
a processing-time comparison: gate work is polynomial in r,log q, and is
polynomial in log q when r<=poly(log q). Explicit-coefficient and one-shot
device-construction time advantages are not established. The direct fallback
ensures that the growing-rank statement does not stand or fall solely on the
QSVT compiler, though it has the rank cost (62).

## MERGE PROPOSAL

**D-R13-SYZYGY-BASIS-SOURCE.** Data are `r>=3,q>=r`, the based degree-`r-1`
tuple (1)--(3) for an unknown row coisometry, and independent copies of
`rho_C=C^dag C/r` obtained by the success-one emitter (8)--(9). No coefficients,
support basis, preparation inverse, controlled emitter or hidden-partition
metadata are supplied. Delivery/device costs are separate.

**D-R13-SYZYGY-BASIS-OUTPUT.** Always output `r` original distinct labels.
Success means their forms generate `(z_0,z_1)^(r-1)`, equivalently their
`r x r` coefficient minor is nonzero. Require uniform success at least `2/3`.
The classical comparator has arbitrary adaptive POVMs on each complete source
copy and unlimited classical processing, but no quantum memory between copies,
and a fixed total copy cap.

**C-R13-SOURCE-AND-GEOMETRY (proposed SKETCH).** Equations (4)--(9) hold for
every row coisometry: the quotient is a length-`r(r-1)/2` fat point, constant
syzygies are `ker C`, a successful label set is exactly a minimal generating
basis, and the emitter is the isometry `C^dag` with success one and output
`C^dag C/r`.

**C-R13-SEPARATE-COPY-LOWER (proposed SKETCH).** For `q=rd`, `r>=3,d>=2`, every
fixed-cap adaptive separate-copy algorithm with uniform success `2/3` obeys
(19), and hence `T(T-1)>=4q/(9r)`. The hidden balanced partition and Haar lines
are fixed for the transcript and not public.

**C-R13-QSVT-UPPER (proposed SKETCH).** The block encoding (24)--(29), QSVT
reflections (30)--(39) and padded retry bank (40)--(46) replace all Fourier
content measurements in tableau steering. With (44)--(51), at most
`O(r^2 log(1/delta))` ideal source copies and polynomial
`r,log q,log(1/delta)` gates produce an exact accepted Slater state and solve
D-R13-SYZYGY-BASIS-OUTPUT with failure at most `delta`. Strict source-copy
advantage holds under (57).

**C-R13-DIRECT-FALLBACK (proposed SKETCH).** Direct exact antisymmetry on flat
rank-`r` copies has overlap `1/r^r`; the padded certificate succeeds with
`gamma_r^2/r^r>1/(4r^r)`. Equations (61)--(63) give an independent non-Fourier
copy advantage in the displayed slowly growing rank regime. No `r!` numerator
is present.
