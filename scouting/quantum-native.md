# Quantum-native varieties: Arm D, exploration round 2

## Statement and sketch

### Scope corrections

- The multigraded QSAT statement is C-030–C-039 and uses D-multidegree-sector and D-quantum-k-sat.
- Proposition 8.2 is C-129/C-130, not C-125.
- C-125 is the unproved BQP-containment subclaim for ground-overlap estimation and still depends on asserted sparse-access oracles.
- Proposition 8.2 concerns the ordinary total-degree bosonic sector after adding D-hard-core-generators.
- The inverse-system statement below concerns the native multidegree \(\mathbf1=(1,\ldots,1)\) sector.
- Under C3, the ground space is the Hermitian apolar dual of \(I\), equivalently the ordinary inverse system of \(\overline I\).
- No step constructs a D-parent-hamiltonian for \(I_{\mathbf1}\); the QSAT Hamiltonian has kernel \(I_{\mathbf1}^{\perp}\), as required by claims §4.

### The QSAT–inverse-system identity

**1. PROVE.**  
For every \(n\)-qudit quantum \(k\)-SAT instance, its zero-energy space equals the
multidegree-\(\mathbf1\) piece of a Macaulay inverse system.

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

Since \(q\) and \(k\) are fixed, \(r_a\le q^k\), so splitting a clause increases the
description by only a constant factor.  
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

associate the multilinear form

\[
f_{a\mu}
=
\sum_{(s_i)_{i\in S_a}}
c^{(a\mu)}_{(s_i)}
\prod_{i\in S_a}z_{i,s_i}.
\]

Its multidegree is \(\mathbf1_{S_a}=\sum_{i\in S_a}e_i\).  
[D-multidegree-sector, C3]

**1.7 DEFINE.**  
Let

\[
I_Q=(f_{a\mu}:1\le a\le M,\ 1\le\mu\le r_a)\subseteq R.
\]

[D-homogeneous-ideal, D-quantum-k-sat]

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
\(R_{\mathbf1-\mathbf1_{S_a}}\) selects an arbitrary computational-basis state on
the complementary sites.  
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

This is the multigraded instance of D-ground-space.  
[D-ground-space, C-008]

**1.15 PROVE.**  
By C3,

\[
\left((I_Q)_{\mathbf1}\right)^\perp
=
\left\{
u\in R_{\mathbf1}:
\overline f(\partial)u=0
\text{ for every }f\in I_Q
\right\}.
\]

This is the \(\mathbf1\)-piece of the inverse system of \(\overline{I_Q}\).  
[D-inverse-system, C3, C12]

**1.16 PROVE.**  
Equivalently, it is the Hermitian apolar dual of \(I_Q\):

\[
\ker H_Q=(I_Q^\perp)_{\mathbf1}.
\]

The bar must not be dropped when coefficients are complex.  
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
For qubit \(2\)-QSAT this decision problem is classically polynomial-time solvable
(arXiv:quant-ph/0602108).

**1.21 PROVE.**  
For qubit \(3\)-QSAT it is \(\mathrm{QMA}_1\)-complete
(arXiv:1302.0290).

**1.22 PROVE.**  
For bilinear constraints on unequal local dimensions \((2,5)\), it is already
\(\mathrm{QMA}_1\)-complete
(arXiv:2401.02368).

**1.23 CAUTION.**  
\(\mathrm{QMA}_1\)-completeness is a hardness result for verification with a
quantum witness.
It is not evidence that a quantum computer can find or prepare a ground state in BQP.  
[D-quantum-k-sat, C-038]

### Product ground states and the multiprojective variety

**2. PROVE.**  
Product ground-state rays are exactly the points of a multiprojective variety.

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

Then \(J_Q\) is the reduced multiprojective vanishing ideal of the product-solution
locus.  
[D-variety, D-saturation-regularity-stable-range]

**2.5 PROVE.**  
The linear span of all product ground states equals

\[
\mathcal P_Q=(J_Q)_{\mathbf1}^{\perp}.
\]

This is the Segre analogue of the coherent-span identity C-028.  
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

contains no product ray.
Every nonzero vector in that complement is entangled.  
[D-entangled-defect]

**2.9 CAUTION.**  
\(e_Q\) is not the “number of entangled states.”
A positive-dimensional linear space contains uncountably many state rays, and entangled
superpositions can also lie inside \(\mathcal P_Q\).  
[D-entangled-defect]

**2.10 PROVE.**  
The ground space is spanned by product ground states if and only if

\[
(I_Q)_{\mathbf1}=(J_Q)_{\mathbf1}.
\]

This is a degreewise statement, not global radicality.  
[C-029, C-216]

### Other multidegrees

**3. PROVE.**  
Other multidegrees encode bosonic extensions of QSAT, not further degeneracies of the
original instance.

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
For \(\mathbf r\ne\mathbf1\), this describes \(r_i\) indistinguishable bosons at site
\(i\).
It is not the Hilbert space of \(r_i\) distinguishable copies of the original qudit.  
[D-multidegree-sector]

**3.4 PHYSICAL READING.**  
The function \(\mathbf r\mapsto\operatorname{HF}_{R/I_Q}(\mathbf r)\) is the degeneracy
profile of this occupation-number extension.

**3.5 PHYSICAL READING.**  
Its eventual polynomial behavior records the dimension and multiprojective degree of
the product-solution scheme, not the spectrum above the QSAT ground space.

**3.6 PHYSICAL READING.**  
Early-degree deviations record irrelevant torsion, nonreduced structure, and algebraic
relations among constraints.

**3.7 CAUTION.**  
None of those quantities fixes the spectral gap.
Generator rescaling and nearly dependent constraints can change the gap without changing
the ideal or its Hilbert function.  
[D-macaulay-gap, D-normalised-gap]

### A Hilbert-function entanglement witness

**4. PROVE.**  
Vanishing in any strictly positive multidegree certifies that all QSAT ground states are
entangled.

**4.1 ASSUME.**  
Let \(\mathbf r\ge\mathbf1\) componentwise and suppose

\[
\operatorname{HF}_{R/I_Q}(\mathbf1)>0,
\qquad
\operatorname{HF}_{R/I_Q}(\mathbf r)=0.
\]

[D-hilbert-function]

**4.2 PROVE.**  
The second equality says

\[
(I_Q)_{\mathbf r}=R_{\mathbf r}.
\]

[D-hilbert-function]

**4.3 PROVE.**  
If \(x\in V_{X_0}(I_Q)\), every element of \((I_Q)_{\mathbf r}\) vanishes at \(x\).

[D-variety]

**4.4 PROVE.**  
At any multiprojective point \(x\), some monomial of degree \(\mathbf r\) is nonzero.

[D-multidegree-sector]

**4.5 PROVE.**  
Thus \(R_{\mathbf r}\) cannot equal \((I_Q)_{\mathbf r}\) when a product solution exists.

[D-variety]

**4.6 CONCLUDE.**  
Therefore \(V_{X_0}(I_Q)=\varnothing\), while the first equality gives a nonzero ground
space.
Every ground state is entangled, and

\[
e_Q=\operatorname{HF}_{R/I_Q}(\mathbf1).
\]

[D-entangled-defect]

**4.7 SPECIAL CASE.**  
The comparison

\[
\operatorname{HF}(\mathbf1)>0,
\qquad
\operatorname{HF}(2,\ldots,2)=0
\]

is a sufficient certificate of an entangled-only ground space.

**4.8 LIMITATION.**  
The converse fails: nonzero \(\operatorname{HF}(2,\ldots,2)\) does not imply a product
ground state.

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
After rank-one splitting, take

\[
I=
\left(
x_0y_0,\;
x_1y_1,\;
\frac{x_0y_1+x_1y_0}{\sqrt2}
\right)
\subseteq\mathbb C[x_0,x_1,y_0,y_1].
\]

[C-032, C3]

