# Cross-copy Hall conflict packing

`docs/646` gives the exact good-centre count `3t-e` for `t` source-star motifs
and `e` additional corruptions, but leaves cross-copy interference unquantified.
This chapter inserts one explicit collision graph between otherwise good centres
and derives the sharp worst-case motif threshold from its maximum degree.

## PP3czs — Cross-copy collision-graph extraction

Let `H` be the graph on the surviving good centres. Join two centres when they
cannot simultaneously enter the Hall pool because of a cross-copy geometric
conflict. If `H` has maximum degree at most `Delta`, then among `3t-e`
surviving good centres there is a conflict-free set of size at least

```text
ceil((3t-e)/(Delta+1)).
```

#### Proof

Greedily choose a vertex and discard its closed neighbourhood. Each choice
removes at most `Delta+1` vertices. Equivalently, every graph of maximum degree
`Delta` has an independent set of size at least `ceil(n/(Delta+1))`. ∎

## PP3czt — Exact motif threshold for twenty-eight Hall resources

The degree-bounded interface guarantees twenty-eight conflict-free good centres
exactly when

```text
3t - e >= 27(Delta+1) + 1.
```

Thus the least sufficient motif count is

```text
ceil((27(Delta+1)+1+e)/3).
```

With no extra corruptions, the thresholds for `Delta=0,1,...,6` are

```text
10, 19, 28, 37, 46, 55, 64.
```

The `Delta=0` case recovers `docs/646`.

## PP3czu — Sharpness of the degree-only interface

The threshold in `PP3czt` cannot be improved using only the maximum-degree
hypothesis. For every `n <= 27(Delta+1)`, partition the `n` vertices into at
most twenty-seven cliques, each of size at most `Delta+1`. The resulting graph
has maximum degree at most `Delta` and independence number at most twenty-seven.

Therefore any better Hall threshold must use source-specific geometry beyond a
cross-copy maximum-degree bound.

## Verification

`scripts/check_hall_cross_copy_conflict_packing.py` checks the exact integer
thresholds, the corruption special cases, and the clique sharpness models.

## Remaining Hall obligation

The conditional host must still construct the motif family, prove an actual
bound on `Delta`, and verify that the separate source and host-defect restriction
families have degree at most two after the conflict-free centre selection.
