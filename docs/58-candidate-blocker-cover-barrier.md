# Candidate blocker covers and the product-measure barrier

This constant-width side analysis follows PP3es and continues at PP3et.

The random partition formulas close the distribution of source edges among
blocks.  This chapter examines one candidate patch cell at a time.  Its source
blocker pairs form a matching.  The controller deletion clears one automatic
axis blocker, but every additional blocker requires another deletion from the
same matching layer.  At prime-gap scale those additional deletions are too rare
for an unstructured product measure.

## 1. The automatic axis blocker

Let `S subseteq [m]^2` be saturated and no-three-in-line, and decompose it into
perfect matching layers

\[
 S=P\mathbin{\dot\cup}P'.
\]

Let `e in P` control a width-two candidate cell `z`.

- If `z=(x,a)` is a movement cell and `e=(x,y)`, the two source points in old
  column `x` form a blocker pair through `z`.
- If `z=(a,y)` is a refill cell, the two source points in old row `y` form the
  analogous blocker pair.

Exactly one point of this pair is `e`; the other lies in `P'`.  Selecting `z`
forces `e` to be deleted, so this axis blocker is automatically cleared.

Let `B^+(z)` be the remaining source blocker pairs through `z`.
Because `S` is no-three-in-line, all blocker pairs through an external point form
an endpoint-disjoint matching.

## 2. Exact matching-layer blocker profile

For `z`, write:

- `a(z)` for the number of pairs in `B^+(z)` with exactly one endpoint in `P`;
- `b(z)` for the number with both endpoints in `P`;
- `c(z)` for the number with no endpoint in `P`.

### Proposition PP3et -- PROVED

Any extension whose source deletions are contained in `P` and which selects `z`
requires `c(z)=0`.

In the random `K`-block experiment of PP3ep, put `d=4K`.  Conditional on
selecting the prescribed candidate cell `z`, the probability that the complete
deletion union covers every source blocker pair through `z` is zero when
`c(z)>0`.  When `c(z)=0`, it is exactly

\[
\boxed{
 C_z=
 \frac{
 \displaystyle
 \sum_{j=0}^{b(z)}(-1)^j\binom{b(z)}j
 \binom{m-1-a(z)-2j}{d-1-a(z)}
 }{
 \binom{m-1}{d-1}
 }.
}
\]

As usual, an impossible binomial coefficient is interpreted as zero.

#### Proof

The automatic axis pair is covered by the controller edge `e`.  Every
additional pair is disjoint from it and from all other blocker pairs.

A pair counted by `c(z)` has no deletable endpoint, proving the first assertion.
Assume `c(z)=0`.  By PP3ep, conditional on selecting `z`, the remaining deletion
set is a uniform `(d-1)`-subset of the `m-1` noncontroller edges of `P`.

All `a(z)` unique layer endpoints must be included.  After forcing them, each of
the `b(z)` disjoint two-endpoint pairs must be hit.  Inclusion-exclusion over the
pairs that are completely missed gives the displayed numerator. ∎

For one additional blocker pair, this gives

\[
 C_z=
 \frac{d-1}{m-1}
\]

when it has one layer endpoint, and

\[
 C_z=
 \frac{2(d-1)}{m-1}
 -
 \frac{(d-1)(d-2)}{(m-1)(m-2)}
\]

when both endpoints lie in `P`.

## 3. Uniform upper bound for nontrivial candidates

### Corollary PP3eu -- PROVED

If `B^+(z)` is nonempty, then

\[
 \boxed{
 C_z\le
 \min\left\{1,\frac{2(d-1)}{m-1}\right\}.
 }
\]

#### Proof

Covering all additional blockers implies covering any one of them.  A one-layer-
endpoint pair is hit with probability `(d-1)/(m-1)`.  A two-layer-endpoint pair
is hit with probability at most twice that by the union bound. ∎

At the prime-gap block scale `d=4K=m^{0.525+o(1)}` this is

\[
 C_z=O(m^{-0.475})
\]

for every candidate with even one additional blocker.

Call a candidate **axis-clean** if `B^+(z)` is empty.  Then `C_z=1`.

## 4. Exact expected unsafe-cell count

Expose every labelled candidate entry before choosing the random partition.  A
prescribed movement or refill cell is selected with probability exactly `2/m`
in the unconditioned full 36-state experiment.

Let `mathcal U` be the labelled candidate entries and define

\[
 X=\#\{z\in\mathcal U:z\text{ is selected and some source blocker survives}\}.
\]

### Proposition PP3ev -- PROVED

One has the exact identity

\[
 \boxed{
 \mathbb E X
 =
 \frac2m\sum_{z\in\mathcal U}(1-C_z).
 }
\]

If `A` entries are axis-clean, then

\[
 \mathbb E X
 \ge
 \frac{2(|\mathcal U|-A)}m
 \left(1-\min\left\{1,\frac{2(d-1)}{m-1}\right\}\right).
\]

#### Proof

Conditional on selecting `z`, the probability that no retained-pair blocker
survives is exactly `C_z` by PP3et.  Multiply by the selection probability
`2/m` and sum.  The second inequality uses PP3eu for every non-axis-clean entry.
∎

There are `4Km` labelled candidate entries and exactly `8K` selected patch
points in every complete state.  If only an `o(1)` fraction of the candidate
entries is axis-clean and `K=o(m)`, then

\[
 \mathbb E X=(8-o(1))K.
\]

Thus a first-moment argument on the unstructured product measure cannot remove
retained-pair blockers: it expects almost every selected patch point to be
unsafe.

## 5. Consequence for the remaining route

### Corollary PP3ew -- PROVED

At prime-gap scale, random equipartition plus independent uniform full-bank state
choices can yield `E X<1` only if all but `O(m)` of the `4Km` labelled candidate
entries are axis-clean, up to lower-order terms.

Equivalently, the non-axis-clean fraction must be `O(1/K)`.

This is a barrier for the product measure, not an impossibility theorem for the
matching-block architecture.  A successful construction must introduce one of
the following correlations:

1. prune almost all non-axis-clean candidate cells while retaining equal-margin
   state domains;
2. choose deletion patterns specifically to cover the blocker matchings of the
   selected cells;
3. use protected trades to remove the surviving blocker endpoints;
4. replace width-two support by endpoint-adapted cells with predominantly
   axis-clean secant profiles.

The remaining geometric target is therefore stronger and more concrete than a
global count of blocker signatures: build large equal-margin state families in
which selected cells and source blocker covers are correlated.