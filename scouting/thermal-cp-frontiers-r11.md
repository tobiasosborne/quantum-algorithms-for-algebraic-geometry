# Thermal-state and completely-positive-map frontiers, R11

2026-09-07. Construction memo, not a claims file. This lane was asked to derive
before searching. Sections 1--5 record those derivations; section 6 records the
subsequent primary-source checks. No row below is promoted to a campaign claim.
In particular, "finalist" means only that its map, algebraic meaning and resource
ledger are concrete enough for an adversarial round. It does not mean that D22 or
a speedup has been established.

Opening convention departures: local `D` denotes the operated finite Hilbert
space dimension (departure from C8), and local `alpha` and its subscripts denote
physical block/Kraus normalization scales (departure from C7). They do not
silently identify a presentation norm with a geometric invariant. Arbitrary
homogeneous generators in the Gram identity need not satisfy C5; the explicit
quadratic control below does use unit Bombieri--Weyl generators.

Canonical integrated objects are in `definitions/thermal-cp-r11.md`.

## 1. Common accounting and tournament rules

Write \(R=\mathbb C[z_0,\ldots,z_n]\), \(M_N=\binom{N+n}{n}\), and give every
homogeneous piece its Fock inner product. A finite input must provide either
(a) coefficient/sparse-access circuits for the named matrices and polynomials,
or (b) circuits for the stated projectors, channels or state preparations. These
are different models. A succinct quantum oracle is also available to the
classical comparator as a circuit description or query oracle; an exponential
separation is never inferred merely from \(\log D\) qubits holding a
\(D\)-dimensional state.

For every channel call, \(C_{\cal E}\) denotes its gate cost, \(a_{\cal E}\) its
work qubits, and \(\epsilon_{\cal E}\) its diamond-norm implementation error.
A physical run charges elapsed evolution time, every fresh bath register, and
every active reset. Reusing the system between steps is allowed; obtaining a new
copy of its evolving state is not. Preparing a Gibbs state costs a named
\(C_{\rm Gibbs}(\beta,\epsilon)\), and convergence for time \(t\) costs \(t\),
normally through a supplied dissipative gap or log-Sobolev promise. A heralded
branch of probability \(p\) costs \(O(p^{-1}\log(1/\delta))\) fresh trials, or
\(O(p^{-1/2}\log(1/\delta))\) coherent uses only when the inverse dilation and
reflections required for amplification are supplied.

The tournament rejects a proposal if its exact output is input-level, if a
normalizer/projector/inverse has merely been moved into an oracle, or if the same
output has a matched classical trajectory. It separately marks D22 failure when
the operation reduces substantively to known Gibbs sampling, generic Lindblad
simulation, heat-kernel filtering, phase/singular-value estimation, quantum
walks, amplitude estimation, or Zeno/holonomic transport.

## 2. Wide candidate table

The costs use \(D\) for the operated Hilbert-space dimension, \(L\) for a Kraus
label or Macaulay-domain dimension, \(s\) for row sparsity, \(\eta\) for a
normalised positive spectral/dissipative gap, \(p\) for heralding weight, and
\(\varepsilon,\delta\) for additive error and failure probability.

