# Round 2: original algebraic transformations

**Status.** Constructive scouting under PRD D22, without web search. Historical novelty is
not established. Of three mechanisms attacked below, only reverse multiplication survives as
a conditional sampling primitive; none is presently a north-star algorithm. The exterior-power
Newton lift and finite-difference jet extractor are rejected as speedup candidates.

This memo departs from frozen convention C1: its main object is a finite-dimensional quotient
algebra with an explicitly chosen Hilbert-space inner product, not the Fock completion of $R$.
That choice is part of the access model, not an invariant silently attributed to the scheme.
This memo also locally departs from C7: its alpha/beta symbols are block-encoding
normalizations. Resource and classical-access scopes were repaired following
`verdicts/original-round2-r1.md`; the identities do not certify a speedup.

## 1. Reverse multiplication: coherent algebraic unzipping

### Exact problem, access, and output

**Succinct quotient-factorisation sampling (SQFS), provisional.** Let $A$ be a
$D$-dimensional commutative unital complex algebra with an orthonormal computational basis
$b_0,\ldots,b_{D-1}$, $d=\lceil\log_2D\rceil$, and multiplication

\[
 \mu:A\otimes A\longrightarrow A,\qquad \mu(a\otimes b)=ab.
\]

The input supplies (i) a circuit preparing a unit vector $|u\rangle\in A$; (ii) a unitary
block encoding of $\mu/\alpha$, including its inverse, at cost $C_\mu$; (iii) an integer
$k$; and (iv) a promise $p_k\ge 1/\operatorname{poly}(d,k)$, defined below. The output is
one tuple $(a_1,\ldots,a_k)$ within total-variation error $\epsilon$ of

\[
 \Pr(a_1,\ldots,a_k)=
 { |\langle b_{a_1}\cdots b_{a_k},u\rangle|^2\over Z_k(u)},\qquad
 Z_k(u)=\sum_{a_1,\ldots,a_k}|\langle b_{a_1}\cdots b_{a_k},u\rangle|^2.
\]

The proposed new computational result is sampling the *coherent factorisation law* of a
succinct quotient element without expanding its $D^k$ possible factorisations. The proposed
new mechanism is to run associative algebra multiplication backward as a branching
comultiplication. Both originality assertions are unverified.

### Operation sequence and exact identity

Set $\Delta=\mu^\dagger$. Reverse the multiplication block encoding at each internal node
of any binary tree with $k$ leaves, starting from $|u\rangle$. Use a fresh flag at every
node, postselect all flags to zero after the tree, then measure the leaves.

For the adjoint $\Delta_T^{(k)}$ of the multiplication tree $\mu_T^{(k)}$,

\[
 \begin{aligned}
 \langle b_{a_1}\otimes\cdots\otimes b_{a_k}|\Delta_T^{(k)}|u\rangle
 &=\langle \mu_T^{(k)}(b_{a_1}\otimes\cdots\otimes b_{a_k}),u\rangle\\
 &=\langle b_{a_1}\cdots b_{a_k},u\rangle .
 \end{aligned}
\]

Associativity makes the amplitude independent of the tree. Consequently

\[
 \|\Delta_T^{(k)}u\|^2=Z_k(u),\qquad
 p_k={Z_k(u)\over \alpha^{2(k-1)}}.
\]

Thus the distribution is exact conditional on heralding; this is not phase estimation, a
Fourier transform, a walk, annealing, HHL, QSVT, or DQI. No amplitude amplification is
credited: adding it would be a Grover mechanism prohibited by D22.

### Two diagnostic algebras

