# Waring component packets by determinant fusion

Constructor memo, 2026-09-05. All claims below are merge proposals awaiting the
independent critic; this file does not assign claim-register status. It uses the
standard tensor Hilbert norm, explicitly departing from the cross-degree Fock
default C1; the local dimension is `q=n+1` as in C2. The notation is local to this
scouting proposal and needs canonical definition IDs before a claim merge.

The strongest constructed operation is an exact, basis-independent conversion of
copies of a Waring tensor into larger component packets. Its probability and
recursive copy cost are explicit. No matched classical separation is proved.
The independent critic identifies an explicit reduction to known redundant-
encoding Bell fusion: the rank-two mechanism fails D22. Its proposed originality
claim should enter the shared register as REFUTED; the exact conversion survives.

## 1. Precisely stated task and access

Fix `k>=3`, `q>=2`. The input source supplies independent copies of the normalized
pure tensor

\[
 |T\rangle=c_u|u\rangle^{\otimes k}+c_v|v\rangle^{\otimes k},
 \qquad \|u\|=\|v\|=1,
 \quad c_uc_v\ne0,\quad |⟨u,v⟩|<1.
\]

The Waring decomposition is unique, up to order and the usual projective scaling,
on this rank-two, independent-component family. Geometrically its two projective
points are the reduced length-two apolar support on the Veronese variety.
Neither component state, an inverse source circuit, nor a description of the
hidden change of basis is supplied. A query means one fresh `T` copy. The initial
claim is a quantum-input/quantum-output source conversion, not a classical
coefficient-list algorithm.

For requested integers `h>=1` and accuracy `epsilon>0`, output an `h`-register
state within trace distance `epsilon` of

\[
 \Sigma_h(T)=\tfrac12\bigl(|u\rangle\langle u|^{\otimes h}
                         +|v\rangle\langle v|^{\otimes h}\bigr).
\]

This outputs an unlabeled sample of a component packet, not its coordinate
description, not a classical Waring decomposition, and not the input weights.
One may instead request the distribution of a specified efficient measurement
on this same output; every proposed classical comparison must then use that
same measurement/output. Scalar-output comparisons must allow arbitrary
adaptive global single-copy measurements, not merely computational-basis samples.

Write `s=<u,v>`, `t=|s|^2`, `g=1-t`. Promises `g>=g_*` and
`p_0>=p_*` below make the cost uniform; neither is inferred from fixed rank.

## 2. Actual circuit and exact seed identity

On two chosen local registers implement the measurement

\[
 P_-=(\mathbb 1-\operatorname{SWAP})/2,\qquad P_+=\mathbb 1-P_-.
\]

A Hadamard ancilla, controlled SWAP, Hadamard, and ancilla measurement implement
it with `O(log q)` elementary gates. Retain only outcome `-`; all affected source
copies are discarded on failure. The two measured registers may also be
discarded after success, because the following identities factor them out.

Define the normalized packet

\[
 |\Psi_m^-\rangle=
 \frac{|u\rangle_A^{\otimes m}|v\rangle_B^{\otimes m}
       -|v\rangle_A^{\otimes m}|u\rangle_B^{\otimes m}}
      {\sqrt{2(1-t^m)}} .                                      \tag{1}
\]

Apply `P_-` between one slot of each of two `T` copies. Equal labels vanish;
the two remaining cross terms have opposite signs. With
`omega=(u tensor v-v tensor u)/sqrt(2g)`, the result is

\[
 c_uc_v\sqrt{g(1-t^{k-1})}\,|\omega\rangle\otimes
 |\Psi_{k-1}^-\rangle,
 \qquad p_0=|c_uc_v|^2g(1-t^{k-1}).                            \tag{2}
\]

The seed therefore costs `2/p_0` source copies in expectation. A small `p_0`
is expensive. Collision alone need not make it small: normalized destructive
coefficient cancellation can keep `p_0` tending to `(k-1)/k^2` as `u` and `v`
coalesce. The separately supplied `g_*` controls the fusion bound; it does not
replace the `p_*` promise.

## 3. Fusion and a resource theorem to audit

Take two independently prepared `m` packets. Apply `P_-` between one `A` slot
of packet 1 and one `B` slot of packet 2. Group the unmeasured `A` slots together
and the unmeasured `B` slots together. The equal orientations survive; opposite
orientations vanish. The output is exactly `Psi_(2m-1)^-`, with

\[
 p_m=\frac{g(1-t^{2m-1})}{4(1-t^m)^2}\ge\frac g4.              \tag{3}
\]

Proof: expand the four orientation terms. The first contributes
`sqrt(g/2) omega tensor u^(2m-1) tensor v^(2m-1)`; the fourth contributes its
negative orientation reversal. Divide by the two input normalizations and take
the squared norm using (1). For `m>=1`, `t^(2m-1)<=t^m`, proving the bound.

