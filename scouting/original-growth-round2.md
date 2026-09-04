# Original-construction round 2: graded quotient transport

2026-09-04. Conventions C1--C12 apply; only kernels, not presentation-dependent
gaps, enter the identities. The input is a homogeneous ideal given by its generators.
Objects use D-ground-space and D-compressed-multiplication. Proposed definitions at
the end are local pending an orchestrator merge. No literature search was used.

This is an attempted new preparation mechanism, not a qualifying new algorithm.
Neither historical originality nor a speedup is established. Two exact identities
survive; the proposed free retry and universal rapid-mixing conclusions do not.
Filtering a projector or invoking a generic Gibbs sampler would not itself meet D22.

## 1. Intended computational result

Given a succinct generating tuple, degree N and target accuracy epsilon, prepare
the uniform mixed state on W_N, or estimate a specified bounded observable in that
state. All costs of obtaining the quotient projectors must be counted. The intended
advance would be a preparation cost polynomial in input size, N and 1/epsilon on
a family where h_N/M_N is exponentially small and the same observable is not known
to be classically easy. Preparing a state is not compared with printing its density
matrix. A scalar-output claim needs a matched classical scalar-output baseline.

The proposed new ingredient was local growth between successive quotient spaces,
with recovery after rejection. The full recovery procedure has not been constructed.
Boson addition and projection are existing physical operations. Merely composing
them is not a D22 novelty claim; any original advantage would have to come from
the presently missing recovery/transport mechanism and its resource theorem.

## 2. Exact growth identity

ASSUME a proper homogeneous ideal and h_N,h_{N+1}>0. Use D-OR-QUOTIENT-GROWTH.
PROVE the successful growth channel takes rho_N exactly to rho_{N+1}.

2.1 Annihilation preserves the inverse system:
`a_j W_{N+1} subset W_N`, since `<a_j u,v>=<u,z_j v>=0` for v in I_N.
This uses D-ground-space, D-mode-operators, and the ideal property.

2.2 Consequently `P_N a_j P_{N+1}=a_j P_{N+1}`. Summing the adjoint products gives
`sum_j Z_{j,N} Z_{j,N}^dagger = (N+1) P_{N+1}`. The only remaining operator is
`sum_j a_j^dagger a_j`, whose restriction to degree N+1 is N+1.

2.3 Boson addition averaged over the mode label is a channel:
`E_N(rho)=sum_j a_j^dagger rho a_j/(N+n+1)`, since
`sum_j a_j a_j^dagger=(N+n+1) 1` on degree N (there are n+1 modes).
Successful projection of E_N(rho_N) gives
`(N+1) P_{N+1}/((N+n+1)h_N)`. Therefore

`q_N=(N+1)h_{N+1}/((N+n+1)h_N)`, and the conditional state is `rho_{N+1}`.

2.4 Starting at vacuum, the probability that N successive growth steps all succeed is
`product_{k=0}^{N-1} q_k = h_N/binom(N+n,n)`.
Thus simple restart from vacuum recovers the original small acceptance probability.
For `(x_1^2,...,x_d^2)` at N=d, it is `1/binom(2d-1,d)`.

## 3. Why local retry is not an algorithm yet

ASSUME the source POVM effect in D-OR-QUOTIENT-GROWTH. Consider its explicit Lüders
instrument, which is a legitimate minimally disturbing realization of that effect.
PROVE the rejected source is not generally rho_N.

3.1 Take I=(x^2) in C[x,y], N=1. In the ON source basis (x,y), W_1 is all of R_1;
W_2 has ON basis (xy,y^2/sqrt(2)). Compressed addition has source acceptance effect
`E=diag(1/3,1)`. This follows directly from the Fock raising coefficients 1 and sqrt(2).

3.2 Starting from rho_1=1/2, the failure probability is 1/3. Under the Lüders
instrument the conditional source is `|x><x|`, not rho_1. Retrying without recovery
changes both the next acceptance probability and its output distribution.

3.3 This is not an impossibility theorem for every recovery map. Here the ideal is
explicitly tiny and rho_1 can trivially be reset. What is refuted is the assertion
that the successful-channel identity alone supplies cost-free source recovery.
For a general succinct quotient, preparing rho_N afresh is the original problem.

3.4 A candidate recovery theorem must specify actual Kraus operators, preserve the
desired state after arbitrary failure histories, and bound their implementation and
success costs. Giving a projector, an unknown-basis twirl, an amplitude-amplification
routine or a fresh rho_N oracle does not meet this requirement or D22.

