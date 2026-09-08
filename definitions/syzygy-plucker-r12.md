# Syzygy Pluecker basis sampling: canonical input and output

2026-09-07, under PRD D25. The polynomial space uses the existing Fock metric
and C3 conjugated annihilation. The bath dimension q counts labelled generators,
independently of the number of polynomial variables. This is a based-generator
problem: the ordered tuple is part of the object, not just its generated ideal.

## D-SYZYGY-PAIR-TUPLE

Let q>=2 and let C be an unknown complex `2 x q` matrix with `C C†=1_2`.
In `R=C[z0,z1]`, use the Fock-orthonormal quadratic forms

    g0=z0²/sqrt(2),  g1=z1²/sqrt(2),
    f_a=C_(0,a) g0+C_(1,a) g1,  1<=a<=q.

The input object is the based tuple `(f_1,...,f_q)`. Its generated ideal is
`(z0²,z1²)`, but its degree-two constant-coefficient syzygy space

    K={v in C^q : sum_a v_a f_a=0}=ker C

depends on the supplied tuple. Set `U=range(C†)=K^perp` and `P_U=C†C`.
Neither C nor a basis of U or K is supplied as a classical list.

## D-SYZYGY-PAIR-SOURCE

The only data access is independent copies of `rho_C=P_U/2` on a q-dimensional
register, encoded in w=ceil(log2 q) qubits. Copies do not include a preparation
inverse, purification, amplitude queries, coherent emitter control, a classical
description of C, or a tunable choice of incident polynomial state.

A geometric realization fixes the maximally mixed state on `R_2`, whose
dimension is three, and applies the Fock emitter of D-THERMAL-SYZYGY-EMITTER
at N=d=2 with success normalization alpha=1. Its outcome label is the bath
register. Only the accepted bath state is delivered. The success flag has
probability 2/3 independent of C, and all other registers are inaccessible.

One source copy has a charged preparation/delivery cost C_source(q). Any
one-time device construction cost B_source(q) is separate. The theorem compares
copy consumption, plus the stated processing gates; it does not assume a free
classical-to-quantum loading of a coefficient table. A raw fixed-emitter-call
variant may expose only the success/failure flag and the successful bath copy.

## D-SYZYGY-PAIR-OUTPUT

Always output a sorted pair J={a,b} of distinct generator labels. Its target law is

    p_C(J)=|det C[:,J]|²=det(P_U[J,J]).

The required total-variation error is at most 1/16 for every promised C. A pair
of positive target weight is a minimal generating pair of the same ideal.
The weighted law favors large squared Fock area; the theorem concerns this
particular volume-sampling law, not every unweighted generator-selection task.

Equivalently these are squared complementary Pluecker coordinates of K:
an orthonormal basis matrix Z for K has
`|det Z[J^c,:]|²=p_C(J)`. For q=2 the complementary minor is the empty
determinant one. The large matrix Z is never an output requirement.

## D-SYZYGY-PAIR-CLASSICAL-COMPARATOR

The comparator receives exactly D-SYZYGY-PAIR-SOURCE. It may perform an arbitrary
global POVM on each complete original q-dimensional copy, choose later POVMs
adaptively, and retain unlimited classical computation and memory. It cannot
retain quantum memory between original copies. Its total copy cap T includes
every copy consumed, including failed or discarded measurements. It must always
output a pair with the same uniform TV guarantee. This is exactly the scope
of D-SUPPORT-CLASSICAL-COPY-MODEL; a coefficient-list algorithm is a different
input model.

## D-SYZYGY-PAIR-SWAP-PROTOCOL

For at most ten independent trials, take two fresh source copies, apply a
standard swap test and accept its antisymmetric outcome. On the first accepted
trial, measure both data registers in their generator-label basis and sort the
two distinct labels. If all ten trials fail, output the fixed pair {1,2}.
For one trial the data Kraus operators are `(1+S)/2` and `(1-S)/2`, where S
swaps the two entire source registers. The ancilla has one Hadamard before
and one after a controlled swap; measuring its one outcome selects the latter.
No phase estimation, quantum Fourier transform, amplitude amplification,
Grover search, DQI, QSVT or knowledge of C is used by this protocol.

## D-SYZYGY-GENERATOR-OUTPUT

For the same based tuple and source, always output two distinct labels J whose
forms generate the ideal of the entire tuple, with probability at least 2/3
for EVERY promised C. Equivalently, `det C[:,J]!=0`. No particular sampling
distribution, conditioning bound, coefficient readout or syzygy basis is requested.
Labels refer to the original available generators; returning the known abstract
forms g0,g1 is not an answer. This is the principal useful selection task.

## D-SYZYGY-GENERATOR-COMPARATOR

Use exactly the access, arbitrary adaptive single-original-copy POVMs,
unlimited classical memory and fixed total copy cap of
D-SYZYGY-PAIR-CLASSICAL-COMPARATOR. Replace its TV requirement by the
uniform success requirement of D-SYZYGY-GENERATOR-OUTPUT. The lower-bound
ensemble chooses a hidden balanced partition S of the q=2d labels, then
independent Haar unit vectors on S and its complement. S is fixed during
the whole run and is NOT supplied as side information. Neither are the vectors.

## D-SYZYGY-GENERATOR-PROTOCOL

Run the same two-copy swap-test instrument for at most FOUR independent trials.
On the first antisymmetric result, measure/sort the generator labels. If all
four fail, output {1,2}. Invalid or repeated labels under a noisy implementation
are mapped to that fixed valid-format pair. The noiseless protocol uses at
most eight copies, and all accepted pairs are generating pairs.
