# Independent audit of the Hall-extension constructions

2026-09-05. Root independently reviewed the agent's
`scouting/hall-extension-r7.md`, including its exact output and access costs.
The scoped mathematical and comparator audit passes. No FATAL or MAJOR
objection remains. This is not a historical-priority or north-star verdict.
Canonical inputs are in `definitions/hall-extension.md`.

## 1. The sampled extension measure and its automorphism factors

Changing a splitting changes the off-diagonal block by `N_a f_1-f_2 M_a`.
The image of this linear map has the same cardinality in every coset.
Uniform framed X therefore induces uniform extension-class sampling; it
does not imply uniform middle-object isomorphism classes. For zero diagonal
arrows, rank classifies the middle arrow. The displayed rank count follows
by factoring a rank-r matrix through F_q^r and dividing by GL_r. Gaussian
elimination on a sampled matrix is a matched same-output classical algorithm.

For each eligible submodule of fixed E, there are `a_N a_M` endpoint
identifications. The stabilizer of such an exact sequence under Aut(E)
consists exactly of `1+i f p`, with `f in Hom(M,N)`; its inverse is
`1-i f p` because `p i=0`. Orbit-stabilizer consequently gives

`|Ext^1(M,N)_E|=F_(MN)^E a_N a_M |Hom(M,N)|/a_E`.

In the two-by-two fixture, the zero middle arrow has `(q+1)^2` flags,
while the rank-one arrow forces the kernel and image lines and has one.
The claimed automorphism counts yield exactly 1 and q-1 extension classes.
This independently checks that the Hom cardinality is in the numerator
and cannot be replaced by its dimension or dropped.

## 2. Coherent pushforward and the affine-interference baseline

Different rows of the flag-forgetting matrix have disjoint supports.
Thus `T T^dagger=diag(F_y)` and `||T||=sqrt(F_max)`. Applying
`T/sqrt(F_max)` to a uniform fibre gives success `F_y/F_max`.
The normalized-coarea map instead has orthonormal rows and is a
coisometry. It projects onto uniform fibres before discarding the fibre
coordinate. Its norm does not construct that fibre transform for free.
The memo correctly separates these maps from injectively retaining the flag.

For two normalized uniform affine-space states, the overlap is the
intersection cardinality divided by the square root of the two sizes.
The three disjoint regions have known constant amplitudes in their plus/minus
superposition. Their masses can be calculated, and proper affine differences
can be sampled with acceptance at least `1-1/q`. The zero minus state is
excluded. This is an actual classical sampler, not a comparison against
listing exponentially many matrix entries of the resulting quantum state.

## 3. Retained order and the geometric obstruction

Apply the four shears right-to-left. The successive nontrivial coordinates
are `v-Xu`, then `w-Yv+YXu`, then restored v, then `w+YXu`.
No flag is erased, and the resulting unitary is exactly the displayed
commutator. The product YX is the path-relation obstruction of the variety
of complexes, with basis covariance `YX -> g_3(YX)g_1^(-1)`.
The adjacent degree-one extension classes give this same length-two
obstruction; the membership algorithm requires no homological oracle.

The kernel of a rank-r linear map on F_q^a has size q^(a-r), so the
nonzero output probability is exactly `1-q^(-r)`. The classical algorithm
samples the same u and applies the same two matrices successively. Its
success law is identical, with no full-product computation and no larger
asymptotic working storage. Repeating the test gives the stated logarithmic
error reduction in either model.

Constant-coefficient field multiplication is binary linear in the supplied
polynomial basis, giving the claimed CNOT implementation bound. The input
matrices remain classical constants. Coherently controlling an entire order
is not silently declared Clifford: the memo explicitly computes its scalar
overlap `q^(-r)` instead. Its destructive port has half the direct-test rate.
Higher path products remain linear in the probe, even when their coefficient
dependence has larger degree. The memo does not conflate a cubic relation
with an ordinary triple Yoneda product.

## 4. Prior art, scope and integration

The Riedtmann--Peng formula is both derived and connected to the primary
Xiao--Xu source. The random-vector comparator is the classical Freivalds
matrix-product test; its success probability is independently established
above. The stated bounds do not depend on an unverified claim about general
module-isomorphism hardness or best-classical orbit enumeration.

The three canonical Hall definitions match these reviewed operations and
outputs. The proposed mathematical integration includes only the exact
measure/norm statements and the retained-order test with its comparator.
No production-code change or unrelated checker run is required by this
algebraic audit. The author's bounded probes support the argument; they do
not promote a speedup or certify historical originality.

There are no unresolved objections requiring a repair. The surviving
statements are the normalized Hall correspondence identities and an exact
retained-register implementation of the obstruction, together with their
matched classical attacks. They leave the broad quiver-geometry search open
but provide no qualifying new quantum algorithm.
