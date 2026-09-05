# Arithmetic incidence scattering: construction and matched sampling audit

2026-09-05; bounded constructor lane under `qaag-6p5`; no claim promotion.
This memo departs from C1/C2/C5: the Hilbert spaces have orthonormal bases
indexed by finite-field points and lines, and generators have explicit finite-field
coefficients. No Fock norm, spectral-gap convention, or quantum input is used.
All new notation below is a provisional definitions MERGE PROPOSAL, local to this
unmerged memo. Root owns the canonical registers and independent adjudication.

The constructed operation is a deterministic orthogonal point-to-line transform.
It samples lines according to squared, centered intersection counts with an
explicit algebraic curve. Its Fourier decomposition defeats D22. Independently,
a classical rejection sampler needs at most three proposals on average and
polynomial root-counting work per proposal. These are scoped statements about
this construction, not an impossibility claim for arithmetic geometry.

## 1. Provisional definitions MERGE PROPOSAL

**D-IG4-FIELD.** Let `q=2^(2m)`, with `m>=1`; an irreducible binary polynomial
of degree `2m` supplies the representation of `F_q`. Thus `sqrt(q)` is an integer.
The trace `tr:F_q -> F_2` defines `chi_k(z)=(-1)^tr(kz)`.
The prime-field coordinate model, including a trace-dual basis if needed, is
computed by ordinary finite-field linear algebra.

**D-IG4-INCIDENCE.** Set `v=q^2+q+1`. The point set is `P^2(F_q)` and the
line set is its projective dual. The `v x v` real matrix `B` has row a line,
column a point, and entry one exactly at incidence. Write `J` for the rectangular
all-ones map between these two equal-size spaces, and `1` for the identity.
Use `c=(q+1-sqrt(q))/v` and `R=(B-cJ)/sqrt(q)`.

**D-IG4-CURVE.** The classical input is a dense coefficient list for
`h in F_q[X]`, of degree at most `d<q`, together with the field representation.
Its smooth affine graph `y=h(x)` has rational point set
`S={(x,h(x),1):x in F_q}`, embedded in the projective plane.
This is the affine part; points at infinity of its projective closure are
deliberately excluded from `S`. Let `r_l=|S intersect l|` and `kappa=qc`.
The output task is one line with total-variation error at most `epsilon` from
`pi(l)=(r_l-kappa)^2/q^2`. Multiplicities are not counted in `r_l`.

**D-IG4-RESOURCES.** Let `T_h,W_h` be the gate count and workspace of a clean
reversible evaluation `|x>|0> -> |x>|h(x)>`; they include the supplied classical
coefficients and are not oracle unit costs. Let `M_q(d)` bound multiplication
of degree-`d` polynomials over `F_q` in field operations. Let `T_F(m,epsilon)`
cover finite-field arithmetic, basis changes, and constant-size rotation
synthesis in the explicit implementation below. It is polynomial in
`m+log(1/epsilon)`. Let `T_h,classical` count field operations for classical
evaluation of `h`. Classical field operations also incur their bit costs.

**D-IG4-SPREAD.** For the extension in section 6 only, let `G=F_2^e` and let
`L_a:G -> G`, indexed by `a in G`, be binary linear maps such that
`L_a-L_b` is invertible whenever `a!=b`. Affine lines have equations
`y=L_a x+b`, together with vertical lines; adjoining their points at infinity
gives a translation plane. This synthetic plane is an audit extension, not a
claim that every such plane is an algebraic projective plane over a field.

## 2. Derive the unitary before choosing an implementation

**2.1 ASSUME:** D-IG4-INCIDENCE. **PROVE:** `BB^T=q1+J`.
Every line contains `q+1` points; two distinct lines share exactly one point.
Thus the diagonal entries of `BB^T` are `q+1` and the off-diagonal entries one.
The identical point-pair count gives `B^TB=q1+J`.

**2.2 PROVE:** `R` is orthogonal, with no postselection.
All row and column sums of `B` are `q+1`, and `JJ^T=vJ`. Therefore

```
RR^T = 1 + [1-2c(q+1)+vc^2]J/q = 1.
```

