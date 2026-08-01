# Parabola retained-source anchor model

`docs/618` uses two synthetic anchors on each unary-run support line.  This
chapter replaces those anchors by cells of one explicit no-three-in-line source.
The model is still finite and is not the saturated source required by prime
patching.

## 1. Explicit retained source

### Theorem PP3cwm -- PROVED / PARABOLA SOURCE ANCHORS

For every ordered composition of eleven unary nodes into maximal runs, assign run
`i` the two source cells

```text
(20i,(20i)^2), (20i+1,(20i+1)^2).
```

The complete anchor set is no-three-in-line.  On the secant through each pair,
one can choose the required number of further integer cells so that all anchor
and insertion rows and columns are globally distinct and every collinear triple
is contained in one run line.

#### Proof

A line meets the integer parabola `y=x^2` in at most two points, so the anchors
are no-three-in-line.  Each secant has primitive integer direction
`(1,40i+1)` and therefore infinitely many integer cells.  At each greedy step,
only finitely many cells are excluded by used rows, used columns, or lines through
two previously placed cells not belonging to the same run.  Choose the first
remaining positive multiple.  ∎

## 2. Complete finite audit

### Theorem PP3cwn -- PROVED / DISTINCT-RESOURCE SOURCE-ANCHOR CENSUS

All `2^10=1024` ordered compositions of eleven are audited.  The canonical greedy
construction:

- uses pairwise distinct rows and columns for every source and insertion cell;
- has zero cross-run collinear triples;
- has maximum coordinate magnitude `40802`; and
- gives every inserted unary cell exactly the intended anchor-pair blocker.

#### Proof

Direct exact determinant tests over all triples certify the claims.  ∎

## 3. Removal-credit count

### Theorem PP3cwo -- PROVED / MAXIMAL-RUN CREDIT AGGREGATE

In the encoded-size-thirty, nine-binary-node profile, the family size is

```text
168212023980.
```

The aggregate number of maximal unary runs is

```text
1212286655580,
```

with mean `209/29`.  Deleting either anchor of a run destroys every anchor-pair
blocker on that run line.  Thus one source deletion per maximal run is sufficient
in this model, and the displayed aggregate is its exact deletion-credit count.

#### Proof

Use a two-state tree recurrence recording whether the root is unary.  Adding a
unary root starts a new run exactly when the child root is not unary; adding a
binary root sums the run counts of its children.  Evaluation at size thirty and
nine binary nodes gives the stated values.  ∎

The remaining gap is source identification: the parabola is explicit and
no-three-in-line, but it is not the two-per-row/two-per-column saturated retained
source of the prime-patching construction.
