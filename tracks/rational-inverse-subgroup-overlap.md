# Exact subgroup-overlap formula for rational-inverse collisions

RI1a identifies image loss with full orbits of

\[
\tau_r(x)=\frac{r(x-1)}{x-r}.
\]

This note evaluates that orbit count for a full subgroup coset and writes
the remaining incidence problem as explicit multiplicative-character
sums.

Let \(H\leq\mathbb F_p^\times\), let \(x_0\in\mathbb F_p^\times\), and
put

\[
C_0=x_0H\setminus\{1,r\}.
\]

For \(u\neq x_0^{-1},rx_0^{-1}\), define the Möbius map

\[
\phi_{r,x_0}(u)
=\frac{\tau_r(x_0u)}{x_0}
=\frac{r(x_0u-1)}{x_0(x_0u-r)}.
\]

## RI1c -- exact coset-overlap count

### Theorem RI1c -- PROVED

Let

\[
J(H;r,x_0)=
\left|\left\{
u\in H:
x_0u\notin\{1,r\},\
\phi_{r,x_0}(u)\in H
\right\}\right|
\]

and let

\[
f(H;r,x_0)=
\left|\left\{
x\in C_0:\tau_r(x)=x
\right\}\right|.
\]

Then \(f(H;r,x_0)\leq2\), the number of full nonfixed collision
orbits in \(C_0\) is

\[
\boxed{\frac{J(H;r,x_0)-f(H;r,x_0)}2,}
\]

and therefore

\[
\boxed{
|F_r(C_0)|
=|C_0|-\frac{J(H;r,x_0)-f(H;r,x_0)}2.
}
\]

Moreover, every counted \(u\), with
\(v=\phi_{r,x_0}(u)\), is a solution in \(H^2\) of

\[
x_0^2uv-rx_0(u+v)+r=0,
\]

and every solution away from the pole arises this way.

### Proof

The definition of \(\phi_{r,x_0}\) gives

\[
\tau_r(x_0u)=x_0\phi_{r,x_0}(u).
\]

Thus \(J\) counts exactly the points of \(C_0\) whose
\(\tau_r\)-partners also lie in \(C_0\).  A nonfixed full orbit
contributes two points to \(J\), while a fixed orbit contributes one.
Hence the number of nonfixed full orbits is \((J-f)/2\).  RI1a gives the
image formula.

A fixed point satisfies

\[
(x-r)^2=r(r-1),
\]

so there are at most two.  Finally, substitution of
\(x=x_0u\) and \(\tau_r(x)=x_0v\) in the collision equation from RI0
gives the displayed bilinear curve.  Solving that equation for \(v\)
recovers \(\phi_{r,x_0}(u)\), proving the converse.
\(\square\)

## Exact character decomposition

Let \(m=[\mathbb F_p^\times:H]\), and choose a multiplicative character
\(\chi\) of exact order \(m\) with kernel \(H\).  Put

\[
U=\mathbb F_p^\times
\setminus\{x_0^{-1},rx_0^{-1}\}.
\]

Character orthogonality gives the exact identity

\[
\boxed{
J(H;r,x_0)
=\frac1{m^2}
\sum_{a,b=0}^{m-1}
\sum_{u\in U}
\chi^a(u)\chi^b\!\left(\phi_{r,x_0}(u)\right).
}
\]

Indeed, for nonzero \(z\),

\[
\mathbf 1_H(z)=\frac1m\sum_{a=0}^{m-1}\chi^a(z),
\]

and inserting this twice in the definition of \(J\) proves the formula.

For the pair \((a,b)\), the inner summand is a constant character factor
times the character of

\[
u^a(x_0u-1)^b(x_0u-r)^{-b}.
\]

Because \(0,x_0^{-1},rx_0^{-1},\infty\) are distinct, its divisor has
orders \(a,b,-b,-a\) at those four points.  For
\(0\leq a,b<m\), all four orders are divisible by \(m\) only when
\((a,b)=(0,0)\).  Thus the trivial pair is the sole possible
\(m\)-th-power main term.

This does not silently import a character-sum estimate.  It isolates the
remaining analytic input exactly: bound the \(m^2-1\) displayed
nontrivial rational-character sums, uniformly in the subgroup index
needed by RI1--RI3, and then convert the resulting image distribution
across target cosets into an absorber or expansion statement.

`scripts/verify_rational_subgroup_overlap.py` exhaustively checks the
overlap, orbit, bilinear-curve, image-loss, and character-orthogonality
identities for subgroup cosets through prime \(31\).
