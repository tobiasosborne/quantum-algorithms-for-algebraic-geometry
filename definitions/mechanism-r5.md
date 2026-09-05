# Definitions for the fifth bounded mechanism probes

2026-09-05. These are ordinary finite-dimensional Hilbert spaces with declared
orthonormal bases, departing from C1's Fock convention. The auxiliary length
`D` locally departs from C8. Identity operators are written `1` or
`mathbb1`, departing from C6 where necessary. Conjugation follows C3.
None of these input models supplies an unmentioned preparation inverse,
root oracle, quotient multiplication table, or canonical geometric metric.

## D-R5-JET-SOURCE

Let `D>=2,r=D-1,0<t<1,m>=D`. The vectors `u_1,...,u_r` in `C^m` are
unknown and orthonormal. The unit vector `u_0=|0>` spans a homogeneous
coordinate register orthogonal to the affine coordinate register. The affine arc is
`gamma(z)=sum_(k=1)^r z^k conjugate(u_k)`; the family has coordinate ring
`C[t,z]/(z^D-t^D)` and its embedding is induced by this arc.
Write `zeta=exp(2 pi i/D)` and `Z_t=sum_(k=0)^r t^(2k)`.
The supplied resource is independent copies of the coherent labelled source

`Psi_t=D^(-1/2)sum_(a=0)^(D-1)|a> v_a`,
`v_a=Z_t^(-1/2)sum_(k=0)^r t^k zeta^(ak) u_k`.

Thus the affine part is the conjugated coordinate vector of
`gamma(t zeta^(-a))`. Set
`chi_k=D^(-1/2)sum_a zeta^(ak)|a>`, let `L chi_k=|k>`, and let
`K_t=sum_k t^(r-k)|k><k|`. The equal-weight jet state is
`Phi=D^(-1/2)sum_k |k>u_k`. Put `s_bit=t^(2r)/Z_t` and
`s_flat=D s_bit`.

The geometric query supplies a linear hyperplane `H` through the affine
origin, containing `conjugate(u_1),...,conjugate(u_(r-1))`. Promise that
`conjugate(u_r)` belongs to `H` or its Hermitian orthogonal complement.
Decide whether the special fibre is scheme-theoretically contained in `H`.
The quantum hyperplane test uses `span{u_0} direct-sum conjugate(H)`.
Each source copy and the supplied hyperplane measurement have charged costs.
Copies alone do not include controlled preparation or its inverse.

## D-R5-DEFECT-TRANSPORT

Let `D>=2` be binary encoded and let complex `tau`, `|tau|<1`, be supplied
to a stated finite precision. The algebra `C[z]/(z^D-tau)` has the declared
orthonormal coefficient basis `|k>=z^k`, `0<=k<D`. Its multiplication by
`z` is `C_tau=sum_(k<D-1)|k+1><k|+tau|0><D-1|`.
Let `beta=sqrt(1-|tau|^2)` and adjoin an orthogonal state `b`. Define

`U_tau|k>=|k+1>` for `k<D-1`,
`U_tau|D-1>=tau|0>+beta|b>`,
`U_tau|b>=beta|0>-conjugate(tau)|b>`.

Here `P` projects onto the live coefficient space and
`c_T=<0|U_tau^T|0>`. The fresh-bath version instead adjoins orthogonal
`e_1,...,e_T`; step `V_j` uses the displayed `U_tau` on the live space
and `e_j` and fixes every other bath state. Its natural measured output is
the final live index or retained exit label. This is different from a
measurement after an arbitrary additional quantum circuit.

## D-R5-TRINOMIAL-COPRODUCT

Let `D=2^n>=4`, `f=x^D-a x-b`, and give `n` and the real and imaginary
coefficient parts to specified binary precision. The declared orthonormal
monomial basis of `A=C[x]/(f)` is `1,x,...,x^(D-1)`. The map `M_f`
multiplies two representatives and takes their remainder modulo `f`.
Put `lambda=1+|a|+|b|`, `alpha_BE=sqrt(D) lambda`, and
`K=M_f^dagger/alpha_BE`. A root diagnostic uses
`w_z=sum_r conjugate(z)^r|r>`, `nu_z=||w_z||`, and `u_z=w_z/nu_z`.

For the terminal problem, take nonnegative rational `0<=a<=1/4,b=1`,
coefficient bit length at most `B`, and integer `2<=m<D`. Begin with
`|D-1>` and apply a binary tree of `m-1` successful `K` operations.
Set `R_s=[x^(D-1)](x^s mod f)` and let `N_(m,D)(s)` be the number
of tuples in `{0,...,D-1}^m` summing to `s`. Put
`Z_m=sum_s N_(m,D)(s)|R_s|^2` and
`p_m=Z_m/(D lambda^2)^(m-1)`.
The output is either a sample of the measured conditional tuple law or an
additive estimate of `p_m`. Roots and multiplication tables are not inputs.

## D-R5-GRASSMANN-QUERY

An explicit-coordinate stream, independent of private sketch randomness,
supplies mutually orthonormal `u_1,...,u_k in R^q`, `k>=1`.
Let `U=span{u_i}` and
`P_U=sum_i u_i u_i^T`. A unit-vector query `v` arrives after the stream,
independently of private sketch randomness. The bit problem promises
`v in U` or `v perpendicular to U`; its relaxed output estimates
`beta=v^T P_U v` to additive `epsilon`, with failure at most `delta`.

Each sketch uses independent random sign vectors `g,h`, each four-wise
independent within its coordinates, and stores
`A=sum_i(g^T u_i)(h^T u_i)`. At the query it computes
`B_query=(g^T v)(h^T v)` and `Z=A B_query`. Repeated sketches are
independent. Four-wise sign seeds cost `O(log q)` bits each. Numeric
accumulator size is charged separately; for common `b`-bit dyadic inputs
it is `O(b+log(kq))` bits. The exact-arithmetic proof and finite-precision
promises are distinct. Adaptive-query robustness is not supplied.
