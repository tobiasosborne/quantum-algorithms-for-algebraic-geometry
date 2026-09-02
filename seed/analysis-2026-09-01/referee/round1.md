1. **Sections 1–2 — significant.** Bargmann–Fock, Drury–Arveson, and sphere norms agree only degreewise. Their full graded direct sums are not the same Hilbert module under the identity map. Kernel statements survive; boundedness, spectra, curvature, and essential normality do not. Fix: specify the Hilbert norm whenever passing between degrees.

2. **Section 2.2 — significant.** The compressed Fock creation operator is not Arveson’s \(d\)-shift. On degree \(N\),
   \[
   M_{z_i}^{DA}=\frac{a_i^\dagger}{\sqrt{N+1}}.
   \]
   Arveson–Douglas statements apply to these normalized bounded shifts, not to the unbounded Fock \(a_i^\dagger\). Also the space is \(H^2_{n+1}\), not \(H^2_n\).

3. **Section 2.2 — minor.** Calling \(R_N=I_N\oplus I_N^\perp\) for an arbitrary ideal “the Fischer decomposition” overstates the terminology. The equality is elementary orthogonal decomposition; classical Fischer decomposition normally refers to more structured principal/harmonic situations.

4. **Section 3, tensor normalization — minor.** The definition
   \[
   |F\rangle=\sum_\alpha f_\alpha\frac{\alpha!}{m!}\sum_{\operatorname{cont}(w)=\alpha}|w\rangle
   \]
   and \(\|F\|^2=\sum_\alpha |f_\alpha|^2\alpha!/m!\) are correct. But under the unitary Fock-to-tensor identification,
   \[
   |p\rangle^{\otimes N}\longleftrightarrow \frac{(p\cdot z)^N}{\sqrt{N!}},
   \]
   not \((p\cdot z)^N\). The report silently switches between normalized and unnormalized representatives.

5. **Section 3, local Hamiltonian formula — minor.** The factorial is correct, but the exact operator statement is
   \[
   U_NH_NU_N^\dagger
   =P_{\rm sym}\!\left[m!\sum_{|S|=m}(|F\rangle\langle F|)_S\right]P_{\rm sym}.
   \]
   Individual subset terms do not preserve \(\operatorname{Sym}^N\); only their permutation-invariant sum does.

6. **Section 3, “projectors” — minor.** \(|F\rangle\langle F|\) is a projector only when \(\|F\|=1\). In general it is \(\|F\|^2\) times a rank-one projector. This matters when quoting endpoint gaps.

7. **Section 3, coherent-state energy — minor.** After correcting the normalization in finding 4, the stated formula is correct:
   \[
   \langle p^{\otimes N}|H_N|p^{\otimes N}\rangle
   =\sum_j\frac{N!}{(N-m_j)!}|f_j(\bar p)|^2 .
   \]
   The algebraic point is \(\bar p\). Equivalently, a point \(x\in V(I)\) gives the physical state \(|\bar x\rangle^{\otimes N}\). There is no conjugation error in the final energy formula.

8. **Section 3, locality — minor.** \(a^\dagger(f)a(f)\) moves \(m\) bosons but can alter as many as \(2m\) mode occupations. “Changes at most \(m\) occupation numbers” is false.

9. **Section 3, quantum \(k\)-SAT terminology — significant.** The ordinary homogeneous construction is not a standard Bravyi \(k\)-QSAT instance: its domain is restricted to \(\operatorname{Sym}^N\), and every forbidden tensor is replicated over all \(m\)-subsets. Standard QSAT acts on the full distinguishable-particle tensor product. Call it a permutation-symmetric/bosonic analogue, not “Bravyi’s sense.”

10. **Section 3, radical ideals — minor.** Equality \(I_N=I(V)_N\) in one degree does not mean that \(I\) is “saturated and radical in degree \(N\).” It is only degree-\(N\) equality. Global radicality and saturation require equality in all sufficiently large degrees, with saturation handled separately.