| id | exact common input and output/promise | CP, thermal or physical operation | full leading costs and strongest classical attack | tournament result and decisive next derivation |
|---|---|---|---|---|
| T01 | Homogeneous tuple \(f_j\), degree \(d\), sparse coefficient access; estimate \(\dim\ker F_d/L\) for the Macaulay map \(F_d:\oplus_jR_{d-m_j}\to R_d\), promised \(\sigma_{\min}^2(F_d)/\alpha^2\ge\eta\). | A bath-emission isometry has labelled jumps \(a(gf_j)\); its environment Gram matrix is a scalar multiple of \(F_d^\dagger F_d\). Equivalently an absorbing Lindblad no-jump probability is the heat trace of \(F_d^\dagger F_d\). | \(O(C_F\eta^{-1}\log(1/\varepsilon)\varepsilon^{-2}\log(1/\delta))\) gates/time-samples, \(O(\log(L+M_d)+a_F)\) qubits, and simulation error \(O(\varepsilon)\). Conditional emission additionally costs \(p^{-1}\). Classical sparse rank/block Wiedemann or randomized heat-trace estimation attacks the same matrix in \(\widetilde O(\operatorname{nnz}(F_d)\,k)\) work and \(O(L+M_d)\) words, with conditioning-dependent \(k\). | **Finalist A, conditional.** Exact AG map and no quotient-state overlap; likely a known rank/heat-trace algorithm after compilation. Prove or refute a same-oracle time/space separation for a non-squarefree family. |
| T02 | A loop \(P(s)\) of equal-rank harmonic or quotient subspaces supplied by projector circuits; estimate an additive \(\varepsilon\) normalised character of the metric Kato holonomy. The output is not called Gauss--Manin unless an intertwiner is separately proved. | Reset-completed projection channel \({\cal E}_j(\rho)=P_j\rho P_j+\operatorname{Tr}(Q_j\rho)P_j/r\); retain the no-reset trajectory \(P_m\cdots P_1\). | \(m=O((\Lambda^2+K)/\varepsilon)\) projector calls under derivative bounds, \(O(mC_P\varepsilon^{-2}\log(1/\delta))\) total gates for a Hadamard/trace estimate, and \(m\) bath records or charged resets. Classical transports an explicit \(D\times r\) frame in \(O(m\operatorname{cost}(P\text{-matvec})r)\). | **Finalist B as a control, D22 fails presently.** General quantum-operation Zeno holonomy is prior art. Establish an AG family where the metric connection itself is the requested invariant and fair \(P(s)\) access is cheaper quantumly, or drop. |
| T03 | D-R11-TRIPLE-QUOTIENT-QUERY: degree-one harmonic inputs a,b,c in a finite Hermitian DGA, exact pair products, positive gap, and explicitly supplied coherent Hodge/quotient access; decide theta=0 versus theta>=gamma for the plus-sign Massey quotient norm. | Two multiplication/Green branches are added coherently with factor 1/2 and followed by the supplied quotient projector Pi; Section 5 gives every successful and failure block. | With actual Kraus scales alpha_h,alpha_mu and beta=2 alpha_h alpha_mu², regularization error and conservative Bernoulli cost are stated in Section 5. Constructing Pi from geometric equations is unsolved and charged separately. Explicit-vector access allows two sparse Green solves and quotient linear algebra; succinct circuits do not grant free classical amplitudes. | **Held conditional compiled primitive.** The exact common output is defined, but its geometric input-to-projector construction, advantage and original mechanism are unproved; displayed Green/LCU processing is known. |
| T04 | Finite complex \((C,d)\), chain symmetry \(G\), and maximally mixed chain input; estimate \(\operatorname{Str}(G e^{-t\Delta_H})/D\). | Absorbing no-jump channel \(K_0=e^{-t\Delta_H/2}\) and a controlled parity-\(G\) interferometer. | \(O(C_{\Delta}t\varepsilon^{-2}\log(1/\delta))\), with no low-temperature preparation. Classical computes \(\operatorname{Str}(G|C)\) directly. | **Rejected decisively.** Equivariant supersymmetric cancellation gives \(\operatorname{Str}(Ge^{-t\Delta_H})=\operatorname{Str}(G|H)=\operatorname{Str}(G|C)\); the thermal experiment adds no information. |
| T05 | Degree blocks of \(R/I\), adjacent compressed multiplication access, and Betti-gap promise; estimate a normalised graded Betti number. | Davies or engineered cooling of the compressed Koszul Laplacian, followed by fermion/degree readout. | \(C_{\rm Gibbs}(\beta,\varepsilon)\) with \(\beta\ge\Delta^{-1}\log(D/\varepsilon)\), plus ground-space preparation weight \(M_N/h_N\) in generator mode and \(O(\varepsilon^{-2})\) reads. Classical sparse Hodge/Koszul rank; squarefree pieces reduce to simplicial Betti computation. | **Rejected as a frontier candidate.** This is the settled Koszul/SUSY construction with Gibbs sampling added; it inherits the Hilbert-weight and gap failures and violates D22. |
| T06 | Homogeneous ideal generators and degree cutoff \(N_{\max}\); sample degree from \(\rho_q\propto\sum_Nq^NP_{W_N}\) or estimate a ratio of its partition function. | Pump/loss reservoir with compressed creation and annihilation jumps, detailed balance ratio \(q=e^{-\beta}\). | Mixing time \(\tau_{\rm mix}\), construction of every \(P_{W_N}\), partition normalisation/annealing, and \(O(\varepsilon^{-2})\) samples; storage \(O(\log\sum M_N)\). Classical Hilbert-series/standard-monomial DP or Markov-chain sampling. | **Rejected in stated access.** The jumps already contain the quotient projectors; without them the stationary law is not the Hilbert series. With them this is known Gibbs sampling. |
| T07 | Sparse monomial ideal and a connected graph on its standard monomials; sample from a prescribed Gibbs weight and estimate a bounded geometric statistic. | Classical Metropolis transitions embedded as rank-one Kraus operators \(K_{yx}=\sqrt{P(y|x)}|y\rangle\langle x|\), optionally coherently dilated. | \(O(\tau_{\rm mix}\varepsilon^{-2}\log(1/\delta))\) steps and fresh random coins/bath records. Classical executes exactly the same Markov chain with the same mixing bound and smaller memory. | **Rejected by matched trajectory.** Coherent quantisation would become an established quantum-walk speedup and still needs a gap. |
| T08 | A finite-dimensional quotient algebra \(A\), contraction multiplication maps \(B_i\), and maximally mixed input; estimate \(\operatorname{Tr}(B_w^\dagger B_w)/D\) for a word \(w\). | Recycle the successful internal state through the trace-decreasing maps \(B_i\); complete each by a permanently flagged failure Kraus operator. | One word trial costs \(\sum_iC_{B_i}\); additive estimation costs \(O(\varepsilon^{-2}\log(1/\delta))\) trials, while a nonzero threshold \(\gamma\) costs \(O(\gamma^{-1})\). Classical Hutchinson trace estimation applies the same word and adjoint to random vectors. | **Rejected only with classically applicable table/sparse matvec access.** The same trace is estimated by random-vector matvecs. A succinct quantum circuit does not provide an efficient classical matvec; that model remains held without a same-output lower bound. Retained-state implementation alone is not a D22 novelty proof. |
| T09 | An Artinian algebra \(A\), multiplication by \(\ell\), nilpotency cap \(r\), and a singular-value gap; recover the ranks of \(m_\ell^k\), hence its Jordan type and, under a strong-Lefschetz promise, the Hilbert vector. | Absorbing no-jump dynamics generated by \(m_\ell^{\dagger k}m_\ell^k\); survival at long time gives \(\dim\ker m_\ell^k/D\). | For all \(k\le r\), \(\widetilde O(rC_m\eta^{-1}\varepsilon^{-2})\) and errors small enough to round ranks require \(\varepsilon<1/(2D)\), hence exponential sampling when an exact Hilbert vector is requested. Classical sparse ranks of powers/Jordan algorithms. | **Held only for coarse normalised Jordan profiles.** The exact invariant has a readout barrier. Nilpotence here is finite transient absorption, never a peripheral Jordan block of a CPTP map. |
| T10 | A polynomial potential \(W\) with isolated critical scheme and an implementable Witten Laplacian; sample a critical component or estimate the Milnor number fraction. | Couple the supersymmetric system to a cold bath so harmonic/Jacobian states are dark; monitor jump cessation. | \(C_{\rm Gibbs}\) or cooling time \(\Omega(\Delta_W^{-1}\log(1/\varepsilon))\), initial dark overlap, spatial discretisation and truncation, then \(O(\varepsilon^{-2})\) samples. Classical Jacobian Gröbner/Macaulay rank or critical-point homotopy. | **Rejected as stated.** Prior quantum-SUSY/Jacobian proposal plus generic cooling; smooth hypersurface families also have closed-form Milnor counts. |
| T11 | A coherent sheaf complex with a supplied local Hodge Laplacian and observables \(A,B\); estimate static Kubo susceptibility \(\int_0^T\!\operatorname{Tr}(\rho_\beta A(t)B)dt\), interpreted through the Green operator. | Prepare \(\rho_\beta\), evolve under a detailed-balance Liouvillian, and use an ancilla to retain the sign/phase of the two-time correlation. | \(C_{\rm Gibbs}+O(TC_{\cal L}\varepsilon^{-2})\), with \(T=\Omega(\eta^{-1}\log(1/\varepsilon))\), correlation decay and Gibbs normaliser charged. Classical sparse resolvent/Krylov and stochastic trace. | **Folded into T03.** Linear response is a useful physical realisation, not yet a distinct algorithmic mechanism. |
| T12 | A family of channel Kraus matrices polynomial in parameters; decide whether the Choi rank is at most \(r\), under a smallest-nonzero-eigenvalue promise. | Feed half of maximally entangled pairs through the channel and cool/filter the Choi density matrix; exterior-power antisymmetrisation detects rank. | At least \(r+1\) channel uses per exterior-power trial; probability is an elementary symmetric polynomial of the Choi spectrum and can be exponentially small. Exact rank needs spectral resolution. Classical explicit Choi rank, or process queries/tomography in black-box access. | **Rejected for D22.** This is standard spectrum/rank testing or universal comparison applied to the determinantal Choi variety. |
| T13 | Supplied ideal projectors P_I,P_J and an initial-state circuit; estimate the heralded no-reset alternating-projection probability. | Apply the projector dilations and retain the entire success record; the accepted branch is their ordered product. A reset-completed channel is a separate optional process. | Charge every projector call, preparation and total survival probability. Principal angles describe the accepted projector product; the full reset-channel spectrum also depends on the reset states. Classically applicable projector matvecs give a matched randomized trace-product estimator. | **Displayed no-reset mechanism rejected for novelty.** No decay-spectrum theorem or efficient classical simulator is claimed for arbitrary reset-completed succinct channels. |
| T14 | A flat family of ideals with a discriminant-avoiding loop and a faithful finite-temperature state \(\rho(s)\); estimate an ordinary Uhlmann Chern number. | Purify \(\rho(s)\) and parallel-transport amplitudes by the Uhlmann condition. | State preparation, fidelity inverses near small eigenvalues, path discretisation and interferometric reads. Classical diagonalisation/parallel transport. | **Rejected as phrased.** The full-rank Uhlmann bundle has trivial ordinary Chern classes; nonzero finite-temperature indicators change the observable. Rank-deficient limits collapse back to support-projector transport. |
| T15 | A finite algebraic correspondence encoded by Kraus maps \(A_e\); estimate a stationary expectation of its CP transfer operator. | Iterate \(\Phi(\rho)=\sum_eA_e\rho A_e^\dagger\), or a detailed-balance completion, until its invariant density is reached. | \(O(C_\Phi\tau_{\rm mix}\varepsilon^{-2}\log(1/\delta))\), including compilation of the TP completion and stationary-state uniqueness promise. Classical power iteration/Monte Carlo on the same transfer operator. | **Held as a problem source, not an algorithm.** A concrete correspondence needs a quantum-only interference observable; explicit-state power iteration is a comparator, while an efficient sampler under general succinct-channel access is not established. |
| T16 | A cover and finite Čech complex with restriction maps; estimate a normalised cohomology dimension. | Local bath jumps enforce pairwise gluing, making harmonic Čech cocycles dark states. | Lindblad construction and simulation, \(\eta^{-1}\log(D/\varepsilon)\) cooling, initial dark overlap, \(O(\varepsilon^{-2})\) readout. Classical sparse Čech-Laplacian rank/Krylov. | **Rejected as generic.** It is Hodge-Laplacian ground-space estimation under another name. |

