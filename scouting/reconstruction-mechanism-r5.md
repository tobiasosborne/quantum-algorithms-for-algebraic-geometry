# Equation-defined reconstruction: a sparse quotient coproduct and its sampler

This memo uses the Euclidean monomial metric on a finite quotient algebra,
explicitly departing from frozen convention C1. Conjugation follows C3. Its
canonical input and operators are D-R5-TRINOMIAL-COPRODUCT in
`definitions/mechanism-r5.md`, including local departures from C6 and C8.
Claim status lives only in `claims/CLAIMS.md`, C-351. Independent review is
`verdicts/reconstruction-mechanism-r5.md`.

The result resolves a conditional opening in
`scouting/original-algebra-round2.md` §1. That memo already derives reverse
multiplication, orthogonal idempotent copying, and nilpotent composition laws.
The additional work here is an equation-level circuit for exponentially large
sparse trinomials, with an exact classical sampler for its entire displayed
terminal experiment. It supplies no original quantum mechanism or speedup.

## 1. Construction before historical verification

Let $D=2^n$, and give the coefficients of

\[
 f(x)=x^D-a x-b,
 \qquad A=\mathbb C[x]/(f),
\]

in binary, together with $n$. The orthonormal computational basis is the
specified monomial basis $1,x,\ldots,x^{D-1}$. It is not an unknown root basis.
Let $M_f:A\otimes A\to A$ be multiplication followed by remainder modulo $f$.
No multiplication table, root list, or normal-form oracle is supplied.

The following formulas use arbitrary complex $a,b$. The explicit classical
bit-complexity family below takes rational $0\le a\le1/4$, $b=1$, $D\ge4$.
Let $B$ bound the input coefficient bit lengths.

For a root $z$, define the conjugated evaluation column and its normalization:

\[
 w_z=\sum_{r=0}^{D-1}\bar z^r|r\rangle,
 \quad \nu_z=\|w_z\|,
 \quad u_z=w_z/\nu_z.
\]

The exact operation suggested by reconstruction is

\[
 M_f^\dagger w_z=w_z\otimes w_z.                 \tag{1}
\]

Indeed, the $(i,j)$-coordinate on the left is the complex conjugate of the
remainder of $x^{i+j}$ evaluated at $z$, hence equals $\bar z^{i+j}$.
Using the unconjugated evaluation column would be wrong for complex data.
Equation (1) itself is the adjoint-multiplication construction already present
in the earlier memo, expressed in the equation-specified metric.

## 2. A complete sparse compilation

Since $i+j\le2D-2$, one reduction suffices:

\[
 x^{i+j}\bmod f=
 \begin{cases}
 x^{i+j},&i+j<D,\\
 b x^{i+j-D}+a x^{i+j-D+1},&i+j\ge D.
 \end{cases}                                  \tag{2}
\]

Consequently,

\[
 M_f^\dagger|r\rangle=
 \sum_{i+j=r}|i,j\rangle
 +\bar b\sum_{i+j=D+r}|i,j\rangle
 +\bar a\sum_{i+j=D+r-1}|i,j\rangle.             \tag{3}
\]

All indices lie between zero and $D-1$. The second sum is omitted for
$r=D-1$; the third is omitted for $r=0$. The latter boundary exception
matters: without it, an erroneous extra term appears at total exponent $D-1$.

Each sum divided by $\sqrt D$ is an explicitly implementable contraction.
Prepare a uniform $n$-bit integer $i$, compute $j=s-i$, and flag the
condition $0\le j<D$. On the valid branch erase the old $r$ using the
known relation between $r$ and $i+j$. This uses integer arithmetic and
Hadamards; it does not use a root-dependent operation or a Fourier transform.

Combining the three contractions by a three-label linear combination gives

\[
 K=M_f^\dagger/\alpha_{\rm BE},
 \qquad \alpha_{\rm BE}=\sqrt D\,\lambda,
 \qquad \lambda=1+|a|+|b|.                     \tag{4}
\]

The combination includes its flag erasure and postselection. A unitary
completion with an ordinary success flag therefore exists constructively.
An elementary implementation costs
$C_K=\operatorname{poly}(n,B,\log(1/\eta))$ gates for operator error $\eta$,
including coefficient rotations and reversible arithmetic. This is a gate
bound, not an uncharged analogue rotation oracle.

A useful independent normalization check is

\[
 M_fM_f^\dagger=
 \operatorname{diag}(1,2,\ldots,D)
 +\sum_{t=0}^{D-2}(D-1-t)
 (b|t\rangle+a|t+1\rangle)
 (\bar b\langle t|+\bar a\langle t+1|).        \tag{5}
\]

The matrix is tridiagonal; (4) upper-bounds its square-root norm.
At every root the heralded copying probability is exactly

\[
 K u_z={\nu_z\over\sqrt D\lambda}\,u_z^{\otimes2},
 \qquad p_z={\nu_z^2\over D\lambda^2}.         \tag{6}
\]

This does not assume that a root state is initially available. Equation (6)
only describes the action on those diagnostic inputs.

## 3. Nontrivial family with constant root heralding

