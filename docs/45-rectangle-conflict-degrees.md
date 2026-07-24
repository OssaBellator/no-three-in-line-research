# Conflict degrees in the rectangle perfect-matching model

PX43--PX44 reduce arbitrary-map PX28 selection to a perfect matching in the
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

### Theorem PX45 -- PROVED

For every orientation and every candidate rectangle edge `e`, at most

\[
\boxed{16n(n-1)^2}
\]

compatible candidate edges `f` form a two-edge diagonal conflict with `e`.

### Proof

A two-rectangle bad triple has two opposite corners from one rectangle and one
corner from the other by PX44.

Fix one of the two diagonals of `e` and one of the four corner types of `f`.
The diagonal line meets that corner's scalar block in at most `n` grid points.
Each point fixes the two coordinates of `f` used by the corner, while the other
two coordinates have at most `(n-1)^2` compatible choices.  Summing over two
diagonals and four corner types gives

\[
8n(n-1)^2.
\]

Reverse the roles.  Fix one of four corners of `e` and one of two diagonal types
of `f`.  Choose one endpoint of that diagonal in at most `(n-1)^2` compatible
ways.  Its line with the fixed corner meets the opposite endpoint block in at
most `n` points.  This contributes another

\[
8n(n-1)^2.
\]

Every pair conflict is counted in at least one direction. \(\square\)

## 2. Three-edge transversal codegree

### Theorem PX46 -- PROVED

Fix two compatible candidate rectangle edges `e,f`.  At most

\[
\boxed{64n(n-2)^2}
\]

candidate edges `g`, compatible with both, form a transversal conflict with
`e,f`.

### Proof

Choose one of four corners of `e`, one of four corners of `f`, and one of four
corner types of `g`.  The first two corners determine a line.  It meets the
chosen scalar block of `g` in at most `n` points, each fixing two coordinates of
`g`.  The other two coordinates avoid the values already used by `e,f`, leaving
at most `(n-2)^2` choices.  There are `4*4*4=64` corner choices. \(\square\)

## 3. Consequences for a random perfect matching

Choose three independent uniform permutations `p,t,r`.  This is the uniform
perfect matching measure on `K_n` with the `U` part fixed pointwise.

### Corollary PX45a -- PROVED

The expected number of two-edge diagonal conflicts is at most

\[
\boxed{\frac{8n^2}{n-1}}
\qquad(n\ge2).
\]

### Proof

There are at most

\[
\frac12 n^4\cdot16n(n-1)^2
=
8n^5(n-1)^2
\]

unordered pair conflicts.  A fixed compatible pair appears with probability

\[
\frac1{n^3(n-1)^3}.
\]

Multiply. \(\square\)

### Corollary PX46a -- PROVED

For `n>=3`, the expected number of three-edge transversal conflicts is at most

\[
\boxed{
\frac{32}{3}\frac{n^2(n-1)}{n-2}
}.
\]

### Proof

There are at most

\[
\frac12n^4(n-1)^4
\]

compatible unordered edge pairs.  For each pair, PX46 supplies at most
`64n(n-2)^2` third edges.  Every unordered conflict triple is counted by its
three edge pairs, so their total number is at most

\[
\frac{64}{6}n^5(n-1)^4(n-2)^2.
\]

A fixed compatible triple appears with probability

\[
\frac1{n^3(n-1)^3(n-2)^3}.
\]

Multiply. \(\square\)

The diagonal contribution is only linear in `n`, but the transversal
contribution is quadratic.  A direct first-moment random-perfect-matching
argument therefore cannot establish an infinite closure theorem.  A successful
probabilistic route must exploit resampling, cancellation, stronger geometric
sparsity, or structured templates.

## 4. Exact small checks

The complete rectangle instances through base four have observed maxima:

| `n` | orientation | maximum pair degree | maximum transversal codegree |
|---:|---|---:|---:|
| 2 | all | 1 | 0 |
| 3 | all | 16 | 1 |
| 4 | `cc` | 71 | 16 |
| 4 | `cf` | 69 | 16 |
| 4 | `fc` | 69 | 16 |
| 4 | `ff` | 67 | 16 |

These are far below the universal bounds.  Obtaining asymptotically smaller
typical or admissible-layer degrees is now a precise bottleneck.

## Verification

Run

```bash
python scripts/verify_product_rectangle_conflicts.py
```

The script exhausts all candidate edges and compatible edge pairs through base
four, computes the exact observed maxima, and checks PX45--PX46.