1. **Reduced special case.** If $A\simeq\mathbb C^D$ is supplied in a positive
   dagger-Frobenius metric with orthonormal primitive idempotents $e_p$, then
   $\mu(e_p\otimes e_q)=\delta_{pq}e_p$, hence
   \[
      \Delta e_p=e_p\otimes e_p,\qquad
      \Delta_T^{(k)}{1\over\sqrt D}\sum_p e_p
      ={1\over\sqrt D}\sum_p e_p^{\otimes k}.
   \]
   This is a unit-success hidden-idempotent broadcaster. It does not violate no-cloning:
   $\Delta(\sum_pc_pe_p)=\sum_pc_pe_p\otimes e_p$, not the tensor square of a general
   superposition. It produces root-correlated registers, but not classical root coordinates.

2. **Nonreduced local test.** For $A_r=\mathbb C[\varepsilon]/(\varepsilon^r)$ with the
   Euclidean-orthonormal monomial basis $|j\rangle=\varepsilon^j$,
   \[
   \Delta|m\rangle=\sum_{i=0}^{m}|i,m-i\rangle,\qquad
   \Delta_T^{(k)}|m\rangle=
      \sum_{i_1+\cdots+i_k=m}|i_1,\ldots,i_k\rangle,
   \]
   so $Z_k(|m\rangle)=\binom{m+k-1}{k-1}$. Since
   $\|\mu\|=\sqrt r$, a global $\alpha=\sqrt r$ gives
   $p_k=\binom{m+k-1}{k-1}/r^{k-1}$. For $k\asymp r$ this is superpolynomially
   small; for fixed $k$ it merely samples a uniform weak composition, which a classical
   stars-and-bars sampler does directly.

The algebraic trace pairing does not repair the second example. Since
$\operatorname{Tr}M_1=r$ and $\operatorname{Tr}M_{\varepsilon^j}=0$ for $j>0$,

\[
 T(\varepsilon^i,\varepsilon^j)=\operatorname{Tr}M_{\varepsilon^{i+j}}
\]

has rank one. It cannot be a positive nondegenerate quantum inner product and it discards
every nilpotent jet. Perfect idempotent copying is therefore a semisimple phenomenon, not
a mechanism for reading arbitrary local scheme structure.

### Cost ledger, hardware, and hidden costs

- Let $C_u$ be the input preparation cost, and $w_\mu,d_\mu$ the workspace and
  depth of the supplied rectangular multiplication encoding, including its
  input/output embeddings. One attempt uses $k-1$ inverse multiplication calls,
  $O(d_\mu\log k)$ tree depth plus preparation/control depth, and up to
  $kd+O(kw_\mu+k)$ qubits. Its gates cost
  $O(C_u+kC_\mu+\operatorname{poly}(k,d))$, including embedding/flag logic.
  A capped failure probability $\delta$ costs
  $O(p_k^{-1}\log(1/\delta))$ attempts; expected repeat-until-success cost
  needs only $p_k^{-1}$ attempts.
- Block-encoding error must be $o(\epsilon p_k/k)$; conditioning on a rare flag amplifies
  implementation error. The promise on $p_k$ is essential.
- Polynomial-ring multiplication run backward resembles number-conserving boson splitting:
  a beam splitter maps one occupation into a binomial superposition of splits. Quotient
  reduction and the chosen metric are not supplied by passive optics; relation postselection
  can restore them only at an unbounded success cost.
- An explicit multiplication table already contains $\Theta(D^3)$ structure constants.
  For equations $I=(f_1,\ldots,f_s)$, implementing $\mu$ in quotient representatives
  requires coherent normal forms $\operatorname{NF}_I(b_ab_b)$, hence a Gröbner/border
  basis or equivalent elimination. The alternative $P_{I^\perp}(ab)$ requires preparing
  the inverse-system projector and collapses back to known spectral filtering, with its
  gap and overlap costs.
- Even for a reduced quotient, the algebraic trace form is bilinear rather than a canonical
  positive Hermitian metric. Supplying a positive metric in which primitive idempotents are
  orthonormal can encode the root evaluation matrix. Whitening it requires a dense
  $G^{-1/2}$ and its condition number.
