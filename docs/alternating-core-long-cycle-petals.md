# Fixed-cross long-cycle petals and second-hub concentration

**Branch:** `research/alternating-core-chain`

AC3ia leaves one exact structural recurrence: many state changes with the same
layer, removed cell, two inserted cross cells and finite role label, where the
symmetric-difference component is an alternating cycle of length at least six.
This note removes the fixed three-edge cross from every such cycle. The remainder
is a simple path between two fixed bipartite vertices. A maximal path packing
then gives either many petals disjoint outside the cross or one additional
row/column hub lying on many episodes.

When the petals are legal alternatives from one common parent state and the
removed cell carries private payment, they form an exact one-state-per-petal
bank. Without a common parent, the theorem remains a historical structural
router and does not combine alternative states.

## Fixed-cross long components

Fix one layer and one AC3ia long signature

\[
\sigma=(e,r,c,\lambda),
\]

where

\[
e=(u,v),\qquad r=(u,y),\qquad c=(x,v),
\]

with `x!=u` and `y!=v`. Every represented transition changes an old permutation
`M` to a new permutation `M'`, removes `e`, inserts `r,c`, and has a
symmetric-difference cycle `Gamma` of length at least six containing those three
edges.

Regard rows and columns as the two vertex classes of the matching bipartite
graph. Delete the three fixed edges `e,r,c` from `Gamma`.

## AC3il -- fixed-cross interior path normal form -- PROVED

The remaining edges form one simple path

\[
P_\Gamma:y\longrightarrow x
\]

from the row vertex `y` to the column vertex `x`. Its internal vertices avoid the
four distinct vertices

\[
u,x,v,y.
\]

It has at least two and at most

\[
\boxed{2n-4}
\]

internal vertices. Conversely, adjoining the fixed edges `r,e,c` to the path
recovers the complete alternating-cycle support.

### Proof

The cycle visits the fixed consecutive segment

\[
y\mathrel{-}r\mathrel{-}u\mathrel{-}e\mathrel{-}v\mathrel{-}c\mathrel{-}x.
\]

Deleting those three edges breaks the simple cycle into the complementary simple
path from `y` to `x`. Simplicity prevents its internal vertices from using
`u,v,x,y`. A long component has length at least six, so the complementary path
has at least three edges and therefore at least two internal vertices. The
bipartite board has `2n` row/column vertices, four of which are excluded, giving
the upper bound. QED.

## AC3im -- path petals or a second hub -- PROVED

Let `t` distinct long-cycle episodes have the same fixed cross signature. For
every integer `p>=2`, one of the following holds.

1. **Path-petal family:** there are `p` episodes whose interior paths are pairwise
   internally vertex-disjoint.
2. **Second-hub concentration:** one row or column vertex
   \[
   w\notin\{u,x,v,y\}
   \]
   belongs to at least
   \[
   \boxed{
   \frac{t}{(p-1)(2n-4)}
   }
   \]
   of the interior paths.

The first output is a fixed-cross alternating-cycle sunflower: all petals share
only the fixed cross vertices and have disjoint interior row/column resources.
The second output is a two-hub historical core carrying the original role label.

### Proof

Choose a maximal subfamily of pairwise internally vertex-disjoint paths. If it
has size at least `p`, take any `p`. Otherwise it has at most `p-1` members. The
union `W` of their internal vertices has size at most

\[
(p-1)(2n-4).
\]

Maximality implies that every observed interior path meets `W`; otherwise that
path could be added. Pigeonholing the `t` paths over `W` gives one vertex with the
displayed incidence. QED.

For `t>=2n-4`, taking

\[
p=1+\left\lceil\sqrt{t/(2n-4)}\right\rceil
\]

gives either that many disjoint petals or a second hub contained in at least

\[
\frac{t}{(2n-4)\lceil\sqrt{t/(2n-4)}\rceil}
\]

episodes.

## Common-parent boundary paths

Assume now that many long transitions are legal alternatives from one common
ordered parent state `S`, with the same fixed cross signature. In the changed
parent layer, let

\[
a=(\alpha,y)
\]

be the old matching cell in row `y`, and let

\[
b=(x,\beta)
\]

be the old matching cell in column `x`. Longness gives

\[
\alpha\ne u,x,
\qquad
\beta\ne v,y.
\]

The five boundary edges

\[
\{r,e,c,a,b\}
\]

are therefore common to every symmetric-difference support, with `r,e,c` on the
new/old/new cross and `a,b` on the old parent boundary.

Deleting those five edges leaves one nonempty simple path

\[
Q_\Gamma:\beta\longrightarrow\alpha.
\]

It has at most

\[
\boxed{2n-5}
\]

edges.

## AC3in -- common-parent edge petals or a repeated cell -- PROVED

Let `t` common-parent long alternatives have one fixed cross signature. For every
integer `p>=2`, one of the following holds.

1. **Edge-petal family:** `p` boundary paths `Q_Gamma` have pairwise-disjoint
   edge sets.
