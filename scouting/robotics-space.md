# Robotics SPACE claims, developed as a proposer (PRD D13)

Lane: `briefs/lane-robotics-space.md`. Date 2026-09-02. Author: Opus subagent, proposer role.
Read in order: `CLAUDE.md`, `PRD.md` (arms, D1-D14, §7), `definitions/definitions.md`
(conventions C1-C12 binding; this memo departs from none of them),
`claims/CLAIMS.md` "Critical claims" and C-255..C-263, `scouting/robotics-deep-dive.md`
(all, especially R1-R3 and K4, K5, K6), `scouting/real-variety.md` Routes 4 and 5,
K-RV7/8/9 and Questions 5 and 9, `scouting/classical-landscape.md` §1 and Traps.

Citations are arXiv ids or DOIs fetched during this pass. Anything not resolved is marked
`[UNVERIFIED]` with what specifically failed. Definition ids are cited, never restated (L2).

---

## 0. Bottom line, stated before the evidence

The existing space killers reach the right verdict on the wrong grounds, and the grounds
they miss are both sharper and more useful.

1. **The real ceiling is not `BQPSPACE = PSPACE`; it is `BQSPACE(s) ⊆ DSPACE(s^2) ∩ DTIME(2^{O(s)})`.**
   Chain: Watrous's dequantization `PrQSPACE(s) = PrSPACE(s)` (Comput. Complexity 12:48-84,
   2003, DOI 10.1007/s00037-003-0177-8) composed with Borodin-Cook-Pippenger
   `PrSPACE(s) ⊆ NC^2(2^s) ⊆ DSPACE(s^2) ∩ DTIME(2^{O(s)})` (Inf. Control 58(1):113-136, 1983,
   DOI 10.1016/S0019-9958(83)80060-6). Fefferman-Remscrim state the `s = log n` case verbatim as
   "`BQL ⊆ DSpace(log^2 n)`" (arXiv:2006.03530). Consequence, and this is the single most
   important sentence in this memo: **in any model where the input sits on a re-readable tape,
   a quantum space advantage can never exceed a quadratic gap in the space exponent, and the
   "`O(n log N)` qubits versus `M_N` classical words" comparison behind bet R1 is not a space
   separation at all.** The honest classical space for `lambda_min(A_N)` at `n = 100`, `r = 3` is
   `O(log^2 B_3) ≈ 300` bits, i.e. about 40 bytes: not 250 GB (seed R1), and not 28 MB (K-RV8).
   Both prior numbers are upper bounds for *time-efficient* algorithms and neither is a lower bound.

2. **What survives in the read-only-input model is a simultaneous (space, time) claim, not a
   space claim.** Quantum: `O(n log N)` qubits and `poly(n, N, 1/eps, 1/sqrt(w))` time under a
   guiding-state promise. Classical, best known: either `Theta(M_N)` words with
   `Theta(M_N)`-per-matvec time (implicit Lanczos, the K-RV8 baseline), or `O(log^2 M_N)` bits with
   `2^{O(log M_N)} = poly(M_N)` time (the Borodin-Cook-Pippenger route). No classical algorithm is
   known with `poly(n, log N)` space *and* `poly(n, N)` time, and none can exist unless
   `BQP = BPP`, provided the bosonic guided-local-Hamiltonian problem of C-NEW-SP-GLH-BOSONIC
   is BQP-hard. That conditional is the entire content of the surviving R1.

3. **The only UNCONDITIONAL quantum space separations known live where the input is consumed:
   streaming and one-way communication.** They exist because the Watrous simulation needs to
   re-read the input, and a stream cannot be re-read. This memo constructs what I believe is the
   first robotics-shaped instance: deciding whether a *streamed binomial ideal on the sign
   hypercube* is consistent (equivalently, whether a streamed 2-local Ising Hamiltonian is
   frustration-free) needs `Omega(sqrt(n))` classical bits of one-pass memory and `O(log n)`
   qubits, unconditionally, by reduction from Gavinsky-Kempe-Kerenidis-Raz-de Wolf
   (arXiv:quant-ph/0611209). Its robotics reading is loop-closure batch certification between two
   robots on a bandwidth-limited link. **Its quantum protocol is one photon in `n` modes with
   phase shifters and one beamsplitter** - the cheapest possible instance of the north star's
   linear-optics clause, and a close relative has already been run in the laboratory
   (DOI 10.1038/s41467-019-12139-z).

4. **The margins are honest and small.** `sqrt(n)` versus `log n` at `n = 10^4` is 100 bits
   versus 14 qubits (ratio 7.5); at `n = 10^6`, 1000 bits versus 20 qubits (ratio 50). The
   BQ_USPACE route buys a quadratic space gap, which is the theoretical maximum and is worth
   about `18` qubits versus `304` bits at the R1 sizes. Deployed sliding-window VIO uses 2.4 MB.
   Neither margin is an engineering product. The products on offer are a theorem (a
   BQ_USPACE-complete algebraic-geometry problem, the space analogue of C-124), an unconditional
   separation with an existing table-top realisation, and three negative results that close doors
   permanently.

5. **A finding that hurts more than any killer: bet R1's motivating premise is unsupported.**
   A dedicated pass over Yang-Carlone (arXiv:2109.03349), TEASER (arXiv:2001.07715), QUASAR
   (arXiv:1905.12536) and One Ring (arXiv:2006.06769) found **no published statement** that the
   level-2 moment relaxation is loose for robust perception while level 3 is out of reach.
   Yang-Carlone use the **lowest** order and report it empirically exact at 30-70 measurements.
   The one documented non-tightness is matrix-weighted noise (arXiv:2308.07275,
   DOI 10.1109/TRO.2024.3475220), whose authors' remedy is **redundant constraints at the same
   order**, not a higher order. So §2.1 aims at a wall nobody is known to have hit
   (C-NEW-SP-R1-PREMISE, KS4b), and unless such a family is exhibited the space direction reduces
   to the streaming claim alone.

Overall colour: the space direction is **not** exhausted, but it has been mis-stated. Its
strongest form is not "quantum needs fewer qubits than classical needs words". It is
"quantum sits at a point on the (space, time) Pareto frontier that classical provably cannot
reach unless `BQP = BPP`", plus "in a stream, quantum beats classical unconditionally".

---

## 1. Formal models in which a quantum space advantage is provable or plausible

### 1.0 The governing ceiling (this subsumes and sharpens K6)

**Fact SP-0.** For space-constructible `s(n) = Omega(log n)`,
```
BQSPACE(s)  subset  PrQSPACE(s) = PrSPACE(s)  subset  NC^2(2^s)  subset  DSPACE(s^2) ∩ DTIME(2^{O(s)}).
```
Sources: Watrous, "On the complexity of simulating space-bounded quantum computations",
Comput. Complexity 12:48-84 (2003), DOI 10.1007/s00037-003-0177-8, for the first equality
(the theorem is about a general "quantum stochastic process" model, so bounded error is a
special case, and no separate hypothesis on the quantum machine's running time is needed:
a halting space-`s` machine runs in `2^{O(s)}` steps because it cannot repeat a configuration);
Borodin-Cook-Pippenger, "Parallel computation for well-endowed rings and space-bounded
probabilistic machines", Inf. Control 58(1):113-136 (1983), DOI 10.1016/S0019-9958(83)80060-6,
for the rest, via parallel determinant/matrix-powering (the same well-endowed-ring machinery
behind Csanky, DOI 10.1137/0205040, and Borodin-von zur Gathen-Hopcroft,
DOI 10.1016/S0019-9958(82)90766-5).
`[PARTIALLY VERIFIED]`: the two primary PDFs could not be fetched in readable form; the
statements above are corroborated by consistent secondary summaries and, for the `s = log n`
case, by a direct quotation in Fefferman-Remscrim arXiv:2006.03530 ("BQL subset DSpace(log^2 n)").
The `DTIME(2^{O(s)})` half of the conclusion, rather than the weaker `2^{O(s^2)}` that would
follow from space alone, rests on the secondary summaries and should be re-verified before it
is quoted outside the repo.

**Three consequences that every space claim in this campaign must be tested against.**

(i) *No superquadratic space advantage exists in the read-only-input model.* If a quantum
algorithm uses `s` qubits, a deterministic classical algorithm uses `O(s^2)` bits. Therefore
"quantum: `O(n log N)` qubits; classical: `M_N = binom(N+n,n)` words" is a comparison of two
upper bounds, one of which is not the classical minimum. The classical minimum is
`O((n log N)^2)` bits, which is *smaller* than `M_N` by an exponential factor in `N`.

(ii) *The quadratic gap is achievable in principle and is exactly what quantum logspace buys.*
So `s` versus `s^2` is a target, not a nullity. K6 is stated at the wrong resolution to see this.

(iii) *The simulation costs `2^{O(s)}` time.* For `s = log_2 M_N` that is `poly(M_N)` - the same
order as one Lanczos sweep - so at fixed `N` the classical space collapse is essentially free.
For `s = O(n log N)` in the occupation encoding it is `N^{O(n)}`, which is not free. The
resolution is that the compact encoding (`ceil(log_2 M_N)` qubits) is the one that matters, and
under it the classical space is `O(log^2 M_N)` at `poly(M_N)` time.

### 1.1 Model (a): quantum logspace

What the class machinery buys, precisely.

- **Ta-Shma**, "Inverting well conditioned matrices in quantum logspace", STOC 2013,
  DOI 10.1145/2488608.2488720 (no arXiv posting found). An entry of `H^{-1}` for an `n x n`
  matrix with condition number `kappa <= poly(n)` is approximated to `1/poly(n)` additive error
  by a bounded-error quantum algorithm in `O(log n)` space, with intermediate measurements.
  Quadratic space improvement over the best known classical bound.
- **Fefferman-Lin**, "A complete characterization of unitary quantum space", ITCS 2018,
  arXiv:1604.01384, DOI 10.4230/LIPIcs.ITCS.2018.4. Two completeness theorems, both for
  `BQ_USPACE[O(k(n))]` (quantum circuits on `O(k)` qubits, unitary, measurement only at the end):
  - *`k(n)`-Well-conditioned Matrix Inversion* (their Def. 13): input is a size-`n` **efficient
    encoding** of a `2^k x 2^k` PSD matrix `H` with a *known* bound `kappa = 2^{O(k)}` and
    `kappa^{-1} 1 <= H <= 1`, plus indices `s, t`; promise `|H^{-1}(s,t)| >= b` or `<= a` for
    **constants** `0 <= a < b <= 1`.
  - *`k(n)`-Minimum Eigenvalue* (their Def. 17): input is a size-`n` efficient encoding of a
    `2^k x 2^k` PSD matrix `H` with `||H||_max = max_{s,t}|H(s,t)|` bounded by a constant;
    promise `lambda_min <= a` or `>= b` with `b - a > 2^{-O(k(n))}`.
  - *Efficient encoding* (their Def. 10): a classical algorithm specified by `n` bits which, on
    input a row index `i in {0,1}^k`, outputs the indices and contents of the nonzero entries of
    row `i` in `poly(n)` time and `O(k)` workspace. This forces row sparsity `<= poly(n)`.
  Also: `PreciseQMA = PSPACE`, and inverse-exponential-precision local-Hamiltonian min-eigenvalue
  is PSPACE-complete even frustration-free.
- **Fefferman-Remscrim**, STOC 2021, arXiv:2006.03530, DOI 10.1145/3406325.3451051:
  `BQUSPACE(s) = BQSPACE(s) = QUMASPACE(s) = QMASPACE(s)` for space-constructible
  `s = Omega(log n)`; a measuring space-`s` time-`t` algorithm becomes unitary in space
  `O(s + log t)` and time `poly(t 2^s)`. Hence `BQL = BQ_UL`: intermediate measurements are free
  in space-bounded quantum computation.
- **Girish-Raz-Zhan**, ICALP 2021, arXiv:2006.04880, DOI 10.4230/LIPIcs.ICALP.2021.73: all
  entries of `A^T` for a contraction `A` (`||A|| <= 1`) and `T <= poly(n)`, to arbitrary
  polynomially small additive error, in unitary quantum logspace.
- **Girish-Raz**, ITCS 2022, arXiv:2106.11877, DOI 10.4230/LIPIcs.ITCS.2022.76: time `T` space
  `S >= log T` with measurements and resets becomes unitary in time `T poly(S)` and space
  `O(S log T)`, via the INW pseudorandom generator.

**Exact statement of the gap, and its conditionality.** Classical: matrix inversion and the
determinant lie in `DET`, and `DET subset NC^2 subset DSPACE(log^2 n)` (Cook, "A taxonomy of
problems with fast parallel algorithms", Inf. Control 64:2-22, 1985,
DOI 10.1016/S0019-9958(85)80041-3; Csanky DOI 10.1137/0205040;
Borodin-von zur Gathen-Hopcroft DOI 10.1016/S0019-9958(82)90766-5). Quantum: `O(log n)` space.
So the gap is `log` versus `log^2`, which by Fact SP-0(i) is the maximum possible. **It is
entirely conditional in the direction that matters**: the classical `log^2` bound is a theorem,
the classical `log` *lower* bound is not, and `BQL` versus `BPL` versus `L` is open. No
unconditional separation is known. The strongest recent candidate is Apers-Edenhofer, "Directed
st-connectivity with few paths is in quantum logspace", CCC 2025,
DOI 10.4230/LIPIcs.CCC.2025.18, arXiv:2408.12473, which the authors describe as the first
natural *candidate* language separating `BQL` from `L` and `BPL`; best known classical is
`DSPACE(log^2 n / log log n)`. Also relevant: Remscrim, ITCS 2021, arXiv:2003.09877, gives the
first sublogarithmic-space quantum *lower* bound (palindromes need `2^{n^{1-Omega(1)}}` time at
`o(log n)` space).

