# Routing dense line blockers to anchor stars or endpoint-disjoint secants

**Branch:** `research/geometric-cleaning`

GC1d bounds the partner loss caused by a declared family of exact non-axis lines,
but a large line inventory is itself geometric structure.  For one target, every
line-blocked partner has one prospective cross-cell and one surviving current pair
on the dangerous line.  Canonical witness selection first retains half the mass
on one cross-cell role.  In that role the partner, inserted cell and dangerous
line are all injectively related.  The current-pair graph then gives a high anchor
star or an endpoint-disjoint secant matching.

The secant certificates in this note are current and physical, but not
automatically paid.  Their conversion to destroyed syndrome incidence remains the
paid-bank branch of GC2 or the alternating-core interface.

## Exact line-blocker witnesses

Fix one target

\[
b=(r_b,c_b)
\]

and partner pool `P`.  For `u=(r_u,c_u)` write

\[
x_u=(r_b,c_u),
\qquad
y_u=(r_u,c_b).
\]

Let `I_line(b) subseteq P` be a line-blocked partner set.  Require every
`u in I_line(b)` to have at least one exact witness

\[
(\rho,L,e),
\]

where:

- `rho in {x,y}` is the cross-cell role;
- the selected cross-cell `rho_u` lies on the non-axis line `L`;
- `e={a,c}` is an unordered pair of distinct current cells which survive the
  assignment `(b,u)`;
- `a,c,rho_u` are collinear on `L`;
- the pair and line are retained in the complete individual-admissibility record.

Choose the lexicographically least witness for each partner.  Give the partner a
nonnegative weight `w(u)` and put

\[
W=\sum_{u\in I_{\rm line}(b)}w(u).
\]

## GC2c -- one cross-cell role retains half the blocker weight -- PROVED

One role `rho in {x,y}` has canonical witness class

\[
I_\rho
=\{u:\text{the canonical witness of }u\text{ uses role }\rho\}
\]

with

\[
\boxed{
\sum_{u\in I_\rho}w(u)\ge W/2.
}
\]

Inside one fixed role:

1. distinct partners have distinct prospective cross-cells;
2. distinct partners have distinct witness lines;
3. distinct partners have distinct current witness pairs.

### Proof

The two role classes partition the line-blocked partners, so one retains at least
half the weight.  In the `x` role, the cross-cell is `(r_b,c_u)` and partner
columns are distinct in a permutation layer; in the `y` role, partner rows are
distinct.  Thus cross-cells are distinct.  One non-axis line meets the fixed row
`r_b` or fixed column `c_b` in at most one point, so it cannot witness two
distinct cross-cells in the same role.  Finally, two distinct current points
determine one line, so distinct witness lines have distinct witness pairs. QED.

The survival condition is essential.  A pair using the removed target or partner
is not a current secant witness for the child candidate state.

## Current-pair graph

For the retained role class, form a simple graph `H` whose vertices are current
cells and whose edge for partner `u` is its witness pair `e_u`.  Give edge `e_u`
weight `w(u)`.  GC2c makes the partner-to-edge map injective.

## GC2d -- unweighted anchor-star or endpoint-disjoint matching -- PROVED

Let `M=|E(H)|` and fix an integer `Delta>=1`.  Then one of:

1. some current cell is incident with more than `Delta` witness edges;
2. `H` contains a matching of size at least
   
   \[
   \boxed{
   \frac{M}{2\Delta-1}.
   }
   \]

The matching is an endpoint-disjoint family of current secant pairs with distinct
prospective cross-cells and distinct dangerous lines.

### Proof

If the first alternative fails, the maximum degree of `H` is at most `Delta`.
The line graph of `H` then has maximum degree at most `2Delta-2`: an edge conflicts
with at most `Delta-1` other edges at each endpoint.  A graph of maximum degree
`D` has an independent set of size at least its vertex count divided by `D+1`,
for example by greedy coloring with `D+1` colors.  An independent set in the line
graph is a matching in `H`, giving the displayed bound. QED.

## GC2e -- weighted endpoint-disjoint retention -- PROVED

If the maximum degree of `H` is at most `Delta`, then `H` contains a matching
`M_*` with

\[
\boxed{
\sum_{e_u\in M_*}w(u)
\ge
\frac{\sum_{u\in I_\rho}w(u)}{2\Delta-1}
\ge
\frac{W}{2(2\Delta-1)}.
}
\]

### Proof

Greedily color the line graph with at most `2Delta-1` colors.  Each color class is
a matching, and the color classes partition the total retained edge weight.  One
class carries at least the average weight.  Apply GC2c for the second inequality.
QED.

No assumption of equal certificate weights is used.

## GC2f -- dense line-blocker router -- PROVED

For every weighted line-blocked partner family and every `Delta>=1`, canonical
witness selection returns one of:

1. a current anchor incident with more than `Delta` distinct dangerous secants in
   one fixed cross-cell role;
2. an endpoint-disjoint current secant family carrying at least
   
   \[
   \boxed{
   W/[2(2\Delta-1)]
   }
   \]
   
   of the original line-blocker weight.

In the second outcome all selected partners, prospective cross-cells, dangerous
lines and current witness pairs are distinct.

### Proof

Use GC2c to select the role-pure graph `H`.  If its maximum degree exceeds
`Delta`, return the incident anchor star.  Otherwise apply GC2e.  Injectivity and
endpoint disjointness are part of GC2c and the matching definition. QED.

## Interface with GC1 and GC2

Suppose GC1e fails because `2|L_b|` or the actual line-blocked partner mass is
large.  Applying GC2f to the actual blocked partners gives a narrow alternative:

- **anchor concentration:** one current cell supports many exact dangerous
  secants through distinct prospective cells on one target row or column;
- **endpoint-disjoint bank:** many current pairs are disjoint and have distinct
  prospective cells, partners and lines.

The anchor alternative enters GC4b/GC4c or the alternating-core anchor router.
The matching alternative has exactly the topology required by GC2's paid
endpoint-disjoint secant-bank outcome.  What remains is to attach current destroyed
syndrome weight or to prove that a large latent family forces a structured core.

A large raw line list with no actual blocked partner weight is irrelevant and
should not be promoted to this router.

## Finite check

`scripts/verify_geometric_line_blocker_router.py` exhausts small permutation
layers and fixed-role line witnesses, checking partner/cross-cell/line
injectivity.  It also exhausts simple graphs through six vertices with small
integer edge weights, verifying the star-or-matching and weighted
`1/(2Delta-1)` bounds.
