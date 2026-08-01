# Threshold augmentation source-margin obstruction

`docs/599` found a unique one-layer augmentation that converts the obstructed
four-slot conservative matrix into a five-slot matrix admitting only legal
no-three-in-line layers.  This chapter asks whether the existing threshold
source operations can supply that augmentation.

Let

```text
M =
(2 1 1 0)
(0 2 1 1)
(1 0 2 1)
(1 1 0 2).
```

Every row and column of `M` has degree four.

## 1. Unique legal source layer

### Theorem PP3cuh — PROVED / UNIQUE MARGIN AUGMENTATION

Among all twenty-four permutation layers, the only layer whose addition yields a
matrix decomposable into five legal no-three-in-line permutation layers is

```text
p = (3,0,1,2).
```

The augmented matrix is

```text
M+P_p =
(2 1 1 1)
(1 2 1 1)
(1 1 2 1)
(1 1 1 2).
```

Every row and column now has degree five.

### Theorem PP3cui — PROVED / EXACT FIVE-SLOT COST

The augmented matrix has exactly `120` ordered decompositions into five legal
layers.  The augmentation contributes four new source-cell units, one in every
row and column.

Relative to the augmented schedule, the new slot occupies `1/5` of the period.
Relative to the original four-slot schedule, the slot count increases by `1/4`.

#### Proof

The checker adds each of the twenty-four permutation matrices to `M`, recursively
enumerates legal five-layer decompositions, and verifies the row and column
margins.  Only `p` has nonzero count. ∎

### Theorem PP3cuj — PROVED / STORED SOURCE-MARGIN OBSTRUCTION

The stored threshold operations—reordering layers, decomposing a fixed
conservative matrix, and balancing their prefixes—preserve the degree-four row
and column margins.  They cannot create the degree-five augmented margins.

Therefore the positive five-slot geometry requires a genuinely new source event
of mass four.  No repository threshold inequality currently pays for that
event, so the direct-clean ledger row is not promoted.

## Exact audit

```bash
python scripts/check_threshold_augmentation_source_margin.py
```
