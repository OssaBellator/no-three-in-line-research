# Nineteenth boundary budget-six obstruction

This chapter continues from the corrected 144-point, eighteen-block state in
`docs/675-corrected-eighteenth-boundary-transition.md`. The canonical state is
reconstructed from the eighteenth correction and contains `(42,378)`, not the
stale coordinate `(42,193)`.

## PP3ddb — Complete minimum-four nineteenth frontier

For the current 144-point state and next origin `(72,213)`, the exact raw
nineteenth spectrum has two minimum-four attempts:

```text
P1/-33: ten conflict triples and one minimum core,
P2/-64: nine conflict triples and five minimum cores.
```

The `P1/-33` core is

```text
(70,214),(74,180),(74,183),(75,181).
```

The five `P2/-64` cores are

```text
(13,77),(73,151),(75,150),(75,152),
(33,101),(73,151),(75,150),(75,152),
(36,163),(73,149),(73,151),(75,152),
(39,162),(73,149),(73,151),(75,152),
(73,149),(73,151),(75,150),(75,152).
```

## PP3ddc — No preserving correction through budget six

For all six minimum-four cores, enumerate every row-and-column-preserving
replacement at deletion budgets four, five, and six. No legal replacement exists.
For every core the exact raw permutation counts are

```text
budget 4:       24,
budget 5:   17,520,
budget 6: 7,595,640.
```

Thus the complete minimum-four budget-six layer contains

```text
6 * 7,595,640 = 45,573,840
```

rejected replacements. The five `P2/-64` cores are checked by
`scripts/check_boundary_nineteenth_corrections.cpp`; the canonical wrapper
`scripts/check_boundary_nineteenth_transition.py` reconstructs and checks the
additional `P1/-33` core before accepting the transition certificate.

## PP3ddd — Exact remaining frontier after budget six

No nineteenth correction exists with deletion budget at most six on either
minimum-four attempt. Therefore any corrected transition has budget at least
seven, or must start from an attempt whose minimum transversal is at least five.

The later canonical repair in `docs/693` attains budget seven, so this lower bound
is sharp. This chapter alone remains a finite obstruction and does not establish a
recurrence or all-length construction.

## Evidence boundary

This is a finite exact obstruction for the complete minimum-four frontier through
budget six. Its coordinate correction is independently reconstructed by
`scripts/check_boundary_nineteenth_transition.py`.
