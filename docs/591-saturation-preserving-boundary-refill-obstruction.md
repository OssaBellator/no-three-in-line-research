# Saturation-preserving boundary refill obstruction

`docs/585` found four symmetric six-block candidates that become no-three-in-line after deleting exactly three old points. Each deletion certificate damages three columns and two rows. This chapter asks the finite completion question: can the same row and column degrees be restored by putting three points back into the deficient resources?

## 1. Exact refill catalogue

### Theorem PP3csr -- PROVED / FINITE SATURATION-REFILL ENUMERATION

For each sharp three-deletion repair, exact restoration of the deleted column degrees requires one refill point in each of the three deficient columns. Exact restoration of the deleted row degrees requires the refill rows to equal the deleted row multiset.

In every repair the row multiset has one singleton row and one repeated row, so there are exactly three distinct assignments of those rows to the three deficient columns. Across the four symmetric repairs, the complete exact catalogue therefore contains

```text
4 * 3 = 12
```

refill sets.

#### Proof

The deficient columns are distinct because the deletion certificate removes one point from each of three columns. The deleted rows have multiplicities two and one. A refill preserving both degree vectors is consequently a bijection from the three columns to that row multiset, modulo the repeated row, giving `3!/2!=3` candidates per repair. ∎

## 2. No exact refill is geometrically legal

### Theorem PP3css -- PROVED / SATURATION-REFILL OBSTRUCTION

None of the twelve exact row-and-column refills preserves the no-three-in-line condition.

For every candidate, the checker stores a collinear-triple witness after reinsertion. For example, in the first repair the refill

```text
(5,-74), (16,-74), (18,-31)
```

creates the triple

```text
(5,-74), (9,-58), (12,-46).
```

#### Proof

The finite list from `PP3csr` is exhaustive. Direct determinant evaluation on every resulting point set gives a nonzero catalogue of failure witnesses and zero legal refills. ∎

## 3. Consequence for seam repair

### Theorem PP3cst -- PROVED / LOCAL REFILL IS INSUFFICIENT

A saturation-preserving completion of the sharp boundary repair cannot be confined to the five damaged row/column resources while simply restoring the deleted degree vector. Any successful mechanism must do at least one of:

1. alter a wider row or column neighbourhood;
2. replace additional old points;
3. use a new boundary block or seam-corrector geometry;
4. change the saturation invariant being preserved.

#### Proof

Every completion that restores exactly the deleted row and column degrees is one of the twelve candidates of `PP3csr`, and every such candidate is obstructed by `PP3css`. ∎

## 4. Exact audit

Run

```bash
python scripts/check_boundary_saturation_refill_obstruction.py
```

The audit reconstructs the four sharp repairs, verifies their three-point deletion certificates, enumerates all twelve exact refills, and stores a first collinearity witness for each repair class.

## 5. Prime-patching consequence

The boundary frontier now has a sharp two-stage negative result: three deletions are necessary to admit the sixth block, and exact local degree refill is impossible. The remaining problem is a genuine wider-neighbourhood replacement problem rather than a missing finite case in the current catalogue.