The first cut retains T01, T02, T03 and the coarse-output version of T09.
T09 loses the final seat because exact Jordan/Hilbert data require additive
precision \(1/D\), while its coarse Schatten/rank profile has no current
intrinsic application. T02 remains deliberately as a calibrated control: it is
the cleanest finite-time channel, and the source check supplies a strong prior-art
reduction against which a real escape must differ.

## 3. Finalist A: a syzygy-emitting bath and absorbing heat trace

### 3.1 Exact algebraic map

Let \(f_j\in R_{m_j}\), fix \(d\ge\max_jm_j\), and put

\[
 {\cal D}_d=\bigoplus_jR_{d-m_j},\qquad
 F_d:{\cal D}_d\longrightarrow R_d,\quad(h_j)_j\mapsto\sum_jh_jf_j.
\]

Choose orthonormal monomial bases in all Fock sectors. Index a basis of
\({\cal D}_d\) by \(a=(j,g)\), and write \(p_a=gf_j\). Thus the coefficient
matrix of \(F_d\) has columns \(|p_a\rangle\). Its kernel is exactly the
degree-\(d\) syzygy space of the supplied tuple. It is not generally a minimal
Betti number; redundant generators remain visible.

For any \(N\ge d\), define

\[
 V=\sum_{a=1}^{L}|a\rangle_E\otimes a(p_a):R_N\to
 \mathbb C^L\otimes R_{N-d}.
\]

