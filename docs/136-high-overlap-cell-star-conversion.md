# High endpoint overlap converts to a selected-cell secant star

PX299--PX302 close the strict-sign-or-child interface whenever realized new
certificates have bounded endpoint overlap.  This chapter resolves the
complementary case.  In a selected matching, one endpoint label occurs in at
most two selected cells.  Therefore high certificate overlap at one label
forces high triple degree at one fixed selected point.  A line-by-line matching
argument converts that degree into a loaded line or an endpoint-disjoint secant
star.

## 1. One endpoint label touches two selected cells

Let `M` be a perfect matching on endpoint labels `[s]`.  Write its selected cells
as

\[
e_i=(x_i,y_{M(i)}).
\]

For a label `a`, the only selected cells whose endpoint-index support contains
`a` are

\[
e_a
\qquad\text{and}\qquad
e_{M^{-1}(a)}.
\]

They may coincide.

### Theorem PX303 -- PROVED

Let `mathcal C` be any family of realized rank-at-most-three certificates in the
selected state `M`.  If one endpoint label `a` belongs to `L` certificate
supports, then one selected cell incident with `a` belongs to at least

\[
\boxed{L/2}
\]

of the actual collinear triples represented by `mathcal C`.

### Proof

Every certificate whose endpoint support contains `a` contains at least one
selected cell using source label `a` or target label `a`.  The perfect matching
has exactly one selected source-`a` cell and exactly one selected target-`a`
cell.  Assign every certificate to one such contained cell.  One of the two
cells receives at least half of the assignments. \(\square\)

This statement is independent of the rank/support sector.

## 2. Triple degree at one selected point

Fix a selected point `f`.  Let `mathcal T_f` be any family of actual collinear
triples containing `f`, and put

\[
\mu_f=|\mathcal T_f|.
\]

For every line `ell` through `f`, form a graph `G_ell` on the other selected
points of `ell`; an edge `{p,q}` belongs to `G_ell` when `{f,p,q}` is in
`mathcal T_f`.

### Theorem PX304 -- PROVED

Fix `K>=2`.  At least one of the following holds.

1. **Loaded line.**  A line through `f` contains more than `K` selected points
   other than `f`.
2. **Endpoint-disjoint star.**  The family `mathcal T_f` contains an
   endpoint-disjoint secant star centred at `f` of order at least

   \[
   \boxed{\mu_f/(2K)}.
   \]

### Proof

Assume the loaded-line outcome fails.  Every graph `G_ell` has maximum degree
at most `K-1`.  A greedy matching in a graph of maximum degree `D` has size at
least `|E|/(2D-1)`, hence at least `|E(G_ell)|/(2K)`.

Choose such a matching independently on every line through `f`.  Distinct lines
through `f` have no other point in common, so the union of these matchings is an
endpoint-disjoint family of pairs.  Its size is at least

\[
\sum_{\ell\ni f}\frac{|E(G_\ell)|}{2K}
=
\frac{\mu_f}{2K}.
\]

Every chosen pair forms a collinear triple with the common centre `f`. \(\square\)

Unlike PX228, the two ray endpoints may be moved cells or background points;
only actual selected-point disjointness is used.

## 3. High endpoint overlap is executable geometry

### Corollary PX305 -- PROVED

If a realized certificate family has endpoint overlap `Lambda`, then either:

1. some selected line contains more than `K+1` points; or
2. there is an endpoint-disjoint secant star of order at least

\[
\boxed{\Lambda/(4K)}.
\]

### Proof

Choose an endpoint label of degree `Lambda`.  PX303 gives a selected point `f`
contained in at least `Lambda/2` certificates.  Apply PX304. \(\square\)

The star is a standard child of the alternating neutralization decoder: keep
`f` fixed and use AN2 to choose movable ray endpoints in one layer-channel
type.  A loaded line is paid by the cubic destruction bound PX242--PX244.

## 4. Complete strict-sign-or-child theorem for realized collateral

Let `m_0` be the minimum child order at which a quantitative matching bank is
used; smaller children go directly to the exact terminal optimizer.  Suppose
the selected universe has at most `Q` channels.

### Theorem PX306 -- PROVED

Fix a line threshold `K>=2` and set

\[
\boxed{B=4Km_0.}
\]

Every decoder transition which destroys at least one unresolved certificate and
creates only rank-at-most-three collateral has one of the following outcomes.

1. **Immediate strict sign.**  Fewer new certificates are realized than old
   unresolved certificates destroyed.
2. **Bounded-overlap child conversion.**  PX302 schedules enough excess
   certificates into at most

   \[
   \boxed{2Q(6B-5)}
   \]

   typed endpoint-disjoint child blocks, with historical degree cost at most
   `B`, while strictly decreasing the current unresolved coordinate.
3. **Loaded-line improvement.**  A selected line has more than `K+1` points and
   PX242--PX244 supplies superlinear destruction.
4. **Clean-star child.**  There is an endpoint-disjoint secant star of order at
   least `m_0`; AN2--AN4 and the causal ledger make it a deeper designated child.

Consequently the strict-sign-or-child interface of PX280 holds for all realized
rank-at-most-three collateral.  Its only quantitative costs are the fixed
constants `B`, `K`, `Q`, and the exact treatment of subthreshold children.

### Proof

Apply PX302 with threshold `B`.  The immediate and bounded-overlap cases give
outcomes 1 and 2.  In the high-overlap case, `Lambda>B`.  PX305 gives either a
loaded line or a star of order

\[
\frac{\Lambda}{4K}
>
\frac{B}{4K}
=m_0.
\]

These are outcomes 3 and 4.  Subthreshold typed blocks are finite terminal
instances by PX273--PX276. \(\square\)

This closes the diffuse clean-star/radial/mixed collateral frontier at the
combinatorial level.  The remaining global obligations are now the small-block
packet range, trajectory-reset descendants, and insertion of the complete
interface into the product closure theorem PX63.

## 5. Verification

Run

```bash
python scripts/verify_product_high_overlap_cell_star.py
```

The verifier enumerates small permutations and certificate families, checks the
two-cell endpoint incidence bound, verifies the line-graph matching extraction,
and tests the constants in PX305--PX306.