**Negative result that must be weighed.** Beame-Kornerup-Whitmeyer, "Quantum time-space
tradeoffs for matrix problems", STOC 2024, DOI 10.1145/3618260.3649700, SICOMP
DOI 10.1137/24M1710164, arXiv:2401.05321. In the quantum *query* model, classical time-space
tradeoff lower bounds carry over to quantum with no asymptotic loss for matrix-vector product
(`T = Omega(n^2/S)`), matrix multiplication (`T = Omega(n^3/sqrt(S))`), matrix powering and
matrix inversion (`T = Omega(n^4 log(d)/S)`), and these are matched by deterministic algorithms.
Quantum gives **no** time-space advantage for these problems at any space bound.
*Why this does not close the present lane*: their model queries the matrix (or the vector)
entrywise as adversarial input. `H_N` is never an input; it is generated by `poly(n)` sparse
polynomials and its rows are computable in `O(log M_N)` workspace, i.e. it is exactly a
Fefferman-Lin efficient encoding. Query lower bounds say nothing about an algorithm that runs
the generating circuit internally instead of querying entries.
`[UNVERIFIED]`: the paper contains no explicit disclaimer to this effect; the exemption is my
reading of its model, not a quoted statement.

### 1.2 Model (b): streaming and one-way communication - the only unconditional separations

**Why this model escapes Fact SP-0.** The `s -> s^2` simulation re-reads the input many times.
A one-pass stream is consumed. There is therefore no barrier here, and indeed this is the only
place in complexity theory where unconditional quantum space separations are known.

Resolved separations:

| result | quantum | classical lower bound | model | id |
|---|---|---|---|---|
| Hidden Matching | `O(log n)` qubits | `Omega(sqrt n)` bits | one-way comm. | Bar-Yossef-Jayram-Kerenidis, STOC 2004, DOI 10.1145/1007352.1007379; SICOMP 38(1):366-384, DOI 10.1137/060651835 |
| `alpha`-Partial Matching, `alpha = 1/4` | `O(log n)` qubits | `Theta(sqrt n)` bits, bounded-error randomized | one-way comm. | Gavinsky-Kempe-Kerenidis-Raz-de Wolf, STOC 2007, arXiv:quant-ph/0611209, DOI 10.1145/1250790.1250866; SICOMP 38(5):1695-1708, DOI 10.1137/070706550 (their Thm 1.2) |
| online `L_DISJ` | `O(log n)` space | `Omega(n^{1/3})` space | online / one-pass | Le Gall, SPAA 2006, arXiv:quant-ph/0606066, DOI 10.1007/s00224-007-9097-3 |
| triangle counting `(1 +- eps)` | `~O(m^{2/5})` | `Omega(sqrt m)` | 1-pass insertion-only stream | Kallaugher, FOCS 2021, arXiv:2106.04633, DOI 10.1109/FOCS52979.2021.00091 |
| Max-DICUT, `0.4844`-approx | `polylog(n)` | `Omega(sqrt n)` to beat `4/9` | 1-pass stream | Kallaugher-Parekh-Voronova, STOC 2024, arXiv:2311.14123, DOI 10.1145/3618260.3649709 |

Note that Kallaugher's triangle-counting advantage is **polynomial**, not exponential; the
Max-DICUT result is the first unconditional exponential quantum space advantage for a natural
streaming optimisation problem.

**The negative result that constrains every robotics instantiation.** Kallaugher-Parekh,
FOCS 2022, arXiv:2206.00213, DOI 10.1109/FOCS54457.2022.00054 (the brief says CCC 2022; the
venue is FOCS 2022): any `(2 - eps)`-approximation to classical Max-Cut in a stream requires
`Omega(n)` space **even for algorithms maintaining a quantum state**, and Quantum Max-Cut admits
a matching `(2 + eps)`-approximation in `O(log n)` space. Truncated-least-squares outlier
rejection is a Max-Cut-shaped problem on the measurement graph, so this rules out a quantum
streaming advantage for the *optimisation* version of robust SLAM below the factor-2 threshold.
Only promise/decision versions and constant-factor-approximation versions above that threshold
remain open. This is an internal constraint I could not argue around and it decides the shape of
§2.2 below.

Classical streaming lower bounds for linear-algebraic quantities, resolved:

- **Clarkson-Woodruff**, "Numerical linear algebra in the streaming model", STOC 2009,
  DOI 10.1145/1536414.1536445. Theorem 5.2, verbatim: "Any randomized 1-pass algorithm which
  solves the Rank Decision Problem with probability of error at most 1/3 must use `Omega(k^2)`
  bits of space", for deciding `rank(A) >= k`, **exact** rank, **turnstile** model. At `k = n`
  this is `Omega(n^2)` bits, and the same construction gives `Omega(n^2)` for testing
  invertibility and for approximating the determinant to *any* relative error.
- **Li-Woodruff**, "On approximating functions of the singular values in a stream", STOC 2016,
  arXiv:1604.08679: for `n x n` matrices with `O(1)` nonzeros per row and column, estimating
  `||A||_p^p = sum_i sigma_i^p` to `(1 + eps)` in one pass needs `n^{1 - g(eps)}` bits when `p` is
  not an even integer (`g(eps) -> 0`); when `p` is an even integer, `n^{1 - 2/p} poly(eps^{-1} log n)`
  suffices in the turnstile model and is optimal up to those factors. Also
  Li-Woodruff RANDOM 2016, DOI 10.4230/LIPIcs.APPROX-RANDOM.2016.39, for operator-norm and
  Schatten sketching lower bounds.
- **Andoni-Nguyen**, "Eigenvalues of a matrix in the streaming model", SODA 2013: this is an
  **upper-bound** paper (heavy eigenvalue-hitters in `O(1/phi^2)` space by a linear sketch), not
  the lower bound the brief assumed. `[UNVERIFIED DOI]`.
- **Bury-Schwiegelshohn on spectral quantities: this reference does not appear to exist.**
  Their joint record is weighted matchings in dynamic streams (ESA 2015), the Jaccard centre
  (ICALP 2017, Algorithmica 2021) and "Sketch 'Em All" (WSDM 2018); none concerns spectral
  quantities. `[UNVERIFIED - probable mis-citation in the brief; do not propagate it.]`
- Lower bound specifically for the smallest nonzero singular value in a stream: none found as a
  standalone theorem; the best available is a reduction to Clarkson-Woodruff Theorem 5.2.
  `[UNVERIFIED]`.

**Answering the brief's question directly.** Is there an algebraic-geometric observable whose
streaming version inherits one of these separations? Yes, and §2.2 constructs it. But note first
what does *not* work: the normalised Hilbert function, the normalised gap, and the distance to a
degree piece of an ideal are all functions of a *derived* object (`Phi_N`, `H_N`) that is
generated from a small input. There is no stream. The input is `poly(n)` polynomials, which fit
in memory, so the streaming model is vacuous for them. **The streaming model applies to an
algebraic-geometry problem only when the generators themselves arrive one at a time and are
discarded**, which in robotics means exactly one thing: sensor measurements that each contribute
one residual polynomial. That is SLAM, bundle adjustment, and calibration - not kinematics, not
synthesis, not vision minimal solvers.

### 1.3 Model (c): space-bounded simulation of a succinctly specified operator

This is where bet R1, killer K-RV8 and the seed's "250 GB versus 300 qubits" all live, and
Fact SP-0 changes the accounting completely.

Set `A_N = ((N-m)!/N!) H_N` (D-residual-spectral-hierarchy), the object of C-260, acting on
`R_N` of dimension `M_N = binom(N+n, n)` (D-polynomial-ring). Three facts:

1. `H_N` satisfies Fefferman-Lin's efficient-encoding condition (their Def. 10) with
   `k = ceil(log_2 M_N)`: row sparsity `s_row <= sum_j (#monomials of f_j)^2 = poly(n)`
   (D-block-encoding-normalisation), entries
   `sum_j conj(f_{j,alpha}) f_{j,beta} sqrt(k!(k-alpha+beta)!)/(k-alpha)!` which are products of
   `O(m)` integers bounded by `N`, computable in `O(m log N + poly(n))` time and `O(k)` workspace.
2. Therefore the promise problem "estimate `lambda_min(A_N)` under the Def. 17 promise" is **in**
   `BQ_USPACE[O(log M_N)] = BQ_USPACE[O(N log n)]`. This is claim C-NEW-SP-MINEIG-CONTAINMENT.
3. Therefore, by Fact SP-0, it is **also in** `DSPACE(O(log^2 M_N)) = DSPACE(O(N^2 log^2 n))`,
   at classical time `2^{O(log M_N)} = poly(M_N)`.

The numbers, for `n+1` homogeneous variables and the affine `B_r = binom(n+r, r)` used in the
Lasserre indexing of C-259 (recall `N = r`, not `2r`):

| `n` | `r=N` | `B_r` | dense PSD block `8 B_r^2` | 20 Krylov vectors | compact qubits `ceil(log2 B_r)` | BCP classical space `~log2^2 B_r` bits |
|---:|---:|---:|---:|---:|---:|---:|
| 50 | 2 | 1,326 | 14.1 MB | 212 kB | 11 | 108 |
| 50 | 3 | 23,426 | 4.39 GB | 3.75 MB | 15 | 211 |
| 50 | 4 | 316,251 | 800 GB | 50.6 MB | 19 | 334 |
| 50 | 5 | 3,478,761 | 96.8 TB | 557 MB | 22 | 483 |
| 100 | 2 | 5,151 | 212 MB | 824 kB | 13 | 152 |
| 100 | 3 | 176,851 | **250 GB** | **28.3 MB** | **18** | **304** |
| 100 | 4 | 4,598,126 | 169 TB | 736 MB | 23 | 490 |
| 100 | 5 | 96,560,646 | 74.6 PB | 15.4 GB | 27 | 700 |
| 100 | 6 | 1,705,904,746 | 2.3e4 PB | 273 GB | 31 | 941 |
| 300 | 2 | 45,451 | 16.5 GB | 7.27 MB | 16 | 239 |
| 300 | 3 | 4,590,551 | 169 TB | 734 MB | 23 | 490 |
| 300 | 4 | 348,881,876 | 974 PB | 55.8 GB | 29 | 806 |
| 300 | 5 | 2.13e10 | 3.6e6 PB | 3.41 TB | 35 | 1190 |
| 300 | 6 | 1.09e12 | 9.4e9 PB | 174 TB | 40 | 1600 |

The bolded row is the one the seed and K-RV8 argued over. Read across it: 250 GB (seed R1,
dense SDP), 28.3 MB (K-RV8, implicit Lanczos), 18 qubits (quantum), **304 bits (classical, by
theorem)**. The last column is a theorem and the first two are not; the space argument as
conducted so far never reached the classical minimum.

**Where does `N` have to grow in robotics?** This is the question that decides whether model (c)
has any content, since at fixed `N` everything is `poly(n)`.
- *Perception (Lasserre order for tightness).* Level 1 suffices outlier-free (SE-Sync, Shonan).
  Yang-Carlone use the **lowest** order and report it empirically tight for TLS; no published
  robotics instance is known to require `r >= 3` (see the premise correction opening §2.1). If
  such a family exists the operative range is `r in {2,3,4,5}`, i.e. `N` grows only through a
  handful of integers, and `M_N` grows by a factor `(n+r)/r ~ n/r` per level. **If it does not
  exist, model (c) has no robotics instance at all.**
- *Kinematic synthesis (Macaulay/solving degree).* For a square system of `s` equations of degree
  `d_i` the Lazard/Macaulay degree bound is `sum_i (d_i - 1) + 1`. Watt II eight-accuracy-point
  is 22 bilinear equations in 22 unknowns (DOI 10.1115/1.4027443), so the bound is `D_reg = 23`
  and the degree-23 monomial count is `binom(45,22) = 4.12e12` (one vector: 33 TB). Stephenson II
  eleven-position is 70 quadratics in 70 unknowns reduced to **ten degree-8 equations in ten
  unknowns** (DOI 10.1115/1.4031124), giving `D_reg = 71` and `binom(81,10) = 1.88e12`
  (one vector: 15 TB); in the unreduced 70-variable presentation the bound is `binom(141,70) =
  1.9e41`, which shows how presentation-dependent this quantity is. Here `N` genuinely must grow
  with `n`. But see §2.4: nobody computes these, so there is no classical space cost to beat.
- *Closure varieties (bet R3).* Regularity must be `poly(j)` for `N ~ n` to sit in the stable
  range (D-saturation-regularity-stable-range); unmeasured.
