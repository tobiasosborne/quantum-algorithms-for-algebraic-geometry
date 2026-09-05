# Independent audit of the sparse trinomial reconstruction probe

2026-09-05. Root reviewed the other agent's construction, rather than authoring
its proof. Scope: `scouting/reconstruction-mechanism-r5.md` sections 1--7.
The mathematical and access audit passes; no FATAL or MAJOR objection remains
in that scope. This is not a historical priority or north-star verdict.

## 1. Exact operation and circuit normalization

For `f=x^D-a x-b`, all products of two basis monomials have exponent at most
`2D-2`, so one remainder step suffices. The three adjoint terms have disjoint
fixed-sum supports within each branch and norm at most `sqrt(D)`. Their linear
combination has the stated `sqrt(D)(1+|a|+|b|)` normalization. The omitted
`a` branch at output index zero and `b` branch at index `D-1` are essential.
The conjugated evaluation column obeys the copying identity for complex
coefficients; the unconjugated column generally does not.

The preparation uses explicitly computed integer sums and interval flags.
No root list, quotient table, metric whitening, or preparation inverse for an
unknown root state is smuggled into the equation-level circuit. The classical
coordinate bit lengths and coefficient rotations are included in the cost.

## 2. Constant-probability diagnostic family

For `0<=a<=1/4,b=1,D>=4`, the radius inequalities give
`9D/16<=nu_z^2<=9D/4`, hence `p_z>=1/9`. The fixed-point map in section 3
maps the complex disk of radius one half into itself: its logarithm has
magnitude at most `-log(1-e^(1/8)/4)<1/2`. Its derivative has magnitude less
than `0.1`. The angular disks for the `D` labels are disjoint modulo a full
turn, so the constructed roots are distinct and exhaust the polynomial.
This is a legitimate efficient classical sampler for the uniform-root
diagnostic, although not a simulation of arbitrary unknown root superpositions.

## 3. Same terminal output and finite-bit costs

For the input basis vector `|D-1>`, associativity makes a tuple amplitude
depend only on its total exponent `s`. A reduction path with `k` steps and
`j` uses of `a x` starts at `(k+1)D-1-j`. Every ordering is valid: until
the final reduction its exponent exceeds `D-1`. The resulting binomial
weight in equation (9) is therefore exact. For `m<D`, the different `k`
support intervals are disjoint and contain only `O(m^2)` total exponents.

The inclusion-exclusion count in equation (10) is the coefficient of
`(1+x+...+x^(D-1))^m`. Sampling its cumulative conditional counts constructs
a uniform bounded composition without enumerating `D^m` tuples. Common
rational denominators and binomial coefficients have polynomial bit length
in `m,B,log D`, so exact arithmetic handles any cancellations. The positive
contribution at `s=D-1` prevents a zero normalizer. The same calculation gives
the quantum herald probability, not merely a related classical observable.

## 4. Retained failures and originality scope

Completeness of an all-branches copier gives the displayed Gram identity;
Cauchy--Schwarz rules it out for distinct overlapping root states. This
does not forbid useful failures with a different retained state. Likewise,
polar whitening changes the map and cannot be inserted for free.

The prose distinguishes known finite-set probabilistic cloning and linear
combination machinery from the specific sparse compiler and classical
sampler. It makes no unsupported assertion that an earlier paper printed
the particular trinomial circuit. Even if those details are historically
new, the sampler removes the claimed advantage for the precise terminal
experiment, and the construction does not meet PRD criterion 6.

## 5. Corrected minor objection

**MINOR, resolved:** the numerical-test range contained the malformed clause
`2<=m<=4<m+D`.

**FIX DEMAND:** state the actual bounded range `2<=m<=min(4,D-1)`.

**SURVIVING STATEMENT:** the supporting finite tests are separate from the
general symbolic proof and do not establish originality. The author applied
the correction. No check of unrelated repository code was required.
