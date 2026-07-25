# All-n route A: prime-size patching

**Branch:** `research/all-n-prime-patching`

This track assumes saturated no-three configurations are eventually available at
prime-minus-one sides and asks for an exact row-column-preserving patch from side
`m` to side `m+t`. The patch must add `2t` net points, leave exactly two points
in every old and new row and column, and create no collinear triple.

The active theorem ledger is
[`proofs/prime-patching-recent-index.md`](../proofs/prime-patching-recent-index.md).

## PP1 — Degree interface

### Status: PROVED

Boundary and arbitrary-reservoir degree states are classified. Matching-edge
deletions and movement/refill insertions restore exact old and new row/column
margins.

## PP2 — Selection interfaces

### Status: PROVED AS IMPLICATIONS

The branch contains clone-space local lemmas, deletion-aware expectations,
finite-state CSPs, 2-SAT/CNF endpoints, weighted local lemmas, and spread
perfect-matching selection. The unresolved work is geometric preparation.

## PP3 — Robust seed preparation

### Status: OPEN, reduced to structured concentration conversion

## 1. Slab-optimal architecture

```text
macro count M = m^(1/20+o(1)),
pool size   R = m^(19/20+o(1)),
macro width W = m^(19/40+o(1)),
total width T = MW = m^(21/40+o(1)).
```

This balance is optimal among disjoint source-pool architectures with local width
`O(sqrt(R))`. Balanced label maps restore saturation, and product-space local
lemmas give internally no-three macros with fixed-rank spread.

## 2. Controller-aware safety and external closure

Unselected matching-pool edges remain in the source. Controller-aware candidate
states are tested against the full active source.

At the slab-optimal exponents, every remaining patch-only cross-macro class and
every ordinary two-slot source-anchor class has `o(1)` incident probability mass.
Any saturation-compatible controller-aware allocation completes an
`Omega(m^0.525)` patch.

## 3. Dynamic excess shadow

Every candidate has one automatic controller-containing axis blocker. The
pairing-invariant potential

\[
\Xi(S)=\sum_z(b_S(z)-1)
\]

counts additional nonaxis blockers. Pool-compatible endpoint trades satisfy an
exact insertion-cost-minus-removal-credit identity, and uniform improvement
terminates automatically.

## 4. Four allocation interfaces

The controller-defect scores provide four independent completion mechanisms:

1. one-sided movement ownership versus cumulative refill slack;
2. deterministic two-sided ownership with `r+s<=W`;
3. random two-sided local Ore allocation;
4. random one-sided average-refill complementary degree.

At threshold `r`, balanced movement ownership exists exactly when

\[
W|N_M(X)|\ge|X|
\]

for every movement-label set `X`. Failure gives a capacitated Hall set and an
all-bad label-by-macro rectangle.

The total same-slot anchor mass is `m^(2+o(1))`, so anchor-driven ownership
failure is a sublinear exceptional label cluster or a nearly dead macro column,
not a middle-density rectangle.

## 5. Source-valid resource endpoint

Adaptive thinning gives a growing endpoint bank with:

- no unary-invalid arc;
- no anchored transition;
- vanishing high-support source-invalid expectation;
- a fully source-valid derangement with one-cell probability `(1+o(1))/q`.

Source admissibility is closed in the sparse-unary endpoint branch.

## 6. Hall and original binary-shadow endpoints

After deleting designated recapture and residual unary-shadow cells, failure of
the source-safe endpoint host is exactly a Hall rectangle

\[
|X|+|Y|>q,
\qquad
X\times Y\subseteq E(\overline{G_0}).
\]

Binary shadow is governed by endpoint-resource congestion. The fractional cover
problem has factor-two rounding, an exact LP dual packing, and Hall inheritance.
The remaining original binary-shadow objects are a linear-congestion dual
packing or a high-overlap witness-line pencil.

## 7. Rectangle extraction

