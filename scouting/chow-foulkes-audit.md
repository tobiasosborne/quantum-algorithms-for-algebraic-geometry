# Chow/Foulkes support, normalization, and failed-source recovery

2026-09-05. Independent bounded audit of the proposed construction. Ordinary
tensor Hilbert norms are used, explicitly departing from C1. Definitions below
are local pending a root merge. Claims remain unratcheted; no new quantum
algorithm or historical novelty is asserted.

The support identity is correct for every copy count, not only `t=m+1`.
The normalized row/column compression has an exponentially small positive
eigenvalue when `t=m+1`, witnessed by a genuine orthogonally split form.
Its Rayleigh quotient is exactly a classical permutation-table probability.
A proposed repair by restoring the same unknown Chow state after failure is
also obstructed: no nonzero exact universal heralded recovery of that failure
instrument exists without fresh copies or a factor-dependent oracle. This is
a scoped recovery theorem, not an impossibility result for Chow algorithms.

## 1. The precise support and adjoint map

Let `V` be finite-dimensional over `C`, with its standard Hermitian metric.
Arrange `mt` tensor slots in `t` rows and `m` columns. Let `R` symmetrize
each row of length `m`, and let `T` symmetrize the `t` rows as whole blocks.
These commute, and `P_row=RT` is the orthogonal projector onto
`Sym^t(Sym^m V)`. Let

`P_col=tensor_(j=1)^m P_(Sym^t V),j`.

Let `Ch_m(V)` be the cone of products of `m` linear forms, represented by
symmetric tensors, and set
`S_(m,t)=span{f^tensor t:0!=f in Ch_m(V)}`. Norming these vectors does not
change their span. Define the positive contraction

`A_(m,t)=P_row P_col P_row`.

### Support statement

ASSUME `m,t>=1`. PROVE

`S_(m,t)=range(P_row P_col)=support(A_(m,t))`.

1.1 Pure powers span each column's `Sym^t V`. Thus `range P_col` is spanned
by tensors `tensor_j v_j^tensor t`, with the slots arranged by columns.

1.2 Regrouping such a tensor into rows gives `t` identical copies of
`v_1 tensor ... tensor v_m`. Applying `R` gives
`[Sym_m(v_1 tensor ... tensor v_m)]^tensor t`. Whole-row symmetrization
then has no effect. This proves both containments in the range identity,
with no factorial prefactor beyond the orthogonal symmetrizer itself.

1.3 The identity `range(L)=support(LL^dag)` with `L=P_row P_col` gives
the support statement. It holds whether or not the map has full rank.

1.4 Simultaneously permuting the columns is a permutation inside every row,
so it is absorbed by `P_row`. It commutes with `P_col`. Consequently adding
outer column symmetrization changes neither `P_row P_col` nor its image.
On the row space, the forward map is

`F=P_col|_(range P_row): Sym^t(Sym^m V) -> Sym^m(Sym^t V)`,

