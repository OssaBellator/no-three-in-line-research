# Complete choice grids contain fixed-cell candidate fans

The paid two-resource theorem PP3ze--PP3zi leaves a candidate-rich projective
cover as one possible description of a hard complete choice grid. That cover
is not a separate geometry.

For one controller candidate `z`, the blocked local states form a matching
between the two choice sets. Equivalently, after choosing one blocker candidate
for each state, candidate labels give a proper edge-colouring of the compatible
state graph: no candidate repeats in one row or one column.

Consequently every row and every column of a complete choice grid already
contains a linear fan of distinct blocker candidates through one fixed endpoint
cell. If paid failure forces total candidate multiplicity at the combined-credit
scale, averaging gives one fixed cell incident with `Omega(R_* q)` distinct
candidate incidences. The complete grid therefore rejoins the endpoint-cell fan,
binary resource-star, conditional-Hall, and paid-collateral chain
PP3wv--PP3xc. A candidate-rich projective cover is no longer an independent
frontier.

## 1. Candidate classes are matchings

Retain the complete two-resource choice grid

```text
S={(a,b) in A x B: a~b}
```

from PP3xm. For every state `s=(a,b)`, let `Z(s)` be the set of distinct
controller candidate cells whose binary insertion shadow is created by selecting
`a,b`. Thus

```text
mu(s)=|Z(s)|.
```

For one candidate `z`, put

```text
S_z={s in S: z in Z(s)}.
```

### Proposition PP3afh -- PROVED

For every candidate `z`, `S_z` is a matching between `A` and `B`. In
particular, for fixed `a` the sets

```text
Z(a,b),  b in B with a~b,
```

are pairwise disjoint. The transposed statement holds for a fixed `b`.

#### Proof

The matching statement is PP3zh. If one candidate belonged to both
`Z(a,b_1)` and `Z(a,b_2)`, then `S_z` would contain two edges incident with
`a`, contradicting that statement. ∎

Thus candidate labels form a proper edge-colouring of the compatible state
graph, allowing several colours on one state when `mu(s)>1`.

## 2. Every complete-grid row is a candidate fan

For `a in A`, define

```text
B(a)={b in B: a~b}
```

and choose one candidate `z_ab in Z(a,b)` for every `b in B(a)`.

### Theorem PP3afi -- PROVED

The candidates `z_ab`, `b in B(a)`, are pairwise distinct. Hence every
`a in A` is the centre of a candidate fan

```text
{(a,b,z_ab): b in B(a)}
```

with `|B(a)|` distinct partner cells and distinct blocker candidates.

If the two fixed resources lie on the same bipartition side, then

```text
|B(a)|>=|B|-1.
```

If they lie on opposite sides after removing the common cell, then

```text
|B(a)|=|B|.
```

The transposed statements hold for every `b in B`.

#### Proof

Distinctness is Proposition PP3afh. In the same-side case, a fixed cell `a`
can be incompatible with at most the one cell of `B` using its variable opposite
resource. In the opposite-side case, PP3xn says every pair is compatible. ∎

Under the superregular degree lower bound `|A|,|B|>=delta q-O(1)`, every choice
cell therefore carries an `Omega(q)` candidate fan.

## 3. The complete grid is already a quadratic resource star

Fix the endpoint resource `v` supporting the choice set `A`. Every state
`(a,b) in S` is a binary conflict touching `v`, with centre cell `a` and partner
cell `b`.

### Corollary PP3afj -- PROVED

The complete choice grid is a binary resource star at `v` of support size

```text
h_v=|S|=Omega(q^2).
```

Every allowed centre cell `a in A` has a partner fibre of size

```text
|P(a)|=|B(a)|=Omega(q).
```

Consequently it is already in the hard quadratic-star/fixed-cell-fan branch
PP3xa, rather than a new projective-cover branch.

#### Proof

The resource-star fibre definition PP3wv gives `P(a)=B(a)` for the grid
conflicts. Apply PP3xn and Theorem PP3afi. ∎

## 4. Weighted failure gives a credit-scale fixed-cell fan

Put

```text
W_grid=sum_{s in S} mu(s)
```

as in PP3zg, and define the row candidate load

```text
W(a)=sum_{b in B(a)} mu(a,b).
```

### Theorem PP3afk -- PROVED

There is one `a in A` satisfying

```text
W(a)>=W_grid/|A|>=W_grid/q.
```

Moreover `W(a)` is exactly the number of distinct candidate cells occurring in
the row of `a`.

Hence if paid failure gives

```text
W_grid>=rho R_* |S|
```

and `|S|>=c q^2`, then one fixed endpoint cell is incident with at least

```text
rho c R_* q
```

distinct blocker candidates, while retaining `Omega(q)` distinct partner cells.

#### Proof

Average the row sums. Proposition PP3afh makes the candidate sets in a fixed
row disjoint, so their cardinalities add without repetition. Insert the two
lower bounds. ∎

The same conclusion follows from a column average.

## 5. Exact handoff

### Corollary PP3afl -- PROVED

A complete paid two-resource choice grid has one of the following forms.

1. The joint local-pair/residual-matching first moment PP3ze gives a paid
   source-valid completion.
2. Some residual host is not superregular, returning to conditional Hall or
   alternating-component analysis.
3. A fixed choice cell has an `Omega(q)` partner fan of distinct candidates,
   feeding PP3xa and PP3ks.
4. Under weighted paid failure, one fixed choice cell has
   `Omega(R_* q)` distinct candidate incidences.
5. Residual source or non-grid insertion cost is already at the credit scale.

In alternatives 3 and 4, conditioning on the fixed centre cell is exactly the
binary resource-star conditional problem PP3wv--PP3xc.

#### Proof

Combine PP3ze--PP3zg with PP3afj--PP3afk. ∎

## 6. Revised weighted-grid endpoint

### Corollary PP3afm -- PROVED

Candidate-rich projective covering is no longer an independent complete-grid
frontier. The remaining weighted-grid obstruction is:

1. paid/source concentration after fixing one fan centre;
2. a conditional Hall family;
3. an alternating residual host;
4. local multiplicity already comparable with the removal credit.

Bare candidate support, many distinct projective correspondences, and the
minimum `Omega(q)` candidate count are absorbed by the fixed-cell fan already
present in every complete grid.

## 7. Finite diagnostic

The script

```text
scripts/check_choice_grid_candidate_fans.py
```

checks that every candidate colour class is a matching, computes row and column
partner fans, verifies that candidate sets are disjoint within each row and
column, and checks the weighted row-average lower bound.
