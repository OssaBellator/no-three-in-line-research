# Protected growth has a finite branch-wide owner-labelled capacity

CMR1034--CMR1069 bound protected growth inside one monotone owner execution.
Structural descent may change factor, routing, wall, or envelope owners and start
a new local protected matching. This chapter aggregates those local capacities
using the finite owner-routing stock CMR691--CMR697, the complete unit-wall tree
bound CMR741--CMR747, and the closure-envelope chain.

The policy is canonical: inside one owner-routing stage, each layer keeps one
monotone protected matching and never resets it. A reset is charged only when the
structural owner changes. If a routing-support edge reaches the recurrent branch,
that paid endpoint is recorded instead of continuing the nonrecurrent count.

Fix an ambient parent side

\[
N=p^h
\]

and a routing recurrence threshold `lambda>=2`. Recall

\[
H_m=2m^2+m+1,
\qquad
R_m(\lambda)
=
\left\lfloor\frac{(\lambda-1)m^2}{2}\right\rfloor.
\]

## 1. Protected capacity at one owner stage

### Theorem CMR1086 -- PROVED

At one owner-routing stage of factor side `m`, the two monotone protected
matchings together can acquire at most

\[
\boxed{2m}
\]

fresh protected edges.

### Proof

Each layer protected matching has size at most `m`. Protected execution only adds
new edges inside the stage. ∎

Initial protected edges only reduce the remaining capacity.

## 2. One strict descent path

Define

\[
\mathcal P(d,\lambda)
=
\sum_{m=1}^{d}
2mH_m\bigl(1+R_m(\lambda)\bigr).
\]

### Theorem CMR1087 -- PROVED

Along one selected strict factor-descent path beginning at side `d`, either one
physical routing-support edge recurs `lambda` times at one owner or the total
owner-labelled protected growth is at most

\[
\boxed{
\mathcal P(d,\lambda)
=
\sum_{m=1}^{d}
2m(2m^2+m+1)
\left(
1+\left\lfloor\frac{(\lambda-1)m^2}{2}\right\rfloor
\right).
}
\]

### Proof

At side `m`, CMR691 gives at most `H_m` static host stages and CMR692 gives at
most `1+R_m(lambda)` routing epochs per stage in the nonrecurrent branch. Apply
CMR1086 to every resulting owner stage and sum over the strictly decreasing side
path. ∎

For fixed `lambda`, this is polynomial of degree six in `d`.

## 3. Complete unit-wall tree

### Theorem CMR1088 -- PROVED

One unit-wall factor tree rooted at side at most `N` has at most `2N+1` nodes.
Therefore, unless a routing-support edge reaches its recurrent branch, the total
protected growth over the complete wall tree is at most

\[
\boxed{(2N+1)\mathcal P(N,\lambda).}
\]

### Proof

Use CMR742 for the node count and apply the coarse full-side path bound CMR1087
to every node. This deliberately overcounts smaller child sides. ∎

## 4. Closure-envelope chain

Define the global owner-labelled capacity

\[
\boxed{
\mathfrak P(N,h,\lambda)
=
(h+1)(2N+1)\mathcal P(N,\lambda).
}
\]

### Theorem CMR1089 -- PROVED

Across one complete closure branch, either one physical routing-support edge
recurs `lambda` times at one owner or all fresh protected growth across every
envelope epoch, wall node, factor path, host stage, and routing epoch is at most

\[
\boxed{\mathfrak P(N,h,\lambda).}
\]

### Proof

There are at most `h+1` closure-envelope epochs. Apply CMR1088 in each epoch. ∎

Owner relabelling does not duplicate a physical restoration, but this theorem is
an owner-labelled capacity upper bound and intentionally permits the same
absolute cell to be protected at different structural owners.

## 5. Globally large-growth episodes are finite

### Theorem CMR1090 -- PROVED

Fix `G_0>=1`. In the nonrecurrent-routing branch, the number of robust episodes
which add at least `G_0` fresh protected edges is at most

\[
\boxed{
\left\lfloor
\frac{\mathfrak P(N,h,\lambda)}{G_0}
\right\rfloor.
}
\]

### Proof

All such gains are nonnegative and their branch-wide sum is bounded by CMR1089. ∎

This includes common-layer stars, cross-layer one-side absorption, entering-pair
line absorption, and loaded-old-line absorption.

## 6. Arbitrary positive-growth episodes

### Theorem CMR1091 -- PROVED

In the nonrecurrent-routing branch, the total number of robust episodes with any
positive protected growth is at most

\[
\boxed{\mathfrak P(N,h,\lambda).}
\]

### Proof

Every positive-growth episode adds at least one protected edge and apply CMR1089. ∎

Thus owner changes cannot restart positive growth indefinitely.

## 7. Zero-growth episodes have structural output

### Theorem CMR1092 -- PROVED

After the finite positive-growth budget is exhausted, every further robust
episode reaches at least one of:

1. large protected core and selected-skeleton minimum descent CMR1038--CMR1045;
2. loaded old target line and the absorption/descent alternatives CMR1046--CMR1053;
3. simultaneous common-layer or cross-layer star large-core output
   CMR1054--CMR1069;
4. same-value target-cell cut, rollback, added-edge contraction, lost-minimum
   ancestry, factor/wall descent, envelope expansion, or strict improvement;
5. one routing-support edge recurring `lambda` times at one owner.

### Proof

Use the zero-growth alternatives CMR1036, CMR1050, CMR1057, and CMR1066, together
with the complete host-transition normalization. ∎

## 8. Global protected-capacity endpoint

### Corollary CMR1093 -- PROVED

Protected-growth reset is not an unbounded branch-wide obstruction. Every closure
branch has the explicit global capacity `mathfrak P(N,h,lambda)` unless a physical
routing-support edge has already entered the recurrent paid endpoint.

Consequently an unbounded robust-target history must eventually concentrate in
large-core product descent, loaded-line or target-cell recurrence, loss/restoration
ancestry, recurrent routing support, envelope expansion, or strict potential
improvement. Repeatedly creating fresh local protected matchings is no longer an
available escape.

### Proof

Combine CMR1086--CMR1092. ∎

No all-`n` theorem is claimed. Owner-stage counts, polynomial capacity,
wall/envelope aggregation, and episode bounds are checked in
[`scripts/verify_prime_power_global_protected_capacity.py`](../scripts/verify_prime_power_global_protected_capacity.py).
