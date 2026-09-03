# Quantum-native varieties: Arm D, exploration round 2

## Statement and sketch

### Scope corrections

- The multigraded QSAT statement is C-030–C-039 and uses D-multidegree-sector and D-quantum-k-sat.
- Proposition 8.2 is C-129/C-130, not C-125.
- C-125 is the unproved BQP-containment subclaim for ground-overlap estimation and still depends on asserted sparse-access oracles.
- Proposition 8.2 concerns the ordinary total-degree bosonic sector after adding D-hard-core-generators.
- The inverse-system statement below concerns the native multidegree \(\mathbf1=(1,\ldots,1)\) sector.
- Under C3, the ground space is the orthogonal complement of \((I_Q)_{\mathbf1}\), equivalently the multidegree-\(\mathbf1\) piece of the Macaulay inverse system of \(\overline{I_Q}\).
- No step constructs a D-parent-hamiltonian for \(I_{\mathbf1}\); the QSAT Hamiltonian has kernel \((I_Q)_{\mathbf1}^{\perp}\), as required by C-008/C-009.
- The broad PRD §4 assertion that Arm D offers no north-star speedup remains unproved. This memo establishes only the tautological negative for algorithms obtained by composing an existing algorithm with the polynomial-time, spectrum-preserving relabelling dictionary.
- Copy-access membership and distance problems are outside that tautology. Their correct classical comparator is adaptive single-copy measurement followed by classical post-processing.
- The Arm D north-star row is therefore a CONJECTURE under HOLD, not a discharge of PRD §4.

### The QSAT–inverse-system identity

**1. PROVE.**  
For every \(n\)-qudit quantum \(k\)-SAT instance, its zero-energy space equals the multidegree-\(\mathbf1\) piece of a Macaulay inverse system.

**1.1 ASSUME.**  
Let the \(i\)-th site be \(\mathcal H_i=\mathbb C^q\), with basis
\(\{|0\rangle,\ldots,|q-1\rangle\}\).  
[D-multidegree-sector, C2]

**1.2 ASSUME.**  
Let

\[
R=\mathbb C[z_{i,s}:1\le i\le n,\ 0\le s<q],
\qquad
\deg z_{i,s}=e_i\in\mathbb Z^n.
\]

[D-multidegree-sector]

**1.3 PROVE.**  
The map

\[
z_{1,s_1}\cdots z_{n,s_n}
\longleftrightarrow
|s_1\cdots s_n\rangle
\]

is a unitary identification

\[
R_{\mathbf1}\cong\bigotimes_{i=1}^n\mathcal H_i.
\]

All monomials in this sector have Fock norm one.  
[D-multidegree-sector, C1]

**1.4 ASSUME.**  
Let

\[
H_Q=\sum_{a=1}^{M}\Pi_a
\]

be a quantum \(k\)-SAT Hamiltonian, where \(\Pi_a\) acts on
\(S_a\subseteq[n]\), \(|S_a|\le k\).  
[D-quantum-k-sat, D-frustration-free]

**1.5 PROVE.**  
Choose an orthonormal basis of the range of each projector:

\[
\Pi_a=\sum_{\mu=1}^{r_a}|\phi_{a\mu}\rangle\langle\phi_{a\mu}|.
\]

Since \(q\) and \(k\) are fixed, \(r_a\le q^k\), so splitting a clause increases the description by only a constant factor.  
[C-032, arXiv:quant-ph/0602108]

**1.6 DEFINE.**  
If

\[
|\phi_{a\mu}\rangle
=
\sum_{(s_i)_{i\in S_a}}
c^{(a\mu)}_{(s_i)}
\bigotimes_{i\in S_a}|s_i\rangle,
\]

associate the multilinear form using the coefficients unconjugated:

\[
f_{a\mu}
=
\sum_{(s_i)_{i\in S_a}}
c^{(a\mu)}_{(s_i)}
\prod_{i\in S_a}z_{i,s_i}.
\]

Its multidegree is \(\mathbf1_{S_a}=\sum_{i\in S_a}e_i\). The unconjugated convention is what makes step 1.8 produce
\(|\phi_{a\mu}\rangle\langle\phi_{a\mu}|\).  
[D-multidegree-sector, C3]

**1.7 DEFINE.**  
Let

\[
I_Q=(f_{a\mu}:1\le a\le M,\ 1\le\mu\le r_a)\subseteq R.
\]

This ideal is independent of the chosen orthonormal rank-one decomposition: a change of orthonormal basis in \(\operatorname{ran}\Pi_a\) applies an invertible unitary change of generators to
\(\operatorname{span}_{\mu}\{f_{a\mu}\}\).  
[D-homogeneous-ideal, D-quantum-k-sat, D-QN-QSAT-IDEAL]

**1.8 PROVE.**  
For every \(a,\mu\),

\[
a^\dagger(f_{a\mu})a(f_{a\mu})\big|_{R_{\mathbf1}}
=
|\phi_{a\mu}\rangle\langle\phi_{a\mu}|_{S_a}
\otimes\mathbb1_{\overline{S_a}}.
\]

There are no factorial factors in this sector.  
[D-multidegree-sector, C-031]

**1.9 PROVE.**  
Summing the rank-one terms gives exact operator equality:

\[
H_Q
=
\left.
\sum_{a,\mu}a^\dagger(f_{a\mu})a(f_{a\mu})
\right|_{R_{\mathbf1}}.
\]

[D-hamiltonian, D-quantum-k-sat]

**1.10 DEFINE.**  
The \(\mathbf1\)-graded Macaulay map is

\[
\Phi_{\mathbf1}:
\bigoplus_{a,\mu}R_{\mathbf1-\mathbf1_{S_a}}
\longrightarrow R_{\mathbf1},
\qquad
(h_{a\mu})\longmapsto\sum_{a,\mu}f_{a\mu}h_{a\mu}.
\]

[D-macaulay-map, D-multidegree-sector]

**1.11 PROVE.**  
Its range is precisely the graded ideal piece:

\[
\operatorname{ran}\Phi_{\mathbf1}=(I_Q)_{\mathbf1}.
\]

[D-homogeneous-ideal]

**1.12 PROVE.**  
Under the identification in 1.3,

\[
\operatorname{ran}\Phi_{\mathbf1}
=
\sum_a\operatorname{ran}
\left(\Pi_a\otimes\mathbb1_{\overline{S_a}}\right).
\]

A multiplier monomial in
\(R_{\mathbf1-\mathbf1_{S_a}}\) selects an arbitrary computational-basis state on the complementary sites.  
[D-multidegree-sector]

**1.13 PROVE.**  
The Hamiltonian is the Gram operator

\[
H_Q=\Phi_{\mathbf1}\Phi_{\mathbf1}^{\dagger}.
\]

[D-hamiltonian, C-008]

**1.14 PROVE.**  
Therefore

\[
\ker H_Q
=
\ker\Phi_{\mathbf1}^{\dagger}
=
\left((I_Q)_{\mathbf1}\right)^\perp.
\]

This is the multigraded instance of C-008.  
[D-ground-space, C-008]

**1.15 PROVE.**  
By C3 and D-inverse-system,

\[
\ker H_Q
=
\left\{
u\in R_{\mathbf1}:
\overline f(\partial)u=0
\text{ for every }f\in I_Q
\right\}.
\]

This is the multidegree-\(\mathbf1\) piece of the Macaulay inverse system of
\(\overline{I_Q}\).  
[D-inverse-system, C3, C12]

**1.16 CAUTION.**  
The expressions
\((I_Q^\perp)_{\mathbf1}\) and
\((\overline{I_Q}^{\,\perp})_{\mathbf1}\) are not used. Under the register’s notation, the latter would mean
\(((\overline{I_Q})_{\mathbf1})^\perp\), which generally differs from
\(((I_Q)_{\mathbf1})^\perp\) for complex coefficients.  
[D-inverse-system, C3]

**1.17 PROVE.**  
The ground-state degeneracy is

\[
g_Q
=
\dim\ker H_Q
=
\dim R_{\mathbf1}-\dim(I_Q)_{\mathbf1}
=
\operatorname{HF}_{R/I_Q}(\mathbf1).
\]

Since \(\dim R_{\mathbf1}=q^n\), explicitly forming this matrix is exponential.  
[D-ground-space, D-hilbert-function, C-009]

**1.18 PROVE.**  
The instance is frustration free exactly when

\[
\operatorname{HF}_{R/I_Q}(\mathbf1)>0.
\]

If this Hilbert value is zero, \(H_Q\) is positive definite on the physical sector.  
[D-frustration-free, D-quantum-k-sat]

**1.19 PROVE.**  
The promise problem

\[
\operatorname{HF}_{R/I_Q}(\mathbf1)>0
\quad\text{versus}\quad
\lambda_{\min}(H_Q)\ge 1/\operatorname{poly}(n)
\]

is precisely quantum \(k\)-SAT, not a new reduction to it.  
[D-quantum-k-sat, C-034–C-038]

**1.20 PROVE.**  
For qubit \(2\)-QSAT this promise decision problem is classically polynomial-time solvable
(arXiv:quant-ph/0602108).

**1.21 PROVE.**  
For qubit \(3\)-QSAT it is \(\mathrm{QMA}_1\)-complete
(arXiv:1302.0290).

**1.22 PROVE.**  
For bilinear constraints on unequal local dimensions \((2,5)\), it is already
\(\mathrm{QMA}_1\)-complete
(arXiv:2401.02368).

**1.23 CAUTION.**  
\(\mathrm{QMA}_1\)-completeness is a promise-problem hardness result for verification with a quantum witness. Without the NO-gap promise, exact Hilbert-function nonvanishing is not thereby placed in \(\mathrm{QMA}_1\). Neither statement supplies a BQP ground-state preparation algorithm.  
[D-quantum-k-sat, C-038]

### Product ground states and the multiprojective variety

**2. PROVE.**  
Product ground-state rays are exactly the points of a multiprojective variety, and their linear span can be separated from the full ground space.

**2.1 DEFINE.**  
Let

\[
X_0=(\mathbb P^{q-1})^n.
\]

A point \(x=([x_1],\ldots,[x_n])\in X_0\) represents the physical product ray

\[
|\overline{x_1}\rangle\otimes\cdots\otimes|\overline{x_n}\rangle.
\]

[D-coherent-state, D-multidegree-sector, C3]

**2.2 PROVE.**  
For every generator \(f_{a\mu}\),

\[
\langle\phi_{a\mu}|
\bigotimes_{i\in S_a}|\overline{x_i}\rangle
=
\overline{f_{a\mu}(x)}.
\]

[D-coherent-state, C3]

**2.3 PROVE.**  
Thus

\[
\bigotimes_i|\overline{x_i}\rangle\in\ker H_Q
\quad\Longleftrightarrow\quad
x\in V_{X_0}(I_Q).
\]

[D-variety, D-multidegree-sector, C-033]

**2.4 DEFINE.**  
Let

\[
B=\bigcap_{i=1}^{n}(z_{i,0},\ldots,z_{i,q-1})
\]

be the irrelevant ideal of the Cox ring of \(X_0\), and set

\[
J_Q=\sqrt{I_Q:B^\infty}.
\]

