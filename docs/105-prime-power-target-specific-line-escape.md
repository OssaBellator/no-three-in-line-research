# Target-specific parent escape and the `t-1` line endpoint

The full derangement parent bank forbids every old diagonal cell. A terminal
four-core escape needs less: to destroy one selected old triple, it is enough to
move one designated endpoint. Allowing the other parent cells to remain fixed
raises the candidate-only line-blocker threshold by one and removes the equality
case CMR243.

Fix a parent board of size `t`, and let `z_*` be the old cell of the designated
target endpoint. The target-specific host is

\[
K_{t,t}\setminus\{z_*\}.
\]

In a nonroot envelope the opposite-layer row fibre is disjoint, so every perfect
matching of this host preserves layer disjointness and removes `z_*`.

For a real line `L`, write

\[
E_*(L)
=
\{\text{all parent-board cells on }L\}\setminus\{z_*\}.
\]

Unlike the full derangement notation `E(L)`, this set includes old diagonal
cells other than `z_*`, because those cells are available in the target-specific
host.

## 1. One-exception Cartesian covering

### Theorem CMR244 — PROVED

Let `A,C` be nonempty finite real coordinate sets of sizes `a,c`. If
nonvertical, nonhorizontal real lines cover every point of

\[
A\times C
\]

except possibly one arbitrary point, then the number `q` of lines satisfies

\[
\boxed{q\ge a+c-2.}
\]

### Proof

First suppose `a=1`. Every nonvertical line meets the unique vertical slice
`A times C` in at most one point. At least `c-1` points must be covered, so

\[
q\ge c-1=a+c-2.
\]

The case `c=1` is symmetric.

Now assume `a,c>=2`. The rectangle boundary contains exactly

\[
2a+2c-4
\]

grid points. At most one is exceptional, so at least

\[
2a+2c-5
\]

boundary points must be covered. Every nonaxis line meets the rectangle boundary
in at most two points. Hence

\[
2q\ge2a+2c-5.
\]

The left side is even, so

\[
2q\ge2a+2c-4,
\]

which gives the result. ∎

## 2. Avoiding `t-2` lines while moving one target

### Theorem CMR245 — PROVED

Let `L_1,...,L_q` be distinct nonaxis real lines in a parent board of size `t`,
where

\[
q\le t-2.
\]

For every

\[
D\subseteq\bigcup_{i=1}^q E_*(L_i),
\]

the graph

\[
K_{t,t}\setminus(\{z_*\}\cup D)
\]

has a perfect matching.

### Proof

Suppose no perfect matching exists. Hall's theorem gives a source set `A` whose
residual neighbourhood has size below `|A|`. Let `C` be the complement of that
neighbourhood. Then

\[
|A|+|C|>t.
\]

Every cell of `A times C` is absent from the residual host. At most the one cell
`z_*` is unavailable independently of the line family; every other absent cell
belongs to `D` and is covered by the `q` nonaxis lines.

CMR244 gives

\[
q\ge |A|+|C|-2\ge t-1,
\]

contradicting `q\le t-2`. ∎

This theorem is parity-free and does not require a pre-existing residual perfect
matching.

## 3. Frozen target-specific extraction

### Theorem CMR246 — PROVED

Let an inherited parent block of size `t>=4` lie in a globally minimal
positive-potential saturated state, and fix one designated endpoint `z_*` of a
selected old triple. At least one of the following holds.

1. A target-specific parent state is covered by a rank-one or rank-two
   certificate, yielding an executable anchored alternating continuation by
   CMR201.
2. There are

   \[
   t-1
   \]

   distinct candidate-only real-line signatures

   \[
   L_1,\ldots,L_{t-1},
   \]

   and one target-specific parent permutation avoids every available candidate
   cell on

   \[
   L_1,\ldots,L_{t-2}.
   \]

### Proof

Choose a perfect matching of the target-specific host. It omits `z_*`, so the
selected old triple is destroyed. Global minimality forces at least one new
covering certificate.

If the certificate has rank one or two, the first alternative holds. Otherwise
it is a candidate-only triple on a nonaxis real line `L_1`. Delete all available
cells `E_*(L_1)` and repeat.

After deleting any `j<=t-2` distinct candidate-only line sets, CMR245 supplies
another target-specific perfect matching. Every later candidate-only certificate
lies on a new line because no available cell of any previous line remains.

After the first `t-2` lines have been deleted, choose one residual perfect
matching. Its required certificate is anchored or supplies the distinct line
`L_{t-1}`. ∎

CMR246 supersedes the one-layer candidate-only counts in CMR230, CMR236, and
CMR242 whenever only one designated target endpoint must be removed.

## 4. Rigidity of a sharp target-specific blocker

### Corollary CMR247 — PROVED

Suppose exactly `t-1` nonaxis real lines block every target-specific parent
matching when all their available cells `E_*(L)` are deleted. Then there is a
Hall rectangle

\[
A\times C
\]

with

\[
|A|+|C|=t+1.
\]

Exactly one of the following geometric descriptions applies.

1. **Singleton fan.** If `|A|=1` or `|C|=1`, the exceptional target cell `z_*`
   belongs to `A times C`. Every one of the other `t-1` cells of that source row
   or target column is covered, and each blocking line meets the singleton slice
   in exactly one of those cells.
2. **Nontrivial boundary factor.** If `|A|,|C|>=2`, all boundary points except
   possibly `z_*` are covered. The total boundary-incidence slack is at most one:
   - if `z_*` is not a boundary point, every line meets the boundary twice and
     the lines partition all boundary points;
   - if `z_*` is a boundary point, at most one boundary incidence is repeated or
     missing from a two-point-per-line partition.

### Proof

The Hall rectangle satisfies

\[
t+1\le |A|+|C|\le q+2=t+1,
\]

so equality holds.

Suppose `|A|=1`; the other singleton case is symmetric. Then `|C|=t`. If `z_*`
did not belong to `A times C`, all `t` cells of the slice would have to be
covered, but each nonvertical line meets it at most once and only `t-1` lines
are available. Hence `z_*` lies on the slice. The other `t-1` cells must all be
covered, and equality forces every line to cover exactly one of them. This is
the singleton fan.

Now assume both sides have size at least two. The boundary has `2t-2` points. If
`z_*` is interior or outside the rectangle, all `2t-2` boundary points must be
covered by `t-1` lines, each meeting the boundary at most twice; equality holds
throughout. If `z_*` lies on the boundary, `2t-3` required boundary points are
covered with capacity `2t-2`, leaving total slack one. ∎

## 5. Revised terminal line obstruction

The candidate-only line endpoint for one selected target is now the sharp
`t-1` case. Every smaller line family is avoidable by a complete parent
permutation which moves the target endpoint.

A complete inherited escape theorem may therefore focus on either the singleton
fan or the nontrivial CMR247 boundary factor, or choose different endpoints of
the same old triple and show that their sharp blockers cannot coexist compatibly
with the prefix and carry ancestry.

No all-`n` theorem is claimed here. One-exception Cartesian counts and exhaustive
small target-specific hosts are checked in
[`scripts/verify_prime_power_target_specific_lines.py`](../scripts/verify_prime_power_target_specific_lines.py).