A recapture-dominated Hall core survives adaptive source-valid thinning. Failed
owner-line improvement gives a positive-density family of target-rich repeated
nonaxis lines. Pairing their owner/replacement and Hall-target traces gives
`Omega(q^3)` alternating rectangle candidates, and a four-resource matching
extracts `Omega(q)` pairwise row/column-disjoint blocks.

Rectangle extraction is closed.

## 8. Superregular installation and paid selection

For a small linear rectangle bank in a superregular endpoint host:

- the residual host has a perfect matching;
- the matching may be chosen source-valid and low-cost;
- each rectangle is an equal-margin finite-state permutation block;
- all remaining no-three conditions are exact rank-at-most-three bad boxes;
- exact insertion shadow is a unary/binary finite-state cost.

First-moment, local-lemma, and support-cleaning criteria close diffuse geometry
and paid collateral.

## 9. Cross-block signature bypass

The original line and cross diagonals are not a terminal state space. Pair two
resource-disjoint rectangles and use only cells in the two cross resource
blocks. This gives four matching states and bypasses every witness supported
solely on the original rectangle states.

The same construction applies to larger blocks. Direct recapture alone removes
fewer edges than are necessary to destroy every perfect matching. Signed and
multistate contradictions at any bounded level may therefore be bypassed by a
larger cross state space.

## 10. Unary-independent growing blocks

Let the rectangle bank have size `H`, and let the non-designated unary endpoint
graph have maximum degree `d=o(H)`.

Join two rectangles when a unary-forbidden cell lies in either cross resource
block. This rectangle-interaction graph has maximum degree at most `4d`.
Properly colour it and split each independent colour class into growing groups
of size `b`, chosen with `(d+1)b=o(H)`. Only `o(H)` rectangles are discarded.

Inside one group there are no non-designated unary edges between different
rectangles. Split the group into two halves and use cross matchings. Direct
recapture removes at most `b/2` cells from each directional `K_(b,b)`, which
remains matchable.

Deleting `o(b)` recapture-heavy rectangles leaves two near-complete superregular
directional hosts. Their product matching law satisfies

\[
\Pr(F\subseteq M)=O(b^{-r})
\]

for every prescribed fixed-rank matching `F`, and the block retains
`(1-o(1))b` designated credits.

Thus every sublinear unary-degree case reduces to the explicit paid condition

\[
K^2\frac{P_b}{b^2}
+
K^3\frac{Q_b}{b^3}
+
\frac1{R_b}
\left(
K\frac{A_b}{b}
+
K^2\frac{B_b}{b^2}
\right)
<1.
\]

Arbitrary binary signatures, dense finite-state CSPs, bounded local
contradictions, and irregular infinite-depth hierarchies are no longer separate
obstructions under sublinear unary degree.

## 11. Current exact bottleneck

The missing conversion theorem is reduced to:

1. convert an ownership Hall/slack core, two-sided threshold gap, or score
   concentration surviving all four allocation interfaces;
2. convert a Hall rectangle or matchable but non-superregular zero-unary host
   outside the superregular recapture branch;
3. convert a unary endpoint resource with linear forbidden cross-block degree;
4. convert source or shadow weights concentrated in the growing-block paid
   expression above;
5. convert a linear-congestion original binary-shadow dual packing or
   witness-line pencil;
6. construct source-admissible pool-compatible trades with `Xi` insertion cost
   below star/resource removal credit.

A successful conversion either gives the global allocation directly or strictly
decreases a nonnegative integer potential.

The branch does not prove the no-three-in-line conjecture.

## PP4 — Prime-gap transfer

### Status: PROVED UNDER PP2--PP3

A fixed positive constant times `m^0.525` patch width covers the published
backward prime-gap scale, with standard constant and rounding slack.

## PP5 — Finite exceptions

### Status: VERIFIER COMPLETE; STORED CERTIFICATES CHECKED FOR `2<=n<=10`

The eventual threshold and finite exception list depend on the missing PP3
conversion theorem.
