# Independent verdict: original constructions, round 2, revision 1

2026-09-05. Reviewed all four `scouting/original-*-round2.md` memos completely,
CLAUDE.md, PRD criteria 1--6 and D21--D22, the definitions conventions and relevant
entries, the claims register conventions, and HANDOFF.md. No web or historical
novelty review was performed. Tracking and shared-file edits belong to the root.

**VERDICT: FAIL.** Five MAJOR objections remain. No FATAL algebraic obstruction
was found to the surviving identities; several resource and refutation statements
are broader than their arguments. No construction establishes a north-star hit.
All decisions below concern proposed rows only; none promotes a row to PROVED.

## Independently checked substance

**Growth.** The Fock factors are correct: there are `n+1` modes,
`sum_j a_j a_j^dag=N+n+1`, and
`sum_j Z_j Z_j^dag=(N+1)P_(N+1)`. Consequently the successful uniform-state
transport probability is `(N+1)h_(N+1)/((N+n+1)h_N)`, and multiplication from the
vacuum telescopes to `h_N/binom(N+n,n)`. For `(x^2)` at degree one the source
effect is `diag(1/3,1)` and its Lueders failure posterior is `|x><x|`.
This refutes the stated free-retry assertion, not arbitrary recovery.

Adjacent-block detailed balance proves the finite-cutoff reservoir state is
stationary; it does not prove uniqueness or mixing. For the radical ideal
`(x_i y_j)`, the diagonal monomial subspace is invariant and the branch-degree
chain is lumpable. Its left-to-vacuum stationary flux is `ta/H`. Dividing by the
indicator variance gives `ta/[Z_a(1-pi(left))]`. At `b=2a,K=8a,t=1/2`,
`Z_a >= binom(2a-1,a)2^(-a)` and `pi(left)<1/2`, giving the claimed
`O(a^(3/2)2^(-a))` gap upper bound. The worst-start/vacuum-start distinction is
correctly maintained. Conditional degree states require `h_N>0`.

**Algebra.** Associativity makes every multiplication tree the same linear map;
taking adjoints therefore gives tree-independent unzipping amplitudes and the
stated `Z_k/alpha^(2k-2)` success. Rectangular dilations cause no algebraic
problem when their input/output embeddings and work registers are supplied.
The truncated-polynomial example has `||mu||=sqrt(r)` and the stated weak-
composition count. Its trace pairing has rank one, and an algebraic bilinear
trace form is not automatically a positive Hermitian metric. Hidden idempotent
correlation gives no root-coordinate measurement for free.

With `E e_i=(-1)^(i-1)e_1 wedge ... omit e_i ... wedge e_n`, the identity
`E^(-1)(exterior^(n-1) J^T)E=adj(J)` has the correct transpose and signs.
The smallest singular value of the adjugate is `sigma_2...sigma_n`, giving the
stated worst-direction probability. Taking `J=diag(1,kappa^(-1),...,kappa^(-1))`
and `b=e_1` explicitly realizes `kappa^(-2(n-1))`. Binomial finite differences
cancel lower Taylor orders, with heralding probability `||r_k(h)||^2/4^k`.
That circuit is directly an LCU construction, independent of its application.

**Geometry.** Refine accepted operations to Kraus records. Their coordinate
polynomials are homogeneous of degree `t`. Coprime coordinates `F_a` and
`G_a F_b=G_b F_a` imply `G_a=hF_a` in the polynomial UFD. Thus every nonzero
exact branch needs `t>=r`; at `t=r`, all accepted restrictions are `c_l A_Phi`.
The CP inequality yields the stated optimal total success. This includes
multiple accepted records, while extra-degree branch zero sets need not obstruct
their combined success. The iterate lower bound correctly uses reduced degree.
The single-branch zero-set claim also holds: coprime coordinates have no common
divisorial base component, whereas nonconstant homogeneous `h` has a divisor.

