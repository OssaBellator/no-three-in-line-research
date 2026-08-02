# Distinct-transient threshold batching

`docs/641` proves that every two-swap realization of a threshold target exposes
one transient source cell.  This chapter organizes all eight targets into
balanced batches with no transient-cell reuse.

## 1. The target--transient incidence graph

### Theorem PP3czd — PROVED / CONNECTED 3-REGULAR DESIGN

Form a bipartite graph with the eight nearest legal targets on one side and the
eight multiplicity-one source cells on the other.  Join a target to a source cell
when that cell can be its unique transient buffer.

This graph is connected and 3-regular on both sides.  It has twenty-four
target-buffer incidences.  Every incidence supports exactly two swap orders.

#### Proof

Enumerate all forty-eight two-swap factorizations and group them by target and
unique outside-support cell.  Every target has three cells, every cell serves
three targets, and each incidence occurs twice.  Connectivity follows by direct
graph traversal in `scripts/check_threshold_distinct_transient_batch.py`. ∎

## 2. Forty-nine balanced assignments

### Theorem PP3cze — PROVED / DISTINCT-BUFFER PERFECT MATCHINGS

The target--transient incidence graph has exactly forty-nine perfect matchings.
Thus all eight targets can be assigned pairwise distinct transient buffer cells
in forty-nine ways.

#### Proof

Enumerate all `8!` bijections from targets to transient cells and retain exactly
those respecting the incidence graph.  Forty-nine survive. ∎

## 3. Ordered eight-target batches

### Theorem PP3czf — PROVED / 12,544 DISTINCT-BUFFER BATCHES

Each chosen target-buffer incidence has two swap orders.  Consequently the
forty-nine perfect matchings lift to

```text
49 * 2^8 = 12,544
```

ordered eight-target batches with no transient-cell reuse.

#### Proof

The order choices are independent across the eight matched incidences. ∎

## Consequence

Matrix-level buffer congestion can be eliminated across one complete eight-
target batch.  The geometric gap remains: every individual intermediate is still
illegal, and no source construction has made the eight distinct transient cells
simultaneously safe.
