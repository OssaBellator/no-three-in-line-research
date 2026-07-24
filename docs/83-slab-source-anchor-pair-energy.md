# Ordinary source-anchor pair energy at the slab scale

After fully safe one-slot pruning PP3ge, every remaining source-containing
certificate uses two distinct slots and one retained source anchor.  At the
slab-optimal parameters PP3gr, these ordinary anchor-pair events also have
summable incident mass.

The proof uses three facts.

1. Every old column and old row contains exactly two source points.
2. Movement coordinates in one pool lie in an interval of length `R`.
3. The mixed movement/refill anchor equation is multiplicative.

Deleting some proposed anchors can only reduce the event family, so throughout
we count against the full saturated source `S`.

## 1. A congruence sum

For positive integers `d,X`, define

\[
 G(d,X)=\sum_{h=1}^X\frac{\gcd(h,d)}h.
\]

### Lemma PP3hg -- PROVED

One has

\[
 \boxed{
 G(d,X)\le \tau(d)(1+\log X).
 }
\]

#### Proof

Use

\[
 \gcd(h,d)=\sum_{q\mid\gcd(h,d)}\varphi(q).
\]

Then

\[
 G(d,X)
 =
 \sum_{q\mid d}\frac{\varphi(q)}q
 \sum_{k\le X/q}\frac1k
 \le
 (1+\log X)
 \sum_{q\mid d}\frac{\varphi(q)}q.
\]

Every summand in the last divisor sum is at most one, so the sum is at most
`tau(d)`. ∎

## 2. Movement--movement anchor pairs

Fix two slots with movement rows `A,A'`, and write

\[
 d=|A'-A|.
\]

If `d=0`, their movement pair is horizontal above the old grid and has no old
anchor.  Assume `d>0`.

### Proposition PP3hh -- PROVED

The number of source-edge value pairs whose two movement points lie on a line
through at least one point of the saturated source is at most

\[
 \boxed{
 2R\tau(d)(1+\log(m+T))+2m.
 }
\]

Consequently the grouped event probability is at most

\[
 O_\gamma\left(
 \frac{\tau(d)\log(m+T)}R+rac m{R^2}
 \right).
\]

#### Proof

Let the anchor be `p=(u,v)` and the movement points be

\[
 (x,A),\qquad (x',A').
\]

Put

\[
 h=A-v>0.
\]

Collinearity gives, up to signs,