The coefficient convention evaluates at `[conj(x)]`, as stated. The fixed-slot
transverse contraction has exactly `binom(m,k)` orthogonal placements, proving
`q_k=binom(m,k)||T_k||^2`. The first nonzero transverse term is the tangent-cone
equation in the chosen chart/trivialization. Lower-polars vanishing makes its
full polar annihilate the radial direction. The occupation measurement and
its scalar multiplicity estimate are available to the single-copy comparator.

Linear Poincare duality maps a Plucker vector to its bilinear annihilator in a
separate dual space without conjugating an unknown state. Wedge multiplication
has `mu mu^dag=binom(p+q,p)1`; the complex annihilator cross-Gram determinant is
`prod_i(1-sigma_i^2)`. Both factors in the displayed success probability are
correct. This is a normalization theorem for the displayed Kraus map, not a
lower bound on every protocol solving the intersection task.

**Broad.** Positive collision sampling gives exactly the displayed endpoint
law and acceptance probability, subject to O1's matched-access qualification.
The prepared signed endpoint vector and its probability are correct, but the
intermediate effective block needs O2. Pullback order and the rational
commutator example are correct. This example can even use the invariant span
of `x,y,(1+y)/x,(1+x)/y,(x+y+1)/(xy)`: the two pullbacks permute these five
rational functions. Their controlled-order difference is a two-term LCU;
unknown-channel quantum-switch access is a separate model, not a supplied gate.

## Objections and required fixes

### O1 — MAJOR: history access and missing preparation costs

**Location:** broad §1, access bullets, operation ledger, positive dequantization;
proposed C-NEW-OB-POSITIVE-FUSION.
Only uniform quantum preparation is supplied. It does not imply an equally
cheap classical uniform-history sampler. Moreover `C` was defined only for
endpoint evaluation, omitting history preparation/unpreparation and weights.
**FIX DEMAND:** Supply matched classical history sampling, or limit the result
to equality of laws without an asymptotic dequantization assertion. Charge
`2C_H+C_e+C_w` per coherent attempt, plus flags/workspace, where the costs
include the corresponding preparation, endpoint, and phase circuits.
Exact replacement: “When uniform histories can be sampled classically at the
charged preparation cost, positive fusion and two-history collision sampling
have identical success and output laws and comparable per-attempt costs.”
**SURVIVING STATEMENT:** The collision identity is unconditional as a
probability identity; a matched-cost algorithmic comparison is conditional.

### O2 — MAJOR: effective fusion block has the wrong normalization

**Location:** broad §1, “Signed attack and equivalence audit,” lines 84--85.
The history-to-endpoint Kraus block is
`K=P^(-1/2) sum_h w_h |e(h)><h|`, not the displayed `P^(-1)` block.
The other `P^(-1/2)` comes from the prepared uniform input.
**FIX DEMAND:** Replace that block and explicitly distinguish the map from
its action on `|+>_H`. For a standard LCU formulation, extend each endpoint
preparation to an isometry/unitary and use the prepared label register.
**SURVIVING STATEMENT:** `K|+>_H=P^(-1)sum_z c_z|z>` and success
`sum_z|c_z|^2/P^2` are correct; the signed mechanism remains postselected LCU.

### O3 — MAJOR: unzipping resource theorem omits supplied-circuit costs

**Location:** algebra §1 cost ledger, lines 107--110; C-NEW-OA-UNZIP-IDENTITY.
The state-preparation cost and arbitrary block-encoding workspace/depth are
absent. A multiplication circuit does not automatically have constant workspace.
**FIX DEMAND:** Introduce `C_u,w_mu,d_mu` and rectangular encoding embeddings.
Replace total gates by
`O((C_u+k C_mu+poly(k,d))*p_k^(-1)*log(1/delta))`, with any additional
encoding/flag logic included explicitly. Parallel tree depth is
`O(d_mu log k)` plus preparation/control depth; its width can be
`kd+O(k w_mu+k)`, or give a sequential-space alternative. Distinguish expected
repeat-until-success cost (no necessary logarithm) from a capped failure bound.
**SURVIVING STATEMENT:** Exact heralded unzipping and its success formula hold;
no cost bound independent of preparation and dilation workspace follows.

### O4 — MAJOR: the jet refutation silently changes its output

