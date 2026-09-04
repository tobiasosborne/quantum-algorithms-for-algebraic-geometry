# Residue round 3: canonical trace, exact cancellation, and physical normalization

2026-09-05. Two explicit operations survive as mathematical constructions: a
residue channel for monomial covers implemented by reversible integer division,
and a normalized family of local-residue samples implemented by photon counting.
Their classical and equivalence audits do not produce a qualifying new algorithm.
An intervening two-root example proves an encoding-specific information bound;
it does not prove intrinsic hardness of residues or degeneration of local duality.

The coefficient spaces and finite branch registers use their stated Hermitian
metrics. Section 3 specifically uses the ordinary Bergman metric on the unit disk,
departing from C1; section 4 returns to the Fock convention. Variable counts are
local to these disjoint settings rather than the frozen projective index C2.
No claim status is assigned. No adjoint quotient-multiplication oracle or positive
interpretation of a bilinear residue pairing is assumed.

## 1. The first proposal: put the Jacobian into a unitary change of variables

The intended operation was to transport a function through a finite polynomial
map, preserving all inverse branches coherently, and then merge the branches to
obtain a residue. The Jacobian can indeed be absorbed into an isometry, but the
formula depends crucially on whether the underlying volume is real or complex.

### 1.1 Four access models with different normalizations

At a regular fibre with `D` points `x_a`, let `J_a` be the nonzero Jacobian
determinants entering the algebraic residue

`L(g)=sum_(a=1)^D g(x_a)/J_a`.

Suppose a register has unnormalized amplitudes `b_a`, and the desired linear
functional is `L(g)=sum_a c_a b_a`. A physical rank-one contraction realizing it
universally is normalized by `N_c=(sum_a |c_a|^2)^(1/2)`. On the normalized
input ket its acceptance probability is

`|L(g)|^2 / [N_c^2 sum_a |b_a|^2]`.

The relevant choices are:

| Amplitudes before state normalization | Coefficients `c_a` | `N_c^2` |
|---|---|---|
| Unweighted evaluations `g(x_a)` | `1/J_a` | `sum_a |J_a|^(-2)` |
| Real half-densities `g(x_a)/sqrt(|J_a|)` | `sqrt(|J_a|)/J_a` | `sum_a |J_a|^(-1)` |
| Complex-volume half-densities `g(x_a)/|J_a|` | `|J_a|/J_a` | `D` |
| Canonical-form transport `g(x_a)/J_a` | `1` | `D` |

These rows are different input encodings. Moving between them is a charged
operation and their source norms cannot be suppressed. The second row is for
a real map with real-volume Jacobian; the last two use a holomorphic map with
standard real `2n`-dimensional volume and complex Jacobian `J_a`.

### 1.2 The exact isometries

ASSUME a regular finite map with a supplied measurable labeling of all inverse
branches over its image. This is an access assumption, not an algorithm for
finding those branches from equations.

1.2.1 For a real map `F:X -> Y`, change of variables gives

`(U_F g)(y,a)=g(x_a(y))/sqrt(|det D F(x_a(y))|)`

and `sum_a integral_Y |(U_F g)(y,a)|^2 dy=integral_X |g(x)|^2 dx`.

1.2.2 For a holomorphic map between complex `n`-dimensional domains, the real
Jacobian determinant is `|det_C D F|^2`. Consequently the corresponding isometry
divides by `|J|`, not by `sqrt(|J|)`. Multiplying by the known Jacobian phase
gives canonical-form transport `g/J`, with the same norm.

1.2.3 The residue trace of a canonical form is then the sum of the branch
amplitudes. Its universal merger has norm `sqrt(D)`, attained when the branch
amplitudes agree. In this encoding there is no extra Jacobian divergence in the
merger operator itself. Conditioning can instead occur in source preparation,
the normalized branch amplitudes, inverse-branch access, and point evaluation.

1.2.4 A row with coefficients `c_a/N_c` is a valid physical measurement amplitude:
prepare the unit vector with entries `bar(c_a)/N_c`, apply its preparation
inverse, and measure the zero label. The conjugation is necessary. The bound
is optimal for this universal linear contraction because its operator norm is
one. Compiling the preparation costs `O(D)` for a general explicit vector; no
efficient preparation from sparse polynomial equations has been established.

This identifies an actual contraction when the access is supplied. The general
finite-map isometry remains an uncompiled operation in the equation-input model.
It is not being declared a new algorithm or an automatic solution of residue
evaluation. Section 3 gives one family where the trace compiles directly, without
the inverse-branch access assumption.

