# Classical algorithms and complexity targets for extra Picard classes

2026-09-08. Requested classical-baseline investigation, with an explicit Boolean
encoding added after user steering. This uses classical coefficient bits and
marked periods, not the earlier fixed quantum-source interface. Canonical inputs
are in `definitions/picard-classical-r15.md`. New deductions enter C-382--C-385
as SKETCH pending independent campaign review. The source ledger is
`refs/picard-classical-r15.md`.

Final user steering, D27: NP-completeness rejects a candidate quantum algorithm.
The Boolean/Picard construction below is therefore retained only as a negative
control. The connected quartic K3 problem has not been classified as NP-complete
by this investigation. No new quantum algorithm is claimed. The user has stopped
this session; remaining proof questions are recorded for a later explicit request.

## 1. The selected problem

Given a smooth quartic surface X=V(F) over Q by its 35 binary integer
coefficients, decide whether its geometric Picard rank is greater than one.
An extra divisor class changes the surface's available curves, fibrations and
divisor geometry. The output is an exact bit. Computing a full Gröbner basis,
an entire Picard lattice, or a large list of curves is a stronger output.

The question is D-QUARTIC-EXTRA-PICARD-CLASS. It has input length L, fixed
degree four and fixed cohomology rank22; after the hyperplane class is removed,
the period-relation lattice has rank21. Large intermediate numbers and unknown
certificate sizes can still make the problem difficult. They cannot be replaced
by a claim that its final linear-algebra matrix has exponential dimension.

The review identifies no established polynomial-time classification or
NP-intersect-coNP theorem for this exact input problem. That is a statement
about the checked literature, not a proof that no such result exists. The
missing bounds are research targets, not reasons to discard the direction.

## 2. What the strongest relevant classical methods actually do

| Method | Computation and evidence | Resource questions that remain |
|---|---|---|
| Explicit divisors | Enumerate/find curves or divisor representatives and compute their intersection pairing. Independent classes give lower bounds on Picard rank. Gröbner and Hilbert-scheme calculations can occur here. | Degree and height of a necessary divisor, its field of definition, elimination cost and certificate size; no uniform polynomial bound is supplied by an observed example. |
| Reduction at good primes | Compute Frobenius on second cohomology, use its Tate-class factors for upper bounds, and compare discriminant square classes from different reductions when needed. | Finding a suitable prime, Frobenius computation and field/precision costs. Real multiplication can force rank jumps, so a convenient reduction is not universal. |
| Single-prime crystalline obstruction | Compute which Tate classes of a reduction can lift through the Hodge filtration; Galois decomposition improves the upper bound. | Usually Frobenius computation dominates, followed by controlled p-adic precision. A vanishing obstruction modulo a large power is not an exact zero certificate. |
| Complex periods and lattice reduction | Compute marked periods by differential equations/analytic continuation and recover integer relations using lattice methods. Modern Picard–Lefschetz algorithms also compute an explicit homology basis. | Path selection, period precision, relation height and certification; a stable numerical lattice is not automatically the complete exact Picard lattice. |
| General Néron–Severi algorithms | Compute enough finite cohomological/Galois information and algebraic cycles for an exact terminating procedure. | A computability theorem is not a polynomial bit-complexity theorem. |

