# Balanced binary routing for marker controllers

`docs/489` realizes a rational marker policy by one cyclic word per state.  A
large action alphabet can require a long flat period and gives no structural
explanation of transient imbalance.  This chapter factors each policy through a
binary routing tree.  Every internal counter is a two-action mechanical word,
so deterministic execution has a depth-controlled discrepancy certificate.

Let a marker state have rational action probabilities `p_a`.  Choose a rooted
binary tree whose leaves are the actions.  At an internal node `v`, let
`alpha_v` be the conditional mass of its left subtree.  On the `n`th visit to
`v`, route left when

```text
floor(n alpha_v)-floor((n-1) alpha_v)=1
```

and route right otherwise.

## 1. Exact deterministic realization

### Theorem PP3chp -- PROVED / BALANCED BINARY ROUTING

For every rational policy and every binary leaf tree, the mechanical routers
produce a deterministic finite-state schedule whose long-run action frequencies
are exactly the prescribed probabilities.  If all internal conditional masses
are rational, the complete router state is periodic.

#### Proof

At node `v`, the number of left routings in its first `n` visits is exactly
`floor(n alpha_v)`, hence differs from `n alpha_v` by less than one.  Inducting
down the tree shows that every leaf receives its product conditional frequency.
Rational conditional masses make every internal floor-increment word periodic;
the product of the finitely many counter phases is finite. ∎

## 2. Prefix discrepancy under arbitrary interleavings

### Theorem PP3chq -- PROVED / DEPTH DISCREPANCY BOUND

Let leaf `a` have depth `d_a`.  After `N` visits to its marker state, if `N_a`
is the number of executions of action `a`, then

```text
|N_a-N p_a| <= d_a.
```

For several marker states encountered in an arbitrary interleaving, any linear
observable `f_(u,a)` therefore has global discrepancy at most

```text
sum_(u,a) |f_(u,a)| d_(u,a).
```

#### Proof

At one router the child-count error is less than one.  If the parent-count error
is `e`, multiplying by the child conditional probability contributes at most
`|e|`, and the child router adds less than one more.  Induction along a root--leaf
path gives the depth bound.  Summing signed leaf errors and applying the triangle
inequality gives the interleaved observable bound; no assumption on the order of
state visits is used. ∎

## 3. Finite routing-tree synthesis

### Theorem PP3chr -- PROVED / EXACT TREE-SELECTION ORACLE

For a finite action set, all labeled full binary routing trees can be enumerated.
Evaluating their leaf depths gives an exact finite oracle for minimizing any
rational discrepancy objective such as

```text
max_a w_a d_a    or    sum_a w_a d_a.
```

A stored tree, its rational conditional masses, and one period of every internal
mechanical word form a complete realization certificate.

#### Proof

There are finitely many labeled full binary trees on a fixed leaf set.  The
conditional masses are rational sums and ratios of the given rational policy.
The objective and all counter periods are therefore exactly computable.  Direct
comparison selects an optimum, and replaying the counters verifies the stored
certificate. ∎

## 4. Stored exact fixture

The audit `scripts/check_balanced_binary_marker_schedules.py` uses policy

```text
(1/2,1/3,1/6).
```

The root isolates the first action with mass `1/2`; the second router splits the
remaining mass in ratio `2/3:1/3`.  The six-step period is

```text
C,A,B,A,B,A.
```

Its exact leaf prefix discrepancies are `1/2,2/3,5/6`.  The script also checks
all `31^2=961` occurrence-count pairs for two arbitrarily interleaved marker
states and verifies the global observable certificate.

## 5. Prime-patching consequence

A rational boundary controller can now be implemented by small binary counters
rather than a flat randomized choice or a long unstructured word.  The same
certificate controls every transient prefix, including asynchronous visits to
different boundary states.
