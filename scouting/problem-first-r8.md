# Disk root counting by coherent Schur reduction: construction and obstruction

Independent construction, 2026-09-05, tracked by root as `qaag-7kv`.
Canonical inputs and operators are D-DISK-COUNT-INPUT,
D-COEFFICIENT-SCHUR-STEP and D-SEPARATED-RADIAL-DISK-FAMILY in
`definitions/schur-disk-count.md`. Claim status lives only in
`claims/CLAIMS.md`, C-359--C-360; independent review is
`verdicts/problem-first-r8.md`. Euclidean coefficient norms, local degree D
and identity notation depart from C1, C8 and C6 as declared there.

The problem-first route produced an exact two-copy implementation of one step
of classical Schur root counting. The proposed recursion has exponential copy
cost. More decisively, an explicit well-separated-root family has matching
exponential collective-quantum and separate-measurement copy complexity. This
memo establishes no qualifying algorithm and makes no originality claim.

## 1. Actual classical bottleneck and matched output

Given a real polynomial `f(z)=sum_(j=0)^D a_j z^j`, a positive rational radius
`R_0`, and a promise that no zero lies on `|z|=R_0`, compute

\[
 \nu_{R_0}(f)=D^{-1}\#\{z:f(z)=0,\ |z|<R_0\},                \tag{1}
\]

with multiplicity, to additive error `1/4` with probability at least `2/3`.
This is a concrete zero-dimensional real-algebraic counting problem and a
stability-analysis task. The output is a scalar; a full list of root coordinates
is not the comparator. Sampling the root measure accurately enough would imply
this task, but the scalar problem already suffices for the obstruction below.

Two distinct access models must be kept separate:

- **Classical coefficients:** rational coefficients and their bit encodings are
  available to both algorithms. Schur-Cohn reduction, structured inertia
  calculations, and certified argument-principle methods are plausible matched
  classical attacks. The elementary recurrence below uses `O(D^2)` arithmetic
  operations under nonvanishing pivots; this is an upper bound, not an
  adjudication that it is the fastest classical algorithm or a bit bound.
- **Coefficient-state source:** both algorithms receive fresh copies of
  `|a>=sum_j a_j|j>/||a||_2`; no inverse preparation circuit, classical
  coefficients, or conjugate-state source is supplied. The quantum algorithm
  may process copies jointly. The classical measurement comparator may use
  arbitrary adaptive POVMs on one complete copy at a time and unlimited
  classical computation. Section 5 gives a much simpler comparator matching
  even an unrestricted collective-quantum lower bound.

Changing between these models is not free. In particular, the scalar output
does not justify comparing a quantum state with a classical root list.

## 2. Derive the classical reduction before its quantum implementation

First take `R_0=1`. Assume `a_D!=0`, `|a_0|!=|a_D|`, and no unit-circle roots.
Define coefficient reversal `f^#(z)=z^D f(1/z)` and

