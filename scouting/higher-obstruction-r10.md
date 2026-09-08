# Higher-obstruction processor, R10 construction lane

2026-09-05. Exploratory derivations, awaiting independent adjudication. This
memo uses D-HIGHER-OBSTRUCTION-PENCIL/QUERY/REALIZATION and their declared
finite-dimensional Hermitian metrics: the departure from C1 and independence
from C2 are explicit; no coherent-state conjugation convention is imported.
Only this scouting file is written by the constructor. Root owns definitions,
claims, tracking, commits and the final verdict. No claim promotion is proposed
merely because an equation below has been derived.

## 1. A concrete operation before literature comparison

1.1. ASSUME the restricted input has D_0=identity, equal endpoint input/output
spaces K of dimension d, equal internal spaces L of dimension m, and a supplied
unitary circuit for the block matrix U=[[A,B],[C,E]] on K direct-sum L. The
splitting is physically marked by an endpoint projector P, with Q=identity-P.
The circuit preparing endpoint x, the circuit for U and the implementation of
P are input resources, not supplied by the sparse coefficients for free.

1.2. OPERATION. Prepare x in K. Apply U, measure {P,Q}, and stop on P. If Q
occurs, retain the entire internal state and apply U again. Continue through
step ell. Output one exactly if the first endpoint click is at step ell.
An earlier click is a rejected outcome; under the promise it has zero
probability. A Q result at ell is the zero output. There is no intermediate
state renormalization operation other than the ordinary conditional quantum
state update, and no discarded internal path label.

1.3. PROVE the unnormalized Kraus map for the first click at step j is

    K_1=A,
    K_j=B E^(j-2) C, j>=2.

Indeed, Q U x=Cx after the first internal outcome, and the next internal
updates are E. The remaining internal map after ell steps is E^(ell-1)C.
Unitarity gives C†C+A†A=identity and E†E+B†B=identity, so telescoping yields

    ||Ax||² + sum_(j=2)^ell ||B E^(j-2)Cx||²
      + ||E^(ell-1)Cx||² = 1.

The full collection of stopped outcomes and the last surviving outcome is
therefore a trace-preserving instrument on endpoint inputs.

1.4. By D-HIGHER-OBSTRUCTION-PENCIL, K_j=(-1)^(j-1) S_j for j>=2 and
K_1=S_1. The promised earlier coefficients vanish on x. All earlier internal
outcomes consequently have conditional probability one, and the output-one
probability is exactly ||S_ell x||². This reads the coefficient at physical
time ell, with no t^ell amplitude penalty. In particular gamma<=1 whenever
the nonzero side is populated in this restricted model.

1.5. The same promise makes the intermediate measurements removable. By
induction U^j x lies entirely in L for 1<=j<ell; at j=ell its endpoint
component is K_ell x. One final P measurement after U^ell therefore produces
the same output probability and the same final two conditional states.
This is an exact operation-and-resource reduction, not a statement that
every quantum algorithm using U is disqualified merely for using gates.

1.6. If ell>=2, the orbit x,Ux,...,U^(ell-1)x is orthonormal: its off-diagonal
inner products reduce by unitarity to <x,U^j x>=0 for 1<=j<ell. All vectors
after the first belong to the m-dimensional L, so ell<=m+1. At ell=m+1,
the m internal orbit vectors span L and U^ell x is orthogonal to all of them;
therefore U^ell x lies in K and the return probability is exactly one.
This strengthening uses unitarity; the general-pencil order cap instead
follows from Cayley–Hamilton and does not assert a deterministic terminal
signal.

## 2. Resources and the honest classical comparison

2.1. Let G_U,G_x,G_P be circuit costs at the chosen precision, and let a_U
denote the work qubits needed to apply U coherently and cleanly. With fresh
runs, R=ceil(gamma^(-2) log(1/delta)) trials suffice: the nonzero-side miss
probability is at most exp(-R gamma²), and the ideal zero side never clicks.
Gate count is O(R[G_x+ell(G_U+G_P)]). There are R endpoint preparations and
at most R ell uses of U. The measured implementation uses
O(log(d+m)+a_U+log ell) qubits/classical counter space; no growing quantum
history register is needed. With the promise and a final-only measurement,
the measurement work is paid once per run.

2.2. Physical circulation takes ell passages per trial. A round-trip time
tau gives R ell tau evolution/delay time. A cavity does not turn this into
constant time. Passive loss of transmissivity eta_pass per passage reduces
the unconditioned click probability by eta_pass^ell when every passage has
that loss. Treating missing photons as free restarts would hide this cost.

