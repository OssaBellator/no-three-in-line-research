# Source-preserving threshold three-cycle trades

The fifth-layer route is geometrically legal but requires degree-five source
margins at positive density.  We therefore return to degree four and classify
the nearest legal matrices that preserve every row and column total.

## 1. Nearest legal matrices

### Theorem PP3cvr — PROVED / EIGHT NEAREST DEGREE-FOUR REPLACEMENTS

Among all multisets of four no-three-in-line permutation layers, the minimum
entrywise `l_1` distance from the stored source matrix is six.  Exactly eight
matrices attain this distance.

#### Proof

There are eighteen legal permutations and 5,985 multisets of four.  Exact
enumeration gives the stated minimum and multiplicity. ∎

## 2. Alternating-cycle structure

### Theorem PP3cvs — PROVED / UNIT THREE-CYCLE TRADE CLASSIFICATION

Every nearest matrix is obtained from the source matrix by moving exactly three
unit cells.  The three removed cells lie in three distinct rows and columns, the
three added cells lie in the same row and column sets, and the old-to-new action
map is one directed three-cycle.

Each of the four row triples occurs exactly twice among the eight replacements.

#### Proof

Row and column totals are both four.  Distance six means three negative and three
positive unit entries.  The checker verifies that exactly three rows change, one
unit per row, and that the induced balanced action map has one orbit of length
three. ∎

## 3. Source-generation interface

### Theorem PP3cvt — PROVED UNDER A THREE-CYCLE SOURCE ACTION

Any geometric operation that realizes one of the eight listed unit alternating
three-cycle trades converts the stored degree-four source matrix into a matrix
with a four-layer legal decomposition, without a fifth slot or changed margins.

#### Proof

The trade identity gives the replacement matrix, and the enumeration stores a
legal four-layer decomposition for it. ∎

## Remaining source obligation

No repository theorem currently realizes any of these eight matrix trades as an
actual prime-patching source move.  The catalogue replaces the impossible
positive-density fifth layer by a finite source-preserving action target.
