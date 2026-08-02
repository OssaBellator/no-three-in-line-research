# Orientation-three cover top support through 64 top orders

PX1000--PX1002 compress the first 128 fixed-top selector obligations of
multiplicity-two case zero into seven-triple covers. This chapter measures which
top-column labels those covers actually depend on.

For one chosen cover, let its **syntactic top support** be the set of scalar
columns occurring in its seven abstract triples. Every point coordinate used by
the cover depends only on the top labels of those columns.

## 1. Exact support-size census

### Theorem PX1007 -- PROVED FINITE

The support-size distribution across the 128 orientation-three covers is:

| Fixed top columns | Covers |
|---:|---:|
| 7 | 1 |
| 8 | 9 |
| 9 | 33 |
| 10 | 79 |
| 11 | 6 |
| **Total** | **128** |

Thus no cover needs more than 11 of the 14 top labels. Every cover leaves at
least three columns free, and ten covers leave at least six columns free.

The minimum-support obligation occurs at top order 35, selector zero. Its
seven-triple cover touches only seven top columns, with support mask `11531`.

## 2. Support-mask reuse

### Theorem PX1008 -- PROVED FINITE

Only 37 distinct support masks occur among the 128 covers. The most common mask,
`6975`, occurs 28 times. The same mask is used by both selectors at top orders
zero and seven and reappears throughout the 64-top prefix.

Consequently the support layer is more compressible than the 93-cover
vocabulary: multiple distinct seven-triple covers induce the same partial-top
assumption pattern.

## 3. Partial-top nogood consequence

### Corollary PX1009 -- PROVED REDUCTION

Fix one stored cover and retain the top labels on its syntactic support. For any
other top assignment agreeing on those supported columns, every point used by
the seven triples has the same scalar coordinates. Therefore each triple covers
exactly the same bottom permutations, and the union still covers all `5,040`
bottom permutations.

Hence every stored cover is a mechanically checkable partial-top nogood:

- the cover itself proves bottom infeasibility for its selector;
- only 7--11 top-column literals are required;
- the remaining 3--7 top columns may vary arbitrarily, subject to clean-top and
  permutation constraints.

This is the first direct bridge between bottom-cover compression and top-master
learning at multiplicity two. It is syntactic rather than deletion-minimal:
additional top literals may be removable because some determinant equalities are
independent of individual supported labels.

## 4. Next target

The next exact step is semantic deletion. For each support mask, remove literals
one at a time and recheck the seven stored triples across every clean top
extension. The resulting minimized masks can be inserted directly as
signature-level master nogoods.

This finite reduction does not advance the selector census boundary and does not
prove an infinite product theorem.

## 5. Verification

```bash
python scripts/verify_product_side_seven_multiplicity2_case0_orientation3_cover_support64.py
```

The verifier regenerates all 128 covers, checks the complete support-size
histogram, asserts 37 distinct support masks, verifies the 28-fold common mask,
and checks the minimum-support obligation and unchanged ordered digest.