Choose a supplied/computed \(\alpha^2\ge\|V^\dagger V\|\). The two-outcome
isometry

\[
 W|\psi\rangle=|s\rangle\,V|\psi\rangle/\alpha+
 |f\rangle\sqrt{I-V^\dagger V/\alpha^2}|\psi\rangle                 \tag{1}
\]

is trace preserving because \(W^\dagger W=I\). The square root is a real
compilation cost, not a free Kraus operator. If a larger unitary dilation is
used, its inverse is also needed for coherent amplification.

Input the fixed-number infinite-temperature state \(\tau_N=I_{R_N}/M_N\).
After outcome \(s\), trace out the residual \(R_{N-d}\). The unnormalised bath
state has entries

\[
 (\widetilde\sigma_E)_{ab}={1\over M_N\alpha^2}
 \operatorname{Tr}_{R_N}\!\left[a(p_b)^\dagger a(p_a)\right].       \tag{2}
\]

Under convention C3, \(a(p)=\overline p(\partial)\) is conjugate-linear in
\(p\). Consequently the \((a,b)\) entry in (2) has the same, rather than the
transposed, conjugation order as \(\langle p_a,p_b\rangle\). If one instead
uses the unconjugated differential convention, (4) becomes
\((F_d^\dagger F_d)^T\) and its kernel is the coefficientwise conjugate
syzygy space. This convention check is essential.

The Hilbert--Schmidt pairing in (2) is \(U(n+1)\)-invariant on the irreducible
space \(R_d\), hence it is a scalar multiple of the Fock pairing. Evaluate the
scalar at \(p=z_0^d/\sqrt{d!}\). Since
\(a(p)=a_0^d/\sqrt{d!}\),

\[
 \|a(p)\|_{\rm HS,R_N}^2
 =\sum_{|\nu|=N}{\nu_0^{\underline d}\over d!}
 =\sum_{|\nu|=N}\binom{\nu_0}{d}
 =\binom{N+n}{N-d}=:c_{N,d}.                                      \tag{3}
\]

The last identity follows by taking the coefficient of \(x^N\) in
\(x^d(1-x)^{-(d+1)}(1-x)^{-n}\). Therefore

\[
 \widetilde\sigma_E={c_{N,d}\over M_N\alpha^2}F_d^\dagger F_d,
 \qquad \ker\widetilde\sigma_E=\ker F_d.                           \tag{4}
\]

This is an exact AG interpretation of a physical bath state. It prepares the
row-space Gram state without first preparing quotient ground states. Syzygies
are ZERO-weight directions of that bath state, so measuring it does not sample
them or estimate their dimension. The coefficient-register absorption process
in the next section is a separate operational nullity estimator.
Its own emission probability is

\[
 p_s=\operatorname{Tr}\widetilde\sigma_E
 ={c_{N,d}\|F_d\|_F^2\over M_N\alpha^2},                           \tag{5}
\]

so conditioning on a normalised bath state still costs \(p_s^{-1}\) trials.

### 3.2 Trace-preserving absorbing realisation and convergence

There is a direct formulation on the coefficient register \({\cal D}_d\).
Let \(B=F_d/\alpha_F\), where \(\alpha_F\ge\|F_d\|\), and let an absorbing
sink hold the image. With jump operator
\(J=|1\rangle\langle0|\otimes B\), the Lindblad generator is

\[
 {\cal L}(\rho)=J\rho J^\dagger-\tfrac12\{J^\dagger J,\rho\}.       \tag{6}
\]

The full semigroup is CPTP. The no-jump Kraus operator on the live sector is
\(K_0(t)=e^{-tB^\dagger B/2}\); all jump-time Kraus operators complete it to
a trace-preserving channel. Starting with \(I_L/L\), the probability of still
being live is

\[
 q(t)={1\over L}\operatorname{Tr}e^{-tF_d^\dagger F_d/\alpha_F^2}.
                                                                        \tag{7}
\]

If every nonzero eigenvalue of \(F_d^\dagger F_d/\alpha_F^2\) is at least
\(\eta\), and \(s_d=\dim\ker F_d\), then

\[
 0\le q(t)-s_d/L\le (1-s_d/L)e^{-t\eta}\le e^{-t\eta}.              \tag{8}
\]