2. **Repeated off-boundary cell:** one physical cell outside the five fixed
   boundary edges belongs to at least
   \[
   \boxed{
   \frac{t}{(p-1)(2n-5)}
   }
   \]
   of the boundary paths.

### Proof

Choose a maximal family of pairwise edge-disjoint boundary paths. If it has at
least `p` members, take any `p`. Otherwise the union of its at most `p-1` paths
contains at most `(p-1)(2n-5)` cells. Maximality forces every observed boundary
path to meet this union. Pigeonhole over its cells. QED.

## Exact common-parent petal bank

Retain an edge-petal family of size `p` from AC3in. Let the child states be

\[
S_1,\ldots,S_p.
\]

Assume the fixed removed cell `e` belongs to one private current certificate
bucket of total weight `D`, so every child state destroys the full bucket.
Every child state shares the same five-edge boundary support. Every other changed
cell lies on one edge-disjoint boundary path.

## AC3io -- one-state-per-petal collateral ledger -- PROVED UNDER THE COMMON-PARENT PAYMENT HYPOTHESES

The uniform choice from `S_1,...,S_p` has the following exact properties.

1. Every state is a legal ordered pair of disjoint permutation layers.
2. Every state destroys certified payment `D` by removing `e`.
3. Every changed cell outside the fixed five-edge boundary occurs in at most one
   petal state.
4. Every newly created triple is either:
   - **boundary-supported**, containing no off-boundary inserted cell; or
   - **petal-specific**, containing at least one off-boundary inserted cell and
     therefore present in at most one state.

Let `F` be the total weight of the union of all boundary-supported candidate
triples over the petal states, and let `C_j` be the total weight of
petal-specific collateral in state `j`. A boundary-supported candidate has
probability at most one, while a petal-specific triple has probability exactly
`1/p` when present in its unique state. Therefore

\[
\boxed{
\mathbb E[\text{created collateral}]
\le F+\frac1p\sum_{j=1}^p C_j.
}
\]

Hence some child state improves whenever

\[
\boxed{
D>F+\frac1p\sum_j C_j.
}
\]

If every state fails, then either

\[
\boxed{F\ge D/2}
\]

or

\[
\boxed{\sum_j C_j\ge pD/2.}
\]

### Proof

Legality and destruction are the common-parent and private-payment hypotheses.
AC3in makes the off-boundary changed-cell sets pairwise disjoint. Every created
triple with an off-boundary inserted cell belongs to one petal state only. The
remaining created triples lie in the declared boundary-supported candidate
union, but petal-specific removals may suppress them in some states; bounding
their probability by one gives the displayed upper ledger. The improvement and
two-term failure split follow. QED.

The theorem is a multistate variable, not a product: exactly one petal is chosen.

## AC3ip -- fixed-cross long-cycle router -- PROVED

A recurrent AC3ia long signature of multiplicity `t` returns one of:

1. a historical path-petal family of any requested size `p` allowed by AC3im;
2. a second row/column hub meeting at least
   \[
   t/((p-1)(2n-4))
   \]
   episodes;
3. a genuine parent-state split;
4. inside one common-parent class, an edge-petal family or one repeated
   off-boundary physical cell from AC3in;
5. under the private-payment hypothesis, an executable multistate bank with the
   exact AC3io collateral ledger;
6. or an explicit outside-context or monotone-mask epoch change.

In the executable case, failure is no longer an arbitrary bank-type change: it
is boundary-supported candidate collateral at scale `D/2` or pairwise
petal-specific raw mass at scale `pD/2`.

### Proof

Apply AC3im to the historical family. Split by parent state. In a fixed parent,
apply AC3in and then AC3io when the removed cell carries private payment. If no
fixed parent supports the selected multiplicity, retain the parent split as an
explicit context output. QED.

## Interface to prime patching

The structural alternatives match the shapes on
`research/all-n-prime-patching`: a one-hub cycle-star or a two-hub
concentration. That branch additionally assumes a fixed matchable host and
designated credit on its reference endpoints. AC3ip may delegate only after
those host and credit hypotheses are verified; the present theorem does not
silently import them.

## Consequence

The fixed-cross long-cycle frontier is now narrowed to:

- an executable common-parent petal bank;
- fixed-boundary candidate collateral;
- pairwise petal-specific collateral;
- a quantified second-hub core;
- or genuine parent/context/epoch change.

The next payment target is to show that recurrent AC histories supply a
common-parent paid subfamily or that the second hub/parent change spends one of
the already finite context, carry, BDA or RI resources.

## Finite check

`scripts/verify_ac_long_cycle_petals.py` exhausts permutation pairs through side
six, extracts every fixed-cross interior path, checks its endpoints and internal
vertex bound, verifies the greedy petal/hub alternative for every observed
signature class, and checks common-parent boundary-path packing, off-boundary
cell disjointness and every AC3io expectation/failure identity.
