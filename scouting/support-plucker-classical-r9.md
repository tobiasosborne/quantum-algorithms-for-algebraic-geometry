# Candidate adaptive single-copy lower bound for support DPP sampling

2026-09-05. Root derivation for the active support-to-Pluecker audit
`qaag-9v2`. This proof is not promoted before independent review. It uses
ordinary finite-dimensional Hilbert spaces and locally defined dimensions,
departing from C1/C2. It does not establish a new quantum mechanism.

## 1. A same-output hard pair

Let H=A direct-sum B, with both blocks of dimension d>=2. Draw independent
Haar matrices U,V in U(d); write their columns u_i,v_i. Define rank-two
orthogonal projectors through these orthonormal spanning vectors:

`W_0=span(u_1 direct-sum 0, 0 direct-sum v_1)`,
`W_1=span((u_1 direct-sum v_1)/sqrt2, (u_2 direct-sum v_2)/sqrt2)`,
`rho_theta=P_(W_theta)/2`, `theta in {0,1}`.

Both source ensembles have one-copy average `tau=mathbb1_H/(2d)` and
block masses one half. Their projection DPP outputs are unordered two-element
subsets of the computational coordinates. Let E be the event that the subset
contains one A index and one B index. Its exact probabilities are

`Pr_0(E)=1`, `Pr_1(E)=1/2`.

For example, the total DPP mass entirely in A is
`det(U_A^dagger U_A)`: it is zero in case zero and one quarter in case one.
The same holds in B, proving the cross masses. These masses hold for every
choice of the hidden frames, not just on average.

## 2. Haar/Gaussian comparison in the required degree

Use independent d-by-d circular complex Gaussian matrices G,H whose entries
have variance 1/d. For any holomorphic polynomial F(U,V) of total homogeneous
degree N, claim

`E_Haar |F(U,V)|^2 >= c_N E_Gauss |F(G,H)|^2`,
`c_N=(d/(d+N-1))^N`.                                  (HG)

For a polynomial of homogeneous degree L in one matrix, the Cauchy
decomposition labelled by a partition lambda has Haar/Gaussian norm ratio

`d^L/C_lambda(d)`, `C_lambda(d)=product_((i,j) in lambda)(d+j-i)`.

Only partitions with at most d rows occur. Each factor is at most d+L-1,
so the ratio is at least `(d/(d+L-1))^L`. This is the same finite-dimensional
covariance comparison proved in `scouting/waring-terminal-baseline.md`; it
does not normalize Gaussian matrices as unitaries or as quantum states.

For two matrices, decompose F into bidegrees (L,N-L). Different bidegrees
are orthogonal for both measures by independent central-phase invariance.
The product of their two lower factors is at least c_N. Summing proves (HG).
The zeroth-degree factor is one. No restriction N<=d is needed for this lower
bound; no upper Haar/Gaussian comparison is being asserted here.

For homogeneous linear polynomials f_1,...,f_N in all Gaussian entries,
the Fock product inequality gives

`E_Gauss product_j |f_j|^2 >= product_j E_Gauss |f_j|^2`.   (GP)

Equivalently, the left side is the permanent of their positive semidefinite
covariance Gram matrix, and it is at least the product of its diagonal
entries. Homogeneity is important: no inhomogeneous product inequality
is used. The existing Fock creation-operator proof supplies (GP).

## 3. Every adaptive transcript has a common component

Consider any protocol using at most N source copies, arbitrary adaptive
single-copy POVMs and classical memory. Pad unused copies and refine each
effect to rank one, absorbing its positive scalar into its vector. A fixed
complete leaf fixes all the vectors z_1,...,z_N, even though their choices
were adaptive. Classical randomness can be conditioned on or included in
the leaf; it is independent of the hidden input ensemble.

Write rho_theta as the equal mixture of its two displayed spanning vectors
`w_(theta,a)`, a=1,2. For each fixed latent sequence a_1,...,a_N, set

`f_j(U,V)=<z_j,w_(theta,a_j)(U,V)>`.

Every f_j is homogeneous linear in the combined entries of U,V. In case
zero it uses only one matrix, while in case one it is a sum of terms from
both matrices. Its product has total degree N, so (HG) applies after
bidegree decomposition. Expanding the mixed-state leaf probability and
then using (GP) gives

`Pr_theta(leaf)`
` =2^(-N) sum_(a_1,...,a_N) E_Haar product_j |f_j|^2`
` >=c_N 2^(-N) sum_(a_1,...,a_N) product_j E_Gauss |f_j|^2`
` =c_N product_j [ (1/2)sum_(a=1)^2 E_Gauss
                         |<z_j,w_(theta,a)>|^2 ]`
` =c_N product_j <z_j,tau z_j>`.

The last equality uses only degree-one moments, which agree exactly for
Haar and the specified Gaussian normalization. It holds separately for
both theta. The right-hand product is the leaf law P_* of the same adaptive
protocol run on fresh copies of tau. It is a normalized common reference
law, not a Gaussian state-preparation experiment.

Consequently each averaged transcript law has the decomposition
`P_theta=c_N P_*+(1-c_N)Q_theta` for a probability law Q_theta. Thus

`TV(P_0,P_1)<=1-c_N<=N(N-1)/d`.                          (TV)

The second inequality is `(1+x)^(-N)>=1-Nx` with x=(N-1)/d.
Rank-one refinement cannot reduce the protocol's information, so this
bound applies to the original coarse records and to any classical output.
For continuous POVMs the same nonnegative-measure argument applies to the
leaf densities, or to finite measurable coarse-grainings of the final output.

## 4. Consequence for approximate DPP sampling

Suppose a single-copy protocol with copy cap N samples within TV epsilon
of the projection DPP for EVERY rank-two support in H, with epsilon<1/4.
Its averaged output probabilities for E differ by at least
`1/2-2 epsilon`. Output processing cannot increase transcript TV, so (TV)
requires

`N(N-1)>=d(1/2-2 epsilon)`.

In particular epsilon<=1/16 implies `N(N-1)>=3d/8`, giving an
Omega(sqrt(d)) lower bound. All measurements inside an original copy are
unrestricted; this is not a tomography comparator or a one-block-average
argument. The dimension convention here is q=2d, not d squared as in the
earlier Waring source. The theorem is for a fixed total copy cap, not yet an
expected-time stopping rule.

The quantum conversion, if its proved resource ledger is completed, uses a
source budget independent of q for fixed r=2 and fixed accuracy. Direct
two-copy antisymmetrization already has that q-independent property at r=2;
this lower bound does not establish novelty of the growing-r construction.
The separate novelty audit remains necessary and may reject its mechanism.
