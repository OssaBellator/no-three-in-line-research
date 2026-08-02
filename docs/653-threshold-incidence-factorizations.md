# Threshold incidence factorizations

The previous threshold chapter found forty-nine perfect matchings between the eight
nearest targets and the eight transient source-unit cells.  This chapter classifies
complete balanced decompositions of the 3-regular incidence graph.

## PP3czv — Three-batch factorization

The twenty-four target-buffer incidences decompose into three pairwise edge-disjoint
perfect matchings in exactly forty-four unordered ways.

Equivalently, there are 132 edge-disjoint pairs of perfect matchings.  In a
3-regular bipartite graph the complement of such a pair is the unique third
perfect matching, so every pair belongs to one factorization.

## PP3czw — Exact exposure balance

Within each factorization:

- every one of the twenty-four incidences appears exactly once;
- every target appears once in each of the three batches;
- every target uses each of its three possible transient cells exactly once;
- every transient cell is used once in each batch.

Thus transient reuse can be balanced not merely inside one eight-target batch but
across a complete three-batch cycle.

The forty-nine perfect matchings participate in respectively one, two, four, or
eight factorizations with multiplicity histogram

```text
1:10, 2:21, 4:16, 8:2.
```

## PP3czx — Ordered schedule count

Ordering the three perfect matchings gives

```text
44*3! = 264
```

batch orders.  Every one of the twenty-four incidences supports two native swap
orders, so the complete catalogue contains

```text
264*2^24 = 4,429,185,024
```

fully ordered three-batch swap schedules.

The exact checker is `scripts/check_threshold_incidence_factorizations.py`.

## Evidence boundary

This result balances matrix-level buffer exposure.  It does not make any native
intermediate geometrically legal and does not supply an exposed-state-safe source
operation.