Thus \(t=\eta^{-1}\log(2/\varepsilon)\) makes the finite-time bias at most
\(\varepsilon/2\). Hoeffding sampling with
\(R=O(\varepsilon^{-2}\log(1/\delta))\) independent preparations estimates
\(s_d/L\) to additive \(\varepsilon\). Total physical evolution is \(Rt\),
not \(t\). For expectation estimation, allocate finite-time bias and
uniform per-trial simulation probability bias at most \(\varepsilon/4\)
each, and reserve \(\varepsilon/2\) for sampling error. Taking
\(t=\eta^{-1}\log(4/\varepsilon)\) suffices. Simulation precision need
not be divided by the number of independent trials. One run uses
\(O(\log L+\log M_d+a_F)\) qubits. A single persistent state supplies one
Bernoulli datum at time \(t\), not fresh samples at all earlier times.

### 3.3 A complete non-squarefree control and matched classical sampler

Take `I=(z0²,z1²)` in `n+1>=2` variables and `d>=4`. Both generators have
unit Bombieri--Weyl norm; use Fock-orthonormal domain monomials. For a degree-d
monomial gamma, direct multiplication gives

    (F_d F_d†)|gamma> = s_gamma |gamma>,
    s_gamma=gamma0(gamma0-1)+gamma1(gamma1-1).

Thus `alpha_F²=d(d-1)` is the exact squared operator norm, and the normalized
positive gap is `eta=2/[d(d-1)]`. The tuple's single Koszul syzygy gives
`dim ker F_d=M_(d-4)`, with `L=2M_(d-2)`. If `d~c n` for fixed positive c,
the normalized nullity tends to `c²/[2(c+1)²]`. Exponential matrix dimension,
a polynomial gap, and a resolvable syzygy fraction coexist on this family.

At ambient degree `N=d`, the emitter uses the same squared normalization and
has success probability `4/[(n+1)(n+2)]`. Indeed the uniform Fock basis has
`E[gamma_j(gamma_j-1)]=2d(d-1)/[(n+1)(n+2)]`. The emitter's cost therefore
also has only polynomial rejection overhead on this control.

Row/column locations use reversible exponent addition/subtraction and at most
two contributing columns per row. The nonzero entries are square roots of
integer falling factorials with O(log d) bits before approximation. A compiled
contraction can coherently combine these at most two columns, apply the
normalized controlled rotation, and retain a failure flag. Index arithmetic,
rotation precision and Fock-sector preparation have polynomial cost in
`n,log d,log(1/epsilon_impl)`; no precomputed syzygy basis is required.

There is nevertheless an exact same-output classical sampler. Sample one
uniform domain column `(j,alpha)`, put `gamma=alpha+2e_j`, and let
`c_gamma` be the number of indices i in {0,1} for which `gamma_i>=2`.
This samples gamma with weight `c_gamma/L`. Its Gram block has one bright
eigenvalue `s_gamma` and `c_gamma-1` dark eigenvalues. Choose the bright branch
with probability `1/c_gamma`, otherwise the dark branch. Dark survives with
probability one; bright survives with probability
`exp(-t s_gamma/[d(d-1)])`. The resulting live bit has exactly q(t).
Uniform weak-composition sampling and scalar evaluation are polynomial in
`n,log d` and the charged precision. The limiting fraction also has the closed
binomial formula above. No quantum advantage exists for this proposed output
on this control under these common interfaces.

For other explicit sparse families, randomized Chebyshev/Krylov heat-trace
methods may require only roughly `eta^(-1/2)` polynomial degree where literal
dissipative time uses `eta^(-1)`; the actual approximation bound must be charged.
For general succinct quantum circuits, no efficient classical matvec or sampler
is inferred. The conditional absorption theorem remains a known heat-kernel
nullity mechanism; a natural hard family and a different observable/mechanism
are still missing. This control refutes neither all nonreduced schemes nor
all possible bath observables.

## 4. Finalist B: reset-completed projector transport

### 4.1 Channel and invariant states

Let \(P_j\) be rank-\(r\) orthogonal projectors in a common \(D\)-dimensional
space and \(Q_j=I-P_j\). Choose bases \(g_{j,a}\) of \(P_j\) and \(e_{j,b}\)
of \(Q_j\). Define Kraus operators

\[
 K_{j,0}=P_j,\qquad K_{j,ab}=r^{-1/2}|g_{j,a}\rangle\langle e_{j,b}|.
                                                                        \tag{9}
\]

They obey
\(K_{j,0}^\dagger K_{j,0}+\sum_{a,b}K_{j,ab}^\dagger K_{j,ab}=P_j+Q_j=I\),
and hence implement

\[
 {\cal E}_j(\rho)=P_j\rho P_j+\operatorname{Tr}(Q_j\rho)P_j/r.     \tag{10}
\]

Every density operator supported in \(P_j\) is fixed, and every fixed density
operator is supported there: applying \(Q_j(\cdot)Q_j\) to (10) proves the
converse. Implementing the reset term requires a basis/preparation of \(P_j/r\);
a bare membership projector does not supply it.

Monitor whether Kraus label \(0\) occurs. Starting in \(P_0\), the no-reset
branch after a discretised loop is

\[
 A_m=P_mP_{m-1}\cdots P_1P_0.                                      \tag{11}
\]