and its Hermitian adjoint has image `S_(m,t)`. These are the normalized
tensor-space Foulkes--Howe map and its adjoint. The classical kernel/Chow-ideal
identification is explicitly stated in
[Cheung--Ikenmeyer--Mkrtchyan, Remark 7](https://arxiv.org/pdf/1509.03944)
and [Guan, §2.5, Proposition 2.5.2](https://oaktrust.library.tamu.edu/server/api/core/bitstreams/7b57f5b5-d567-4d4a-b326-3a470d79925b/content).
These references establish the algebraic map and kernel; the physical
normalizations and spectral estimates here are separately derived.

1.5 The choice `t=m+1` is motivated by defining equations, rather than by
the support identity. Brill's equations of that degree have the Chow
variety as their zero set; see Guan §2.4, Theorem 2.4.5 in the same primary
source. No maximal-rank Foulkes conjecture is assumed.

## 2. An exact classical law for the orthogonal split form

ASSUME `dim V>=m` and use orthonormal vectors `e_1,...,e_m`. The normalized
split-form state is

`|f>=(m!)^(-1/2) sum_(sigma in S_m) |sigma(1),...,sigma(m)>`.

Let `Omega` be the set of `t x m` tables whose every row is a permutation
of `[m]`. Then `|f>^tensor t` is the uniform positive superposition over
`Omega`, with `|Omega|=(m!)^t`.

2.1 The column group is `G=(S_t)^m`, of order `(t!)^m`. For a column shuffle
`gamma`, orthogonality of the computational words gives exactly

`<f^t,U_gamma f^t>=|Omega intersect gamma Omega|/|Omega|`.

Averaging over `G` proves

`p_(m,t):=<f^t,P_col f^t>`
` =Pr[gamma X has every row a permutation]`,

where `X` has independent uniform permutation rows and the column shuffles
are independent uniform permutations. There is no extra square, inverse
group order, or postselection factor. Coherence is already accounted for by
the intersection count in each matrix element.

2.2 In the first output row, let `J_j in [t]` be the source row selected
by column `j`. The `J_j` are independent uniform indices. For fixed `J`,
let `s_i=|{j:J_j=i}|`. Entries drawn from the same original row are sampled
without replacement, while different original rows are independent.
Each prescribed permutation output therefore has probability
`1/prod_i (m)_(s_i)`, where `(m)_s=m(m-1)...(m-s+1)`. There are `m!`
such outputs, giving the exact conditional law

`Pr[first output row is a permutation | J]=m!/prod_i (m)_(s_i)`.

2.3 Hence the all-row probability is bounded by the expectation of that
first-row expression. The two probabilities are generally different; the
first-row expression must not be reported as equality for `p_(m,t)`.
Classically, one trial of the all-row experiment can be sampled using
ordinary permutation generation and table checks in polynomial time in `mt`.
This is an easy counterexample family, not a classical-hardness witness.

## 3. Exponentially small positive spectrum at `t=m+1`

3.1 Set `b=floor(m/2)+1`. On the event `max_i s_i<=m/2`,
`(m)_(s_i)>=(m/2)^(s_i)`, and therefore the first-row probability is at
most `m!(2/m)^m`. By a union bound over a source row and `b` chosen columns,

`Pr[max_i s_i>m/2] <= t binom(m,b) t^(-b)`.

The earlier `ceil(m/2)` threshold is also an upper bound, but is looser
when `m` is even. The strict-failure threshold above matches the event exactly.

3.2 At `t=m+1` this proves

`0<p_(m,m+1)<=B_m`,
`B_m=m!(2/m)^m+(m+1)binom(m,b)(m+1)^(-b)`.

The right side can of course be capped at one. Stirling's formula gives
the first term `O(sqrt(m)(2/e)^m)`; the second is
`exp(-Omega(m log m))`. Thus `B_m=exp(-Omega(m))`.

3.3 The vector `f^t` lies in `S_(m,t)=support(A_(m,t))`, by §1. It is
also in the row space, so

`<f^t,A_(m,t) f^t>=<f^t,P_col f^t>=p_(m,t)`.

It has no component in the operator kernel. The variational principle on
the positive support therefore yields

`lambda_min_positive(A_(m,m+1)) <= B_m`.

This is a genuine small-positive-eigenvalue bound, not an artifact from
testing a vector with a large kernel component. The witness need not itself
be an eigenvector. Its positivity also follows directly from the nonzero
overlap with the column tensor `tensor_j e_j^tensor t`.

3.4 A scoped consequence concerns generic bounded-polynomial support filters.
When the row space also contains a zero eigenvalue, a polynomial bounded by
one on `[0,1]`, with `|p(0)|<=epsilon` and
`|p(lambda)-1|<=epsilon` at every positive eigenvalue, needs degree at least

`sqrt((1-2epsilon)/(2 lambda_min_positive))` for `epsilon<1/2`.

This follows from the mean value theorem and Markov's derivative bound on
`[0,1]`. It is exponential in `m` for the family above. For `m>=3` and
`dim V>=m`, the Chow variety is proper and the degree-`m+1` defining
equations give such a kernel. This conclusion is about this normalized
operator and bounded-polynomial filtering, not every possible Chow tester.
An arbitrary rescaling cannot help for free: `A_(m,t)` already has eigenvalue
one on every `v^tensor mt`.

## 4. A concrete obstruction to exact failed-source recovery

The following addresses the specific attempted repair: after a failed column
projection, restore the same unknown `f^tensor t` and retry, using only the
failed registers, fixed ancillas, and a state-independent recovery circuit.
The recovery may itself be heralded and may have input-dependent success.

### Irreducible-family recovery lemma

ASSUME a finite-dimensional Hilbert space, an irreducible projective family
`Y` spanning a linear space `S`, and a failure instrument with Kraus maps
`K_beta`. Suppose some nonzero `x_0 in Y` satisfies `K_beta x_0=0` for every
failure Kraus map. PROVE: no fixed CP recovery of those failure outputs can
have nonzero accepted probability on `Y` while returning the original pure
ray exactly whenever it accepts, for every input in `Y`.

4.1 Combine failure and accepted recovery into one trace-nonincreasing CP
map. It has finite Kraus operators `L_a` on the original input space;
every `L_a` annihilates `x_0`. Keeping the failure record, using fixed
ancillas, or adapting finitely many recovery steps does not change this fact.

4.2 Exact pure output requires `L_a x` to be proportional to `x` for every
`x in Y` and every `a`; a zero vector is permitted. This follows because
a positive sum of rank-one operators has rank one only when its nonzero
vectors are collinear. Since `Y` spans `S`, each `L_a` preserves `S`.

4.3 A finite-dimensional endomorphism has finitely many eigenvalues. Its
eigenvectors lie in the finite union of its projective eigenspaces. Since
`Y` is irreducible and lies in that union, it lies in one eigenspace.
Spanning then gives `L_a|_S=c_a I_S`.

4.4 But `L_a x_0=0` and `x_0!=0`, so `c_a=0`. Every accepted Kraus operator
vanishes on `S`. The total accepted recovery probability is therefore zero
for every input in `Y`, proving the claimed obstruction.

### Application to the column/Foulkes failure

4.5 The projectivized Chow variety is irreducible, being the image of a
product of projective spaces under multiplication. Its `t`th Veronese
image `Y={[f^tensor t]:f split}` is irreducible and spans `S_(m,t)`.
For the actual column measurement, `K_fail=I-P_col` annihilates every
`v^tensor mt`, which is a member of this family. The lemma applies.

4.6 The same conclusion holds for any source-space failure instrument with
effect `I-A_(m,t)` on the row space, including its Lueders realization.
That effect annihilates `v^tensor mt`, so positivity forces every failure
Kraus operator to annihilate it. The orthogonal split form has nonzero
failure probability when `m,t>=2`, so the result is not merely a statement
about a branch that never happens.

4.7 This rules out even probabilistic exact universal recovery of the same
input after that failure, with no positive lower success bound assumed.
It does not rule out approximate recovery, consuming additional copies,
restoring fewer copies, changing the target state, or using a circuit that
depends on supplied factors. If the factors are supplied classically,
preparing the input again is a different access model whose factorization
and preparation costs must be charged. Nor does the lemma forbid a different
Chow measurement whose failure branch already vanishes on the entire variety.

The obstruction uses the actual dark pure-power states and the irreducible
factor family. It is more specific than the observation that one example's
posterior changes or that the symmetrizer has low acceptance.

## 5. Finite checks and disposition

An exact finite recomputation grouped input permutation tables by their
column histograms. If an orbit `O` has `n_O` valid input tables, its
contribution is `n_O^2/(|Omega||O|)`, with
`|O|=prod_j t!/prod_v count_(j,v)!`. This independently checks the averaging
normalization using integer counts and rational arithmetic.

| `m,t` | All-row probability `p_(m,t)` | First-row probability |
|---|---|---|
| 2,3 | 1/2 | 2/3 |
| 2,6 | 7/64 | 7/12 |
| 3,2 | 1/2 | 1/2 |
| 3,4 | 79/1296 | 1/3 |
| 3,5 | 35/1944 | 23/75 |

For `m=2` the exact formula is `(t+1)/2^t`: the orbit with `s` rows of one
orientation contains `binom(t,s)` valid tables and has size `binom(t,s)^2`.
For the specified `t=m+1`, the rigorous bound `B_m` is approximately
`0.3728931, 0.02432903, 7.420706e-5, 4.896981e-10` at `m=10,20,40,80`.
These are finite checks, not a spectral lower-bound computation or a
classical separation. The run was bounded by 60 seconds with one BLAS thread;
all exact consistency checks passed. No registered checker was written here.

Proposed dispositions: retain the all-`t` support identity as classical
Foulkes--Howe structure with the explicitly normalized quantum realization;
retain the exact probability identity, small-positive-gap upper bound, and
scoped exact-recovery obstruction as SKETCH pending independent review.
Refute a uniform polynomial-gap claim for this row/column compression and
an exact free-retry repair under the stated access. No alternative successful
normalization-free instrument or qualifying D22 algorithm has been constructed.
