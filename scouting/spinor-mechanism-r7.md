# Octonionic reassociation: retained phases and actual associator filtering

2026-09-05. Independent bounded construction for root-tracked qaag-62k.
Canonical data and operations are D-OCTONION-CONVENTION,
D-OCTONION-PHASE-QUERY and D-OCTONION-CONTINUOUS-QUERY in
`definitions/octonionic-operations.md`. Claim status lives only in
`claims/CLAIMS.md`, C-357--C-358; independent review is
`verdicts/spinor-mechanism-r7.md`.
The ordinary positive Euclidean coefficient metric departs from C1.
All coefficient maps are complex-linear when used on quantum registers.
Real norm-composition identities below are explicitly restricted to real
octonion coefficients. Identity notation locally departs from C6 as
declared in the canonical file.

The initial proposed feature was to retain multiplication labels and erase
only their common output, exposing nonassociativity as a unitary phase without
the small success probability of multiplication. That operation exists.
On a growing geometric family it is exactly a cubic-phase IQP circuit.
Its fixed-frequency geometric bit has a matched classical Monte Carlo attack.
A second operation actually erases the labels and tests continuous octonion
associativity; its different operator norm and its own comparator are derived
separately. Neither construction meets the north star.

## 1. Fix the multiplication convention before constructing the operation

Use the real octonions obtained by Cayley–Dickson doubling of the quaternions:

\[
 (a,b)(c,d)=(ac-\overline d\,b,\; da+b\overline c).
\]

The basis is $e_0=(1,0)$, $e_1=(i,0)$, $e_2=(j,0)$, $e_3=(k,0)$,
$e_4=(0,1)$, $e_5=(0,i)$, $e_6=(0,j)$, $e_7=(0,k)$.
Identify its labels with $\mathbb F_2^3$, using the low-to-high bits
$a_0,a_1,a_2$. Multiplication has the signed-XOR form

\[
 e_a e_b=(-1)^{F(a,b)}e_{a+b},
\]

where all additions in the exponent are modulo two and, in this convention,

\[
\begin{aligned}
 F(a,b)={}&a_0b_0+a_1b_0+a_2b_0+a_1b_1+a_2b_1+a_2b_2\\
 &+a_2b_0b_1+a_1b_0b_2+a_0b_1b_2.                 \tag{1}
\end{aligned}
\]

This is an explicit table specification, not an unspecified root, component,
or multiplication oracle. Changing the octonion basis convention can change
the particular polynomial $F$; all calculations here use (1).

The two bracketings have the same output label $a+b+c$. Their relative sign is

\[
\begin{aligned}
 (-1)^{\partial F(a,b,c)}
 &=(-1)^{F(a,b)+F(a+b,c)+F(b,c)+F(a,b+c)},\\
 \partial F(a,b,c)&=\det_{\mathbb F_2}(a,b,c)
 =\sum_{(i,j,k)\text{ a permutation of }(0,1,2)}a_i b_j c_k.
                                                               \tag{2}
\end{aligned}
\]

Substitution into (1) cancels the quadratic and repeated-index terms, leaving
the six displayed cubic monomials. In particular this determinant cochain is
explicitly a coboundary. It is not asserted to represent a nontrivial
third group-cohomology class or a nontrivial topological bulk action.

## 2. A deterministic retained-label operation

Keep three three-qubit registers $a,b,c$. Compute the two bracket signs
reversibly, phase a minus-state ancilla by their XOR, and uncompute all
intermediate labels. The two bracketings have the same final XOR label, so
that label carries no which-bracketing information after uncomputation.
The exact operation left on the registers is

\[
 U_{\rm ass}|a,b,c\rangle=(-1)^{\det(a,b,c)}|a,b,c\rangle.       \tag{3}
\]

Equivalently, it is the product of six CCZ gates, one for each monomial in
(2). The optimized circuit uses nine data qubits, no heralding, and a
constant number of ordinary gates. The operator is unitary on all complex
input states. Its implementation never infers a contraction from a real
norm identity.

For arbitrary coefficient states $x,y,z$, a plain Hadamard-test expectation is

\[
 \langle U_{\rm ass}\rangle
 =\sum_{a,b,c}|x_a|^2|y_b|^2|z_c|^2(-1)^{\det(a,b,c)}.        \tag{4}
\]

Separate computational measurements of the three original sources followed
by evaluation of the determinant have exactly that mean and bounded variance.
Thus the plain diagonal expectation provides no copy advantage.

