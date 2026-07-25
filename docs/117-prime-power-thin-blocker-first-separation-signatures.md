# Thin Hall blockers concentrate in one p-adic line signature

The width-two divisor stratum in CMR293 can be sharpened in the prime-power
setting.  Two fixed Hall slices do not generate an arbitrary collection of
gcd classes: after the common power of `p` is removed, the pair direction has
only one vertical type at each earlier row-separation depth and `p` types at
the column-separation depth.  Consequently a linear, up to one logarithm,
population of canonical thin-blocker lines shares one exact first-separation
scale and one projective direction.

Let

\[
t=p^h
\]

with `p` an odd prime.  Work in the normalized inherited parent board.  For a
nonaxis line containing two cells

\[
P=(x,a),\qquad Q=(x+d,a+e),
\]

where `d,e` are nonzero integers of absolute value below `t`, define

\[
r=v_p(d),
\qquad
b=\min\{v_p(d),v_p(e)\}.
\]

Its **Hall-pair first-separation signature** is

\[
\Sigma(P,Q)
=
\left(
 b,
 \left[
 p^{-b}d:p^{-b}e
 \right]_{\mathbb P^1(\mathbb F_p)}
\right).
\]

The projective pair is nonzero because `b` is the minimum valuation.

## 1. Exact signature classification for two fixed slices

### Theorem CMR294 — PROVED

Fix a nonzero source-slice separation `d`, and put `r=v_p(d)`.  As the nonzero
row displacement `e` varies, at most

\[
\boxed{r+p}
\]

distinct Hall-pair first-separation signatures occur.

More precisely:

1. for each `0<=b<r`, there is only the vertical projective type
   \[
   \left(b,[0:1]\right);
   \]
2. at `b=r`, there are at most the `p` types
   \[
   \left(r,[1:s]\right),
   \qquad s\in\mathbb F_p.
   \]

### Proof

If `v_p(e)=b<r`, then after division by `p^b` the source displacement is zero
modulo `p` and the row displacement is a unit.  The projective direction is
therefore `[0:1]`, independently of the unit part of `e`.

Now suppose `v_p(e)>=r`.  Division by `p^r` leaves the source displacement a
unit.  Normalize its projective coordinate to one.  The second coordinate is

\[
s
\equiv
\frac{e/p^r}{d/p^r}
\pmod p.
\]

It may be any element of `F_p`; the value zero is exactly the case
`v_p(e)>r`.  These are the stated `p` possibilities.  No other minimum
valuation can occur. ∎

## 2. Width-two linear-over-logarithmic extraction

### Theorem CMR295 — PROVED

Let a sharp width-two target-specific blocker lie in a parent block of size
`t=p^h`.  Among the `t-2` pairwise endpoint-disjoint full chords from CMR284,
there is a subfamily of size at least

\[
\boxed{
\operatorname{ceil}\left(
\frac{t-2}{v_p(d)+p}
\right)
}
\]

whose Hall endpoint pairs have one common first-separation depth and one common
projective direction.

In particular, because `v_p(d)<=h-1`, the subfamily has size at least

\[
\boxed{
\operatorname{ceil}\left(
\frac{t-2}{h+p-1}
\right).
}
\]

Every external third-point witness on one of these chord lines lies on the same
real primitive direction represented by the extracted projective class.

### Proof

The endpoint row displacements are nonzero because a compatible matching event
cannot prescribe the same target row at the two Hall columns.  Apply CMR294 to
the `t-2` chords and pigeonhole their at most `v_p(d)+p` signatures.  The final
bound uses `0<d<t=p^h`.  A third point on the chord has the same primitive real
line direction; multiplication by its integer continuation parameter may
increase a pair-separation valuation, but it does not change the projective
line direction. ∎

## 3. Width-three extraction

### Theorem CMR296 — PROVED

Let a sharp width-three target-specific blocker with `t=p^h>=10` be reduced by
CMR288 to `t-9` pairwise cell-disjoint full triples on source slices

\[
x_1<x_2<x_3.
\]

Put `D=x_3-x_1`.  Among those triples, at least

\[
\boxed{
\operatorname{ceil}\left(
\frac{t-9}{v_p(D)+p}
\right)
}
\]

have one common first-separation signature between their outer Hall endpoints.
Hence there is always a common class of size at least

\[
\boxed{
\operatorname{ceil}\left(
\frac{t-9}{h+p-1}
\right).
}
\]

The dual statement holds when the smaller Hall side consists of target slices.

### Proof

For every retained triple, the two outer row coordinates are distinct; otherwise
collinearity would make the entire triple horizontal, which is incompatible
with a matching event.  Apply CMR294 with fixed source displacement `D` and
pigeonhole.  Coordinate duality gives the target-side statement. ∎

## 4. Prefix-scale ownership

### Corollary CMR297 — PROVED

Suppose the normalized parent block is a prefix block at absolute depth `s`.
A normalized Hall-pair signature

\[
(b,\theta)
\]

lifts to the absolute signature

\[
\boxed{(s+b,\theta)}.
\]

Thus every width-two or width-three blocker contains a canonical population of
size

\[
\Omega_p\left(\frac{t}{\log t}\right)
\]

owned by one absolute first-separation scale and one direction in
`P^1(F_p)`.

### Proof

Both physical coordinate differences in the prefix block are obtained from the
normalized differences by multiplication by `p^s`.  Their common minimum
valuation therefore increases by exactly `s`, while division by the common
power leaves the same projective residue direction.  Apply CMR295 or CMR296. ∎

## 5. Revised thin-blocker interface

The width-two `Omega(sqrt(t))` exact-gcd class from CMR293 remains useful when
one needs one exact primitive horizontal step.  CMR295 is stronger when the
relevant ledger records only p-adic first-separation depth and projective
direction.  Width three now has the same prime-power concentration.

The remaining charging theorem may therefore work with a finite directional
alphabet at every prefix scale.  It must show that the extracted population is
an anchored continuation, an envelope expansion, or a boundedly reusable
quotient/carry cell; this chapter does not yet prove that global reuse bound.

No all-`n` theorem is claimed here.  The signature classification, scale lift,
and finite prime-power counts are checked in
[`scripts/verify_prime_power_thin_first_separation.py`](../scripts/verify_prime_power_thin_first_separation.py).
