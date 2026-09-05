# Independent verdict: coded Waring-packet synchronization

2026-09-05. Reviewed the completed `scouting/waring-coded-fusion.md` and
independently checked its guard model, phases, norms, seed cost, recurrence,
and rank dependence. The separate terminal scalar lower-bound proposal is
not adjudicated here. Only this verdict is written by the reviewer.

**VERDICT: PASS for the scoped mathematical/resource statements, with the
minor implementation qualifications below.** The logarithmic guard reduction
is real and optimal in its declared model. It is not global quantum optimality
or a polynomial-in-rank algorithm. Under D22's explicit exclusion of new
compositions of established algorithms, the displayed comparison-only
construction does not qualify as a new mechanism: §4 gives the operational
reduction, independently of the rank-two Bell-fusion argument. Historical
priority of the separating schedule remains unverified. A same-output
classical separation remains HOLD until its own proof is adjudicated.

## 1. Synchronization, slot counts, and phases

1.1 Fix two component permutations `pi_A,pi_B`. The selected labels in
edge `S` are `pi_A(S)` and `pi_B(S^c)`. Each input contributes a set of
distinct labels, and all `r` selected labels are distinct exactly when
`pi_A(S)=pi_B(S)`. Independence of the component vectors makes this
equivalent to a nonzero alternating projection.

1.2 Consequently the relative permutation `tau=pi_B^(-1)pi_A` must preserve
every selected subset. Giving rows distinct binary signatures forces `tau`
to fix every row, so only pairs `pi_A=pi_B` survive. This is a pointwise
statement about labels, not a probability or approximate-comparison claim.

1.3 Each of the `b=ceil(log_2 r)` edges selects exactly one slot from each
row, choosing its origin from packet A or B. The total consumed from a
merged row is therefore exactly `b`, even though its split between A and B
varies. Distinct physical slots make the edge projectors commute. For input
degrees `m,n>b`, every merged row has `ell=m+n-b`, and this exceeds both
input degrees. The unequal-size formula has no missing degree correction.

1.4 With row-ordered edge registers, a surviving permutation gives

`sgn(pi) sqrt(det G/r!) omega`

at every edge. Thus the packet sign is precisely
`sigma_A+sigma_B+b mod 2`. There is no additional hidden component-dependent
phase. Moving all A registers ahead of all B registers contributes only
the stated constant crossing sign for each subset, hence an irrelevant
overall phase. The discarded `omega^tensor b` factors from the output.

1.5 With `G_m=G^(circ m)`, expanding the permutation-vector Gram matrix
gives `N_1(m)=r! det G_m`, `N_0(m)=r! per G_m`. The factors from all
edges and both input norms therefore give exactly

`p_(m,n)=(det G/r!)^b N_(sigma_out)(m+n-b)`
`                         /[N_(sigma_A)(m)N_(sigma_B)(n)]`.

All determinant/permanent and `r!` factors in equations (3), (9), and (10)
are correct. This also checks normalization for complex Gram matrices.

## 2. What the guard-count lower bound proves

2.1 With `t` subset tests, rows have at most `2^t` membership signatures.
If two rows share a signature, their transposition preserves all tests.
For every `pi_B`, taking `pi_A` to differ by that transposition gives a
nonmatching surviving pair. Hence exact synchronization in this model
requires `t>=ceil(log_2 r)`, and binary signatures attain it.

2.2 There is no hidden interference cancellation rescuing an undersized
guard family in the stated regime. When `t<b`, the assumptions `m,n>b`
leave an unmeasured A and B slot in every row. Distinct input permutation
pairs then leave distinct component words. Those words are linearly
independent because the `u_a` are independent. Their nonzero coefficients
cannot cancel the unwanted pairs. An extra row-symmetrization or another
measurement would change the guard model and is not covered by this bound.

2.3 More generally, the number of relative permutations preserving a family
is the product of factorials of its signature-class sizes. Multiplying by
`r!` gives the surviving ordered input-pair count. This independently yields
24 and 120 survivors for the full rank-four and rank-five codes, and 96
and 240 after their last edge is removed.

This is a sharp theorem for complementary row-selection all-distinct tests.
It says nothing about arbitrary collective instruments, approximation,
additional outcome information, other seed resources, or classical cost.

## 3. Seed and repeated-growth resources

3.1 The seed has edge norm `det G/r!` and alternating-packet norm
`r! det G_(k-1)`. Thus

`p_0=|prod_a c_a|^2 det G det G_(k-1)=det_positive(rho_1)`.