**Location:** geometry §2.1 and §2.4; C-NEW-R2-GEO-5, lines 478--486.
Q-TANGENT-CONE includes a quantum tangent-cone ket. Its proposed refutation
proves equality of the classical multiplicity law; the declared classical
comparator performs measurements and classical post-processing. It has not
been defined to return the same quantum ket.
**FIX DEMAND:** Refute only the scalar multiplicity claim. Exact replacement:
“The displayed multiplicity estimator has a collective copy advantage over
adaptive single-copy measurements.” Keep this narrow statement REFUTED, with
the identical `q_k` measurement and `R` bound as survivor. Hold any advantage
claim for producing/using the tangent-cone ket until a same-output task exists.
**SURVIVING STATEMENT:** The scalar estimator is exactly matched; the quantum
instrument is valid, and no separation for a downstream state-output task is
proved or refuted by that scalar comparison.

### O5 — MAJOR: efficient representation is not supplied classical access

**Location:** geometry §3.3 and C-NEW-R2-GEO-7's surviving statement;
algebra §1's blanket “Monomial algebras admit combinatorial samplers.”
Efficient classical evolution of orbital frames assumes those frames are
known. Unknown Plucker copies do not supply their entries. Likewise a monomial
multiplication rule alone does not give classical samples of an arbitrary
circuit-prepared `u` or of its factorization-reweighted coefficient law.
**FIX DEMAND:** Say “Given explicit orbital frames, the displayed decomposable
evolution and output measurements admit polynomial classical matrix
simulation.” Restrict the monomial sampling assertion to the exhibited
monomial input/weak-composition case, or supply a general access theorem.
Keep the known-operation objection separate from classical input comparisons.
**SURVIVING STATEMENT:** Explicit-frame Grassmann intersection is classically
tractable; the displayed quantum map is antisymmetric projection with its
stated success cost. Neither sentence settles arbitrary copy-access tasks.

### O6 — MINOR: determinant recovery is not necessary for Newton scale

**Location:** algebra §2, lines 186--189.
For normalized `v` on the Newton ray,
`||J^(-1)b||=||b||/||Jv||`; scale can be recovered without evaluating `det J`.
An exact complex correction also requires a phase reference relative to `b`.
**FIX DEMAND:** Replace “additionally needs det J” by “requires additional
scale and phase readout; determinant postselection is one costly option.”
Do not present the determinant-product cost as compulsory for all readouts.
**SURVIVING STATEMENT:** The adjugate preparation probability itself already
refutes a uniform polynomial-cost claim for this circuit.

### O7 — MINOR: special-case scope and gauge qualifications

**Location:** algebra §1 reduced broadcaster and §3 Taylor probability;
growth §5.5 and C-NEW-OR-UNIFORM-MIXING's last survivor clause.
**FIX DEMAND:** Unit-success broadcasting requires an implementation with
`alpha_BE=1`; an unnecessarily scaled supplied block does not have it.
Specify real-analytic parameter dependence along a fixed real deformation
path and a nonzero kth derivative for the displayed jet asymptotic. A
nonconstant holomorphic *unit-normalized* lift on a complex open set does not
exist. Limit monomial-reservoir classical simulation to its invariant
diagonal sector with charged membership/rate access and simulated time.
**SURVIVING STATEMENT:** The reduced adjoint is abstractly an isometry;
the exact finite-difference formula holds; diagonal monomial evolution is a
classical occupation process. No stationary-sampling cost follows automatically.

### O8 — MINOR: definition and convention hygiene before merging

**Location:** algebra/geometry/broad introductions and merge definitions.
C7 reserves `alpha_BE` for block normalization; the memos repeatedly use bare
`alpha,beta`. Geometry's ambient `D` also departs from C8 without a specific
declaration. The orthogonal-jet merge definition uses `T_k` without defining it.
**FIX DEMAND:** Rename or explicitly declare local departures, and define the
fixed-slot `T_k` contraction in its sole definition. Specify orthonormal
coordinate/dual bases and unit volume for the norm-sensitive Poincare map.
Rational-map branches mean refined Kraus records; pure outputs after a discarded
environment are handled by refining its Kraus operators. Keep probability-zero
base points and zero-dimensional degree blocks outside conditional-output claims.
**SURVIVING STATEMENT:** The audited formulas are valid with these conventions;
definitions do not provide circuits, complexity promises, or theorem status.

