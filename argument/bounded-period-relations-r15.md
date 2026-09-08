# A classical reduction for bounded, separated period relations

2026-09-08. Derived during the classical-baseline review. Canonical statement
C-382 enters as SKETCH pending independent campaign review. This argument
does not classify the unrestricted Picard-rank problem.

## Statement

ASSUME D-BOUNDED-SEPARATED-PERIOD-RELATION with fixed m. PROVE that its
finite-input decision problem is in deterministic polynomial time in the
binary lengths of H,g,a,b.

1. For every z in the height box, the real and imaginary errors in its
   approximate pairing are each at most
   `sum_i |z_i| g/(4mH)<=g/4`.
   REFERENCE: the approximation promise and the triangle inequality.

2. If z.pi=0, then both `|a.z|` and `|b.z|` are at most g/4.
   If z.pi is nonzero, the separation promise and step1 imply that at least
   one of those two quantities is at least 3g/4.
   REFERENCE: step1 and the second canonical promise.

3. Consequently exact zero is equivalent, within the nonzero integer height
   box, to the rational linear inequalities

       -H<=z_i<=H for every i,
       -g/2<=a.z<=g/2,
       -g/2<=b.z<=g/2.

   REFERENCE: step2. The threshold lies strictly between the two error bands.

4. Exclude z=0 by taking the union of 2m systems: for each i add either
   `z_i>=1` or `z_i<=-1`. Every nonzero integer vector belongs to at least
   one system; no feasible vector of one of these systems is zero.
   REFERENCE: integrality and step3.

5. Each system has m integer variables and rational linear inequalities.
   Clearing denominators has polynomial bit cost. Lenstra's fixed-variable
   integer-programming theorem solves each system in polynomial time for
   fixed m. There are only 2m systems.
   REFERENCE: H. W. Lenstra Jr., *Integer Programming with a Fixed Number
   of Variables*, DOI 10.1287/moor.8.4.538, and steps3--4.

6. Thus the finite promised search is polynomial, including recovery of a
   witness. For a quartic, m=21 is fixed. This gives a complexity upper bound;
   it does not assert that a 21-variable integer-programming implementation
   is the fastest practical alternative to LLL.
   REFERENCE: step5 and the canonical model.

7. To infer a polynomial algorithm for D-QUARTIC-EXTRA-PICARD-CLASS one would
   additionally need a sufficiently large H for every relevant surface, a
   valid separation g with polynomially many required bits, and a polynomial
   procedure constructing the marked periods at that precision. None of
   those uniform bounds follows from steps1--6.
   REFERENCE: the separate input models in definitions/picard-classical-r15.md.
