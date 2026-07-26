# Reflection coupling between destruction and repair swap words

**Branch:** `research/sparse-algebraic-spread`

SAS5j partitions the constraints affected by a fixed cross-label column swap into
six singleton and six double-scope words on each side.  The destruction and
repair alphabets are not independent.  Reflection of the column coordinate
about the midpoint of the swapped columns sends every destruction word to one
canonical repair word and preserves the required row-label vector.

This gives an exact cross-side comparison.  Failure of the reflected repair is
caused only by the board boundary or by at most two unchanged reflected column
labels.

## Swap reflection

Fix swapped columns `x,y` with current labels `a,b`, where `a!=b`.  Define the
integer affine involution

`R(c)=x+y-c`.

It exchanges `x` and `y` and preserves collinearity because it is an affine
reflection of the column coordinate.

Define the mirror map from destruction words to repair words by

- `m(X_i)=Y_i`;
- `m(Y_i)=X_i`;
- `m(XY_ij)=XY_ji`.

The same formulas define the inverse map.

## SAS5z -- canonical reflected word involution -- PROVED

Let `Q` be a geometric destruction record in one word `w`.  Keep all three row
positions and their required row-block labels, and apply `R` to every scope
column.  The resulting rational record `Q*` is collinear and lies in the repair
word `m(w)`.

The operation is an involution: `(Q*)*=Q`.

### Proof

For three cells `(r_i,c_i)`, collinearity is the vanishing of

`(r_j-r_i)(c_k-c_i)-(r_k-r_i)(c_j-c_i)`.

Replacing every column by `x+y-c` multiplies both column differences by `-1`,
so the determinant remains zero.  Reflection exchanges the occurrences of
`x,y`; hence `X_i` becomes `Y_i`, `Y_i` becomes `X_i`, and `XY_ij` becomes
`XY_ji`.  Required labels are attached to row positions and are unchanged.
Finally `R(R(c))=c`. QED.

For a double-scope word, if the destruction third column is `z`, the mirror
repair third column is exactly

`z*=x+y-z`.

Thus integrality of one address is equivalent to integrality of the other.

## SAS5aa -- exact reflected repair criterion -- PROVED

Assume `Q` is a destruction constraint satisfied by the current balanced
colouring.  Its reflected record `Q*` is a valid repair constraint for the same
swap if and only if:

1. every reflected non-swapped column lies in the board range; and
2. every reflected non-swapped column currently carries the required label of
   its row position.

There is one unchanged label test for a double-scope word and two for a
singleton word.  Distinctness creates no additional obstruction.

### Proof

After the swap, `y` carries label `a` and `x` carries label `b`.  These are
exactly the required swapped labels in the mirror repair word.  All other
columns are unchanged by the swap, so the mirror constraint is repaired
exactly when their current labels equal their required row labels.

Reflection is injective, exchanges `x,y`, and preserves inequality.  Therefore
distinct original scope columns reflect to distinct columns, and a non-swapped
column distinct from `x,y` reflects to one distinct from `y,x`.  Only board
range and the unchanged labels remain. QED.

## SAS5ab -- weighted mirror-repair or defect localization -- PROVED

Let a weighted family of destruction constraints lie in one fixed word `w` for
one fixed swap, with total weight `W`.  Reflect every record and classify it by
the first applicable outcome:

1. the mirror record is board-valid and repaired by the swap;
2. at least one reflected non-swapped column is outside the board;
3. the mirror is board-valid but the least non-swapped position has the wrong
   current label.

For a double-scope word there are at most three classes, so one class carries
weight at least `W/3`.  For a singleton word there are at most four classes, so
one class carries weight at least `W/4`.

In the first class, the destruction and repair records are paired by an exact
involution.  In every other class, failure is localized to one boundary role or
one exact reflected-label role.

### Proof

SAS5aa makes the listed classes exhaustive.  There is one possible label-defect
position for a double-scope word and two for a singleton word.  Canonically
choose the least failing position when both singleton labels fail.  The classes
partition the weighted family, so weighted pigeonhole gives the bounds. QED.

This theorem does not claim that the reflected repair class is always the heavy
class.  It replaces arbitrary cross-side failure by one of at most three or
four explicit roles.

## SAS5ac -- reflection reverses primitive parameter increments -- PROVED

Inside one exact double-scope progression, suppose consecutive destruction
parameters have third columns `z(s),z(s+1)` with increment `D_0`.  Their mirror
repair columns satisfy

`z*(s+1)-z*(s)=-D_0`.

Inside one singleton dilation, reflection sends the primitive increment
`(A_0,B_0)` to `(-A_0,-B_0)`.

Therefore every disjoint adjacent-parameter family from SAS5w reflects to a
family with the same parameter adjacency and one common opposite arithmetic
increment, subject only to the SAS5aa boundary and label tests.

### Proof

Use `R(c)=x+y-c` coordinatewise and subtract consecutive reflected values. QED.

## SAS5ad -- corrected destruction/repair comparison frontier -- PROVED

For any concentrated destruction word supplied by SAS5l, the corresponding
mirror repair geometry is now completely classified:

- exact repair mass;
- one reflected-board boundary role;
- one of at most two reflected-label defect roles.

Combined with SAS5u--SAS5y, a diffuse destruction family of bounded primitive
shape either has many mirror repairs or concentrates on one reflected boundary
or label-defect profile.  Common-increment adjacent pairs remain common-step
after reflection, with opposite orientation.

The unresolved SAS6 work is consequently narrower:

1. compare the selected repair word with the canonical mirror repair word;
2. exploit a heavy reflected-label defect as a balanced-colour discrepancy;
3. install compatible pairs when the mirror-repair class is heavy;
4. control collateral across several physical swaps.

### Proof

Apply SAS5ab to the exhaustive word types and SAS5ac to every adjacent family.
QED.

## Finite check

`scripts/verify_sparse_swap_reflection.py` exhausts small row triples, swapped
columns, word positions and board-valid scope columns.  It checks determinant
preservation, the word involution, double-scope complementary columns,
distinctness, exact reflected repair tests and increment reversal.