Two details materially change the comparison. First, the older Charles algorithm
has conditional termination in its Theorem5, and its Theorem1 explains forced
specialization jumps. Second, Poonen--Testa--van Luijk Theorem8.38 gives an
UNCONDITIONAL algorithm for K3 Néron–Severi groups over finitely generated
fields of characteristic not2. Reading only either abstract would miss this
distinction. [Charles](https://arxiv.org/abs/1111.4117),
[Poonen--Testa--van Luijk](https://math.mit.edu/~poonen/papers/compute_ns.pdf).

For a concrete implementation baseline, use the certified crystalline upper
bound together with exact lower-bound divisors, or combine those with a period
calculation suggesting the lattice. A new quantum method must be compared with
this combined workflow, rather than only with general Gröbner elimination.

## 3. What has actually been computed

Lairez--Pichon-Pharabod--Vanhove's 2024 method reports computing hundreds of
digits of periods of a smooth complex quartic in typically about an hour on
a laptop. This is period computation, not a uniform complexity theorem for
the exact Picard-rank decision.
[Primary paper](https://arxiv.org/abs/2306.05263).

Costa--Sertöz tested their upper-bound method on 184,725 quartics. The reported
Galois-obstruction computations took about10CPU-months in aggregate, versus
about16 for their vanilla obstruction comparison; their roughly32CPU-month
van-Luijk figure is an estimate. These are database-specific results, not
worst-case bounds in coefficient bit length. Their precision example5.6 also
shows why a fixed number of p-adic digits cannot work uniformly over all
inputs. [Primary paper, examples5.5--5.6](https://arxiv.org/abs/2003.11037).

The classical software is concrete:

- [PeriodSuite](https://github.com/emresertoz/PeriodSuite) combines SageMath and
  Magma. Its documentation explicitly distinguishes numerical Hodge lattices
  from certified exact answers and notes strong dependence on the deformation path.
- [crystalline_obstruction](https://github.com/edgarcosta/crystalline_obstruction)
  computes rigorous upper bounds from finite-precision obstruction data.
- [lefschetz-family](https://github.com/ericpipha/lefschetz-family) implements
  the modern Picard–Lefschetz period/homology approach.

These packages and the cited benchmarks were inspected, not rerun here.
No claim about the fastest implementation on every input follows from them.

## 4. A useful classical complexity deduction

The bounded search remaining after certified period data are supplied is
classically polynomial for fixed lattice dimension. This is more informative
than counting `(2H+1)^21` potential relation vectors.

In D-BOUNDED-SEPARATED-PERIOD-RELATION, true pairings either vanish or have
real/imaginary maximum magnitude at least g. The delivered approximations have
coordinate error at most g/(4mH). For every integer vector in the height box,
the pairing error is at most g/4. Consequently exact zero is equivalent to

    -H<=z_i<=H,
    |a.z|<=g/2,  |b.z|<=g/2,
    z is a nonzero integer vector.

Exclude zero with 2m cases `z_i>=1` or `z_i<=-1`. Each is an integer linear
feasibility problem with a FIXED number m=21 of variables, so Lenstra's theorem
applies. Its cost is polynomial in the actual bit lengths of the rational
period approximations, H and g. The full derivation is in
`argument/bounded-period-relations-r15.md`.
[Lenstra's theorem](https://doi.org/10.1287/moor.8.4.538).

This does not put the original quartic problem in P. One still needs to obtain
a sufficient H, a certified separation g, the integral marking and the periods
at the requested precision. A small formula describing g does not supply a
long precision string for free. The fixed-dimension result also does not apply
when the number of cohomology coordinates grows as part of a different input.

## 5. Where the large precision costs appear

Lairez--Sertöz give, for a fixed quartic and chosen period basis, a computable
constant c which can be enlarged above1, with

    z.pi=0 or |z.pi| > 2^(-c^(max_i |z_i|^9)).

The nested exponent is essential. A sufficient precision from this bound is
roughly c^(H^9) bits, before accounting for the surface-dependent constant and
marking. This is a sufficient bound, not a lower bound on every algorithm.
Their section4.4 analyzes testing one given class on a FIXED surface and gives
an exp(Delta(class)^O(1)) bound; it does not provide a uniform polynomial
classification as the quartic input varies. It also discusses a conjectural
improvement to that classical bound.
[Separation theorem and complexity discussion](https://arxiv.org/abs/2011.12316).

This locates a meaningful target for a quantum proof: derive a different
geometric procedure that avoids the expensive certification/precision step,
and compare it with both the period and arithmetic routes. Merely applying
QSVT to a 21-dimensional numerical matrix does not address that bottleneck.

## 6. What NP intersect coNP would require

There are plausible TYPES of evidence on both sides, but their existence is
weaker than a complexity-class membership theorem.

For a YES answer, an explicitly represented divisor D with
`det [[h²,h.D],[h.D,D²]] !=0` proves a class independent of h. A polynomial
certificate theorem needs bounds on all representation sizes and a verifier:
curve equations, field degree, coefficient heights, Cartier/containment data,
intersection computation and the bit cost of checking them.

For a NO answer, a certified upper bound rho<=1 suffices because h exists.
Two rank-two reductions with incompatible discriminant square classes provide
one well-known certificate pattern; a suitable crystalline obstruction can
provide another. A polynomial certificate theorem needs bounds on the chosen
primes, extension and precision data, and verification cost. Charles's
specialization result prevents treating the simplest two-prime pattern as
universal without additional hypotheses.

This review therefore does NOT label the quartic problem NP-intersect-coNP.
The concrete research problem is whether both sides admit uniformly
polynomial-size, polynomially checkable certificates in coefficient bit
length, possibly on a useful declared subfamily. Certificate discovery may
still be hard even if verification is easy. If the chosen sufficient
certificates are themselves polynomially enumerable and computable, the
subfamily could instead be in P; that possibility must be checked as well.

A simple YES control is

    F=x0³x2+x1³x3+x2⁴+x3⁴.

The line x2=x3=0 lies on X. The gradient equations force all four coordinates
to vanish if X were singular, so X is smooth in projective space. The line
has self-intersection -2 and meets h in1, giving determinant `4*(-2)-1=-9`.
This is a short extra-class certificate. It supplies no worst-case height bound
and no evidence that difficult NO certificates are short.

## 7. What variable-dimensional integer programming can encode

The user's suggested reduction can be made explicit for a broader geometric
family. Start with binary A,b and Boolean feasibility Ax=b. Define the
projective quadratic scheme in D-BOOLEAN-PICARD-SURFACE:

    t(t-h)=0,
    x_i(x_i-h)=0,       (h-t)x_i=0,
    t(sum_i A_ji x_i-b_j h)=0.

There is one point with t=0 and x=0. At t=h=1, its other points are exactly
the Boolean solutions. There are no projective points at h=0, and the Boolean
coordinate algebra is a product of fields, so all points are reduced.
For Y=Z x P²,

    rho(Y)=1+#{x in {0,1}^v : Ax=b}.

The Segre embedding converts this into a polynomial-size list of ordinary
homogeneous quadrics, with no hidden elimination oracle. Thus deciding rho>1
on this syntactically encoded family is NP-complete. The full proof and exact
encoding details are in `argument/boolean-picard-encoding-r15.md`; C-385 remains
SKETCH until independently reviewed.

The restriction matters: these are smooth PROJECTIVE SCHEMES of pure dimension
two, generally disconnected, in growing ambient dimension. The hardness is
component counting. This is not an NP-hardness theorem for connected quartic
K3 surfaces, and it is not a quantum algorithm. A reduction preserving
connectedness, the K3 condition and a compact quartic input would be a separate,
substantive result. An abstract universality or blow-up argument cannot supply
its polynomial encoding for free.

For this NP-complete family, an additional coNP classification would imply
NP=coNP. A polynomial quantum solver would imply NP subset BQP. This explains
why generic integer-programming hardness and an NP-intersect-coNP research
target are different routes.

## 8. The super-exponential proposal and the simulation ceiling

For D-STANDARD-POLYNOMIAL-QUANTUM-COMPUTATION with m qubits and T local gates,
a classical state-vector simulation uses `2^m poly(T,m)` arithmetic work, with
polynomially many precision bits for constant decision error. With m,T both
polynomial in classical input length L, this is `2^poly(L)` time. Quantum
polynomial time is also contained in PSPACE. These statements apply regardless
of whether the quantum circuit uses QSVT, quantum walks or adiabatic techniques,
provided its full resources have been compiled and charged.
[Watrous's complexity account](https://arxiv.org/abs/0804.3401).

Consequences:

- A genuine requirement for more than `2^poly(L)` classical time is incompatible
  with a standard polynomial quantum algorithm for that SAME problem and input.
- A doubly exponential COST OF A KNOWN CLASSICAL METHOD is not such a lower
  bound. A polynomial quantum method could still exist; its classical
  simulation would itself establish a better `2^poly(L)` upper bound.
- Factorial time `L!=2^Theta(L log L)` is super-exponential relative to `2^L`
  but still within EXP. The terminology must be specified before invoking
  the ceiling.
- Printing a huge explicit Gröbner basis also costs its output length on a
  quantum computer. A scalar query or compressed output is a different task.

Unrestricted polynomial-ideal membership over Q is a sharper case: Mayr--Meyer
give exponential-space hardness and Mayr gives the matching EXPSPACE upper.
If that complete problem were in BQP, then EXPSPACE would be contained in
PSPACE, contradicting the deterministic space hierarchy. Thus generic ideal
membership cannot have a standard polynomial quantum algorithm. This is not
a dismissal of structured ideals, bounded-degree-piece observables, or other
restricted geometric problems; hardness must be transferred to their exact
encoding separately.
[Mayr--Meyer](https://doi.org/10.1016/0001-8708(82)90048-2),
[Mayr's matching upper](https://doi.org/10.1007/BFb0029002).

## 9. Resulting research programme

The earlier tournament used missing classical hardness too much as a stopping
condition. The correct workflow now is to identify the strongest classical
pipeline, prove the quantum resource bound, and separately develop a matched
hardness argument or explicitly stated complexity assumption. An upper bound
for one classical implementation is not a lower bound against all algorithms.
Conversely, lack of an unconditional lower bound is not a reason to stop:
proving superpolynomial lower bounds for a natural NP problem could itself
settle major open complexity questions.

For the selected quartic problem, the most concrete next investigations are:

1. Prove or refute polynomial certificate-size bounds on a specified surface
   family, including field, prime, relation-height and precision parameters.
   This is the route to an honest NP-intersect-coNP statement.
2. Determine the complexity of a useful CONNECTED quartic K3 subfamily, including
   whether a reduction from a suitable intermediate problem is possible. An
   NP-completeness result would reject that family under D27. The disconnected
   construction above identifies exactly what has not yet been preserved.
3. Measure the dominant costs on height-controlled quartic examples: period
   preparation and certified relation precision versus good-prime search,
   Frobenius computation and crystalline obstruction precision. Compare the
   same exact bit, not period approximation on one side and a complete Picard
   lattice on the other.

The quantum target remains open. This review replaces an unspecified classical
obstacle by exact computational tasks, a nontrivial classical upper for one
promised subproblem, an explicit generic geometric hardness encoding, and
concrete certificate/reduction obligations.
