# Coefficient-state Schur reduction and disk counting

2026-09-05. These coefficient spaces use the Euclidean monomial metric,
departing from C1. Degree D and identity mathbb1 locally depart from C8
and C6. The root-count interpretation uses real coefficients; a physical
coefficient-reversal gate is not an antiunitary conjugation operation.

## D-DISK-COUNT-INPUT

Let `f(z)=sum_(j=0)^D a_j z^j` be a real polynomial of degree D>=1,
with a_D nonzero. Supply a positive rational radius R_0 and promise no
root lies on its boundary. The target is
`nu_(R_0)(f)=D^(-1) #{z:f(z)=0, |z|<R_0}`, with multiplicities,
to additive error 1/4 and success probability at least 2/3.

In the classical-bit model, all rational coefficient encodings are supplied
to either algorithm. In the copy model, only independent copies of
`|f>=sum_j a_j|j>/sqrt(sum_j |a_j|^2)` are supplied. A quantum protocol
may process them jointly. Its separate-measurement comparator may use any
adaptive POVM on one complete copy at a time and arbitrary classical
processing. Copies provide no coefficient queries or preparation inverse.
These models cannot be interchanged by ignoring normalization or loading.

## D-COEFFICIENT-SCHUR-STEP

For a current positive degree d, let `H_d=C^(d+1)` have coefficient
basis |0>,...,|d>. Define

`R_d|j>=|d-j>`,
`K_d=(<d| tensor mathbb1-<0| tensor R_d)/sqrt(2)`,
`S_d=sum_(j=1)^d |j-1><j|`, `Ktilde_d=S_d K_d`.

For a normalized coefficient vector a put
`p_d(a)=||Ktilde_d(a tensor a)||^2`.
The raw K_d has target H_d; the degree-changing Ktilde_d has target H_(d-1).
The zero raw output coordinate is rejected, though it has zero amplitude
on every identical product input. This specifies a physical contraction
on all inputs, not just a nonlinear rule on polynomial coefficients.

For the real unit-disk recurrence assume no unit-circle roots and
`|a_0|!=|a_d|` at every visited positive-degree reduced polynomial.
Define `f^#(z)=z^d f(1/z)` and
`g(z)=(a_d f(z)-a_0 f^#(z))/z`.
The resulting normalized coefficient state is the next input on success.
Write n(f) for the integer unit-disk root count with multiplicities.
The no-boundary-root and all-stage strict-endpoint promises are distinct.

In the fixed fresh-child recursion, C_t is the expected number of original
copies to produce one state after t degree reductions, with C_0=1. Every
failed step discards both inputs and prepares fresh children. Let p_t be
that step's probability. At stage t of an initial degree-D input, a^(t)
has degree D-t; learning the branch from copies additionally charges a
known lower bound gamma_t>0 on
`abs(|a^(t)_(D-t)|^2-|a^(t)_0|^2)`.
No optimality among all implementations, shortcuts or source-reuse methods
is included in this particular recursion model.

For `0<R_0<1`, direct radius rescaling uses the separate filter
`A_(R_0)=sum_j R_0^j|j><j|`. Its heralding probability is charged.

## D-SEPARATED-RADIAL-DISK-FAMILY

Let D>=3, set R_0=5/8, and promise
`f_R(z)=z^D-R^D` with `R in {1/2,3/4}`. Its supplied normalized
coefficient state is
`F_R=(|D>-R^D|0>)/sqrt(1+R^(2D))`.
The two target values nu_(R_0) are one and zero. Put
`x=(1/2)^D`, `y=(3/4)^D` and
`delta_fid=(y-x)^2/((1+x^2)(1+y^2))`.
The lower bound concerns a total source-copy cap N and includes every
failure/postselection event in the overall success probability.
It is not a claim about quantum algorithms given the classical coefficient
bits instead, nor a lower bound for the unit disk, whose two counts agree.