2.3. An implementation error epsilon_run in output probabilities accumulates
over R repetitions. A sufficient conservative allocation is
epsilon_run<=delta/(4R). With operator-norm unitary error epsilon_U, state
preparation vector error epsilon_x and measurement error epsilon_P,
epsilon_run<=2(epsilon_x+ell epsilon_U)+epsilon_P is sufficient up to an
inessential constant. Thus one may require each term to be
O(delta/(R ell)), giving bit precision
O(log(R ell/delta)) for gates with a logarithmic compilation dependence.
The original rational coefficients, their precision, and exact promise
testing are not replaced by this gate-accuracy estimate.

2.4. Explicit sparse input admits the matched recurrence v_0=Cx,
v_(k+1)=E v_k, followed by B v_(ell-2), and a norm comparison. It uses
O(ell nnz(E)+nnz(B)+nnz(C)) arithmetic operations once x is available,
O(m+d) numerical words, and no full cohomology calculation. For a uniformly
sparse unitary this is O(ell s_row(m+d)). If x is given by a succinct quantum
circuit rather than an explicit vector, its classical simulation/preparation
cost must be counted; it is incorrect to give only the quantum side a free x.

2.5. In a succinct circuit model, repeated U can have the usual quantum
simulation advantage over dense classical state evolution. No lower bound
against the best same-output classical algorithm is established here.
An explicit coefficient list may already have size proportional to m, while
compiling a general listed unitary can cost quadratically many gates. Sparse
entry/location access does not itself supply unit-cost access to U. This memo
does not infer a speedup by comparing log(m) qubits with a printed basis.

## 3. Algebraic meaning, with the splitting retained

3.1. The supplied pencil presents the coherent sheaf coker F on A1. Over
the local ring C[t]_(t), D_0+tE is invertible, and invertible block row and
column operations transform F into diag(S(t),D_0+tE). This identifies its
local cokernel with coker S(t). These are local operations: D_0+tE need not
be invertible over all of C[t], and other support points can be present.

3.2. For d=1 and x=1, if S_1=...=S_(ell-1)=0 and S_ell is nonzero, then
S(t)=t^ell u(t), u(0)!=0. The local cokernel is C[t]_(t)/(t^ell), with
length ell. If S_ell=0, its length is at least ell+1 when S is nonzero,
or it has a free summand when S identically vanishes. Thus the scalar
unitary-colligation subfamily supplies an actual infinitesimal-thickening
query about a coherent sheaf on A1, with a metric gap on the leading
coefficient. This interpretation is intrinsic in the scalar case; the
coefficient's norm still depends on the stated metric and presentation.

3.3. For a general endpoint vector x, the exact statement is about the
constant endpoint section: with the unique formal internal section
y(t)=-t(D_0+tE)^(-1)Cx, the residual is S(t)x. The query decides whether
this residual's coefficient at t^ell vanishes. It does not generally
decide whether some moving endpoint section x(t)=x+O(t) has a lift.
The critic's explicit counterexample is
A=(0,1), B=1, C=(1,0), D_0=1, E=0, x=(1,0): S_2x=-1, but
x(t)=(1,t), y(t)=-t gives F(t)(x(t),y(t))=0 exactly. No intrinsic Massey
product, Ext obstruction, or spectral-sequence differential is claimed.

## 4. First repair: a general-pencil dilation exposes the lost scale

4.1. For this derivation abbreviate the canonical pencil's internal
recurrence by T=D_0^(-1)E and v=D_0^(-1)Cx. Form the block map

    J=[[A,-B],[D_0^(-1)C,-T]].

If lambda>=max(1,||J||), J/lambda is a contraction. A unitary dilation
implements it as a successful Kraus map; a complementary failure map has
effect identity-J†J/lambda². Recycling only successful internal branches,
and marking every failure so that it cannot re-enter the signal, gives
first endpoint amplitude S_j x/lambda^j. The target event probability is
||S_ell x||²/lambda^(2ell). Previous obstruction zeros eliminate premature
endpoint events, but do not eliminate dilation failures.

4.2. Retaining and recombining the failure bath is not an automatic repair.
If a failed amplitude re-enters the internal signal, the new transfer
function includes bath-return paths absent from J's powers. If it remains
orthogonal and excluded from the accepted outcome, the accepted Kraus map
above is unchanged. The unitarity of a dilation alone neither erases these
paths coherently nor proves that their sum equals the requested coefficient.

