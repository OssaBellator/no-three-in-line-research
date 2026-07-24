# Off-diagonal reservoir obstruction

The row-lift construction is viable only when the retained ambient geometry
spreads the old reservoir coordinates. A tempting isolated-block version is
impossible for an elementary reason.

## 1. Two aligned off-diagonal blocks

Let

\[
I=\{a+1,\ldots,a+t\},
\qquad
J=\{a+t+1,\ldots,a+2t\}.
\]

Consider a replacement set supported in the two off-diagonal blocks

\[
(I\times J)\cup(J\times I).
\]

This is the support produced when an aligned contiguous `t x t` reservoir is
deleted and its row and column deficits are filled only by moving old columns
to the `t` new rows and moving old rows to the `t` new columns.

### Proposition PP3s -- PROVED

Every set of `4t` distinct points contained in

\[
(I\times J)\cup(J\times I)
\]

contains three collinear points. In fact, three points lie on one line of slope
`-1`.

#### Proof

For every point `(x,y)` in either off-diagonal block,

\[
2a+t+2\le x+y\le2a+3t.
\]

There are exactly

\[
(2a+3t)-(2a+t+2)+1=2t-1
\]

possible integer values of `x+y`. Each value is one line of slope `-1`. If no
such line contained three points, the union of all `2t-1` lines would contain at
most

\[
2(2t-1)=4t-2
\]

points, contradicting the assumed `4t` points. ∎

The statement uses neither saturation nor the internal construction of the
points; support and cardinality alone force the triple.

### Corollary PP3t -- PROVED

An aligned contiguous `t x t` reservoir containing `2t` old points cannot be
replaced by a width-`t` patch supported only in its two old/new off-diagonal
rectangles. Any saturation-preserving replacement has `4t` inserted points and
therefore contains a slope-`-1` triple by PP3s.

In particular, deleting an entire solved `[t]^2` configuration and applying the
full row-lift construction can never produce a no-three-in-line configuration
on `[2t]^2`.

### Candidate design PP3-R4 -- REFUTED

The following recursive block-doubling design is impossible:

1. take a saturated no-three configuration on an aligned `t x t` block;
2. delete all `2t` points;
3. refill only the two off-diagonal `t x t` blocks to obtain side `2t`.

The obstruction is independent of the chosen permutations or absorber states.

## 2. Projection-dispersion requirement

Let `Y` be the `t` old reservoir rows, let `C` be the set of old columns hit by
the deleted points, and let

\[
N=\{m+1,\ldots,m+t\}
\]

be the new coordinate interval. Every row-lift state is contained in

\[
U=(C\times N)\cup(N\times Y).
\]

For a primitive nonaxis integer functional

\[
\lambda_{a,b}(x,y)=ax+by,
\qquad ab\ne0,\quad\gcd(a,b)=1,
\]

its level sets are parallel lattice lines.

### Proposition PP3u -- PROVED

If a row-lift state `A subseteq U` has `|A|=4t` and is no-three-in-line, then
for every primitive nonaxis pair `(a,b)`,

\[
\boxed{
|\lambda_{a,b}(U)|
=
|(aC+bN)\cup(aN+bY)|
\ge2t.
}
\]

#### Proof

Every level set of `lambda_{a,b}` contains at most two points of `A`. Hence

\[
4t=|A|\le2|\lambda_{a,b}(A)|
\le2|\lambda_{a,b}(U)|.
\]

Divide by two. ∎

Thus projection dispersion is a necessary support-level test that can be run
before any local-lemma or state search.

## 3. Classification of the minimal projection failure

We use the elementary equality case of the integer sumset bound:
for finite integer sets `A,B` with at least two elements,

\[
|A+B|\ge|A|+|B|-1,
\]

with equality only when `A` and `B` are arithmetic progressions with the same
common difference.

Every deleted column contains at most two reservoir points, so `|C|>=t`.

### Proposition PP3v -- PROVED

Assume `t>=2`. If for some primitive nonaxis `(a,b)` one has

\[
|(aC+bN)\cup(aN+bY)|\le2t-1,
\]

then all of the following hold:

1. `|C|=t`;
2. `|a|=|b|=1`;
3. `C` and `Y` are intervals of length `t`;
4. the two component image intervals coincide.

For a reservoir contained in `[m]` and the adjacent new interval
`N={m+1,...,m+t}`, the only possible case is `a=b` and `C=Y`. Equivalently,
the support is the aligned configuration from PP3s and the forcing lines have
slope `-1`.

#### Proof

Both component images satisfy the integer sumset bound:

\[
|aC+bN|\ge|C|+t-1\ge2t-1,
\]

and

\[
|aN+bY|\ge2t-1.
\]

If their union has at most `2t-1` elements, both inequalities are equalities,
`|C|=t`, and the two image sets coincide.

Equality in the first sumset bound says that `aC` and `bN` are arithmetic
progressions with one common difference. Since `bN` has common difference
`|b|`, the progression `aC` must have the same difference. Coprimality of
`a,b` then forces `|a|=1`, and `C` is an interval. Applying the same argument
to `aN+bY` forces `|b|=1` and makes `Y` an interval.

It remains to compare the two image intervals. When `a=b`, equality is
`C+N=N+Y`, hence `C=Y`. When `a=-b`, equality would require the centre of
`C-N` to equal the centre of `N-Y`. But every element of `C` and `Y` is at
most `m`, whereas every element of `N` is at least `m+1`; the two centres have
opposite signs after translation and cannot agree. Changing both signs does
not change the level-set family. Therefore only `a=b` and `C=Y` remain. ∎

PP3v shows that the slope-`-1` obstruction is the unique primitive-direction
failure at the absolute `2t-1` projection threshold. Other row-lift placements
are not automatically valid, but they pass this first support-level
pigeonhole screen.

## 4. Consequence for reservoir placement

The general row-lift theorem PP3i is not refuted. Its old reservoir rows and
hit columns may be distributed throughout a much larger `[m]^2` core. Then the
linear projections of the two cross rectangles can occupy many more than
`2t-1` levels.

A viable PP3 preparation theorem must therefore use at least one of the
following:

- geometrically dispersed old reservoir rows or columns;
- a staggered row interval and column interval rather than one aligned square;
- old-old replacement cells or new-new corner cells outside the two cross
  rectangles;
- a different trade whose support is not confined to two aligned off-diagonal
  blocks.

This is a placement obstruction, not merely a failure of the unpruned
permutation bank.