## 4. A different transport construction: a reservoir for the Hilbert series

ASSUME finite cutoff K and 0<t<1, and the projected raising/lowering jumps in
D-OR-HILBERT-RESERVOIR. PROVE rho_t is stationary.

4.1 Let Z_j raise degree by one, truncated at K. Set
`L_t = sum_j (D[sqrt(t) Z_j] + D[Z_j^dagger])`,
where `D[J](rho)=J rho J^dagger - {J^dagger J,rho}/2`.

4.2 On adjacent degree blocks rho_t has weights t^N and t^{N+1}. For every raising
block Z from W_N to W_{N+1}, the two dissipators cancel separately on both blocks:
upward gain is `t*t^N Z Z^dagger`, downward loss is `t^{N+1} Z Z^dagger`, and
the two terms on W_N cancel similarly. Hence `L_t(rho_t)=0` exactly.

4.3 Measuring degree in rho_t returns
`Pr(N)=h_N t^N / H_{I,K}(t)`. Conditional on N, the state is rho_N.
This could bypass one-shot ambient rejection only if mixing, implementation,
cutoff and degree-selection costs are all polynomial on an explicit hard family.
Stationarity supplies none of those bounds.

4.4 The projected jumps are not bare photon creation and loss. Realizing them needs
the quotient protection/projectors. A Zeno or reservoir-engineering proposal must
prove its approximation and rate/error bounds; a large penalty is not free.
Generic quantum Gibbs sampling is an existing algorithmic framework, not an
originality certificate for this construction.

## 5. Radical quadratic ideals already obstruct universal rapid mixing

ASSUME `I=(x_i y_j:1<=i<=a,1<=j<=b)` in C[x_1,...,x_a,y_1,...,y_b]. This ideal is
radical: it is the intersection of the two coordinate prime ideals. Its projective
variety is a disjoint union of two coordinate linear spaces. There is no nilpotent
pathology in this example.

5.1 The inverse-system basis consists of vacuum, x-only monomials and y-only monomials.
Degree populations on each branch form an invariant classical chain for the reservoir:
on a branch with r variables, upward rate at degree k is `t(k+r)` and downward rate
is k. The only route between branches passes through vacuum.

5.2 At cutoff K define
`Z_a=sum_{k=1}^K binom(k+a-1,k)t^k`, similarly Z_b. Stationary weights are
`pi(vac)=1/(1+Z_a+Z_b)` and `pi(left)=Z_a/(1+Z_a+Z_b)`.
The flux from the left branch to vacuum is `ta/(1+Z_a+Z_b)`.

5.3 For the centered indicator of the left branch, the Dirichlet-form/variance ratio is
`ta/[Z_a(1-pi(left))]`. By the variational principle, this bounds the population
generator's gap above, and therefore rules out a larger uniform gap for the whole
quantum generator (the classical diagonal subspace is invariant).

5.4 Set t=1/2, b=2a, K=8a. Already the k=a summand gives
`Z_a >= binom(2a-1,a)2^{-a} = Omega(2^a/sqrt(a))`, while pi(left)<1/2.
Hence the gap is at most `O(a^{3/2}2^{-a})`. Generator degrees are two; variable
count and cutoff are linear in a. A universal polynomial mixing guarantee is false.
This is a worst-initial-state obstruction; it does not by itself prove an exponential
mixing time from vacuum for every family. The asymmetric example motivates that
separate question, but no vacuum-start lower bound is claimed here.

5.5 This family is also classically easy. It is a counterexample to a generic
mixing theorem, not evidence for a quantum advantage. A useful restricted family
would need geometric hypotheses that both remove this bottleneck and leave a hard
classical task. On monomial ideals the reservoir itself is a classical occupation
process and cannot supply the new quantum mechanism sought in D22.

## 6. Bounded computations and candidate disposition

`checkers/explore/quotient_growth.py`, run 2026-09-04 with a 60-second bound and one
BLAS thread, exits 0: 137 checks. It verifies the growth identity for a nonreduced
ideal, a conic, a complex quadric and a twisted cubic; the explicit failure posterior;
truncated reservoir stationarity; and exact detailed balance/variational bounds in
the population chain. This is finite verification, not proof or a claim-status upgrade.

At d=16 and 32 the complete-intersection final success probabilities are
3.327342e-9 and 1.0913313e-18. For (a,b)=(4,8),(8,16),(12,24),(16,32), with K=8a,
the variational gap upper bounds are 0.141146, 0.01574731, 0.001465559, 0.000122074.
All three mutations in checkers/MUTATIONS.md exit 1: incorrect Fock coefficients,
incorrect temperature amplitude, and scalarized rejection effect.

