# Converting paid geometry into alternating banks

CMR123--CMR128 compress a globally frozen alternating closure, but CMR125
originally treated two outcomes as paid terminal branches:

1. a vertex-disjoint family of real collinear triples;
2. a heavy real line in the outside set.

Both outcomes actually contain another executable alternating bank. Thus no
cross-node no-double-charge ledger is needed for these two geometric classes.
The bookkeeping must distinguish the **endpoint-board size** from the
**target load**, meaning the number of old triples guaranteed to disappear in
every bank state.

Throughout, a **saturated state** is the disjoint union of two permutation
layers on an `N` by `N` grid. An endpoint bank selects points from one fixed
layer, keeps their column and row sets, forbids their old cells and the cells
occupied by the other layer, and rematches the selected columns to the selected
rows.

## 1. Disjoint triples expose a same-layer endpoint bank

### Theorem CMR129 — PROVED

Let `Q_1,...,Q_q` be vertex-disjoint real collinear triples in a saturated
state. Then one permutation layer contains a chosen point from at least

\[
\left\lceil\frac q2\right\rceil
\]

of the triples, with all chosen points distinct.

More precisely, for every integer

\[
4\le r\le N
\]

such that

\[
r\ge \left\lceil\frac q2\right\rceil,
\]

there is an endpoint set `B` of size `r` in one permutation layer containing
one chosen point from at least `ceil(q/2)` of the triples. The degree-two
forbidden board on `B` has an allowed perfect matching. Every allowed state
moves all points of `B`, preserves saturation and layer disjointness, and
destroys all those chosen triples.

Thus a disjoint family of size `q` gives a bank with target load at least
`ceil(q/2)`. The board may be padded to any size `r` between that target load
and `N`, subject to `r>=4`.

### Proof

Every three-point set has at least two points in one of the two permutation
layers. Assign each triple to a layer in which it has at least two points. One
layer receives at least `ceil(q/2)` assigned triples. Choose one point in that
layer from each assigned triple.

The chosen points are distinct because the triples are vertex-disjoint. Points
in one permutation layer occupy distinct rows and distinct columns. If fewer
than `r` points were chosen, add arbitrary further points from the same layer
until the endpoint set has size `r`; this is possible because the layer has
exactly `N` points.

Forbid each endpoint's old cell and every selected-row/selected-column cell
occupied by the opposite layer. The forbidden board has row and column degree
at most two. CMR128 gives an allowed perfect matching for `r>=4`. Its old-cell
forbidden diagonal moves every selected endpoint. Therefore every chosen old
triple loses at least one of its cells. Saturation and disjointness are
preserved by the endpoint rematching. ∎

## 2. Heavy lines expose a same-layer secant star

### Theorem CMR130 — PROVED

Let `s>=4`, and suppose a real line `L` contains more than `2s` points of a
saturated state. Then `L` exposes an alternating endpoint bank of board size and
target load exactly `s`.

There are `s` points `B={b_1,...,b_s}` in one fixed permutation layer and two
further points `u,v` on `L`, outside `B`, such that every old triple

\[
\{b_i,u,v\}
\]

is destroyed in every state of the endpoint bank on `B`.

### Proof

A vertical line contains at most two selected points, so `L` is nonvertical.
Consequently all its selected points have distinct columns.

Since `L` contains at least `2s+1` points, one of the two permutation layers
contains at least `s+1` of them. Choose `s` of those points as `B`. At least
`s+1>=5` line points remain outside `B`, so choose two of them as `u,v`.

The points of `B` lie in one permutation layer and therefore have distinct rows
and columns. Apply CMR128 to their degree-two forbidden board. Every allowed
matching moves every `b_i`, so none of the old triples `{b_i,u,v}` survives.
The matching preserves the endpoint row and column sets and avoids the opposite
layer. ∎

The same conclusion holds when the heavy line lies entirely in the outside set
`X` of CMR124: its points may simply become the endpoint set of the next bank.

## 3. Geometry-to-bank conversion with target load

For an endpoint bank `B`, write `d(B)` for any certified number of old triples
which every bank state destroys. The board size and `d(B)` need not be equal.

### Corollary CMR131 — PROVED

Apply CMR124 with an integer `s>=4`. Each of its three geometric alternatives
produces another alternating endpoint bank:

1. the direct secant-star alternative gives board size `s` and target load `s`;
2. the `s` vertex-disjoint triples give, after CMR129 and padding, board size
   `s` and target load at least `ceil(s/2)`;
3. the heavy-line alternative gives, by CMR130, board size `s` and target load
   `s`.

Thus every geometric outcome has a next bank of board size exactly `s` and
certified target load at least `ceil(s/2)`.

### Proof

Only the disjoint-triple case needs explanation. CMR129 selects one point from
at least `ceil(s/2)` triples in one layer. Pad that endpoint set to exactly `s`
points in the same layer and apply CMR128. Every selected triple loses its
chosen point. The other two cases are the direct CMR124 bank and CMR130. ∎

### Corollary CMR132 — PROVED

Suppose a saturated state contains at least

\[
12(s-1)^2(3s-2)
\]

real triples touching a designated point set, with `s>=4`. Then it exposes an
alternating bank of board size `s` and target load at least `ceil(s/2)`.

Consequently the disjoint-defect and heavy-line alternatives never require a
separate global charging ledger. They are executable continuation certificates.

### Proof

Apply CMR124 and then CMR131. ∎

## 4. Revised remaining endpoint

The correct recursive invariant is the target load, not merely the number of
endpoint columns. The next chapter combines this invariant with the fixed
baseline and proves that both low-excess and high-excess branches contract.

The unresolved tasks after that contraction are:

1. the universal four-endpoint, one-target closure core;
2. payment for fine structures recreated by later coarse prefix repairs.

No all-`n` theorem is claimed here. The layer-pigeonhole, padding, and heavy-line
bank assertions are checked in
[`scripts/verify_prime_power_paid_geometry_conversion.py`](../scripts/verify_prime_power_paid_geometry_conversion.py).
