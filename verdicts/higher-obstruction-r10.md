# Higher-obstruction processor: independent audit

2026-09-05. This audit follows D-HIGHER-OBSTRUCTION-PENCIL,
D-HIGHER-OBSTRUCTION-QUERY and D-HIGHER-OBSTRUCTION-REALIZATION, including
their explicit finite-dimensional Hermitian departure from C1. Dimensions
here are independent of C2. Only this verdict is critic-owned; canonical
claim status remains with the orchestrator.

Audit in progress: independent derivations below are complete; the
constructor's final artifact and repair responses are still being checked.
Mathematical correctness and qualification under PRD D22 are separate.

## 1. Independent input audit

### 1.1 Formal elimination and its domain

1. ASSUME the supplied pencil of D-HIGHER-OBSTRUCTION-PENCIL. Write
   `D(t)=D0+tE`. Since `D(0)` is invertible, `D(t)` is invertible over
   `C[[t]]`, and also over the local ring at `t=0`.
2. Multiplying the pencil on the right by
   `[[1,0],[-D(t)^(-1)tC,1]]` and on the left by
   `[[1,-tB D(t)^(-1)],[0,1]]` gives `diag(S(t),D(t))`.
   Both multipliers are invertible in those rings. This is generally not
   elimination by invertible polynomial matrices on the whole affine line.
3. Thus the supplied local module presentation has the effective map in
   D-HIGHER-OBSTRUCTION-PENCIL. No analytic convergence was used.
   A sufficient Neumann-series domain is
   `|t| ||D0^(-1)E|| < 1`; its failure is not a formal obstruction.

### 1.2 A finite-order bound

1. For this derivation abbreviate `T=D0^(-1)E` and `v=D0^(-1)Cx`.
   The canonical coefficient formula gives
   `S_k x=(-1)^(k-1)B T^(k-2)v` for `k>=2`.
2. By Cayley--Hamilton, every `T^j` for `j>=m` is a linear combination of
   `1,T,...,T^(m-1)`.
3. Consequently `Ax=0` and `B T^j v=0` for `0<=j<m` imply
   `S_k x=0` for every `k`. Every finite first surviving order is at most
   `m+1`. In particular, a promised query with `ell>m+1` has zero answer.
   This is an exact arithmetic statement, not a finite-precision equality
   test. At `m=0`, only `S_1=A` remains.

### 1.3 A constant endpoint is not an arbitrary formal lift

1. Set `K_in=C^2`, `K_out=L_in=L_out=C`,
   `A=(0,1)`, `B=1`, `C=(1,0)`, `D0=1`, `E=0`, and `x=(1,0)`.
   The effective row is `S(t)=(-t^2,t)`, so `S_1x=0`, `S_2x=-1`.
2. Nevertheless, `x(t)=(1,t)` and `y(t)=-t` satisfy
   `F(t)(x(t),y(t))=0` exactly. Hence a nonzero supplied coefficient need
   not obstruct lifting the initial endpoint when its higher coefficients
   are allowed to vary.
3. The invertible endpoint change
   `R(t)=[[1,0],[t,1]]`, with `R(0)=1`, gives `S(t)R(t)=(0,t)`.
   The new constant `x` has no surviving coefficient. Thus the raw vector
   query is not invariant under formal gauges even fixing the special
   fibre. Exact zeros under consistent constant basis changes and norms
   under unitary basis changes are different, valid invariances.
4. For one-dimensional endpoints the stronger local statement does hold:
   if `S(t)` has finite order `ell`, local elimination identifies the
   cokernel with `C[t]_(t)/(t^ell)`; if `S(t)=0`, it is free of rank one.
   A unit of the local ring does not change that order. The coefficient's
   norm still depends on the supplied metric and presentation.

## 2. Reconstructed unitary instrument

1. ASSUME the constructor's restricted input: `D0=1`, common endpoint
   space `K`, common internal space `L`, and the supplied operator
   `U=[[A,B],[C,E]]` is unitary on `K direct-sum L`. Let `P` and `Q` be
   the orthogonal endpoint and internal projections.
2. Start with the supplied unit vector `x` in `K`. Apply `U`, measure
   `{P,Q}`, and continue on outcome `Q`. Stop at the first `P` outcome.
   At a fixed cutoff `r`, the complete instrument has first-detection
   Kraus maps `K_j=P U(QU)^(j-1)P`, `1<=j<=r`, and residual
   `R_r=(QU)^rP`. This defines all outcomes, including failure to return.
