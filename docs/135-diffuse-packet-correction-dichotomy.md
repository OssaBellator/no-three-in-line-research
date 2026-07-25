# Diffuse packet defects: correction matching or clean star

PX223--PX224 isolate the diffuse packet regime: every anchor-product level has
sublinear old selected load, but many levels may remain. Counting packet
levels is not the right invariant. Each selected packet defect has a unique
correcting transposition of two current matching rows, independent of which
anchor certifies it.

Aggregating defects by this correcting transposition produces a weighted graph
on the current endpoint labels. A low-degree correction graph has a large
weight matching and hence many commuting defect corrections. A high-degree
vertex is exactly a selected point incident with many anchor--partner triples;
bounded line occupancy converts that concentration into a clean-star child.

## 1. The packet correction graph

Let `M` be the current selected matching on row labels `[h]`. Write

\[
P_r=(x_r,y_{M(r)}).
\]

For a background anchor `z=(a,b)`, a selected pair `P_r,P_s` is a packet defect
when it is collinear with `z`. Equivalently,

\[
(x_r-a)(y_{M(s)}-b)
=
(x_s-a)(y_{M(r)}-b).
\]

The two crossed candidate cells

\[
r\to M(s),
\qquad
s\to M(r)
\]

therefore lie in one common anchor-product packet. Swapping the two current
columns of rows `r,s` moves the selected pair to those packet cells.

For each unordered row pair `e={r,s}`, let `w_e` be the number of background
anchors certifying `P_r,P_s` as an old packet defect. Let `G_corr` be the simple
graph whose edges are the pairs with `w_e>0`.

### Theorem PX300 -- PROVED

The old anchor-weighted packet defect mass is exactly

\[
\boxed{
D_{\rm pkt}(M)=\sum_{e\in E(G_{\rm corr})}w_e.
}
\]

Every defect counted by `w_{rs}` has the same unique correcting transposition:
swap `M(r)` and `M(s)`.

### Proof

Collinearity gives the displayed cross-product identity, so the two swapped
cells belong to one product packet for the certifying anchor. Conversely the
packet cross identity is exactly the collinearity determinant. The row pair
`{r,s}` determines the column swap uniquely. Summing over anchors and row
pairs gives the identity. \(\square\)

Different anchors may give different packet levels, but they contribute to the
same correction edge whenever they certify the same selected row pair.

## 2. Disjoint correction transpositions

### Theorem PX301 -- PROVED

Let `Q` be any matching in `G_corr`. The transpositions associated with the
edges of `Q` are pairwise row- and column-disjoint, commute, and define a valid
partial rematching. Before counting newly created collateral, this move
destroys exactly

\[
\boxed{
D(Q)=\sum_{e\in Q}w_e
}
\]

old anchor-weighted packet defects carried by the selected correction edges.

### Proof

Edges of `Q` have disjoint row endpoints. Since `M` is a matching, their
current target columns are also disjoint. The corresponding swaps therefore
commute and preserve injectivity. For an edge `{r,s}`, every one of its `w_e`
certificates uses the old selected cells `P_r,P_s`; the swap removes both old
cells and replaces them by the packet arcs. Distinct correction edges use
disjoint old selected cells, so the destroyed certificate sets are disjoint.
\(\square\)

This is an exact old-destruction statement. Rank-at-most-three creation by the
completion of the partial rematching remains governed by PX201--PX234.

## 3. Low correction degree gives a heavy matching

Let `rho` be the maximum unweighted degree of `G_corr`.

### Theorem PX302 -- PROVED

There is a correction matching `Q` satisfying

\[
\boxed{
D(Q)\ge\frac{D_{\rm pkt}(M)}{\max(1,2\rho-1)}.
}
\]

### Proof

Greedily edge-colour the simple graph `G_corr`. When an edge is coloured, at
most `2rho-2` colours are blocked by previously coloured adjacent edges, so
`2rho-1` colours suffice. Every colour class is a matching. The total edge
weight over all colour classes is `D_pkt(M)`, so one class carries at least the
displayed fraction. \(\square\)

No packet-count bound appears: all anchor-product levels sharing one correcting
transposition are paid simultaneously by its edge weight.

## 4. High correction degree is clean-star geometry

Assume every line contains at most `K+1` points of the set consisting of the
selected points and background anchors, where the extra one allows the chosen
centre.

For a row `r`, define its weighted correction degree

\[
\mu(r)=\sum_{s:\{r,s\}\in E(G_{\rm corr})}w_{rs}.
\]

### Theorem PX303 -- PROVED

The selected point `P_r` centres an endpoint-disjoint clean star with at least

\[
\boxed{
\frac{\mu(r)}K
}
\]

rays, each ray consisting of one background anchor and one distinct selected
partner point.

### Proof

Partition all defects incident with `r` by their line through `P_r`. On one
such line let `a` be the number of certifying anchors and `b` the number of
selected partner points. Every anchor--partner pair on the line gives one
certificate, so the line contributes `ab` to `mu(r)`. Since `a+b<=K`, a
matching between anchors and partners has size

\[
\min(a,b)=\frac{ab}{\max(a,b)}\ge\frac{ab}{K}.
\]

Choose such a matching independently on every line through `P_r`. Distinct
lines share only the centre, so their anchor and partner endpoints are
disjoint. Summing gives at least `mu(r)/K` rays. \(\square\)

This is the selected-defect analogue of the candidate-cell star extraction in
PX228.

## 5. Exact diffuse-packet dichotomy

### Corollary PX304 -- PROVED

For every integer threshold `R>=1`, one of the following holds.

1. **Clean-star child.** Some selected point centres an endpoint-disjoint clean
   star of order at least

   \[
   \boxed{R/K.}
   \]

2. **Disjoint correction bank.** There is a commuting matching of correcting
   transpositions which destroys at least

   \[
   \boxed{
   \frac{D_{\rm pkt}(M)}{2R-1}
   }
   \]

   old anchor-weighted packet defects.

### Proof

If `rho>=R`, a vertex with at least `R` distinct correction neighbours has
weighted degree at least `R`, so PX303 gives the first outcome. If `rho<R`,
PX302 gives

\[
D(Q)\ge D_{\rm pkt}(M)/(2\rho-1)>D_{\rm pkt}(M)/(2R-1).
\]

\(\square\)

PX304 supplies the missing geometric conversion for diffuse packet mass:
packet dispersion is either executable as many disjoint corrections or becomes
a clean-star child. The remaining numerical question is to compare the exact
destruction `D(Q)` with the rank-at-most-three collateral ledger of the
completion bank.

## 6. Verification

Run

```bash
python scripts/verify_product_packet_correction_dichotomy.py
```

The verifier checks the collinearity/product identity on constructed integer
instances, validates simultaneous disjoint transpositions, greedily
edge-colours random weighted correction graphs, and exhausts the line-group
inequality underlying the star extraction.