The one-slot reduced state has rank `r`, with nonzero eigenvalues summing
to one. Arithmetic--geometric means gives `p_0<=r^(-r)` and expected
seed cost `r/p_0>=r^(r+1)`. This is a universal ceiling for this particular
antisymmetric seed, not for all possible component-packet preparation.
The normalized-cancellation qualification is necessary and correctly stated.

3.2 Each merge adds degrees and subtracts `b`, so a tree with `L` seeds
has degree `b+(k-1-b)L`. Its sign is `L+(L-1)b mod 2`. These are
independent of tree shape. Equal-size doubling gives exactly equation (14),
and strictly growing seeds require `k>=b+2`. Discarding surplus slots does
not supply an exact pure-packet size conversion; the memo correctly keeps
the attainable-degree restriction.

3.3 The known conditioning promise supplies the claimed probability floor.
From `G>=eta I` and unit diagonal,

`G_m=G circ G_(m-1)>=eta(I circ G_(m-1))=eta I`.

The permutation Gram matrix is a principal submatrix of `G_m^tensor r`,
so its least eigenvalue is at least `eta^r`. The sign vector has squared
norm `r!`, proving `N_sigma(m)>=r! eta^r`; the triangle bound gives
`N_sigma(m)<=(r!)^2`. Substitution yields exactly

`f_*=eta^(r(b+1))/(r!)^(b+3)`.

When `b` is odd, all packets are alternating and Hadamard's determinant
bound improves this to `eta^(r(b+1))/(r!)^(b+1)`, as stated.

3.4 Offline restart accounting gives
`C_(j+1)=2C_j/p_(m_j,m_j)` and the known bound
`C_j<=(r/p_*)(2/f_*)^j`. Actual Gram/permanent values are not needed to
run or cap the algorithm. The alternation-count recurrence is also valid
when each fusion attempt performs all `b` guards. To check its upper bound,

`r A_(j+1)/C_(j+1)=r A_j/C_j+br/(2C_j)`.

Since `C_j>=2^j C_0>=2^j r`, summing gives `A_j<=(b+1)C_j/r`.
Early abort inside a fusion attempt can only reduce that conservative cost.

3.5 Orthogonal equal-weight components attain the seed ceiling and have
fusion probability `(r!)^(-(b+1))`. The table values 28,311,552 at rank
four and 6,480,000,000,000 at rank five are correct. The degree-growth
exponent is `1+(b+1)log_2(r!)=Theta(r(log r)^2)`, versus
`Theta(r^2 log r)` for the earlier `r-1` guards. This is a real improvement
between the two constructions, with severe rank costs still present.

## 4. A direct operational comparison with published algorithms

