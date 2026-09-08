# Growing-rank generator-basis source and QSVT budgets

2026-09-08. Current criterion D25 admits QSVT and excludes QFT/Grover/DQI
disguises. These definitions use the Fock polynomial metric and C3 conjugated
annihilation. Source rank r and bath dimension q are independent of the number
of polynomial variables. The tuple uses a row-coisometry normalization rather
than separately unit-Bombieri generators, an explicit C5 departure. Local
block normalization symbols below are alpha_BE,k, following C7.

## D-R13-SYZYGY-BASIS-SOURCE

Let r>=3,q>=r,e=r-1 and R=C[z0,z1]. The orthonormal degree-e monomials are
`g_i=z0^(e-i)z1^i/sqrt((e-i)!i!)`, 0<=i<r. An unknown r-by-q matrix C obeys
`CC†=1_r`. Its based tuple is `f_a=sum_i C_ia g_i`. Set K=ker C,
U=range(C†), and `rho_C=C†C/r`.

Input consists only of independent copies of rho_C, encoded in
w=ceil(log2 q) qubits, plus the known r,q. No coefficient list, purification,
support basis, preparation inverse, controlled emitter, or hidden partition
is supplied. At emitter/Macaulay degree e, the fixed incident state is
`1_(R_e)/r` and the Fock emission map is the isometry `V=C†`, with success one.
One-time source construction B_source(q,r) and each delivery C_source(q,r)
are separately charged. This is quantum-source data, not free loading of a
classical polynomial table.

## D-R13-SYZYGY-BASIS-OUTPUT

Always return a sorted set J of r distinct ORIGINAL generator labels. Success
means the selected forms generate the ideal of the whole based tuple,
equivalently `det C[:,J]!=0`. Require success at least 2/3 for every promised C.
A stronger parameterized algorithm may have failure at most 0<delta<=1/3.
Returning an abstract monomial basis, a larger generating list, or a quantum
state alone is a different output.

## D-R13-SYZYGY-BASIS-COMPARATOR

The same independent source copies are available. The comparator may perform
any POVM inside one whole original copy, adapt later measurements, and use
unlimited classical memory/computation. No quantum memory connects copies.
T is a fixed total copy cap, including discarded/failed measurements.
For the hard family q=rd,d>=2, a uniform ordered balanced partition of the q
coordinates into r blocks of size d and independent Haar lines within those
blocks are hidden and fixed throughout a transcript. They are not metadata.
The common reference is the same strategy on independent maximally mixed
q-dimensional inputs.

## D-R13-HERMITIAN-CONTENT-ENCODING

On N source registers set `X_k=sum_(i<k)S_(i,k)`, 2<=k<=N, with full-register
swaps. Let `alpha_BE,k=2^ceil(log2(k-1))` and use that many selection labels.
Prepare them uniformly with Hadamards. For labels i<k-1, SELECT acts as
`S_(i+1,k)` on data and identity on a padding-signal qubit; padded labels act
as identity on data and Pauli X on that signal. Conjugating SELECT by PREP
gives a Hermitian involution U_X,k. Its joint-zero projected block is
`A_k=X_k/alpha_BE,k`. This is a Hermitian projected-unitary encoding.

For a threshold t, add a selector with probabilities
`1/(1+|t|), |t|/(1+|t|)` and Hermitian SELECT branches `U_X,k,-sgn(t)1`.
The resulting Hermitian involution has projected block
`Y_t=(A_k-t1)/(1+|t|)`. At t=0 omit the identity branch. For content c use
thresholds `t_-=(c-1/2)/alpha_BE,k`, `t_+=(c+1/2)/alpha_BE,k` and reflection
`R_kc=-sgn(Y_t-)sgn(Y_t+)=2P_kc-1`. Spectral-edge constant signs may be
implemented directly. Odd bounded sign polynomials and Hermitian eigenvalue
QSVT act on signed eigenvalues, not their absolute values. All phase and
selector synthesis, leakage registers and controls are included in the
specified window-instrument error. No inverse Fourier transform is used.

## D-R13-CONTENT-WINDOW-BANK

For each k, `J_k=2k-1` integer windows cover its content spectrum. Pad to
`H_k=2^ceil(log2 J_k)` labels, with zero projectors on unused labels.
A trial draws a uniform label c and performs the binary projective instrument
with Kraus maps `P_kc,1-P_kc`. Thus the label-and-outcome Kraus maps carry
the factor `1/sqrt(H_k)`. On no, reuse the same data with fresh/reset ancillas;
on yes, return c. Stop after the stated cap L_k. All failures and resets count.
Its approximated version uses the QSVT reflection of the preceding definition.

## D-R13-BASIS-COMPILER-BUDGET

For r,delta as above define

    N=ceil(2r²), M=N(N-1)/2,
    A_move=ceil(log_4(8M)), K=(N-1)+A_move M,
    L_k=ceil(H_k log(256K)),
    W_cap=ceil(4KN[log(256K)+1]),
    A_cert=ceil(log(16)/log(4/3))=10,
    B_batch=ceil(log(1/delta)/log(8/5)), Q_quant=B_batch N.

W_cap bounds the total number of binary window tests per batch. Every actual
compiled test, including all phase-synthesis and discarded-work effects, must
have instrument diamond error at most `1/(256W_cap)`. The sign-polynomial
and clean-space leakage allocations are specified in the construction memo;
they give degree `O(k log W_cap)` with polynomial classical phase generation.
Only exact controlled permutations touch the source data. Approximate rotations
act on ancillary registers, preserving U^(tensor N) on every branch.

Initial content measurements give a tableau; valid adjacent swaps steer it
toward column-first order, with at most A_move attempts per move and at most
M moves. At the end, the first r registers undergo the padded signed-permutation
certificate below, retried at most A_cert times. Failure on a correctly steered
column leaves that column unchanged; no such reset promise is made on a bad
column. Every accepted certificate has exact exterior support.

Fresh batches are independent; on total failure return a fixed r-label set.
At delta=1/3 there are three batches and Q_quant=6r². Source/noise models
with correlated deliveries need a joint-state error bound; marginal-only
source error bounds do not justify a copywise hybrid argument.

## D-R13-SIGNED-CERTIFICATE

Let `h_r=2^ceil(log2(r!))` and `gamma_r=r!/h_r`, so 1/2<gamma_r<=1.
Prepare a uniform binary label of size h_r. Valid labels are reversibly
unranked to permutations pi and apply `sign(pi)T(pi)` to the r data registers;
invalid labels apply identity and carry a separate validity flag. Projection
onto the uniform-label/valid outcome gives the exact Kraus map
`gamma_r P_-^(r)`, where `P_-^(r)=(1/r!)sum_pi sign(pi)T(pi)`.
Every other label/validity outcome belongs to the complete instrument.
Factoradic unranking, padding and all controls are charged; no factorial-size
table or uniform-superposition oracle is supplied.

## D-R13-DIRECT-CERTIFICATE-FALLBACK

Apply the same certificate directly to r fresh flat-source copies. A batch
accepts with probability `gamma_r²/r^r`, and produces an exact exterior ray.
Repeat at most `ceil(4r^r log(1/delta))` independent batches, then use a fixed
fallback set. This costs `O(r^(r+1)log(1/delta))` copies. It is a separate
non-Fourier upper for slowly growing r; it is not the polynomial-r QSVT method.
