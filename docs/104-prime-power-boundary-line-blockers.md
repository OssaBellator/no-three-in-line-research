# Boundary geometry of candidate-only line blockers

The near-transversal argument CMR234--CMR236 pushes simultaneous line deletion
slightly beyond half the parent block.  A boundary count gives the essentially
sharp result: fewer than `t-2` nonaxis real lines can never block all parent
derangements.

## 1. Boundary points and diagonal exceptions

Let `A,C` be finite subsets of the real line with

\[
|A|=a\ge2,
\qquad
|C|=c\ge2.
\]

The boundary grid points of `A times C` are those with source coordinate equal
to `min A` or `max A`, or target coordinate equal to `min C` or `max C`.
There are exactly

\[
2a+2c-4
\]

such points.

### Theorem CMR240 — PROVED

Suppose nonvertical, nonhorizontal real lines cover every point of `A times C`
except possibly diagonal points

\[
(x,x),
\qquad x\in A\cap C.
\]

Then the number `q` of lines satisfies

\[
\boxed{q\ge a+c-3.}
\]

### Proof

At most one diagonal point lies on the union of the left and bottom sides of
the rectangle.  Indeed, if both `(min A,min A)` and `(min C,min C)` were grid
points and the two values were distinct, the smaller value would contradict
the minimality of the larger set's minimum.  The same argument at the maximum
shows that at most one diagonal point lies on the union of the right and top
sides.

Thus at most two boundary grid points may be omitted.  At least

\[
2a+2c-6
\]

boundary points must be covered.

A nonvertical, nonhorizontal line is not a supporting line of the axis-parallel
rectangle and meets its boundary in at most two points.  Hence `q` such lines
cover at most `2q` boundary points.  Therefore

\[
2q\ge2a+2c-6,
\]

which is the claimed inequality. ∎

The lower bound is independent of line multiplicities in the interior.

## 2. Simultaneous avoidance of `t-3` lines

Let

\[
G_t=K_{t,t}\setminus I
\]

be the parent derangement graph.

### Theorem CMR241 — PROVED

Let

\[
L_1,\ldots,L_q
\]

be distinct nonaxis real lines in the parent board, where

\[
q\le t-3.
\]

For every deleted set

\[
D\subseteq\bigcup_{i=1}^q E(L_i),
\]

the graph

\[
G_t-D
\]

has a perfect matching.

### Proof

Suppose the residual graph has no perfect matching.  Hall's theorem gives a
source set `A` with residual neighbourhood `N(A)` satisfying

\[
|N(A)|<|A|.
\]

Put

\[
C=[t]\setminus N(A).
\]

Then

\[
|A|+|C|>t.
\]

Every off-diagonal cell of `A times C` is absent from the residual graph.  The
old diagonal accounts for the permitted diagonal exceptions, while every other
cell must belong to `D` and hence to the union of the `q` real lines.

CMR240 therefore gives

\[
q\ge |A|+|C|-3\ge t-2,
\]

contradicting `q\le t-3`. ∎

Unlike CMR228 and CMR235, this theorem does not assume that the residual graph
already has a perfect matching.  Matchability follows directly.

## 3. The candidate-only endpoint is `t-2` lines

### Theorem CMR242 — PROVED

Let an inherited parent block of size `t\ge5` lie in a globally minimal
positive-potential saturated state.  At least one of the following holds.

1. Some residual parent state is covered by a rank-one or rank-two certificate,
   giving an executable anchored alternating continuation by CMR201.
2. There are
   
   \[
   t-2
   \]
   
   distinct candidate-only real-line signatures
   
   \[
   L_1,\ldots,L_{t-2},
   \]
   
   and one parent derangement avoids every candidate cell on
   
   \[
   L_1,\ldots,L_{t-3}.
   \]

### Proof

Start with the complete derangement graph.  Choose one residual perfect
matching.  Because its old diagonal is absent, it destroys the designated old
target endpoint.  Global minimality forces a new covering certificate.

If the certificate has rank one or two, the first alternative holds.  Otherwise
it is a candidate-only triple on a nonaxis real line `L_1`.  Delete all cells of
`E(L_1)`.

Repeat.  After `j\le t-3` distinct lines have been deleted, CMR241 guarantees a
residual perfect matching.  Every later candidate-only certificate uses a new
line because no cell from an earlier line remains.

After deleting `L_1,...,L_{t-3}`, choose a residual perfect matching.  Its
covering certificate is either anchored or supplies the distinct line
`L_{t-2}`. ∎

This supersedes the quantitative line counts in CMR230 and CMR236.  Those
results remain valid but are no longer the strongest simultaneous-avoidance
statements.

## 4. Rigidity at equality

### Corollary CMR243 — PROVED

Suppose exactly `t-2` nonaxis real lines block every parent derangement.  Then
there is a Hall rectangle `A times C` satisfying

\[
|A|+|C|=t+1
\]

such that:

1. exactly two of its boundary grid points are old diagonal exceptions;
2. every other boundary grid point lies on the blocking lines;
3. every blocking line meets the rectangle boundary in exactly two points;
4. the blocking lines partition the non-diagonal boundary points into pairs.

### Proof

The Hall rectangle in the proof of CMR241 satisfies

\[
t+1\le |A|+|C|\le q+3=t+1,
\]

so equality holds.  The boundary proof of CMR240 also has equality throughout:
there are exactly `2t-4=2q` required boundary points and each of the `q` lines
can cover at most two.  Hence there are exactly two diagonal boundary
exceptions, no required boundary point is multiply counted, and every line has
two boundary intersections. ∎

The remaining candidate-only obstruction is therefore not a diffuse signature
population.  It is an equality-case boundary factorization by exactly `t-2`
nonaxis lines.

## 5. Revised fixed-envelope target

The internal no-return theorem has been reduced to the equality case CMR243:

- anchored rank-one or rank-two certificates are executable;
- every family of at most `t-3` candidate-only line signatures is avoidable by
  a complete parent permutation;
- a frozen candidate-only cover must contain a rigid `t-2`-line boundary
  factorization of one Hall rectangle.

The next proof should classify or absorb these boundary pairings, or show that
their primitive-height/carry signatures force strict envelope expansion.

No all-`n` theorem is claimed here.  Boundary-exception counts and exhaustive
small parent boards are checked in
[`scripts/verify_prime_power_boundary_line_blockers.py`](../scripts/verify_prime_power_boundary_line_blockers.py).