## 2. Two colliding roots: exact cancellation survives, root encoding does not

### 2.1 The complete local-duality calculation

Let `0<t<=1`, `f_t(z)=z^2-t^2`, and `A_t=C[z]/(f_t)`. In the coefficient
basis `1,z`, define the global residue functional by

`lambda_t(g)=g(t)/(2t)-g(-t)/(2t)`.

For a remainder `g=c_0+c_1 z`, direct cancellation gives `lambda_t(g)=c_1`.
Adding a multiple of `f_t` does not affect finite residues. At `t=0`, the
double-pole formula gives `lambda_0(g)=g'(0)`, the same coefficient functional.

ASSUME this definition. PROVE the residue pairing remains nondegenerate even
as the two roots collide.

2.1.1 Since `z^2=t^2` in the quotient, the bilinear form
`B_t(u,v)=lambda_t(uv)` has matrix

`B_t=[[0,1],[1,0]]`.

It is independent of `t`, including at `t=0`, and has determinant `-1`.
It is a bilinear local-duality form, not a positive Hermitian inner product.

2.1.2 The root-evaluation matrix and residue weight matrix are

`V_t=[[1,t],[1,-t]]`, `D_t=diag(1/(2t),-1/(2t))`.

They satisfy `V_t^T D_t V_t=B_t`. The transpose here is bilinear, not adjoint.
The singular values of `V_t` are `sqrt(2)` and `sqrt(2)t`. Thus root evaluations
can be ill-conditioned while the coefficient-basis residue pairing stays fixed.

2.1.3 The ordinary algebra trace pairing is a different object. Its matrix is
`[[2,0],[0,2t^2]]`, because multiplication by `c_0+c_1 z` has trace `2c_0`.
It degenerates at the nonreduced point. That degeneration must not be attributed
to the Grothendieck residue pairing in 2.1.1.

### 2.2 An explicit circuit and its operational meaning

Suppose the input state is the normalized evaluation ket of `g=c_0+c_1 z`:

`|v_t(g)>=[(c_0+t c_1)|+>+(c_0-t c_1)|->]`
`/sqrt(2(|c_0|^2+t^2|c_1|^2))`.

Projecting onto the antisymmetric branch vector gives acceptance probability

`a_t(g)=t^2|c_1|^2/(|c_0|^2+t^2|c_1|^2)`.

This is a one-qubit basis change and measurement, fully implementable when this
evaluation ket is supplied or its two amplitudes are classically available. It
is an interference readout, not an original algorithmic mechanism.

The absolute Jacobians on the two roots are equal. Therefore normalizing either
of the half-density encodings in section 1 gives the same ket in this example.
Their different functional norms are exactly compensated by their different
unnormalized source norms. Changing rows of the access table does not remove
the displayed `t^2` acceptance factor.

### 2.3 A genuine copy-only lower bound, with narrow scope

Give the equation `f_t`, and copies of the evaluation ket for one unknown member
of the two-element family `g_0=1`, `g_1=1+z`. The desired output is whether its
residue is `0` or `1`. Its overall scale is fixed by this promise; no unobservable
global phase is being requested.

2.3.1 These normalized kets have squared overlap `1/(1+t^2)`. On `T` copies,
the squared overlap is `(1+t^2)^(-T)`.

2.3.2 For two pure states, trace distance is the square root of one minus
squared overlap. Success probability at least `2/3` under a uniform prior
therefore requires trace distance at least `1/3`. It follows that

`T >= log(9/8)/log(1+t^2) = Omega(t^(-2))` as `t -> 0`.

This bound permits arbitrary collective measurements, so it does not merely
criticize the particular antisymmetric measurement. For `t=2^(-b)` it is
exponential in the parameter's bit length in this copy-only input model.

2.3.3 The bound does not apply when the coefficient list, the polynomial's
arithmetic circuit, a reversible value oracle, or controlled preparation and
its inverse are supplied instead. Classical coefficient access reads the answer
directly in the displayed family. At `t=0`, root-value data lose the derivative
entirely, whereas coefficient or jet data still determine the residue exactly.

2.3.4 Tensoring the example gives `f_j=z_j^2-t^2`,
`g=product_j(1+z_j)`, with global residue one. Performing all the branch
antisymmetrizations succeeds with probability `[t^2/(1+t^2)]^n`. This is a
cost of that specified global readout, not a universal exponential-in-`n`
lower bound: its product structure and coefficient input permit other methods.