The bracket vanishes for the value of `c` in D-IG4-INCIDENCE. Equivalently,
`B` has singular value `q+1` on the uniform line and `sqrt(q)` on its
orthogonal complement, and `R` sends normalized uniform points to normalized
uniform lines. The correction is essential: `(B-(q+1)J/v)/sqrt(q)` annihilates
the uniform vector and is only a partial isometry.

**2.3 Actual quantum procedure.** Prepare `2m` Hadamards on `x`, evaluate
`h(x)` reversibly into a second field register, and tag the affine chart.
The first register is the actual point coordinate, so no hidden parameter
register needs to be erased. This prepares

```
|S> = q^(-1/2) sum_x |x,h(x),1>.
```

Apply the explicit implementation of `R` in section 4, then measure the line.
The amplitude is `(r_l-kappa)/q`; hence the output is D-IG4-CURVE's `pi`.
This is destructive incidence interference, with both positive and negative
amplitudes. The argument does not assume free fusion of positive histories.

**2.4 Intrinsic content and limitation.** The input describes an honest affine
algebraic curve, and the output is an actual projective line. The distribution
depends only on its rational point set and point-line incidence. It emphasizes
intersection-count deviations, but it is a deliberately chosen sampling task;
it is not a point count, an intersection-multiplicity certificate, or the
uniform distribution on tangent lines. No claim is made that it solves these.

## 3. The apparent access advantage and its first resource test

With an efficient implementation of `R`, the circuit resource equation is

```
T_quantum = T_h + T_F(m,epsilon),
W_quantum = W_h + O(m) + workspace for arithmetic and synthesis.
```

Approximate `R` in operator norm to `O(epsilon)`; the final line law then has
total-variation error `O(epsilon)`. There is no rare heralding event in this
implemented algorithm. For dense coefficients, Horner evaluation costs `O(d)`
field multiplications before reversible-computation overhead is included.

Merely having an incidence oracle gives a weaker implementation. Uniform
point-to-incident-line and line-to-incident-point isometries overlap as
`B/(q+1)`. On the uniform-vector complement their singular value is
`sqrt(q)/(q+1)`. Alternating their reflections has a rotation angle of order
`q^(-1/2)` on each associated two-dimensional invariant space.
The usual fixed-angle transfer through those reflections therefore takes
`Theta(sqrt(q))` steps. This is an analysis of that reflection construction,
not a lower bound for every oracle algorithm or every implementation of `R`.

The direct circuit below avoids this cost precisely by using Fourier structure.
Consequently the cheap circuit is already disqualified by D22; counting only
the successful arithmetic implementation while hiding that structure is invalid.

## 4. Exact decomposition: the operation is a Fourier Radon transform

Label affine points `(x,y)`, nonvertical lines `(a,b):y=ax+b`, vertical lines
`V_b:x=b`, and the line at infinity. Label their infinity points by their
slopes `a` and by the vertical direction. All arithmetic here is in D-IG4-FIELD.

**4.1 Nonzero characters.** Define the point vectors
`|x;k>=q^(-1/2)sum_y chi_k(y)|x,y>` and corresponding line vectors
`|a;k>=q^(-1/2)sum_b chi_k(b)|a,b>`. For `k!=0`, direct substitution gives

```
R |x;k> = q^(-1/2) sum_a chi_k(ax) |a;k>.
```

The all-ones correction vanishes because a nontrivial character sums to zero.
The right side is exactly an additive finite-field Fourier transform in `x`,
with the nonzero field multiplication by `k` absorbed into its output labels.
The intercept basis changes are additive Fourier transforms as well. In binary
coordinates these are Hadamards and reversible linear maps; changing their gate
names does not change the problem-level mechanism.

**4.2 Zero characters and boundary.** Let `X_x` be uniform in affine `y`
at fixed `x`, and `A_a` uniform in line intercept `b` at fixed slope `a`.
On sum-zero combinations, the following maps hold exactly:

```
sum_x u_x X_x -> sum_x u_x V_x,             sum_x u_x=0;
sum_a w_a P_infinity,a -> sum_a w_a A_a,    sum_a w_a=0.
```

They are relabelings. It remains to handle three uniform vectors:
`X=q^(-1/2)sum_x X_x`, `P=q^(-1/2)sum_a P_infinity,a`, and the vertical
infinity point. The corresponding output basis is the uniform `A`, uniform
vertical lines, and the line at infinity. In these bases,

