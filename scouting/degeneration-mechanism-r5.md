# Degeneration operations: jet rescaling and retained defect transport

2026-09-05. Independent bounded construction for `qaag-5si`.
Canonical inputs and operators are D-R5-JET-SOURCE and
D-R5-DEFECT-TRANSPORT in `definitions/mechanism-r5.md`.
Claim status lives only in `claims/CLAIMS.md`, C-349--C-350; independent
review is in `verdicts/degeneration-mechanism-r5.md`.
We use orthonormal quantum registers, explicitly departing from the default
cross-degree Fock interpretation in convention C1. Auxiliary D and identity
notation locally depart from C8 and C6 as declared in the canonical file.
Point kets represent
conjugate coordinates as required by C3. Shared files remain root-owned.

Two operations were derived before targeted literature verification.
The first has a complete source-information obstruction and is recorded
briefly. The second retains all outcomes and has normalization one;
its obstacle is that bath reinjection changes algebraic multiplication.
Neither displayed operation establishes an original quantum algorithm.
These conclusions concern the explicit constructions, not all degenerations.

## 1. A flat family and a precise geometric bit

1.1. Fix length D>=2, r=D-1, 0<t<1, m>=D, and unknown orthonormal
vectors u_1,...,u_r in C^m. Set gamma(z)=sum_(k=1)^r z^k conjugate(u_k).
The algebra C[t,z]/(z^D-t^D) is free over C[t] with basis 1,z,...,z^r.
The map C[t,x_1,...,x_m] -> C[t,z]/(z^D-t^D), x_j -> gamma_j(z), is
surjective: a linear functional dual to conjugate(u_1) recovers z.
Its kernel thus defines a flat embedded family. Nonzero fibres consist
of the D distinct labelled points gamma(t*zeta^(-a)),
zeta=exp(2*pi*i/D), 0<=a<D. This inverse label phase implements C3.
The zero fibre is an embedded curvilinear scheme Spec C[z]/(z^D).
D=4 includes a twisted-cubic arc with an unknown orthonormal frame.

1.2. Let u_0=|0> be orthogonal to the affine coordinate register and
Z_t=sum_(k=0)^r t^(2k). Supply copies, without a preparation inverse, of

    |v_a(t)> = Z_t^(-1/2) sum_(k=0)^r t^k*zeta^(ak)|u_k>,
    |Psi_t(U)> = D^(-1/2) sum_(a=0)^(D-1) |a>|v_a(t)>.

This coherent labelled source is an explicit stronger promise than an
unlabelled mixture or classical samples of roots. It costs C_src per copy.
Each point register is normalized by orthonormality of the u_k.
Data size is log D+log(m+1) qubits; no QRAM loading is hidden.

1.3. Supply a geometric complex linear hyperplane H through the origin,
containing conjugate(u_1),...,conjugate(u_(r-1)). Promise conjugate(u_r)
lies in H or is orthogonal to H; output whether the special fibre is
scheme-theoretically contained in that affine hyperplane.
Its defining equation pulls back to c*z^r modulo z^D, so containment
is exactly c=0. Containment of its support point alone is vacuous.
The quantum test projects onto span{u_0} plus conjugate(H).
The geometric bit is independent of local reparametrization of z;
the orthonormal jet description is an additional quantitative promise.

## 2. Exact rescaling, cost, and its source lower bound

2.1. The known orthonormal labels chi_k=D^(-1/2)sum_a zeta^(ak)|a>
give the exact expansion

    |Psi_t(U)> = Z_t^(-1/2) sum_(k=0)^r t^k |chi_k>|u_k>.       (1)

Let L map chi_k to k. The inverse diagonal weights t^(-k) have norm
t^(-r); their maximally scaled contraction is

    K_t=sum_(k=0)^r t^(r-k)|k><k|,
    (K_t L tensor 1)|Psi_t(U)> = sqrt(D/Z_t)*t^r |Phi(U)>,
    |Phi(U)>=D^(-1/2)sum_k |k>|u_k>,
    s_flat=D*t^(2r)/Z_t,       s_bit=s_flat/D=t^(2r)/Z_t.       (2)