By the multiprojective Nullstellensatz, \(J_Q\) is the multihomogeneous vanishing ideal of the reduced closed subscheme
\(V_{X_0}(I_Q)\subseteq X_0\), of any dimension. Adopt \(I(\varnothing)=R\). Indeed,
\(V_{X_0}(I_Q)=\varnothing\) implies \(B\subseteq\sqrt{I_Q}\), hence
\(B^k\subseteq I_Q\) for some \(k\), so \(I_Q:B^\infty=R\) and \(J_Q=R\).  
[D-QN-MULTIPROJECTIVE-SATURATION; [Feigin–Makhlin, Theorem 1.8.1](https://doi.org/10.1007/s00029-024-00935-5)]

**2.5 PROVE.**  
The linear span of all fully product ground states is

\[
\mathcal P_Q
=
\operatorname{span}
\left\{
\bigotimes_i|\overline{x_i}\rangle:
x\in V_{X_0}(I_Q)
\right\}
=
(J_Q)_{\mathbf1}^{\perp}.
\]

When \(V_{X_0}(I_Q)=\varnothing\), this span is \(\{0\}\). This is the Segre analogue of C-028.  
[D-coherent-state, C-028]

**2.6 PROVE.**  
Since \(I_Q\subseteq J_Q\),

\[
\mathcal P_Q\subseteq\ker H_Q.
\]

[D-ground-space, D-variety]

**2.7 DEFINE.**  
The multigraded entangled defect is

\[
e_Q
=
\dim\ker H_Q-\dim\mathcal P_Q
=
\dim(J_Q)_{\mathbf1}-\dim(I_Q)_{\mathbf1}.
\]

[D-entangled-defect, C-029]

**2.8 PROVE.**  
The orthogonal complement

\[
\ker H_Q\ominus\mathcal P_Q
\]

contains no product ray. Every nonzero vector in that complement is entangled.  
[D-entangled-defect]

**2.9 CAUTION.**  
\(e_Q\) is not the “number of entangled states.” A positive-dimensional linear space contains uncountably many state rays, and entangled superpositions can also lie inside \(\mathcal P_Q\).  
[D-entangled-defect]

**2.10 PROVE.**  
The ground space is spanned by product ground states if and only if

\[
(I_Q)_{\mathbf1}=(J_Q)_{\mathbf1}.
\]

This is a degreewise statement, not global radicality or saturation.  
[C-029; the contrary draft claim is REFUTED as C-216]

Laumann–Läuchli–Moessner–Scardicchio–Sondhi already established a geometrization theorem for the generic dimension of the product-satisfying manifold
(DOI:10.1103/PhysRevA.81.062345). The additional content proposed here is the degree-\(\mathbf1\) linear-span identity and the defect separating that span from the full QSAT ground space. Novelty of that additional content remains unestablished.

### Other multidegrees

**3. PROVE.**  
Other multidegrees encode bosonic extensions of QSAT, not further degeneracies of the original instance.

**3.1 PROVE.**  
For \(\mathbf r=(r_1,\ldots,r_n)\),

\[
R_{\mathbf r}
\cong
\bigotimes_{i=1}^{n}\operatorname{Sym}^{r_i}(\mathbb C^q),
\]

with dimension

\[
\dim R_{\mathbf r}
=
\prod_{i=1}^{n}\binom{r_i+q-1}{q-1}.
\]

[D-multidegree-sector, C1]

**3.2 PROVE.**  
The same polynomial Hamiltonian restricted to \(R_{\mathbf r}\) has kernel

\[
(I_Q)_{\mathbf r}^{\perp}
\]

and degeneracy \(\operatorname{HF}_{R/I_Q}(\mathbf r)\).  
[D-ground-space, D-inverse-system]

**3.3 CAUTION.**  
For \(\mathbf r\ne\mathbf1\), this describes \(r_i\) indistinguishable bosons at site \(i\). It is not the Hilbert space of \(r_i\) distinguishable copies of the original qudit.  
[D-multidegree-sector]

**3.4 PHYSICAL READING.**  
The function \(\mathbf r\mapsto\operatorname{HF}_{R/I_Q}(\mathbf r)\) is the degeneracy profile of this occupation-number extension.

**3.5 PHYSICAL READING.**  
Its eventual polynomial behavior records the dimension and multiprojective degree of the product-solution scheme, not the spectrum above the QSAT ground space.

**3.6 PHYSICAL READING.**  
Early-degree deviations record irrelevant torsion, nonreduced structure, and algebraic relations among constraints.

**3.7 CAUTION.**  
None of those quantities fixes the spectral gap. Generator rescaling and nearly dependent constraints can change the gap without changing the ideal or its Hilbert function.  
[D-macaulay-gap, D-normalised-gap]

### A Hilbert-function entanglement witness

**4. PROVE.**  
For a multihomogeneous ideal, vanishing in a sufficiently positive multidegree certifies an empty multiprojective zero locus. For a QSAT ideal with a nonzero physical-sector inverse system, this certifies that every ground state is entangled.

**4.1 ASSUME.**  
Let \(I\) be any multihomogeneous ideal in the Cox ring of
\((\mathbb P^{q-1})^n\). Let
\(\mathbf r\ge\mathbf1\) componentwise, with
\(\mathbf r\ne\mathbf1\), and suppose

\[
\operatorname{HF}_{R/I}(\mathbf r)=0.
\]

If \(I=I_Q\), also suppose

\[
\operatorname{HF}_{R/I_Q}(\mathbf1)>0.
\]

[D-hilbert-function]

**4.2 PROVE.**  
The vanishing says

\[
I_{\mathbf r}=R_{\mathbf r}.
\]

[D-hilbert-function]

**4.3 PROVE.**  
If \(x\in V_{X_0}(I)\), every element of \(I_{\mathbf r}\) vanishes at \(x\).  
[D-variety]

**4.4 PROVE.**  
At any multiprojective point \(x\), some monomial of degree \(\mathbf r\) is nonzero.  
[D-multidegree-sector]

**4.5 PROVE.**  
Thus \(R_{\mathbf r}\) cannot equal \(I_{\mathbf r}\) when a multiprojective solution exists.

**4.6 CONCLUDE.**  
Therefore

\[
V_{X_0}(I)=\varnothing.
\]

For \(I=I_Q\), the physical-sector Hilbert value is positive, so the ground space is nonzero but contains no product ray. With \(I(\varnothing)=R\),

\[
J_Q=R,
\qquad
e_Q=\operatorname{HF}_{R/I_Q}(\mathbf1).
\]

[D-QN-MULTIPROJECTIVE-SATURATION, D-entangled-defect]

**4.7 SPECIAL CASE.**  
The comparison

\[
\operatorname{HF}(\mathbf1)>0,
\qquad
\operatorname{HF}(2,\ldots,2)=0
\]

is a sufficient certificate of an entangled-only QSAT ground space.

**4.8 LIMITATION.**  
The converse fails: nonzero \(\operatorname{HF}(2,\ldots,2)\) does not imply a product ground state.

**4.9 COMPLETENESS.**  
This is a multihomogeneous Nullstellensatz certificate. Conversely, if
\(V_{X_0}(I)=\varnothing\), then \(I:B^\infty=R\), so \(B^k\subseteq I\) for some saturation exponent \(k\). Consequently
\(I_{\mathbf r}=R_{\mathbf r}\) for every sufficiently large componentwise multidegree, and some finite Hilbert-function level vanishes. No effective bound on the first such multidegree in terms of the encoded input parameters is established here; that degree-bound problem remains open in this memo.  
[D-QN-MULTIPROJECTIVE-SATURATION; [Feigin–Makhlin, Theorem 1.8.1](https://doi.org/10.1007/s00029-024-00935-5)]

### Two-qubit exact example

**5. PROVE.**  
The smallest entangled-only QSAT example is two qubits with one rank-three projector.

**5.1 DEFINE.**  
Let

\[
|\psi^-\rangle=\frac{|01\rangle-|10\rangle}{\sqrt2},
\qquad
\Pi=\mathbb1-|\psi^-\rangle\langle\psi^-|.
\]

This is one valid \(2\)-local QSAT clause of rank three.  
[D-quantum-k-sat]

**5.2 DEFINE.**  
Use the single ideal

\[
I=
\left(
x_0y_0,\;
x_1y_1,\;
x_0y_1+x_1y_0
\right)
\subseteq\mathbb C[x_0,x_1,y_0,y_1].
\]

Replacing the third generator by
\((x_0y_1+x_1y_0)/\sqrt2\) changes neither the ideal nor its Hilbert function, but it does rescale Macaulay minors.  
[C-032, C3]

**5.3 PROVE.**  
The three generators are independent in the four-dimensional \(R_{(1,1)}\), so

\[
\operatorname{HF}_{R/I}(1,1)=4-3=1.
\]

[D-hilbert-function]

**5.4 PROVE.**  
The inverse-system piece is

\[
(I_{(1,1)})^\perp=\mathbb C|\psi^-\rangle.
\]

[D-inverse-system, D-ground-space]

**5.5 PROVE.**  
The equations have no point in \(\mathbb P^1\times\mathbb P^1\).

**5.5.1.**  
If \(x_0=0\), projectivity gives \(x_1\ne0\).  
[D-variety]

**5.5.2.**  
Then \(x_1y_1=0\) gives \(y_1=0\), hence \(y_0\ne0\).  
[D-variety]

**5.5.3.**  
But \(x_0y_1+x_1y_0=x_1y_0\ne0\), a contradiction.  
[D-variety]

**5.5.4.**  
The other cases are symmetric.  
[D-variety]

**5.6 PROVE.**  
At bidegree \((2,2)\),

\[
\dim R_{(2,2)}=3^2=9.
\]

[D-multidegree-sector]

**5.7 PROVE.**  
For the unnormalised ideal in 5.2, the \(9\times12\) bidegree-\((2,2)\) Macaulay matrix has rank \(9\). Exactly \(18\) of its \(220\) maximal \(9\times9\) minors are nonzero, and each has
\(|\det|=1\) in the monomial basis; both determinant signs occur. With the
\(1/\sqrt2\)-normalised third generator, the corresponding nonzero absolute determinants are instead

\[
|\det|\in\{0.25,\ 0.353553\ldots,\ 0.5\}.
\]

These determinants are basis- and normalization-dependent under C1; the rank is the invariant conclusion.  
[D-macaulay-matrix, C1]

**5.8 CONCLUDE.**  
Therefore

\[
\operatorname{HF}_{R/I}(2,2)=0.
\]

The criterion in step 4 detects the unique singlet as entangled without optimizing over product states.  
[D-entangled-defect]

### Why degree \((2,\ldots,2)\) is not complete

**6. REFUTE.**  
The implication

\[
\operatorname{HF}_{R/I}(2,\ldots,2)>0
\Longrightarrow
V_{X_0}(I)\ne\varnothing
\]

is false.

**6.1 ASSUME.**  
Take four qubits and five generic rank-one \(4\)-local clause vectors, all of multidegree
\((1,1,1,1)\).  
[D-quantum-k-sat]

**6.2 PROVE.**  
The physical sector has dimension \(2^4=16\), and five generic independent forms leave

\[
\operatorname{HF}_{R/I}(1,1,1,1)=16-5=11.
\]

[D-hilbert-function]

**6.3 PROVE.**  
The product-state variety \((\mathbb P^1)^4\) has dimension four.  
[D-variety]

**6.4 PROVE.**  
Five generic hypersurfaces of class \(h_1+h_2+h_3+h_4\) have empty common intersection: four meet in \(4!=24\) points counting multiplicity, and a fifth generic hypersurface avoids those points.  
[D-multihomogeneous-bezout; arXiv:2412.19623, Definition 52]

**6.5 COMPUTE.**  
For generic clause vectors, the diagonal Hilbert profile is

\[
\begin{aligned}
\operatorname{HF}(1,1,1,1)&=11,\\
\operatorname{HF}(2,2,2,2)&=11,\\
\operatorname{HF}(3,3,3,3)&=1,\\
\operatorname{HF}(4,4,4,4)&=0.
\end{aligned}
\]

The ambient dimensions at those levels are \(16,81,256,625\), respectively.

**6.6 CONCLUDE.**  
Although \(V_{X_0}(I)=\varnothing\),

\[
\operatorname{HF}_{R/I}(2,2,2,2)=11>0.
\]

Level two is therefore inconclusive for this family.

**6.7 CERTIFY.**  
The first diagonal certifying level for this generic four-qubit family is

\[
r=4,
\qquad
\operatorname{HF}_{R/I}(4,4,4,4)=0.
\]

**6.8 CONSEQUENCE.**  
Diagonal Hilbert-function vanishing gives a complete hierarchy in the existential sense of step 4.9:

\[
V_{X_0}(I)=\varnothing
\Longrightarrow
\operatorname{HF}_{R/I}(r,\ldots,r)=0
\quad\text{for some finite }r.
\]

The first certifying level need not be \(2\), and this memo gives no effective general upper bound for it.

### Bézout and BKK counts of product ground states

**7. PROVE.**  
Multiprojective intersection theory gives an exact generic count for square product-solution systems, but the QSAT statement is prior art rather than a new Arm D result.

**7.1 ASSUME.**  
Let

\[
m=n(q-1)=\dim(\mathbb P^{q-1})^n
\]

and select exactly \(m\) rank-one forms. Steps 7.1–7.7 apply only to such square subsystems. They do not apply directly to the three-form two-qubit example of §5 or the five-form four-qubit example of §6.

**7.2 DEFINE.**  
Let \(d_{ai}=1\) if form \(a\) acts nontrivially on site \(i\), and \(d_{ai}=0\) otherwise.

**7.3 PROVE.**  
Form \(a\) defines a divisor of class

\[
\sum_{i=1}^{n}d_{ai}h_i
\]

in the Chow ring

\[
\mathbb Z[h_1,\ldots,h_n]/(h_1^q,\ldots,h_n^q).
\]

[arXiv:2412.19623, Definition 52]

**7.4 PROVE.**  
When the common product-solution scheme is zero-dimensional, its generic length is the existing D-multihomogeneous-bezout coefficient

\[
B(D)
=
[h_1^{q-1}\cdots h_n^{q-1}]
\prod_{a=1}^{m}
\left(\sum_i d_{ai}h_i\right).
\]

[arXiv:2412.19623, Definition 52; D-multihomogeneous-bezout]

**7.5 SPECIALIZE.**  
For qubits, \(m=n\), and the incidence matrix is square, so

\[
B(D)=\operatorname{per}(D).
\]

The permanent formulation is in arXiv:2005.14485 and D-multihomogeneous-bezout/C-295. It is not attributed to arXiv:2412.19623.

**7.6 BOUND.**  
If every form has locality at most \(k\), then

\[
B(D)\le k^n,
\]

because each permanent term chooses one of at most \(k\) incident sites per row.

**7.7 GENERICITY.**  
For a square subsystem of forms generic within the family of tuples having the fixed supports and the orthonormality constraints imposed by the clause decomposition, positive \(B(D)\) gives exactly \(B(D)\) solutions with multiplicity. For special coefficients it remains the intersection number when the intersection is proper. A rank-\(r_a>1\) projector does not produce a tuple generic in the full unconstrained coefficient space because its split clause vectors are mutually orthonormal.

**7.8 CAUTION.**  
This counts product ground-state rays only. It says nothing about

\[
g_Q=\operatorname{HF}_{R/I_Q}(\mathbf1),
\]

which may be much larger.

**7.9 CAUTION.**  
The coefficient is a multihomogeneous Bézout number, not the general BKK mixed volume. Sparse Newton polytopes can give a sharper BKK number.

**7.10 NOVELTY VERDICT.**  
The proposed QSAT Bézout definition and count are prior art. Definition 52 of
arXiv:2412.19623 defines the coefficient, Observation 55 states that the number of weighted SDRs in a PRODSAT instance equals the Bézout number, and the accompanying remark says that computing \(d_{\mathrm{Béz}}\) counts perfect matchings. The permanent formulation itself is credited to arXiv:2005.14485 and the campaign’s D-multihomogeneous-bezout/C-295. Laumann et al. supplied the earlier generic product-satisfiability geometry
(DOI:10.1103/PhysRevA.81.062345).

**7.11 SURVIVING CANDIDATE.**  
The product-span formula in step 2 and the finite-degree entangled-only certificate in steps 4–6 are mathematically supported by the recomputations in
`verdicts/quantum-native-r1.md`. Their novelty is unestablished. They are not presented as new until a broader literature audit and an L4 checker pass are complete.

## QSAT dictionary

| Algebraic object | Physical meaning | Classical complexity | Quantum complexity | Reference |
|---|---|---|---|---|
| \(R_{\mathbf1}\) | Full \(n\)-qudit Hilbert space | Dimension \(q^n\); basis indexing is polynomial-space | Native \(n\)-qudit register | D-multidegree-sector, C-030 |
| Generating forms \(f_{a\mu}\) | Forbidden rank-one clause vectors, with unconjugated coefficients | Constructed in polynomial time from projectors for fixed \(q,k\) | Direct local-projector description | C-032; D-QN-QSAT-IDEAL |
| \((I_Q)_{\mathbf1}\) | Sum of local forbidden ranges | Explicit rank computation has exponential ambient dimension in general | Its orthogonal complement is the ground space | C-008, D-ground-space |
| \((I_Q)_{\mathbf1}^{\perp}\) | QSAT ground space | Implicitly described by clauses; an explicit basis can be exponentially large | A witness may inhabit it, but preparation is not supplied | D-inverse-system, D-quantum-k-sat |
| Promise problem: \(\operatorname{HF}_{R/I_Q}(\mathbf1)>0\) versus \(\lambda_{\min}(H_Q)\ge1/\operatorname{poly}(n)\) | Promised frustration freeness | In P for qubit \(2\)-QSAT | \(\mathrm{QMA}_1\)-complete for qubit \(3\)-QSAT and bilinear \((2,5)\)-QSAT | C-034–C-037; arXiv:quant-ph/0602108; arXiv:1302.0290; arXiv:2401.02368 |
| Exact \(\operatorname{HF}_{R/I_Q}(\mathbf1)>0\), no promise | Exact frustration freeness | In P for qubit \(2\)-QSAT | Not thereby in \(\mathrm{QMA}_1\) | C-038; arXiv:quant-ph/0602108 |
| Exact \(\operatorname{HF}_{R/I_Q}(\mathbf1)\) | Ground-state degeneracy | Computing it exactly is \(\#\mathrm P\)-hard already for qubit \(2\)-QSAT, by Ji–Wei–Zeng’s reduction to and from the classical analogue composed with \(\#\mathrm{2\text{-}SAT}\) hardness | General gapped local degeneracy is \(\#\mathrm{BQP}\)-complete, not ordinary BQP | D-hardness-anchors; arXiv:1010.2480; DOI:10.1016/0304-3975(79)90044-6; arXiv:1010.3060 |
| \(\operatorname{HF}(\mathbf r)\), \(\mathbf r\ne\mathbf1\) | Degeneracy of a local bosonic occupation extension | Rank of a matrix of dimension \(\prod_i\binom{r_i+q-1}{q-1}\) | No known generic advantage | D-multidegree-sector |
| Minimal multigraded generators | Constraints not implied at lower multidegrees after complementary-site multiplication | Minimizing the ideal presentation can require Gröbner computations and exponential output | No known quantum algorithm | D-homogeneous-ideal |
| First syzygies | Linear dependencies among forbidden vectors tensored with complementary states | Kernel of the Macaulay map; exponential sector size | A relation-space nullity, not a ground-state observable by itself | D-syzygy-module |
| Higher syzygies | Relations among those redundancies | Free-resolution computation; output can be exponential | No known QSAT primitive | D-syzygy-module |
| \(V_{X_0}(I_Q)\) | Fully product ground-state rays | Polynomial-system solving; distinct from QSAT decision | Product-state variational search only | C-033; DOI:10.1103/PhysRevA.81.062345 |
| \(\dim V_{X_0}(I_Q)\) | Dimension of the product-ground-state locus | Accessible by elimination in small instances; not uniformly polynomial | No known estimator from a QSAT ground state | D-variety |
| Multiprojective degree | Number of product solutions after generic complementary slicing | Bézout/BKK or numerical algebraic geometry | Optical permanent sampling does not directly return it | D-multihomogeneous-bezout; arXiv:2412.19623; arXiv:2005.14485 |
| \(J_Q=\sqrt{I_Q:B^\infty}\) | Reduced closed product-solution subscheme, of any dimension | Radical and saturation may dominate the computation | No known generic quantum construction | D-QN-MULTIPROJECTIVE-SATURATION |
| Primary decomposition of \(J_Q\) | Branches/components of product solutions | Potentially exponential output | No known quantum output model | D-variety |
| Embedded or nonreduced components of \(I_Q\) | Algebraic multiplicity and finite-degree inverse-system directions | Detected by saturation, radicals, and local dual spaces | May contribute to D-entangled-defect, but not an orthogonal phase decomposition | D-entangled-defect |
| \((J_Q)_{\mathbf1}^{\perp}\) | Span of all product ground states | Requires the product-solution vanishing ideal | Could be probed if a product-state ensemble were available | C-028, C-029 |
| \(e_Q\) | Ground directions orthogonal to every product ground state | Difference of two degree-\(\mathbf1\) Hilbert values | No known efficient generic estimator | D-entangled-defect |
| \(\operatorname{HF}(\mathbf r)=0\), \(\mathbf r\ge\mathbf1\) | Multihomogeneous Nullstellensatz certificate that no product ground state exists | One Macaulay-rank computation at that level; first-level bound open here | No generic speedup; level two is not complete | Steps 4–6 |
| \(\lambda_{\min}(H_Q)\) when \(g_Q=0\) | Frustration energy | Local-Hamiltonian promise problem | \(\mathrm{QMA}_1\)-hard at \(k=3\) | arXiv:1302.0290 |
| Macaulay singular values | Constraint conditioning and excitation energies | Sparse eigensolvers are the baseline | Phase estimation still pays the inverse normalized gap | D-macaulay-gap |
| Bézout coefficient \(B(D)\) | Generic number of product ground rays for a square subsystem | Permanent for square qubit incidence matrices; nonnegative permanent has an FPRAS | Boson sampling returns a related probability, not the count | D-multihomogeneous-bezout; C-295; arXiv:2005.14485; DOI:10.1145/1008731.1008738 |
| Hard-core generators | Energetic isolation of the \(\mathbf1\) occupation pattern inside total degree \(N=n\) | Adds \(3n\) quadratic generators for qubits | Transfers QSAT hardness to the symmetric bosonic sector | D-hard-core-generators, C-129, C-130 |
| A positive parent for \(I_{\mathbf1}\) | Would make the forbidden span, rather than its complement, the ground space | Obstructed by the AND/OR mismatch | QSVT spectral projection is nonlocal | D-parent-hamiltonian, C-040–C-047 |

### Complexity conclusions

- Only the promise decision boundary for qubit \(2\)-QSAT is classically polynomial.
- Computing \(\operatorname{HF}_{R/I_Q}(\mathbf1)\) exactly is \(\#\mathrm P\)-hard already for qubit \(2\)-QSAT, by Ji–Wei–Zeng’s reduction to and from the classical analogue
  (arXiv:1010.2480, DOI:10.1103/PhysRevA.84.042338) composed with
  \(\#\mathrm{2\text{-}SAT}\) hardness
  (Valiant 1979, DOI:10.1016/0304-3975(79)90044-6); see D-hardness-anchors.
- Exact ground-space degeneracy of qubit \(2\)-QSAT is equivalent in both directions to its classical counting analogue; the decision problem is in P, so decision and counting separate.
- No \(\#\mathrm P\)-completeness claim is made without a containment argument.
- Qubit \(3\)-QSAT promised frustration-freeness is \(\mathrm{QMA}_1\)-complete
  (arXiv:1302.0290).
- Bilinear \((2,5)\)-QSAT is also \(\mathrm{QMA}_1\)-complete
  (arXiv:2401.02368).
- Minimal generators, syzygies, radicals, and primary decompositions are not thereby
  \(\mathrm{QMA}_1\)-complete.
- They are function or output problems, often with exponentially large outputs.
- No generic quantum procedure in the seed computes any of them.
- The Hilbert dictionary transfers hardness; it does not reduce it.
- C-038, with C-034–C-037, remains binding; the contrary draft is REFUTED as C-217.
- C-041/C-043 remain binding, with C-044 the only few-mode survivor; the contrary draft is REFUTED as C-219.

## Entanglement varieties

### Which loci are actually varieties?

- The Segre variety is the locus of fully product pure states.
- Its ideal is generated by \(2\times2\) minors of matrix flattenings.
- The \(r\)-th secant variety is the Zariski closure of tensors of rank at most \(r\).
- Membership means border rank at most \(r\), not necessarily tensor rank at most \(r\).
- Flattening \((r+1)\)-minors are necessary secant equations.
- For more than two tensor factors they are not sufficient in general.
- Strassen-type and representation-theoretic equations are required in some small cases
  (arXiv:math/0601452; arXiv:1111.4567).
- Tensor rank, best rank-\(r\) approximation, multilinear rank, and border rank are different outputs.
- Hillar–Lim prove NP-hardness for tensor rank and best rank-one approximation of a
  \(3\)-tensor (arXiv:0911.1393, DOI:10.1145/2512329).
- No border-rank-optimization hardness claim is attributed to Hillar–Lim.
- D-tensor-secant-problem correctly keeps these outputs separate.

For tensor networks, “fixed bond dimension is an algebraic variety” needs qualification.

- For an open chain, bond dimension at most \(\chi\) is characterized by Schmidt-rank bounds across all contiguous cuts.
- Those bounds are flattening-minor equations, so the bounded-rank locus is Zariski closed.
- Tree tensor-network varieties have prime ideals generated by edge-flattening minors
  (arXiv:2608.19071).
- arXiv:1501.01120 compares tree tensor formats through the Hackbusch conjecture; it is not cited as the source of the edge-flattening description.
- Exact bond dimension \(\chi\), as opposed to at most \(\chi\), is generally a locally closed stratum.
- For cyclic and more general tensor networks, the parametrized image need not be closed.
- The correct algebraic object is often its Zariski closure
  (arXiv:1105.4449).
- Uniform translation-invariant MPS varieties have additional trace identities and boundary phenomena
  (arXiv:1210.2812; arXiv:1904.07563).
- Dimension formulas and bounds are studied in
  arXiv:2101.03148 and DOI:10.1142/S0219199722500596.

The citation suggested in the original brief needs correction.

- Bernardi–Carusotto is arXiv:1109.0221, not arXiv:1105.2390.
- Its full title is “Algebraic Geometry tools for the study of entanglement: an application to spin squeezed states.”
- Its journal DOI is 10.1088/1751-8113/45/10/105304.
- It is relevant to Veronese/secant entanglement, not the foundational MPS-variety claim.
- Landsberg–Qi–Ye arXiv:1105.4449 is the correct tensor-network geometry citation.

### What the seed can estimate from copies

Let \(\mathcal H=(\mathbb C^q)^{\otimes n}\), with \(D=q^n\), and let
\(|\psi\rangle\in\mathcal H\) be physically supplied.

Suppose \(f_1,\ldots,f_d\) are homogeneous degree-\(m\) equations for a candidate variety
\(X\subseteq\mathbb P(\mathcal H)\). Under C3, represent each equation by
\(|F_j\rangle\in\operatorname{Sym}^m(\mathcal H)\) such that

\[
f_j(\overline\psi)
=
\langle F_j|\psi^{\otimes m}\rangle.
\]

C-019 gives

\[
\|F_j\|=\|f_j\|_{\mathrm{BW}}.
\]

For nonnegative weights \(w_j\), define

\[
\Lambda=\sum_{j=1}^{d}w_j\|F_j\|^2
\]

and the normalized residual observable on
\(\operatorname{Sym}^m(\mathcal H)\),

\[
A_F
=
\frac{1}{\Lambda}
\sum_{j=1}^{d}w_j|F_j\rangle\langle F_j|.
\]

Since the operator norm of the positive numerator is at most its trace,

\[
0\le A_F\le\mathbb1.
\]

Then

\[
E_F(\psi)
=
\langle\psi|^{\otimes m}A_F|\psi\rangle^{\otimes m}
=
\frac1\Lambda
\sum_jw_j|f_j(\overline\psi)|^2.
\]

This is the normalized form of C-027.

Operationally:

- If the listed equations define \(X\) set-theoretically, then
  \(E_F(\psi)=0\) exactly when \([\overline\psi]\in X\).
- If only flattening minors are measured, \(E_F=0\) means membership in the flattening relaxation.
- For a general secant variety, that relaxation can strictly contain the desired secant.
- A measured \(E_F>\varepsilon\) is a one-sided nonmembership witness.
- A measured \(E_F\le\varepsilon\) is not a distance certificate without a quantitative error bound.
- Replacing one generator \(f_j\) by \(\lambda f_j\) changes its squared residual by
  \(|\lambda|^2\) without changing \(X\).
- Near singular points, residuals can vanish to order greater than geometric distance.
- There is therefore no universal identity between squared residual and squared projective distance.
- A Łojasiewicz exponent, reach bound, or condition number would be required to convert residual energy into distance.
- This is the entanglement analogue of the D-macaulay-gap conditioning problem.

In D-QN-PHYSICAL-DATA-ACCESS case 1, uncontrolled copies, a direct measurement of \(A_F\) estimates its expectation to additive error \(\varepsilon\) and failure probability \(\delta\) using

\[
O\!\left(\varepsilon^{-2}\log(1/\delta)\right)
\]

measurements. Each measurement acts on \(m\) copies, so the total copy cost is

\[
m\cdot O\!\left(\varepsilon^{-2}\log(1/\delta)\right).
\]

That bound is conditional on an implementation of \(A_F\). It omits potentially dominant costs:

- preparing \(m\) copies for every shot;
- implementing the projector, randomized equation selector, or block encoding of \(A_F\);
- dependence on the number and norms of equations through the implementation;
- state loss and failed collective measurements.

Observation B does not make the cost independent of \(d\) automatically.

- A structured LCU, symmetry decomposition, or randomized equation sampler is required.
- If the equations are enumerated one by one, the implementation still costs \(d\).
- If \(d\) is exponential and no succinct selector exists, the proposed batch evaluation is not efficient.

With a controlled preparation unitary for \(|\psi\rangle\), its inverse, and coherent access to \(A_F\), amplitude estimation can improve the sampling dependence from
\(\varepsilon^{-2}\) to \(O(\varepsilon^{-1})\) coherent queries. Uncontrolled copies do not supply those reflections.

D-QN-PHYSICAL-DATA-ACCESS extends D-input-model by distinguishing:

1. uncontrolled copies of a physical state;
2. a preparation circuit;
3. controlled preparation and inverse access;
4. classical measurement samples;
5. a classical amplitude description.

These inputs are not interchangeable.

### Classical baseline

For a dense classical amplitude array:

- Reading the state costs \(\Omega(D)=\Omega(q^n)\).
- A specified flattening can be formed in \(O(D)\) storage.
- Its numerical rank is obtained by an SVD at a cost determined by its two matrix dimensions.
- All contiguous MPS cuts can be checked by sequential Schmidt decompositions.
- Known tensor-network parameters make membership tautological.
- Tensor rank and best rank-one approximation of \(3\)-tensors are NP-hard
  (arXiv:0911.1393, DOI:10.1145/2512329).
- Border-rank optimization is a separate problem; no hardness result for it is taken from Hillar–Lim.

For a circuit description:

- The input length can be polynomial in \(n\).
- Classically expanding its state vector takes \(D\) amplitudes in the worst case.
- That observation alone is not a lower bound for a particular variety-membership property.
- A property-specific classical algorithm may avoid state-vector simulation.
- No such lower bound is supplied by the seed.

For copies of an unknown pure state:

- A classical amplitude array does not exist.
- The same-input classical comparator is a protocol using single-copy, possibly adaptive measurements followed by classical post-processing.
- Full pure-state tomography to infidelity \(\varepsilon\) requires
  \(\Omega(q^n/\varepsilon)\) copies as the \(r=1\), \(d=q^n\) case of Yuen’s
  \(\Omega(rd/\varepsilon)\) lower bound
  (arXiv:2206.11185).
- Tomography returns a much stronger output than a membership bit and is not the correct same-problem comparator for property testing.

### The actual MPS-testing result

Soleimanifar–Wright study the precise copy-access promise problem of distinguishing a pure \(n\)-qudit state in \(\mathrm{MPS}_r\) from one promised a constant distance from every such state. Their algorithm uses

\[
O(nr^2)
\]

copies, independent of the local dimension, and they prove an
\(\Omega(\sqrt n)\) copy lower bound for \(r\ge2\)
([arXiv:2201.01824](https://arxiv.org/abs/2201.01824)).

Consequences:

- This is exponentially fewer copies than generic tomography when \(D=q^n\).
- It tests an open-chain flattening-rank variety without reconstructing the state.
- It is stronger and cleaner than separately measuring every flattening minor.
- It is published prior art, so it fails the novelty requirement in CLAUDE.md §1 / PRD §1.
- PRD §2 itself has no novelty criterion.
- Tomography is a different-output comparator and does not establish criterion 2.
- The correct same-input classical comparator is adaptive single-copy measurement plus classical post-processing.
- No lower bound against that comparator for MPS membership is supplied here.
- Consequently, the published tester does not currently establish a PRD §2 speedup over the best classical protocol for the same copy-access problem.
- Its copy-access input is not disqualified: PRD §2 criterion 3 explicitly makes the input model part of the problem statement.

Known work proves exponential separations between quantum-memory/collective-measurement protocols and protocols without quantum memory for other learning tasks. Chen–Cotler–Huang–Li prove such separations for shadow tomography, purity testing, dynamics, and symmetry learning
([arXiv:2111.05881](https://arxiv.org/abs/2111.05881)). Huang et al. prove and experimentally demonstrate exponential advantages for selected quantum-learning tasks
([DOI:10.1126/science.abn7293](https://doi.org/10.1126/science.abn7293)).

Those results show that copy-access separations are admissible and can be exponential. They do not establish such a separation for membership in, or distance to, an entanglement, secant, MPS, or other tensor-network variety. Transfer to a variety-membership problem remains open and is deferred to Question 6.

### Secant and entanglement-class decisions

For the Segre variety:

- The two-copy product test directly probes separability of a pure state.
- It estimates a property related to the sum of subsystem purities.
- It avoids tomography.
- It does not return the closest product state or exact geometric entanglement.

For general secant varieties:

- Known equations give one-sided border-rank witnesses.
- Flattening spectra give lower bounds on border rank.
- They do not decide membership whenever flattenings are incomplete.
- Exact rank is unstable at arbitrarily small singular values.
- Any finite-copy decision therefore needs an additive-distance or singular-value promise.
- A promise-free exact entanglement-class decision is not statistically identifiable from finitely many copies.
- Orbit-closure classes share boundaries, so arbitrarily close states can lie in different exact classes.

The seed’s primitive can therefore estimate:

- a normalized sum of squared known invariants;
- a specified flattening-minor residual;
- a one-sided nonmembership witness;
- a promised MPS/tree-network property through existing tests;
- selected moments or purities.

It cannot presently estimate:

- the exact distance to a general secant variety;
- CP rank;
- a closest tensor-network state;
- an exact SLOCC class without a separation promise;
- the defining ideal when that ideal is not already supplied.

### Phylogenetic and tree-tensor-network varieties

For a \(k\)-taxon, four-state model, the joint-distribution tensor has \(4^k\) entries.

The general Markov model on a tree is an algebraic variety with phylogenetic invariants
(arXiv:math/0410604).

Its tensor-network relation is mathematically exact at the parameterization level.

Tree tensor-network varieties have edge-flattening-minor descriptions
(arXiv:2608.19071).

The input semantics remain decisive.

**Classical empirical distribution.**

- Sequencing produces classical site-pattern counts.
- The data are samples from a probability distribution \(p_x\).
- Classical quartet and flattening methods operate directly on those counts.
- Preparing
  \[
  |p\rangle/\|p\|_2
  \]
  requires coherent access to all \(4^k\) probabilities.
- Classical samples do not provide that coherent access.
- Amplitude encoding recreates the original input bottleneck.

**Coherent sample \(\sum_x\sqrt{p_x}|x\rangle\).**

- This state can sometimes be prepared from a generative quantum process.
- Its amplitudes are \(\sqrt{p_x}\), not \(p_x\).
- Phylogenetic minors are polynomials in \(p_x\).
- Substituting \(\sqrt{p_x}\) changes the variety.
- Ordinary tensor-network amplitude tests therefore answer a different problem.

**Born probabilities of a physical state.**

- If \(p_x=|\psi_x|^2\), a degree-\(m\) polynomial in \(p\) is a diagonal statistic of
  \(m\) independently measured copies.
- The same statistic can be estimated from classical measurement strings.
- Coherence is not automatically useful.
- A quantum advantage would require a coherent oracle and an amplitude-estimation comparison, not merely physical preparation.

**Amplitudes deliberately equal to phylogenetic coordinates.**

- A device could be engineered so that \(\psi_x\propto p_x\).
- Observation B would then test invariant violation without tomography.
- That device would model a quantum amplitude tensor, not ordinary observed evolutionary frequencies.
- It is a useful analogue demonstration but not a faster phylogenetic inference algorithm.

Therefore shortlist entry 5 remains a classical shadow of shortlist entry 1.

Physical production removes the amplitude-loading cost only when the physically produced amplitudes are themselves the scientific object. If only the probabilities are the scientific object, classical samples retain the relevant information and Arm D gains no asymptotic advantage.

## Hardware

### Dual-rail realization of the \(\mathbf1\) sector

For qubits, use two optical modes per site:

\[
(a_{i,0},a_{i,1}).
\]

The computational subspace contains exactly one photon in each pair.

For \(n\) qubits this uses:

- \(2n\) computational modes;
- \(n\) photons;
- postselection on occupation pattern \((1,\ldots,1)\).

This realizes D-multidegree-sector directly. It does not energetically enforce the sector during a general interferometer.

Two distinct strategies must not be conflated.

1. Inject one photon per dual-rail block and discard outputs that leave the sector.
2. Work in total degree \(N=n\) and add D-hard-core-generators to penalize all other occupation patterns.

Strategy 1 is postselection. Strategy 2 is the C-129/C-130 Hamiltonian reduction.

Passive block-diagonal optics preserves one photon per block but supplies only one-qubit gates. A generic QSAT clause needs entangling measurements or measurement-induced nonlinearities.

KLM supplies universal postselected linear-optical gates
(DOI:10.1038/35051009). Its existence does not supply a favorable success probability for a long QSAT projector sequence.

### Smallest nontrivial instance

The smallest entangled example has:

- \(n=2\) qubits;
- \(q=2\);
- four computational modes;
- two photons;
- one rank-three \(2\)-local projector;
- a one-dimensional singlet ground space.

Use the ideal

\[
I=
(x_0y_0,\ x_1y_1,\ x_0y_1+x_1y_0).
\]

The normalized physical clause vector uses
\((x_0y_1+x_1y_0)/\sqrt2\), which generates the same ideal. It has

\[
\operatorname{HF}_{R/I}(1,1)=1,
\qquad
\operatorname{HF}_{R/I}(2,2)=0,
\qquad
V_{\mathbb P^1\times\mathbb P^1}(I)=\varnothing.
\]

A two-beamsplitter postselected preparation is explicit.

Start with one photon in mode \(a_0\) and one in mode \(b_1\). Apply balanced beamsplitters

\[
a_0^\dagger\mapsto
\frac{a_0^\dagger+b_0^\dagger}{\sqrt2},
\qquad
b_1^\dagger\mapsto
\frac{a_1^\dagger-b_1^\dagger}{\sqrt2}.
\]

The output is

\[
\frac12
(a_0^\dagger+b_0^\dagger)
(a_1^\dagger-b_1^\dagger)|0\rangle.
\]

Postselect exactly one photon in the \(A\) rails and one in the \(B\) rails. The surviving state is

\[
\frac{-a_0^\dagger b_1^\dagger+b_0^\dagger a_1^\dagger}{\sqrt2}|0\rangle
=
-|\psi^-\rangle
\]

up to the chosen rail ordering and a global phase. Its preparation success probability is exactly \(1/2\).

No ancillary photon is needed for this state-preparation demonstration.

A standard passive linear-optical Bell analyzer cannot discriminate all four Bell states with success above \(50\%\) using only vacuum ancillas
(arXiv:quant-ph/0007058, DOI:10.1007/s003400000484). This citation does not by itself supply a unit-efficiency singlet-projector implementation.

### What a degeneracy measurement would demonstrate

Preparing one singlet demonstrates only that one ground state exists. It does not measure the ground-space dimension.  
[C-297]

For the two-qubit example, conditioned on the occupation pattern \((1,1)\) in each rail pair and assuming an ideal, unit-efficiency implementation of both the maximally mixed probe on the four-dimensional dual-rail sector and the projector
\(|\psi^-\rangle\langle\psi^-|\),

\[
p_0
=
\operatorname{Tr}(P_0\mathbb1/4)
=
\frac{\dim\ker H}{4}
=
\frac14.
\]

Estimating \(p_0\) to additive error \(1/8\), Hoeffding’s bound gives

\[
N_{\rm shots}
\ge
\frac{\log(2/0.05)}{2(1/8)^2}
=
118.04,
\]

so \(119\) ideal, post-selected, unit-efficiency shots suffice for \(95\%\) confidence.

If \(\eta_{\mathrm{sector}}\) is the probability that a full physical trial reaches and is accepted in the dual-rail sector, the unconditioned singlet acceptance is

\[
p_{\mathrm{unconditioned}}
=
\eta_{\mathrm{sector}}/4.
\]

No preparation-and-readout protocol or loss model fixing
\(\eta_{\mathrm{sector}}\) is supplied here. Consequently, \(119\) is not a launched-shot count.

Under its stated ideal conditioning, this test would demonstrate:

- the physical rank of the ground projector is one;
- \(\operatorname{HF}_{R/I}(1,1)=1\);
- the sole ground ray is not a point of the Segre variety;
- the ground space is the inverse-system piece rather than the product-solution variety.

It would not demonstrate computational speedup.

For \(n\) qubits, adjacent degeneracies change the maximally mixed ground probability by \(2^{-n}\). At positive degeneracy \(g\), variance-sensitive independent sampling requires

\[
\Theta(g\,2^n)
\]

shots for adjacent-integer resolution; over all \(g\), the worst case is

\[
\Theta(4^n).
\]

Ideal coherent amplitude estimation requires

\[
\Theta(\sqrt g\,2^{n/2})
\]

projector queries at degeneracy \(g\), with worst case

\[
\Theta(2^n).
\]

Exact degeneracy readout therefore remains exponentially expensive in the low-degeneracy and worst-case regimes.  
[D-analogue-degeneracy-readout, C-297, C-298]

### Relation to boson sampling

A passive interferometer \(U\) has collision-free Fock transition amplitudes

\[
\langle S|U_{\rm LO}|T\rangle
=
\operatorname{per}(U_{S,T})
\]

up to occupation factorials
(arXiv:1011.3245).

This fact does not make QSAT coherent overlaps hard permanents.

For multigraded product states,

\[
\left\langle
\bigotimes_i x_i
\middle|
\bigotimes_i y_i
\right\rangle
=
\prod_i\langle x_i|y_i\rangle.
\]

This factorized product may be written as the permanent of a diagonal matrix, but it is computationally trivial.

For total-degree bosonic coherent states,

\[
\langle p^{\otimes N}|q^{\otimes N}\rangle
=
\langle p|q\rangle^N.
\]

This is likewise a closed-form overlap.

Nontrivial permanents arise only after a global interferometer mixes the modes. Such an interferometer generally leaks out of the
\((1,\ldots,1)\) sector. Postselecting back into that sector produces boson-sampling amplitudes, but the success probability can be exponentially small.

C-296 already records the surviving statement that the device supplies permanent-weighted samples and that such samples are useful only when the requested output is the distribution or the relevant event probability is not too small.

The additional QSAT-specific obstruction is:

- the device samples from probabilities proportional to
  \(|\operatorname{per}|^2\);
- it does not output a signed or complex permanent;
- a specified rare probability needs inverse-probability shots;
- QSAT incidence matrices used in the Bézout count are nonnegative;
- nonnegative permanents have the Jerrum–Sinclair–Vigoda FPRAS
  (DOI:10.1145/1008731.1008738).

Therefore no optical sampling advantage is available for that Bézout count. This is the genuinely additional point relative to C-296.  
[D-optical-counting-access, D-QN-DUAL-RAIL-SECTOR, C-295, C-296]

### Spinor-BEC conic

For

\[
f=z_0z_1-z_2^2,
\]

the seed Hamiltonian is

\[
H
=
\hat n_0\hat n_1
+
\hat n_2(\hat n_2-1)
-
\left(
a_0^\dagger a_1^\dagger a_2^2+\mathrm{h.c.}
\right).
\]

This matches the spin-mixing Hamiltonian of a spin-1 condensate
(arXiv:cond-mat/9807258, DOI:10.1103/PhysRevLett.81.5257).

The algebraic ground-space dimension is

\[
\operatorname{HF}_{R/(f)}(N)=2N+1.
\]

Spin-mixing dynamics have been observed experimentally
(DOI:10.1103/PhysRevLett.92.140403).

The evidence supports only:

- the Hamiltonian-form identification;
- physical realization of the spin-mixing interaction;
- observation of spin-changing dynamics.

It does not support a direct experimental measurement of the full \(2N+1\) ground-space dimension. C-024’s final clause must therefore be weakened in lockstep with PRD §4 Arm A, HANDOFF, and its claim shard. C-297 independently forbids inferring degeneracy from spectroscopy or observation of a single zero-energy state.

A two-generator extension in four or five modes would be a useful analogue test only if it specifies:

- the complete Hamiltonian coefficients;
- the fixed-number sector;
- the normalized spectral gap;
- how the ground projector is measured;
- how degeneracy is separated from thermal occupation;
- the shot count and loss model.

## Against the north star

### Verdict

Arm D does not currently contain an established north-star speedup. The broad negative in PRD §4 is also not proved and is not discharged by this memo.

The scoped conclusion is narrower:

- the QSAT–inverse-system dictionary is an exact polynomial-time, spectrum-preserving relabelling;
- composing an existing decision, preparation, gap-estimation, or degeneracy algorithm solely with that relabelling gives no asymptotic advantage from the relabelling itself;
- the dictionary can still support structural theorems and small experiments;
- no generic Arm D speedup is currently known;
- copy-access variety testing, the bosonic C-129/C-130 sector, and specially structured QSAT subfamilies are not covered by the relabelling argument.

The strongest copy-access example is the published \(O(nr^2)\)-copy MPS tester
(arXiv:2201.01824). It uses exponentially fewer copies than full tomography, whose pure-state lower bound is the \(r=1\) case of
\(\Omega(rd/\varepsilon)\), namely \(\Omega(q^n/\varepsilon)\)
(arXiv:2206.11185). This does not yet constitute a north-star hit:

- it is prior art and therefore fails the novelty requirement in CLAUDE.md §1 / PRD §1;
- PRD §2 has no novelty criterion;
- tomography returns a different, stronger output;
- the correct same-input comparator is adaptive single-copy measurement plus classical post-processing;
- no best-in-class bound for that comparator on MPS membership is established here;
- no dequantization audit or required heuristic-hardware mapping with resource estimates is supplied.

The quantum-memory separations of arXiv:2111.05881 and
DOI:10.1126/science.abn7293 show that exponential separations over the correct copy-access comparator are possible for other learning problems. No such separation is presently established for membership in or distance to an entanglement, secant, MPS, or tensor-network variety.

### Criteria audit

| PRD §2 criterion | Relabelling-composition family | Copy-access variety testing |
|---|---|---|
| 1. Precise problem | QSAT promise decision, degeneracy, preparation, and readout tasks can be stated precisely | The Soleimanifar–Wright MPS promise test is precise |
| 2. Best classical baseline | Qubit \(2\)-QSAT has a polynomial algorithm; other tasks require problem-specific baselines | Tomography is the wrong output; the adaptive single-copy baseline has not been adjudicated |
| 3. Quantum algorithm beating that baseline | Fail: the relabelling preserves the operator and composes with, rather than improves, the underlying algorithm | Input model is legitimately part of the problem; the \(O(nr^2)\) quantum copy bound is known, but no separation from the same-problem classical baseline is established |
| 4. Dequantization and hidden costs | Fail: preparation, normalized gap, implementation, postselection, and readout remain | Incomplete: collective measurements, copy preparation, noise, and the single-copy comparator require audit |
| 5. Heuristic hardware attack | Dual rail and spinor-BEC mappings are concrete, though scalable success bounds are absent | No qualifying linear-optical, MBQC, boson-sampling, or condensed-matter implementation with an end-to-end estimate is supplied here |

No current candidate satisfies all five criteria.

Novelty is required by CLAUDE.md §1 / PRD §1, not by PRD §2. If the campaign wants novelty duplicated as a formal sixth success criterion, that is a governance change for Question 13, not an existing criterion.

### REFUTED-style negative row and proof sketch

This subsection no longer supports a broad REFUTED Arm D row. It isolates the tautology underlying the narrower CONJECTURE placed on HOLD.

**Claim under test.**  
“Composing an algorithm with the QSAT–inverse-system relabelling dictionary makes that algorithm asymptotically faster.”

**8.1 ASSUME.**  
An input QSAT instance is supplied as local projectors \(\{\Pi_a\}\), and an algorithm
\(\mathcal A\) addresses a specified task for that instance.  
[D-quantum-k-sat]

**8.2 DEFINE.**  
The relabelling map replaces every rank-one clause vector by the same unconjugated coefficient tensor viewed as a multilinear polynomial.  
[C-030–C-032, D-QN-QSAT-IDEAL]

**8.3 PROVE.**  
On \(R_{\mathbf1}\), the resulting Hamiltonian is exactly \(H_Q\), with identical spectrum, normalized gap, and ground projector.  
[D-multidegree-sector, C-008, C-009]

**8.4 PROVE.**  
The map is computable in polynomial time and invertible by reading the polynomial coefficients as clause amplitudes.  
[D-quantum-k-sat]

**8.5 TAUTOLOGY.**  
Composing \(\mathcal A\) with this polynomial-time relabelling changes its resource bound only by the relabelling overhead.

**8.6 TAUTOLOGY.**  
Because the relabelling preserves the operator, it cannot by itself remove search, preparation, gap, or readout cost.

**8.7 CONSEQUENCE.**  
For qubit \(3\)-QSAT the relabelled promise decision problem remains
\(\mathrm{QMA}_1\)-complete
(arXiv:1302.0290).

**8.8 SCOPED VERDICT.**  
The encoding-as-algorithm reading is rejected: the dictionary alone supplies no speedup. This is a tautology about composition with a spectrum-preserving relabelling, not an impossibility theorem for Arm D.

**8.9 SURVIVING STATEMENT.**  
The dictionary may transfer algebraic invariants, structural theorems, and experimental witnesses between QSAT and multiprojective geometry.

**8.10 SCOPE BOUNDARY.**  
The argument covers exactly algorithm families whose only Arm D ingredient is composition with the relabelling dictionary, including relabelled QSAT decision, ground-state preparation, gap-estimation, and degeneracy/readout procedures.

It does not cover:

- the total-degree bosonic C-129/C-130 construction;
- copy-access membership or distance testing for entanglement, secant, MPS, or tensor-network varieties;
- structured QSAT subfamilies whose algorithms exploit structure beyond the dictionary;
- an algorithm with a new collective-measurement separation from adaptive single-copy measurement plus classical post-processing;
- any new preparation, gap, or readout theorem not inherited from the original QSAT formulation.

The correct comparator for copy-access problems is adaptive single-copy measurement plus classical post-processing. Exponential separations against that comparator exist for other learning tasks
(arXiv:2111.05881; DOI:10.1126/science.abn7293), but no transfer to variety membership is proved here.

PRD Q13 should therefore be treated as follows:

- a multigraded mechanism/QSAT dictionary may be a publishable physics construction;
- it is not a speedup unless a separate algorithmic separation is proved;
- the broader statement that no Arm D speedup exists remains an open negative.

## Killers

### K-QN1 — Identity is not an algorithm

The QSAT Hamiltonian and the multigraded Macaulay Hamiltonian are the same operator on the same \(q^n\)-dimensional space. No asymptotic resource is reduced by renaming its forbidden range an ideal piece.

### K-QN2 — QMA hardness is not quantum efficiency

Qubit \(3\)-QSAT is \(\mathrm{QMA}_1\)-complete
(arXiv:1302.0290). A BQP ground-state preparation or decision algorithm is not implied.

### K-QN3 — Degeneracy is harder than satisfiability

Computing \(\operatorname{HF}_{R/I_Q}(\mathbf1)\) exactly is \(\#\mathrm P\)-hard already for qubit \(2\)-QSAT, by Ji–Wei–Zeng’s equivalence with the classical analogue composed with \(\#\mathrm{2\text{-}SAT}\) hardness
(arXiv:1010.2480; DOI:10.1016/0304-3975(79)90044-6; D-hardness-anchors). The decision problem remains polynomial. A degeneracy measurement is not a free readout.

### K-QN4 — Other multidegrees change the physical system

\(\operatorname{HF}(\mathbf r)\) for \(\mathbf r\ne\mathbf1\) describes locally symmetrized bosonic occupations, not copies of the original QSAT system.

### K-QN5 — Product geometry sees only a subset of the ground space

\(V_{X_0}(I_Q)\) lists fully product rays. It may be empty while
\(\operatorname{HF}(\mathbf1)\) is positive or large.

### K-QN6 — Hilbert functions erase the gap

The ideal and its Hilbert function are invariant under nonzero generator rescaling. The excitation spectrum is not.

### K-QN7 — Residual energy is not geometric distance

A sum of squared invariants depends on generator normalization and can vanish at high order near singularities. No distance estimate follows without a quantitative error bound.

### K-QN8 — Known equations can be incomplete

Flattening minors do not generally define higher secant varieties. A zero residual may certify only membership in a relaxation.

### K-QN9 — Tensor-network images may not be closed

For cyclic networks, limits of bounded-parameter tensor-network states need not remain in the parametrized image
(arXiv:1105.4449). The algorithmic target must specify the image, its closure, or distance to either.

### K-QN10 — Tomography is the wrong comparator

A membership tester returns one bit, whereas tomography returns a full state description. For copy-access membership, the correct comparator is an adaptive single-copy measurement protocol with classical post-processing. That comparator is not yet audited for MPS or tensor-variety membership.

### K-QN11 — Copies do not provide coherent oracle access

Amplitude estimation needs controlled preparation and reflection access. Uncontrolled physical copies support ordinary sampling, generally with
\(\Theta(\varepsilon^{-2})\) measurement dependence.

### K-QN12 — Batch evaluation still needs an observable implementation

An exponentially large invariant set is not free merely because its sum is written as one Hamiltonian. A succinct selector or symmetry decomposition is required.

### K-QN13 — Phylogenetic probabilities are not amplitudes

The coherent state \(\sum_x\sqrt{p_x}|x\rangle\) does not lie on the same algebraic variety as the probability tensor \(p\).

### K-QN14 — Postselection multiplies

Each leakage filter or measurement-induced optical nonlinearity introduces a success probability. A polynomial number of constant-success filters can have exponentially small joint acceptance.

### K-QN15 — Permanents have the wrong output

Boson sampling produces samples with probabilities involving
\(|\operatorname{per}|^2\), as already recorded by C-296. Bézout theory asks for a scalar count, the relevant QSAT incidence matrices are nonnegative, and their permanents admit the JSV FPRAS.

### K-QN16 — Fixed small hardware is classically explicit

The two-qubit singlet and three-mode conic are exact small demonstrations. C-298 already records that fixed-mode hardware feasibility does not establish an asymptotic advantage.

### K-QN17 — No parent Hamiltonian for the ideal

Positive local terms intersect kernels. They do not make the span \(I_N\) into a local ground space.  
[D-parent-hamiltonian, C-041, C-043; C-044 is the only few-mode survivor; the contrary draft is REFUTED as C-219]

## Proposed definitions

### D-QN-QSAT-IDEAL

For a quantum \(k\)-SAT instance \(Q=\{\Pi_a\}\), choose an orthonormal rank-one decomposition

\[
\Pi_a=\sum_\mu|\phi_{a\mu}\rangle\langle\phi_{a\mu}|.
\]

Write each \(|\phi_{a\mu}\rangle\) as a multilinear coefficient tensor on its support and form \(f_{a\mu}\) using those coefficients unconjugated. The **QSAT ideal** is

\[
I_Q=(f_{a\mu})
\]

in the Cox ring of \((\mathbb P^{q-1})^n\).

The ideal does not depend on the chosen orthonormal rank-one decomposition, because
\(\operatorname{span}_{\mu}\{f_{a\mu}\}\) is the image of
\(\operatorname{ran}\Pi_a\) in the multilinear forms on \(S_a\); another orthonormal decomposition changes these generators by a unitary matrix.

Source: D-multidegree-sector, D-quantum-k-sat, C-030–C-032.

Pitfalls: coefficients are taken unconjugated; this is what makes
\(a^\dagger(f)a(f)|_{R_{\mathbf1}}=|\phi\rangle\langle\phi|\). The ideal forgets positive weights and spectral conditioning. Under C3 its ground space is the multidegree-\(\mathbf1\) inverse system of \(\overline{I_Q}\).

### D-QN-MULTIPROJECTIVE-SATURATION

For

\[
R=\mathbb C[z_{i,s}]
\]

with site multigrading, let

\[
B=\bigcap_i(z_{i,0},\ldots,z_{i,q-1}).
\]

The **reduced multiprojective saturation** of \(I\) is

\[
J=\sqrt{I:B^\infty}.
\]

By the multiprojective Nullstellensatz, \(J\) is the multihomogeneous vanishing ideal of the reduced closed subscheme

\[
V_{X_0}(I)\subseteq(\mathbb P^{q-1})^n,
\]

of any dimension. Adopt \(I(\varnothing)=R\). If
\(V_{X_0}(I)=\varnothing\), then \(B\subseteq\sqrt I\), hence
\(B^k\subseteq I\) for some \(k\), so \(I:B^\infty=R\).

Source: [Feigin–Makhlin, Theorem 1.8.1](https://doi.org/10.1007/s00029-024-00935-5); multiprojective use in arXiv:2412.19623.

Pitfalls: \(I_{\mathbf1}=J_{\mathbf1}\) is only a degreewise equality and does not imply global radicality or saturation. The closed subscheme need not be finite.

### D-QN-PRODUCT-SPAN

For a QSAT ideal \(I_Q\) and
\(J_Q=\sqrt{I_Q:B^\infty}\), the **product-ground span** is

\[
\mathcal P_Q=(J_Q)_{\mathbf1}^{\perp}.
\]

Equivalently,

\[
\mathcal P_Q
=
\operatorname{span}
\left\{
\bigotimes_i|\overline{x_i}\rangle:
x\in V_{X_0}(I_Q)
\right\},
\]

with \(\mathcal P_Q=\{0\}\) when the variety is empty.

Source: D-coherent-state and C-028.

Pitfalls: \(\mathcal P_Q\) contains entangled superpositions; it is not the set of product states.

### D-QN-MULTIGRADED-ENTANGLED-DEFECT

The **multigraded entangled defect** of \(Q\) is

\[
e_Q
=
\dim(I_Q)_{\mathbf1}^{\perp}
-
\dim(J_Q)_{\mathbf1}^{\perp}
=
\dim(J_Q)_{\mathbf1}-\dim(I_Q)_{\mathbf1}.
\]

Source: specialization of D-entangled-defect.

Pitfalls: it counts linear directions orthogonal to the product-ground span, not entangled rays or an entanglement entropy.

### D-QN-COPY-RESIDUAL-OBSERVABLE

For homogeneous degree-\(m\) equations \(f_j\) on a pure-state amplitude space, let
\(|F_j\rangle\in\operatorname{Sym}^m(\mathcal H)\) satisfy, under C3,

\[
f_j(\overline\psi)
=
\langle F_j|\psi^{\otimes m}\rangle.
\]

C-019 gives

\[
\|F_j\|=\|f_j\|_{\mathrm{BW}}.
\]

For \(w_j\ge0\), define

\[
\Lambda=\sum_jw_j\|F_j\|^2,
\qquad
A_F=\Lambda^{-1}\sum_jw_j|F_j\rangle\langle F_j|.
\]

Then \(A_F\) acts on \(\operatorname{Sym}^m(\mathcal H)\), satisfies
\(0\le A_F\le\mathbb1\), and has expectation

\[
\langle\psi|^{\otimes m}A_F|\psi\rangle^{\otimes m}
=
\Lambda^{-1}\sum_jw_j|f_j(\overline\psi)|^2.
\]

Each shot consumes \(m\) copies.

Source: D-coherent-state, C-019, and the normalized form of C-027.

Pitfalls: residual is not distance; implementing the sum can scale with the number of generators; uncontrolled copies do not supply amplitude-estimation reflections.

### D-QN-TENSOR-NETWORK-VARIETY

For a graph \(G\), local dimensions, and bond bounds \(\boldsymbol\chi\), the
**tensor-network variety** is the Zariski closure of the polynomial contraction image.

For trees and open chains, the bounded-rank locus is characterized by edge-flattening rank conditions
(arXiv:2608.19071). arXiv:1501.01120 concerns comparison of tree tensor formats.

Source: arXiv:1105.4449, arXiv:1501.01120, arXiv:2101.03148,
arXiv:2608.19071.

Pitfalls: the exact parametrized image can be nonclosed; “bond dimension exactly
\(\chi\)” is generally a stratum rather than the closed variety.

### D-QN-PHYSICAL-DATA-ACCESS

D-QN-PHYSICAL-DATA-ACCESS **extends**, rather than replaces, the campaign’s classical
D-input-model. A physical data-state problem must specify one of:

1. uncontrolled copies of \(\rho\);
2. a preparation circuit \(U_\rho\);
3. controlled \(U_\rho,U_\rho^\dagger\);
4. classical measurement samples;
5. a classical amplitude description.

For a comparison, both algorithms must receive the same declared input or the statement must explicitly describe different measurement models on the same physical source.

Source: D-input-model; proposed extension for physical/copy access.

Pitfalls: copy bounds, coherent-query bounds, and classical input runtimes cannot be compared without fixing the access model. A classical copy-access baseline means single-copy, possibly adaptive measurements followed by classical post-processing, not possession of a dense amplitude array.

### D-QN-DUAL-RAIL-SECTOR

The **dual-rail \(\mathbf1\) sector** for \(n\) qubits is the two-optical-mode-per-site Fock subspace with exactly one photon in each mode pair.

Source: D-multidegree-sector; linear-optical computation in
DOI:10.1038/35051009.

Pitfalls: general passive interferometers do not preserve per-site occupation; output postselection is not an energetic hard-core constraint.

### D-multihomogeneous-bezout amendment

No D-QN-PRODUCT-BEZOUT-NUMBER is proposed. The existing
D-multihomogeneous-bezout should instead be amended to include the general-\(q\) coefficient

\[
B_D
=
[t_1^{q-1}\cdots t_n^{q-1}]
\prod_{a=1}^{n(q-1)}
\left(\sum_i d_{ai}t_i\right).
\]

For \(q=2\), \(D\) is square and this coefficient is \(\operatorname{per}(D)\). Definition 52 and Observation 55 of arXiv:2412.19623 supply the PRODSAT Bézout/weighted-SDR formulation; arXiv:2005.14485 supplies the permanent formulation for the one-dimensional-block case.

Pitfalls: this counts product solutions with multiplicity, not QSAT ground-space degeneracy, and it applies directly only to square subsystems.

## Proposed claim rows

### C-NEW-QN-QSAT-INVERSE-SYSTEM

- statement: For every finite `n`-qudit quantum `k`-SAT instance `Q = {Π_a}` and every orthonormal rank-one decomposition `Π_a = Σ_μ|φ_{aμ}⟩⟨φ_{aμ}|`, let `I_Q` be the associated D-QN-QSAT-IDEAL and `Φ_{\mathbf 1}` the multidegree-`\mathbf 1` Macaulay map (D-macaulay-map, D-multidegree-sector). Under the unitary identification `R_{\mathbf 1} ≅ (\mathbb C^q)^{⊗n}`: `H_Q = Φ_{\mathbf 1}Φ_{\mathbf 1}^†`; `ker H_Q = ((I_Q)_{\mathbf 1})^{⊥} = \{u ∈ R_{\mathbf 1} : \bar f(∂)u = 0\ ∀f ∈ I_Q\}`, i.e. the multidegree-`\mathbf 1` piece of the Macaulay inverse system of `\overline{I_Q}` (C3, D-inverse-system); and `\dim\ker H_Q = HF_{R/I_Q}(\mathbf 1)`. This is the multidegree-`\mathbf 1` instance of C-008 and C-009.
- status: CONJECTURE
- depends-on: C-008, C-009, C-033, D-macaulay-map, D-multidegree-sector,
  D-quantum-k-sat, D-inverse-system, D-ground-space, C-030, C-031, C-032
- where-proved: Statement and sketch, steps 1.1–1.18
- where-tested: numerically verified on four instances in
  `verdicts/quantum-native-r1.md`; no L4 checker or mutation record yet

### C-NEW-QN-PRODUCT-SPAN-DEFECT

- statement: For every QSAT ideal `I_Q`, let
  `J_Q := \sqrt{I_Q : B^∞}` with `B` the irrelevant ideal
  (D-QN-MULTIPROJECTIVE-SATURATION), and let `J_Q = R` when
  `V_{X_0}(I_Q) = ∅`. The span of all fully product ground states means
  `span\{⊗_i|\bar x_i⟩ : x ∈ V_{X_0}(I_Q)\}`, with value `{0}` when
  `V = ∅`; it equals `((J_Q)_{\mathbf 1})^⊥`. The dimension of its orthogonal
  complement in the full ground space is
  `e_Q = \dim(J_Q)_{\mathbf 1} - \dim(I_Q)_{\mathbf 1}`.
- status: CONJECTURE
- depends-on: D-QN-MULTIPROJECTIVE-SATURATION, D-QN-PRODUCT-SPAN,
  D-QN-MULTIGRADED-ENTANGLED-DEFECT, D-entangled-defect, C-028, C-029
- where-proved: Statement and sketch, steps 2.1–2.10
- where-tested: numerically verified on three point sets and an explicit
  `e_Q = 1` instance in `verdicts/quantum-native-r1.md`; no L4 checker

### C-NEW-QN-HILBERT-VANISH-ENTANGLEMENT

- statement: For every multihomogeneous ideal `I` in the Cox ring of
  `(\mathbb P^{q-1})^n`, if there exists
  `\mathbf r ≥ \mathbf 1`, `\mathbf r ≠ \mathbf 1`, with
  `HF_{R/I}(\mathbf r)=0`, then `V_{X_0}(I)=∅`. For a QSAT ideal `I_Q`
  with `HF_{R/I_Q}(\mathbf 1)>0`, every nonzero ground state is then
  entangled and, under the convention `I(∅)=R`,
  `e_Q=HF_{R/I_Q}(\mathbf 1)`. This is a multihomogeneous Nullstellensatz
  certificate. The existential completeness direction
  `V_{X_0}(I)=∅ ⇒ HF_{R/I}(\mathbf r)=0` for some finite `\mathbf r`
  follows from saturation; an effective input-size degree bound remains open here.
- status: CONJECTURE
- depends-on: D-hilbert-function, D-variety, D-entangled-defect,
  D-QN-MULTIPROJECTIVE-SATURATION,
  D-QN-MULTIGRADED-ENTANGLED-DEFECT
- where-proved: Statement and sketch, steps 4.1–4.9
- where-tested: the four-qubit profile was numerically recomputed in
  `verdicts/quantum-native-r1.md`; no L4 checker

### C-NEW-QN-SINGLET-HILBERT-WITNESS

- statement: For
  `I = (x_0y_0, x_1y_1, x_0y_1+x_1y_0)`, one has
  `HF_{R/I}(1,1)=1`, `HF_{R/I}(2,2)=0`, and
  `V_{\mathbb P^1\times\mathbb P^1}(I)=∅`; the `(1,1)` inverse-system
  piece is the Bell singlet line. The `9×12` bidegree-`(2,2)` Macaulay
  matrix has rank `9`; 18 of its 220 `9×9` minors are nonzero, each with
  `|det|=1` in the monomial basis. These determinant values are
  basis-dependent under C1.
- status: CONJECTURE
- depends-on: C-NEW-QN-QSAT-INVERSE-SYSTEM,
  C-NEW-QN-HILBERT-VANISH-ENTANGLEMENT, D-macaulay-matrix, C1
- where-proved: Statement and sketch, steps 5.1–5.8
- where-tested: exactly recomputed in `verdicts/quantum-native-r1.md`; no
  L4 checker or recorded red mutation

### C-NEW-QN-HF2-COMPLETE

- statement: For every QSAT ideal `I_Q`,
  `HF_{R/I_Q}(2,\ldots,2)>0` implies the existence of a product ground
  state.
- status: REFUTED
- surviving statement: Vanishing at `(2,\ldots,2)` is sufficient for the
  absence of product ground states, but nonvanishing is inconclusive. For
  five generic four-local rank-one clause vectors on four qubits,
  `HF(1^4)=11`, `HF(2^4)=11`, `HF(3^4)=1`, and `HF(4^4)=0`; the product
  variety is empty and the first certifying diagonal level is `r=4`.
- depends-on: D-hilbert-function, D-variety,
  C-NEW-QN-HILBERT-VANISH-ENTANGLEMENT
- where-proved: refuted by the generic four-qubit family in steps 6.1–6.8
- where-tested: profile recomputed in `verdicts/quantum-native-r1.md`; no
  L4 checker

### C-NEW-QN-BEZOUT-NOVELTY

- statement: The permanent-form multiprojective Bézout count for generic
  product solutions of a QSAT instance is a new consequence of the seed.
- status: REFUTED
- surviving statement: Definition 52 (Bézout number) and Observation 55
  (“the number of weighted SDRs in a PRODSAT instance is equal to the
  Bézout number”) of arXiv:2412.19623 /
  DOI:10.4230/LIPIcs.ITCS.2026.7, together with its remark that computing
  `d_Béz` counts perfect matchings, already contain the QSAT/PRODSAT
  count. The permanent formulation is in arXiv:2005.14485 and in
  D-multihomogeneous-bezout/C-295, not in arXiv:2412.19623. The earlier
  product-satisfiability geometry is due to Laumann et al.,
  DOI:10.1103/PhysRevA.81.062345.
- depends-on: D-multihomogeneous-bezout, D-quantum-k-sat, C-295
- where-proved: literature comparison in steps 7.1–7.11
- where-tested: coefficient/permanent equality recomputed in
  `verdicts/quantum-native-r1.md`

### C-NEW-QN-COPY-RESIDUAL

- statement: For every normalized pure state `|\psi⟩`, every finite family
  of homogeneous degree-`m` equations `f_j`, coefficient vectors `|F_j⟩`
  satisfying `f_j(\bar\psi)=⟨F_j|\psi^{⊗m}⟩`, and nonnegative weights
  `w_j`, let `Λ=Σ_jw_j\|F_j\|²` and
  `A_F=Λ^{-1}Σ_jw_j|F_j⟩⟨F_j|`. Then `0≤A_F≤1`,
  `\|F_j\|=\|f_j\|_{BW}` by C-019, and
  `⟨\psi|^{⊗m}A_F|\psi⟩^{⊗m}
  =Λ^{-1}Σ_jw_j|f_j(\bar\psi)|²`. In
  D-QN-PHYSICAL-DATA-ACCESS case 1, given a measurement of `A_F`, its
  expectation can be estimated to additive error `ε` and failure
  probability `δ` using `m·O(ε^{-2}\log(1/δ))` copies. This is the
  normalized form of C-027.
- status: CONJECTURE
- depends-on: D-QN-COPY-RESIDUAL-OBSERVABLE,
  D-QN-PHYSICAL-DATA-ACCESS, D-coherent-state, C-019, C-027
- where-proved: Entanglement varieties, “What the seed can estimate from copies”
- where-tested: none

### C-NEW-QN-RESIDUAL-EQUALS-DISTANCE

- statement: For every projective variety
  `X=V(f_1,\ldots,f_d)` in `P(\mathcal H)` and every normalized `\psi`,
  `Σ_j|f_j(\bar\psi)|²=dist_{FS}([\bar\psi],X)²`, where `dist_{FS}` is
  Fubini–Study distance.
- status: REFUTED
- surviving statement: The residual vanishes exactly on `X` when the
  equations define `X` set-theoretically. Replacing `f_j` by `λf_j`
  multiplies the left side by `|λ|²` and leaves the right side fixed, so
  no identity can hold for all generating tuples. Quantitative distance
  bounds require fixed normalization and a condition, reach, or
  Łojasiewicz constant.
- depends-on: D-QN-COPY-RESIDUAL-OBSERVABLE, D-condition-number, C3
- where-proved: generator-rescaling counterexample and singular-order
  argument in Entanglement varieties
- where-tested: none

### C-NEW-QN-MPS-TOMOGRAPHY-SPEEDUP

- statement: The `O(nr²)`-copy MPS tester of arXiv:2201.01824 is a
  north-star exponential speedup over the
  `Ω(q^n/ε)`-copy tomography lower bound of arXiv:2206.11185.
- status: REFUTED
- surviving statement: The Soleimanifar–Wright tester is an exponential
  physical-query saving relative to full tomography, with
  `Ω(q^n/ε)` being the `r=1` case of Yuen’s `Ω(rd/ε)` lower bound, but it
  is published prior art and therefore fails the novelty requirement of
  CLAUDE.md §1 / PRD §1. It also compares a membership bit with a complete
  classical description. PRD §2 has no novelty criterion, and its
  criterion 3 makes the input model part of the problem. The same-input
  classical comparator—single-copy adaptive measurement plus classical
  post-processing—is not audited here and is deferred to Question 6.
  Exponential separations for that measurement-model comparison are
  proven for other learning tasks in arXiv:2111.05881 and
  DOI:10.1126/science.abn7293, but no transfer to an entanglement or
  tensor-network variety is established.
- depends-on: D-QN-PHYSICAL-DATA-ACCESS,
  D-QN-TENSOR-NETWORK-VARIETY, D-tensor-secant-problem
- where-proved: Against the north star
- where-tested: none

### C-NEW-QN-COHERENT-OVERLAP-PERMANENT

- statement: Multigraded coherent-state overlaps are general matrix
  permanents and therefore provide a boson-sampling speedup for QSAT
  product-state geometry.
- status: REFUTED
- surviving statement: Segre product-state overlaps factor as
  `∏_i⟨x_i|y_i⟩`; nontrivial permanents arise only from global
  interferometer transitions, which can leave the multidegree sector.
  C-296 already records that boson-sampling devices supply
  permanent-weighted samples rather than the requested scalar count.
  The QSAT Bézout incidence matrices are nonnegative and hence admit the
  Jerrum–Sinclair–Vigoda FPRAS
  (DOI:10.1145/1008731.1008738), so no optical sampling advantage is
  available for that count.
- depends-on: D-optical-counting-access, D-QN-DUAL-RAIL-SECTOR,
  D-multidegree-sector, D-coherent-state, C-295, C-296
- where-proved: Hardware, “Relation to boson sampling”
- where-tested: factorization and Bézout/permanent identities recomputed
  in `verdicts/quantum-native-r1.md`

### C-NEW-QN-OPTICAL-SINGLET-DEMO

- statement: Two photons in four dual-rail modes, passed through two
  balanced beamsplitters and postselected on one photon per rail pair,
  prepare with probability exactly `1/2` the unique ground state
  `-|ψ^-⟩` of the rank-three two-qubit QSAT projector
  `1-|ψ^-⟩⟨ψ^-|`. Conditioned on the occupation pattern `(1,1)` in each
  rail pair and assuming an ideal, unit-efficiency implementation of the
  projector `|ψ^-⟩⟨ψ^-|` and of the maximally mixed probe on the
  four-dimensional dual-rail sector, the acceptance is `1/4` and `119`
  post-selected shots suffice for a `1/8`-additive estimate at `95%`
  confidence. The unconditioned acceptance is
  `η_sector/4`; `η_sector`, losses, and a complete readout protocol remain
  missing ingredients.
- status: CONJECTURE
- depends-on: D-QN-DUAL-RAIL-SECTOR,
  D-analogue-degeneracy-readout, C-297,
  C-NEW-QN-SINGLET-HILBERT-WITNESS
- where-proved: Hardware, “Smallest nontrivial instance” and “What a
  degeneracy measurement would demonstrate”
- where-tested: state-preparation probability and Hoeffding count
  recomputed in `verdicts/quantum-native-r1.md`; no loss-aware L4 checker

### C-NEW-QN-C024-WEAKENING

- statement: C-024’s clause “this quadric ideal’s ground space has already
  been realised experimentally” is not supported by
  DOI:10.1103/PhysRevLett.92.140403, which reports spin-mixing dynamics,
  not a measurement of the `2N+1` ground-space dimension. The supported
  statement is that the Hamiltonian of C-023 has been physically realised
  (arXiv:cond-mat/9807258,
  DOI:10.1103/PhysRevLett.81.5257) and its spin-changing dynamics
  observed.
- status: CONJECTURE
- depends-on: C-023, C-024, C-297,
  D-analogue-degeneracy-readout
- where-proved: Hardware, “Spinor-BEC conic”
- where-tested: source comparison in `verdicts/quantum-native-r1.md`
- lockstep: C-024, its shard, HANDOFF, and the PRD §4 Arm A sentence must
  move together if merged

### C-NEW-QN-ARM-D-NORTHSTAR

- statement: CONJECTURE: For every algorithm family whose only Arm D
  operation is to compose an algorithm for QSAT decision, ground-state
  preparation, gap estimation, degeneracy, or readout with the
  polynomial-time invertible, spectrum-preserving relabelling
  `Π_a ↔ f_{aμ}`, the relabelling supplies no asymptotic speedup. This
  covers exactly algorithms that merely compose with the dictionary. It
  does not cover the bosonic Proposition 8.2 sector C-129/C-130,
  copy-access membership or distance problems for entanglement or
  tensor-network varieties, structured QSAT subfamilies exploiting
  additional structure, or algorithms with new preparation, gap,
  measurement, or readout theorems. For copy-access problems the correct
  comparator is adaptive single-copy measurement plus classical
  post-processing; exponential separations against that comparator exist
  for other learning tasks
  (arXiv:2111.05881, DOI:10.1126/science.abn7293), but no such separation
  is established here for variety membership.
- status: CONJECTURE; HOLD — do not merge as discharging the PRD §4 Arm D
  sentence
- depends-on: D-quantum-k-sat, D-multidegree-sector,
  D-QN-PHYSICAL-DATA-ACCESS, C-NEW-QN-QSAT-INVERSE-SYSTEM,
  C-034, C-036, C-129, C-130
- where-proved: Against the north star, steps 8.1–8.10, for the scoped
  relabelling-composition family only
- where-tested: none

## References

1. Sergey Bravyi, “Efficient algorithm for a quantum analogue of 2-SAT,”
   [arXiv:quant-ph/0602108](https://arxiv.org/abs/quant-ph/0602108).

2. David Gosset and Daniel Nagaj, “Quantum 3-SAT is QMA1-complete,”
   [arXiv:1302.0290](https://arxiv.org/abs/1302.0290).

3. Dorian Rudolph, Sevag Gharibian, and Daniel Nagaj, “Quantum 2-SAT on low dimensional systems is \(\mathsf{QMA}_1\)-complete: Direct embeddings and black-box simulation,”
   [arXiv:2401.02368](https://arxiv.org/abs/2401.02368).

4. Zhengfeng Ji, Zhaohui Wei, and Bei Zeng, “Complete Characterization of the Ground Space Structure of Two-Body Frustration-Free Hamiltonians for Qubits,”
   [arXiv:1010.2480](https://arxiv.org/abs/1010.2480),
   [DOI:10.1103/PhysRevA.84.042338](https://doi.org/10.1103/PhysRevA.84.042338).

5. Brielin Brown, Steven T. Flammia, and Norbert Schuch, “Computational Difficulty of Computing the Density of States,”
   [arXiv:1010.3060](https://arxiv.org/abs/1010.3060),
   [DOI:10.1103/PhysRevLett.107.040501](https://doi.org/10.1103/PhysRevLett.107.040501).

6. Marco Aldi, Sevag Gharibian, and Dorian Rudolph, “An Unholy Trinity: TFNP, Polynomial Systems, and the Quantum Satisfiability Problem,”
   [arXiv:2412.19623](https://arxiv.org/abs/2412.19623),
   [DOI:10.4230/LIPIcs.ITCS.2026.7](https://doi.org/10.4230/LIPIcs.ITCS.2026.7).

7. Mehdi Soleimanifar and John Wright, “Testing matrix product states,”
   [arXiv:2201.01824](https://arxiv.org/abs/2201.01824).

8. J. M. Landsberg, Yang Qi, and Ke Ye, “On the geometry of tensor network states,”
   [arXiv:1105.4449](https://arxiv.org/abs/1105.4449).

9. Alessandra Bernardi and Iacopo Carusotto, “Algebraic Geometry tools for the study of entanglement: an application to spin squeezed states,”
   [arXiv:1109.0221](https://arxiv.org/abs/1109.0221),
   [DOI:10.1088/1751-8113/45/10/105304](https://doi.org/10.1088/1751-8113/45/10/105304).

10. Andrew Critch and Jason Morton, “Algebraic Geometry of Matrix Product States,”
    [arXiv:1210.2812](https://arxiv.org/abs/1210.2812),
    [DOI:10.3842/SIGMA.2014.095](https://doi.org/10.3842/SIGMA.2014.095).

11. Alessandra Bernardi, Claudia De Lazzari, and Fulvio Gesmundo, “Dimension of Tensor Network varieties,”
    [arXiv:2101.03148](https://arxiv.org/abs/2101.03148),
    [DOI:10.1142/S0219199722500596](https://doi.org/10.1142/S0219199722500596).

12. Serkan Hoşten, Niharika Chakrabarty Paul, Otto T. P. Schmidt, and Dmitry Skurt, “Equations of Tree Tensor Network Varieties,”
    [arXiv:2608.19071](https://arxiv.org/abs/2608.19071).

13. Weronika Buczyńska, Jarosław Buczyński, and Mateusz Michałek, “The Hackbusch Conjecture on Tensor Formats,”
    [arXiv:1501.01120](https://arxiv.org/abs/1501.01120).

14. Christopher J. Hillar and Lek-Heng Lim, “Most Tensor Problems are NP-Hard,”
    [arXiv:0911.1393](https://arxiv.org/abs/0911.1393),
    [DOI:10.1145/2512329](https://doi.org/10.1145/2512329).

15. J. M. Landsberg and Jerzy Weyman, “On the ideals and singularities of secant varieties of Segre varieties,”
    [arXiv:math/0601452](https://arxiv.org/abs/math/0601452).

16. J. M. Landsberg and Giorgio Ottaviani, “Equations for secant varieties of Veronese and other varieties,”
    [arXiv:1111.4567](https://arxiv.org/abs/1111.4567),
    [DOI:10.1007/s10231-011-0238-6](https://doi.org/10.1007/s10231-011-0238-6).

17. Henry Yuen, “An Improved Sample Complexity Lower Bound for Fidelity Quantum State Tomography,”
    [arXiv:2206.11185](https://arxiv.org/abs/2206.11185).

18. Elizabeth S. Allman and John A. Rhodes, “Phylogenetic ideals and varieties for the general Markov model,”
    [arXiv:math/0410604](https://arxiv.org/abs/math/0410604).

19. Evangelos Bartzos, Ioannis Z. Emiris, and Josef Schicho, “On the multihomogeneous Bézout bound on the number of embeddings of minimally rigid graphs,”
    [arXiv:2005.14485](https://arxiv.org/abs/2005.14485).

20. Scott Aaronson and Alex Arkhipov, “The Computational Complexity of Linear Optics,”
    [arXiv:1011.3245](https://arxiv.org/abs/1011.3245).

21. Mark Jerrum, Alistair Sinclair, and Eric Vigoda, “A polynomial-time approximation algorithm for the permanent of a matrix with nonnegative entries,”
    [DOI:10.1145/1008731.1008738](https://doi.org/10.1145/1008731.1008738).

22. Emanuel Knill, Raymond Laflamme, and Gerard J. Milburn, “A scheme for efficient quantum computation with linear optics,”
    [DOI:10.1038/35051009](https://doi.org/10.1038/35051009).

23. John Calsamiglia and Norbert Lütkenhaus, “Maximum efficiency of a linear-optical Bell-state analyzer,”
    [arXiv:quant-ph/0007058](https://arxiv.org/abs/quant-ph/0007058),
    [DOI:10.1007/s003400000484](https://doi.org/10.1007/s003400000484).

24. C. K. Law, H. Pu, and N. P. Bigelow, “Quantum Spins Mixing in Spinor Bose-Einstein Condensates,”
    [arXiv:cond-mat/9807258](https://arxiv.org/abs/cond-mat/9807258),
    [DOI:10.1103/PhysRevLett.81.5257](https://doi.org/10.1103/PhysRevLett.81.5257).

25. M.-S. Chang et al., “Observation of Spinor Dynamics in Optically Trapped
    \(^{87}\mathrm{Rb}\) Bose-Einstein Condensates,”
    [DOI:10.1103/PhysRevLett.92.140403](https://doi.org/10.1103/PhysRevLett.92.140403).

26. Adam Czapliński, Mateusz Michałek, and Tim Seynnaeve, “Uniform matrix product states from an algebraic geometer’s point of view,”
    [arXiv:1904.07563](https://arxiv.org/abs/1904.07563).

27. C. R. Laumann, A. M. Läuchli, R. Moessner, A. Scardicchio, and S. L. Sondhi, “Product, generic, and random generic quantum satisfiability,”
    [DOI:10.1103/PhysRevA.81.062345](https://doi.org/10.1103/PhysRevA.81.062345).

28. Leslie G. Valiant, “The Complexity of Computing the Permanent,”
    [DOI:10.1016/0304-3975(79)90044-6](https://doi.org/10.1016/0304-3975(79)90044-6).

29. Sitan Chen, Jordan Cotler, Hsin-Yuan Huang, and Jerry Li, “Exponential separations between learning with and without quantum memory,”
    [arXiv:2111.05881](https://arxiv.org/abs/2111.05881).

30. Hsin-Yuan Huang et al., “Quantum advantage in learning from experiments,”
    [arXiv:2112.00778](https://arxiv.org/abs/2112.00778),
    [DOI:10.1126/science.abn7293](https://doi.org/10.1126/science.abn7293).

31. Evgeny Feigin and Igor Makhlin, “Relative poset polytopes and semitoric degenerations,”
    [DOI:10.1007/s00029-024-00935-5](https://doi.org/10.1007/s00029-024-00935-5).

The erroneous orphan entry naming “Changhyoup Oh” has been removed; the correct first-author name is Changhun Oh. The other listed-but-uncited entries
arXiv:1004.3787, arXiv:1801.02662, arXiv:1508.01907, and arXiv:cs/0405021 have also been removed.

## Questions for TJO

1. Should C-NEW-QN-QSAT-INVERSE-SYSTEM and
   C-NEW-QN-PRODUCT-SPAN-DEFECT enter another critic loop as structural claims despite not being speedup claims?

2. Is the finite-degree criterion
   \[
   \operatorname{HF}(\mathbf1)>0,\qquad
   \operatorname{HF}(\mathbf r)=0
   \]
   a sufficient mathematical product for Arm D if novelty remains unestablished?

3. Should the four-qubit, five-clause profile become the first L4 checker for the multigraded entangled-defect hierarchy?

4. Does an exponential copy saving count as a campaign deliverable when the output is only a property-testing bit?

5. If so, should the target be a genuinely new tester beyond arXiv:2201.01824 rather than the seed residual observable?

6. Should the campaign prioritize proving a separation between collective quantum measurements and adaptive single-copy measurements with classical post-processing for membership in, or distance to, an entanglement or tensor-network variety?

7. Is a one-sided border-rank residual witness sufficient, or must Arm D estimate distance to the secant variety with a proved conditioning constant?

8. Should phylogenetics remain in Arm D only as an analogy, given the mismatch between probability coordinates \(p_x\) and quantum amplitudes \(\sqrt{p_x}\)?

9. Should the proposed C-024 weakening be merged in lockstep into C-024, its shard, HANDOFF, and the PRD §4 Arm A sentence?

10. Is the two-photon singlet experiment worth running if its stated output is an inverse-system/entangled-defect demonstration rather than a speedup?

11. Should PRD Q13’s mechanism dictionary be judged as publishable structure but outside the north star unless it gains a separate algorithmic theorem?

12. Should Arm D remain open specifically for copy-access separations and structured subfamilies, while the relabelling-only route is closed?

13. PRD §2 currently has no novelty criterion; novelty appears in CLAUDE.md §1 / PRD §1. Should novelty remain there, or should PRD §2 be amended with an explicit sixth criterion?

# Repair r1 response

| objection | severity | disposition | exact location | one-line note |
|---|---|---|---|---|
| O1 | MAJOR | FIXED | QSAT dictionary; Complexity conclusions; K-QN3 | Removed the false `#P` attribution to arXiv:1010.2480, cited D-hardness-anchors, and stated the Ji–Wei–Zeng plus Valiant composition as hardness only. |
| O2 | MAJOR | FIXED | QSAT dictionary, promise and exact rows | Split promised QSAT from exact no-promise nonvanishing and cited C-038. |
| O3 | MAJOR | FIXED | Step 2.10; Complexity conclusions; K-QN17 | Replaced REFUTED rows used as authority by their surviving live rows and explicitly labelled the contrary drafts REFUTED. |
| O4 | MAJOR | FIXED | Steps 1.14–1.16; C-NEW-QN-QSAT-INVERSE-SYSTEM | Deleted the false conjugated-orthogonal-complement equality and copied the critic’s inverse-system wording. |
| O5 | MAJOR | DOWNGRADED | Steps 2.10, 4.9, 6.8, 7.10–7.11 | Added Laumann et al. and the multihomogeneous Nullstellensatz hierarchy; novelty is now explicitly unestablished and the effective degree bound open. |
| O6 | MAJOR | RETRACTED | Steps 7.4–7.10; Relation to boson sampling; Proposed definitions and rows | Deleted the duplicate Bézout definition, distinguished AGR from the permanent source, and cited C-295–C-298. |
| O7 | MAJOR | DOWNGRADED | Against the north star; steps 8.1–8.10; C-NEW-QN-ARM-D-NORTHSTAR | Restricted the argument to relabelling-composition families, labelled it a tautology, and placed the broader negative under CONJECTURE/HOLD. |
| O8 | MAJOR | FIXED | The actual MPS-testing result; Against the north star; Criteria audit; MPS row | Stated that §2 has no novelty criterion, used the copy-access baseline required by criterion 3, and audited the known quantum-memory separations without claiming transfer. |
| O9 | MAJOR | FIXED | Spinor-BEC conic; C-NEW-QN-C024-WEAKENING | Added the exact proposed weakening and named every lockstep artifact, including PRD §4 Arm A. |
| O10 | MAJOR | DOWNGRADED | Smallest nontrivial instance; degeneracy readout; optical row | Kept the verified \(1/2\) preparation but conditioned the \(1/4\) acceptance and 119 shots, with unconditioned acceptance \(\eta_{\rm sector}/4\) left explicit. |
| O11 | MAJOR | FIXED | Steps 5.2 and 5.7; singlet row; Hardware example | Used the unnormalised ideal consistently for the integer minors and recorded the distinct \(\sqrt2\)-normalised determinant magnitudes. |
| O12 | MINOR | FIXED | Copy-residual subsection, definition, and row | Defined \(\Lambda\), cited C-019, named access case 1, and restored the factor \(m\) in copy complexity. |
| O13 | MAJOR | FIXED | Steps 2.4–2.5 and 4.6; D-QN-MULTIPROJECTIVE-SATURATION | Replaced “point set” by an arbitrary-dimensional reduced closed subscheme, added \(I(\varnothing)=R\), its proof, and a Nullstellensatz citation. |
| O14 | MINOR | FIXED | C-NEW-QN-COHERENT-OVERLAP-PERMANENT | Removed D-reserved-photonic and now depends on D-optical-counting-access and D-QN-DUAL-RAIL-SECTOR. |
| O15 | MINOR | FIXED | References; tensor-network discussion | Removed all five orphans, added arXiv:1904.07563, expanded both truncated titles, and eliminated the wrong Changhyoup Oh name in favor of the correct Changhun Oh note. |
| O16 | MINOR | FIXED | What a degeneracy measurement would demonstrate | Replaced unconditional \(\Theta(4^n)\)/\(\Theta(2^n)\) claims by degeneracy-sensitive costs and retained the old bounds only as worst cases. |
| O17 | MINOR | FIXED | Which loci are actually varieties; Classical baseline; D-QN-TENSOR-NETWORK-VARIETY | Restricted Hillar–Lim to rank and best rank-one approximation and moved edge-flattening support to arXiv:2608.19071. |
| O18 | MINOR | FIXED | Steps 6.1–6.8; C-NEW-QN-HF2-COMPLETE | Recorded \(11,11,1,0\), generic clause vectors, first certifying level \(r=4\), and existential hierarchy completeness. |
| O19 | MINOR | RESIDUE | `where-tested` fields for inverse-system and singlet rows | The critic recomputations are cited, but no L4 checker or mutation record can be shipped in this read-only memo; both rows remain CONJECTURE. |
| O20 | MINOR | FIXED | Steps 7.1 and 7.7 | Restricted Bézout claims to square subsystems and genericity subject to fixed supports and clause-orthonormality constraints. |
| O21 | MINOR | FIXED | C-NEW-QN-QSAT-INVERSE-SYSTEM | Added C-008, C-009, C-033, and D-macaulay-map dependencies and stated that the row is the multidegree-\(\mathbf1\) instance of C-008/C-009. |

Rows after repair: 13 (CONJECTURE 7, REFUTED 5, HOLD 1, deleted 0)