Take $0\le a\le1/4$, $b=1$, $D\ge4$. Every root obeys

\[
 (3/4)^{1/D}\le |z|\le(3/2)^{1/D},
 \qquad {9D\over16}\le\nu_z^2\le{9D\over4}.
\]

For the upper radial bound, a root with $|z|\ge1$ first satisfies $|z|<2$,
because $r^D>1+r/4$ for $r\ge2$. Then $r^D\le1+r/4\le3/2$.
For $r\le1$, the reverse triangle inequality gives $r^D\ge1-r/4\ge3/4$.
Bounding each term of $\sum_r|z|^{2r}$ gives the displayed norm bounds.
Thus $p_z\ge1/9$ under the explicitly compiled normalization.

The family has exponentially many distinct, generally nonorthogonal root
columns. Its small circuit is therefore more than an explicit-table example.
Constant $p_z$ does not imply a fast algorithm for any unprovided root state,
or constant probability for an arbitrary cascade input.

There is already a strong classical root attack. For each integer $j\in[0,D)$,
solve the fixed-point equation

\[
 t=\operatorname{Log}\bigl(1+a\exp((2\pi i j+t)/D)\bigr),
 \qquad z_j=\exp((2\pi i j+t)/D).              \tag{7}
\]

On $|t|\le1/2$, the right side maps into the disk and has derivative magnitude
less than $0.1$. These bounds follow from
$|a\exp((2\pi i j+t)/D)|\le e^{1/8}/4<0.284$.
The $D$ fixed points lie in disjoint argument intervals and exhaust the roots.
Iteration from zero computes a selected root with bit cost polynomial in
$B,n,\log(1/\epsilon)$; no exponential root list is needed.
Uniformly choosing $j$ therefore samples a uniform root classically.

Also, in the binary index encoding, each known root column factorizes:

\[
 w_z=\bigotimes_{k=0}^{n-1}(|0\rangle+\bar z^{2^k}|1\rangle).
\]

Thus preparing its normalized state from an approximated root takes $n$
one-qubit preparations at appropriately charged precision. This observation
does not imply classical simulation for an arbitrary coherent superposition
of unknown root columns.

## 4. Exact terminal problem and quantum resource equation

Use the actual equation-preparable input $|D-1\rangle$, and an integer
$2\le m<D$. Run a binary tree of $m-1$ copies of $K$, herald all successes,
and measure the $m$ output indices. Write

\[
 R_s=[x^{D-1}](x^s\bmod f),\qquad
 N_{m,D}(s)=\#\{(i_1,\ldots,i_m):0\le i_\ell<D,\ \sum i_\ell=s\}.
\]

Associativity gives the exact amplitude and heralding equations

\[
 \langle i_1,\ldots,i_m|K_T|D-1\rangle
 ={\overline{R_{\sum i_\ell}}\over\alpha_{\rm BE}^{m-1}},
 \quad Z_m=\sum_s N_{m,D}(s)|R_s|^2,
 \quad p_m={Z_m\over(D\lambda^2)^{m-1}}.       \tag{8}
\]

Two fully specified outputs are relevant: sample the conditional index tuple,
or estimate the scalar $p_m$ to additive error $\epsilon$ with failure
probability $\delta$. The latter is the normalized squared norm of the
degree-$m$ multiplication functional dual to $x^{D-1}$. It is a
presentation-dependent finite-scheme computation, not an intrinsic invariant.

The quantum sampler needs
$O(p_m^{-1}\log(1/\delta))$ attempts, each costing $O(mC_K+mn)$ gates and
$mn+\operatorname{poly}(n,B,m,\log(1/\eta))$ qubits.
For conditional total-variation error $\epsilon$, a sufficient per-call
accuracy is $\eta=O(\epsilon p_m/m)$. For scalar estimation, ordinary
Bernoulli sampling uses $O(\epsilon^{-2}\log(1/\delta))$ attempts and only
$\eta=O(\epsilon/m)$. Rare success is charged only where conditioning needs it.
No amplitude amplification is used or credited.

## 5. Same-output classical sampler, including bit growth

For the target coefficient $x^{D-1}$, every reduction lowers the exponent
by either $D$ or $D-1$. If there are $k$ reductions and $j$ use the
$a x$ term, the starting exponent must be $s=(k+1)D-1-j$. All orderings
remain above degree $D-1$ until the final reduction, so all contribute:

\[
 R_s=\sum_{k=0}^{m-1}
 \mathbf1_{0\le j_k\le k}\binom{k}{j_k}a^{j_k}b^{k-j_k},
 \qquad j_k=(k+1)D-1-s.                       \tag{9}
\]

For $m<D$, the supporting intervals for different $k$ are disjoint.
There are at most $m(m+1)/2$ supported values of $s$. Values outside the
actual tuple range $0\le s\le m(D-1)$ are discarded.
Inclusion-exclusion supplies their multiplicities:

\[
 N_{m,D}(s)=\sum_{\ell=0}^{\min(m,\lfloor s/D\rfloor)}
 (-1)^\ell\binom m\ell\binom{s-\ell D+m-1}{m-1}.                \tag{10}
\]