**5.3 PROVE.**  
The three generators are independent in the four-dimensional
\(R_{(1,1)}\), so

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
At bidegree \((2,2)\), \(\dim R_{(2,2)}=3^2=9\).

[D-multidegree-sector]

**5.7 PROVE.**  
Nine products of the three generators with bidegree-\((1,1)\) monomials form a
\(9\times9\) Macaulay minor of determinant \(-1\).

[D-macaulay-matrix]

**5.8 CONCLUDE.**  
Therefore

\[
\operatorname{HF}_{R/I}(2,2)=0.
\]

The criterion in step 4 detects the unique singlet as entangled without optimizing over
product states.  
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
Take four qubits and five generic rank-one \(4\)-local constraints, all of multidegree
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
Five generic hypersurfaces of class \(h_1+h_2+h_3+h_4\) have empty common intersection:
four meet in \(4!=24\) points counting multiplicity, and a fifth generic hypersurface
avoids those points.  
[arXiv:2412.19623, DOI:10.4230/LIPIcs.ITCS.2026.7]

**6.5 PROVE.**  
At degree \((2,2,2,2)\),

\[
\dim R_{(2,2,2,2)}=3^4=81.
\]

[D-multidegree-sector]

**6.6 PROVE.**  
Products of the five generators with \(R_{(1,1,1,1)}\) span at most

\[
5\cdot16=80
\]

dimensions.

[D-homogeneous-ideal]

**6.7 CONCLUDE.**  
Hence

\[
\operatorname{HF}_{R/I}(2,2,2,2)\ge1
\]

despite the absence of every product ground state.

**6.8 CONSEQUENCE.**  
The diagonal Hilbert function becomes a hierarchy of product-unsatisfiability
certificates, but level two is only sufficient, not complete.

### Bézout and BKK counts of product ground states

**7. PROVE.**  
Multiprojective intersection theory gives an exact generic count, but this QSAT statement
is prior art rather than a new Arm D result.

**7.1 ASSUME.**  
Let

\[
m=n(q-1)=\dim(\mathbb P^{q-1})^n
\]

and take exactly \(m\) rank-one clauses.

**7.2 DEFINE.**  
Let \(d_{ai}=1\) if clause \(a\) acts nontrivially on site \(i\), and \(d_{ai}=0\)
otherwise.

**7.3 PROVE.**  
Clause \(a\) defines a divisor of class

\[
\sum_{i=1}^{n}d_{ai}h_i
\]

in the Chow ring

\[
\mathbb Z[h_1,\ldots,h_n]/(h_1^q,\ldots,h_n^q).
\]

[arXiv:2412.19623, DOI:10.4230/LIPIcs.ITCS.2026.7]

**7.4 PROVE.**  
When the common product-solution scheme is zero-dimensional, its length is

\[
B(D)
=
[h_1^{q-1}\cdots h_n^{q-1}]
\prod_{a=1}^{m}
\left(\sum_i d_{ai}h_i\right).
\]

[arXiv:2412.19623, arXiv:2005.14485]

**7.5 SPECIALIZE.**  
For qubits, \(m=n\), so

\[
B(D)=\operatorname{per}(D).
\]

[arXiv:2412.19623, arXiv:2005.14485]

**7.6 BOUND.**  
If every clause has locality at most \(k\), then trivially

\[
B(D)\le k^n,
\]

because each permanent term chooses one of at most \(k\) incident sites per row.

**7.7 GENERICITY.**  
For generic clause coefficients and positive \(B(D)\), the count is exactly \(B(D)\)
with multiplicity.
For special coefficients it remains the intersection number when the intersection is
proper.  
[arXiv:2412.19623]

**7.8 CAUTION.**  
This counts product ground-state rays only.
It says nothing about \(g_Q=\operatorname{HF}_{R/I_Q}(\mathbf1)\), which may be exponentially
larger.

**7.9 CAUTION.**  
The coefficient is a multihomogeneous Bézout number, not the general BKK mixed volume.
Sparse Newton polytopes can give a sharper BKK number.

**7.10 NOVELTY VERDICT.**  
The proposed “new QSAT Bézout bound” is already present, including the weighted
system-of-distinct-representatives interpretation and generic product-solution count, in
arXiv:2412.19623 and DOI:10.4230/LIPIcs.ITCS.2026.7.

**7.11 SURVIVING NEW CANDIDATE.**  
The inverse-system product-span formula in step 2 and the finite-degree entangled-only
certificate in steps 4–6 do not appear in that source.
Novelty remains to be checked adversarially.

## QSAT dictionary

