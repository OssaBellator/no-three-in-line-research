# Converting paid geometry into alternating banks

CMR123--CMR128 compress a globally frozen alternating closure, but CMR125
originally treated two outcomes as paid terminal branches:

1. a vertex-disjoint family of real collinear triples;
2. a heavy real line in the outside set.

Both outcomes actually contain another executable alternating bank. Thus no
cross-node no-double-charge ledger is needed for these two geometric classes.
The only nongeometric stopping alternative left by CMR125 is an excess barrier
relative to the fixed global baseline.

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

In particular, if `q>=4`, the disjoint family exposes an alternating bank of
some size between `4` and `q`; if a prescribed target size `r` satisfies

\[
\left\lceil\frac q2\right\rceil\le r\le N,
\]

then the bank may be padded to exactly `r` endpoints.

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
saturated state. Then `L` exposes an alternating endpoint bank of size exactly
`s`.

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

## 3. Closure conversion without geometric payment

Retain the global baseline `S_0` and the function

\[
\sigma(t)=
\max\{s\ge4:24(s-1)^2(3s-2)\le t\}
\]

from CMR125.

### Corollary CMR131 — PROVED

Let an endpoint bank of size `t>=2160` destroy `t` current star triples. Then at
least one of the following holds.

1. Some bank state has potential strictly below `Phi(S_0)`.
2. The parent state has excess at least `t/2` above `S_0`.
3. Some globally nonimproving bank state exposes a new alternating endpoint
   bank of size exactly `sigma(t)`.

### Proof

Apply CMR125. Its direct alternating-expansion alternative already gives a bank
of size `sigma(t)`.

If CMR125 gives `sigma(t)` vertex-disjoint triples, apply CMR129. At least
`ceil(sigma(t)/2)` of them supply chosen points in one fixed layer. Pad those
points inside that layer to exactly `sigma(t)` endpoints and apply CMR128. The
resulting bank destroys all selected disjoint triples.

If CMR125 gives a line with more than `2sigma(t)` outside points, CMR130 gives a
bank of size exactly `sigma(t)`.

Thus the three geometric alternatives of CMR125 all produce the same next-bank
outcome. ∎

### Corollary CMR132 — PROVED

Along every alternating-closure branch which

- never improves the fixed baseline, and
- never crosses the half-star excess barrier,

the bank sizes satisfy

\[
t_{j+1}=\sigma(t_j)
<
\left(\frac{t_j}{12}\right)^{1/3}
\]

whenever `t_j>=2160`. Hence the branch reaches a bank below `2160` after
`O(log log t_0)` expansions, without invoking any disjoint-triple or heavy-line
charging ledger.

### Proof

CMR131 leaves only the next-bank alternative on such a branch. The contraction
estimate is CMR126. ∎

## 4. Revised remaining endpoint

The repeated-charge task is now narrower than stated after CMR127.

The following no longer require global accounting:

- vertex-disjoint replacement-touching defects;
- heavy outside lines.

Both are executable expansion certificates. The unresolved alternating problem
is reduced to:

1. control or bypass the **half-star excess barrier** relative to the fixed
   baseline;
2. eliminate or classify the absolute endpoint-bank core below `2160`;
3. pay for fine structures recreated by later coarse prefix repairs.

No all-`n` theorem is claimed here. The layer-pigeonhole, padding, and heavy-line
bank assertions are checked in
[`scripts/verify_prime_power_paid_geometry_conversion.py`](../scripts/verify_prime_power_paid_geometry_conversion.py).