Prepare the two children offline, and rebuild them both following a failed
fusion. This is different in cost from demanding simultaneous success on a
predetermined tree. If `m_j=1+(k-2)2^j`, the expected source-copy count satisfies

\[
 C_0=2/p_0,\qquad C_{j+1}=2C_j/p_{m_j},\qquad
 C_j\le\frac2{p_0}(8/g)^j.                                  \tag{4}
\]

This is polynomial in the requested packet size for fixed `g>0`, with exponent
`log_2(8/g)`. It is **not** polynomial jointly in `1/g` and packet size: the
exponent itself grows as the components collide. A recursion with depth-first
storage uses `O(m_j log q)` qubits. Expected gate work is
`O(C_j k log q)` including source-register handling, plus source preparation
cost `C_j G_T` and its supplied preparation workspace if a preparation circuit
of gate cost `G_T` is separately available.
All restarts are included; no failed-state restoration is assumed.

Retain `h<=m` slots from side `A` of (1) and trace out everything else. Direct
partial trace gives

\[
 \rho_{m,h}=\frac{U_h+V_h-s^ht^{m-h}|u^h\rangle\langle v^h|
             -\bar s^ht^{m-h}|v^h\rangle\langle u^h|}
                 {2(1-t^m)},                                \tag{5}
\]

where `U_h=|u^h><u^h|` and `V_h=|v^h><v^h|`. After making `s` real by a harmless
component phase convention, diagonalize in the normalized vectors `u^h +/- v^h`.
The exact trace distance is

\[
 \tfrac12\|\rho_{m,h}-\Sigma_h\|_1
   =\frac{(1-t^h)t^{m-h/2}}{2(1-t^m)}.                        \tag{6}
\]

For `h=m`, it is `|s|^m/2`. In fact `rho_(m,m)` is exactly half the orthogonal
projector onto `span{u^m,v^m}`. This also supplies a useful geometric description
of the packet algorithm: it grows a Veronese secant-line support.
Choose the smallest attainable `m_j>=h` with
`(1-g_*)^(m_j/2)/2<=epsilon`, using the supplied lower promise `g_*`, not the
unknown overlap. Use (2)--(4) and discard surplus slots. The known upper bound
`Cbar_j=(2/p_*)(8/g_*)^j` gives a usable resource budget: Markov truncation at
`3 Cbar_j` source copies succeeds with probability at least `2/3`. Abort flags
are explicit; the actual `p_0,t` are used only to analyze performance.

## 4. Explicit family and matched classical attacks

For any `q>=2` and arbitrary unknown unitary `W` on `C^q`, let

\[
 u=W e_0,\quad v=W(\tfrac12e_0+\tfrac{\sqrt3}2e_1),\quad
 k=3,\quad T=\tfrac23(u^{\otimes3}+v^{\otimes3}).              \tag{7}
\]

Then `s=1/2`, `g=3/4`, `p_0=5/36`, `m_j=1+2^j`, and
`C_j<=(72/5)(32/3)^j`, independently of `q`. This is a nonorthogonal family,
with exponentially many ambient coordinates when `q=2^b`; its source must still
be supplied in the stated model. Supplying `W` as a classical circuit would
give direct component preparation and destroy the intended access distinction.

The strongest immediate classical attacks are:

