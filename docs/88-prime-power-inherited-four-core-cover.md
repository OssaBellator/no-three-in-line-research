# Exact cylinder covers of the inherited nonroot four-core

The abstract four-board census CMR139 allows a partial second forbidden
matching from the opposite layer. A terminal core inside a nonroot closure
envelope is more rigid: the two inherited layer row sets are disjoint. Hence the
opposite layer contributes no forbidden position in the chosen endpoint board.
The normalized core is the unique four-object derangement board.

This chapter classifies every fixed-rank cylinder of that board and the complete
Pareto frontier of certificate profiles covering all its states.

## 1. The inherited board is the derangement board

### Theorem CMR181 — PROVED

Let a four-endpoint one-target core lie in one layer of a nonroot closure
envelope from CMR172--CMR175. Normalize its four selected columns and four
selected rows to `0,1,2,3`, with the old endpoint matching equal to the
identity.

Then the allowed states are exactly the nine derangements of four objects. No
opposite-layer cell lies in the board.

### Proof

The endpoint rows belong to one inherited layer row set over the nonroot
envelope. CMR173 says the other layer's row set over that envelope is disjoint.
Therefore no opposite-layer point can use one of the four endpoint rows in one
of the selected columns. The only forbidden board cell in each source row is
its old endpoint cell. An allowed rematching is exactly a derangement. There are
`D_4=9` such permutations. ∎

This is the board corresponding to the unique `9`-state entry in CMR139.

## 2. Exact cylinder sizes

A rank-`r` cylinder is the set of derangements containing one compatible
prescribed partial matching of rank `r`.

### Theorem CMR182 — PROVED BY EXHAUSTIVE FINITE CHECK

For the inherited four-core board:

1. every nonempty rank-one cylinder has size exactly `3`;
2. the nonempty rank-two cylinders consist of `12` cylinders of size `2` and
   `9` cylinders of size `1`;
3. every nonempty rank-three cylinder is a singleton, and there are `9` distinct
   singleton state cylinders.

Consequently the exact rank atom bounds are

\[
\boxed{
\alpha_1=\frac13,
\qquad
\alpha_2=\frac29,
\qquad
\alpha_3=\frac19.
}
\]

### Proof

The checker enumerates the nine derangements and every compatible rank-one,
rank-two, and rank-three prescription. ∎

### Corollary CMR183 — PROVED

Let `T_r` be the number of real-collinear candidate certificates of rank `r`
for an inherited nonroot four-core. If every allowed state creates at least one
new triple, then

\[
\boxed{
3T_1+2T_2+T_3\ge9.
}
\]

Equivalently,

\[
\frac13T_1+rac29T_2+rac19T_3\ge1.
\]

### Proof

Count incidences between allowed states and candidate certificates. Every one of
the nine states must be covered. By CMR182, one certificate covers at most
`3,2,1` states according to rank. ∎

This replaces the abstract four-board inequality from CMR140 by the exact
inherited constants.

## 3. Minimum covers

### Theorem CMR184 — PROVED BY EXHAUSTIVE FINITE CHECK

The minimum number of cylinders covering all nine inherited states is three.
Every three-cylinder cover consists of three rank-one cells.

There are exactly eight such minimum covers. They are precisely:

- the three non-diagonal cells in one fixed source row; or
- the three non-diagonal cells in one fixed target column.

Thus every minimum cover is a complete row shadow or complete column shadow of
the derangement board.

### Proof

No one cylinder covers more than three states. Exhaustive set-cover enumeration
shows that no pair covers all nine states and that exactly eight triples do.
Direct inspection gives the displayed row/column form. Conversely every
permutation uses exactly one cell in a fixed source row and exactly one cell in
a fixed target column, so each displayed triple partitions the nine states. ∎

This identifies the cheapest possible terminal obstruction: three rank-one
secant shadows concentrated in one endpoint column or one endpoint row.

## 4. Complete Pareto frontier

For a cylinder cover, let `(u_1,u_2,u_3)` count its rank-one, rank-two, and
rank-three certificates. A profile is Pareto-minimal if no other cover uses no
more certificates at every rank and fewer at some rank.

### Theorem CMR185 — PROVED BY EXHAUSTIVE FINITE CHECK

The complete Pareto-minimal profile list is

```text
(3,0,0)
(2,1,1)  (2,2,0)  (2,0,3)
(1,2,2)  (1,3,1)  (1,4,0)  (1,1,4)  (1,0,6)
(0,3,3)  (0,4,2)  (0,5,1)  (0,6,0)
(0,2,5)  (0,1,7)  (0,0,9)
```

Every certificate family covering all states componentwise dominates at least
one profile in this list.

### Proof

Dynamic programming over the `2^9` subsets of allowed states computes the
nondominated rank-count profiles. The checker independently verifies that each
listed profile is realized and that no omitted profile is minimal. ∎

## 5. Revised inherited obstruction

A frozen nonroot four-core is therefore not an arbitrary finite trap. It must
contain one of sixteen exact rank patterns. The extremal low-complexity case is
a three-cell row or column secant shadow.

The next escape theorem may be reduced accordingly:

1. convert a complete three-cell row/column shadow into an improving envelope
   parent state or a strict carry signature;
2. show that every other Pareto profile pays enough rank-two/rank-three mass to
   the already bounded joint-parent collateral;
3. or resample several disjoint inherited four-cores simultaneously so that the
   finite cover slack becomes strict.

No all-`n` theorem is claimed here. The board type, cylinder sizes, minimum
covers, and Pareto frontier are checked in
[`scripts/verify_prime_power_inherited_four_core_cover.py`](../scripts/verify_prime_power_inherited_four_core_cover.py).
