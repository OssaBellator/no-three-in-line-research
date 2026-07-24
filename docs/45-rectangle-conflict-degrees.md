# Conflict degrees in the rectangle perfect-matching model

PX41--PX42 reduce arbitrary-map PX28 selection to a perfect matching in the
complete four-partite four-uniform hypergraph

\[
\mathcal K_n=U\times P\times T\times R
\]

with explicit two-edge diagonal conflicts and three-edge transversal conflicts.
This chapter gives uniform conflict-degree bounds and quantifies the failure of
a naive random perfect matching.

## 1. Two-edge diagonal-conflict degree

Call two hyperedges **compatible** when they are disjoint in all four vertex
parts, so they can belong to one perfect matching.

### Theorem PX43 -- PROVED

For every orientation and every candidate rectangle edge `e`, at most

\[
\boxed{
16n(n-1)^2
}
\]

compatible candidate edges `f` form a two-edge diagonal conflict with `e`.

### Proof

A two-rectangle bad triple has exactly two opposite corners from one rectangle
and one corner from the other by PX42.

First fix one of the two diagonals of `e` and one of the four corner types of
`f`.  The diagonal line meets the scalar block of that corner type in at most
`n` grid points: the block has `n` possible scalar rows, and a line meets each
row at most once unless horizontal, in which case it still contains only the
`n` block points in that row.  Each point fixes the two coordinates of `f` used
by that corner.  The other two coordinates have at most `(n-1)^2` compatible
choices.  Summing over two diagonals and four corner types gives

\[
8n(n-1)^2.
\]

Now reverse the roles.  Fix one of the four corners of `e` and one of the two
diagonal types of `f`.  Choose the endpoint of that diagonal in one scalar
block, in at most `(n-1)^2` compatible ways.  The line through this endpoint
and the fixed corner of `e` meets the opposite endpoint block in at most `n`
points.  Thus this direction contributes another

\[
8n(n-1)^2.
\]

Every two-edge conflict is counted in at least one of these directions, proving
the bound. \(\square\)

## 2. Three-edge transversal codegree

### Theorem PX44 -- PROVED

Fix two compatible candidate rectangle edges `e,f`.  At most

\[
\boxed{
64n(n-2)^2
}
\]

candidate edges `g`, compatible with both, form a transversal conflict with
`e,f`.

### Proof

Choose one of four corners of `e` and one of four corners of `f`.  Their line is
fixed.  Choose one of the four corner types of `g`.  The line meets the
corresponding scalar block in at most `n` points, each fixing the two coordinates
of `g` used by that corner.  The other two coordinates must avoid the values
already used by both `e` and `f`, leaving at most `(n-2)^2` choices.

There are

\[
4\cdot4\cdot4=64
\]

corner-type choices, giving the displayed bound. \(\square\)

## 3. Consequences for a random perfect matching

Choose three independent uniform permutations `p,t,r`.  This is the uniform
perfect matching measure on `K_n` with the `U` part fixed pointwise.

### Corollary PX44a -- PROVED

The expected number of two-edge diagonal conflicts is at most

\[
\boxed{
\frac{8n^2}{n-1}
}
\qquad(n\ge2).
\]

### Proof

There are at most

\[
\frac12 n^4\cdot16n(n-1)^2
=
8n^5(n-1)^2
\]

unordered pair conflicts.  A fixed compatible pair appears in the random
matching with probability

\[
\frac1{n^3(n-1)^3}.
\]

Multiply. \(\square\)

### Corollary PX44b -- PROVED

For `n>=3`, the expected number of three-edge transversal conflicts is at most

\[
\boxed{
\frac{32}{3}
\frac{n^2(n-1)}{n-2}
}.
\]

### Proof

There are at most

\[
\frac12n^4(n-1)^4
\]

compatible unordered edge pairs.  For each pair, PX44 supplies at most
`64n(n-2)^2` third edges.  Every unordered triple is counted once for each of
its three edge pairs, so the total number of transversal conflict triples is at
most

\[
\frac{64}{6}
 n^5(n-1)^4(n-2)^2.
\]

A fixed compatible triple appears with probability

\[
\frac1{n^3(n-1)^3(n-2)^3}.
\]

Multiply. \(\square\)

The pair contribution is only linear in `n`, but the transversal contribution
is quadratic.  Therefore a direct first-moment random-perfect-matching argument
cannot by itself establish an infinite closure theorem.  Any probabilistic
route must exploit resampling, cancellation, geometric sparsity stronger than
the worst-case codegree, or a structured template family.

## 4. Exact small checks

The complete rectangle instances through base four have the following observed
maximum degrees:

| `n` | orientation | maximum pair degree | maximum transversal codegree |
|---:|---|---:|---:|
| 2 | all | 1 | 0 |
| 3 | all | 16 | 1 |
| 4 | `cc` | 71 | 16 |
| 4 | `cf` | 69 | 16 |
| 4 | `fc` | 69 | 16 |
| 4 | `ff` | 67 | 16 |

These values are far below the universal bounds, showing that PX43--PX44 are
safe structural estimates rather than sharp formulas.  Obtaining asymptotically
smaller typical or admissible-layer degrees is now a precise bottleneck.

## Verification

Run

```bash
python scripts/verify_product_rectangle_conflicts.py
```

The script exhausts all candidate edges and compatible edge pairs through base
four, computes the exact observed maxima, and checks PX43--PX44.
