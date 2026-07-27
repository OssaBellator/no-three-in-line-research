# Certified auxiliary blocks eliminate by a nonnegative resolvent

The current labelled recurrent quotient contains a small number of difficult
core rows together with auxiliary modules such as subunit selectors, fixed-
interface tables, thin tables and reused-support states.  Once one auxiliary
module has its own strict certificate, repeated excursions through that module
need not remain as separate coordinates in the final search.  They can be
summed exactly by a nonnegative resolvent.

This chapter proves the finite nonnegative Schur-complement criterion.  The
scalar selector condition

\[
\alpha+\beta T<1
\]

is the one-dimensional zero-self special case.

Let

\[
M=
\begin{pmatrix}
A&B\\
C&D
\end{pmatrix}
\]

be a finite nonnegative rational matrix.  The `A` coordinates are the retained
core and the `D` coordinates are an auxiliary recurrent module.

## 1. Nonnegative auxiliary resolvent

Assume

\[
\rho(D)<1.
\]

### Theorem CMR1694 -- PROVED

The inverse

\[
\boxed{
R_D=(I-D)^{-1}
}
\]

exists, is rational, and is entrywise nonnegative.  Moreover

\[
R_D=I+D+D^2+\cdots
\]

entrywise.

### Proof

Because `rho(D)<1`, the Neumann series converges and equals `(I-D)^{-1}`.  Every
term is nonnegative.  Since `D` is rational, the inverse of the nonsingular
rational matrix `I-D` is rational. ∎

The matrix `R_D` records all finite auxiliary excursions before return to the
core.

## 2. Effective core matrix

Define

\[
\boxed{
S=A+B R_D C.
}
\]

### Theorem CMR1695 -- PROVED

If `M` is subcritical, then `S` is subcritical:

\[
\rho(M)<1
\quad\Longrightarrow\quad
\rho(S)<1.
\]

### Proof

Choose positive vectors `x,y` with

\[
Ax+By<x,
\qquad
Cx+Dy<y.
\]

The second inequality gives

\[
(I-D)y>Cx.
\]

Multiplication by the nonnegative inverse `R_D` yields

\[
y>R_DCx.
\]

Therefore

\[
Sx=Ax+B R_DCx<Ax+By<x.
\]

A finite nonnegative matrix admitting a positive strict vector has spectral
radius below one. ∎

Thus no contraction is lost by eliminating the certified auxiliary coordinates.

## 3. Constructive lift from the effective core

### Theorem CMR1696 -- PROVED

If `rho(S)<1`, then `rho(M)<1`.  More precisely, let `x>0` satisfy

\[
Sx<x
\]

and choose `z>0` satisfying

\[
Dz<z.
\]

Then for every sufficiently small rational `epsilon>0`,

\[
\boxed{
y=R_DCx+\epsilon z
}
\]

satisfies

\[
Ax+By<x,
\qquad
Cx+Dy<y.
\]

### Proof

Using `R_D=I+DR_D`,

\[
Cx+D R_DCx=R_DCx.
\]

Hence

\[
Cx+Dy
=R_DCx+\epsilon Dz
< R_DCx+\epsilon z
=y.
\]

The first row is

\[
Ax+By
=Sx+\epsilon Bz.
\]

Because `x-Sx` is positive, choose a positive rational `epsilon` small enough
that `epsilon Bz<x-Sx` coordinatewise. ∎

The lift is explicit and preserves rationality.

## 4. Exact subcriticality equivalence

### Theorem CMR1697 -- PROVED

Under `rho(D)<1`,

\[
\boxed{
\rho(M)<1
\quad\Longleftrightarrow\quad
\rho\bigl(A+B(I-D)^{-1}C\bigr)<1.
}
\]

### Proof

Combine CMR1695 and CMR1696. ∎

This is the nonnegative finite Schur-complement test at spectral threshold one.

## 5. Zero-self auxiliary rows

If the auxiliary module has zero self-row, `D=0`, then `R_D=I`.

### Theorem CMR1698 -- PROVED

For

\[
M=
\begin{pmatrix}
A&B\\
C&0
\end{pmatrix},
\]

one has

\[
\boxed{
\rho(M)<1
\quad\Longleftrightarrow\quad
\rho(A+BC)<1.
}
\]

For one return coordinate and one selector coordinate,

\[
A=(\alpha),
\qquad B=(\beta),
\qquad C=(T),
\]

this becomes exactly

\[
\boxed{\alpha+\beta T<1.}
\]

### Proof

Set `D=0` in CMR1697. ∎

The same reduction simultaneously eliminates any finite family of zero-self
auxiliary classes.

## 6. Rational and strict integer certificates

### Theorem CMR1699 -- PROVED

Suppose `A,B,C,D` are rational and `rho(D)<1`.  Then the following data form a
finite rational certificate for `rho(M)<1`:

1. a positive rational auxiliary vector `z` with `Dz<z`;
2. the rational resolvent `R_D=(I-D)^{-1}`;
3. a positive rational core vector `x` with
   \[
   (A+B R_D C)x<x;
   \]
4. one positive rational `epsilon` satisfying the CMR1696 bound.

After clearing one common denominator, all matrix identities and strict
inequalities become a finite strict integer certificate.

### Proof

CMR1694 gives a rational resolvent, CMR1696 gives the rational lift, and common-
denominator clearing preserves strict inequalities after multiplying by a
positive integer. ∎

No numerical eigenvalue approximation is required.

## 7. Block-diagonal auxiliary modules

Suppose

\[
D=\operatorname{diag}(D_1,\ldots,D_k)
\]

and every `D_i` has a strict rational certificate.

### Theorem CMR1700 -- PROVED

The effective core is

\[
\boxed{
S=A+
\sum_{i=1}^k B_i(I-D_i)^{-1}C_i,
}
\]

where `B_i,C_i` are the corresponding block columns and rows.  The full matrix
is subcritical exactly when this effective core is subcritical.

### Proof

The inverse of `I-D` is block diagonal with blocks `(I-D_i)^{-1}`.  Expand
`B(I-D)^{-1}C` and apply CMR1697. ∎

Thus independently certified thin, fixed-interface or support modules may be
eliminated before searching the final difficult core.

## 8. Auxiliary-elimination endpoint

### Corollary CMR1701 -- PROVED

The labelled recurrent quotient may now be reduced in the following order.

1. Certify any finite auxiliary module, including normalized thin or fixed-
   interface orbit tables.
2. Retain all collision, local-line, owner and CRT labels inside that module.
3. Compute its exact rational resolvent.
4. Add the effective excursion term `B(I-D)^{-1}C` to the remaining core.
5. Search a strict rational or integer certificate only for the reduced core.
6. Lift the certificate constructively and then apply labelled SCC/CRT gluing.

The remaining obstacle is still numerical: the effective core itself must be
proved subcritical.  The theorem prevents already-certified auxiliary tables
from inflating that final search.  No all-`n` theorem is claimed.

Nonnegative resolvents, exact Schur complements, rational lifts and integer
certificate clearing are checked in
[`scripts/verify_prime_power_subcritical_auxiliary_block_elimination.py`](../scripts/verify_prime_power_subcritical_auxiliary_block_elimination.py).
