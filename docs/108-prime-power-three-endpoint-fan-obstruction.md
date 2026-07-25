# Three-endpoint obstruction for singleton sharp fans

CMR247 separates a sharp target-specific blocker into a singleton fan or a
nontrivial Hall-boundary factor. A singleton fan is highly target-dependent: it
covers every alternative cell in one source slice or target slice. The three
endpoints of one old nonaxis triple cannot all reuse the same near-complete fan.
A first- and second-moment argument gives the exact common-family threshold.

Let `Y` be a finite set of `t` real row coordinates. Let

\[
x_1<x_2<x_3
\]

be three source coordinates, and let

\[
z_i=(x_i,y_i),
\qquad
y_i\in Y,
\]

be three distinct collinear points on a nonhorizontal line. Put

\[
\lambda=\frac{x_3-x_2}{x_3-x_1},
\qquad
0<\lambda<1.
\]

Then

\[
y_2=\lambda y_1+(1-\lambda)y_3.
\]

A **common source-fan family** is a family of nonvertical lines such that on
each slice `x=x_i` the intersection coordinates are distinct elements of
`Y\setminus\{y_i\}`.

## 1. Three-slice moment obstruction

### Theorem CMR257 — PROVED

Every common source-fan family has size at most

\[
\boxed{t-3.}
\]

The bound is sharp.

### Proof

A common family has size at most `t-1` because its intersections on each slice
are distinct and avoid `y_i`. It is enough to rule out size `t-2`; a larger
family contains a subfamily of that size.

Suppose there are `t-2` common lines. On slice `i`, their intersection set has
the form

\[
Y\setminus\{y_i,r_i\}
\]

for some second omitted value `r_i` distinct from `y_i`.

Every common line is affine, so if its three intersection ordinates are
`a_1,a_2,a_3`, then

\[
a_2=\lambda a_1+(1-\lambda)a_3.
\]

Sum this identity over the line family. Writing

\[
S_1=\sum_{y\in Y}y,
\]

we obtain

\[
S_1-y_2-r_2
=
\lambda(S_1-y_1-r_1)
+(1-\lambda)(S_1-y_3-r_3).
\]

The target collinearity relation cancels, leaving

\[
r_2=\lambda r_1+(1-\lambda)r_3.
\]

Now apply convexity of the square to every line:

\[
a_2^2
\le
\lambda a_1^2+(1-\lambda)a_3^2.
\]

After summing and writing

\[
S_2=\sum_{y\in Y}y^2,
\]

we get

\[
S_2-y_2^2-r_2^2
\le
\lambda(S_2-y_1^2-r_1^2)
+(1-\lambda)(S_2-y_3^2-r_3^2).
\]

Equivalently,

\[
y_2^2+r_2^2
\ge
\lambda(y_1^2+r_1^2)
+(1-\lambda)(y_3^2+r_3^2).
\]

But the two affine interpolation identities and convexity give the reverse
inequality. Equality would require simultaneously

\[
y_1=y_3
\qquad\text{and}\qquad
r_1=r_3.
\]

The first condition says that the old target line is horizontal, impossible for
three points in a saturated state because every row contains only two points.
This contradiction proves the upper bound.

Sharpness already occurs on the standard coordinate set

\[
Y=\{0,1,\ldots,t-1\}.
\]

Take target points `(0,0),(1,1),(2,2)` and the `t-3` parallel lines

\[
y=x+r,
\qquad
1\le r\le t-3.
\]

Their intersections are distinct and avoid all three target cells. ∎

## 2. Dual target-slice form

### Corollary CMR258 — PROVED

The dual statement holds for three target-coordinate slices. Namely, if the
three old target points are written with distinct row coordinates and a family
of nonhorizontal lines meets each corresponding horizontal slice in distinct
source coordinates avoiding the old target cell, then the family has size at
most `t-3`.

### Proof

Interchange the two board coordinates in CMR257. ∎

## 3. Expansion across three singleton blockers

### Corollary CMR259 — PROVED

Let one old nonaxis target triple have endpoints `z_1,z_2,z_3`. Suppose each
endpoint has a sharp CMR247 singleton blocker on its source side, with line
families

\[
\mathcal L_1,
\mathcal L_2,
\mathcal L_3,
\qquad
|\mathcal L_i|=t-1.
\]

Then

\[
\boxed{
|\mathcal L_1\cup\mathcal L_2\cup\mathcal L_3|
\ge t.
}
\]

In particular the same `t-1` line signatures cannot be the sharp source-fan
blocker for all three target endpoints. The same conclusion holds when all
three singleton blockers lie on the target side.

### Proof

CMR257 gives

\[
|\mathcal L_1\cap\mathcal L_2\cap\mathcal L_3|
\le t-3.
\]

If the union had size at most `t-1`, then every one of its three subsets of size
`t-1` would equal the whole union, and their triple intersection would also have
size `t-1`, a contradiction. Hence the union has size at least `t`. The target
side follows from CMR258. ∎

The bound `t` is the exact set-theoretic consequence of the `t-3` common-family
threshold: three `(t-1)`-subsets of a `t`-set can have triple intersection
`t-3`.

## 4. Three-endpoint blocker dichotomy

### Corollary CMR260 — PROVED

For the three endpoint-specific sharp blockers of one old target triple, at
least one of the following holds.

1. Some blocker has a nontrivial Hall-boundary factor from CMR247.
2. The singleton blockers do not all lie on the same board side.
3. Their candidate-line universe contains at least `t` distinct real-line
   signatures.

### Proof

If neither of the first two alternatives holds, all three blockers are singleton
fans on one common board side. Apply CMR259. ∎

CMR260 is not yet a complete blocker conversion: mixed source/target fans and
nontrivial Hall-boundary factors remain possible. It does, however, prove an
exact no-reuse statement across the three endpoint choices and identifies the
two geometric configurations which still need inherited prefix or carry input.

No all-`n` theorem is claimed here. The moment identities and the sharp standard
grid examples are checked in
[`scripts/verify_prime_power_three_endpoint_fans.py`](../scripts/verify_prime_power_three_endpoint_fans.py).
