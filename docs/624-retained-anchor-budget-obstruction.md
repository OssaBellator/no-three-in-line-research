# Retained-anchor budget obstruction

`docs/618` gives two synthetic anchors for every maximal unary run.  To identify
those anchors with retained source cells, one must supply two distinct source
cells per run while respecting global row and column resources.  This chapter
computes the exact demand distribution at the selected profile.

The profile has encoded size thirty, nine binary nodes, eleven unary nodes, and
nineteen non-unary nodes.

## 1. Exact maximal-run distribution

### Theorem PP3cwm -- PROVED / MAXIMAL UNARY-RUN HISTOGRAM

Across the `168212023980` ordered trees, the number of maximal unary runs has
histogram

```text
1:92378,
2:8314020,
3:212007510,
4:2261413440,
5:11872420560,
6:33242777568,
7:51447155760,
8:44097562080,
9:20211382620,
10:4491418360,
11:367479684.
```

The aggregate number of runs is `1212286655580`, with mean `209/29`.

#### Proof

The dynamic program records size, binary-node count, whether the root is unary,
and the number of maximal unary runs.  Adding a unary root creates a new run
exactly when the child root is not unary; adding a binary root sums the two child
run counts.  Exact integer recurrence gives the displayed histogram. ∎

## 2. One-cell-one-anchor impossibility

### Theorem PP3cwn -- PROVED / RETAINED NON-UNARY ANCHOR BUDGET FAILURE

If every anchor must be a distinct retained non-unary source cell, then
`4858898044` trees cannot receive two anchors per run.  Their exact proportion is
`289/10005`.

#### Proof

There are nineteen non-unary nodes.  Trees with ten or eleven maximal unary runs
need twenty or twenty-two anchors, respectively.  Summing the last two histogram
classes gives

```text
4491418360 + 367479684 = 4858898044.
```

Dividing by the family size reduces to `289/10005`. ∎

## 3. Aggregate anchor demand

### Theorem PP3cwo -- PROVED / EXACT ANCHOR REMOVAL CREDIT REQUIREMENT

Two anchors per run require aggregate anchor demand

```text
2424573311160
```

and mean demand `418/29` per tree.  Any construction that inserts and later
removes those retained anchors must account for exactly the same source-cell
removal credit, unless anchors are shared or recycled.

#### Proof

Double the aggregate run count and its mean. ∎

## Consequence

The synthetic-anchor model cannot be identified uniformly with the nineteen
non-unary cells under a one-cell-one-anchor rule.  A valid source realization
must share anchors, recycle them across runs, use an external retained reservoir,
or replace the two-anchor support model.
