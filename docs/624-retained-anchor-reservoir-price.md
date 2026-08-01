# Retained-anchor reservoir price for support chords

`docs/618` used two synthetic anchor cells for every maximal unary run.  This
chapter computes the exact number of retained source cells that would be needed
to replace those synthetic anchors without changing the anchored blocker count.

## 1. Unary-run distribution

### Theorem PP3cwm — PROVED / EXACT MAXIMAL-RUN HISTOGRAM

At encoded size thirty with nine binary nodes and eleven unary nodes, the family
has `168212023980` ordered unary-binary trees.  The maximal-unary-run histogram is

```text
1:92378, 2:8314020, 3:212007510, 4:2261413440,
5:11872420560, 6:33242777568, 7:51447155760,
8:44097562080, 9:20211382620, 10:4491418360,
11:367479684.
```

The aggregate number of runs is `1212286655580`, with mean `209/29`.

#### Proof

The dynamic program records size, binary-node count, whether the root is unary,
and the number of maximal unary runs.  Adding a unary root starts a run exactly
when the child root is not unary; adding a binary root sums the two child run
counts. ∎

## 2. Two-anchor reservoir

### Theorem PP3cwn — PROVED / EXACT RETAINED-SOURCE PRICE

Two retained source anchors per maximal unary run require aggregate reservoir

```text
2424573311160,
```

with mean `418/29` anchors per encoding and worst-case requirement twenty-two.

The eleven anchored blockers per encoding have aggregate
`1850332263780`, so the exact blocker-to-reserved-anchor ratio is `29/38`.

#### Proof

Multiply the run count by two and the family size by eleven.  The ratio reduces
exactly. ∎

## 3. Conditional retained-source conversion

### Theorem PP3cwo — PROVED UNDER A RETAINED-ANCHOR RESERVOIR

If each maximal unary run has two actual retained source cells on its support
line, all anchor and insertion rows and columns are distinct, and the mixed-run
triple exclusions of `docs/618` hold, then the synthetic-anchor model converts
without adding new anchor points.  The required retained-source occupancy is
exactly the quantity in `PP3cwn`.

#### Proof

Identify the two synthetic anchors of each run with the two supplied retained
cells.  The incidence and distinct-resource checks are unchanged; only the source
provenance changes. ∎

## Remaining source obligation

No current construction identifies the required retained cells or proves the
mean `418/29` and worst-case twenty-two reservoir can be reserved with the needed
row, column, and line incidences.  The anchor obligation is now exactly priced.
