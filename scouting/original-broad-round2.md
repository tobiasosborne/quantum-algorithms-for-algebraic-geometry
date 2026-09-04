# Round 2 broad pass: correspondences and birational order

**Verdict.** No D22 survivor was found. Two concrete mechanisms were constructed from
algebraic correspondences and moduli-chart transformations, then reduced respectively to
classical collision sampling / LCU and to a controlled-order quantum switch. The reductions
are exact; the classical runtime comparison requires matched classical history
sampling, as clarified after verdicts/original-round2-r1.md. Historical novelty
is unverified, and no web search was used. This memo locally departs from C7:
its displayed alpha parameters denote block-encoding normalizations.

This memo does not use quotient multiplication, Fock states, root search, spectral
estimation, copy-polynomial transduction, or linear/Grassmann intersection.

## 1. Coherent fusion of algebraic correspondences

### Problem and access

Let
\[
 X_0 \xleftarrow{\ C_1\ } X_1 \xleftarrow{\ C_2\ }\cdots
 \xleftarrow{\ C_r\ }X_r
\]
be finite algebraic correspondences over a fixed field, with a fixed input point
$x\in X_0$. A *history* $h\in H_x$ is a branch through the fibre product
$C_1\times_{X_1}\cdots\times_{X_{r-1}}C_r$ above $x$; $e(h)\in X_r$ is its endpoint.
The access model supplies:

- a uniform preparation of the finite history-label set $H_x$, of size $P$,
  and its inverse, each of charged cost $C_H$;
- a reversible circuit of cost $C_e$ computing $h\mapsto e(h)$;
- a unit-modulus local weight $w_h$ computable reversibly from declared branch
  data, at charged phase-circuit cost $C_w$.

The positive runtime comparison additionally assumes a classical uniform-history
sampler of cost $O(C_H)$ and matched classical endpoint evaluation of cost $O(C_e)$.
Quantum preparation alone does not supply that classical sampler.

If scheme multiplicities are wanted, the input circuit must enumerate branches with those
multiplicities; this is charged, not inferred from equations. Define the composite coefficient
\[
 c_z=\sum_{h:e(h)=z}w_h.
\]

**Composite-fibre coefficient sampling (CFCS), provisional:** output $z$ with probability
$|c_z|^2/\sum_y|c_y|^2$. The candidate computational result is sampling coefficients of a
composed correspondence without materialising its fibre product. The candidate mechanism is
coherent erasure of intermediate branches so that equal endpoints fuse in amplitude.

### Operation and derived identity

Prepare
\[
 |\Psi\rangle={1\over\sqrt P}\sum_{h\in H_x}w_h|h\rangle|e(h)\rangle .
\]
Project the history register onto
$|+\rangle_H=P^{-1/2}\sum_h|h\rangle$. The unnormalised endpoint state is
\[
 (\langle+|_H\otimes\mathbb 1)|\Psi\rangle
 ={1\over P}\sum_z c_z|z\rangle,
\]
so
\[
 p_{\rm fuse}={\sum_z|c_z|^2\over P^2}.
\]
Conditional measurement solves CFCS exactly. One attempt costs
$2C_H+C_e+C_w+O(\log P)$ gates and
$O(\log P+\log|X_r|)$ qubits plus the supplied circuits' workspaces and flags;
failure probability $\delta$ costs
$O(p_{\rm fuse}^{-1}\log(1/\delta))$ attempts. No amplitude amplification is credited.

This resembles physical path erasure in a multiport interferometer, but the actual resource
is the coherent history oracle and the postselection probability. Constructing that oracle
from equations for a multivalued correspondence generally requires solving its finite fibres.
For explicit morphisms the next branch is deterministic, so the proposed exponential history
space disappears.

### Exact positive dequantization

Suppose $w_h=1$ and write $m_z=|\{h:e(h)=z\}|$. A classical algorithm draws two independent
uniform histories $h,h'$, accepts exactly when $e(h)=e(h')$, and outputs that endpoint. Then
\[
 \Pr[\mathrm{accept\ and\ output}\ z]={m_z^2\over P^2},\qquad
 \Pr[\mathrm{accept}]=\sum_z{m_z^2\over P^2}=p_{\rm fuse}.
\]
Its conditional distribution and expected repetitions are identical to the quantum
procedure, with two classical endpoint evaluations versus one coherent evaluation.
The equality of output laws is exact. With the matched-access assumption above,
their per-attempt costs are comparable, so positive fusion supplies no asymptotic
advantage over collision sampling. Without that assumption only equality of laws
has been proved, not a classical algorithm at the quantum preparation cost.

### Signed attack and equivalence audit

Signs or phases invalidate the acceptance interpretation because $c_z$ contains cancellation.
They do not produce a D22 mechanism. Projection onto $|+\rangle_H$ is precisely a
postselected linear combination of the history maps: the effective block is
$P^{-1/2}\sum_hw_h|e(h)\rangle\langle h|$. The second factor $P^{-1/2}$
comes from the prepared uniform input. Extend each endpoint preparation to an
isometry/unitary to write the usual controlled-label LCU implementation.
Thus signed CFCS is an LCU/path-sum circuit.
If cancellation is severe, $p_{\rm fuse}$ is exponentially small; if it is not, the circuit
is still a known mechanism applied to a new coefficient problem. Grover amplification,
Fourier analysis of $H_x$, a walk on the fibre graph, or phase estimation would each add an
explicitly disallowed known algorithm.