If \(P(s)\) is differentiable and \(\|\dot P(s)\|\le\Lambda\), then for a
unit vector in \(P_{j-1}\),
\(\|Q_j\psi\|\le\|P_j-P_{j-1}\|\le\Lambda/m+O(m^{-2})\).
Consequently a union/product bound gives

\[
 \Pr[\hbox{some reset}]\le \Lambda^2/m+O(m^{-2}).                   \tag{12}
\]

With a second-derivative bound \(\|\ddot P\|\le K\), the standard product
limit of projections makes (11), restricted to \(P_0\), converge to Kato
parallel transport with operator error \(O((\Lambda^2+K)/m)\). Equation (12)
also proves that heralding does not carry an exponentially small path weight
when \(m\) is chosen polynomially.

### 4.2 Exact geometric scope and resources

For a smooth loop of homogeneous ideals with constant Hilbert function, one can
embed the degree-\(N\) quotients or harmonic representatives into the common
ambient \(R_N\) and take their orthogonal support projectors. Equation (11)
then measures holonomy of the **metric Kato connection on this embedded bundle**.
That is an algebraic-family-derived observable, but it is generally not the flat
Gauss--Manin connection. Equality requires a proved intertwiner compatible with
the chosen metric; it is not supplied by flatness of the family.

A concrete benchmark is the Dwork pencil
\(X_\psi:\sum_{i=0}^{n}x_i^{n+1}-(n+1)\psi\prod_i x_i=0\), along a loop
avoiding \(\psi^{n+1}=1\), using a fixed graded piece of its Jacobian quotient
embedded in \(R_N\). The output declared here is the Kato holonomy of those
Fock-metric subspaces. The classical comparator propagates an explicit quotient
frame. Computing periods through the Gauss--Manin connection is a related but
different problem unless the missing metric/flat-connection comparison is
proved.

Separate three resources. The exact reset-completed CPTP channel needs a
preparation of `P_j/r` on its failure branch. The accepted product of projectors
does not: a two-outcome dilation with termination on failure gives the identical
accepted map. Finally, a normalized-character experiment additionally needs
a reference maximally entangled with the initial `P_0` subspace.

For the character, keep all projective dilations coherent and interfere the
controlled product with the identity branch. Measure the ancilla quadrature
jointly with all-success flags. Its expectation is the real or imaginary part
of the UNNORMALIZED accepted map's trace divided by r. This avoids treating
measured bath records as coherent and avoids a conditional normalization bias.
The reference-state preparation, controlled dilations and flag processing are
charged. The chosen reset density is not used by this terminating experiment.

Parameterize the path on `[0,1]`, with `||P'||<=Lambda` and `||P''||<=K`.
The product's error relative to metric Kato transport is
`O((Lambda²+K)/m)` under these smoothness bounds. Taking
`m=O((Lambda²+K)/epsilon)` and `O(epsilon^-2 log(1/delta))` bounded-observable
trials suffices, with `m` controlled projector calls per trial plus reference
preparation. This is an oracle count; synthesis of those projectors from a
Macaulay/Hodge operator pays its norm, gap and implementation precision.

An explicit classical method propagates an orthonormal \(D\times r\) frame and
costs \(O(mr)\) projector matvecs plus reorthogonalisation. A succinct-projector
model can make this exponentially large in memory, but no lower bound is known.
More decisively, repeated-projection non-Abelian holonomy and Zeno dynamics from
general quantum operations are known operations. Therefore this candidate does
not meet D22 as written. Its proof obligations are: identify a useful metric
holonomy invariant, construct \(P(s)\) without solving the cohomology problem,
and isolate an operation beyond the known Zeno product formula.

## 5. Finalist C: CP Green response for a higher obstruction

### 5.1 A precise quotient-norm decision

Use D-R11-TRIPLE-QUOTIENT-QUERY in `definitions/thermal-cp-r11.md`.
All three normalized harmonic inputs have degree one, the products `ab,bc`
are exact, and the common output is the zero-versus-`gamma` decision for

    theta=||Pi(mu(h mu(a,b),c)+mu(a,h mu(b,c)))||.

Here `Pi` is the orthogonal projector onto the complement of
`[a]H^1+H^1[c]` inside harmonic degree two. Thus it includes BOTH harmonic
projection and the Massey-indeterminacy quotient. Its construction from the
original sheaf/DGA input is not supplied by this proposal. A compiled projector
circuit is an additional, charged input to the conditional primitive below.
No phase output is requested, so no unspecified phase reference is assumed.

The relative plus sign is forced: with `u=h(ab),v=h(bc)`, the graded Leibniz
rule gives `d(uc)=abc` and `d(av)=-abc`. The earlier minus-sign display was
incorrect for these degrees. The norm is defined by the declared Hodge and
quotient metric, while the zero class in the quotient is representative-independent.

### 5.2 Complete conditional primitive and regularization budget

Write `Delta_min` for the supplied positive spectral lower bound. For
`0<zeta<=Delta_min`, use

    h_zeta=d†(Delta+zeta)^(-1)(1-P).

Its operator norm is at most
`alpha_h=sqrt(Delta_min)/(Delta_min+zeta)`, since
`sqrt(lambda)/(lambda+zeta)` decreases on `lambda>=Delta_min>=zeta`.
The broader bound `1/(2sqrt(zeta))` is safe but hides the useful gap promise.
A compiled implementation may have a larger block normalization; if so that
actual normalization replaces `alpha_h` in every resource formula.
The successful Kraus maps are `h_zeta/alpha_h`, `mu/alpha_mu`, and `Pi`,
each with its complete flagged failure complement and charged implementation.