- A gate-level black box for hidden-basis copying can hide the answer in an oracle.
  Conversely, if its basis-change circuit is exposed, measuring after its inverse reveals
  the labels without unzipping. Neither case is an equation-level advantage.

### Strongest classical and known-quantum attacks

With explicit $\mu$, the output amplitudes form a tree tensor network of bond dimension
$D$. Double-layer contraction and sequential sampling cost polynomial time in $k,D$
(a crude bound is $O(kD^6)$), not $D^k$. A quantum advantage could therefore only be
in the succinct $d=\log D$ access model. No commutative algebra family is known here for
which that access is natural, $p_k$ is polynomial, and classical sampling is hard.
The exhibited truncated-monomial algebra with a specified monomial input admits
weak-composition sampling. A general circuit-prepared coefficient input is not
classically sampleable merely because multiplication is monomial. Group/toric
multiplication risks reducing to
established hidden-subgroup/Fourier algorithms.

The useful reduced-case output is also under-specified. Tracing out leaves gives no root
coordinates, while extracting joint eigenvalues of coordinate multiplications returns to
nonnormal eigensolving or ordinary phase estimation in the normal case. Moment readout
reduces to trace estimation. Thus the unzipping identity and circuit survive this algebraic
audit, but their historical novelty and a useful problem-level speedup remain unverified.

**Specific missing theorem.** Exhibit a natural, equation-succinct family $I_n$ with
$D_n=2^{\Omega(n)}$ for which quotient multiplication and $|u_n\rangle$ have
$\operatorname{poly}(n)$-size circuits not containing a normal form or root decomposition,
$p_k\ge1/\operatorname{poly}(n,k)$, and SQFS has no classical polynomial-time sampler under
a stated standard assumption; also give a polynomial-copy measurement that answers a
geometric question not reducible to a trace or eigenvalue computation.

## 2. Exterior-power Newton/Hensel lift

### Problem and operation

Given a square system $F:\mathbb C^n\to\mathbb C^n$, an approximate nonsingular root $x$,
and sparse reversible access to $J=DF(x)$ and $b=-F(x)$, output the classical Newton
correction $\delta=J^{-1}b$ to error $\epsilon$. The attempted mechanism puts $n-1$
registers in the antisymmetric sector, applies a block encoding of $J^{\mathsf T}/\beta$
to every particle, and uses the Levi-Civita identification
$E:\mathbb C^n\to\bigwedge^{n-1}\mathbb C^n$.

The compound-matrix identity is

\[
 E^{-1}\bigl(\bigwedge\nolimits^{n-1}J^{\mathsf T}\bigr)E
   =\operatorname{adj}(J),
\]

so postselection on all $n-1$ dilations prepares the ray of
$\operatorname{adj}(J)b=\det(J)J^{-1}b$. Fermionic antisymmetry computes all cofactors in
one coherent transformation; this is the candidate original mechanism.

### Resource obstruction and equivalence audit

The success probability is exactly

\[
 p_b={\|\operatorname{adj}(J)b\|^2\over
          \beta^{2(n-1)}\|b\|^2}.
\]

If $\sigma_1\ge\cdots\ge\sigma_n>0$ and $\beta\ge\sigma_1$, its worst-case lower
envelope is $(\sigma_2\cdots\sigma_n/\beta^{n-1})^2$, which can be
$\kappa(J)^{-2(n-1)}$. Recovering the correction requires additional scale and
phase readout. Determinant postselection is one costly option, not a compulsory
one: for a normalized Newton-ray vector $v$, its scale obeys
$\|J^{-1}b\|=\|b\|/\|Jv\|$. An exact complex correction also needs a phase
reference relative to $b$. The optional $n$-particle determinant branch succeeds with
$|\det J|^2/\beta^{2n}=\prod_i(\sigma_i/\beta)^2$. Fermionic hardware supplies the wedge
projection, not these missing probabilities.