A herald qubit realizes amplitude t^(r-k) for success in sector k.
Contractivity on |r> proves the scalar is optimal among maps required
to equal a scalar times this inverse on the whole label space.
That scoped argument is about an unknown coherent combination, not
unambiguous discrimination of one unknown root; it is not a universal
joint-register optimality theorem. L is a finite Fourier transform here.

2.2. Failure acts by F_t=sum_k sqrt(1-t^(2(r-k)))|k><k|, hence kills
|r> exactly. Two sources differing only in u_r have identical failed
outputs. Every failure Kraus operator for this success effect kills |r>,
because the total failure effect has zero expectation on |r>.
Recovery from that failed output cannot restore the missing top jet.
The decision event from a successful Phi clicks outside H with
probability 1/D. Repetition to error epsilon therefore suffices with

    M_bit=ceil(Z_t*t^(-2r)*log(1/epsilon)) source copies.        (3)

Charge M_bit*(C_src+C_L+C_K+C_H), where C_H is the supplied hyperplane
measurement cost, C_L the Fourier basis change, and C_K the controlled
rotations. Generic bounds are C_L=O(D^2*polylog(D/eta)) and
C_K=O(D*polylog(D/eta)); Fourier circuits can improve C_L.
Per-trial trace-distance error O(epsilon/M_bit) is sufficient. Required
absolute amplitude precision involves O(r*log(1/t)+log(D/epsilon)) bits.
A dense hyperplane or source description need not have cheap preparation.

2.3. Fix equal lower jets and choose u_r=e_r in one instance and
u_r=e_(r+1) in the other, with H separating those final directions.
Their source overlap is exactly 1-s_bit. For M copies the trace distance is

    T_M=sqrt(1-(1-s_bit)^(2M)).

Every collective/adaptive copy algorithm is subject to this bound.
Success at least 2/3 on both instances requires T_M>=1/3, so

    M >= log(8/9)/(2*log(1-s_bit))
      = Omega(Z_t*t^(-2r)).                                  (4)

This rules out collision-independent copy complexity even for a new
physical mechanism. A supplied preparation unitary AND its inverse
instead permit O(s_bit^(-1/2)) reflection-based amplification calls;
that is the known amplitude-amplification mechanism and a different
access model. No inverse is available from copies alone.

2.4. The strongest matched attack is simpler than the proposed circuit:
apply the quantum test for H directly on each point register. Its click probability is
zero or s_bit, attaining (3) without L, K, or memory across sources.
For classical coefficient input the bit is a linear coefficient test;
reading and checking all dense data needs O(D*m) arithmetic operations.
Exact samples at known nodes admit O(D^2*m) interpolation arithmetic,
with precision growing as r*log(1/t), rather than t^(-2r) physical copies.
These explicit upper bounds suffice here; they are not a best-known
assertion for arbitrary succinct curve presentations.

2.5. Exterior cancellation also fails to help. For V_t=[v_0,...,v_r],

    singular_values(V_t)=sqrt(D/Z_t)*(1,t,...,t^r),
    s_wedge=det(V_t^*V_t)/D!
           =(D/Z_t)^D*t^(D*(D-1))/D!.                        (5)

This assumes one separately supplied copy of every labelled root, so
costs at least D preparations per attempt. The amplitude's order
D*(D-1)/2 is the Vandermonde divisor of an alternating polynomial in
root parameters. A bounded alternating operation cannot remove it.
For D=4,t=0.1: s_bit=9.900000099e-7, s_flat=3.960000040e-6,
s_wedge=1.024635785e-11, and 1,109,710 direct trials suffice at error 1/3.