Two research questions remain, not two algorithms: construct an equation-level
local recovery map with polynomial cost; or prove a useful mixing/degree-selection
theorem for a non-monomial family using a new mechanism. Neither has a specified
hard family or an established classical separation. They are not north-star hits.

## MERGE PROPOSAL — definitions

### D-OR-QUOTIENT-GROWTH
For D-ground-space let W_N=ker H_N, P_N its projector, h_N=dim W_N>0,
rho_N=P_N/h_N and M_N=binom(N+n,n). Define
`Z_{j,N}=P_{N+1}a_j^dagger P_N`. Normalized boson addition is
`E_N(rho)=sum_j a_j^dagger rho a_j/(N+n+1)`. Its success event is projection onto
W_{N+1}; its source POVM effect is `sum_j Z_{j,N}^dagger Z_{j,N}/(N+n+1)`.
The Lüders realization of a POVM effect E has Kraus operators sqrt(E),sqrt(1-E).
Source: this memo §§2--3; no historical novelty assertion.

### D-OR-HILBERT-RESERVOIR
On `W_{<=K}=direct_sum_{N=0}^K W_N`, let `Z_j=sum_{N<K}Z_{j,N}` and
`L_t=sum_j(D[sqrt(t)Z_j]+D[Z_j^dagger])`, 0<t<1, with D as in §4.1.
Set `H_{I,K}(t)=sum_{N=0}^K h_N t^N` and
`rho_t=H_{I,K}(t)^{-1} sum_N t^N P_N`. Implementation of Z_j is part of any
algorithmic cost, not supplied by the definition.
Source: this memo §§4--5; no historical novelty assertion.

## MERGE PROPOSAL — claims

### C-NEW-OR-GROWTH
- statement: For every proper homogeneous ideal and N with h_N,h_{N+1}>0,
  successful D-OR-QUOTIENT-GROWTH applied to rho_N has probability
  `(N+1)h_{N+1}/((N+n+1)h_N)` and output rho_{N+1}. N consecutive successes
  from vacuum have probability h_N/M_N.
- status: CONJECTURE
- depends-on: D-ground-space, D-mode-operators, D-OR-QUOTIENT-GROWTH
- where-proved: scouting/original-growth-round2.md §2 (derivation, not ratcheted)
- where-tested: checkers/explore/quotient_growth.py, growth

### C-NEW-OR-FREE-RETRY
- statement: For every homogeneous ideal, the Lüders failure branch of the
  D-OR-QUOTIENT-GROWTH source effect preserves rho_N, so the same source may be
  retried without recovery or fresh preparation.
- status: REFUTED
- surviving statement: The success identity C-NEW-OR-GROWTH holds, but the failure
  posterior for I=(x^2), N=1 is |x><x| instead of 1/2. A different recovery map
  requires its own implementation and cost analysis.
- depends-on: D-OR-QUOTIENT-GROWTH
- where-proved: scouting/original-growth-round2.md §3
- where-tested: checkers/explore/quotient_growth.py, recycling

### C-NEW-OR-HILBERT-RESERVOIR
- statement: For every proper homogeneous ideal, finite K and 0<t<1,
  D-OR-HILBERT-RESERVOIR has stationary state rho_t. Degree measurement in that
  state has probabilities h_N t^N/H_{I,K}(t), conditional state rho_N.
- status: CONJECTURE
- depends-on: D-OR-QUOTIENT-GROWTH, D-OR-HILBERT-RESERVOIR
- where-proved: scouting/original-growth-round2.md §4 (derivation, not ratcheted)
- where-tested: checkers/explore/quotient_growth.py, thermal

### C-NEW-OR-UNIFORM-MIXING
- statement: D-OR-HILBERT-RESERVOIR at t=1/2 has a spectral gap bounded below by
  an inverse polynomial in variable count and cutoff for every radical quadratic
  monomial ideal.
- status: REFUTED
- surviving statement: For I=(x_i y_j), with a x-variables, 2a y-variables and
  K=8a, an invariant population sector has gap at most O(a^{3/2}2^{-a}).
  Stationarity survives; restricted-family and vacuum-start mixing need separate
  analysis, and monomial reservoirs are classically simulable.
- depends-on: D-OR-HILBERT-RESERVOIR
- where-proved: scouting/original-growth-round2.md §5
- where-tested: checkers/explore/quotient_growth.py, bottleneck
