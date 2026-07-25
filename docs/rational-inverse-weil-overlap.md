# Weil bound for subgroup--Möbius overlap

RI1c expresses the collision-partner count inside a full subgroup coset
as \(m^2\) rational multiplicative-character sums, where
\(m=[\mathbb F_p^\times:H]\). The divisor calculation in that note makes
the standard Weil character bound directly applicable.

Retain

\[
J(H;r,x_0)=
\left|\left\{
u\in H:
x_0u\notin\{1,r\},\
\phi_{r,x_0}(u)\in H
\right\}\right|,
\]

where

\[
\phi_{r,x_0}(u)
=\frac{r(x_0u-1)}{x_0(x_0u-r)}.
\]

We use the standard multiplicative-character estimate on
\(\mathbb P^1\): if \(\chi\) has order \(m\), a rational function \(g\)
is not an \(m\)-th power over \(\overline{\mathbb F}_p\), and its divisor
has \(\nu\) distinct points, then

\[
\left|\sum_{u\in\mathbb F_p}\chi(g(u))\right|
\leq(\nu-1)\sqrt p.
\]

Characters, including the principal character, are extended by zero at
zero, and a summand at a pole is interpreted as zero.

## RI1d -- uniform full-coset collision bound

### Theorem RI1d -- PROVED

Let \(H\leq\mathbb F_p^\times\) have index \(m\), let
\(r\neq0,1\), and let \(x_0\neq0\). Then

\[
\boxed{
\left|
J(H;r,x_0)-\frac{p-3}{m^2}
\right|
\leq
3\left(1-\frac1{m^2}\right)\sqrt p
<3\sqrt p.
}
\]

Let

\[
C_0=x_0H\setminus\{1,r\}.
\]

The number \(P_0\) of full nonfixed collision orbits in \(C_0\) satisfies

\[
\boxed{
P_0
\leq
\frac{p-3}{2m^2}+\frac32\sqrt p.
}
\]

Consequently every subset \(C\subseteq C_0\) obeys

\[
\boxed{
|F_r(C)|
\geq
|C|-\frac{p-3}{2m^2}-\frac32\sqrt p.
}
\]

### Proof

Choose a character \(\chi\) of exact order \(m\) with kernel \(H\).
RI1c gives

\[
J=
\frac1{m^2}
\sum_{a,b=0}^{m-1}
\sum_u
\chi^a(u)\chi^b\!\left(\phi_{r,x_0}(u)\right)
\]

over the admissible set
\(\mathbb F_p^\times\setminus\{x_0^{-1},rx_0^{-1}\}\).
Up to a constant character factor of absolute value one, its
\((a,b)\)-summand is the character of

\[
u^a(x_0u-1)^b(x_0u-r)^{-b}.
\]

To turn it into a full-field character sum without boundary errors,
multiply inside the character by the \(m\)-th-power mask

\[
\left(\frac{u(x_0u-1)}{x_0u-r}\right)^m.
\]

This does not change any admissible summand, and the zero/pole convention
makes the three excluded values contribute zero. The resulting rational
function has divisor orders

\[
a+m,\quad b+m,\quad-(b+m),\quad-(a+m)
\]

at \(0,x_0^{-1},rx_0^{-1},\infty\), respectively.

For \((a,b)=(0,0)\), the summand is one at the \(p-3\) admissible values
and zero at the three excluded values. Its contribution is \(p-3\).

For a nontrivial pair \((a,b)\), the four orders modulo \(m\) are
\(a,b,-b,-a\). Since \(0\leq a,b<m\), the masked rational function is an
\(m\)-th power only when \((a,b)=(0,0)\). Thus every nontrivial term has
four distinct divisor points and the Weil bound gives absolute value at
most \(3\sqrt p\).

There are \(m^2-1\) nontrivial terms. Dividing their total bound by
\(m^2\) proves the estimate for \(J\).

RI1c gives

\[
P_0=\frac{J-f}{2}
\]

with \(f\geq0\), so \(P_0\leq J/2\), proving the second display. Every
collision pair wholly contained in \(C\) is also a collision pair in
\(C_0\). Applying the exact image-loss identity RI1a and the bound on
\(P_0\) proves the final display.
\(\square\)

## Interpretation

Since \(|H|=(p-1)/m\),

\[
\frac{J(H;r,x_0)}{|H|}
=\frac1m+O\!\left(\frac{m}{\sqrt p}\right).
\]

Thus for every fixed proper subgroup index \(m\geq2\), only an
asymptotic \(1/m\) fraction of a full source coset has its collision
partner in the same coset. This rules out dense full-coset collision
pairing except at the square-root error scale.

RI1 is not yet complete: the target asks for distribution of
\(F_r(C)\) among target \(H\)-cosets, or growth of its quotient set, for
an arbitrary dense subset \(C\). RI1d controls cardinality loss but does
not by itself prevent the surviving image values from concentrating in a
small union of target cosets.

`scripts/verify_rational_weil_overlap.py` exhaustively checks the exact
overlap counts and the squared Weil inequality through prime \(43\).
