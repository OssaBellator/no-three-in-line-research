# A recycled mixed fan forces an opposite-deviation carry pair

CMR309 extracts a linear modular-ratio population from a fully recycled mixed
singleton fan.  The complete fan also contains two unavoidable shared-cell
lines: one through `(x_1,y_3)` and one through `(x_2,y_3)`.  Multiplying the
CMR306 factorization over every other line gives an exact factorial identity
for the two remaining row deviations.  At a prime-power side length, that
identity becomes a universal p-adic opposite-residue condition.

Let

\[
z_i=(x_i,y_i),
\qquad
x_1<x_2<x_3,
\]

be the old target triple.  Assume one family of `t-1` lines is simultaneously a
sharp source fan at `z_1`, a sharp source fan at `z_2`, and a sharp target fan at
`z_3`.

There is one line whose target-slice intersection is `c=x_1`.  It uses the cell
`(x_1,y_3)` and has second-source intersection `(x_2,b_0)`.  There is one line
with `c=x_2`; it uses `(x_2,y_3)` and has first-source intersection
`(x_1,a_0)`.  Nonaxis compatibility gives

\[
a_0\ne y_3,
\qquad
b_0\ne y_3.
\]

Define the signed factorial weight

\[
F_t(x)
=
\prod_{0\le r<t,\ r\ne x}(x-r)
=
(-1)^{t-1-x}x!(t-1-x)!.
\]

## 1. Exact factorial identity

### Theorem CMR318 — PROVED

The two special deviations satisfy

\[
\boxed{
F_t(x_2)(y_3-b_0)
=
-F_t(x_1)(y_3-a_0).
}
\]

Equivalently, with

\[
W_t(x)=x!(t-1-x)!,
\]

one has

\[
\boxed{
\frac{|y_3-b_0|}{|y_3-a_0|}
=
\frac{W_t(x_1)}{W_t(x_2)}.
}
\]

### Proof

Remove the two shared-cell lines.  The remaining `t-3` lines have slice
intersections

\[
a\in[0,t-1]\setminus\{y_1,y_3,a_0\},
\]

\[
b\in[0,t-1]\setminus\{y_2,y_3,b_0\},
\]

and

\[
c\in[0,t-1]\setminus\{x_1,x_2,x_3\}.
\]

For each line, CMR306 gives

\[
(x_2-c)(y_3-a)
=
(c-x_1)(b-y_3).
\]

Multiply over the `t-3` lines.  The four products are

\[
\prod(x_2-c)
=
\frac{F_t(x_2)}{(x_2-x_1)(x_2-x_3)},
\]

\[
\prod(y_3-a)
=
\frac{F_t(y_3)}{(y_3-y_1)(y_3-a_0)},
\]

\[
\prod(c-x_1)
=
(-1)^{t-3}
\frac{F_t(x_1)}{(x_1-x_2)(x_1-x_3)},
\]

and

\[
\prod(b-y_3)
=
(-1)^{t-3}
\frac{F_t(y_3)}{(y_3-y_2)(y_3-b_0)}.
\]

Cancel `F_t(y_3)` and use collinearity of the old target triple:

\[
\frac{y_3-y_2}{y_3-y_1}
=
\frac{x_3-x_2}{x_3-x_1}.
\]

The remaining signed equation is exactly the displayed identity.  Taking
absolute values gives the second form. ∎

## 2. Prime-power valuation balance

### Theorem CMR319 — PROVED

Let

\[
t=p^h
\]

for an odd prime `p`.  Then

\[
\boxed{
v_p(y_3-b_0)=v_p(y_3-a_0).}
\]

If this common valuation is `r`, then

\[
\boxed{
\frac{(y_3-b_0)/p^r}{(y_3-a_0)/p^r}
\equiv-1\pmod p.
}
\]

Thus the two shared-cell lines carry one exact opposite-deviation projective
signature at one common p-adic depth.

### Proof

Write

\[
W_t(x)
=
\frac{(t-1)!}{\binom{t-1}{x}}.
\]

Since `t-1=p^h-1` has every base-`p` digit equal to `p-1`, Lucas' congruence
gives

\[
\binom{t-1}{x}\equiv(-1)^x\pmod p.
\]

In particular every binomial coefficient is a p-adic unit, so all `W_t(x)` and
all `F_t(x)` have the same p-adic valuation.  CMR318 therefore gives equality
of the two special-deviation valuations.

After the common powers of `p` are removed, the unit ratio

\[
\frac{F_t(x_1)}{F_t(x_2)}
\]

is congruent to one modulo `p`: the sign ratio
`(-1)^{x_2-x_1}` is cancelled by the same ratio of the two Lucas congruences.
CMR318 then gives the residue `-1`. ∎

## 3. Archimedean localization

### Corollary CMR320 — PROVED

A fully recycled mixed fan can occur only when

\[
\boxed{
\frac{1}{t-1}
\le
\frac{W_t(x_1)}{W_t(x_2)}
\le
 t-1.
}
\]

Equivalently,

\[
\boxed{
W_t(x_2)
\le
(t-1)W_t(x_1)
\quad\text{and}\quad
W_t(x_1)
\le
(t-1)W_t(x_2).
}
\]

### Proof

The two nonzero special deviations have absolute values between one and
`t-1`.  Apply the absolute identity in CMR318. ∎

The ratio of consecutive weights is explicit:

\[
\frac{W_t(x+1)}{W_t(x)}
=
\frac{x+1}{t-1-x}.
\]

Hence CMR320 confines a recycled mixed fan to source-slice pairs whose factorial
weights differ by at most one factor `t-1`; this is an additional finite
archimedean restriction, although no optimal classification is claimed here.

## 4. Coordinate-dual form

### Corollary CMR321 — PROVED

For a fully recycled target/target/source fan, the corresponding two special
source deviations have equal p-adic valuation and reduced ratio `-1 mod p`.
The factorial identity uses `F_t(y_1),F_t(y_2)` instead of
`F_t(x_1),F_t(x_2)`.

### Proof

Interchange source and target coordinates throughout CMR318--CMR320. ∎

## 5. Revised mixed-fan endpoint

A fully recycled mixed fan now supplies two simultaneous structures.

1. CMR309 gives a linear unit-ratio population among the nondegenerate lines.
2. CMR319 gives an exact opposite-deviation carry pair on the two shared-cell
   lines.

The remaining weighted conversion theorem may use either structure: the large
ratio class can feed a common-ratio bank, while the two special lines give a
canonical p-adic anchor at one depth.  What is not yet proved is that one of
these structures necessarily carries a positive fraction of the current target
load.

No all-`n` theorem is claimed here.  The product identity, prime-power unit
ratio, special-deviation valuation balance, and small-board mixed-fan examples
are checked in
[`scripts/verify_prime_power_mixed_fan_factorial.py`](../scripts/verify_prime_power_mixed_fan_factorial.py).
