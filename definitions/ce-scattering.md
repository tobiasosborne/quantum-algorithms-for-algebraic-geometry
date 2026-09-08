# Finite higher-obstruction scattering definitions

2026-09-07. This finite boson/fermion construction is an R11 diagnostic, not a
promoted algorithm. Bosonic factors use the Fock convention C1, and fermionic
occupation vectors are orthonormal. Weighted degree below is a new grading,
not the total boson number of the seed. The operator norm and evolution time
refer to the stated finite sector, not the unbounded full Fock operator.

## D-R11-CE-CUBIC-SCHEME

For a supplied real `g>0`, let

    f_v(X,U)=U+(g/sqrt(6))X²,   f_w(X,U)=g X U,
    A_g=C[X,U]/(f_v,f_w).

Give `X,U` weights `1,2`. The two relations have weights `2,3`. Eliminating
`U` gives the relation `-(g²/sqrt(6))X³`; thus the intended local scheme is
a cubic fat point. At `g=0`, the algebra is instead `C[X]`, and statements
about finite length are not extended to that parameter.

## D-R11-CE-FOCK-SUPERCHARGE

There are bosonic annihilators `a_x,a_u` and fermionic creators `c_v†,c_w†`.
Different bosonic modes commute; fermionic creators anticommute; the two kinds
commute. Assign the conserved weight

    W=n_x+2n_u+2n_v+3n_w.

For real `g>=0`, define the finite restrictions of

    Q_g=c_v†(a_u+(g/sqrt(6))a_x²)+g c_w† a_x a_u,
    H_g=Q_g+Q_g†.

The only weight-three occupation states are

    e0=|3_x>, e1=|1_x,1_v>, e2=|1_x,1_u>, e3=|1_w>.

Their order fixes all matrix and phase conventions. The state `e0` is a
normalized three-boson state, not the unnormalized monomial `X³`.

## D-R11-CE-SCATTERING-OUTPUT

Input is a chosen real `g>=0`, time `t>=0`, and a compiled implementation of
`H_g` on the weight-three sector, with a stated energy scale and error budget.
Prepare `e0`, evolve for time `t`, and output one on measurement `|e3><e3|`.
The common scalar is

    p_g(t)=|<e3|exp(-itH_g)|e0>|².

The gate/physical cost includes preparation, evolution, mode control and readout.
An explicit `4 x 4` matrix is also supplied to the classical comparator. This
fixed-size problem is a mechanism diagnostic and cannot have an asymptotic
computational advantage. General growing dg Lie families are a different
candidate requiring a separate definition and algorithm.