## 3. A positive cancellation theorem: residue trace as integer division

The next construction avoids colliding-root evaluation altogether. It shows
explicitly how canonical-form residue cancellation can be performed before
normalization. Its final classical-input audit is nevertheless decisive.

### 3.1 Map, metric, and exact trace

Let `d>=2` be an integer and `F(z)=z^d` map the unit disk to itself. For a
polynomial `g`, define the canonical trace

`(T_d g)(y)=sum_(z^d=y) g(z)/(d z^(d-1))`, initially for `y!=0`.

Use the Bergman norm `||g||_B^2=integral_(|z|<1)|g(z)|^2 d^2z`. Its normalized
monomial basis is `e_n(z)=sqrt((n+1)/pi) z^n`. This is not the Fock metric.

ASSUME these definitions. PROVE that `T_d/sqrt(d)` is an explicit partial
isometry with a circuit using reversible arithmetic on the exponent label.

3.1.1 Summing the `d` roots of unity gives

`T_d(z^n)=y^m` if `n=dm+d-1`, and zero for every other nonnegative `n`.

The possible negative exponent in the intermediate formula never survives.
Consequently the trace extends polynomially through the branch point `y=0`.
This is exact cancellation of the apparent Jacobian poles.

3.1.2 In the stated orthonormal bases,

`T_d e_(dm+d-1)=sqrt(d) e_m`.

All other basis vectors are annihilated. Thus `||T_d||=sqrt(d)`, and the
normalized operator is exactly

`K_res |dm+d-1>=|m>`, `K_res |dm+r>=0` for `r!=d-1`.

### 3.2 Full instrument and resource identity

3.2.1 On the nonnegative exponent label, implement the bijection

`|n> -> |floor(n/d)> |n mod d>`.

With a finite cutoff, unused basis labels are padded to a unitary encoding.
Reversible integer division costs `poly(log(M+1),log d)` gates for degree
cutoff `M`; it does not compute roots, Jacobians, or a Fourier transform.
Read the remainder register. Outcome `d-1` implements `K_res`.

3.2.2 Other remainder outcomes are retained as the other polynomial coefficient
sectors. The full instrument is trace preserving. It decomposes the coefficient
register, but does not turn every outcome into the same residue output. If the
requested trace is zero, the residue outcome correctly has probability zero.

3.2.3 If the input is the Bergman-normalized ket of `g=sum_n a_n z^n`, its
residue-outcome probability is exactly

`a_res(g)=||T_d g||_B^2/[d ||g||_B^2]`
`= [sum_(n congruent d-1 mod d) |a_n|^2/(n+1)]`
`  / [sum_n |a_n|^2/(n+1)]`.

Conditional on that outcome, the quotient register is the normalized coefficient
ket of `T_d g`. Repetition on fresh supplied copies costs expected
`O(poly(log M,log d)/a_res)` gates, plus all input preparation costs. If the
input is promised supported on the selected congruence class, success is one.

3.2.4 This is an encoded-register circuit, not an assertion that a passive
single-mode optical device can coherently divide photon occupation numbers.
Such a hardware realization would require its own operations and accounting.

### 3.3 Matched classical-input comparison

Give a sparse classical list of the nonzero pairs `(n,a_n)`, of length `S`,
with binary exponents bounded by `M`. The classical algorithm keeps indices
congruent to `d-1`, replaces each by `(n-d+1)/d`, and samples with weights
`|a_n|^2/(n+1)`. This costs `O(S poly(log M,log d,B))`, including numerical
precision `B`, and produces the identical conditional coefficient sample.

Loading the original arbitrary coefficient ket already has a linear-in-`S`
cost in this access model. For a requested residue output, it is also possible
to load the filtered classical list directly. Thus rare residue outcomes do
not establish a classical-input quantum advantage.

An arithmetic circuit for `g` with enormous degree is a different input model.
This lane does not supply an efficient procedure for loading its coefficient
ket. Substituting such a loading oracle would hide the main computation. The
actual circuit above is basis-label arithmetic and admits the displayed classical
simulation; it is not a qualifying original algorithmic mechanism under D22.

### 3.4 Nonmonomial follow-on: automorphisms and all-branch residue packets

The proposed extension is to interleave division by two with canonical pullbacks
of disk automorphisms. For `|a|<1`, put

`phi_a(z)=(z-a)/(1-bar(a)z)`, `C_a g(z)=phi_a'(z) g(phi_a(z))`.

