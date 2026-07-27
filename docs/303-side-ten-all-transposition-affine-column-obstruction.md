# Side-ten all-transposition affine-column obstruction

PX65 shows that every successful rectangle product produces an output factor in
the all-transposition relative class. The exact side-five rectangle closure
therefore produces a side-ten factor of type

\[
(2,2,2,2,2).
\]

A recursive `10 -> 20` use of the same pathway needs a full-selector template for
this class. This chapter closes the complete affine-column subfamily while
allowing arbitrary row labeling and arbitrary degree-two selection.

## 1. Normalized search family

Use

\[
H_{2^5}=(1,0,3,2,5,4,7,6,9,8)
\]

and the affine permutation group on `Z/10Z`,

\[
A_{10}
=
\{x\mapsto ax+b\pmod {10}:
  a\in\{1,3,7,9\},\ b\in\mathbb Z/10\mathbb Z\}.
\]

It has order `40`. For each orientation and each pair

\[
(T,Q)\in A_{10}^2,
\]

use the PX61 row-pattern normal form. The first row block has fixed abstract
patterns. In the second block, assigning unused patterns to scalar rows is
exactly the arbitrary permutation `P`. For each assigned row pattern, choose any
two of its four incident columns.

Thus one exact search geometry includes:

- one affine pair `(T,Q)`;
- every `P in S_10`;
- every spanning degree-two selector;
- every real-grid collinearity constraint.

There are

\[
4\cdot40^2=\boxed{6400}
\]

column geometries.

## 2. Complete exact census

### Theorem PX970 -- PROVED FINITE

No affine-column geometry for the side-ten all-transposition relative class
contains a no-three spanning degree-two state, even when `P` and the selector are
arbitrary.

The complete deterministic node census is:

| Orientation | `(T,Q)` pairs | Search nodes | Maximum nodes in one geometry |
|---|---:|---:|---:|
| `cc` | 1,600 | 35,797,487 | 495,008 |
| `cf` | 1,600 | 23,449,947 | 183,088 |
| `fc` | 1,600 | 72,141,241 | 2,818,716 |
| `ff` | 1,600 | 34,485,733 | 361,408 |
| **Total** | **6,400** | **165,874,408** | **2,818,716** |

### Proof

For fixed `(T,Q,theta)`, process all twenty scalar rows. In the first coarse row
block the abstract pattern is fixed. In the second block choose one unused
abstract pattern, which chooses the value of `P` on that row. Then choose two of
the pattern's four incident columns.

The search tracks scalar column degrees and the selected-point bitset. It rejects
an insertion exactly when the new point forms a zero integer determinant with
two earlier selected points. A capacity bound prunes whenever the remaining
fixed rows and unused patterns cannot complete some column to degree two.

At depth twenty, every column must have degree exactly two. Exhaustion before
that depth proves infeasibility for the geometry. The affine group has exactly
forty elements, so the 1,600 pairs in each orientation exhaust `A_10^2`; pattern
assignment exhausts every `P`. The four searches therefore exhaust all 6,400
stated geometries. \(\square\)

The generalized solver independently reproduces the four published side-eight
node totals of PX66 before running the side-ten census.

## 3. Recursive consequence

### Corollary PX971 -- PROVED REDUCTION

The exact side-five rectangle output cannot be recursively doubled from side ten
to side twenty by keeping both column labelings affine and placing all
nonlinearity in the second-row permutation or the selector.

Any successful `10 -> 20` full-selector recurrence for the all-transposition
class must use at least one of:

1. a non-affine first-column labeling `T`;
2. a non-affine relative-column labeling `Q`;
3. a larger structured map group containing a useful non-affine double coset;
4. the general low-syndrome repair/resampling path rather than a fixed template.

### Proof

PX65a places every rectangle output in the all-transposition class. PX970 rules
out every affine pair `(T,Q)` while already allowing every `P` and every selector.
The listed alternatives are precisely the remaining degrees of freedom in the
PX61 normal form or a departure from fixed-template selection. \(\square\)

## 4. Reusable solver

### Theorem PX972 -- PROVED IMPLEMENTATION REDUCTION

The executable

`scripts/search_product_transposition_affine_columns.cpp`

implements the same row-pattern search for every even base `2<=n<=20`, any of
the four orientations, and any contiguous interval of affine-pair indices. A
`FOUND` line includes the complete scalar cell set; a `NONE` line reports exact
node totals for the interval.

The interval interface permits independently replayable parallel shards without
changing the search tree inside one affine geometry.

## 5. Verification

```bash
python scripts/verify_product_transposition_class_ten.py
```

The verifier compiles the generic C++ search, partitions each orientation into
sixteen exact 100-pair intervals, rejects any `FOUND` output, and asserts the
four aggregate node totals and maxima displayed above.