11. **Section 3, multigraded embedding — minor.** This part is correct: in multidegree \((1,\ldots,1)\), all relevant monomials have Fock norm \(1\), so
    \[
    a^\dagger(f)a(f)=|f\rangle\langle f|_S\otimes\mathbf1
    \]
    exactly, with no factorial. State this separately from the ordinary symmetric formula.

12. **Sections 3 and 8.2, QSAT complexity — significant.** Bravyi and Gosset–Nagaj prove promise problems: zero energy versus energy at least \(1/\operatorname{poly}(n)\). Exact \(\mathrm{HF}(1,\ldots,1)>0\) without a NO-gap promise is not thereby in \(\mathrm{QMA}_1\). The corrected statement is the standard promised QSAT theorem. [Bravyi](https://arxiv.org/abs/quant-ph/0602108), [Gosset–Nagaj](https://arxiv.org/abs/1302.0290).

13. **Sections 3 and 8.2, ranks of QSAT clauses — minor.** The reductions use local projectors, not necessarily rank-one projectors. For constant local dimension, spectral decomposition into rank-one constraints is legitimate and preserves both the Hamiltonian and its gap. The report should say this, not claim that the reductions intrinsically output rank-one clauses.

14. **Section 4, monomial exception — fatal.** The claim that monomial ideals admit fixed-\(k\)-body parents with kernel \(I_N\) is false. For \(I=(z_0)\), \(I_N\) is the span of states containing at least one \(0\)-mode boson. Its complement projector is
    \[
    (\mathbf1-|0\rangle\langle0|)^{\otimes N}
    \]
    restricted to the symmetric sector, hence \(N\)-body. A threshold \(\theta(\hat n_0)\) is diagonal and efficiently computable in occupation encoding, but it is not fixed-body local.

15. **Conjecture 4.1 — significant.** The marginal argument is plausible but not written as a proof. What must be shown is that the joint support of the \(k\)-body marginals of \(fR_{N-m}\) is all of \(\operatorname{Sym}^k\); then every positive \(k\)-local term annihilating \(I_N\supset fR_{N-m}\) is zero. This obstruction already applies to monomial \(f\), so the conjecture’s monomial/non-monomial distinction is spurious.

16. **Conjecture 4.1 — minor.** No nontrivial obvious non-monomial counterexample exists under standard first-quantized locality. Trivial cases \(I_N=0\) or \(I_N=R_N\), or allowing \(k\ge N\), are vacuous. A unitary rotation of a monomial ideal does not help because the alleged monomial parent was not fixed-local to begin with.

17. **Section 4, invariant subspaces — significant.** “Ideals are exactly the closed invariant subspaces” is false. Closed shift-invariant subspaces include Hilbert submodules not generated by polynomial ideals; already in one variable Beurling subspaces \(\theta H^2\) need not come from polynomial ideals. Invariance under unbounded \(a_i^\dagger\) is also not automatically equivalent to invariance under the bounded shifts \(J_i\).

18. **Section 5, sparsity and norm — minor.** The row-sparsity estimate and
    \[
    \|H_N\|\le\sum_j\frac{N!}{(N-m_j)!}\|f_j\|_{\rm BW}^2
    \]
    are correct. A sparse-access block encoding is normalized by an efficiently known \(\alpha\), typically \(s\max|H_{xy}|\), not automatically by \(\|H_N\|\). Replace every \(\|H_N\|/\Delta_N\) runtime by \(\alpha/\Delta_N\), absorbing only genuinely polynomial overheads.

19. **Section 5, input model — significant.** Coefficient bit length, requested numerical precision, reversible row enumeration, and sparse-state preparation are omitted. Row computability alone is not an algorithm unless these oracles are constructed with those costs included.

20. **Section 5, exponential \(N\) — fatal.** Exponential \(N\) is cheap only in qubits. The displayed algorithms cost at least \(N^m/\Delta_N\), and trace estimation to precision \(N^{-c}\) costs polynomially in \(N\), not \(\log N\). Thus \(N=d^{\Theta(n)}\) produces exponential runtime even though the register is polynomial-sized.

21. **Sections 5 and 8.1, gap promise — fatal.** An absolute promise \(\Delta_N\ge1/\operatorname{poly}(n)\) does not imply BQP containment. Rescaling generators changes both \(\Delta_N\) and the block-encoding normalization. The required promise is
    \[
    \Delta_N/\alpha\ge1/\operatorname{poly}(n),
    \]
    together with bounded coefficient norms and efficient access.

22. **Section 5.2, DQC1 — significant.** No DQC1 algorithm is actually supplied. Standard DQC1 starts maximally mixed on a power-of-two register; here one needs the maximally mixed state on the valid weak-composition subspace and controlled QSVT with clean ancillas. “DQC1-style trace estimation” is defensible; membership in DQC1 is not established.

23. **Section 5.3 — significant.** “Apply \(P_0\) to a Haar-random symmetric state” is not an efficient preparation prescription. Haar-random states in an exponentially large space cannot generally be prepared efficiently. Starting from a maximally mixed state instead yields a mixed state proportional to \(P_0\), not a Haar-random pure quotient element.

24. **Section 5.4 — significant.** \(Z_j=Z_0X_j\) is correct only after defining
    \[
    X_j=\mu_{z_0}^{-1}\mu_{z_j}
    \]
    on the stabilized quotient, transporting it to \(G_N=I_N^\perp\), and assuming \(I\) is saturated in that range and \(z_0\) is a nonzerodivisor. As written, \(X_j\) and \(Z_j\) act on different spaces.

25. **Section 5.4 — significant.** For a nonradical zero-dimensional scheme, stable \(\mathrm{HF}\) equals scheme length, not \(\#V\). The multiplication matrices can have Jordan blocks. Replace “\(\dim\ker H_N=\#V\)” by “\(\deg(R/I)\), equal to \(\#V\) only for reduced points.”

26. **Section 5.4 — fatal.** Singular-value scans of \(Z_j-\lambda Z_0\) do not constitute an efficient non-Hermitian eigensolver or a uniform root sampler. Complexity depends on eigenvector condition numbers, Jordan structure, pseudospectral behavior, search precision, and state preparation—not merely coordinate separation \(\delta\).

27. **Section 5.5 — fatal.** The family generated only by the displayed \(f_j(t)\) is not generally flat at \(t=0\). Its special fibre is
    \[
    (\operatorname{in}_w f_1,\ldots,\operatorname{in}_w f_d),
    \]
    which may be strictly smaller than \(\operatorname{in}_w(I)\). Eisenbud’s flat ideal is generated by the homogenizations of all \(g\in I\), or finitely by a suitable Gröbner basis, not an arbitrary generating list. [Eisenbud, Thm. 15.17](https://www.math.ens.psl.eu/~benoist/refs/Eisenbud.pdf).

28. **Section 5.5 — significant.** For every \(t\ne0\), constant Hilbert function is indeed trivial from diagonal coordinate change. Constancy at \(t=0\) is precisely what fails without a Gröbner basis or \(t\)-saturation.

29. **Section 5.5 — significant.** \(H_N(0)\) is diagonal only if every limiting generator is a single monomial. A weight initial form may contain several tied terms even when the initial ideal is monomial after refinement. Its ground monomials are standard monomials of \((\operatorname{in}_wf_j)\), not necessarily of \(\operatorname{in}_w(I)\).

30. **Sections 5.5 and 8.4 — significant.** The endpoint gap is not automatically an integer or at least \(1\):
    \[
    \Delta_N(0)\ge \min_j |c_j|^2\alpha^{(j)}!
    \]
    only after a correct monomial presentation, and coefficients \(c_j\) can be arbitrarily small. Rescaling a generator leaves the ideal unchanged but changes the Hamiltonian gap.

31. **Section 5.5 — significant.** Flatness plus a gap does not prepare “a basis” of an exponentially dimensional ground space. Adiabatic evolution transports one prepared state at a time and introduces non-Abelian Berry holonomy inside a degenerate ground space. The runtime is not generally just \(\int\|\dot H\|/\Delta^2\).

32. **Section 5.6 — minor.** Correct algebraic statement: \(\mathrm{HF}_{R/I_t}(N)\) is upper semicontinuous, so an exceptional fibre can have larger value than nearby generic fibres. It does not “jump only up” along an oriented path: for \(I_t=(tx,y)\), the value is larger at \(t=0\) and jumps down immediately when leaving \(0\).

33. **Section 5.6 — significant.** Avoiding Macaulay-rank drops at one degree is not equivalent to avoiding the homotopy discriminant. Roots can collide and become nonreduced while the Hilbert function and scheme length remain constant. The comparison with Beltrán–Pardo/Lairez is therefore unjustified.

34. **Section 6, Boolean ideal — significant.** The pure Boolean ideal
    \[
    J=(z_i^2-z_iz_0)
    \]
    is radical and saturated, with \(\operatorname{reg}(R/J)=n\). After adjoining homogenized cubic clause indicators, the affine dehomogenization remains radical, but the displayed homogeneous ideal is generally neither radical nor saturated; it has irrelevant-ideal torsion. Its saturation is the intersection of the satisfying-point ideals.

35. **Section 6, Boolean Hilbert function — minor.** The eventual identity is valid, but justify it directly. Since \((R/J)_N\) is the full algebra of functions on \(\{0,1\}^n\) for \(N\ge n\), cubic clause multiples generate all functions supported on unsatisfying assignments once \(N\ge n+3\). Hence
    \[
    \mathrm{HF}_{R/K}(N)=\#\mathrm{SAT}(\phi)\qquad(N\ge n+3).
    \]
    Invoking an unspecified “Lazard bound” obscures the torsion issue.

36. **Section 6, complexity classes — minor.** “Exact \(\mathrm{HF}\in\mathrm{BQP}\)” is ill-typed: BQP is a decision class. An exact-output quantum algorithm would place the corresponding function in FBQP and imply \(\#P\subseteq\mathrm{FBQP}\).

37. **Section 6, monomial Hilbert hardness — minor.** Bayer–Stillman is not the reference for a \(\#P\)-hardness theorem; their paper gives algorithms and an NP-hardness statement in a suitable model. The edge-ideal/independence-polynomial reduction or Dickenstein–Tobis supports the \(\#P\) claim. [Bayer–Stillman](https://www.sciencedirect.com/science/article/pii/074771719290024X), [Dickenstein–Tobis](https://arxiv.org/abs/1003.3508).

38. **Section 6, zero kernel — significant.** The direction is reversed:
    \[
    \ker H_N\ne0\iff\phi\text{ is satisfiable}
    \]
    is NP-hard, while \(\ker H_N=0\) is coNP-hard. Calling the zero-kernel language NP-hard is unjustified unless NP \(=\) coNP or a nonstandard reduction is intended.

39. **Section 6, Koiran — significant.** Koiran puts the common-root/nonemptiness problem in AM under GRH. Emptiness is its complement and lies in coAM under GRH. SAT reduces to nonemptiness; UNSAT reduces to emptiness. [Koiran](https://archive.dimacs.rutgers.edu/TechnicalReports/abstracts/1996/96-27.html).

40. **Section 6, overlap lower bound — fatal.** There is no universal lower bound \(\sqrt{\dim R_N/\mathrm{HF}(N)}\) for “any task.” That factor applies to black-box projection from a state with that overlap. Structured ideals may have easily preparable ground states even when the dimension ratio is tiny.

41. **Section 6, dequantization — minor.** Bounded variety dimension does not imply \(\mathrm{rank}(P_0)=\operatorname{poly}(N)\) uniformly in the input: the degree may itself be exponential. Low-rank classical algorithms also require sample/query access and conditioning, not rank alone.

42. **Section 7, generator dependence — significant.** The example is written backwards. Replacing \(f_2\) by \(f_2+\epsilon f_1\) tends to the original tuple as \(\epsilon\to0\) and does not generally force \(\Delta=O(\epsilon^2)\). The nearly redundant tuple is
    \[
    (f_1,\ f_1+\epsilon f_2),
    \]
    which generates the same ideal for \(\epsilon\ne0\) and becomes singular as \(\epsilon\to0\).

43. **Section 7.1 — minor.** The principal Bombieri lower bound is correct, but “attained for monomials” is false without qualification. In one variable, for \(f=z^m\),
    \[
    \Delta_N=\frac{N!}{(N-m)!}>m!=\|f\|_F^2
    \]
    when \(N>m\). Equality requires enough degree to be placed in variables absent from the monomial, or \(N=m\).

44. **Sections 6–7 — significant.** “The Boolean ideal gap is exactly \(2\)” is not established. The report only reports computations for \(n\le6\) at \(N=n+1\). This cannot be used as a theorem for arbitrary \(n,N\), still less after clause generators are added.

45. **Conjecture 8.1 — fatal.** The hardness reduction does not match the decision promise. The proposed overlap is generally a nonzero number on both BQP cases; an oracle deciding “exactly \(f\in I_N\)” versus “distance at least \(\epsilon\)” does not estimate \(\operatorname{Re}\langle y|U|0\rangle\). The reduction would establish hardness for additive ground-overlap estimation, not for exact ideal membership.

46. **Conjecture 8.1 — minor.** The overlap identity assumes the test state is normalized:
    \[
    |\phi\rangle=\frac{|0,0\rangle+|y,T\rangle}{\sqrt2}.
    \]
    For the unnormalized sum written in the report, the expectation is twice the displayed value.

47. **Conjecture 8.1 — significant.** The Feynman–Kitaev block has gap \(\Omega(T^{-2})\), but the conjecture promises a gap for the entire ordinary degree-\(N\) Hamiltonian. The other multidegree blocks can contain smaller positive eigenvalues. No lower bound for the global \(\Delta_N\) is proved.

48. **Conjecture 8.2 — significant.** The multigraded statement is already the QSAT theorem, after adding the inverse-polynomial NO-gap promise; it is not a new conjecture. The monomial version is classical \(k\)-SAT and is NP-complete for \(k\ge3\).

49. **Conjecture 8.2, ordinary grading — fatal.** The suggested hardness embedding fails immediately. If all generators are multilinear across distinct site blocks, putting all \(N\) bosons in one site block makes every \(k\ge2\) annihilation constraint vanish. Thus the ordinary total-degree sector always has spurious zero modes in this construction.

50. **Conjecture 8.3(a) — significant.** This is a meaningful open uniform closed-range estimate, not supported by the numerical survey. Its “polynomial-time in \(N\)” consequence is algorithmically weak because \(N\) is encoded in \(\log N\); polynomial in \(N\) is exponential in the input length.

51. **Conjecture 8.3(b) — fatal.** It is false. Let \(P\) be the lattice pyramid over the unit square. Its normal toric ideal is
    \[
    I=(x_{00}x_{11}-x_{10}x_{01})
    \]
    in a ring with an additional apex variable \(y\) absent from the relation. Taking \(h=y^{N-2}\) attains the principal lower bound, so
    \[
    \Delta_N=\|x_{00}x_{11}-x_{10}x_{01}\|_F^2=2
    \]
    for every \(N\ge2\), not \(\Theta(N)\).

52. **Conjecture 8.3(c) — significant.** It is ill-posed until “Kostlan-random” is normalized and the probability quantifiers over all \(N\) are specified. A sensible version is
    \[
    \Pr\!\left[\inf_{N\ge m}\Delta_N\ge c(m)\right]\to1
    \]
    for unit Bombieri-norm forms. No cited theorem or evidence at \(N=3,4\) supports the uniform-in-\(N\) claim.

53. **Conjecture 8.3(d) — minor.** This is essentially already a theorem, not a conjecture. Area-weighted Motzkin chains are 2-local, frustration-free, and have gap at most \(8ns\,t^{-n^2/3}\); the multigraded embedding transfers that eigenvalue, and padding by identities handles larger fixed \(m\). [Levine–Movassagh](https://arxiv.org/abs/1611.03147).

54. **Conjecture 8.3(e) — significant.** “Syzygy-module data” is undefined and can encode the entire problem, making the proposed bound vacuous. The claim that the infimum is attained by \(N\le\operatorname{reg}(I)+m\) has no argument and is probably false; distinguish a minimum from an asymptotic infimum.

55. **Conjecture 8.3(d), requested monotonicity check — minor.** The supplied file contains no monotonicity claim in 8.3(d). The closest claims are the numerical \(t\)-monotonicity in 5.5/8.4(a) and the explicitly abandoned \(N\)-monotonicity. Neither follows from flatness.

56. **Conjecture 8.4(a) — fatal.** False as stated because the path in 5.5 is not generally flat, the endpoint gap depends on generator coefficients and presentation, and flatness imposes no spectral monotonicity. Even within a fixed ideal, ill-conditioned \(t\)-dependent row operations can make the gap arbitrarily small at an interior point.

57. **Conjecture 8.4(b) — significant.** “Cone width,” allowed paths, normalization of generators, and the metric on the Gröbner fan are undefined. Since \(\Delta\) changes under harmless rescaling and row operations, this is not an invariant of \(I\) without fixing a normalized presentation.

58. **Conjecture 8.5 — significant.** The exact characterization is already a theorem:
    \[
    \operatorname{span}\{|p\rangle^{\otimes N}: \bar p\in V(I)\}
    =I(V)_N^\perp.
    \]
    Hence equality with \(\ker H_N\) is equivalent to \(I_N=I(V)_N\). It is not a conjecture.

59. **Conjecture 8.5 — significant.** The “entangled defect” is merely
    \[
    \dim I(V)_N-\dim I_N.
    \]
    It equals a finite scheme-theoretic length only for zero-dimensional schemes in the stable range. In positive dimension it grows polynomially, and for nonsaturated \(I\) it also counts irrelevant torsion.

60. **Conjecture 8.5 — significant.** A root-sampling oracle does not automatically provide the projector onto the span of coherent root states. Those states are nonorthogonal and can have an exponentially ill-conditioned Gram matrix. The claimed BQP radicality test therefore does not follow.

61. **Conjecture 8.6 — fatal.** The Boolean/CNF gap is not known to be \(1/\operatorname{poly}(n)\). Adding PSD clause terms can split the \(2^n\)-dimensional Boolean ground space by exponentially small amounts; monotonicity of the full ordered spectrum gives no lower bound on the new first positive eigenvalue.

62. **Conjecture 8.6 — fatal.** The proposed overlap does not “match Grover.” At \(N\simeq n\),
    \[
    \dim R_N=\binom{2n}{n}\asymp\frac{4^n}{\sqrt n}.
    \]
    For one satisfying assignment the report’s factor is \(\Theta(2^n)\), whereas Grover costs \(\Theta(2^{n/2})\). For the pure Boolean ideal \(D=2^n\), the report still predicts \(2^{n/2}\) overhead although sampling a Boolean string is trivial. One would need an efficiently prepared state inside the Boolean quotient, giving overlap \(D/2^n\), not \(D/\dim R_N\).

63. **Conjecture 8.6 — significant.** Coordinate separation \(\delta\) does not control a nonnormal multiplication tuple. Root sampling also depends on eigenvector/Jordan conditioning and the Gram matrix of evaluation vectors. Uniformity over distinct roots is not automatic.

64. **Conjecture 8.6 — significant.** The report’s assertion that the Ding–Gheorghiu–Gilyén–Hallgren–Li condition number and this overlap factor are “the same phenomenon” is unsupported. They are condition numbers of different Macaulay systems, not an established equality or reduction. [Ding et al.](https://quantum-journal.org/papers/q-2023-07-26-1069/).

65. **Conjecture 8.7 — significant.** Hilbert-polynomial asymptotics are a theorem, but the algorithmic conclusion is false without uniform bounds on regularity and lower-order coefficients. Merely taking \(N\ge\operatorname{poly}(n)\) need not place the input in the stable range or separate different \((c,\deg V)\).

66. **Conjecture 8.7 — minor.** To recover the exact integer degree \(D\), the additive error must be less than roughly
    \[
    \frac12\,\frac{n!}{(n-c)!}N^{-c},
    \]
    after controlling lower-order terms. “\(N^{-c}/\operatorname{poly}(n)\)” is too vague to imply this.

67. **Conjecture 8.8 — fatal.** “Amplitude encoding needs characteristic zero because it needs a positive-definite inner product” is false. Quantum amplitudes are complex regardless of the data field. The real obstruction is that \(\mathbb F_q\) has no field embedding into \(\mathbb C\), so complex linear algebra does not preserve rank or multiplication over \(\mathbb F_q\).

68. **Conjecture 8.8 — significant.** In positive characteristic, ordinary differentiation does not realize apolarity correctly—\(\partial(x^p)=0\). One must use divided powers/contraction. The Fourier orthogonal complement under the coefficient dot product is not automatically the Macaulay inverse system unless the divided-power dual basis is used.

69. **Conjecture 8.8 — minor.** The hidden-subgroup formulation gives no advantage because \(\Phi\) is an explicitly known linear map; finding its kernel is ordinary finite-field linear algebra. Conversely, saying the entire problem is classically easy ignores that the Macaulay dimension may be exponential in the succinct input.

70. **Conjecture 8.9 — significant.** Arveson’s curvature theorem captures the leading multiplicity/degree under its hypotheses, not the entire Hilbert polynomial. This portion is known theory, not a conjecture. [Arveson](https://arxiv.org/abs/math/9808100).

71. **Conjecture 8.9 — significant.** The Schatten threshold uses the complex dimension of the affine cone, which is projective dimension plus one. The report appears to use projective \(\dim V\), producing an off-by-one threshold.

72. **Conjecture 8.9 — significant.** The compressed coordinate multipliers \(Z_i\) commute exactly. Essential normality concerns \([Z_i,Z_j^\dagger]\), so the physical interpretation should be “asymptotically normal,” not “become commuting.”

73. **Conjecture 8.9 — significant.** Essential normality for principal ideals and varieties smooth away from the origin is already known in appropriate formulations; the latter is due to Engliš–Eschmeier. It gives no finite-\(N\) eigenvalue-separation or nonnormal-conditioning bound. [Engliš–Eschmeier](https://arxiv.org/abs/1312.6777).

74. **Conjecture 8.9 — fatal.** Ordinary quantum phase estimation does not apply to nonnormal \(Z_j\). Essential normality modulo compact operators does not make a finite truncation unitarily diagonalizable or well-conditioned near singularities.

75. **Section 9 — significant.** Correction 6 repeats the false monomial exception from Section 4. Replace it with: monomial ideals make \(P_{I_N}\) diagonal in occupation number, but exact threshold projectors are generally \(N\)-body, not fixed-local.

76. **Prior art — significant.** The report correctly mentions Chen–Gao and Ding et al., but it should not present “QSVT on Macaulay matrices” as conceptually new without separating the new observable from existing quantum linear-system work. It also omits the recent formal bosonic-complexity framework, which is relevant but different from this fixed-particle symmetric-sector construction. [Bosonic Quantum Computational Complexity](https://arxiv.org/abs/2410.04274).

77. **Overall — fatal.** The algebraic kernel identity and the Section 3 factorial/conjugation formulas are basically sound. The claimed quantum-algorithmic program is not: its main hardness reduction does not match its promise problem, its Gröbner path is not the flat family claimed, its root-sampling/Grover accounting is wrong by an exponential factor, and several “conjectures” are either known theorems, false, or undefined.