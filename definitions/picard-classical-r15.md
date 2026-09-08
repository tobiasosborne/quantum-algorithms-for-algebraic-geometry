# Classical Picard-rank and period-relation problems

2026-09-08. These are classical bit-input and topological-period models, not
the campaign's Fock-state input. The period-coordinate metric and height below
are explicitly different from C1. The lattice dimension is independent of C2.
No integral marking, period oracle, divisor basis, or Frobenius matrix is free.

## D-QUARTIC-EXTRA-PICARD-CLASS

Input is the 35 binary integer coefficients of a primitive homogeneous quartic
F in Q[x0,x1,x2,x3], with the promise that X=V(F) in P^3 is smooth.
Let L be total coefficient bit length and h the hyperplane class. The exact
classical output is one iff the geometric Picard rank
`rank NS(X_(Qbar))` is greater than one. The rank is geometric, not the rank
of classes fixed by the ground-field Galois group. No numerical tolerance is
part of this exact problem. The output is one bit, not an explicit Picard basis.

## D-BOUNDED-SEPARATED-PERIOD-RELATION

Fix an integer dimension m; the quartic application uses m=21 after quotienting
the integral cohomology lattice by the primitive hyperplane class. A chosen
integral marking and a fixed algebraic normalization of the holomorphic form
specify a period vector pi in C^m. Computing that data from F is separately
charged in any application to D-QUARTIC-EXTRA-PICARD-CLASS.

Finite input consists of an integer H>=1 in binary, a positive rational g,
and rational vectors a,b in Q^m. The promises are:

1. Each real and imaginary coordinate of pi differs from a,b, respectively,
   by at most `g/(4mH)`.
2. For every nonzero z in Z^m with `||z||_infty<=H`, either `z.pi=0` or
   `max(|Re(z.pi)|,|Im(z.pi)|)>=g`.

Output one iff there is a nonzero such z with z.pi=0. Rational data are charged
by their actual binary lengths, including delivered approximation precision.
A short expression for an extremely small g is not a supply of the required
long precision string. A primitive relation may be obtained by dividing z by
the gcd of its coordinates.

## D-STANDARD-POLYNOMIAL-QUANTUM-COMPUTATION

Input is an L-bit classical string. The circuit family is uniform, uses a
fixed finite universal gate set with efficiently computable amplitudes, and
has polynomially many qubits, gates and measured output bits in L. Its
decision error is at most 1/3. State preparation, precision, conditioning,
and postselection success are charged. No opaque quantum-data source,
unbounded-precision real advice, or unit-cost exponential oracle is supplied.
The BQP simulation statements in this review apply to this model.

## D-BOOLEAN-PICARD-SURFACE

Input is an integer matrix A with s rows and v>=1 columns, and an integer
vector b, all in binary. The underlying Boolean feasibility question is
`Ax=b`, `x in {0,1}^v`. This is a separate growing-ambient family from the
smooth connected quartic K3 problem.

In projective coordinates `[h:t:x_1:...:x_v]` define Z by the quadrics

    t(t-h)=0,
    x_i(x_i-h)=0,        (h-t)x_i=0 for 1<=i<=v,
    t(sum_i A_ji x_i-b_j h)=0 for 1<=j<=s.

Define the projective pure two-dimensional scheme `Y=Z x P^2`.
An ordinary projective encoding is also part of the definition: apply the
Segre embedding into `P^(3(v+2)-1)`, impose its two-by-two minors, and for
each displayed quadric G impose G on each of the three columns of Segre
coordinates. The expanded quadratic equation list has polynomial size.

The output is one iff geometric Picard rank of Y exceeds one. The input uses
this explicit syntactic construction; it does not hide normalization,
irreducible decomposition, saturation, or a blow-up inside a free oracle.
The output schemes are smooth and projective but need not be connected.