Compute these weights, sample $s$ with probability
$N_{m,D}(s)|R_s|^2/Z_m$, and then sample a uniformly random bounded
composition of $s$ into $m$ parts. The latter uses sequential conditional
counts, with cumulative counts evaluated by the binomial hockey-stick identity.
Binary search on each next coordinate costs $O(\log D)$ count evaluations.
This produces exactly the same conditional tuple law as (8).

For rational $a,b$ of $B$ bits, all powers have exponent at most $m-1$.
A common coefficient denominator to power $2(m-1)$ converts the weights
to nonnegative integers. Their bit lengths are
$O(m(B+n+\log m))$, including the composition counts and the sum of weights.
Exact arithmetic therefore gives a randomized classical sampler in
$\operatorname{poly}(m,n,B)$ expected bit operations. Rational cancellations
cause no numerical conditioning assumption. Zero weights are simply skipped.
The contribution $R_{D-1}=1$ guarantees $Z_m>0$.

For the stated nonnegative rational family, $\lambda=2+a$ is rational, so
$p_m$ itself is an exactly computable rational with polynomial bit length.
The scalar output can therefore be computed to any additive precision with
polynomial classical bit cost. This attacks the precise output, including all
herald probabilities, without comparison to full root reconstruction.
The argument does not classically simulate arbitrary further quantum circuits
on the output registers; such extra circuits require a specified new task.

## 6. Retaining failures cannot give free root-preserving retries

Suppose an instrument has Kraus operators $L_c$, all of whose branches copy
each normalized root column: $L_cu_i=d_{ci}u_i\otimes u_i$, and
$\sum_cL_c^\dagger L_c=\mathbb1$. For $G_{ij}=\langle u_i,u_j\rangle$,
completeness forces

\[
 G_{ij}=G_{ij}^2\sum_c\bar d_{ci}d_{cj},
 \qquad\sum_c|d_{ci}|^2=1.
\]

Cauchy-Schwarz implies $|G_{ij}|\le|G_{ij}|^2$, impossible when
$0<|G_{ij}|<1$. This is a scoped no-cloning obstruction, not a new theorem
about every possible useful retained failure. A complementary operator
$(\mathbb1-K^\dagger K)^{1/2}$ is valid mathematically, but its efficient
implementation and its information content do not follow from (3).
A flag dilation of the explicit circuit is available; its other branches
need not preserve root columns or admit free root-label correction.

Using the polar isometry $M_f^\dagger(M_fM_f^\dagger)^{-1/2}$ would change
the operation. The inverse square root is an additional metric transformation,
and generally destroys the copying equation on nonorthogonal roots. It cannot
be silently inserted as a deterministic version of the proposed mechanism.

## 7. Verification, novelty, and disposition

A bounded, one-BLAS-thread numerical probe checked 210 identities for
$D\in\{3,4,5,8,16\}$, three real/complex coefficient pairs, and
$m\in\{2,3,4\}$ when $m<D$. It checked (1), (5), contraction, (8),
and the finite sums (9)--(10) against explicit tensors. The maximum relative
root-copy residual was $2.50\times10^{-14}$. This is a scouting probe,
not a registered red-capable checker or an independent proof certification.
For $a=0.2,b=1,D=8,16,32,64$, implemented root probabilities ranged
approximately from $0.167$ to $0.249$, consistent with the analytical bound.

Targeted primary-source verification occurred after deriving the operation.
[Duan and Guo, quant-ph/9804064](https://arxiv.org/abs/quant-ph/9804064)
construct heralded exact cloning of linearly independent finite state sets.
The root columns for a squarefree $f$ are Vandermonde-independent, and (6)
is a concrete equation-compiled instance of this established mechanism.
[Coecke and Kissinger, arXiv:1002.2540](https://arxiv.org/abs/1002.2540)
already treat copying coalgebras and GHZ/W algebraic structures; merely
replacing reduced root columns by nilpotent jets does not establish originality.
These sources do not claim the specific sparse compiler or sampler derived here.

For $a=0,b=1$, the operation with optimal normalization copies an orthogonal
Fourier basis. This gives an additional exact known-algorithm reduction on that
subfamily. The three-label implementation elsewhere is also ordinary linear
combination machinery. The failure of D22 is substantive, not the vacuous
observation that the circuit can be compiled into universal gates.

A small $D=4$, $m=3$ implementation is an MBQC experiment on the arithmetic
circuit with two heralded branching steps. It tests (8), including failed
trials. A physical passive-optics realization of quotient reduction has not
been supplied; arbitrary MBQC universality is only a concrete small-circuit
route, not evidence of a new heuristic computational advantage.

The useful surviving statement is an efficiently compiled, equation-defined
coproduct on a succinct trinomial algebra together with a polynomial classical
sampler for its demonstrated output. It narrows the old reverse-multiplication
opening and does not reopen its settled generic cases. The missing lemma for
a future different family is a separation for a specified same classical output
after all algebra access and retained-branch costs are charged; for the family
and outputs above, equations (9)--(10) rule out that hoped-for separation.