1. **Explicit input:** read and decompose the low-rank tensor using flattenings,
   Hankel matrices, or simultaneous diagonalization. State preparation from a
   coefficient list is charged to the quantum algorithm; this memo proves no
   improvement over these methods. Brachat--Comon--Mourrain--Tsigaridas,
   [arXiv:0901.3706](https://arxiv.org/abs/0901.3706), is a primary baseline anchor,
   not an adjudication of best-known complexity for the precise task here.
2. **Known component encoding:** represent every packet by its two vectors and
   a `2x2` Gram matrix; all probabilities and terminal observables are cheap
   whenever vector evaluation and sampling are cheap. Exponential Hilbert-space
   dimension by itself supplies no advantage.
3. **Single-copy coherent output:** for orthogonal components, retaining `h<k`
   slots of one `T` copy already outputs a weighted component mixture. In the
   equal-weight case this is exactly the target. A measure-and-prepare-only
   comparator would exclude this trivial quantum memory and must be declared.
4. **Classical terminal data:** after choosing a scalar observable, a low-order
   moment or randomized single-copy measurement may estimate the same result
   without ever preparing the packet. No tomography lower bound proves otherwise.

The missing speedup lemma is precise: exhibit a terminal classical task with
the above source access and family, and prove that *every* adaptive sequence of
arbitrary single-copy POVMs needs asymptotically more copies than (4), or supply
an equally explicit same-quantum-output classical comparison. No such lemma is
proved here. This alone prevents a north-star claim, independent of D22.

## 5. Targeted novelty check: rank-two D22 failure

The construction was derived before searching. Primary sources fetched afterward:

- Browne--Rudolph, [arXiv:quant-ph/0405157](https://arxiv.org/html/quant-ph/0405157v2),
  gives redundant photon encodings, Type-II destructive Bell fusion, and offline
  assembly with expected resource accounting. Its displayed Kraus bras in the
  redundant-encoding discussion are Bell contractions on arbitrary attached
  states. A fixed local Pauli gives the singlet Bell bra.
- Zhao--Pan--Zhan, [arXiv:quant-ph/0104039](https://arxiv.org/abs/quant-ph/0104039),
  concentrates unknown-weight pure entanglement from two copies through a
  conditional GHZ state. This is a relevant seed comparison, not by itself an
  exact identification of (2).

The reduction is stronger than saying that the circuit contains known gates.
Write the injective map `E:C^2 -> C^q` as `E|0>=u`, `E|1>=v`. Then

\[
 P_-^{(q)}(E\otimes E)=(E\otimes E)P_-^{(2)},\qquad
 \langle\omega_2|(L\otimes L)=\det(L)\langle\omega_2|       \tag{8}
\]

for square `L` in the polar factorization `E=QL`. Every fusion tree above is
therefore the image under the same unknown local `E` of a redundant-qubit
GHZ/Bell fusion tree. The determinant and norms explain all overlap-dependent
success factors. Neither an implementation of `E` nor its inverse is needed in
this identity. The independent critic and orchestrator both identify this as
the existing redundant-GHZ fusion network under a nonorthogonal encoding.
The Waring interpretation and overlap-dependent cost analysis do not supply a
new mechanism under D22. See the independent audit in
`verdicts/waring-fusion-r1.md`; that verdict's precise scope remains binding.

## 6. Higher-rank determinant variant

For `T=sum_(a=1)^r c_a u_a^k` with independent unit `u_a`, let
`G=(<u_a,u_b>)`, `G_m=(<u_a,u_b>^m)`. Alternating one slot from each of `r` source
copies produces the permutation packet

\[
 \Omega_m^-\propto\sum_{\pi\in S_r}\operatorname{sgn}(\pi)
           \bigotimes_{i=1}^r u_{\pi(i)}^{\otimes m},
 \quad m=k-1,\quad p_0=|\prod_a c_a|^2\det G\det G_m.          \tag{9}
\]

Two packets can be synchronized with `r-1` disjoint alternating hyperedges.
For each `j=1,...,r-1`, consume one slot from every row `i!=j` of packet 1 and
one slot from row `j` of packet 2, and project those `r` slots onto `wedge^r`.
The first packet already has distinct labels, so this hyperedge forces the
second packet's row `j` label to match the first. The last row then matches too.
Every surviving row has exponent `ell=2m-r+1`; growth requires `m>r-1`.
If packet coefficients have sign parity `sigma in {0,1}`, the output parity is
`sigma_out=sigma_1+sigma_2+r-1 mod 2`. Even `r` keeps alternating packets;
odd `r` becomes symmetric after the first fusion and remains symmetric.

For `Z_m^sigma` the squared norm of the unnormalized permutation sum, the exact
proposed probability is

\[
 p_m=\left(\frac{\det G}{r!}\right)^{r-1}
       \frac{Z_{2m-r+1}^{\sigma_{out}}}
            {Z_m^{\sigma_1}Z_m^{\sigma_2}}.                  \tag{10}
\]

This determinant synchronization is a separately held second candidate, not a proven escape
from known multipartite fusion or from the classical-output obstruction.
It is exponentially costly in growing `r` already on orthogonal components;
only fixed `r` is a plausible regime. Its exact prior-art equivalence and any
useful growing-r bound remain unaudited, so rank two remains the strongest fully
costed construction.

## 7. Checks and disposition

An inline NumPy run with one BLAS thread and a 45-second timeout checked (2),
(3), and (6) on random complex vectors in dimensions 2 and 3, `k=3,4`, and
`m=2,3` where feasible: 63 scalar/vector checks, worst residual `1.33e-15`.
This is exploratory evidence, not a registered red-capable checker. No shared
claim/definition files were changed.

There is a concrete optical test on the `q=2,k=3` family: two three-photon input
states, one successful singlet projection, and tomography of the retained four
photons test (2). Four inputs and three successful singlet projections test the
next packet step. On (7), the next fusion succeeds with probability `21/100`;
offline preparation needs `960/7` source copies in expectation, compared with
`6912/7` if all three singlet events are demanded on fresh four-copy trees.
General `q` has an ideal controlled-SWAP implementation;
scalable high-dimensional optical encoding is not assumed free.

The surviving product is an exact packet conversion and recursive resource
bound. Classical advantage is unresolved and rank-two mechanism novelty fails
D22 by (8). The separately held higher-rank construction has no originality or
speedup certificate; rank-two failure is not a theorem about every higher rank.