Prepare a balanced branch qubit and coherent versions of the two ordered
multiplication/homotopy circuits. Retain success flags coherently; projecting
the branch qubit back onto plus gives the sum of the two branch maps divided
by TWO. Conditional on all specified successful outcomes, the raw final
vector on the three source registers is therefore

    Pi(mu(h_zeta mu(a,b),c)+mu(a,h_zeta mu(b,c)))/beta,
    beta=2 alpha_h alpha_mu².

An ordinary measured branch mixture would lose the cross term. The success
probability of this fully specified event is `p=theta_zeta²/beta²`.
State preparations, coherent controls, failures, the final quotient circuit,
and any block-encoding normalization are paid; the primitive does not build
its own Hodge or quotient oracle.

The exact error estimate is

    ||h_zeta-h|| <= zeta/[sqrt(Delta_min)(Delta_min+zeta)],
    |theta_zeta-theta| <= 2 alpha_mu² zeta/[sqrt(Delta_min)(Delta_min+zeta)].

For example, taking
`zeta<=min(Delta_min, gamma Delta_min^(3/2)/(16 alpha_mu²))`
makes the norm bias at most `gamma/8`. Consequently the exact-zero promise
has `p<=gamma²/(64 beta²)`, while the nonzero promise has
`p>=49 gamma²/(64 beta²)`. These are separated probability intervals, not
an exact-zero click certificate under regularization. Independent Bernoulli
trials and a threshold between the intervals give a decision; a conservative
additive-Hoeffding bound is `O(beta^4 gamma^-4 log(1/delta))` trials.
Each compiled trial must have probability bias smaller than a fixed fraction
of `gamma²/beta²`. No claim of sample optimality is made.

A coherently retained reservoir time could implement the same regularized
Green map. Classical random waiting time instead produces a mixture of Kraus
maps, not their amplitude integral. Supplying an LCU/QSVT implementation
repairs the physical primitive but identifies its displayed mechanism with
known matrix-function and linear-combination processing. A different physical
implementation needs its own complete instrument and comparative resource bound.

### 5.3 Family, classical comparator and obligations

Endomorphism DGAs of finite locally free resolutions of ideal sheaves of curves
in \(\mathbb P^3\) give a concrete algebraic family: \(\operatorname{Ext}^1\)
classes are first-order embedded deformations and higher products can obstruct
their extension in \(\operatorname{Ext}^2\). A sparse cellular or monomial
resolution can make the
cochain dimension exponential while keeping local maps succinct. The same
instance is attacked classically by two sparse Green-equation solves followed
by sparse products and projection. Krylov memory can be linear in the cochain
dimension, leaving a possible space claim, but no time lower bound or D22 escape
is established.

The decisive obligations are to give one family where (15) is not readable
from the presentation, prove polynomial Hodge and multiplication
normalisations, include the Massey indeterminacy quotient, and either find a CP
response unavailable to generic resolvent algorithms or mark the mechanism
known. Until then Finalist C is an exact conditional construction rather than a
north-star candidate.

## 6. Targeted primary-source checks after derivation