For explicit correspondences, sparse dynamic programming combines equal endpoints as it
advances through the chain. Its cost is polynomial in the number of reached endpoints and
branches, often far smaller than $P$. For succinct endpoint circuits, a hardness claim can
encode arbitrary circuit interference and is not automatically algebraic-geometric.

**Held hypothesis H-CFCS-SIGN (do not merge).** There may be a natural arithmetic-geometric
chain whose local signs arise intrinsically, whose history oracle is constructible without
finding its fibres, with $p_{\rm fuse}\ge1/\operatorname{poly}$, and whose CFCS law is
classically hard. No example or lower bound is supplied. Even proving this hypothesis would
not satisfy D22 with the present LCU mechanism.

## 2. Birational order-defect interferometer

### Problem, operation, and identity

Let $\phi,\psi$ be two birational self-transformations of a moduli chart, and let
$B_\phi,B_\psi$ be their pullbacks on a finite-dimensional section space $S$ preserved by
both maps. The input supplies block encodings $B_\phi/\alpha_\phi$ and
$B_\psi/\alpha_\psi$ and a section state $|s\rangle$. The proposed task is to distinguish
\[
 K|s\rangle=0\quad\hbox{from}\quad
 \|K|s\rangle\|\ge\gamma,\qquad
 K=B_\psi B_\phi-B_\phi B_\psi,
\]
and, in the second case, sample coefficients of the normalised order-defect section.

Prepare a control in $|+\rangle$. On control zero apply $B_\psi B_\phi$; on control one
apply $B_\phi B_\psi$. After a Hadamard, postselection on the minus control and all block
flags gives
\[
 {K|s\rangle\over2\alpha_\phi\alpha_\psi},\qquad
 p_-={\|K|s\rangle\|^2\over4\alpha_\phi^2\alpha_\psi^2}.
\]
This is a direct derived signal for failure of two chart transformations to commute.

For a concrete rank-two birational example,
\[
 \phi(x,y)=((1+y)/x,y),\qquad \psi(x,y)=(x,(1+x)/y).
\]
On the rational section $s=x$,
\[
 (B_\psi B_\phi-B_\phi B_\psi)s
 ={x+y+1\over xy}-{1+y\over x}
 ={x+1-y^2\over xy}\ne0.
\]
The quantum branch has merely reproduced two short rational substitutions and their
difference.

### Strongest attacks

- With explicit transformations, controlled order is an ordinary controlled circuit, not
  indefinite causal structure. With unknown channel oracles it is the established quantum
  switch. Either interpretation fails D22's original-mechanism test.
- Classical symbolic composition evaluates both orders on chart generators. Random-point
  polynomial identity testing detects a nonzero rational commutator after clearing
  denominators. Sparse monomial maps are cheaper still.
- Near commuting maps have $p_-=O(\gamma^2/(\alpha_\phi^2\alpha_\psi^2))$; repeated
  postselection costs its reciprocal. Amplitude amplification would append Grover.
- If $\dim S$ is exponentially large, a classical-output comparison incurs tomography,
  while a succinct quantum block oracle may hide an arbitrary circuit. Neither establishes
  a moduli-specific advantage for the same output.

**Held hypothesis H-ORDER-GEOMETRY (do not merge).** A norm of a pullback commutator might
admit an intrinsic interpretation in terms of noncommuting elementary modifications or
Hecke-type correspondences. No basis-independent norm, gap theorem, or equation-level access
construction is supplied; the present measurement would remain a quantum-switch application.

## MERGE PROPOSAL

### C-NEW-OB-POSITIVE-FUSION

- statement: Even when uniform histories and endpoints have matched classical
  sampling/evaluation costs, positive coherent fusion of a succinct chain of finite
  correspondences gives an asymptotic advantage for squared fibre-multiplicity sampling.
- status: REFUTED
- depends-on: none
- where-proved: refuted in this memo, §1, “Exact positive dequantization”
- where-tested: none
- referee: not yet reviewed
- surviving statement: Quantum path erasure and classical two-history collision sampling
  have exactly the same success probability and conditional endpoint law; matched
  per-attempt costs additionally require the declared classical history access.
- north-star relevance: an unconditional dequantization of the positive construction.

### C-NEW-OB-SIGNED-FUSION

- statement: Adding intrinsic signs to correspondence histories makes coherent fusion a
  genuinely original D22-compliant quantum mechanism.
- status: REFUTED
- depends-on: none
- where-proved: refuted in this memo, §1, “Signed attack and equivalence audit”
- where-tested: none
- referee: not yet reviewed
- surviving statement: Signed fusion prepares coefficients with success
  $\sum_z|c_z|^2/P^2$, but is exactly postselected LCU and may have exponential cancellation.
- north-star relevance: a possible coefficient-sampling problem, but not a qualifying mechanism.

### C-NEW-OB-ORDER-DEFECT

- statement: Coherently superposing the two orders of birational pullbacks supplies a
  genuinely original D22 algorithm for detecting noncommuting moduli transformations.
- status: REFUTED
- depends-on: none
- where-proved: refuted in this memo, §2
- where-tested: none
- referee: not yet reviewed
- surviving statement: The minus branch is exactly
  $(B_\psi B_\phi-B_\phi B_\psi)|s\rangle/(2\alpha_\phi\alpha_\psi)$, but its implementation
  is a controlled circuit or quantum switch and its classical baseline is direct composition.
- north-star relevance: fails originality and supplies no same-output speedup.

**Recommendation.** Merge the three negative rows. Keep both held hypotheses only as
boundary markers: neither has a qualifying mechanism, a noncircular access theorem, or a
classical separation.