4.3. This is a diagnosis of this uniform-rescaling dilation, not a lower
bound asserting that all implementations pay lambda^ell. Separate block
normalizations, structure, or a better internal metric can change the cost.
Inverse access to D_0 is already a charged prerequisite here: constructing
T or v numerically requires solving with D_0, and a block-encoding inverse
has an explicit normalization/condition-number and precision cost.

## 5. Second repair derived before source checking: energy-metric recycling

5.1. ASSUME rho(T)<1 and that the observability Gramian

    H=sum_(k>=0) (T†)^k B†B T^k

is positive definite. Finite dimension and strict spectral radius less than
one ensure convergence, even when ||T||>1. Positivity additionally excludes
an invisible internal direction. The series obeys the Stein identity
H=T†HT+B†B. This is an additional construction from the original matrices,
not additional free information in D-HIGHER-OBSTRUCTION-QUERY.

5.2. Define the internal transformation R_H=H^(1/2)T H^(-1/2) and the
emission map B_H=B H^(-1/2). Then

    B_H†B_H+R_H†R_H=identity.

Consequently W:z -> |out>B_H z + |internal>R_H z is an isometry. Pad the
output/internal labels and complete its columns to a unitary if a circuit
is needed. Every output click stops the process. The internal branch is
retained and recycled; its state is never projected on a specified vector.

5.3. Write h=v†Hv. If v!=0, prepare z_0=H^(1/2)v/sqrt(h). The first
output amplitude after k+1 passages is

    B_H R_H^k z_0 = B T^k v/sqrt(h).

The target coefficient S_ell x occurs at passage ell-1, up to its irrelevant
sign, and target probability is ||S_ell x||²/h. The earlier-zero promise
again makes preceding internal outcomes deterministic. Moreover
h=sum_(k>=0)||B T^k v||², so this is normalization by the total future
emission energy rather than a product of independent block norms.

5.4. This can repair a bad coordinate normalization. For example, let
T e_j=g e_(j+1) for j<m, T e_m=0, B=e_m† and g>1. Then
H=diag(g^(2(m-1)),g^(2(m-2)),...,1); R_H is the unit-amplitude shift,
B_H=e_m†. On v=e_1 the sole output is at passage m, with probability one.
Uniformly dividing the original recurrence by g obscures this exact
lossless realization. This family is classically a single path, so the
repair does not establish a computational advantage.

5.5. The costs displaced into H are real. Its explicit computation is a
discrete Lyapunov/Stein solve in m² unknowns, or a truncated Gramian series
whose convergence depends on transient growth as well as rho(T). H can
be dense and arbitrarily ill-conditioned. Producing R_H,B_H and preparing
z_0 requires the square root, inverse square root, and v; an arbitrary
compiled isometry can require quadratic-size synthesis. No cheap sparse
oracle for these transformed objects follows from sparse B,T.

5.6. If z_0 and W are actually compiled, fresh trials have the same costs
as section 2 with ell replaced by ell-1 and with
R=ceil((h/gamma²) log(1/delta)); a known upper bound on h suffices. If h is
unknown, a normalization bound must be computed or supplied. A direct
heralded preparation using Kraus map H^(1/2)D_0^(-1)C/a_H succeeds with
h/a_H², and the combined target event has probability
||S_ell x||²/a_H². Thus heralding cannot silently delete the preparation
normalization. The case v=0 is the zero answer and has no normalized z_0.

5.7. If H is singular, restriction to its observable quotient is possible
mathematically, but constructing this quotient is additional work. A
positive Gramian formed with B†B+epsilon identity creates a separate leak
channel sqrt(epsilon)H^(-1/2). Earlier obstruction zeros then do not remove
leak events. If rho(T)>=1, even convergence is absent; choosing a damping
radius replaces coefficients by radius^k coefficients and reinstates a
charged extraction scale. No general-pencil algorithm is proved by 5.1.

## 6. Targeted literature verification and remaining diagnostic

The operations in sections 1 and 5 were derived before targeted primary
source verification. This section will record the exact prior-operation
maps and the bounded numerical/optical diagnostic; it will not infer
originality from a source search returning no match.

## MERGE PROPOSAL (provisional)

Retain the exact unitary-colligation instrument, its no-small-t coefficient
readout, scalar sheaf-length interpretation, and explicit general-dilation
normalization. Do not promote an intrinsic higher-obstruction or original
quantum-mechanism claim. The energy-metric repair is a derived construction
whose implementation costs and precise prior-operation reduction remain
under active checking. The research goal is not complete.