So the growing-`N` regime that model (c) needs exists only in synthesis, where the classical
method has no space cost; and the regime with a real classical space cost (perception) has `N`
bounded by a small constant. **This tension is the deepest structural problem with the space
direction and I have not resolved it.** It is killer KS7 below.

### 1.4 Summary of the three models

| model | separation status | max gap | robotics instance | verdict |
|---|---|---|---|---|
| (a) quantum logspace | conditional; `BQL` vs `L` open | quadratic (Fact SP-0) | `lambda_min(A_N)`, `dim I_N` under conditioning promise | a theorem is available (completeness); a separation is not |
| (b) streaming / one-way | **unconditional**, several | exponential (`sqrt n` vs `log n`) | streamed loop-closure consistency (§2.2) | the only rigorous space claim in the lane |
| (c) succinct-operator simulation | not a space claim at all (Fact SP-0) | zero, as a pure space claim | R1 perception certification | survives only as a (space, time) claim |

---

## 2. Robotics instances, in the brief's required form

Format per instance: **Input model / Observable / Quantum space / Classical space bound (theorem
or best-known, stated) / Time on both sides.**

### 2.1 Robust perception certification (Yang-Carlone TLS, STRIDE)

**A correction to the premise, before anything else.** The robotics memo's §10 and bet R1 rest on
"level 2 is not tight and level 3 is out of reach". **No published source says this.**
Yang-Carlone (arXiv:2109.03349, IEEE TPAMI 2022, DOI 10.1109/TPAMI.2022.3179463) use the
**lowest** order of the moment hierarchy and report it empirically exact for their TLS
formulations; their "sparse" relaxation is a term-sparsity plus basis-reduction shrinkage of the
dense relaxation at that order, and STRIDE (SpecTrahedral pRojected gradIent Descent along
vErtices) is reported up to 100x faster than MOSEK and the only solver reaching SDPs with
hundreds of thousands of constraints. TEASER (arXiv:2001.07715), QUASAR (arXiv:1905.12536) and
One Ring (arXiv:2006.06769) were checked directly and none states a level-2/level-3 wall.
The one **documented** non-tightness is Holmes-Dumbgen-Barfoot, "On semidefinite relaxations for
matrix-weighted state-estimation problems in robotics", IEEE T-RO 40:4805-4824, 2024,
arXiv:2308.07275, DOI 10.1109/TRO.2024.3475220: matrix-weighted (anisotropic) noise loses
tightness, and their matrix-weighted SLAM relaxation is inherently non-tight **unless redundant
constraints are added** - the remedy they propose is redundant constraints, **not a higher
hierarchy order**. Redundant constraints add rows at the same `r`, which grows `nnz` and the
constraint count but not `B_r`. **So the space wall that bet R1 attacks is, on the present
evidence, a wall nobody has hit.** This is claim C-NEW-SP-R1-PREMISE below, and it is the single
biggest threat to §2.1 - larger than K-RV8 and K-RV9 combined, because it removes the motivation
rather than the arithmetic. Everything that follows in this subsection is conditional on somebody
exhibiting a robotics family that genuinely needs `r >= 3`.

**Input model.** D-input-model, real-coefficient version: residual forms
`f_1, ..., f_d` of degree `m = 2` in `n+1` homogeneous real variables, `poly(n)` monomials and
`poly(n)`-bit coefficients, sparse row access. Variables for TLS point-cloud registration with
`K` correspondences: a quaternion or rotation block plus a translation block plus `K` binary
indicators `theta_i^2 = 1`, so `n ~ K + 7` (quaternion) or `n ~ K + 12` (rotation matrix). Hence
`n = 50, 100, 300` corresponds to roughly `K = 43, 93, 293` correspondences. Yang-Carlone's
exactness demonstrations are at 30-70 measurements, so `n = 50` is the size at which their
claims are actually verified and `n = 300` is extrapolation. Relaxation order
`N = r` (C-259: the Fock sector is `N = r`, not `2r`). A guiding state `|p*>^{⊗N}` from the
Gauss-Newton local solution, with squared ground-space overlap `w`.

**Observable.** `lambda_min(A_N)` to additive `eps * alpha_A`, with
`A_N = ((N-m)!/N!) H_N` and `alpha_A = ((N-m)!/N!) alpha_BE` (D-block-encoding-normalisation,
C7). By C-260 this is a valid lower bound on `min_{||x||=1} sum_j f_j(x)^2`, hence a certificate
of global optimality or of a bounded suboptimality gap. It is **not** the Lasserre value
(C-261, K-RV7) and must never be called one.

**Quantum space.** `ceil(log_2 B_r)` data qubits in a compact basis encoding, or
`(n+1) ceil(log_2(N+1))` in the occupation encoding, plus ancillas for the row oracle and QSVT
phases. Exact: `n = 100, r = 3`: 18 compact / 202 occupation. `n = 300, r = 4`: 29 / 903.
`n = 100, r = 6`: 31 / 303. The compact encoding is the one that matters for Fact SP-0.

**Classical space bound.**
- Dense moment SDP: `8 B_r^2` bytes. `250 GB` at `n = 100, r = 3`; `169 TB` at `r = 4`. This is
  a *best-known-algorithm* number for a *different problem* (the full structured SDP), and
  K-RV8/K-RV9 are right to reject it here.
- Implicit Lanczos/LOBPCG: `k B_r` words for `k` Krylov vectors. `28.3 MB` at `k = 20`,
  `n = 100, r = 3`; `736 MB` at `r = 4`; `15.4 GB` at `r = 5`; `273 GB` at `r = 6`. Also a
  *best-known-algorithm* number. The K-RV8 wall is only two to three levels above where K-RV8
  evaluated it.
- **Theorem**: `O(log^2 B_r)` bits, i.e. `304` bits at `n = 100, r = 3`, by Fact SP-0 composed
  with the containment of §1.3. This is the classical space *upper* bound and it beats both of
  the above by many orders of magnitude. No classical space *lower* bound above
  `Omega(log B_r)` is known for this problem. **Every number in the R1 debate so far has been an
  upper bound; there is no space separation here.**

**Time on both sides.**
- Quantum: `~O(alpha_A/(eps sqrt(w)))` block-encoding uses, each `poly(n, log N)` gates
  (real-variety Route 4). With `alpha_BE = poly(n) N^m max_j ||f_j||^2` this is
  `poly(n, N, 1/eps) / sqrt(w)`. Polynomial in `n` and `N`, i.e. **polylogarithmic in `B_r`**,
  provided `w >= 1/poly`.
- Classical Lanczos: `O(k nnz(A_N))` with `nnz <= t B_r`, so `Omega(B_r)` per matvec, i.e.
  polynomial in `B_r` and exponential in `r`.
- Classical BCP route: `poly(B_r)` time at `O(log^2 B_r)` space.
- So the honest claim is on the **(space, time) Pareto frontier**: quantum attains
  `(O(log B_r), poly(n,N))`; classical attains `(O(B_r), poly(B_r))` or
  `(O(log^2 B_r), poly(B_r))`, and no classical point at `(polylog, poly(n,N))` is known.
  A space advantage bought with exponential time is not a claim, and this one is not: the
  quantum time is *smaller* than both classical times, conditional on the overlap promise.

**Which trap this is checked against (classical memo Traps).** Comparing against the wrong
classical algorithm: addressed by giving three classical baselines, not one. Confusing absolute
and normalised gaps: the promise is on `gamma_N = Delta/alpha_BE`, per C5/C7. Exponentially
small overlap: `w` is the entire risk and is the subject of experiment E4. Hiding exponential
`N`: `N` is in unary and all costs are polynomial in `N`, per D-input-model.

**The unproven half.** For this to be a claim rather than a wish, the guided problem must be
BQP-hard for the bosonic symmetric-sector family. See C-NEW-SP-GLH-BOSONIC. The general
guided-local-Hamiltonian problem is BQP-complete (Gharibian-Le Gall arXiv:2111.09079; improved
to 2-local with constant guiding fidelity, arXiv:2207.10250), but `H_N` on `Sym^N(C^{n+1})` is
permutation-invariant, and C-099 records that permutation-invariant Hamiltonians at **fixed**
local dimension are classically easy (Anschuetz-Bauer-Kiani-Lloyd, arXiv:2211.16998,
Quantum 7:1189). Here the local dimension is `n+1` and grows, so C-099 does not apply, but the
hardness must be re-derived and is not inherited.

### 2.2 SLAM as a stream of polynomial measurements: the one unconditional claim

**Input model (new; proposed as D-streaming-polynomial-input).** A one-pass stream
`sigma = (g_1, g_2, ..., g_T)` in which each item is either a coefficient assignment for one
variable or one generator polynomial with `poly(n)` monomials. The algorithm holds `S` bits (or
`S` qubits plus `S` classical bits), reads each item once in the order given, and outputs at the
end. Arrival order is part of the problem specification. The reduction to one-way communication
is immediate for any *fixed prefix split* `sigma = sigma_A sigma_B`: a classical one-pass
algorithm with `S` bits yields a one-way protocol with `S` bits, so
`S >= R^{1-way}(sigma_A ; sigma_B)`.

**The problem (proposed as SIGN-CONSISTENCY-STREAM(n, alpha)).**
- `sigma_A`: the point ideal `I_A = (s_i - a_i : i in [n])` for `a in {+1,-1}^n`, streamed one
  generator at a time.
- `sigma_B`: the binomial ideal `I_B = (s_i^2 - 1 : i in [n]) + (s_i s_j - w_e : e = (i,j) in M)`
  for a **partial matching** `M` on `[n]` with `|M| = alpha n`, and signs `w_e in {+1,-1}`,
  streamed one edge at a time.
- Promise: either every edge is satisfied by `a` (`w_e = a_i a_j` for all `e in M`) or every edge
  is violated (`w_e = -a_i a_j` for all `e`).
- Decide which. Equivalently, decide `1 not in I_A + I_B` versus `1 in I_A + I_B`; equivalently
  `HF_{R/(I_A+I_B)} = 1` versus `= 0`; equivalently, for the D-hamiltonian of the tuple,
  `lambda_min = 0` (frustration-free) versus `lambda_min = 4 alpha n` (maximally frustrated).

**Observable.** Consistency of a streamed binomial ideal on the sign hypercube, i.e. a
Nullstellensatz decision (classical memo §4). The ideal is radical and zero-dimensional and
D-boolean-ideal applies after the standard `s = 1 - 2x` change of variables.

**Quantum space.** `O(log n)` qubits, one pass, error `<= 1/3`. The protocol:
1. Prepare `n^{-1/2} sum_i |i>` on `ceil(log_2 n)` qubits.
2. On reading `a_i`, apply the diagonal phase gate `|i> -> a_i |i>`. After `sigma_A` the register
   holds `|psi_a> = n^{-1/2} sum_i a_i |i>`.
3. On reading edge `e = (i,j)` with value `w_e`, apply the two-outcome projective measurement
   `{P_e = |i><i| + |j><j|, 1 - P_e}`. On outcome `1 - P_e` the post-measurement state is the
   same uniform-phase state supported on the surviving indices, so the pass continues with no
   loss. On outcome `P_e` (a "hit"), measure in `{(|i> +- |j>)/sqrt 2}` to obtain `a_i a_j`
   exactly, compare with `w_e`, output, and halt.
4. Because the edges of `M` are disjoint, the hit probabilities telescope: the probability of
   never hitting over the whole stream is `prod_{k=0}^{alpha n - 1} (n - 2k - 2)/(n - 2k)
   = 1 - 2 alpha`. At `alpha = 1/4` a single register hits with probability `1/2`; running
   `c` independent registers in parallel (total `c ceil(log_2 n)` qubits) fails with probability
   `2^{-c}`. `c = 2` gives error `1/4`.
   Under the promise, a hit gives the correct answer with certainty.

**Classical space lower bound: `Omega(sqrt n)` bits, and this is a THEOREM.** Under the prefix
split above, the problem is exactly the `alpha`-Partial Matching problem of
Gavinsky-Kempe-Kerenidis-Raz-de Wolf (arXiv:quant-ph/0611209, Thm 1.2), whose bounded-error
randomized one-way communication complexity is `Theta(sqrt n)` at `alpha = 1/4`. The lower bound
is unconditional, holds against randomized protocols with error `<= 1/3`, and transfers to
one-pass streaming space by the reduction above. This is the same machinery Kapralov-Khanna-Sudan
used to get `Omega(sqrt n)` for Max-Cut streaming (SODA 2015, via Boolean Hidden Partition)
`[UNVERIFIED DOI]`.

**Time on both sides.** Quantum: `O(1)` gates per stream item, `O(T)` total, plus `O(log n)`
gates of setup - strictly cheaper than the classical `Omega(sqrt n)`-bit sketch, which must also
touch every item. Neither side pays a superlinear time cost. **This is the one place in the lane
where the space advantage is not bought with time at all.**

