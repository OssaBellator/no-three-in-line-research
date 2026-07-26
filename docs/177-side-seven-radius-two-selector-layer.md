# Exact side-seven radius-two selector layer

PX518 proves that any successful side-seven template must have selector-cycle
distance at least two from the corresponding certified centre.  The selector
graph can therefore be explored before any coordinate search is run.

This chapter enumerates the complete distance-two layer and isolates its
smallest-support stratum.

## 1. Exact breadth-first generation

For one relative class, let `F_0` be its certified centre and let `N(F)` denote
the set of selectors obtained from `F` by one simple alternating-cycle flip.
PX514 gives

\[
L_1=N(F_0).
\]

Define

\[
L_2=
\left(\bigcup_{F\in L_1}N(F)\right)
\setminus\bigl(\{F_0\}\cup L_1\bigr).
\]

### Theorem PX519 -- PROVED FINITE

The exact distance-two selector counts are:

| Relative class | Radius one | Radius two |
|---|---:|---:|
| `(7)` | 1,092 | 947,789 |
| `(5,2)` | 364 | 26,550 |
| `(4,3)` | 180 | 10,531 |
| `(3,2,2)` | 112 | 4,433 |
| **Total** | **1,748** | **989,303** |

### Proof

Regenerate the radius-one set by the PX514 cycle enumerator.  For every parent,
enumerate all simple alternating cycles, flip them, and insert the result into a
hash set after deleting the centre and the complete radius-one set.  Equality
of selectors is equality of their fourteen row masks, so deduplication is
exact. \(\square\)

## 2. Parent-move incidence

A distance-two selector may have many radius-one parents.  Count every directed
pair

\[
(F,G),\qquad F\in L_1,\quad G\in N(F).
\]

### Theorem PX520 -- PROVED FINITE

The directed parent-neighbour counts are:

| Relative class | Directed moves from radius one |
|---|---:|
| `(7)` | 45,106,960 |
| `(5,2)` | 296,416 |
| `(4,3)` | 59,644 |
| `(3,2,2)` | 14,848 |
| **Total** | **45,477,868** |

The large difference between directed moves and distinct radius-two selectors
measures the amount of path coalescence available to a cached coordinate CSP.

## 3. Shortest-support radius-two stratum

For a selector `F`, write

\[
\delta(F)=|F\triangle F_0|.
\]

Every radius-two selector has `delta(F)>=8`: two nontrivial alternating-cycle
moves cannot produce a new state at symmetric difference four without that
state already lying in radius one.

### Theorem PX521 -- PROVED FINITE

The minimum support at radius two is exactly eight.  The number of selectors
with

\[
\delta(F)=8
\]

is:

| Relative class | Support-eight radius-two selectors |
|---|---:|
| `(7)` | 435 |
| `(5,2)` | 533 |
| `(4,3)` | 543 |
| `(3,2,2)` | 725 |
| **Total** | **2,236** |

The verifier also checks the complete symmetric-difference histogram in each
class.

### Corollary PX522 -- PROVED REDUCTION

Before testing the full set of 989,303 radius-two selectors, the exact next
coordinate target is the 2,236-selector support-eight stratum.  It is the
smallest selector change not covered by PX517 and is comparable in size to the
already completed 1,748-selector radius-one census.

Failure of this stratum would force either:

1. a radius-two selector with symmetric difference at least ten; or
2. a selector at distance at least three.

## 4. Verification

Compile and run

```bash
g++ -O3 -std=c++17 scripts/verify_product_side_seven_radius_two_selectors.cpp \
  -o /tmp/side7_radius2_selectors
/tmp/side7_radius2_selectors cycle7
/tmp/side7_radius2_selectors cycle52
/tmp/side7_radius2_selectors cycle43
/tmp/side7_radius2_selectors cycle322
```

The verifier regenerates both breadth-first layers, checks every directed move,
deduplicates exact selector masks, and verifies the complete support
histograms.
