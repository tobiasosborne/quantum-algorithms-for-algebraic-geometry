# R11 higher-obstruction scattering: an exact finite construction

2026-09-07. Candidate R09, derived by root after the broad portfolio. Canonical
objects are D-R11-CE-CUBIC-SCHEME, D-R11-CE-FOCK-SUPERCHARGE and
D-R11-CE-SCATTERING-OUTPUT in `definitions/ce-scattering.md`. This is an
explicit diagnostic for the proposed many-body homological-transfer mechanism.
No claim is promoted without the independent tournament review.

## 1. Why try this operation

The strongest unresolved geometry proposal sums rooted trees for higher
Kuranishi obstructions. Summing exponentially many written trees is not a
classical lower bound: a coefficient recurrence can reuse the same subexpressions.
The new attempt is to realize the transfer directly in a physical supercharge,
where pair-merging interactions and virtual contractible modes generate higher
operations. It must produce a measurable signal at a charged evolution time.

For a dg Lie algebra, shifting degree-one directions to even variables and
degree-two directions to odd variables produces a Chevalley--Eilenberg
coderivation with linear and pair-merging parts. In the central degree-two
example below, nilpotence follows directly from anticommuting fermion creators
and commuting polynomial annihilators; no infinite-dimensional formal path
integral is required. The positive Hilbert space and its finite invariant sector
are specified in the definitions.

## 2. Exact algebraic and physical calculation

1. ASSUME D-R11-CE-CUBIC-SCHEME with `g>0`. Solving its first relation gives
   `U=-(g/sqrt(6))X²`. Substitution into the second gives
   `-(g²/sqrt(6))X³=0`. Hence the quotient is `C[X]/(X³)` and has length three.
   This is an actual nonreduced affine scheme. It is not a claim about the
   deformation space of every smooth complex surface.
2. On D-R11-CE-FOCK-SUPERCHARGE, the two bosonic polynomial factors commute.
   Expanding the square of `Q_g`, the two cross terms cancel by fermionic
   anticommutation and the repeated-creator terms vanish. Thus `Q_g²=0`.
   Each summand preserves `W`, so restriction to `W=3` is exact, not a truncation
   that discards outgoing amplitude.
3. The nonzero maps of `Q_g` on that sector are

       Q_g e0=g e1,     Q_g e2=e1+g e3.

   Here `a_x²|3_x>=sqrt(6)|1_x>`, which is why the coefficient in the
   definition is `g/sqrt(6)`. Both odd vectors are killed by `Q_g`.
4. In the even basis `(e0,e2)` and odd basis `(e1,e3)`, the differential is

       F(g)=[[g,1],[0,g]].

   At zero coupling, `e2 -> e1` is a contractible pair and `e0,e3` are
   harmonic. Eliminating the contractible pair in this supplied splitting
   gives the endpoint map `-g²`. It is the Fock-normalized version of the
   cubic residual in step 1, not a free general Gauss--Manin or Massey oracle.
5. The physical Hermitian generator, in the ordered occupation basis, is

       H_g=[[0,g,0,0],[g,0,1,0],[0,1,0,g],[0,0,g,0]].

   This exact four-state chain includes every reverse transition. Its endpoint
   probability is not inferred by substituting the formal effective coupling
   into a two-state model at arbitrary `g`.

## 3. Complete scattering probability and time scale

Put `Omega=sqrt(1+4g²)`. Reflection-symmetric and antisymmetric endpoint
combinations reduce `H_g` to the two `2 x 2` blocks
`[[0,g],[g,1]]` and `[[0,g],[g,-1]]`. Exponentiating them gives

    <e3|exp(-itH_g)|e0>
      = i[cos(t/2) sin(Omega t/2)/Omega
          - sin(t/2) cos(Omega t/2)].

The squared modulus is the exact common output for every `g,t>=0`. At short
times the amplitude starts at `i g² t³/6`: three physical hops are required.
This need not equal `i sin(g²t)` outside the long-time, small-coupling
effective regime.

The four eigenvalues are `+/- (Omega+1)/2` and `+/- (Omega-1)/2`. In particular
the small singular/energy scale is `(Omega-1)/2=g²+O(g^4)`. For small `g`,
the exact amplitude can also be written

    (i/2)[(1/Omega-1) sin((Omega+1)t/2)
             +(1/Omega+1) sin((Omega-1)t/2)].

The fast term has amplitude `O(g²)` and the slow term varies on time `Theta(g^-2)`.
Thus an order-one transition in this fixed middle-coupling normalization needs
time `Omega(g^-2)` as `g` tends to zero. This conclusion follows from the exact
two-frequency expression; it is scoped to this family and fixed energy scale.

There is a resonant escape from small-coupling perturbation theory: at
`g=sqrt(3)/2`, `Omega=2` and `t=pi` the endpoint amplitude is exactly `i`,
so the transition succeeds with probability one. No postselection or thermal
state is needed. The operator norm is `3/2` at that parameter, and all four
physical states must remain coherent during the run.

## 4. Tournament attack on the apparent escape

At the resonant parameter, the couplings are `(sqrt(3)/2,1,sqrt(3)/2)`.
They are exactly the spin-`3/2` angular-momentum `J_x` matrix in its magnetic
basis. Rotation by `pi` performs the endpoint transfer. The same weighted chain
is the known perfect-state-transfer spin network. This is an explicit
operation-and-resource identification, not rejection because the construction
uses elementary gates.

The classical common-output algorithm evaluates the two-frequency expression
in Section 3, or exponentiates the supplied `4 x 4` matrix. The scheme's length
is also obtained by the two substitutions in Section 2. Neither output has
an asymptotic speedup here. The resonant physical signal is a valid small
experiment connecting a cubic local scheme to a supersymmetric chain; it does
not meet D22.

Targeted primaries fetched after these derivations:

- [Christandl, Datta, Ekert and Landahl, Perfect state transfer in quantum spin
  networks, quant-ph/0309131](https://arxiv.org/abs/quant-ph/0309131): weighted
  spin-chain transfer is the specific operation comparator.
- [Arvanitakis, Hohm, Hull and Lekeu, Homotopy Transfer and Effective Field Theory I,
  arXiv:2007.07942](https://arxiv.org/abs/2007.07942): effective higher operations
  from integrating out contractible directions are established mathematics.
- [Tree-level Scattering Amplitudes via Homotopy Transfer,
  arXiv:2312.09306](https://arxiv.org/abs/2312.09306): a classical recursive
  treatment is part of the comparison, not enumeration of all printed trees.

## 5. What a growing-family continuation must change

The finite example settles a normalization and time question but does not settle
the proposed general algorithm. A substantive continuation would need an actual
growing family of deformation complexes with nontrivial interacting tree paths,
a uniformly compiled Hermitian generator or trace-preserving instrument, and a
specific common output that the best classical recurrence cannot compute at the
same cost. The input cannot be an already-solved minimal model.

One concrete attempt is irreversible pair-merging with a single jump
`J=sum mu^k_ij a_k†a_i a_j`, retaining coherent alternatives. Conditional on
`m-1` jumps, one might hope to realize the required `m`-linear tree operation.
But the no-jump propagators are `exp(-t J†J/2)`, generally not scalar on the
particle-number sectors. They reweight the tree histories. Different bath
labels may instead reveal the chosen pair and destroy the desired interference.
Any next derivation must include those exact no-jump maps and every label.

Known homotopy transfer alone does not prove a quantum algorithm, and a known
general Hamiltonian-simulation routine alone is not enough to refute originality
of every possible future protocol. For this explicit resonant construction,
however, the perfect-state-transfer reduction and constant-size classical
algorithm are already decisive.