**What the classical baseline actually is in deployed SLAM, and why it hurts.** The classical
bounded-memory method is sliding-window marginalization, and its measured footprint is tiny.
Demmel-Schubert-Sommer-Cremers-Usenko, "Square root marginalization for sliding-window bundle
adjustment", ICCV 2021, arXiv:2109.02182, state for VIO on EuRoC MH01: at most 4033 observations
across all landmarks and at most 7 keyframes in the window, "giving an approximate upper bound of
**2.4 MB** with 32-bit floats" (measured: 1.3 MB square-root versus 0.9 MB Schur-complement;
whole-process peak ~300 MB, dominated by non-optimization subsystems). Related baselines:
iSAM2 (Kaess et al., IJRR 31(2):217-236, 2012, DOI 10.1177/0278364911430419), whose cost is
governed by fill-in and whose min-fill ordering problem is NP-hard; Square Root SAM
(Dellaert-Kaess, IJRR 25(12):1181-1204, 2006, DOI 10.1177/0278364906072768), `O(mn^2)` for dense
QR/Cholesky with min-fill ordering NP-complete and a worked case where the dense EKF alternative
would be a 15000 x 15000 matrix; MSCKF (Mourikis-Roumeliotis, ICRA 2007), linear in features and
at most cubic in retained states, with the window size an explicit tunable "according to the
available computing resources". **No formal space-complexity lower bound for SLAM or bundle
adjustment exists in the literature** (searched; reporting absence explicitly). So the streaming
claim of this subsection is not competing against a documented classical space wall - it is
competing against 2.4 MB. Its value is theoretical, and §6 KS7 says so.

**Robotics reading.** Two robots, or one robot across two sessions, on a bandwidth-limited link
(deep space, under ice, under water). Robot A holds a binary label per keyframe - the sign in a
`Z_2` relaxation of rotation averaging, or which branch of a two-fold pose ambiguity was taken in
a mirror-symmetric corridor. Robot B independently detects `alpha n` **disjoint** place-revisits
and, for each, a relative binary label. Question: is B's loop-closure batch globally consistent
with A's map, or systematically inverted (which is exactly what a mirrored or repetitive
environment produces)? Classically A must send `Omega(sqrt n)` bits; quantumly `O(log n)` qubits.

**Hardware.** `|psi_a> = n^{-1/2} sum_i a_i |i>` is **one photon in `n` modes** with a `pi` phase
shifter on mode `i` when `a_i = -1`; the edge measurement is a 50:50 beamsplitter on modes `i, j`
followed by photon detection. No nonlinearity, no postselection beyond detecting the photon.
A close relative has been run: Kumar-Kerenidis et al., "Experimental demonstration of quantum
advantage for one-way communication complexity surpassing best-known classical protocol",
Nat. Commun. 10:4152 (2019), DOI 10.1038/s41467-019-12139-z, using a Sampling Matching variant
with coherent-state phase encoding, a fixed linear-optics circuit and single-photon detection,
beating the best known classical protocol in transmitted information above input size ~3000.
**This is the cheapest realisation of the north star's linear-optics clause found anywhere in
this campaign, and it already exists in a laboratory.**

**Honest caveats, all fatal to a deployment story and none to the theorem.** (i) The
all-or-nothing promise is not a real outlier model; a real batch is `p`-fraction outliers.
Removing the promise moves the problem to Max-Cut territory, where Kallaugher-Parekh's `Omega(n)`
bound holds *even quantumly*. (ii) Loop closures must form a matching (each keyframe used once);
real loop-closure sets are not matchings, and the Boolean Hidden Partition generalisation to
sparse graphs is the right object but has not been checked here. (iii) The margin is `sqrt n`
versus `log n`: 100 bits versus 14 qubits at `n = 10^4`. (iv) The quantum register must stay
coherent across the entire pass. (v) It is a communication/streaming claim, not a computation
claim: nothing is computed faster.

### 2.3 On-robot inverse-kinematics tables: a clean no-go

**Input model.** A precomputed table `T in {0,1}^L` mapping a discretised workspace cell to a
preferred IK branch or seed; `L = (#cells) x (bits per entry)`, typically `10^6` to `10^9` bits.
**Observable.** `T_i` for a query index `i` supplied at run time.
**Quantum space.** Any quantum encoding from which an *arbitrary* `T_i` is recoverable with
probability `p > 1/2` requires at least `(1 - H(p)) L` qubits: Nayak, "Optimal lower bounds for
quantum automata and random access codes", FOCS 1999, arXiv:quant-ph/9904093 (see also
Ambainis-Nayak-Ta-Shma-Vazirani, JACM 49(4):496-511, 2002, arXiv:quant-ph/9804043).
**Classical space bound.** `L` bits, and this is optimal - so the quantum bound is `Theta(L)` too.
**Time.** Irrelevant; the space claim is dead before time is considered.
**Verdict: REFUTED direction.** There is no quantum compression of a lookup table, by theorem.
And if the table is generated by a small circuit, no table is needed at all: IKFast emits a
closed-form solver of a few kilobytes running in ~5 microseconds (robotics memo §2). Both horns
close.

### 2.4 Kinematic synthesis (Watt II, Stephenson II): no space claim, and K5 is right here

**Input model.** Multihomogeneous synthesis systems, all root counts now resolved:
Watt II eight-accuracy-point, 22 bilinear equations in 22 unknowns, multihomogeneous degree
705,432, **92,736** nonsingular solutions (Plecnik-McCarthy, J. Mech. Rob. 2015,
DOI 10.1115/1.4027443); Stephenson II eleven-position, 70 quadratics in 70 unknowns reduced to
ten degree-8 equations, multihomogeneous degree 264,241,152, **1,521,037** solutions, obtained in
311 hours on 256 cores (DOI 10.1115/1.4031124); Stephenson III eleven-position, degree
55,050,240, **834,441** solutions (Mech. Mach. Theory 2015,
DOI 10.1016/j.mechmachtheory.2015.10.004); nine-point four-bar, 8 equations, **8652** roots and
**1442** distinct linkages (Wampler-Morgan-Sommese, ASME JMD 114(1):153-159, 1992,
DOI 10.1115/1.2916909). All four were `[UNVERIFIED]` in the robotics memo; all four are now
verified with DOIs.
**Observable.** A root satisfying a design predicate (bet R2), or the root count.
**Quantum space.** `O(n log N)` qubits in the multigraded sector; `6^11 = 3.6e8` sector dimension
for Watt II, so 29 compact qubits.
**Classical space bound.** Two very different numbers.
- Macaulay/Groebner route: the Lazard degree bound is `sum_i (d_i - 1) + 1 = 23` for Watt II, so
  the degree-23 monomial space has `binom(45,22) = 4.12e12` dimension; one vector is 33 TB and
  the matrix is unstorable. Stephenson II in the reduced ten-variable presentation:
  `binom(81,10) = 1.88e12`, one vector 15 TB. Nine-point four-bar: `binom(17,8) = 24310`, one
  vector 194 kB.
- Homotopy continuation, which is what is actually used: **"each track requires a few Kbytes"**
  (GPU-HC, Chien et al., CVPR 2022, arXiv:2112.03444, DOI 10.1109/CVPR52688.2022.01531, quoted
  verbatim), with the optimal design assigning one track to a 32-thread warp for about 4 kB of
  fast register memory per track, on systems up to 32 x 32. Best-known-algorithm, and K5's point
  exactly, now with a quotable number rather than an estimate. `[UNVERIFIED]`: no explicit
  memory-per-path statement was found for HomotopyContinuation.jl or Bertini.
**Time.** Classical: `D` parameter-homotopy path tracks, `10^2`-`10^4` predictor-corrector steps
of `O(n^3)`, so `10^12`-`10^14` flops per design query. Quantum: `sqrt(dim(sector)/|good roots|)`
ground-space projections at `alpha/Delta` block-encoding uses each, with `alpha/Delta` unmeasured
for any robotics ideal (K10).
**Verdict.** There is no space claim in synthesis, because the classical method with the smallest
space is also the classical method with the best time. **K5 is exactly correct in this instance,
and its scope is exactly this instance.** Bet R2 remains a time claim (D10) and this memo does not
touch it. One genuinely open sub-question: the *actual* solving degree of these systems (as
opposed to the Lazard bound) appears nowhere in the literature; see experiment E2.
`[UNVERIFIED - no published Macaulay or solving degree or Castelnuovo-Mumford regularity for any
six-bar synthesis system was found in this pass.]`

### 2.5 Contact and mode enumeration: the output is the space

**Input model.** `K` contacts, `d` effective DOF; contact modes are sign vectors compatible with
the kinematics. Huang-Cheng-Mason, "Efficient contact mode enumeration in 3D", WAFR 2020,
DOI 10.1007/978-3-030-66723-8_29 (now verified, primary text read): contacting/separating (CS)
enumeration is `O(d K^{d+1})` with at most `O(K^{d/2})` distinct CS-modes; sticking/sliding given
a CS-mode is `O((kK)^{2+2d})`; full enumeration is `O(K^{d/2 + 2.5d})`. Reported counts are much
larger than the robotics memo's "50-400": Box-box-2 (`K = 16`, `d = 9`) has 184 CS-modes and
**168,746** SS-modes; Hand-ball (`K = 12`, `d = 17`) has 4096 CS-modes and SS enumeration did not
complete in over an hour. **Correction to robotics memo §12.**
**Observable.** The mode list, or a count, or a sample.
**Quantum space.** `O(log K)` qubits for a sample; `O(K)` to name one mode.
**Classical space bound.** The classical enumerator also streams its output and needs only
`poly(K, d)` working space plus the output; the `168,746` figure is the *output* size, not the
working space. So there is nothing to beat: `Theta(output)` on both sides, by an information
argument.
**Time.** Time, not space, is the documented bottleneck (">1h" above). Grover over modes gives a
square-root saving on the search version; that is bet-R2-shaped and outside this memo.
**Verdict.** No space claim. Counting modes exactly is the exact-small-integer trap again
(K3, K-RV3): a signature or count changes in units of one, so additive normalised estimation
needs `eps = O(1/D)` and amplitude estimation then costs `O(D)`.

### 2.6 Instance scorecard for the space direction

| # | instance | quantum space | classical space, and its status | separation type | score |
|---|---|---|---|---|---|
| 2.1 | robust perception certification | `O(log B_r)` qubits | `O(log^2 B_r)` bits, **theorem**; `O(B_r)` words, best-known time-efficient | quadratic space; (space,time) Pareto conditional on BQP != BPP | 2/5 (was 3/5 before the premise correction) |
| 2.2 | streamed loop-closure consistency | `O(log n)` qubits | `Omega(sqrt n)` bits, **theorem** | exponential, **unconditional** | 4/5 |
| 2.3 | on-robot IK table | `Theta(L)` qubits | `L` bits, **theorem** (Nayak) | none, refuted | 0/5 |
| 2.4 | kinematic synthesis | `O(n log N)` qubits | `O(n^2)` doubles per path, best-known | none | 1/5 |
| 2.5 | contact modes | output-bounded | output-bounded, **theorem** | none | 1/5 |

---

## 3. Where the killers are weak

### K5 - "homotopy continuation is `O(n)`-space per path, so the Macaulay-space argument attacks a strawman"

**What it covers, and covers correctly.** Zero-dimensional square systems whose deliverable is
the root list, and for which a start system with a tight root count exists: 6R IK, parallel FK,
vision minimal problems, rigidity realisations, kinematic synthesis. In every one of these,
homotopy's per-path memory is `O(n^2)` doubles (the Jacobian; K5's "`O(n)`" understates its own
case by a factor `n` and this does not matter), the method parallelises trivially, and any
Macaulay-matrix space comparison is indeed against a method the field abandoned. §2.4 confirms
this quantitatively for Watt II: 4 kB per path versus a 33 TB vector.

**What it does not cover.** Four regimes, and the important robotics problems live in them.
1. *Certification and optimisation.* When the deliverable is a **lower bound on a minimum**,
   homotopy computes nothing: it finds roots, and a bound is not a root. The classical method
   there is a moment/SOS SDP or a Krylov eigensolve, both with real space costs. All of §2.1.
2. *Inconsistent systems.* Noisy perception, calibration and SLAM have `V = empty`, `I = (1)`,
   and there are no paths to track. Homotopy is not merely unused, it is undefined.
   K5 was derived from the kinematics canon and silently generalised to the whole lane.
3. *Positive-dimensional decomposition.* A witness set costs at least `deg V` path tracks and
   `O(n deg V)` memory if retained. Bet R3 lives here.
4. *Streaming.* If the system arrives as a stream and cannot be stored, homotopy's low per-path
   memory is irrelevant because the system itself does not fit. All of §2.2.

**The specific hand-wave.** "A space speedup over a method nobody uses is not a speedup" is true
of Macaulay matrices in synthesis and **false** of moment matrices in certifiable perception,
where the moment matrix *is* the deployed method (STRIDE, SE-Sync, Shonan) and its size is the
documented failure mode. K5 licenses a conclusion about the whole lane from evidence about half
of it.

### K6 - "`BQPSPACE = PSPACE`, so no quantum space advantage for motion planning"

**What it covers, and covers correctly.** The generalised movers' decision problem is
PSPACE-complete (Reif; Canny, *The Complexity of Robot Motion Planning*, MIT Press 1988), and
`BQPSPACE = PSPACE` (Watrous, JCSS 59(2):281-326, 1999, DOI 10.1006/jcss.1999.1655). For a
PSPACE-complete language, polynomial quantum space gives nothing over polynomial classical space.
Correct, and it closes motion planning.

