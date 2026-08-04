# Nineteenth low-frontier budget-six obstruction

`docs/681` excludes every correction through deletion budget six for the complete
minimum-four nineteenth frontier. This chapter extends the exact obstruction to
all raw attempts whose minimum transversal is five or six, using the canonical
144-point state reconstructed from the eighteenth transition.

## PP3ddt — Corrected minimum-five and minimum-six frontier census

For the same 1,032 raw nineteenth attempts, there are

```text
minimum five:  9 attempts,  54 minimum cores,
minimum six:  47 attempts, 435 minimum cores.
```

The number of minimum cores per minimum-five attempt has histogram

```text
3:3, 5:2, 6:1, 9:2, 11:1.
```

The corresponding minimum-six histogram is

```text
1:6, 3:15, 5:1, 9:15, 11:1, 15:3,
21:2, 27:1, 33:1, 39:1, 47:1.
```

Together with the six minimum-four cores in `docs/681`, this accounts for all
495 minimum cores belonging to the 58 raw attempts with transversal at most six.

## PP3ddu — No low-frontier correction through budget six

For every minimum-five core, enumerate all row-and-column-preserving replacements
at budgets five and six. For every minimum-six core, enumerate the complete
budget-six replacement layer.

No legal correction exists. The exact rejected replacement counts are

```text
minimum-five cores, budget five:       3,810,
minimum-five cores, budget six:    3,318,750,
minimum-six cores, budget six:       143,640.
```

Thus the complete minimum-five and minimum-six frontier contributes

```text
3,466,200
```

additional rejected replacements beyond the minimum-four audit in `docs/681`.
The canonical checker is
`scripts/check_boundary_nineteenth_transition.py`.

## PP3ddv — Sharp remaining boundary alternative

Every raw nineteenth attempt with minimum transversal at most six is obstructed
through deletion budget six. Hence any corrected nineteenth transition requires
budget at least seven, or a raw attempt whose minimum transversal is at least
seven.

The later correction in `docs/693` attains budget seven on the first
`P2/-64` minimum core, so the budget lower bound is sharp. The resulting finite
nineteenth transition does not itself supply a recurrence or periodic invariant.

## Evidence boundary

This is an exhaustive finite obstruction for the complete raw low-transversal
frontier of the canonical state. The stale 60-attempt/515-core census came from a
single incorrect base coordinate and is superseded by the exact 58-attempt,
495-core reconstruction above.
