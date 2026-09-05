# Octonionic phase and associator input models

2026-09-05. Quantum coefficient spaces have the ordinary positive Euclidean
metric, a C1 departure. The identity mathbb1 below locally departs from C6.
Real norm identities are used only on real unit octonion coefficients.
All operators on quantum registers are complex-linear. No basis-label
phase is silently identified with a map on continuous geometric points.

## D-OCTONION-CONVENTION

Use Cayley--Dickson multiplication
`(a,b)(c,d)=(ac-conjugate(d)b, da+b conjugate(c))`
on quaternion pairs. Ordered basis:
`e_0=(1,0),e_1=(i,0),e_2=(j,0),e_3=(k,0),`
`e_4=(0,1),e_5=(0,i),e_6=(0,j),e_7=(0,k)`.
Labels a,b belong to F_2^3, with low-to-high bits a_0,a_1,a_2.
The table is `e_a e_b=(-1)^F(a,b)e_(a+b)`, where

`F(a,b)=a_0 b_0+a_1 b_0+a_2 b_0+a_1 b_1+a_2 b_1+a_2 b_2`
`       +a_2 b_0 b_1+a_1 b_0 b_2+a_0 b_1 b_2` over F_2.

Let `partial F(a,b,c)=F(a,b)+F(a+b,c)+F(b,c)+F(a,b+c)`.
The retained-label operator is
`U_ass|a,b,c>=(-1)^(partial F(a,b,c))|a,b,c>`.
The different continuous associator is `[x,y,z]=(xy)z-x(yz)`.
Its complex-linear coefficient map is
`A:C^8 tensor C^8 tensor C^8 -> C^8`,
`A(x tensor y tensor z)=[x,y,z]`.
Set `K=A/sqrt(96)` and `P=K^dagger K`.

## D-OCTONION-PHASE-QUERY

Supply a simple three-uniform hypergraph H on v>=3 vertices with m edges,
and y in F_2^(3v). Each vertex has a variable a_i in F_2^3. Let n=3v and

`f_H(a)=sum_({i,j,k} in E(H)) det_(F_2)(a_i,a_j,a_k)`,
`X_H=V(f_H) subset A_(F_2)^n`,
`b_y=2^(-n)sum_a (-1)^(f_H(a)+y.a)`, `p_y=b_y^2`.

The sparse equation and y have O(m log v+v) input bits. For supplied
`0<gamma<=1` and `0<delta<=1/3`, decide p_y=0 versus p_y>=gamma with
failure at most delta. The circuit prepares uniform bits, applies U_ass
at each edge, and measures after a final Walsh transform.
Its complete sampling output is the bit string Y with probability p_Y;
this is a different output from the fixed-frequency decision problem.
For a particular subfamily, nonemptiness of the promised positive case is
not assumed beyond its actual attainable p_y.

## D-OCTONION-CONTINUOUS-QUERY

One-use quantum point inputs are three real unit coefficient vectors
`x,y,z in R^8`, supplied as separate three-qubit states. Global signs do
not affect the associator norm. The event of the folded filter K has
probability `||[x,y,z]||^2/96`; its coherent output is the normalized
associator only if that norm is nonzero. Copy access supplies neither
coefficient queries nor an inverse state-preparation circuit.

A separate classical-list model gives L>=1 triples `(x_i,y_i,z_i)`
with real unit rational coordinates of at most B input bits. Put
`R=(1/L)sum_i ||[x_i,y_i,z_i]||^2`. For `0<gamma<=4` and
`0<delta<=1/3`, decide R=0 versus R>=gamma with error at most delta.
The zero locus consists of
the cubic associator equations and the given real unit-sphere quadrics.
Indexed list access is charged equally to either algorithm; a coherent
whole-list oracle is not supplied. A quantum row trial prepares three
coefficient states and applies K at explicitly charged accuracy eta.

For the one-triple copies-only variant, the same promise is on
`||[x,y,z]||^2`. Separate-source tomography is an allowed concrete upper
bound; no optimality or generic tomography baseline is assumed.

For the tensor-power scope diagnostic, each of three original sources
contains a normalized maximally entangled pair of eight-dimensional sites.
The two local effects P act across corresponding sites of the three sources.
This state is product across the original sources, but is not product
across the two sites within a source.