**What it does not cover, and this is the substantive weakness.**
1. *It is an equality of classes at the polynomial level.* It says nothing about `O(s)` versus
   `O(s^2)`, which is the resolution at which every quantum space claim ever made operates:
   quantum logspace versus classical `log^2` space, and the compact `log M_N` versus `log^2 M_N`
   of §1.3. K6 is a true statement quoted at the wrong resolution.
2. *The correct statement at the right resolution is strictly stronger and was not made.*
   Fact SP-0 gives `BQSPACE(s) subset DSPACE(s^2)` for every `s = Omega(log n)`, not just
   polynomial `s`. This **kills the seed's R1 space comparison outright**, which K6 did not do,
   and simultaneously **bounds the maximum achievable advantage at quadratic**, which K6 also
   did not do. A campaign that had this fact would never have written "300 qubits versus 250 GB".
3. *It says nothing about simultaneous space and time.* The `s -> s^2` simulation costs
   `2^{O(s)}` time. Every surviving claim in this memo is a (space, time) claim and K6 does not
   reach any of them.
4. *It says nothing in the streaming or one-way model.* The simulation re-reads the input; a
   stream cannot be re-read. Every unconditional quantum space separation known lives precisely
   in the gap K6 leaves, and §2.2 is one.
5. *It says nothing about communication.* Bandwidth is a robotics resource and the separations
   there are unconditional.

**Net.** K6 as written is a true statement used to close a door it does not reach. Its correct
form closes a *larger* door (the whole "compact register versus big matrix" family) and opens two
specific ones (quadratic gaps; consumed inputs).

### K-RV8 - "the R1 memory comparison changes the problem; `H_N` admits `O(B_N)`-memory Krylov"

**What it covers, and covers correctly.** The point comparison at `n = 100`, `r = 3`. Implicit
Lanczos needs `~28 MB`, not `250 GB`, and the seed's headline number compares a sparse
eigenproblem against a dense SDP. This is decisive against the R1 sentence as written and
D12 was right to act on it.

**What it does not cover.**
1. *Growth in `r`.* `k B_r` words is 28.3 MB at `r = 3`, 736 MB at `r = 4`, 15.4 GB at `r = 5`,
   273 GB at `r = 6` (`n = 100`); at `n = 300` it is 734 MB, 55.8 GB, 3.41 TB, 174 TB. K-RV8's
   "tens of megabytes" is a statement about one point presented as a statement about the method.
   The Lanczos baseline has its own wall, two to three levels above where K-RV8 evaluated it,
   and the levels above 2 are exactly the ones the R1 story needs.
2. *Time.* At the order where Lanczos runs out of memory it also runs out of time: a matvec is
   `Omega(B_r)`. K-RV8 compares memory only, so it cannot see that its own baseline degrades in
   both resources simultaneously, which is the situation in which a (space, time) claim becomes
   interesting rather than empty.
3. *It is not a lower bound and does not claim to be, but it is used as one.* `O(B_N)` is an
   upper bound for a time-efficient method. The classical space *minimum* is `O(log^2 B_N)` bits
   by Fact SP-0 - 304 bits at `n = 100, r = 3`, five orders of magnitude below K-RV8's own
   number. So the correct verdict on R1 is stronger than K-RV8's: **not "the comparison uses the
   wrong classical baseline", but "no space comparison can succeed at all in this model".**

**The specific hand-wave.** "admits an `O(M_N)`-memory classical Krylov method" is offered as if
it settles the matter. It settles it at `r = 3` and loses at `r = 6`, and it is the wrong kind of
statement (an upper bound) to settle a separation question in either direction.

### K-RV9 - "sparse and chordal classical solvers attack the real bottleneck"

**What it covers, and covers correctly.** Instances with correlative or term sparsity, where
TSSOS/CS-TSSOS (arXiv:2103.00915, arXiv:2005.02828), Burer-Monteiro, STRIDE and first-order conic
solvers reduce the dense block to the largest clique. For pose-graph SLAM the measurement graph
is genuinely sparse and near-chordal, and K-RV9 is decisive there. It also correctly warns that a
quantum claim must beat the largest sparse clique, not `B_r^3`.

**What it does not cover.**
1. *Correlative sparsity is a treewidth statement, and robust perception has a hub.* In TLS
   point-cloud registration a single global pose block couples to every one of the `K` binary
   indicators, so the variable-interaction graph is a star with a large hub and the clique
   containing the pose has size `Theta(K)`. Chordal decomposition does not shrink that block.
   Yang-Carlone's "sparse second-order relaxation" is not a chordal decomposition at all; it is a
   basis restriction (monomials `{1, x, theta_i x}`), i.e. term sparsity, and it is exactly that
   restriction which loses tightness at high outlier rates. Experiment E5 measures this.
2. *Sparsity does not repair non-tightness.* K-RV9 answers "the dense block is not the baseline"
   and does not answer "what do you do when the sparse relaxation is loose", which is the case
   R1 targets and the documented failure mode (arXiv:2308.07275).
3. *It names a family of solvers, not a theorem.* It is a best-known-algorithm statement and can
   never be a lower bound. Like K-RV8 it is being used to close a question that only a lower
   bound can close.

**What K-RV9 gets righter than it knows.** Sparsity cuts both ways (classical memo Traps): the
same correlative sparsity that helps TSSOS also reduces `s_row` in
D-block-encoding-normalisation and therefore `alpha_BE`, so it helps the quantum side too. But
any preconditioner or sparsity pattern given to the quantum algorithm must also be given to the
classical baseline, and that is a discipline K-RV9 correctly imposes.

### Summary table

| killer | regime it covers | regime it does not cover | status |
|---|---|---|---|
| K5 | 0-dim square systems with a root-list deliverable | certification, inconsistent systems, positive-dim decomposition, streaming | correct but over-generalised |
| K6 | PSPACE-complete decision problems at polynomial space | `s` vs `s^2`; simultaneous space-time; streaming; communication | correct, quoted at the wrong resolution; its sharp form is Fact SP-0 |
| K-RV8 | `n = 100`, `r = 3` | `r >= 5`; time; the actual classical space minimum | correct at a point, presented as a method |
| K-RV9 | sparsity-friendly instances (pose graphs) | hub-structured TLS; non-tightness; it is not a lower bound | correct and incomplete |

---

## 4. Proposed claim rows and definitions

All rows enter at **CONJECTURE** per L1. Ids `C-NEW-SP-<NAME>`.

### C-NEW-SP-WATROUS-CEILING
- statement: For every space-constructible `s(n) = Omega(log n)` and every promise problem `P`
  decidable with bounded error by a quantum algorithm using `s(n)` qubits on an input available
  on a read-only random-access tape, `P` is decidable by a deterministic classical algorithm
  using `O(s(n)^2)` bits of workspace and `2^{O(s(n))}` time. Consequently, for every family of
  problems in that model, the ratio (classical space)/(quantum space) is `O(s)`, and no
  comparison of the form "quantum uses `O(n log N)` qubits while classical uses
  `M_N = binom(N+n,n)` words" is a space separation.
- status: CONJECTURE
- depends-on: D-input-model
- where-proved: Watrous DOI 10.1007/s00037-003-0177-8 composed with Borodin-Cook-Pippenger
  DOI 10.1016/S0019-9958(83)80060-6; `s = log n` case quoted in arXiv:2006.03530
- where-tested: none (it is a literature composition; the checker is a citation audit)
- north-star relevance: it is the ceiling every space claim in the campaign must respect, and it
  refutes bet R1's space sentence more strongly than K-RV8 does.
- traps audited: comparing against the wrong classical algorithm; confusing an upper bound with a
  lower bound.

### C-NEW-SP-MINEIG-CONTAINMENT
- statement: For every tuple of real homogeneous generators `f_1,...,f_d` of degree `<= m` in
  `n+1` variables with `poly(n)` monomials and `poly(n)`-bit coefficients, and every `N` given in
  unary, the promise problem "decide `lambda_min(H_N/alpha_BE) <= a` or `>= b`" with
  `b - a > 2^{-O(N log n)}` lies in `BQ_USPACE[O(N log n)] = BQ_USPACE[O(log M_N)]`, because
  `H_N` satisfies the Fefferman-Lin efficient-encoding condition with row sparsity `poly(n)` and
  entries computable in `O(log M_N)` workspace; and consequently it lies in
  `DSPACE(O(N^2 log^2 n))` at classical time `poly(M_N)`.
- status: CONJECTURE
- depends-on: D-macaulay-map, D-block-encoding-normalisation, D-input-model,
  D-residual-spectral-hierarchy, C-NEW-SP-WATROUS-CEILING
- where-proved: proposed here, §1.3; containment by arXiv:1604.01384 Def. 10 and Def. 17
- where-tested: none; E1 measures the constants
- north-star relevance: replaces bet R1's space claim with a correct one, and supplies the exact
  classical space number (`O(log^2 B_r)` bits) that the R1 debate never reached.
- traps audited: hiding exponential `N`; confusing absolute and normalised gaps.

### C-NEW-SP-MINEIG-HARDNESS
- statement: There exists a family of real homogeneous generator tuples arising from robot
  perception residuals for which the promise problem of C-NEW-SP-MINEIG-CONTAINMENT is hard for
  `BQ_USPACE[O(log M_N)]` under `NC^1` reductions; equivalently, an arbitrary efficiently
  encoded PSD matrix can be embedded, with `poly` blow-up in `log M_N`, as the degree-`N`
  Macaulay Hamiltonian of a `poly(n)`-sparse generator tuple.
- status: CONJECTURE
- depends-on: C-NEW-SP-MINEIG-CONTAINMENT, D-hard-core-generators, D-quantum-k-sat
- where-proved: proposed here; the analogous time-bounded statement is the seed's Prop. 8.2
  (`QMA_1`-hardness of bosonic QSAT), and the analogous complex statement is C-124
- where-tested: none
- north-star relevance: this is the **space analogue of C-124**. It is the only theorem-shaped
  product the space direction offers in the read-only-input model, and it does not depend on any
  gap conjecture.
- traps audited: treating the ground space as the variety; changing the output.

### C-NEW-SP-KRYLOV-WALL
- statement: For the residual spectral hierarchy at order `r = N` on `n` affine variables with
  `B_r = binom(n+r, r)`, an implicit Lanczos or LOBPCG eigensolver retaining `k` Krylov vectors
  requires `8 k B_r` bytes and `Omega(B_r)` arithmetic per matrix-vector product. In particular
  at `k = 20`: `(n, r) = (100, 3) -> 28.3 MB`; `(100, 4) -> 736 MB`; `(100, 5) -> 15.4 GB`;
  `(100, 6) -> 273 GB`; `(300, 3) -> 734 MB`; `(300, 4) -> 55.8 GB`; `(300, 5) -> 3.41 TB`.
  Hence the K-RV8 baseline exhausts a 64 GB workstation at `r = 6` for `n = 100` and at `r = 4`
  for `n = 300`.
- status: CONJECTURE
- depends-on: D-residual-spectral-hierarchy, D-lasserre-order, C-259
- where-proved: arithmetic, this memo §1.3
- where-tested: E1 measures the true `k`
- north-star relevance: bounds the regime in which K-RV8 is decisive, and identifies the order at
  which the time-efficient classical baseline fails.
- traps audited: assuming sparse means quantum-fast only.

### C-NEW-SP-R1-PREMISE
- statement: No published source states that the second-order moment relaxation is loose for
  outlier-robust geometric perception while the third-order relaxation is computationally out of
  reach. Yang-Carlone (arXiv:2109.03349, DOI 10.1109/TPAMI.2022.3179463) use the **lowest** order
  of the hierarchy and report it empirically exact for their truncated-least-squares
  formulations at 30-70 measurements, with sparsity and basis reduction shrinking the SDP at that
  order; TEASER (arXiv:2001.07715), QUASAR (arXiv:1905.12536) and One Ring (arXiv:2006.06769)
  state no such wall. The only documented loss of tightness is for matrix-weighted noise
  (Holmes-Dumbgen-Barfoot, arXiv:2308.07275, DOI 10.1109/TRO.2024.3475220), and the remedy those
  authors propose is **redundant constraints at the same order**, not a higher order. Therefore
  the motivating premise of bet R1 - that robotics needs `r >= 3` - is currently unsupported, and
  every claim in §2.1 of `scouting/robotics-space.md` is conditional on exhibiting a robotics
  family that provably requires `r >= 3`.
- status: CONJECTURE
- depends-on: C-259, C-260, C-261, D-lasserre-order
- where-proved: literature scout, this memo §2.1; four primary sources checked directly, absence
  reported explicitly rather than inferred
- where-tested: E1/E4 would exhibit or fail to exhibit such a family
- north-star relevance: removes the *motivation* for the R1 space claim rather than its
  arithmetic, which is a stronger objection than K-RV8 or K-RV9.
- traps audited: comparing against the wrong classical algorithm; changing the output.

