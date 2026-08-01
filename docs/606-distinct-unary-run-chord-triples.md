# Distinct unary-run chord triples

`docs/600` obtained a nonzero ancestry statistic by allowing unary nodes in the
same chain to reuse one interval chord.  Coincident cells are not legal geometric
objects.  Here the coincident copies are separated into distinct integer points
while retaining an exact ancestry-sensitive collinearity count.

## 1. Run-specific perturbation

Index the maximal unary runs of one encoded tree.  For a run of length `k`, place
its `k` unary nodes at distinct integer points on one run-specific vertical line,
in ancestry order.  Different runs receive different vertical lines.

The statistic counts only triples internal to one maximal run.  Cross-run
incidences, if any in a chosen global placement, are deliberately not credited.

### Theorem PP3cuk — PROVED / DISTINCT LOCAL GEOMETRY

A maximal unary run of length `k` supplies exactly

```text
C(k,3)
```

guaranteed collinear triples of distinct points.  Extending a top run from length
`k` to `k+1` adds `C(k,2)` new triples.

### Theorem PP3cul — PROVED / EXACT PROFILE AGGREGATE

At encoded size thirty with nine binary nodes, the family size is

```text
168212023980.
```

The aggregate number of guaranteed within-run collinear triples is

```text
396499770810,
```

and the exact mean is

```text
33/14.
```

#### Proof

The dynamic program tracks encoded size, binary count, and the length of the
root unary run.  Unary extension applies the increment `C(k,2)`.  Binary
composition multiplies child counts and adds their internal totals. ∎

### Theorem PP3cum — PROVED / REMAINING TYPE GAP

The construction removes coincident cells and gives a genuine nonzero
collinearity statistic on distinct integer points.  Its vertical lines are
encoding coordinates, not source-derived prime-patching support chords, and the
audit does not charge cross-run incidences.

The prefix ledger row therefore remains unpromoted.

## Exact audit

```bash
python scripts/check_prefix_distinct_run_chord_triples.py
```
