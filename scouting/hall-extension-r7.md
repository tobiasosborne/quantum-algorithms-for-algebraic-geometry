# Hall extensions and a retained-order obstruction circuit

2026-09-05. Bounded independent construction for `qaag-y71`.
Canonical inputs are D-HALL-A2-EXTENSIONS, D-HALL-FLAG-FORGETTING and
D-HALL-YONEDA-QUERY in `definitions/hall-extension.md`. Claim status lives
only in `claims/CLAIMS.md`, C-355--C-356; independent review is in
`verdicts/hall-extension-r7.md`. Local orthonormal field-register bases,
field-order q and identity notation depart from C1, C2 and C6 as declared
in the canonical file. No historical novelty is asserted.

Two concrete operations were derived before targeted source verification.
Uniform elementary Hall extensions have a direct classical sampler; coherent
flag forgetting has a nontrivial normalization. A different operation retains
all auxiliary registers and converts extension order into the obstruction YX.
Its geometric bit admits an equally efficient classical random-vector probe.
The calculations below concern these operations, not all quantum algorithms
on quiver varieties or all possible Hall correspondences.

## 1. First diagnostic: framed extensions and their actual distribution

1.1. Use the quiver 1->2 over F_q. The executable quantum family takes
q=2^s with an explicitly supplied irreducible polynomial defining the field;
the counting formulas hold for every finite field. Each field entry has s bits.
Supply matrices N_a of size n_2-by-n_1 and M_a of size m_2-by-m_1, with fixed
vertex bases. Framed extensions with the standard subobject and quotient are

    E_X,a = [[N_a, X], [0, M_a]],
    X in C^1=Mat_(n_2 by m_1)(F_q).                          (1)

Changing a splitting by f_i:M_i->N_i sends

    X -> X+N_a f_1-f_2 M_a = X+d(f),
    C^0=Hom(M_1,N_1) direct-sum Hom(M_2,N_2).

For this hereditary one-arrow quiver, Ext^1(M,N)=C^1/im(d).
Every quotient class has q^(rank d) representatives. Thus a uniformly random
X gives a uniformly random extension class, although the middle-object
isomorphism classes need not be uniformly distributed.

1.2. The literal quantum state is q^(-n_2*m_1/2)sum_X |E_X,a> with the
fixed standard subobject understood. Preparing the random field bits uses
n_2*m_1*s Hadamards, and copying the fixed blocks is ordinary data loading.
X is recoverable from the off-diagonal block, so this step is injective and
requires no coherent many-to-one erasure. Measurement has exactly the same
law as choosing the entries of X independently and uniformly classically.
Computing a quotient basis for Ext^1 is Gaussian elimination on d, charged
to either implementation if that quotient output is requested.

1.3. A scalable explicit output is the isomorphism class of E_X when
N_a=M_a=0. It is determined by r=rank X, with X of size b-by-c. Its probability is

    Prob(r)=q^(-bc) product_(i=0)^(r-1)
                    [(q^b-q^i)(q^c-q^i)/(q^r-q^i)].         (2)

The empty product gives the single zero matrix at r=0. Factor a rank-r matrix
as a full-column-rank b-by-r matrix times a full-row-rank r-by-c matrix and
divide by |GL_r(F_q)| to obtain the count. Sampling X and computing its rank
takes O(bc min(b,c)) field operations by ordinary elimination. No exponential
orbit list or general module-isomorphism oracle is a relevant baseline here.

## 2. Flags, automorphisms, and the norm of pushforward

2.1. Define F_(MN)^E as the number of submodules W of E isomorphic to N
with E/W isomorphic to M. Write a_A=|Aut(A)| and h=|Hom(M,N)|. The exact identity is

    |Ext^1(M,N)_E| = F_(MN)^E * a_N*a_M*h/a_E.                (3)

Proof: each W yields a_N*a_M choices of endpoint identifications in a
short exact sequence with fixed middle E. Aut(E) acts on those sequences;
its stabilizer is {1+i f p : f in Hom(M,N)}, of size h. Orbit-stabilizer gives
(3). The zero map is included in Hom, so h is a field cardinality, not a dimension.
Uniform extension classes, uniform flags, and Hall structure constants are
different measures; removing these factors changes the proposed operation.

2.2. Let f:mathcal X->mathcal Y forget a flag from a finite framed
correspondence, with nonempty fibre sizes F_y. For

    T|x>=|f(x)>,   T T^dagger=sum_y F_y |y><y|,
    ||T||=sqrt(F_max),   F_max=max_y F_y.                    (4)

The largest uniform Kraus scaling is T/sqrt(F_max). On the normalized
uniform fibre vector omega_y=F_y^(-1/2)sum_(x:f(x)=y)|x>, its success probability
is F_y/F_max. On a general source psi it is ||T psi||^2/F_max.
Retaining the flag instead defines the injective map |x>->|f(x),x> and
creates no interference between different x values.