### C-NEW-SP-GLH-BOSONIC
- statement: For every `m = O(1)` there is a family of degree-`m` real homogeneous generator
  tuples in `n+1` variables, with `N = O(1)` or `N = poly(n)`, such that the guided problem
  "given a guiding state with squared ground-space overlap `w >= 1/poly(n)` and a promise
  `gamma_N = Delta/alpha_BE >= 1/poly(n, N)`, estimate `lambda_min(A_N)` to additive
  `eps alpha_A` with `eps >= 1/poly(n,N)`" is BQP-hard; consequently no classical algorithm
  solves it in `poly(n, N)` time and `poly(n, log N)` space unless `BQP = BPP`.
- status: CONJECTURE
- depends-on: D-residual-spectral-hierarchy, D-hamiltonian, C-260, C-099
- where-proved: proposed here; the unrestricted guided-local-Hamiltonian problem is BQP-complete
  (arXiv:2111.09079; 2-local with constant guiding fidelity, arXiv:2207.10250), but `H_N` is
  permutation-invariant on `Sym^N(C^{n+1})` and the hardness is **not** inherited
- where-tested: none
- north-star relevance: the entire conditional content of the surviving R1. Without it, §2.1 has
  no lower bound of any kind on the classical side.
- traps audited: exponentially small overlap; ignoring dequantization; changing the output.
- note: C-099 (Anschuetz-Bauer-Kiani-Lloyd, arXiv:2211.16998) makes the **fixed** local dimension
  case classically easy, so any proof must use `n -> infinity`.

### C-NEW-SP-STREAM-CONSISTENCY
- statement: For every `n` and `alpha = 1/4`, in the one-pass streaming model of
  D-streaming-polynomial-input with the fixed prefix split (point ideal first, binomial ideal
  second), the promise problem SIGN-CONSISTENCY-STREAM(`n`, `alpha`) - decide
  `1 in I_A + I_B` versus `1 not in I_A + I_B`, equivalently `lambda_min(H) = 0` versus
  `lambda_min(H) = 4 alpha n` for the D-hamiltonian of the streamed tuple - is decided with
  error `<= 1/3` by a quantum algorithm using `O(log n)` qubits and `O(log n)` classical bits,
  while every classical randomized one-pass algorithm with error `<= 1/3` uses `Omega(sqrt n)`
  bits. The separation is unconditional.
- status: CONJECTURE
- depends-on: D-boolean-ideal, D-hamiltonian, D-hilbert-function, D-streaming-polynomial-input
- where-proved: proposed here, §2.2; the classical lower bound is
  Gavinsky-Kempe-Kerenidis-Raz-de Wolf arXiv:quant-ph/0611209 Thm 1.2 transferred to streaming by
  the prefix-split reduction; the quantum upper bound is the sequential-projection protocol of
  §2.2, whose success probability telescopes to `2 alpha`
- where-tested: E3 (14 qubits; runs on a laptop)
- north-star relevance: **the only unconditional space separation in the campaign**, on an
  ideal-theoretic decision problem, with a one-photon linear-optics realisation.
- traps audited: changing the output (the output is one bit, on both sides); hidden state
  preparation (the state is prepared by the stream itself); exponentially small overlap (none
  arises).

### C-NEW-SP-LOOPCLOSURE
- statement: The two-robot loop-closure batch certification problem - robot A holds a binary label
  per keyframe, robot B holds `alpha n` disjoint place-revisits with relative binary labels, and
  the batch is promised either wholly consistent or wholly inverted - is an instance of
  `alpha`-Partial Matching. Hence for `alpha = 1/4` it requires `Omega(sqrt n)` bits of one-way
  classical communication from A to B and `O(log n)` qubits, unconditionally; and the quantum
  protocol is realisable with one photon in `n` modes, `n` phase shifters and one beamsplitter.
- status: CONJECTURE
- depends-on: C-NEW-SP-STREAM-CONSISTENCY, D-boolean-ideal
- where-proved: proposed here, §2.2
- where-tested: none; the closest existing experiment is DOI 10.1038/s41467-019-12139-z
- north-star relevance: the campaign's cheapest heuristic-hardware attack and its only
  unconditional application claim, simultaneously.
- traps audited: claiming the coherent-state test as a quantum algorithm (this is not that: the
  classical bound is a proven communication lower bound).

### C-NEW-SP-NO-QUANTUM-TABLE
- statement: For every `L`, every `p > 1/2`, and every quantum encoding `rho(T)` of a table
  `T in {0,1}^L` from which an arbitrary queried bit `T_i` can be recovered with probability at
  least `p`, `rho` occupies at least `(1 - H(p)) L` qubits. Consequently no quantum encoding of a
  precomputed inverse-kinematics or roadmap lookup table saves space over the classical table,
  and the on-robot-table direction admits no space claim.
- status: CONJECTURE
- depends-on: D-input-model
- where-proved: Nayak arXiv:quant-ph/9904093 (FOCS 1999); Ambainis-Nayak-Ta-Shma-Vazirani
  arXiv:quant-ph/9804043, JACM 49(4):496-511 (2002)
- where-tested: none needed
- north-star relevance: closes a direction permanently; a negative result is a product (L5).
- traps audited: changing the output.

### C-NEW-SP-SYNTHESIS-NO-SPACE
- statement: For every six-bar kinematic-synthesis system, the classical algorithm with the
  smallest working space (parameter homotopy continuation, `O(n^2)` doubles per path) is also the
  classical algorithm with the best running time, so no space separation exists in this family;
  in particular for Watt II eight-accuracy-point (22 quadrics in 22 unknowns) the homotopy
  working set is `~4 kB` per path against a degree-23 Macaulay space of dimension
  `binom(45,22) = 4.12e12` that no classical method builds.
- status: CONJECTURE
- depends-on: D-macaulay-matrix, D-saturation-regularity-stable-range
- where-proved: proposed here, §2.4; K5
- where-tested: E2 measures the actual solving degree, which is unpublished
- north-star relevance: confirms K5 inside its true scope and blocks the space direction from
  reclaiming bet R2's territory.
- traps audited: comparing against the wrong classical algorithm.

### C-NEW-SP-TIMESPACE-EXEMPTION
- statement: The quantum time-space tradeoff lower bounds of Beame-Kornerup-Whitmeyer
  (arXiv:2401.05321) for matrix-vector product, matrix multiplication, matrix powering and matrix
  inversion are proved in a query model in which the matrix (or vector) entries are adversarial
  queried inputs; they do not apply to `H_N`, whose rows are generated by a `poly(n)`-size
  classical circuit computable in `O(log M_N)` workspace, and therefore do not obstruct
  C-NEW-SP-GLH-BOSONIC. They do apply to any robotics instance in which the matrix entries are
  measured data that must be read.
- status: CONJECTURE
- depends-on: C-NEW-SP-GLH-BOSONIC, D-block-encoding-normalisation
- where-proved: proposed here, §1.1; the paper contains no explicit disclaimer, so this is a
  reading of its model `[UNVERIFIED]`
- where-tested: none
- north-star relevance: the only known general obstruction to a quantum time-space advantage in
  linear algebra; if the exemption fails, §2.1 dies.
- traps audited: ignoring dequantization.

### Proposed definitions (register format, for `definitions/definitions.md`)

MERGE PROPOSAL (`definitions/definitions.md`, new entry):

#### D-streaming-polynomial-input
A one-pass stream `sigma = (g_1, ..., g_T)` whose items are generators of an ideal
`I = (g_1, ..., g_T) subset R` (D-polynomial-ring), each with `poly(n)` monomials and
`poly(n)`-bit coefficients. An algorithm for `sigma` holds `S(n)` bits, or `S(n)` qubits together
with `S(n)` classical bits, reads each item exactly once in the given order, may not revisit an
item, and produces its output after the last item. The **arrival order** is part of the problem
specification. For a fixed prefix split `sigma = sigma_A sigma_B`, one-pass space is at least the
one-way communication complexity of the induced two-party problem, so every one-way lower bound
transfers. Distinguish from D-input-model, where the whole generator tuple is available for
re-reading and `N` is given in unary.
Source: proposed in `scouting/robotics-space.md` §2.2; streaming conventions follow
Clarkson-Woodruff DOI 10.1145/1536414.1536445 and Kallaugher arXiv:2106.04633.
Pitfalls: the model is vacuous for problems whose input is a small generator tuple and whose
large object (`Phi_N`, `H_N`) is derived; it has content only when the generators themselves are
consumed sensor data. The `Omega(sqrt n)` transfers only under a fixed prefix split; adversarial
interleaving needs the Kapralov-Khanna-Sudan / Kallaugher-Parekh-Voronova machinery.

MERGE PROPOSAL (`definitions/definitions.md`, new entry):

#### D-quantum-space-measure
For an algorithm on a register of `q` logical qubits with a classical control of `c` bits, the
quantum space is `q + c`, counting every ancilla including those of the row oracle and of QSVT
phase angles, and the algorithm's description must be uniform in `O(q + c)` classical workspace.
Two encodings of `R_N` are used and must never be conflated: the **occupation encoding**,
`(n+1) ceil(log_2(N+1))` qubits (D-input-model), and the **compact encoding**,
`ceil(log_2 M_N)` qubits. Fact SP-0 is stated in the compact encoding; the occupation encoding is
larger by a factor `~ (n+1) log(N)/ (N log n)` and quoting a classical bound against it
overstates the advantage.
Source: proposed in `scouting/robotics-space.md` §1.3-§2.1; class definitions from
Fefferman-Lin arXiv:1604.01384 and Fefferman-Remscrim arXiv:2006.03530.
Pitfalls: `q` logical qubits is not a comparable resource to `q` classical bits of DRAM at any
current or projected error rate; a space claim quoted in logical qubits against a classical
byte count is a category error unless said so.

MERGE PROPOSAL (`definitions/definitions.md`, new entry):

#### D-space-time-pareto
A **space advantage** for a problem `P` is a pair of statements: a quantum algorithm attaining
`(S_Q, T_Q)` and a proof that no classical algorithm attains `(S_C, T_C)` with
`S_C = O(S_Q polylog)` and `T_C = O(T_Q polylog)`. By C-NEW-SP-WATROUS-CEILING a pure space
statement (`T` unbounded) can never exceed a quadratic gap in the read-only-input model, so every
nontrivial claim in this campaign is a statement about the `(S, T)` Pareto frontier and must
quote both coordinates for both sides.
Source: proposed in `scouting/robotics-space.md` §0, §1.0.
Pitfalls: a space advantage bought with exponential time is not a claim (brief, task 2); nor is a
time advantage bought with exponential space. The three classical points that must always be
quoted for a succinctly-specified operator are: time-efficient (`O(M_N)` space), space-efficient
(`O(log^2 M_N)` space, `poly(M_N)` time), and any sparsity-exploiting solver in between.

---

## 5. First experiments, each `<= 1` day

**E1 - How many Krylov vectors does a level-3 perception instance actually need?**
Take a single-rotation-averaging or point-cloud-registration TLS instance from the
MIT-SPARK CertifiablyRobustPerception family at `K = 20, 40, 60` correspondences (so
`n ~ 27, 47, 67`). Build `A_N` for `N = r = 2, 3, 4` implicitly (matvec only, no dense matrix)
with `bf.py`. Run LOBPCG with and without the Gauss-Newton guiding vector; record `k`, the number
of Krylov vectors needed for `10^{-6}` relative accuracy in `lambda_min`, and the resulting
`8 k B_r` bytes. Compare against `ceil(log_2 B_r)` qubits and against `O(log^2 B_r)` bits.
*Decides:* the constant in C-NEW-SP-KRYLOV-WALL, i.e. whether the classical time-efficient space
wall sits at `r = 5` or `r = 7`. *Falsifies:* C-NEW-SP-KRYLOV-WALL if `k` is `O(1)` and the wall
moves out of reach.

**E2 - What is the actual solving degree of a synthesis system?**
Nine-point four-bar (8 equations, `n = 8`, `D = 8652`) in `msolve` or Macaulay2 over a large
prime: compute the degree at which the Macaulay matrix first attains the rank implying the
zero-dimensional quotient, i.e. the solving degree, and compare with the Lazard bound `9` and
with `binom(17,8) = 24310`. Then attempt the same on a Watt II subsystem (a truncation to 12-14
of the 22 equations) to see whether the solving degree grows like the Lazard bound `23` or much
more slowly. *Decides:* whether the 33 TB figure in §2.4 is real or an artefact of a loose bound,
and supplies the first published solving degree for a six-bar synthesis system.
*Falsifies:* C-NEW-SP-SYNTHESIS-NO-SPACE is unaffected either way (homotopy still wins), but a
small solving degree would reopen a Macaulay route for bet R2.

**E3 - Simulate the streaming consistency separation. This is the cheapest decisive experiment
in the lane and it runs on a laptop.**
`n = 2^{10}` to `2^{16}` needs 10 to 16 qubits, i.e. a state vector of at most 65536 amplitudes.
(a) Implement the §2.2 protocol exactly (phase updates, then sequential two-outcome projections),
with `c = 1, 2, 3` parallel registers; verify empirically that the miss probability is
`(1 - 2 alpha)^c` and that a hit is always correct under the promise.
(b) Implement the best classical bounded-memory heuristics at `S = 8, 16, 32, 64, 128, 256` bits:
a random sample of `S/log n` indices of `a`; a linear sketch of `a` over `F_2`; a Bloom-filter
parity sketch. Measure the empirical `S` at which error drops below `1/3`, and compare with the
`Omega(sqrt n)` theorem.
(c) Break the promise: sweep the outlier fraction from 0 to 1/2 and record where the quantum
protocol's advantage disappears. *Decides:* whether C-NEW-SP-STREAM-CONSISTENCY's promise is a
knife edge or has a robust neighbourhood. If the advantage vanishes for any outlier fraction
strictly between 0 and 1/2, the robotics reading of C-NEW-SP-LOOPCLOSURE should be recorded as
REFUTED and only the promise-problem theorem kept.

