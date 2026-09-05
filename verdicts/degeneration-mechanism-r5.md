# Independent audit: degeneration mechanisms, round 5

2026-09-05. Reviewed scouting/degeneration-mechanism-r5.md after its
coordinate-conjugation repair. This is an independent review of the displayed
operations and obstructions, not a certification of a new quantum algorithm.
No shared definitions or claims-register statuses are changed by this verdict.

**Verdict: PASS for the mathematical and resource statements.**
No current FATAL, MAJOR, or MINOR remains after the verified repairs below.
The C3 repair was necessary: its original hyperplane wording changed the bit.
The repaired source, copy lower bound, characteristic polynomial, return
recurrence, and finite-horizon retained-bath trajectory agree.

## 1. Repaired objection: geometric and quantum conjugations

**Original severity: MAJOR. Status: repaired and verified.**
Originally the geometric point was labelled by
$\gamma(t\zeta^a)$ while its source ket used coefficients $\zeta^{ak}u_k$.
Since $\gamma(z)=\sum_k z^k\overline{u_k}$, conjugating that geometric point
actually gives coefficients $\zeta^{-ak}u_k$. More seriously, the geometric
hyperplane was described using $u_k$ before conjugating the measurement.

This is not harmless for complex frames. At $D=2$, take
$u_1=(1,i)/\sqrt2$ and $H=\operatorname{span}(u_1)\subset\mathbb C^2$.
Then $u_1\in H$, but $\overline{u_1}\perp H$; the literal original promise
would call the jet contained while its embedded geometric direction is not.

**FIX DEMAND:** Use one coordinate convention throughout: label the supplied
point as $\gamma(t\zeta^{-a})$, require the geometric $H$ to contain
$\overline{u_1},\ldots,\overline{u_{r-1}}$, promise containment or orthogonality
of $\overline{u_r}$, and measure the quantum subspace
$\operatorname{span}\{u_0\}\oplus\overline H$.

**Verification:** These repairs are present in current §§1.1–1.3. The Fourier
label vectors $\chi_k$ may consequently keep their $+ak$ convention, and the
later source expansion and probabilities require no sign changes.

**SURVIVING STATEMENT:** The specified copy source encodes the stated flat
embedded family, and its top-jet containment bit is exactly the stated
hyperplane measurement bit.

## 2. Repaired minor origin convention

**Original severity: MINOR. Status: repaired and verified.**
The text called $H$ an affine hyperplane but used a vector-subspace projector
and asserts that containment of the origin is vacuous. These require $H$
to pass through the origin. Merely containing the listed coefficient
vectors would not force a general affine hyperplane's constant term to vanish.

**FIX DEMAND:** Say explicitly that $H$ is a complex linear hyperplane through
the origin, viewed as a hyperplane in the affine coordinate space.

**Verification:** Current §1.3 explicitly says "complex linear hyperplane H
through the origin," satisfying the requested convention.

**SURVIVING STATEMENT:** All displayed calculations hold under the already
intended zero-constant-term convention; no mathematical construction changes.

## 3. Copy access and coherent-oracle access are kept distinct

The supplied source is copies of a coherent labelled state, with neither a
preparation unitary nor its inverse. Expanding in the known $\chi_k$ basis
gives orthogonal sectors of squared weight $t^{2k}/Z_t$.
Thus the direct hyperplane event has probability
$s=t^{2r}/Z_t$ under the noncontainment promise and zero under containment.
No Fourier transform, rescaling, or intercopy interaction is needed for this
matched adaptive single-copy upper bound.

For the two fixed-frame instances differing only in the final orthogonal
direction, the source inner product is $1-s$. Their $M$-copy trace distance
is $\sqrt{1-(1-s)^{2M}}$, so Helstrom's inequality gives the displayed
$\Omega(1/s)$ lower bound for every collective measurement strategy.
This is an actual comparison with the same geometric bit.

The diagonal inverse succeeds on the flat target with probability $Ds$,
but its conditional top-sector probability is $1/D$. Their product is $s$.
The success effect has eigenvalue one in the top label sector; completeness
therefore makes every failure Kraus operator annihilate that sector.
No failed-output recovery can distinguish the chosen pair of top jets.
This statement is correctly scoped to the specified inverse operation.