2.3. The different map C|x>=F_(f(x))^(-1/2)|f(x)> has norm one and sends
omega_y to |y>. It is a coisometry, with success effect equal to the projector
onto uniform fibre vectors. Its action on arbitrary inputs is not the original
Hall counting pushforward. Implementing it needs coherent fibre coordinates
and a transform isolating each uniform fibre vector. Neither cardinalities
nor that transform follow merely from writing the Hall multiplication formula.
If y is an unframed isomorphism class, computing its canonical label is another
charged operation; the map is not furnished by moduli-space terminology.

2.4. A two-by-two example shows the factors materially matter. Take N=M to
have dimension (1,1) and zero arrow. For a zero middle arrow, F=(q+1)^2;
for a rank-one middle arrow, F=1. The first counts arbitrary lines at the two
vertices; the second forces the kernel line at vertex 1 and image line at vertex 2.
Here h=q^2, a_N=a_M=(q-1)^2, and

    a_(rank 0)=|GL_2(F_q)|^2,
    a_(rank 1)=q^2*(q-1)^3.

Equation (3) gives respectively 1 and q-1 extension classes, summing to q.
On these flag fibres the raw forgetting contraction needs normalization q+1;
the rank-one uniform fibre succeeds with probability 1/(q+1)^2.
This is not the fibre count for forgetting X directly to its rank, which
is instead the rank-matrix count in (2).

