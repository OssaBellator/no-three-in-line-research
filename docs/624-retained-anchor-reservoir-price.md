# Retained-anchor reservoir and parabola source model

`docs/618` uses two anchors for every maximal unary run.  This chapter combines
the exact anchor-demand distribution, the obstruction to sourcing all anchors
from the nineteen non-unary cells, and an explicit external no-three source that
realizes the required incidences.

## 1. Exact maximal-run distribution and internal budget failure

### Theorem PP3cwm -- PROVED / MAXIMAL-RUN HISTOGRAM

At encoded size thirty with nine binary nodes and eleven unary nodes, the
`168212023980` ordered trees have maximal-unary-run histogram

```text
1:92378, 2:8314020, 3:212007510, 4:2261413440,
5:11872420560, 6:33242777568, 7:51447155760,
8:44097562080, 9:20211382620, 10:4491418360,
11:367479684.
```

The aggregate run count is `1212286655580`, with mean `209/29`.  Under a rule
requiring two distinct retained non-unary cells per run, exactly
`4858898044` trees—proportion `289/10005`—cannot be supplied by the nineteen
non-unary cells, because ten or eleven runs require twenty or twenty-two anchors.

#### Proof

A dynamic program records size, binary count, root-unary status, and maximal-run
count.  The budget failure is the sum of the ten- and eleven-run classes.  ∎

## 2. Explicit external retained source

### Theorem PP3cwn -- PROVED / PARABOLA ANCHOR REALIZATION

For every ordered composition of eleven unary nodes into runs, assign run `i`
the source cells

```text
(20i,(20i)^2), (20i+1,(20i+1)^2).
```

The complete anchor set is no-three-in-line.  The required insertion cells can
be chosen on the corresponding secants so that all source and insertion rows and
columns are globally distinct and every collinear triple is contained in one run
line.

All 1,024 ordered compositions of eleven are audited.  The canonical greedy
construction has zero cross-run triples and maximum coordinate magnitude `40802`.

#### Proof

A line meets `y=x^2` in at most two points.  Each secant has primitive integer
direction `(1,40i+1)` and infinitely many integer cells.  At each step only
finitely many cells are forbidden by used resources or mixed lines, so greedy
selection succeeds.  Exact determinant checking certifies all 1,024 cases.  ∎

## 3. Exact reservoir and removal-credit price

### Theorem PP3cwo -- PROVED / RETAINED-SOURCE PRICE

Two anchors per maximal run require aggregate reservoir

```text
2424573311160,
```

mean `418/29`, and worst-case twenty-two anchors per encoding.  The eleven
anchor-pair blockers per encoding have aggregate `1850332263780`, giving exact
blocker-to-reserved-anchor ratio `29/38`.

Deleting either anchor of a run destroys every anchor-pair blocker on that run
line.  Hence one deletion per run is sufficient after construction, with
aggregate deletion count `1212286655580` and mean `209/29`.

#### Proof

Double the aggregate run count for reservoir occupancy and multiply the family
size by eleven for blocker count.  The deletion statement follows because all
insertions on a run use the same source-anchor pair.  ∎

## Consequence

The anchor incidence and price are now explicit, and an external no-three source
realizes them.  The remaining gap is the actual PP3 source: the parabola reservoir
is not the two-per-row/two-per-column saturated retained source, while the
internal nineteen-cell reservoir fails on a positive fraction of the family.