One attempt uses $n-1$ matrix calls, $\Theta(n\log n)$ qubits, and an additional
$\operatorname{poly}(n)$ antisymmetric state-preparation/unpreparation circuit, but repetition
is $1/p_b$ without prohibited Grover amplification. Outputting $n$ classical coordinates
requires tomography. Classical dense adjugate-free solving costs $O(n^\omega)$, while sparse
Krylov/Newton solvers avoid both the determinant product and tomography. Algebraically the
construction is the classical cofactor formula in superposition; algorithmically it is
postselected matrix application. It is neither a new Newton result nor an advantage, and
using HHL/QSVT/amplitude amplification to fix it would violate D22.

**Missing theorem (now implausible).** A promised Jacobian family with polynomial $p_b$,
cheap scale recovery, and sublinear classical readout for the same classical correction.
The output and singular-value products make these promises mutually unmotivated.

## 3. Collision-jet finite-difference interferometer

### Problem, sequence, and identity

Suppose a flat deformation supplies coherent, analytically gauge-fixed preparation
$U(t)|0\rangle=|\psi(t)\rangle$, where colliding branches encode a local scheme. Given
$k$, output the normalized first nonzero $k$-jet at $t=0$, intended to distinguish a
fat point from its reduced support. Prepare the $k+1$ parameter values $jh$ coherently
and interfere them with signed binomial weights. Postselecting the control produces

\[
 r_k(h)=\sum_{j=0}^k(-1)^{k-j}\binom{k}{j}|\psi(jh)\rangle.
\]

Writing $|\psi(t)\rangle=\sum_{m\ge0}t^m|\psi_m\rangle$ and using

\[
 \sum_{j=0}^k(-1)^{k-j}\binom{k}{j}j^m=k!\,S(m,k)
\]

gives $r_k(h)=k!h^k|\psi_k\rangle+\sum_{m>k}k!S(m,k)h^m|\psi_m\rangle$.
The zeroth through $(k-1)$-st branches cancel exactly.

### Cost, classical attack, and rejection

The coefficient one-norm is $2^k$, so the heralding probability is
$p=\|r_k(h)\|^2/4^k\sim h^{2k}\|\psi^{(k)}(0)\|^2/4^k$. Small $h$, needed to suppress
higher jets, makes the experiment exponentially unlikely in the very multiplicity being
resolved. A coherent analytic gauge across all $U(jh)$ is additional information; arbitrary
branch phases change the alleged jet. Classical finite differences use the same $k+1$
preparations if their amplitudes are accessible, and numerical local algebra avoids this
cancellation by dual bases or deflation.

Most decisively for D22, the circuit is exactly linear combination of unitaries applied to
ordinary finite differencing. Calling the cancelled derivative a local-algebra state changes
the application, not the mechanism. Amplitude amplification would only append Grover. This
candidate is therefore rejected independently of whether some promise controls $p$.

**Missing theorem (blocked by equivalence).** An operation isolating jets without an LCU,
Fourier, phase-estimation, or amplitude-amplification reduction and without $h^{2k}$
postselection. No such operation is supplied.

## MERGE PROPOSAL

All identifiers are provisional; novelty is unverified.

### Provisional definitions

- **D-OA-coherent-factorisation-law.** The SQFS distribution
  $|\langle b_{a_1}\cdots b_{a_k},u\rangle|^2/Z_k(u)$, including the chosen quotient basis
  and Hilbert metric as input data.
- **D-OA-dagger-multiplication-access.** A reversible block encoding of
  $\mu/\alpha:A\otimes A\to A$, not merely generators of an ideal; its construction cost,
  metric, normal-form information, error, and heralding normalisation are charged.

### Proposed claim rows

#### C-NEW-OA-UNZIP-IDENTITY

- statement: Under D-OA-dagger-multiplication-access, reversing any $k$-leaf associative
  multiplication tree samples D-OA-coherent-factorisation-law after heralding, with
  $p_k=Z_k(u)/\alpha^{2(k-1)}$ and expected gate cost
  $O(kC_\mu p_k^{-1}\log(1/\delta))$, before approximation-error overhead.
