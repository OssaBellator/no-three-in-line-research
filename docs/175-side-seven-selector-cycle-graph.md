# The side-seven selector graph and exact radius-one census

PX500 gives alternating-cycle flips as degree-preserving selector moves.  This
chapter proves that these moves connect the complete selector space, gives a
uniform diameter bound, and enumerates the first selector-changing layer around
the four PX501 centres.

## 1. Alternating-cycle connectivity

Fix one of the four-regular abstract full-selector hosts determined by a
relative permutation `H`.  A selector is a spanning subgraph of degree two at
every abstract row and column vertex.

### Theorem PX512 -- PROVED

The graph whose vertices are spanning degree-two selectors and whose edges are
simple alternating-cycle flips is connected.

More precisely, any two selectors `F,F'` can be joined by at most

\[
\boxed{14}
\]

alternating-cycle flips.

### Proof

Colour the edges of `F\setminus F'` red and the edges of `F'\setminus F` blue.
At every abstract row or column vertex, the red and blue degrees are equal,
because both `F` and `F'` have degree two there.  Therefore the balanced
red-blue graph decomposes into edge-disjoint cycles alternating red and blue.
Flipping those cycles one at a time replaces all red edges by all blue edges and
transforms `F` into `F'`.

Each selector has 28 edges, so the symmetric difference has at most 56 edges.
Every alternating cycle has length at least four.  Hence the decomposition has
at most `56/4=14` cycles. \(\square\)

The bound is uniform and deliberately crude; it does not assert that the actual
diameter is fourteen.

## 2. Exact selector populations

PX54 gives the one-cycle count

\[
A_L=2+2\cdot4^L+(4+2\sqrt3)^L+(4-2\sqrt3)^L.
\]

Counts multiply over relative-cycle components.

### Corollary PX513 -- PROVED

The four side-seven relative classes contain the following numbers of abstract
spanning degree-two selectors:

| Relative type | Selector count |
|---|---:|
| `(7)` | 1,323,522 |
| `(5,2)` | 2,269,620 |
| `(4,3)` | 1,975,428 |
| `(3,2,2)` | 4,422,600 |
| **Total** | **9,991,170** |

### Proof

Use

\[
A_2=90,
\quad
A_3=546,
\quad
A_4=3618,
\quad
A_5=25218,
\quad
A_7=1323522.
\]

Then the four counts are

\[
A_7,
\qquad
A_5A_2,
\qquad
A_4A_3,
\qquad
A_3A_2^2.
\]

Direct multiplication gives the table. \(\square\)

## 3. Exact radius-one layers around the centres

A **simple alternating-cycle neighbour** of a selector is obtained by flipping
one simple bipartite cycle whose edges alternate between selected and
unselected host edges.  Distinct resulting selectors are counted once.

### Theorem PX514 -- PROVED FINITE

The four PX501 centre selectors have the following exact radius-one profiles.

| Cycle length | `(7)` | `(5,2)` | `(4,3)` | `(3,2,2)` |
|---:|---:|---:|---:|---:|
| 4 | 32 | 36 | 36 | 42 |
| 6 | 16 | 8 | 12 | 28 |
| 8 | 12 | 32 | 16 | 30 |
| 10 | 16 | 48 | 84 | 12 |
| 12 | 8 | 96 | 32 | 0 |
| 14 | 16 | 32 | 0 | 0 |
| 16 | 128 | 32 | 0 | 0 |
| 18 | 352 | 64 | 0 | 0 |
| 20 | 384 | 16 | 0 | 0 |
| 22 | 128 | 0 | 0 | 0 |
| **Distinct neighbours** | **1,092** | **364** | **180** | **112** |

Thus the complete first selector-changing layer contains

\[
\boxed{1748}
\]

distinct class-labelled neighbours.

### Proof

For every unselected edge from a starting row, alternate through a selected
edge incident with its column and continue without repeating an abstract row or
column.  Close only at the starting row, toggle the complete cycle, and
canonicalise the resulting 14 row bitmasks.  The verifier checks degree two at
every row and column after every flip and asserts the displayed length
histograms. \(\square\)

## 4. Updated exact frontier

PX512 shows that alternating cycles are not merely local heuristics: they form a
complete move language for the selector space.  PX514 makes the first exact
layer small enough to combine with the coordinate CSP.

The immediate computational theorem target is therefore:

1. apply PX504 to all 1,748 radius-one neighbours;
2. stop with an explicit side-seven template if any coordinate orbit embeds;
3. otherwise record a certified radius-one selector obstruction and continue by
   breadth-first distance, using PX512 to guarantee completeness by distance
   fourteen.

No radius-one coordinate conclusion is claimed in this chapter.

## Verification

Run

```bash
g++ -O3 -std=c++17 scripts/verify_product_side_seven_selector_cycle_graph.cpp -o /tmp/side7_selector_cycles
/tmp/side7_selector_cycles
```

The verifier checks the transfer recurrence values, all four selector totals,
centre degrees, every simple alternating-cycle flip, and the complete radius-one
histograms.