Equation (3) also does not test the continuous associator
$[x,y,z]=(xy)z-x(yz)$ by simply replacing labels with arbitrary coefficient
superpositions. For $x=y=z=8^{-1/2}\sum_a e_a$, alternativity gives
$[x,x,x]=0$. Yet independent uniform basis labels have determinant one in
$7\cdot6\cdot4=168$ of the $512$ triples, giving probability $21/64$.
The phase operation retains labels that the continuous associator sums over.
This distinction is part of the task definition, not an implementation error.

## 3. A growing geometric input family with an off-diagonal readout

Give a three-uniform hypergraph $\mathcal H$ on $v$ vertices with $m$ edges,
and a binary vector $y\in\mathbb F_2^{3v}$. Each vertex carries a variable
$a_i\in\mathbb F_2^3$. Define the homogeneous cubic

\[
 f_{\mathcal H}(a_1,\ldots,a_v)
 =\sum_{\{i,j,k\}\in E(\mathcal H)}\det(a_i,a_j,a_k).
                                                               \tag{5}
\]

The exact geometric input is the affine hypersurface
$X_{\mathcal H}=V(f_{\mathcal H})\subset\mathbb A_{\mathbb F_2}^{3v}$,
represented by this sparse equation. Its input length is
$O(m\log v+v)$ bits. Bounded-degree connected hypergraphs with $m=\Theta(v)$
give a growing family; no claim that every such family is classically hard
is needed or made.

This hypersurface records parity of the local determinants. It is not the
intersection of all individual determinant-zero loci. On nonzero basis
labels the local determinant condition is Fano-plane dependence, but no
equivalence with continuous real-octonion associativity is silently imposed.

Put $n=3v$ and define

\[
 b_y=2^{-n}\sum_{a\in\mathbb F_2^n}
             (-1)^{f_{\mathcal H}(a)+y\cdot a},
 \qquad p_y=b_y^2.                                          \tag{6}
\]

For $y\ne0$, let $H_y=\{a:y\cdot a=0\}$. Then