With a supplied coherent preparation circuit and inverse, reflection-based
amplification would instead use $O(s^{-1/2})$ oracle calls. That change is
correctly identified as both a different access model and an established
mechanism. It cannot be inferred from the copy promise.

The exterior probability is also correctly normalized: the antisymmetric
projector on one separately supplied copy of each root has acceptance
$\det(V_t^\dagger V_t)/D!$. Its determinant carries the squared
Vandermonde order $t^{D(D-1)}$.

## 4. One-bath characteristic and return formulas

Write $\beta=\sqrt{1-|\tau|^2}$. The two exceptional columns of $U_\tau$
are orthonormal; the remaining live shift columns are disjoint from them.
The modular increment followed by the displayed two-state rotation produces
exactly those exceptional columns, including the conjugation and minus sign.
Thus the circuit is a normalization-one unitary completion.

For an eigenvector with live coordinate $v_0$, the live shift gives
$v_{D-1}=\lambda^{-(D-1)}v_0$ and the bath equation gives
$(\lambda+\overline\tau)v_b=\beta v_{D-1}$.
Substitution into the zero-coordinate equation yields

\[
 \lambda^D(\lambda+\overline\tau)=\tau\lambda+1.
\]

This confirms the characteristic polynomial in equation (8).
Because $|\tau|<1$ and eigenvalues of $U_\tau$ have modulus one, the intermediate
denominators do not introduce an exceptional eigenvalue.
At $\tau=0$ the unitary is a $(D+1)$-cycle, whereas multiplication is nilpotent.

Inserting the bath projector between two steps gives

\[
 PU_\tau^2P-C_\tau^2=\beta^2|0\rangle\langle D-1|.
\]

Consequently one-step compression cannot be used as an all-powers identity.
The first-return series independently equals

\[
 \tau w^D+\frac{\beta^2w^{D+1}}{1+\overline\tau w}
 =\frac{w^D(\tau+w)}{1+\overline\tau w}.
\]

Summing concatenated first returns confirms the stated $R(w)$ and recurrence.
Its initial condition is $c_1=0$ for $D\ge2$; the recurrence begins at $n=2$.
In particular $c_D=\tau$ and $c_{D+1}=1-|\tau|^2$ agree.

The classical recurrence costs $O(T)$ arithmetic operations. Its rounding
bound follows from $1/Q(w)=R(w)/(1+\overline\tau w)$: unitary return
coefficients satisfy $|c_n|\le1$, so reciprocal-denominator coefficients
are bounded by $1/(1-\rho)$ for $|\tau|\le\rho<1$.
The memo charges the additional precision as the unit circle is approached.
It does not infer a universal classical space lower bound from the direct
$O(D)$-storage implementation.

## 5. Fresh baths preserve the intended powers

At step $j$, no amplitude occupies the new bath state $e_j$. All earlier
baths are fixed by every later step. Induction therefore gives the exact
compression $PV_T\cdots V_1P=C_\tau^T$ on every live input.
This is a $D+T$-dimensional horizon-dependent construction, not a claimed
fixed finite all-powers dilation.

For initial $|0\rangle$, the only possible exits occur at times $\ell D$.
Before the $\ell$th exit, the live amplitude is $\tau^{\ell-1}$.
This proves the complete state in equation (12), including its phases,
exit labels, and geometric-series norm one.
Keeping exit amplitudes does not raise the live survival probability.

The basis measurement law is a truncated geometric distribution, so the
stated inverse-CDF classical sampler matches that output. The compressed
return moment is either zero or the single power $\tau^{T/D}$.
Arbitrary quantum readout of the retained coherent history is properly
excluded from this scoped classical-sampling conclusion.

## 6. Independent checks and historical scope

An independent bounded inline Python probe used a 40-second timeout and one
BLAS thread. It passed 1212 small-matrix checks for $D=2,\ldots,7$,
$\tau\in\{0,0.2,0.35+0.4i,-0.2+0.6i\}$, and horizons through $3D+2$.
Checks covered unitarity, the characteristic polynomial, the two-step defect,
the return recurrence, every fresh-bath compression, and every displayed
trajectory. The complex-hyperplane counterexample above was also verified.
This is numerical support, not a registered red-capable checker.

