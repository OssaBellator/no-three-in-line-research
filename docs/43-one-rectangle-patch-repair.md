# One-rectangle repair of near-miss patches

A matching-reservoir patch may preserve every row and column degree and have
only a small number of residual triples.  The simplest exact repair is an
alternating switch on one axis-parallel rectangle.

## 1. Alternating rectangle switches

Let `T subseteq [n]^2` have exactly two points in every row and column.  Suppose

\[
 a=(x_1,y_1),\qquad b=(x_2,y_2)
\]

are selected, with `x_1!=x_2` and `y_1!=y_2`, while the other rectangle corners

\[
 c=(x_1,y_2),\qquad d=(x_2,y_1)
\]

are unselected.  Define

\[
 T'=T\setminus\{a,b\}\cup\{c,d\}.
\]

### Proposition PP3ax -- PROVED

The switch preserves the point count and leaves exactly two selected points in
every row and column.

#### Proof

Rows `y_1,y_2` and columns `x_1,x_2` each lose one selected corner and gain one
selected corner.  Every other row and column is unchanged. ∎

## 2. Exact geometric repair criterion

Put

\[
 X=T\setminus\{a,b\}.
\]

### Theorem PP3ay -- PROVED

The switched set `T'=X union {c,d}` is no-three-in-line if and only if:

1. `X` is no-three-in-line;
2. neither `c` nor `d` lies on a secant through two points of `X`;
3. the line through `c,d` contains no point of `X`.

#### Proof

Every triple in `T'` is either wholly inside `X`, contains exactly one of
`c,d`, or contains both.  The three displayed conditions exclude those three
classes respectively.  Conversely, a failure of any condition produces the
corresponding triple. ∎

Condition 1 is equivalent to saying that every triple of the original state
`T` contains at least one of the removed corners `a,b`.  Thus one rectangle
switch can repair many old triples at once, provided they are covered by its
removed diagonal and its added diagonal has no collateral certificate.

## 3. Exhaustive width-two repair result

The script

```bash
python scripts/search_width_two_rectangle_repairs.py \
  certificates/prime-patching-small.json
```

starts from every internally clean cross-only width-two matching patch in
PP3aw, identifies every alternating rectangle switch, and checks the switched
configuration with exact integer determinants.

### Proposition PP3az -- PROVED BY EXHAUSTIVE FINITE CHECK

Among the `80,731` internally clean width-two matching-patch states generated
from the stored certificates with `4<=m<=10`, exactly three initial states admit
a one-rectangle repair.  Each has exactly one repairing switch, and the three
repaired target configurations are distinct:

| Source side | Target side | Triples before switch | Removed corners | Added corners |
|---:|---:|---:|---|---|
| 4 | 6 | 3 | `(2,6),(1,3)` | `(2,3),(1,6)` |
| 5 | 7 | 2 | `(1,2),(5,5)` | `(1,5),(5,2)` |
| 6 | 8 | 1 | `(1,2),(5,3)` | `(1,3),(5,2)` |

The repaired configurations are saturated and no-three-in-line.

For the `6 -> 8` repair, the near-miss matching patch deletes

```text
(2,4), (3,1), (4,6), (6,3)
```

and inserts

```text
(2,7), (4,7), (3,8), (6,8),
(7,1), (7,3), (8,4), (8,6).
```

Its only triple is

```text
(1,2), (2,5), (3,8).
```

The rectangle switch deletes `(1,2),(5,3)` and inserts `(1,3),(5,2)`, removing
the final blocker without creating collateral triples.

## 4. Consequence for PP3 preparation

The parabolic and general width-two searches showed that external certificates,
not internal patch geometry, are the finite obstruction.  PP3az gives a concrete
mechanism for absorbing that obstruction into the old core:

1. construct an internally clean matching patch;
2. cover the residual certificate set by the removed diagonals of a small family
   of alternating rectangles;
3. require the added diagonals to be clean against the post-removal set.

The remaining asymptotic target is therefore a **patch-plus-trade bank** rather
than a patch bank alone.  A useful preparation theorem may install protected
rectangles around high-load retained anchors or blocker endpoints and select a
small compatible set of switches after the boundary patch is chosen.
