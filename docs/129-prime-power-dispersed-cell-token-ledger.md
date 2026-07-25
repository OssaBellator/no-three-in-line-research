# Dispersed thin carry cells have a finite prefix-token ledger

CMR303 separates a thin-signature population into a heavy carry cell or many
distinct carry cells.  CMR342 makes the heavy alternative executable.  The
dispersed alternative also has a finite static budget inside one inherited
parent block.  For one fixed projective direction, all row-prefix cells across
all depths form a geometric series of size `(t-1)/(p-1)`.  Therefore fresh
dispersion cannot continue indefinitely; a long closure must reuse one exact
prefix token.

Let

\[
t=p^h.
\]

Fix one normalized inherited parent block, one permutation layer, and one
projective direction

\[
\theta\in\mathbb P^1(\mathbb F_p).
\]

A **row-prefix direction token** is a triple

\[
\tau=(b,c,\theta),
\]

where

\[
0\le b<h,
\qquad
c\in\mathbb Z/p^b\mathbb Z.
\]

The column-prefix block and layer are fixed in this local ledger.  In absolute
coordinates, CMR297 adds the parent prefix depth to `b`.

## 1. Exact token count

### Theorem CMR344 — PROVED

The number of row-prefix direction tokens in one parent block for one fixed
projective direction is exactly

\[
\boxed{
Q_p(t)
=
\sum_{b=0}^{h-1}p^b
=
\frac{t-1}{p-1}.
}
\]

If all `p+1` projective directions are retained, the token count is

\[
\boxed{
(p+1)Q_p(t).
}
\]

### Proof

At depth `b`, the row-prefix residue has exactly `p^b` possibilities.  Sum the
geometric series.  The projective line has `p+1` directions. ∎

## 2. Fresh-dispersion packing

### Theorem CMR345 — PROVED

Let `E_1,...,E_J` be dispersed-cell episodes in the same parent block, layer,
and projective direction.  Suppose every episode uses at least `R` distinct
row-prefix tokens.  If the token sets are pairwise disjoint, then

\[
\boxed{
J
\le
\left\lfloor
\frac{Q_p(t)}{R}
\right\rfloor.
}
\]

Without the disjointness assumption, some exact token belongs to at least

\[
\boxed{
\operatorname{ceil}\left(
\frac{JR}{Q_p(t)}
\right)
}
\]

episodes.

### Proof

The first statement is ordinary packing into the `Q_p(t)` available tokens.
For the second, count episode-token incidences.  There are at least `JR`
incidences distributed among `Q_p(t)` tokens. ∎

## 3. Width-two and width-three bounds

### Corollary CMR346 — PROVED

For a width-two episode, CMR304 permits

\[
R_2
=
\frac{t-2}{(h+p-1)\sqrt t}.
\]

Consequently the number of pairwise token-disjoint width-two dispersion
episodes in one fixed direction is strictly below

\[
\boxed{
\frac{(h+p-1)(t-1)\sqrt t}{(p-1)(t-2)}.
}
\]

For width three with `t>=10`, the corresponding bound is strictly below

\[
\boxed{
\frac{(h+p-1)(t-1)\sqrt t}{(p-1)(t-9)}.
}
\]

For fixed prime base, both are

\[
O_p(\sqrt t\log t).
\]

### Proof

Insert the dispersed-cell lower bounds from CMR304 and CMR305 into CMR345 and
use the exact value of `Q_p(t)`.  The word “strictly” reflects that CMR303 gives
more than the displayed real-valued number of occupied cells. ∎

## 4. Absolute ownership and envelope changes

Inside one closure envelope epoch, attach the parent prefix depth, column
prefix, and layer to every token.  A repair strictly below the token depth
preserves its coarser row and column residues by CMR93 and CMR173.  Replacing
the parent envelope changes the absolute token namespace and is charged to the
at-most-`h` envelope-expansion budget of CMR174.

Thus every long dispersed closure has one of two explanations:

1. it consumes fresh tokens, whose number is bounded by CMR344--CMR346; or
2. it revisits one exact absolute token many times.

The second alternative is the remaining no-return problem.  The theorem needed
next is dynamic: show that repeated visits to one token create simultaneous
heavy-cell load, a monotone certificate-exchange ancestry, or a paid quotient
or carry defect.

No all-`n` theorem is claimed here.  Token counts, packing bounds, and temporal
pigeonhole estimates are checked in
[`scripts/verify_prime_power_dispersed_token_ledger.py`](../scripts/verify_prime_power_dispersed_token_ledger.py).