2.5. Interfering two normalized uniform affine extension spaces does not
rescue the diagnostic. For affine spaces L,L' in one framed matrix register,

    <L|L'>=|L intersect L'|/sqrt(|L||L'|),                    (5)

zero for an empty intersection, and otherwise a power of q determined by
three affine dimensions. Linear algebra computes it. Computational sampling
from their plus/minus superposition reduces to the three regions L\L',
L'\L, and their intersection, with constant amplitudes in each region.
This refers to a branch of positive norm; the identically zero minus branch
when L=L' is never declared a preparable normalized state.
Their sizes and affine intersections are explicit. Nonempty proper affine
differences have rejection-sampling success at least 1-1/q.
Thus this elementary order interference has a matched classical sampler too.

## 3. Different operation: a nonlinear extension obstruction from retained order

3.1. Change to the bound quiver

    1 --e--> 2 --f--> 3,       relation f e=0.

Its representation variety at dimension vector (a,b,c) is the variety of complexes

    mathcal R_(a,b,c)={(X,Y): X in Mat_(b by a), Y in Mat_(c by b), YX=0}.

Here the dimension symbols a,b,c are integers. Input is explicit matrices
X,Y, comprising s(ab+bc) bits.
The classical output is the bit deciding membership in this affine variety.
Equivalently, it decides whether the two prescribed adjacent extension blocks
can occur in one three-step filtered representation of this bound quiver.

3.2. The adjacent Ext^1 coordinates between the corresponding vertex-simple
blocks are X and Y. Their degree-two extension obstruction is the composition
YX. This can also be read directly, without a homological oracle, by imposing
the defining path relation on the two arrow matrices. The condition YX=0
is invariant under the graded basis changes (g_1,g_2,g_3), since the product
changes to g_3*(YX)*g_1^(-1). No canonical middle-object label is required.

3.3. On an auxiliary register |u,v,w>, with u in F_q^a, v in F_q^b and
w in F_q^c, define two reversible shears

    S_X|u,v,w>=|u,v+Xu,w>,
    T_Y|u,v,w>=|u,v,w+Yv>.

These act on an auxiliary three-block vector. They are not asserted to be
vertex-preserving base changes identifying two quiver representations.
Their order commutator is the exact unitary

    C_(X,Y)=T_Y S_X T_Y^(-1) S_X^(-1),
    C_(X,Y)|u,v,w>=|u,v,w+YXu>.                              (6)

Proof: the four steps change v to v-Xu, w to w-Yv+YXu, restore v,
and finally restore the Yv term in w. All auxiliary coordinates and all
input matrices are retained. There is no flag erasure or postselection.

3.4. Prepare u uniformly using a*s Hadamards and v=w=0. The result is

    q^(-a/2)sum_u |u,0,YXu>.

If r=rank(YX), measuring whether w is nonzero detects nonmembership with

    s_detect=1-q^(-r).                                      (7)

It never rejects a representation satisfying the relation. For r>=1 it
rejects with probability at least 1-1/q. Taking
ell=ceil(log(1/delta)/log q) independent trials bounds error by delta.

3.5. With explicit field coefficients, multiplication by each constant is
an s-by-s binary linear transformation. The shear uses O((ab+bc)s^2)
CNOT gates, and the four-step commutator has the same asymptotic cost.
Live data need (a+b+c)s qubits, besides the classical input/gate description.
Uniform state preparation and field arithmetic are exact in this model;
there is no analytic amplitude precision or unknown state-preparation inverse.
At nonzero implementation error, O(delta/ell) trace error per trial suffices.
Repeated access and compiling the coefficient-controlled CNOT network are
charged, rather than counted as a free unitary oracle.

## 4. Why the retained-order operation still fails the matched audit

4.1. A classical algorithm chooses the same uniform u, computes v=Xu and
w=Yv, and checks w. Its success probability is exactly (7), its work is two
matrix-vector products, and its working storage is O((a+b+c)s) bits beyond
the same explicit input. It does not form the full matrix YX or enumerate
representations. This is the matrix-product random-vector test, so the
displayed quantum circuit has no time or space advantage on the stated bit.
This comparison is not a lower bound against other quantum algorithms.

4.2. Literal interference between the two orders has no hidden stronger
signal. On the uniform u source with v=w=0, the branch states for S_X T_Y
and T_Y S_X are q^(-a/2)sum_u|u,Xu,0> and q^(-a/2)sum_u|u,Xu,YXu>.
Their overlap is q^(-r). The destructive-port probability is

    (1-q^(-r))/2,                                          (8)

half the direct random-probe detection rate. Common registers are retained,
so this statement does not rely on illicitly identifying different flags.

4.3. Using a Fourier-character w register yields the phase
(-1)^(Tr_(F_q/F_2)(eta^T YXu)). For fixed classical X,Y this is a binary
quadratic character in u,eta. The uncontrolled shear and phase-kickback
versions are stabilizer operations, with matrices fixed by finite linear
algebra. A coherently controlled order can require extra non-Clifford gates;
its displayed scalar overlap is nevertheless exactly (8). The diagnosis is the linear shear
and quadratic-character structure, not just membership in a universal gate set.

4.4. A higher polynomial relation does not automatically escape this attack.
For a four-vertex chain with relation g f e=0, fixed arrow matrices X,Y,Z
have obstruction ZYX. Nested adjacent shears can add ZYXu to a final retained
register, but a classical probe applies X,Y,Z successively and detects a
nonzero product with probability 1-q^(-rank(ZYX)). The relation is cubic
in input coefficients while remaining linear in the probe register.
This is not called an ordinary triple Yoneda product: a length-three
defining relation can represent a higher extension operation of another degree.

4.5. More generally, if a proposed retained loop only evaluates a supplied
matrix polynomial R on a probe u, deciding R=0 admits the same test whenever
Ru can be evaluated by that circuit's matrix-vector recurrence. This scoped
observation does not classify nonlinear quiver correspondences. Allowing
X,Y themselves to be arbitrary quantum superpositions changes the input
problem and may create off-diagonal phase information, but the present
geometric membership bit does not specify a use for that coherence.

## 5. Verification, hardware, and exact remaining work

5.1. After deriving the operations, the primary PDF of Xiao--Xu,
[arXiv:1208.2312](https://arxiv.org/abs/1208.2312), Example 2.3, was fetched
and checked for the Riedtmann--Peng automorphism formula. Index conventions
there differ, so equation (3) is also independently proved above.
The original proceedings paper by Freivalds, *Fast Probabilistic Algorithms*,
MFCS 1979, pp. 57--69, DOI 10.1007/3-540-09526-8_5, was inspected in this
[primary proceedings scan](https://raganwald.com/assets/fractran/Mathematical-Foundations-of-Computer-Science-1979-Proceedings-8th-Symposium-Olomouc-Czechoslovakia-September-3-7-1979.pdf).
Its random-vector matrix-product verification is the matched mechanism here.

5.2. One inline probe, timeout 30 seconds and one BLAS thread, passed
720 checks of small Hall flag counts, automorphism factors, the retained
commutator and its exact detection probability. Six omitted-Hom-factor
variants were rejected. Tests used small prime fields; the formulas and
binary-field circuit bounds above follow algebraically. These supporting
probes do not establish a speedup or replace independent proof review.

5.3. At q=2 and a=b=c=1, each known nonzero coefficient gives an ordinary
CNOT shear. A small MBQC circuit can compare the two orders and verify the
destructive-port rate in (8). Input injection, cluster preparation and
gate/detection noise are experiment costs. This is an elementary check of
the extension obstruction, not a novel quantum or heuristic mechanism.

5.4. The first candidate lacks a cheap, useful coherent pushforward with
the actual Hall weighting; replacing T by C changes it. Its measured
elementary extension law already has a same-input classical sampler.
The second candidate does implement a nonlinear geometric obstruction
without erasure, but its proposed speedup lemma fails because the same
matrix-vector recurrence is a classical test with the same success rate.
No unresolved estimate inside these displayed algorithms supplies a speedup.

5.5. A different Hall proposal would need a genuinely nonlinear framed
correspondence whose useful interference survives retaining or explicitly
transforming its fibre coordinates, and a geometric output that is not
removed by the affine-space or random-matrix-probe attacks above. Merely
increasing relation degree is insufficient. Hall-to-Hecke/Baxterization and
standard flag recoupling were already tested in
`scouting/original-enumerative-round3.md` and are not reopened here.
No general module-isomorphism hardness or universal impossibility claim
is made. This bounded diagnostic is complete; the wider search remains open.