4.1 The higher-rank primitive has a specific prior algorithm, independently
of Bell fusion. [Chefles--Andersson--Jex, §V, equations (5.10)--(5.14)](https://arxiv.org/pdf/quant-ph/0402125)
gives universal unambiguous detection that all `r` input states are different
by the antisymmetric projector, with success `det(Gram)/r!`. Under the
present independent-component promise it is exactly the guard in equation (4).
The usual retained projector outcome has the same Kraus map, including on
inputs entangled with untouched registers by linearity.
Moreover, because the selected edge registers are discarded, their
postselected spectator state depends only on the POVM effect `P_anti`;
the comparison device need not expose any particular edge-output encoding.

4.2 Apply `b` copies of that instrument to the classically specified disjoint
register groups, require all accepts, discard their output edges, and regroup
the untouched slots. This gives precisely the retained-packet map (9), not just its
acceptance distribution. Its gate calls are `b C_alt(r,q)`, and its success
is exactly (10). There is no added normalization, variance, inverse-state
oracle, or asymptotic loss in this reduction. The seed itself is the same
antisymmetric comparison/Schmidt-projection operation on the source copies.

4.3 The paper does not claim the present separating schedule or Waring
source-conversion theorem. Those may have independent mathematical interest,
and historical priority of that schedule has not been certified here.
Nevertheless the displayed *quantum mechanism* is a fixed parallel
composition of the existing comparison algorithm, with a binary classical
routing rule. Under the user's express D22 exclusion of new applications
or compositions of established algorithms, it does not qualify. This is
an operational, resource-preserving reduction of the whole displayed map;
it is not generic universal-gate decomposability or an extrapolation from
rank two to every higher-rank protocol.

Accordingly, retain the coding improvement while treating a D22-qualification
claim for this comparison-only construction as REFUTED. A future protocol
using further coherent operations, different source resources, or a genuinely
different mechanism would need its own audit. A scalar separation for the
current construction would be a separate valuable result, not an originality
certificate.

## 5. The traced-mixture symmetrization comparator

This section audits the root's separate proposed comparator. It assumes an
already prepared balanced mixture
`rho_m=(1/r)sum_a |u_a^m><u_a^m|`; this is not the coherent packet.

5.1 Apply the full symmetric projector `P_(2m)` to two independent `rho_m`
blocks. Same-component terms survive exactly with total probability `1/r`.
For different components with overlap magnitude `a`, the acceptance is

`q_m(a)=binom(2m,m)^(-1)sum_(j=0)^m binom(m,j)^2 a^(2j)`
` <=(2m+1)((1+a)/2)^(2m)`.

The equality follows by counting how many of the `m` positions cross between
the two input groups in a symmetrizing permutation. For the bound, use the
square of the binomial sum in the numerator and
`binom(2m,m)>=4^m/(2m+1)`. If `1-a^2>=g_*`, it is at most
`(2m+1)exp(-g_*m/2)`. A known `G>=eta I` also supplies a pairwise gap,
since every two-by-two principal block gives `a<=1-eta`.

5.2 The accepted unnormalized output is exactly `rho_(2m)/r+B`, with
`B>=0` and `Tr B<=(r-1)q_max/r`. Its success is at least `1/r`; after
conditioning, trace distance to `rho_(2m)` is at most `(r-1)q_max`.
This is an explicit same-quantum-output comparison for balanced mixtures.
Symmetric projection is an established operation with an efficient network;
see [Barenco et al.](https://arxiv.org/abs/quant-ph/9604028).
The displayed conditional-mixture bound is derived here, not attributed
wholesale to that paper.

5.3 Approximate input must be charged. If
`D(rho_tilde_m,rho_m)<=delta_m`, the input product differs by at most
`2delta_m`. Success is at least `1/r-2delta_m`. For
`delta_m<=1/(4r)`, a safe conditional-output bound is

`delta_(2m)<=4r delta_m+(r-1)q_max`.

It follows by trace-norm contraction for the accepted CP map and normalization
by the ideal success, which is at least `1/r`. Repeated doubling therefore
needs an explicit amplified-error budget. A constant-error approximate seed
cannot simply be assumed to stay equally accurate after arbitrarily many
conditioned rounds. Choosing larger initial `m` can suppress the cross terms,
but the cost of preparing that initial balanced mixture remains charged.

5.4 Nothing in this comparison recreates the coherent permutation signs,
the pure packet, or its full joint-row output. It neither supplies a cheap
seed nor removes the specific seed lower bound in §3. It is relevant only
when the ultimate requested output has already been reduced to a mixture.
The independent terminal scalar ensemble requires separate verification.

## 6. Minor qualifications and decisions

**C1 — MINOR. Location:** §5, optional source-circuit resource ledger.
**FIX DEMAND:** Add the supplied source-preparation workspace to the live
qubit bound when such a circuit is included. **SURVIVING STATEMENT:** The
displayed recursion-space bound is valid for the primary fresh-copy model;
it does not bound an arbitrary optional source implementation's workspace.

**C2 — MINOR. Location:** §5, finite precision and the execution cap.
**FIX DEMAND:** State that the exact packet formulas and three-times-cap
success bound concern ideal projectors. Give an output-accuracy parameter
for finite-gate synthesis and leave a constant probability margin, e.g.
a six-times ideal cap with separately budgeted compilation error.
**SURVIVING STATEMENT:** Known bounds permit controlled finite-precision
implementation; exact ideal identities do not imply exact synthesized output.

Accept the synchronization, phase, degree, normalization, restricted guard
optimality, seed lower bound, and restart formulas for mathematical retention.
Accept the quantitative improvement over the older guards at its stated
scope. The displayed D22-qualification claim is refuted by §4's independent
higher-rank comparison reduction; historical priority of the coding result
remains unverified. HOLD the terminal classical separation until its actual
proof is adjudicated. Neither this verdict nor the guard lower bound claims
global quantum optimality or impossibility of other higher-rank mechanisms.

Independent bounded computation used one BLAS thread and a 60-second timeout:
118 checks passed for subset stabilizers through rank seven, slot counts,
complex permutation Gram norms, determinant/permanent formulas, unequal-size
phase/probability identities, uniform probability floors, and the mixture
binomial bound. These were unregistered scratch checks; the root's separate
registered checker and terminal lower-bound proof were not substituted for
this audit. Primary browsing was limited to the concrete comparison and
symmetrization mechanisms cited above.

**VERDICT: PASS for the scoped mathematics; no D22-compliant mechanism or
adjudicated scalar separation is established by this memo.**