**E4 - Does the overlap collapse exactly where the relaxation is loose?**
This is bet R1's first experiment restated as a space-time test. For the same instances as E1,
compute `w = |<p*^{⊗N}|psi_0>|^2` for `N = 3, 4, 5`, separately for instances where the level-2
relaxation is tight and where it is loose, and tabulate the implied quantum time
`alpha_A/(eps sqrt w)` against the classical Lanczos time `k nnz(A_N)`. *Decides:* whether §2.1's
(space, time) claim survives; a collapse of `w` on the loose instances converts the space
advantage into a space advantage bought with exponential time, which per the brief is not a
claim. Record as REFUTED if so.

**E5 - Does chordal sparsity actually help robust perception?**
Build the variable-interaction (correlative sparsity) graph of Yang-Carlone TLS at
`K = 50, 100, 300` correspondences, run a greedy min-fill / min-degree elimination, and record
the largest clique and the treewidth bound. Compare `binom(clique + r, r)` against `B_r`.
*Decides:* the precise regime of K-RV9. If the hub makes the largest clique `Theta(K)`, K-RV9's
scope is pose-graph SLAM only and the R1 target family is untouched by it.

---

## 6. Killers of the space direction (mine, sharp)

**KS1 - The `s -> s^2` ceiling kills the headline comparison outright.** By
C-NEW-SP-WATROUS-CEILING, "`O(n log N)` qubits versus `M_N` classical words" is not a space
separation and never was. The true classical space for the R1 observable at `n = 100, r = 3` is
about 304 bits. This is a stronger killer than K-RV8, it is unconditional, and it applies to
every "compact register versus large matrix" argument anywhere in this campaign, including the
seed's §5 framing and bet R3's `O(n log N)` qubits against `binom(2n,n)`.

**KS2 - The quadratic ceiling is not achieved by anything anyone has proved.** `BQL` versus
`BPL` versus `L` is open. There is no unconditional quantum space separation for any
linear-algebraic problem in the read-only-input model. So the best available outcome in model (a)
is a *completeness theorem*, not a separation - and completeness is two-edged: proving
C-NEW-SP-MINEIG-HARDNESS proves the problem is in `BQ_USPACE[O(log M_N)]`, hence in
`DSPACE(O(log^2 M_N))`, hence *classically space-cheap*. The theorem we most want to prove is
also the theorem that most decisively kills the space story.

**KS3 - Beame-Kornerup-Whitmeyer.** For explicitly presented matrix problems there is **no**
quantum time-space advantage at any space bound. The lane's escape (C-NEW-SP-TIMESPACE-EXEMPTION)
is that `H_N` is succinct. Note what this costs: it means the space direction can only ever apply
to problems whose data are `poly(n)` polynomials, never to problems whose data are `Theta(T)`
measurements. **Robotics has exactly one problem of the first kind (perception certification with
few residual templates) and its most space-hungry problems are all of the second kind.**

**KS4 - The regime tension of §1.3, unresolved.** Model (c) needs `N` to grow for `M_N` to be
large; the classical space cost only exists where `N` is small (perception, `r <= 5`); and where
`N` must grow (synthesis) the classical method has no space cost. I could not find a robotics
family in which large `N` and a real classical space cost coincide. If none exists, model (c) is
empty for robotics regardless of everything else in this memo.

**KS4b - The R1 premise is unsupported (C-NEW-SP-R1-PREMISE), and this is the worst finding in
the memo.** A dedicated literature pass over Yang-Carlone, TEASER, QUASAR and One Ring found no
statement that level 2 is loose and level 3 out of reach; Yang-Carlone use the lowest order and
call it empirically exact. The one documented non-tightness is matrix-weighted noise, whose
authors' remedy is redundant constraints at the same order. So the entire perception space story
is aimed at a wall that, on present evidence, nobody has hit. Unless a family requiring `r >= 3`
is exhibited, §2.1 has no application and the space direction reduces to §2.2 alone.

**KS5 - Coherence across a sensor stream.** The §2.2 protocol needs a coherent `log n`-qubit
register held across the entire pass. A 10^4-measurement SLAM stream at 30 Hz is five minutes.
That is a harder requirement than any batch algorithm in this campaign, and it is required by the
one claim that is unconditional.

**KS6 - The margin is arithmetically tiny.** `sqrt n` versus `log n` is 100 bits versus 14 qubits
at `n = 10^4` and 1000 bits versus 20 qubits at `n = 10^6`. The Nature Communications experiment
needed input size ~3000 before it beat the best known classical protocol *in transmitted
information*, using a modified problem (Sampling Matching) because the original Hidden Matching
advantage was unreachable. No robotics link is bandwidth-limited at the level of 100 bits.

**KS7 - Space is not what robotics is short of, and there is now a number for it.** Embedded
platforms ship 8-32 GB. The level-3 perception figure at `n = 100` is 250 GB dense but 28 MB by
Lanczos and 304 bits by theorem. Deployed sliding-window VIO uses **2.4 MB** for the optimizer
against a ~300 MB whole-process peak dominated by everything except the optimization
(arXiv:2109.02182). There is no deployed robotics computation whose binding constraint is memory
rather than latency, power or determinism, and no formal space lower bound for SLAM or bundle
adjustment exists to appeal to. Even a correct space theorem would not be bought. (This is K4 in
space clothing and it has not weakened.)

**KS8 - Every available separation is a promise problem.** Fefferman-Lin min-eigenvalue,
`alpha`-Partial Matching, guided local Hamiltonian: all promise problems. The robotics instance
must satisfy the promise, and "all inliers or exactly half outliers" is not an outlier model.
Removing the promise from §2.2 lands in Kallaugher-Parekh territory, where the classical
`Omega(n)` bound holds **even against quantum streaming algorithms**.

**KS9 - The quantum space measure is not commensurable with the classical one.** `18` logical
qubits at any projected error rate is `10^3`-`10^5` physical qubits plus a factory; the classical
side being beaten is `28 MB` of DRAM, or `304` bits. D-quantum-space-measure records this; it
does not repair it.

**KS10 - The output is still a scalar you must trust the device for** (K-RV10). Nothing in the
space direction changes the certification-culture objection; a smaller register does not make a
quantum-only lower bound into an SOS certificate.

**KS11 - The streaming claim is not new mathematics.** The separation is
Gavinsky-Kempe-Kerenidis-Raz-de Wolf, transferred by a standard prefix-split reduction, in the
style Kapralov-Khanna-Sudan and Kallaugher already use. What is new here is only the *algebraic
framing* (a streamed binomial ideal on the sign hypercube; a streamed frustration-free-versus-
frustrated decision) and the *robotics instance*. Under the north star's "genuinely new" clause
that is a new bridge with old objects on both ends - the same objection §18 Q3 of the robotics
memo raised against bet R1's identification.

---

## 7. Questions for TJO

1. **Does a simultaneous (space, time) claim count as a space claim under D2?** By KS1 a pure
   space claim can never exceed a quadratic gap in the read-only-input model, so if D13's "space
   direction" means space alone with time unbounded, the honest answer is that the direction is
   closed by C-NEW-SP-WATROUS-CEILING and this memo's job is done. If it means the Pareto pair
   `(S, T)` of D-space-time-pareto, §2.1 survives and needs C-NEW-SP-GLH-BOSONIC proved.

2. **Is a promise problem an acceptable robotics deliverable?** Every space separation available
   - Fefferman-Lin min-eigenvalue, `alpha`-Partial Matching, guided local Hamiltonian - is a
   promise problem, and the robotics instance must satisfy the promise. If not, the lane closes
   after E3.

3. **Does bandwidth count as space?** The only unconditional separation in the campaign is a
   *communication* separation (C-NEW-SP-LOOPCLOSURE), and its robotics setting is deep-space,
   under-ice or acoustic links between robots. This is a different resource from memory. If D13
   means memory only, C-NEW-SP-LOOPCLOSURE is out of scope and should be moved to a
   communication-complexity lane or dropped.

4. **Is a completeness theorem a product, given that it also proves the problem is classically
   space-cheap (KS2)?** C-NEW-SP-MINEIG-HARDNESS would be the space analogue of C-124 and would
   be, as far as this pass could determine, the first `BQ_USPACE`-complete problem from algebraic
   geometry. It is also self-defeating as a speedup claim. Same question as PRD §7 Q4.

5. **Which of the two survivors gets the budget?** They are disjoint and cannot both be pursued.
   (i) *Streaming/communication*: unconditional, tiny margin, needs a quantum channel or a
   long-lived coherent register, has an existing table-top realisation, is not new mathematics.
   (ii) *Succinct operator*: large nominal margin, conditional on `BQP != BPP` **and** on an
   unproven bosonic guided-local-Hamiltonian hardness, blocked by KS4's regime tension, and now
   also missing its motivating application (KS4b).
   My recommendation: (i) for one week to run E3 and settle whether the promise has a robust
   neighbourhood, because it is the only unconditional statement in the campaign and its hardware
   attack is a bench-top experiment; then (ii) only if somebody first answers Q9 below.

6. **Should Fact SP-0 be ratcheted immediately as a campaign-wide constraint?** It refutes the
   space sentence of bet R1 more strongly than K-RV8 did (which D12 already acted on), and it
   also applies to bet R3's `O(n log N)` qubits versus `binom(2n,n)` framing and to the seed's
   §5 register argument. Recommendation: yes, enter C-NEW-SP-WATROUS-CEILING before any further
   space number is quoted anywhere, and audit every existing row that compares a qubit count to a
   classical word count.

7. **Reference verification budget, specifically for Fact SP-0.** The Watrous 2003 and
   Borodin-Cook-Pippenger 1983 primary texts could not be fetched in readable form in this pass;
   the `DSPACE(s^2)` half is corroborated by a direct quotation in Fefferman-Remscrim, but the
   `DTIME(2^{O(s)})` half rests on secondary summaries. Fact SP-0 is now the load-bearing
   statement of the whole space direction. Half a day of library access before it is quoted
   outside the repo?

8. **The brief's Bury-Schwiegelshohn citation appears not to exist.** Their joint record contains
   no paper on streaming spectral quantities. Should mis-citations found in briefs be recorded as
   rows, or fixed silently in the brief?

9. **Does anyone know a robotics family that provably needs Lasserre order `r >= 3`?** This is a
   question for TJO's network rather than for a literature search, which has already failed
   (C-NEW-SP-R1-PREMISE). If the answer is no, bet R1 should be closed as unmotivated rather than
   as arithmetically wrong, and D12's reframing does not save it. If the answer is yes, name the
   family and E1/E4 become worth running.

10. **Should the corrections this pass produced be merged into the robotics memo?** Four
    `[UNVERIFIED]` synthesis root counts are now resolved with DOIs (Watt II
    DOI 10.1115/1.4027443, Stephenson II DOI 10.1115/1.4031124, Stephenson III
    DOI 10.1016/j.mechmachtheory.2015.10.004, nine-point DOI 10.1115/1.2916909); the contact-mode
    counts in §12 are wrong by three orders of magnitude (168,746 SS-modes for Box-box-2, not
    "50-400"); and Stephenson II is ten degree-8 equations in ten unknowns, not 26 unknowns.
    Robotics memo §18 Q6 asked whether the DOI-resolution half-day was worth it; it was, and it
    is done for §4.

---

## 8. References resolved in this pass

**Quantum space complexity.** Watrous, JCSS 59(2):281-326, 1999, DOI 10.1006/jcss.1999.1655
(`BQPSPACE = PSPACE`; primary text not fetched, `[PARTIALLY VERIFIED]`). Watrous,
Comput. Complexity 12:48-84, 2003, DOI 10.1007/s00037-003-0177-8 (`PrQSPACE(s) = PrSPACE(s)`;
`[PARTIALLY VERIFIED]`). Borodin-Cook-Pippenger, Inf. Control 58(1):113-136, 1983,
DOI 10.1016/S0019-9958(83)80060-6 (`PrSPACE(s) subset NC^2(2^s) subset DSPACE(s^2) ∩ DTIME(2^{O(s)})`;
`[PARTIALLY VERIFIED]`). Ta-Shma, STOC 2013, DOI 10.1145/2488608.2488720 (no arXiv posting
exists). Fefferman-Lin, ITCS 2018, arXiv:1604.01384, DOI 10.4230/LIPIcs.ITCS.2018.4 (Defs. 10,
13, 17 quoted in §1.1). Fefferman-Lin, arXiv:1601.01975 (`QMA_EXP = PSPACE`; separate venue
`[UNVERIFIED]`). Fefferman-Remscrim, STOC 2021, arXiv:2006.03530, DOI 10.1145/3406325.3451051.
Girish-Raz-Zhan, ICALP 2021, arXiv:2006.04880, DOI 10.4230/LIPIcs.ICALP.2021.73. Girish-Raz,
ITCS 2022, arXiv:2106.11877, DOI 10.4230/LIPIcs.ITCS.2022.76. Apers-Edenhofer, CCC 2025,
arXiv:2408.12473, DOI 10.4230/LIPIcs.CCC.2025.18. Remscrim, ITCS 2021, arXiv:2003.09877.
Space-bounded quantum state testing via space-efficient QSVT, arXiv:2308.05079.

