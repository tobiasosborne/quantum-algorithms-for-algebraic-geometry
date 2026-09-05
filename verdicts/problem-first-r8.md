# Independent audit: coefficient-state Schur reduction and disk counting

2026-09-05. Review of scouting/problem-first-r8.md for root-tracked qaag-7kv.
The reduction, coisometry, product-state probability, and copy-complexity
family were derived independently. Only this verdict file was written.
Root owns canonical definitions and any claims-register changes.

**Verdict: PASS for the mathematical construction and matched copy-cost
obstruction, with no outstanding FATAL, MAJOR, or MINOR objections.**
Both source repairs below were applied and independently verified.
The success probability admits the
stronger bound proved in §3; the corresponding recursion statement must
remain restricted to the displayed fresh-child procedure.
This is not a north-star, historical-priority, or original-algorithm verdict.

## 1. Both strict Schur branches

Let $f$ be real of degree $D\ge1$, with nonzero leading coefficient.
On $|z|=1$, its reversal satisfies
$f^\#(z)=z^D\overline{f(z)}$ and hence $|f^\#(z)|=|f(z)|$.
Assume $f$ has no root on that circle and $|a_D|\ne|a_0|$.
For $h=a_Df-a_0f^\#$, the constant coefficient vanishes and the leading
coefficient is $a_D^2-a_0^2\ne0$. Thus $h=zg$, with $\deg g=D-1$.

If $|a_D|>|a_0|$, the term $a_Df$ strictly dominates on the circle.
Rouché gives $n(h)=n(f)$ and therefore $n(f)=1+n(g)$.
If $|a_D|<|a_0|$, the term $-a_0f^\#$ strictly dominates.
Its inside count is $D-n(f)$, so $1+n(g)=D-n(f)$.
These are exactly the two displayed branches.
Strict domination also prevents $h$, and hence $g$, from having a unit-circle
root. It does not imply strict endpoint inequality at the next step.

The root-count identity for reversal still accounts correctly for zeros of
$f$ at the origin: reversal lowers its degree by their multiplicity, and
the remaining roots are reciprocated. The second branch has $a_0\ne0$;
the first also covers $a_0=0$.

Equality of endpoint moduli is a different event from a unit-circle root.
For example $f=z^2+3z+1$ has roots $(-3\pm\sqrt5)/2$, neither on the circle,
but equal endpoints and $f=f^\#$, so the proposed numerator is identically
zero. This is why a recursive nondegeneracy promise is necessary.

## 2. Coisometry, coordinate deletion, and complex scope

With $q=D+1$, let $R|j\rangle=|D-j\rangle$. Orthogonality of the first
register's endpoint labels gives

\[
 K_DK_D^\dagger
 =\tfrac12(\mathbb1+RR^\dagger)=\mathbb1_q.
\]

For the actual degree-reducing map define

\[
 S_D=\sum_{j=1}^{D}|j-1\rangle\langle j|,\qquad
 \widetilde K_D=S_DK_D.
\]

Then $\widetilde K_D\widetilde K_D^\dagger=\mathbb1_D$.
For every identical product $a\otimes a$, the discarded constant coordinate
is $a_Da_0-a_0a_D=0$, even when the entries are complex.
Consequently deletion adds no loss on the allowed real coefficient-state
inputs, and the success probability is precisely the displayed $p_D(a)$.
For arbitrary other inputs, deletion is a contraction/projection rather than
an operation that may freely erase a populated coordinate.

The success vectors
$(|D,j\rangle-|0,D-j\rangle)/\sqrt2$ are orthonormal.
Endpoint tests, controlled coefficient reversal, and a two-level Hadamard
give the claimed unitary completion. Reversal and reindexing are ordinary
integer permutations on a binary embedding, with unused codewords assigned
a unitary extension. Their costs are polynomial in $\log(D+1)$.
No unknown coefficient division or nontrivial real rotation oracle appears.
The recursion stops before the meaningless $D=0$ endpoint map.

The algebraic action of this physical map does not extend the real root-count
recurrence to complex coefficients. For complex $f$ the correct polynomial is