Change of variables makes `C_a` unitary in ordinary Bergman space. Retaining
every remainder label after division, then applying further automorphisms, looks
like a deterministic packet transform for compositions of proper disk maps.
The following two audits are necessary before that interpretation or its claimed
resources can be used.

**Branch metrics.** Write `g(z)=sum_(r=0)^(d-1) z^r h_r(z^d)`. Direct polar
integration gives the exact orthogonal decomposition

`||g||_B^2=sum_r (1/d) integral_(|y|<1) |h_r(y)|^2`
`                                      |y|^(2(r+1)/d-2) d^2y`.

Thus a branch has output function `h_r/sqrt(d)` in the weighted space with
`alpha_r=(r+1)/d` and weight `|y|^(2 alpha_r-2)`. Its normalized monomials are
`sqrt((m+alpha_r)/pi)y^m`. Only `r=d-1` is ordinary Bergman space. The digital
division circuit respects these branch bases; it does not put all the functions
`h_r` in one common unweighted analytic metric.

Applying `C_a` as though every branch were ordinary Bergman is generally wrong.
For instance, in the even branch of `d=2`, the squared norm of the constant is
`2pi`. For real small `a`, direct expansion of `phi_a'` gives

`||C_a 1||_(alpha=1/2)^2=2pi-(4pi/3)a^2+O(a^4)`.

Hence it is not unitary in that branch metric. A genuine canonical pullback
must transport the weight and its branch divisor. A fixed-space isometric
correction would involve a factor with modulus `|phi_a(z)/z|^(alpha_r-1)`;
its fractional holomorphic interpretation carries branch data in general.

One can define an artificial common-register task by the basis identification
`J_alpha(e_m^(alpha))=e_m^(1)`. On monomials it rescales by
`sqrt((m+1)/(m+alpha))`. Applying ordinary Bergman matrices to these common
labels then means `J_alpha^(-1) C_a J_alpha`, not the original geometric
canonical pullback. That change of task must be stated explicitly.

**No exponential packet count in the classical comparator.** Suppose all old
remainder labels are retained, finally measured, and future operations act only
on the quotient label or are controlled diagonally by the old labels. All those
labels may be measured immediately with the same final joint sampling law.
For a classical coefficient input and a cutoff `M`, a classical simulator needs
one length-`M+1` coefficient vector along the sampled trajectory, together with
the classical label history. It does not need `2^L` packet vectors after `L`
binary divisions. This argument fails if a later operation coherently mixes
different old labels; such a recombination is a further operation to construct.

**The actual automorphism implementation has a resource gap.** In ordinary
Bergman space, the noncompact group generators satisfy

`K_0|n>=(n+1)|n>`,
`K_+|n>=sqrt((n+1)(n+2))|n+1>`.

They are realized by two-mode squeezing on the encoding `|n> -> |n+1,n>`.
This supplies a native Gaussian operation for `C_a`, with squeezing parameter
`r=artanh |a|`. It does not supply a digital `poly(log M)` implementation.
Conversely, the digital division circuit does not supply coherent photon-number
halving in that physical encoding; that is a non-Gaussian operation.
There is no common encoding with both promised cheap operations established here.

**A controlled classical regime.** For the artificial ordinary-Bergman packet
task, define the mean degree resource `E=Tr((N+1)rho)`. In the two-mode
representation, `K_0+K_x` and `K_0-K_x` are positive, so the boost identity gives

`C_a^dag K_0 C_a <= exp(2r) K_0`.

After integer halving, `floor(N/2)+1 <= (N+2)/2`; consequently one stage obeys

`E_next <= [exp(2r) E+1]/2`.

If all `r<r_*<(log 2)/2`, this bounds the mean by a constant plus its initial
value. This statement is averaged over retained branch labels, and remains
valid with label-dependent choices satisfying the same uniform squeezing bound.

For polynomially bounded initial mean, choosing a cutoff polynomial in the
number of stages and inverse error controls the entire calculation: Markov's
inequality bounds each tail by `E/(M+1)`, and the usual square-root disturbance
bound plus a hybrid argument gives total error at most
`O(L sqrt(E_max/(M+1)))`. Matrix elements of `C_a` up to that cutoff are
computed from the power-series expansion of
`(1-|a|^2)(z-a)^n/(1-bar(a)z)^(n+2)`. This yields a polynomial-time classical
single-trajectory simulator at polynomial cutoff, without a packet-tree explosion.