3. Block multiplication gives `K_1=A` and
   `K_j=B E^(j-2)C=(-1)^(j-1)S_j` for `j>=2`, with
   `R_r x=E^(r-1)Cx` in `L` for `r>=1`.
4. The identity `||K_jx||^2=||R_(j-1)x||^2-||R_jx||^2`, taking
   `R_0=P`, proves completeness and the full stopping distribution.
   First detection at `ell` has probability exactly `||S_ell x||^2`.
   There are no omitted independently normalized successful factors.
5. Under the canonical earlier-zero promise every earlier internal
   outcome is deterministic. Inductively `U^j x=(QU)^j x` for `j<ell`,
   and the entire state before the last projection agrees at `j=ell`.
   Thus `U^ell` followed by one endpoint measurement implements the same
   final success and residual states, using the same `ell` applications
   of `U`. The intermediate measurements can be removed for this bit task.
6. An ideal trial uses one preparation, at most `ell` passages, and the
   endpoint detector. With known `0<gamma<=1`,
   `ceil(gamma^(-2) log(1/delta))` independent trials have false-negative
   probability at most `delta` when the nonzero promise holds. The exact
   zero case never clicks. Endpoint preparation, detector implementation,
   passage time, storage and any mode-to-qubit encoding are charged.
7. No spectral-gap or small-`t` obstruction applies to this proof. Its
   validity does not imply that an arbitrary supplied pencil has this
   unitary block structure or admits an efficient conversion to it.

### 2.1 Stronger finite-dimensional check

1. Under the earlier-zero promise,
   `<U^a x,U^b x>=<x,U^(b-a)x>=0` for `0<=a<b<ell`.
   Thus `x,Ux,...,U^(ell-1)x` are orthonormal.
2. The last `ell-1` vectors lie in the `m`-dimensional internal space,
   proving `ell<=m+1` for a possible first return in the unitary family.
3. If `ell=m+1`, those internal vectors form a basis. The same inner
   product identity makes `U^ell x` orthogonal to that basis, so the
   endpoint detection probability at `ell` is exactly one. This conclusion
   does not require the endpoint dimension to be one.

### 2.2 Finite-accuracy meaning

1. Exact order extraction from unrestricted noisy real coefficients is
   discontinuous. The input's explicit zero-versus-`gamma` promise is
   necessary; an implementation cannot certify arbitrary exact zeros.
2. For the equivalent final-measurement circuit, suppose the supplied
   implementation errors obey
   `e=epsilon_x+ell epsilon_U+epsilon_P<=gamma/4` in vector, operator and
   projector norm. Telescoping products bound the final endpoint amplitude
   error by `e`.
3. The noisy probability is at most `gamma^2/16` in the ideal zero case
   and at least `9gamma^2/16` in the ideal nonzero case. A count threshold
   at `gamma^2/4`, with `O(gamma^(-2) log(1/delta))` trials, separates
   these cases by multiplicative Chernoff bounds. Under noise, the ideal
   rule that a single click certifies nonzero must be replaced.

## 3. Exact prior-operation identification