2.6. In a path register K_t is a bank of attenuating beam splitters with
heralded dump ports. In a number register it is t^r*g^(number), g=1/t.
This is the already described noiseless-amplification transformation:
Ralph--Lund, equation (11), [arXiv:0809.0326](https://arxiv.org/abs/0809.0326).
Their finite optical network has additional cutoff factors. Our exact
finite-register normalization does not make amplification original.
The missing copy-speedup lemma for this family is disproved by (4).

## 3. Second construction: retain every normal-cone escape amplitude

3.1. Now use the unramified base coordinate tau and the flat family

    A_tau=C[tau,z]/(z^D-tau),       |tau|<1.

The previous source considered the positive slice tau=t^D after base
change. Monodromy in tau is different from monodromy in that t-cover.
Supply D in binary and complex tau to b bits. In the explicitly declared
orthonormal coefficient basis |k>=z^k, 0<=k<D, multiplication is

    C_tau=sum_(k=0)^(D-2)|k+1><k| + tau|0><D-1|.              (6)

This Hilbert metric is a chosen coefficient metric, not a canonical
metric on every local algebra. The filtration by degree supplies the
normal-cone sectors. Both defect operators have rank one:

    1-C_tau^* C_tau=(1-|tau|^2)|D-1><D-1|,
    1-C_tau C_tau^*=(1-|tau|^2)|0><0|.

3.2. Write beta=sqrt(1-|tau|^2), introduce one bath state |b>, and define

    U_tau|k>=|k+1>,                       0<=k<D-1,
    U_tau|D-1>=tau|0>+beta|b>,
    U_tau|b>=beta|0>-conjugate(tau)|b>.                     (7)

Columns are orthonormal. Thus U_tau is a unitary with normalization one,
no postselection, and P U_tau P=C_tau for P onto the D live sectors.
It acts on an arbitrary unknown coherent input, not just on roots.
This is a one-step unitary completion, NOT an all-powers finite dilation.

3.3. Implementation is concrete: increment modulo D+1, identifying b
with D, then apply the two-state unitary

    [[beta,tau],[-conjugate(tau),beta]]

on output states 0,b. A reversible modular increment and a two-level
rotation use polylog(D/eta) gates per step at error eta. An initial
|0> is free up to O(log D) initialization; no unknown eigenstate is
supplied. T steps cost O(T*polylog(D*T/epsilon)) gates with eta=O(epsilon/T),
and O(log D) data qubits. A phase-reference return-amplitude estimate
at additive epsilon costs O(epsilon^(-2)) repetitions by a Hadamard test.
Every bath outcome is retained in this account.
These resource bounds assume |tau|<=rho<1 with fixed rho and input
precision b=Omega(log(T/epsilon)); they hold throughout degeneration.
Approaching the unit circle additionally requires charging square-root
precision: coefficient error must be O(epsilon*beta/T).

3.4. A path-encoded optical circuit is a D+1-cycle with one adjustable
beam splitter and phase shift at the boundary. It can test coherent
transport among local-algebra degrees even at tau=0. Ordinary photon
loss is not the algorithm's retained bath and must be separately charged.

## 4. What the one-bath operation actually computes

4.1. Direct elimination of an eigenvector gives

    det(lambda*1-U_tau)
      =lambda^(D+1)+conjugate(tau)*lambda^D-tau*lambda-1.      (8)

At tau=0 this is a D+1-cycle with distinct eigenvalues, whereas C_0
is the nilpotent multiplication operator of a length-D nonreduced point.
This is an exact algebraic discrepancy, not poor conditioning.

4.2. It appears already after two steps:

    P U_tau^2 P - C_tau^2 = (1-|tau|^2)|0><D-1|.              (9)

Proof: insert 1=P+|b><b| between the two U factors. The additional
term is exactly the amplitude leaving the live space and returning.
Discarding this distinction would falsely turn a unitary completion
into a faithful arithmetic simulation of arbitrary multiplication powers.

4.3. Let c_n=<0|U_tau^n|0>. First-return paths either traverse D live
steps with amplitude tau, or spend additional time in b. Their generating
series and the complete return series are

    B(w)=w^D*(tau+w)/(1+conjugate(tau)*w),
    R(w)=sum_(n>=0)c_n*w^n
        =(1+conjugate(tau)*w)
          /(1+conjugate(tau)*w-tau*w^D-w^(D+1)).              (10)

For n>=2 this gives the scalar recurrence

    c_n=-conjugate(tau)*c_(n-1)+tau*c_(n-D)+c_(n-D-1),

with c_0=1 and negative-index terms zero. Thus c_D=tau and
c_(D+1)=1-|tau|^2 for D>=2. Return amplitudes include bath feedback.

4.4. The recurrence computes c_T classically in O(T) arithmetic
operations and O(D) stored numbers, matching the T dependence of the
quantum circuit without sampling. For |tau|<=rho<1, coefficients of
the reciprocal denominator have modulus at most 1/(1-rho): multiply
R(w), whose coefficients have modulus <=1 by unitarity, by
sum_j(-conjugate(tau)*w)^j. Accumulated local rounding delta therefore
causes at most O(T*delta/(1-rho)) error. Precision
O(log(T/(epsilon*(1-rho)))) bits beyond the input precision suffices.
A general quantum space advantage over every classical recurrence
strategy is not proved; in any case this is a known scattering primitive.

4.5. Nearby-fibre monodromy does not pass to the ordinary unitary
spectrum. Going once around tau=0 cyclically permutes the D roots
lambda^D=tau of C_tau. In contrast, U_0 has minimum spectral spacing
Delta_D=2*sin(pi/(D+1)). For sufficiently small |tau| compared with
Delta_D, the U_tau eigenvalues stay in disjoint disks around those
D+1 roots. A small loop therefore permutes none of them.
Berry phases of those eigenlines may occur, but approach the identity
as the loop contracts; they do not restore the missing D-cycle.
The monodromy conjugacy class on this family is also classically
available immediately from D. No hidden hard output has been established.

## 5. Repair all powers while retaining the history

5.1. Allocate fresh orthogonal bath states e_1,...,e_T. At step j use
(7) on the live D-space plus e_j, fixing every other bath state.
No earlier bath amplitude is fed back. If V_j denotes this step,

    P V_T ... V_1 P=C_tau^T.                                (11)

Proof by induction: old bath states are fixed and never couple to live
states; the new bath state has zero amplitude before its assigned step.
This is a faithful finite-horizon construction on D+T dimensions.
It costs O(T*polylog((D+T)*T/epsilon)) gates and O(log(D+T)) data qubits.
Its extra storage is charged rather than called failure recovery.

5.2. For initial |0>, put q=floor(T/D) and h=T mod D. The exact final
all-outcome state is

    tau^q|h> + beta*sum_(ell=1)^q tau^(ell-1)|e_(ell*D)>.      (12)

Its squared norm is |tau|^(2q)+(1-|tau|^2)sum_(ell=0)^(q-1)|tau|^(2ell)=1.
The live component is exactly C_tau^T|0>. Retaining all outcomes is
fully compatible with unitarity; the live survival probability is
|tau|^(2q), and conditioning on it does not make that probability free.

5.3. The recorded exit time has a truncated geometric distribution.
A classical inverse-CDF sampler generates that same natural output
with polylog(T) arithmetic overhead at supplied numeric precision.
The compressed algebraic moment is even simpler:

    <0|C_tau^T|0> = tau^(T/D) if D divides T, and zero otherwise.

An arbitrary final circuit acting on (12) could pose a different quantum
computation problem; no intrinsic geometric predicate or original
mechanism follows merely from allowing an unrestricted readout circuit.

## 6. Targeted verification and disposition

6.1. The second construction was derived before searching. Its rank-one
defect completion belongs to established unitary colligation theory;
Arlinskii--Golinskii--Tsekanovskii explicitly study this setting and
truncated CMV models in [arXiv:math/0611439](https://arxiv.org/abs/math/0611439),
sections 2--3. The primary PDF was fetched. No originality claim is made
for adjoining the defect channel or propagating its retained history.

6.2. Two bounded inline probes used timeout 30 seconds and one BLAS
thread. The first passed 135 checks of (1)--(5) for D=2,...,6 and
three positive t values, rejecting 30 wrong exponents. The second passed
750 checks of unitarity, complex conjugations, (8)--(12), and norm
conservation for D=2,...,7 and five real/complex tau values. It rejected
42 bad conjugation or false all-powers-compression assertions.
These are supporting numerical probes, not registered proof checkers.

6.3. The precise missing lemma for the retained one-bath proposal would
identify a native nearby-cycle invariant in its spectral or return data
and furnish a nontrivial matched advantage. Equations (8)--(9) refute
the tempting identification of its eigenvalue monodromy or powers with
those of algebraic multiplication. Equation (12) repairs the powers,
but its natural output has the direct classical attack in section 5.3.
A different invariant or a different mechanism remains necessary.

6.4. MERGE PROPOSAL: retain these exact operations and their narrowly
scoped obstructions if useful. No new success, speedup, or historical
originality claim is proposed. The first operation is inverse attenuation;
the second is defect scattering with explicitly accounted bath history.
This bounded lane is complete, while the campaign's search remains open.