## Per-row and definition decisions

“ACCEPT” below does not excuse the cited wording repairs elsewhere in a memo.
Rows marked HOLD are not ready for merge in their current form.

| Proposed row | Decision | Scope/reason |
|---|---|---|
| C-NEW-OR-GROWTH | ACCEPT AS CONJECTURE | Exact conditional identity. |
| C-NEW-OR-FREE-RETRY | ACCEPT AS REFUTED | Lueders counterexample only. |
| C-NEW-OR-HILBERT-RESERVOIR | ACCEPT AS CONJECTURE | Stationarity; condition on `h_N>0`. |
| C-NEW-OR-UNIFORM-MIXING | ACCEPT AS REFUTED | Radical worst-start gap obstruction; O7 scope. |
| C-NEW-OA-UNZIP-IDENTITY | HOLD | Repair total resource bound, O3. |
| C-NEW-OA-UNZIP-SPEEDUP | HOLD | No natural family/access/hardness/output theorem. |
| C-NEW-OA-TRACE-BROADCAST | ACCEPT AS REFUTED | Rank-one trace-form counterexample. |
| C-NEW-OA-WEDGE-NEWTON | ACCEPT AS REFUTED | Explicit exponential heralding family; O6. |
| C-NEW-OA-JET-LCU | ACCEPT AS REFUTED | LCU equivalence; resolution-dependent success. |
| C-NEW-R2-GEO-1 | ACCEPT AS CONJECTURE | Refined-Kraus degree and optimal-success statements. |
| C-NEW-R2-GEO-2 | ACCEPT AS REFUTED | Contraction alone establishes no claimed advantage. |
| C-NEW-R2-GEO-3 | ACCEPT AS REFUTED | Direct construction costs; reduced iterate degree. |
| C-NEW-R2-GEO-4 | ACCEPT AS CONJECTURE | Chart-dependent jet identity and tangent cone. |
| C-NEW-R2-GEO-5 | HOLD | Restrict refutation to scalar multiplicity, O4. |
| C-NEW-R2-GEO-6 | ACCEPT AS CONJECTURE | Exact probability of this normalized wedge map. |
| C-NEW-R2-GEO-7 | HOLD | Fix copy/explicit-frame scope of survivor, O5. |
| C-NEW-OB-POSITIVE-FUSION | HOLD | Add matched classical history access, O1. |
| C-NEW-OB-SIGNED-FUSION | ACCEPT AS REFUTED | Correct survivor; repair intermediate block, O2. |
| C-NEW-OB-ORDER-DEFECT | ACCEPT AS REFUTED | Controlled two-order LCU; charge supplied blocks. |

Definition decisions: accept D-OR-QUOTIENT-GROWTH, D-OR-HILBERT-RESERVOIR,
D-OA-coherent-factorisation-law, D-OA-dagger-multiplication-access, and
D-R2-RATIONAL-TRANSDUCER as definitions with the stated access/domain
qualifications. Hold D-R2-ORTHOGONAL-JET and D-R2-REGRESSIVE-MEET until O8's
normalization data are included. These are not algorithmic access constructions.
H-CFCS-SIGN and H-ORDER-GEOMETRY remain held, unproved hypotheses.

Finite recomputation: a timeout-60, single-BLAS-thread, unregistered Python run
passed 35 checks of complex adjugate signs/transposes, annihilator Gram norms,
wedge splitting counts, and determinant-free correction scale. This does not
replace proofs or a registered checker. Existing growth checker/mutation claims
were not rerun; circuit synthesis, hardware error, and historical novelty were
not checked. No shared claim status was changed. After repairs, recheck the
statement/status/surviving-statement lockstep before merging any rows.

**VERDICT: FAIL — O1--O5 remain MAJOR; no north-star algorithm established.**