\[
 f^*(z)=z^D\overline{f(1/\overline z)},\qquad
 g_{\mathbb C}=(\overline{a_D}f-a_0f^*)/z.
\]

As an explicit witness, $f=z^2+z+i/2$ has one inside root.
Using mere reversal gives $g_{\rm wrong}=(5/4)z+1-i/2$, with one inside root,
and would incorrectly predict two. The conjugated version is
$g_{\mathbb C}=(3/4)z+1-i/2$, whose root lies outside, giving the correct count.
The memo correctly restricts its copy circuit to real coefficients.
It does not acquire a conjugate-state source by reversing basis labels.

## 3. Stronger product-input probability and the exact recursion scope

The source's bound $p_D(a)\le |a_0|^2+|a_D|^2$ is correct.
There is a sharper bound on the identical normalized products used here.
Decompose $a=x+y$ into the $+1$ and $-1$ eigenspaces of $R$, and put
$A=\langle0|x\rangle=\langle D|x\rangle$ and
$B=\langle D|y\rangle=-\langle0|y\rangle$.
The two orthogonal components have total squared norm one, and

\[
 a_Da-a_0Ra=2Bx+2Ay.
\]

The distinct endpoint coordinates imply
$|A|^2\le\|x\|^2/2$ and $|B|^2\le\|y\|^2/2$.
Consequently

\[
\begin{aligned}
 p_D(a)
 &=2\bigl(|B|^2\|x\|^2+|A|^2\|y\|^2\bigr)\\
 &\le2\|x\|^2\|y\|^2\le\tfrac12.             \tag{V1}
\end{aligned}
\]

This argument even permits complex $a$, although the Schur-count
interpretation still requires real coefficients. The bound is attained,
for example, by $a=|D\rangle$.

Let $C_t$ denote the **expected** original-copy cost to prepare one accepted
normalized state after $t$ reductions. For the fixed procedure that generates
two fresh children for every parent attempt and discards both on failure,

\[
 C_{t+1}=2C_t/p_t,\quad C_0=1,\quad C_t\ge4^t. \tag{V2}
\]

The equality is an expectation for repeat-until-success preparation; it is not
a deterministic execution cap. A depth-first implementation retains a sibling
at each level, giving the stated $O(D\log D)$ upper bound on live register
space, with source workspace separately charged.

Neither (V1) nor (V2) is a universal lower bound on every possible root-counting
algorithm, every degree-reducing map, or a branch that exploits additional
structure. In particular the degree-one count can be terminated directly after
learning its branch; a claim about taking the displayed circuit all the way to
degree zero is a claim about that chosen procedure.

At every normalized real stage, the final output coefficient is
$(a_D^2-a_0^2)/\sqrt2$, so also
$p_D(a)\ge(|a_D|^2-|a_0|^2)^2/2$.
This does not create an efficient recursion: the promised endpoint gaps and
the cost of producing every reduced-state copy still have to be charged.
The bounded endpoint-outcome variable has the stated mean and gives the
claimed elementary $O(\gamma_t^{-2}\log(D/\epsilon))$ sign-estimation upper.
It is not an optimal-gap complexity assertion.

## 4. The lower-bound radius must remain $5/8$

For $f_R(z)=z^D-R^D$ with $R=1/2$ or $3/4$, both unit-disk counts are $D$.
The two cases therefore cannot give a nontrivial lower bound for the
unit-disk query alone. Their normalized counts at radius $5/8$ are one and
zero, respectively, which is the actual promised output in §5 of the memo.

Rescaling to a unit-disk problem means replacing $f(z)$ by $f(R_0z)$.
For copies this is the diagonal contraction
$A_{R_0}=\sum_jR_0^j|j\rangle\langle j|$ when $0<R_0<1$.
On the displayed family its success probability is

\[
 \frac{R_0^{2D}+R^{2D}}{1+R^{2D}}.
\]

Thus the radius change can condition the surviving states strongly while
having exponentially small success. It is not a free change of notation
or a cost-free replacement for the original coefficient-state source.
The collective source-information lower bound below applies to any physical
replacement using those copies, including attempts to use failure outcomes.

