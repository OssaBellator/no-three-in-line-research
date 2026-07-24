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

## 2. Consequence for reservoir placement

The general row-lift theorem PP3i is not refuted. Its old reservoir rows and
hit columns may be distributed throughout a much larger `[m]^2` core. Then the
sum coordinates of the two cross rectangles can occupy far more than `2t-1`
levels.

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