The primary source was fetched only after deriving the instrument:
Bourgain, Grunbaum, Velazquez and Wilkening,
[Quantum recurrence of a subspace and operator-valued Schur functions]
(https://arxiv.org/abs/1302.7286), DOI
[10.1007/s00220-014-1929-9](https://doi.org/10.1007/s00220-014-1929-9).
The [author-hosted full text]
(https://math.berkeley.edu/~wilken/papers/Subspace_Recurrence_CMP.pdf),
Section 2, page 4, equation (1), and page 5, equation (3), specify the
same monitored subspace-return instrument, its amplitude and survival law.
The identification is `V=K`, the same `U`, the same projection `P`, and
the same initial `x`. It preserves all outcomes, conditional states,
preparations, measurements and number of passages exactly.

Independently summing the blocks gives the first-return generating
function `a(z)=zA+z^2 B(1-zE)^(-1)C`; hence `S(t)=-a(-t)`.
The coefficient signs are global phases on individual recorded outcomes;
if times are retained coherently they require only the corresponding
diagonal phase on the existing time register. Thus the displayed processor
has an exact prior-channel identification. Its D22 rejection is stronger
than observing that its circuit consists of known elementary gates.

## 4. Matched classical algorithms and access limits

1. **Explicit matrices and endpoint vector.** For `D0=1`, form `Cx`,
   apply `E` exactly `ell-2` times, apply `B`, and evaluate the output
   norm (or test exact rational zero). The earlier coefficients need not
   be computed when their vanishing is promised. The arithmetic cost is
   `O(nnz(C)+(ell-2)nnz(E)+nnz(B))`, with vector storage linear in the
   relevant dimensions. Vector-input reading and arithmetic precision
   are additional charged costs. Dense full cohomology is irrelevant.
2. **General explicit invertible `D0`.** Factor `D0` once, solve for
   `v=D0^(-1)Cx`, then repeatedly apply `E` and solve against the same
   factorization. A standard dense upper bound is `O(m^3)` factorization
   plus `O(m^2)` arithmetic per solve and the matrix-vector costs. Sparse
   factorizations or iterative solves can improve this; a quantum
   comparison must also charge condition numbers and solve accuracy.
   These are constructive upper bounds, not optimality claims. Rational
   input bit growth must not be replaced by unit-cost exact arithmetic.
3. **Succinct sparse row/column entry access.** With an explicitly
   preparable basis state or classically available vector, scanning all
   sparse rows implements each matrix-vector multiplication using
   `O(N s_row)` oracle calls and `O(N)` stored amplitudes. The same
   endpoint norm is returned. Forward path enumeration may be cheaper
   when column access is supplied and the accessible support is small;
   its branching factor must be charged. No efficient general stochastic
   path estimator follows for signed or complex interfering paths.
4. **Unitary circuit descriptions.** A classical state-vector simulation
   of the same preparation and `ell` copies of the step circuit is a
   matched same-bit upper bound. Its exponential dimension dependence
   may matter. This audit does not prove efficient dequantization of
   arbitrary succinct unitary evolution or exclude an oracle speedup.
   A proved speedup would still need to survive the exact known-mechanism
   identification in Section 3 to qualify under D22.
5. **Opaque block encodings or state-preparation oracles.** A classical
   entry oracle, coefficient list or sample-and-query interface is not
   automatically supplied by a quantum block encoding. Conversely a
   black-box amplitude encoding is not free for explicit coefficients.
   Without a common declared input model, no matched speedup statement
   is established.

## 5. Review objections and required scope

### O1: intrinsic-obstruction interpretation

**Severity:** MAJOR if asserted; the canonical definition already avoids it.

**FIX DEMAND:** State the constant endpoint and gauge as part of the query.
Use the explicit local cokernel identification for scalar endpoints. An
Ext/Massey/deformation or spectral-sequence interpretation requires its
own identification and quotient argument.

**SURVIVING STATEMENT:** Sections 1.1--1.3 prove a valid framed module
query and, in the scalar case, a local torsion-length interpretation.

### O2: original mechanism

**Severity:** FATAL to D22 qualification of the monitored unitary processor;
not an error in its mathematical correctness.

**FIX DEMAND:** Do not label this processor or its final-measurement
simplification an original quantum algorithm. A replacement would need a
different substantive operation and a new independent audit.

**SURVIVING STATEMENT:** Exact extraction without a `t^ell` penalty is
valid on the supplied unitary-colligation family and is precisely the
known monitored subspace-return operation.

### O3: normalization for a general pencil

**Severity:** MAJOR if the unitary result is extended to arbitrary blocks
without a charged conversion. Constructor's Gramian repair is under audit.

**FIX DEMAND:** Include the conversion, all loss branches, preparation
probabilities, inverse costs, conditioning and precision. Avoid treating
the arbitrary internal resolvent as a unitary scattering device.

**SURVIVING STATEMENT:** The original coefficient recurrence remains
valid for every supplied pencil; Section 2 currently applies only to the
explicit unitary restriction.

### O4: exact zeros and the classical comparator

**Severity:** MAJOR if a noisy single click is an exact certificate or if
dense basis extraction is the classical comparator.

**FIX DEMAND:** Use the promised, metric-explicit finite-accuracy decision
and a threshold detector under noise; compare to the same recurrence or
same circuit with the actual common input access.

**SURVIVING STATEMENT:** Section 2.2 supplies a robust gapped bit test;
Section 4 supplies matched constructive baselines without a universal
classical simulation claim.

## 6. Pending convergence

The constructor must finish its artifact and answer O3. No new canonical
claim is promoted by this interim document. No numerical probe or checker
was run by this critic; the statements above are direct finite-dimensional
derivations and an independently verified primary-operation comparison.