The cited primary pages were independently opened:
[Ralph–Lund, arXiv:0809.0326](https://arxiv.org/abs/0809.0326) addresses
nondeterministic noiseless amplification, and
[Arlinskii–Golinskii–Tsekanovskii, math/0611439](https://arxiv.org/abs/math/0611439)
addresses contractions with rank-one defects and their unitary models.
The memo's restrained historical disposition is consistent with those sources.
This review certifies neither a new invariant nor a new algorithmic mechanism.

The surviving products are the explicit operations, their exact costs, and
their family-specific obstructions. Nothing here proves that all geometric
degeneration algorithms, all retained-bath computations, or all alternative
source encodings admit the same classical attacks.

## 7. Independent integration audit of C-349–C-352

2026-09-05 follow-up. Scope: definitions/mechanism-r5.md and the four new
claims-register rows, compared with the three r5 scouting memos and their
independent verdicts. PRD, HANDOFF, and the active theta lane were outside
this audit and were not edited.

**Integration verdict: PASS, with no outstanding FATAL, MAJOR, or MINOR.**
Both canonical-input clarifications below were applied and verified.
No mismatch or unsupported scope extension was found. This does not independently
reauthorize promotion of an unreviewed statement; each row cites the relevant
existing independent verdict.

C-349 uses the repaired C3 convention consistently: the source and Fourier
label vectors retain $+ak$, while the corresponding geometric point is
$\gamma(t\zeta^{-a})$. The geometric hyperplane contains conjugated lower
coefficient vectors, passes through the origin, and becomes $\overline H$
in the quantum point register. The constant-error $\Theta(1/s_{\rm bit})$
copy statement matches the single-copy upper and collective-copy lower bounds.
It explicitly excludes preparation-and-inverse access from that lower bound.

C-350 preserves the distinction between one-step compression and compression
of all powers. The characteristic polynomial, return series, fresh-bath
trajectory, and truncated-geometric measured output agree verbatim with the
accepted mathematical formulas. The natural-output definition excludes an
arbitrary later quantum circuit, so no broader dequantization result is implied.

C-351 restricts its exact classical terminal algorithms to the rational
nonnegative coefficient family, input $|D-1\rangle$, and $2\le m<D$.
These are precisely the assumptions needed for the polynomial-size support
and polynomial-bit arithmetic. Its generic complex-coefficient copying
diagnostic uses conjugated root columns. The root-authored independent
verdict accepts the compiler and the full same-output classical attack;
the integration does not call that compiler a new quantum mechanism.

C-352 uses the conservative variance $9k$, rather than overstating an optimal
constant. The full working-bit budget includes seed storage, temporary dot
products, products at query time, and group sums. It agrees with the accepted
precision repair. The fixed seed-independent query list and absence of an
unrestricted adaptive-query claim are both preserved.

**RESOLVED MINOR I1 — normalize the separate homogeneous coordinate explicitly.**
D-R5-JET-SOURCE originally described a separate vector $u_0$ spanning a
homogeneous coordinate register. The source memo explicitly uses
$u_0=|0\rangle$ orthogonal to the affine register.

**FIX DEMAND:** State that $u_0=|0\rangle$ is a unit vector orthogonal to the
affine register. This makes the source normalization syntactically complete.
**RESOLUTION:** The canonical definition now explicitly calls $u_0=|0\rangle$
a unit vector and places its register orthogonally to the affine register.
This was reread and verified after the root edit.
**SURVIVING STATEMENT:** C-349 holds exactly with that intended basis vector.

**RESOLVED MINOR I2 — state seed independence for the stream as well as the query.**
D-R5-GRASSMANN-QUERY originally explicitly made only the late query independent of private
sketch randomness. Verdicts/grassmann-streaming-r5.md §4.1 also requires the
input stream to be independent of those seeds, as is standard for a fixed
input to the randomized sketch.

**FIX DEMAND:** Add that input-stream independence explicitly. A stream chosen
as a function of private seeds is not covered by the fixed-projector moment
calculation. No proof of a broader adversarial-stream theorem was supplied.
**RESOLUTION:** The canonical definition now begins with an explicit-coordinate
stream independent of private sketch randomness, in addition to the late-query
condition. This was reread and verified after the root edit.
**SURVIVING STATEMENT:** C-352 remains unchanged for the intended fixed or
seed-independent stream and seed-independent late query.

No new numerical checks were needed for this reference-and-quantifier audit.
The earlier bounded probes remain support for their respective symbolic
arguments; no numerical test was treated as proof of the integrated rows.
