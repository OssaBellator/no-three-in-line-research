# Polynomial direction growth is necessary for direct rectangle codegree savings

PX173 proves protected simultaneous-rainbow spread for every fixed finite
direction family.  This chapter shows that a fixed family, or even a
polylogarithmically growing family, cannot supply the polynomial transversal
codegree saving required by the direct rectangle conflict theorem.

The obstruction is not confined to the diagonal directions.  Every fixed
positive primitive direction supports an explicit family of order
\(n^3/h\) transversal completions, where \(h\) is its primitive height.

Let

\[
(a,b)\in\mathbb Z_{>0}^2,
\qquad
\gcd(a,b)=1,
\qquad
h=\max(a,b).
\]

Assume \(2h\le n-1\).  In the rectangle host \(\mathcal K_n\), put

\[
e=(0,0,0,0),
\qquad
f=(a,1,b,1).
\]

For

\[
2\le k\le\left\lfloor\frac{n-1}{h}\right\rfloor,
\qquad
p,r\in\{2,\ldots,n-1\},
\]

define

\[
g_{k,p,r}=(ka,p,kb,r).
\]

## Theorem PX174 -- PROVED

For every one of the four radix orientations, the edges \(e,f\) are compatible
and every \(g_{k,p,r}\) is compatible with both.  Their corresponding
\((0,0)\)-corners are collinear.  Hence

\[
\boxed{
\operatorname{codeg}_{\rm trans}(e,f)
\ge
\left(
\left\lfloor\frac{n-1}{h}\right\rfloor-1
\right)(n-2)^2.
}
\]

The primitive direction of the displayed line is

\[
\operatorname{prim}(c_xa,c_yb),
\]

where

\[
c_x,c_y\in\{1,2\}
\]

depend only on the two radix modes.

### Proof

Coordinatewise compatibility is immediate:

- the first and second edges use respectively \(0\) and the nonzero coordinates
  \(a,1,b,1\);
- the multiplier satisfies \(k\ge2\), so \(ka\notin\{0,a\}\) and
  \(kb\notin\{0,b\}\);
- the remaining coordinates \(p,r\) avoid \(0,1\).

For the \((0,0)\)-corner, the flattening map in one scalar coordinate is
multiplication by \(c=1\) in coarse-major mode and by \(c=2\) in fine-major
mode.  Thus the three relevant corners are

\[
(0,0),
\qquad
(c_xa,c_yb),
\qquad
(kc_xa,kc_yb),
\]

which are collinear.  The multiplier has

\[
\left\lfloor\frac{n-1}{h}\right\rfloor-1
\]

choices, independently of the \((n-2)^2\) choices for \(p,r\). \(\square\)

For fixed \((a,b)\), this is \(\Theta(n^3)\).  Therefore infinitely many
primitive direction classes, not merely the diagonals, have full-order
transversal codegree as \(n\to\infty\).

## 2. Quantitative necessity

## Theorem PX175 -- PROVED

Fix constants

\[
C>0,
\qquad
0<\delta<1.
\]

Suppose a direction-protection scheme is intended to leave every unprotected
compatible rectangle pair with transversal codegree at most

\[
C n^{3-\delta}.
\]

Then, for every sufficiently large \(n\), it must protect at least

\[
\boxed{c_C n^{2\delta}}
\]

distinct primitive directions, where \(c_C>0\) depends only on \(C\).

Equivalently, since the rectangle host degree is \(d=n^3\), achieving the
standard conflict bound

\[
O(d^{1-\varepsilon})
\]

requires at least

\[
\boxed{\Omega(n^{6\varepsilon})}
\]

protected directions.

### Proof

Let

\[
H=\left\lfloor\frac{n^\delta}{32C}\right\rfloor.
\]

For every positive primitive pair with \(a,b\le H\), PX174 and elementary
estimates give, for large \(n\),

\[
\left(
\left\lfloor\frac{n-1}{h}\right\rfloor-1
\right)(n-2)^2
\ge
\frac{n^3}{16h}
\ge
2C n^{3-\delta}.
\]

Its direction must therefore be protected.

The number of positive coprime pairs in \([H]^2\) is at least \(H^2/4\).  Indeed,
if a pair is not coprime, some integer \(q\ge2\) divides both coordinates, so
by the union bound the number of noncoprime pairs is at most

\[
H^2\sum_{q=2}^{H}\frac1{q^2}
<
H^2\left(\frac14+\int_2^\infty\frac{dx}{x^2}\right)
=
\frac34H^2.
\]

For each of the four orientations, the map

\[
(a,b)\longmapsto\operatorname{prim}(c_xa,c_yb)
\]

is injective on primitive positive pairs.  When one scale is two, the parity of
the unscaled coordinate distinguishes whether the common factor two was
removed.  Thus these coprime pairs give at least \(H^2/4=\Omega_C(n^{2\delta})\)
distinct protected directions.

Finally put \(3-\delta=3(1-\varepsilon)\), so
\(\delta=3\varepsilon\). \(\square\)

## 3. Consequence for the protected-spread route

PX173 solves every fixed direction family, but PX175 proves that a direct
application of a conflict theorem with a fixed polynomial codegree exponent
requires polynomially many simultaneous linear forms.  The next theorem must
therefore do one of the following.

1. Extend PX172 to host uniformity

   \[
   s=p^\kappa
   \]

   for some fixed \(\kappa>0\).
2. Replace uniform direction protection by a weighted or direction-aware
   conflict process which tolerates many low-height labels.
3. Use the exact low-syndrome/repair route instead of a direct rectangle
   perfect-matching theorem.

A fixed-family theorem, even with arbitrarily strong cylinder spread, cannot
by itself cross the direction barrier.

## Verification

Run

```bash
python scripts/verify_product_direction_lower_family.py
```

The verifier checks every explicit family in all four orientations through
side fifteen and confirms the elementary quadratic count of positive primitive
directions at several cutoffs.
