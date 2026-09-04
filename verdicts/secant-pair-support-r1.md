# Independent audit of pair support and the four-copy gap

2026-09-05. Reviewer: root, independently checking the construction by the
`round2_critic` subagent (which acted as proposer for this separate task).
Reviewed `scouting/secant-pair-support.md`, its canonical definitions, and
C-339--C-341. The review is confined to the stated mathematics. It does not
certify historical originality or the north-star algorithm requirement.

**VERDICT: PASS for C-339, C-340 and C-341.** No FATAL or MAJOR objection remains
for these three statements. One scope wording issue was corrected before this
verdict. Their promotion to PROVED is authorized by this independent review.

## 1. Algebraic support, C-339

Both containments were reconstructed. At t=r+1, pigeonhole repetition in a
power of a sum of r product vectors gives the symmetrized repeated-pair span.
Conversely each mixed coefficient is obtained by finite polarization in r
scalar parameters. This argument does not assume a decomposition of an unknown
input is available to a quantum circuit. Product vectors span each remaining
replica, and squares of product vectors span the tensor product of local
symmetric-square spaces, exactly the range of B_12.

The finite-dimensional identity range(T)=range(T T^dag) gives the asserted
support for T=P B_12. Twirling B_12 gives the uniform pair average, but that
average agrees with A_t only after restriction to global replica invariants.
The manuscript and row retain this necessary restriction. Border closure,
nonzero normalization, r=1, and k=1 cause no exceptional failure.

**Decision: ACCEPT C-339 as PROVED.**

## 2. Representation compression, C-340

The transposition-fixed dimensions 1,2,1,1,0 for the five S4 types are correct.
The normal/plane cofactor identity gives the sign-twisted line compression as
det(C_g). The perfect-matching action gives precisely beta=1 or -1/2. These
facts were independently evaluated on all 24 permutation matrices.

The party Schur block (a-j,j) carries det^j tensor Sym^(a-2j). Its unitary
normalization is the normalized Dicke metric, not the monomial coefficient
metric. The archived checker compares this symmetric-power formula with
explicit tensor powers and compares the entire 2^a-dimensional group spectrum
with the multiset of small-block spectra and the correct Schur multiplicities.

The seven matrix types and their counts exhaust all 24 permutations. Their
parity sum yields the rank-one term and the coefficient in (PAIR-4), including
the important singular-matrix zeroth-power convention. A local 1111 type has
no positive spectrum. Weyl factors are spectators only when the corresponding
type actually occurs at the supplied local dimensions.

**O1 — MINOR, corrected: occurrence qualification.**
Location: C-340's first sentence. A union over unrealizable local types could
add spurious spectra for small local dimensions.
**FIX DEMAND:** State that the union is over occurring local-type patterns and
party irreps, and that only their nonzero eigenvalues are included.
**SURVIVING STATEMENT:** The formula exactly covers every occurring block.
The corrected wording is now in C-340; this objection is closed.

**Decision: ACCEPT C-340 as PROVED.**

## 3. Uniform bound and sharpness, C-341

The proof was checked case by case, rather than inferred from the finite scan.

- C has eigenvalues 1 and -1/2. Its normalized symmetric power has eigenvalues
  (-1/2)^j, so the two rank-one outlier inequalities are valid. Compression by
  the inverse of D_0 preserves the indicated one-outlier bounds because that
  inverse is a contraction; this is the place where metric control matters.
- At odd ell and h=0, the weight-zero vector is a decoupled kernel vector.
  Its negative diagonal term may be removed only after this is established.
- For h+c>=2 the elementary upper/lower bounds on S give 1/12 directly.
  Any remaining extra rank-one term is positive.
- At h+c=1 the displayed projected tensor powers supply the single exceptional
  eigenvalue 1/2. Rank-one interlacing controls every other eigenvalue by 1/4.
  The ell=0,1 empty-block cases are correctly separated.
- At h=c=0 the projected one-excitation vector supplies eigenvalue -1/4.
  Every other eigenvalue is at least -1/8. The ell=1,3 exceptions are explicitly
  computed and consistent with the formula. The coefficient proportional to
  ell-3 verifies why the odd-ell vector becomes nonzero at ell>=5.
- Congruence is not treated as unitary equivalence: the comparison follows
  from the nonzero spectrum of N^(1/2) D_0^2 N^(1/2)>=N for N>=0,D_0>=1.
  Thus kernel vectors do not invalidate the lower bound on positive eigenvalues.

All parameters in the representation reduction fall into one of these cases.
At ell=0,h=2,c=1 the scalar is exactly 1/12. The type pattern 211,211,22
exists at local dimensions 3,3,2, so sharpness is achieved in an actual tensor
space, not merely a formal block. The upper bound is the compression-of-a-
projector bound. C-339 identifies its support, giving the claimed operator
inequalities including zero extensions.

**Decision: ACCEPT C-341 as PROVED.**

## 4. Red-capable finite verification and limits

`checkers/explore/secant_pair_support.py` passed 1415 checks in 0.2 seconds,
with one BLAS thread and a 60-second timeout. It covers 425 analytic blocks,
all 24 permutation compressions, explicit tensor/symmetric-power comparisons,
and full compressed spectra for a<=6,b,c<=2. It finds the sharp value 1/12.
Both mutations exit 1: dropping the exceptional rank-one term changes the
trivial block by 1/6; changing the interference sign changes a different
group spectrum by 2/3. These checks support the algebraic audit but do not
replace its all-parameter proof.

The claims register is the sole source of status. No correctness claim in
this verdict implies that the spanning identity or gap is historically new.
Section 5's generic-filter implementation consequence is outside these three
promotions; in particular it does not meet D22 merely because the gap is uniform.
No original quantum algorithm or end-to-end classical-input advantage has been
established by this review.