```
B_3 = [[q,sqrt(q),0], [sqrt(q),0,sqrt(q)], [0,sqrt(q),1]],
u   = (q,sqrt(q),1)^T,
R_3 = (B_3-c uu^T)/sqrt(q).
```

`R_3` is a real orthogonal `3 x 3` matrix. Fourier zero labels isolate these
uniform sectors; chart tags implement the relabelings; a constant number of
two-level rotations implements `R_3` to the requested accuracy. This accounts
for every dimension, including the often-discarded zero-frequency sector.
The decomposition establishes the resource equation and the D22 failure.

## 5. Matched classical attack: a constant-success exact sampler

Enumerating all `v` lines is an inappropriate comparator for one output sample.
The following algorithm uses the same dense coefficients and outputs the same
line distribution. Its only nontrivial geometric query is a univariate root count.

**5.1 Intersection moment identities.** Counting incidences and ordered point
pairs in D-IG4-CURVE gives

```
sum_l r_l = q(q+1),
sum_l r_l(r_l-1) = q(q-1),
sum_l r_l^2 = 2q^2,
sum_l (r_l-kappa)^2 = q^2.
```

The last identity also follows from 2.2. Coincident input points are handled
separately, not declared to determine a unique line.

**5.2 Sample the square-count distribution.** With probability `(q-1)/(2q)`,
sample an ordered pair of distinct uniform points of `S` and output their line.
With probability `(q+1)/(2q)`, sample one uniform point of `S` and one uniform
line through that point. The resulting probability for line `l` is

```
[(q-1)/(2q)] r_l(r_l-1)/[q(q-1)]
 + [(q+1)/(2q)] r_l/[q(q+1)] = r_l^2/(2q^2).
```

All these sampling and line-construction operations use polynomial-time field
arithmetic and at most two evaluations of `h`. A line through one point is
chosen by a uniform slope in `F_q` or the vertical direction.

**5.3 Rejection envelope.** Put `Z=2q^2+v kappa^2`. Mix the preceding law with
uniform projective lines, using mixture weights `2q^2/Z` and `v kappa^2/Z`.
The proposal probability is `Q(l)=(r_l^2+kappa^2)/Z`. Accept the line with
probability

```
A(l) = (r_l-kappa)^2/(r_l^2+kappa^2).
```

Both quantities in the squared difference are nonnegative, so `0<=A(l)<=1`.
The accepted distribution is exactly `pi`, with acceptance probability

```
P_accept = q^2/Z = 1/[2+v c^2] >= 1/3.
```

The bound uses `(q+1-sqrt(q))^2<=v`. Thus there are at most three proposals
on average, without a degree-dependent rejection penalty. Since `sqrt(q)` is
integer here, the sampling probabilities are rational of polynomial bit length;
integer rejection implements them exactly with polynomial expected bit work.

**5.4 Count the intersections.** For a nonvertical line form
`g(X)=h(X)-aX-b`. If `g=0`, return `q`; otherwise compute

```
r_l = degree gcd(g(X), X^q-X).
```

Repeated roots of `g` do not cause an error because `X^q-X` is squarefree.
Compute `X^q mod g` by binary modular powering, not by writing a degree-`q`
polynomial. Vertical lines have count one; the line at infinity has count zero.
Using fast multiplication and gcd, a sufficient resource equation is

```
E[T_classical] = O(T_h,classical + M_q(d)(log q + log d))
```

field operations up to ordinary gcd logarithmic factors, plus polynomial-bit
sampling work. This explicit attack is already near-linear in `d` up to logs.
It is an upper bound, not an assertion that an exhaustive 2026 best-algorithm
survey has proved optimality. No time or space separation from it is established;
possible logarithmic differences require an honest common bit-cost model.

## 6. A second attempted mechanism: nonlinear translation-plane incidence

The suggested escape was to replace field multiplication by more general
coordinates, retaining the exact design identity while breaking the Fourier
implementation. D-IG4-SPREAD allows nonlinear dependence of `L_a` on `a`;
it is broader than an associative field or a bilinear semifield product.

