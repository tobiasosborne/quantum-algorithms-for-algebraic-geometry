# Encoding Boolean integer feasibility into a Picard-rank question

2026-09-08. Derived construction, registered as C-385 at SKETCH pending an
independent campaign audit. Under current D27 this NP-complete family is a
negative control and a rejected quantum-algorithm target. It concerns
D-BOOLEAN-PICARD-SURFACE, not the
connected quartic K3 family. The reduction itself uses only polynomial-size
lists of homogeneous quadrics.

## Statement

ASSUME the binary matrix input (A,b) of D-BOOLEAN-PICARD-SURFACE, and let N
be its number of Boolean solutions. PROVE that Y is a smooth projective pure
two-dimensional scheme with

    Y_(Qbar) is the disjoint union of N+1 copies of P^2,
    rank Pic(Y_(Qbar))=rank NS(Y_(Qbar))=N+1.

Consequently the rank-greater-than-one decision on this explicitly encoded
family is NP-complete. This does not assert that general Picard-rank detection
is in NP, nor that connected K3 Picard-rank detection is NP-hard.

1. There are no projective points or scheme pieces at h=0. In that quotient,
   the equations imply t²=x_i²=0. Every homogeneous prime contains every
   remaining coordinate, so Proj is empty. Thus Z is contained in D_+(h).
   REFERENCE: the canonical quadrics and the definition of Proj.

2. Set h=1. The equations t²=t and x_i²=x_i present the split Boolean algebra
   `Q[t,x]/(t²-t,x_i²-x_i) = product_(t,x in {0,1}) Q`.
   Quotienting a product of fields by additional equations keeps precisely
   the factors on which those equations vanish; it creates no nilpotents.
   REFERENCE: Chinese remainder theorem and the canonical equations.

3. At t=0 the equations (1-t)x_i=0 force every x_i=0, giving one known point.
   At t=1 they impose no additional constraint on Boolean x, and the row
   equations become Ax=b. Therefore Z is the disjoint union of N+1 rational
   reduced points. In particular it is finite étale and never empty.
   REFERENCE: steps1--2.

4. Product with P² gives a disjoint union of N+1 projective planes. Each
   component is smooth over Q, so their finite disjoint union is smooth and
   projective of pure dimension two. Picard groups of finite disjoint unions
   are products, Pic(P²)=Z and Pic^0(P²)=0. This proves the asserted ranks.
   REFERENCE: step3 and the elementary Picard group of projective space.

5. The input has 1+2v+s quadrics in v+2 projective coordinates, with O(v+sv)
   nonzero terms before combining cancellations. Coefficients are original
   entries or constants. For an ordinary projective output, write Segre
   coordinates z_ij=u_i y_j, where u=(h,t,x).
   REFERENCE: D-BOOLEAN-PICARD-SURFACE.

6. The Segre minors impose its image. For each source quadric G, impose
   `G(z_0j,...,z_(v+1)j)=y_j²G(u)=0` for j=0,1,2. On the open set y_j!=0
   this is exactly G(u)=0. These opens cover P², so the equations define
   Z x P² scheme-theoretically, not merely set-theoretically.
   There are O(v²+s+v) quadrics with polynomial total sparse encoding length.
   REFERENCE: step5, the Segre embedding, and localization on those three opens.

7. A Boolean solution is a polynomial-size witness for rank>1 by steps3--4.
   Conversely, rank>1 supplies a non-dummy Boolean solution by the same steps.
   Boolean equality feasibility is NP-hard already with one row (subset sum),
   and its proposed Boolean vector is verified in polynomial time.
   The explicit syntactic geometric family therefore has an NP-complete
   decision problem. REFERENCE: steps3--6 and Karp's Boolean integer/knapsack
   NP-completeness results, DOI 10.1007/978-1-4684-2001-2_9.

8. The construction does not preserve connectedness or irreducibility, fixes
   no quartic embedding in P³, and places its hardness in the number of
   components. It does not establish an NP-hardness reduction to the extra
   divisor problem on a connected K3 surface. An abstract appeal to a
   blow-up, smoothing or universality theorem would still require a
   polynomial-size explicit encoding and proof that the rank criterion survives.
   REFERENCE: the output in step4 and the fixed input definition for quartics.

9. If this NP-complete family were also in coNP, then NP=coNP. A polynomial
   quantum solver would imply NP subset BQP, which is not currently ruled
   out but would be a much stronger claim than a typical NP-intersect-coNP
   speedup. Neither consequence is asserted to hold.
   REFERENCE: step7 and closure under polynomial-time reductions.

## Small exact control

For A=(1,2,3), b=3, the Boolean solutions are (1,1,0) and (0,0,1), so Y
has three P² components and Picard rank3. For the same A and b=7 there is
no solution, so Y=P² and its Picard rank is1. These examples test the
encoding; they do not replace the uniform argument.
