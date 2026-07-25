# Width-two blockers carry primitive displacement signatures

CMR284 reduces a sharp width-two Hall blocker to at least `t-2` endpoint-disjoint
chords between two fixed Hall slices, each with an external third-point witness.
The lattice geometry of one chord is exact: its primitive step is obtained by
dividing the slice separation and row displacement by their gcd, and every
witness is an integer continuation parameter. Pigeonholing the divisors of the
slice separation produces a large common horizontal-step stratum.

Assume the smaller Hall side consists of two source coordinates

\[
x_1<x_2,
\qquad
d=x_2-x_1.
\]

The dual target-side form follows by interchanging coordinates.

## 1. Exact primitive continuation

### Theorem CMR291 — PROVED

Let one full chord join

\[
P=(x_1,a),
\qquad
Q=(x_2,b),
\]

and put

\[
e=b-a,
\qquad
g=\gcd(d,|e|),
\qquad
u=\frac{d}{g},
\qquad
v=\frac{e}{g}.
\]

Then `(u,v)` is the primitive integer direction of the chord line. Every grid
cell on that line is uniquely of the form

\[
\boxed{
P+q(u,v),
\qquad q\in\mathbb Z.
}
\]

The second Hall endpoint is the parameter `q=g`. Every external witness for the
candidate-only chord triple has a parameter

\[
q\in\mathbb Z\setminus\{0,g\}
\]

for which both coordinates remain in the parent board.

### Proof

The displacement from `P` to `Q` is

\[
(d,e)=g(u,v),
\]

with `gcd(u,|v|)=1`. The integer points on a line through one lattice point with
primitive direction `(u,v)` are exactly its integer translates by that vector.
The parameter is unique because the direction is nonzero. The two endpoints
correspond to `0` and `g`; every distinct third grid point has another integer
parameter. ∎

## 2. Internal and extension witnesses

### Corollary CMR292 — PROVED

A witness parameter from CMR291 is exactly one of the following.

1. **Internal witness:**
   \[
   1\le q\le g-1.
   \]
   This is possible only when `g>=2`.
2. **Left extension:**
   \[
   q<0.
   \]
3. **Right extension:**
   \[
   q>g.
   \]

In particular, when `g=1`, every candidate witness lies beyond the segment
joining the two Hall slices.

### Proof

The source coordinate is `x_1+qu`, while `x_2=x_1+gu` and `u>0`. Its position
relative to the two slices is therefore determined exactly by the comparison of
`q` with `0` and `g`. ∎

## 3. A common gcd stratum

### Theorem CMR293 — PROVED

Among the `t-2` endpoint-disjoint full chords supplied by CMR284, there is a
subfamily of size at least

\[
\boxed{
\operatorname{ceil}\left(\frac{t-2}{\tau(d)}\right)
}
\]

having one common value of

\[
g=\gcd(d,|b-a|).
\]

Every chord in this subfamily has the same primitive horizontal step

\[
\boxed{u=d/g.}
\]

Using the elementary divisor bound

\[
\tau(d)\le2\sqrt d,
\]

one obtains the uniform lower bound

\[
\boxed{
\operatorname{ceil}\left(
\frac{t-2}{2\sqrt{t-1}}
\right).
}
\]

### Proof

For every chord, `g` is a positive divisor of the fixed slice separation `d`.
There are `tau(d)` possibilities. Pigeonholing the `t-2` chords gives the first
bound. The primitive horizontal coordinate is `d/g`, hence is common on that
class.

Every divisor below `sqrt(d)` pairs with one above `sqrt(d)`, with at most one
unpaired square-root divisor, giving `tau(d)<=2sqrt(d)`. Finally `d<=t-1`. ∎

## 4. Width-two arithmetic endpoint

Every sharp width-two blocker therefore supplies:

- a two-slice endpoint matching with at most one slack unit;
- an external integer continuation parameter on every full chord;
- and a common primitive horizontal-step population of size
  `Omega(sqrt(t))` without using any deep divisor estimate.

This is the precise interface to the existing displacement, first-separation,
and carry-cell machinery. A stronger divisor bound would enlarge the common
stratum, but the remaining theorem is qualitative: prove that one such stratum
forces an anchored continuation, an envelope expansion, or a paid primitive
carry population.

No all-`n` theorem is claimed here. Primitive continuation and divisor-stratum
arithmetic are checked in
[`scripts/verify_prime_power_width_two_signatures.py`](../scripts/verify_prime_power_width_two_signatures.py).