For a nonzero intercept character `k in G`, the character block of the same
normalized incidence transform has entries

```
U_k[a,x] = |G|^(-1/2) (-1)^(k dot L_a x)
         = |G|^(-1/2) (-1)^((L_a^T k) dot x).
```

For fixed `k!=0`, the map `a -> L_a^T k` is a permutation: equality for two
different `a,b` would put `k` in the kernel of the invertible transpose
`(L_a-L_b)^T`. Therefore `U_k` is exactly a Walsh Fourier transform followed
by a row permutation. The same boundary decomposition applies.

When that permutation and its inverse are efficiently computable, the entire
operation is once again Fourier plus arithmetic. When inversion is not supplied,
forward evaluation is insufficient to assert clean in-place permutation access;
computing the forward value while retaining `a` does not implement `U_k`.
For a bilinear semifield multiplication, this permutation is binary linear and
its inverse follows by Gaussian elimination, so even nonassociativity adds no
new primitive in that subfamily.
No efficient inversion lemma was found. Applying generic search would violate D22.
Synthetic non-Desarguesian incidence also needs a separate AG justification;
an arbitrary finite plane is not automatically the field-valued point-line
geometry of a projective algebraic plane.

## 7. Targeted novelty check, hardware, and exact unresolved requirements

The formulas and classical sampler above were derived before browsing.
Ma, Li, and Zhao's [Quantum Radon Transform and Its Application,
arXiv:2107.05524](https://arxiv.org/abs/2107.05524), fetched with its PDF, uses
the Fourier-slice mechanism and reversible arithmetic to implement a quantum
Radon transform. Its transform and input/output contract are not asserted to
be identical to ours. The explicit section 4 reduction independently suffices
for D22; no inference from a merely similar title is required.

For polynomial arithmetic, the fetched publisher page of Kedlaya and Umans,
[Fast Polynomial Factorization and Modular Composition,
DOI 10.1137/08073408X](https://doi.org/10.1137/08073408X),
documents fast finite-field polynomial algorithms. Full factorization is stronger
than this task needs; section 5 uses only modular powering and a gcd. Neither
reference is entered in `refs/` by this lane, and no historical originality claim
is made for the orthogonal completion or the rejection identity.

A small optical test is concrete: at `q=4`, the real orthogonal `21 x 21` matrix
`R` acts on 21 path modes of one photon. Prepare equal amplitudes on the four
curve-point modes and measure the output line mode. A generic interferometer
uses at most `21*20/2=210` two-mode eliminations plus phases. This is a useful
normalization check, with an immediate 21-dimensional classical simulation;
it is not an asymptotically cheap heuristic attack meeting the north star.

The exact missing lemma for the second attempt was: uniformly compute, and
cleanly reversibly implement, `a -> L_a^T k` and its inverse in time polynomial
in `log |G|` for a supplied succinct spread family. If supplied, it establishes
the known Fourier implementation and still does not repair novelty. No lemma
about the existing `R` can make its section 4 Fourier equivalence disappear.
A successor must change the actual operation or task and derive a new resource
advantage; merely changing a finite-field coordinate law is insufficient here.

## 8. Bounded numerical audit and handoff

Run `IG4-CHECK-20260905` used inline Python/NumPy with a 60-second timeout and
`OPENBLAS_NUM_THREADS=OMP_NUM_THREADS=MKL_NUM_THREADS=1`. It built the complete
incidence matrices over `F_4` and `F_16`, checked every nonzero character block,
all 64 quadratic coefficient lists over `F_4`, and 32 seeded degree-four lists
over `F_16`. It checked orthogonality, the Born law, both mixture identities,
rejection normalization, and the one-third success bound: **932 demands passed**
in 0.32 seconds. Two deliberately changed expressions were detected: replacing
`c` by `(q+1)/v`, and replacing the two square-count mixture weights by halves.
This exploratory run is not a newly registered campaign checker or a verdict.

Root-facing disposition: retain the exact operation, the Fourier decomposition
including zero modes, and the same-output rejection sampler as a bounded audit.
Do not promote a novel-algorithm row, treat dense matrix enumeration as the
classical comparator, or reopen the discarded positive-fusion/finite-difference
branches. No D22-compliant candidate remains from this bounded construction.
