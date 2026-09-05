# Constructive proof: support-to-Pluecker conversion by tableau steering

Read CLAUDE.md, PRD criteria 1--6/D22--D24 and HANDOFF.md. Root owns shared
files and tracking (`qaag-j8n`); no additional subagents. Write only
`scouting/support-plucker-r9.md`. This is a positive candidate to prove or
repair, not permission to assert a new mechanism before an independent audit.

Input: copies of a rank-r density matrix rho on H=C^q, known r and
lambda_min(rho|support)>=eta/r. The unknown support is U. Desired quantum
output: the unit Slater vector Omega_U in wedge^r U, up to global phase.
Desired classical output: sample a sorted r-subset I of computational
coordinates with probability det(P_U[I,I]) (the rank-r projection DPP).
No classical basis of U, preparation inverse, QRAM or amplitude queries.

Root's proposed algorithm and proofs to audit constructively:

1. Take N=ceil(2r^2/eta) copies. Weak Schur shape lambda has at most r rows.
   Under the Schur--Weyl/RSK distribution for the eigenvalue alphabet, having
   the decreasing subsequence r,r-1,...,1 guarantees r rows. Its waiting
   time has expectation sum_i 1/p_i <=r^2/eta. Markov therefore suggests
   Pr(length(lambda)=r)>=1/2. Check the convention and exact bound.
2. Obtain a known standard Young path/tableau b in the symmetric-group
   irrep, without disturbing the U(q) multiplicity space. Avoid assuming a
   full U(q) Schur transform is poly(log q). Use nested NONDEMOLITION weak
   Schur measurements on prefixes, or prove an equally efficient route.
   Generalized phase estimation with an S_k Fourier transform must copy
   only the shape and be uncomputed, giving the Lueders projector; merely
   discarding the other Fourier labels can depolarize the irrep.
3. Choose a standard tableau b0 of the same final shape whose first r boxes
   form the first column. Connect b to b0 by O(N^2) valid adjacent-number
   swaps, using connectivity of linear extensions of the Young-diagram poset.
4. For a valid adjacent swap s_k, Young's orthogonal form sends
   |b> to (1/d)|b>+sqrt(1-1/d^2)|s_k b>, with |d|>=2. Physically swap
   tensor registers k,k+1, then measure the prefix-k shape nondestructively.
   Success moves to s_k b with probability >=3/4; failure restores b.
   Repeat without replacing the input rho copies. All operations act only
   on the symmetric-group factor, leaving the support U unchanged.
5. At b0, the first r physical systems are in wedge^r H AND in U^tensor r,
   hence in the one-dimensional wedge^r U. Discard the other systems.
   Verify exact factorization for mixed post-Schur states, not only a pure
   highest-weight vector. Charge precision and capped feedback attempts.

Prove the actual q-efficient circuit and its complete resource bound.
Only basic controlled permutations, group transforms and prefix projectors
that are explicitly compiled may be used. A dimension-exponential Schur
transform or unnoticed postselection factor would invalidate the proposal.
The requested original mechanism is the measured-tableau steering and column
extraction; it may already be described as universal purification or quantum
Schur processing. Derive first, then targeted primary-source checks.

Root is independently studying the classical output baseline, and another
agent is assigned adversarial novelty/baseline work. Send exact obstacles or
the first successful proof early. A small diagnostic is r=2,q=3 or4,N=3:
for flat rank-two rho, shape (2,1) has probability1/2 and should yield the
unknown support singlet; direct two-copy antisymmetrization has probability1/4.
Do not compare only against that inferior quantum construction.
