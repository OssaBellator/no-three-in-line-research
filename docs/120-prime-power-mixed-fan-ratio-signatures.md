# Mixed singleton fans carry modular ratio signatures

Same-side singleton fans are controlled by the three-slice moment obstruction
CMR257.  The remaining orientation pattern has two source-side fans and one
target-side fan, or its coordinate dual.  Its geometry is bilinear rather than
affine, but it has an exact primitive-ratio parameterization.  A large recycled
mixed fan therefore contains a linear population with one common modular ratio
signature.

Let an old nonaxis target triple be

\[
z_i=(x_i,y_i),
\qquad
x_1<x_2<x_3.
\]

Consider a real line `L` common to source-side singleton fans at `z_1,z_2` and
a target-side singleton fan at `z_3`.  Write its three slice intersections as

\[
(x_1,a),
\qquad
(x_2,b),
\qquad
(c,y_3).
\]

Put

\[
d=x_2-x_1,
\qquad
s=c-x_1,
\qquad
\alpha=y_3-a,
\qquad
\beta=b-y_3.
\]

The intersections on each singleton slice are distinct across a common fan
family.

## 1. Exact mixed-fan factorization

### Theorem CMR306 — PROVED

The three slice intersections are collinear if and only if

\[
\boxed{(d-s)\alpha=s\beta.}
\]

If `s` is neither `0` nor `d`, put

\[
g=\gcd(|s|,|d-s|)=\gcd(|s|,d).
\]

Then there is one nonzero integer `q` such that

\[
\boxed{
\alpha=q\frac{s}{g},
\qquad
\beta=q\frac{d-s}{g}.
}
\]

Conversely every such integer parameter whose three cells remain in the board
gives the required collinearity.

### Proof

The determinant of the three intersections is

\[
d(y_3-a)-(c-x_1)(b-a).
\]

Using `b-a=alpha+beta` and `c-x_1=s`, its vanishing is

\[
d\alpha=s(\alpha+\beta),
\]

which is the displayed factorization.  When `s(d-s)` is nonzero, divide the two
coefficients by their gcd.  The resulting integers `s/g` and `(d-s)/g` are
coprime, so the equality forces `alpha` and `beta` to be one common integer
multiple of them.  The converse is immediate. ∎

## 2. The only shared-cell degeneracies

### Corollary CMR307 — PROVED

A common mixed fan contains at most two lines not covered by the nondegenerate
parameterization:

1. `s=0`, when `(x_1,a)=(c,y_3)` and hence `a=y_3`;
2. `s=d`, when `(x_2,b)=(c,y_3)` and hence `b=y_3`.

Each type occurs at most once because singleton-fan intersections on every
slice are distinct.

### Proof

Substitute `s=0` or `s=d` into CMR306.  The relevant source-slice intersection
must equal the horizontal-slice intersection.  Distinctness on that source
slice permits at most one line of each type. ∎

## 3. Unit-ratio extraction

Assume now that the parent side is

\[
t=p^h.
\]

For a nondegenerate line with both `s` and `d-s` units modulo `p`, define

\[
\rho(L)
=
 s(d-s)^{-1}
\pmod p.
\]

### Theorem CMR308 — PROVED

Let `mathcal F` be a common mixed-fan family of size `m`.  It contains a
subfamily of size at least

\[
\boxed{
\operatorname{ceil}\left(
\frac{
\max\{0,m-2-2t/p\}
}{p-1}
\right)
}
\]

with one common value of `rho(L)`.

For every line in this subfamily,

\[
v_p(\alpha)=v_p(\beta),
\]

and after their common power of `p` is removed,

\[
\boxed{
[\alpha:\beta]
=
[\rho:1]
\quad\text{in }\mathbb P^1(\mathbb F_p).
}
\]

If `p` does not divide `d`, the common ratio also fixes one target-intersection
residue `c mod p`.

### Proof

CMR307 removes at most two lines.  The target-slice intersections `c` are
distinct.  Among all `t` board columns, at most `t/p` satisfy `p|s`, and at most
`t/p` satisfy `p|(d-s)`.  Removing those two residue classes leaves at least

\[
\max\{0,m-2-2t/p\}
\]

unit-unit lines.  Their ratios lie in `F_p^*`, which has `p-1` elements, so
pigeonholing gives the stated population.

For a unit-unit line, the gcd `g` in CMR306 is a `p`-adic unit.  The exact
factorization therefore gives equal valuations of `alpha` and `beta`, and the
reduced projective ratio is `s:(d-s)=rho:1`.

Finally

\[
s\equiv\rho(d-s)\pmod p.
\]

If `p` does not divide `d`, then `rho` cannot equal `-1`, and

\[
s\equiv\frac{\rho d}{1+\rho}\pmod p
\]

is fixed.  Since `c=x_1+s`, the target-intersection residue is fixed as well. ∎

## 4. Recycled sharp mixed fans

### Corollary CMR309 — PROVED

Suppose three sharp singleton blockers with orientation source/source/target
recycle one common line family of size `t-1`.  Then they contain a common
unit-ratio population of size at least

\[
\boxed{
\operatorname{ceil}\left(
\frac{t-3-2t/p}{p-1}
\right).
}
\]

For every fixed prime `p>=5`, this is `Omega_p(t)`.  The coordinate-dual result
holds for target/target/source orientation.

### Proof

Apply CMR308 with `m=t-1`.  Coordinate interchange gives the dual statement. ∎

## 5. Revised mixed-fan target

A fully recycled mixed singleton blocker is therefore not an arbitrary set of
`t-1` lines.  Apart from two shared-cell exceptions, it contains a linear
family whose two row deviations have one common projective ratio.  When the
source-slice gap is a unit, the witness intersections also lie in one target
column residue modulo `p`.

This is the natural input for a weighted common-ratio or aligned-carry
conversion.  The remaining theorem must attach current target load to this
ratio population and show that it opens an alternating bank, expands the
closure envelope, or consumes a bounded modular carry signature.

No all-`n` theorem is claimed here.  The exact factorization, degeneracies,
unit-residue counts, and ratio extraction are checked in
[`scripts/verify_prime_power_mixed_fan_ratios.py`](../scripts/verify_prime_power_mixed_fan_ratios.py).