With coefficient bits, by contrast, rescaling is ordinary rational arithmetic.
The source-copy lower bound does not become a lower bound for that model.

## 5. Robust scalar output and matched copy complexity

For $x=2^{-D}$ and $y=(3/4)^D$, the overlap is
$(1+xy)/\sqrt{(1+x^2)(1+y^2)}$. Direct subtraction gives

\[
 \Delta=1-|\langle F_{1/2},F_{3/4}\rangle|^2
 =\frac{(y-x)^2}{(1+x^2)(1+y^2)}\le y^2.
\]

The trace distance of $N$ copies is
$\sqrt{1-(1-\Delta)^N}\le\sqrt{N\Delta}$.
An additive-$1/4$ estimate of the normalized disk count, successful with
probability $2/3$, distinguishes the two inputs by thresholding at $1/2$.
Helstrom's bound therefore forces trace distance at least $1/3$ and
$N\ge1/(9\Delta)\ge(16/9)^D/9$.
This includes arbitrary collective processing of the supplied copies.
It does not compare atomic root distributions in total variation.

The separate measurement strategy is correct for the explicitly used
$D\ge3$ regime. A constant-coordinate outcome has probabilities
$x^2/(1+x^2)$ and $y^2/(1+y^2)$.
For $N=\lceil2\log(3)/y^2\rceil$, the latter input has no-event probability
at most $\exp(-Ny^2/2)\le1/3$.
The former input has any-event probability at most

\[
 Nx^2\le(2\log3+y^2)(2/3)^{2D}<1/3.
\]

The upper bound decreases with $D$ and already holds at $D=3$.
Thus the optimal collective-copy and separate-measurement copy complexities
are both $\Theta((16/9)^D)$ on this promised family.
The upper uses complete-source computational measurements and requires
neither tomography nor any restricted within-copy measurement assumption.

The roots have circle distance $1/8$ from the query boundary and within-set
minimum separation $2R\sin(\pi/D)=\Theta(1/D)$. These geometric conditions
are correctly distinguished from coefficient-state information conditioning.
Exact rational coefficient input has $O(D)$ bits for this family, and the
radius comparison uses polynomial-time integer arithmetic instead.
A coherent preparation unitary with inverse is another stronger access model;
the copy-only lower bound cannot simply be transferred to oracle queries.

## 6. Resolved source clarifications

**RESOLVED MINOR O1 — make nondegeneracy explicitly recursive.**
The initial no-boundary-root promise does not guarantee strict endpoint
inequality at the first stage or at every later reduced polynomial.
The example $z^2+3z+1$ proves the distinction.

**FIX DEMAND:** State that the proposed simple recursion separately promises
strict endpoint modulus inequality at every visited positive degree,
with the known per-stage gap bounds charged in the branch-readout cost.
Do not infer those gaps from the root-boundary promise.
**RESOLUTION:** Current §2 states the promise at every visited positive degree
and includes the equality-pivot counterexample. Section 4 charges the known
stage gaps and explicitly uses the current leading label $D-t$.
The updated source was reread and verified.
**SURVIVING STATEMENT:** Both strict Rouché branches and their physical
real-coefficient implementation hold on that recursive promise domain.
Equality cases require an additional treatment rather than a boundary-root
diagnosis.

**RESOLVED MINOR O2 — label the expected cost and incorporate the stronger bound.**
The recurrence $C_{t+1}=2C_t/p_t$ is an expected repeat-until-success cost.
The current weaker $2^t$ lower bound is valid, but root requested inclusion
of the stronger (V1)–(V2) result.

**FIX DEMAND:** Define $C_t$ as expected original-copy cost; include
$p_t\le1/2$ and hence $C_t\ge4^t$ for this fixed fresh-child recursion.
Keep the explicit exclusion of alternative global maps, algebraic
cancellations, special-family shortcuts, and early termination.
**RESOLUTION:** Current §3 contains the reversal-eigenspace proof of
$p_D\le1/2$ and explicitly defines the deleted-coordinate coisometry.
Section 4 defines expected cost, gives $C_t\ge4^t$, and preserves the requested
cancellation, source-reuse, alternative-map, and early-termination caveats.
The updated source was reread and verified.
**SURVIVING STATEMENT:** The stated implementation has exponential expected
copy cost even before its charged endpoint readouts. This recursion-specific
fact is separate from the genuine all-protocol lower bound in §5.