\[
 b_y=\frac{2}{2^n}
 \bigl(\#(X_{\mathcal H}\cap H_y)
       -\#(X_{\mathcal H}\cap\{y\cdot a=1\})\bigr).            \tag{7}
\]

Thus $p_y$ is a precisely normalized squared hyperplane-count imbalance.
For $y=0$, $b_0=2\#X_{\mathcal H}/2^n-1$.
The classical output is the bit distinguishing $p_y=0$ from $p_y\ge\gamma$,
for a supplied promise $0<\gamma\le1$, with failure at most $\delta$.
This is a growing classical-equation input problem with a scalar output.

For an explicit nonempty growing diagnostic, take the connected star with
edges $\{1,2,i\}$ for $3\le i\le v$, $v\ge4$. Its cubic is
$\det(a_1,a_2,\sum_{i\ge3}a_i)$. Thus $b_0=11/32$ and $p_0=121/1024$
for every $v$. A frequency assigning unequal vectors to two leaf vertices has
$b_y=0$, because translating both leaves by the same vector preserves the
cubic and can flip that character. Both promise alternatives therefore occur
for any fixed $0<\gamma\le121/1024$.

Prepare $|+\rangle^{\otimes n}$, apply (3) at each hyperedge, and apply
$H^{\otimes n}$. The resulting amplitude at $y$ is exactly $b_y$.
This readout uses off-diagonal coherence and is different from (4).
The entire output distribution is

\[
 \Pr(Y=y)=p_y,\qquad \sum_y p_y=1.                            \tag{8}
\]

Each trial costs $6m$ CCZ gates and $2n$ Hadamards, plus classical comparison
with $y$. A CCZ has a constant exact Clifford+T decomposition. No amplitude
loading, unspecified point preparation, or real-number precision oracle is
present. The live quantum register has $n$ qubits; the graph description and
classical output counter are separately charged ordinary input/control data.

Observing the event $Y=y$ gives a one-sided-error decision with

\[
 M_Q=\left\lceil\gamma^{-1}\log(1/\delta)\right\rceil,\qquad
 G_Q=O((v+m)M_Q).                                          \tag{9}
\]

The circuit itself has no postselection. The specified target event is rare
when $p_y$ is small, and its repetition cost is explicitly included.
For implemented gates, a sufficient total per-trial channel error is
$O(\delta/M_Q)$; error per compiled gate can be divided by $O(v+m)$.

## 4. The same geometric bit has the same-margin classical upper bound

Draw a uniform $a\in\mathbb F_2^n$, evaluate (5), and form
$Z=(-1)^{f_{\mathcal H}(a)+y\cdot a}$. Then $Z\in\{-1,1\}$ and
$\mathbb E Z=b_y$. The promise on $p_y$ is exactly
$b_y=0$ versus $|b_y|\ge\sqrt\gamma$.

Estimate $b_y$ by an independent sample mean and threshold its absolute value
at $\sqrt\gamma/2$. Hoeffding's inequality gives the explicit sufficient bound

\[
 M_C=\left\lceil\frac8\gamma\log\frac2\delta\right\rceil,
 \qquad G_C=O((v+m)M_C),                                   \tag{10}
\]

in elementary bit operations. Generating the assignment uses $n$ random bits;
the working assignment and sample counter need $O(v+\log M_C)$ bits beyond
the common graph input. The polynomial and determinant evaluations are exact
finite-field arithmetic, with no numerical condition number.

This matches the quantum margin exponent. Estimating $p_y$ directly by a
generic bounded estimator to additive $O(\gamma)$ would give an unnecessarily
weak $\gamma^{-2}$ comparator. The unsquared mean is the relevant attack.
The claim is the zero-versus-margin problem in (6); uniform additive
approximation of $p_y$ to arbitrary $\epsilon$ has a different worst-case
sample-complexity statement.

For some hypergraphs further exact classical algorithms are faster. No
optimal classical lower bound is asserted. The explicit upper (10) already
prevents claiming a speedup for the displayed quantum procedure.

## 5. Full sampling reaches a known mechanism rather than a new algorithm

The circuit in (8) is exactly
$H^{\otimes n}\operatorname{diag}((-1)^{f_{\mathcal H}})H^{\otimes n}$.
It is a cubic-phase IQP circuit, with the usual Walsh-squared output law.
This is an explicit whole-circuit reduction, not the observation that any
quantum operation can be compiled into universal gates.

A single logical CCZ is obtained by restricting three label registers to
$(x,0,0),(0,y,0),(0,0,z)$ in $\mathbb F_2^3$: their determinant is $xyz$.
The association of these familiar cubic gates with an octonion grading does
not change their quantum information processing.

The scalar Monte Carlo attack does not by itself sample the full law (8).
No efficient classical sampler for every hypergraph is claimed. Conversely,
hardness results for general IQP ensembles cannot automatically be transferred
to this restricted determinant-hypergraph ensemble without a reduction.
Even if a sampling advantage were established for such a subfamily, the
displayed algorithm remains the known cubic-phase/Fourier-sampling mechanism
and fails the strict originality criterion.

## 6. A materially different map: erase labels to get the actual associator

Let $A:\mathbb C^8\otimes\mathbb C^8\otimes\mathbb C^8\to\mathbb C^8$
be the complex-linear coefficient operator of
$A(x\otimes y\otimes z)=(xy)z-x(yz)$, with the multiplication convention (1).
On each basis triple the output is zero or
$2(-1)^{F(a,b)+F(a+b,c)}e_{a+b+c}$.
It is nonzero exactly when $a,b,c$ are independent over $\mathbb F_2$.

For each nonzero output label $d$, exactly 24 independent ordered triples
have $a+b+c=d$. One may choose $a\notin\operatorname{span}(d)$ in six ways,
then $b\notin\operatorname{span}(d,a)$ in four ways and set $c=d+a+b$.
No such triple has output zero. Different output rows have disjoint supports.
Therefore the actual complex Hilbert-space norm is

\[
 AA^\dagger=96(\mathbb1-|0\rangle\langle0|),\qquad
 \|A\|=\sqrt{96}=4\sqrt6.                                  \tag{11}
\]

The maximally uniformly scaled Kraus operator is
$K=A/\sqrt{96}$. Its physical implementation can be explicit: for each
nonzero $d$, prepare the uniform signed superposition of its 24 triples.
Those seven states are orthonormal. Extend this constant-size preparation to
a unitary, run its inverse on the nine input qubits, and herald the clean
workspace and a nonzero coarse output label. The zero output label is excluded
without measuring which of the seven other labels occurred.
This realizes $K$; it is not an assumed nonlinear multiplication gate.
The preparation is a fixed ideal-rotation circuit in constant dimension.
Its $1/\sqrt{24}$ amplitudes do not imply an exact constant-size Clifford+T
implementation. For a fixed finite gate set, charge
$C_K(\eta)=O(\operatorname{polylog}(1/\eta))$ synthesis gates per attempt
to reach operator error $O(\eta)$ and instrument diamond error $O(\eta)$.

For real unit octonions, norm composition and the triangle inequality give
$\|[x,y,z]\|\le2$, with equality at suitable independent basis triples. Hence

\[
 p_{\rm ass}=\|[x,y,z]\|^2/96\le1/24.                       \tag{12}
\]

This is only a one-use real-product-input bound. It is not a bound on
arbitrary complex inputs or a multiplicativity theorem for tensor powers.
In fact, put $P=K^\dagger K$, a real rank-seven projector.
Pairing the two sites within each of three original sources in a normalized
maximally entangled eight-dimensional state gives two-use acceptance

\[
 \operatorname{Tr}(P^2)/8^3=7/512>(1/24)^2.                 \tag{13}
\]

The vectorization identity gives this directly. It is a scope warning,
not an algorithm, speedup, or historical-originality claim.

## 7. A growing continuous-geometric output and its matched attack

Give an explicit list of $L$ triples of real unit octonions
$(x_i,y_i,z_i)$ with rational coordinates of at most $B$ bits.
The geometric zero locus consists of the cubic equations
$[x_i,y_i,z_i]=0$, together with the displayed unit-sphere quadric promises.
Decide whether

\[
 R=L^{-1}\sum_i\|[x_i,y_i,z_i]\|^2
 \quad\hbox{is zero or at least }\gamma,\qquad 0<\gamma\le4.
\]

Choose $i$ uniformly, prepare its three coefficient states and apply $K$.
The average click probability is $R/96$. Thus
$O(96\gamma^{-1}\log(1/\delta))$ trials suffice.
Every trial charges indexed input access, three state preparations at the
required accuracy, and the synthesized filter circuit. For a trial budget $M$,
take $\eta=O(\delta/M)$ for each source preparation and filter instrument.
The total gate cost is
$O(M(C_{\rm access}+3C_{\rm prep}(B,\eta)+C_K(\eta)))$.
No whole-list coherent oracle is supplied.

Classically, evaluate the sampled row's octonion associator exactly and test
whether it is nonzero. Because every residual lies in $[0,4]$, at least a
$\gamma/4$ fraction of rows are nonzero in the positive case.
$O(4\gamma^{-1}\log(1/\delta))$ random row evaluations therefore suffice;
scanning all $L$ rows is an additional exact upper bound.
Each row uses a fixed number of rational arithmetic operations with $O(B)$
bit-length growth. This matches or improves the displayed quantum scaling.

Even in a separate copies-only version for one unknown triple, fixed dimension
prevents an asserted margin-exponent advantage. An allowed strategy measures
the real density-matrix entries separately on each original three-qubit source,
estimates them to $O(\sqrt\gamma)$, and extracts the leading unit eigenvector.
The rank-one spectral gap is one; eigenvector error is $O(\sqrt\gamma)$ up to
an irrelevant sign. The real associator is Lipschitz with constant at most two
in each unit input, so sufficiently small constants decide the same norm gap.
This uses $O(\gamma^{-1}\log(1/\delta))$ copies in dimension eight.
It is a concrete separate-source upper bound, not a claim that tomography
is optimal or a substitute for the full allowed measurement model.

## 8. Verification, hardware, and remaining obstruction

An author probe with a 30-second timeout and one BLAS thread passed 576
grading and associator-phase identities. Deleting a cubic determinant term
was rejected on 64 of 512 triples. A second bounded probe passed 72 checks
of (11)–(13), the continuous/retained-label counterexample, and the exact
Walsh and hyperplane-count identities on growing three- and four-vertex
hypergraphs. These support the symbolic derivations and are not registered
proof checkers. Independent criticism remains required.

The smallest retained-phase hardware diagnostic uses nine input qubits and
six CCZ gates, or their ordinary MBQC realization. Preparing the three uniform
real octonion states distinguishes the retained determinant event $21/64$
from the continuous-associator filter's zero event. The latter can use the
fixed-dimension inverse preparation of the seven signed 24-term rows, with
its actual success flag and source costs. No special condensed-matter
implementation or effortless optical nonlinear interaction is assumed.

Primary-source checks were made only after deriving the operations.
[Albuquerque–Majid, math/9802116](https://arxiv.org/abs/math/9802116)
already presents the octonions as a cochain-twisted group algebra; the
associator is a coboundary. The particular basis signs here are fixed by (1).
[Bremner–Montanaro–Shepherd, arXiv:1504.07999](https://arxiv.org/abs/1504.07999)
studies commuting quantum computations and low-degree-polynomial gaps.
These are direct prior mechanisms relevant to (2)–(8), not evidence that every
restricted geometric sampling ensemble has a proved hardness theorem.

The surviving results are the exact label-retaining operation, its explicit
cubic-phase reduction and geometric Monte Carlo comparator, and the separate
continuous associator contraction with its correctly scoped norm and baseline.
An unproved classical sampling lower bound would not rescue the first
mechanism's originality. A new mechanism or a new physical operation with a
matched geometric advantage is still required; neither is claimed here.
