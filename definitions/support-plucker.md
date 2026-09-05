# Support-to-Pluecker conversion and its sampling comparator

2026-09-05. This task uses ordinary finite-dimensional Hermitian tensor
spaces, departing from C1. The local dimension q is independent of the
seed's variable convention C2. U denotes a physical Hilbert support, and
Omega_U uses its coefficient vectors directly: identifying U itself with
the Grassmannian point is a declared C3 departure, with no conjugation gate.
The coordinate-volume probabilities are unchanged by complex conjugation.

## D-SUPPORT-PLUCKER-INPUT

The source supplies independent copies of a density operator rho on H=C^q,
with known rank `1<=r<=q` and known `0<eta<=1` such that each nonzero
eigenvalue is at least eta/r. Set `U=range(rho)` and let P_U be its orthogonal
projector. Each physical register uses the first q basis states of
`w=ceil(log_2 q)` qubits. A source-copy cost is charged separately.
Copies do not supply a support basis, coefficient queries, QRAM, a purification
register, controlled preparation or a preparation inverse.

## D-SUPPORT-PLUCKER-OUTPUT

For any orthonormal basis u_1,...,u_r of U, define

`Omega_U=(r!)^(-1/2)sum_(pi in S_r) sign(pi)`
`                         u_(pi(1)) tensor ... tensor u_(pi(r))`.

Its ray is the one-dimensional exterior space wedge^r U and is independent
of the chosen basis. The quantum output is this ray in r registers, with
a success flag. Its allowed failure probability is `0<delta<=1/3`.

The corresponding classical output is a sorted r-element coordinate subset J,
with projection-DPP law `Pr(J)=det(P_U[J,J])`. It is normalized; it is not
the unconditioned DPP with correlation kernel rho. For an always-output
approximate sampler, replace a failed quantum run by a fixed subset J_0.
Failure at most delta then gives unconditional total-variation error at most
delta. In the uncapped exact version, repeat batches until the first success.

## D-SUPPORT-TABLEAU-OPERATORS

On N source registers, T(pi) permutes tensor factors, `S_ij=T((i j))`,
and `X_1=0`, `X_k=sum_(i<k) S_ik`. Use the Schur--Weyl decomposition
`H^tensor N=direct-sum_lambda Q_lambda(H) tensor V_lambda`.
Here V_lambda has the orthonormal Young branching basis of standard tableaux.
For b in that basis, `c_b(k)=column_b(k)-row_b(k)` and
`E_b=mathbb1_(Q_lambda(H)) tensor |b><b|`, extended by zero elsewhere.
The isotypic projector is P_lambda. English Young diagrams and their
coordinatewise box order are used. The target b_0 reads each column from
top to bottom, then proceeds left to right. If lambda has r rows, its first
r boxes form the first column. `P_-^(r)` antisymmetrizes the first r registers.

All content/shape measurements in the conversion are Lueders instruments:
compute the eigenlabel coherently, copy the desired label, uncompute the
work circuit, then measure only the copy. Merely discarding unmeasured
Fourier indices is not this instrument.

## D-SUPPORT-STEERING-BUDGET

For r>=2, define

`N=ceil(2 r^2/eta)`, `M=N(N-1)/2`,
`A=ceil(log_4(4M))`, `K=(N-1)+AM`,
`m=ceil(log_2(2N))`, `nu=1/(256K)`,
`L=ceil(40mN^2/nu)`, `B=ceil(16 ln(1/delta))`.

N is the number of source copies per batch; A caps retries of each valid
adjacent-tableau move; K caps content measurements; L is the first-order
swap-exponential product-formula repetition count. B caps independent batches.
The exact final certificate uses `a=ceil(log_2(r!))`, `h=2^a`, and
`gamma_r=r!/h`: a uniformly padded binary permutation register gives the
Kraus operator `gamma_r P_-^(r)`. All data operations remain controlled
permutations, including when ancilla phases are approximated. The model
assumes noiseless finite gates and the exact input-support promise; arbitrary
physical noise is not declared support-preserving. For r=1, return one copy.

## D-SUPPORT-CLASSICAL-COPY-MODEL

The comparator receives the same rho copies, can apply any global POVM
within one complete copy, and may choose later POVMs adaptively using
unlimited classical memory and computation. It retains no quantum memory
connecting distinct source copies. The approximate sampling task must always
output a subset, with total-variation error at most epsilon for every promised
rho. A lower bound with total copy cap T concerns a fixed cap, including all
failed or postselected events. It is not an expected-stopping-time bound.

The exact sampling question allows failure flags or almost-sure finite
stopping, but demands the exact conditional projection-DPP law whenever it
succeeds. The nonexistence result concerns `2<=r<q`. Rank one and full
support have elementary classical exact samplers and are excluded.

## D-SUPPORT-BLOCK-PAIR

For the quantitative lower bound take q=2d, d>=2, H=H_A direct-sum H_B,
with known d-dimensional coordinate blocks. Draw independent Haar matrices
G_A,G_B in U(d) once for the entire run, with columns u_i,v_i. Define

`W_0=span(u_1 direct-sum 0, 0 direct-sum v_1)`,
`W_1=span((u_1 direct-sum v_1)/sqrt2,(u_2 direct-sum v_2)/sqrt2)`,
`rho_theta=P_(W_theta)/2`, `theta in {0,1}`.

These are rank-two flat sources and satisfy eta=1. Copies are independent
conditional on the fixed hidden frames; the frames are not redrawn per copy.
Both ensemble means equal `tau=mathbb1_H/(2d)`. The DPP event E is that
the two output indices lie in different blocks. The separate decision task
distinguishes the two displayed families at success at least 2/3 in each case.

In the transcript proof, set `c_T=(d/(d+T-1))^T`. Auxiliary Gaussian
matrices have independent circular complex entries of variance 1/d; they
are only holomorphic-polynomial comparison variables, not normalized source
states. The proof keeps the coherent off-diagonal blocks of rho_1.