**Classical parallel/space baselines.** Csanky, SIAM J. Comput. 5(4):618-623, 1976,
DOI 10.1137/0205040. Borodin-von zur Gathen-Hopcroft, Inf. Control 52(3):241-256, 1982,
DOI 10.1016/S0019-9958(82)90766-5. Cook, Inf. Control 64(1-3):2-22, 1985,
DOI 10.1016/S0019-9958(85)80041-3 (the class `DET`, `DET subset NC^2 subset DSPACE(log^2 n)`).
No BPL algorithm for general well-conditioned inversion was found; the closest are eigenvalue
approximation for stochastic matrices (DOI 10.1007/s00037-016-0150-y) and probabilistic-logspace
Laplacian solvers (DOI 10.4230/LIPIcs.APPROX-RANDOM.2017.41).

**Quantum time-space tradeoffs (negative).** Beame-Kornerup-Whitmeyer, STOC 2024,
DOI 10.1145/3618260.3649700; SICOMP DOI 10.1137/24M1710164; arXiv:2401.05321.

**One-way communication and streaming.** Bar-Yossef-Jayram-Kerenidis, STOC 2004,
DOI 10.1145/1007352.1007379; SICOMP 38(1):366-384, DOI 10.1137/060651835 (no arXiv posting found;
bound corroborated from GKKRdW's restatement, `[PARTIALLY VERIFIED]`).
Gavinsky-Kempe-Kerenidis-Raz-de Wolf, STOC 2007, arXiv:quant-ph/0611209,
DOI 10.1145/1250790.1250866; SICOMP 38(5):1695-1708, DOI 10.1137/070706550 (Thm 1.2:
`R^1(alpha PM) = Theta(sqrt n)`, `Q^1 = O(log n)` at `alpha = 1/4`). Le Gall, SPAA 2006,
arXiv:quant-ph/0606066, Theory Comput. Syst. 45(2):188-202, DOI 10.1007/s00224-007-9097-3.
Kallaugher, FOCS 2021, arXiv:2106.04633, DOI 10.1109/FOCS52979.2021.00091. Kallaugher-Parekh,
FOCS 2022, arXiv:2206.00213, DOI 10.1109/FOCS54457.2022.00054 (the negative result).
Kallaugher-Parekh-Voronova, STOC 2024, arXiv:2311.14123, DOI 10.1145/3618260.3649709.
Kapralov-Khanna-Sudan, SODA 2015, Boolean Hidden Partition `[UNVERIFIED DOI]`. Noisy Boolean
Hidden Matching, ITCS 2022, DOI 10.4230/LIPIcs.ITCS.2022.91. Preprints not yet peer reviewed and
therefore not relied on here: arXiv:2606.05366 (Max-kSAT streaming), arXiv:2604.18014 (entropy,
multi-pass), arXiv:2607.08517 (negative, triangle finding).

**Classical streaming lower bounds for linear algebra.** Clarkson-Woodruff, STOC 2009,
DOI 10.1145/1536414.1536445 (Thm 5.2, `Omega(k^2)` bits for exact rank decision, turnstile).
Li-Woodruff, STOC 2016, arXiv:1604.08679. Li-Woodruff, RANDOM 2016,
DOI 10.4230/LIPIcs.APPROX-RANDOM.2016.39. Andoni-Nguyen, SODA 2013 (upper bounds, not lower;
`[UNVERIFIED DOI]`). **Bury-Schwiegelshohn on spectral quantities: no such paper found
`[UNVERIFIED]`.**

**Random access codes.** Nayak, FOCS 1999, arXiv:quant-ph/9904093.
Ambainis-Nayak-Ta-Shma-Vazirani, JACM 49(4):496-511, 2002, arXiv:quant-ph/9804043.

**Hardware.** Kumar-Kerenidis et al., Nat. Commun. 10:4152 (2019),
DOI 10.1038/s41467-019-12139-z (Sampling Matching, coherent-state phase encoding, fixed
linear-optics circuit, single-photon detection, advantage above input size ~3000).

**Robotics baselines resolved in this pass.** Yang-Carlone, IEEE TPAMI 2022, arXiv:2109.03349,
DOI 10.1109/TPAMI.2022.3179463 (lowest-order relaxation, empirically exact at 30-70 measurements;
STRIDE = SpecTrahedral pRojected gradIent Descent along vErtices; up to 100x faster than MOSEK;
`[UNVERIFIED]` for any GB memory figure). Yang-Shi-Carlone TEASER, IEEE T-RO 2020,
arXiv:2001.07715, DOI 10.1109/TRO.2020.3033695. Yang-Carlone QUASAR, ICCV 2019, arXiv:1905.12536,
DOI 10.1109/ICCV.2019.00175. Yang-Carlone One Ring, NeurIPS 2020, arXiv:2006.06769.
Holmes-Dumbgen-Barfoot, IEEE T-RO 40:4805-4824, 2024, arXiv:2308.07275,
DOI 10.1109/TRO.2024.3475220 (matrix-weighted non-tightness; remedy is redundant constraints).
Rosen-Carlone-Bandeira-Leonard SE-Sync, IJRR 2019, arXiv:1612.07386, DOI 10.1177/0278364918784361.
Dellaert-Rosen-Wu-Mahony-Carlone Shonan, ECCV 2020, arXiv:2008.02737.
Kaess-Johannsson-Roberts-Ila-Leonard-Dellaert iSAM2, IJRR 31(2):217-236, 2012,
DOI 10.1177/0278364911430419. Dellaert-Kaess Square Root SAM, IJRR 25(12):1181-1204, 2006,
DOI 10.1177/0278364906072768. Demmel-Schubert-Sommer-Cremers-Usenko, ICCV 2021, arXiv:2109.02182
(the 2.4 MB sliding-window figure). Qin-Li-Shen VINS-Mono, arXiv:1708.03852. Leutenegger et al.
OKVIS, IJRR 2015 (`[UNVERIFIED]` for any numeric memory bound). Mourikis-Roumeliotis MSCKF,
ICRA 2007. Plecnik-McCarthy Watt II, DOI 10.1115/1.4027443; Stephenson II,
DOI 10.1115/1.4031124; Stephenson III, DOI 10.1016/j.mechmachtheory.2015.10.004.
Wampler-Morgan-Sommese, ASME JMD 114(1):153-159, 1992, DOI 10.1115/1.2916909.
Chien et al. GPU-HC, CVPR 2022, arXiv:2112.03444, DOI 10.1109/CVPR52688.2022.01531.
Huang-Cheng-Mason, WAFR 2020, DOI 10.1007/978-3-030-66723-8_29.
**Reported absent after direct search:** any published Macaulay degree, solving degree or
Castelnuovo-Mumford regularity for a six-bar synthesis system; any formal space-complexity or
memory-bounded lower bound for SLAM or bundle adjustment; any published statement that level 2 is
loose and level 3 out of reach for robust perception; any memory-per-path statement for
HomotopyContinuation.jl or Bertini.

**Carried over from the other lanes, not re-verified here.** Gharibian-Le Gall arXiv:2111.09079;
arXiv:2207.10250; Anschuetz-Bauer-Kiani-Lloyd arXiv:2211.16998 (Quantum 7:1189);
Fang-Fawzi arXiv:1908.05155; Lovitz-Johnston arXiv:2310.17827; DOI 10.1137/24M1717750;
Lasserre DOI 10.1137/S1052623400366802; TSSOS arXiv:2103.00915; CS-TSSOS arXiv:2005.02828;
Canny, MIT Press 1988.

---

## 9. Lane report

**Delivered.** Three formal models of quantum space advantage with resolved citations and exact
theorem statements (§1); five robotics instances in the brief's Input/Observable/Quantum
space/Classical space/Time format with the requested `B_r` tables at `n = 50, 100, 300` (§2);
a regime-by-regime audit of K5, K6, K-RV8 and K-RV9 (§3); eleven claim rows `C-NEW-SP-*` and three
proposed definitions in register format (§4); five experiments each `<= 1` day (§5); twelve
killers of my own and ten questions (§6, §7).

**The three findings that matter most.**
1. Fact SP-0, `BQSPACE(s) subset DSPACE(s^2) ∩ DTIME(2^{O(s)})`, which is the correct form of K6
   and which refutes the "compact register versus large matrix" argument campaign-wide, including
   bet R1, bet R3 and the seed's §5 framing. Nobody in the campaign had this.
2. C-NEW-SP-STREAM-CONSISTENCY: an unconditional exponential quantum space separation for an
   ideal-theoretic decision problem, with a one-photon linear-optics protocol that satisfies the
   north star's hardware clause and has a laboratory precedent.
3. C-NEW-SP-R1-PREMISE: bet R1's motivating wall is not documented anywhere. This is a worse
   objection than K-RV8's, because it removes the application rather than the arithmetic.

**Could not pin down.** (i) The `DTIME(2^{O(s)})` half of Fact SP-0 rests on secondary summaries;
the Watrous 2003 and Borodin-Cook-Pippenger 1983 primary texts could not be fetched
(§7 Q7). (ii) Whether the bosonic symmetric-sector guided local Hamiltonian is BQP-hard
(C-NEW-SP-GLH-BOSONIC) - this is the load-bearing open problem of §2.1 and it is a real theorem
to prove, not a numerics question. (iii) Whether any robotics family needs `r >= 3` (§7 Q9).
(iv) Whether the Boolean Hidden Partition generalisation of §2.2 to non-matching loop-closure
graphs preserves the `Omega(sqrt n)` bound; Kapralov-Khanna-Sudan did this for Max-Cut and the
transfer looks routine but was not checked.

**Length.** 1300 lines against a 500-900 target. The overrun is in §2 and §4, and is caused by
the brief's requirement that every instance carry both classical space baselines plus the time
column, and by the ratchet format for ten claim rows. No content was padded; nothing was cut to
fit because cutting a verified citation to hit a line count is the wrong trade. Flagging rather
than trimming.

**Corrections this lane owes other artifacts** (orchestrator's call; no shared file touched):
- `scouting/robotics-deep-dive.md` §4: four `[UNVERIFIED]` synthesis root counts resolved
  (DOIs in §8); Stephenson II is ten degree-8 equations in ten unknowns, not 26 unknowns.
- `scouting/robotics-deep-dive.md` §12: contact-mode counts are wrong by three orders of
  magnitude (168,746 SS-modes for Box-box-2, not "50-400"); exact complexities in §2.5.
- `scouting/robotics-deep-dive.md` §10 and Bet R1: the "level 2 is not tight, level 3 is
  infeasible" premise is unsupported (C-NEW-SP-R1-PREMISE).
- `scouting/robotics-deep-dive.md` K6 and `scouting/real-variety.md` K-RV8: both should cite
  Fact SP-0 rather than `BQPSPACE = PSPACE` and `O(B_N)`-Lanczos respectively.
- `briefs/lane-robotics-space.md`: the Bury-Schwiegelshohn citation does not appear to exist.

**MERGE PROPOSAL (`claims/CLAIMS.md`).** Eleven rows, all CONJECTURE: C-NEW-SP-WATROUS-CEILING,
C-NEW-SP-MINEIG-CONTAINMENT, C-NEW-SP-MINEIG-HARDNESS, C-NEW-SP-KRYLOV-WALL,
C-NEW-SP-R1-PREMISE, C-NEW-SP-GLH-BOSONIC, C-NEW-SP-STREAM-CONSISTENCY, C-NEW-SP-LOOPCLOSURE,
C-NEW-SP-NO-QUANTUM-TABLE, C-NEW-SP-SYNTHESIS-NO-SPACE, C-NEW-SP-TIMESPACE-EXEMPTION.
Recommended sequencing: C-NEW-SP-WATROUS-CEILING first (it constrains every other space row in
the DAG and forces an audit of C-NEW-SP-KRYLOV-WALL's framing, bet R1 and bet R3), then
C-NEW-SP-R1-PREMISE (it decides whether §2.1 has an application at all), then
C-NEW-SP-STREAM-CONSISTENCY with experiment E3.

**MERGE PROPOSAL (`definitions/definitions.md`).** Three entries: D-streaming-polynomial-input,
D-quantum-space-measure, D-space-time-pareto (all in register format in §4).

**MERGE PROPOSAL (`PRD.md` §6, decision record, to append).** A candidate D15: "Space claims are
stated as `(space, time)` Pareto pairs per D-space-time-pareto. A pure space claim is bounded by
`BQSPACE(s) subset DSPACE(s^2)` (C-NEW-SP-WATROUS-CEILING) and is not a north-star hit; the
unconditional separations available to the campaign are in the streaming and one-way
communication models only." Pending TJO answer to §7 Q1 and Q3.