- status: CONJECTURE
- depends-on: D-OA-coherent-factorisation-law, D-OA-dagger-multiplication-access
- where-proved: this memo, §1, “Operation sequence and exact identity”
- where-tested: none
- referee: not yet reviewed
- north-star relevance: candidate mechanism only; no advantage or useful geometric output
  follows from the identity.

#### C-NEW-OA-UNZIP-SPEEDUP

- statement: HOLD (do not merge): there is a natural equation-succinct quotient family for
  which multiplication access does not encode normal forms or roots, $p_k$ is polynomial,
  SQFS answers a useful algebraic-geometric question, and no classical polynomial-time
  sampler exists under a standard assumption.
- status: CONJECTURE
- depends-on: C-NEW-OA-UNZIP-IDENTITY
- where-proved: none
- where-tested: none
- referee: not yet reviewed
- north-star relevance: this is the missing problem-level result and speedup; the current
  memo supplies none of its four substantive lemmas.

#### C-NEW-OA-TRACE-BROADCAST

- statement: For every finite zero-dimensional quotient, the algebraic trace pairing is a
  positive nondegenerate Hilbert metric and its multiplication adjoint gives a unit-success
  broadcaster of both primitive roots and nilpotent jets.
- status: REFUTED
- depends-on: D-OA-dagger-multiplication-access
- where-proved: refuted in this memo, §1, “Two diagnostic algebras”
- where-tested: none
- referee: not yet reviewed
- surviving statement: For a supplied reduced dagger-Frobenius algebra with orthonormal
  primitive idempotents, $\Delta e_p=e_p\otimes e_p$; for
  $\mathbb C[\varepsilon]/(\varepsilon^r)$ the trace pairing has rank one, while Euclidean
  unzipping only samples weak compositions with degree-dependent success.
- north-star relevance: blocks the attempted extension from reduced points to local schemes.

#### C-NEW-OA-WEDGE-NEWTON

- statement: For all nonsingular polynomial-system Jacobians, antisymmetric
  $(n-1)$-copy application yields a polynomial-time Newton/Hensel lift with the same
  classical correction output and without a condition-number product.
- status: REFUTED
- depends-on: none
- where-proved: refuted in this memo, §2
- where-tested: none
- referee: not yet reviewed
- surviving statement: The circuit prepares the adjugate ray with
  $p_b=\|\operatorname{adj}(J)b\|^2/(\beta^{2(n-1)}\|b\|^2)$, which is
  $\kappa^{-2(n-1)}$ on a diagonal family; scale recovery and classical readout remain.
- north-star relevance: rules out “all cofactors at once” as a Newton speedup.

#### C-NEW-OA-JET-LCU

- statement: Signed binomial interference is a genuinely original D22-compliant mechanism
  that extracts a multiplicity-$k$ local-algebra jet with polynomial success uniformly in
  $k$ and the deformation resolution.
- status: REFUTED
- depends-on: none
- where-proved: refuted in this memo, §3
- where-tested: none
- referee: not yet reviewed
- surviving statement: The binomial sum cancels orders below $k$, but it is standard
  finite differencing implemented by LCU and has success
  $\|r_k(h)\|^2/4^k\sim h^{2k}\|\psi^{(k)}(0)\|^2/4^k$; its jet is also gauge-dependent.
- north-star relevance: fails both the originality and resource criteria of D22.

**Recommendation.** Retain C-NEW-OA-UNZIP-IDENTITY only as a bounded theory question and
hold C-NEW-OA-UNZIP-SPEEDUP. Do not promote either to an arm until quotient multiplication
is built from equations without solving the quotient and a non-trace, non-eigenvalue useful
output is proved. Merge the three negative rows because they prevent attractive algebraic
identities from being mistaken for new algorithms.