1. [Verstraete, Wolf and Cirac, arXiv:0803.1447](https://arxiv.org/abs/0803.1447)
   proved that time-independent
   local Markovian dissipation can perform universal quantum computation and
   prepare frustration-free ground states. Therefore "the answer is in a
   dissipative steady state" is not itself an originality argument for T01,
   T05, T10, T15 or T16.
2. [Chen, Kastoryano and Gilyén, arXiv:2311.09207](https://arxiv.org/abs/2311.09207)
   construct implementable exact
   detailed-balance Lindbladians for arbitrary noncommuting Gibbs states, with
   cost proportional to mixing time and inverse temperature up to logarithmic
   factors. This supports the accounting rule and defeats any claim that a
   detailed-balance completion removes thermal-state preparation cost.
3. [Burgarth et al., arXiv:1305.6433](https://arxiv.org/abs/1305.6433)
   explicitly obtain non-Abelian phases by repeated projective Zeno dynamics.
   [Burgarth et al., arXiv:1809.09570](https://arxiv.org/abs/1809.09570)
   generalise Zeno dynamics to arbitrary quantum operations and identify the
   associated adiabatic evolution. These are substantive operation-level
   reductions of T02, not a generic appeal to Stinespring dilation.
4. [Gilyén, Su, Low and Wiebe, arXiv:1806.01838](https://arxiv.org/abs/1806.01838)
   give quantum singular-value
   transformation and pseudoinverse/matrix-function primitives. They cover the
   compiled resolvent step in T03 and spectral filtering in T01/T09; a new AG
   application does not make those mechanisms original.
5. [Hayakawa, arXiv:2111.00433](https://arxiv.org/abs/2111.00433) gives a quantum
   algorithm for normalised
   persistent Betti numbers. Together with the campaign's resolved Koszul memo,
   this makes squarefree specialisations of T01/T05 especially vulnerable to a
   known quantum-TDA reduction.
6. [Iarrobino, Macias Marques and McDaniel,
   arXiv:1802.07383](https://arxiv.org/abs/1802.07383) develop Jordan type
   of multiplication by an element in an Artinian algebra and its relationship
   with Lefschetz properties and Hilbert functions. This verifies T09's exact AG
   interpretation; it does not provide the proposed dissipative estimator.
7. [Penkava and Weldon,
   arXiv:math/9808058](https://arxiv.org/abs/math/9808058) treat infinity
   algebras, generalised
   Massey products and deformation problems. This supports the deformation
   interpretation of T03 at a broad level. A concrete sheaf family and its exact
   indeterminacy quotient remain unresolved rather than being inferred from this
   citation.
8. [Holevo, arXiv:quant-ph/0509101](https://arxiv.org/abs/quant-ph/0509101)
   treats complementary channels explicitly. T01's environment Gram state is
   therefore a special complementary-channel output; novelty must rest on the
   annihilation/Macaulay identity and an algorithmic resource separation, not
   on the generic act of tracing out the system.

These searches did not establish novelty of the bath-Gram identity (4). Absence
of a located paper is not evidence of originality. T01 must still be compared
against Gram-matrix preparation, heat-kernel nullity estimation and sparse-rank
algorithms at the operation and resource level.

## 7. Proof obligations and tournament verdict

| rank | candidate | proved inside this memo | unresolved or adverse fact | current D22 status |
|---|---|---|---|---|
| 1 | T01 syzygy-emitting bath | exact TP dilation; exact bath Gram \(=cF_d^\dagger F_d\); exact absorbing survival law and finite-time bias | compilation normalisation, singular gap, same-oracle classical lower bound, and whether bath access adds more than a block encoding | **Unverified; likely reducible in its present readout** |
| 2 | T03 CP Green obstruction | legal Kraus normalisation; regularisation error; coherent-sign requirement; exact Ext/Massey target form | concrete hard family, indeterminacy projector, success weight, and generic QLSA/QSVT reduction | **Fails unless a distinct response operation is found** |
| 3 | T02 reset-completed transport | Kraus completeness, fixed-state set, no-reset path and loss bound | metric Kato versus Gauss--Manin, reset-state access, projector construction, known Zeno holonomy | **Fails as written; retained as control** |

No candidate presently meets all six PRD criteria. The constructive result of
the round is narrower: T01 gives a one-shot CP environment state whose kernel is
exactly a polynomial-tuple syzygy space, without first preparing the quotient;
T03 makes every inverse, normalisation and coherent branch needed for a genuine
higher obstruction explicit; and T02 supplies a fully trace-preserving transport
control that exposes both the reset resource and the distinction between metric
and flat algebraic connections.

## MERGE PROPOSAL

**Proposed definition D-THERMAL-SYZYGY-EMITTER.** For a homogeneous tuple
\((f_j)\), degree \(d\), ambient degree \(N\ge d\), Fock-orthonormal domain
basis \(a=(j,g)\), and \(p_a=gf_j\), define
\(V_{N,d}=\sum_a|a\rangle\otimes a(p_a)\) and its legal two-outcome dilation by
(1), with an explicitly supplied bound \(\alpha^2\ge\|V_{N,d}^\dagger
V_{N,d}\|\). The conditional state is never assumed free.

**Proposed quantified claim C-THERMAL-SYZYGY-GRAM (SKETCH pending independent
audit).** For every homogeneous tuple, \(N\ge d\), and the maximally mixed state
on \(R_N\), the unnormalised successful environment state of
D-THERMAL-SYZYGY-EMITTER is
\[
 {\binom{N+n}{N-d}\over M_N\alpha^2}F_d^\dagger F_d.
\]
Consequently its kernel equals the degree-\(d\) syzygy space of the supplied
tuple and its trace is
\(\binom{N+n}{N-d}\|F_d\|_F^2/(M_N\alpha^2)\).

**Proposed quantified claim C-THERMAL-SYZYGY-ABSORPTION (SKETCH pending
independent audit).** With \(B=F_d/\alpha_F\), the absorbing Lindbladian (6) is
CPTP and its live probability from \(I_L/L\) is (7). Under
\(\lambda_{\min}^+(B^\dagger B)\ge\eta\), time
\(t\ge\eta^{-1}\log(2/\varepsilon)\) and
\(O(\varepsilon^{-2}\log(1/\delta))\) fresh trials estimate
\(\dim\ker F_d/L\) to additive \(\varepsilon\), before Lindblad-simulation
error. This is a conditional heat-trace algorithm and carries no originality or
classical-speedup status.

**Proposed definition D-RESET-PROJECTOR-TRANSPORT.** For equal-rank projectors
\(P_j\), define the CPTP channel by (9)--(10), including explicit access to a
preparation of \(P_j/r\), and define its no-reset branch by (11).

**Proposed negative decision.** Do not identify D-RESET-PROJECTOR-TRANSPORT
with Gauss--Manin transport without an explicit intertwiner. Do not promote its
mechanism under D22: repeated-projector and general-operation Zeno holonomies
are resolved prior art. Do not promote thermal equivariant index T04: its exact
output equals the alternating chain trace before any thermal evolution.

**Next bounded test.** For T01, construct sparse degree-\(d\) matrices for one
non-squarefree monomial family and one binomial family; verify (4) numerically,
measure \(\eta\), syzygy fraction and \(alpha^2/\|V^\dagger V\|\), and benchmark
the same matvec oracle with block Wiedemann/Lanczos. Continue only if the
syzygy fraction and normalised gap are inverse-polynomial while the best
same-output classical method still needs superpolynomial time or memory.
