# Multi-rung parabolic coordinate budget

A single monotone parabolic reservoir has square-root width.  This does not by
itself match the current one-shot prime-gap exponent, but several smaller rungs
could in principle be installed in one prepared seed.  This chapter records the
exact coordinate budget before any geometric compatibility claim is made.

## 1. Disjoint old-coordinate blocks

Use the smallest parabolic parameters `L=2,d=1`.  A width-`t_i` rung occupies
an old-coordinate interval of length

\[
 s_i=2(t_i-1)^2+1.
\]

Suppose `K` such row patterns and `K` such column patterns are placed in
pairwise disjoint old-coordinate intervals.  A necessary and sufficient
one-dimensional packing condition for these intervals is

\[
 \sum_{i=1}^K s_i\le m.
\]

This statement concerns only coordinate placement.  It does not assert that the
prime-size seed contains the required matching reservoirs or that the resulting
patches are mutually no-three.

### Proposition PP3ah -- PROVED

Let

\[
 T=\sum_{i=1}^K t_i.
\]

If the `K` parabolic coordinate intervals fit in `[m]`, then

\[
 \boxed{
 T\le
 K+\sqrt{\frac{K(m-K)}2}.
 }
\]

#### Proof

Put `u_i=t_i-1`.  The packing inequality is

\[
 2\sum_{i=1}^K u_i^2+K\le m.
\]

Hence

\[
 \sum_i u_i^2\le\frac{m-K}{2}.
\]

Cauchy--Schwarz gives

\[
 T-K
 =
 \sum_i u_i
 \le
 \sqrt{K\sum_i u_i^2}
 \le
 \sqrt{\frac{K(m-K)}2}.
\]

Add `K`. ∎

The bound is attained up to rounding by taking all widths nearly equal.  If

\[
 u=
 \left\lfloor\sqrt{\frac{m-K}{2K}}\right\rfloor,
 \qquad
 t_i=u+1,
\]

then the `K` intervals fit and their total width is `K(u+1)`.

## 2. Exponent conversion

### Corollary PP3ai -- PROVED

Let a desired total extension width be `T=m^theta` with fixed
`theta>1/2`.  In the regime `K=o(T)`, any disjoint equal-scale parabolic-rung
architecture needs

\[
 K=\Omega(m^{2\theta-1}),
\]

and the coordinate budget permits

\[
 K=O(m^{2\theta-1})
\]

up to constant factors and rounding.

#### Proof

From PP3ah and `K=o(T)`,

\[
 T\le(1+o(1))\sqrt{Km/2},
\]

so `K>= (2-o(1))T^2/m`.  Conversely choose `K` a sufficiently large constant
multiple of `T^2/m` and use nearly equal widths as above. ∎

For the published prime-gap exponent `theta=0.525`, the coordinate exponent is

\[
 2\theta-1=0.05.
\]

Thus an `m^{0.525}` total ladder needs only `m^{0.05}` square-root-scale rungs
at the level of one-dimensional coordinate capacity.

## 3. What this does and does not solve

The arithmetic removes one possible objection to square-root absorbers: the old
row and column sets have enough total capacity for a subpolynomial number of
rungs covering a current prime gap.

The missing theorem is geometric and substantially stronger.  A prepared seed
would need:

1. one matching reservoir for each rung;
2. external cleanliness against the retained core;
3. compatibility between points inserted by different rungs;
4. preservation of the required conditions as the consecutive new-coordinate
   intervals are exposed.

No such multi-rung compatibility theorem is proved here.  PP3ah--PP3ai merely
quantify the exact size of the target: for exponent `0.525`, it is enough to
control about `m^0.05` rungs rather than construct one absorber of width
`m^0.525`.