Large squeezing or exponentially large initial mean falls outside that regime.
No efficient digital gate theorem, geometric metric-transport circuit, or hard
classical-output result is established there. An exact identification with a
published quantum wavelet or baker-map algorithm has not been proved; resemblance
alone is not used as a novelty rejection. The concrete metric and encoding gaps,
and the scoped trajectory simulation, are the conclusions that survive.

## 4. A globally normalized residue sampler, and its exact known equivalence

To check whether local duality itself can remove a global success denominator,
consider a family where the coefficient state is physically preparable from
classical data with norm exactly one.

### 4.1 Input, output, and local residues

Give an `m`-mode unitary matrix `U` by its classical entries or a list of optical
gates, and an integer `1<=N<=m`. Define the split form

`g_U(z)=product_(i=1)^N [sum_(j=1)^m U_(ji) z_j]`.

For every occupation multiindex `alpha` of total degree `N`, let

`I_alpha=(z_1^(alpha_1+1),...,z_m^(alpha_m+1))`.

Its local Grothendieck residue at the origin satisfies

`Res_(I_alpha)(g_U)= [z^alpha]g_U`,

by repeated one-variable coefficient extraction. The proposed classical output
is an index `alpha` drawn with probability

`alpha! |Res_(I_alpha)(g_U)|^2`.

Here the output selects a member of an explicitly specified family of monomial
complete intersections; it does not estimate a chosen residue to relative accuracy.

### 4.2 Actual circuit and normalization proof

4.2.1 Prepare one photon in each of the first `N` input modes and vacuum in
the rest. Apply the supplied passive unitary and measure all output occupations.
Creation operators transform by its columns, so the resulting Fock ket is
exactly the polynomial `g_U` in the Fock identification.

4.2.2 The occupied input columns are orthonormal. The transformed creation
operators therefore obey the same canonical commutation relations, and the
input ket has norm one. Expanding `g_U=sum_alpha c_alpha z^alpha` gives

`sum_alpha alpha! |c_alpha|^2=1`.

The output law is consequently exactly the residue law in 4.1, without a global
postselection denominator. A matrix input can be decomposed into polynomially
many optical elements; a supplied gate list is executed directly. Preparation
uses `N` photons, and readout returns their occupation multiset.

4.2.3 For a repeated-row matrix `U_alpha` formed from the first `N` columns,
coefficient expansion gives `c_alpha=per(U_alpha)/alpha!`. Therefore

`Pr(alpha)=|per(U_alpha)|^2/alpha!`.

This is precisely ordinary BosonSampling, with identical input, physical circuit,
and classical output. The residue vocabulary has not introduced a new mechanism.

### 4.3 Classical baseline and disposition

The full coefficient expansion is not the appropriate classical sampling baseline.
Clifford and Clifford's exact sampler costs
`O(N 2^N+poly(m,N))` time and linear additional space:
[The Classical Complexity of Boson Sampling, arXiv:1706.01260v2](https://arxiv.org/abs/1706.01260v2).
Their later work gives improved average-case scaling when the mode count is
proportional to the photon count:
[Faster classical Boson Sampling, arXiv:2005.04214v2](https://arxiv.org/abs/2005.04214v2).
These are fetched primary sources and explicit attacks, not an exhaustive claim
about the current best algorithm for every structured optical input.

The exact operation equivalence in 4.2.3 already defeats D22. Nor does selecting
one rare occupation event give a useful approximation to an arbitrary residue:
additive and relative accuracy, event probability, and the residue's complex phase
are different outputs requiring separate promises and analyses.

## 5. Verification and MERGE PROPOSAL

Bounded in-memory calculations checked the constant two-root pairing and the
evaluation-ket overlap at `t=1,0.1,0.001`; the Bergman trace probability identity
for random degree-30 polynomials and `d=2,3,7`; and the full residue-family
normalization for `(m,N)=(3,2),(4,3),(6,4)`. All errors were below `1e-12`.
These are exploratory checks, not registered red-capable checkers or adjudication.

Candidate statements for independent review are the encoding table with its
real/complex volume distinction; the fixed bilinear pairing, singular evaluation
transform, and scoped copy lower bound in section 2; and the exact normalized
residue partial isometry and arithmetic implementation in section 3.

The residue-family sampler in section 4 should be retained only with its exact
BosonSampling equivalence. No new mechanism, classical-input speedup, or intrinsic
residue-conditioning theorem is proposed for promotion. In particular, the failure
of a root-value encoding does not imply failure of coefficient or jet access,
and nondegenerate bilinear local duality is never identified with a positive
quantum metric. The positive cancellation theorem survives these qualifications.
