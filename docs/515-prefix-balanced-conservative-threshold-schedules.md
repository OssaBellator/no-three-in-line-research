# Prefix-balanced conservative threshold schedules

`docs/509` rounds a rational source-by-action matrix while preserving every row
sum and every global action total. The rounded matrix specifies a full-period
schedule but does not by itself control transient prefixes. This chapter adds a
deterministic low-discrepancy ordering without changing either margin.

Let `n_(i,j)` be a nonnegative integer matrix whose row sums are all `M`. Row
`i` prescribes how often source `i` uses action `j` during one period.

## 1. Binary-router ordering

### Theorem PP3cjx -- PROVED / ROWWISE PREFIX-BALANCED REALIZATION

Choose for each row a binary tree whose leaves are its actions. At every internal
node, route arrivals by the mechanical word for the rational split determined by
the total leaf counts below its two children. Then:

1. the period has length `M`;
2. action `j` appears exactly `n_(i,j)` times in row `i`; and
3. at every prefix `t`, each leaf count differs from `t n_(i,j)/M` by at most the
   depth of that leaf.

#### Proof

At a node receiving `T` arrivals, the mechanical binary word sends exactly the
prescribed child totals and has binary prefix discrepancy below one. A leaf
count is obtained by composing the routers along its root-to-leaf path, so its
error is bounded by the sum of the node errors, at most the path depth. Exact
child totals inductively give the exact leaf totals after `M` arrivals. ∎

## 2. Global action and load discrepancy

### Theorem PP3cjy -- PROVED / CONSERVATIVE PREFIX LOAD BOUND

Let `d_i` be the maximum router depth in row `i`. For every action `j`, the
global prefix-count discrepancy is at most

```text
sum_i d_i.
```

More generally, if one use of action `(i,j)` contributes a nonnegative target
load `a_(i,j,y)`, then the absolute prefix load error at target `y` is at most

```text
sum_(i,j) d_i a_(i,j,y).
```

The complete-period row and column totals remain exactly those of the rounded
matrix from `PP3cjf`.

#### Proof

Sum the rowwise signed count errors and apply the triangle inequality. Weighting
each error by its nonnegative target contribution gives the second bound. The
ordering permutes fixed row multisets and therefore changes no full-period
margin. ∎

## 3. Stored exact fixture

### Theorem PP3cjz -- PROVED / THREE-SOURCE PREFIX AUDIT

The audit `scripts/check_prefix_balanced_threshold_schedules.py` orders the
conservative matrix

```text
2 1 1 0
1 2 0 1
1 0 2 1
```

into the row words

```text
CBAA,
DBBA,
DCCA.
```

The row totals are `(4,4,4)`, the global action totals are `(4,3,3,2)`, the
attained row-action prefix discrepancy is one, and the attained global action
prefix discrepancy is two. Every prefix and every full-period margin is checked
exactly.

## 4. Prime-patching consequence

A fractional direct-clean layer can now be rounded, margin-conserved, and
executed online with a uniform transient load certificate. No random ordering or
post-hoc averaging is required.