\[
 h(x'-x)=d(u-x).
\]

For fixed `p`, an admissible `x` must satisfy

\[
 h\mid d(u-x).
\]

Writing `g=gcd(h,d)`, this is equivalent to one residue class modulo `h/g`.
Inside an interval of length `R`, there are at most

\[
 \frac{Rg}{h}+1
\]

such `x`.  Once `x` is fixed, the equation determines `x'`; the perfect
matching layer has at most one source edge in each old column.

Every old row contains exactly two source anchors.  As `v` ranges over the old
rows, `h=A-v` ranges over an interval contained in `[1,m+T]`.  Summing the
preceding bound and using PP3hg gives

\[
 2R\tau(d)(1+\log(m+T))+2m.
\]

Grouping anchors can only decrease the count.  Divide by the two slot-domain
sizes, each at least `gamma R`. ∎

## 3. Refill--refill anchor pairs

Fix two slots with distinct refill columns `B,B'`, and put

\[
 d=|B'-B|.
\]

### Proposition PP3hi -- PROVED

The number of source-edge value pairs whose two refill points lie on a line
through at least one source anchor is at most

\[
 \boxed{
 2m\tau(d)(1+\log(m+T))+2m.
 }
\]

Consequently the grouped event probability is at most

\[
 O_\gamma\left(
 \frac{m\tau(d)\log(m+T)}{R^2}
 +
 \frac m{R^2}
 \right).
\]

#### Proof

Write the anchor as `p=(u,v)` and the two refill points as

\[
 (B,y),\qquad (B',y').
\]

Put

\[
 h=B-u>0.
\]

Collinearity gives

\[
 h(y'-y)=d(v-y)
\]

up to signs.  For fixed `p`, the admissible `y` values occupy one residue class
modulo `h/gcd(h,d)`.  The slot's row-coordinate domain is an arbitrary subset
of `[m]`, so it contains at most

\[
 \frac{m\gcd(h,d)}h+1
\]

such values.  Once `y` is fixed, `y'` is determined, and the matching layer has
at most one source edge in each old row.

Every old column contains exactly two source anchors.  Sum over `u`, use
PP3hg, and divide by the two domain sizes. ∎

## 4. Movement--refill anchor pairs

Fix distinct slots with movement row `A` and refill column `B`.  Let their
selected source-edge values have old coordinates `x` and `y`, respectively.
For an anchor `p=(u,v)`, collinearity is exactly

\[
 \boxed{
 (x-u)(y-v)=(A-v)(B-u).
 }
\]

This is the PP3dv product identity without requiring the movement and refill
points to be controlled by the same source edge.

We use the elementary divisor-square estimate

\[
 \sum_{n\le X}\tau(n)^2
 \le
 X(1+\log X)^3.
\]

Indeed `tau(n)^2<=d_4(n)`, and summing the ordered factorisations
`abcd=n` gives the displayed bound by three harmonic sums.

### Proposition PP3hj -- PROVED

The number of source-edge value pairs whose movement/refill points lie on a
line through at least one source anchor is at most

\[
 \boxed{
 4(m+T)(1+\log(m+T))^3.
 }
\]

Consequently the grouped event probability is at most

\[
 O_\gamma\left(
 \frac{m\log^3(m+T)}{R^2}
 \right).
\]

#### Proof

For one anchor `p`, every solution `(x,y)` gives a signed factor pair of

\[
 N_p=(A-v)(B-u).
\]

Hence there are at most `2tau(N_p)` coordinate pairs, and matching uniqueness
turns each coordinate pair into at most one pair of source-edge values.

Use

\[
 \tau(N_p)\le\tau(A-v)\tau(B-u).
\]

By Cauchy--Schwarz and saturation,

\[
 \begin{aligned}
 \sum_{p\in S}\tau(A-v_p)\tau(B-u_p)
 &\le
 \left(
 2\sum_{v=1}^m\tau(A-v)^2
 \right)^{1/2}
 \\
 &\qquad\cdot
 \left(
 2\sum_{u=1}^m\tau(B-u)^2
 \right)^{1/2}.
 \end{aligned}
\]

Both difference intervals lie in `[1,m+T]`.  The divisor-square estimate bounds
each parenthesised sum by

\[
 2(m+T)(1+\log(m+T))^3.
\]

Multiplying by the signed-factor constant two gives the stated relation-size
bound.  Grouping duplicate anchor witnesses only improves it.  Divide by the
two domain sizes. ∎

The transpose orientation is identical.

## 5. Total ordinary anchor mass

Every new movement row and refill column is used by exactly two slots.  For a
fixed slot there are fewer than `2T` partner slots of each relevant type.
Also

\[
 \tau(d)\le2\sqrt d\le2\sqrt T.
\]

### Theorem PP3hk -- PROVED

At the slab-optimal parameters, the total grouped ordinary source-anchor pair
mass incident to every slot is

\[
 \boxed{o(1)}.
\]

More explicitly, it is bounded by

\[
 O_\gamma\left(
 \frac{T^{3/2}\log(m+T)}R
 +
 \frac{mT^{3/2}\log(m+T)}{R^2}
 +
 \frac{mT\log^3(m+T)}{R^2}
 +
 \frac{mT}{R^2}
 \right).
\]

At

\[
 T=m^{21/40+o(1)},
 \qquad
 R=m^{19/20+o(1)},
\]

these terms have powers respectively

\[
 m^{-13/80+o(1)},
 \quad
 m^{-9/80+o(1)},
 \quad
 m^{-3/8+o(1)},
 \quad
 m^{-3/8+o(1)}.
\]

#### Proof

Apply PP3hh to all movement partners, PP3hi to all refill partners, and PP3hj
to the two mixed orientations.  Use at most `O(T)` partners and the elementary
bound on `tau(d)`.  The exponent computations are direct. ∎

## 6. Conditional completion after global allocation

### Corollary PP3hl -- PROVED

Suppose the slab-optimal pools admit the saturation-compatible global refined
label allocation PP3fw with fully safe domains PP3ge.  Then all source-anchor
and patch-only external event mass is `o(1)` at every slot.

Consequently, for all sufficiently large `m`, the weighted endpoint PP3fk gives
a simultaneous saturated no-three patch of width

\[
 \Omega(m^{21/40}).
\]

#### Proof

The ordinary anchor mass is `o(1)` by PP3hk.  Patch-only cross-macro mass is
`o(1)` by PP3he.  Unary source classes were removed by the fully safe domains.
The sum is eventually below the positive residual PP3fj budget

\[
 \frac1{48}-o(1).
\]

Apply PP3fk. ∎

Thus the geometric completion-energy half of the prime-patching bottleneck is
closed.  The remaining asymptotic input is the global refined-label allocation:
construct the fully safe domains with the complementary-degree condition of
PP3gl, or resolve its explicit boundary-shadow and bad-label concentration
obstructions by protected trades.
