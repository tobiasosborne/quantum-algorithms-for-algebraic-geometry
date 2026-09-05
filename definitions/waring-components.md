# Waring source, packet, and terminal-query definitions

2026-09-05. Ordinary tensor Hilbert norms are used, departing from C1. Here q
denotes a component Hilbert-space dimension and k a source tensor order.
No preparation circuit for the unknown source is implicit in copy access.

## D-WARING-SOURCE

For integers r>=2,q>=r,k>=3, let u_1,...,u_r be independent unit vectors in C^q
and let `T=sum_a c_a u_a^tensor k` be normalized, with all c_a nonzero. Copies
of T are supplied; the u_a, c_a, their Gram matrix G, and an inverse source
circuit are not supplied. Component rays are unordered. Define
`G_ab=<u_a,u_b>`, `G_m=G^(circ m)`, and
`p_0=|prod_a c_a|^2 det G det G_(k-1)`.
Let rho_1 be the one-slot reduced density matrix of the original T source.
When used, known lower promises are `G>=eta 1` and `p_0>=p_*`, with positive
eta,p_*. Source-generation gates G_T and workspace w_T are charged separately
if an actual preparation circuit is supplied rather than an external copy source.

## D-WARING-PACKET

For m>=1 and sigma in {0,1}, define
`w_m^sigma=sum_(pi in S_r) sgn(pi)^sigma tensor_(i=1)^r u_(pi(i))^tensor m`.
Write `N_sigma(m)=||w_m^sigma||^2` and `Omega_m^sigma=w_m^sigma/sqrt(N_sigma(m))`.
Define `Sigma_h=(1/r)sum_a |u_a><u_a|^tensor h` for h>=1.
Packets are quantum outputs; neither they nor Sigma_h are classical coordinate
descriptions of the Waring components.

## D-WARING-CODED-FUSION

Let b=ceil(log_2 r). Give row i the binary code of i-1 and let S_j contain
the rows with bit j equal to one. Guard j selects one unused register from
packet-A row i for i in S_j and from packet-B row i otherwise, ordered by row i.
It applies the alternating projector
`P_alt,r=(1/r!)sum_(tau in S_r)sgn(tau) U_tau`.
All b guards use disjoint physical registers. Accept only if every guard
accepts, then discard their registers and regroup each pair of remaining rows.
The guard model for the restricted optimality claim allows exactly such
complementary-row all-distinct tests, with all-accept postselection.

For equal-size recursive fusion starting from degree k-1, define
`m_j=b+(k-1-b)2^j`, requiring k>=b+2. A seed consumes r original source copies
per attempt. For promised bounds define
`f_*=eta^(r(b+1))/(r!)^(b+3)` and
`Cbar_j=(r/p_*)(2/f_*)^j`.
They are proposed resource bounds, whose validity is C-344.

## D-WARING-TERMINAL-QUERY

Fix r=k=4, q=d^2,d>=20, with a supplied factorization C^q=C^d_A tensor C^d_B.
The original source Hilbert space is W=Sym^4(C^d_A tensor C^d_B).
Use D-WARING-SOURCE with `G>=1/2` and `p_0>=1/512`. For the unique Waring rays,
let `rho_A(u)=Tr_B|u><u|` and
`Gamma(T)=(1/4)sum_a e_5(rho_A(u_a))`.
Here e_5 is the fifth elementary symmetric polynomial of eigenvalues, equivalently
the sum of squared 5-by-5 minors of the normalized component coefficient matrix.
The promise is `Gamma(T)=0` or `Gamma(T)>=gamma=10^(-6)`; output the appropriate
YES/NO bit with success at least 2/3. No separate query state is provided.

The comparator may perform arbitrary adaptive global POVMs on every register
of one whole original T copy at a time, with arbitrary within-measurement
ancillas and unlimited classical computation, memory and randomness. Quantum
information from a copy may not be retained while processing the next copy.
This is a copy-access comparison, not an explicit classical coefficient-list model.

## D-WARING-DIRECT-POINT-TEST

For D-WARING-SOURCE with k>=3, let Q be the accepting positive-contraction
POVM effect of a supplied implemented two-outcome measurement on h copies of
a component, with 1<=h<=2k-2. Its measurement cost is charged; a mere block
encoding of the linear operator Q is not this access model. Put
`f_a=<u_a^h,Q u_a^h>` and `Gamma_Q=(1/r)sum_a f_a`.
One trial uses r+1 original T copies. Seed by alternating one slot from each
of the first r sources. Choose packet row 1; then alternate one unused slot
from each other packet row and one slot of the extra source. Measure Q on
h unused slots of the merged selected row, and record an event only when all
three measurements accept. The seed, guard and point measurement use disjoint
physical registers. Define the promised event coefficient
`alpha_point=p_*^2 eta^(3r-2)(r-1)^(r-1)/r!`.
Its correctness is C-347, not an assumed oracle normalization.