\[
 g(z)=\frac{a_D f(z)-a_0 f^\#(z)}z.                           \tag{2}
\]

The constant numerator coefficient cancels exactly; its leading coefficient is
`a_D^2-a_0^2`, so `g` has degree `D-1`. Let `n(f)` count roots inside the unit
disk, with multiplicity. On the unit circle, `|f^#|=|f|`. Rouché's theorem gives

\[
 n(f)=
 \begin{cases}
   1+n(g),& |a_D|>|a_0|,\\
   D-1-n(g),& |a_D|<|a_0|.
 \end{cases}                                                \tag{3}
\]

Indeed the first summand in the numerator dominates in the first case, whereas
the reversed polynomial dominates in the second; `n(f^#)=D-n(f)` and the
numerator has the factored zero at the origin. General implementations need
block pivots or another treatment of equality cases. The proposed simple
quantum recursion explicitly promises strict endpoint inequality at every
visited positive-degree reduced polynomial. This is separate from the promise
of no boundary roots: `z^2+3z+1` has no unit-circle root but has equal endpoint
moduli and a zero numerator in (2). Quantitative gaps for learning all visited
branches from copies are additionally charged below.

For complex coefficients, (2) instead needs coefficient conjugation. That is
not supplied by reversing an unknown state. The circuit below is deliberately
restricted to real coefficients; it does not assume universal state conjugation.

## 3. Actual two-register operation

Normalize `||a||_2=1` and let `R|j>=|D-j>` on the `D+1` coefficient labels.
The fixed coisometry

\[
 K_D=\frac{\langle D|\otimes\mathbb 1-⟨0|\otimes R}{\sqrt2}
 \quad\text{satisfies}\quad K_DK_D^\dagger=\mathbb 1.          \tag{4}
\]

It acts on two source copies as

\[
 K_D(|a\rangle\otimes|a\rangle)
  =\frac{a_D|a\rangle-a_0R|a\rangle}{\sqrt2}.                 \tag{5}
\]

The `|0>` amplitude is identically zero. On success, delete this unused
coordinate and subtract one from the remaining label. Formally put
`S_D=sum_(j=1)^D |j-1><j|` and `Ktilde_D=S_D K_D`; then
`Ktilde_D Ktilde_D^dagger=mathbb1_D`. On general two-register inputs the
zero output coordinate is another failed branch; it never occurs on the
promised identical product input in (5). The result is the
normalized coefficient state of (2), with probability

\[
 p_D(a)=\frac12\|a_Da-a_0Ra\|_2^2
       \le |a_0|^2+|a_D|^2.                                 \tag{6}
\]

In fact `p_D(a)<=1/2` on every identical normalized product input. To see this,
write `a=x+y` in the orthogonal +1 and -1 eigenspaces of R, and put
`alpha=<0|x>`, `beta=<D|y>`. Then `a_D=alpha+beta`, `a_0=alpha-beta`,
and the numerator in (5) is `2 beta x+2 alpha y`. The endpoint projections
onto each reversal eigenspace have squared norm one half, so
`|alpha|^2<=||x||^2/2` and `|beta|^2<=||y||^2/2`. Consequently
`p_D<=2||x||^2||y||^2<=1/2`. This bound also holds on complex coefficient
product states, although the root-count interpretation remains real-only.

An explicit circuit first tests whether the first label is `0` or `D`, applies
reversal to the second register conditionally on the first label being zero,
and measures the first two-dimensional label subspace in its difference basis.
It discards both source copies on failure. Equivalently, the orthonormal vectors
`(|D,j>-|0,D-j>)/sqrt(2)` are the success subspace of a unitary completion.
Index tests, reversal, and the shift cost `poly(log D)` gates. There is no
division by an unknown coefficient in this circuit.

This is a concrete information-processing proposal tied to the classical
elimination recurrence. Its first correctness obligation, (5), holds. Its
second obligation, efficient preparation of enough reduced states to finish
(3), fails for the straightforward recursive implementation.

## 4. Resource ledger and the failed algorithmic claim

Let `C_t` be the expected number of original source copies needed to prepare
one normalized polynomial state after `t` degree reductions. In this fixed
repeat-until-success procedure, both children are freshly prepared after every
failed attempt. With `p_t` the success probability at that stage, this gives

\[
 C_0=1,\qquad C_{t+1}=2C_t/p_t,\qquad C_t\ge4^t.              \tag{7}
\]

Thus reducing all the way to degree zero has expected cost at least `4^D`,
before endpoint-sign readout. Stopping at degree one still costs at least
`4^(D-1)` to produce that state by this procedure. These are bounds for the
fixed fresh-child recursion, not universal lower bounds against cancellations,
alternative global maps, source reuse, or promised inputs permitting earlier
termination or structural shortcuts.

To choose the branch in (3), measure an additional reduced-state copy in the
coefficient basis and report `+1` at its current leading label, `-1` at label
`0`, and zero otherwise. At step t the normalized coefficient vector is
`a^(t)` of degree `D-t`, and the mean is
`delta_t=|a^(t)_(D-t)|^2-|a^(t)_0|^2`. A known promise
`|delta_t|>=gamma_t` permits elementary sign estimation with
`O(gamma_t^(-2) log(D/epsilon))` reduced-state copies per step. Those copies
carry their own cost `C_t`; unknown gaps cannot be used to set stopping rules.

The depth-first recursion stores one sibling at each degree, requiring up to
`O(D log D)` live qubits, plus optional source-circuit workspace. Gate work is
the total number of source calls times preparation cost, plus every failed and
successful `K_D` attempt and all readout copies. Normalizing the algebraic
recurrence on paper does not remove (6) or (7).

For a radius `0<R_0<1`, direct coefficient rescaling would use the contraction
`A_(R_0)=sum_j R_0^j|j><j|`, with success

\[
 p_{scale}=\frac{\sum_j|a_j|^2R_0^{2j}}{\sum_j|a_j|^2}.       \tag{8}
\]

This is the familiar attenuation route, not a new mechanism. It must be charged
if used; Section 5 shows why a clever replacement cannot generally remove its
information cost under copy-source access. For exact classical coefficients,
rescaling is ordinary arithmetic, and neither (8) nor the copy lower bound
applies to that bit-access model.

Finite-precision gates and source error would additionally require a known
execution cap and an error budget accounting for rare accepted branches. No
polynomial resource theorem is rescued by leaving that precision unspecified.

## 5. An explicit family with matching quantum and classical copy costs

Fix `R_0=5/8` and

\[
 f_R(z)=z^D-R^D,\qquad R\in\{1/2,3/4\},\qquad
 |F_R\rangle=\frac{|D\rangle-R^D|0\rangle}{\sqrt{1+R^{2D}}}.  \tag{9}
\]

Every root has modulus `R`, so the outputs in (1) are respectively one and
zero. Both root sets have pairwise separation `2R sin(pi/D)=Theta(1/D)` and
distance `1/8` from the counting circle. Geometric root separation and distance
from the query boundary therefore do not alone make amplitude-source access
well conditioned; coefficient-to-root sensitivity still matters.

Write `x=(1/2)^D`, `y=(3/4)^D`. The exact one-copy infidelity is

\[
 \delta=1-|⟨F_{1/2},F_{3/4}⟩|^2
        =\frac{(y-x)^2}{(1+x^2)(1+y^2)}\le y^2.               \tag{10}
\]

For `N` copies, trace distance is `sqrt(1-(1-delta)^N)<=sqrt(N delta)`.
Any estimator succeeding with probability at least `2/3` distinguishes the two
equiprobable inputs with that probability, requiring trace distance at least
`1/3`. Hence even unrestricted collective quantum processing needs

\[
 N\ge\frac1{9\delta}\ge\frac19(16/9)^D.                     \tag{11}
\]

This bound includes arbitrary ancillas, adaptive measurements, and postselection
whose probability is included in the overall success condition.

A classical single-copy strategy matches it: measure each copy in the
coefficient basis; output `R=3/4` if any constant-term outcome appears, and
`R=1/2` otherwise. With

\[
                     N=\left\lceil2\log(3)/y^2\right\rceil, \tag{12}
\]

the error for `R=3/4` is at most `1/3`, since its event probability is
`y^2/(1+y^2)>=y^2/2`. For `R=1/2`, the union bound is
`N x^2<=(2 log 3+y^2)(2/3)^(2D)<1/3` for `D>=3`.
Consequently optimal unrestricted quantum and separate-measurement copy costs
are both `Theta((16/9)^D)` on (9). No tomography lower bound is being used.

With exact rational coefficient bits instead, this family has `O(D)` input bits
and its output follows from comparing `|a_0/a_D|` with `(5/8)^D`, using integer
arithmetic polynomial in `D`. That is a distinct access model; both algorithms
can use the same cheap classical calculation when those bits are available.

## 6. Novelty, verification, and surviving statement

After deriving (2)--(12), a targeted primary-source check found
[Gilyén--Kiss--Jex, DOI:10.1038/srep20076](https://www.nature.com/articles/srep20076).
It implements rational maps through multi-copy unitaries and selective
measurement and proves that amplifying nearby quantum states requires loss of
source copies. This is substantive prior art for the state-processing template
behind (4)--(7), not merely a universal-gate compilation objection. It does not
by itself establish a published exact implementation of this degree-changing
Schur recurrence, and no such historical claim is made here.

The new computational claim sought was a faster scalar disk-root count; the
proposed mechanism was coherent cancellation of the constant coefficient in
the classical Schur step. The exact circuit is real, but the sought speedup
fails its first resource audit. A special polynomial recurrence and a different
register dimension are not an originality certificate under D22.

An inline bounded NumPy calculation, using one BLAS thread, tested (4)--(6)
and the independent root counts in (3) on random real polynomials of degrees
one through seven. It also checked the two error probabilities in (12) at
`D=3,5,10,20,40`. Result: 232 checks passed; worst norm residual `6.28e-16`.
These are exploratory checks, not a registered red-capable checker artifact.

The abandoned initial nilpotent-trace square is not retained as a proposal:
ordinary multiplication paths commute, derivative inversion fails at a
nonreduced point, and the existing trace/residue analyses already cover that
opening. The surviving result of this task is the explicit Schur-step circuit
and the precisely matched copy-complexity obstruction (9)--(12). No hardware
experiment or north-star claim is warranted by this failed algorithmic route.