| Algebraic object | Physical meaning | Classical complexity | Quantum complexity | Reference |
|---|---|---|---|---|
| \(R_{\mathbf1}\) | Full \(n\)-qudit Hilbert space | Dimension \(q^n\); basis indexing is polynomial-space | Native \(n\)-qudit register | D-multidegree-sector, C-030 |
| Generating forms \(f_{a\mu}\) | Forbidden rank-one clause vectors | Constructed in polynomial time from the projectors for fixed \(q,k\) | Direct local-projector description | C-032; arXiv:quant-ph/0602108 |
| \((I_Q)_{\mathbf1}\) | Sum of all local forbidden ranges | Explicit rank computation costs exponential dimension in general | Its orthogonal complement is the ground space | D-ground-space |
| \((I_Q)_{\mathbf1}^{\perp}\) | QSAT ground space | Implicitly described by clauses; explicit basis can be exponential | A witness may inhabit it, but preparation is not supplied | D-inverse-system, D-quantum-k-sat |
| \(\operatorname{HF}_{R/I_Q}(\mathbf1)>0\) | Exact frustration freeness | In P for qubit \(2\)-QSAT; \(\mathrm{QMA}_1\)-hard for qubit \(3\)-QSAT | \(\mathrm{QMA}_1\)-complete, not known in BQP | arXiv:quant-ph/0602108; arXiv:1302.0290 |
| Exact \(\operatorname{HF}(\mathbf1)\) | Ground-state degeneracy | \(\#\mathrm P\)-complete even for qubit \(2\)-QSAT | General gapped local degeneracy is \(\#\mathrm{BQP}\)-complete, not ordinary BQP | arXiv:1010.2480; arXiv:1010.3060 |
| \(\operatorname{HF}(\mathbf r)\), \(\mathbf r\ne\mathbf1\) | Degeneracy of a local bosonic occupation extension | Rank of a matrix of dimension \(\prod_i\binom{r_i+q-1}{q-1}\) | No known generic advantage | D-multidegree-sector |
| Minimal multigraded generators | Constraints not implied by lower-multidegree constraints after arbitrary complementary-site multiplication | Input generators are given; minimizing the ideal presentation can require Gröbner computations and exponential output | No known quantum algorithm | D-homogeneous-ideal |
| First syzygies | Linear dependencies among forbidden vectors tensored with complementary states | Kernel of the Macaulay map; exponential sector size | A relation-space nullity, not a ground-state observable by itself | D-syzygy-module |
| Higher syzygies | Relations among those redundancies | Free-resolution computation; output can be exponential | No known QSAT primitive | D-syzygy-module |
| \(V_{X_0}(I_Q)\) | Fully product ground-state rays | Polynomial-system solving; distinct from QSAT decision | Product-state variational search only | C-033; arXiv:2412.19623 |
| \(\dim V_{X_0}(I_Q)\) | Number of continuous parameters in product ground states | Accessible from elimination in small instances; not polynomial uniformly | No known estimator from the QSAT ground state | D-variety |
| Multiprojective degree | Number of product solutions after generic complementary slicing | Bézout/BKK or numerical algebraic geometry | Optical permanent sampling does not directly return it | arXiv:2412.19623; arXiv:1011.3245 |
| \(J_Q=\sqrt{I_Q:B^\infty}\) | Reduced product-solution scheme | Radical and saturation may dominate the computation | No known generic quantum construction | D-saturation-regularity-stable-range |
| Primary decomposition of \(J_Q\) | Branches/components of product solutions | Potentially exponential output | No known quantum output model | D-variety |
| Embedded or nonreduced components of \(I_Q\) | Algebraic multiplicity and finite-degree inverse-system directions | Detected by saturation, radicals, and local dual spaces | May contribute to D-entangled-defect, but not an orthogonal phase decomposition | D-entangled-defect |
| \((J_Q)_{\mathbf1}^{\perp}\) | Span of all product ground states | Requires the product-solution vanishing ideal | Could be probed if a product-state ensemble were available | C-028, C-029 |
| \(e_Q\) | Ground directions orthogonal to every product ground state | Difference of two degree-\(\mathbf1\) Hilbert values | No known efficient generic estimator | D-entangled-defect |
| \(\operatorname{HF}(\mathbf r)=0\), \(\mathbf r\ge\mathbf1\) | Certificate that no product ground state exists | One exponentially large Macaulay-rank computation at that level | No generic speedup; level two is not complete | Steps 4–6 |
| \(\lambda_{\min}(H_Q)\) when \(g_Q=0\) | Frustration energy | Local-Hamiltonian promise problem | \(\mathrm{QMA}_1\)-hard at \(k=3\) | arXiv:1302.0290 |
| Macaulay singular values | Constraint conditioning and excitation energies | Sparse eigensolvers are the baseline | Phase estimation still pays inverse normalized gap | D-macaulay-gap |
| Bézout coefficient \(B(D)\) | Generic number of product ground rays | Permanent for square qubit incidence matrices | Boson sampling returns a related probability, not the count | arXiv:2412.19623; arXiv:1011.3245 |
| Hard-core generators | Energetic isolation of the \(\mathbf1\) occupation pattern inside total degree \(N=n\) | Adds \(3n\) quadratic generators for qubits | Transfers QSAT hardness to the symmetric bosonic sector | D-hard-core-generators, C-129, C-130 |
| A positive parent for \(I_{\mathbf1}\) | Would make the forbidden span, rather than its complement, the ground space | Obstructed by the AND/OR mismatch | QSVT spectral projection is nonlocal | D-parent-hamiltonian, C-040–C-047 |

### Complexity conclusions

- Only the decision boundary for qubit \(2\)-QSAT is classically polynomial.
- Exact degeneracy is already \(\#\mathrm P\)-complete for \(2\)-QSAT
  (arXiv:1010.2480).
- Qubit \(3\)-QSAT frustration-freeness is \(\mathrm{QMA}_1\)-complete
  (arXiv:1302.0290).
- Bilinear \((2,5)\)-QSAT is also \(\mathrm{QMA}_1\)-complete
  (arXiv:2401.02368).
- Minimal generators, syzygies, radicals, and primary decompositions are not thereby
  \(\mathrm{QMA}_1\)-complete.
- They are function or output problems, often with exponentially large outputs.
- No generic quantum procedure in the seed computes any of them.
- The Hilbert dictionary transfers hardness; it does not reduce it.
- C-217 remains binding: without a NO-gap promise, exact Hilbert nonvanishing is not
  thereby placed in \(\mathrm{QMA}_1\).
- C-219 remains binding: no local positive parent Hamiltonian for the ideal itself is
  obtained.

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
- Tensor rank, best rank-\(r\) approximation, multilinear rank, and border rank are
  different outputs.
- General tensor-rank and approximation problems are NP-hard
  (arXiv:0911.1393, DOI:10.1145/2512329).
- D-tensor-secant-problem correctly keeps these outputs separate.

For tensor networks, “fixed bond dimension is an algebraic variety” needs qualification.

- For an open chain, bond dimension at most \(\chi\) is characterized by Schmidt-rank
  bounds across all contiguous cuts.
- Those bounds are flattening-minor equations, so the bounded-rank locus is Zariski closed.
- Tree tensor-network loci similarly admit edge-flattening descriptions
  (arXiv:1501.01120; arXiv:2608.19071).
- Exact bond dimension \(\chi\), as opposed to at most \(\chi\), is generally a locally
  closed stratum.
- For cyclic and more general tensor networks, the parametrized image need not be closed.
- The correct algebraic object is often its Zariski closure
  (arXiv:1105.4449).
- Uniform translation-invariant MPS varieties have additional trace identities and
  boundary phenomena
  (arXiv:1210.2812; arXiv:1904.07563).
- Dimension formulas and bounds are studied in
  arXiv:2101.03148 and DOI:10.1142/S0219199722500596.

The citation suggested in the brief needs correction.

- Bernardi–Carusotto is arXiv:1109.0221, not arXiv:1105.2390.
- It studies symmetric rank, symmetric border rank, coherent spin states, and spin-squeezed
  states.
- Its journal DOI is 10.1088/1751-8113/45/10/105304.
- It is relevant to Veronese/secant entanglement, not the foundational MPS-variety claim.
- Landsberg–Qi–Ye arXiv:1105.4449 is the correct tensor-network geometry citation.

### What the seed can estimate from copies

Let \(\mathcal H=(\mathbb C^q)^{\otimes n}\), with \(D=q^n\), and let
\(|\psi\rangle\in\mathcal H\) be physically supplied.

Suppose \(f_1,\ldots,f_d\) are homogeneous degree-\(m\) equations for a candidate variety
\(X\subseteq\mathbb P(\mathcal H)\).

Represent each equation by a vector \(|F_j\rangle\in\operatorname{Sym}^m(\mathcal H)\) such that

\[
f_j(\overline\psi)
=
\langle F_j|\psi^{\otimes m}\rangle.
\]

Define the normalized residual observable

\[
A_F
=
\frac{1}{\Lambda}
\sum_{j=1}^{d}w_j|F_j\rangle\langle F_j|,
\qquad
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

This is the quantum-native reading of Observation B and D-coherent-state.

It gives the following operational statements.

- If the listed equations generate the vanishing ideal set-theoretically, then
  \(E_F(\psi)=0\) exactly when \([\overline\psi]\in X\).
- If only flattening minors are measured, \(E_F=0\) means membership in the flattening
  relaxation.
- For a general secant variety, that relaxation can strictly contain the desired secant.
- A measured \(E_F>\varepsilon\) is a one-sided nonmembership witness.
- A measured \(E_F\le\varepsilon\) is not a distance certificate without a quantitative
  error bound.
- Rescaling the equations rescales \(E_F\) without changing \(X\).
- Near singular points, residuals can vanish to order greater than the geometric distance.
- Therefore no universal identity
  \(E_F(\psi)=\operatorname{dist}([\psi],X)^2\) exists.
- A Łojasiewicz exponent, reach bound, or condition number would be required to convert
  residual energy into distance.
- This is the entanglement analogue of the D-macaulay-gap conditioning problem.

If one can directly measure \(A_F\), ordinary sampling gives

\[
O\!\left(\varepsilon^{-2}\log(1/\delta)\right)
\]

copies for additive error \(\varepsilon\) and failure probability \(\delta\).

That copy count omits three potentially dominant costs.

- Preparing \(m\) coherent copies for every shot.
- Implementing the projector or block encoding of \(A_F\).
- Normalizing by \(\Lambda\), which can grow with the number and norms of the equations.

Observation B does not make the cost independent of \(d\) automatically.

- A structured LCU, symmetry decomposition, or randomized equation sampler is required.
- If the equations are enumerated one by one, the implementation still costs \(d\).
- If \(d\) is exponential and no succinct selector exists, the proposed batch evaluation
  is not efficient.

With a controlled preparation unitary for \(|\psi\rangle\), its inverse, and coherent access
to \(A_F\), amplitude estimation can improve \(\varepsilon^{-2}\) to
\(O(\varepsilon^{-1})\) coherent queries.

With copies alone, those reflections are not supplied.

Thus the input model must distinguish:

1. a dense classical amplitude array;
2. a sparse or tensor-network classical description;
3. a preparation circuit \(U_\psi\);
4. uncontrolled copies of \(|\psi\rangle\);
5. classical samples from the Born distribution.

These five inputs are not interchangeable.

### Classical baseline

For a dense classical amplitude array:

- Reading the state already costs \(\Omega(D)=\Omega(q^n)\).
- A specified flattening can be formed in \(O(D)\) storage.
- Its numerical rank is obtained by an SVD at a cost determined by its two matrix
  dimensions.
- All contiguous MPS cuts can be checked by sequential Schmidt decompositions.
- Known tensor-network parameters make membership tautological.
- General CP or border-rank optimization remains nonconvex and NP-hard
  (arXiv:0911.1393).

For a circuit description:

- The input length can be polynomial in \(n\).
- Classically expanding its state vector takes \(D\) amplitudes in the worst case.
- But that observation alone is not a lower bound for a particular variety-membership
  property.
- A property-specific classical algorithm may avoid state-vector simulation.
- No such lower bound is supplied by the seed.

For copies of an unknown state:

- A classical amplitude array does not exist.
- Some physical measurement protocol is mandatory.
- Full pure-state tomography to infidelity \(\varepsilon\) requires
  \(\Omega(D/\varepsilon)\) copies
  (arXiv:2206.11185).
- This is exponential in \(n\) for fixed \(q\).
- Full tomography nevertheless returns a much stronger output than a membership bit.

### The actual MPS-testing result

There is a genuine quantum-native property tester already in the literature.

For a pure \(n\)-qudit state and fixed bond dimension \(r\), it distinguishes:

\[
|\psi\rangle\in\mathrm{MPS}_r
\]

from

\[
|\psi\rangle
\text{ being a promised constant distance from every }
\mathrm{MPS}_r
\]

using

\[
O(nr^2)
\]

copies, independent of the local dimension.

It also proves an \(\Omega(\sqrt n)\) copy lower bound for \(r\ge2\)
(arXiv:2201.01824).

Consequences:

- This is exponentially fewer copies than generic tomography when \(D=q^n\).
- It tests a flattening-rank variety without reconstructing the state.
- It is stronger and cleaner than applying the seed to every flattening minor.
- It is prior art, not a new Arm D algorithm.
- Its comparator is tomography, which solves a different and strictly stronger problem.
- It does not establish a quantum time or space speedup over the best classical algorithm
  for the same classically encoded input.
- It is best described as a property-testing advantage for a physical quantum object.
- Under a permissive reading, it is an exponential experimental query saving.
- Under PRD §2’s same-problem and novelty requirements, it is not a north-star hit.

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
- A promise-free exact entanglement-class decision is not statistically identifiable from
  finitely many copies.
- Orbit-closure classes share boundaries, so arbitrarily close states can lie in different
  exact classes.

The seed’s primitive can therefore estimate:

- a normalized sum of squared known invariants;
- a specified flattening-minor residual;
- a one-sided nonmembership witness;
- a promised MPS/tree-network property via more direct existing tests;
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

Tree tensor-network varieties and general Markov models can share flattening-minor
descriptions
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
- Thus ordinary tensor-network amplitude tests answer a different problem.

**Born probabilities of a physical state.**

- If \(p_x=|\psi_x|^2\), a degree-\(m\) polynomial in \(p\) is a diagonal statistic of
  \(m\) independently measured copies.
- The same statistic can be estimated from classical measurement strings.
- Coherence is not automatically useful.
- A quantum advantage would require a coherent oracle and an amplitude-estimation
  comparison, not merely physical preparation.

**Amplitudes deliberately equal to phylogenetic coordinates.**

- A device could be engineered so that \(\psi_x\propto p_x\).
- Observation B would then test invariant violation without tomography.
- That device would model a quantum amplitude tensor, not ordinary observed evolutionary
  frequencies.
- It is a useful analogue demonstration but not a faster phylogenetic inference algorithm.

Therefore shortlist entry 5 remains a classical shadow of shortlist entry 1.

Physical production removes the amplitude-loading cost only when the physically produced
amplitudes are themselves the scientific object.

If only the probabilities are the scientific object, classical samples retain the relevant
information and Arm D gains no asymptotic advantage.

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

This realizes D-multidegree-sector directly.

It does not energetically enforce the sector during a general interferometer.

Two distinct strategies must not be conflated.

1. Inject one photon per dual-rail block and discard outputs that leave the sector.
2. Work in total degree \(N=n\) and add D-hard-core-generators to penalize all other
   occupation patterns.

Strategy 1 is postselection.

Strategy 2 is the C-129/C-130 Hamiltonian reduction.

Passive block-diagonal optics preserves one photon per block but supplies only one-qubit
gates.

A generic QSAT clause needs entangling measurements or measurement-induced nonlinearities.

KLM supplies universal postselected linear-optical gates
(DOI:10.1038/35051009).

Its existence does not supply a favorable success probability for a long QSAT projector
sequence.

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
(x_0y_0,\ x_1y_1,\ (x_0y_1+x_1y_0)/\sqrt2).
\]

It has

\[
\operatorname{HF}_{R/I}(1,1)=1,
\qquad
\operatorname{HF}_{R/I}(2,2)=0,
\qquad
V_{\mathbb P^1\times\mathbb P^1}(I)=\varnothing.
\]

A two-beamsplitter postselected preparation is explicit.

Start with one photon in mode \(a_0\) and one in mode \(b_1\).

Apply balanced beamsplitters

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

Postselect exactly one photon in the \(A\) rails and one in the \(B\) rails.

The surviving state is

\[
\frac{|10\rangle-|01\rangle}{\sqrt2}
\]

up to a global phase.

The success probability is \(1/2\).

No ancillary photon is needed for this state-preparation demonstration.

A standard passive linear-optical Bell analyzer cannot discriminate all four Bell states
with success above \(50\%\) using only vacuum ancillas
(arXiv:quant-ph/0007058, DOI:10.1007/s003400000484).

That limitation does not prevent identifying the singlet signature.

### What a degeneracy measurement would demonstrate

Preparing one singlet demonstrates only that one ground state exists.

It does not measure the ground-space dimension.

For the two-qubit example, a calibrated maximally mixed probe gives

\[
p_0
=
\operatorname{Tr}(P_0\mathbb1/4)
=
\frac{\dim\ker H}{4}
=
\frac14.
\]

If the zero-energy projector is implemented and its efficiency is calibrated, estimate
\(p_0\) to additive error \(1/8\).

Hoeffding’s bound gives

\[
N_{\rm shots}
\ge
\frac{\log(2/0.05)}{2(1/8)^2}
=
118.04,
\]

so \(119\) ideal independent shots suffice for \(95\%\) confidence.

Rounding \(4\widehat p_0\) then distinguishes adjacent integer degeneracies.

This demonstrates:

- the physical rank of the ground projector is one;
- \(\operatorname{HF}_{R/I}(1,1)=1\);
- the sole ground ray is not a point of the Segre variety;
- the ground space is the inverse-system piece rather than the product-solution variety.

It does not demonstrate computational speedup.

For \(n\) qubits, adjacent degeneracies change the maximally mixed ground probability by
\(2^{-n}\).

Independent sampling then needs

\[
\Theta(4^n)
\]

shots for exact integer recovery.

Ideal coherent amplitude estimation still needs

\[
\Theta(2^n)
\]

projector queries.

Thus scalable exact degeneracy readout is exponentially expensive even when the
Hamiltonian is physically available.  
[D-analogue-degeneracy-readout]

### Relation to boson sampling

A passive interferometer \(U\) has collision-free Fock transition amplitudes

\[
\langle S|U_{\rm LO}|T\rangle
=
\operatorname{per}(U_{S,T})
\]

up to occupation factorials
(arXiv:1011.3245).

This fact does not make the QSAT coherent overlaps hard permanents.

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

This is a factorized product.

It can be written as the permanent of a diagonal matrix, but that is computationally
trivial.

For total-degree bosonic coherent states,

\[
\langle p^{\otimes N}|q^{\otimes N}\rangle
=
\langle p|q\rangle^N.
\]

This is likewise the permanent of a repeated rank-one matrix only in a degenerate,
closed-form sense.

Nontrivial permanents arise only after a global interferometer mixes the modes.

Such an interferometer generally leaks out of the \((1,\ldots,1)\) sector.

Postselecting back into that sector produces the boson-sampling permanent, but its success
probability can be exponentially small.

Moreover:

- the device samples from probabilities proportional to
  \(|\operatorname{per}|^2\);
- it does not output the signed or complex permanent;
- a specified rare probability needs inverse-probability shots;
- nonnegative permanents have an FPRAS
  (DOI:10.1145/1008731.1008738);
- QSAT incidence matrices used in the Bézout count are nonnegative.

Therefore boson sampling does not accelerate the Bézout count or inverse-system
degeneracy.

It remains a useful state-preparation and proposal-sampling platform.

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

This matches the spin-mixing interaction of a spin-1 condensate
(arXiv:cond-mat/9807258, DOI:10.1103/PhysRevLett.81.5257).

The algebraic ground-space dimension is

\[
\operatorname{HF}_{R/(f)}(N)=2N+1.
\]

Spin-mixing dynamics and ferromagnetic behavior have been observed experimentally
(DOI:10.1103/PhysRevLett.92.140403).

The record should nevertheless distinguish three claims.

- The Hamiltonian-form identification is supported.
- Spin-changing collisions have been experimentally observed.
- A direct experimental measurement of the full \(2N+1\) Hilbert-function degeneracy has
  not been identified here.

Thus C-024 is strongest as an existing physical realization of the interaction, not yet
as an experimental degeneracy readout.

A two-generator extension in four or five modes would be a useful analogue test only if it
specifies:

- the complete Hamiltonian coefficients;
- the fixed-number sector;
- the normalized spectral gap;
- how the ground projector is measured;
- how degeneracy is separated from thermal occupation;
- the shot count and loss model.

## Against the north star

### Verdict

Arm D does not currently offer a north-star speedup.

It offers:

- an exact QSAT–inverse-system dictionary;
- a candidate new entangled-defect theorem;
- finite-degree algebraic witnesses of entangled-only ground spaces;
- a direct connection to existing MPS property testing;
- the campaign’s cleanest small hardware demonstrations.

The strongest apparent exception is the \(O(nr^2)\)-copy MPS tester
(arXiv:2201.01824).

It is an exponential query saving relative to full tomography, whose lower bound is
\(\Omega(q^n/\varepsilon)\) copies
(arXiv:2206.11185).

It does not satisfy PRD §2 because:

- it is published prior art;
- tomography returns a classical state description, not the same membership bit;
- a classical algorithm cannot receive an unknown quantum state without a measurement
  interface;
- no same-input classical-vs-quantum time or space separation is stated;
- it does not use the seed construction.

### Criteria audit

| PRD §2 criterion | Arm D result | Verdict |
|---|---|---|
| 1. Precise problem | QSAT Hilbert nonvanishing, product-solution geometry, and promised MPS membership are precise | Pass |
| 2. Best classical baseline | Qubit \(2\)-QSAT has a polynomial algorithm; \(3\)-QSAT is hardness, not a practical baseline; MPS tomography is a different output | Partial/fail |
| 3. Quantum algorithm beating that baseline | The inverse-system map is an exact re-encoding; no solver or preparation theorem follows | Fail |
| 4. Dequantization and hidden costs | Quantum input avoids amplitude loading, but gap, copies, residual conditioning, equation implementation, and readout remain | Fail |
| 5. Heuristic hardware attack | Dual rail, postselected Bell tests, and spinor-BEC spin mixing are concrete | Pass |

All five criteria are required.

Failure of criterion 3 is decisive.

### REFUTED-style negative row and proof sketch

**Claim under test.**  
“The multigraded inverse-system construction yields a quantum speedup for QSAT.”

**8.1 ASSUME.**  
An input QSAT instance is supplied as local projectors \(\{\Pi_a\}\).  
[D-quantum-k-sat]

**8.2 PROVE.**  
The construction replaces every rank-one clause vector by the same coefficient tensor
viewed as a multilinear polynomial.  
[C-030–C-032]

**8.3 PROVE.**  
On \(R_{\mathbf1}\), the resulting Hamiltonian is exactly \(H_Q\), with identical spectrum,
gap, and ground projector.  
[D-multidegree-sector]

**8.4 PROVE.**  
The map is computable in polynomial time and is invertible by reading the polynomial
coefficients as clause amplitudes.  
[D-quantum-k-sat]

**8.5 CONCLUDE.**  
Any algorithm using only the resulting local coefficient access can be composed with this
map to give an algorithm with the same asymptotic cost on the original QSAT instance.

**8.6 CONCLUDE.**  
The encoding itself removes no search, preparation, gap, or readout cost.

**8.7 CONCLUDE.**  
For qubit \(3\)-QSAT the resulting decision problem remains
\(\mathrm{QMA}_1\)-complete
(arXiv:1302.0290).

**8.8 VERDICT.**  
The claim that the dictionary alone supplies a speedup is REFUTED.

**8.9 SURVIVING STATEMENT.**  
The dictionary may transfer algebraic invariants, structural theorems, and experimental
witnesses between QSAT and multiprojective geometry.

**8.10 WHY IT CANNOT BE REPAIRED BY REWORDING.**  
A unitary identification of the same matrix cannot itself improve its asymptotic
complexity.

Repair requires a genuinely additional ingredient:

- a restricted QSAT family with a new BQP algorithm;
- a proven resource bound including ground-state preparation and gap;
- a best classical algorithm for the same restricted input and output;
- or a separation between two precisely specified measurement models on the same
  copy-access input.

Calling the state “native” removes loading cost but does not provide any of those four
ingredients.

PRD Q13 should therefore be treated the same way:

- a multigraded mechanism/QSAT dictionary may be a publishable physics construction;
- it is not a speedup unless a separate algorithmic separation is proved.

## Killers

### K-QN1 — Identity is not an algorithm

The QSAT Hamiltonian and the multigraded Macaulay Hamiltonian are the same operator on the
same \(q^n\)-dimensional space.

No asymptotic resource is reduced by renaming its range an ideal piece.

### K-QN2 — QMA hardness is not quantum efficiency

Qubit \(3\)-QSAT is \(\mathrm{QMA}_1\)-complete
(arXiv:1302.0290).

A BQP ground-state preparation or decision algorithm is not implied.

### K-QN3 — Degeneracy is harder than satisfiability

Qubit \(2\)-QSAT decision is polynomial, but exact ground-space dimension is
\(\#\mathrm P\)-complete
(arXiv:1010.2480).

A degeneracy measurement is not a free readout.

### K-QN4 — Other multidegrees change the physical system

\(\operatorname{HF}(\mathbf r)\) for \(\mathbf r\ne\mathbf1\) describes locally symmetrized
bosonic occupations, not copies of the original QSAT system.

### K-QN5 — Product geometry sees only a subset of the ground space

\(V(I_Q)\) lists fully product rays.

It may be empty while \(\operatorname{HF}(\mathbf1)\) is large.

### K-QN6 — Hilbert functions erase the gap

The ideal and its Hilbert function are invariant under generator rescaling.

The excitation spectrum is not.

### K-QN7 — Residual energy is not geometric distance

A sum of squared invariants depends on generator normalization and can vanish at high order
near singularities.

No distance estimate follows without a quantitative error bound.

### K-QN8 — Known equations can be incomplete

Flattening minors do not generally define higher secant varieties.

A zero residual may certify only membership in a relaxation.

### K-QN9 — Tensor-network images may not be closed

For cyclic networks, limits of bounded-parameter tensor-network states need not remain in
the parametrized image
(arXiv:1105.4449).

The algorithmic target must specify the image, its closure, or distance to either.

### K-QN10 — Tomography is the wrong comparator

A membership tester returns one bit.

Tomography returns \(q^n\) amplitudes or a density matrix.

An exponential copy saving against tomography is not automatically a same-problem
speedup.

### K-QN11 — Copies do not provide coherent oracle access

Amplitude estimation needs controlled preparation and reflection access.

Uncontrolled physical copies support ordinary sampling, generally with
\(\Theta(\varepsilon^{-2})\) dependence.

### K-QN12 — Batch evaluation still needs an observable implementation

An exponentially large invariant set is not free merely because its sum is written as one
Hamiltonian.

A succinct selector or symmetry decomposition is required.

### K-QN13 — Phylogenetic probabilities are not amplitudes

The coherent state \(\sum_x\sqrt{p_x}|x\rangle\) does not lie on the same algebraic variety
as the probability tensor \(p\).

### K-QN14 — Postselection multiplies

Each leakage filter or measurement-induced optical nonlinearity introduces a success
probability.

A polynomial number of constant-success filters can have exponentially small joint
acceptance.

### K-QN15 — Permanents have the wrong output

Boson sampling produces samples with probabilities involving
\(|\operatorname{per}|^2\).

Bézout theory asks for a scalar count, and the relevant incidence matrices are
nonnegative.

### K-QN16 — Fixed small hardware is classically explicit

The two-qubit singlet and three-mode conic are exact demonstrations.

Their Hilbert spaces are too small, or their number of modes fixed, to establish an
asymptotic advantage.

### K-QN17 — No parent Hamiltonian for the ideal

Positive local terms intersect kernels.

They do not make the span \(I_N\) into a local ground space.  
[D-parent-hamiltonian, C-040–C-047]

## Proposed definitions

### D-QN-QSAT-IDEAL

For a quantum \(k\)-SAT instance \(Q=\{\Pi_a\}\), choose an orthonormal rank-one
decomposition
\(\Pi_a=\sum_\mu|\phi_{a\mu}\rangle\langle\phi_{a\mu}|\).
The **QSAT ideal** \(I_Q\) is the multihomogeneous ideal generated by the multilinear
coefficient forms \(f_{a\mu}\) in the Cox ring of
\((\mathbb P^{q-1})^n\).

Source: proposed here from D-multidegree-sector and D-quantum-k-sat.

Pitfalls: the ideal forgets positive weights and much spectral conditioning; under C3 its
ground space is the inverse system of \(\overline{I_Q}\), not silently of \(I_Q\).

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

It is the vanishing ideal of the reduced point set
\(V(I)\subseteq(\mathbb P^{q-1})^n\).

Source: proposed here; multiprojective use in
arXiv:2412.19623 and DOI:10.4230/LIPIcs.ITCS.2026.7.

Pitfalls: \(I_{\mathbf1}=J_{\mathbf1}\) is only a degreewise equality and does not imply
global radicality or saturation.

### D-QN-PRODUCT-SPAN

For a QSAT ideal \(I_Q\) and
\(J_Q=\sqrt{I_Q:B^\infty}\), the **product-ground span** is

\[
\mathcal P_Q=(J_Q)_{\mathbf1}^{\perp}.
\]

It is the span of all fully product ground-state rays.

Source: proposed here from D-coherent-state and C-028.

Pitfalls: \(\mathcal P_Q\) contains entangled superpositions; it is not the set of product
states.

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

Source: proposed specialization of D-entangled-defect.

Pitfalls: it counts linear directions orthogonal to the product-ground span, not entangled
rays or an entanglement entropy.

### D-QN-COPY-RESIDUAL-OBSERVABLE

For degree-\(m\) equations \(f_j\) on a pure-state amplitude space, with coefficient vectors
\(|F_j\rangle\), a **copy residual observable** is

\[
A_F=\Lambda^{-1}\sum_jw_j|F_j\rangle\langle F_j|
\]

on \(m\) copies, normalized so \(0\le A_F\le\mathbb1\).

Its expectation is the normalized sum
\(\Lambda^{-1}\sum_jw_j|f_j(\overline\psi)|^2\).

Source: proposed here from D-coherent-state and applications Observation B.

Pitfalls: residual is not distance; implementing the sum can scale with the number of
generators; copies do not supply amplitude-estimation reflections.

### D-QN-TENSOR-NETWORK-VARIETY

For a graph \(G\), local dimensions, and bond bounds \(\boldsymbol\chi\), the
**tensor-network variety** is the Zariski closure of the polynomial contraction image.

For trees and open chains, the bounded-rank locus is characterized by edge-flattening rank
conditions.

Source: arXiv:1105.4449, arXiv:1501.01120, arXiv:2101.03148,
arXiv:2608.19071.

Pitfalls: the exact parametrized image can be nonclosed; “bond dimension exactly
\(\chi\)” is generally a stratum rather than the closed variety.

### D-QN-PHYSICAL-DATA-ACCESS

A **physical data-state input** specifies one of:

1. uncontrolled copies of \(\rho\);
2. a preparation circuit \(U_\rho\);
3. controlled \(U_\rho,U_\rho^\dagger\);
4. classical measurement samples;
5. a classical amplitude description.

Source: proposed here.

Pitfalls: copy bounds, coherent-query bounds, and classical input runtimes cannot be
compared without fixing the same access model.

### D-QN-DUAL-RAIL-SECTOR

The **dual-rail \(\mathbf1\) sector** for \(n\) qubits is the two-photon-mode-per-site Fock
subspace with exactly one photon in each mode pair.

Source: D-multidegree-sector; linear-optical computation in
DOI:10.1038/35051009.

Pitfalls: general passive interferometers do not preserve per-site occupation; output
postselection is not an energetic hard-core constraint.

### D-QN-PRODUCT-BEZOUT-NUMBER

For \(m=n(q-1)\) rank-one clauses with incidence multidegrees \(d_{ai}\in\{0,1\}\), define

\[
B_Q
=
[t_1^{q-1}\cdots t_n^{q-1}]
\prod_{a=1}^{m}\left(\sum_i d_{ai}t_i\right).
\]

It is the multiprojective intersection number and the generic number of product solutions
when the intersection is zero-dimensional.

Source: arXiv:2412.19623, DOI:10.4230/LIPIcs.ITCS.2026.7.

Pitfalls: it counts product solutions with multiplicity, not ground-space degeneracy; for
qubits it is a nonnegative permanent.

## Proposed claim rows

### C-NEW-QN-QSAT-INVERSE-SYSTEM

- statement: For every finite \(n\)-qudit quantum \(k\)-SAT instance
  \(Q=\{\Pi_a\}\), every orthonormal rank-one decomposition of its clauses, and the
  associated D-QN-QSAT-IDEAL \(I_Q\), the unitary identification
  \(R_{\mathbf1}\cong(\mathbb C^q)^{\otimes n}\) satisfies
  \[
  H_Q=\Phi_{\mathbf1}\Phi_{\mathbf1}^{\dagger},
  \qquad
  \ker H_Q=((I_Q)_{\mathbf1})^\perp
  =
  (\overline{I_Q}^{\,\perp})_{\mathbf1},
  \]
  and
  \[
  \dim\ker H_Q=\operatorname{HF}_{R/I_Q}(\mathbf1).
  \]
- status: CONJECTURE
- depends-on: D-multidegree-sector, D-quantum-k-sat, D-inverse-system,
  D-ground-space, C-030, C-031, C-032
- where-proved: Statement and sketch, steps 1.1–1.18
- where-tested: none; the two-qubit determinant calculation is not an L4 checker

### C-NEW-QN-PRODUCT-SPAN-DEFECT

- statement: For every QSAT ideal \(I_Q\), with
  \(J_Q=\sqrt{I_Q:B^\infty}\), the span of all fully product ground states is
  \((J_Q)_{\mathbf1}^{\perp}\), and the dimension of its orthogonal complement in the
  full ground space is
  \[
  e_Q=\dim(J_Q)_{\mathbf1}-\dim(I_Q)_{\mathbf1}.
  \]
- status: CONJECTURE
- depends-on: D-QN-MULTIPROJECTIVE-SATURATION, D-QN-PRODUCT-SPAN,
  D-QN-MULTIGRADED-ENTANGLED-DEFECT, D-entangled-defect, C-028, C-029
- where-proved: Statement and sketch, steps 2.1–2.10
- where-tested: none

### C-NEW-QN-HILBERT-VANISH-ENTANGLEMENT

- statement: For every multihomogeneous QSAT ideal \(I_Q\), if
  \[
  \operatorname{HF}_{R/I_Q}(\mathbf1)>0
  \]
  and there exists \(\mathbf r\ge\mathbf1\) with
  \[
  \operatorname{HF}_{R/I_Q}(\mathbf r)=0,
  \]
  then \(V_{(\mathbb P^{q-1})^n}(I_Q)=\varnothing\), every nonzero QSAT ground state is
  entangled, and
  \[
  e_Q=\operatorname{HF}_{R/I_Q}(\mathbf1).
  \]
- status: CONJECTURE
- depends-on: D-hilbert-function, D-variety, D-entangled-defect,
  D-QN-MULTIGRADED-ENTANGLED-DEFECT
- where-proved: Statement and sketch, steps 4.1–4.8
- where-tested: none

### C-NEW-QN-SINGLET-HILBERT-WITNESS

- statement: For
  \[
  I=(x_0y_0,x_1y_1,x_0y_1+x_1y_0),
  \]
  one has
  \[
  \operatorname{HF}_{R/I}(1,1)=1,
  \qquad
  \operatorname{HF}_{R/I}(2,2)=0,
  \qquad
  V_{\mathbb P^1\times\mathbb P^1}(I)=\varnothing,
  \]
  and the \((1,1)\) inverse-system piece is the Bell singlet line.
- status: CONJECTURE
- depends-on: C-NEW-QN-QSAT-INVERSE-SYSTEM,
  C-NEW-QN-HILBERT-VANISH-ENTANGLEMENT, D-macaulay-matrix
- where-proved: Statement and sketch, steps 5.1–5.8
- where-tested: none; proposed exact checker should verify the \(9\times9\) determinant
  \(-1\)

### C-NEW-QN-HF2-COMPLETE

- statement: For every QSAT ideal \(I_Q\),
  \[
  \operatorname{HF}_{R/I_Q}(2,\ldots,2)>0
  \]
  implies the existence of a product ground state.
- status: REFUTED
- surviving statement: vanishing at \((2,\ldots,2)\) is sufficient for the absence of
  product ground states, but nonvanishing is inconclusive
- depends-on: D-hilbert-function, D-variety,
  C-NEW-QN-HILBERT-VANISH-ENTANGLEMENT
- where-proved: refuted by five generic \(4\)-local rank-one clauses on four qubits;
  \(\operatorname{HF}(\mathbf1)=11\), \(V=\varnothing\), and
  \(\operatorname{HF}(2,2,2,2)\ge1\)
- where-tested: none

### C-NEW-QN-BEZOUT-NOVELTY

- statement: The permanent-form multiprojective Bézout count for generic product solutions
  of a QSAT instance is a new consequence of the seed.
- status: REFUTED
- surviving statement: the count is valid, but it and the weighted-SDR interpretation
  already appear in arXiv:2412.19623 and DOI:10.4230/LIPIcs.ITCS.2026.7
- depends-on: D-multihomogeneous-bezout, D-QN-PRODUCT-BEZOUT-NUMBER,
  D-quantum-k-sat
- where-proved: literature comparison in Statement and sketch, steps 7.1–7.11
- where-tested: none

### C-NEW-QN-COPY-RESIDUAL

- statement: For every normalized pure state \(|\psi\rangle\), every finite family of
  homogeneous degree-\(m\) equations \(f_j\), and every normalization
  \(0\le A_F\le\mathbb1\), the D-QN-COPY-RESIDUAL-OBSERVABLE satisfies
  \[
  \langle\psi|^{\otimes m}A_F|\psi\rangle^{\otimes m}
  =
  \Lambda^{-1}\sum_jw_j|f_j(\overline\psi)|^2,
  \]
  and its expectation can be estimated to additive error \(\varepsilon\) and failure
  probability \(\delta\) using
  \(O(\varepsilon^{-2}\log(1/\delta))\) independent measurements once \(A_F\) is
  implementable.
- status: CONJECTURE
- depends-on: D-QN-COPY-RESIDUAL-OBSERVABLE, D-coherent-state, C-027
- where-proved: Entanglement varieties, “What the seed can estimate from copies”
- where-tested: none

### C-NEW-QN-RESIDUAL-EQUALS-DISTANCE

- statement: For every projective variety \(X=V(f_1,\ldots,f_d)\) and every normalized
  \(\psi\),
  \[
  \sum_j|f_j(\psi)|^2=\operatorname{dist}([\psi],X)^2.
  \]
- status: REFUTED
- surviving statement: the residual vanishes exactly on \(X\) when the equations define
  \(X\) set-theoretically; quantitative distance bounds require fixed normalization and a
  condition, reach, or Łojasiewicz constant
- depends-on: D-QN-COPY-RESIDUAL-OBSERVABLE, D-condition-number
- where-proved: generator-rescaling counterargument and singular-order argument in
  Entanglement varieties
- where-tested: none

### C-NEW-QN-MPS-TOMOGRAPHY-SPEEDUP

- statement: The \(O(nr^2)\)-copy MPS tester of arXiv:2201.01824 is a north-star
  exponential speedup over the \(\Omega(q^n/\varepsilon)\)-copy tomography lower bound of
  arXiv:2206.11185.
- status: REFUTED
- surviving statement: it is an exponential physical-query saving relative to full
  tomography, but it is prior art and compares a membership bit with a complete classical
  description, so PRD §2 criteria 2 and 3 are not met
- depends-on: D-QN-PHYSICAL-DATA-ACCESS, D-QN-TENSOR-NETWORK-VARIETY,
  D-tensor-secant-problem
- where-proved: Against the north star
- where-tested: none

### C-NEW-QN-COHERENT-OVERLAP-PERMANENT

- statement: Multigraded coherent-state overlaps are general matrix permanents and
  therefore provide a boson-sampling speedup for QSAT product-state geometry.
- status: REFUTED
- surviving statement: Segre product-state overlaps factor as
  \(\prod_i\langle x_i|y_i\rangle\); nontrivial permanents arise only from global
  interferometer transitions, which can leave the multidegree sector
- depends-on: D-reserved-photonic, D-multidegree-sector,
  D-optical-counting-access, D-coherent-state
- where-proved: Hardware, “Relation to boson sampling”
- where-tested: none

### C-NEW-QN-OPTICAL-SINGLET-DEMO

- statement: Two photons in four dual-rail modes, passed through two balanced
  beamsplitters and postselected on one photon per rail pair, prepare with probability
  \(1/2\) the unique ground state of the rank-three two-qubit QSAT projector
  \(\mathbb1-|\psi^-\rangle\langle\psi^-|\); a calibrated maximally mixed ground-projector
  test has acceptance \(1/4\) and \(119\) ideal shots suffice to resolve its integer
  degeneracy with \(95\%\) confidence by a \(1/8\)-additive estimate.
- status: CONJECTURE
- depends-on: D-QN-DUAL-RAIL-SECTOR, D-analogue-degeneracy-readout,
  C-NEW-QN-SINGLET-HILBERT-WITNESS
- where-proved: Hardware, “Smallest nontrivial instance”
- where-tested: none; requires an optical circuit simulation and loss-aware checker

### C-NEW-QN-ARM-D-NORTHSTAR

- statement: For every QSAT instance, translating its local projectors to
  D-QN-QSAT-IDEAL and restricting the seed Hamiltonian to multidegree \(\mathbf1\) yields
  an asymptotically faster quantum algorithm for deciding frustration freeness.
- status: REFUTED
- surviving statement: the translation is a polynomial-time, spectrum-preserving
  identification and can support new structural theorems or experiments, but supplies no
  solver or speedup
- depends-on: D-quantum-k-sat, D-multidegree-sector,
  C-NEW-QN-QSAT-INVERSE-SYSTEM, C-034, C-036
- where-proved: Against the north star, steps 8.1–8.10
- where-tested: none

## References

1. Sergey Bravyi, “Efficient algorithm for a quantum analogue of 2-SAT,”
   arXiv:quant-ph/0602108.

2. David Gosset and Daniel Nagaj, “Quantum 3-SAT is QMA1-complete,”
   arXiv:1302.0290.

3. Dorian Rudolph, Sevag Gharibian, and Daniel Nagaj, “Quantum 2-SAT on low dimensional
   systems is \(\mathsf{QMA}_1\)-complete,” arXiv:2401.02368.

4. Zhengfeng Ji, Zhaohui Wei, and Bei Zeng, “Complete Characterization of the Ground Space
   Structure of Two-Body Frustration-Free Hamiltonians for Qubits,” arXiv:1010.2480,
   DOI:10.1103/PhysRevA.84.042338.

5. Jianxin Chen, Xie Chen, Runyao Duan, Zhengfeng Ji, and Bei Zeng, “No-go Theorem for
   One-way Quantum Computing on Naturally Occurring Two-level Systems,” arXiv:1004.3787,
   DOI:10.1103/PhysRevA.83.050301.

6. Brielin Brown, Steven T. Flammia, and Norbert Schuch, “Computational Difficulty of
   Computing the Density of States,” arXiv:1010.3060,
   DOI:10.1103/PhysRevLett.107.040501.

7. Marco Aldi, Sevag Gharibian, and Dorian Rudolph, “An Unholy Trinity: TFNP, Polynomial
   Systems, and the Quantum Satisfiability Problem,” arXiv:2412.19623,
   DOI:10.4230/LIPIcs.ITCS.2026.7.

8. Mehdi Soleimanifar and John Wright, “Testing matrix product states,”
   arXiv:2201.01824.

9. J. M. Landsberg, Yang Qi, and Ke Ye, “On the geometry of tensor network states,”
   arXiv:1105.4449.

10. Alessandra Bernardi and Iacopo Carusotto, “Algebraic Geometry tools for the study of
    entanglement,” arXiv:1109.0221, DOI:10.1088/1751-8113/45/10/105304.

11. Andrew Critch and Jason Morton, “Algebraic Geometry of Matrix Product States,”
    arXiv:1210.2812, DOI:10.3842/SIGMA.2014.095.

12. Alessandra Bernardi, Claudia De Lazzari, and Fulvio Gesmundo, “Dimension of Tensor
    Network varieties,” arXiv:2101.03148, DOI:10.1142/S0219199722500596.

13. Serkan Hoşten, Niharika Chakrabarty Paul, Otto T. P. Schmidt, and Dmitry Skurt,
    “Equations of Tree Tensor Network Varieties,” arXiv:2608.19071.

14. Weronika Buczyńska, Jarosław Buczyński, and Mateusz Michałek, “The Hackbusch
    Conjecture on Tensor Formats,” arXiv:1501.01120.

15. Ke Ye and Lek-Heng Lim, “Tensor network ranks,” arXiv:1801.02662.

16. Christopher J. Hillar and Lek-Heng Lim, “Most Tensor Problems are NP-Hard,”
    arXiv:0911.1393, DOI:10.1145/2512329.

17. J. M. Landsberg and Jerzy Weyman, “On the ideals and singularities of secant varieties
    of Segre varieties,” arXiv:math/0601452.

18. J. M. Landsberg and Giorgio Ottaviani, “Equations for secant varieties of Veronese and
    other varieties,” arXiv:1111.4567, DOI:10.1007/s10231-011-0238-6.

19. Henry Yuen, “An Improved Sample Complexity Lower Bound for Fidelity Quantum State
    Tomography,” arXiv:2206.11185.

20. Ryan O’Donnell and John Wright, “Efficient quantum tomography,” arXiv:1508.01907.

21. Elizabeth S. Allman and John A. Rhodes, “Phylogenetic ideals and varieties for the
    general Markov model,” arXiv:math/0410604.

22. Evangelos Bartzos, Ioannis Z. Emiris, and Josef Schicho, “On the multihomogeneous
    Bézout bound on the number of embeddings of minimally rigid graphs,”
    arXiv:2005.14485.

23. Scott Aaronson and Alex Arkhipov, “The Computational Complexity of Linear Optics,”
    arXiv:1011.3245.

24. Mark Jerrum, Alistair Sinclair, and Eric Vigoda, “A polynomial-time approximation
    algorithm for the permanent of a matrix with nonnegative entries,”
    DOI:10.1145/1008731.1008738.

25. Emanuel Knill, Raymond Laflamme, and Gerard J. Milburn, “A scheme for efficient
    quantum computation with linear optics,” DOI:10.1038/35051009.

26. John Calsamiglia and Norbert Lütkenhaus, “Maximum efficiency of a linear-optical
    Bell-state analyzer,” arXiv:quant-ph/0007058, DOI:10.1007/s003400000484.

27. C. K. Law, H. Pu, and N. P. Bigelow, “Quantum Spins Mixing in Spinor Bose-Einstein
    Condensates,” arXiv:cond-mat/9807258, DOI:10.1103/PhysRevLett.81.5257.

28. M.-S. Chang et al., “Observation of Spinor Dynamics in Optically Trapped
    \(^{87}\mathrm{Rb}\) Bose-Einstein Condensates,”
    DOI:10.1103/PhysRevLett.92.140403.

29. Changhyoup Oh, Minzhao Liu, Yuri Alexeev, Bill Fefferman, and Liang Jiang, “Classical
    Algorithm for Simulating Experimental Gaussian Boson Sampling,” arXiv:2306.03709,
    DOI:10.1038/s41567-024-02535-8.

30. Gregorio Malajovich and Klaus Meer, “Computing Multi-Homogeneous Bezout Numbers is
    Hard,” arXiv:cs/0405021.

## Questions for TJO

1. Should C-NEW-QN-QSAT-INVERSE-SYSTEM and
   C-NEW-QN-PRODUCT-SPAN-DEFECT enter a critic loop as structural claims, despite not being
   speedup claims?

2. Is the finite-degree criterion
   \[
   \operatorname{HF}(\mathbf1)>0,\qquad
   \operatorname{HF}(\mathbf r)=0
   \]
   a sufficient mathematical product for Arm D?

3. Should the four-qubit, five-clause counterexample become the first checker for the
   multigraded entangled-defect hierarchy?

4. Does an exponential copy saving against tomography count as a campaign deliverable when
   the property-testing output is only one bit?

5. If it does, should the target be a genuinely new tester beyond
   arXiv:2201.01824 rather than the seed residual observable?

6. Should the campaign define a same-copy-input classical comparator, such as adaptive
   single-copy measurements with classical postprocessing, before using “quantum query
   advantage”?

7. Is a one-sided border-rank residual witness sufficient, or must Arm D estimate distance
   to the secant variety with a proved conditioning constant?

8. Should phylogenetics remain in Arm D only as an analogy, given the mismatch between
   probability coordinates \(p_x\) and quantum amplitudes \(\sqrt{p_x}\)?

9. Should C-024 be weakened from “ground space already realised experimentally” to
   “the interaction and spin-mixing dynamics have been realised, but Hilbert-function
   degeneracy has not been read out”?

10. Is the two-photon singlet experiment worth running if its stated output is an
    inverse-system/entangled-defect demonstration rather than a speedup?

11. Should PRD Q13’s mechanism dictionary be judged by the same standard: publishable
    structure, but outside the north star unless it gains a separate algorithmic theorem?

12. Does TJO want Arm D closed as a speedup arm while retaining it as a structural and
    hardware-demonstration arm?