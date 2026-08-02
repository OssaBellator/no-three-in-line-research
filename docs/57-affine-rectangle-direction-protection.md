# Affine rectangle protection of low primitive directions

PX81--PX84 isolate low primitive height as the sole source of full-order
transversal codegree in the rectangle matching model.  This chapter gives a
factor-compatible positive construction which removes any prescribed finite set
of nonaxis directions from the product state.

The construction is a rectangle analogue of the affine finite-direction theorem
A1, but it remains inside the full-symmetric one-inner-layer product family and
therefore transports to every saturated factor.

Throughout this chapter use the ordinary `cc` orientation and write line
directions as primitive integer vectors

\[
q=(a,b),
\qquad a b\ne0.
\]

The integer line coordinate is

\[
\lambda_q(x,y)=b x-a y.
\]

## 1. Affine rectangle family

Fix residues `m,c,s modulo n` with `gcd(m,n)=1`, and define

\[
p_s(u)=u+s\pmod n,
\]

\[
t_c(u)=r_c(u)=mu+c\pmod n.
\]

The rectangle state is

\[
Q_{m,c,s}=Q(p_s,t_c,r_c).
\]

For every `u` it contains all four corners of

\[
\{u,n+p_s(u)\}\times\{t_c(u),n+t_c(u)\}.
\]

It is automatically saturated by PX43.

### Theorem PX86 -- PROVED

Let `D` be a finite set of nonaxis primitive directions.  Suppose

\[
\gcd(m,n)=1
\]

and

\[
\gcd(b-am,n)=1
\qquad ((a,b)\in D).
\]

Then every real scalar line whose direction lies in `D` contains at most two
points of `Q_(m,c,s)`.  Consequently the state has no collinear triple in any
direction from `D`.

The assertion holds for every pair of shifts `c,s`.

### Proof

Colour the four corner types by their coarse row block.  The top colour consists
of

\[
(u,t_c(u)),
\qquad
(u,n+t_c(u)),
\]

and the bottom colour consists of

\[
(n+p_s(u),t_c(u)),
\qquad
(n+p_s(u),n+t_c(u)).
\]

Fix `q=(a,b) in D`.  For the first top corner type,

\[
\lambda_q(u,t_c(u))=b u-a t_c(u).
\]

If two indices `u,v` give the same integer line coordinate, reduction modulo
`n` gives

\[
(b-am)(u-v)=0\pmod n.
\]

The gcd hypothesis forces `u=v`.  Thus this corner type uses distinct real
`q`-lines.  The second top corner has coordinate

\[
\lambda_q(u,n+t_c(u))=\lambda_q(u,t_c(u))-an.
\]

It is separately injective.  Equality between a first-type and second-type
coordinate again gives `u=v` modulo `n`, after which the two integers differ by
`an`, which is nonzero because the direction is nonaxis.  Hence all `2n` top
corners lie on distinct real `q`-lines.

For the bottom colour,

\[
\lambda_q(n+p_s(u),t_c(u))
=bn+bs+(b-am)u
\pmod{\text{integer wrap terms}},
\]

and the exact equality argument modulo `n` is identical.  The second bottom
corner differs by `-an`.  Therefore all `2n` bottom corners also lie on distinct
real `q`-lines.

A real line can contain at most one top point and at most one bottom point, hence
at most two selected points in total.  The shifts contribute only constants and
do not affect injectivity. \(\square\)

## 2. Arithmetic existence

The same residue-avoidance argument as A2 supplies a slope.

### Theorem PX87 -- PROVED

Let `D` be a finite set of nonaxis primitive directions.  If every prime divisor
`ell` of `n` satisfies

\[
ell>|D|+1,
\]

then there is a residue `m` satisfying all hypotheses of PX86.

### Proof

For each prime divisor `ell` of `n`, avoid `m=0`.  For a direction `(a,b)`, if
`a` is nonzero modulo `ell`, at most one further residue

\[
m=b a^{-1}\pmod\ell
\]

is forbidden.  If `a=0 modulo ell`, then `b` is nonzero modulo `ell` because
`(a,b)` is primitive, so the direction imposes no restriction.  There are at
most `|D|+1` forbidden residues and therefore at least one allowed residue.
Choose allowed residues independently at each prime power and combine them by
the Chinese remainder theorem.  The resulting `m` is a unit modulo `n` and
makes every `b-am` a unit. \(\square\)

## 3. Protection through height `H`

Let `D_H` be a fixed-half-plane set of all nonaxis primitive directions with

\[
\max(|a|,|b|)\le H.
\]

PX62 gives at most `4h` primitive directions of exact height `h`, so

\[
|D_H|\le\sum_{h=1}^H4h=2H(H+1).
\]

### Corollary PX88 -- PROVED

If the least prime factor of `n` is greater than

\[
2H(H+1)+1,
\]

then every saturated no-three side-`n` factor has a factor-compatible saturated
side-`2n` rectangle state containing no triple in any primitive direction of
height at most `H`.

### Proof

Apply PX87 to `D_H`, then PX86.  The normalized scalar rectangle state is
available to every permutation layer of every saturated side-`n` factor by the
full-symmetric gauge transport PX41. \(\square\)

For prime `n`, any `H` with

\[
2H(H+1)+1<n
\]

is admissible, so one may protect `H=Theta(sqrt(n))` primitive height.

## 4. Consequence for transversal codegree

Inside a repair or resampling family which preserves all protected line
occupancies, every remaining bad triple has primitive height greater than `H`.
PX82 then bounds every remaining transversal completion codegree by

\[
64n^2\left(1+\frac{2n}{H}\right).
\]

For prime `n` and `H=Theta(sqrt(n))`, this is

\[
O(n^{5/2})=O(d^{5/6}),
\qquad d=n^3.
\]

Thus the polynomial codegree saving required by conflict-free matching methods
is available after low-direction protection.  The remaining missing step is to
construct a sufficiently rich factor-compatible repair or absorber family which
preserves the protected line capacities while varying the high-direction
geometry.

This is a sharper target than an unrestricted perfect-matching theorem: the
low-height obstruction has been removed explicitly, and only entropy inside the
protected family is missing.

## 5. Verification

Run

```bash
python scripts/verify_product_affine_rectangle_protection.py
```

The verifier checks the line-coordinate injectivity directly on exact scalar
states, tests the arithmetic slope search on rough composite moduli and primes,
and confirms protection of every primitive direction through the chosen height.