## 7. Independent checks and historical scope

A 40-second one-BLAS-thread inline probe passed 894 checks.
It checked the original and reduced coisometries for $D=1,\ldots,8$,
constant-coordinate cancellation, product-input probability bounds, and both
strict Schur branches on random real normalized polynomials.
It also checked the real equality-pivot witness, the complex reversal
counterexample, and the exact promised-family error formulas for
$D=3,\ldots,80$. The maximum action residual was $1.15\times10^{-16}$.
The probe would fail with a nonzero exit on a violated identity; it was not
added as a registered proof checker. Symbolic arguments establish the scopes.

After the derivations, the cited primary work was independently fetched as
[Gilyén–Kiss–Jex, arXiv:1508.03191](https://arxiv.org/abs/1508.03191).
It constructs postselected rational state maps and charges the source loss
associated with amplifying small state differences. This is relevant prior
state-processing machinery. It does not by itself show that the exact
degree-changing Schur circuit here was previously printed.

The memo correctly separates a mathematical implementation from an original
algorithmic result. The accepted products are the exact real Schur operation,
its explicitly scoped recursion cost, and the matched robust disk-count
copy-complexity obstruction. No universal impossibility statement for algebraic
root counting, no classical coefficient-list lower bound, and no north-star
success is established.

## 8. Final bounded canonical integration audit

2026-09-05 follow-up. Independently checked definitions/schur-disk-count.md
and proposed C-359/C-360 against the accepted source and this verdict.
The rows were SKETCH during review; promotion remains root-owned.

**Integration verdict: PASS. No FATAL, MAJOR, or MINOR mismatch remains.**
No shared file was edited and no additional numerical campaign was run.

D-DISK-COUNT-INPUT retains the robust normalized-count output, multiplicities,
boundary promise, and the distinction between classical coefficient bits and
copies. Its separate-measurement comparator permits arbitrary adaptive POVMs
on a complete original copy. It supplies neither coefficient queries nor a
preparation inverse by implication.

D-COEFFICIENT-SCHUR-STEP correctly separates the raw map
$K_d:H_d\otimes H_d\to H_d$ from
$\widetilde K_d:H_d\otimes H_d\to H_{d-1}$.
The zero raw output coordinate is explicitly rejected on general inputs and
vanishes identically on the identical products used by the construction.
The dimensions and both coisometry identities in C-359 therefore agree.
Its product probability bound applies independently of the real-only
root-count interpretation.

The all-stage real strict-endpoint promise is explicit and separate from
absence of unit-circle roots. The stage gap uses the current degree $D-t$.
C-359 preserves both strict Rouché branches and asserts normalized output only
on that domain, where the numerator is nonzero.
The expected $C_t$ definition, discard-and-reprepare rule, separately charged
branch readout, and $4^t$ bound are all limited to the fixed fresh-child
recursion. No universal lower bound is inferred from that tree.

D-SEPARATED-RADIAL-DISK-FAMILY fixes $D\ge3$ and radius $5/8$, exactly the
scope in which the stated upper strategy and both error estimates hold.
It explicitly says that the two unit-disk counts agree.
The definition's source-copy cap $N$ is a fixed total cap, including every
failed or postselected event; this is correctly distinct from the expected
cost used for the Schur tree.

C-360 consequently matches the accepted two-state trace-distance lower bound
and the rare-constant-outcome separate-measurement upper bound.
An adaptive protocol using fewer than $N$ copies can be padded with unused
copies, so the same fixed-cap discrimination argument applies.
The two error guarantees concern the robust scalar task, not unrounded atomic
root measures in total variation.

The coefficient-bit comparison, charged radius-rescaling filter, and absence
of any lower-bound transfer to preparation-and-inverse access remain intact.
The canonical integration adds no original-mechanism, all-input hardness, or
new algorithmic-success assertion beyond the reviewed statements.
